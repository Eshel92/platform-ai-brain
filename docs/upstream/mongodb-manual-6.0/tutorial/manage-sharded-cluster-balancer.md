<!-- Converted from tutorial/manage-sharded-cluster-balancer.txt (reStructuredText). Includes are inlined. -->

# Manage Sharded Cluster Balancer

**Changed in version:** 6.0

This page describes common administrative procedures related
to balancing. For an introduction to balancing, see
sharding-balancing. For lower level information on balancing, see
sharding-balancing-internals.

The balancer process has moved from the `mongos` instances
to the primary member of the config server replica set.

## Check the Balancer State

`sh.getBalancerState()` checks if the balancer is enabled 
(i.e. that the balancer is permitted to run). 
`sh.getBalancerState()` does not check if the balancer is 
actively migrating data.

To see if the balancer is enabled in your sharded cluster,
run the following command, which returns a boolean:

```javascript
sh.getBalancerState()
```

You can also see if the balancer is enabled using `sh.status()`.
The `currently-enabled` field indicates
whether the balancer is enabled, and the
`currently-running` field indicates if the
balancer is currently running.

## Check if Balancer is Running

To see if the balancer process is active in your cluster:

#. Connect to any `mongos` in the cluster using the
   `mongosh` shell.

#. Use the following operation to determine if the balancer is running:

   ```javascript
   sh.isBalancerRunning()
   ```

## Configure Default Range Size

The default range size for a sharded cluster is 128 megabytes. In most
situations, the default size is appropriate for splitting and migrating
chunks. For information on how range size affects deployments, see
details, see sharding-range-size.

Changing the default range size affects ranges that are processes during
migrations and auto-splits but does not retroactively affect all ranges.

Changing the default chunk size affects chunks that are processes during
migrations and auto-splits but does not retroactively affect all chunks.

Starting in MongoDB 6.0.3, automatic chunk splitting is not performed. 
This is because of balancing policy improvements. Auto-splitting commands 
still exist, but do not perform an operation. For details, see
release-notes-6.0-balancing-policy-changes.

To configure default range size, see 
tutorial-modifying-chunk-size.

## Schedule the Balancing Window

In some situations, particularly when your data set grows slowly and a
migration can impact performance, it is useful to ensure
that the balancer is active only at certain times. The following
procedure specifies the `activeWindow`, 
which is the timeframe during which the balancer will
be able to migrate chunks:

**Step 1: Connect to `mongos` using `mongosh`.**

You can connect to any `mongos` in the cluster.

**Step 2: Switch to the config-database.**

Issue the following command to switch to the config database.

```sh
use config
```

**Step 3: Ensure that the balancer is not `stopped`.**

The balancer will not activate in the `stopped` state.
To ensure that the  balancer
is not `stopped`, use `sh.startBalancer()`,
as in the following:

```sh
sh.startBalancer()
```

The balancer will not start if you are outside
of the `activeWindow` timeframe.

Starting in MongoDB 6.0.3, automatic chunk splitting is not performed. 
This is because of balancing policy improvements. Auto-splitting commands 
still exist, but do not perform an operation. For details, see
release-notes-6.0-balancing-policy-changes.

In MongoDB versions earlier than 6.0.3, `sh.startBalancer()`
also enables auto-splitting for the sharded cluster.

**Step 4: Modify the balancer's window.**

Set the `activeWindow` using `updateOne()`,
as in the following:

```sh
db.settings.updateOne(
   { _id: "balancer" },
   { $set: { activeWindow : { start : "<start-time>", stop : "<stop-time>" } } },
   { upsert: true }
)
```

Replace `<start-time>` and `<end-time>` with time values using
two digit hour and minute values (i.e. `HH:MM`) that specify the
beginning and end boundaries of the balancing window.

- For `HH` values, use hour values ranging from `00` - `23`.
- For `MM` value, use minute values ranging from `00` - `59`.

For on-premises or self-managed sharded clusters, MongoDB evaluates the 
start and stop times relative to the time zone of the primary member in 
the config server replica set.

For Atlas clusters, MongoDB evaluates the start and stop times 
relative to the UTC timezone. 

**Note:**

