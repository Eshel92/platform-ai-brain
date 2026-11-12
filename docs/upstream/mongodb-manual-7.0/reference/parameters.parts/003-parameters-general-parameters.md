<!-- Part 3 of 8 of reference/parameters.md (split because the page is big). -->

### General Parameters

**`allowDiskUseByDefault`**

Available for `mongod` only.

*Default*: True

Starting in MongoDB 6.0, pipeline stages that require more than 100 
megabytes of memory to execute write temporary files to disk by 
default. These temporary files last for the duration of the pipeline 
execution and can influence storage space on your instance. In earlier 
versions of MongoDB, you must pass  `{ allowDiskUse: true }` to 
individual `find` and `aggregate` commands to enable this 
behavior.

Individual `find` and `aggregate` commands can override the 
`allowDiskUseByDefault` parameter by either:

- Using `{ allowDiskUse: true }` to allow writing temporary files out 
  to disk when `allowDiskUseByDefault` is set to `false`

- Using `{ allowDiskUse: false }` to prohibit writing temporary files
  out to disk when `allowDiskUseByDefault` is set to `true`

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

```bash
mongod --setParameter allowDiskUseByDefault=false
```

`allowDiskUseByDefault` only works on `mongod` 
not `mongos`. `mongos` never writes temporary
files to disk. Use the `setParameter` command in 
a `mongosh` session that is connected to a running 
`mongod` to change the value of the parameter while the
server is running:

```javascript
db.adminCommand( 
  {
      setParameter: 1, 
      allowDiskUseByDefault: false 
  }
)
```

**`capMemoryConsumptionForPreAuthBuffers`**

**New in version:** 7.0.29

Available for both `mongod` and `mongos`.

*Type*: Int

*Default*: 20

Specifies the maximum percentage of total memory to allocate to pre-auth 
buffers for connections. Setting the parameter to `100` disables this 
limitation.

This parameter is only available at startup. To set the
parameter, use the `setParameter` setting. 

The following operation sets `capMemoryConsumptionForPreAuthBuffers`
to `30`:

```bash
mongod --setParameter capMemoryConsumptionForPreAuthBuffers=30
```

**`httpVerboseLogging`**

Available for both `mongod` and `mongos`.

Adds more verbose tracing for curl on Linux and macOS. Has no affect on Windows.

By default, the parameter is unset.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

```bash
mongos --setParameter httpVerboseLogging=true
```

**`slowConnectionThresholdMillis`**

**New in version:** 6.3

Available for both `mongod` and `mongos`.

*Default*: 100

Sets the time limit in milliseconds to log the establishment of slow
server connections.

If a connection takes longer to establish than the
`slowConnectionThresholdMillis` parameter, an event is
added to the log with the message `msg`
field set to `"Slow connection establishment"`.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

The following example sets `slowConnectionThresholdMillis`
to `250` milliseconds.

```bash
mongod --setParameter slowConnectionThresholdMillis=250
```

Or, if using the `setParameter` command within
`mongosh`:

```javascript
db.adminCommand( { setParameter: 1, slowConnectionThresholdMillis: 250 } )
```

**`connPoolMaxConnsPerHost`**

Available for both `mongod` and `mongos`.

*Default*: 200

Sets the maximum size of the legacy connection pools for outgoing connections
to other `mongod` instances in the global connection pool. The size
of a pool does not prevent the creation of additional connections,
but *does* prevent a connection pool from retaining connections in
excess of the value of `connPoolMaxConnsPerHost`.

**Note:**

The parameter is separate from the connections in TaskExecutor
pools. See `ShardingTaskExecutorPoolMaxSize`.

**Only** adjust this setting if your driver does *not* pool
connections and you're using authentication in the
context of a sharded cluster.

This parameter is only available at startup. To set the
parameter, use the `setParameter` setting. 

```bash
mongod --setParameter connPoolMaxConnsPerHost=250
```

**`connPoolMaxInUseConnsPerHost`**

Available for both `mongod` and `mongos`.

Sets the maximum number of in-use connections at any given time for
for outgoing connections to other `mongod` instances in
the legacy global connection pool.

By default, the parameter is unset.

This parameter is only available at startup. To set the
parameter, use the `setParameter` setting. 

```bash
mongod --setParameter connPoolMaxInUseConnsPerHost=100
```

**See also:**

