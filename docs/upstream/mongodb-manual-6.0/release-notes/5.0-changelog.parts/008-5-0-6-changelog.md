<!-- Part 8 of 12 of release-notes/5.0-changelog.md (split because the page is big). -->

## 5.0.6 Changelog

### Sharding

- SERVER-45149 replSetStepDown command in txn_two_phase_commit_failover.js should not timeout
- SERVER-56127 Retryable update may execute more than once if chunk is migrated and shard key pattern uses nested fields
- SERVER-56227 Add user-facing command to set allowMigrations to false for a sharded collection
- SERVER-58622 DDL coordinator handle write concern error incorrectly when removing coordinator document
- SERVER-60624 txn_commit_optimizations_for_read_only_shards.js pauses replication on coordinator and can leave transaction stuck in prepare
- SERVER-60682 TransactionCoordinator may block acquiring WiredTiger write ticket to persist its decision, prolonging transactions being in the prepared state
- SERVER-60860 ReshardingCollectionCloner uses primary read preference when nearest was intended
- SERVER-61003 ReadConcernMajorityNotAvailableYet errors from ShardRegistry must be retried
- SERVER-61105 The sessions migration logic during moveChunk pollutes the logs
- SERVER-61268 Fixing the release of a recoverable critical section on secondaries
- SERVER-61416 Indefinitely retry errors in rename coordinator
- SERVER-61459 ShardingCatalogManager::assignKeyRangeToZone() reads stale version of CollectionType while running locally on config server primary
- SERVER-61461 update_shard_key_doc_moves_shards.js fails due to spurious refreshes from secondaries
- SERVER-61628 Do not reschedule range deletion task when numDeleted < numDocsToRemovePerBatch
- SERVER-61637 Review range deleter batching policy
- SERVER-61689 ActiveMigrationsRegistry::lock method doesn't properly handle its exceptions
- SERVER-61759 Unsetting the AllowMigrations flag should abort ongoing migrations
- SERVER-61816 cancel_coordinate_txn_commit_with_tickets_exhausted.js can hang forever due to race condition between transaction reaper and transaction coordinator
- SERVER-61945 Resharding collection cloning may fail with NamespaceNotSharded when "nearest" read preference chooses secondary
- SERVER-61950 ReshardingOplogFetcher waits on network request completing without interruption, potentially preventing shard step-up from ever completing
- SERVER-61976 [Resharding] Shards can error while refreshing their shard version following step-up, stalling the resharding operation
- SERVER-62065 Upgrade path from 3.6 to 4.0 can leave chunk entries without history on the shards
- SERVER-62171 Add logs to output of runConcurrentMoveChunk in sharding_statistics_server_status.js
- SERVER-62178 Resharding can fail with NamespaceNotSharded if recipient primary fails over before creating temporary resharding collection
- SERVER-62207 ReshardCollection with small maxTimeMS can crash the shard due to incorrect BSON object lifetime
- SERVER-62245 MigrationRecovery must not assume that only one migration needs to be recovered
- SERVER-62296 MoveChunk should recover any unfinished migration before starting a new one

### Replication

SERVER-59721 Node may become unable to sync from other members after performing rollback to stable timestamp

### Query

- SERVER-57588 Inconsistent query results when an array position is indexed whose value is an array
- SERVER-59754 Incorrect logging of queryHash/planCacheKey for operations that share the same $lookup shape
- SERVER-62147 Exhaust query using the OP_QUERY protocol is broken when more than one getMore batch is required

### Storage

- SERVER-30846 Run dbCheck as background workload in FSM tests
- SERVER-55483 Add a new startup parameter that skips verifying the table log settings
- SERVER-58409 Startup RecordId initialization is flawed with durable history and reconstructing prepared transactions

### Operations

SERVER-28953 Capture df (disk full) statistics in FTDC

### Internals