The balancer window must be sufficient to *complete* the
migration of all data inserted during the day.

As data insert rates can change based on activity and usage
patterns, it is important to ensure that the balancing window
you select will be sufficient to support the needs of your
deployment.

## Remove a Balancing Window Schedule

If you have set the balancing window and wish to remove the schedule
so that the balancer is always running, use `$unset` to clear
the `activeWindow`, as in the following:

```javascript
use config
db.settings.updateOne( { _id : "balancer" }, { $unset : { activeWindow : true } } )
```

## Disable the Balancer

**Important:**

Leaving the balancer disabled for extended periods of time can lead to
unbalanced shards, which degrade cluster performance. Only disable the
balancer if necessary, and ensure that you re-enable the balancer when maintenance is complete.

By default, the balancer may run at any time and only moves chunks as
needed. To disable the balancer for a short period of time and prevent
all migration, use the following procedure:

#. Connect to any `mongos` in the cluster using the
   `mongosh` shell.

#. Issue the following operation to disable the balancer:

   ```javascript
   sh.stopBalancer()
   ```

   If a migration is in progress, the system will complete the
   in-progress migration before stopping.
   

   Starting in MongoDB 6.0.3, automatic chunk splitting is not performed. 
   This is because of balancing policy improvements. Auto-splitting commands 
   still exist, but do not perform an operation. For details, see
   release-notes-6.0-balancing-policy-changes.

   In MongoDB versions earlier than 6.0.3, `sh.stopBalancer()`
   also disables auto-splitting for the sharded cluster.

#. To verify that the balancer won't start, run the following command,
   which returns `false` if the balancer is disabled:

   ```javascript
   sh.getBalancerState()
   ```

   Optionally, to verify no migrations are in progress after disabling,
   run the following operation in the `mongosh` shell:

   ```javascript
   use config
   while( sh.isBalancerRunning() ) {
             print("waiting...");
             sleep(1000);
   }
   ```

**Note:**

To disable the balancer from a driver,
use the `balancerStop` command against the `admin` database,
as in the following:

```javascript
db.adminCommand( { balancerStop: 1 } )
```

## Enable the Balancer

Use this procedure if you have disabled the balancer and are ready to
re-enable it:

#. Connect to any `mongos` in the cluster using the
   `mongosh` shell.

#. Issue one of the following operations to enable the balancer:

   From the `mongosh` shell, run:

   ```javascript
   sh.startBalancer()
   ```

   **Note:**

   To enable the balancer from a driver, use the `balancerStart`
   command against the `admin` database, as in the following:

   ```javascript
   db.adminCommand( { balancerStart: 1 } )
   ```

   Starting in MongoDB 6.0.3, automatic chunk splitting is not performed. 
   This is because of balancing policy improvements. Auto-splitting commands 
   still exist, but do not perform an operation. For details, see
   release-notes-6.0-balancing-policy-changes.

   In MongoDB versions earlier than 6.0.3, `sh.startBalancer()`
   also enables auto-splitting for the sharded cluster.

## Disable Balancing During Backups

**Note:**

Disabling the balancer is only necessary when **manually** taking backups,
either by calling `mongodump` or scheduling a task that calls
`mongodump` at a specific time.

You do **not** have to disable the balancer when using coordinated backup
and restore processes:

