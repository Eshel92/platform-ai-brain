<!-- Converted from core/inmemory.txt (reStructuredText). Includes are inlined. -->

# In-Memory Storage Engine for Self-Managed Deployments

The in-memory storage engine is included in MongoDB Enterprise. It is not 
available for MongoDB Community Edition.

Other than some metadata and diagnostic data, the in-memory storage engine does
not maintain any on-disk data, including configuration data, indexes, user
credentials, etc. By avoiding disk I/O, the in-memory storage engine allows for
more predictable latency of database operations.

## Specify In-Memory Storage Engine

To select the in-memory storage engine, specify:

- `inMemory` for the `--storageEngine` option, or the
  `storage.engine` setting if using a configuration file.

- `--dbpath`, or `storage.dbPath` if using a configuration
  file. Although the in-memory storage engine does not write data to
  the filesystem, it maintains in the `--dbpath` small metadata files
  and diagnostic data as well temporary files for building large
  indexes.

For example, from the command line:

```bash
mongod --storageEngine inMemory --dbpath <path> 
```

Or, if using the YAML configuration file format:

```yaml
storage:
   engine: inMemory
   dbPath: <path>
```

See cli-mongod-inmemory for configuration options specific to
this storage engine. Most `mongod` configuration options are
available for use with in-memory storage engine except for those
options that are related to data persistence, such as journaling or
encryption at rest configuration.

**Warning:**

The in-memory storage engine does not persist data after process shutdown.

## Transaction (Read and Write) Concurrency

Starting in version 7.0, MongoDB uses a default algorithm to dynamically
adjust the maximum number of concurrent storage engine transactions, 
or read and write tickets. The dynamic concurrent storage engine
transaction algorithm optimizes database throughput during cluster 
overload. 

**Note:**

The dynamic algorithm also results in lower overall ticket usage, even
under normal conditions, because the algorithm starts with a much
lower baseline number of available tickets. As a result, when upgrading to
MongoDB 7.0, you may observe a significant drop in ticket usage, which is
expected behavior.

The maximum number of concurrent storage engine transactions,
or read and write tickets, never exceeds 128 read tickets and 128
write tickets and may differ across nodes in a cluster. The maximum
number of read tickets and write tickets within a single node are always
equal. 

To specify a maximum number of read and write transactions, or read and
write tickets, that the dynamic maximum can not exceed, use
`storageEngineConcurrentReadTransactions` and
`storageEngineConcurrentWriteTransactions`.

If you want to disable the dynamic concurrent storage engine
transactions algorithm, file a support request to work with a MongoDB
Technical Services Engineer. 

## Document Level Concurrency

The in-memory storage engine uses *document-level* concurrency control for write
operations. As a result, multiple clients can modify different
documents of a collection at the same time.

## Memory Use

In-memory storage engine requires that all its data (including indexes,
oplog if `mongod` instance is part of a replica set, etc.) must
fit into the specified `--inMemorySizeGB` command-line option
or `storage.inMemory.engineConfig.inMemorySizeGB` setting in
the YAML configuration file.

By default, the in-memory storage engine uses 50% of physical RAM minus
1 GB.

If a write operation would cause the data to exceed the specified
memory size, MongoDB returns with the error:

```bash
"WT_CACHE_FULL: operation would overflow cache"
```

To specify a new size, use the
`storage.inMemory.engineConfig.inMemorySizeGB` setting in the
YAML configuration file format:

```yaml
storage:
   engine: inMemory
   dbPath: <path>
   inMemory:
      engineConfig:
         inMemorySizeGB: <newSize>
```

Or use the command-line option `--inMemorySizeGB`:

```bash
mongod --storageEngine inMemory --dbpath <path> --inMemorySizeGB <newSize>
```

## Durability

The in-memory storage engine is non-persistent and does not write data
to a persistent storage. Non-persisted data includes
application data and system data, such as users, permissions, indexes,
replica set configuration, sharded cluster configuration, etc.

As such, the concept of journal or waiting for data to become
durable does not apply to the in-memory storage engine.

