<!-- Part 5 of 10 of release-notes/7.0-changelog.md (split because the page is big). -->

## 7.0.14 Changelog

### Internals

- SERVER-93205 Expose number of prepareUnique indexes in
  serverStatus
- SERVER-93224 drop_database_before_write_is_targeted.js is not
  compatible with config stepdown suites
- SERVER-93326 Add retries to cloneing jstestfuzz.git
- SERVER-93578  [v7.0] Revert "SERVER-92273 ListCollections
  without filter should include commit pending namespaces (7.0 only)"
- SERVER-79766 TransactionRouter ignores atClusterTime setting
  in the request
- SERVER-80315 grouped_match_push_down.js wrong assert on
  getStageSequence() result
- SERVER-80661 Sandbox background test activity
- SERVER-82476 Disable diagnostics latches by default
- SERVER-82551 Use parallel compressor to speedup binaries
  archival
- SERVER-82814 Support internal expr comparison operators when
  determining clustered collection scan bounds
- SERVER-84045 Ensure that the PlanExecutor remains in scope
  while accessing the shard key index in AutoSplitVector
- SERVER-84531 Inserting mixed-schema buckets through the
  system.buckets collection doesn't set the
  timeseriesBucketsMayHaveMixedSchemaData flag
- SERVER-84625 Fix data race on MigrationSourceManager
- SERVER-84699 Add a check to validation to check for
  mixed-schema buckets for time-series
- SERVER-85384 Remove aliases post branch
- SERVER-85892 $merge with pipeline after $documents returns
  error
- SERVER-86669 Invalid authoritative knowledge on secondary
  node after move primary locally creates the collection on the primary
  shard
- SERVER-86879 `concurrency_replication*` tasks are not running
  on the UBSan DEBUG build variant
- SERVER-87760 add an amazon linux x86 variant to
  mongodb-mongo-master evergreen project
- SERVER-87961 Time series $group rewrite may produce incorrect
  results when a preceding $project stage projects out accessed fields
- SERVER-88255 Sys-perf: Replace mongotools compilation with
  the download of a static artifact
- SERVER-88439 Use after free in DocumentSourceLookup::clone
- SERVER-88530 BF setup script for C++ unit tests doesn't set
  up unit test binary/debug symbols
- SERVER-88750 Add "bypassEmptyTsReplacement" param to insert,
  update, findAndModify, and bulkWrite
- SERVER-88811 Parsing oplog entries before the stable
  timestamp can fail
- SERVER-89391 Increase timeoutMS in
  exhaust_hello_topology_changes.js
- SERVER-89727 Remove acquisition of database and collection
  locks in compaction
- SERVER-89748 Retry _flushRoutingTableCacheUpdates command if
  it fails in retry_on_transient_error_basic.js
- SERVER-89769 Test is not waiting for journal flusher before
  checkpointing
- SERVER-89844 Make $jsonSchema with dollar fields in all
  keyword fields reparseable
- SERVER-89861 include decoded length in invalid nested bson
  validation error message
- SERVER-89890 Fix
  assertRetryableCommandWorkedOrFailedWithCodes
- SERVER-90147 Upgrade timelib.h to 2022.10 and timezone files
  to 2024a
- SERVER-90330 Creation of DDL coordinator hang indefinetly if
  executed on secondary node
- SERVER-90352 AsioNetworkBaton::detachImpl doesn't clear the
  _timersById map
- SERVER-90391 Clarify headers and readme
- SERVER-90625 QueryStats for sum of squares execution time
  overflows its int64_t
- SERVER-90727 Fix analyze_shard_key.js to ignore errors
  related to readConcern: available
- SERVER-90790 Add debugging code for CommonAsioSession
  constructor
- SERVER-90825 Add README explaining compliance for
  src/third_party
- SERVER-90845 update idxEntryBytesWritten check
  index_build_operation_metrics.js to account for write conflicts
- SERVER-90958 $bucketAuto should group documents with same
  grouping keys in the same bucket
- SERVER-90984 Fix exhaust hello stream to process
  SplitHorizonChange if response is from stale horizon.
- SERVER-90995 Shadowing metaField should not be considered as
  a "computed" meta field
- SERVER-91067 Skip
  setMinVisibleForAllCollectionsToOldestOnStartup code during rollback
- SERVER-91108 Log with utf-8 encoding to avoid charmap errors
  on Windows
- SERVER-91159 Delay FTDC-on-arbiter log spam filtering until
  the node knows it's an arbiter.
- SERVER-91195 Provide a generic backportable solution not to
  miss top-level timeseries collection options
- SERVER-91223 $log gives incorrect calculation with Decimal128
- SERVER-91247 Ensure that DDLCoordinator creation does not
  survive node stepDown-stepUp
- SERVER-91254 Error when deciding whether documents are inside
  a window in classic
- SERVER-91257 Set build team as owner of linenoise in the sbom
- SERVER-91258 Increase oplog size in
  change_streams_split_event tests
