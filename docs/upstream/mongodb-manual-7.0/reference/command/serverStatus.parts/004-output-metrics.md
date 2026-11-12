<!-- Part 4 of 11 of reference/command/serverStatus.md (split because the page is big). -->

### metrics

```javascript
metrics : {
   abortExpiredTransactions: {
      passes: <integer>,
      successfulKills: <integer>,
      timedOutKills: <integer>
   },
   apiVersions: {
      <appName1>: <string>, 
      <appName2>: <string>, 
      <appName3>: <string>
   },
   aggStageCounters : {
      <aggregation stage> : Long("<num>")
   },
   changeStreams: {
      largeEventsFailed: Long("<num>"),
      largeEventsSplit: Long("<num>")
   },
   commands: {
      <command>: {
         failed: Long("<num>"),
         validator: { 
           total: Long("<num>"), 
           failed: Long("<num>"), 
           jsonSchema: Long("<num>")
         }, 
         total: Long("<num>")
      }
   },
   cursor : {
      moreThanOneBatch : Long("<num>"),
      timedOut : Long("<num>"),
      totalOpened : Long("<num>"),
      lifespan : {
         greaterThanOrEqual10Minutes : Long("<num>"),
         lessThan10Minutes : Long("<num>"),
         lessThan15Seconds : Long("<num>"),
         lessThan1Minute : Long("<num>"),
         lessThan1Second : Long("<num>"),
         lessThan30Seconds : Long("<num>"),
         lessThan5Seconds : Long("<num>")
      },
      open : {
         noTimeout : Long("<num>"),
         pinned : Long("<num>"),
         multiTarget : Long("<num>"),
         singleTarget : Long("<num>"),
         total : Long("<num>")
      }
   },
   document : {
      deleted : Long("<num>"),
      inserted : Long("<num>"),
      returned : Long("<num>"),
      updated : Long("<num>")
   },
   dotsAndDollarsFields : {
         inserts : Long("<num>"),
         updates : Long("<num>")
   },
   getLastError : {
      wtime : {
         num : <num>,
         totalMillis : <num>
      },
      wtimeouts : Long("<num>"),
      default : {
         unsatisfiable : Long("<num>"),
         wtimeouts : Long("<num>")
      }
   },
   mongos : {
      cursor : {
         moreThanOneBatch : Long("<num>"),
         totalOpened : Long("<num>")
      }
   },
   network : {  // Added in MongoDB 6.3
      totalEgressConnectionEstablishmentTimeMillis : Long("<num>"),
      totalIngressTLSConnections : Long("<num>"),
      totalIngressTLSHandshakeTimeMillis : Long("<num>"),
      totalTimeForEgressConnectionAcquiredToWireMicros : Long("<num>"),
      totalTimeToFirstNonAuthCommandMillis : Long("<num>")
   },
   operation : {
      killedDueToClientDisconnect : Long("<num>"),  // Added in MongoDB 7.1 (*Also available in 7.0.5*)
      killedDueToMaxTimeMSExpired : Long("<num>"),  // Added in MongoDB 7.2 (*Also available in 7.0.5*)
      numConnectionNetworkTimeouts : Long("<num>"),  // Added in MongoDB 6.3
      totalTimeWaitingBeforeConnectionTimeoutMillis : Long("<num>"),  // Added in MongoDB 6.3
      scanAndOrder : Long("<num>"),
      writeConflicts : Long("<num>")
   },
   operatorCounters : {
      expressions : {
         <command> : Long("<num>")
      },
      match : {
         <command> : Long("<num>")
      }
   },
   query: {
      allowDiskUseFalse: Long("<num>"),
      updateOneOpStyleBroadcastWithExactIDCount: Long("<num>"),
      lookup: {
         hashLookup: Long("<num>"),
         hashLookupSpillToDisk: Long("<num>"),
         indexedLoopJoin: Long("<num>"),
         nestedLoopJoin: Long("<num>")
      },
      multiPlanner: {
         classicCount: Long("<num>"),
         classicMicros: Long("<num>"),
         classicWorks: Long("<num>"),
         sbeCount: Long("<num>"),
         sbeMicros: Long("<num>"),
         sbeNumReads: Long("<num>"),
         histograms: {
            classicMicros: [
               { lowerBound: Long("0"), count: Long("<num>") },
               { < Additional histogram groups not shown. > },
               { lowerBound: Long("1073741824"), count: Long("<num>")> }>
            ],
            classicNumPlans: [
               { lowerBound: Long("0"), count: Long("<num>") },
               { < Additional histogram groups not shown. > },
               { lowerBound: Long("32"), count: Long("<num>") }
            ],
            classicWorks: [
               { lowerBound: Long("0"), count: Long("<num>") },
               { < Additional histogram groups not shown. > },
               { lowerBound: Long("32768"), count: Long("<num>") }
            ],
            sbeMicros: [
               { lowerBound: Long("0"), count: Long("<num>") },
               { < Additional histogram groups not shown. > },
               { lowerBound: Long("1073741824"), count: Long("<num>") }
            ],
            sbeNumPlans: [
               { lowerBound: Long("0"), count: Long("<num>") },
               { < Additional histogram groups not shown. > },
               { lowerBound: Long("32"), count: Long("<num>") }
            ],
            sbeNumReads: [
               { lowerBound: Long("0"), count: Long("<num>") },
               { < Additional histogram groups not shown. > },
               { lowerBound: Long("32768"), count: Long("<num>") }
            ]
         }
      },
      planCache: {
         classic: { hits: Long("<num>"), misses: Long("<num>") },
         sbe: { hits: Long("<num>"), misses: Long("<num>") },
         classic: { hits: Long("<num>"), misses: Long("<num>"), replanned: Long("<num>") },
         sbe: { hits: Long("<num>"), misses: Long("<num>"), replanned: Long("<num>") }            
      },
      queryFramework: {
         aggregate: {
            classicHybrid: Long("<num>"),
            classicOnly: Long("<num>"),
            cqf: Long("<num>"),
            sbeHybrid: Long("<num>"),
            sbeOnly: Long("<num>")
         },
         find: { classic: Long("<num>"), cqf: Long("<num>"), sbe: Long("<num>") }
      }
   },
   queryExecutor: {
      scanned : Long("<num>"),
      scannedObjects : Long("<num>"),
      collectionScans : {
         nonTailable : Long("<num>"),
         total : Long("<num>")
      },
      profiler : {
         collectionScans : {
            nonTailable : Long("<num>"),
            tailable : Long("<num>"),
            total : Long("<num>")
         }
      }
   },
   record : {
      moves : Long("<num>")
   },
   repl : {
      executor : {
         pool : {
            inProgressCount : <num>
         },
         queues : {
            networkInProgress : <num>,
            sleepers : <num>
         },
         unsignaledEvents : <num>,
         shuttingDown : <boolean>,
         networkInterface : <string>
      },
      apply : {
         attemptsToBecomeSecondary : Long("<num>"),
         batches : {
            num : <num>,
            totalMillis : <num>
         },
         ops : Long("<num>")
      },
      buffer : {
         count : Long("<num>"),
         maxSizeBytes : Long("<num>"),
         sizeBytes : Long("<num>")
      },
      initialSync : {
         completed : Long("<num>"),
         failedAttempts : Long("<num>"),
         failures : Long("<num>")
      },
      network : {
         bytes : Long("<num>"),
         getmores : {
            num : <num>,
            totalMillis : <num>
         },
         notPrimaryLegacyUnacknowledgedWrites : Long("<num>"),
         notPrimaryUnacknowledgedWrites : Long("<num>"),
         oplogGetMoresProcessed : {
            num : <num>,
            totalMillis : <num>
         },
         ops : Long("<num>"),
         readersCreated : Long("<num>"),
         replSetUpdatePosition : {
            num : Long("<num>")
         }
      },
      reconfig : {
         numAutoReconfigsForRemovalOfNewlyAddedFields : Long("<num>")
      },
      stateTransition : {
         lastStateTransition : <string>,
         userOperationsKilled : Long("<num>"),
         userOperationsRunning : Long("<num>")
      },
      syncSource : {
         numSelections : Long("<num>"),
         numTimesChoseSame : Long("<num>"),
         numTimesChoseDifferent : Long("<num>"),
         numTimesCouldNotFind : Long("<num>")
      },
      waiters : {
         opTime : Long("<num>"),
         replication : Long("<num>")
      }
   },
   storage : {
      freelist : {
         search : {
            bucketExhausted : <num>,
            requests : <num>,
            scanned : <num>
         }
      }
   },
   ttl : {
      deletedDocuments : Long("<num>"),
      passes : Long("<num>"),
      subPasses : Long("<num>")
   }
}
```

