<!-- Part 8 of 10 of reference/command/serverStatus.md (split because the page is big). -->

### shardedIndexConsistency

```javascript
shardedIndexConsistency : {
   numShardedCollectionsWithInconsistentIndexes : Long("<num>")
},
```

**`shardedIndexConsistency`**

*Available only on config server instances.*

A document that returns results of index consistency checks for
sharded collections.

The returned metrics are meaningful only when run on the primary of
the config server replica set for a 
sharded cluster.

**See also:**

- `enableShardedIndexConsistencyCheck` parameter
- `shardedIndexConsistencyCheckIntervalMS` parameter

**`shardedIndexConsistency.numShardedCollectionsWithInconsistentIndexes`**

*Available only on config server instances.*

Number of sharded collections whose indexes are inconsistent across
the shards. A sharded collection has an inconsistent index if the
collection does not have the exact same indexes (including the index
options) on each shard that contains chunks for the collection.

To investigate if a sharded collection has inconsistent indexes, see
manage-indexes-find-inconsistent-indexes.

The returned metrics are meaningful only when run on the primary of
the config server replica set for a sharded cluster.

**See also:**

- `enableShardedIndexConsistencyCheck` parameter
- `shardedIndexConsistencyCheckIntervalMS` parameter


### storageEngine

```javascript
storageEngine : {
   name : <string>,
   supportsCommittedReads : <boolean>,
   persistent : <boolean>
},
```

**`storageEngine`**

A document with data about the current storage engine.

**`storageEngine.name`**

The name of the current storage engine.

**`storageEngine.supportsCommittedReads`**

A boolean that indicates whether the storage engine supports
`"majority"` read concern.

**`storageEngine.persistent`**

A boolean that indicates whether the storage engine does or does not persist data to disk.


### transactions

tabs:

   - id: mongod
     name: mongod
     content: |

        ```javascript
        transactions : {
           retriedCommandsCount : Long("<num>"),
           retriedStatementsCount : Long("<num>"),
           transactionsCollectionWriteCount : Long("<num>"),
           currentActive : Long("<num>"),
           currentInactive : Long("<num>"),
           currentOpen : Long("<num>"),
           totalAborted : Long("<num>"),
           totalCommitted : Long("<num>"),
           totalStarted : Long("<num>"),
           totalPrepared : Long("<num>"),
           totalPreparedThenCommitted : Long("<num>"),
           totalPreparedThenAborted :  Long("<num>"),
           currentPrepared :  Long("<num>"),
           lastCommittedTransaction : <document>
        },
        ```

   - id: mongos
     name: mongos
     content: |

        ```javascript
        transactions : {
           currentOpen : Long("<num>"),  
           currentActive : Long("<num>"),  
           currentInactive : Long("<num>"),
           totalStarted : Long("<num>"),
           totalCommitted : Long("<num>"),
           totalAborted : Long("<num>"),
           abortCause : {
              <String1> : Long("<num>"),
              <String2> : Long("<num>"),
              ...
           },
           totalContactedParticipants : Long("<num>"),
           totalParticipantsAtCommit : Long("<num>"),
           totalRequestsTargeted : Long("<num>"),
           commitTypes : {
              noShards : {
                 initiated : Long("<num>"),
                 successful : Long("<num>"),
                 successfulDurationMicros : Long("<num>")
              },
              singleShard : {
                 initiated : Long("<num>"),
                 successful : Long("<num>"),
                 successfulDurationMicros : Long("<num>")
              },
              singleWriteShard : {
                 initiated : Long("<num>"),
                 successful : Long("<num>"),
                 successfulDurationMicros : Long("<num>")
              },
              readOnly : {
                 initiated : Long("<num>"),
                 successful : Long("<num>"),
                 successfulDurationMicros : Long("<num>")
              },
              twoPhaseCommit : {
                 initiated : Long("<num>"),
                 successful : Long("<num>"),
                 successfulDurationMicros : Long("<num>")
              },
              recoverWithToken : {
                 initiated : Long("<num>"),
                 successful : Long("<num>"),
                 successfulDurationMicros : Long("<num>")
              }
           }
        },
        ```

