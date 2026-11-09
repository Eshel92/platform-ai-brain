<!-- Converted from tutorial/nav/restore-overview.txt (reStructuredText). Includes are inlined. -->

# Restore Overview

To restore a deployment from a backup, select a snapshot or point in
time from which you want to restore your database. Ops Manager provides you
with the files from which you can restore your database.

You can restore a single MongoDB database, a replica set, or all
shards in a sharded cluster.

You can restore a deployment from an existing snapshot or a
specific point in time. For the point in time, you can specify a date and time, 
an oplog timestamp, or a checkpoint for
a sharded cluster.

If you are restoring from a point in time, you must download the
MongoDB Backup Restore Utility to your target host. The MBRU (MongoDB Backup Restore Utility) requests
and applies oplog entries between the latest complete snapshot
and the point in time you choose.

To restore your backup, use one of these options:

- Restore the files to another cluster using automation
- Manually copy restored files to the hosts you choose
- Restore from a queryable backup

## Cancel a Restore

To cancel a restore:

1. Navigate to the Backup > Restore History
   tab.

2. Click Cancel.

## Automated Restore

If you choose to have Ops Manager automation restore your backup, the Automation
removes all existing data from the target hosts and replaces that data
with new backup data from your snapshot.

### Limitations

If you are restoring a sharded cluster, you must restore all shards. The
restore process fails if you try to restore a single shard in a sharded
cluster.

### Prerequisites

To perform automated restores:

- Install an MongoDB Agent installed on the source and all target hosts,
  and check that an MongoDB Agent on the target deployment can connect
  to all hosts in the target deployment.

- Configure Backup Admin and
  Automation Admin roles in Ops Manager.

- Ensure that the source and target clusters have the same number of
  shards. Ops Manager excludes clusters with a different number of shards
  from the available restore targets.

- For sharded clusters running FCV 4.0 or earlier,
  enable checkpoints.

- Check that the target cluster's `featureCompatibilityVersion` is greater
  than or equal to the source cluster's `featureCompatibilityVersion`.

  **Example:**

  Run the following command to retrieve the
  `featureCompatibilityVersion` of a given host:

  ```javascript
  db.adminCommand( {
    getParameter: 1,
    featureCompatibilityVersion: 1
  } )
  ```

  To learn more, see
  setFeatureCompatibilityVersion.

- Review the following compatibility matrix for the supported source cluster
  for each MongoDB version. The MongoDB version of each host in
  the target cluster *must* support the FCV (Feature Compatibility Version) of the snapshot of the
  source cluster.

  | Source Cluster FCV (Feature Compatibility Version) | \| MongoDB \| 4.2 | \| MongoDB \| 4.4 | \| MongoDB \| 5.0 | \| MongoDB \| 6.0 | \| MongoDB \| 7.0 |
  |---|---|---|---|---|---|
  | 4.2 | check-circle | check-circle |  |  |  |
  | 4.4 |  | check-circle | check-circle |  |  |
  | 5.0 |  |  | check-circle | check-circle |  |
  | 6.0 |  |  |  | check-circle | check-circle |
  | 7.0 |  |  |  |  | check-circle |

### Restore to Different Project

You can choose to restore to a cluster of a different project:

- To restore to another Ops Manager project, you must have
  Automation Admin or
  Backup Admin roles for the
  target project.

- To restore to another MongoDB Atlas project, you must have
  Project Owner role for the target project.

### Potential Causes for Automated Restore Failure

An automated restore can fail when certain storage settings of the
backup's database and target database do not match:

- `storage.engine`
- `storage.directoryPerDB`
- `storage.mmapv1.nsSize`
- `storage.mmapv1.smallFiles`
- `storage.wiredTiger.collectionConfig.blockCompressor`
- `storage.wiredTiger.engineConfig.directoryForIndexes`

No method exists to check for mismatches before attempting a restore.
If a restore attempt fails, Ops Manager displays any mismatched settings. If
you still want to restore the backup's database, fix the settings in
the target database that do not match backup's database, then retry the
restore process for the backup's database.

**Important:**

MongoDB removed support for the MMAPv1 storage engine in MongoDB 4.2.
If you
edit your deployment's configuration
to change your storage engine to storage-wiredtiger, Ops Manager
restarts the MongoDB processes.

An automated restore fails when you attempt to restore a single shard
in a sharded cluster. If you are restoring a sharded cluster, you must
restore all shards.

### Restore Procedures

To perform an automated restore, see the procedure for the deployment
you want to restore:

- Replica Set
- Sharded Cluster

## Manual Restore

### Prerequisites

To perform manual restores, you must have the
Backup Admin role in Ops Manager.

### Restore File Format

Ops Manager provides each snapshot as an uncompressed
(`.tar`) or compressed (`.tar.gz`) archive containing a copy of
your database files.

Choosing compressed snapshots results in faster
delivery, but requires sufficient space on the target host for both
the compressed snapshot and its extracted database files.

- For a replica set, Ops Manager provides one snapshot that
  you copy to each replica set member.

- For a sharded cluster, Ops Manager provides one snapshot for the
  config servers and one snapshot for
  each shard.

### Manual Restore Procedures

To perform a manual restore, see:

- Restore a Single Database or Collection using Queryable Backup
- Restore a Replica Set
- Restore a Sharded Cluster

### Restore Process Flows

You can restore from a completed shapshot or from a specific point in time.
Use the following pages to learn about the manual restore process flows.