**`metrics`**

A document that returns various statistics that reflect the current
use and state of a running `mongod` instance.

**`metrics.abortExpiredTransactions`**

Document that returns statistics on the current state of the
`abortExpiredTransactions` thread.

**`metrics.abortExpiredTransactions.passes`**

Indicates the number of successful passes aborting transactions
older than the `transactionLifetimeLimitSeconds` parameter.

If the `passes` value stops incrementing, it indicates that the
`abortExpiredTransactions` thread may be stuck.

**`metrics.abortExpiredTransactions.successfulKills`**

Number of expired transactions successfully ended by MongoDB.

A session is checked out from a session pool to run database operations.

`AbortExpiredTransactionsSessionCheckoutTimeout` sets the
maximum number of milliseconds for a session to be checked out when
attempting to end an expired transaction.

If the expired transaction is successfully ended, MongoDB increments
`metrics.abortExpiredTransactions.successfulKills`. If the
transaction isn't successfully ended because it timed out when
attempting to check out a session, MongoDB increments
`metrics.abortExpiredTransactions.timedOutKills`.

**New in version:** 7.0.26

**`metrics.abortExpiredTransactions.timedOutKills`**

Number of expired transactions unsuccessfully ended by MongoDB
because it timed out when attempting to check out a session.

A session is checked out from a session pool to run database operations.

