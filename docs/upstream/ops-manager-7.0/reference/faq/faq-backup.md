<!-- Converted from reference/faq/faq-backup.txt (reStructuredText). Includes are inlined. -->

# FAQ: Backup and Restore

This FAQ addresses common questions about Ops Manager and how it backs up and
restores databases and collections.

The introduction of the MongoDB Agent and the new backup process for
MongoDB 4.2 with a FCV of `4.2` have changed some of these
answers. Those answers have admonitions explaining the impact of these
new features to existing answers.

## Requirements

### What Version of MongoDB Does the Backup Feature Require?

| Ops Manager Release Series | 1.6 to 1.8 | 2.0 to 3.2 | 3.4 | 3.6 | 4.0 | 4.2 |
|---|---|---|---|---|---|---|
| Minimum MongoDB 2.4 version | 2.4.3 | 2.4.3 | 2.4.3 | 2.4.0 [1]_ |  |  |
| Minimum MongoDB 2.6 version | 2.6.0 | 2.6.0 | 2.6.0 | 2.6.0 | 2.6.0 | 2.6.0 [2]_ |
| Minimum MongoDB 3.0 version | 3.0.0 | 3.0.0 | 3.0.0 | 3.0.0 | 3.0.0 | 3.0.0 [2]_ |
| Minimum MongoDB 3.2 version |  | 3.2.0 | 3.2.0 | 3.2.0 | 3.2.0 | 3.2.0 |
| Minimum MongoDB 3.4 version |  |  | 3.4.0 | 3.4.0 | 3.4.0 | 3.4.0 |
| Minimum MongoDB 3.6 version |  |  |  | 3.6.0 | 3.6.0 | 3.6.0 |
| Minimum MongoDB 4.0 version |  |  |  |  | 4.0.0 | 4.0.0 |
| Minimum MongoDB 4.2 version |  |  |  |  |  | 4.2.0 |

### What MongoDB Permissions does Backup Require?

If you are backing up a MongoDB instance that has authentication
enabled, the MongoDB Agent requires the privileges described for the
MongoDB Agent backup function.

**See also:**

User Privilege Roles in MongoDB.

### How Does Ops Manager Measure Data Size?

Ops Manager uses the following conversions to measure snapshot size and to
measure how much oplog data has been processed:

- 1 MB = 1024`2` bytes (1 MiB)

- 1 GB = 1024`3` bytes (1 GiB)

- 1 TB = 1024`4` bytes (1 TiB)

### Does Backup Work with All Types of Deployments?

- For MongoDB 4.2 and later, see
  Backup Considerations for Databases.
- For any MongoDB with FCV (Feature Compatibility Version) `4.0` and earlier databases, Backup
  doesn't support standalone deployments. Backup has full
  support for replica sets and sharded clusters.

### Why Does The Backup Feature Not Support Standalone Deployments?

Ops Manager copies data from the oplog to provide a continuous backup
with point-in-time recovery. Ops Manager does not support backup of standalone
hosts because they do not have an oplog. To support backup with
a single `mongod` instance, you can run a one-member
replica set. 

**See also:**

/tutorial/convert-standalone-to-replica-set

## Operations

### How Does The Backup Feature Work?

To learn about the Backup feature, see /core/backup-overview.

### Will Backup Impact My Production Databases?

**Note:**

This answer applies only to databases running MongoDB with FCV (Feature Compatibility Version)
`4.0` and earlier

The Backup feature typically has minimal impact on production MongoDB
deployments. This impact performs similar to that of adding a new
secondary to a replica set.

By default, the agent performs its initial sync, the most
resource intensive operation for backups, against a secondary member of
the replica set to limit its impact. You may optionally configure the
Backup Agent to perform the initial sync against the replica set's
primary, although this increases the impact of the initial
sync operation.

### How Do I Maintain a Replica Set with Backup enabled?

Most operations in a replica set are replicated via the oplog and are
thus captured by the backup process. Some operations, however, make
changes that are *not* replicated: for these operations you *must*
have Ops Manager
resync from your current replica set
to include the changes.

The following operations are not replicated and therefore require
resync:

- Renaming or deleting a database by deleting the data files in the
  data directory. As an alternative, remove databases using an
  operation that MongoDB will replicate, such as
  `db.dropDatabase` from `mongosh`.

- Changing any data while the instance is running as a
  standalone.

- Rolling index builds.

- Using `compact` or `repairDatabase` to reclaim
  a significant amount of space.

  Resync is not strictly necessary after `compact` or
  `repairDatabase` operations but will ensure that the
  Ops Manager copy of the data is resized, which means quicker restores.