`connPoolMaxConnsPerHost`

**`globalConnPoolIdleTimeoutMinutes`**

Available for both `mongod` and `mongos`.

Sets the time limit that connection in the legacy global connection
pool can remain idle before being closed.

By default, the parameter is unset.

This parameter is only available at startup. To set the
parameter, use the `setParameter` setting. 

```bash
mongos --setParameter globalConnPoolIdleTimeoutMinutes=10
```

**`cursorTimeoutMillis`**

Available for both `mongod` and `mongos`.

*Default*: 600000 (10 minutes)

Sets the expiration threshold in milliseconds for idle cursors before
MongoDB removes them; specifically, MongoDB removes cursors that have
been idle for the specified `cursorTimeoutMillis`.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

For example, the following sets the `cursorTimeoutMillis`
to `300000` milliseconds (5 minutes).

```bash
mongod --setParameter cursorTimeoutMillis=300000
```

Or, if using the `setParameter` command within
`mongosh`:

```javascript
db.adminCommand( { setParameter: 1, cursorTimeoutMillis: 300000 } )
```

Setting `cursorTimeoutMillis` to less than or equal
to `0` results in all cursors being immediately eligible for timeout.
Generally, the timeout value should be greater than the average amount of
time for a query to return results. Use tools like the `cursor.explain()`
cursor modifier to analyze the average query time and select an appropriate
timeout period.

**Warning:**

MongoDB cleans up orphaned cursors after the
`cursorTimeoutMillis` threshold only if they are not tied to sessions.

MongoDB cleans up cursors linked to sessions with the
`localLogicalSessionTimeoutMinutes` lifecycle, regardless of
the `cursorTimeoutMillis` value. To handle long idle periods,
use `Mongo.startSession()` and refresh the session using the
`refreshSessions` command. For details, see
refresh-session-cursor-example.

**`maxNumActiveUserIndexBuilds`**

Available for `mongod` only.

*Type*: integer

*Default*: 3

Sets the maximum number of index build requests that MongoDB can
perform concurrently. `maxNumActiveUserIndexBuilds` is a global
limit that applies for all collections.

The following table shows the default values for 
`maxNumActiveUserIndexBuilds` based on Atlas tiers:

| **Atlas Tiers** | **maxNumActiveUserIndexBuilds Default** |
|---|---|
| Small M tiers (`M10`, `M20`, `M30`, `M40`) | `1` |
| Medium M tiers (`M50`, `M60`) | `2` |
| Large M tiers (`M80` and higher, including NMVe variants) | `3` |

**Note:**

These defaults also apply to the corresponding low-CPU `R` tiers.

The `createIndexes` command builds indexes. Even if the
`createIndexes` command builds multiple indexes at once, the
command execution only adds `1` to `maxNumActiveUserIndexBuilds`.

Increasing the value of `maxNumActiveUserIndexBuilds` allows
additional concurrent index builds at the cost of increased pressure
on the WiredTiger cache.

System indexes are not limited to `maxNumActiveUserIndexBuilds`,
however a system index build counts against the limit for user index
builds.

After the server reaches `maxNumActiveUserIndexBuilds`, it blocks
additional user index builds until the number of concurrent index
builds drops below the `maxNumActiveUserIndexBuilds` limit. If an
index build is blocked, the server logs this message:

```sh
Too many index builds running simultaneously, waiting until the
number of active index builds is below the threshold.
```

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

The following command sets a limit of 4 concurrent index builds:

```javascript
db.adminCommand( { setParameter: 1, maxNumActiveUserIndexBuilds: 4 } )
```

See also:

- `maxIndexBuildMemoryUsageMegabytes`
- index-creation-background

**`messageSizeErrorRateSec`**

**New in version:** 7.0.29

Available for both `mongod` and `mongos`.

*Type*: Int

*Default*: 5

Specifies the rate, in seconds, at which the server logs message size errors
at the Info level. 

This parameter is only available at startup. To set the
parameter, use the `setParameter` setting. 

The following operation sets `messageSizeErrorRateSec`
to `6`:

```bash
mongod --setParameter messageSizeErrorRateSec=6
```

**`notablescan`**

Available for `mongod` only.

Prevents running some collection scans when an index could be used, whether 
present or not. If `true`, MongoDB will not execute queries that require
a collection scan and will return an error. Exclusions include queries 
without filters and queries against capped collections, such as the oplog.