`AbortExpiredTransactionsSessionCheckoutTimeout` sets the
maximum number of milliseconds for a session to be checked out when
attempting to end an expired transaction.

If the expired transaction is successfully ended, MongoDB increments
`metrics.abortExpiredTransactions.successfulKills`. If the
transaction isn't successfully ended because it timed out when
attempting to check out a session, MongoDB increments
`metrics.abortExpiredTransactions.timedOutKills`.

**New in version:** 7.0.26

**`metrics.aggStageCounters`**

A document that reports on the use of
aggregation pipeline stages. The fields in 
`metrics.aggStageCounters` are the names of 
aggregation pipeline stages. For each pipeline stage,
`serverStatus` reports the number of times that stage
has been executed.

*Updated in version 5.2 (and 5.0.6).*

**`metrics.apiVersions`**

A document that contains:

- The name of each client application
- The Stable API version that each application was configured with within
  the last 24-hour period

Consider the following when viewing `metrics.apiVersions`:

- The possible returned values for each `appname` are:

  - `default`: The command was issued without a Stable API version specified.
  - `1`: The command was issued with Stable API version 1.

  **Note:**

  You may see both return values for an `appname` because you can
  specify a Stable API version at the command level. Some of your
  commands may have been issued with no Stable API version, while
  others were issued with version 1.

- API version metrics are retained for 24 hours. If
  no commands are issued with a specific API version from an 
  application in the past 24 hours, that `appname` and API version 
  are removed from the metrics. This also applies to the
  `default` API version metric.

- Set the `appname` when connecting to a MongoDB instance by 
  specifying the `appname` in the connection URI. `?appName=ZZZ` 
  sets the `appname` to `ZZZZ`.

- Drivers accessing the Stable API can set a default `appname`.

- If no `appname` is configured, a default value is
  automatically populated based on the product. For example, for a 
  `MongoDB Compass` connection with no `appname` in 
  the URI, the metric returns: `'MongoDB Compass': [ 'default' ]`.

*New in version 5.0.* 

**`metrics.operatorCounters`**

A document that reports on the use of aggregation pipeline operators and expressions.

**`metrics.operatorCounters.expressions`**

A document with a number that indicates how often
aggregation-expression-operators ran.

To get metrics for a specific operator, such as the greater-than
operator (`$gt`), append the operator to the command:

```javascript
db.runCommand( { serverStatus: 1 } ).metrics.operatorCounters.expressions.$gt
```

**New in version:** 5.0

**`metrics.operatorCounters.match`**

A document with a number that indicates how often
match expressions ran.

Match expression operators
also increment as part of an aggregation pipeline `$match`
stage. If the `$match` stage uses the `$expr` operator, the
counter for `$expr` increments, but the component counters do not
increment. 

Consider the following query: 

```javascript
db.matchCount.aggregate(
   [
      { $match:
         {  $expr: { $gt: [ "$_id", 0 ] } }
      }
   ]
)
```

The counter for `$expr` increments when the query runs. The
counter for `$gt` does not. 

**`metrics.changeStreams`**

A document that reports information about change stream events larger than 16 MB.

**New in version:** 7.0

**`metrics.changeStreams.largeEventsFailed`**

The number of change stream events that caused a
`BSONObjectTooLarge` exception because the event was larger than 16
MB. To prevent the exception, see
`$changeStreamSplitLargeEvent`.

**New in version:** 7.0 (*Also available in 6.0.9 and 5.0.19*)

**`metrics.changeStreams.largeEventsSplit`**

The number of change stream events larger than 16 MB that were split
into smaller fragments. Events are only split if you use the
`$changeStreamSplitLargeEvent` pipeline stage.

**New in version:** 7.0 (*Also available in 6.0.9*)

**`metrics.commands`**

A document that reports on the use of database commands. The fields
in `metrics.commands` are the names of
database commands. For each command, the
`serverStatus` reports the total number of executions and
the number of failed executions.

`metrics.commands` includes
`replSetStepDownWithForce` (that is, the `replSetStepDown`
command with `force: true`) as well as the overall
`replSetStepDown`. In earlier versions, the command
reported only overall `replSetStepDown` metrics.

**`metrics.commands.<command>.failed`**

The number of times `<command>` failed on this
`mongod`.

**`metrics.commands.<create or collMod>.validator`**

For the `create` and `collMod` commands, a document
that reports on non-empty `validator` objects passed to the command to
specify validation rules or expressions
for the collection.

