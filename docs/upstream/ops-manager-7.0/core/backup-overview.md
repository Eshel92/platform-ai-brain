<!-- Converted from core/backup-overview.txt (reStructuredText). Includes are inlined. -->

# Backup Process

Backups depend upon which version of MongoDB your database is
compatible.  This
Feature Compatibility Version ranges from the current version to one
version earlier. For MongoDB 4.2, the FCV can be `4.0` or `4.2`.
For deployments with FCV `4.2` or later, Ops Manager requires
opening a `$backupCursor` at the backup source host to copy data
files to capture a snapshot. This requires at least one MongoDB
agent with a backup module enabled and colocated on the data-bearing
servers per shard or replica set. The agent opens a `$backupCursor`
at the storage engine level to allow copying of database files in a
consistent state while still accepting writes.

Oplog tailing of the primary node is required for backups. This task is
typically performed by the MongoDB agent with a backup module enabled
on the primary node of the data shard or replica set.

**fcv42:**

The backup process takes a snapshot of the data directory at its
scheduled snapshot intervals. This
process copies the data files in a MongoDB deployment, sending them
over the network via Ops Manager to your existing snapshot storage. Your
deployment can still handle read and write operations during the
copying process.

The backup process works in this manner regardless of how snapshots are
stored.

**Note:**

With the new Backup process, there are no longer initial syncs. As a
result of not having initial syncs, Ops Manager can support a wider
array of customers such as those heavily using
renameCollection.

**fcv40:**

Once backup has started, Ops Manager backs up the data as a ongoing and
continuous process. This process continues creating snapshots as
long as the head database remains synchronized with the database.

This process works like
replica set data synchronization.

The backup process:

1. Performs an `initial sync` to back up all of your existing
   data in its current state.
   In sharded clusters, this occurs on each
   shard and on the config servers.

   **Note:** Conditions or Actions that Restart Initial Sync

   During the initial sync process, certain actions or conditions
   can restart the initial sync process. Avoid the following actions
   and conditions:

   **Actions to Avoid during Initial Sync:**

   - Restarting, shutting down, or changing the version or
     FCV (Feature Compatibility Version) value of the source database.
   - Renaming the collection
     of the source database.
   - Changing the $out
     value in the Aggregation Pipeline of the source database.
   - Restarting or shutting down Ops Manager Application or Backup Daemon.
   - Restarting, shutting down, or upgrading the
     MongoDB Agent.

   **Conditions to Avoid during Initial Sync:**

   - Head Directory is full.
   - Network connectivity between Ops Manager components is
     unstable.

#. Takes snapshots of the `data` directory in a deployment as often
   as your snapshot schedule
   specifies and then transfers the snapshots to a storage system.

   **Note:**

   Sharded Clusters also can
   enable checkpoints to permit
   restores at points in time between snapshots. To learn how
   sharded clusters use checkpoints, see
   checkpoints.

   **Important:**

   You may use checkpoints for clusters that run MongoDB with
   Feature Compatibility Version of 4.0 or earlier. Checkpoints were removed from
   MongoDB instances with FCV (Feature Compatibility Version) of 4.2 or later.

#. Monitors the oplog constantly and adds new database
   operations to the latest backup to keep the local Ops Manager copy of
   the data current.

The backup process works in this manner regardless of how snapshots are
stored.

## Backup Definition and Operational States

Each backup is defined as a job. Each job defines
how much and how often data is backed up. Backup jobs are defined on a
per-project basis.

### Operational States

The following table lists the states of a backup job:

**fcv42:**

| State | Retain Old Snapshots | Create New Snapshots |
|---|---|---|
| `Active` | Yes | Yes |
| `Stopped` | Yes | No |
| `Inactive` | No | No |
| `Misconfigured` |  |  |

	   - Yes
	   - No

      **Note:**

      The `Misconfigured` state applies only to regional-backup.

   **fcv40:**

   | State | Retain Old Snapshots | Create New Snapshots | Apply Oplogs |
   |---|---|---|---|
   | `Active` | Yes | Yes | Yes |
   | `Stopped` | Yes | No | No |
   | `Inactive` | No | No | No |

### Change Operational States

Once backup jobs are active for a `project`, they run without
further intervention until they are stopped or terminated. The operator
can change the state of a backup in the following ways:

**fcv42:**

| Initial State | Desired State | Method |
|---|---|---|
| `Inactive` | Active | Click Start. |
| `Active` | Stopped | Click Stop. |
| `Stopped` | Active | Click Restart. |
| `Stopped` | Inactive | Click Terminate. WARNING: Terminate deletes all retained backups. |

**fcv40:**

| Initial State | Desired State | Method |
|---|---|---|
| `Inactive` | Active after `Initial Sync` | Click Start. |
| `Active` | Stopped | Click Stop. |
| `Stopped` | Active after `Initial Sync` | Click Restart. |
| `Stopped` | Inactive | Click Terminate. WARNING: Terminate deletes all retained backups. |

**Important:**

You may receive a `Backup requires a resync` alert for your
backup jobs. This may require you to /tutorial/resync-backup.
This is not a different state, but a triggering of a new
Backup Process Flow. Once ``Initial
Sync`` completes, the backup job becomes Active
again.

## Backup Process Flows

Once created, a backup job goes through the following process flow:

**fcv42:**

(Figure: /images/backup-flow-wt.svg)