- SERVER-91312 Report metrics about temporary record stores and
  external files used for query spilling
- SERVER-91336 Temporary C++ objects in an expression is short
  lived
- SERVER-91339 $redact may corrupt memory if $$ROOT is used in
  the expression.
- SERVER-91352 Do not check for the no-op entry in
  readConcern_atClusterTime_noop_write.js
- SERVER-91366 Fix possible crash in coordinator completion
- SERVER-91390 Collection validation memory needed calculation
  can overflow
- SERVER-91406 $changeStreamSplitLargeEvent returns
  Location7182803 error when used with non-renameable match expression
- SERVER-91412 Unowned BSONObj use in splitVector
- SERVER-91499 Append "-sysperf" to mongo version in sys-perf.
- SERVER-91566 Suppress checkIndexesConsistentAcrossCluster in
  index_operations_abort_concurrent_outgoing_migrations.js
- SERVER-91573 $match pushed before $addFields can lead to
  incorrect results
- SERVER-91625 [v7.0] Enable indexed plans for expressions with
  $$NOW, $$CLUSTER_TIME and $$USER_ROLES
- SERVER-91630 configsvr_remove_chunks.js should use retriable
  writes when writing to the config server
- SERVER-91680 Disable test case on
  concurrent_drops_and_create.js on v6.0 multiversion
- SERVER-91699 Subtracted memory greater than the total memory
- SERVER-91701 Robustify
  max_time_ms_does_not_leak_shard_cursor.js test
- SERVER-91703 Disable PeriodicShardedIndexConsistencyChecker
  during read_committed_lookup.js
- SERVER-91728 Fix a bad merge in backport-21214
- SERVER-91758 mongos_rs_shard_failure_tolerance.js should
  retry NetworkInterfaceTimeLimitExceeded for a sharded find command on
  versions earlier than 8.0
- SERVER-91778 Do not close cursor in the shell when cursor
  reaches limit
- SERVER-91781 Wait for replication in
  merge_let_params_size_estimation.js
- SERVER-91784 $project-$addFields on arrays can produce
  incorrect results
- SERVER-91787 Assign Cyrus SASL to "Build" team
- SERVER-91793 Exclude backports touching only
  `etc/*suppressions` files from release codeownership
- SERVER-91817 Make analyze_shard_key.js workload more robust
- SERVER-91818
  resharding_coordinator_recovers_abort_decision.js Should Be More
  Insistent When Stepping Up New Primary
- SERVER-91831 uassert in NetworkInterfaceTL::setTimer can
  crash the server
- SERVER-91859 analyze_shard_key_jscore_passthrough fails when
  it encounters CommandOnShardedViewNotSupportedOnMongod errors
- SERVER-91894 Fix views_basic.js to reference correct database
  name
- SERVER-91919
  change_stream_pit_pre_image_deletion_asymmetric.js can use excessive
  amount of memory
- SERVER-91938 Make read_and_write_distribution.js and
  analyze_shard_key.js in 7.0 not perform updateOne and removeOne
  without shard key
- SERVER-91940 Remove all ignored files from server
  evergreen.yml
- SERVER-91969 Test initial sync with mixed-schema time-series
  buckets
- SERVER-91970 Wait for overlapping range deletion tasks to be
  cleared up on the donor side before starting a migration
- SERVER-91985 Fix race in
  egress_connection_acquisition_to_wire_metrics.js
- SERVER-91993 [v7.0] Fix now_variable.js in classic engine
- SERVER-92021 fix mongotmock or write kill_cursors.js with
  real mongot
- SERVER-92030 Upgrade mongo-c-driver (libbson) version in
  SERVER to 1.27.1
- SERVER-92045 Mixed-schema time-series bucket validation check
  does not set valid flag on error
- SERVER-92085 Skip tailable cursor invalidation test for
  config fuzzer
- SERVER-92086 Time-series mixed-schema buckets tests can
  incorrectly try to validate that no buckets are uncompressed
- SERVER-92145 The balancer settings refresh can overwrite
  newer config
- SERVER-92158 Disable hedged_reads.js on windows variants
- SERVER-92160 Increase average task setup time constant for
  timeout calculations
- SERVER-92183 Mongod crashes when running aggregation
- SERVER-92186 Implement simple API to get/set app_metadata
  from/to wiredtiger config strings
- SERVER-92193 Index Bounds Builder tries to build geo bounds
  using non-geo index
- SERVER-92199 Ban change_stream_lookup_single_shard_cluster.js
  from stepdown suites
- SERVER-92201 currentop_shell.js may not wait long enough for
  all shards to be ready in sharded collection passthroughs
- SERVER-92231 [v7.0] Enable the bucket unpacker to read v3
  buckets and treat them as v2 buckets
- SERVER-92233 Await replication after collection creation in
  text_search_index_commands.js
- SERVER-92247 Exclude internal elemMatch types from
  computeWhetherMatchOnAs
