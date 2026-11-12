<!-- Part 7 of 10 of release-notes/7.0-changelog.md (split because the page is big). -->

## 7.0.9 Changelog

### Sharding

SERVER-89134 Test wrongly assumes multi writes outside of
transactions are atomic 

### Write Operations

SERVER-88200 Time-series writes on manually-created buckets may
misbehave

### Storage

SERVER-30832 Fix dbCheck behavior on rollback

#### WiredTiger

- WT-10807 Skip in-memory deleted pages as part of the tree
  walk
- WT-11911 Fix use-after-free with bounded cursor and
  search_near

### Internals

- SERVER-65974 Replace HistoricalIdentTracker with checkpoint
  cursors
- SERVER-74931 Add AtomicWord::storeRelaxed
- SERVER-76001 Add serverStatus metrics for
  PeriodicThreadToAbortExpiredTransactions
- SERVER-76534 Fix reporting the namespace and UUID in a backup
  cursor when the changes have not yet been checkpointed
- SERVER-77427 Avoid going through the network when a shard is
  targeting only itself for a $lookup subpipeline
- SERVER-77530 Join the mirroring executor on shutdown
- SERVER-79049 Server returns unexpected CollectionUUIDMismatch
  with actual collection name equal to expected collection name
- SERVER-79637 Incorrect query results in $lookup with TS
  foreign collection using a correlated predicate
- SERVER-79774 Emit warning when balancing disabled for
  collections with chunks on draining shard
- SERVER-80194 In sharded_agg_helpers.cpp we retrieve
  CollectionRoutingInfo without checking for transaction
- SERVER-80340 Handle and test dbCheck during initial sync
- SERVER-80341 sharded_agg_helpers::attachCursorToPipeline
  should not attach dbVersion when targeting local shard by routing
  table
- SERVER-81807 Cached SBE plans have let-bound constants baked
  in
- SERVER-82349 Mongo 7 crashes on applyOps index delete/drops
  without a collection UUID
- SERVER-82571 insert_with_data_size_aware_balancing.js may
  occasionally fail when run against slow machine/variants
- SERVER-82717 QueryPlannerIXSelect::stripInvalidAssignments
  tries to strip non-existent index assignment from
  $_internalSchemaAllElemMatchFromIndex
- SERVER-83193 Replace deprecated BatchedCommandRequest
  getters/setters for WC with the ones provided by OperationContext
- SERVER-83370 PrepareUnique:true for time-series collections
  should error
- SERVER-83984 WiredTiger verbosity level is suppressed
- SERVER-84440 Expose the number of replication waiters in
  serverStatus
- SERVER-84653 Make the auto_safe_reconfig_helper tests wait
  for newly added removal
- SERVER-84717 [SBE] Fix buildGroup() to tolerate multiple
  output fields with the same name
- SERVER-85681 Fix for negative value being passed to
  BasicBufBuilder::grow()
- SERVER-85694 $searchMeta aggregation pipeline stage not
  passing correct query to mongot after PlanShardedSearch
- SERVER-85969 Documentation Updates
- SERVER-86201 Cluster upserts performed through the
  ShardServerProcessInterface should use the operation context to
  configure their write concern
- SERVER-86253 Add serverstatus to record how many users use
  retryable writes
- SERVER-86327 Time-series single schema per bucket column is
  not maintained in some cases
- SERVER-86375 Make index_build_memory_tracking.js less strict
- SERVER-86380 Allow for multiple IdP configurations with the
  same issuer but unique issuer-audience pair
- SERVER-86407 validation does not produce complete results
  when it should
- SERVER-86419 SBE and Classic behave differently for
  $bitsAnyClear on NumberDecimal infinity
- SERVER-86474 $_internalApplyOplogUpdate with $set: { foo:
  Timestamp(0, 0) } is not replicated correctly
- SERVER-86478 Time-series bucket min/max does not track empty
  field names under certain circumstances
- SERVER-86529 Re-enable powercycle tests in Evergreen
- SERVER-86640 Refactor out JWKS refresh from IdentityProvider
  into a IDPJWKSRefresher
- SERVER-86642 Update IDP registration selection process
- SERVER-86648 Resumable index build sorter files are not
  fsynced on shutdown
- SERVER-86987 Ensure check_metadata_consistency.js use
  retriable writes when contacting config server
- SERVER-87032 Query Stats appear not to be collected for
  whole-db and whole-cluster change streams
