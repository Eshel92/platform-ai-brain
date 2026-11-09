<!-- Converted from reference-architectures/multi-cluster/multi-cluster-sharded-cluster.txt (reStructuredText). Includes are inlined. -->

# Multi-Cluster Sharded Cluster

You can distribute MongoDB Sharded Clusters over
multiple Kubernetes Clusters. With multi-cluster functionality, you can:

- Improve the resilience of your deployment by distributing it across multiple
  Kubernetes clusters, each in a different geographic region.
- Configure your deployment for geo sharding by deploying primary nodes of
  specified shards in different Kubernetes clusters that are located closer to the
  application or clients that depend on that data, reducing latency.
- Tune your deployment for improved performance. For example, you can deploy
  read-only analytical nodes for all or specified shards in different
  Kubernetes clusters or with customized resource allocations.

## Prerequisites

Before you begin the following procedure, perform the following actions:

- Install `kubectl`.
- Install [Mongosh](https://www.mongodb.com/docs/mongodb-shell/install/)
- Complete the GKE Clusters procedure or the equivalent.
- Complete the TLS Certificates procedure or the equivalent.
- Complete the Istio Service mesh procedure or the equivalent.
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

export SC_RESOURCE_NAME=mdb-sh
export MONGODB_VERSION="8.0.5-ent"
```

## Source Code

You can find all included source code in the [MongoDB Kubernetes Operator repository](https://github.com/mongodb/mongodb-kubernetes/tree/1.7.0/public/architectures/ra-08-mongodb-sharded-multi-cluster).

## Procedure

**Step 1: Generate TLS certificates.**

Run the following command to generate the required TLS certificates for
each shard, your mongos, and your config servers.

```bash
kubectl apply --context "${K8S_CLUSTER_0_CONTEXT_NAME}" -n "${MDB_NAMESPACE}" -f - <<EOF
apiVersion: cert-manager.io/v1
kind: Certificate
metadata:
  name: mdb-sh-cert
spec:
  dnsNames:
  - "*.${MDB_NAMESPACE}.svc.cluster.local"
  duration: 240h0m0s
  issuerRef:
    name: my-ca-issuer
    kind: ClusterIssuer
  renewBefore: 120h0m0s
  secretName: cert-prefix-mdb-sh-cert
  usages:
  - server auth
  - client auth
---
apiVersion: cert-manager.io/v1
kind: Certificate
metadata:
  name: mdb-sh-0-cert
spec:
  dnsNames:
  - "*.${MDB_NAMESPACE}.svc.cluster.local"
  duration: 240h0m0s
  issuerRef:
    name: my-ca-issuer
    kind: ClusterIssuer
  renewBefore: 120h0m0s
  secretName: cert-prefix-mdb-sh-0-cert
  usages:
  - server auth
  - client auth
---
apiVersion: cert-manager.io/v1
kind: Certificate
metadata:
  name: mdb-sh-1-cert
spec:
  dnsNames:
  - "*.${MDB_NAMESPACE}.svc.cluster.local"
  duration: 240h0m0s
  issuerRef:
    name: my-ca-issuer
    kind: ClusterIssuer
  renewBefore: 120h0m0s
  secretName: cert-prefix-mdb-sh-1-cert
  usages:
  - server auth
  - client auth
---
apiVersion: cert-manager.io/v1
kind: Certificate
metadata:
  name: mdb-sh-2-cert
spec:
  dnsNames:
  - "*.${MDB_NAMESPACE}.svc.cluster.local"
  duration: 240h0m0s
  issuerRef:
    name: my-ca-issuer
    kind: ClusterIssuer
  renewBefore: 120h0m0s
  secretName: cert-prefix-mdb-sh-2-cert
  usages:
  - server auth
  - client auth
---
apiVersion: cert-manager.io/v1
kind: Certificate
metadata:
  name: mdb-sh-config-cert
spec:
  dnsNames:
  - "*.${MDB_NAMESPACE}.svc.cluster.local"
  duration: 240h0m0s
  issuerRef:
    name: my-ca-issuer
    kind: ClusterIssuer
  renewBefore: 120h0m0s
  secretName: cert-prefix-mdb-sh-config-cert
  usages:
  - server auth
  - client auth
---
apiVersion: cert-manager.io/v1
kind: Certificate
metadata:
  name: mdb-sh-mongos-cert
spec:
  dnsNames:
  - "*.${MDB_NAMESPACE}.svc.cluster.local"
  duration: 240h0m0s
  issuerRef:
    name: my-ca-issuer
    kind: ClusterIssuer
  renewBefore: 120h0m0s
  secretName: cert-prefix-mdb-sh-mongos-cert
  usages:
  - server auth
  - client auth
EOF
```

**Step 2: Deploy a MongoDB custom resource.**

Run the following command to deploy your custom resources.

```bash
kubectl apply --context "${K8S_CLUSTER_0_CONTEXT_NAME}" -n "${MDB_NAMESPACE}" -f - <<EOF
apiVersion: mongodb.com/v1
kind: MongoDB
metadata:
  name: ${SC_RESOURCE_NAME}
spec:
  shardCount: 3
  # we don't specify mongodsPerShardCount, mongosCount and configServerCount as they don't make sense for multi-cluster
  topology: MultiCluster
  type: ShardedCluster
  version: ${MONGODB_VERSION}
  opsManager:
    configMapRef:
      name: mdb-org-project-config
  credentials: mdb-org-owner-credentials
  persistent: true
  backup:
    mode: enabled
  externalAccess: {}
  security:
    certsSecretPrefix: cert-prefix
    tls:
      ca: ca-issuer
    authentication:
      enabled: true
      modes: ["SCRAM"]
  mongos:
    clusterSpecList:
      - clusterName: ${K8S_CLUSTER_0_CONTEXT_NAME}
        members: 2
  configSrv:
    clusterSpecList:
      - clusterName: ${K8S_CLUSTER_0_CONTEXT_NAME}
        members: 3 # config server will have 3 members in main cluster
      - clusterName: ${K8S_CLUSTER_1_CONTEXT_NAME}
        members: 1 # config server will have additional non-voting, read-only member in this cluster
        memberConfig:
          - votes: 0
            priority: "0"
  shard:
    clusterSpecList:
      - clusterName: ${K8S_CLUSTER_0_CONTEXT_NAME}
        members: 3 # each shard will have 3 members in this cluster
      - clusterName: ${K8S_CLUSTER_1_CONTEXT_NAME}
        members: 1 # each shard will have additional non-voting, read-only member in this cluster
        memberConfig:
          - votes: 0
            priority: "0"
EOF
```

**Step 3: Wait for the resources to spin up.**

Run the following command to confirm that all resources are up and running.

```bash
echo; echo "Waiting for MongoDB to reach Running phase..."
kubectl --context "${K8S_CLUSTER_0_CONTEXT_NAME}" -n "${MDB_NAMESPACE}" wait --for=jsonpath='{.status.phase}'=Running "mdb/${SC_RESOURCE_NAME}" --timeout=900s
echo; echo "Pods running in cluster ${K8S_CLUSTER_0_CONTEXT_NAME}"
kubectl --context "${K8S_CLUSTER_0_CONTEXT_NAME}" -n "${MDB_NAMESPACE}" get pods
echo; echo "Pods running in cluster ${K8S_CLUSTER_1_CONTEXT_NAME}"
kubectl --context "${K8S_CLUSTER_1_CONTEXT_NAME}" -n "${MDB_NAMESPACE}" get pods
echo; echo "Pods running in cluster ${K8S_CLUSTER_2_CONTEXT_NAME}"
kubectl --context "${K8S_CLUSTER_2_CONTEXT_NAME}" -n "${MDB_NAMESPACE}" get pods
```

**Step 4: Create a MongoDB user and credentials.**

Run the following command to create a user and credentials in your sharded cluster.

```bash
kubectl apply --context "${K8S_CLUSTER_0_CONTEXT_NAME}" -n "${MDB_NAMESPACE}" -f - <<EOF
apiVersion: v1
kind: Secret
metadata:
  name: sc-user-password
type: Opaque
stringData:
  password: password
---
apiVersion: mongodb.com/v1
kind: MongoDBUser
metadata:
  name: sc-user
spec:
  passwordSecretKeyRef:
    name: sc-user-password
    key: password
  username: "sc-user"
  db: "admin"
  mongodbResourceRef:
    name: ${SC_RESOURCE_NAME}
  roles:
  - db: "admin"
    name: "root"
EOF

kubectl --context "${K8S_CLUSTER_0_CONTEXT_NAME}" wait --for=jsonpath='{.status.phase}'=Updated -n "${MDB_NAMESPACE}" mdbu/sc-user --timeout=300s
```

**Step 5: Verify connectivity with the MongoDB Shell.**

Run the following command to verify that your MongoDB resource in your sharded cluster is accessible.

```bash
```

Output:

```
```