**`metrics.commands.<create or collMod>.validator.total`**

The number of times a non-empty `validator` object was passed as an option
to the command on this `mongod`.

**`metrics.commands.<create or collMod>.validator.failed`**

The number of times a call to the command on this `mongod`
failed with a non-empty `validator` object due to a schema validation
error.

**`metrics.commands.<create or collMod>.validator.jsonSchema`**

The number of times a `validator` object with a `$jsonSchema` was passed
as an option to the command on this `mongod`.

**`metrics.commands.<command>.total`**

The number of times `<command>` executed on this
`mongod`.

**`metrics.commands.update.pipeline`**

The number of times an
aggregation pipeline
was used to update documents on this `mongod`. Subtract
this value from the total number of updates to get the number of
updates made with document
syntax.

The `pipeline` counter is only available for `update` and
`findAndModify` operations.

**`metrics.commands.findAndModify.pipeline`**

The number of times `findAndModify()` was
used in an
aggregation pipeline
to update documents on this `mongod`.

The `pipeline` counter is only available for `update` and
`findAndModify` operations.

**`metrics.commands.update.arrayFilters`**

The number of times an arrayFilter
was used to update documents on this `mongod`.

The `arrayFilters` counter is only available for `update` and
`findAndModify` operations.

**`metrics.commands.findAndModify.arrayFilters`**

The number of times an arrayFilter
was used with `findAndModify()` to update
documents on this `mongod`.

The `arrayFilters` counter is only available for `update` and
`findAndModify` operations.

**`metrics.document`**

A document that reflects document access and modification patterns.
Compare these values to the data in the `opcounters`
document, which track total number of operations.

**`metrics.document.deleted`**

The total number of documents deleted.

**`metrics.document.inserted`**

The total number of documents inserted.

**`metrics.document.returned`**

The total number of documents returned by queries.

**`metrics.document.updated`**

The total number of documents matched for update operations. This value is not 
necessarily the same as the number of documents modified by updates.

**`metrics.dotsAndDollarsFields`**

A document with a number that indicates how often
insert or update
operations ran using a dollar (`$`) prefixed name. The value does
not report the exact number of operations.  

When an upsert operation creates a new document, it is
considered to be an `insert` rather than an `update`.

**New in version:** 5.0

**`metrics.executor`**

A document that reports on various statistics for the replication
executor.

**`metrics.getLastError`**

A document that reports on write concern use.

**`metrics.getLastError.wtime`**

A document that reports write concern
operation counts with a `w` argument greater than `1`.

**`metrics.getLastError.wtime.num`**

The total number of operations with a specified write concern
(that is, `w`) that wait for one or more members of a replica set
to acknowledge the write operation (that is, a `w` value greater
than `1`.)

**`metrics.getLastError.wtime.totalMillis`**

The total amount of time in milliseconds that the
`mongod` has spent performing write concern operations with a write concern (that is, `w`)
that waits for one or more members of a replica set to acknowledge
the write operation (that is, a `w` value greater than `1`.)

**`metrics.getLastError.wtimeouts`**

The number of times that write concern operations have timed
out as a result of the `wtimeout` threshold. This number
increments for both default and non-default write concern
specifications.

**`metrics.getLastError.default`**

A document that reports on when a default write concern was used (meaning, a non-`clientSupplied` write
concern). The possible origins of a default write concern are:

- `implicitDefault`
- `customDefault`
- `getLastErrorDefaults`

Refer to the following table for information on
each possible write concern origin, or `provenance`:

| Provenance | Description |
|---|---|
| `clientSupplied` | The write concern was specified in the application. |
| `customDefault` | The write concern originated from a custom defined default value. See `setDefaultRWConcern`. |
| `getLastErrorDefaults` | The write concern originated from the replica set's `settings.getLastErrorDefaults` field. |
| `implicitDefault` | The write concern originated from the server in absence of all other write concern specifications. |

**`metrics.getLastError.default.unsatisfiable`**

Number of times that a non-`clientSupplied` write concern
returned the `UnsatisfiableWriteConcern` error code.

**`metrics.getLastError.default.wtimeouts`**

Number of times a non-`clientSupplied` write concern timed out.

**`metrics.mongos`**

A document that contains metrics about `mongos`.

**`metrics.mongos.cursor`**

A document that contains metrics for cursors used by
`mongos`.

**`metrics.mongos.cursor.moreThanOneBatch`**

The total number of cursors that have returned more than one batch
since `mongos` started. Additional batches are retrieved
using the `getMore` command.

**New in version:** 5.0

**`metrics.mongos.cursor.totalOpened`**

The total number of cursors that have been opened since
`mongos` started, including cursors currently open.
Differs from `metrics.cursor.open.total`, which is the
number of currently open cursors only.

**New in version:** 5.0

