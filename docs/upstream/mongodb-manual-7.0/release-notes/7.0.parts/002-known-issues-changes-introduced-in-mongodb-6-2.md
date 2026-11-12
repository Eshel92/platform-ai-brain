<!-- Part 2 of 3 of release-notes/7.0.md (split because the page is big). -->

## Known Issues

This section describes known issues in MongoDB 7.0 and their resolution
status.

| In Version | Issue | Status |
|---|---|---|
| 7.0.29, 7.0.30 | .. include:: /includes/known-issue-mongrocryptd-size-limit.rst | Unresolved. |


## Atlas Search Index Management

Starting in MongoDB 7.0, you can manage Atlas Search indexes with `mongosh`
methods and database commands. Atlas Search index commands are only available
for deployments hosted on MongoDB Atlas, and require an
Atlas cluster tier of at least M10.

To manage Atlas Search indexes, use the following commands:

### mongosh Methods

| Name | Description |
|---|---|
| `db.collection.createSearchIndex()` | .. include:: /includes/atlas-search-commands/command-descriptions/createSearchIndex-method.rst |
| `db.collection.dropSearchIndex()` | .. include:: /includes/atlas-search-commands/command-descriptions/dropSearchIndex-description.rst |
| `db.collection.getSearchIndexes()` | .. include:: /includes/atlas-search-commands/command-descriptions/getSearchIndexes-description.rst |
| `db.collection.updateSearchIndex()` | .. include:: /includes/atlas-search-commands/command-descriptions/updateSearchIndex-description.rst |

### Database Commands

| Name | Description |
|---|---|
| `createSearchIndexes` | .. include:: /includes/atlas-search-commands/command-descriptions/createSearchIndexes-description.rst |
| `dropSearchIndex` | .. include:: /includes/atlas-search-commands/command-descriptions/dropSearchIndex-description.rst |
| `updateSearchIndex` | .. include:: /includes/atlas-search-commands/command-descriptions/updateSearchIndex-description.rst |

### Aggregation Stages

| Name | Description |
|---|---|
| `$listSampledQueries` | Lists sampled queries for all collections or a specific collection. |
| `$listSearchIndexes` | .. include:: /includes/atlas-search-commands/command-descriptions/getSearchIndexes-description.rst |


## General Changes

### serverStatus Output

Starting in MongoDB 7.0.38, you can exclude all optional fields 
from the `serverStatus` output by specifying `none: 1`. 
After you exclude all optional fields, you can then specify
the fields you want to include.

For details, see serverstatus-excl-fields.

### Oplog serverStatus Metrics

MongoDB 7.0.42 adds the following `serverStatus` metrics:

- `metrics.repl.network.oplogFetcherLagSeconds`
- `metrics.repl.network.oplogGetMoresProcessed`

### Cache Refresh Time Fields

Starting in MongoDB 7.0, log messages for slow queries includes a new cache refresh time field.

### Concurrent Storage Engine Transactions (Read and Write Tickets)

Starting in version 7.0, MongoDB uses a default algorithm to dynamically
adjust the maximum number of concurrent storage engine transactions
(including both read and write tickets) to optimize database throughput
during overload.

The following table summarizes how to identify overload scenarios for MongoDB 
7.0 and prior releases:

| Version | Diagnosing Overload Scenarios |
|---|---|
| 7.0 | A large number of queued operations that persists for a prolonged period of time likely indicates an overload. A concurrent storage engine transaction (ticket) availability of 0 for a prolonged period of time **does not** indicate an overload. |
| 6.0 and prior | A large number of queued operations that persists for a prolonged period of time likely indicates an overload. A concurrent storage engine transaction (ticket) availibility of 0 for a prolonged period of time likely indicates an overload. |

To learn more, see:

- `wiredTiger.concurrentTransactions` 
- `storageEngineConcurrentReadTransactions` 
- `storageEngineConcurrentWriteTransactions`

### `currentOp` Metrics

Starting in MongoDB 7.0, the `currentOp` command and the
`db.currentOp()` method include these new fields:

