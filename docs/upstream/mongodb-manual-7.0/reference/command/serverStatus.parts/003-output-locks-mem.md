<!-- Part 3 of 11 of reference/command/serverStatus.md (split because the page is big). -->

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

Provides metrics around the caching of
server sessions.

**`logicalSessionRecordCache.activeSessionsCount`**

The number of all active local sessions cached in memory by the
`mongod` or `mongos` instance since the last
refresh period.

**See also:**

- `$listLocalSessions`
- `logicalSessionRefreshMillis`

**`logicalSessionRecordCache.sessionsCollectionJobCount`**

The number of times the refresh process has run on the
`config.system.sessions` collection.

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
