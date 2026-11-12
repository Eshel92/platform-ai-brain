<!-- Part 7 of 10 of reference/command/serverStatus.md (split because the page is big). -->

### shardingStatistics

tabs:

   - id: shard
     name: Shard
     content: |

      When run on a member of a shard:

      ```javascript
      shardingStatistics : {
         countStaleConfigErrors : Long("<num>"),
         countDonorMoveChunkStarted : Long("<num>"),
         countDonorMoveChunkCommitted : Long("<num>"),
         countDonorMoveChunkAborted : Long("<num>"),
         totalDonorMoveChunkTimeMillis : Long("<num>"),
         totalDonorChunkCloneTimeMillis : Long("<num>"),
         totalCriticalSectionCommitTimeMillis : Long("<num>"),
         totalCriticalSectionTimeMillis : Long("<num>"),
         countDocsClonedOnRecipient : Long("<num>"),
         countBytesClonedOnRecipient : Long("<num>"),
         countDocsClonedOnCatchUpOnRecipient : Long("<num>"),
         countBytesClonedOnCatchUpOnRecipient : Long("<num>"),
         countDocsClonedOnDonor : Long("<num>"),
         countRecipientMoveChunkStarted : Long("<num>"),
         countDocsDeletedByRangeDeleter : Long("<num>"),
         countDonorMoveChunkLockTimeout : Long("<num>"),
         unfinishedMigrationFromPreviousPrimary : Long("<num>"),
         chunkMigrationConcurrency : Long("<num>"),
         catalogCache : {
            numDatabaseEntries : Long("<num>"),
            numCollectionEntries : Long("<num>"),
            countStaleConfigErrors : Long("<num>"),
            totalRefreshWaitTimeMicros : Long("<num>"),
            numActiveIncrementalRefreshes : Long("<num>"),
            countIncrementalRefreshesStarted : Long("<num>"),
            numActiveFullRefreshes : Long("<num>"),
            countFullRefreshesStarted : Long("<num>"),
            countFailedRefreshes : Long("<num>")
         },
         rangeDeleterTasks : <num>,
         resharding : {
            countReshardingOperations : Long("<num>"),
            countReshardingSuccessful : Long("<num>"),
            countReshardingFailures : Long("<num>"),
            countReshardingCanceled : Long("<num>"),
            totalOperationTimeElapsedMillis : Long("<num>"),
            remainingOperationTimeEstimatedMillis : Long("<num>"),
            approxDocumentsToCopy : Long("<num>"),
            documentsCopied : Long("<num>"),
            approxBytesToCopy : Long("<num>"),
            bytesCopied : Long("<num>"),
            totalCopyTimeElapsedMillis : Long("<num>"),
            oplogEntriesFetched : Long("<num>"),
            oplogEntriesApplied : Long("<num>"),
            totalApplyTimeElapsedMillis : Long("<num>"),
            countWritesDuringCriticalSection : Long("<num>"),
            totalCriticalSectionTimeElapsedMillis : Long("<num>"),
            donorState : <num>,
            recipientState : <num>,
            coordinatorState : <num>,
            opStatus : <num>,
            lastOpEndingChunkImbalance: Long("<num>")
         }
      },
      ```

   - id: mongos
     name: mongos
     content: |

      When run on a `mongos`:

      ```javascript
      shardingStatistics : {
         numHostsTargeted: {
            find : {
               allShards: Long("<num>"),
               manyShards: Long("<num>"),
               oneShard: Long("<num>"),
               unsharded: Long("<num>") 
                     },
            insert: { 
               allShards: Long("<num>"),
               manyShards: Long("<num>"),
               oneShard: Long("<num>"),
               unsharded: Long("<num>") 
                     },
            update: { 
               allShards: Long("<num>"),
               manyShards: Long("<num>"),
               oneShard: Long("<num>"),
               unsharded: Long("<num>") 
                     },
            delete: { 
               allShards: Long("<num>"),
               manyShards: Long("<num>"),
               oneShard: Long("<num>"),
               unsharded: Long("<num>") 
                     },
            aggregate: { 
               allShards: Long("<num>"),
               manyShards: Long("<num>"),
               oneShard: Long("<num>"),
               unsharded: Long("<num>") 
                     }
            }
         },
         catalogCache : {
            numDatabaseEntries : Long("<num>"),
            numCollectionEntries : Long("<num>"),
            countStaleConfigErrors : Long("<num>"),
            totalRefreshWaitTimeMicros : Long("<num>"),
            numActiveIncrementalRefreshes : Long("<num>"),
            countIncrementalRefreshesStarted : Long("<num>"),
            numActiveFullRefreshes : Long("<num>"),
            countFullRefreshesStarted : Long("<num>"),
            countFailedRefreshes : Long("<num>")
         }
      }
      ```

   - id: config
     name: Config
     content: |

      When run on a config server:

      ```javascript
      "shardingStatistics" : {
         "numShardedCollections" : Long(<num>) 
      }
      ```