- `currentOp.collUuid`
- `currentOp.startTime`
- `currentOp.samplesPerSecond`
- `currentOp.sampledReadsCount`
- `currentOp.sampledWritesCount`
- `currentOp.sampledReadsBytes`
- `currentOp.sampledWritesBytes`

### `$currentOp` (aggregation) Metrics

Starting in MongoDB 7.0, the currentOp 
aggregation stage includes these new fields: 

- `$currentOp.collUuid`
- `$currentOp.startTime`
- `$currentOp.samplesPerSecond`
- `$currentOp.sampledReadsCount`
- `$currentOp.sampledWritesCount`
- `$currentOp.sampledReadsBytes`
- `$currentOp.sampledWritesBytes`

### Compound Wildcard Indexes

Starting in MongoDB 7.0, you can create compound wildcard indexes. A compound wildcard index has one wildcard
term and one or more additional index terms.

Use compound wildcard indexes to support queries on known patterns and
to limit the total number of indexes in a collection. 

### Disk Space

Starting in MongoDB 7.0, if disk space is running low,
MongoDB fails queries that spill to disk.

### Large Change Stream Events

Starting in MongoDB 7.0, if you have change stream events larger than 16 MB, you can use the new
`$changeStreamSplitLargeEvent` stage to split the events into
smaller fragments.

The following new metrics report information about large change stream
events:

- `metrics.changeStreams`
- `metrics.changeStreams.largeEventsFailed`
- `metrics.changeStreams.largeEventsSplit`

### serverStatus Output Change

`serverStatus` includes the following new fields in its
output:

Plan Cache Metrics
  - `planCache`

queryAnalyzer Metrics
  - `queryAnalyzers.activeCollections` 
  - `queryAnalyzers.totalCollections`
  - `queryAnalyzers.totalSampledReadsCount`
  - `queryAnalyzers.totalSampledWritesCount`
  - `queryAnalyzers.totalSampledReadsBytes`
  - `queryAnalyzers.totalSampledWritesBytes`

### Slot-Based Query Execution Engine

Starting in MongoDB 7.0, the slot-based query execution engine improves
performance for a wider range of find and aggregation queries.

Slow query log messages now
include a `queryFramework` field that indicates which query engine
completed the query:

- `queryFramework: "classic"` indicates that the classic engine
  completed the query.

- `queryFramework: "sbe"` indicates that the slot-based query execution engine completed the
  query.

### User Roles System Variable

Starting in MongoDB 7.0, you can use the new `USER_ROLES`
system variable to return the roles of the current user.

For use cases that include `USER_ROLES`, see the find, aggregation, view, updateOne, updateMany, and
findAndModify
examples.

### New Sharding Statistics for Chunk Migrations

Available starting in MongoDB 7.0 (and 6.3.2, 6.0.6, and 5.0.18).

MongoDB includes the following new sharding statistics for chunk
migrations:

- `shardingStatistics.countDonorMoveChunkCommitted`
- `shardingStatistics.countDonorMoveChunkAborted`
- `shardingStatistics.totalDonorMoveChunkTimeMillis`
- `shardingStatistics.countBytesClonedOnRecipient`
- `shardingStatistics.countDocsClonedOnCatchUpOnRecipient`
- `shardingStatistics.countBytesClonedOnCatchUpOnRecipient`

### New Slow Query Log Message

The `totalOplogSlotDurationMicros` in the slow query log message shows the 
time between a write operation getting a commit timestamp to commit the 
storage engine writes and actually committing. `mongod` supports 
parallel writes. However, it commits write operations with commit 
timestamps in any order. 

To learn more, see log-message-slow-ops.

### New Parameters

#### analyzeShardKey-related Parameters

MongoDB 7.0 adds the following parameters related to the 
`analyzeShardKey` command:

- `analyzeShardKeyCharacteristicsDefaultSampleSize`
- `analyzeShardKeyMonotonicityCorrelationCoefficientThreshold`
- `analyzeShardKeyNumMostCommonValues`
- `analyzeShardKeyNumRanges`
- `analyzeShardKeyNumSamplesPerRange`

#### autoMergerIntervalSecs Parameter

