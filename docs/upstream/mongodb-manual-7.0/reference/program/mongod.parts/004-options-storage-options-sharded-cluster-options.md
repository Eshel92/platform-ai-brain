<!-- Part 4 of 6 of reference/program/mongod.md (split because the page is big). -->

### Storage Options

**`--storageEngine string`**

*Default*: `wiredTiger`

Specifies the storage engine for the `mongod` database. Available
values include:

| Value | Description |
|---|---|
| `wiredTiger` | To specify the /core/wiredtiger. |
| `inMemory` | To specify the /core/inmemory. *Available in MongoDB Enterprise only.* |

If you attempt to start a `mongod` with a
`--dbpath` that contains data files produced by a
storage engine other than the one specified by
`--storageEngine`, `mongod` doesn't start.

**`--dbpath <path>`**

*Default*: `/data/db` on Linux and macOS, `\data\db` on Windows

The directory where the `mongod` instance stores its data.

If using the default
Configuration File
included with a package manager installation of MongoDB, the
corresponding `storage.dbPath` setting uses a different
default.

The files in `--dbpath` must correspond to the storage engine
specified in `--storageEngine`. If the data files do not
correspond to `--storageEngine`, `mongod` doesn't start.

**`--directoryperdb`**

Uses a separate directory to store data for each database. The
directories are under the `--dbpath` directory, and each subdirectory
name corresponds to the database name.

Not available for `mongod` instances that use the
in-memory storage engine.

Starting in MongoDB 5.0, dropping the final collection in a database
(or dropping the database itself) when `--directoryperdb` is
enabled deletes the newly empty subdirectory for that database.

To change the `--directoryperdb` option for existing
deployments:

- For standalone instances:

  #. Use `mongodump` on the existing
     `mongod` instance to generate a backup.
  #. Stop the `mongod` instance.
  #. Add the `--directoryperdb` value **and**
     configure a new data directory
  #. Restart the `mongod` instance.
  #. Use `mongorestore` to populate the new data
     directory.

- For replica sets:

  #. Stop a secondary member.
  #. Add the `--directoryperdb` value **and**
     configure a new data directory to that secondary member.
  #. Restart that secondary.
  #. Use initial sync to populate
     the new data directory.
  #. Update remaining secondaries in the same fashion.
  #. Step down the primary, and update the stepped-down member in the
     same fashion.

**`--syncdelay <value>`**

*Default*: 60

Controls how much time can pass before MongoDB flushes data to the data
files.

**Do not set this value on
production systems.** In almost every situation, you should use the
default setting.

The `mongod` process writes data very quickly to the journal and
lazily to the data files. `--syncdelay` has no effect on 
journaling, but if `--syncdelay` is set to 
`0` the journal eventually consumes all available disk space.

Not available for `mongod` instances that use the
in-memory storage engine.

To provide durable data, WiredTiger
uses checkpoints. For more
details, see journaling-wiredTiger.

**`--upgrade`**

Upgrades the on-disk data format of the files specified by the
`--dbpath` to the latest version, if needed.

This option only affects the operation of the `mongod` if the data
files are in an old format.

In most cases you should not set this value, so you can exercise the
most control over your upgrade process. See the MongoDB release notes
for more information about the upgrade process.

**`--repair`**

Runs a repair routine on all databases for a `mongod`
instance.

Starting in MongoDB 5.0:

- The repair operation validates the collections to find any
  inconsistencies and fixes them if possible, which avoids
  rebuilding the indexes.

- If a collection's data file is salvaged or if the collection has
  inconsistencies that the validate step is unable to fix, then all
  indexes are rebuilt.

**Tip:**

If you are running with journaling enabled, there is
almost never any need to run repair since the server can use the
journal files to restore the data files to a clean state automatically.
However, you may need to run repair in cases where you need to recover
from a disk-level data corruption.

**Warning:**

- Only use `mongod --repair` if you have no other options.
  The operation removes and does not save any corrupt data during
  the repair process.

- Avoid running `--repair` against
  a replica set member:

  - To repair a replica set member, if you have an intact
    copy of your data available (e.g. a recent backup or an intact
    member of the replica set), restore from that intact
    copy instead. To learn more, see resync-replica-member.

  - If you choose to run `mongod --repair` against a
    replica set member and the operation modifies the data or the
    metadata, you must still perform a full resync in order for the
    member to rejoin the replica set.

- Before using `--repair`, make a backup
  copy of the `dbpath` directory.

- If repair fails to complete for any reason, you must restart the
  instance using the `--repair` option.

**`--journalCommitInterval <value>`**

*Default*: 100

The maximum amount of time in milliseconds that
the `mongod` process allows between
journal operations. Values can range from 1 to 500 milliseconds. Lower
values increase the durability of the journal, at the expense of disk
performance.

On WiredTiger, the default journal commit interval is 100
milliseconds. A write that includes or implies
`j:true` causes an immediate sync of the journal. For details
and additional conditions that affect the frequency of the sync, see
journal-process.

