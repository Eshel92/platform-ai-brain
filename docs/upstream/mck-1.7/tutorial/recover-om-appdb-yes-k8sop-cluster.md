<!-- Converted from tutorial/recover-om-appdb-yes-k8sop-cluster.txt (reStructuredText). Includes are inlined. -->

# Recover Ops Manager and AppDB if the Central Cluster Works

If Kubernetes clusters running the Ops Manager Application instances or Application Database nodes
fail, but the central cluster is
available, you can use the
Kubernetes Operator to reconfigure deployments of the Application Database\'s replica
set and the Ops Manager Application instances based on the following scenarios:

- If some or all Ops Manager Application instances fail, no data is lost because the
  Ops Manager Application is stateless. To increase the availability of the Ops Manager Application,
  add new Ops Manager Application instances to already configured and available Kubernetes member
  clusters, or add new Kubernetes clusters for running the Ops Manager Application instances.

- If only a minority of replica set's nodes fail and the majority of nodes
  in a replica set are available, during the reconciliation process, the
  Kubernetes Operator ignores the failed Kubernetes clusters and the Application Database
  remains in a writable state.

  Use the `spec.applicationDatabase.clusterSpecList` settings
  to add Application Database\'s replica set nodes to already configured and
  available member Kubernetes clusters, or add new Kubernetes clusters on which
  you deploy Application Database\'s failed replica set members.
  You can also scale down the replica set's nodes on a failed Kubernetes cluster
  to reconfigure the replica set to not contain these nodes anymore.

- If a majority of replica set's nodes fail, the replica set can't form
  a voting majority to elect a primary node. To learn more, see
  Replica Set Deployment Architectures.
  In this case, if at least one node in an Application Database\'s replica set
  remains available, then no data is lost. Because there is no primary node
  in a replica set, you must
  forcibly reconfigure the replica set
  to add new replica set nodes. The nodes will form a voting majority allowing
  the replica set to elect a primary. New Application Database instances will sync with
  the healthy nodes to receive the data.

- If all Kubernetes member clusters hosting the Application Database\'s replica set
  nodes fail, this causes an irreversible data loss (Ops Manager doesn't back
  up the Application Database). If possible, use an odd number of member
  Kubernetes clusters and distribute your Application Database nodes across
  data centers, zones, or Kubernetes clusters. To learn more, see Replica Sets Distributed Across Two or More Data Centers.