- SERVER-92273 ListCollections has inconsistent behavior for
  commit pending namespaces (7.0 only)
- SERVER-92298 Remove unused ProjectionPathASTNode argument to
  speed up $project aggregation requests
- SERVER-92375 Remove minor version from rhel8.x variant names
- SERVER-92376 update suse15 package test container to sp5
- SERVER-92377 Clean up the system_perf.yml configuration
- SERVER-92379 Reuse the mongodb-mongo-master compile for the
  mongocrypt library
- SERVER-92381 Ensure MigrationSourceManager fulfills its
  promise when aborting in early stages
- SERVER-92382 Updating a prepareUnique index does not check
  whether constraints are being enforced
- SERVER-92389 Make a new shared_ptr to avoid use after free
- SERVER-92395 Do not push down group to SBE if it has SBE
  incompatible expressions
- SERVER-92402 read_and_write_distribution.js is racy
- SERVER-92414 [v7.0] Tag enterprise-rhel-83-s390x with
  --excludeWithAnyTags=resource_intensive
- SERVER-92415 Bump db-contrib-tool version to v0.8.3
- SERVER-92426 Adapt tests to rely on new
  timeseriesBucketsMayHaveMixedSchemaData catalog option format
- SERVER-92516 Remove openssl111 buildvariants
- SERVER-92547 Use the old rhel80 variant name on v4.2 and v4.4
  multiversion tests
- SERVER-92556 fsync.js is non-deterministic due to ticket
  exhaustion
- SERVER-92562 Update sbom version to its branch
- SERVER-92601 Remove the package_new_compile task
- SERVER-92603 Or-to-in rewrite does not always avoid rewriting
  parameterized expressions
- SERVER-92612 set cache dir for pip installs in evergreen
- SERVER-92623 Pin the version of v5.0 to 5.0.28 in
  timeseries_collection_mixed_type.js
- SERVER-92660 Ensure consistent validations in
  all_collection_stats.js by eventually comparing $collStats and
  $_internalAllCollectionStats
- SERVER-92663 Temporary disable lint_sbom
- SERVER-92682 change sbom_linter to use local schema
- SERVER-92694 restart_during_downgrading_fcv.js isn't waiting
  for the shards to agree on a primary
- SERVER-92736 Update symbol mapper to use the original
  executed task
- SERVER-92777 Fix the URL components for the RHEL8 artifact
- SERVER-92812 Get rid of
  gCollModTimeseriesBucketsMayHaveMixedSchemaData feature flag
- SERVER-92842 Suppress assertion in
  store_historical_placement_data.js
- SERVER-92899 [7.0] Fix indexbg_killop_secondary.js error code
- SERVER-92902 Fix overflow issue when casting numInitialChunks
  from size_t to int
- SERVER-92927 Add rhel8 key to package_test.py docker dict
- SERVER-92939 Route tools download to the newest rhel version
- SERVER-92974 Ensure that valid THP parameter modes don't trip
  a startup warning.
- SERVER-92986 Make
  resharding_coordinator_recovers_abort_decision.js wait for election
- SERVER-93014 Setting locally
  timeseriesBucketsMayHaveMixedSchemaData during MultiIndexBlock::commit
  might generate catalog inconsistencies
- SERVER-93099 Allow collMod with
  timeseriesBucketsMayHaveMixedSchemaData=false
- SERVER-93139 Ensure causal consistency between read_committed
  test operations
- SERVER-93174 Do not elect secondaries in
  mongos_rs_shard_failure_tolerance test
- SERVER-93212 Get mongod version and git version information
  without spinning up a mongod process
- SERVER-93318 [v7.0] Revert SERVER-86904
- WT-11391 Add a stat to track when we abort reconciliation
  because we cannot make progress

### Sharding

- SERVER-69234 Make
  txn_recover_decision_using_recovery_router.js robust to spurious shard
  version refreshes
- SERVER-82281 ShardingTest.js Does Not Merge Multiple
  SetParameters Properly
- SERVER-89529 Retryable writes during resharding may execute
  more than once if chunk migration follows the reshard operation

### Query

- SERVER-37164 Incorrect query results on $gte null with sparse
  index
- SERVER-92668 Wrong result with SBE, hash index, $lookup

### Storage

#### WiredTiger

- WT-9607 Fix timing of compact progress messages
- WT-10619 Update Clang-Format to 12.0.1
- WT-10689 Fix number of expected keys in test-prepare-hs03
- WT-10720 Increase slope threshold in
  test_sweep04.test_big_run in unit-test-long
- WT-12139 Fix memory leak in system backup recovery
- WT-12302 Fix compact progress time message
- WT-12560 Application thread is stuck in forced eviction
  because of uncommitted updates
- WT-12643 Fix Eviction Server walk logic so that it's able to
  evict all pages
- WT-13091 Make cursor_copy debug mode more precise
- WT-13109 Fix test_scrub_eviction_prepare.py to evict the page
  with release_evict cursor

### Operations

WT-11669 Create new log record for backup ids