Not available for `mongod` instances that use the
in-memory storage engine.


### WiredTiger Options

**`--wiredTigerCacheSizeGB <float>`**

Defines the maximum size of the internal cache that WiredTiger
uses for all data. The memory consumed by an index build (see
`maxIndexBuildMemoryUsageMegabytes`) is separate from the
WiredTiger cache memory. 

Values can range from `0.25` GB to `10000` GB.

#### Cache Configuration Settings

The default WiredTiger internal cache size is the larger of either:

- 50% of (RAM - 1GB), or

- 0.256 GB.

For example, on a system with a total of 4GB of RAM the
WiredTiger cache uses 1.5GB of RAM (``0.5 * (4GB - 1GB) =
1.5 GB``). When providing a specific cache size ensure the RAM does not 
exceed the bounds of 0.256GB to 10000GB. 

**Note:**

In some instances, such as when running in a container that is configured
to use less RAM than the amount of memory provisioned for the host, you
must account for the limits. You may need to configure the WiredTiger cache
to an appropriate value, as WiredTiger may not account for the memory 
limits of the specific container in certain cases. 

To view the `memory limit`, the value
that WiredTiger utilizes as the maximum amount of RAM available use the
`hostInfo` command. 

With WiredTiger, MongoDB utilizes both the WiredTiger internal cache
and the filesystem cache.

With the filesystem cache, MongoDB automatically uses all free memory
that is not used by the WiredTiger cache or by other processes.

**Note:**

The `--wiredTigerCacheSizeGB` limits the size of the WiredTiger internal
cache. The operating system uses the available free memory
for filesystem cache, which allows the compressed MongoDB data
files to stay in memory. In addition, the operating system 
uses any free RAM to buffer file system blocks and file system
cache.

To accommodate the additional consumers of RAM, you may have to
decrease WiredTiger internal cache size.

The default WiredTiger internal cache size value assumes that there is a
single `mongod` instance per machine. If a single machine
contains multiple MongoDB instances, then you should decrease the setting to
accommodate the other `mongod`
instances.

If you run `mongod` in a container (for example, `lxc`,
`cgroups`, Docker, etc.) that does *not* have access to all of the
RAM available in a system, you must set `--wiredTigerCacheSizeGB` 
to a value less than the amount of RAM available in the container. The exact
amount depends on the other processes running in the container. See
`memLimitMB`.

**`--wiredTigerJournalCompressor <compressor>`**

*Default*: snappy

Specifies the type of compression to use to compress WiredTiger
journal data.

Available compressors are:

- `none`

- snappy

- zlib

- zstd

**`--wiredTigerDirectoryForIndexes`**

When you start `mongod` with `--wiredTigerDirectoryForIndexes`, `mongod` stores indexes and collections in separate
subdirectories under the data (i.e. `--dbpath`) directory.
Specifically, `mongod` stores the indexes in a subdirectory named
`index` and the collection data in a subdirectory named
`collection`.

By using a symbolic link, you can specify a different location for
the indexes. Specifically, when `mongod` instance is **not**
running, move the `index` subdirectory to the destination and
create a symbolic link named `index` under the data directory to
the new destination.

**`--wiredTigerCollectionBlockCompressor <compressor>`**

*Default*: snappy

Specifies the default compression for collection data. You can
override this on a per-collection basis when creating collections.

Available compressors are:

- `none`

- snappy

- zlib

- zstd

`--wiredTigerCollectionBlockCompressor` affects all collections created. If you change
the value of `--wiredTigerCollectionBlockCompressor` on an existing MongoDB deployment, all new
collections use the specified compressor. Existing collections
continue to use the compressor specified when they were
created, or the default compressor at that time.

**`--wiredTigerIndexPrefixCompression <boolean>`**

*Default*: true

Enables or disables prefix compression for index data.

Specify `true` for `--wiredTigerIndexPrefixCompression` to enable prefix compression for
index data, or `false` to disable prefix compression for index data.

The `--wiredTigerIndexPrefixCompression` setting affects all indexes created. If you change
the value of `--wiredTigerIndexPrefixCompression` on an existing MongoDB deployment, all new
indexes use prefix compression. Existing indexes
are not affected.


### Replication Options

**`--replSet <setname>`**

Configures replication. Specify a replica set name as an argument to
this set. All hosts in the replica set must have the same set name.

If your application connects to more than one replica set, each set must
have a distinct name. Some drivers group replica set connections by 
replica set name.

**`--oplogSize <value>`**

The maximum size in megabytes for the oplog. The
`oplogSize` setting configures the uncompressed size of the
oplog, not the size on disk.

**Note:**

The oplog can grow past its configured size
limit to avoid deleting the `majority commit point`.

By default, the `mongod` process creates an oplog based on
the maximum amount of space available. For 64-bit systems, the oplog
is typically 5% of available disk space.

