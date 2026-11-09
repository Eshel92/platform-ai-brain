<!-- Converted from tutorial/install-fts-vs-with-enterprise.txt (reStructuredText). Includes are inlined. -->

:noprevnext:

# Install and Use Search With MongoDB Enterprise Edition

You can use the Kubernetes Operator to deploy MongoDB Search and 
Vector Search resources to run with MongoDB enterprise v8.2.0 
or higher on a Kubernetes cluster. This procedure demonstrates how to deploy
and configure the `mongot` process to run with a new or existing
replica set in your Kubernetes cluster. The deployment uses TLS (Transport Layer Security)
certificates to ensure secure communication between MongoDB nodes and
the `mongot` search process.

## Prerequisites

To deploy MongoDB Search and Vector Search, you must have the
following: 

- A running Kubernetes cluster with `kubeconfig` available locally. 
- Kubernetes command-line tool, `kubectl`, configured to communicate with
  your cluster.
- [Helm](https://helm.sh/), the package manager for Kubernetes, to install the Kubernetes Operator.
- Bash v5.1 or higher for running the commands in this tutorial. 
- `MongoDB Ops Manager` or MongoDB Cloud Manager project and API (Application Programming Interface) credentials. 

## Procedure

**Step 1: Required. Set the environment variables.**

Set the environment variables for use in the subsequent steps in
this procedure. Copy the following commands, update the values for
your environment, and then run them to load the variables:   

```yaml
# set it to the context name of the k8s cluster
export K8S_CTX="<local cluster context>"

# the following namespace will be created if not exists
export MDB_NS="mongodb"

# name of the MongoDB Custom Resource.
export MDB_RESOURCE_NAME="mdb-rs"

export MDB_MEMBERS=3
# OM/CM's project name to be used to manage mongodb replica set
export OPS_MANAGER_PROJECT_NAME="<arbitrary project name>"

# URL to Cloud Manager or Ops Manager instance
export OPS_MANAGER_API_URL="https://cloud-qa.mongodb.com"

# The API key can be an Org Owner - the operator can create the project automatically then.
# The API key can also be created in a particular project that was created manually with the Project Owner scope.
export OPS_MANAGER_API_USER="<SET API USER>"
export OPS_MANAGER_API_KEY="<SET API KEY>"
export OPS_MANAGER_ORG_ID="<SET ORG ID>"

# minimum required MongoDB version for running MongoDB Search is 8.2.0
export MDB_VERSION="8.2.0-ent"

# root admin user for convenience, not used here at all in this guide
export MDB_ADMIN_USER_PASSWORD="admin-user-password-CHANGE-ME"
# regular user performing restore and search queries on sample mflix database
export MDB_USER_PASSWORD="mdb-user-password-CHANGE-ME"
# user for MongoDB Search to connect to the replica set to synchronise data from
export MDB_SEARCH_SYNC_USER_PASSWORD="search-sync-user-password-CHANGE-ME"

export OPERATOR_HELM_CHART="mongodb/mongodb-kubernetes"
# comma-separated key=value pairs for additional parameters passed to the helm-chart installing the operator
export OPERATOR_ADDITIONAL_HELM_VALUES=""

export MDB_TLS_CERT_SECRET_PREFIX="certs"
export MDB_TLS_CA_CONFIGMAP="${MDB_RESOURCE_NAME}-ca-configmap"

export CERT_MANAGER_NAMESPACE="cert-manager"
export MDB_TLS_SELF_SIGNED_ISSUER="selfsigned-bootstrap-issuer"
export MDB_TLS_CA_CERT_NAME="my-selfsigned-ca"
export MDB_TLS_CA_SECRET_NAME="root-secret"
export MDB_TLS_CA_ISSUER="my-ca-issuer"
export MDB_TLS_SERVER_CERT_SECRET_NAME="${MDB_TLS_CERT_SECRET_PREFIX}-${MDB_RESOURCE_NAME}-cert"
export MDB_SEARCH_TLS_SECRET_NAME="${MDB_RESOURCE_NAME}-search-tls"

export MDB_CONNECTION_STRING="mongodb://mdb-user:${MDB_USER_PASSWORD}@${MDB_RESOURCE_NAME}-svc.${MDB_NS}.svc.cluster.local:27017/?replicaSet=${MDB_RESOURCE_NAME}&tls=true&tlsCAFile=/tls/ca.crt"
```

To verify that all necessary environment variables are set,
run the following the following code in your terminal:

```yaml
required=(
  K8S_CTX
  MDB_NS
  MDB_RESOURCE_NAME
  MDB_VERSION
  MDB_MEMBERS
  CERT_MANAGER_NAMESPACE
  MDB_TLS_CA_SECRET_NAME
  MDB_TLS_SERVER_CERT_SECRET_NAME
  MDB_SEARCH_TLS_SECRET_NAME
  MDB_ADMIN_USER_PASSWORD
  MDB_SEARCH_SYNC_USER_PASSWORD
  MDB_USER_PASSWORD
  OPERATOR_HELM_CHART
  OPS_MANAGER_PROJECT_NAME
  OPS_MANAGER_API_URL
  OPS_MANAGER_API_USER
  OPS_MANAGER_API_KEY
)

missing_req=()
for v in "${required[@]}"; do [[ -n "${!v:-}" ]] || missing_req+=("${v}"); done
if (( ${#missing_req[@]} )); then
  echo "ERROR: Missing required environment variables:" >&2
  for m in "${missing_req[@]}"; do echo "  - ${m}" >&2; done
else
  echo "All required environment variables present."
fi
```

**Step 2: Conditional. Add the MongoDB Helm repository.**

[Helm](https://helm.sh/) automates the deployment and management of MongoDB
instances on Kubernetes. If you have already added the Helm
repository that contains the Helm chart for installing the
Kubernetes Operator operator, skip this step. Otherwise, add the
Helm repository.

To add, copy, paste, and run the following command:  

```shell
```

Output:

```shell
```

**Step 3: Conditional. Install the MongoDB Controllers for Kubernetes Operator.**

The Kubernetes Operator watches `MongoDB`, `MongoDBOpsManager`, and
MongoDBSearch custom resources and manages the lifecycle of
your MongoDB deployments. If you already installed the MongoDB Controllers for Kubernetes Operator,
skip this step. Otherwise, install the MongoDB Controllers for Kubernetes Operator from the Helm
repository you added in the previous step. 

To install the MongoDB Controllers for Kubernetes Operator in the `mongodb` namespace, copy, paste,
and run the following: 

```shell
```

Output:

```shell
```

**Step 4: Conditional. Install the `cert-manager`.**

The `cert-manager` is required for managing TLS (Transport Layer Security) certificates.
If you already have `cert-manager` installed in your cluster,
skip this step. Otherwise, install `cert-manager` using [Helm](https://helm.sh/).

To install `cert-manager` in the `cert-manager` namespace,
run the following command in your terminal:

```shell
helm upgrade --install \
  cert-manager \
  oci://quay.io/jetstack/charts/cert-manager \
  --kube-context "${K8S_CTX}" \
  --namespace "${CERT_MANAGER_NAMESPACE}" \
  --create-namespace \
  --set crds.enabled=true

for deployment in cert-manager cert-manager-cainjector cert-manager-webhook; do
  kubectl --context "${K8S_CTX}" \
    -n "${CERT_MANAGER_NAMESPACE}" \
    wait --for=condition=Available "deployment/${deployment}" --timeout=300s
done

echo "cert-manager is ready in namespace ${CERT_MANAGER_NAMESPACE}."
```

**Step 5: Required. Prepare certificate issuer and CA infrastructure.**

Create the certificate authority infrastructure that will issue TLS (Transport Layer Security)
certificates for `MongoDB` and `MongoDBSearch` resources. The
commands perform the following actions: 

- Create a self-signed `ClusterIssuer`.
- Generate a CA certificate.
- Publish a cluster-wide CA issuer that all namespaces can use. 
- Expose the CA bundle through a `ConfigMap` so MongoDB
  resources can use it. 

```shell
# Bootstrap a self-signed ClusterIssuer to mint the CA secret consumed by application workloads.
kubectl apply --context "${K8S_CTX}" -f - <<EOF_MANIFEST
apiVersion: cert-manager.io/v1
kind: ClusterIssuer
metadata:
  name: ${MDB_TLS_SELF_SIGNED_ISSUER}
spec:
  selfSigned: {}
EOF_MANIFEST

kubectl --context "${K8S_CTX}" wait --for=condition=Ready clusterissuer "${MDB_TLS_SELF_SIGNED_ISSUER}"

kubectl apply --context "${K8S_CTX}" -f - <<EOF_MANIFEST
apiVersion: cert-manager.io/v1
kind: Certificate
metadata:
  name: ${MDB_TLS_CA_CERT_NAME}
  namespace: ${CERT_MANAGER_NAMESPACE}
spec:
  isCA: true
  commonName: ${MDB_TLS_CA_CERT_NAME}
  secretName: ${MDB_TLS_CA_SECRET_NAME}
  privateKey:
    algorithm: ECDSA
    size: 256
  issuerRef:
    name: ${MDB_TLS_SELF_SIGNED_ISSUER}
    kind: ClusterIssuer
EOF_MANIFEST

kubectl --context "${K8S_CTX}" wait --for=condition=Ready -n "${CERT_MANAGER_NAMESPACE}" certificate "${MDB_TLS_CA_CERT_NAME}"

kubectl apply --context "${K8S_CTX}" -f - <<EOF_MANIFEST
apiVersion: cert-manager.io/v1
kind: ClusterIssuer
metadata:
  name: ${MDB_TLS_CA_ISSUER}
spec:
  ca:
    secretName: ${MDB_TLS_CA_SECRET_NAME}
EOF_MANIFEST

kubectl --context "${K8S_CTX}" wait --for=condition=Ready clusterissuer "${MDB_TLS_CA_ISSUER}"

TMP_CA_CERT="$(mktemp)"
trap 'rm -f "${TMP_CA_CERT}"' EXIT

kubectl --context "${K8S_CTX}" get secret "${MDB_TLS_CA_SECRET_NAME}" -n "${CERT_MANAGER_NAMESPACE}" -o jsonpath="{.data['ca\\.crt']}" | base64 --decode > "${TMP_CA_CERT}"

kubectl --context "${K8S_CTX}" create configmap "${MDB_TLS_CA_CONFIGMAP}" -n "${MDB_NS}" \
  --from-file=ca-pem="${TMP_CA_CERT}" --from-file=mms-ca.crt="${TMP_CA_CERT}" \
  --from-file=ca.crt="${TMP_CA_CERT}" \
  --dry-run=client -o yaml | kubectl --context "${K8S_CTX}" apply -f -
```

**Step 6: Required. Issue TLS certificates.**

Issue TLS (Transport Layer Security) certificates for both the `MongoDB` server
(`${MDB_RESOURCE_NAME}-server-tls`) and the `MongoDBSearch`
service (`${MDB_RESOURCE_NAME}-search-tls`). The MongoDB server
certificate includes all necessary DNS names for the pod and
service communication. Both certificates support server and client
authentication. 

```shell
server_certificate="${MDB_RESOURCE_NAME}-server-tls"
search_certificate="${MDB_RESOURCE_NAME}-search-tls"

mongo_dns_names=()
for ((member = 0; member < MDB_MEMBERS; member++)); do
  mongo_dns_names+=("${MDB_RESOURCE_NAME}-${member}")
  mongo_dns_names+=("${MDB_RESOURCE_NAME}-${member}.${MDB_RESOURCE_NAME}-svc.${MDB_NS}.svc.cluster.local")
done
mongo_dns_names+=(
  "${MDB_RESOURCE_NAME}-svc.${MDB_NS}.svc.cluster.local"
  "*.${MDB_RESOURCE_NAME}-svc.${MDB_NS}.svc.cluster.local"
)

search_dns_names=(
  "${MDB_RESOURCE_NAME}-search-svc.${MDB_NS}.svc.cluster.local"
)

render_dns_list() {
  local dns_list=("$@")
  for dns in "${dns_list[@]}"; do
    printf "      - \"%s\"\n" "${dns}"
  done
}

kubectl apply --context "${K8S_CTX}" -n "${MDB_NS}" -f - <<EOF_MANIFEST
apiVersion: cert-manager.io/v1
kind: Certificate
metadata:
  name: ${server_certificate}
  namespace: ${MDB_NS}
spec:
  secretName: ${MDB_TLS_SERVER_CERT_SECRET_NAME}
  issuerRef:
    name: ${MDB_TLS_CA_ISSUER}
    kind: ClusterIssuer
  duration: 240h0m0s
  renewBefore: 120h0m0s
  usages:
    - digital signature
    - key encipherment
    - server auth
    - client auth
  dnsNames:
$(render_dns_list "${mongo_dns_names[@]}")
---
apiVersion: cert-manager.io/v1
kind: Certificate
metadata:
  name: ${search_certificate}
  namespace: ${MDB_NS}
spec:
  secretName: ${MDB_SEARCH_TLS_SECRET_NAME}
  issuerRef:
    name: ${MDB_TLS_CA_ISSUER}
    kind: ClusterIssuer
  duration: 240h0m0s
  renewBefore: 120h0m0s
  usages:
    - digital signature
    - key encipherment
    - server auth
    - client auth
  dnsNames:
$(render_dns_list "${search_dns_names[@]}")
EOF_MANIFEST

kubectl --context "${K8S_CTX}" -n "${MDB_NS}" wait --for=condition=Ready certificate "${server_certificate}" --timeout=300s
kubectl --context "${K8S_CTX}" -n "${MDB_NS}" wait --for=condition=Ready certificate "${search_certificate}" --timeout=300s
```

**Step 7: Conditional. Create and deploy the MongoDB Enterprise resource.**

If you have already deployed MongoDB Enterprise, skip to the next
step. Otherwise, deploy the MongoDB Enterprise resource. 

To deploy the MongoDB Enterprise, complete the following steps:

a. Create the ConfigMap and secret for the `MongoDB Ops Manager` project if
   you are using `MongoDB Ops Manager`.

   To store the configuration and credentials for integration with
   `MongoDB Ops Manager`, copy, paste, and run the following commands:

   ```shell
   kubectl --context "${K8S_CTX}" -n "${MDB_NS}" create configmap om-project \
     --from-literal=projectName="${OPS_MANAGER_PROJECT_NAME}" --from-literal=baseUrl="${OPS_MANAGER_API_URL}" \
     --from-literal=orgId="${OPS_MANAGER_ORG_ID:-}"

   kubectl --context "${K8S_CTX}" -n "${MDB_NS}" create secret generic om-credentials \
     --from-literal=publicKey="${OPS_MANAGER_API_USER}" \
     --from-literal=privateKey="${OPS_MANAGER_API_KEY}"
   ```

#. Create a `MongoDB` custom resource named `mdb-rs`. 

   The resource defines CPU and memory resources for the `mongod`
   and `mongodb-agent` containers and instructs the
   Kubernetes Operator to configure a MongoDB replica set with 3
   members:

   To deploy MongoDB Enterprise, copy, paste, and run the
   following in the namespace: 

   ```shell
   kubectl apply --context "${K8S_CTX}" -n "${MDB_NS}" -f - <<EOF
   apiVersion: mongodb.com/v1
   kind: MongoDB
   metadata:
     name: ${MDB_RESOURCE_NAME}
   spec:
     members: ${MDB_MEMBERS}
     version: ${MDB_VERSION}
     type: ReplicaSet
     opsManager:
       configMapRef:
         name: om-project
     credentials: om-credentials
     security:
       authentication:
         enabled: true
         ignoreUnknownUsers: true
         modes:
         - SCRAM
       certsSecretPrefix: ${MDB_TLS_CERT_SECRET_PREFIX}
       tls:
         enabled: true
         ca: ${MDB_TLS_CA_CONFIGMAP}
     agent:
       logLevel: INFO
     podSpec:
       podTemplate:
         spec:
           containers:
           - name: mongodb-enterprise-database
             resources:
               limits:
                 cpu: "2"
                 memory: 2Gi
               requests:
                 cpu: "1"
                 memory: 1Gi
   EOF
   ```

#. Wait for the `MongoDB` resource deployment to complete.

   When you apply the `MongoDB` custom resource, the
   Kubernetes operator begins deploying the MongoDB nodes (pods). This
   step pauses the execution until the `mdbc-rs` resource's
   status phase is `Running`, which indicates that the
   MongoDB Community replica set is operational.

   ```shell
   ```

   Output:

   ```shell
   Waiting for MongoDB resource to reach Running phase...
   mongodb.mongodb.mongodb.com/mdbc-rs condition met

   MongoDB resource
   NAME      PHASE     VERSION
   mdbc-rs   Running   8.2

   Pods running in cluster minikube
   NAME                                           READY   STATUS    RESTARTS   AGE
   mdbc-rs-0                                      2/2     Running   0          2m30s
   mdbc-rs-1                                      2/2     Running   0          82s
   mdbc-rs-2                                      2/2     Running   0          38s
   mongodb-kubernetes-operator-5776c8b4df-cppnf   1/1     Running   0          7m37s
   ```

**Step 8: Required. Create and load the MongoDB user secrets.**

MongoDB requires authentication for secure access. In this step,
you create three Kubernetes secrets: 

- `mdb-admin-user-password`: Credentials for the MongoDB administrator.
- `mdb-user-password`: Credentials for the user authorized to perform search queries.
- `mdbc-rs-search-sync-source-password`: Credentials for a
  dedicated search user used internally by the `mongot` process
  to synchronize data and manage indexes.  

Kubernetes Operator mounts these secrets into the MongoDB pods. 

To create the secrets, copy, paste, and run the following in the
namespace where you deployed MongoDB Server and plan to deploy
MongoDB Search and Vector Search:

```shell
```

Output:

```
secret/mdb-admin-user-password created
secret/mdbc-rs-search-sync-source-password created
secret/mdb-user-password created
```

**Step 9: Required. Create and deploy the resource for MongoDB Search and Vector Search.**

You can deploy one instance of the search node without any load
balancing. To deploy, complete the following steps: 

a. Create a MongoDBSearch custom resource named `mdbc-rs`.

   This resource specifies the CPU and memory resource
   requirements for the search nodes. To learn more about the
   settings in this custom resource, see k8s-fts-vs-settings.

   ```shell
   kubectl apply --context "${K8S_CTX}" -n "${MDB_NS}" -f - <<EOF
   apiVersion: mongodb.com/v1
   kind: MongoDBSearch
   metadata:
     name: ${MDB_RESOURCE_NAME}
   spec:
     # no need to specify source.mongodbResourceRef if MongoDBSearch CR has the same name as MongoDB CR
     # the operator infer it automatically
     security:
       tls:
         certificateKeySecretRef:
           name: ${MDB_SEARCH_TLS_SECRET_NAME}
     resourceRequirements:
       limits:
         cpu: "3"
         memory: 5Gi
       requests:
         cpu: "2"
         memory: 3Gi
   EOF
   ```

#. Wait for the MongoDBSearch resource deployment to
   complete.

   When you apply the MongoDBSearch custom resource, the
   Kubernetes operator begins deploying the search nodes (pods). This
   step pauses the execution until the `mdbc-rs` resource's
   status phase is `Running`, which indicates that the
   MongoDB Community replica set is operational.

   ```shell
   echo "Waiting for MongoDBSearch resource to reach Running phase..."
   kubectl --context "${K8S_CTX}" -n "${MDB_NS}" wait --for=jsonpath='{.status.phase}'=Running "mdbs/${MDB_RESOURCE_NAME}" --timeout=300s
   ```

**Step 10: Optional. Verify the MongoDB Enterprise resource status.**

Ensure that the `MongoDB` resource deployment with
MongoDBSearch was successful.

```javascript
echo "Waiting for MongoDB resource to reach Running phase..."
kubectl --context "${K8S_CTX}" -n "${MDB_NS}" wait --for=jsonpath='{.status.phase}'=Running "mdb/${MDB_RESOURCE_NAME}" --timeout=400s
```

**Step 11: Optional. View all the running pods in your namespace.**

View all the running pods in your namespace pods for the MongoDB
replica set members, the MongoDB Controllers for Kubernetes Operator, and the Search nodes.

```shell
```

Output:

```shell
```

## Next Steps

Now that you've successfully deployed MongoDB Search and Vector Search
to use with MongoDB Enterprise Edition, you can add data in your MongoDB
cluster, create MongoDB Search and Vector Search indexes, and run
queries against your data. To learn more, see k8s-fts-vs-settings.
