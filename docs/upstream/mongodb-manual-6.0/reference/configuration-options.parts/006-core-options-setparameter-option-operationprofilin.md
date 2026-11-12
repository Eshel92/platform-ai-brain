<!-- Part 6 of 7 of reference/configuration-options.md (split because the page is big). -->

### `setParameter` Option

**`setParameter`**

Set MongoDB parameter or parameters described in
/reference/parameters

To set parameters in the YAML configuration file, use the following
format:

```yaml
setParameter:
   <parameter1>: <value1>
   <parameter2>: <value2>
```

For example, to specify the `enableLocalhostAuthBypass` in
the configuration file:

```yaml
setParameter:
   enableLocalhostAuthBypass: false
```

   

#### LDAP Parameters

**`setParameter.ldapUserCacheInvalidationInterval`**

*Type*: int

*Default*: 30

For use with `mongod` servers using security-ldap-external.

The interval (in seconds) `mongod` waits
between external user cache flushes. After `mongod` flushes the external
user cache, MongoDB
reacquires authorization data from the LDAP server the
next time an LDAP-authorized user issues an operation.

Increasing the value specified increases the amount of time
`mongod` and the LDAP server can be out of sync, but reduces the load on
the LDAP server. Conversely, decreasing the value specified
decreases the time `mongod` and the LDAP server can be out of sync while
increasing the load on the LDAP server.

```yaml
setParameter:
   ldapUserCacheInvalidationInterval: <int>
```


### `storage` Options

**Changed in version:** 4.4

- MongoDB removes the `storage.indexBuildRetry` option and the
  corresponding `--noIndexBuildRetry` command-line option.

- MongoDB deprecates
  `storage.wiredTiger.engineConfig.maxCacheOverflowFileSizeGB`
  option. The option has no effect starting in MongoDB 4.4.

```yaml
storage:
   dbPath: <string>
   journal:
      enabled: <boolean>
      commitIntervalMs: <num>
   directoryPerDB: <boolean>
   syncPeriodSecs: <int>
   engine: <string>
   wiredTiger:
      engineConfig:
         cacheSizeGB: <number>
         journalCompressor: <string>
         directoryForIndexes: <boolean>
         maxCacheOverflowFileSizeGB: <number> 
      collectionConfig:
         blockCompressor: <string>
      indexConfig:
         prefixCompression: <boolean>
   inMemory:
      engineConfig:
         inMemorySizeGB: <number>
   oplogMinRetentionHours: <double>
```

**`storage.dbPath`**

*Type*: string

*Default*:

- `/data/db` on Linux and macOS
- `\data\db` on Windows

The directory where the `mongod` instance stores its
data.

The `storage.dbPath` setting is available only for
`mongod`.

**Note:** Configuration Files

The default `mongod.conf` configuration file included with
package manager installations uses the following platform-specific
default values for `storage.dbPath`:

| Platform | Package Manager | Default `storage.dbPath` |
|---|---|---|
| RHEL (Red Hat Enterprise Linux) / CentOS and Amazon | `yum` | `/var/lib/mongo` |
| SUSE | `zypper` | `/var/lib/mongo` |
| Ubuntu and Debian | `apt` | `/var/lib/mongodb` |
| macOS | `brew` | `/usr/local/var/mongodb` |

The Linux package init scripts do not expect `storage.dbPath` to change from the
defaults. If you use the Linux packages and change `storage.dbPath`, you must
use your own init scripts and disable the built-in scripts.

**`storage.journal.enabled`**

*Type*: boolean

*Default*: `true` on 64-bit systems, `false` on 32-bit systems

Enable or disable the durability journal to ensure data files remain valid
and recoverable. This option applies only when you specify the
`storage.dbPath` setting. `mongod` enables journaling by default.

The `storage.journal.enabled` setting is available only for `mongod`.

Not available for `mongod` instances that use the
in-memory storage engine.

You cannot specify `--nojournal` option or `storage.journal.enabled: false` 
for replica set members that use the WiredTiger storage engine.

**`storage.journal.commitIntervalMs`**

*Type*: number

*Default*: 100

The maximum amount of time in milliseconds that
the `mongod` process allows between
journal operations. Values can range from 1 to 500 milliseconds. Lower
values increase the durability of the journal, at the expense of disk
performance.