Once the `mongod` has created the oplog for the first time,
changing the `--oplogSize` option doesn't affect the size of
the oplog. To change the minimum oplog retention period after
starting the `mongod`, use
`replSetResizeOplog`. `replSetResizeOplog`
enables you to resize the oplog dynamically without restarting the
`mongod` process. To persist the changes made using
`replSetResizeOplog` through a restart, update the value
of `--oplogSize`.

See replica-set-oplog-sizing for more information.

**`--oplogMinRetentionHours <value>`**

Specifies the minimum number of hours to preserve an oplog entry,
where the decimal values represent the fractions of an hour. For
example, a value of `1.5` represents one hour and thirty
minutes.

The value must be greater than or equal to `0`. A value of `0`
indicates that the `mongod` should truncate the oplog
starting with the oldest entries to maintain the configured
maximum oplog size.

Defaults to `0`.

A `mongod` started with `--oplogMinRetentionHours`
only removes an oplog entry *if*:

- The oplog has reached the maximum configured oplog size *and*

- The oplog entry is older than the configured number of hours based
  on the host system clock.

The `mongod` has the following behavior when configured
with a minimum oplog retention period:

- The oplog can grow without constraint so as to retain oplog entries
  for the configured number of hours. This may result in reduction or
  exhaustion of system disk space due to a combination of high write
  volume and large retention period.

- If the oplog grows beyond its maximum size, the
  `mongod` may continue to hold that disk space even if
  the oplog returns to its maximum size *or* is configured for a
  smaller maximum size. See replSetResizeOplog-cmd-compact.

- The `mongod` compares the system wall clock to an 
  oplog entry creation wall clock time when enforcing oplog entry
  retention. Clock drift between cluster components may result in
  unexpected oplog retention behavior. See
  production-notes-clock-synchronization for more information on
  clock synchronization across cluster members.

To change the minimum oplog retention period after starting the
`mongod`, use `replSetResizeOplog`.
`replSetResizeOplog` enables you to resize the oplog
dynamically without restarting the `mongod` process. To
persist the changes made using `replSetResizeOplog`
through a restart, update the value of 
`--oplogMinRetentionHours`.

**`--enableMajorityReadConcern`**

*Default*: true

Configures support for `"majority"` read concern.

Starting in MongoDB 5.0,
`--enableMajorityReadConcern` cannot be changed
and is always set to `true`. In earlier versions of MongoDB,
`--enableMajorityReadConcern` was configurable.

**Warning:**

If you are using a three-member primary-secondary-arbiter (PSA) 
architecture, consider the following:

- The write concern `"majority"` can cause
  performance issues if a secondary is unavailable or lagging. For 
  advice on how to mitigate these issues, see 
  performance-issues-psa.

- If you are using a global default `"majority"` 
  and the write concern is less than the size of the majority,
  your queries may return stale (not fully replicated) data.


### Sharded Cluster Options

**`--configsvr`**

*Required if starting a config server.*

Declares that this `mongod` instance serves as the config
server of a sharded cluster. When
running with this option, clients (i.e. other cluster components)
cannot write data to any database other than `config`
and `admin`. The default port for a `mongod` with this option is
`27019` and the default `--dbpath` directory is
`/data/configdb`, unless specified.

**Important:**

When starting a MongoDB server with `--configsvr`, you must also
specify a `--replSet`. 

The use of the deprecated mirrored `mongod` instances as
config servers (SCCC) is no longer supported.

The replica set config servers (CSRS) must run the
WiredTiger storage engine.

The `--configsvr` option creates a local oplog.

Do not use the `--configsvr` option with `--shardsvr`. Config
servers cannot be a shard server.

Do not use the `--configsvr` with the
`skipShardingConfigurationChecks` parameter. That is, if
you are temporarily starting the `mongod` as a
standalone for maintenance operations, include the parameter
`skipShardingConfigurationChecks` and exclude `--configsvr`.
Once maintenance has completed, remove the
`skipShardingConfigurationChecks` parameter and restart
with `--configsvr`.

**`--shardsvr`**

*Required if starting a shard server.*

Configures this `mongod` instance as a shard in a
sharded cluster. The default port for these instances is
`27018`.

**Important:**

When starting a MongoDB server with `--shardsvr`, you must also
specify a `--replSet`. 

Do not use the `--shardsvr` with the
`skipShardingConfigurationChecks` parameter. That is, if
you are temporarily starting the `mongod` as a
standalone for maintenance operations, include the parameter
`skipShardingConfigurationChecks` and exclude `--shardsvr`.
Once maintenance has completed, remove the
`skipShardingConfigurationChecks` parameter and restart
with `--shardsvr`.

**`--moveParanoia`**

If specified, during chunk migration, a shard saves,
to the `moveChunk` directory of the `--dbpath`, all documents
migrated from that shard.

MongoDB does not automatically delete the data saved in the
`moveChunk` directory.

**`--noMoveParanoia`**

During chunk migration, a shard does not save documents migrated from
the shard.

This is the default behavior.
