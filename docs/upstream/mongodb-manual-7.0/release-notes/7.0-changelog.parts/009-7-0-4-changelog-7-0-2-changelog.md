<!-- Part 9 of 10 of release-notes/7.0-changelog.md (split because the page is big). -->

## 7.0.4 Changelog

### Sharding

- SERVER-82069 Throwable function used in scope guard when
  registering index
- SERVER-82364 Fix $config.transitions table for
  analyze_shard_key.js FSM workload

### Internals

- SERVER-67962 Applying config.image_collection deletes needs
  better concurrency control
- SERVER-69206 Coverity analysis defect 122738: Using a moved
  object
- SERVER-69244 $merge fails when session default read concern
  has been set to "majority"
- SERVER-72532 CommandNotFound: no such command: 'shardVersion'
- SERVER-75756 Check query presence in plan cache
- SERVER-77113 Exclude fields containing dots from time series
  indexes
- SERVER-79317 Provide more documentation and helper functions
  for case where feature flag checks could be run when FCV is
  uninitialized during initial sync
- SERVER-79470 Update shard-lite-audit infra provision for
  sysperf
- SERVER-79975 [Classic] Optimize large group keys
- SERVER-81028 Incorrect $listCatalog behavior in presence of a
  concurrent collection rename in v7.0
- SERVER-81133 Speedup logic to persist routing table cache
- SERVER-81295 Cannot resume V2 changeStream pipelines with V1
  resume tokens
- SERVER-81390 HashAggStage fails to respect the collation when
  spilling to disk
- SERVER-81435 Add metrics to capture impact of time series
  group commit
- SERVER-81456 Suppress leak sanitizer failures for AsioReactor
- SERVER-81467 Run Jepsen list-append in Evergreen
- SERVER-81524 No-op invocations of setUserWriteBlockMode must
  await majority confirmation of SystemLastOpTime
- SERVER-81581 Extend BlackDuck timeout
- SERVER-81605 cleanupOrphanedWhileMigrating.js  should not run
  on stepdown suites
- SERVER-81942 ShardingDDLCoordinator should retry on
  LockTimeout errors
- SERVER-82028 DDL operations on timeseries collection during
  tenant migration can crash the recipient due to an invariant failure.
- SERVER-82086 Add tsbs query workloads to sys perf
- SERVER-82156 Inconsistency between FLE insert and FLE update
  responses for retriedStmtIds
- SERVER-82178 Update references to
  ycsb_like_queryable_encrypt1_cfdefault_sharded in system_perf.yml
- SERVER-82204 Classic window functions first/last handle
  missing field incorrectly
- SERVER-82220 Avoid invariant during assertIsPrimaryShardForDb
- SERVER-82234 Relax assertions in session_pooling.js
- SERVER-82324 Fix data race when reading/writing the logical
  session id
- SERVER-82328 Concurrent access to
  MovePrimaryCoordinatorDocument without acquiring mutex
- SERVER-82410 DocumentSourceListSearchIndexes should hold
  owned copy of command object
- SERVER-82428 Include idle connections in currentOp aggregate
  cmd in fsync.js
- SERVER-82446 $densify use case can result in documents
  outside of range
- SERVER-82590 [7.0 Only] Feature Flag Upgrade/Downgrade
  Testing For Timeseries Arbitrary Deletes
- SERVER-82798 Respect time-series bucket minimum size when
  calculating bucket size limit
- SERVER-82799 Increase reshardingCriticalSectionTimeoutMillis
  for resharding_update_tag_zones.js
- SERVER-82803 CheckMetadataConsistency hook should ignore
  NetworkInterfaceExceededTimeLimit errors
- WT-11698 Re-enable HS verification in v7.0


## 7.0.3 Changelog

### Security

SERVER-77119 fle2_crud.js should use the same session to read
from encrypted/unencrypted collections

### Sharding

- SERVER-40459 Optimize the construction of the balancer's
  collection distribution status histogram
- SERVER-77479 Sharded rename participants may incorrectly
  snapshot/restore pending range deletion documents
- SERVER-79327 Missing verification in refine collection shard
  key
