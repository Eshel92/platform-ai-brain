<!-- Part 2 of 11 of reference/command/serverStatus.md (split because the page is big). -->

### electionMetrics

The `electionMetrics` section provides information on elections
called by this `mongod` instance in a bid to become the
primary:

```javascript
electionMetrics : {
   stepUpCmd : {
      called : Long("<num>"),
      successful : Long("<num>")
   },
   priorityTakeover : {
      called : Long("<num>"),
      successful : Long("<num>")
   },
   catchUpTakeover : {
      called : Long("<num>"),
      successful : Long("<num>")
   },
   electionTimeout : {
      called : Long("<num>"),
      successful : Long("<num>")
   },
   freezeTimeout : {
      called : Long("<num>"),
      successful : Long("<num>")
   },
   numStepDownsCausedByHigherTerm : Long("<num>"),
   numCatchUps : Long("<num>"),
   numCatchUpsSucceeded : Long("<num>"),
   numCatchUpsAlreadyCaughtUp : Long("<num>"),
   numCatchUpsSkipped : Long("<num>"),
   numCatchUpsTimedOut : Long("<num>"),
   numCatchUpsFailedWithError : Long("<num>"),
   numCatchUpsFailedWithNewTerm : Long("<num>"),
   numCatchUpsFailedWithReplSetAbortPrimaryCatchUpCmd : Long("<num>"),
   averageCatchUpOps : <double>
}
```

**`electionMetrics.stepUpCmd`**

Metrics on elections that were called by the `mongod`
instance as part of an election handoff when the primary stepped down.

The `stepUpCmd` includes both the number of elections
called and the number of elections that succeeded.

**`electionMetrics.priorityTakeover`**

Metrics on elections that were called by the `mongod`
instance because its `priority` is higher
than the primary's.

The `electionMetrics.priorityTakeover` includes both the number of
elections called and the number of elections that succeeded.

**`electionMetrics.catchUpTakeover`**

Metrics on elections called by the `mongod` instance
because it is more current than the primary.

The `catchUpTakeover` includes both the number of
elections called and the number of elections that succeeded.

**See also:**

`settings.catchUpTakeoverDelayMillis`

**`electionMetrics.electionTimeout`**

Metrics on elections called by the `mongod` instance
because it has not been able to reach the primary within
`settings.electionTimeoutMillis`.

The `electionTimeout` includes both the number of
elections called and the number of elections that succeeded.

**See also:**

`settings.electionTimeoutMillis`

**`electionMetrics.freezeTimeout`**

Metrics on elections called by the `mongod` instance
after its `freeze period` (during which the
member cannot seek an election) has expired.

The `electionMetrics.freezeTimeout` includes both the number of
elections called and the number of elections that succeeded.

**`electionMetrics.numStepDownsCausedByHigherTerm`**

Number of times the `mongod` instance stepped down
because it saw a higher term (specifically, other member(s)
participated in additional elections).

**`electionMetrics.numCatchUps`**

Number of elections where the `mongod` instance as the
newly-elected primary had to catch up to the highest known oplog
entry.

**`electionMetrics.numCatchUpsSucceeded`**

Number of times the `mongod` instance as the
newly-elected primary successfully caught up to the highest known
oplog entry.

**`electionMetrics.numCatchUpsAlreadyCaughtUp`**

Number of times the `mongod` instance as the
newly-elected primary concluded its catchup process because it was
already caught up when elected.

**`electionMetrics.numCatchUpsSkipped`**

Number of times the `mongod` instance as the
newly-elected primary skipped the catchup process.

**`electionMetrics.numCatchUpsTimedOut`**

Number of times the `mongod` instance as the
newly-elected primary concluded its catchup process because of the
`settings.catchUpTimeoutMillis` limit.

**`electionMetrics.numCatchUpsFailedWithError`**

Number of times the newly-elected primary's catchup process failed
with an error.

**`electionMetrics.numCatchUpsFailedWithNewTerm`**

Number of times the newly-elected primary's catchup process concluded
because another member(s) had a higher term (specifically, other
member(s) participated in additional elections).

**`electionMetrics.numCatchUpsFailedWithReplSetAbortPrimaryCatchUpCmd`**

Number of times the newly-elected primary's catchup process
concluded because the `mongod` received the
`replSetAbortPrimaryCatchUp` command.

**`electionMetrics.averageCatchUpOps`**

Average number of operations applied during the newly-elected
primary's catchup processes.


### extra_info