**`shardingStatistics`**

A document which contains metrics on metadata refresh on sharded
clusters.

**`shardingStatistics.countStaleConfigErrors`**

The total number of times that threads hit stale config exception.
Since a stale config exception triggers a refresh of the metadata,
this number is roughly proportional to the number of metadata
refreshes.

*Only present when run on a shard.*

**`shardingStatistics.countDonorMoveChunkStarted`**

The total number of times that MongoDB starts the
`moveChunk` command or `moveRange` command on
the primary node of the shard as part of the range migration
procedure. This increasing number does not
consider whether the chunk migrations succeed or not.

*Only present when run on a shard.*

**`shardingStatistics.countDonorMoveChunkCommitted`**

The total number of chunk migrations that MongoDB commits on the
primary node of the shard.

The chunk migration is performed by `moveChunk` and
`moveRange` commands in a range migration procedure.

*Only available on a shard.*

Available starting in MongoDB 6.0.6 (and 5.0.18).

**`shardingStatistics.countDonorMoveChunkAborted`**

The total number of chunk migrations that MongoDB aborts on the
primary node of the shard. 

The chunk migration is performed by `moveChunk` and
`moveRange` commands in a range migration procedure.

*Only available on a shard.*

Available starting in MongoDB 6.0.6 (and 5.0.18).

**`shardingStatistics.totalDonorMoveChunkTimeMillis`**

Cumulative time in milliseconds to move chunks from the current shard
to another shard. For each chunk migration, the time starts when a
`moveRange` or `moveChunk` command starts, and
ends when the chunk is moved to another shard in a range
migration procedure.

*Only available on a shard.*

Available starting in MongoDB 6.0.6 (and 5.0.18).

**`shardingStatistics.totalDonorChunkCloneTimeMillis`**

The cumulative time, in milliseconds, that the clone phase of
the range migration procedure takes on
the primary node of the shard.  Specifically, for each migration on
this shard, the tracked time starts with the `moveRange`
and `moveChunk` commands and ends before the destination
shard enters a `catchup` phase to apply changes that occurred
during the range migration procedure.

*Only present when run on a shard.*

**`shardingStatistics.totalCriticalSectionCommitTimeMillis`**

The cumulative time, in milliseconds, that the update metadata
phase of the range migrations procedure
takes on the primary node of the shard. During the update metadata
phase, MongoDB blocks all operations on the collection.

*Only present when run on a shard.*

**`shardingStatistics.totalCriticalSectionTimeMillis`**

The cumulative time, in milliseconds, that the catch-up
phase and the update metadata phase of the range migration procedure takes on the primary node of the shard. 

To calculate the duration of the catch-up phase, subtract
`totalCriticalSectionCommitTimeMillis` from
`totalCriticalSectionTimeMillis`:

```none
totalCriticalSectionTimeMillis - totalCriticalSectionCommitTimeMillis
```

*Only present when run on a shard.*

**`shardingStatistics.countDocsClonedOnRecipient`**

The cumulative, always-increasing count of documents that MongoDB
clones on the primary node of the recipient shard.

*Only present when run on a shard.*

**`shardingStatistics.countBytesClonedOnRecipient`**

The cumulative number of bytes that MongoDB clones on the primary
node of the recipient shard during the range migration procedure. 

For details about data synchronization, see replica-set-sync.

*Only available on a shard.*

Available starting in MongoDB 6.0.6 (and 5.0.18).

**`shardingStatistics.countDocsClonedOnCatchUpOnRecipient`**

The cumulative number of documents that MongoDB clones on the primary
node of the recipient shard during the catch-up phase of the
range migration procedure. 

For details about data synchronization, see replica-set-sync.

*Only available on a shard.*

Available starting in MongoDB 6.0.6 (and 5.0.18).

**`shardingStatistics.countBytesClonedOnCatchUpOnRecipient`**

The cumulative number of bytes that MongoDB clones on the primary
node of the recipient shard during the catch-up phase of the
range migration procedure. 

For details about data synchronization, see replica-set-sync.

*Only available on a shard.*

Available starting in MongoDB 6.0.6 (and 5.0.18).

**`shardingStatistics.countDocsClonedOnDonor`**

The cumulative, always-increasing count of documents that MongoDB
clones on the primary node of the donor shard. 

*Only present when run on a shard.*

**`shardingStatistics.countRecipientMoveChunkStarted`**

Cumulative, always-increasing count of chunks this member, acting as
the primary of the recipient shard, has started to receive (whether
the move has succeeded or not).

*Only present when run on a shard.*

**`shardingStatistics.countDocsDeletedByRangeDeleter`**

The cumulative, always-increasing count of documents that MongoDB
deletes on the primary node of the donor shard during chunk
migration. 

*Only present when run on a shard.*

**Changed in version:** 7.1

**`shardingStatistics.countDonorMoveChunkLockTimeout`**

The cumulative, always-increasing count of chunk migrations that MongoDB
aborts on the primary node of the donor shard due to lock acquisition
timeouts.

*Only present when run on a shard.*

**`shardingStatistics.unfinishedMigrationFromPreviousPrimary`**

The number of unfinished migrations left by the previous
primary after an election. This value is only updated after
the newly-elected `mongod` completes the transition to
primary.

*Only present when run on a shard.*

**`shardingStatistics.chunkMigrationConcurrency`**

The number of threads on the source shard and the receiving shard for
performing chunk migration
operations.

*Only present when run on a shard.*

*Available starting in MongoDB 6.3 (and 6.0.5 and 5.0.15)*

**`shardingStatistics.catalogCache`**

A document with statistics about the cluster's routing information cache.

**`shardingStatistics.catalogCache.numDatabaseEntries`**

The total number of database entries that are currently in the
catalog cache.

**`shardingStatistics.catalogCache.numCollectionEntries`**

The total number of collection entries (across all databases) that
are currently in the catalog cache.

**`shardingStatistics.catalogCache.countStaleConfigErrors`**

The total number of times that threads hit stale config exception. A
stale config exception triggers a refresh of the metadata.

**`shardingStatistics.catalogCache.totalRefreshWaitTimeMicros`**

The cumulative time, in microseconds, that threads had to wait for a
refresh of the metadata.

**`shardingStatistics.catalogCache.numActiveIncrementalRefreshes`**

The number of incremental catalog cache refreshes that are currently
waiting to complete.

**`shardingStatistics.countIncrementalRefreshesStarted`**

The cumulative number of incremental refreshes that have started.

**`shardingStatistics.catalogCache.numActiveFullRefreshes`**

The number of full catalog cache refreshes that are currently
waiting to complete.

