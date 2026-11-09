<!-- Converted from tutorial/recover-appdb-forced-reconfig.txt (reStructuredText). Includes are inlined. -->

# Recover the Application Database if its Replica Set Loses Majority

If the Kubernetes member clusters fail and the Application Database
loses a majority of replica set's nodes available to elect a primary,
the Kubernetes Operator doesn't automatically trigger a forced replica set reconfiguration.
You must manually initiate a forced replica set reconfiguration and restore
the Application Database replica set to a healthy state.

## Overview

In certain severe Kubernetes cluster outages your Application Database\'s
replica set deployment could lose the majority of the replica set's nodes.
For example, if you have an Application Database deployment with two nodes
in `cluster 1` and three nodes in `cluster 2`, and `cluster 2` undergoes
an outage, your Application Database\'s replica set deployment will lose the
node majority needed to elect a primary. Without a primary, the MongoDB Agent
can't reconfigure a replica set.

To enable rescheduling replica set's nodes, the Kubernetes Operator must forcibly
reconfigure the `Automation Configuration`
for the MongoDB Agent to enable deploying replica set nodes in the remaining
healthy member clusters.
To achieve this, the Kubernetes Operator sets
the `replicaSets[n].force`
flag in the replica set configuration.
The flag instructs the MongoDB Agent to force a replica set to use the
current (latest) `Automation Configuration version`.
Using the flag allows the Kubernetes Operator to reconfigure the replica set in
case a primary node isn't elected.

**Important:**

Forced reconfiguration of the Application Database can result in undesired behavior,
including rollback
of "majority"
committed writes, which could lead to an unexpected data loss.

## Recover the Application Database through a Forced Reconfiguration

To perform a forced reconfiguration of the Application Database\'s nodes:

1. Change the `spec.applicationDatabase.clusterSpecList` configuration
   settings to reconfigure the Application Database\'s deployment on healthy
   Kubernetes clusters to allow the replica set to form a majority of healthy nodes.

2. Scale failed Kubernetes member clusters down to zero nodes and then remove
   those clusters from the `spec.applicationDatabase.clusterSpecList`.
   Removing an entry without scaling it down first isn't supported. This
   ensures the replica set doesn't count the Application Database\'s nodes hosted on
   those clusters as voting members of the replica set. For example, having
   two healthy nodes in `cluster 1` and a failed `cluster 2` containing
   3 nodes, you have two healthy nodes from a total of five replica set
   members (2/5 healthy). Adding one node to `cluster 1` results in
   having 3/6 ratio of healthy nodes to the number of members in the
   replica set. To form a replica set majority, you have the following
   options:

   - Add at least two new replica set nodes to `cluster 1`, or a new
     healthy Kubernetes cluster. This achieves a majority (4/7), with four nodes
     in a seven-member replica set.
   - Scale down a failed Kubernetes cluster to zero nodes, remove the cluster
     from the `spec.applicationDatabase.clusterSpecList`, and
     add at least one node to `cluster 1` to have 3/3 healthy nodes in the
     replica set's StatefulSet.

3. Add the annotation `"mongodb.com/v1.forceReconfigure": "true"` at
   the top level of the `MongoDBOpsManager` custom resource and ensure
   that the value `"true"` is a string in quotes. 

   Based on this annotation, the Kubernetes Operator performs a forced reconfiguration
   of the replica set in the next reconciliation process and scales
   the Application Database\'s replica set nodes according to the changed
   deployment configuration.

   The Kubernetes Operator has no means to determine whether the nodes in the
   failed Kubernetes cluster are healthy. Therefore, if the Kubernetes Operator
   can't connect to the failed member Kubernetes cluster's API server, the
   Kubernetes Operator ignores the cluster during the reconciliation process
   of the Application Database\'s replica set nodes.

   This means that scaling down of the Application Database nodes removes
   failed processes from the replica set configuration.
   In cases when only the API server is down, but the replica set's nodes
   are running, the Kubernetes Operator doesn't remove the Pods from the failed
   Kubernetes clusters.

   To indicate that it completed the forced reconfiguration, the Kubernetes Operator
   adds the annotation key, `"mongodb.com/v1.forceReconfigurePerformed"`,
   with the current timestamp as the value.

   **Important:**

   The Kubernetes Operator performs only one forced reconfiguration of the
   replica set. After the replica set reaches a running state, the
   Kubernetes Operator adds the `"mongodb.com/v1.forceReconfigurePerformed"`
   annotation to prevent itself from forcing the reconfiguration again
   in the future. Therefore, to re-trigger a new forced reconfiguration
   event, remove one or both of the following annotations from the resource,
   in the `metadata.annotations`
   for the `MongoDBOpsManager` custom resource.

   - `"mongodb.com/v1.forceReconfigurePerformed"`
   - `"mongodb.com/v1.forceReconfigure"`

4. Reapply the configuration for the changed `MongoDBOpsManager` custom resource
   in the Kubernetes Operator.
