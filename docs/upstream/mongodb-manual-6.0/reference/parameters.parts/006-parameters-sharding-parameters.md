<!-- Part 6 of 8 of reference/parameters.md (split because the page is big). -->

### Sharding Parameters

**`balancerMigrationsThrottlingMs`**

**New in version:** 6.0.6 (*Also available starting 5.0.18*)

*Type*: integer

*Default*: 1000

Available for `mongod` only.

Specifies the minimum amount of time between two consecutive 
balancing rounds. This allows you to throttle the balancing
rate. This parameter only takes effect on config server nodes.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command

- To set the parameter at startup, use the
  `setParameter` setting

This example sets `balancerMigrationsThrottlingMs` to 2000 
milliseconds at startup:

```bash
mongod --setParameter balancerMigrationsThrottlingMs=2000
```

During runtime, you can also set the parameter with the
`setParameter` command:

```javascript
db.adminCommand( { setParameter: 1, balancerMigrationsThrottlingMs: 2000 } )
```

**`chunkDefragmentationThrottlingMS`**

**New in version:** 5.3

*Type*: integer

*Default*: 0

Available for both `mongod` and `mongos`.

Specifies the minimum time period (in milliseconds) between
consecutive split and merge commands run by the balancer when
the chunks in a sharded collection
are defragmented. `chunkDefragmentationThrottlingMS`
limits the rate of split and merge commands.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command

- To set the parameter at startup, use the
  `setParameter` setting

The following example sets
`chunkDefragmentationThrottlingMS` to `10` milliseconds:

```bash
mongod --setParameter chunkDefragmentationThrottlingMS=10
```

During runtime, you can also set the parameter with the
`setParameter` command:

```javascript
db.adminCommand( { setParameter: 1, chunkDefragmentationThrottlingMS: 10 } )
```

**`disableResumableRangeDeleter`**

Available for `mongod` only.

*Type*: boolean

*Default*: false

If set on a shard's primary, specifies if range deletion is paused on
the shard. If set to `true`, cleanup of chunk ranges 
containing orphaned documents is paused.
The shard can continue to donate chunks to other shards, but the
donated documents will not be removed from this shard until you set
this parameter to `false`. This shard can continue to receive
chunks from other shards as long as it does not have a pending range
deletion task in the `config.rangeDeletions` collection that
overlaps with the incoming chunk's range.

When `disableResumableRangeDeleter` is `true`, chunk
migrations fail if orphaned documents
exist on the recipient shard's primary in the same range as the
incoming chunks.

The parameter has no effect on the `mongod` if it is not
the shard's primary.

**Important:**

If you set `disableResumableRangeDeleter` parameter to
`true`, ensure that you apply it consistently for all members in
the shard's replica set. In the event of a failover, this
setting's value on the new primary dictates the behavior of the
range deleter.

This parameter is only available at startup. To set the
parameter, use the `setParameter` setting. 

```javascript
mongod --setParameter disableResumableRangeDeleter=false
```

**`enableShardedIndexConsistencyCheck`**

Available for `mongod` only.

*Type*: boolean

*Default*: true

If set on the config server's primary, enables or disables the index
consistency check for sharded collections. The parameter has no
effect on the `mongod` if it is not the config server's
primary.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command

- To set the parameter at startup, use the
  `setParameter` setting

The following example sets
`enableShardedIndexConsistencyCheck` to `false` for a
config server primary:

```javascript
mongod --setParameter enableShardedIndexConsistencyCheck=false
```

During runtime, you can also set the parameter with the
`setParameter` command:

```bash
db.adminCommand( { setParameter: 1, enableShardedIndexConsistencyCheck: false } )
```

**See also:**

- `shardedIndexConsistencyCheckIntervalMS` parameter
- `shardedIndexConsistency` metrics returned by the
  `serverStatus` command.

**`opportunisticSecondaryTargeting`**

**New in version:** 6.0.0

*Type*: boolean

*Default*: `false`

Available for `mongos` only.

Determines whether `mongos` performs opportunistic reads against
replica sets.

When this parameter is set to `true`, `mongos` directs secondary 
reads to secondaries with active connections. It sends the request to the 
first secondary that accepts the connection. When this parameter is set to 
`false`, `mongos` holds secondary reads until it can establish 
a connection to a specific secondary, (except in the case of 
hedged reads).

**Note:**

Under certain workloads, opportunistic reads may trigger the 
opening of unnecessary connections from `mongos` to 
`mongod` and reduce overall performance. 
This parameter should not be enabled unless your application has 
a specific need for the feature.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command

