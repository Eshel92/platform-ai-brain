<!-- Converted from tutorial/om-resource-crd-parts.txt (reStructuredText). Includes are inlined. -->

# The `MongoDBOpsManager` Custom Resource Definition

The Kubernetes Operator manages Ops Manager deployments using the `MongoDBOpsManager`
[custom resource](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/) in each Kubernetes cluster where you deploy the resource.
The Kubernetes Operator watches the resource's specification for changes.
When the specification changes, the Kubernetes Operator validates the changes
and makes the appropriate updates to the resource in each of the Kubernetes
clusters where you deploy Ops Manager components.

`MongoDBOpsManager` [custom resource](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/)\s specification defines the
following Ops Manager components:

- The Application Database
- The Ops Manager application
- The Backup Daemon

The following diagram describes the related components for an Ops Manager
deployment:

- In single-cluster deployments, you deploy these components in the same Kubernetes
  cluster where you install the Kubernetes Operator. This cluster serves as
  the central cluster.
- In multi-cluster deployments, you:

  - Deploy each component in different Kubernetes clusters, known as
    member clusters.
    You can also deploy a simplified multi-cluster deployment with a single
    member Kubernetes cluster. To learn more, see mode-multi-or-single.
  - Install the Kubernetes Operator in one Kubernetes cluster, the central
    cluster, from where the Kubernetes Operator manages all other member
    clusters. The central cluster can also be considered a member
    cluster as it too can host the Ops Manager components.
    See Multi-Cluster Architecture Diagram.

(Figure: /images/meko-arch.svg)
      Enterprise Kubernetes Operator (single Kubernetes Cluster)
:figwidth: 600px

## Application Database

For the Application Database, the Kubernetes Operator deploys a MongoDB replica set
as a [StatefulSet](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/).

Each Pod for the Application Database has the following containers:

- `mongod`.
- MongoDB Agent. To override the MongoDB Agent version, use
  the `$AGENT_IMAGE` environment variable or `agent.version`
  in the Helm chart that you use for installing the Kubernetes Operator.
- Monitoring Agent. You can't override the Monitoring Agent\'s version.
  The version that the Kubernetes Operator uses ensures backwards compatibility
  with the Ops Manager versions.

  To view the Monitoring Agent\'s version:

  - Inspect `/usr/local/om_version_mapping.json` inside the Pod for
    the Kubernetes Operator or the image for the Kubernetes Operator.
  - Check the Monitoring Agent\'s container image on the Pod where you deploy
    the Application Database.

In multi-cluster deployments (when you set
`spec.applicationDatabase.topology` to `MultiCluster`),
the Kubernetes Operator creates the StatefulSet in each Kubernetes cluster specified
for the Application Database in `spec.applicationDatabase.clusterSpecList`.

The following actions take place in each member Kubernetes cluster hosting 
MongoDB replica set nodes for the Application Database:

- Kubernetes creates one Pod in the StatefulSet for each node that comprises
  your Application Database replica set. Each Pod in the StatefulSet runs
  a `mongod` and the MongoDB Agent.

  To enable each MongoDB Agent to start `mongod` on its Pod in the StatefulSet,
  you must specify a specific MongoDB Server version for the Application Database
  using the `spec.applicationDatabase.version` setting. The version
  that you specify in this setting must correspond to the tag in the
  `container registry`.
  
- Each MongoDB Agent starts `mongod`\s on its Application Database
  Pod. MongoDB Agent\'s add `mongod` processes to the Application Database replica set.

  You configure the number of replicas and other configuration options
  for the Application Database replica set in the `spec.applicationDatabase`
  collection in the `MongoDBOpsManager` custom resource. The Kubernetes Operator
  passes this configuration to the MongoDB Agent\'s using a [secret](https://kubernetes.io/docs/concepts/configuration/secret/) that the
  Kubernetes Operator mounts to each Pod in the Application Database StatefulSet.

  In multi-cluster Application Database deployments, (where `spec.applicationDatabase.topology`
  is set to `MultiCluster`), you specify the number of nodes in each member
  cluster separately for each member cluster in
  `spec.applicationDatabase.clusterSpecList`.
  In multi-cluster deployments, the `replicas` setting in
  `spec.applicationDatabase` is ignored.

- Each time that you update the `spec.applicationDatabase` collection,
  the Kubernetes Operator applies the changes to the MongoDB Agent configuration and
  the StatefulSet specification, if applicable. If the StatefulSet specification
  changes, Kubernetes upgrades the Pods in a rolling fashion and restarts each Pod.

