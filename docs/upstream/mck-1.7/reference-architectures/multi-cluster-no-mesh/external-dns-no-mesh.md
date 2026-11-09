<!-- Converted from reference-architectures/multi-cluster-no-mesh/external-dns-no-mesh.txt (reStructuredText). Includes are inlined. -->

# Configure External DNS

This page walks you through the process of deploying and validating external DNS 
for your Kubernetes Operator components deployed across multiple Kubernetes clusters 
without a service mesh. 

## Prerequisites

Before you begin, perform the following tasks:

- Install `kubectl`.
- Update as needed and set the environment variables defined in the following  `env_variables.sh` file.

  ```bash
  # This script builds on top of the environment configured in the setup guides.
  # It depends (uses) the following env variables defined there to work correctly.
  # If you don't use the setup guide to bootstrap the environment, then define them here.
  #  ${K8S_CLUSTER_0}
  #  ${K8S_CLUSTER_1}
  #  ${K8S_CLUSTER_2}
  #  ${K8S_CLUSTER_0_ZONE}
  #  ${K8S_CLUSTER_1_ZONE}
  #  ${K8S_CLUSTER_2_ZONE}
  #  ${K8S_CLUSTER_0_CONTEXT_NAME}
  #  ${K8S_CLUSTER_1_CONTEXT_NAME}
  #  ${K8S_CLUSTER_2_CONTEXT_NAME}
  #  ${MDB_GKE_PROJECT}

  suffix_short="${K8S_CLUSTER_SUFFIX}"
  # Ensure suffix_short is no longer than 19 characters to make GKE identifiers fit under 30 characters
  if [[ -n "${suffix_short}" && ${#suffix_short} -gt 19 ]]; then
      # Calculate positions for cutting from the middle
      prefix_len=$(((19 - 1) / 2))  # -1 for the 'x' replacement
      suffix_start=$((${#suffix_short} - prefix_len))
      # Create the truncated version with 'x' in the middle
      suffix_short="${suffix_short:0:${prefix_len}}x${suffix_short:${suffix_start}}"
  fi

  export DNS_SA_NAME="ext-dns-sa${suffix_short}"
  export DNS_SA_EMAIL="${DNS_SA_NAME}@${MDB_GKE_PROJECT}.iam.gserviceaccount.com"

  export CUSTOM_DOMAIN="mongodb.custom"
  export DNS_ZONE="mongodb${suffix_short}"
  ```

## Source Code

You can find all included source code in the MongoDB Kubernetes Operator repository.

## Procedure

**Step 1: Create a GCP service account for ExternalDNS.**

```sh
gcloud iam service-accounts create "${DNS_SA_NAME}" --display-name "${DNS_SA_NAME}"
```

**Step 2: Add the DNS admin role to your GCP service account.**

```sh
gcloud projects add-iam-policy-binding "${MDB_GKE_PROJECT}" --member serviceAccount:"${DNS_SA_EMAIL}" --role roles/dns.admin
```

**Step 3: Create GCP service account key.**

```sh
mkdir -p secrets

gcloud iam service-accounts keys create secrets/external-dns-sa-key.json --iam-account="${DNS_SA_EMAIL}"
```

**Step 4: Create a Kubernetes namespace for deploying ExternalDNS.**

```sh
kubectl --context "${K8S_CLUSTER_0_CONTEXT_NAME}" create ns external-dns
kubectl --context "${K8S_CLUSTER_1_CONTEXT_NAME}" create ns external-dns
kubectl --context "${K8S_CLUSTER_2_CONTEXT_NAME}" create ns external-dns
```

**Step 5: Create a Kubernetes Secret containing the service account key.**