- To set the parameter at startup, use the
  `setParameter` setting

For example, to set `opportunisticSecondaryTargeting` during startup:

```bash
mongos --setParameter opportunisticSecondaryTargeting=true
```

**`shardedIndexConsistencyCheckIntervalMS`**

Available for `mongod` only.

*Type*: integer

*Default*: 600000

If set on the config server's primary, the interval, in
milliseconds, at which the config server's primary checks the index
consistency of sharded collections. The parameter has no effect on
the `mongod` if it is not the config server's primary.

This parameter is only available at startup. To set the
parameter, use the `setParameter` setting. 

For example, the following sets the interval at 300000 milliseconds
(5 minutes) at startup:

```javascript
mongod --setParameter shardedIndexConsistencyCheckIntervalMS=300000
```

**See also:**

- `enableShardedIndexConsistencyCheck` parameter
- `shardedIndexConsistency` metrics returned by the
  `serverStatus` commandq

**`enableFinerGrainedCatalogCacheRefresh`**

Available for both `mongod` and `mongos`.

*Type*: boolean

*Default*: true

This parameter allows the catalog cache to be refreshed only if the
shard needs to be refreshed. If disabled, any stale chunk will cause
the entire chunk distribution for a collection to be considered stale
and force all routers who
contact the shard to refresh their shard catalog cache.

This parameter is only available at startup. To set the
parameter, use the `setParameter` setting. 

```bash
mongod --setParameter enableFinerGrainedCatalogCacheRefresh=true
mongos --setParameter enableFinerGrainedCatalogCacheRefresh=true
```

**See also:**

- sharding-background
- `shardingStatistics.catalogCache`

**`maxTimeMSForHedgedReads`**

Available for `mongos` only.

*Type*: integer

*Default*: 150

Specifies the maximum time limit (in milliseconds) for the
hedged read. That is, the additional
read sent to hedge the read operation uses the `maxTimeMS` value
of `maxTimeMSForHedgedReads` while the read operation
that is being hedged uses the `maxTimeMS` value specified for the
operation.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command

- To set the parameter at startup, use the
  `setParameter` setting

For example, to set the limit to 200 milliseconds, you can issue the
following during startup:

```bash
mongos --setParameter maxTimeMSForHedgedReads=200
```

Or if using the `setParameter` command in a
`mongosh` session that is connected to a running
`mongos`:

```javascript
db.adminCommand( { setParameter: 1, maxTimeMSForHedgedReads: 200 } )
```

**See also:**

- `readHedgingMode`
- mongos-hedged-reads

**`maxCatchUpPercentageBeforeBlockingWrites`**

**New in version:** 5.0

Available for `mongod` only.

*Type*: integer

*Default*: 10

For `moveChunk` and `moveRange` operations, 
specifies the maximum percentage of untrasferred data allowed by the 
migration protocol (expressed in percentage of the total chunk size) 
to transition from the `catchup` phase to the `commit` phase.

Setting a higher catchup percentage can decrease the amount of time
it takes for the migration to complete at the cost of increased
latency during concurrent `upsert`
and `delete` operations.

This parameter is only available at startup. To set the
parameter, use the `setParameter` setting. 

**Changed in version:** 7.1 (and 7.0.1), you can set the

parameter during runtime. 

For example, to set the maximum percentage to 20, you can issue the
following during startup:

```bash
mongod --setParameter maxCatchUpPercentageBeforeBlockingWrites=20
```

You cannot change
`maxCatchUpPercentageBeforeBlockingWrites` during runtime.

**See also:**