- SERVER-87306 Prevent accessing OCSP manager ptr during
  shutdown
- SERVER-87379 Cache the value of CanonicalQuery::toStringShort
  in PrepareExecutionHelper
- SERVER-87521 Fix race in BackgroundSync between making
  RollbackImpl and shutdown
- SERVER-87537 Make InternalSearchMongotRemoteSpec not strict
- SERVER-87573 Allow token_endpoint to be optional in OpenID
  Discovery Document
- SERVER-87845 Fix watchdog unit test PauseAndResume timeout
  issue
- SERVER-87905 BSONColumn validation integer overflow
- SERVER-87930 Unittest CaptureLogs utility allows
  unsynchronized access to log statements
- SERVER-87987 Timeseries optimization does not exclude the
  timeField though it's renamed by the $addFields and excluded by a
  project
- SERVER-88017 Resolve lock-order-inversion TSAN error in
  TimestampKVEngineTest
- SERVER-88034 Fix powercycle task configurations
- SERVER-88063 Add RetryableWriteError label when write
  operation fails with StaleConfig and is direct to shard
- SERVER-88097 Add the --release flag to the sys-perf compiles
- SERVER-88136 Fix arbiter_always_has_latest_fcv.js test to
  correctly test arbiter FCV behavior
- SERVER-88173 BinData bit comparisons give wrong results in
  many cases
- SERVER-88202 Fix possible integer overflow in BSON validation
- SERVER-88262 Prevent timeouts in
  read_pref_with_hedging_mode.js
- SERVER-88296 $group constant expression fails to re-parse
- SERVER-88328 Namespace may become unavailable while sharding
  collection during downgrade from v7.2 to v7.0
- SERVER-88404 checkMetadataConsistency should refresh if it
  finds no cached info for database
- SERVER-88650 Deadlock in VectorClockMongoD during shutdown
- SERVER-88676 Backport build_patch_id functionality to 7.0
- SERVER-88755 Make sure all sys-perf build variants specify a
  mongodb_setup_release
- SERVER-88779 FLE2 retryable write breaks if an internal
  transaction is retried
- SERVER-88833 mongos generates a reply for writes sent by
  client with w:0
- SERVER-88864 Make
  nodes_eventually_sync_from_closer_data_center.js more robust to
  transient slow heartbeat issues
- SERVER-88942 Update db-contrib-tool version that includes fix
  for downloading old binaries
- SERVER-89026 Remove bench_test_with_tenants.js on v7.0
- SERVER-89067 Invalidate all user requests matching a user
  name
- SERVER-89068 Explicitly set exec_timeout and timeout_secs for
  the sys-perf project
- SERVER-89076
  test_resharding_test_fixture_shutdown_retry_needed does not handle
  SnapshotUnavailable errors
- SERVER-89235 internal_strip_invalid_assignment.js missing tag
- SERVER-89251 Revert concurrent movePrimary and aggregations
  test from v7.0 and v6.0
- SERVER-89253 Make re-using compiled binaries in scons compile
  script more resilient
- SERVER-89402 insert_with_data_size_aware_balancing.js is
  incompatible with test suites killing/terminating the CSRS primary
- SERVER-89414 Harden shard removal in a
  store_historical_placement_data.js test teardown
- SERVER-89554 Fix evergreen/compiled_binaries_get.sh script
- WT-11532 Fix session reset RNG by using cursor RNG
- WT-12225 Fix RNG generator weakness around mongodb $sample
  stage


## 7.0.8 Changelog

### Internals

- SERVER-75845 Catch InterruptedDueToStorageChange in parallel
  shell for fcbis_election_during_storage_change.js
- SERVER-77559 Implement file system log handler for resmoke
- SERVER-77737 $top/$bottom gives incorrect result for sharded
  collection and constant expressions
- SERVER-78556 Return default of internalInsertMaxBatchSize to
  64
- SERVER-78832 AutoGetCollectionForReadLockFree constructor
  should check the shard version when setting shard key
- SERVER-78852 Test movePrimary and $out running concurrently
- SERVER-79575 Fix numa node counting
- SERVER-79999 reduce test code coverage on macos builders
- SERVER-81108 Sharded $search fails tassert in writeQueryStats
- SERVER-83422 Remove explain from AggQueryShape
- SERVER-84179 Simple8b builder does not fully reset state
  after writing RLE block
- SERVER-84530 Add query stats key hash to output of
  $queryStats
- SERVER-85580 Undo any update on ScopedSetShardRole
  construction failure