**`shardingStatistics.catalogCache.countFullRefreshesStarted`**

The cumulative number of full refreshes that have started.

**`shardingStatistics.catalogCache.countFailedRefreshes`**

The cumulative number of full or incremental refreshes that have failed.

**`shardingStatistics.rangeDeleterTasks`**

The current total of the queued chunk range deletion tasks that are
ready to run or are running as part of the range migration
procedure.

Inspect the documents in the `config.rangeDeletions` collection
for information about the chunk ranges pending deletion from a shard
after a chunk migration.

*Only present when run on a shard member.*

**`shardingStatistics.resharding`**

A document with statistics about resharding operations.

Each shard returns its own resharding operation statistics. If a
shard is not involved in a resharding operation, then that shard will
not contain statistics about the resharding operation.

*Only present when run on a shard or config server.*

**New in version:** 5.0

**`shardingStatistics.resharding.countReshardingOperations`**

The sum of
`countReshardingSuccessful`,
`countReshardingFailures`,
and
`countReshardingCanceled`.
The sum is further incremented by `1` if a resharding
operation has started but has not yet
completed. Sum is set to 0 when `mongod` is started or
restarted.

*Only present when run on a shard or config server.*

**New in version:** 5.0

**`shardingStatistics.resharding.countReshardingSuccessful`**

Number of successful resharding operations. Number is set to 0 when `mongod`
is started or restarted.

*Only present when run on a shard or config server.*

**New in version:** 5.0

**`shardingStatistics.resharding.countReshardingFailures`**

Number of failed resharding operations.
Number is set to 0 when `mongod` is started or
restarted.

*Only present when run on a shard or config server.*

**New in version:** 5.0

**`shardingStatistics.resharding.countReshardingCanceled`**

Number of canceled resharding operations. Number is set to 0 when `mongod`
is started or restarted.

*Only present when run on a shard or config server.*

**New in version:** 5.0

**`shardingStatistics.resharding.totalOperationTimeElapsedMillis`**

Total elapsed time, in milliseconds, for the current resharding
operation. Time is set to 0 when a new
resharding operation starts.

*Only present when run on a shard or config server. Returns 0 on a
config server.*

**New in version:** 5.0

**`shardingStatistics.resharding.remainingOperationTimeEstimatedMillis`**

Estimated remaining time, in milliseconds, for the current resharding
operation. Time is set to 0 when a new resharding operation starts.

*Only present when run on a shard or config server. Returns 0 on a
config server.*

**New in version:** 5.0

**`shardingStatistics.resharding.approxDocumentsToCopy`**

Approximate number of documents to copy from donor shards to
recipient shards for the current resharding operation. Number is an estimate that is set when the
resharding operation starts and the number is not updated as the
operation progresses. Number is set to 0 when a new resharding
operation starts.

*Only present when run on a shard or config server. Returns 0 on a
config server.*

**New in version:** 5.0

**`shardingStatistics.resharding.documentsCopied`**

Number of documents copied from donor shards to recipient shards for
the current resharding operation. Number
is set to 0 when a new resharding operation starts.

*Only present when run on a shard or config server. Returns 0 on a
config server.*

**New in version:** 5.0

**`shardingStatistics.resharding.approxBytesToCopy`**

Approximate number of bytes to copy from donor shards to recipient
shards for the current resharding operation. Number is an estimate that is set when the
resharding operation starts and the number is not updated as the
operation progresses. Number is set to 0 when a new resharding
operation starts.

*Only present when run on a shard or config server. Returns 0 on a
config server.*

**New in version:** 5.0

**`shardingStatistics.resharding.bytesCopied`**

Number of bytes copied from donor shards to recipient shards for the
current resharding operation. Number is
set to 0 when a new resharding operation starts.

*Only present when run on a shard or config server. Returns 0 on a
config server.*

**New in version:** 5.0

**`shardingStatistics.resharding.totalCopyTimeElapsedMillis`**

