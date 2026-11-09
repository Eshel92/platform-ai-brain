<!-- Converted from tutorial/backup-sharded-cluster-with-database-dumps.txt (reStructuredText). Includes are inlined. -->

# Back Up a Self-Managed Sharded Cluster with a Database Dump

Starting in MongoDB 7.1 (also available starting in 7.0.2,
6.0.11, and 5.0.22), you can back up data on sharded clusters
using `mongodump`.

## About this Task

`mongodump` is a utility that creates a binary export of database
content. You can use the `mongodump` utility to take self-managed backups of
a sharded cluster.

To back up a sharded cluster with `mongodump`, you must stop
the balancer, stop writes, and stop any schema transformation
operations on the cluster. This helps reduce the likelihood of
inconsistencies in the backup.

MongoDB provides backup and restore operations that can run with the balancer
and running transactions through the following services:

- [MongoDB Atlas](https://www.mongodb.com/atlas/database?tck=docs_server)

- [MongoDB Cloud Manager](https://www.mongodb.com/cloud/cloud-manager?tck=docs_server)

- [MongoDB Ops Manager](https://www.mongodb.com/products/ops-manager?tck=docs_server)

### Stale Backups

Backups provide a snapshot of the current state of the database.
When you restore from a backup, the restored database doesn't
include any changes made after the backup was taken, which can
result in data loss.

## Before you Begin

This task uses `mongodump` to back up a sharded cluster. Ensure
that you have a cluster running that contains data in sharded collections.

### Version Compatibility

This procedure requires a version of MongoDB that supports fsync
locking from `mongos`.

   `fsyncUnlock` commands

Starting in MongoDB 6.0.11 (also available starting in
5.0.22) the `fsync` and can run on
`mongos` to lock and unlock a sharded cluster.

### Admin Privileges

To use this procedure, your MongoDB user must have the
`fsync` authorization, which can be available
through a custom role or using the built-in
`hostManager` role.

With this authorization you can run the `fsync`
and `fsyncUnlock` commands.

## Steps

To take a self-managed backup of a sharded cluster, complete the following
steps:

**Step 1: Find a Backup Window**

To find a good time to perform a backup, monitor your
application and database usage to find a time when chunk
migrations, resharding, and schema transformation
operations are unlikely to occur. 

**Note:**

These steps can only produce a consistent backup if
they are followed exactly and no operations are in
progress when you begin.

For more information, see sharded-schedule-backup.

**Step 2: Stop the Balancer**

To prevent chunk migrations from disrupting the backup, connect to
`mongos` and use the `sh.stopBalancer` method to stop
the balancer:

```javascript
sh.stopBalancer()
```

If a balancing round is in progress, the operation waits for balancing to
complete.

To verify that the balancer is stopped, use the
`sh.getBalancerState` method:

```javascript
use config
while( sh.isBalancerRunning().mode != "off" ) {
   print( "Waiting for Balancer to stop..." );
   sleep( 1000 );
} 
```

**Step 3: Lock the Cluster**

The sharded cluster must remain locked during the backup process to protect
the database from writes, which may cause inconsistencies in the backup.

To lock a sharded cluster, connect to `mongos` and use the
`db.fsyncLock` method:

```javascript
db.getSiblingDB("admin").fsyncLock()
```

To confirm the lock, on `mongos` and the primary
`mongod` of the config servers, run the following
aggregation pipeline and ensure that all the shards are
locked:

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

**Step 4: Take Backup**

To back up the sharded cluster, use `mongodump` to connect to
`mongos` and perform the backup:

```bash
mongodump \
   --host mongos.example.net \
   --port 27017 \
   --username user \
   --password "passwd" \
   --out /opt/backups/example-cluster-1
```

**Step 5: Unlock the Cluster**

After the backup completes, you can unlock the cluster to allow writes
to resume.

To unlock the cluster, use the `db.fsyncUnlock` method:

```bash
db.getSibling("admin").fsyncUnlock()
```

To confirm the unlock, on `mongos` and the primary
`mongod` of the config servers, run the following
aggregation pipeline and ensure that all shards are unlocked:

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

**Step 6: Restart the Balancer**

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

## Next Steps

You can restore data from a `mongodump` backup using `mongorestore`.

- To migrate to a replica set or standalone server, execute `mongorestore`
  against `mongod`.

- To restore to a sharded cluster, execute `mongorestore` against
  `mongos` with `--nsExclude` set
  to exclude the `config` database: 

  ```sh
  mongorestore --nsExclude='config.*' /data/backup 
  ```

**Important:**

`mongorestore` does not shard restored collections on the destination cluster. 

To ensure that a restored collection is sharded on the destination cluster, 
create a collection with the same namespace on the destination cluster then 
shard the collection before running `mongorestore`.
The balancer will eventually spread the restored documents
across the shards of the destination cluster. 

For more information, see manual-tutorial-backup-and-restore.