- SERVER-85721 Point evergreen task log lobster links to
  Parsley
- SERVER-85799
  rollback_recovery_commit_transaction_before_stable_timestamp should
  wait for system to stablize before disabling failpoint
- SERVER-86021 [v7.0] 7.0 backport testing audit
- SERVER-86583 Non-transactional snapshot read on unsharded
  collection may execute with mismatched sharding metadata
- SERVER-86622 Resharding coordinator use possibly stale
  database info
- SERVER-86672 CollMod coordinator use possibly stale database
  information
- SERVER-86774 Increase oplog size for PIT (point in time
  restore) tests
- SERVER-86782 geo_axis_aligned.js takes too long
- SERVER-86798 deny list validate_db_metadata_command.js from
  tenant migrations suite
- SERVER-86965 [v7.0] Enable query stats for $search in 7.0
- SERVER-87058 Chunk refresh from a secondary does not wait for
  majority writeConcern while flushing
- SERVER-87081 query stats for sharded search on v7.0
- SERVER-87166 [v7.0] Fix collation_bucket.js for query_stats
  on 7.0
- SERVER-87323 Future continuations must capture vector clock
  as shared pointer
- SERVER-87610 Relax shardVersionRetry tripwires on the
  namespace of received stale exceptions
- SERVER-87616 Create minimal trySbeEngine build variant on
  release configurations which have SBE
- SERVER-87666 Query shape for $documents is unique on each
  execution
- SERVER-87982 Rename the THP_enabled field in the ftdc
  systemMetrics status section
- SERVER-88111 random_DDL_CRUD_operations.js bulk insert should
  perform max internalInsertMaxBatchSize inserts
- SERVER-88360 Remove "Sharding catalog and local catalog
  collection uuid do not match" tripwire assertion


## 7.0.7 Changelog

### Sharding

SERVER-84368 CreateIndex fails with StaleConfig if run from a
stale mongos against a sharded non-empty collection

### Query

SERVER-83602 $or -> $in MatchExpression rewrite should not
generate $or directly nested in another $or

### Aggregation

SERVER-87313 [v7.0] [SBE] Aggregate command hits tripwire
assertion in SortStage::SortImpl::runLimitCode()

### Build and Packaging

WT-11407 Fix test_txn24 test (not WiredTiger) to stop
WT_ROLLBACK errors on MacOS

### Internals

- SERVER-70672 Merge enterprise repo into 10gen/mongo
- SERVER-72431 Make the commit of split chunks idempotent
- SERVER-76700 Increase window of acceptable elapsed CPU times
  in OperationCPUTimerTest::TestReset
- SERVER-79285 makeOperationContext should not be called on the
  primaryOnlyService instance cleanup executor
- SERVER-79999 reduce test code coverage on macos builders
- SERVER-80177 validate() should not return valid:false for
  non-compliant documents
- SERVER-83501 Write script to generate a file of all available
  server parameters for sys-perf runs
- SERVER-83508 Race between watchdog and FCBIS deleting old
  storage files
- SERVER-83956 Balancer wrongly emit warning message in
  multiversion clusters
- SERVER-84008 Enable query stats sys-perf variants on 7.0
- SERVER-84123 Add versioning to BSON validation
- SERVER-84125 Check fieldname size in BSONColumn validation
- SERVER-84179 Simple8b builder does not fully reset state
  after writing RLE block
- SERVER-84240 Make replSetReconfig retry network errors
- SERVER-84589 Error when directly dropping a sharded
  time-series buckets collection is misleading.
- SERVER-84612 Define a version for immer
- SERVER-84615 Define a version for linenoise
- SERVER-84628 Startup warning in mongos for Read/Write Concern
- SERVER-85318 Change expireAfterSeconds in
  timeseries_out_non_sharded.js
- SERVER-85459 [v7.0] bucketRoundingSeconds param is accepted
  by nodes on FCV 6.0, binary 7.0
- SERVER-85534 Checkpoint the vector clock after committing
  shard collection
- SERVER-85690 Wait for stepdown to finish before continuing
  index build in index_build_unregisters_after_stepdown.js
- SERVER-85716 Fix for empty buffer being passed to BSONColumn
  validation
- SERVER-85843 A write operation may fail with
  NamespaceNotFound if the database has been concurrently dropped
  (sharding-only)
- SERVER-85869 Exhaustive find on config shard can return stale
  data
