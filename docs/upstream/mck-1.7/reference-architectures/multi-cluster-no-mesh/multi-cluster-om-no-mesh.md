<!-- Converted from reference-architectures/multi-cluster-no-mesh/multi-cluster-om-no-mesh.txt (reStructuredText). Includes are inlined. -->

# Multi-Cluster Ops Manager Without a Service Mesh

The Ops Manager is responsible for facilitating workloads such as backing up 
data, monitoring database performance and more. To make your multi-cluster Ops 
Manager and the Application Database deployment resilient to entire data center 
or zone failures, deploy the Ops Manager Application and the Application 
Database on multiple Kubernetes clusters.

## Prerequisites

Before you begin the following procedure, perform the following actions:

- Install `kubectl`.
- Complete the GKE Clusters procedure or the equivalent.
- Complete the TLS Certificates procedure or the equivalent.
- Complete the ExternalDNS procedure or the equivalent.
- Complete the Deploy the MongoDB Operator procedure.
- Set the required environment variables as follows:

```bash
# This script builds on top of the environment configured in the setup guides.
# It depends (uses) the following env variables defined there to work correctly.
# If you don't use the setup guide to bootstrap the environment, then define them here.
#  ${K8S_CLUSTER_0_CONTEXT_NAME}
#  ${K8S_CLUSTER_1_CONTEXT_NAME}
#  ${K8S_CLUSTER_2_CONTEXT_NAME}
#  ${OM_NAMESPACE}
#  ${CUSTOM_DOMAIN}
#  ${DNS_ZONE}

export S3_OPLOG_BUCKET_NAME=s3-oplog-store
export S3_SNAPSHOT_BUCKET_NAME=s3-snapshot-store

# If you use your own S3 storage - set the values accordingly.
# By default we install Minio to handle S3 storage and here are set the default credentials.
export S3_ENDPOINT="minio.tenant-tiny.svc.cluster.local"
export S3_ACCESS_KEY="console"
export S3_SECRET_KEY="console123"

export OPS_MANAGER_VERSION="8.0.5"
export APPDB_VERSION="8.0.5-ent"

export OPS_MANAGER_EXTERNAL_DOMAIN="opsmanager.${CUSTOM_DOMAIN}"
export APPDB_CLUSTER_0_EXTERNAL_DOMAIN="${K8S_CLUSTER_0}.${CUSTOM_DOMAIN}"
export APPDB_CLUSTER_1_EXTERNAL_DOMAIN="${K8S_CLUSTER_1}.${CUSTOM_DOMAIN}"
export APPDB_CLUSTER_2_EXTERNAL_DOMAIN="${K8S_CLUSTER_2}.${CUSTOM_DOMAIN}"
```

## Source Code

You can find all included source code in the MongoDB Kubernetes Operator repository.

## Procedure

**Step 1: Generate TLS certificates.**

```sh
kubectl --context "${K8S_CLUSTER_0_CONTEXT_NAME}" -n "${OM_NAMESPACE}" apply -f - <<EOF
apiVersion: cert-manager.io/v1
kind: Certificate
metadata:
  name: om-cert
spec:
  dnsNames:
  - ${OPS_MANAGER_EXTERNAL_DOMAIN}
  duration: 240h0m0s
  issuerRef:
    name: my-ca-issuer
    kind: ClusterIssuer
  renewBefore: 120h0m0s
  secretName: cert-prefix-om-cert
  usages:
  - server auth
  - client auth
---
apiVersion: cert-manager.io/v1
kind: Certificate
metadata:
  name: om-db-cert
spec:
  dnsNames:
  - "*.${APPDB_CLUSTER_0_EXTERNAL_DOMAIN}"
  - "*.${APPDB_CLUSTER_1_EXTERNAL_DOMAIN}"
  - "*.${APPDB_CLUSTER_2_EXTERNAL_DOMAIN}"
  duration: 240h0m0s
  issuerRef:
    name: my-ca-issuer
    kind: ClusterIssuer
  renewBefore: 120h0m0s
  secretName: cert-prefix-om-db-cert
  usages:
  - server auth
  - client auth
EOF
```

**Step 2: Add TLS certificate to GCP.**

```sh
mkdir -p certs

kubectl --context "${K8S_CLUSTER_0_CONTEXT_NAME}" -n "${OM_NAMESPACE}" get secret cert-prefix-om-cert -o jsonpath="{.data['tls\.crt']}" | base64 --decode > certs/tls.crt
kubectl --context "${K8S_CLUSTER_0_CONTEXT_NAME}" -n "${OM_NAMESPACE}" get secret cert-prefix-om-cert -o jsonpath="{.data['tls\.key']}" | base64 --decode > certs/tls.key

gcloud compute ssl-certificates create om-certificate --certificate=certs/tls.crt --private-key=certs/tls.key
```

**Step 3: Create the required Kubernetes components for a load balancer.**

This load balancer distributes traffic between all the replicas of 
Ops Manager across all 3 clusters.

```sh
```

Output:

```
```

**Step 4: Add an "A" record to your DNS zone with your external domain.**

