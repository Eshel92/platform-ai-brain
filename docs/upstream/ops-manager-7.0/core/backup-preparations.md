<!-- Converted from core/backup-preparations.txt (reStructuredText). Includes are inlined. -->

# Backup Preparations

Before backing up your cluster or replica set, decide how to back up
the data and what data to back up. This page describes items you must
consider before starting a backup.

**See also:**

To learn how Backup works, see
mms-backup-functional-overview.

**Warning:**

Ops Manager no longer supports the creation of cluster snapshots from
database deployments that use local key encryption.
If you encrypt a database deployment with local key encryption,
the snapshot fails.
To encrypt snapshots, use KMIP (Key Management Interoperability)-based encryption with your database deployments.

## Backup Configuration Options

The backup and recovery requirements of a given system vary to meet
the cost, performance and data protection standards the system's
owner sets.

Ops Manager Enterprise Backup and Recovery supports five backup
architectures, each with its own strengths and trade-offs. Consider
the architecture that meets the data protection requirements for
your deployment before configuring and deploying your backup
architecture.

**Example:**

Consider a system whose requirements include low operational
costs. The system's owners may have strict limits on what they
can spend on storage for their backup and recovery configuration.
They may accept a longer recovery time as a result.

Conversely, consider a system whose requirements include a low
`Recovery Time Objective`. The system's owners tolerate
greater storage costs if it results in a backup and recovery
configuration that fulfills the recovery requirements.

Ops Manager Enterprise Backup and recovery supports the following backup
architectures:

- A file system on a SAN (Storage Area Network) with advanced features for filesystem
  backups, such as high availability, compression, or
  deduplication
