<!-- Converted from reference-architectures/multi-cluster/multi-cluster-om.txt (reStructuredText). Includes are inlined. -->

# Multi-Cluster Ops Manager

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
- Complete the Istio Service mesh procedure or the equivalent.
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

export S3_OPLOG_BUCKET_NAME=s3-oplog-store
export S3_SNAPSHOT_BUCKET_NAME=s3-snapshot-store

# If you use your own S3 storage - set the values accordingly.
# By default we install Minio to handle S3 storage and here are set the default credentials.
export S3_ENDPOINT="minio.tenant-tiny.svc.cluster.local"
export S3_ACCESS_KEY="console"
export S3_SECRET_KEY="console123"

export OPS_MANAGER_VERSION="8.0.5"
export APPDB_VERSION="8.0.5-ent"
```

## Source Code

You can find all included source code in the [MongoDB Kubernetes Operator repository](https://github.com/mongodb/mongodb-kubernetes/tree/1.7.0/public/architectures/ra-06-ops-manager-multi-cluster).

## Procedure

**Step 1: Generate TLS certificates.**

```bash
kubectl --context "${K8S_CLUSTER_0_CONTEXT_NAME}" -n "${OM_NAMESPACE}" apply -f - <<EOF
apiVersion: cert-manager.io/v1
kind: Certificate
metadata:
  name: om-cert
spec:
  dnsNames:
  - om-svc.${OM_NAMESPACE}.svc.cluster.local
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
  - "*.${OM_NAMESPACE}.svc.cluster.local"
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

**Step 2: Install Ops Manager.**

At this point, you have prepared the environment and the Kubernetes Operator
to deploy the Ops Manager resource.

a. Create the necessary credentials for the Ops Manager admin user that the
   Kubernetes Operator will create after deploying the Ops Manager Application instance:

   ```bash
   kubectl --context "${K8S_CLUSTER_0_CONTEXT_NAME}" --namespace "${OM_NAMESPACE}" create secret generic om-admin-user-credentials \
     --from-literal=Username="admin" \
     --from-literal=Password="Passw0rd@" \
     --from-literal=FirstName="Jane" \
     --from-literal=LastName="Doe"
   ```

b. Deploy the simplest `MongoDBOpsManager` custom resource possible
   (with TLS (Transport Layer Security) enabled) on a single member cluster, which also serves as the
   central cluster.

   This deployment is almost the same as the deployment for the single-cluster mode,
   but with `spec.topology` and `spec.applicationDatabase.topology`
   set to `MultiCluster`.

   Deploying this way shows that a single Kubernetes cluster deployment is
   a special case of a multi-Kubernetes cluster deployment on a single Kubernetes member cluster.
   You can start deploying the Ops Manager Application and the Application Database
   on as many Kubernetes clusters as necessary from the beginning, and don't
   have to start with the deployment with only a single member Kubernetes cluster.

   At this point, you have prepared the Ops Manager deployment to span more
   than one Kubernetes cluster, which you will do later in this procedure.

   ```bash
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
       type: LoadBalancer
     security:
       certsSecretPrefix: cert-prefix
       tls:
         ca: ca-issuer
     clusterSpecList:
       - clusterName: "${K8S_CLUSTER_0_CONTEXT_NAME}"
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
           members: 3
     backup:
       enabled: false
   EOF
   ```

c. Wait for the Kubernetes Operator to pick up the work and reach the
   `status.applicationDatabase.phase=Pending` state. Wait for both the
   Application Database and Ops Manager deployments to complete.

   ```bash
   ```

   Output:

   ```bash
   ```

d. Deploy Ops Manager. The Kubernetes Operator deploys Ops Manager by performing
   the following steps. It:

   - Deploys the Application Database\'s replica set nodes and waits
     for the MongoDB processes in the replica set to start running.
   - Deploys the Ops Manager Application instance with the Application Database\'s
     connection string and waits for it to become ready.
   - Adds the Monitoring MongoDB Agent containers to each Application Database\'s Pod.
   - Waits for both the Ops Manager Application and the Application Database Pods to start running.

   ```bash
   ```

   Output:

   ```bash
   ```

   Now that you have deployed a single-member cluster in a multi-cluster mode,
   you can reconfigure this deployment to span more than one Kubernetes cluster.

e. On the second member cluster, deploy two additional Application Database
   replica set members and one additional instance of the Ops Manager Application:

   ```bash
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
       type: LoadBalancer
     security:
       certsSecretPrefix: cert-prefix
       tls:
         ca: ca-issuer
     clusterSpecList:
       - clusterName: "${K8S_CLUSTER_0_CONTEXT_NAME}"
         members: 1
       - clusterName: "${K8S_CLUSTER_1_CONTEXT_NAME}"
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
           members: 3
         - clusterName: "${K8S_CLUSTER_1_CONTEXT_NAME}"
           members: 2
     backup:
       enabled: false
   EOF
   ```

