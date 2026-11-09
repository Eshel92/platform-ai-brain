<!-- Converted from tutorial/install-fts-vs-with-community.txt (reStructuredText). Includes are inlined. -->

:noprevnext:

# Install and use With MongoDB Community Edition

You can use the Kubernetes Operator and deploy the `mongot` process
resources to run with MongoDB Community Edition v8.2.0 or higher on a
Kubernetes cluster. The `mongot` process supports both MongoDB Search and
Vector Search. Optionally, you can enable and configure Vector Search 
to automatically generate vector embeddings for text data in your 
collections and queries using a supported Voyage AI embedding model. 

**Important:**

Automated embedding is in Preview. The feature and the corresponding 
documentation might change at any time during the preview period. To 
learn more, see [Preview Features](https://www.mongodb.com/docs/preview-features/). 

The following procedure demonstrates how to deploy and
configure MongoDB Search and Vector Search to run with a new or
existing replica set in your Kubernetes cluster. The deployment uses TLS (Transport Layer Security)
certificates to ensure secure communication between MongoDB nodes and
the `mongot` search process.

## Prerequisites

To deploy MongoDB Search and Vector Search, you must have the
following: 

- A running Kubernetes cluster.
- Kubernetes command-line tool, `kubectl`, configured to communicate with
  your cluster.
- [Helm](https://helm.sh/), the package manager for Kubernetes, to install the Kubernetes Operator.
- [cert-manager](https://cert-manager.io/) or an alternative certificate
  management solution for TLS (Transport Layer Security) certificate provisioning.
- Bash v5.1 or higher for running the commands in this tutorial. 

**Optionally**, to configure Vector Search to automatically generate 
vector embeddings for text data in your collections and queries, you 
must create API (Application Programming Interface) keys for the embedding service. We recommend creating 
two keys, one for generating embeddings at index-time for text data in 
your collection and another for generating embeddings at query-time for 
your query text. If you don't have the keys, you can create the keys 
from the Atlas UI.

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

# MongoDBCommunity resource name referenced throughout the guide
export MDB_RESOURCE_NAME="mdbc-rs"
# Number of replica set members deployed in the sample MongoDBCommunity
export MDB_MEMBERS=3

# TLS-related secret names used for MongoDBCommunity and MongoDBSearch
export MDB_TLS_CA_SECRET_NAME="${MDB_RESOURCE_NAME}-ca"
export MDB_TLS_SERVER_CERT_SECRET_NAME="${MDB_RESOURCE_NAME}-tls"
export MDB_SEARCH_TLS_SECRET_NAME="${MDB_RESOURCE_NAME}-search-tls"

export MDB_TLS_CA_CONFIGMAP="${MDB_RESOURCE_NAME}-ca-configmap"
export MDB_TLS_SELF_SIGNED_ISSUER="${MDB_RESOURCE_NAME}-selfsigned-cluster-issuer"
export MDB_TLS_CA_CERT_NAME="${MDB_RESOURCE_NAME}-selfsigned-ca"
export MDB_TLS_CA_ISSUER="${MDB_RESOURCE_NAME}-cluster-issuer"

# minimum required MongoDB version for running MongoDB Search is 8.2.0
export MDB_VERSION="8.2.0"

# root admin user for convenience, not used here at all in this guide
export MDB_ADMIN_USER_PASSWORD="admin-user-password-CHANGE-ME"
# regular user performing restore and search queries on sample mflix database
export MDB_USER_PASSWORD="mdb-user-password-CHANGE-ME"
# user for MongoDB Search to connect to the replica set to synchronise data from
export MDB_SEARCH_SYNC_USER_PASSWORD="search-sync-user-password-CHANGE-ME"

export OPERATOR_HELM_CHART="mongodb/mongodb-kubernetes"
# comma-separated key=value pairs for additional parameters passed to the helm-chart installing the operator
export OPERATOR_ADDITIONAL_HELM_VALUES=""

# TLS is mandatory; connection string must include tls=true
export MDB_CONNECTION_STRING="mongodb://mdb-user:${MDB_USER_PASSWORD}@${MDB_RESOURCE_NAME}-0.${MDB_RESOURCE_NAME}-svc.${MDB_NS}.svc.cluster.local:27017/?replicaSet=${MDB_RESOURCE_NAME}&tls=true&tlsCAFile=/tls/ca.crt"

export CERT_MANAGER_NAMESPACE="cert-manager"

# Vector Search auto embedding related configurations
export AUTO_EMBEDDING_API_KEY_SECRET_NAME="voyage-api-keys"
export AUTO_EMBEDDING_API_QUERY_KEY="<embedding-model-query-key>"
export AUTO_EMBEDDING_API_INDEXING_KEY="<embedding-model-indexing-key>"
export PROVIDER_ENDPOINT="https://ai.mongodb.com/v1/embeddings"
export EMBEDDING_MODEL="voyage-4"
```

**Note:**

If you have the API (Application Programming Interface) keys to enable Vector Search to automatically 
generate embeddings, replace the following placeholder values in the 
environment variables: 

|  |  |
|---|---|
| `AUTO_EMBEDDING_API_QUERY_KEY` | API (Application Programming Interface) key for generating embeddings for the query text. |
| `AUTO_EMBEDDING_API_INDEXING_KEY` | API (Application Programming Interface) key for generating embeddings for text data in your collection at index-time. |
| `PROVIDER_ENDPOINT` | Embedding model provider's endpoint. Value defaults to `https://ai.mongodb.com/v1/embeddings` for keys created from the Atlas UI. Replace with `https://api.voyageai.com/v1/embeddings` if you created the API (Application Programming Interface) keys directly from Voyage AI. |

To verify that all necessary environment variables are set,
run the following code in your terminal:

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
instances on Kubernetes. If you already have the Helm repository
that contains the Helm chart for installing the Kubernetes Operator
operator, or skip this step. Otherwise, add the Helm repository. 

To add the Helm repository, copy, paste, and run the following: 

```shell
```

Output:

```shell
```

**Step 3: Conditional. Install the MongoDB Controllers for Kubernetes Operator.**

The Kubernetes Operator watches `MongoDBCommunity` and
MongoDBSearch custom resources and manages the lifecycle of
your MongoDB deployments. If you already installed the MongoDB Controllers for Kubernetes Operator,
skip this step. Otherwise, install the MongoDB Controllers for Kubernetes Operator from the Helm
repository you added in the previous step. 

To install the MongoDB Controllers for Kubernetes Operator in the `mongodb` namespace, copy, paste,
and run the following commands: 

```shell
```

Output:

```shell
```

**Step 4: Optional. Wait for the operator deployment.**

Ensure that the Kubernetes Operator is fully operational before
proceeding with the MongoDB Search and Vector Search deployment.
Run the following command to verify that all operator components
are running and available. 

```shell
```

Output:

```shell
```

**Step 5: Required. Create and load the MongoDB user secrets.**

MongoDB requires authentication for secure access. In this step,
you create three Kubernetes secrets: 

- `mdb-admin-user-password`: Credentials for the  MongoDB
  administrator.
- `mdb-user-password`: Credentials for the user authorized to
  perform search queries.
- `mdbc-rs-search-sync-source-password`: Credentials for a
  dedicated search user used internally by the `mongot` 
  process to synchronize data and manage indexes. 

Kubernetes Operator uses passwords from those secrets to automatically
create the users in the MongoDB database.  

To create the secrets, copy, paste, and run the following command: 

```shell
```

Output:

```
secret/mdb-admin-user-password created
secret/mdbc-rs-search-sync-source-password created
secret/mdb-user-password created
```

**Step 6: Conditional. Install the `cert-manager`.**

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

**Step 7: Required. Prepare certificate issuer and CA infrastructure.**

Create the certificate authority infrastructure that will issue TLS (Transport Layer Security)
certificates for `MongoDB` and `MongoDBSearch` resources. The
commands perform the following actions: 

- Create a self-signed `ClusterIssuer`.
- Generate a CA certificate.
- Publish a cluster-wide CA issuer that all namespaces can use. 
- Expose the CA bundle through a `ConfigMap` so that MongoDB
  resources can use it. 

```shell
# Bootstrap a self-signed ClusterIssuer that will mint the CA material consumed by
# the MongoDBCommunity deployment.
kubectl apply --context "${K8S_CTX}" -f - <<EOF_MANIFEST
apiVersion: cert-manager.io/v1
kind: ClusterIssuer
metadata:
  name: ${MDB_TLS_SELF_SIGNED_ISSUER}
spec:
  selfSigned: {}
EOF_MANIFEST

kubectl --context "${K8S_CTX}" wait --for=condition=Ready clusterissuer "${MDB_TLS_SELF_SIGNED_ISSUER}"

# Create the CA certificate and secret in the cert-manager namespace.
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

# Publish a cluster-scoped issuer that fronts the generated CA secret so all namespaces can reuse it.
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

kubectl --context "${K8S_CTX}" \
  get secret "${MDB_TLS_CA_SECRET_NAME}" -n "${CERT_MANAGER_NAMESPACE}" \
  -o jsonpath="{.data['ca\\.crt']}" | base64 --decode > "${TMP_CA_CERT}"

# Expose the CA bundle through a ConfigMap for workloads and the MongoDBCommunity resource.
kubectl --context "${K8S_CTX}" create configmap "${MDB_TLS_CA_CONFIGMAP}" -n "${MDB_NS}" \
  --from-file=ca-pem="${TMP_CA_CERT}" --from-file=mms-ca.crt="${TMP_CA_CERT}" \
  --from-file=ca.crt="${TMP_CA_CERT}" \
  --dry-run=client -o yaml | kubectl --context "${K8S_CTX}" apply -f -

echo "Cluster-wide CA issuer ${MDB_TLS_CA_ISSUER} is ready."
```

**Step 8: Required. Issue TLS certificates.**

Issue TLS (Transport Layer Security) certificates for both the `MongoDB` server and the
`MongoDBSearch` service. The MongoDB server certificate includes
all necessary DNS names for the pod and service communication. Both
certificates support server and client authentication.

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

echo "MongoDB TLS certificates have been issued."
```

**Step 9: Conditional. Create and deploy the MongoDB Community resource.**

If you've already deployed the MongoDB Community Edition, skip this
step. Otherwise, deploy the MongoDB Community Edition.

To deploy the MongoDB Community Edition, complete the following steps:

a. Create a `MongoDBCommunity` custom resource named `mdb-rs`. 

   The resource defines CPU and memory resources for the `mongod`
   and `mongodb-agent` containers, and sets up the following three
   users: 

   |  |  |
   |---|---|
   | `mdb-user` | User that can restore database and run search queries. This user uses the `mdb-user-password` secret to perform these operations. |
   | `search-sync-source` | User that MongoDB Search uses to connect to MongoDB database in order to manage and build indexes. This user uses `searchCoordinator` role that the Kubernetes operator creates. This uses uses the `mdbc-rs-search-sync-source-password` secret to connect `mongot` to `mongod`. |
   | `admin-user` | Database admin user. |

   The Kubernetes Operator uses this resource to configure a MongoDB 
   replica set with 3 members. 

   To create the secrets, copy, paste, and run the following
   commands: 

   ```shell
   kubectl apply --context "${K8S_CTX}" -n "${MDB_NS}" -f - <<EOF
   apiVersion: mongodbcommunity.mongodb.com/v1
   kind: MongoDBCommunity
   metadata:
     name: ${MDB_RESOURCE_NAME}
   spec:
     version: ${MDB_VERSION}
     type: ReplicaSet
     members: ${MDB_MEMBERS}
     security:
       tls:
         enabled: true
         certificateKeySecretRef:
           name: ${MDB_TLS_SERVER_CERT_SECRET_NAME}
         caConfigMapRef:
           name: ${MDB_TLS_CA_CONFIGMAP}
       authentication:
         ignoreUnknownUsers: true
         modes:
           - SCRAM
     agent:
       logLevel: DEBUG
     statefulSet:
       spec:
         template:
           spec:
             containers:
               - name: mongod
                 resources:
                   limits:
                     cpu: "2"
                     memory: 2Gi
                   requests:
                     cpu: "1"
                     memory: 1Gi
               - name: mongodb-agent
                 resources:
                   limits:
                     cpu: "1"
                     memory: 2Gi
                   requests:
                     cpu: "0.5"
                     memory: 1Gi
     users:
       # admin user with root role
       - name: mdb-admin
         db: admin
         # a reference to the secret containing user password
         passwordSecretRef:
           name: mdb-admin-user-password
         scramCredentialsSecretName: mdb-admin-user
         roles:
           - name: root
             db: admin
       # user performing search queries
       - name: mdb-user
         db: admin
         # a reference to the secret containing user password
         passwordSecretRef:
           name: mdb-user-password
         scramCredentialsSecretName: mdb-user-scram
         roles:
           - name: restore
             db: sample_mflix
           - name: readWrite
             db: sample_mflix
       # user used by MongoDB Search to connect to MongoDB database to
       # synchronize data from.
       # For MongoDB <8.2, the operator will be creating the
       # searchCoordinator custom role automatically.
       # From MongoDB 8.2, searchCoordinator role will be a
       # built-in role.
       - name: search-sync-source
         db: admin
         # a reference to the secret that will be used to generate the user's password
         passwordSecretRef:
           name: ${MDB_RESOURCE_NAME}-search-sync-source-password
         scramCredentialsSecretName: ${MDB_RESOURCE_NAME}-search-sync-source
         roles:
           - name: searchCoordinator
             db: admin
   EOF
   ```

#. Wait for the `MongoDBCommunity` resource deployment to
   complete.

   When you apply the `MongoDBCommunity` custom resource, the
   Kubernetes operator begins deploying the MongoDB nodes (pods). This
   step pauses the execution until the `mdbc-rs` resource's
   status phase is `Running`, which indicates that the
   MongoDB Community replica set is operational.

   ```shell
   ```

   Output:

   ```shell
   Waiting for MongoDBCommunity resource to reach Running phase...
   mongodbcommunity.mongodbcommunity.mongodb.com/mdbc-rs condition met

   MongoDBCommunity resource
   NAME      PHASE     VERSION
   mdbc-rs   Running   8.2

   Pods running in cluster minikube
   NAME                                           READY   STATUS    RESTARTS   AGE
   mdbc-rs-0                                      2/2     Running   0          2m30s
   mdbc-rs-1                                      2/2     Running   0          82s
   mdbc-rs-2                                      2/2     Running   0          38s
   mongodb-kubernetes-operator-5776c8b4df-cppnf   1/1     Running   0          7m37s
   ```

**Step 10: Required. Create and deploy the resource for MongoDB Search and Vector Search.**

You can deploy one instance of the search node without any load
balancing. 

To deploy, complete the following steps: 

a. Create a MongoDBSearch custom resource named `mdbc-rs`.

   This resource specifies the CPU and memory resource
   requirements for the search nodes. To learn more about the
   settings in this custom resource, see k8s-fts-vs-settings.

   **with-auto-embed:**

   ```shell
   # create a Kubernetes secret that would have embedding model's API Keys
   kubectl create secret generic "${AUTO_EMBEDDING_API_KEY_SECRET_NAME}" \
     --from-literal=query-key="${AUTO_EMBEDDING_API_QUERY_KEY}" \
     --from-literal=indexing-key="${AUTO_EMBEDDING_API_INDEXING_KEY}" --context "${K8S_CTX}" -n "${MDB_NS}"

   # create MongoDBSearch resource, enabling the auto embedding using the API Keys provided above
   kubectl apply --context "${K8S_CTX}" -n "${MDB_NS}" -f - <<EOF
   apiVersion: mongodb.com/v1
   kind: MongoDBSearch
   metadata:
     name: ${MDB_RESOURCE_NAME}
   spec:
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
     autoEmbedding:
       providerEndpoint: ${PROVIDER_ENDPOINT}
       embeddingModelAPIKeySecret:
         name: ${AUTO_EMBEDDING_API_KEY_SECRET_NAME}
   EOF
   ```

   **Note:**

   Since the Kubernetes Operator only deploys single instance of MongoDB Search, that instance is automatically configured as the embedding materialized View writer.

   **without-auto-embed:**

   ```shell
   kubectl apply --context "${K8S_CTX}" -n "${MDB_NS}" -f - <<EOF
   apiVersion: mongodb.com/v1
   kind: MongoDBSearch
   metadata:
     name: ${MDB_RESOURCE_NAME}
   spec:
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
   step pauses the execution until the `mdbc-rs`
   MongoDBSearch resource's status phase is `Running`, which
   indicates that the MongoDB Search is operational.

   ```shell
   echo "Waiting for MongoDBSearch resource to reach Running phase..."
   kubectl --context "${K8S_CTX}" -n "${MDB_NS}" wait \
     --for=jsonpath='{.status.phase}'=Running mdbs/"${MDB_RESOURCE_NAME}" --timeout=300s
   ```

**Step 11: Optional. Verify the MongoDB Community resource status.**

Ensure that the `MongoDBCommunity` resource deployment with
MongoDBSearch was successful.

```javascript
echo "Waiting for MongoDBCommunity resource to reach Running phase..."
kubectl --context "${K8S_CTX}" -n "${MDB_NS}" wait \
  --for=jsonpath='{.status.phase}'=Running mdbc/mdbc-rs --timeout=400s
echo; echo "MongoDBCommunity resource"
kubectl --context "${K8S_CTX}" -n "${MDB_NS}" get mdbc/mdbc-rs
echo; echo "Pods running in cluster ${K8S_CTX}"
kubectl --context "${K8S_CTX}" -n "${MDB_NS}" get pods
```

**Step 12: Optional. View all the running pods in your namespace.**

View all the running pods in your namespace pods for the MongoDB
replica set members, the MongoDB Controllers for Kubernetes Operator, and the Search nodes. 

```shell
```

Output:

```shell
```

## Next Steps

Now that you've successfully deployed MongoDB Search and Vector Search
to use with MongoDB Community Edition, proceed to add data into your
MongoDB cluster, create MongoDB Search and Vector Search indexes, and
run queries agaist your data. To learn more, see k8s-use-fts-vs.