Consider the following example which sets `notablescan` to `true`
or true:

```javascript
db.adminCommand( { setParameter: 1, notablescan: true } )
```

Set `notablescan` to `true` to test application queries
and identify queries that scan an entire collection and cannot use
an index.

To detect unindexed queries without `notablescan`, consider reading
the /tutorial/evaluate-operation-performance section and using
the `logLevel` parameter, `mongostat` and
profiling.

Don't run production `mongod` instances with
`notablescan` because preventing collection scans can potentially
affect queries in all databases, including administrative queries.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

**Note:**

`notablescan` does not allow unbounded queries that use a
clustered index because the queries require a full collection
scan. For more information, see Collection Scans.

**`preAuthMaximumMessageSizeBytes`**

**New in version:** 7.0.29

Available for both `mongod` and `mongos`.

*Type*: Int

*Default*: 16384 (16 KiB)

The maximum size of a message in bytes that you can send before the session
authenticates.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

For example, the following sets the maximum size of the message to 
1700 bytes:

```bash
mongod --setParameter preAuthMaximumMessageSizeBytes=1700
```

During run time, you can also set the parameter with the
`setParameter` command:

```bash
db.adminCommand( { setParameter: 1, preAuthMaximumMessageSizeBytes: 1700 } )
```

**`ttlMonitorEnabled`**

Available for `mongod` only.

*Default*: `true`

To support TTL Indexes, `mongod`
instances have a background thread that is responsible for deleting
documents from collections with TTL indexes.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

To disable this worker thread for a `mongod`, set
`ttlMonitorEnabled` to `false`, as in the following
operations:

```javascript
db.adminCommand( { setParameter: 1, ttlMonitorEnabled: false } )
```

Alternately, you may disable the thread at startup time by starting the
`mongod` instance with the following option:

```bash
mongod --setParameter ttlMonitorEnabled=false
```

**Important:**

Do not run production `mongod` instances with
`ttlMonitorEnabled` disabled, except under guidance from MongoDB
support. Preventing TTL document removal can negatively impact
MongoDB internal system operations that depend on TTL Indexes.

**`tcpFastOpenServer`**

Available for both `mongod` and `mongos`.

*Default*: `true`

Enables support for accepting inbound TCP Fast Open (TFO) connections
to the `mongod/mongos` from a client. TFO requires both the
client and `mongod/mongos` host machine support and enable
TFO:

Windows
  The following Windows operating systems support TFO:

  - Microsoft Windows Server 2016 and later.
  - Microsoft Windows 10 Update 1607 and later.

macOS
  macOS 10.11 (El Capitan) and later support TFO.

Linux
  Linux operating systems running Linux Kernel 3.7 or later
  can support inbound TFO.

  Set the value of `/proc/sys/net/ipv4/tcp_fastopen` to
  enable inbound TFO connections:

  - Set to `2` to enable only inbound TFO connections.
  - Set to `3` to enable inbound and outbound TFO connections.

This parameter has no effect if the host operating system does not
support *or* is not configured to support TFO connections.

This parameter is only available at startup. To set the
parameter, use the `setParameter` setting. 

**See also:**

