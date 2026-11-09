<!-- Converted from tutorial/recover-mcsc-yes-k8sop-cluster.txt (reStructuredText). Includes are inlined. -->

# Recover the Sharded Cluster if the Central Cluster Is Operational

If one of your Kubernetes clusters fails, but your central cluster is available, and each of your
MongoDB shard's replica sets and config server replica sets
maintain a voting majority, you can use the Kubernetes Operator to reconfigure 
deployments of the Sharded Cluster.

## Procedure

**Step 1: Remove the failed cluster from the `mongodb-kubernetes-operator-member-list`.**

1. When a member cluster is no longer operational, you must remove 
   it from the `mongodb-kubernetes-operator-member-list` configmap containing 
   the list of member clusters the Kubernetes Operator is managing. 

2. When you update the config map, the Kubernetes Operator restarts.

3. After the Kubernetes Operator restarts, without the failed member cluster in its 
   configuration, the multi-Kubernetes cluster MongoDB deployment custom resource referencing this 
   failed cluster in its `clusterSpecList` reconciles correctly. 

   Even though the failed member cluster is still referenced in the `clusterSpecList`,
   it is ignored during the reconciliation (other clusters are be reconciled 
   normally). However, the failed memeber's processes are not removed from Ops Manager. 
   Instead, they are ignored and shown in the Ops Manager UI as being in a down/stale state.

**Step 2: Manually scale down the replica set members in the failed cluster.**

In order to reconfigure the deployment, you must first manually 
scale down the replica set members deployed in the failed member clusters 
to `0`. To do so, you can either remove the whole cluster element from `clusterSpecList` element 
or specify its `members` count to `0`.

**Note:**

Sometimes it is not possible to correctly reconfigure the deployment 
when there are non-operational members of replica sets. In such a case, 
you must remove the failed processes first from both the shard and config 
server replica sets.

**Step 3: Reconfigure the deployment to its original state.**

After you've scaled the failed `members` counts to `0`, you can 
reconfigure the deployment to its original size by adding members on 
healthy Kubernetes clusters or by adding entirely new clusters as well.