```sh
ip_address=$(gcloud compute forwarding-rules describe om-forwarding-rule --global --format="get(IPAddress)")

gcloud dns record-sets create "${OPS_MANAGER_EXTERNAL_DOMAIN}" --zone="${DNS_ZONE}" --type="A" --ttl="300" --rrdatas="${ip_address}"
```

**Step 5: Create credentials for the Ops Manager admin user.**

```sh
kubectl --context "${K8S_CLUSTER_0_CONTEXT_NAME}" --namespace "${OM_NAMESPACE}" create secret generic om-admin-user-credentials \
  --from-literal=Username="admin" \
  --from-literal=Password="Passw0rd@" \
  --from-literal=FirstName="Jane" \
  --from-literal=LastName="Doe"
```

**Step 6: Deploy Ops Manager.**

```sh
kubectl apply --context "${K8S_CLUSTER_0_CONTEXT_NAME}" -n "${OM_NAMESPACE}" -f - <<EOF
apiVersion: mongodb.com/v1
kind: MongoDBOpsManager
metadata:
  name: om
spec:
  topology: MultiCluster
  version: "${OPS_MANAGER_VERSION}"
  adminCredentials: om-admin-user-credentials
  externalConnectivity:
    type: ClusterIP
    annotations:
      cloud.google.com/neg: '{"exposed_ports": {"8443":{}}}'
  opsManagerURL: "https://${OPS_MANAGER_EXTERNAL_DOMAIN}"
  security:
    certsSecretPrefix: cert-prefix
    tls:
      ca: ca-issuer
  clusterSpecList:
    - clusterName: "${K8S_CLUSTER_0_CONTEXT_NAME}"
      members: 1
    - clusterName: "${K8S_CLUSTER_1_CONTEXT_NAME}"
      members: 2
  applicationDatabase:
    version: "${APPDB_VERSION}"
    topology: MultiCluster
    security:
      certsSecretPrefix: cert-prefix
      tls:
        ca: ca-issuer
    clusterSpecList:
      - clusterName: "${K8S_CLUSTER_0_CONTEXT_NAME}"
        members: 2
        externalAccess:
          externalDomain: "${APPDB_CLUSTER_0_EXTERNAL_DOMAIN}"
          externalService:
            annotations:
               external-dns.alpha.kubernetes.io/hostname: "{podName}.${APPDB_CLUSTER_0_EXTERNAL_DOMAIN}"
      - clusterName: "${K8S_CLUSTER_1_CONTEXT_NAME}"
        members: 2
        externalAccess:
          externalDomain: "${APPDB_CLUSTER_1_EXTERNAL_DOMAIN}"
          externalService:
            annotations:
               external-dns.alpha.kubernetes.io/hostname: "{podName}.${APPDB_CLUSTER_1_EXTERNAL_DOMAIN}"
      - clusterName: "${K8S_CLUSTER_2_CONTEXT_NAME}"
        members: 1
        externalAccess:
          externalDomain: "${APPDB_CLUSTER_2_EXTERNAL_DOMAIN}"
          externalService:
            annotations:
               external-dns.alpha.kubernetes.io/hostname: "{podName}.${APPDB_CLUSTER_2_EXTERNAL_DOMAIN}"
  backup:
    enabled: false
EOF
```

**Step 7: Wait for the Kubernetes Operator to enter a pending state.**

Wait for both the Application Database and Ops Manager deployments to complete.

```sh
```

Output:

```
```

**Step 8: Set up load balancer services.**

```sh
svcneg0=$(kubectl --context "${K8S_CLUSTER_0_CONTEXT_NAME}" -n "${OM_NAMESPACE}" get svcneg -o=jsonpath='{.items[0].metadata.name}')

gcloud compute backend-services add-backend om-backend-service \
    --global \
    --network-endpoint-group="${svcneg0}" \
    --network-endpoint-group-zone="${K8S_CLUSTER_0_ZONE}" \
    --balancing-mode RATE --max-rate-per-endpoint 5
```

```sh
svcneg1=$(kubectl --context "${K8S_CLUSTER_1_CONTEXT_NAME}" -n "${OM_NAMESPACE}" get svcneg -o=jsonpath='{.items[0].metadata.name}')

gcloud compute backend-services add-backend om-backend-service \
    --global \
    --network-endpoint-group="${svcneg1}" \
    --network-endpoint-group-zone="${K8S_CLUSTER_1_ZONE}" \
    --balancing-mode RATE --max-rate-per-endpoint 5
```

**Step 9: Wait for Ops Manager to enter a running state.**

```sh
```

Output:

```
```

**Step 10: Install Minio.**

```sh
kubectl kustomize "github.com/minio/operator/resources/?timeout=120&ref=v5.0.12" | \
  kubectl --context "${K8S_CLUSTER_0_CONTEXT_NAME}" apply -f -

kubectl kustomize "github.com/minio/operator/examples/kustomization/tenant-tiny?timeout=120&ref=v5.0.12" | \
  kubectl --context "${K8S_CLUSTER_0_CONTEXT_NAME}" apply -f -

# add two buckets to the tenant config
kubectl --context "${K8S_CLUSTER_0_CONTEXT_NAME}" -n "tenant-tiny" patch tenant/myminio \
  --type='json' \
  -p="[{\"op\": \"add\", \"path\": \"/spec/buckets\", \"value\": [{\"name\": \"${S3_OPLOG_BUCKET_NAME}\"}, {\"name\": \"${S3_SNAPSHOT_BUCKET_NAME}\"}]}]"
```