**`metrics.network`**

**New in version:** 6.3

A document that reports server network metrics.

**`metrics.network.totalEgressConnectionEstablishmentTimeMillis`**

**New in version:** 6.3

The total time in milliseconds to establish server connections.

**`metrics.network.totalIngressTLSConnections`**

**New in version:** 6.3

The total number of incoming connections to the server that use TLS.
The number is cumulative and is the total after the server was
started.

**`metrics.network.totalIngressTLSHandshakeTimeMillis`**

**New in version:** 6.3

The total time in milliseconds that incoming connections to the
server have to wait for the TLS network handshake to complete. The
number is cumulative and is the total after the server was started.

**`metrics.network.totalTimeForEgressConnectionAcquiredToWireMicros`**

**New in version:** 6.3

The total time in microseconds that operations wait between
acquisition of a server connection and writing the bytes to send to
the server over the network. The number is cumulative and is the
total after the server was started.

**`metrics.network.totalTimeToFirstNonAuthCommandMillis`**

**New in version:** 6.3

The total time in milliseconds from accepting incoming connections to
the server and receiving the first operation that isn't part of the
connection authentication handshake. The number is cumulative and is
the total after the server was started.

**`metrics.operation`**

A document that holds counters for several types of update and query
operations that MongoDB handles using special operation types.

**`metrics.operation.killedDueToClientDisconnect`**

**New in version:** 7.1 (*Also available in 7.0.5*)

Total number of operations cancelled before completion 
because the client disconnected.

**`metrics.operation.killedDueToMaxTimeMSExpired`**

**New in version:** 7.2 (*Also available in 7.0.5*)

Total number of operations that timed out before completion.

**`metrics.operation.numConnectionNetworkTimeouts`**

**New in version:** 6.3

Total number of operations that failed because of server connection
acquisition time out errors.

**`metrics.operation.totalTimeWaitingBeforeConnectionTimeoutMillis`**

**New in version:** 6.3

Total time in milliseconds that operations waited before failing
because of server connection acquisition time out errors.

**`metrics.operation.scanAndOrder`**

The total number of queries that return sorted numbers that cannot
perform the sort operation using an index.

**`metrics.operation.writeConflicts`**

The total number of queries that encountered write conflicts.

**`metrics.query.lookup`**

A document that provides detailed data on the use of the  `$lookup` 
stage with the slot-based query execution engine. To learn more, see agg-lookup-optimization-sbe.

These metrics are primarily intended for internal use by MongoDB.

*New in version 6.1* 

**`metrics.query.multiPlanner`**

Provides detailed query planning data for the slot-based query execution engine and the classic
query engine. For more information on the slot-based query execution engine see:
sbe-pipeline-optimizations.

These metrics are primarily intended for internal use by MongoDB.

*New in version 6.0.0 and 5.0.9* 

**`metrics.query.sort`**

A document that holds counters related to sort stages.

**New in version:** 6.2

**`metrics.query.sort.spillToDisk`**

The total number of writes to disk caused by sort stages.

**New in version:** 6.2

**`metrics.query.sort.totalBytesSorted`**

The total amount of sorted data in bytes. 

**New in version:** 6.2

**`metrics.query.sort.totalKeysSorted`**

The total number of keys used in sorts.

**New in version:** 6.2

**`query.multiPlanner.classicMicros`**

Aggregates the total number of microseconds spent in the classic
multiplanner.

**`query.multiPlanner.classicWorks`**

Aggregates the total number of "works" performed in the classic
multiplanner.

**`query.multiPlanner.classicCount`**

Aggregates the total number of invocations of the classic
multiplanner.

**`query.multiPlanner.sbeMicros`**

Aggregates the total number of microseconds spent in the slot-based execution engine
multiplanner.

**`query.multiPlanner.sbeNumReads`**

Aggregates the total number of reads done in the slot-based execution engine
multiplanner.

**`query.multiPlanner.sbeCount`**

Aggregates the total number of invocations of the slot-based execution engine
multiplanner.

**`query.multiPlanner.histograms.classicMicros`**

A histogram measuring the number of microseconds spent in an
invocation of the classic multiplanner.

**`query.multiPlanner.histograms.classicWorks`**

A histogram measuring the number of "works" performed during an
invocation of the classic multiplanner.

**`query.multiPlanner.histograms.classicNumPlans`**

A histogram measuring the number of plans in the candidate set during
an invocation of the classic multiplanner.

**`query.multiPlanner.histograms.sbeMicros`**

A histogram measuring the number of microseconds spent in an
invocation of the slot-based execution engine multiplanner.

**`query.multiPlanner.histograms.sbeNumReads`**

A histogram measuring the number of reads during an invocation of the
slot-based execution engine multiplanner.

**`query.multiPlanner.histograms.sbeNumPlans`**

A histogram measuring the number of plans in the candidate set during
an invocation of the slot-based execution engine multiplanner.

