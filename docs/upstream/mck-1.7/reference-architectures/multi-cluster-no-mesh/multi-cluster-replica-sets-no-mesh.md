<!-- Converted from reference-architectures/multi-cluster-no-mesh/multi-cluster-replica-sets-no-mesh.txt (reStructuredText). Includes are inlined. -->

# Multi-Cluster ReplicaSets Without a Service Mesh

Multi-Kubernetes cluster MongoDB deployments allow you to add MongoDB instances in global clusters
that span multiple geographic regions for increased availability and
global distribution of data.

## Prerequisites

Before you begin the following procedure, perform the following actions:

- Install `kubectl`.
- Install [Mongosh](https://www.mongodb.com/docs/mongodb-shell/install/)
- Complete the GKE Clusters procedure or the equivalent.
- Complete the External DNS procedure or the equivalent.
- Complete the TLS Certificates procedure or the equivalent.
- Complete the Deploy the MongoDB Operator procedure.
- Complete the Multi-Cluster Ops Manager procedure procedure.
  You can skip this step if you use Cloud Manager instead of Ops Manager.
- Set the required environment variables as follows:

```bash
# This script builds on top of the environment configured in the setup guides.
# It depends (uses) the following env variables defined there to work correctly.
# If you don't use the setup guide to bootstrap the environment, then define them here.
#  ${K8S_CLUSTER_0_CONTEXT_NAME}
#  ${K8S_CLUSTER_1_CONTEXT_NAME}
#  ${K8S_CLUSTER_2_CONTEXT_NAME}
#  ${MDB_NAMESPACE}
#  ${CUSTOM_DOMAIN}

export RS_RESOURCE_NAME=mdb
export MONGODB_VERSION="8.0.5-ent"

export MDB_CLUSTER_0_EXTERNAL_DOMAIN="${K8S_CLUSTER_0}.${CUSTOM_DOMAIN}"
export MDB_CLUSTER_1_EXTERNAL_DOMAIN="${K8S_CLUSTER_1}.${CUSTOM_DOMAIN}"
export MDB_CLUSTER_2_EXTERNAL_DOMAIN="${K8S_CLUSTER_2}.${CUSTOM_DOMAIN}"
```

## Source Code

You can find all included source code in the MongoDB Kubernetes Operator repository.

## Procedure

**Step 1: Create a CA certificate.**

Run the following script to create the required CA Certificate with your 
certificate issuer. 

```bash
kubectl apply --context "${K8S_CLUSTER_0_CONTEXT_NAME}" -n "${MDB_NAMESPACE}" -f - <<EOF
apiVersion: cert-manager.io/v1
kind: Certificate
metadata:
  name: mdb-cert
spec:
  dnsNames:
  - "*.${MDB_CLUSTER_0_EXTERNAL_DOMAIN}"
  - "*.${MDB_CLUSTER_1_EXTERNAL_DOMAIN}"
  - "*.${MDB_CLUSTER_2_EXTERNAL_DOMAIN}"
  duration: 240h0m0s
  issuerRef:
    name: my-ca-issuer
    kind: ClusterIssuer
  renewBefore: 120h0m0s
  secretName: cert-prefix-mdb-cert
  usages:
  - server auth
  - client auth
EOF
```

**Step 2: Deploy the `MongoDBMultiCluster` resource.**

Set `spec.credentials`, `spec.opsManager.configMapRef.name`, 
which you defined in the reference-architectures-multi-cluster-ops-manager-no-mesh procedure;
define your security settings and deploy the `MongoDBMultiCluster` resource.

```bash
kubectl apply --context "${K8S_CLUSTER_0_CONTEXT_NAME}" -n "${MDB_NAMESPACE}" -f - <<EOF
apiVersion: mongodb.com/v1
kind: MongoDBMultiCluster
metadata:
  name: ${RS_RESOURCE_NAME}
spec:
  type: ReplicaSet
  version: ${MONGODB_VERSION}
  opsManager:
    configMapRef:
      name: mdb-org-project-config
  credentials: mdb-org-owner-credentials
  duplicateServiceObjects: false
  persistent: true
  backup:
    mode: enabled
  security:
    certsSecretPrefix: cert-prefix
    tls:
      ca: ca-issuer
    authentication:
      enabled: true
      modes: ["SCRAM"]
  clusterSpecList:
    - clusterName: ${K8S_CLUSTER_0_CONTEXT_NAME}
      members: 2
      externalAccess:
        externalDomain: "${MDB_CLUSTER_0_EXTERNAL_DOMAIN}"
        externalService:
          annotations:
             external-dns.alpha.kubernetes.io/hostname: "{podName}.${MDB_CLUSTER_0_EXTERNAL_DOMAIN}"
    - clusterName: ${K8S_CLUSTER_1_CONTEXT_NAME}
      members: 1
      externalAccess:
        externalDomain: "${MDB_CLUSTER_1_EXTERNAL_DOMAIN}"
        externalService:
          annotations:
             external-dns.alpha.kubernetes.io/hostname: "{podName}.${MDB_CLUSTER_1_EXTERNAL_DOMAIN}"
    - clusterName: ${K8S_CLUSTER_2_CONTEXT_NAME}
      members: 2
      externalAccess:
        externalDomain: "${MDB_CLUSTER_2_EXTERNAL_DOMAIN}"
        externalService:
          annotations:
             external-dns.alpha.kubernetes.io/hostname: "{podName}.${MDB_CLUSTER_2_EXTERNAL_DOMAIN}"
EOF
```

**Step 3: Verify that the `MongoDBMultiCluster` resource is running.**

Run the following command to confirm that the `MongoDBMultiCluster` resource is running. 

```bash
echo; echo "Waiting for MongoDB to reach Running phase..."
kubectl --context "${K8S_CLUSTER_0_CONTEXT_NAME}" -n "${MDB_NAMESPACE}" wait --for=jsonpath='{.status.phase}'=Running "mdbmc/${RS_RESOURCE_NAME}" --timeout=900s
echo; echo "Pods running in cluster ${K8S_CLUSTER_0_CONTEXT_NAME}"
kubectl --context "${K8S_CLUSTER_0_CONTEXT_NAME}" -n "${MDB_NAMESPACE}" get pods
echo; echo "Pods running in cluster ${K8S_CLUSTER_1_CONTEXT_NAME}"
kubectl --context "${K8S_CLUSTER_1_CONTEXT_NAME}" -n "${MDB_NAMESPACE}" get pods
echo; echo "Pods running in cluster ${K8S_CLUSTER_2_CONTEXT_NAME}"
kubectl --context "${K8S_CLUSTER_2_CONTEXT_NAME}" -n "${MDB_NAMESPACE}" get pods
```

**Step 4: Create a MongoDB user and password.**

Run the following command to create a MongoDB user and password. Please use strong passwords for your deployments.

```bash
kubectl apply --context "${K8S_CLUSTER_0_CONTEXT_NAME}" -n "${MDB_NAMESPACE}" -f - <<EOF
apiVersion: v1
kind: Secret
metadata:
  name: rs-user-password
type: Opaque
stringData:
  password: password
---
apiVersion: mongodb.com/v1
kind: MongoDBUser
metadata:
  name: rs-user
spec:
  passwordSecretKeyRef:
    name: rs-user-password
    key: password
  username: "rs-user"
  db: "admin"
  mongodbResourceRef:
    name: ${RS_RESOURCE_NAME}
  roles:
  - db: "admin"
    name: "root"
EOF

kubectl --context "${K8S_CLUSTER_0_CONTEXT_NAME}" wait --for=jsonpath='{.status.phase}'=Updated -n "${MDB_NAMESPACE}" mdbu/rs-user --timeout=300s
```

**Step 5: Verify connectivity.**

Run the `mongosh` following command to ensure that you can access your running MongoDB instance.

```bash
```

Output:

```
```
