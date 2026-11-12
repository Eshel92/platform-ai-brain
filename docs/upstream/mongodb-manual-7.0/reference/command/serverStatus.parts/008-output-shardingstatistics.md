<!-- Part 8 of 11 of reference/command/serverStatus.md (split because the page is big). -->

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
         unauthorizedDirectShardOps : Long("<num>"),
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
            countStarted : Long("1"),
             countSucceeded : Long("1"),
             countFailed : Long("0"),
             countCanceled : Long("0"),
             lastOpEndingChunkImbalance : Long("0"),
             active : {
                     documentsCopied : Long("0"),
                     bytesCopied : Long("0"),
                     countWritesToStashCollections : Long("0"),
                     countWritesDuringCriticalSection : Long("0"),
                     countReadsDuringCriticalSection : Long("0"),
                     oplogEntriesFetched : Long("0"),
                     oplogEntriesApplied : Long("0"),
                     insertsApplied : Long("0"),
                     updatesApplied : Long("0"),
                     deletesApplied : Long("0")
             },
             oldestActive : {
                     coordinatorAllShardsHighestRemainingOperationTimeEstimatedMillis : Long("0"),
                     coordinatorAllShardsLowestRemainingOperationTimeEstimatedMillis : Long("0"),
                     recipientRemainingOperationTimeEstimatedMillis : Long("0")
             },
             latencies : {
                     collectionCloningTotalRemoteBatchRetrievalTimeMillis : Long("0"),
                     collectionCloningTotalRemoteBatchesRetrieved : Long("0"),
                     collectionCloningTotalLocalInsertTimeMillis : Long("0"),
                     collectionCloningTotalLocalInserts : Long("0"),
                     oplogFetchingTotalRemoteBatchRetrievalTimeMillis : Long("0"),
                     oplogFetchingTotalRemoteBatchesRetrieved : Long("0"),
                     oplogFetchingTotalLocalInsertTimeMillis : Long("0"),
                     oplogFetchingTotalLocalInserts : Long("0"),
                     oplogApplyingTotalLocalBatchRetrievalTimeMillis : Long("0"),
                     oplogApplyingTotalLocalBatchesRetrieved : Long("0"),
                     oplogApplyingTotalLocalBatchApplyTimeMillis : Long("0"),
                     oplogApplyingTotalLocalBatchesApplied : Long("0")
             },
             currentInSteps : {
                     countInstancesInCoordinatorState1Initializing : Long("0"),
                     countInstancesInCoordinatorState2PreparingToDonate : Long("0"),
                     countInstancesInCoordinatorState3Cloning : Long("0"),
                     countInstancesInCoordinatorState4Applying : Long("0"),
                     countInstancesInCoordinatorState5BlockingWrites : Long("0"),
                     countInstancesInCoordinatorState6Aborting : Long("0"),
                     countInstancesInCoordinatorState7Committing : Long("-1"),
                     countInstancesInRecipientState1AwaitingFetchTimestamp : Long("0"),
                     countInstancesInRecipientState2CreatingCollection : Long("0"),
                     countInstancesInRecipientState3Cloning : Long("0"),
                     countInstancesInRecipientState4Applying : Long("0"),
                     countInstancesInRecipientState5Error : Long("0"),
                     countInstancesInRecipientState6StrictConsistency : Long("0"),
                     countInstancesInRecipientState7Done : Long("0"),
                     countInstancesInDonorState1PreparingToDonate : Long("0"),
                     countInstancesInDonorState2DonatingInitialData : Long("0"),
                     countInstancesInDonorState3DonatingOplogEntries : Long("0"),
                     countInstancesInDonorState4PreparingToBlockWrites : Long("0"),
                     countInstancesInDonorState5Error : Long("0"),
                     countInstancesInDonorState6BlockingWrites : Long("0"),
                     countInstancesInDonorState7Done : Long("0")
             }
          }
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
      shardingStatistics : {
         numShardedCollections : Long("<num>") 
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

Available starting in MongoDB 7.0 (and 6.3.2, 6.0.6, and 5.0.18).

**`shardingStatistics.countDonorMoveChunkAborted`**

The total number of chunk migrations that MongoDB aborts on the
primary node of the shard. 

The chunk migration is performed by `moveChunk` and
`moveRange` commands in a range migration procedure.

*Only available on a shard.*

Available starting in MongoDB 7.0 (and 6.3.2, 6.0.6, and 5.0.18).

**`shardingStatistics.totalDonorMoveChunkTimeMillis`**

Cumulative time in milliseconds to move chunks from the current shard
to another shard. For each chunk migration, the time starts when a
`moveRange` or `moveChunk` command starts, and
ends when the chunk is moved to another shard in a range
migration procedure.

*Only available on a shard.*

Available starting in MongoDB 7.0 (and 6.3.2, 6.0.6, and 5.0.18).

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

Available starting in MongoDB 7.0 (and 6.3.2, 6.0.6, and 5.0.18).

**`shardingStatistics.countDocsClonedOnCatchUpOnRecipient`**

The cumulative number of documents that MongoDB clones on the primary
node of the recipient shard during the catch-up phase of the
range migration procedure. 

For details about data synchronization, see replica-set-sync.

*Only available on a shard.*

Available starting in MongoDB 7.0 (and 6.3.2, 6.0.6, and 5.0.18).

**`shardingStatistics.countBytesClonedOnCatchUpOnRecipient`**

The cumulative number of bytes that MongoDB clones on the primary
node of the recipient shard during the catch-up phase of the
range migration procedure. 

For details about data synchronization, see replica-set-sync.

*Only available on a shard.*

Available starting in MongoDB 7.0 (and 6.3.2, 6.0.6, and 5.0.18).

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

*Available starting in MongoDB 6.3 (and 5.0.15).*

**`shardingStatistics.unauthorizedDirectShardOps`**

The number of direct shard operations attempted without sufficient 
authorization.  If the operation generates a warning rather than an 
error, `unauthorizedDirectShardOps` might count it more than once.

On a sharded cluster with a single shard, you can control this counter 
by setting the `directConnectionChecksWithSingleShard` parameter to
`true`.

**`shardingStatistics.databaseCriticalSectionStatistics`**

A document with statistics about the critical sections for
databases, including counts of how many operations hold the critical section, 
how many are waiting, and how long they have waited.

**New in version:** 8.3

**`shardingStatistics.collectionCriticalSectionStatistics`**

A document with statistics about the critical sections for
collections, including counts of how many operations hold the critical section, 
how many are waiting, and how long they have waited.

**New in version:** 8.3

**`shardingStatistics.databaseVersionUpdateCounters`**

A document with counters that track updates to the sharding database
version, including information on how many sets, clears, access
changes, and durable changes have been made since the server started.

**New in version:** 8.3

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

**`shardingStatistics.resharding.countStarted`**

The sum of
`countSucceeded`,
`countFailed`,
and
`countCanceled`.
The sum is further incremented by `1` if a resharding
operation has started but has not yet
completed. Sum is set to 0 when `mongod` is started or
restarted.

*Only present when run on a shard or config server.*

**New in version:** 5.0

**`shardingStatistics.resharding.countSucceeded`**

Number of successful resharding operations. Number is set to 0 when `mongod`
is started or restarted.

*Only present when run on a shard or config server.*

**New in version:** 5.0

**`shardingStatistics.resharding.countFailed`**

Number of failed resharding operations.
Number is set to 0 when `mongod` is started or
restarted.

*Only present when run on a shard or config server.*

**New in version:** 5.0

**`shardingStatistics.resharding.countCanceled`**

Number of canceled resharding operations. Number is set to 0 when `mongod`
is started or restarted.

*Only present when run on a shard or config server.*

**New in version:** 5.0

**`shardingStatistics.resharding.active.documentsCopied`**

Number of documents copied from donor shards to recipient shards for
the current resharding operation. Number
is set to 0 when a new resharding operation starts.

*Only present when run on a shard or config server. Returns 0 on a
config server.*

**New in version:** 5.0

*Updated in version 6.1*

**`shardingStatistics.resharding.active.bytesCopied`**

Number of bytes copied from donor shards to recipient shards for the
current resharding operation. Number is
set to 0 when a new resharding operation starts.

*Only present when run on a shard or config server. Returns 0 on a
config server.*

**New in version:** 5.0

*Updated in version 6.1*

**`shardingStatistics.resharding.active.countWritesToStashCollections`**

During resharding, the number of writes to the recipient stash
collections.

**New in version:** 6.1

**`shardingStatistics.resharding.active.countWritesDuringCriticalSection`**

Number of writes perfomed in the critical section for the current
resharding operation. The critical
section prevents new incoming writes to the collection currently
being resharded. Number is set to 0 when a new resharding operation
starts.

*Only present when run on a shard or config server. Returns 0 on a
config server.*

**New in version:** 5.0

*Updated in version 6.1*

**`shardingStatistics.resharding.active.countReadsDuringCriticalSection`**

During resharding, the number of reads attempted during the donor's
critical section.

**New in version:** 6.1

**`shardingStatistics.resharding.active.oplogEntriesFetched`**

Number of entries fetched from the oplog for the current
resharding operation. Number is set to 0
when a new resharding operation starts.

*Only present when run on a shard or config server. Returns 0 on a
config server.*

*Updated in version 6.1*

**`shardingStatistics.resharding.active.oplogEntriesApplied`**

Number of entries applied to the oplog for the current
resharding operation. Number is set to 0
when a new resharding operation starts.

*Only present when run on a shard or config server. Returns 0 on a
config server.*

**New in version:** 5.0

*Updated in version 6.1* 

**`shardingStatistics.resharding.active.insertsApplied`**

The total number of insert operations applied during resharding.

**New in version:** 6.1

**`shardingStatistics.resharding.active.updatesApplied`**

The total number of update operations applied during resharding.

**New in version:** 6.1

**`shardingStatistics.resharding.active.deletesApplied`**

The total number of delete operations applied during resharding.

**New in version:** 6.1

**`shardingStatistics.resharding.oldestActive.coordinatorAllShardsHighestRemainingOperationTimeEstimatedMillis`**

Calculated across all shards, the highest estimate of the number of
seconds remaining. If the time estimate cannot be computed, the 
value is set to -1.

**New in version:** 6.1

**`shardingStatistics.resharding.oldestActive.coordinatorAllShardsLowestRemainingOperationTimeEstimatedMillis`**

Calculated across all shards, the lowest estimate of the number of
seconds remaining. If the time estimate cannot be computed, the 
value is set to -1.

**New in version:** 6.1

**`shardingStatistics.resharding.oldestActive.recipientRemainingOperationTimeEstimatedMillis`**

Estimated remaining time, in milliseconds, for the current resharding
operation. Prior to resharding, or when
the time cannot be calculated, the value is set to -1.

If a shard is involved in multiple resharding operations, this field
contains the remaining time estimate for the oldest resharding
operation where this shard is a recipient.

**New in version:** 6.1

**`shardingStatistics.resharding.oldestActive.totalOperationTimeElapsedMillis`**

Total elapsed time, in milliseconds, for the current resharding
operation. Time is set to 0 when a new
resharding operation starts.

*Only present when run on a shard or config server. Returns 0 on a
config server.*

**New in version:** 5.0

**`shardingStatistics.resharding.latencies`**

Timing metrics for resharding operations.

**New in version:** 6.1

**`shardingStatistics.resharding.latencies.collectionCloningTotalRemoteBatchRetrievalTimeMillis`**

Total time recipients spent retrieving batches of documents from
donors, in milliseconds.

**New in version:** 6.1

**`shardingStatistics.resharding.latencies.collectionCloningTotalRemoteBatchesRetrieved`**

Total number of batches of documents recipients retrieved from
donors.

**New in version:** 6.1

**`shardingStatistics.resharding.latencies.collectionCloningTotalLocalInsertTimeMillis`**

Total time recipients spent inserting batches of documents from
donors, in milliseconds.

**New in version:** 6.1

 

**`shardingStatistics.resharding.latencies.collectionCloningTotalLocalInserts`**

Total number of batches of documents from donors that recipients
inserted.

**New in version:** 6.1

   

**`shardingStatistics.resharding.latencies.oplogFetchingTotalRemoteBatchRetrievalTimeMillis`**

Total time recipients spent retrieving batches of oplog entries from
donors, in milliseconds.

**New in version:** 6.1

 

**`shardingStatistics.resharding.latencies.oplogFetchingTotalRemoteBatchesRetrieved`**

Total number of batches of oplog entries recipients retrieved from
donors.

**New in version:** 6.1

    

**`shardingStatistics.resharding.latencies.oplogFetchingTotalLocalInsertTimeMillis`**

Total time recipients spent inserting batches of oplog entries from
donors, in milliseconds.

**New in version:** 6.1

    

**`shardingStatistics.resharding.latencies.oplogFetchingTotalLocalInserts`**

Total number of batches of oplog entries from donors that recipients
inserted.

**New in version:** 6.1

    

**`shardingStatistics.resharding.latencies.oplogApplyingTotalLocalBatchRetrievalTimeMillis`**

Total time recipients spent retrieving batches of oplog entries that
were inserted during fetching, in milliseconds.

**New in version:** 6.1

    

**`shardingStatistics.resharding.latencies.oplogApplyingTotalLocalBatchesRetrieved`**

Total number of batches of oplog entries that were inserted during
fetching that recipients retrieved.

**New in version:** 6.1

    

**`shardingStatistics.resharding.latencies.oplogApplyingTotalLocalBatchApplyTimeMillis`**

Total time recipients spent applying batches of oplog entries, in
milliseconds.

**New in version:** 6.1

    

**`shardingStatistics.resharding.latencies.oplogApplyingTotalLocalBatchesApplied`**

Total number of batches of oplog entries that recipients applied.

**New in version:** 6.1

**`shardingStatistics.resharding.totalApplyTimeElapsedMillis`**

Total elapsed time, in milliseconds, for the apply step of the
current resharding operation. In the
apply step, recipient shards modify their data based on new incoming
writes from donor shards. Time is set to 0 when a new resharding
operation starts.

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
command is run, the following metrics increment.

| Name | Description |
|---|---|
| `allShards` | A command targeted all shards |
| `manyShards` | A command targeted more than one shard |
| `oneShard` | A command targeted one shard |
| `unsharded` | A command was run on an unsharded collection |

**Note:**

Running the `serverStatus` command on `mongos`
provides insight into the CRUD and aggregation operations that
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

**New in version:** 6.2

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