f. Wait for the Kubernetes Operator to pick up the work (pending phase):

   ```bash
   ```

   Output:

   ```bash
   ```

g. Wait for the Kubernetes Operator to finish deploying all components:

   ```bash
   ```

   Output:

   ```bash
   ```

**Step 3: Enable backup.**

In a multi-Kubernetes cluster deployment of the Ops Manager Application, you can configure
only S3 (Simple Storage Service)-based backup storage. This procedure refers to `S3_*`
defined in env_variables.sh.

a. Optional. Install the [MinIO Operator](https://github.com/minio/operator).

   This procedure deploys S3 (Simple Storage Service)-compatible storage for your backups using the [MinIO Operator](https://github.com/minio/operator).
   You can skip this step if you have AWS (Amazon Web Services) S3 (Simple Storage Service) or other S3 (Simple Storage Service)-compatible
   buckets available. Adjust the `S3_*` variables accordingly in
   env_variables.sh in this case.

   ```bash
   kubectl kustomize "github.com/minio/operator/resources/?timeout=120&ref=v5.0.12" | \
     kubectl --context "${K8S_CLUSTER_0_CONTEXT_NAME}" apply -f -

   kubectl kustomize "github.com/minio/operator/examples/kustomization/tenant-tiny?timeout=120&ref=v5.0.12" | \
     kubectl --context "${K8S_CLUSTER_0_CONTEXT_NAME}" apply -f -

   # add two buckets to the tenant config
   kubectl --context "${K8S_CLUSTER_0_CONTEXT_NAME}" -n "tenant-tiny" patch tenant/myminio \
     --type='json' \
     -p="[{\"op\": \"add\", \"path\": \"/spec/buckets\", \"value\": [{\"name\": \"${S3_OPLOG_BUCKET_NAME}\"}, {\"name\": \"${S3_SNAPSHOT_BUCKET_NAME}\"}]}]"

   kubectl --context "${K8S_CLUSTER_0_CONTEXT_NAME}" label namespace "tenant-tiny" istio-injection=enabled --overwrite
   ```

b. Before you configure and enable backup, create secrets:

   - `s3-access-secret` - contains S3 (Simple Storage Service) credentials.
   - `s3-ca-cert` - contains a CA (Certificate Authority) certificate that issued the bucket's
     server certificate. In the case of the sample MinIO deployment used
     in this procedure, the default Kubernetes Root CA (Certificate Authority) certificate
     is used to sign the certificate. Because it's not a publicly trusted
     CA (Certificate Authority) certificate, you must provide it so that Ops Manager can
     trust the connection.

   If you use publicly trusted certificates, you may skip this step and
   remove the values from the `spec.backup.s3Stores.customCertificateSecretRefs`
   and `spec.backup.s3OpLogStores.customCertificateSecretRefs` settings.

   ```bash
   kubectl --context "${K8S_CLUSTER_0_CONTEXT_NAME}" -n "${OM_NAMESPACE}" create secret generic s3-access-secret \
     --from-literal=accessKey="${S3_ACCESS_KEY}" \
     --from-literal=secretKey="${S3_SECRET_KEY}"

   # minio TLS secrets are signed with the default k8s root CA
   kubectl --context "${K8S_CLUSTER_0_CONTEXT_NAME}" -n "${OM_NAMESPACE}" create secret generic s3-ca-cert \
     --from-literal=ca.crt="$(kubectl --context "${K8S_CLUSTER_0_CONTEXT_NAME}" -n kube-system get configmap kube-root-ca.crt -o jsonpath="{.data.ca\.crt}")"
   ```

**Step 4: Re-deploy Ops Manager with backup enabled.**

a. The Kubernetes Operator can configure and deploy all components,
   the Ops Manager Application, the Backup Daemon instances, and the Application
   Database's replica set nodes in any combination on any member clusters
   for which you configure the Kubernetes Operator.

   To illustrate the flexibility of the multi-Kubernetes cluster deployment
   configuration, deploy only one Backup Daemon instance on the third
   member cluster and specify zero Backup Daemon members for the first
   and second clusters.

   ```bash
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
       type: LoadBalancer
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
         members: 1
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
           members: 3
         - clusterName: "${K8S_CLUSTER_1_CONTEXT_NAME}"
           members: 2
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

b. Wait until the Kubernetes Operator finishes its configuration:

   ```bash
   ```

   Output:

   ```
   ```

**Step 5: Create credentials for the Kubernetes Operator.**

To configure credentials, you must create an Ops Manager organization,
generate programmatic API keys in the Ops Manager UI, and create a [secret](https://kubernetes.io/docs/concepts/configuration/secret/) 
with your Load Balancer IP. See create-k8s-credentials to learn more.