On WiredTiger, the default journal commit interval is 100
milliseconds. Additionally, a write that includes or implies
`j:true` causes an immediate sync of the journal. For details
or additional conditions that affect the frequency of the sync, see
journal-process.

The `storage.journal.commitIntervalMs` setting is available only for `mongod`.

Not available for `mongod` instances that use the
in-memory storage engine.

**`storage.directoryPerDB`**

*Type*: boolean

*Default*: false

When `true`, MongoDB uses a separate directory to store data for each database. The
directories are under the `storage.dbPath` directory, and each subdirectory
name corresponds to the database name.

The `storage.directoryPerDB` setting is available only for `mongod`.

Not available for `mongod` instances that use the
in-memory storage engine.

Starting in MongoDB 5.0, dropping the final collection in a database
(or dropping the database itself) when
`storage.directoryPerDB` is enabled deletes the newly empty
subdirectory for that database.

To change the `storage.directoryPerDB` option for existing
deployments:

- For standalone instances:

  #. Use `mongodump` on the existing
     `mongod` instance to generate a backup.
  #. Stop the `mongod` instance.
  #. Add the `storage.directoryPerDB` value **and**
     configure a new data directory
  #. Restart the `mongod` instance.
  #. Use `mongorestore` to populate the new data
     directory.

- For replica sets:

  #. Stop a secondary member.
  #. Add the `storage.directoryPerDB` value **and**
     configure a new data directory to that secondary member.
  #. Restart that secondary.
  #. Use initial sync to populate
     the new data directory.
  #. Update remaining secondaries in the same fashion.
  #. Step down the primary, and update the stepped-down member in the
     same fashion.

**`storage.syncPeriodSecs`**

*Type*: number

*Default*: 60

The amount of time that can pass before MongoDB flushes data to the data
files.

**Do not set this value on
production systems.** In almost every situation, you should use the
default setting.

The `mongod` process writes data very quickly to the journal and
lazily to the data files. `storage.syncPeriodSecs` has no effect on 
journaling-internals, but if `storage.syncPeriodSecs` is 
set to `0` the journal eventually consumes all available disk space. 

The `storage.syncPeriodSecs` setting is available only for `mongod`.

Not available for `mongod` instances that use the
in-memory storage engine.

To provide durable data, WiredTiger
uses checkpoints. For more
details, see journaling-wiredTiger.

**`storage.engine`**

*Default*: `wiredTiger`

The storage engine for the `mongod` database. Available
values include:

| Value | Description |
|---|---|
| `wiredTiger` | To specify the /core/wiredtiger. |
| `inMemory` | To specify the /core/inmemory. Available in MongoDB Enterprise only. If you attempt to start a `mongod` with a `storage.dbPath` that contains data files produced by a storage engine other than the one specified by `storage.engine`, `mongod` refuses to start. |

**`storage.oplogMinRetentionHours`**

*Type*: double

Specifies the minimum number of hours to preserve an oplog entry,
where the decimal values represent the fractions of an hour. For
example, a value of `1.5` represents one hour and thirty
minutes.

The value must be greater than or equal to `0`. A value of `0`
indicates that the `mongod` should truncate the oplog
starting with the oldest entries to maintain the configured
maximum oplog size.

Defaults to `0`.

A `mongod` started with `oplogMinRetentionHours` only
removes an oplog entry *if*:

- The oplog has reached the maximum configured oplog size *and*

- The oplog entry is older than the configured number of hours based
  on the host system clock.

The `mongod` has the following behavior when configured
with a minimum oplog retention period:

- The oplog can grow without constraint so as to retain oplog entries
  for the configured number of hours. This may result in reduction or
  exhaustion of system disk space due to a combination of high write
  volume and large retention period.

- If the oplog grows beyond its maximum size, the `mongod` 
  may continue to hold that disk space even if the oplog returns to its
  maximum size *or* is configured for a smaller maximum size. See
  replSetResizeOplog-cmd-compact.

- The `mongod` compares the system wall clock to an 
  oplog entries creation wall clock time when enforcing oplog entry
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
`oplogMinRetentionHours`.

#### `storage.wiredTiger` Options