- [MongoDB Atlas](https://www.mongodb.com/atlas/database?tck=docs_server)

- [MongoDB Cloud Manager](https://www.mongodb.com/cloud/cloud-manager?tck=docs_server)

- [MongoDB Ops Manager](https://www.mongodb.com/products/ops-manager?tck=docs_server)

If MongoDB migrates a chunk during a backup, you can end with an inconsistent snapshot
of your sharded cluster. Never run a backup while the balancer is
active. To ensure that the balancer is inactive during your backup
operation:

- Set the balancing window
  so that the balancer is inactive during the backup. Ensure that the
  backup can complete while you have the balancer disabled.

- manually disable the balancer
  for the duration of the backup procedure.

If you turn the balancer off while it is in the middle of a balancing round,
the shut down is not instantaneous. The balancer completes the chunk
move in-progress and then ceases all further balancing rounds.

Before starting a backup operation, confirm that the balancer is not
active. You can use the following command to determine if the balancer
is active:

```javascript
!sh.getBalancerState() && !sh.isBalancerRunning()
```

When the backup procedure is complete you can reactivate
the balancer process.

## Disable Balancing on a Collection

You can disable balancing for a specific collection with the
`sh.disableBalancing()` method. You may want to disable the
balancer for a specific collection to support maintenance operations or
atypical workloads, for example, during data ingestions or data exports.

When you disable balancing on a collection, MongoDB will not interrupt in
progress migrations.

To disable balancing on a collection, connect to a `mongos`
with the `mongosh` shell and call the
`sh.disableBalancing()` method.

For example:

```javascript
sh.disableBalancing("students.grades")
```

The `sh.disableBalancing()` method accepts as its parameter the
full namespace of the collection.

## Enable Balancing on a Collection

You can enable balancing for a specific collection with the
`sh.enableBalancing()` method.

When you enable balancing for a collection, MongoDB will not *immediately*
begin balancing data. However, if the data in your sharded collection is
not balanced, MongoDB will be able to begin distributing the data more
evenly.

To enable balancing on a collection, connect to a `mongos`
with the `mongosh` shell and call the
`sh.enableBalancing()` method.

For example:

```javascript
sh.enableBalancing("students.grades")
```

The `sh.enableBalancing()` method accepts as its parameter the
full namespace of the collection.

## Confirm Balancing is Enabled or Disabled

To confirm whether balancing for a collection is enabled or disabled,
query the `collections` collection in the `config` database for the
collection namespace and check the `noBalance` field. For
example:

```javascript
db.getSiblingDB("config").collections.findOne({_id : "students.grades"}).noBalance;
```

This operation will return a null error, `true`, `false`, or no output:

- A null error indicates the collection namespace is incorrect.

- If the result is `true`, balancing is disabled.

- If the result is `false`, balancing is enabled currently but has been
  disabled in the past for the collection. Balancing of this collection
  will begin the next time the balancer runs.

- If the operation returns no output, balancing is enabled currently and
  has never been disabled in the past for this collection. Balancing of
  this collection will begin the next time the balancer runs.

You can also see if the balancer is enabled using `sh.status()`.
The `currently-enabled` field indicates if the
balancer is enabled.

## Change Replication Behavior for Chunk Migration

### Secondary Throttle

During chunk migration, the `_secondaryThrottle` value determines
when the migration proceeds with next document in the chunk.

In the `config.settings` collection:

- If the `_secondaryThrottle` setting for the balancer is set to a
  write concern, each document moved during chunk migration must receive
  the requested acknowledgment before proceeding with the next
  document.

- If the `_secondaryThrottle` setting is unset, the migration process
  does not wait for replication to a secondary and instead continues
  with the next document.
  
  This is the default behavior for WiredTiger. 

To change the `_secondaryThrottle` setting, connect to a
`mongos` instance and directly update the
`_secondaryThrottle` value in the `settings` collection
of the config database. For example, from a
`mongosh` shell connected to a `mongos`, run
the following command:

```javascript
use config
db.settings.updateOne(
   { "_id" : "balancer" },
   { $set : { "_secondaryThrottle" : { "w": "majority" }  } },
   { upsert : true }
)
```

The effects of changing the `_secondaryThrottle` setting may not be
immediate. To ensure an immediate effect, stop and restart the balancer
to enable the selected value of `_secondaryThrottle`.

For more information on the replication behavior during various steps
of chunk migration, see chunk-migration-replication.

- Use the `moveRange` command's `secondaryThrottle` and 
  `writeConcern` options to specify the behavior during the command. 

- Use the `moveChunk` command's `_secondaryThrottle` and 
  `writeConcern` options to specify the behavior during the command. 

For details, see `moveRange` and `moveChunk`.

### Wait for Delete

The `_waitForDelete` setting of the balancer and the
`moveChunk` command affects how the balancer migrates
multiple chunks from a shard. Similarly, the `_waitForDelete` setting 
of the balancer and the `moveRange` command also affect how 
the balancer migrates multiple chunks from a shard. By default, the 
balancer does not wait for the on-going migration's delete phase to 
complete before starting the next chunk migration. To have the delete 
phase **block** the start of the next chunk migration, you can set the 
`_waitForDelete` to true.

For details on chunk migration, see sharding-chunk-migration.
For details on the chunk migration queuing behavior, see
chunk-migration-queuing.

**Important:**

When the `_waitForDelete` field is set, MongoDB does not wait on the 
`orphanCleanupDelaySecs` delay before performing the range 
deletion. If you use the `_waitForDelete` parameter and have any
read operations occurring on secondaries, the read may miss documents 
due to the migration's delete phase. 

To change the balancer's `_waitForDelete` value:

#. Connect to a `mongos` instance.

#. Update the `_waitForDelete` value in the `settings`
   collection of the config database. For
   example:

   ```javascript
   use config
   db.settings.updateOne(
      { "_id" : "balancer" },
      { $set : { "_waitForDelete" : true } },
      { upsert : true }
   )
   ```

Once set to `true`, to revert to the default behavior:

#. Connect to a `mongos` instance.

#. Update or unset the `_waitForDelete` field in the
   `settings` collection of the config database:

   ```javascript
   use config
   db.settings.updateOne(
      { "_id" : "balancer", "_waitForDelete": true },
      { $unset : { "_waitForDelete" : "" } }
   )
   ```

### Balance Ranges that Exceed Size Limit

By default, MongoDB cannot move a range if the number of documents in
the range is greater than 2 times the result of dividing the
configured range size by the average
document size.

By specifying the balancer setting `attemptToBalanceJumboChunks` to `true`, 
the balancer can migrate these large ranges as long as they have not been 
labeled as jumbo. 

To set the balancer's `attemptToBalanceJumboChunks` setting, connect
to a `mongos` instance and directly update the
`config.settings` collection. For example, from a
`mongosh` shell connected to a `mongos`
instance, run the following command:

```javascript
db.getSiblingDB("config").settings.updateOne(
   { _id: "balancer" },
   { $set: { attemptToBalanceJumboChunks : true } },
   { upsert: true }
)
```

If the range you want to move is labeled `jumbo`, you can
manually clear the jumbo flag to
have the balancer attempt to migrate the range.

You can also manually migrate ranges that exceed the size limit 
(with or without the `jumbo` label) using either:

- the `moveRange` command with the 
  forceJumbo: true option
- the `moveChunk` command with the
  forceJumbo: true option

However, when you run `moveRange` or `moveChunk`
with `forceJumbo: true`, write operations to the collection may block 
for a long period of time during the migration.

## Change the Maximum Storage Size for a Given Shard

By default shards have no constraints in storage size. However, you can set a
maximum storage size for a given shard in the sharded cluster. When 
selecting potential destination shards, the balancer ignores shards 
where a migration would exceed the configured maximum storage size.

The `shards` collection in the config
database stores configuration data related to shards. 

```javascript
{ "_id" : "shard0000", "host" : "shard1.example.com:27100" }
{ "_id" : "shard0001", "host" : "shard2.example.com:27200" }
```

   
To limit the storage size for a given shard, use the
`db.collection.updateOne()` method with the `$set` operator to
create the `maxSize` field and assign it an `integer` value. The
`maxSize` field represents the maximum storage size for the shard in
`megabytes`.

The following operation sets a maximum size on a shard of `1024 megabytes`:

```javascript
config = db.getSiblingDB("config")
config.shards.updateOne( { "_id" : "<shard>"}, { $set : { "maxSize" : 1024 } } )
```

This value includes the mapped size of *all* data files on the
shard, including the `local` and `admin` databases.

By default, `maxSize` is not specified, allowing shards to consume the
total amount of available space on their machines if necessary.

You can also set `maxSize` when adding a shard.

To set `maxSize` when adding a shard, set the `addShard`
command's `maxSize` parameter to the maximum size in `megabytes`. The
following command run in the `mongosh` shell adds a shard 
with a maximum size of 125 megabytes:

```javascript
config = db.getSiblingDB("config")
config.runCommand( { addshard : "example.net:34008", maxSize : 125 } )
```