- SERVER-85973 Update README.third_party.md to indicate that
  Valgrind is licensed under BSD-4-Clause
- SERVER-86021 7.0 backport testing audit
- SERVER-86065 BSONColumn structural validation should check
  for nested interleaved mode
- SERVER-86106 shadow-utils is not on suse
- SERVER-86158 change fail point used in TTL operation metrics
  tests
- SERVER-86273 $search should set protocol version and search
  sequence token in establishSearchCursors
- SERVER-86355 recoverRefreshDbVersion is swallowing errors
- SERVER-86395 Investigate DuplicateKey error while recovering
  convertToCapped from stable checkpoint
- SERVER-86399 Ensure that FTDC tracks information related to
  systems that could be running the new allocator
- SERVER-86403 Fix THP startup warnings
- SERVER-86417 Change $vectorSearch filter to owned obj
- SERVER-86424 $facet should be able to generate documents with
  searchSequenceToken
- SERVER-86433 Clear memory in the data_union stored on the
  endpoint before use
- SERVER-86452 [v7.0] make v7.0 fle variant closer to master
- SERVER-86454 Merge canSwapWithRedact and
  canSwapWithSingleDocTransform constraints
- SERVER-86481 Jepsen set, register, and read concern majority
  tests are not running in Evergreen
- SERVER-86523 Backport Query Stats to 7.0 Batch #5
- SERVER-86607 Reject access tokens with multiple audience
  claims
- SERVER-86619 Document::shouldSkipDeleted() accesses string
  without checking for missingg
- SERVER-86620 [v7.0] Backport script for sys-perf parameters
- SERVER-86622 Resharding coordinator use possibly stale
  database info
- SERVER-86624 Make RSLocalClient also wait for a snapshot to
  be available
- SERVER-86632 plan_cache_drop_database.js should catch
  DatabaseDropPending errors
- SERVER-86634 A collection that ends with ecoc.compact must be
  considered a FLE collection
- SERVER-86646 Fix decodeRecordIdStrAtEnd handling of
  unterminated size bytes
- SERVER-86652 Query Stats 7.0 Backport Batch #6
- SERVER-86698 Add query stats passthroughs to
  evergreen_nightly for 7.0
- SERVER-86700 [7.X] Fix timeseries_agg_out.js not expecting
  NamespaceNotFound error
- SERVER-86705 moveChunk op slower than TTL index in
  ttl_deletes_not_targeting_orphaned_documents.js
- SERVER-86717 Resharding should validate user provided zone
  range doesn't include $-prefixed fields.
- SERVER-86772 Fix racy watchdog_test
- SERVER-86822 remove sharding_gen from macOS builders
- SERVER-86840 fix gather unittest script to handle split
  unittests tasks
- SERVER-86841 Fix test setup for shapifying_bm.cpp on 7.0
  branch
- SERVER-86876 Disable diagnostic latches for sys-perf variants
  on 7.0
- SERVER-86889 Fix idl_check_compability.py to consider edge
  cases
- SERVER-86903 Backport QS to 7.0 Batch #7
- SERVER-87061 Sharded multi-document transactions can observe
  partial effects of concurrent reshard operation
- SERVER-87130 Backport Query Stats to 7.0 Batch #8
- SERVER-87177 Modify tests in expression_test.cpp to not use
  $getFields.
- SERVER-87330 Accept JWKSets with non-RSA keys
- SERVER-87394 [v7.0] Explore fixes for broken debian11 package
- SERVER-87415 Remove run_command__simple workload from
  sys-perf
- SERVER-87479 Manually run SBE build variants on release
  branches in evergreen to generate and add SBE $group/$lookup tests
  with $skip/$limit prefixes
- SERVER-87544 Fix up gitignore to permit git awareness of
  enterprise module
- SERVER-87557 Exclude some FF tests from an invalid build
  variant
- SERVER-87567 The SessionWorkflow  should correctly return a
  response error on malformed requests
- SERVER-87600 Delete older variants from system_perf.yml
- SERVER-87612 Backport Query Stats to 7.0 Batch #9
- WT-10178 Fix timing stress causing format to time out with
  prepare-conflict
- WT-11239 Add CLANG_C/CXX_VERSION compile flags to the
  configure wiredtiger task
- WT-11325 Missing keys in schema-abort-predictable-test
- WT-12304 RTS should provide information about how much more
  work it has to do
- WT-12321 Add stat to track how many bulk cursors are opened
- WT-12402 Add stats to track when eviction server skips
  walking a tree