```javascript
extra_info : {
   note : 'fields vary by platform',
   page_faults : <num>
},
```

**`extra_info`**

A document that provides additional information about the underlying
system.

**`extra_info.note`**

A string with the text `'fields vary by platform'`

**`extra_info.page_faults`**

The total number of page faults. The
`extra_info.page_faults` counter may increase
dramatically during moments of poor performance and may correlate
with limited memory environments and larger data sets. Limited and
sporadic page faults do not necessarily indicate an issue.

Windows differentiates "hard" page faults involving disk I/O from
"soft" page faults that only require moving pages in memory. MongoDB
counts both hard and soft page faults in this statistic.


### flowControl

```javascript
flowControl : {
   enabled : <boolean>,
   targetRateLimit : <int>,
   timeAcquiringMicros : Long("<num>"),
   locksPerKiloOp : <double>,  
   sustainerRate : <int>,
   isLagged : <boolean>,
   isLaggedCount : <int>,
   isLaggedTimeMicros : Long("<num>")
},
```

**`flowControl`**

A document that returns statistics on the flow-control. With
flow control enabled, as the `majority commit` point lag grows
close to the `flowControlTargetLagSeconds`, writes on the
primary must obtain tickets before taking locks. As such, the
metrics returned are meaningful when run on the primary.

**`flowControl.enabled`**

A boolean that indicates whether flow-control is
enabled (`true`) or disabled (`false`).

See also `enableFlowControl`.

**`flowControl.targetRateLimit`**

When run on the primary, the maximum number of tickets that can be
acquired per second.

When run on a secondary, the returned number is a placeholder.
   

**`flowControl.timeAcquiringMicros`**

When run on the primary, the total time write operations have waited
to acquire a ticket.

When run on a secondary, the returned number is a placeholder.

**`flowControl.locksPerKiloOp`**

When run on the primary, an approximation of the number of locks
taken per 1000 operations.

When run on a secondary, the returned number is a placeholder.

**`flowControl.sustainerRate`**

When run on the primary, an approximation of operations applied per
second by the secondary that is sustaining the commit point.

When run on a secondary, the returned number is a placeholder.

**`flowControl.isLagged`**

When run on the primary, a boolean that indicates whether flow
control has engaged. Flow control engages when the majority
committed lag is greater than some percentage of the configured
`flowControlTargetLagSeconds`.

Replication lag can occur without engaging flow control.
An unresponsive secondary might lag without the replica set
receiving sufficient load to engage flow control, leaving 
the `flowControl.isLagged` value at `false`.

For additional information, see Flow Control.

**`flowControl.isLaggedCount`**

When run on a primary, the number of times flow control has engaged
since the last restart. Flow control engages when the majority
committed lag is greater than some percentage of the
`flowControlTargetLagSeconds`.

When run on a secondary, the returned number is a placeholder.

**`flowControl.isLaggedTimeMicros`**

When run on the primary, the amount of time flow control has spent
being engaged since the last restart. Flow control engages when the
majority committed lag is greater than some percentage of the
`flowControlTargetLagSeconds`.

When run on a secondary, the returned number is a placeholder.


### globalLock

```javascript
globalLock : {
   totalTime : Long("<num>"),
   currentQueue : {
      total : <num>,
      readers : <num>,
      writers : <num>
   },
   activeClients : {
      total : <num>,
      readers : <num>,
      writers : <num>
   }
},
```

**`globalLock`**

A document that reports on the database's lock state.

Generally, the locks document provides more detailed
data on lock uses.

**`globalLock.totalTime`**

The time, in microseconds, since the database last started and
created the `globalLock`. This is approximately
equivalent to the total server uptime.

**`globalLock.currentQueue`**

A document that provides information concerning the number of
operations queued because of a lock.

**`globalLock.currentQueue.total`**

The total number of operations queued waiting for the lock (that is,
the sum of `globalLock.currentQueue.readers` and
`globalLock.currentQueue.writers`).

A consistently small queue, particularly of shorter operations,
should cause no concern. The
`globalLock.activeClients` readers and writers
information provides context for this data.

**`globalLock.currentQueue.readers`**

The number of operations that are currently queued and waiting for
the read lock. A consistently small read queue, particularly of
shorter operations, should cause no concern.

**`globalLock.currentQueue.writers`**

The number of operations that are currently queued and waiting for
the write lock. A consistently small write queue, particularly of
shorter operations, is no cause for concern.

**`globalLock.activeClients`**

A document that provides information about the number of connected
clients and the read and write operations performed by these clients.