**`transactions`**

When run on a `mongod`, a document with data about the
retryable writes and
transactions.

When run on a `mongos`, a document with data about the
transactions run on the instance.

**`transactions.retriedCommandsCount`**

*Available on mongod only.*

The total number of retry attempts that have been received after the
corresponding retryable write command has already been committed.
That is, a retryable write is attempted even though the write has
previously succeeded and has an associated record for the
transaction and session in the `config.transactions`
collection, such as when the initial write response to the client is
lost.

**Note:**

MongoDB does not re-execute the committed writes.

The total is across all sessions.

The total does not include any retryable writes that may happen
internally as part of a chunk migration.

**`transactions.retriedStatementsCount`**

*Available on mongod only.*

The total number of write statements associated with the retried
commands in `transactions.retriedCommandsCount`.

**Note:**

MongoDB does not re-execute the committed writes.

The total does not include any retryable writes that may happen
internally as part of a chunk migration.

**`transactions.transactionsCollectionWriteCount`**

*Available on mongod only.*

The total number of writes to the `config.transactions`
collection, triggered when a new retryable write statement is
committed.

For update and delete commands, since only single document
operations are retryable, there is one write per statement.

For insert operations, there is one write per batch of documents
inserted, except when a failure leads to each document being
inserted separately.

The total includes writes to a server's `config.transactions`
collection that occur as part of a migration.

**`transactions.currentActive`**

*Available on both mongod and mongos.*

The total number of open transactions currently executing a command.

**`transactions.currentInactive`**

*Available on both mongod and mongos.*

The total number of open transactions that are not currently
executing a command.

**`transactions.currentOpen`**

*Available on both mongod and mongos.*

The total number of open transactions. A transaction is opened when
the first command is run as a part of that transaction, and stays
open until the transaction either commits or aborts.

**`transactions.totalAborted`**

For the `mongod`, the total number of transactions
aborted on this instance since its last startup.

For the `mongos`, the total number of transactions
aborted through this instance since its last startup.

**`transactions.totalCommitted`**

For the `mongod`, the total number of transactions
committed on the instance since its last startup.

For the `mongos`,the total number of transactions
committed through this instance since its last startup.

**`transactions.totalStarted`**

For the `mongod`, the total number of transactions
started on this instance since its last startup.

For the `mongos`, the total number of transactions
started on this instance since its last startup.

**`transactions.abortCause`**

*Available on mongos only.*

Breakdown of the `transactions.totalAborted` by cause.
If a client issues an explicit `abortTransaction`, the cause is
listed as `abort`.

For example:

```javascript
totalAborted : Long("5"),
abortCause : {
   abort : Long("1"),
   DuplicateKey : Long("1"),
   StaleConfig : Long("3"),
   SnapshotTooOld : Long("1")
},
```

**`transactions.totalContactedParticipants`**

*Available on mongos only.*

The total number of shards contacted for all transactions started
through this `mongos` since its last startup.

The number of shards contacted during the transaction processes can
include those shards that may not be included as part of the commit.

**`transactions.totalParticipantsAtCommit`**

*Available on mongos only.*

Total number of shards involved in the commit for all transactions
started through this `mongos` since its last startup.

**`transactions.totalRequestsTargeted`**

*Available on mongos only.*

Total number of network requests targeted by the
`mongos` as part of its transactions.

**`transactions.commitTypes`**

*Available on mongos only.*

Breakdown of the commits by types. For example:

