<!-- Converted from tutorial/deploy-sharded-cluster.txt (reStructuredText). Includes are inlined. -->

# Deploy a Sharded Cluster

Sharded clusters provide horizontal scaling
for large data sets and enable high throughput operations by
distributing the data set across a group of servers.

To learn more about sharding, see
Sharding Introduction in the
MongoDB manual.

Use this procedure to deploy a new sharded cluster that Ops Manager manages.
Later, you can use Ops Manager to add shards and perform other maintenance
operations on the cluster.

**Note:** Added in Ops Manager 4.0

You can use Kubernetes to deploy MongoDB instances with
Ops Manager version 4.0 or later. 

To learn how to deploy a sharded cluster using a Kubernetes object, see
`Deploy a Sharded Cluster` in
the MongoDB Enterprise Kubernetes Operator documentation.

## Prerequisites

To deploy MongoDB clusters, you must
provision hosts to serve those
clusters. Ops Manager requires access to these hosts.

**Important:**

If you run `MongoDB Enterprise`
and provision your own Linux hosts, then you must manually install a
set of dependencies to each server **before installing MongoDB**.
The MongoDB manual provides the appropriate command to install the
dependencies.

To learn more about the specifics for an operating system, see the
following:

- Red Hat

- Ubuntu

- Debian

- SUSE

- Amazon AMI

## Considerations

### Unique Names for Sharded Clusters

Use unique names for the new cluster and its shards.

**Important:**

Replica set, sharded cluster, and shard names within the same
project must be unique. Failure to have unique names for the
deployments will result in broken backup snapshots.

### Do Not Deploy Monitoring Agents inside and outside Kubernetes

Do not mix MongoDB deployments outside Kubernetes with ones inside Kubernetes
in the same Project.

Due to Kubernetes network translation, a Monitoring Agent outside Kubernetes
cannot monitor MongoDB instances inside Kubernetes. For this reason, k8s
and non-k8s deployments in the same Project is not supported. Use
separate projects.

### Configuration Server Deployment Architecture

**New in version:** Ops Manager 4.0

Starting with MongoDB 3.2 or later versions of configuration
server `mongod` processes, Ops Manager deploys your configuration servers
as a replica set.

To learn more about CSRS (Config Servers as Replica Sets) and mirrored configuration servers (SCCC (Sync Cluster Connection Configuration)),
see Config Servers.

### Removing a Shard

When you remove a shard, any unsharded databases in that shard are 
moved to a remaining shard using the 
movePrimary command.

All sharded collections remain online and available during the shard 
removal process. However, read and write operations sent to unsharded 
collections during the `movePrimary` operation can result in 
unexpected behavior, including failure of the migration or loss of 
data.

We recommend moving the primary shard for any databases containing 
unsharded collections before removing the shard.

To learn more about removing shards, see 
Remove Shards from an Existing Sharded Cluster.

## Procedure

**Step 1: Navigate to the Deployment page for your project.**

a. If it is not already displayed, select the organization that
   contains your desired project from the `office` Organizations menu in the
   navigation bar.

#. If it is not already displayed, select your desired project
   from the Projects menu in the navigation bar.

#. If it is not already displayed, click Deployment in 
   the sidebar.

**Step 2: Open the Cluster Creation View.**

Click the Add arrow in the top-right of the
Deployment page. Select New Cluster
from the drop-down menu to open the Create New Cluster
view.

**Step 3: Configure Cluster-Wide Settings.**

The Cluster Configuration section contains the following
cluster-wide configuration settings. Settings marked with an
* asterisk in the  Ops Manager UI are **required**.

| Setting | Description |
|---|---|
| Cluster Name | .. include:: /includes/extracts/deploy-sharded-cluster-name.rst |
| Config Server Replica Set Name | .. include:: /includes/extracts/deploy-sharded-csrs-name.rst |
| Shard Name Prefix | .. include:: /includes/extracts/deploy-sharded-shard-name.rst |
| Process Name | .. include:: /includes/extracts/deploy-sharded-process-name.rst |
| Version | .. include:: /includes/extracts/deploy-sharded-version.rst |
| Data Directory | .. include:: /includes/extracts/deploy-data-directory.rst |
| Log File | .. include:: /includes/extracts/deploy-sharded-log-file.rst |

**Step 4: Configure Each Shard in Your Cluster.**

From the Member Configuration section, click
Shard Settings to open the shard configuration
options. Ops Manager lists each shard in the cluster and the
`mongod` processes associated to that shard.
Each shard process has the following options:

| Setting | Description |
|---|---|
| Member | .. include:: /includes/extracts/deploy-member-configuration-member.rst |
| Hostname | .. include:: /includes/extracts/deploy-member-configuration-hostname.rst |
| Port | .. include:: /includes/extracts/deploy-member-configuration-port.rst |
| Votes | .. include:: /includes/extracts/deploy-member-configuration-votes.rst |
| Priority | .. include:: /includes/extracts/deploy-member-configuration-priority.rst |
| Delay | .. include:: /includes/extracts/deploy-member-configuration-delay.rst |
| Build Indexes | .. include:: /includes/extracts/deploy-member-configuration-build-indexes.rst |
| Tags | .. include:: /includes/extracts/deploy-member-configuration-tags.rst |
| Add a Mongod | .. include:: /includes/extracts/deploy-sharded-member-configuration-add-mongod.rst |

To add additional shards to the cluster:

a. Click Add a Shard.
b. Under the Cluster Configuration section, set the
   following parameters for each `mongod` in the shard:

   - Version
   - Data Directory
   - Log File

**Step 5: Configure Each Configuration Server in Your Cluster.**

Ops Manager displays a different heading for your configuration server
settings depending on the MongoDB version you selected for your
configuration servers.