- SERVER-81241 Range deleter processor must not try reschedule
  task during service shutdown

### Build and Packaging

SERVER-80752 Increase windows AMI size to reduce chance of OOM

### Internals

- SERVER-62921 Improve sync source selection logging
- SERVER-66018 Expose metrics for readPreference usage
- SERVER-69244 $merge fails when session default read concern
  has been set to "majority"
- SERVER-69821 Fix underflow error in query memory tracking
- SERVER-71819 Broadcast collMod command to all shards
- SERVER-72687 Support for $out to Time-series collections
- SERVER-74061 Support $out for time-series on secondaries and
  sharded clusters
- SERVER-76341 Add range deletion throughput statistic
- SERVER-76626 Investigate test failures for concurrent $out
  and shardCollection commands
- SERVER-76789 Add immer to README.third_party.md
- SERVER-76912 Exclude
  migration_recovers_unfinished_migrations.js from config shard suites
- SERVER-77231 Platform Support: Add support for Debian 12
- SERVER-77506 Sharded multi-document transactions can mismatch
  data and ShardVersion
- SERVER-78009 shardSvrCommitReshardCollection command should
  fail recoverably if the node is shutting down
- SERVER-78091 Run publish_packages tasks on rhel 8.7 instead
  of rhel 8.0
- SERVER-78108 POS interface should expose its shutdown state
- SERVER-78115 Shard primaries must commit a majority write
  before using new routing information from the config server
- SERVER-78342 nReturned in slow query is incorrect when no
  docs are matched
- SERVER-78384 mongos should allow --port 0
- SERVER-78687 Set up copybara syncing between 10gen/mongo and
  10gen/mongo-copybara
- SERVER-78847 Search Index Management Commands Fail To Detect
  Collection on Other Shards
- SERVER-78851 movePrimary may fail on clone phase if $out runs
  concurrently
- SERVER-78854 CurOp::completeAndLogOperation waits on a ticket
  to acquire the GlobalLock
- SERVER-78952 Revert SERVER-78855 after SERVER-77506
- SERVER-79088 Improve SBE multi-planner performance for query
  which returns zero results
- SERVER-79251 Test dropping hashed shard key index mid chunk
  migration aborts migration
- SERVER-79335 Audit gFeatureFlagColumnstoreIndexes
- SERVER-79384 Allow startup with unavailable Issuer URI
- SERVER-79446 insert ignores collectionUUID for time-series
  collections
- SERVER-79471 Mirrored reads should include databaseVersion in
  addition to shardVersion
- SERVER-79585 A valid $match query fails on time-series
  collection
- SERVER-79632 Stop range deletion when hashed shard key index
  does not exist
- SERVER-79664 Handle TemporarilyUnavailableException in
  prepared transactions application
- SERVER-79779 AsyncResultsMerger leaks shard cursor when
  getMore fails due to not primary error
- SERVER-79781 TestGetDestinedRecipientThrowsOnBlockedRefresh
  should not run two refreshes without resetting the catalog cache
  loader mock return value
- SERVER-79926 Investigate OCSP failure possibilities
- SERVER-80001 Delist opCtx during ClientDisconnect during
  getMores
- SERVER-80021 Make $convert round-trip correctly between
  double and string
- SERVER-80157 ExclusionProjectionExecutor forces Document
  cache to load excluded fields
- SERVER-80203 Normalization of time-series meta field can
  break insert targeting
- SERVER-80270 Test new evergreen function var behavior
- SERVER-80279 Commit on non-existing transaction then proceed
  to continue can trigger an invariant
- SERVER-80358 Time-series inserts generate duplicate index
  fields in bucket document
- SERVER-80809 Make _logOplogEntriesForInvalidResults resilient
  to non-existing oplog
- SERVER-80886 $out may fail with a StaleDbVersion after a
  movePrimary
- SERVER-81033 Ignore the collMod response from the DBPrimary
  shard if it has no chunks
- SERVER-81041 Fix time-series collection compact locking
- SERVER-81044 Handle internal oplog update correctly in
  transactions
- SERVER-81055 $listSearchIndexes does not throw when used
  outside of atlas in 7.2 alpha releases