**`query.queryFramework.aggregate`**

A document that reports on the number of aggregation operations run on each 
query framework. The subfields in `query.queryFramework.aggregate`
indicate the number of times each framework was used to perform an 
aggregation operation.

**`query.queryFramework.find`**

A document that reports on the number of find operations run on each 
query framework. The subfields in `query.queryFramework.find` 
indicate the number of times each framework was used to perform a find 
operation.

**`metrics.queryExecutor`**

A document that reports data from the query execution system.

**`metrics.queryExecutor.scanned`**

The total number of index items scanned during queries and
query-plan evaluation. This counter is the same as
`totalKeysExamined` in the output of
`explain()`.

**`metrics.queryExecutor.scannedObjects`**

The total number of documents scanned during queries and query-plan
evaluation. This counter is the same as
`totalDocsExamined` in the output of
`explain()`.

**`metrics.queryExecutor.collectionScans`**

A document that reports on the number of queries that performed a
collection scan.

**`metrics.queryExecutor.collectionScans.nonTailable`**

The number of queries that performed a collection scan that did not
use a tailable cursor.

**`metrics.queryExecutor.collectionScans.total`**

The total number queries that performed a collection scan. The total
consists of queries that did and did not use a
tailable cursor.

**`metrics.queryExecutor.profiler.collectionScans.nonTailable`**

The number of queries that performed a collection scan on a
`profile` collection that did not use a
tailable cursor.

**`metrics.queryExecutor.profiler.collectionScans.tailable`**

The number of queries that performed a collection scan on a
`profile` collection that used a
tailable cursor.

**`metrics.queryExecutor.profiler.collectionScans.total`**

The total number of queries that performed a collection scan on a 
`profile` collection. This includes queries that
used both tailable and non-tailable cursors.

**`metrics.record`**

A document that reports on data related to record allocation in the
on-disk memory files.

**`metrics.repl`**

A document that reports metrics related to the replication process.
`metrics.repl` document appears on all
`mongod` instances, even those that aren't members of
replica sets.

**`metrics.repl.apply`**

A document that reports on the application of operations from the
replication oplog.

**`metrics.repl.apply.batchSize`**

The total number of oplog entries applied. The
`metrics.repl.apply.batchSize` is incremented with the
number of oplog entries in a batch at the batch boundaries instead of
being incremented by one after each entry.

For finer granularity, see `metrics.repl.apply.ops`.

**`metrics.repl.apply.batches`**

`metrics.repl.apply.batches` reports on the
oplog application process on secondaries
members of replica sets. See
replica-set-internals-multi-threaded-replication for more
information on the oplog application processes.

**`metrics.repl.apply.batches.num`**

The total number of batches applied across all databases.

**`metrics.repl.apply.batches.totalMillis`**

The total amount of time in milliseconds the `mongod` has
spent applying operations from the oplog.

**`metrics.repl.apply.ops`**

The total number of operations applied during the replication process.
`metrics.repl.apply.ops` is incremented after each
operation, including operations that derive from oplog entries during
application, such as updates to internal metadata collections like 
`config.transactions`.

**See also:**

`metrics.repl.apply.batchSize`

**`metrics.repl.buffer`**

MongoDB buffers oplog operations from the replication sync source
buffer before applying oplog entries in a
batch. `metrics.repl.buffer` provides a way to
track the oplog buffer. See
replica-set-internals-multi-threaded-replication for more
information on the oplog application process.

**`metrics.repl.buffer.count`**

The current number of operations in the oplog buffer.

**`metrics.repl.buffer.maxSizeBytes`**

The maximum size of the buffer. This value is a constant setting in
the `mongod`, and is not configurable.

**`metrics.repl.buffer.sizeBytes`**

The current size of the contents of the oplog buffer.

**`metrics.repl.network`**

`metrics.repl.network` reports network use by
the replication process.

**`metrics.repl.network.bytes`**

`metrics.repl.network.bytes` reports the total
amount of data read from the replication sync source.

**`metrics.repl.network.getmores`**

`metrics.repl.network.getmores` reports on the
`getmore` operations, which are requests for additional results
from the oplog cursor as part of the oplog replication
process.

**`metrics.repl.network.getmores.num`**

`metrics.repl.network.getmores.num` reports the
total number of `getmore` operations, which are operations that
request an additional set of operations from the replication sync
source.

**`metrics.repl.network.getmores.totalMillis`**

`metrics.repl.network.getmores.totalMillis`
reports the total amount of time required to collect data from
`getmore` operations.

**Note:**

This number can be quite large, as MongoDB will wait for more
data even if the `getmore` operation does not initial return
data.

**`metrics.repl.network.getmores.numEmptyBatches`**

The number of empty `oplog` batches a secondary receives from its
sync source. A secondary receives an empty batch if it is fully
synced with its source and either:

