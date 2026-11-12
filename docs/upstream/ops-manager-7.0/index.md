<!-- Converted from index.txt (reStructuredText). Includes are inlined. -->

# MongoDB Ops Manager

MongoDB Ops Manager can automate, monitor, and back up your MongoDB
infrastructure.

## Automation

Ops Manager Automation enables you to configure and maintain MongoDB nodes
and clusters.

(Figure: /images/how-it-works-ops.png)

MongoDB Agents using Automation on each MongoDB host can maintain your
MongoDB deployments. You can
install the
MongoDB Agent. Automation can
add hosts and
deploy and upgrade new or existing clusters.

## Monitoring

Ops Manager Monitoring provides real-time reporting, visualization, and
alerting on key database and hardware indicators.

### How Monitoring Works

When you activate Monitoring on a MongoDB host, Monitoring collects
statistics from the nodes in your MongoDB deployment. The Agent
transmits database statistics back to Ops Manager to report deployment status
in real time. You can set alerts on
indicators you choose.

## Backup

Ops Manager Backup provides scheduled
snapshots and
point-in-time
recovery
of your MongoDB replica sets and
sharded clusters.

### How Backup Works

When you activate Backup for a MongoDB deployment, Backup takes
snapshots of data from the MongoDB processes you have specified.

**Note:**

Sharded clusters and replica sets are the only deployment types you can back up if
your databases run MongoDB FCV 4.2 and earlier. To back up a
standalone mongod process
running MongoDB FCV 4.2 or earlier, you must
convert it to a single-member replica set.

### Backup Workflow

Backups rely upon the
MongoDB version compatibility
of your database.
This Feature Compatibility Version ranges from the current version to
one version earlier. For MongoDB 4.2, the FCV (Feature Compatibility Version) can be `4.0` or
`4.2`.

**fcv42:**

The backup process takes a snapshot of the data directory at its
scheduled snapshot intervals.

This process copies the data files in a MongoDB deployment, sending
them over the network via Ops Manager to your existing snapshot storage.

Your deployment can still handle read and write operations during the
copying process.

With the new backup process, there are no longer initial syncs. As a
result of not having initial syncs, Ops Manager (using a `mongod` running
FCV 4.2) can support a wider array of customers such as those
heavily using `renameCollection`.

The MongoDB Agent uses WiredTiger's incremental backup cursor to
capture the incremental changes.

**fcv40:**

Once backup has started, Ops Manager backs up the data as an ongoing
and continuous process. This process continues creating snapshots
as long as the head database remains synchronized with the
database.

This process works like
replica set data synchronization.

The backup process:

1. Performs an `initial sync` to back up all of your existing
   data in its current state.
   In sharded clusters, this occurs on each
   shard and on the config servers.

#. Takes snapshots of the `data` directory in a deployment as often
   as your snapshot schedule
   specifies and then transfers the snapshots to a storage system.

#. Monitors the oplog constantly and adds new database
   operations to the latest backup to keep the local Ops Manager copy of
   the data to allow
   `point-in-time restores`.

The MongoDB Agent then tails each replica set's oplog
to maintain on disk a standalone database, called a
`head database`. Ops Manager maintains one
head database for each backed-up replica set. The head
database stays consistent with the original primary up
to the last oplog that the MongoDB Agent supplies.

The backup process works in this manner regardless of how snapshots are
stored.

Backup uses a MongoDB instance version equal to or greater than the
version of the replica set it backs up.

Backup takes and stores snapshots based on a user-defined
snapshot retention policy.
Sharded cluster snapshots temporarily stop the balancer. The snapshots
then can insert a marker token into all shards and config servers in
the cluster. Ops Manager takes a snapshot when the marker tokens
appear in the snapshot data.

**fcv42:**

Ops Manager can back up data as a full or incremental backup. Ops Manager
requires a full backup:

- For your first backup.
- After a snapshot has been deleted.
- If the blockstore block size has been changed.

Incremental backups reduce network transfer and storage costs.

**fcv40:**

How much storage capacity you need depends on both the number
of snapshots and the type of snapshot storage you choose. The
following table outlines the differences in snapshot stores:

| Snapshot Store | Description |
|---|---|
| MongoDB blockstore | Only the differences between each successive snapshot are stored. Compression and block-level deduplication reduce the size of snapshot data. |
| AWS (Amazon Web Services) S3-compatible storage bucket | Only the differences between each successive snapshot are stored. Compression and block-level deduplication reduce the size of snapshot data. |
| File system store | Depending on the configuration, compression reduces the size of the snapshot data. |

All snapshots represent a full backup.

To learn more about how to configure backups, see
Backup Configuration Options.

### Restore Data

Backup can restore data from a complete scheduled snapshot or from
a selected point between snapshots.

**fcv42:**

You can restore sharded clusters and
replica sets from selected points in time.

**fcv40:**

- For sharded clusters, you can restore
  from checkpoints between snapshots.

- For replica sets, you can restore from
  selected points in time.

When you restore from a snapshot, Ops Manager reads directly from
the snapshot storage. You can restore the snapshot:

- To another cluster.
- To download the snapshot files from an HTTPS (Hypertext Transfer Protocol Secure) link.

**fcv42:**

When you restore from a point in time, Ops Manager does the following:

1. Restores a full snapshot from the snapshot storage.
#. Applies stored oplogs until it reaches the 
   specified point.
#. Delivers the snapshot and oplog updates using the same
   HTTPS (Hypertext Transfer Protocol Secure) mechanisms.

You can configure how much of the oplog you want to keep per
backup. This affects the amount of time a point-in-time restore
can cover.

**fcv40:**

When you restore from a checkpoint or point in time, Ops Manager does the following:

1. Restores a full snapshot from the snapshot storage. 
#. Applies stored oplogs until it reaches the
   specified point. 
#. Delivers the snapshot and oplog updates using the same HTTPS (Hypertext Transfer Protocol Secure) mechanisms. 
   To enable checkpoints, see enable-cluster-checkpoints.

You can configure how much of the oplog you want to keep per
backup. This affects how much time a checkpoint and
point-in-time restore can cover.

MongoDB welcomes your feedback. Let us know how we can
[improve Ops Manager](https://feedback.mongodb.com/ideas).