- SERVER-81106 Recipient shard doesn't wait for the collection
  version to be locally persisted before starting the cloning phase
- SERVER-81146 Use historic runtime data to set default
  timeouts when the data is not full
- SERVER-81149 Time-series update bucket compression failed due
  to decompression data loss
- SERVER-81155 Use move semantic to avoid copying all chunks in
  createCollection coordinator
- SERVER-81198 Fix last_lts entry in
  backports_required_for_multiversion_tests.yml file
- SERVER-81201 Limiting the memory usage during the cloning
  phase on the recipient shard
- SERVER-81202 Use host environment when signing
- SERVER-81203 Change
  featureFlagShardKeyIndexOptionalHashedSharding version to 7.0
- SERVER-81226 Deadlock between
  _commitSplitPreparedTxnOnPrimary and stepDown
- SERVER-81232 Skip RSTL lock acquisition in TimestampMonitor
  calls
- SERVER-81312 cannot import collection with hidden index
- SERVER-81318 The TimestampMonitor should be high priority and
  not take tickets
- SERVER-81332 Remove unnecessary log message in
  read_and_write_distribution.js
- SERVER-81393 Make multiversion-config resmoke command output
  yaml to file
- SERVER-81398 Make analyzeShardKey and query sampling take
  locks when looking up collection UUID
- SERVER-81427 Check feature flag is enabled on both shards
- SERVER-81431 Add canaries_only task to older mongo branches
- SERVER-81904 Address test-only issue in UpdateChunkMapRandom
  unit test
- SERVER-81939 Make configureQueryAnalyzer and analyzeShardKey
  command check that input namespace is correctly formatted
- SERVER-81966 Avoid modification of previous ChunkMap
  instances during refresh
- SERVER-81985 FlushRoutingTableCacheUpdates command should not
  be allowed on databases
- SERVER-82002 Fix no_selinux tagging in
  transaction_too_large_for_cache jstest
- SERVER-82003 powercycle tests are missing variables
- SERVER-82070 Classic window function $stdDevSamp handles
  empty window frame incorrectly
- SERVER-82272 [7.0] Remove benchmarks_orphaned stream tests
- WT-10809 MemorySanitizer: use-of-uninitialized-value in
  __wt_txn_commit
- WT-10972 Eliminate long periods of silence when recovering
  with recovery_progress verbose messages enabled
- WT-11491 Log the WiredTiger time spent during startup and
  shutdown
- WT-11564 Fix RTS to read the newest transaction value only
  when it exists in the checkpoint
- WT-11602 Hide expected eviction failures from the application
  and don't rollback in case of errors


## 7.0.2 Changelog

### Sharding

- SERVER-44422 Allow findAndModify and delete one to target by
  query instead of extracted shard key
- SERVER-75634 The logic in
  attachCursorSourceToPipelineForLocalRead performs shard versioning by
  UUID
- SERVER-78657 Get rid of
  getSplitCandidatesForSessionsCollection and
  minNumChunksForSessionsCollection
- SERVER-79086 Deletion of ReshardingCoordinatorService state
  document is not idempotent
- SERVER-79682 ShardsvrReshardCollection Can Hang If Stepdown
  Occurs Shortly After Stepping Up
- SERVER-79771 Make Resharding Operation Resilient to
  NetworkInterfaceExceededTimeLimit
- SERVER-80236 Race in migration source registration and
  capturing writes for xferMods for deletes
- SERVER-80246 Fsync test is not correctly checking for
  concurrent ddl operations
- SERVER-80463
  MigrationChunkClonerSourceOpObserver::onInserts() written to look like
  it skips checking some documents for whether their chunk has moved
- SERVER-80712 Avoid leaving the replica set shard partitioned
  at the end of linearizable_read_concern.js

### Operations

- SERVER-58534 Collect FCV in FTDC
- SERVER-77610 Log session id associated with the backup cursor

### Build and Packaging

WT-11302 failed: format-failure-configs-test on
ubuntu2004-arm64 with OOM [wiredtiger @ e298381e]

### Internals

- SERVER-50606 NetworkInterfaceTest needs to be more permissive
  with async op timeout