1. When the cluster is ready for its scheduled snapshot, it determines
   an optimal available node to take the snapshot. In most cases, the
   `mongod` determines lowest priority secondary member as the
   preferred snapshot node. Other metrics can factor into determining
   the preferred node, such as how current the secondary is with the
   primary and the previously chosen snapshot's member.

#. Once the `mongod` process determines the origin node for the
   snapshot, the backup process opens a `$backupCursor` on the
   targeted node.

   The `$backupCursor`, a storage engine layer mechanism, allows the
   database files in storage to be copied in a consistent state while
   still accepting writes.

#. The MongoDB Agent Backup function copies and processes these data
   files.

#. The MongoDB Agent Backup function sends the data files to Ops Manager.

#. The backup process collects and transfers these files to the
   snapshot store that you choose to store your backup. Depending upon
   which snapshot store you chose to store your snapshot, a snapshot
   can be written out as:

   a. Blocks to a blockstore.
      Binary chunks written to a MongoDB database on the Ops Manager host.

   #. Blocks to an `AWS S3 bucket`. The
      metadata for those blocks is written to a MongoDB database on the
      Ops Manager host.

   #. Snapshot files to a `file system store`. 
      The `Backup Daemon` that owns the backup 
      job for the replica creates a full snapshot by combining the changed and the new blocks with the 
      unchanged blocks from the last snapshot. If the Backup Daemon that owns the backup job is 
      down, you need to recover the Backup Daemon or 
      move the head database to another Daemon.

**Note:**

To learn more about the characteristics of each storage method, see
backup-configuration-options.

**fcv40:**

**Initial Backup**

(Figure: /images/backup-flow.bakedsvg.svg)

#. The Backup-enabled MongoDB Agent connects to, and authenticates with,
   the databases associated with the backup job.

#. The `initial sync` begins and enters its `starting` phase.
   Initial sync is a transition state between Inactive and
   Active. Initial Sync goes through a series of phases
   that are displayed on the Backup page to show progress.
   Backup streams the existing data to Ops Manager in 10 MB
   compressed bundles of documents called slices. Backup
   creates slices at the point in time when the snapshot was created.
   Ops Manager captures data inserted to the instance once the snapshot
   starts separately.

#. The `transferring` phase begins as the slices are streamed and
   stored in the `Oplog Store` temporarily
   on the Backup Daemon's behalf. The Backup Daemon service cannot
   dedicate itself to processing the large stream of initial sync
   slices at the expense of processing other backup jobs. The Oplog
   Store stores the slices until the Backup Daemon can fetch them. The
   Oplog Store is created when the first `snapshot store` is
   created.

#. While Backup is streaming the data, it tails the oplog.
   This tailing collects any differences between the state of the
   deployment database when the backup began and the deployment
   database's current state. The oplog entries are sent in 10 MB
   compressed bundles of documents called oplog slices. These two streams of slices are collected in parallel to
   reduce the time needed to construct a complete snapshot.

#. The `building` phase begins once Ops Manager receives the first batch
   of initial sync slices. In this phase, Ops Manager creates a local
   version of the backed up database called a `head database` on
   the host running the Backup Daemon service.

#. Ops Manager uses the Backup Daemon service to insert the documents
   stored in the Oplog Store into the head database.

#. The `applying oplogs` phase begins as Ops Manager applies the
   tailed oplog entries into the head database.

#. During the `fetching missing documents` phase, Ops Manager queries
   the deployment database for documents missed during document
   insertion. Ops Manager inserts the missing documents found in the
   deployment database into the head database.

#. After inserting the missing documents, the `creating indexes`
   phase begins as Ops Manager creates all of the indexes found in the
   deployment databases in the head database. When the indexes finish,
   the initial sync ends and the phase changes to `complete`.

#. Depending upon which snapshot store you chose to store your
   snapshot, a snapshot can be written out as:

   a. Blocks to a blockstore.

   #. Blocks to an `AWS S3 bucket`. The
      metadata for those blocks is written to a MongoDB database on the
      Ops Manager host.

   #. Snapshot files to a `file system store`.

**Note:**

The characteristics of each storage method is covered in
backup-configuration-options.

**Subsequent Backups**

The head database works as a full copy of the deployment database. It
needs oplogs applied to it on a regular basis to keep its data
synchronized with the deployment database. Snapshots are generated from
the data stored in the head database according to your
snapshot schedule.

Once the first full backup is completed, each active backup job follows
this process:

1. Backup tails the deployment's oplog.
2. Backup routinely batches new oplog entries in
   oplog slices and transfers them to Ops Manager.
3. Ops Manager stores the oplog entries in the Oplog Store.
4. Ops Manager applies the new oplog entries from the oplog slices to the
   head database that stores the deployment backup.
5. Ops Manager creates a new snapshot and stores it in the snapshot store
   as specified in your
   snapshot schedule.

## Regional Backup

You can assign backup jobs to deployment-regions-interface to
promote data isolation. When you assign a backup job to a deployment
region, Ops Manager writes all snapshots, oplogs, and sync data that the
job generates to the relevant storage configured for that
region. Regional backup is available for replica sets and sharded
clusters. To enable regional backup for a sharded cluster, you must
assign deployment regions and initiate backup jobs for each shard
separately.

To determine whether regional backup is enabled in your deployment, you
can check for the following in the Continuous Backup
dashboard. 

- Backup Region on the top right corner displays the group's
  deployment region by default and if the project is enabled for
  regional backup, it displays the legend Multi-Region. 
- Regional Backup column displays in the dashboard.