- The `getmore` times out waiting for more data, or

- The sync source's majority commit point has advanced since the
  last batch sent to this secondary.

For a primary, if the instance was previously a secondary, the
number reports on the empty batches received when it was a
secondary. Otherwise, for a primary, this number is `0`.

**`metrics.repl.network.notPrimaryLegacyUnacknowledgedWrites`**

The number of unacknowledged (`w: 0`) legacy write operations (see
wp-request-opcodes) that failed because the current
`mongod` is not in `PRIMARY` state.

**`metrics.repl.network.notPrimaryUnacknowledgedWrites`**

The number of unacknowledged (`w: 0`) write operations that failed
because the current `mongod` is not in
`PRIMARY` state.

**`metrics.repl.network.oplogFetcherHighestFetchedOptime`**

The highest optime that the oplog fetcher has fetched from its sync source in
the most recent batch.

**`metrics.repl.network.oplogFetcherLagSeconds`**

The replication fetch lag, in seconds, between the sync source’s last applied
optime and the oplog fetcher’s highest fetched optime on this node.

**`metrics.repl.network.oplogGetMoresProcessed`**

A document that reports the number of `getMore`
commands to fetch the oplog that a node processed as a sync
source.

**`metrics.repl.network.oplogGetMoresProcessed.num`**

The number of `getMore` commands to fetch the
oplog that a node processed as a sync source.

**`metrics.repl.network.oplogGetMoresProcessed.totalMillis`**

The time, in milliseconds, that a node spent processing the
`getMore` commands counted in
`metrics.repl.network.oplogGetMoresProcessed.num`. 

**`metrics.repl.network.ops`**

The total
number of operations read from the replication source.

**`metrics.repl.network.readersCreated`**

The total number of oplog query processes created. MongoDB
creates a new oplog query any time an error occurs in the
connection, including a timeout, or a network operation. This
value also increments every time MongoDB selects a new source
for replication.

**`metrics.repl.network.replSetUpdatePosition`**

A document that reports the number of `replSetUpdatePosition`
commands a node sent to its sync source.

**`metrics.repl.network.replSetUpdatePosition.num`**

The number of `replSetUpdatePosition` commands a node sent
to its sync source. `replSetUpdatePosition` commands are internal
replication commands that communicate replication progress from
nodes to their sync sources.

**Note:**

Replica set members in the `STARTUP2` state do not send
the `replSetUpdatePosition` command to their sync source.

**`metrics.repl.reconfig`**

A document containing the number of times that member `newlyAdded`
fields were automatically removed by the primary. When a member is
first added to the replica set, the member's `newlyAdded` field is
set to `true`.

**New in version:** 5.0

**`metrics.repl.reconfig.numAutoReconfigsForRemovalOfNewlyAddedFields`**

The number of times that `newlyAdded` member fields were
automatically removed by the primary. When a member is first added to
the replica set, the member's `newlyAdded` field is set to
`true`. After the primary receives the member's heartbeat response
indicating the member state is `SECONDARY`,
`RECOVERING`, or `ROLLBACK`, the primary
automatically removes the member's `newlyAdded` field. The
`newlyAdded` fields are stored in the `local.system.replset`
collection.

**New in version:** 5.0

**`metrics.repl.stateTransition`**

Information on user operations when the member undergoes one of the
following transitions that can stop user operations:

- The member steps up to become a primary.

- The member steps down to become a secondary.

- The member is actively performing a rollback.

**`metrics.repl.stateTransition.lastStateTransition`**

The transition being reported:

| State Change | Description |
|---|---|
| `"stepUp"` | The member steps up to become a primary. |
| `"stepDown"` | The member steps down to become a secondary. |
| `"rollback"` | The member is actively performing a rollback. |
| `""` | The member has not undergone any state changes. |

**`metrics.repl.stateTransition.userOperationsKilled`**

The number of operations stopped during the
`mongod` instance's state change.

**Note:**

This metric reflects the total number of operations
killed, regardless of whether the operation was 
initiated by the user or the server.

**`metrics.repl.stateTransition.userOperationsRunning`**

The number of operations that remained running during the
`mongod` instance's state change.

**Note:**

This metric reflects the total number of operations
running, regardless of whether the operation was initiated
by the user or the server.

**`metrics.repl.syncSource`**

Information on a replica set node's
sync source selection process.

**`metrics.repl.syncSource.numSelections`**

Number of times a node attempted to choose a node to sync from among
the available sync source options. A node attempts to choose a node
to sync from if, for example, the sync source is re-evaluated or the
node receives an error from its current sync source.

**`metrics.repl.syncSource.numTimesChoseSame`**

Number of times a node kept its original sync source after
re-evaluating if its current sync source was optimal.

**`metrics.repl.syncSource.numTimesChoseDifferent`**

Number of times a node chose a new sync source after re-evaluating if
its current sync source was optimal.