- SERVER-52149 Create feature flag for Make taking self-managed
  backups in 4.4+ as safe as possible
- SERVER-52452 Enable feature flag for Make taking self-managed
  backups in 4.4+ as safe as possible
- SERVER-68132 Remove Feature Flag for PM-2076
- SERVER-71520 Dump all thread stacks on RSTL acquisition
  timeout
- SERVER-73253 Better path tracking when renaming
  nested/compound grouping fields
- SERVER-73348 Aggregation bug in
  DocumentSourceSequentialDocumentCache
- SERVER-74893 Change default enumeration strategy for planning
  $or queries
- SERVER-74954 Incorrect result when contained $or rewrites
  $elemMatch extra condition
- SERVER-75255 Remove all outdated entries from
  backports_required_for_multiversion_tests.yml
- SERVER-75693 $vectorSearch Documentation Updates
- SERVER-76780 Robustify sparse_index_internal_expr.js and
  compound_wildcard_index_hiding.js test
- SERVER-76840 Filter oplog for query_oplogreplay collection
- SERVER-76932 Add a way for a thread to know when the
  SignalHandler thread is done with printAllThreadStacks
- SERVER-77134 Search queries hold storage tickets while
  waiting for response from network
- SERVER-77232 Platform Support: Remove support for Debian 10
- SERVER-77233 Platform Support: Remove support for Ubuntu
  18.04
- SERVER-77542 Internal operations should handle
  TemporarilyUnavailable and TransactionTooLargeForCache exceptions
- SERVER-77638 Add logging on completion of resharding
- SERVER-77677 Test or_to_in.js should run only in 7.0 and
  above.
- SERVER-77732 Create LTO variant
- SERVER-77862 Exclude compact.js from running in macos
  variants
- SERVER-77991 $$USER_ROLES not available within aggregation
  sub-pipeline
- SERVER-78149 Implement the mongos fsync (lock : true) command
- SERVER-78150 Implement the mongos fsyncUnlock command
- SERVER-78151 Add fsyncLock status to the mongos currentOp
  command
- SERVER-78153 Unlock the config server primary via the mongos
  fsyncUnlock command
- SERVER-78154 Detect on-going DDL operations in fsync with
  lock command
- SERVER-78156 Test the mongos fsync with lock command with
  distributed transactions
- SERVER-78159 Merge DocumentSourceInternalSearchMongotRemote
  and DocumentSourceInternalIdLookup into DocumentSourceSearch
- SERVER-78164 Make SBE eligible for DocumentSource with
  requiresInputDocSource = false
- SERVER-78217 Renaming view return wrong error on sharded
  cluster (2nd attempt)
- SERVER-78252 Block chunk migrations for hashed shard keys if
  you don’t have the shard key index
- SERVER-78253 Allow folks with hashed shard keys to drop the
  hashed index
- SERVER-78505 Database cache does not use the 'allowLocks'
  option correctly
- SERVER-78529 Create feature flag
- SERVER-78530 Enable feature flag
- SERVER-78650 Change stream oplog rewrite of $nor hits
  empty-array validation if no children are eligible for rewrite
- SERVER-78721 Remove multiversion compatibility for rename
  view test
- SERVER-78746 Enable feature flag in 7.0
- SERVER-78793 Add a timeout to the mongos FSync Lock Command
- SERVER-78831 Make $listSearchIndexes throw an Exception when
  used outside of Atlas
- SERVER-78848 $listSearchIndexes behavior should be consistent
  with other aggregations when the collection does not exist
- SERVER-78917 Relax condition in a router loop in
  shard_version_retry
- SERVER-78987 Remove the free monitoring code from
  mongodb/mongo repo
- SERVER-79025 Mongos Fsync with lock command should use mongos
  fsyncUnlock command
- SERVER-79045 Update yaml-cpp entry in README.third_party.md
  to 0.6.3
- SERVER-79046 The PreWriteFilter should be disabled if the
  mongod process is started with --shardsvr and in queryable backup mode
- SERVER-79054 Modify service_executor_bm to run an empty
  benchmark on ASAN
- SERVER-79236 Server cannot start in standalone if there are
  cluster parameters