```javascript
noShards : {
   initiated : Long("0"),
   successful : Long("0"),
   successfulDurationMicros : Long("0")
},
singleShard : {
   initiated : Long("5"),
   successful : Long("5"),
   successfulDurationMicros : Long("203118")
},
singleWriteShard : {
   initiated : Long("0"),
   successful : Long("0"),
   successfulDurationMicros : Long("0")
},
readOnly : {
   initiated : Long("0"),
   successful : Long("0"),
   successfulDurationMicros : Long("0")
},
twoPhaseCommit : {
   initiated : Long("1"),
   successful : Long("1"),
   successfulDurationMicros : Long("179616")
},
recoverWithToken : {
   initiated : Long("0"),
   successful : Long("0"),
   successfulDurationMicros : Long("0")
}
```

The types of commit are:

| Type | Description |
|---|---|
| `noShards` | Commits of transactions that did not contact any shards. |
| `singleShard` | Commits of transactions that affected a single shard. |
| `singleWriteShard` | Commits of transactions that contacted multiple shards but whose write operations only affected a single shard. |
| `readOnly` | Commits of transactions that only involved read operations. |
| `twoPhaseCommit` | Commits of transactions that included writes to multiple shards |
| `recoverWithToken` | Commits that recovered the outcome of transactions from another instance or after this instance was restarted. |

For each commit type, the command returns the following metrics:

| Metrics | Description |
|---|---|
| `initiated` | Total number of times that commits of this type were initiated. |
| `successful` | Total number of times that commits of this type succeeded. |
| `successfulDurationMicros` | Total time, in microseconds, taken by successful commits of this type. |

**`transactions.totalPrepared`**

*Available on mongod only.*

The total number of transactions in prepared state on this server
since the `mongod` process's last startup.

**`transactions.totalPreparedThenCommitted`**

*Available on mongod only.*

The total number of transactions that were prepared and committed on
this server since the `mongod` process's last
startup.

**`transactions.totalPreparedThenAborted`**

*Available on mongod only.*

The total number of transactions that were prepared and aborted on
this server since the `mongod` process's last
startup.

**`transactions.currentPrepared`**

*Available on mongod only.*

The current number of transactions in prepared state on this server.

**`transactions.lastCommittedTransaction`**

*Available on mongod only.*

The details of the last transaction committed when the
`mongod` is primary.

When returned from a secondary,
`lastCommittedTransaction` returns the
details of the last transaction committed when that secondary was a
primary.

```javascript
lastCommittedTransaction : {
   operationCount : Long("1"),
   oplogOperationBytes : Long("211"),
   writeConcern : {
      w : "majority",
      wtimeout : 0
   }
}
```

| Metrics | Description |
|---|---|
| `operationCount` | The number of write operations in the transaction. |
| `oplogOperationBytes` | The size of the corresponding oplog entry or entries for the transaction. [#oplog-change]_ |
| `writeConcern` | The write concern used for the transaction. |


### transportSecurity

```javascript
transportSecurity : {
   1.0 : Long("<num>"),
   1.1 : Long("<num>"),
   1.2 : Long("<num>"),
   1.3 : Long("<num>"),
   unknown : Long("<num>")
},
```

**`transportSecurity.<version>`**

The cumulative number of TLS <version> connections that have been
made to this `mongod` or `mongos`
instance. The value is reset upon restart.


### watchdog

```javascript
watchdog : {
   checkGeneration : Long("<num>"),
   monitorGeneration : Long("<num>"),
   monitorPeriod : <num>
}
```

**Note:**

The `watchdog` section is only present if the Storage Node Watchdog is enabled.

**`watchdog`**

A document reporting the status of the
Storage Node Watchdog.

**`watchdog.checkGeneration`**

The number of times the directories have been checked since startup.
Directories are checked multiple times every `monitoringPeriod`.

**`watchdog.monitorGeneration`**

The number of times the status of all filesystems used by
`mongod` has been examined. This is incremented once
every `monitoringPeriod`.

**`watchdog.monitorPeriod`**

The value set by `watchdogPeriodSeconds`. This is the
period between status checks.