**See also:**

Maintenance Operations for Replica Set Members.

## Legacy Backup Agent

Backup capability has been moved to the MongoDB Agent with Backup
activated. This replaces the individual Backup Agent. This information
covers issues unique to the legacy Backup Agent. All of this
information applies to MongoDB databases running FCV (Feature Compatibility Version) `4.0` or
earlier.

### Where Should I Run The Backup Agent?

Run the Backup Agent on a host that:

- Is separate from your MongoDB instances. This avoids system resource
  contention.

- Can connect to your MongoDB instances. Check network settings for
  connections between the agent and MongoDB hosts. For a list of
  needed ports, see
  open ports for agents.

- Has at least 2 CPU cores and 3 GB of RAM above platform
  requirements. With each backup job it runs, the Backup Agent further
  impacts host performance.

### Can I Run the Backup and Monitoring Agents on a Single System?

There is no technical restriction that prevents the Backup Agent and
the Monitoring from running on a single system or host. However,
both agents have resource requirements, and running both on a single
system can affect the ability of these agents to support your
deployment in Ops Manager.

The resources required by the Backup Agent depend on rate and size
of new oplog entries (i.e. total oplog gigabyte/hour produced.)
The resources that the Monitoring requires depends on the number
of monitored `mongod` instances and the total number of
databases provided by the `mongod`
instances.

### Can I Run Multiple Backup Agents to Achieve High Availability?

You can run multiple Backup Agents for high availability. If you do,
the Backup Agents must run on different hosts.

When you run multiple Backup Agents, only one agent per project is the
**primary agent**. The primary agent performs the backups. The
remaining agents are completely idle, except to log their status as
standbys and to periodically ask Ops Manager whether they should become the
primary.

### Does the Backup Agent Modify My Database?

The Backup Agent writes a small token called a checkpoint into
the oplog of the source database at a regular interval. These tokens
provide a heartbeat for backups and have no effect on the source
deployment. Each token is less than 100 bytes.

**Important:**

You may use checkpoints for clusters that run MongoDB with
Feature Compatibility Version of 4.0 or earlier. Checkpoints were removed from
MongoDB instances with FCV (Feature Compatibility Version) of 4.2 or later.

**See also:**

checkpoint

### How Does the Initial Backup Sync Impact Database Performance?

The impact of the initial backup synchronization should be similar to
syncing a new secondary replica set member. The Backup Agent does not
throttle its activity, and attempts to perform the sync as quickly as
possible.

## Namespace Filters

**Note:**

Namespace filtering is supported only for Ops Manager versions 
`6.0.8` and later. Your MongoDB deployments must have 
`featureCompatibilityVersion` values of `4.0` and earlier, 
or `6.0.1` and later.

### How Can I Prevent Ops Manager from Backing Up a Collection?

Ops Manager provides a namespaces filter that
allows you to specify which collections or databases to back up.

### How Can I Change which Namespaces Are Backed Up?

To edit the filter, see /tutorial/edit-backup. Changing the
namespaces filter might necessitate a
resync. If so, Ops Manager handles the resync.

#### How can I use Backup if Backup jobs fail to bind?

The most common reason that jobs fail to bind to a Backup Daemon is
because no daemon has space for a local copy of the backed up replica
set.

To increase capacity so that the backup job can bind, you can:

- add an additional backup daemon.

- increase the size of the file system that holds the
  `head directory`.

- On FCV 4.0 and earlier, move the `head database` data to a 
  new volume with more space, and create a symlink or configure the 
  file system mount points so that the daemon can access the data 
  using the original path.

  FCV 4.2 and later do not use `head databases`.

#### How do I resolve `applyOps` errors during backups?

If you notice *consistent* errors in `applyOps` commands in your
Backup logs, it *may* indicate that the daemon has run out of space.

To increase space on a daemon to support continued operations, you
can:

- increase the size of the file system that holds the
  `head directory`.

- For FCV 4.0 and earlier, move the `head database` data to 
  a new volume with more space, and create a symlink or configure the 
  file system mount points so that the daemon can access the data 
  using the original path.

  FCV 4.2 and later do not use `head databases`.

## Data Restoration

Ops Manager produces a copy of your data files that you can use to seed a
new deployment.

### How Does Ops Manager Provide Point-in-Time Restores?

**Important:**

Ops Manager 4.2.13 and later supports this feature with FCV (Feature Compatibility Version) `4.2` or later.