If any voting member of a replica set uses the in-memory
storage engine, you must set
`writeConcernMajorityJournalDefault` to `false`.

**Note:**

Starting in version 4.2 (and 4.0.13 and 3.6.14 ), if a replica set
member uses the in-memory storage engine
(voting or non-voting) but the replica set has
`writeConcernMajorityJournalDefault` set to true, the
replica set member logs a startup warning.

With `writeConcernMajorityJournalDefault` set to `false`,
MongoDB does not wait for `w: "majority"`
writes to be written to the on-disk journal before acknowledging the
writes. As such, `"majority"` write operations could
possibly roll back in the event of a transient loss (e.g. crash and
restart) of a majority of nodes in a given replica set.

Write operations that specify a write concern `journaled` are acknowledged immediately. When an `mongod` instance
shuts down, either as result of the `shutdown` command or
due to a system error, recovery of in-memory data is impossible.

## Transactions

Transactions are supported on replica sets
and sharded clusters where:

- the primary uses the WiredTiger storage
  engine, and

- the secondary members use either the WiredTiger storage engine or the
  in-memory storage engines.

**Note:**

You cannot run transactions on a sharded cluster that has a shard
with `writeConcernMajorityJournalDefault` set to
`false`, such as a shard with a voting member that uses the
in-memory storage engine.

## Deployment Architectures

In addition to running as standalones, `mongod` instances that
use in-memory storage engine can run as part of a replica set or part
of a sharded cluster.

### Replica Set

You can deploy `mongod` instances that use in-memory storage
engine as part of a replica set. For example, as part of a three-member
replica set, you could have:

- two `mongod` instances run with in-memory storage engine.

- one `mongod` instance run with WiredTiger storage engine. Configure the WiredTiger member
  as a hidden member (i.e. `hidden: true`
  and `priority: 0`).

With this deployment model, only the `mongod` instances
running with the in-memory storage engine can become the primary.
Clients connect only to the in-memory storage engine `mongod`
instances. Even if both `mongod` instances running in-memory
storage engine crash and restart, they can sync from the member running
WiredTiger. The hidden `mongod` instance running with
WiredTiger persists the data to disk, including the user data, indexes,
and replication configuration information.

**Note:**

In-memory storage engine requires that all its data (including oplog
if `mongod` is part of replica set, etc.) fit into the
specified `--inMemorySizeGB` command-line option or
`storage.inMemory.engineConfig.inMemorySizeGB` setting. See
inmemory-memory-use.

### Sharded Cluster

You can deploy `mongod` instances that use an in-memory 
storage engine as part of a sharded cluster. The in-memory 
storage engine avoids disk I/O to allow for more
predictable database operation latency. In a sharded cluster, a 
shard can consist of a single `mongod` instance or a 
replica set. For example, you could have one shard that 
consists of the following replica set:

- two `mongod` instances run with in-memory storage engine

- one `mongod` instance run with WiredTiger storage engine. Configure the WiredTiger member
  as a hidden member (i.e. `hidden: true`
  and `priority: 0`).

To this shard, add the `tag` `inmem`. For
example, if this shard has the name `shardC`, connect to the
`mongos` and run `sh.addShardTag()`.

For example, 

```javascript
sh.addShardTag("shardC", "inmem")
```

To the other shards, add a separate tag `persisted` .

```javascript
sh.addShardTag("shardA", "persisted")
sh.addShardTag("shardB", "persisted")
```

For each sharded collection that should reside on the `inmem` shard,
`assign to the entire chunk range` the tag
`inmem`:

```javascript
sh.addTagRange("test.analytics", { shardKey: MinKey }, { shardKey: MaxKey }, "inmem")
```

For each sharded collection that should reside across the
`persisted` shards, `assign to the entire chunk range` the tag
`persisted`:

```javascript
sh.addTagRange("salesdb.orders", { shardKey: MinKey }, { shardKey: MaxKey }, "persisted")
```

For the `inmem` shard, create a database or move the database.

**Note:**

Read concern level `"snapshot"` is not officially supported
with the in-memory storage engine.