- A file system on one or more NAS (Network Attached Storage) devices
- An [S3-compatible](https://aws.amazon.com/s3) blockstore
- MongoDB blockstore in a highly available configuration
- MongoDB blockstore in a standalone configuration

We provide the backup architecture recommendations as
guidance for developing your own data protection approaches.
Our recommendations don't cover or represent each scenario
or deployment.

### Backup Method Features

| Backup System Feature | File System on SAN (Storage Area Network) | File System on NAS (Network Attached Storage) | AWS S3 Blockstore | MongoDB HA (High Availability) Blockstore | MongoDB Blockstore |
|---|---|---|---|---|---|
| Snapshot Types | Complete ***** | Complete ***** | Many partial | Many partial | Many partial |
| Backup Data Deduplication | If SAN supports | No | Yes | Yes | Yes |
| Backup Data Compression | Yes | No | Yes | Yes | Yes |
| Backup Data Replication | If SAN supports | No | No | Yes | No |
| Backup Storage Cost | Higher | Medium | Lower | Higher | Lower |
| Staff Time to Manage Backups | Medium | Medium | Lower | Higher | Medium |
| Backup RTO (recovery time objective) | Lower | Medium | Lower | Lower | Medium |

***** To perform an incremental backup to a
File System Store, the MongoDB Agent
slices each storage engine
file in the path specified for backup into block(s) of
data and transfers only changed block(s) to Ops Manager.
Ops Manager creates a new snapshot from received
block(s) and copies the remaining unchanged block(s)
from the previous full backup snapshot. Each incremental
backup snapshot stored to a file system saves
network I/O. Each such backup snapshot contains a full
copy of all required files from a backed up MongoDB
deployment and does not de-duplicate
records.

**Note:** **When Do You Use a Particular Backup Method?**

- To run backups frequently on large amounts of data and
  restore from backups, consider backing up to a file
  system on a SAN (Storage Area Network), an AWS S3-compatible storage snapshot store, or a MongoDB
  blockstore configured as a replica set or a
  sharded cluster.

- To restore data without relying on MongoDB
  database, consider backing up to an AWS S3-compatible storage snapshot store,
  one or more NAS (Network Attached Storage) devices, or a file system on a SAN (Storage Area Network) with
  advanced features for file system backups, such as high
  availability, compression, or deduplication.

- To minimize internal storage and maintenance
  costs, consider backing up to an AWS S3-compatible storage snapshot store or
  a MongoDB standalone blockstore.

  A MongoDB standalone blockstore offers limited resilience. If
  the disk fills, this blockstore may go offline. You can
  recover backup snapshots only after adding additional storage.

## Backup Sizing Recommendation

When sizing the backup of your data, keep the replica set 
size to 2 TB or less of uncompressed data. If 
your database increases beyond 2 TB of uncompressed data:

- Shard the database
- Keep each shard to 2 TB or less of uncompressed data

We recommend that you review the amount of data that you are backing up
to the blockstore. If the amount of data that you back up negatively 
affects the performance of the blockstore or if you can't meet your
RTO (Recovery Time Objective) requirements with a single
blockstore, distribute the workload across multiple blockstores to
balance the backup operations. You can even configure a single
blockstore per shard to meet your scaling needs. 

You can create additional blockstores any time and configure your backup
jobs to use the blockstores manually: 

- To learn more about allocating specific blockstores to a project, see
  admin-manage-backup-resources. 
- To learn more about configuring shard backups to use specific
  blockstores, see manual-blockstore-maintenance.

These size recommendations are a best practice. They are not a
limitation of the MongoDB database or Ops Manager.

Backup and restore can use large amounts of CPU, memory, storage, 
and network bandwidth.

**Example:**

Your stated network throughput, such as 10 Gbps or 100 Gbps, is 
a *theoretical* maximum. That value doesn't account for sharing 
or throttling of network traffic.

Consider the following scenario:

- You want to back up a 2 TB database.
- Your hosts support a 10 Gbps TCP connection from Ops Manager to its
  backup storage.
- The network connection has very low packet loss and a low round
  trip delay time.

A *full* backup of your data would take *more than 30 hours to
complete*. [#]_

This doesn't account for disk read and write speeds, which can be,
at most, 3 Gbps reads and 1 Gbps writes for a single or mirrored
NVMe storage device.

The time required to complete each successive incremental backup
depends on write load.

If you shard this database
into 4 shards, each shard runs its backup separately. This results
in a backup that takes less than 8 hours to complete.

## Snapshot Frequency and Retention Policy

By default, Ops Manager takes a base snapshot of your data every 24 hours.

If desired, administrators can change the frequency of base snapshots
to 6, 8, 12, or 24 hours. Ops Manager creates snapshots automatically on a
schedule; you cannot take snapshots on demand.

Ops Manager retains snapshots for the time periods listed in the following
table. 

If you terminate a deployment's backup,
Ops Manager immediately deletes the snapshots that are within the dates
of the current retention policy.

If you stop a deployment's backup, Ops Manager stops
taking new snapshots but retains existing snapshots until their listed
expiration date.

| Snapshot | Default Retention Policy | Maximum Retention Policy |
|---|---|---|
| Base snapshot | 2 days | 5 days (30 days if frequency is 24 hours) |
| Daily snapshot | 0 days | 1 year |
| Weekly snapshot | 2 weeks | 1 year |
| Monthly snapshot | 1 month | 7 years |

**Note:**

Monthly snapshots are full snapshots by default, not incremental snapshots.

You can change a backed-up deployment's schedule through its
Edit Snapshot Schedule menu option, available through the
Backup page. Administrators can change snapshot frequency
and retention through the
snapshotSchedule resource in the API.

Changing the reference time changes the time of the next scheduled
snapshot. You can't make the next scheduled snapshot happen sooner than
the current next snapshot time. The current next snapshot time is the
current reference time plus the interval between snapshots.

To determine the time of the next snapshot, compare the current next
snapshot time to the new reference time:

- If the new reference time is before the current next snapshot time,
  the next snapshot still occurs after the current next snapshot time.
  The snapshot occurs at the new reference time plus the number of
  intervals needed to surpass the current next snapshot time. If this
  time has already passed when you make the change, the Ops Manager takes the
  next snapshot at the next occurrence of the new reference time. See
  the first two rows of the following table for examples.

- If the new reference time is after the current next snapshot time,
  Ops Manager takes the next snapshot at the next occurrence of the new
  reference time. See the third and fourth row of the following table
  for examples.

| Time of Change | Current Reference Time | Interval Between Snapshots | Current Next Snapshot Time | New Reference Time | Time of Next Snapshot |
|---|---|---|---|---|---|
| 08:00 UTC | 12:00 UTC | 6 hours | 12:00 UTC | 10:00 UTC | 16:00 UTC today |
| 23:00 UTC | 12:00 UTC | 6 hours | 00:00 UTC | 10:00 UTC | 04:00 UTC tomorrow |
| 08:00 UTC | 12:00 UTC | 6 hours | 12:00 UTC | 19:00 UTC | 19:00 UTC today |
| 20:00 UTC | 12:00 UTC | 6 hours | 00:00 UTC | 19:00 UTC | 01:00 UTC tomorrow |

If you change the schedule to save fewer snapshots, Ops Manager does
**not** delete existing snapshots to conform to the new schedule. To
delete unneeded snapshots, see /tutorial/delete-backup-snapshots.

### Limits

- Ops Manager does not backup deployments where the total number of
  collections on the deployment meets or exceeds `100,000`.

- Ops Manager does not replicate index collection options.

### Encryption

Ops Manager can encrypt any backup job stored in a
`head database` running
`MongoDB Enterprise` between
FCV 3.4 and 4.0 with the
WiredTiger storage engine.

FCV `4.2` and later use 
backup cursors instead of
`head databases`. For
more information, see backup-daemon.

**See also:**

/tutorial/encrypt-snapshots.

## Backup Considerations

### Consistency and Snapshots

For clusters running MongoDB version 4.2 or and later: 

- Ops Manager maintains
  causal consistency 
  when taking snapshots except for size statistics reported by collStats
  and `db.[collection].count()`. Size statistics reported
  by collStats and `db.[collection].count()` may be inccurate.
- Ops Manager coordinates the time across all
  shards for sharded clusters. This ensures that snapshots include all documents written to every
  shard and node as of the scheduled snapshot time.

For clusters running MongoDB version 4.0 and earlier:

- Ops Manager maintains crash-consistent snapshots.
- Ops Manager takes snapshots from each of the shards for sharded clusters
  and the Config Server Replica Sets at approximately the same time.

### Databases Running FCV 4.2 and Later

**Important:**

Sharded clusters and replica sets are the only deployment types you can back up if
your databases run MongoDB FCV 4.2 and earlier. To back up a
standalone mongod process
running MongoDB FCV 4.2 or earlier, you must
convert it to a single-member replica set.

#### Backup Features Supported at Present

| Feature | Databases running FCV 4.2 and later | Databases running FCV 4.0 and earlier |
|---|---|---|
| Backs up Data using WiredTiger Snapshots | check-circle |  |
| Backs up Data using the Backup Daemon |  | check-circle |
| Backs up Replica Sets | check-circle | check-circle |
| Backs up Sharded Clusters | check-circle | check-circle |
| Can Filter using Namespaces [#]_ |  | check-circle |
| Can Specify Sync Source Database |  | check-circle |
| Can Restore Data to Specific Point in Time [#]_ | check-circle | check-circle |
| Can Perform Incremental Backups [#]_ | check-circle | check-circle |
| Supports Snapshots that use KMIP (Key Management Interoperability) Encryption [#]_ | check-circle | check-circle |
| Supports Snapshots that use Local Key Encryption [#]_ |  | check-circle |
| Supports Saving to blockstore snapshot storage | check-circle | check-circle |
| Supports Saving to S3-compatible storage Snapshot Storage | check-circle | check-circle |
| Supports Saving to File System Storage [#]_ | check-circle | check-circle |
| Supports Databases running MongoDB Enterprise | check-circle | check-circle |
| Supports Databases running MongoDB Community |  | check-circle |
| Requires a MongoDB Agent with backup enabled on every `mongod` cluster node | check-circle |  |

#### Requirements and Limitations

To run backups and restores if you are running MongoDB 4.2 or later
with FCV 4.2 or later, you:

- Must run `MongoDB Enterprise`.

- Must account for the change in blockstore block size. If you
  didn't set your block size and used the default, that block size
  changes from 64 KB to 1 MB. This can impact storage usage.

- Must ensure the hostnames in your replica set configuration match 
  the hostnames that the MongoDB Agent uses, or that your 
  host mappings contain the correct hostnames. You 
  can use rs.conf() to verify 
  your replica set configuration. 

- Can use namespace filter lists to define the
  namespaces included in a backup only if you are
  running MongoDB 6.0 or later. Snapshots taken on versions MongoDB 4.2
  through 5.0 always include all namespaces.

- Don't need a sync source database. When taking a Snapshot, Ops Manager
  selects the replica set member with the least performance impact
  and greatest storage-level duplication of Snapshot data.

- Must deploy a MongoDB Agent with every `mongod` node in
  the cluster.

**Note:**

If Ops Manager doesn't manage your cluster:

- Grant the
  `backup` and `clusterAdmin` roles to the
  MongoDB user that runs backups.
- Ensure that the operating system user that runs the MongoDB Agent
  has read permission for all data files (including journal files)
  of the deployment.

##### Shared File System

If you configure Ops Manager to use multiple Ops Manager application 
servers behind an HTTP (Hypertext Transfer Protocol) or HTTPS (Hypertext Transfer Protocol Secure) load balancer and use 
file system snapshots, 
FCV 4.2 or 
later backup snapshot jobs run in parallel on one or more servers. 
Ensure that you have a shared file system mounted on each Ops Manager 
server. The Ops Manager application server might open and write 
different offsets of the same files. Ensure that the shared file 
system allows this. Otherwise, you will encounter access errors.

### Databases Running FCV 4.0 and Earlier

**Important:**

Sharded clusters and replica sets are the only deployment types you can back up if
your databases run MongoDB FCV 4.2 and earlier. To back up a
standalone mongod process
running MongoDB FCV 4.2 or earlier, you must
convert it to a single-member replica set.

The following considerations apply when your databases run any version
of MongoDB 4.0 or earlier or when they run MongoDB 4.2 with
`"featureCompatibilityVersion" : 4.0`

### Garbage Collection of Expired Snapshots

Ops Manager manages expired snapshots using groom jobs. These groom jobs act
differently depending upon which snapshot store contains the snapshots:

| Snapshot Store | How Groom Jobs Work |
|---|---|
| MongoDB Blockstore | Uses additional disk space up to the amount of living blocks for each job. |
| Filesystem Snapshot stores | Deletes expired snapshots |
| S3 snapshot stores | May use additional disk space if Ops Manager creates a snapshot while the groom job runs. Ops Manager can run concurrent groom jobs on S3 snapshot stores. |

**Note:**

Snapshot jobs and groom jobs can't run concurrently. If you
initiate a groom job while a snapshot job is running, the groom job
fails, and Ops Manager logs an error and automatically retries the
groom job after the snapshot job completes. If you initiate a
snapshot job while a groom job is running, the snapshot job fails,
and Ops Manager logs an error and retries the snapshot job after the
groom job completes.

To learn more about groom jobs, see Groom jobs.

### Namespaces Filter

The namespaces filter lets you specify which databases and collections
to back up. You can apply a namespace filter to any database except
`admin` and `local` and any collection that doesn't start with
`system`.

**Tip:**

If you apply namespace filters to a snapshot, you can't query that snapshot.

You create either a Deny List of the collections to
exclude or a Allow List of the collections to include. You make your
selections when starting a backup and can later edit them as needed.

Use the deny list to prevent backup of collections that contain logging
data, caches, or other ephemeral data. Excluding these kinds of
databases and collections will allow you to reduce backup time and
costs. Using a deny list is often preferable to using an allow list as an allow
list requires you to intentionally opt in to every namespace you want to back up.

**Note:**

Namespace filtering is supported only for Ops Manager versions 
`6.0.8` and later. Your MongoDB deployments must have 
`featureCompatibilityVersion` values of `4.0` and earlier, 
or `6.0.1` and later.

### Storage Engine

To back up MongoDB clusters, use the
WiredTiger storage engine storage engine.

If your current backing databases use MMAPv1, upgrade to WiredTiger:

- Change Sharded Cluster to WiredTiger

- Change Replica Set to WiredTiger

With WiredTiger, Ops Manager limits backups to deployments with fewer than
100,000 files. Files includes collections and indexes.

MongoDB 4.2 removes MMAPv1 storage. To learn more about storage
engines, see Storage in the MongoDB manual.

### Resyncing Production Deployments

For production deployments, resync all
backed up replica sets periodically, such as once a year. When you resync,
data is read from a secondary in each replica set. During resync,
no new snapshots are generated.

You may also want to resync your backup if you:

- Reduce the size of the data, such that the size of Ops Manager's copy of the
  data on disk is also reduced.

- Create a TTL index, which periodically
  deletes documents.

- Drop a collection
  (MMAPv1 only).

- Run a sharded cluster, and move chunks
  from a particular shard.

- Switch storage engines, if you want Ops Manager to provide snapshots
  in the new storage engine format.

- Build an Index on a replica set in a rolling fashion.

### Checkpoints

**Important:**

You may use checkpoints for clusters that run MongoDB with
Feature Compatibility Version of 4.0 or earlier. Checkpoints were removed from
MongoDB instances with FCV (Feature Compatibility Version) of 4.2 or later.

For sharded clusters, checkpoints provide
additional restore points between snapshots. With checkpoints enabled,
Ops Manager creates restoration points at configurable intervals of every 15,
30 or 60 minutes between snapshots. To enable checkpoints, see
enable checkpoints.

To create a checkpoint, Ops Manager stops the balancer and inserts a
token into the oplog of each shard and config
server in the cluster. These checkpoint tokens are lightweight and don't
affect performance or disk use.

Backup doesn't require checkpoints, and they are disabled by default.

Restoring from a checkpoint requires Ops Manager to apply the oplog
of each shard and config server to the last snapshot captured before
the checkpoint. Restoration from a checkpoint takes longer than
restoration from a snapshot.

### Snapshots when Agent Can't Stop Balancer

For sharded clusters running with FCV 4.0 or
earlier, Ops Manager disables the balancer before taking a cluster
snapshot. In certain situations, such as a long migration or no running
mongos, Ops Manager tries to disable the balancer but cannot. In
such cases, Ops Manager continues to take cluster snapshots but flags the
snapshots that may have incomplete or inconsistent data. Cluster
snapshots taken during an active balancing operation run the risk of
data loss or orphaned data.

### Snapshots when Agent Can't Contact a `mongod`

For sharded clusters, if the Backup
can't reach a mongod process,
whether a shard or config server, then the agent can't insert a
synchronization oplog
token. In these cases, Ops Manager doesn't create the snapshot and displays
a warning message.

### Regional Backup Considerations

To enable regional-backup you must associate at least one
of the following with the deployment region that a replica set or shard targets:

- manage-snapshot-blockstore

- manage-s3-snapshot-store

- manage-snapshot-filestore

Additionally, you must associate one of each of the following items
with a deployment region:

- oplog-stores-page
- `sync store`
  (unless you set `mms.backup.noSyncState` to `true`)
- `backup daemons`

If you add a shard to a sharded cluster after you enable regional
backup for that sharded cluster, you must assign a deployment region
to the new shard to continue the backup jobs for the existing
shards. Until you assign a deployment region to the new shard, the
entire sharded cluster backup job has a `Misconfigured` state and
doesn't generate new snapshots. A sharded cluster with a
`Misconfigured` state continues to generate oplog entries.