```yaml
storage:
   wiredTiger:
      engineConfig:
         cacheSizeGB: <number>
         journalCompressor: <string>
         directoryForIndexes: <boolean>
         maxCacheOverflowFileSizeGB: <number> 
      collectionConfig:
         blockCompressor: <string>
      indexConfig:
         prefixCompression: <boolean>
```

**`storage.wiredTiger.engineConfig.cacheSizeGB`**

*Type*: float

Defines the maximum size of the internal cache that WiredTiger
uses for all data. The memory consumed by an index build (see
`maxIndexBuildMemoryUsageMegabytes`) is separate from the
WiredTiger cache memory. 

Values can range from `0.25` GB to `10000` GB.

The default WiredTiger internal cache size is the larger of either:

- 50% of (RAM - 1 GB), or

- 256 MB.

For example, on a system with a total of 4GB of RAM the
WiredTiger cache uses 1.5GB of RAM (``0.5 * (4 GB - 1 GB) =
1.5 GB``). Conversely, on a system with a total of 1.25 GB of
RAM WiredTiger allocates 256 MB to the WiredTiger cache
because that is more than half of the total RAM minus one
gigabyte (`0.5 * (1.25 GB - 1 GB) = 128 MB < 256 MB`).

**Note:**

In some instances, such as when running in a container, the database
can have memory constraints that are lower than the total system
memory. In such instances, this memory limit, rather than the total
system memory, is used as the maximum RAM available.

To see the memory limit, see `hostInfo.system.memLimitMB`.

Avoid increasing the WiredTiger internal cache size above its
default value.

With WiredTiger, MongoDB utilizes both the WiredTiger internal cache
and the filesystem cache.

With the filesystem cache, MongoDB automatically uses all free memory
that is not used by the WiredTiger cache or by other processes.

**Note:**

The `storage.wiredTiger.engineConfig.cacheSizeGB` limits the size of the WiredTiger internal
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
RAM available in a system, you must set `storage.wiredTiger.engineConfig.cacheSizeGB` to a value
less than the amount of RAM available in the container. The exact
amount depends on the other processes running in the container. See
`memLimitMB`.

   

**`storage.wiredTiger.engineConfig.journalCompressor`**

*Default*: snappy

Specifies the type of compression to use to compress WiredTiger
journal data.

Available compressors are:

- `none`

- snappy

- zlib

- zstd
   

**`storage.wiredTiger.engineConfig.directoryForIndexes`**

*Type*: boolean

*Default*: false

When `storage.wiredTiger.engineConfig.directoryForIndexes` is `true`, `mongod` stores indexes and collections in separate
subdirectories under the data (i.e. `storage.dbPath`) directory.
Specifically, `mongod` stores the indexes in a subdirectory named
`index` and the collection data in a subdirectory named
`collection`.

By using a symbolic link, you can specify a different location for
the indexes. Specifically, when `mongod` instance is **not**
running, move the `index` subdirectory to the destination and
create a symbolic link named `index` under the data directory to
the new destination.

   

**`storage.wiredTiger.engineConfig.zstdCompressionLevel`**

*Type*: integer

*Default*: 6

Specifies the level of compression applied when using
the zstd compressor.

Values can range from 1 to 22.

The higher the specified value for `zstdCompressionLevel`
the higher the compression which is applied.

Only applicable when either
`blockCompressor` 
or `journalCompressor` (or both) are
set to `zstd`.

*Available starting in MongoDB 5.0*

**`storage.wiredTiger.collectionConfig.blockCompressor`**

*Default*: snappy

Specifies the default compression for collection data. You can
override this on a per-collection basis when creating collections.

Available compressors are:

- `none`

- snappy

- zlib

- zstd

`storage.wiredTiger.collectionConfig.blockCompressor` affects all collections created. If you change
the value of `storage.wiredTiger.collectionConfig.blockCompressor` on an existing MongoDB deployment, all new
collections uses the specified compressor. Existing collections
continue to use the compressor specified when they were
created, or the default compressor at that time.

**`storage.wiredTiger.indexConfig.prefixCompression`**

*Default*: true

Enables or disables prefix compression for index data.

Specify `true` for `storage.wiredTiger.indexConfig.prefixCompression` to enable prefix compression for
index data, or `false` to disable prefix compression for index data.