Use this data to provide context for the
`globalLock.currentQueue` data.

**`globalLock.activeClients.total`**

The total number of internal client connections to the database
including system threads as well as queued readers and writers.
This metric is higher than the total of `activeClients.readers`
and `activeClients.writers` due to the inclusion of system threads.

**`globalLock.activeClients.readers`**

The number of the active client connections performing read
operations.

**`globalLock.activeClients.writers`**

The number of active client connections performing write operations.


### hedgingMetrics

For `mongos` instances only.

```javascript
hedgingMetrics : {
   numTotalOperations : <num>,
   numTotalHedgedOperations : <num>,
   numAdvantageouslyHedgedOperations : <num>
},
```

**`hedgingMetrics`**

Provides metrics on hedged reads for
the `mongos` instance.

For `mongos` instances only.

**`hedgingMetrics.numTotalOperations`**

The total number of the operations issued with the hedged read
option enabled to this
`mongos` instance.

For `mongos` instances only.

**`hedgingMetrics.numTotalHedgedOperations`**

The number of all operations for which the `mongos`
instance hedged the read operation;
i.e. sent the operation to an additional member of each queried
shard.

For `mongos` instances only.

**`hedgingMetrics.numAdvantageouslyHedgedOperations`**

The total number of the operation where the additional read sent to
hedge the read operation fulfilled the
client request.

For `mongos` instances only.


### indexBuilds

```json
indexBuilds : { 
   total : <num>,
   phases : { 
      scanCollection : <num>, 
      drainSideWritesTable: <num>,
      drainSideWritesTablePreCommit: <num>,
      waitForCommitQuorum: <num>,
      drainSideWritesTableOnCommit: <num>,
      processConstraintsViolatonTableOnCommit: <num>,
      commit: <num>
   }
}
```

**`indexBuilds`**

A document that provides metrics for index builds. Use these metrics to
diagnose index build issues.

**Note:**

`indexBuilds` replaces the `activeIndexBuilds` field.

**New in version:** 6.1

**`indexBuilds.total`**

The total number of in-progress and completed index builds. 

**New in version:** 6.1

**`indexBuilds.phases`**

A document that provides counters for each stage of the 
index-build-process. Each sub-field under `indexBuilds.phases` 
increments when the index build reaches the specified stage.

**New in version:** 6.1


### indexBulkBuilder

```json
indexBulkBuilder: {
   count: <long>, 
   resumed: <long>, 
   filesOpenedForExternalSort: <long>, 
   filesClosedForExternalSort: <long>, 
   spilledRanges: <long>, 
   bytesSpilledUncompressed: <long>,
   bytesSpilled: <long>,
   numSorted: <long>,
   bytesSorted: <long>,
   memUsage: <long>
}
```

**`indexBulkBuilder`**

Provides metrics for index bulk builder operations.  Use these metrics to
diagnose index build issues with `createIndexes`, collection 
cloning during initial sync, index builds that resume after startup, and
statistics on disk usage by the external sorter.

**`indexBulkBuilder.bytesSpilled`**

**New in version:** 6.0.4

The number of bytes written to disk by the external sorter.

**`indexBulkBuilder.bytesSpilledUncompressed`**

**New in version:** 6.0.4

The number of bytes to be written to disk by the external sorter 
before compression. 

**`indexBulkBuilder.count`**

The number of instances of the bulk builder created.

**`indexBulkBuilder.filesClosedForExternalSort`**

The number of times the external sorter closed a file handle to spill data
to disk.  Combine this value with 
`filesOpenedForExternalSort` to determine
the number of open file handles in use by the external sorter.

**`indexBulkBuilder.filesOpenedForExternalSort`**

The number of times the external sorter opened a file handle to spill data
to disk.  Combine this value with 
`filesClosedForExternalSort` to determine
the number of open file handles in use by the external sorter.

**`indexBulkBuilder.resumed`**

The number of times the bulk builder was created for a resumable index build.

**`indexBulkBuilder.spilledRanges`**

**New in version:** 6.0.4

The number of times the external sorter spilled to disk. 

**`indexBulkBuilder.numSorted`**

**New in version:** 6.3

The total number of sorted documents.

**`indexBulkBuilder.bytesSorted`**

**New in version:** 6.3

The total number of bytes for sorted documents. For example, if
a total of 10 documents were sorted and each document is 20 bytes,
the total number of bytes sorted is 200.

**`indexBulkBuilder.memUsage`**

