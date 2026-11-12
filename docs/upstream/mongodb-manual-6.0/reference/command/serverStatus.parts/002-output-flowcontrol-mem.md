<!-- Part 2 of 10 of reference/command/serverStatus.md (split because the page is big). -->

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

The total number of operations queued waiting for the lock (i.e.,
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
This metric will be higher than the total of `activeClients.readers`
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


### indexBulkBuilder

```json
indexBulkBuilder: {
   count: <long>, 
   resumed: <long>, 
   filesOpenedForExternalSort: <long>, 
   filesClosedForExternalSort: <long>, 
   spilledRanges: <long>, 
   bytesSpilledUncompressed: <long>,
   bytesSpilled: <long>
}
```

**`indexBulkBuilder`**

Provides metrics for index bulk builder operations.  Use these metrics to
diagnose index build issues with `createIndexes`, collection 
cloning during initial sync, index builds that resume after startup, and
statistics on disk usage by the external sorter.

**`indexBuildBuilder.bytesSpilled`**

**New in version:** 6.0.4

The number of bytes written to disk by the external sorter.

**`indexBuilder.bytesSpilledUncompressed`**

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
course-grained time keeping system.

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


### locks

```javascript
locks : {
   <type> : {
         acquireCount : {
            <mode> : Long("<num>"),
            ...
         },
         acquireWaitCount : {
            <mode> : Long("<num>"),
            ...
         },
         timeAcquiringMicros : {
            <mode> : Long("<num>"),
            ...
         },
         deadlockCount : {
            <mode> : Long("<num>"),
            ...
         }
   },
   ...
```

**`locks`**

A document that reports for each lock `<type>`, data on lock
`<modes>`.

The possible lock `<types>` are:

| Lock Type | Description |
|---|---|
| `ParallelBatchWriterMode` | Represents a lock for parallel batch writer mode. In earlier versions, PBWM information was reported as part of the `Global` lock information. |
| `ReplicationStateTransition` | Represents lock taken for replica set member state transitions. |
| `Global` | Represents global lock. |
| `Database` | Represents database lock. |
| `Collection` | Represents collection lock. |
| `Mutex` | Represents mutex. |
| `Metadata` | Represents metadata lock. |
| `oplog` | Represents lock on the oplog. |

The possible `<modes>` are:

| Lock Mode | Description |
|---|---|
| `R` | Represents Shared (S) lock. |
| `W` | Represents Exclusive (X) lock. |
| `r` | Represents Intent Shared (IS) lock. |
| `w` | Represents Intent Exclusive (IX) lock. |

All values are of the `Long()` type.

**`locks.<type>.acquireCount`**

Number of times the lock was acquired in the specified mode.

**`locks.<type>.acquireWaitCount`**

Number of times the `locks.<type>.acquireCount` lock
acquisitions encountered waits because the locks were held in a
conflicting mode.

**`locks.<type>.timeAcquiringMicros`**

Cumulative wait time in microseconds for the lock acquisitions.

`locks.<type>.timeAcquiringMicros` divided by
`locks.<type>.acquireWaitCount` gives an
approximate average wait time for the particular lock mode.

**`locks.<type>.deadlockCount`**

Number of times the lock acquisitions encountered deadlocks.


### logicalSessionRecordCache

```javascript
logicalSessionRecordCache : {
   activeSessionsCount : <num>,
   sessionsCollectionJobCount : <num>,
   lastSessionsCollectionJobDurationMillis : <num>,
   lastSessionsCollectionJobTimestamp : <Date>,
   lastSessionsCollectionJobEntriesRefreshed : <num>,
   lastSessionsCollectionJobEntriesEnded : <num>,
   lastSessionsCollectionJobCursorsClosed : <num>,
   transactionReaperJobCount : <num>,
   lastTransactionReaperJobDurationMillis : <num>,
   lastTransactionReaperJobTimestamp : <Date>,
   lastTransactionReaperJobEntriesCleanedUp : <num>,
   sessionCatalogSize : <num>  
},
```

**`logicalSessionRecordCache`**

Provides metrics around the caching of server sessions.

**`logicalSessionRecordCache.activeSessionsCount`**

The number of all active local sessions cached in memory by the
`mongod` or `mongos` instance since the last
refresh period.

**See also:**

- `$listLocalSessions`
- `logicalSessionRefreshMillis`

**`logicalSessionRecordCache.sessionsCollectionJobCount`**

The number that tracks the number of times the refresh process has
run on the `config.system.sessions` collection.

**See also:**

`logicalSessionRefreshMillis`

**`logicalSessionRecordCache.lastSessionsCollectionJobDurationMillis`**

The length in milliseconds of the last refresh.

**`logicalSessionRecordCache.lastSessionsCollectionJobTimestamp`**

The time at which the last refresh occurred.

**`logicalSessionRecordCache.lastSessionsCollectionJobEntriesRefreshed`**

The number of sessions that were refreshed during the last refresh.

**`logicalSessionRecordCache.lastSessionsCollectionJobEntriesEnded`**

The number of sessions that ended during the last refresh.

**`logicalSessionRecordCache.lastSessionsCollectionJobCursorsClosed`**

The number of cursors that were closed during the last
`config.system.sessions` collection refresh.

**`logicalSessionRecordCache.transactionReaperJobCount`**

The number that tracks the number of times the transaction record
cleanup process has run on the `config.transactions`
collection.

**`logicalSessionRecordCache.lastTransactionReaperJobDurationMillis`**

The length (in milliseconds) of the last transaction record cleanup.

**`logicalSessionRecordCache.lastTransactionReaperJobTimestamp`**

The time of the last transaction record cleanup.

**`logicalSessionRecordCache.lastTransactionReaperJobEntriesCleanedUp`**

The number of entries in the `config.transactions` collection
that were deleted during the last transaction record cleanup.

**`logicalSessionRecordCache.sessionCatalogSize`**

- For a `mongod` instance, 
     The size of its in-memory cache of the `config.transactions`
     entries. This corresponds to retryable writes
     or transactions whose sessions have not expired within the
     `localLogicalSessionTimeoutMinutes`.

- For a `mongos` instance, 
     The number of the in-memory cache of its sessions that have had
     transactions within the most recent
     `localLogicalSessionTimeoutMinutes` interval.


### mem

```javascript
mem : {
   bits : <int>,
   resident : <int>,
   virtual : <int>,
   supported : <boolean>
},
```

**`mem`**

A document that reports on the system architecture of the
`mongod` and current memory use.

**`mem.bits`**

A number, either `64` or `32`, that indicates whether the
MongoDB instance is compiled for 64-bit or 32-bit architecture.

**`mem.resident`**

The value of `mem.resident` is roughly equivalent to
the amount of RAM, in mebibyte (MiB), currently used by the database
process. During normal use, this value tends to grow. In dedicated
database servers, this number tends to approach the total amount of
system memory.

**`mem.virtual`**

`mem.virtual` displays the quantity, in mebibyte
(MiB), of virtual memory used by the `mongod` process.

**`mem.supported`**

A boolean that indicates whether the underlying system supports
extended memory information. If this value is false and the system
does not support extended memory information, then other
`mem` values may not be accessible to the database
server.

**`mem.note`**

The field `mem.note` appears if
`mem.supported` is false.

The `mem.note` field contains the text: ``'not all mem
info support on this platform'``.