MongoDB 7.0 adds the `autoMergerIntervalSecs` parameter 
which, when AutoMerger is enabled, specifies the amount of 
time between automerging rounds, in seconds. 
`autoMergerIntervalSecs` can only be set on config servers of sharded
clusters.

#### autoMergerThrottlingMS Parameter

MongoDB 7.0 adds the `autoMergerThrottlingMS` which, when 
AutoMerger is enabled, specifies the minimum amount time 
between merges initiated by the AutoMerger on the same 
collection, in milliseconds. `autoMergerThrottlingMS` can only be set
on config servers of sharded clusters.

#### balancerMigrationsThrottlingMs Parameter

MongoDB 7.0 adds the `balancerMigrationsThrottlingMs`
parameter which allows you to throttle the balancing rate.

#### enableDetailedConnectionHealthMetricLogLines Parameter

MongoDB 7.0 adds the `enableDetailedConnectionHealthMetricLogLines`
parameter which lets you specify whether a set of log messages related to cluster connection health metrics appears in the
log.

#### `oidcIdentityProviders` Parameter

MongoDB 7.0  adds the `oidcIdentityProviders` parameter which allows 
you to specify identity provider (IDP) configurations when using 
OpenID Connect authentication. 

#### configureQueryAnalysis-related Parameters

MongoDB 7.0 adds the following parameters related to the
`configureQueryAnalysis` command:

- `queryAnalysisSamplerConfigurationRefreshSecs`
- `queryAnalysisWriterIntervalSecs`
- `queryAnalysisWriterMaxMemoryUsageBytes`
- `queryAnalysisWriterMaxBatchSize`
- `queryAnalysisSampleExpirationSecs`

### chars Length Limit for $trim, $ltrim, and $rtrim

Starting in MongoDB 7.0.33, the length of the string you provide to `chars` is 
limited to 4096 characters. For details, see $trim Limitations.


## Security

### Queryable Encryption General Availability

Starting in MongoDB 7.0, Queryable Encryption with equality
queries is generally available (GA). 
Improvements in the GA make it incompatible with the
{+qe+} Public Preview, which should not be used now that the feature is GA. 
For details, see 7.0-compatibility.

### KMIP 1.0 and 1.1 Support

MongoDB 7.0 (and 6.0.6) adds the `useLegacyProtocol` setting. This setting allows MongoDB
servers to connect to KMIP servers that use KMIP protocol version 1.0 or
1.1.

#### OpenSSL and FIPS Support

Starting in MongoDB 7.0 and 6.0.7, MongoDB supports OpenSSL 3.0 and the
OpenSSL FIPS provider with these operating systems:

- Red Hat Enterprise Linux 9
- Amazon Linux 2023
- Ubuntu Linux 22.04

For details, see transport-encryption.

#### OpenID Connect

Starting in 7.0, MongoDB Enterprise provides support for 
OpenID Connect authentication. OpenID Connect is an 
authentication layer built on top of OAuth2. You can use OpenID Connect to 
configure single sign-on between your MongoDB database and a third-party identity 
provider.


## Aggregation

New operators:

| Name | Description |
|---|---|
| `$median` | Returns an approximation of the median (50th percentile) value within each group. This operator can be used as an accumulator and as an aggregation expression. |
| `$percentile` | .. include:: /includes/aggregation/fact-return-percentile.rst This operator can be used as an accumulator and as an aggregation expression. |

### Month Name Specifier for $dateToString

MongoDB 7.0 adds the following format specifiers to use with the 
`$dateToString` operator: 

| Specifiers | Description | Possible Values |
|---|---|---|
| `%b` | Abbreviated month name (3 letters) | `jan`-`dec` |
| `%B` | Full month name | `january`-`december` |


## Time Series

MongoDB 7.0 removes most of the time series limitations from these operations 
that are based on the `delete` command:

- `delete`
- `deleteOne`
- `deleteMany`
- `Bulk.find.delete`
- `Bulk.find.deleteOne`


## Sharding

### Sharding Metadata Diagnostics