**New in version:** 6.3

The current bytes of memory allocated for building indexes.


### indexStats

```json
indexStats: {
   count: Long("<num>"), 
   features: {
      '2d': { count: Long("<num>"), accesses: Long("<num>") },
      '2dsphere': { count: Long("<num>"), accesses: Long("<num>") },
      '2dsphere_bucket': { count: Long("<num>"), accesses: Long("<num>") },
      collation: { count: Long("<num>"), accesses: Long("<num>") },
      compound: { count: Long("<num>"), accesses: Long("<num>") },
      hashed: { count: Long("<num>"), accesses: Long("<num>") },
      id: { count: Long("<num>"), accesses: Long("<num>") },
      normal: { count: Long("<num>"), accesses: Long("<num>") },
      partial: { count: Long("<num>"), accesses: Long("<num>") },
      prepareUnique: { count: Long("<num>"), accesses: Long("<num>") }, // Added in 7.0.14 (and 6.0.20)
      single: { count: Long("<num>"), accesses: Long("<num>") },
      sparse: { count: Long("<num>"), accesses: Long("<num>") },
      text: { count: Long("<num>"), accesses: Long("<num>") },
      ttl: { count: Long("<num>"), accesses: Long("<num>") },
      unique: { count: Long("<num>"), accesses: Long("<num>") },
      wildcard: { count: Long("<num>"), accesses: Long("<num>") }
   }
}
```

**`indexStats`**

A document that reports statistics on all indexes on databases and collections 
in non-system namespaces only. `indexStats` does not report statistics 
on indexes in the `admin`, `local`, and `config` databases.

**New in version:** 6.0

**`indexStats.count`**

The total number of indexes.

**New in version:** 6.0

**`indexStats.features`**

A document that provides counters for each index type and the number of 
accesses on each index. Each index type under `indexStats.features` 
has a `count` field that counts the total number of indexes for that 
type, and an `accesses` field that counts the number of accesses on that 
index.

**New in version:** 6.0


### Instance Information

```javascript
host : <string>,
advisoryHostFQDNs : <array>,
version : <string>,
process : <'mongod'|'mongos'>,
pid : Long("<num>"),
uptime : <num>,
uptimeMillis : Long("<num>"),
uptimeEstimate : Long("<num>"),
localTime : ISODate("<Date>"),
```

**`host`**

The system's hostname. In Unix/Linux systems, this should be the
same as the output of the `hostname` command.

**`advisoryHostFQDNs`**

An array of the system's fully qualified domain names (FQDNs).

**`version`**

The MongoDB version of the current MongoDB process.

**`process`**

The current MongoDB process. Possible values are: `mongos` or
`mongod`.

**`pid`**

The process ID number.

**`uptime`**

The number of seconds that the current MongoDB process has been
active.

**`uptimeMillis`**

The number of milliseconds that the current MongoDB process has been
active.

**`uptimeEstimate`**

The uptime in seconds as calculated from MongoDB's internal
coarse-grained time keeping system.

**`localTime`**

The ISODate representing the current time, according to the server,
in UTC.


### latchAnalysis

**New in version:** 4.4

```javascript
latchAnalysis : {
   <latch name> : {
      created : <num>,
      destroyed : <num>,
      acquired : <num>,
      released : <num>,
      contended : <num>,
      hierarchicalAcquisitionLevelViolations : {
            onAcquire : <num>,
            onRelease : <num>
      }
   },
   ...
```

**`latchAnalysis`**

A document that reports on metrics related to internal locking
primitives (also known as latches).

To return `latchAnalysis` information, you must
explicitly specify the inclusion:

```javascript
db.runCommand( { serverStatus: 1, latchAnalysis: 1 } )
```

The `latchAnalysis` returns for each latch the `<latch name>`
and the following associated metrics:

* - Metric
  - Description

* - `created`

  - Number of times the latch was created.

* - `destroyed`

  - Number of times the latch was destroyed.

* - `acquired`

  - Number of times the latch was acquired.

* - `released`

  - Number of times the latch was released.

* - `contended`
  - Number of times the latch had contention.

* - `hierarchicalAcquisitionLevelViolations`

  - *Only returned if violations exist*

    Contains the following fields:

    - `onAcquire`

      - Number of times the latch hierarchy (i.e. the latch level
        ordering) has been violated during latch acquisition.

    - `onRelease`

      - Number of times the latch hierarchy (i.e. the latch level
        ordering) has been violated during latch release.

**New in version:** 4.4