The `storage.wiredTiger.indexConfig.prefixCompression` setting affects all indexes created. If you change
the value of `storage.wiredTiger.indexConfig.prefixCompression` on an existing MongoDB deployment, all new
indexes uses prefix compression. Existing indexes
are not affected.

#### `storage.inmemory` Options

```yaml
storage:
   inMemory:
      engineConfig:
         inMemorySizeGB: <number>
```

**`storage.inMemory.engineConfig.inMemorySizeGB`**

*Type*: float

*Default*: 50% of physical RAM less 1 GB

Values can range from 256MB to 10TB and can be a float.

Maximum amount of memory to allocate for in-memory storage
engine data, including indexes, oplog if the
`mongod` is part of replica set, replica set or sharded
cluster metadata, etc.

By default, the in-memory storage engine uses 50% of physical RAM minus
1 GB.

**Note:** Enterprise Feature

Available in MongoDB Enterprise only.

   


### `operationProfiling` Options

```yaml
operationProfiling:
   mode: <string>
   slowOpThresholdMs: <int>
   slowOpSampleRate: <double>
   filter: <string>
```

**`operationProfiling.mode`**

*Type*: string

*Default*: `off`

Specifies which operations should be profiled.
The following profiler levels are available:

| Level | Description |
|---|---|
| `off` | The profiler is off and does not collect any data. This is the default profiler level. This level corresponds to profiler level 0. |
| `slowOp` | The profiler collects data for operations that take longer than the value of `slowms`. This level corresponds to profiler level 1. |
| `all` | The profiler collects data for all operations. This level corresponds to profiler level 2. |

**Warning:**

Profiling can degrade performance and expose unencrypted query data in the
system log. Carefully consider any performance and security implications
before configuring and enabling the profiler on a production deployment.

See database-profiling-overhead for more information on
potential performance degradation.

   

**`operationProfiling.slowOpThresholdMs`**

*Type*: integer

*Default*: 100

The *slow* operation time threshold, in milliseconds. Operations
that run for longer than this threshold are considered *slow*.

When `logLevel` is set to `0`, MongoDB records *slow*
operations to the diagnostic log at a rate determined by
`slowOpSampleRate`.

At higher `logLevel` settings, all operations appear in
the diagnostic log regardless of their latency with the following
exception: the logging of slow oplog entry messages by the
secondaries. The secondaries log only the slow oplog
entries; increasing the `logLevel` does not log all
oplog entries.

This setting is available for `mongod` and `mongos`.

- For `mongod` instances, the setting affects both
  the diagnostic log and, if enabled, the profiler.

- For `mongos` instances, the setting affects the
  diagnostic log only and not the profiler, since profiling is not
  available on `mongos`.
   

**`operationProfiling.slowOpSampleRate`**

*Type*: double

*Default*: 1.0

The fraction of *slow* operations that should be profiled or logged.
`operationProfiling.slowOpSampleRate` accepts values between
0 and 1, inclusive.

The `slowOpSampleRate` setting is
available for `mongod` and `mongos`. 

- For `mongod` instances, the setting affects both
  the diagnostic log and, if enabled, the profiler.

- For `mongos` instances, the setting affects the
  diagnostic log only and not the profiler since profiling is not
  available on `mongos`.

**`operationProfiling.filter`**

*Type*: string representation of a query document

A filter expression that controls which operations are profiled and
logged.

When `filter` is set,
`slowOpThresholdMs` and
`slowOpSampleRate` are not used for
profiling and slow-query log lines.

When you set a profile filter in the configuration file, the filter
applies to all databases in the deployment. To set a profile filter
for a specific database, use the `db.setProfilingLevel()`
method.

The option takes a string representation of a query document
of the form:

```javascript
{ <field1>: <expression1>, ... }
```

The `<field>` can be any field in the profiler output. The `<expression>` is a query condition
expression.

To specify a profiling filter in a configuration file, you must:

- Enclose the filter document in single quotes to pass the document
  as a string.

- Use the YAML format of the configuration file.

For example, the following `filter` configures the profiler to
log `query` operations that take longer than 2 seconds:

```yaml
operationProfiling:
   mode: all
   filter: '{ op: "query", millis: { $gt: 2000 } }'
```