**`metrics.repl.syncSource.numTimesCouldNotFind`**

Number of times a node could not find an available sync source when
attempting to choose a node to sync from.

**`metrics.repl.waiters.replication`**

The number of threads waiting for replicated or journaled write concern
acknowledgements.

**New in version:** 7.0.10 (Also available in 6.0.16 and 5.0.27)

**`metrics.repl.waiters.opTime`**

The number of threads queued for local replication optime assignments.

**New in version:** 7.0.10 (Also available in 6.0.16 and 5.0.27)

**`metrics.storage.freelist.search.bucketExhausted`**

The number of times that `mongod` has examined the free
list without finding a large record allocation.

**`metrics.storage.freelist.search.requests`**

The number of times `mongod` has searched for available
record allocations.

**`metrics.storage.freelist.search.scanned`**

The number of available record allocations `mongod` has
searched.

**`metrics.ttl`**

A document that reports on the operation of the resource use of the
ttl index process.

**`metrics.ttl.deletedDocuments`**

The total number of documents deleted from collections with a
ttl index.

**`metrics.ttl.passes`**

Number of passes performed by the TTL background process to check for
expired documents. A pass is complete when the TTL monitor has
deleted as many candidate documents as it can find from all TTL
indexes. For more information on the TTL index deletion process, see
ttl-monitor-deletion-process.

**`metrics.ttl.subPasses`**

Number of sub-passes performed by the TTL background process to check
for expired documents. For more information on the TTL index deletion
process, see ttl-monitor-deletion-process.

**`metrics.cursor`**

A document that contains data regarding cursor state and use.

**`metrics.cursor.moreThanOneBatch`**

The total number of cursors that have returned more than one batch
since the server process started. Additional batches are retrieved
using the `getMore` command.

**New in version:** 5.0

**`metrics.cursor.timedOut`**

The total number of cursors that have timed out since the server
process started. If this number is large or growing at a regular
rate, this may indicate an application error.

**`metrics.cursor.totalOpened`**

The total number of cursors that have been opened since the server
process started, including cursors currently open. Differs from
`metrics.cursor.open.total`, which is the number of
currently open cursors only.

**New in version:** 5.0

**`metrics.cursor.lifespan`**

A document that reports the number of cursors that have lifespans
within specified time periods. The cursor lifespan is the time period
from when the cursor is created to when the cursor is killed using
the `killCursors` command or the cursor has no remaining
objects in the batch.

The lifespan time periods are:

- < 1 second

- >= 1 second to < 5 seconds

- >= 5 seconds to < 15 seconds

- >= 15 seconds to < 30 seconds

- >= 30 seconds to < 1 minute

- >= 1 minute to < 10 minutes

- >= 10 minutes

**New in version:** 5.0

**`metrics.cursor.lifespan.greaterThanOrEqual10Minutes`**

The number of cursors with a lifespan >= 10 minutes.

**New in version:** 5.0

**`metrics.cursor.lifespan.lessThan10Minutes`**

The number of cursors with a lifespan >= 1 minute to < 10 minutes.

**New in version:** 5.0

**`metrics.cursor.lifespan.lessThan15Seconds`**

The number of cursors with a lifespan >= 5 seconds to < 15 seconds.

**New in version:** 5.0

**`metrics.cursor.lifespan.lessThan1Minute`**

The number of cursors with a lifespan >= 30 seconds to < 1 minute.

**New in version:** 5.0

**`metrics.cursor.lifespan.lessThan1Second`**

The number of cursors with a lifespan < 1 second.

**New in version:** 5.0

**`metrics.cursor.lifespan.lessThan30Seconds`**

The number of cursors with a lifespan >= 15 seconds to < 30 seconds.

**New in version:** 5.0

**`metrics.cursor.lifespan.lessThan5Seconds`**

The number of cursors with a lifespan >= 1 second to < 5 seconds.

**New in version:** 5.0

**`metrics.cursor.open`**

A document that contains data regarding open cursors.

**`metrics.cursor.open.noTimeout`**

The number of open cursors with the option
`DBQuery.Option.noTimeout` set to prevent timeout after a
period of inactivity.

**`metrics.cursor.open.pinned`**

The number of "pinned" open cursors.

**`metrics.cursor.open.total`**

The number of cursors that MongoDB is maintaining for clients.
Because MongoDB exhausts unused cursors, typically this value small
or zero. However, if there is a queue, or stale tailable cursors, or
a large number of operations this value may increase.

**`metrics.cursor.open.singleTarget`**

The total number of cursors that only target a *single* shard. Only
`mongos` instances report
`metrics.cursor.open.singleTarget` values.

**`metrics.cursor.open.multiTarget`**

The total number of cursors that only target *more than one* shard.
Only `mongos` instances report
`metrics.cursor.open.multiTarget` values.