Starting in MongoDB 7.0, the `checkMetadataConsistency` command
is available to check sharding metadata at the cluster, database, and 
collection levels for inconsistencies.  These inconsistencies can originate
in cases such as:

- Upgrades in cases where the cluster encountered a bug while running previous
  releases of MongoDB
  
- Manual interventions that corrupt the cluster catalog

The following helper methods are now available through `mongosh`:

* `db.checkMetadataConsistency`
* `db.collection.checkMetadataConsistency`
* `sh.checkMetadataConsistency`

For more information on the inconsistencies the command checks for, see
inconsistency-types.

### mergeAllChunksOnShard Command

Starting in MongoDB 7.0, the `mergeAllChunksOnShard` command
finds and merges all mergeable chunks that a shard 
owns for a given collection.

### The AutoMerger

Starting in MongoDB 7.0, the AutoMerger can automatically merge chunks that meet the 
mergeability requirements. The 
AutoMerger is enabled by default. 

Starting in MongoDB 7.0, you can use the following methods to control
the AutoMerger behavior:

- `sh.startAutoMerger()`
- `sh.stopAutoMerger()`
- `sh.enableAutoMerger()`
- `sh.disableAutoMerger()`

### enableAutoMerger Parameter for configureCollectionBalancing

Starting in MongoDB 7.0, the `configureCollectionBalancing`
command accepts the `enableAutoMerger` parameter. Use 
`enableAutoMerger` to set whether the
AutoMerger takes this collection
into account.

### operationsBlockedByRefresh Metrics Removed

MongoDB 7.0 removes the `operationsBlockedByRefresh` document that
contains statistics about operations blocked by catalog cache refresh
activity because the `operationsBlockedByRefresh` counters increased
on `mongos` for every operation that used collection routing
information even if the operation wasn't blocked by a catalog refresh
activity. 

### analyzeShardKey Command and db.collection.analyzeShardKey() Method

MongoDB 7.0 adds the `analyzeShardKey` command and the 
`db.collection.analyzeShardKey()` method, which let you
calculate metrics for evaluating a shard key.

### configureQueryAnalyzer Command and db.collection.configureQueryAnalyzer() Method

MongoDB 7.0 adds the `configureQueryAnalyzer` command, which
allows you to configure query sampling for a collection. MongoDB 7.0
also adds the `db.collection.configureQueryAnalyzer()`, which
wraps the `configureQueryAnalyzer` command. Sampled queries provide 
information to `analyzeShardKey` to calculate metrics about read and 
write distribution of a shard key.


## Platform Support

### Removed Platforms

MongoDB 7.0 removes support for **RHEL 7 / CentOS 7 / Oracle 7** on the
PPC64LE and s390x architectures.
  


## Changes Introduced in MongoDB 6.3

### Aggregation

MongoDB 6.3 introduces the following aggregation operators: 

| Operator | Description |
|---|---|
| `$bitAnd` | Returns the result of a bitwise `and` operation on an array of `int` or `long` values. |
| `$bitNot` | Returns the result of a bitwise `not` operation on a single argument or an array that contains a single `int` or `long` value. |
| `$bitOr` | Returns the result of a bitwise `or` operation on an array of `int` or `long` values. |
| `$bitXor` | Returns the result of a bitwise `xor` (exclusive or) operation on an array of `int` and `long` values. |

### Connection Acquisition To Wire Log Message

Starting in MongoDB 6.3, a message is added to the log if the time that
an operation waited between acquisition of a server connection and
writing the bytes to send to the server over the network exceeds 1
millisecond. For details, see
log-messages-connection-acquisition-to-wire.

### `connPoolStats` Metrics

Starting in MongoDB 6.3, the `connPoolStats` command has
these output changes:

| Document | Field(s) |
|---|---|
| New `connPoolStats.acquisitionWaitTimes` document. | Time ranges with the number of connection requests in each range. Total number of connection requests for all time ranges. |

### `explain` Output Includes Fields for Spilled Data File Size

Starting in MongoDB 6.3, the `explain` output for the 
`$group` stage includes new metrics on spill data when using the 
classic execution engine:

