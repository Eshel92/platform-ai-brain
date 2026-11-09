<!-- Converted from multi-cluster-disaster-recovery.txt (reStructuredText). Includes are inlined. -->

# Disaster Recovery

The Kubernetes Operator can orchestrate the recovery of MongoDB replica set
members to a healthy Kubernetes cluster when the Kubernetes Operator identifies
that the original Kubernetes cluster is down.

## Disaster Recovery Modes

The Kubernetes Operator can orchestrate either an automatic or manual remediation
of the `MongoDBMultiCluster` resources in a disaster recovery scenario, using one of the following modes:

- **Auto Failover Mode** allows the Kubernetes Operator to shift the affected
  MongoDB replica set members from an unhealthy Kubernetes cluster to healthy
  Kubernetes clusters. When the Kubernetes Operator performs this auto remediation,
  it evenly distributes replica set members across the healthy Kubernetes clusters.
  
  To enable this mode, use `--set multiCluster.performFailover=true` in
  the MongoDB Helm Charts for Kubernetes. In the `values.yaml` file in the
  [MongoDB Helm Charts for Kubernetes](https://mongodb.github.io/helm-charts) directory,
  the environment's variable default value is `true`.

  Alternatively, you can set the multi-Kubernetes cluster MongoDB deployment environment variable
  `PERFORM_FAILOVER` to `true`, as in the following abbreviated example:

  ```yaml
  spec:
    template:
      ...
      spec:
        containers:
        - name: mongodb-kubernetes-operator
          ...
          env:
          ...   
          - name: PERFORM_FAILOVER
            value: "true"
          ...
  ```

  

- **Manual(plugin-based) Failover Mode** allows you to use the
  MongoDB kubectl plugin to
  reconfigure the Kubernetes Operator to use new healthy Kubernetes clusters.
  In this mode, you distribute replica set members across the new healthy
  clusters by configuring the `MongoDBMultiCluster` resource based on your configuration.

  To enable this mode, use `--set multiCluster.performFailover=true`
  in the [MongoDB Helm Charts for Kubernetes](https://mongodb.github.io/helm-charts),
  or set the multi-Kubernetes cluster MongoDB deployment environment variable `PERFORM_FAILOVER`
  to `false`, as in the following abbreviated example:

  ```yaml
  spec:
    template:
      ...
      spec:
        containers:
        - name: mongodb-kubernetes-operator
          ...
          env:
          ...   
          - name: PERFORM_FAILOVER
            value: "false"
          ...
  ```

**Note:**

You can't rely on the auto or manual failover modes
when a Kubernetes cluster hosting one or more Kubernetes Operator instances goes
down, or the replica set member resides on the same failed Kubernetes
cluster as the Kubernetes that manages it.

In such cases, to restore replica set members from lost Kubernetes clusters
to the remaining healthy Kubernetes clusters, you must first restore the
Kubernetes Operator instance that manages your multi-Kubernetes cluster MongoDB deployments, or
redeploy the Kubernetes Operator to one of the remaining Kubernetes clusters,
and rerun the `kubectl mongodb` plugin. To learn more, see disaster-recovery-manual.

## Manually Recover from a Failure Using the MongoDB Plugin

When a Kubernetes cluster hosting one or more Kubernetes Operator instances goes down,
or the replica set member resides on the same failed Kubernetes cluster as the
Kubernetes that manages it, you can't rely on the
auto or manual failover modes
and must use the following procedure to manually recover from a failed
Kubernetes cluster.

The following procedure uses the MongoDB kubectl Plugin
to:

- Configure new healthy Kubernetes clusters.
- Add these Kubernetes clusters as new member clusters to the `mongodb-kubernetes-operator-member-list`
  ConfigMap for your multi-Kubernetes cluster MongoDB deployment.
- Rebalance nodes hosting `MongoDBMultiCluster` resources on the nodes in the healthy Kubernetes clusters.

The following tutorial for manual disaster recovery assumes that you:

- Deployed one central cluster and three member clusters, following the
  multi-cluster-quick-start-ref. In this case, the
  Kubernetes Operator is installed with the automated failover disabled with
  `--set multiCluster.performFailover=false`.

- Deployed a `MongoDBMultiCluster` resource as follows:

  ```sh
  kubectl apply -n mongodb -f - <<EOF
  apiVersion: mongodb.com/v1
  kind: MongoDBMultiCluster
  metadata:
   name: multi-replica-set
  spec:
   version: 8.0.0
   type: ReplicaSet
   persistent: false
   duplicateServiceObjects: true
   credentials: my-credentials
   opsManager:
     configMapRef:
       name: my-project
   security:
     tls:
       ca: custom-ca
   clusterSpecList:
     - clusterName: ${MDB_CLUSTER_1_FULL_NAME}
       members: 3
     - clusterName: ${MDB_CLUSTER_2_FULL_NAME}
       members: 2
     - clusterName: ${MDB_CLUSTER_3_FULL_NAME}
       members: 3
  EOF
  ```

The Kubernetes Operator periodically checks for connectivity to the clusters
in the multi-Kubernetes cluster MongoDB deployment by pinging the `/readyz` endpoints of the
corresponding servers. To learn more about `/readyz`, see the [Kubernetes API health endpoints](https://kubernetes.io/docs/reference/using-api/health-checks/).

In the case that `CLUSTER_3` in our example becomes unavailable, the
Kubernetes Operator detects the failed connections to the cluster and marks the
`MongoDBMultiCluster` resources with the `failedClusters` annotation for subsequent reconciliations.

The resources with data nodes deployed on this cluster fail reconciliation
until you run the manual recovery steps as in the following procedure.

To rebalance the MongoDB data nodes so that all the workloads run on
`CLUSTER_1` and `CLUSTER_2`:

**Step 1: Recover the multi-Kubernetes cluster MongoDB deployment using the MongoDB kubectl plugin.**

```sh
kubectl mongodb multicluster recover \
  --central-cluster="MDB_CENTRAL_CLUSTER_FULL_NAME" \
  --member-clusters="${MDB_CLUSTER_1_FULL_NAME},${MDB_CLUSTER_2_FULL_NAME}" \
  --member-cluster-namespace="mongodb" \
  --central-cluster-namespace="mongodb" \
  --operator-name=mongodb-kubernetes-operator-multi-cluster \
  --source-cluster="${MDB_CLUSTER_1_FULL_NAME}"
```

This command:

- Reconfigures the Kubernetes Operator to manage workloads on the two healthy
  Kubernetes clusters. (This list could also include new Kubernetes clusters).

- Marks `CLUSTER_1` as the source of configuration for the member node
  configuration for new Kubernetes clusters. Replicates Role and Service Account
  configuration to match the configuration in `CLUSTER_1`.

**Step 2: Rebalance the data nodes on the healthy Kubernetes clusters.**

Reconfigure the `MongoDBMultiCluster` resource to rebalance the data nodes on the healthy
Kubernetes clusters by editing the resources affected by the change:

```yaml
kubectl apply -n mongodb -f - <<EOF
apiVersion: mongodb.com/v1
kind: MongoDBMultiCluster
metadata:
  name: multi-replica-set
spec:
  version: 8.0.0
  type: ReplicaSet
  persistent: false
  duplicateServiceObjects: true
  credentials: my-credentials
  opsManager:
    configMapRef:
      name: my-project
 security:
   tls:
     ca: custom-ca
 clusterSpecList:
   - clusterName: ${MDB_CLUSTER_1_FULL_NAME}
     members: 4
   - clusterName: ${MDB_CLUSTER_2_FULL_NAME}
     members: 3
 EOF
```

## Manually Recover from a Failure Using GitOps Workflows

For an example of use of the MongoDB kubectl plugin
in a GitOps workflow with [Argo CD](https://argoproj.github.io/cd), see
multi-cluster plugin example for GitOps.

GitOps recovery requires manual reconfiguration of
`Role Based Access Control`
using `.yaml` resource files. To learn more, see
multi-cluster-rbac-manual.
