<!-- Converted from tutorial/backup-sharded-cluster-with-filesystem-snapshots.txt (reStructuredText). Includes are inlined. -->

# Back Up a Self-Managed Sharded Cluster with File System Snapshots

## Overview

This document describes a procedure for taking a backup of all
components of a sharded cluster. This procedure uses file system
snapshots to capture a copy of the `mongod` instance.

**Important:**

To back up a sharded cluster you **must** stop *all* writes to the cluster.

For more information on backups in MongoDB and backups of sharded
clusters in particular, see /core/backups and
/administration/backup-sharded-clusters.

## Considerations

### Transactions Across Shards

To take a backup with a file system snapshot, you must first stop the balancer,
stop writes, and stop any schema transformation operations on the cluster.

MongoDB provides backup and restore operations that can run with the balancer
and running transactions through the following services:

- [MongoDB Atlas](https://docs.atlas.mongodb.com/)

- [MongoDB Cloud Manager](https://docs.cloudmanager.mongodb.com/)

- [MongoDB Ops Manager](https://docs.opsmanager.mongodb.com/)

### Encrypted Storage Engine (MongoDB Enterprise Only)

For encrypted storage engines that
use `AES256-GCM` encryption mode, `AES256-GCM` requires that every
process use a unique counter block value with the key.

For encrypted storage engine
configured with `AES256-GCM` cipher:

- Restoring from Hot Backup
      Starting in 4.2, if you restore from files taken via "hot"
      backup (i.e. the `mongod` is running), MongoDB
      can detect "dirty" keys on startup and automatically rollover
      the database key to avoid IV (Initialization Vector) reuse.

- Restoring from Cold Backup
      However, if you restore from files taken via "cold" backup
      (i.e. the `mongod` is not running), MongoDB
      cannot detect "dirty" keys on startup, and reuse of IV voids
      confidentiality and integrity guarantees.

      Starting in 4.2, to avoid the reuse of the keys after
      restoring from a cold filesystem snapshot, MongoDB adds a new
      command-line option `--eseDatabaseKeyRollover`. When started with the
      `--eseDatabaseKeyRollover` option, the `mongod`
      instance rolls over the database keys configured with
      `AES256-GCM` cipher and exits.

### Balancer

It is *essential* that you stop the balancer before capturing a backup.

If the balancer is active while you capture backups, the backup
artifacts may be incomplete or have duplicate data, as chunks may migrate while recording backups.

### Precision

In this procedure, you will stop the cluster balancer and take a backup
up of the config database, and then take backups of each
shard in the cluster using a file-system snapshot tool. If you need an
exact moment-in-time snapshot of the system, you will need to stop all
writes before taking the file system snapshots; otherwise the snapshot will
only approximate a moment in time.

### Consistency

To back up a sharded cluster, you must use the `fsync` command or
`db.fsyncLock` method to stop writes on the cluster. This helps 
reduce the likelihood of inconsistencies in the backup. 

**Note:**

These steps can only produce a consistent backup if they are
followed exactly and no operations are in progress when you
begin.

### Snapshots with Amazon EBS in a RAID 10 Configuration

If your deployment depends on Amazon's Elastic Block Storage (EBS) with
RAID configured within your instance, it is impossible to get a
consistent state across all disks using the platform's snapshot tool. As
an alternative, you can do one of the following:

- Set a `fsync` lock to flush all writes and lock the
  cluster against new writes to help reduce the likelihood of an
  inconsistent state occurring during the backup process. 

  If you choose this option see backup-without-journaling.

- Configure LVM to run and hold your MongoDB data files on top of the
  RAID within your system.

  If you choose this option, perform the LVM backup operation described
  in lvm-backup-operation.

### Version Compatibility

This procedure requires a version of MongoDB that supports fsync
locking from `mongos`.

   `fsyncUnlock` commands

Starting in MongoDB 6.0.11 (also available starting in
5.0.22) the `fsync` and can run on
`mongos` to lock and unlock a sharded cluster.

### Stale Data

Backups provide a snapshot of the current state of the database.
When you restore from a backup, the restored database doesn't
include any changes made after the backup was taken, which can
result in data loss.

## Steps

To take a self-managed backup of a sharded cluster, complete the following
steps:

**Step 1: Find a Backup Window**

Chunk migrations, resharding, and schema migration operations can cause
inconsistencies in backups. To find a good time to perform a backup,
monitor your application and database usage and find a time when these
operations are unlikely to occur.

For more information, see sharded-schedule-backup.

**Step 2: Stop the Balancer**

To prevent chunk migrations from disrupting the backup, use
the `sh.stopBalancer` method to stop the balancer:

```javascript
sh.stopBalancer()
```

If a balancing round is currently in progress, the operation waits for
balancing to complete.

To verify that the balancer is stopped, use the
`sh.getBalancerState` method:

```javascript
use config
while( sh.isBalancerRunning().mode != "off" ) {
   print("waiting...");
   sleep(1000);
}
```

**Step 3: Lock the Cluster**

Writes to the database can cause backup inconsistencies. Lock your
sharded cluster to protect the database from writes.

To lock a sharded cluster,  use the `db.fsyncLock` method:

```javascript
db.getSiblingDB("admin").fsyncLock()
```

Run the following aggregation pipeline on both `mongos` and
the primary `mongod` of the config servers. To confirm the
lock, ensure that the `fysncLocked` field returns `true` and
`fsyncUnlocked` field returns `false`.

```javascript
db.getSiblingDB("admin").aggregate( [
   {  $currentOp: { } },
   {  $facet: {
      "locked": [
         { $match: { $and: [
            { fsyncLock: { $exists: true } }
         ] } }],
       "unlocked": [
         { $match: { fsyncLock: { $exists: false } } }
       ]
   } },
   {  $project: {
      "fsyncLocked": { $gt: [ { $size: "$locked" }, 0 ] },
      "fsyncUnlocked": { $gt: [ { $size: "$unlocked" }, 0 ] }
   } }
 ] )
```

Output:

```json
[ { fsyncLocked: true }, { fsyncUnlocked: false } ]
```

**Step 4: Back up the Primary Config Server**

**Note:**

Backing up a config server backs
up the sharded cluster's metadata. You only need to back up one
config server, as they all hold the same data. Perform this step
against the CSRS primary member.

To create a filesystem snapshot of the config server, follow the
procedure in lvm-backup-operation.

**Step 5: Back up the Primary Shards**

Perform a filesystem snapshot against the primary member of each shard,
using the procedure found in backup-restore-filesystem-snapshots.

**Step 6: Unlock the Cluster**

After the backup completes, you must unlock the cluster to allow writes
to resume.

To unlock the cluster, use the `db.fsyncUnlock` method:

```bash
db.getSibling("admin").fsyncUnlock()
```

Run the following aggregation pipeline on both `mongos` and
the primary `mongod` of the config servers. To confirm the
unlock, ensure that the `fysncLocked` field returns `false` and
`fsyncUnlocked` field returns `true`.

```javascript
db.getSiblingDB("admin").aggregate( [
   {  $currentOp: { } },
   {  $facet: {
      "locked": [
         { $match: { $and: [
            { fsyncLock: { $exists: true } }
         ] } }],
       "unlocked": [
         { $match: { fsyncLock: { $exists: false } } }
       ]
   } },
   { $project: {
      "fsyncLocked": { $gt: [ { $size: "$locked" }, 0 ] },
      "fsyncUnlocked": { $gt: [ { $size: "$unlocked" }, 0 ] }
   } }
 ] )
```

Output:

```json
[ { fsyncLocked: false }, { fsyncUnlocked: true } ]
```

**Step 7: Restart the Balancer**

To restart the balancer, use the `sh.startBalancer` method:

```javascript
sh.startBalancer()
```

To confirm that the balancer is running, use the
`sh.getBalancerState` method:

```javascript
sh.getBalancerState()
```

Output:

```javascript
true
```

The command returns `true` when the balancer is running.