- `spillFileSizeBytes`, the size of the spill file written to disk in the 
  `$group` stage
- `numBytesSpilledEstimate`, estimate of the number of bytes written to disk 
  in the `$group` stage before compression

For details, see sort-and-group-executionStats-and-above.

### `serverStatus` Metrics

Starting in MongoDB 6.3, the `serverStatus` command and the
`db.serverStatus()` method have these output changes:

| Document | Field(s) |
|---|---|
| New `network.listenerProcessingTime` document. | `network.listenerProcessingTime.durationMicros` |
| Addition to `connections` document. | `connections.rejected` |
| New `metrics.network` document. | `metrics.network.totalEgressConnectionEstablishmentTimeMillis` `metrics.network.totalIngressTLSConnections` `metrics.network.totalIngressTLSHandshakeTimeMillis` `metrics.network.totalTimeForEgressConnectionAcquiredToWireMicros` `metrics.network.totalTimeToFirstNonAuthCommandMillis` |
| Additions to `metrics.operation` document. | `metrics.operation.numConnectionNetworkTimeouts` `metrics.operation.totalTimeWaitingBeforeConnectionTimeoutMillis` |
| Addition to `shardingStatistics` document. | `shardingStatistics.chunkMigrationConcurrency` |
| Additions to `indexBulkBuilder` document. | `indexBulkBuilder.numSorted` `indexBulkBuilder.bytesSorted` `indexBulkBuilder.memUsage` |

### Session Workflow Log Message

Starting in MongoDB 6.3, a message is added to the log if the time to
send an operation response exceeds the slowms threshold option. For details, see
log-messages-session-workflow-example.

### Server Parameters

Starting in MongoDB 6.3, these server parameters were added:

- `slowConnectionThresholdMillis` sets the time limit to log
  the establishment of slow server connections. 
- `planCacheSize` sets the size of the plan cache for the slot-based query execution engine.

### Time Series Collection Custom Bucketing Parameters

MongoDB 6.3 adds the following time series parameters:

- `bucketMaxSpanSeconds` sets the maximum time span between measurements
  in a bucket.
- `bucketRoundingSeconds` sets the time interval that determines the 
  starting timestamp for a new bucket.

### `compact` Support for Time Series Collections

Starting in MongoDB 6.3, the `compact` command works with
time series collections.

### Time Series Indexing

Starting in MongoDB 6.3, MongoDB automatically generates a compound index on the `metaField` and `timeField` fields when 
creating a time series collection.


## Changes Introduced in MongoDB 6.2

### Collection Validation

Starting in MongoDB 6.2, the `validate` command and
`db.collection.validate()` method:

- Check collections to ensure the
  BSON documents conform to the BSON
  specifications.
- Check time series collections
  for internal data inconsistencies.
- Have a new option `checkBSONConformance` that enables comprehensive
  BSON checks.

### Deprecated Commands

Starting in MongoDB 6.2, the following database commands are deprecated:

- `collStats`
- `currentOp`

Use the `$collStats` and `$currentOp` aggregation 
stages instead.

### serverStatus Metrics

Starting in MongoDB 6.2, the `serverStatus` command output
includes these new fields:

- `metrics.query.sort`
- `metrics.query.sort.spillToDisk`
- `metrics.query.sort.totalBytesSorted`
- `metrics.query.sort.totalKeysSorted`

Starting in MongoDB 6.2, the `serverStatus` command and 
the `db.serverStatus()` method report the 
`opLatencies` metric for `mongos` 
instances. Latencies reported by `mongos` include operation latency 
time and communication time between the `mongod` and `mongos` 
instances.

### Server Parameters

Starting in MongoDB 6.2, `mongod` adds these parameters:

- `transactionTooLargeForCacheThreshold`

### Sharding

Starting in version 6.2, MongoDB removes the `maxSize` field 
from the `addShard` command. As a result:

- Running `addShard` with the `maxSize` field returns 
  an `InvalidOptions` error.

- New documents in the `shards` collection no longer 
  include the `maxSize` field.

- Any pre-existing `maxSize` field entries are ignored.