When you trigger the restore, Ops Manager creates a link to this snapshot.
Once clicked, Ops Manager retrieves chunks from the Snapshot Store and
streams them to the target host.

The MongoDB Backup Restore Utility running on that host then downloads
and applies oplog entries to reach the specified point in time.

The ability of Ops Manager to provide a given point-in-time restore
depends on the retention policy of the snapshots and the configured
point-in-time window.

To learn more about retention policy and the point-in-time window,
see edit-snapshot-schedule.

### Can I Take Snapshots More Frequently than Every 6 Hours?

No. Ops Manager does not support a snapshot schedule more frequent than
every 6 hours. For more information, see
snapshot-frequency-and-retention.

### Can I Set My Own Snapshot Retention Policy?

Yes. You can change the schedule through the Edit Snapshot
Schedule menu option for a backed-up deployment.
Administrators can change the snapshot frequency and retention
policy through the
snapshotSchedule resource in
the API.

### How Long Does It Take to Create a Restore Snapshot?

Ops Manager transmits all backups in a compressed form from the Ops Manager host
to your infrastructure.

In addition, point-in-time restores depend upon the amount the oplog
entries that your host must apply to the received snapshot to roll
forward to the requested point-in-time of the backup.

### Does the Backup Feature Perform Any Data Validation?

Backup conducts basic corruption checks and provides an alert if any
component (e.g. the agent) is down or broken, but does not perform
explicit data validation. When it detects corruption, Ops Manager errs on
the side of caution and invalidates the current backup and sends an
alert.

### How Do I Restore a Snapshot?

You can request a restore via Ops Manager, where you can then choose which
snapshot to restore and how you want Ops Manager to deliver the restore. All
restores require 2-factor authentication. If you have SMS set up, Ops Manager
will send an authorization code via SMS. You must enter the
authorization code into the backup interface to begin the restore
process.

**Note:** From India, use Google Authenticator for two-factor

authentication. Google Authenticator is more reliable than
authentication with SMS text messages to Indian mobile phone
numbers (i.e. country code 91).

### What Is Delivered when I Restore a Snapshot?

Ops Manager delivers restores as `tar.gz` archives of MongoDB data files.

To learn more about restores, see
/tutorial/nav/backup-restore-deployments.

### How Does Ops Manager Roll Back Backed-up Data?

**Important:**

For MongoDB deployments running FCV (Feature Compatibility Version) 4.2 or later, rollbacks do not 
affect backed-up data in Ops Manager. From FCV (Feature Compatibility Version) 4.2 onward, Ops Manager only retains 
snapshots with timestamps up to and including the 
majority-commit point.

If your MongoDB deployment experiences a
rollback, then Ops Manager also
rolls back the backed-up data.

Ops Manager detects the rollback when a
tailing cursor finds a mismatch in
timestamps or hashes of write operations. Ops Manager enters a rollback
state and tests three points in the oplog of your replica set's
primary to locate a common point in history. Ops Manager rollback
differs from MongoDB secondary rollback in that the common
point does not necessarily have to be the most *recent* common point.

When Ops Manager finds a common point, the service invalidates oplog entries
and snapshots beyond that point and rolls back to the most recent
snapshot before the common point. Ops Manager then resumes normal backup
operations.

If Ops Manager cannot find a common point, a
resync is required.

### What Conditions Require a Resync?

**Important:**

This feature is incompatible with MongoDB 4.2 with FCV (Feature Compatibility Version) `4.2`.

If the Backup Agent's tailing cursor cannot
keep up with your deployment's oplog, then you must
resync your backups.

This scenario might occur if:

- Your application periodically generates a lot of data, shrinking the
  primary's oplog window to the point that data is written to the
  oplog faster than Ops Manager can consume it.

- If the Backup Agent is running on an under-provisioned or over-used
  machine and cannot keep up with the oplog activity.

- If the Backup Agent is down for a period of time longer than the
  oplog size allows. If you bring down your agents, such as for
  maintenance, restart them in a timely manner. For more information
  on oplog size, see
  Replica Set Oplog in the MongoDB
  manual.

- If you delete all replica set data and deploy a new replica set with
  the same name, as might happen in a test environment where
  deployments are regularly torn down and rebuilt.

- If there is a rollback, and Ops Manager cannot find a common point in the
  oplog.

- If an oplog event tries to update a document that does not exist in
  the backup of the replica set, as might happen if syncing from a
  secondary that has inconsistent data with respect to the primary.

- If you
  create an index in a rolling fashion.