**Step 11: Configure Kubernetes Secrets for Ops Manager backups.**

```sh
kubectl --context "${K8S_CLUSTER_0_CONTEXT_NAME}" -n "${OM_NAMESPACE}" create secret generic s3-access-secret \
  --from-literal=accessKey="${S3_ACCESS_KEY}" \
  --from-literal=secretKey="${S3_SECRET_KEY}"

# minio TLS secrets are signed with the default k8s root CA
kubectl --context "${K8S_CLUSTER_0_CONTEXT_NAME}" -n "${OM_NAMESPACE}" create secret generic s3-ca-cert \
  --from-literal=ca.crt="$(kubectl --context "${K8S_CLUSTER_0_CONTEXT_NAME}" -n kube-system get configmap kube-root-ca.crt -o jsonpath="{.data.ca\.crt}")"
```

**Step 12: Enable S3 (Minio) backups in Ops Manager.**

```sh
kubectl apply --context "${K8S_CLUSTER_0_CONTEXT_NAME}" -n "${OM_NAMESPACE}" -f - <<EOF
apiVersion: mongodb.com/v1
kind: MongoDBOpsManager
metadata:
  name: om
spec:
  topology: MultiCluster
  version: "${OPS_MANAGER_VERSION}"
  adminCredentials: om-admin-user-credentials
  externalConnectivity:
    type: ClusterIP
    annotations:
      cloud.google.com/neg: '{"exposed_ports": {"8443":{}}}'
  opsManagerURL: "https://${OPS_MANAGER_EXTERNAL_DOMAIN}"
  security:
    certsSecretPrefix: cert-prefix
    tls:
      ca: ca-issuer
  clusterSpecList:
    - clusterName: "${K8S_CLUSTER_0_CONTEXT_NAME}"
      members: 1
      backup:
        members: 0
    - clusterName: "${K8S_CLUSTER_1_CONTEXT_NAME}"
      members: 2
      backup:
        members: 0
    - clusterName: "${K8S_CLUSTER_2_CONTEXT_NAME}"
      members: 0
      backup:
        members: 1
  applicationDatabase:
    version: "${APPDB_VERSION}"
    topology: MultiCluster
    security:
      certsSecretPrefix: cert-prefix
      tls:
        ca: ca-issuer
    clusterSpecList:
      - clusterName: "${K8S_CLUSTER_0_CONTEXT_NAME}"
        members: 2
        externalAccess:
          externalDomain: "${APPDB_CLUSTER_0_EXTERNAL_DOMAIN}"
          externalService:
            annotations:
               external-dns.alpha.kubernetes.io/hostname: "{podName}.${APPDB_CLUSTER_0_EXTERNAL_DOMAIN}"
      - clusterName: "${K8S_CLUSTER_1_CONTEXT_NAME}"
        members: 2
        externalAccess:
          externalDomain: "${APPDB_CLUSTER_1_EXTERNAL_DOMAIN}"
          externalService:
            annotations:
               external-dns.alpha.kubernetes.io/hostname: "{podName}.${APPDB_CLUSTER_1_EXTERNAL_DOMAIN}"
      - clusterName: "${K8S_CLUSTER_2_CONTEXT_NAME}"
        members: 1
        externalAccess:
          externalDomain: "${APPDB_CLUSTER_2_EXTERNAL_DOMAIN}"
          externalService:
            annotations:
               external-dns.alpha.kubernetes.io/hostname: "{podName}.${APPDB_CLUSTER_2_EXTERNAL_DOMAIN}"
  backup:
    enabled: true
    s3Stores:
      - name: my-s3-block-store
        s3SecretRef:
          name: "s3-access-secret"
        pathStyleAccessEnabled: true
        s3BucketEndpoint: "${S3_ENDPOINT}"
        s3BucketName: "${S3_SNAPSHOT_BUCKET_NAME}"
        customCertificateSecretRefs:
          - name: s3-ca-cert
            key: ca.crt
    s3OpLogStores:
      - name: my-s3-oplog-store
        s3SecretRef:
          name: "s3-access-secret"
        s3BucketEndpoint: "${S3_ENDPOINT}"
        s3BucketName: "${S3_OPLOG_BUCKET_NAME}"
        pathStyleAccessEnabled: true
        customCertificateSecretRefs:
          - name: s3-ca-cert
            key: ca.crt
EOF
```

**Step 13: Wait for Ops Manager to enter a running state.**

```sh
```

Output:

```
```

**Step 14: Create MongoDB Organization and get credentials.**

To configure credentials, you must create an Ops Manager organization,
generate programmatic API keys in the Ops Manager UI, and create a [secret](https://kubernetes.io/docs/concepts/configuration/secret/) 
with your Load Balancer IP. See create-k8s-credentials to learn more.