- To provide connectivity to each Application Database Pod from within each
  Kubernetes cluster hosting the Application Database, the Kubernetes Operator creates
  a headless [service](https://kubernetes.io/docs/concepts/services-networking/service/).
  In multi-cluster deployments of the Application Database, the Kubernetes Operator
  also creates one service per Pod named `<om_resource_name>-db-N-svc` (this corresponds
  to `metadata.name`),
  and uses its FQDN (fully qualified domain name), such as `<om_resource_name>-db-0.<namespace>.svc.cluster.local`,
  as a hostname for connecting to a particular `mongod`.

- Depending on the [StorageClass](https://kubernetes.io/docs/concepts/storage/storage-classes/) or the environment to which you deploy the
  Kubernetes Operator, Kubernetes might create the [Persistent Volumes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/) using
  `dynamic volume provisioning`.

  You can customize the [Persistent Volume Claims](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims) for the Application Database Pods using
  `spec.applicationDatabase.podSpec.persistence.single`
  or `spec.applicationDatabase.podSpec.persistence.multiple`.

### Application Database Topology

To elect a primary, a majority of the Application Database replica set's
nodes must be available. If a majority of replica set's nodes fail,
the replica set can't form a voting majority to elect a primary node.
To learn more, see Replica Set Deployment Architectures.

If possible, use an odd number of member Kubernetes clusters and distribute your
Application Database nodes across data centers, zones, or Kubernetes clusters.
To learn more, see Replica Sets Distributed Across Two or More Data Centers.

Consider the following examples of the Application Database\'s topology:

**five-member:**

For a five-member Application Database, some possible distributions of members include:

- Two clusters: three members to `Cluster 1` and two members to `Cluster 2`.

  - If `Cluster 2` fails, `Cluster 1` hosts a sufficient number of
    Application Database\'s replica set members to elect a primary node.
  - If `Cluster 1` fails, `Cluster 2` doesn't have enough Application
    Database's members to elect a primary node.

- Three clusters: two members to `Cluster 1`, two members to `Cluster 2`, and one member to `Cluster 3`.

  - If any single cluster fails, there are enough members on the remaining clusters to elect a primary node.
  - If two clusters fail, there are not enough members on any remaining cluster to elect a primary node.

**seven-member:**

For a seven-member Application Database, consider the following distribution of members:

- Two clusters: four members to `Cluster 1` and three members to `Cluster 2`.

  - If `Cluster 2` fails, there are enough members on `Cluster 1` to elect a primary node.
  - If `Cluster 1` fails, there are not enough members on `Cluster 2` to elect a primary node.

Although `Cluster 2` meets the three member minimum for the Application Database,
a majority of the Application Database\'s seven members must be available
to elect a primary node.

To learn more, see disaster-recovery-om-appdb.

## Ops Manager Application

After the Application Database reaches a **Running** state, the Kubernetes Operator
starts deploying the Ops Manager Application:

- It configures a StatefulSet on each member Kubernetes cluster.
- For each Ops Manager replica set that you want to deploy, Kubernetes creates one Pod
  in the StatefulSet.
- Each Pod contains one Ops Manager Application process.

To make your single cluster Ops Manager deployment resilient to single Pod
failures, increase the number of replicas hosting the Ops Manager Application,
using `spec.replicas`.

To make your multi-cluster Ops Manager deployment resilient to entire data
center or zone failures, deploy the Ops Manager Application in multiple Kubernetes clusters
by setting `spec.topology` and `spec.applicationDatabase.topology`
to `MultiCluster`. See also disaster-recovery-om-appdb.

## Backup Daemon

If `spec.backup.enabled` is **true**, then on each member
Kubernetes cluster, the Kubernetes Operator starts the Backup Daemon after
the Ops Manager Application reaches a **Running** stage. For the Backup Daemon,
the Kubernetes Operator deploys a StatefulSet to each member Kubernetes cluster.
In each member cluster, Kubernetes creates as many Backup Daemon Pods in the
StatefulSet as specified in `spec.backup.members`.
In single cluster deployments, these actions take place on the operator
cluster that you use for installing the Kubernetes Operator and deploying the
Ops Manager components.

If you enable backup, configure the oplog store,
a blockstore,
or an S3 (Simple Storage Service) snapshot store at the global
`spec.backup` level, and not for each Kubernetes member cluster.

You can also encrypt backup jobs,
but limitations apply to deployments where the
same  Kubernetes Operator instance is not managing both the
MongoDBOpsManager and MongoDB
custom resources.

If you enable backup, the Kubernetes Operator creates a [Persistent Volume Claim](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims) for the
Backup Daemon's head database on each member Kubernetes cluster.
You can configure the head database using the `spec.backup.headDB`
setting.

The Kubernetes Operator invokes Ops Manager APIs to ensure that the Ops Manager Application\'s
backup configuration matches the one that you define in the custom resource
definitions for each member Kubernetes cluster.