[Live Migration Protocol](https://github.com/mongodb/mongo/blob/master/src/mongo/db/s/README.md#the-live-migration-protocol)

**`metadataRefreshInTransactionMaxWaitBehindCritSecMS`**

**New in version:** 5.2 (*Also available starting in 5.1.0, 5.0.4*)

*Type*: integer

*Default*: 500

Available for `mongod` only.

Limits the time a shard waits for a critical section within a
transaction. 

When a query accesses a shard, a chunk migration or DDL operation may already hold the critical
section for the collection. If the query finds the critical
section is taken, the shard waits until the critical section has
been released. When the shard returns control to `mongos`,
`mongos` retries the query. However, if a multi-shard
transaction interacts with an operation that takes the critical
section on multiple shards, the interaction can result in a
distributed deadlock.

`metadataRefreshInTransactionMaxWaitBehindCritSecMS`
limits the maximum time a shard waits within a transaction for the
critical section to be released.

To reduce the maximum wait time for the critical section within a
transaction, lower the value of
`metadataRefreshInTransactionMaxWaitBehindCritSecMS`. 

**Warning:**

If `metadataRefreshInTransactionMaxWaitBehindCritSecMS`
is too low, `mongos` could use all of its retry attempts
and return an error.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command

- To set the parameter at startup, use the
  `setParameter` setting

For example, to set `metadataRefreshInTransactionMaxWaitBehindCritSecMS`
to 400 milliseconds:

```javascript
db.adminCommand( { setParameter: 1, metadataRefreshInTransactionMaxWaitBehindCritSecMS: 400 } )
```

**`readHedgingMode`**

Available for `mongos` only.

*Type*: string

*Default*: on

Specifies whether `mongos` supports hedged reads for
those read operations whose read preference have enabled the hedged read option.

Available values are:

| Value | Description |
|---|---|
| `on` | The `mongos` instance supports hedged reads for read operations whose read preference have enabled the hedged read option. |
| `off` | The `mongos` instance does not support hedged reads. That is, hedged reads are unavailable, even for read operations whose read preference have enabled the hedged read option. |

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command

- To set the parameter at startup, use the
  `setParameter` setting

For example, to turn off hedged read support for a
`mongos` instance, you can issue the following during
startup:

```bash
mongos --setParameter readHedgingMode=off
```

Or if using the `setParameter` command in a
`mongosh` session that is connected to a running
`mongos`:

```javascript
db.adminCommand( { setParameter: 1, readHedgingMode: "off" } )
```

**See also:**

- mongos-hedged-reads
- `maxTimeMSForHedgedReads`

**`routingTableCacheChunkBucketSize`**

**New in version:** 6.0.10

Available for both `mongod` and `mongos`.

*Type*: integer

*Default*: 500

Specifies the size of the routing table cache buckets used to 
implement chunk grouping optimization. Must be greater than `0`.

This parameter is only available at startup. To set the
parameter, use the `setParameter` setting. 

For example, to set the cache chunk bucket size to `250` on a 
`mongod`, issue the following command at startup:

```bash
mongod --setParameter routingTableCacheChunkBucketSize=1000
```

**`shutdownTimeoutMillisForSignaledShutdown`**

**New in version:** 5.0

*Type*: integer

*Default*: 15000

Available for `mongod` only.

Specifies the time (in milliseconds) to wait for any ongoing database
operations to complete before initiating a shutdown of
`mongod` in response to a `SIGTERM` signal.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command

- To set the parameter at startup, use the
  `setParameter` setting

For example, to set the time to 250 milliseconds, you can issue the
following during startup:

```bash
mongod --setParameter shutdownTimeoutMillisForSignaledShutdown=250
```

Or if using the `setParameter` command in a
`mongosh` session that is connected to a running
`mongod`:

```javascript
db.adminCommand( { setParameter: 1, shutdownTimeoutMillisForSignaledShutdown: 250 } )
```

**`mongosShutdownTimeoutMillisForSignaledShutdown`**

**New in version:** 5.0

*Type*: integer

*Default*: 15000

Available for `mongos` only.

Specifies the time (in milliseconds) to wait for any ongoing database
operations to complete before initiating a shutdown of
`mongos` in response to a `SIGTERM` signal.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command

- To set the parameter at startup, use the
  `setParameter` setting

For example, to set the time to 250 milliseconds, you can issue the
following during startup:

```bash
mongos --setParameter mongosShutdownTimeoutMillisForSignaledShutdown=250
```

Or if using the `setParameter` command in a
`mongosh` session that is connected to a running
`mongos`:

```javascript
db.adminCommand( { setParameter: 1, mongosShutdownTimeoutMillisForSignaledShutdown: 250 } )
```

**`ShardingTaskExecutorPoolHostTimeoutMS`**

Type: integer

Default: 300000 (5 minutes)

Available for both `mongod` and `mongos`.

Maximum time that `mongos` goes without communication to a
host before `mongos` drops all connections to the host.

If set, `ShardingTaskExecutorPoolHostTimeoutMS` should be
greater than the sum of
`ShardingTaskExecutorPoolRefreshRequirementMS` and
`ShardingTaskExecutorPoolRefreshTimeoutMS`. Otherwise,
`mongos` adjusts the value of
`ShardingTaskExecutorPoolHostTimeoutMS` to be greater than the
sum.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command

- To set the parameter at startup, use the
  `setParameter` setting

The following example sets
`ShardingTaskExecutorPoolHostTimeoutMS` to `120000`
during startup:

```bash
mongos --setParameter ShardingTaskExecutorPoolHostTimeoutMS=120000
```

During runtime, you can also set the parameter with the
`setParameter` command:

```javascript
db.adminCommand( { setParameter: 1, ShardingTaskExecutorPoolHostTimeoutMS: 120000 } )
```

**`ShardingTaskExecutorPoolMaxConnecting`**

Type: integer

Default: 2

Available for both `mongod` and `mongos`.

Maximum number of simultaneous initiating connections (including
pending connections in setup/refresh state) each TaskExecutor
connection pool can have to a `mongod` instance. You can
set this parameter to control the rate at which `mongos`
adds connections to a `mongod` instance.

If set, `ShardingTaskExecutorPoolMaxConnecting` should be
less than or equal to `ShardingTaskExecutorPoolMaxSize`.
If it is greater, `mongos` ignores the
`ShardingTaskExecutorPoolMaxConnecting` value.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command

- To set the parameter at startup, use the
  `setParameter` setting

The following example sets
`ShardingTaskExecutorPoolMaxConnecting` to `20`
during startup:

```bash
mongos --setParameter ShardingTaskExecutorPoolMaxConnecting=20
```

During runtime, you can also set the parameter with the
`setParameter` command:

```javascript
db.adminCommand( { setParameter: 1, ShardingTaskExecutorPoolMaxConnecting: 20 } )
```

**`ShardingTaskExecutorPoolMaxSize`**

Type: integer

Default: 2`64` - 1

Available for both `mongod` and `mongos`.

Maximum number of outbound connections each TaskExecutor connection
pool can open to any given `mongod` instance. The maximum
possible connections to any given host across all TaskExecutor pools
is:

```none
ShardingTaskExecutorPoolMaxSize * taskExecutorPoolSize
```

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command

- To set the parameter at startup, use the
  `setParameter` setting

The following example sets
`ShardingTaskExecutorPoolMaxSize` to `20`
during startup:

```bash
mongos --setParameter ShardingTaskExecutorPoolMaxSize=20
```

During runtime, you can also set the parameter with the
`setParameter` command:

```javascript
db.adminCommand( { setParameter: 1, ShardingTaskExecutorPoolMaxSize: 20 } )
```

`mongos` can have up to `n` TaskExecutor connection
pools, where `n` is the number of cores. See
`taskExecutorPoolSize`.

**See also:**

`ShardingTaskExecutorPoolMinSize`

**`ShardingTaskExecutorPoolMaxSizeForConfigServers`**

**New in version:** 6.0

Type: integer

Default: -1

Available for both `mongod` and `mongos`.

Optional override for `ShardingTaskExecutorPoolMinSize` to set the minimum number
of outbound connections each TaskExecutor connection pool can open to a
configuration server.

When set to:

- `-1`, `ShardingTaskExecutorPoolMinSize` is used. This is the default.

- an integer value greater than `-1`, overrides the
  minimum number of outbound connections each TaskExecutor
  connection pool can open to a configuration server.

Parameter only applies to sharded deployments.

The following example sets `ShardingTaskExecutorPoolMinSize` to `2` during startup, which
sets the minimum number of outbound connections each
TaskExecutor connection pool can open to a configuration server to
`2`:

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command

- To set the parameter at startup, use the
  `setParameter` setting

```bash
mongos --setParameter ShardingTaskExecutorPoolMaxSizeForConfigServers=2
```

During runtime, you can also set the parameter with the
`setParameter` command:

```javascript
db.adminCommand( { setParameter: 1, ShardingTaskExecutorPoolMaxSizeForConfigServers: 2 } )
```

**`ShardingTaskExecutorPoolMinSize`**

Type: integer

Default: 1

Available for both `mongod` and `mongos`.

Minimum number of outbound connections each TaskExecutor connection
pool can open to any given `mongod` instance.

`ShardingTaskExecutorPoolMinSize` connections are created the
first time a connection to a new host is requested from the pool.
While the pool is idle, the pool maintains this number of
connections until `ShardingTaskExecutorPoolHostTimeoutMS`
milliseconds pass without any application using that pool.

For a `mongos` using the
`warmMinConnectionsInShardingTaskExecutorPoolOnStartup`
parameter, the `ShardingTaskExecutorPoolMinSize` parameter also
controls how many connections to each shard host are established on
startup of the `mongos` instance before it begins
accepting incoming client connections.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command

- To set the parameter at startup, use the
  `setParameter` setting

The following example sets
`ShardingTaskExecutorPoolMinSize` to `2`
during startup:

```bash
mongos --setParameter ShardingTaskExecutorPoolMinSize=2
```

During runtime, you can also set the parameter with the
`setParameter` command:

```javascript
db.adminCommand( { setParameter: 1, ShardingTaskExecutorPoolMinSize: 2 } )
```

`mongos` can have up to `n` TaskExecutor connection
pools, where `n` is the number of cores. See
`taskExecutorPoolSize`.

**See also:**

- `ShardingTaskExecutorPoolMaxSize`
- `warmMinConnectionsInShardingTaskExecutorPoolOnStartup`

**`ShardingTaskExecutorPoolMinSizeForConfigServers`**

**New in version:** 6.0

Type: integer

Default: -1

Available for both `mongod` and `mongos`.

Optional override for `ShardingTaskExecutorPoolMinSize` to set the minimum number
of outbound connections each TaskExecutor connection pool can open to a
configuration server.

When set to:

- `-1`, `ShardingTaskExecutorPoolMinSize` is used. This is the default.

- an integer value greater than `-1`, overrides the
  minimum number of outbound connections each TaskExecutor
  connection pool can open to a configuration server.

Parameter only applies to sharded deployments.

The following example sets `ShardingTaskExecutorPoolMinSize` to `2` during startup, which
sets the minimum number of outbound connections each
TaskExecutor connection pool can open to a configuration server to
`2`:

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command

- To set the parameter at startup, use the
  `setParameter` setting

```bash
mongos --setParameter ShardingTaskExecutorPoolMinSizeForConfigServers=2
```

During runtime, you can also set the parameter with the
`setParameter` command:

```javascript
db.adminCommand( { setParameter: 1, ShardingTaskExecutorPoolMinSizeForConfigServers: 2 } )
```

**`ShardingTaskExecutorPoolRefreshRequirementMS`**

Type: integer

Default: 60000 (1 minute)

Available for both `mongod` and `mongos`.

Maximum time the `mongos` waits before attempting to
heartbeat an idle connection in the pool. An idle connection may be 
discarded during the refresh if the pool is above its 
minimum size. 

If set, `ShardingTaskExecutorPoolRefreshRequirementMS` should be
greater than `ShardingTaskExecutorPoolRefreshTimeoutMS`.
Otherwise, `mongos` adjusts the value of
`ShardingTaskExecutorPoolRefreshTimeoutMS` to be less than
`ShardingTaskExecutorPoolRefreshRequirementMS`.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command

- To set the parameter at startup, use the
  `setParameter` setting

The following example sets
`ShardingTaskExecutorPoolRefreshRequirementMS` to
`90000` during startup:

```bash
mongos --setParameter ShardingTaskExecutorPoolRefreshRequirementMS=90000
```

During runtime, you can also set the parameter with the
`setParameter` command:

```javascript
db.adminCommand( { setParameter: 1, ShardingTaskExecutorPoolRefreshRequirementMS: 90000 } )
```

**`ShardingTaskExecutorPoolRefreshTimeoutMS`**

Type: integer

Default: 20000 (20 seconds)

Available for both `mongod` and `mongos`.

Maximum time the `mongos` waits for a heartbeat before
timing out the heartbeat.

If set, `ShardingTaskExecutorPoolRefreshTimeoutMS` should be
less than `ShardingTaskExecutorPoolRefreshRequirementMS`.
Otherwise, `mongos` adjusts the value of
`ShardingTaskExecutorPoolRefreshTimeoutMS` to be less than
`ShardingTaskExecutorPoolRefreshRequirementMS`.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command

- To set the parameter at startup, use the
  `setParameter` setting

The following example sets
`ShardingTaskExecutorPoolRefreshTimeoutMS` to
`30000` during startup:

```bash
mongos --setParameter ShardingTaskExecutorPoolRefreshTimeoutMS=30000
```

During runtime, you can also set the parameter with the
`setParameter` command:

```javascript
db.adminCommand( { setParameter: 1, ShardingTaskExecutorPoolRefreshTimeoutMS: 30000 } )
```

**`ShardingTaskExecutorPoolReplicaSetMatching`**

**Changed in version:** 5.0

Available for both `mongod` and `mongos`.

Type: string

Default: "automatic"

On a `mongos` instance, this parameter sets the policy
that determines the minimum size limit of its connection pools to
nodes within replica sets.

On a `mongod` instance, this parameter sets the policy
that determines the minimum size limit of its connection pools to
nodes within *other* replica sets.

Note that this parameter only manages connections for operations that
are directly related to user requests and CRUD operations.

Available values are:

| Matching Policy | Description |
|---|---|
| `"automatic"` (Default) | Starting in 5.0, `"automatic"` is the new default value. When set for a `mongos`, the instance follows the behavior specified for the `"matchPrimaryNode"` option. When set for a `mongod`, the instance follows the behavior specified for the `"disabled"` option. WARNING: If the `ShardingTaskExecutorPoolReplicaSetMatching` is set to `"automatic"`, the `replicaSetMatchingStrategy` still describes the actual policy being used, not `"automatic"`. To find the value of the `ShardingTaskExecutorPoolReplicaSetMatching`, use `getParameter` which returns the value of the server parameter. |
| `"matchPrimaryNode"` | When set for a `mongos`, the minimum size limit of the instance's connection pool to each secondary of a replica set in the sharded cluster (specifically, shard replica set and config servers) is equal to the size of its connection pool to that replica set's primary. When set for a `mongod`, the minimum size limit of the instance's connection pool to each secondary of another replica set in the sharded cluster (specifically, shard replica set and config servers) is equal to the size of its connection pool to that replica set's primary. WARNING: If multiple shard servers in your topology can experience a rapid influx of cross-shard operations, do not set this option on your `mongod` instances. In case of a primary stepdown, `matchPrimaryNode` ensures that any secondary that becomes the primary can handle the current level of primary reads and writes. |
| `"matchBusiestNode"` | When set for a `mongos`, the instance's minimum size limit of the connection pool to each member of a replica set in the sharded cluster (specifically, shard replica set and config servers) is equal to the largest among the active connection counts to the primary and each secondary member of that replica set. When set for a `mongod`, the instance's minimum size limit of the connection pool to each member of another replica set in the sharded cluster (specifically, shard replica set and config servers) is equal to the largest among the active connection counts to the primary and each secondary member of that replica set. With `"matchBusiestNode"`, `mongos` maintains enough connections to each secondary to handle the current level of primary and secondary reads and writes. The number of connections to maintain in the pool decreases as the number of active connections decreases. |
| `"disabled"` | When set for a `mongos`, the instance's minimum number of connections in the instance's connection pool to each node of a replica set in the sharded clusterv (specifically, shard replica set and config servers) is equal to the `ShardingTaskExecutorPoolMinSize`. When set for a `mongod`, the instance's minimum number of connections in the instance's connection pool to each node of another replica set in the sharded cluster (specifically, shard replica set and config servers) is equal to the `ShardingTaskExecutorPoolMinSize`. |

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command

- To set the parameter at startup, use the
  `setParameter` setting

The following example sets the
`ShardingTaskExecutorPoolReplicaSetMatching` to
`"automatic"` during startup:

```bash
mongod --setParameter ShardingTaskExecutorPoolReplicaSetMatching="automatic"
```

During runtime, you can also set the parameter with the
`setParameter` command:

```javascript
db.adminCommand( { setParameter: 1,  ShardingTaskExecutorPoolReplicaSetMatching: "automatic" } )
```

**`taskExecutorPoolSize`**

Type: integer

Default: 1

Available for `mongos` only.

The number of Task Executor connection pools to use for a given
`mongos`.

If the parameter value is `0` or less, the number of Task Executor
connection pools is the number of cores with the following
exceptions:

- If the number of cores is less than 4, the number of Task Executor
  connection pools is 4.

- If the number of cores is greater than 64, the number of Task
  Executor connection pools is 64.

**Important:**

Before you modify the `taskExecutorPoolSize` value on Linux, consult
with a MongoDB Support professional.
Modifying this parameter may cause performance regressions.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command

- To set the parameter at startup, use the
  `setParameter` setting

```bash
mongos --setParameter taskExecutorPoolSize=6
```

**See also:**

- `ShardingTaskExecutorPoolMaxSize`
- `ShardingTaskExecutorPoolMinSize`

**`loadRoutingTableOnStartup`**

Available for `mongos` only.

Type: boolean

*Default*: true

Configures a `mongos` instance to preload the routing
table for a sharded cluster on startup. With this setting
enabled, the `mongos` caches the cluster-wide routing
table for each sharded collection as part of its startup procedure,
before it begins accepting client connections.

Without this setting enabled, the `mongos` only loads
a routing table as needed for incoming client connections, and only
loads the specific routing table for the namespace of a given
request.

A `mongos` instance with the
`loadRoutingTableOnStartup` parameter enabled may
experience longer startup times, but will result in faster servicing
of initial client connections once started.

`loadRoutingTableOnStartup` is enabled by default.

This parameter is only available at startup. To set the
parameter, use the `setParameter` setting. 

**`warmMinConnectionsInShardingTaskExecutorPoolOnStartup`**

Available for `mongos` only.

Type: boolean

*Default*: true

Configures a `mongos` instance to prewarm its connection
pool on startup. With this parameter enabled, the
`mongos` attempts to establish
`ShardingTaskExecutorPoolMinSize` network
connections to each shard server as part of its startup procedure,
before it begins accepting client connections.

A timeout for this behavior can be configured with the
`warmMinConnectionsInShardingTaskExecutorPoolOnStartupWaitMS`
parameter. If this timeout is reached, the `mongos` will
begin accepting client connections regardless of the size of its
connection pool.

A `mongos` instance with this parameter enabled may
experience longer startup times, but will result in faster servicing
of initial client connections once started.

`warmMinConnectionsInShardingTaskExecutorPoolOnStartup` is
enabled by default.

This parameter is only available at startup. To set the
parameter, use the `setParameter` setting. 

**See also:**

- `warmMinConnectionsInShardingTaskExecutorPoolOnStartupWaitMS`
- `ShardingTaskExecutorPoolMinSize`

**`warmMinConnectionsInShardingTaskExecutorPoolOnStartupWaitMS`**

Available for `mongos` only.

Type: integer

*Default*: 2000 (2 seconds)

Sets the timeout threshold in milliseconds for a
`mongos` to wait for `ShardingTaskExecutorPoolMinSize`
connections to be established per shard host when using the
`warmMinConnectionsInShardingTaskExecutorPoolOnStartup`
parameter. If this timeout is reached, the `mongos` will
begin accepting client connections regardless of the size of its
connection pool.

This parameter is only available at startup. To set the
parameter, use the `setParameter` setting. 

**See also:**

- `warmMinConnectionsInShardingTaskExecutorPoolOnStartup`
- `ShardingTaskExecutorPoolMinSize`

**`migrateCloneInsertionBatchDelayMS`**

Available for `mongod` only.

Type: Non-negative integer

Default: 0

Time in milliseconds to wait between batches of insertions during
cloning step of the migration process. This wait is in addition to
the `secondaryThrottle`.

The default value of `0` indicates no additional wait.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command

- To set the parameter at startup, use the
  `setParameter` setting

The following sets the `migrateCloneInsertionBatchDelayMS` to 200
milliseconds:

```bash
mongod --setParameter migrateCloneInsertionBatchDelayMS=200
```

The parameter may also be set using the `setParameter`
command:

```javascript
db.adminCommand( { setParameter: 1, migrateCloneInsertionBatchDelayMS: 200 } )
```

**`migrateCloneInsertionBatchSize`**

Available for `mongod` only.

Type: Non-negative integer

Default: 0

The maximum number of documents to insert in a single batch during
the cloning step of the migration process.

The default value of `0` indicates no maximum number of documents
per batch. However, in practice, this results in batches that
contain up to 16 MB of documents.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command

- To set the parameter at startup, use the
  `setParameter` setting

The following sets the `migrateCloneInsertionBatchSize` to 100
documents:

```bash
mongod --setParameter migrateCloneInsertionBatchSize=100
```

The parameter may also be set using the `setParameter`
command:

```javascript
db.adminCommand( { setParameter: 1, migrateCloneInsertionBatchSize: 100 } )
```

**`orphanCleanupDelaySecs`**

Default: 900 (15 minutes)

Available for `mongod` only.

Minimum delay before a migrated chunk is deleted from the source
shard.

Before deleting the chunk during chunk migration, MongoDB waits for
`orphanCleanupDelaySecs` or for in-progress queries
involving the chunk to complete on the shard primary, whichever is
longer.

However, because the shard primary has no knowledge of in-progress queries
run on the shard secondaries, queries that use the chunk but are run on
secondaries may see documents disappear if these queries take longer than
the time to complete the shard primary queries and the
`orphanCleanupDelaySecs`.

**Note:**

This behavior only affects in-progress queries that start before the
chunk migration. Queries that start after the chunk migration starts
will not use the migrating chunk.

If a shard has storage constraints, consider reducing this value
temporarily. If running queries that exceed 15 minutes on shard
secondaries, consider increasing this value.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command

- To set the parameter at startup, use the
  `setParameter` setting

The following sets the `orphanCleanupDelaySecs` to 20 minutes:

```bash
mongod --setParameter orphanCleanupDelaySecs=1200
```

This may also be set using the `setParameter` command:

```javascript
db.adminCommand( { setParameter: 1, orphanCleanupDelaySecs: 1200 } )
```

**`persistedChunkCacheUpdateMaxBatchSize`**

**New in version:** 6.0.13 (and 5.0.25)

Available for `mongod` only.

Type: Integer

Default: 1000

To route and serve operations, shards must know the routing and
ownership information associated with their collections. This
information propogates from a shard's primary node to its
secondary nodes through the replication of the internal cache
collections `config.cache.collections` and
`config.cache.chunks.<collectionName>`.

In previous versions, updates on the chunk cache collection were
performed individually (meaning that an entry was deleted and a new
entry was inserted). Starting in MongoDB 6.0.13, these updates are
performed as a batch of deletions followed by a batch of insertions.
The updated logic improves performance for collections that contain a
large number of chunks.

The `persistedChunkCacheUpdateMaxBatchSize` parameter specifies the
maximum batch size used for updating the persisted chunk cache.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command

- To set the parameter at startup, use the
  `setParameter` setting

The following example sets `persistedChunkCacheUpdateMaxBatchSize`
to 700 at startup:

```bash
mongod --setParameter persistedChunkCacheUpdateMaxBatchSize=700
```

You can also set `persistedChunkCacheUpdateMaxBatchSize` during
runtime:

```javascript
db.adminCommand( { setParameter: 1, persistedChunkCacheUpdateMaxBatchSize: 700 } )
```

**`rangeDeleterBatchDelayMS`**

Available for `mongod` only.

Type: Non-negative integer

Default: 20

The amount of time in milliseconds to wait before the next batch of
deletion during the cleanup stage of range migration (or the `cleanupOrphaned`
command).

The _secondaryThrottle replication delay occurs after each batch deletion.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command

- To set the parameter at startup, use the
  `setParameter` setting

The following sets the `rangeDeleterBatchDelayMS` to 200
milliseconds:

```bash
mongod --setParameter rangeDeleterBatchDelayMS=200
```

The parameter may also be set using the `setParameter`
command:

```javascript
db.adminCommand( { setParameter: 1, rangeDeleterBatchDelayMS: 200 } )
```

**`rangeDeleterBatchSize`**

Available for `mongod` only.

Type: Non-negative integer

Default: 2147483647 starting in MongoDB 5.1.2 and 5.0.6

The maximum number of documents in each batch to delete during the
cleanup stage of range migration
(or the `cleanupOrphaned` command).

A value of `0` indicates that the system chooses the default value.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command

- To set the parameter at startup, use the
  `setParameter` setting

The following example sets `rangeDeleterBatchSize` to 32
documents:

```bash
mongod --setParameter rangeDeleterBatchSize=32
```

The parameter may also be set using the `setParameter`
command:

```javascript
db.adminCommand( { setParameter: 1, rangeDeleterBatchSize: 32 } )
```

**Tip:**

In versions prior to 6.0.3, the new value of `rangeDeleterBatchSize` is
only applied to range deletions created after the value is changed. To
apply the new value to existing range deletions, force a step down.

From 6.0.3 on, the new value of the parameter is applied to all the range deletions processed 
after the update, regardless of when the range deletion was created.

**`skipShardingConfigurationChecks`**

Available for `mongod` only.

Type: boolean

Default: false

When `true`, allows for starting a shard member or config server
member as a standalone for maintenance operations. This parameter is
mutually exclusive with the `--configsvr` or `--shardsvr` options.

This parameter is only available at startup. To set the
parameter, use the `setParameter` setting. 

```bash
mongod --setParameter skipShardingConfigurationChecks=true
```

**Important:**

Once maintenance has completed, remove the
`skipShardingConfigurationChecks` parameter when
restarting the `mongod`.

**`findChunksOnConfigTimeoutMS`**

**New in version:** 5.0

Available for both `mongod` and `mongos`.

Type: Non-negative integer

Default: 900000

The timeout in milliseconds for find operations on
`chunks`.

If there is a large number of chunks in the cluster and chunk loading
fails with the error `ExceededTimeLimit`, increase the parameter
value:

```bash
mongod --setParameter findChunksOnConfigTimeoutMS=1000000
```

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command

- To set the parameter at startup, use the
  `setParameter` setting