MongoDB 3.2 or Later:
  From the Member Configuration section, click
  Config Server Replica Set Settings to open
  the CSRS configuration options. Each config server
  replica set member has the following options:

  | Setting | Description |
  |---|---|
  | Member | .. include:: /includes/extracts/deploy-member-configuration-member.rst |
  | Hostname | .. include:: /includes/extracts/deploy-member-configuration-hostname.rst |
  | Port | .. include:: /includes/extracts/deploy-member-configuration-port.rst |
  | Votes | .. include:: /includes/extracts/deploy-member-configuration-votes.rst |
  | Priority | .. include:: /includes/extracts/deploy-member-configuration-priority.rst |
  | Delay | .. include:: /includes/extracts/deploy-member-configuration-delay.rst |
  | Build Indexes | .. include:: /includes/extracts/deploy-member-configuration-build-indexes.rst |
  | Tags | .. include:: /includes/extracts/deploy-member-configuration-tags.rst |
  | Add a Mongod | .. include:: /includes/extracts/deploy-sharded-member-configuration-add-mongod.rst |

MongoDB 3.0 or Earlier
  From the Member Configuration section, click
  Config Server Settings to open the configuration
  server options. Each configuration server has the following
  options:

  | Setting | Description |
  |---|---|
  | Hostname | .. include:: /includes/extracts/deploy-member-configuration-hostname.rst |
  | Port | .. include:: /includes/extracts/deploy-member-configuration-port.rst |

**Step 6: Configure Each `mongos` in Your Cluster.**

From the Member Configuration section, click
Mongos Settings to open the `mongos`
configuration options. Each `mongos` process has the
following options:

| Setting | Description |
|---|---|
| Hostname | .. include:: /includes/extracts/deploy-sharded-member-configuration-hostname.rst |
| Port | .. include:: /includes/extracts/deploy-sharded-member-configuration-port.rst |
| Add a Mongos | .. include:: /includes/extracts/deploy-sharded-member-configuration-add-mongos.rst |

**Step 7: Configure Each Replica Set in your Cluster.**

The Replication Settings section contains the following
configuration options for each replica set in the cluster:

| Setting | Description |
|---|---|
| Protocol Version | .. include:: /includes/extracts/deploy-member-replication-protocol-version.rst |
| Chaining Allowed | .. include:: /includes/extracts/deploy-member-replication-chaining-allowed.rst |
| Write Concern Majority Journal Default | .. include:: /includes/extracts/deploy-member-replication-write-concern-majority-journal-default.rst |
| Heartbeat Timeout (secs) | .. include:: /includes/extracts/deploy-member-replication-heartbeat-timeouts.rst |
| Election Timeout (ms) | .. include:: /includes/extracts/deploy-member-replication-election-timeout.rst |
| CatchUp Timeout (ms) | .. include:: /includes/extracts/deploy-member-replication-catch-up-timeout.rst |
| CatchUp Takeover Delay (ms) | .. include:: /includes/extracts/deploy-member-replication-catch-up-takeover-delay.rst |
| Last Error Defaults | .. include:: /includes/extracts/deploy-member-replication-last-error-defaults.rst |
| Force Reconfigure | .. include:: /includes/extracts/deploy-member-replication-force-reconfigure.rst |

**Step 6: Set the default read and write concerns for your MongoDB replica set.**

In the Default Read Concerns/Write Concerns card, you
configure the default level of acknowledgement requested from MongoDB
for read and write operations for this cluster. Setting the default
read and write concern can help with MongoDB 5.0 and later deployments
using arbiters.

From the Default Read Concerns section, you can set
consistency and isolation properties for the data
read from the cluster.

Select the default read concern from the Level dropdown
menu. You can choose from the following values:

- local, the MongoDB 5.0 and
  later default value,
- available, the
  MongoDB 4.4 default value, or
- majority.

From the Default Write Concerns section, you configure the
default level of acknowledgment requested from MongoDB for
write operations from the cluster. You
can set three parameters:

* - Parameter
  - Value

* - w Option
  - Desired number of `mongod` instances that must acknowledge a
    write operation. You can enter one of the
    following values:

    - `majority`, the MongoDB 5.0 and later default value, or
    - Any positive integer. MongoDB 4.4 defaults to `1`.

* - j Option
  - Flag that indicates whether the write acknowledgement must be
    written to the
    on-disk journal.

* - w Timeout
  - Desired time limit for the write concern expressed in
    milliseconds. Set this value when you set **w** to a value
    greater than `1` including `majority`.

**Step 8: Set any advanced configuration options for your MongoDB sharded cluster.**

The Advanced Configuration Options section allows you to 
set MongoDB runtime options for each MongoDB process
in your deployment.

To add an option:

a. Click Add Advanced Options.

#. Click Select a Startup Option and select the
   configuration option.

#. Ops Manager displays a context-sensitive input for configuring an
   acceptable value for the selected option.

#. Click Add to add the selected option and its
   corresponding value to every process of the selected process type
   in the cluster.

Ops Manager lists each process in the cluster grouped logically. Click
the grey arrow to the left of the logical grouping to display
its sub-groupings and processes. You can modify the advanced options
for each process individually as necessary.

For descriptions of the available Advanced Configuration 
Options, see /reference/deployment-advanced-options.

**Step 9: Click Create Cluster.**

Ops Manager redirects you to the Deployment view, where you
must review the cluster configuration before Ops Manager begins deployment.

**Step 10: Click Review & Deploy to review your changes.**

**Step 11: Review and approve your changes.**

Ops Manager displays your proposed changes.

a. If you are satisfied, click Confirm & Deploy.
b. If you want to make further configuration changes, 
   click Cancel. Click Modify for the
   cluster to make additional changes.