- SERVER-79336 [Security] Audit v7.0 feature flag
- SERVER-79360 Avoid accessing OpDebug from other threads
- SERVER-79497 Backport $vectorSearch to 7.0
- SERVER-79552 $group rewrite for timeseries returns incorrect
  result if referencing the metaField in an object
- SERVER-79599 Geospatial Query Error on MongoDB Version 6.3.2
- SERVER-79780 ScopedCollectionDescription shouldn't hold a
  RangePreserver
- SERVER-79912 CheckReplDBHash reports failure with
  system.buckets collections due to invalid BSON
- SERVER-79958 Schedule the high-value workloads to run more
  regularly
- SERVER-79974 Time-series bucket change stream shardCollection
  events translate shardKey fields
- SERVER-79982 Batched catalog writers can run concurrently
  with  HistoricalCatalogIdTracker::cleanup() and lead to incorrect PIT
  find results.
- SERVER-80100 Fix typo in excluding
  compound_wildcard_index_hiding.js and sparse_index_internal_expr.js
- SERVER-80140 Use the $currentOp to verify that
  fsyncLockWorker threads are waiting for the lock
- SERVER-80234 Catalog cache unit tests of allowLocks should
  block the refresh
- SERVER-80302 capped_large_docs.js is not resilient to
  replication rollback
- SERVER-80465 Make numCandidates optional on mongod for
  $vectorSearch
- SERVER-80488 Avoid traversing routing table in balancer split
  chunk policy
- SERVER-80491 Expose more granular metrics around balancing
  round
- SERVER-80544 Fix incorrect wait in
  runSearchCommandWithRetries
- SERVER-80655 Reduce logging in release tasks
- SERVER-80678 Remove an outdated test case
- SERVER-80696 Fix How limit is calculated in
  $_internalSearchMongotRemote
- SERVER-80708 Increase the sys-perf 'Compile for Atlas-like'
  task size
- SERVER-80740 [7.0,7.1] Remove stream testing
- SERVER-80772 Stage builders generate invalid plan for simple
  project after sort query
- SERVER-80786 [7.0] Sharded time-series buckets should allow
  deleteOne against _id
- SERVER-80828 Disable configure_query_analyzer_persistence.js
  from the sharding_csrs_continuous_config_stepdown suite
- SERVER-80912 Enterprise RHEL 7.1 ppc64le failures on 6.0
  waterfall
- SERVER-80975 shardCollection(timeseriesNss) may accessed
  unititialised request parameters when invoked on a multiversion suite
- SERVER-81013 Fix resolveCollator to return 'kNo' when query
  has collator and collection does not
- SERVER-81031 Remove unowned RecordStore reference in WT
  RandomCursor class
- SERVER-81036 Fix the test entry in the
  backports_required_for_multiversion_tests.yml
- SERVER-81372 Collection defragmentation phases sporadically
  jump backward
- WT-10108 Add a data structure encapsulating user level
  truncate context
- WT-10786 Block checksum mismatch in bench-tiered-push-pull-s3
- WT-10873 failed: Unable to locate update associated with a
  prepared operation [wiredtiger @ 57bcfe46]
- WT-10927 Re enable HS verification
- WT-10987 Always log a truncate even if no work to do
- WT-10992 Implement testutil functions for directory copy and
  remove
- WT-11060 format failure: unable to locate update associated
  with a prepared operation
- WT-11168 Remove the page image reuse logic
- WT-11222 Fix run_format_configs to execute failed configs in
  parallel
- WT-11223 Prepare resolution diagnostic check reads freed
  update
- WT-11247 Reduce long-test format rows to limit disk usage
- WT-11280 Generation tracking might not be properly
  synchronized
- WT-11299 Fix run_format_configs.sh script to grep exact
  process id
- WT-11423 Unable to locate update associated with a prepared
  operation
- WT-11424 WT_CURSOR.search: timed out with prepare-conflict
- WT-11636 Disable Google SDK tiered test
- WT-11638 Fix prepared update resolution assertion
- WT-11684 Revert "WT-10927 Re-enable HS verification in
  mongodb-v7.0"
