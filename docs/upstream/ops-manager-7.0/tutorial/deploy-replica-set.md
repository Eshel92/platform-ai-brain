<!-- Converted from tutorial/deploy-replica-set.txt (reStructuredText). Includes are inlined. -->

# Deploy a Replica Set

A replica set is a group of MongoDB deployments that maintain 
the same data set. Replica sets provide redundancy and high 
availability and are the basis for all production deployments. 

To learn more about replica sets, see the Replication
Introduction in the MongoDB manual.

Use this procedure to deploy a new replica set managed by Ops Manager. After
deployment, use Ops Manager to manage the replica set, including such 
operations as adding, removing, and reconfiguring members.

**Note:** Added in Ops Manager 4.0

You can use Kubernetes to deploy MongoDB instances with
Ops Manager version 4.0 or later. 

To learn how to deploy a replica set using a Kubernetes object, see
`Deploy a Replica Set` in the
MongoDB Enterprise Kubernetes Operator documentation.

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

### Unique Names for Replica Set

Use a unique name for the replica set.

**Important:**

Replica set, sharded cluster, and shard names within the same
project must be unique. Failure to have unique names for the
deployments will result in broken backup snapshots.

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
Deployment page. Select New Replica Set
from the drop-down menu to open the Create New Replica Set
view.

**Step 3: Configure Cluster-Wide Settings.**

The Replica Set Configuration section contains the
following cluster-wide configuration settings. Settings marked with an
* asterisk in the  Ops Manager UI are **required**.

| Setting | Description |
|---|---|
| Replica Set Id | .. include:: /includes/extracts/deploy-replica-set-id.rst |
| Replica Set Settings | .. include:: /includes/extracts/deploy-replica-set-settings.rst |
| Process Name | .. include:: /includes/extracts/deploy-process-name.rst |
| Version | .. include:: /includes/extracts/deploy-version.rst |
| Data Directory | .. include:: /includes/extracts/deploy-data-directory.rst |
| Log File | .. include:: /includes/extracts/deploy-log-file.rst |

**Step 4: Configure each Replica Set Member.**

Ops Manager lists each replica set member under the
MongoD Settings heading of the
Member Configuration section. Each replica set member
has the following options:

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
| Add a Mongod | .. include:: /includes/extracts/deploy-member-configuration-add-mongod.rst |

**Step 5: Configure your Replication Settings.**

The Replication Settings section contains the following
configuration options for the replica set:

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

**Step 7: Set any advanced configuration options for your MongoDB replica set.**

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

**Step 8: Click Create Replica Set.**

Ops Manager automatically deploys the replica set as configured.
You can monitor the progress of cluster deployment from the
Deployment view.