- SERVER-49748 Initial sync should clone admin.system.version before any other collections
- SERVER-54468 Enable Feature flag for Minimal support for sharding time-series collections
- SERVER-56167 Guarantee hang analyzer collects core dumps for sharded clusters, at minimum
- SERVER-57037 Improve precision of operator counters
- SERVER-57092 Use real test name for JS runner resmoke suites
- SERVER-57289 redact should not convert BSONArray into BSONObj
- SERVER-57312 Pin transitive Python dependencies and use the pinned file for installation in Evergreen
- SERVER-57772 Failpoints on mongos rewrite state change error codes in writeConcernError
- SERVER-58035 Remove db.runCommandWithMetadata from mongo shell
- SERVER-58135 ReplSetTest initiate failing in replica sets with chaining disabled
- SERVER-59428 Use more robust regex matching in rollback resumable index build fixture
- SERVER-59779 Call asCluster() before replSetFreeze in ReplSetTest
- SERVER-59781 multi_statement_transaction.js does not retry transaction on StaleConfig
- SERVER-60048 CheckReplDBHash should not fail for cases where we expect retryable findAndModify images to be inconsistent after a restart
- SERVER-60217 [v5.0] enableReconfigRollbackCommittedWritesCheck should be applied on 4.4
- SERVER-60310 OCSP response validation should not consider statuses of irrelevant certificates
- SERVER-60334 Pause the WiredTigerSizeStorer during Rollback To Stable
- SERVER-60392 Fix timing in priority_takeover_two_nodes_equal_priority test.
- SERVER-60513 Run burn_in_tags compile on -large distro
- SERVER-60517 Enforce eviction_dirty_target < eviction_dirty_trigger in the fuzzer
- SERVER-60685 TransactionCoordinator may interrupt locally executing update with non-Interruption error category, leading to server crash
- SERVER-60788 merge_causes_infinite_loop.js attempts to expose a problem that no longer exists
- SERVER-60809 Add ability to not idLookup after $search
- SERVER-60959 Insert to a Time-Series getting error collection ErrorCodes::TimeseriesBucketCleared
- SERVER-61005 rs.initiate() fails with "Invariant failure" under specific startup options
- SERVER-61012 Instantiation of TEMPLATE rule sometimes has a command in generated ninja
- SERVER-61097 SizeStorer can cause deadlocks with cache eviction
- SERVER-61121 Make TransactionMetricsObserver support TxnNumberAndRetryCounter
- SERVER-61122 Log TxnNumberAndRetryCounter in metrics and log methods inside TransactionParticipant and TransactionRouter
- SERVER-61188 When storeImageInSideCollection=true, pre-image noop entries for collection with preImageRecordingEnabledForCollection=true are assigned wrong opTimes
- SERVER-61194 Prevent time-series bucket OID reuse with coarse granularity
- SERVER-61201 Creating a view can lead to a deadlock
- SERVER-61214 Ensure having the latest known entry of the catalog cache when creating config.system.sessions
- SERVER-61216 The --cache-disable flag results in a python stacktrace
- SERVER-61275 Destruct the size storer after the session cache has shutdown
- SERVER-61307 Add context to parsing errors for $setWindowFields' partitionBy expression
- SERVER-61358 validate cachedir incorrectly re-raising InvalidChecksum 
- SERVER-61427 Unique index builds can cause a loss of availability during commit due to checking many false duplicates
- SERVER-61479 Increase the number of retries to connect to a replica set following a stepdown
- SERVER-61532 Opcounters to detect constrain violations need to be exposed.
- SERVER-61550 Modify auto_workload_path in perf.yml to be relative to cwd
- SERVER-61590 Presence of system.buckets collection should not assume that the collection is time-series collection.
- SERVER-61591 Robustify currentop_shell.js test
- SERVER-61602 timeseries_min_max.js assumes measurements are returned in insertion order
- SERVER-61650 Disconnect nodes before restarting replication in sync_source_selection_ignores_minvalid_after_rollback.js
- SERVER-61681 Wait for replSetGetStatus to update in replSetGetStatus_member_wall_times.js
- SERVER-61690 Adjust stored fields protocol for atlas search
- SERVER-61738 Revive dbCheck.js and make it deterministic
- SERVER-61743 The -fno-builtin-memcmp flag shouldn't be applied except on x86_64 platforms
- SERVER-61748 dbCheck should not hold a strong database lock during batches
- SERVER-61754 dbCheck should not hold a strong collection lock during batches
- SERVER-61757 Add a dbCheck command option to customize the batch size
- SERVER-61791 pin pymongo
- SERVER-61805 Use port to check primary node in timeseries_retryable_write_downgrade_oplog_rollover.js
- SERVER-61846 Prevent redact from throwing BSONObjectTooLarge
- SERVER-61852 dbCheck should tryLock the collection with backoff
- SERVER-61858 Wait for node to become primary before disconnecting in sync_source_selection_ignores_minvalid_after_rollback.js
- SERVER-61877 Remove catalog consistency verification from dbCheck
- SERVER-61883 [v5.0] Read support for compressed time-series buckets
- SERVER-61910 initiate_takes_stable_checkpoint.js doesn't account for closing connections in rollback
- SERVER-61931 Allow ClusterManager role to operate against system.buckets.* collections
- SERVER-61955 Expose dbCheck as a generally available command
- SERVER-62022 Reduce dbCheck info logging in production, log start and stop 
- SERVER-62023 Improve dbCheck observability
- SERVER-62037 Fix replica set definition in the system perf yaml file for linux-1-node-15gbwtcache
- SERVER-62041 Add a maximum batch execution time to dbCheck
- SERVER-62164 Remove several obsoleted build variants across all stable branches
- SERVER-62210 Fix dbCheck progress meter handling of dropped and recreated collections
- SERVER-62212 Support writeConcern for dbCheck
- SERVER-62226 Disable dbcheck_no_history_on_secondary.js on EFT
- SERVER-62243 Wait for vector clock document majority-commit without timeout
- SERVER-62277 Performance regression from dbstats due to occupied disk space calculation
- SERVER-62336 Tolerate SnapshotTooOld errors in dbCheck testing
- SERVER-62380 Wait for majority commit point to be advanced on each node before starting rollback test in rollback_set_fcv.js
- SERVER-62382 Several Amazon Linux 2 tests on the 5.0, 5.1, 5.2 and master waterfalls are not running
- SERVER-62419 recover_multiple_migrations_on_stepup.js fails when executed in config server stepdown suite
- SERVER-62423 Fix replsetinitiate_works_with_keyfile_profile_verbose_options.js to work on ephemeralForTest
- SERVER-62592 Make timeseries_sharding_admin_commands.js clearJumboFlag test more resilient
- SERVER-62706 dbcheck.js: handle replica sets with mixed debug/release members
- WT-8395 Inconsistent data after upgrade from 4.4.3 and 4.4.4 to 4.4.8+ and 5.0.2+
- WT-8534 Allow retrieving checkpoint snapshot for backup restore recovery
- WT-8576 Enable logging in test checkpoint