Total elapsed time, in milliseconds, for ongoing data copy tasks from
donor shards to recipient shards for the current resharding
operation. Time is set to 0 when a new
resharding operation starts.

*Only present when run on a shard or config server. Returns 0 on a
config server.*

**New in version:** 5.0

**`shardingStatistics.resharding.oplogEntriesFetched`**

Number of entries fetched from the oplog for the current
resharding operation. Number is set to 0
when a new resharding operation starts.

*Only present when run on a shard or config server. Returns 0 on a
config server.*

**`shardingStatistics.resharding.oplogEntriesApplied`**

Number of entries applied to the oplog for the current
resharding operation. Number is set to 0
when a new resharding operation starts.

*Only present when run on a shard or config server. Returns 0 on a
config server.*

**New in version:** 5.0

**`shardingStatistics.resharding.totalApplyTimeElapsedMillis`**

Total elapsed time, in milliseconds, for the apply step of the
current resharding operation. In the
apply step, recipient shards modify their data based on new incoming
writes from donor shards. Time is set to 0 when a new resharding
operation starts.

*Only present when run on a shard or config server. Returns 0 on a
config server.*

**New in version:** 5.0

**`shardingStatistics.resharding.countWritesDuringCriticalSection`**

Number of writes perfomed in the critical section for the current
resharding operation. The critical
section prevents new incoming writes to the collection currently
being resharded. Number is set to 0 when a new resharding operation
starts.

*Only present when run on a shard or config server. Returns 0 on a
config server.*

**New in version:** 5.0

**`shardingStatistics.resharding.totalCriticalSectionTimeElapsedMillis`**

Total elapsed time, in milliseconds, for the critical section of the
current resharding operation. The
critical section prevents new incoming writes to the collection
currently being resharded. Time is set to 0 when a new resharding
operation starts.

*Only present when run on a shard or config server. Returns 0 on a
config server.*

**New in version:** 5.0

**`shardingStatistics.resharding.donorState`**

State of the donor shard for the current resharding operation. Number is set to 0 when a new
resharding operation starts.

| Number Returned | Meaning | Description |
|---|---|---|
| 0 | `unused` | The shard is not a donor in the current resharding operation. |
| 1 | `preparing-to-donate` | The donor shard is preparing to donate data to the recipient shards. |
| 2 | `donating-initial-data` | The donor shard is donating data to the recipient shards. |
| 3 | `donating-oplog-entries` | The donor shard is donating oplog entries to the recipient shards. |
| 4 | `preparing-to-block-writes` | The donor shard is about to prevent new incoming write operations to the collection that is being resharded. |
| 5 | `error` | An error occurred during the resharding operation. |
| 6 | `blocking-writes` | The donor shard is preventing new incoming write operations and the donor shard has notified all recipient shards that new incoming writes are prevented. |
| 7 | `done` | The donor shard has dropped the old sharded collection and the resharding operation is complete. |

*Only present when run on a shard or config server. Returns 0 on a
config server.*

**New in version:** 5.0

**`shardingStatistics.resharding.recipientState`**

State of the recipient shard for the current resharding
operation. Number is set to 0 when a new
resharding operation starts.

| Number Returned | Meaning | Description |
|---|---|---|
| 0 | `unused` | Shard is not a recipient in the current resharding operation. |
| 1 | `awaiting-fetch-timestamp` | The recipient shard is waiting for the donor shards to be prepared to donate their data |
| 2 | `creating-collection` | The recipient shard is creating the new sharded collection. |
| 3 | `cloning` | The recipient shard is receiving data from the donor shards. |
| 4 | `applying` | The recipient shard is applying oplog entries to modify its copy of the data based on the new incoming writes from donor shards. |
| 5 | `error` | An error occurred during the resharding operation. |
| 6 | `strict-consistency` | The recipient shard has all data changes stored in a temporary collection. |
| 7 | `done` | The resharding operation is complete. |