[RFC7413](https://tools.ietf.org/html/rfc7413).

**`tcpFastOpenClient`**

Available for both `mongod` and `mongos`.

*Default*: `true`

*Linux Operating System Only*

Enables support for outbound TCP Fast Open (TFO) connections from the
`mongod/mongos` to a client. TFO requires both the client
and the `mongod/mongos` host machine support and enable TFO.

Linux operating systems running Linux Kernel 4.11 or later can
support outbound TFO.

Set the value of `/proc/sys/net/ipv4/tcp_fastopen` to enable
outbound TFO connections:

- `1` to enable only outbound TFO connections.
- `3` to enable inbound and outbound TFO connections.

This parameter has no effect if the host operating system does not
support *or* is not configured to support TFO connections.

This parameter is only available at startup. To set the
parameter, use the `setParameter` setting. 

**See also:**

[RFC7413](https://tools.ietf.org/html/rfc7413).

**`tcpFastOpenQueueSize`**

Available for both `mongod` and `mongos`.

*Default*: `1024`

As part of establishing a TCP Fast Open (TFO) connection, the client
submits a valid TFO cookie to the `mongod/mongos` *before*
completion of the standard TCP 3-way handshake. The
`mongod/mongos` keeps a queue of all such pending TFO connections.

The `tcpFastOpenQueueSize` parameter sets the size of the queue of
pending TFO connections. While the queue is full, the
`mongod/mongos` falls back to the normal three-way handshake for
incoming client requests and ignores the presence of TFO cookies.
Once the queue size falls back below the limit, the `mongod/mongos`
begins accepting new TFO cookies.

- Increasing the default queue size may improve the effect of
  TFO on network performance. However, large queue sizes also
  increase the risk of server resource exhaustion due to excessive
  incoming TFO requests.

- Decreasing the default queue size may reduce the risk of resource
  server resource exhaustion due to excessive incoming TFO requests.
  However, small queue sizes may also reduce the effect of TFO on
  network performance.

  The minimum queue size is `0`. A queue of `0` effectively
  disables TFO.

This parameter has no effect on host operating systems that do
not support or are not configured for TFO connections. 

This parameter is only available at startup. To set the
parameter, use the `setParameter` setting. 

**See also:**

- [RFC7413 TCP Fast Open Section 5: Security Considerations](https://tools.ietf.org/html/rfc7413#section-5)

- [RFC7413 TCP Fast Open Section 6: TFO Applicability](https://tools.ietf.org/html/rfc7413#section-6)

**`disableJavaScriptJIT`**

Available for `mongod` only.

The MongoDB JavaScript engine uses SpiderMonkey, which implements
Just-in-Time (JIT) compilation for improved performance when running scripts.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

To enable the JIT, set `disableJavaScriptJIT` to `false`, as in
the following example:

```javascript
db.adminCommand( { setParameter: 1, disableJavaScriptJIT: false } )
```

**Note:**

`$where` will reuse existing JavaScript interpreter
contexts, so changes to `disableJavaScriptJIT` may not
take effect immediately for these operations.

Alternately, you may enable the JIT at startup time by starting the
`mongod` instance with the following option:

```bash
mongod --setParameter disableJavaScriptJIT=false
```

**`indexMaxNumGeneratedKeysPerDocument`**

**New in version:** 5.3

*Default*: 100000

Limits the maximum number of keys generated for a document to
prevent out of memory errors. It is possible to raise the limit, but
if an operation requires more keys than the
`indexMaxNumGeneratedKeysPerDocument` parameter specifies,
the operation will fail.

This parameter is only available at startup. To set the
parameter, use the `setParameter` setting. 

**`maxIndexBuildMemoryUsageMegabytes`**

*Default*: 200 

Limits the amount of memory that simultaneous index
builds on one collection may consume for the duration of the
builds. The specified amount of memory is shared between all
indexes built using a single
`createIndexes` command or its shell helper
`db.collection.createIndexes()`.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

The memory consumed by an index build is separate from the
WiredTiger cache memory (see
`cacheSizeGB`).

`maxIndexBuildMemoryUsageMegabytes` sets a limit on how much 
memory the index build uses at once. This can impact performance 
when the index build process generates 
and sorts keys for the index. Increasing the memory limit 
improves sorting performance during an index build.

The `maxIndexBuildMemoryUsageMegabytes` limit applies to all
index builds initiated by user commands like `createIndexes` or
administrative processes like initial sync.

An initial sync populates only one collection 
at a time and has no risk of exceeding the memory limit. However, it is 
possible for a user to start index builds on multiple collections in 
multiple databases simultaneously.

Changing `maxIndexBuildMemoryUsageMegabytes` does not affect an 
in progress index build if it has already started a collection scan. 
However, a forced replica set reconfiguration restarts the collection 
scan and uses the most current 
`maxIndexBuildMemoryUsageMegabytes` provided.

- For feature compatibility version (fcv) `"4.2"`
  and later, the index build memory limit applies to all index builds.

**`reportOpWriteConcernCountersInServerStatus`**

*Default*: false

A boolean flag that determines whether the
`db.serverStatus()` method and `serverStatus`
command return `opWriteConcernCounters` information. [#perf]_

```bash
mongod --setParameter reportOpWriteConcernCountersInServerStatus=true
```

**`watchdogPeriodSeconds`**

Available for `mongod` only.

*Type*: integer

*Default*: -1 (disabled)

Determines how frequent the Storage Node Watchdog checks the status of the monitored
filesystems:

* The `--dbpath` directory
* The `journal` directory inside the `--dbpath` 
  directory
* The directory of `--logpath` file
* The directory of `--auditPath` file

Valid values for `watchdogPeriodSeconds` are:

- `-1` (the default), to disable/pause Storage Node Watchdog, or

- An integer greater than or equal to 60.

**Note:**

- If a filesystem on a monitored directory becomes unresponsive,
  it can take a maximum of nearly *twice* the value of
  `watchdogPeriodSeconds` to terminate the
  `mongod`.

- If any of its monitored directory is a symlink to other
  volumes, the Storage Node Watchdog does not monitor the symlink
  target. For example, if the `mongod` uses
  `storage.directoryPerDB: true` (or `--directoryperdb`) and symlinks a database directory to
  another volume, the Storage Node Watchdog does not follow the
  symlink to monitor the target.

To enable Storage Node Watchdog,
`watchdogPeriodSeconds` must be set during startup.

```bash
mongod --setParameter watchdogPeriodSeconds=60
```

You can only enable the Storage Node Watchdog at startup. However, once enabled, you can
pause the Storage Node Watchdog or
change the `watchdogPeriodSeconds` during run time.

Once enabled,

- To pause the Storage Node Watchdog
  during run time, set `watchdogPeriodSeconds` to -1.

  ```javascript
  db.adminCommand( { setParameter: 1, watchdogPeriodSeconds: -1 } )
  ```

- To resume or change the period during run time, set
  `watchdogPeriodSeconds` to a number greater than or
  equal to 60.

  ```javascript
  db.adminCommand( { setParameter: 1, watchdogPeriodSeconds: 120 } )
  ```

**`tcmallocAggressiveMemoryDecommit`**

*Type*: integer (`0` or `1` only)

Default: 0

If you enable `tcmallocAggressiveMemoryDecommit`, MongoDB:

- releases a chunk of memory to system, and 

- attempts to return all neighboring free chunks. 

A value of `1` enables `tcmallocAggressiveMemoryDecommit`; 
`0` disables this parameter.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

If you enable this parameter, the system will require new memory allocations 
for use. Consider enabling `tcmallocAggressiveMemoryDecommit` 
only on memory-constrained systems and after pursuing other memory and 
performance options.

Despite the potential performance degradation when using 
`tcmallocAggressiveMemoryDecommit`, it is often preferred over using 
`tcmallocReleaseRate`.

**`tcmallocReleaseRate`**

Default: 1.0

Specifies the tcmalloc release rate ([TCMALLOC_RELEASE_RATE](https://gperftools.github.io/gperftools/tcmalloc.html#runtime)).
Per https://gperftools.github.io/gperftools/tcmalloc.html#runtime
TCMALLOC_RELEASE_RATE is described as the "Rate at which we release
unused memory to the system, via
madvise(MADV_DONTNEED), on systems that support it. Zero means we
never release memory back to the system. Increase this flag to
return memory faster; decrease it to return memory slower.
Reasonable rates are in the range [0,10]."

**Note:**

Consider using `tcmallocAggressiveMemoryDecommit` instead of 
`tcmallocReleaseRate`, unless you see a significant performance 
degradation when using `tcmallocAggressiveMemoryDecommit`.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

To modify the release rate during run time, you can use the
`setParameter` command; for example:

```javascript
db.adminCommand( { setParameter: 1, tcmallocReleaseRate: 5.0 } )
```

You can also set `tcmallocReleaseRate` at startup time;
for example:

```bash
mongod --setParameter "tcmallocReleaseRate=5.0"
```

**`fassertOnLockTimeoutForStepUpDown`**

**New in version:** 5.3

Available for both `mongod` and `mongos`.

Default: 15 seconds

Allows a server that receives a request to step up or step down, to 
terminate if it is unable to comply (for example due
to faulty server disks) within the timeout. This enables a cluster to 
successfully elect a new primary node and thus continue to be available. 

`fassertOnLockTimeoutForStepUpDown` defaults to 15 seconds. To disable
nodes from fasserting, set `fassertOnLockTimeoutForStepUpDown=0`. 

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

The following example disables nodes from fasserting: 

```bash
mongod --setParameter fassertOnLockTimeoutForStepUpDown=0
```