```sh
# create secret with service account key
kubectl --context "${K8S_CLUSTER_0_CONTEXT_NAME}" -n external-dns create secret generic external-dns-sa-secret --from-file credentials.json=secrets/external-dns-sa-key.json
kubectl --context "${K8S_CLUSTER_1_CONTEXT_NAME}" -n external-dns create secret generic external-dns-sa-secret --from-file credentials.json=secrets/external-dns-sa-key.json
kubectl --context "${K8S_CLUSTER_2_CONTEXT_NAME}" -n external-dns create secret generic external-dns-sa-secret --from-file credentials.json=secrets/external-dns-sa-key.json
```

**Step 6: Install ExternalDNS.**

ExternalDNS makes Kubernetes resources discoverable via public DNS servers. 
Deploy the `eternal-dns` Kubernetes deployment and related permissions objects 
to the namespace you just created. 

```sh
kubectl --context "${K8S_CLUSTER_0_CONTEXT_NAME}" -n external-dns apply -f yamls/externaldns.yaml
kubectl --context "${K8S_CLUSTER_1_CONTEXT_NAME}" -n external-dns apply -f yamls/externaldns.yaml
kubectl --context "${K8S_CLUSTER_2_CONTEXT_NAME}" -n external-dns apply -f yamls/externaldns.yaml
```

```yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  name: external-dns
  labels:
    app.kubernetes.io/name: external-dns
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: external-dns
  labels:
    app.kubernetes.io/name: external-dns
rules:
  - apiGroups: [""]
    resources: ["services","endpoints","pods","nodes"]
    verbs: ["get","watch","list"]
  - apiGroups: ["extensions","networking.k8s.io"]
    resources: ["ingresses"]
    verbs: ["get","watch","list"]
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: external-dns-viewer
  labels:
    app.kubernetes.io/name: external-dns
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: external-dns
subjects:
  - kind: ServiceAccount
    name: external-dns
    namespace: external-dns
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: external-dns
  labels:
    app.kubernetes.io/name: external-dns
spec:
  strategy:
    type: Recreate
  selector:
    matchLabels:
      app.kubernetes.io/name: external-dns
  template:
    metadata:
      labels:
        app.kubernetes.io/name: external-dns
    spec:
      serviceAccountName: external-dns
      containers:
        - name: external-dns
          image: registry.k8s.io/external-dns/external-dns:v0.16.1
          args:
            - --source=service
            - --source=ingress
            - --provider=google
            - --log-format=json # google cloud logs parses severity of the "text" log format incorrectly
            - --interval=10s
            - --policy=upsert-only # would prevent ExternalDNS from deleting any records, omit to enable full synchronization
            - --registry=txt
      #     # uncomment below if static credentials are used
          env:
             - name: GOOGLE_APPLICATION_CREDENTIALS
               value: /etc/secrets/service-account/credentials.json
          volumeMounts:
             - name: google-service-account
               mountPath: /etc/secrets/service-account/
      volumes:
         - name: google-service-account
           secret:
             secretName: external-dns-sa-secret
```

**Step 7: Set up the DNS zone.**

This example includes a private DNS zone. This means that you can only 
access the resources deployed in the DNS zone from the GKE clusters we 
created. If you are planning to access your resources from outside your 
GKE clusters, use a public DNS zone. To do so, you must have a 
[registered domain](https://en.wikipedia.org/wiki/Domain_name_registry).

```sh
FQ_CLUSTER_0="projects/${MDB_GKE_PROJECT}/locations/${K8S_CLUSTER_0_ZONE}/clusters/${K8S_CLUSTER_0}"
FQ_CLUSTER_1="projects/${MDB_GKE_PROJECT}/locations/${K8S_CLUSTER_1_ZONE}/clusters/${K8S_CLUSTER_1}"
FQ_CLUSTER_2="projects/${MDB_GKE_PROJECT}/locations/${K8S_CLUSTER_2_ZONE}/clusters/${K8S_CLUSTER_2}"

gcloud dns managed-zones create "${DNS_ZONE}" \
  --description="" \
  --dns-name="${CUSTOM_DOMAIN}" \
  --visibility="private" \
  --gkeclusters="${FQ_CLUSTER_0}","${FQ_CLUSTER_1}","${FQ_CLUSTER_2}"
```