*Only present when run on a shard or config server. Returns 0 on a
config server.*

**New in version:** 5.0

**`shardingStatistics.numHostsTargeted`**

Indicates the number of shards targeted for `CRUD` operations and 
aggregation commands. When a `CRUD` operation or aggregation
command is run, the following metrics will be incremented.

| Name | Description |
|---|---|
| `allShards` | A command targeted all shards |
| `manyShards` | A command targeted more than one shard |
| `oneShard` | A command targeted one shard |
| `unsharded` | A command was run on an unsharded collection |

**Note:**

Running the `serverStatus` command on `mongos` 
will provide insight into the CRUD and aggregation operations that
run on a sharded cluster.

Multi-shard operations can either be 
scatter-gather
or shard specific. Multi-shard scatter-gather operations can
consume more resources.
By using the 
`shardingStatistics.numHostsTargeted`
metrics you can tune the aggregation queries that run on a 
sharded cluster.

**`shardingStatistics.numShardedCollections`**

Indicates the number of sharded collections in the cluster.

*Only present when run on a config server.*

**`shardingStatistics.resharding.coordinatorState`**

State of the resharding coordinator for the current resharding
operation. The resharding coordinator is a
thread that runs on the config server primary. Number is set to 0
when a new resharding operation starts.

* - Number Returned
  - Meaning
  - Description

* - 0
  - `unused`
  - The shard is not the coordinator in the current resharding
    operation.

* - 1
  - `initializing`
  - The resharding coordinator has inserted the coordinator
    document into `config.reshardingOperations` and has added
    the `reshardingFields` to the `config.collections` entry
    for the original collection.

* - 2
  - `preparing-to-donate`
  - The resharding coordinator

    - has created a `config.collections` entry for the temporary
      resharding collection.
    - has inserted entries into `config.chunks` for ranges based
      on the new shard key.
    - has inserted entries into `config.tags` for any zones
      associated with the new shard key.

    The coordinator informs participant shards to begin the
    resharding operation. The coordinator then waits until all
    donor shards have picked a `minFetchTimestamp` and are ready
    to donate.

* - 3
  - `cloning`
  - The resharding coordinator informs donor shards to donate data
    to recipient shards. The coordinator waits for all recipients
    to finish cloning the data from the donor.

* - 4
  - `applying`
  - The resharding coordinator informs recipient shards to modify
    their copies of data based on new incoming writes from donor
    shards. The coordinator waits for all recipients to finish
    applying oplog entries.

* - 5
  - `blocking-writes`
  - The resharding coordinator informs donor shards to prevent new
    incoming write operations to the collection being resharded.
    The coordinator then waits for all recipients to have all data
    changes.

* - 6
  - `aborting`
  - An unrecoverable error occurred during the resharding
    operation or the `abortReshardCollection` command
    (or the `sh.abortReshardCollection()` method) was run.

* - 6
  - `committing`
  - The resharding coordinator removes the `config.collections`
    entry for the temporary resharding collection. The coordinator
    then adds the `recipientFields` to the source collection's
    entry.

*Only present when run on a shard or config server.*

**New in version:** 5.0

**`shardingStatistics.resharding.opStatus`**

Status for the current resharding operation.

| Number Returned | Description |
|---|---|
| -1 | Resharding operation not in progress. |
| 0 | Resharding operation succeeded. |
| 1 | Resharding operation failed. |
| 2 | Resharding operation canceled. |

*Only present when run on a shard or config server.*

**New in version:** 5.0

**`shardingStatistics.resharding.lastOpEndingChunkImbalance`**

This field contains the highest numeric difference for 
(`maxNumChunksInShard - minNumChunksInShard`) among all 
zones for the 
collection that was processed by the most recent
resharding operation.

See sharding-chunk-size.

*Only updated on config servers.*

**New in version:** 5.0
