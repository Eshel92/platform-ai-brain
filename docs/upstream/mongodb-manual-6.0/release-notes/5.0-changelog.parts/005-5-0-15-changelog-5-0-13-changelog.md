<!-- Part 5 of 12 of release-notes/5.0-changelog.md (split because the page is big). -->

## 5.0.15 Changelog

### Sharding

- SERVER-68361
  LogTransactionOperationsForShardingHandler::commit misses transferring
  documents from prepared and non-prepared transactions changing a
  document's shard key value
- SERVER-71092 shard_id_test.cpp relies on a pure behavior of
  std::string::compare function
- SERVER-71219 Migration can miss writes from prepared
  transactions
- SERVER-71305 Legacy shard collection path waits on wrong
  opTime to be majority committed (5.0 and older)
- SERVER-71689 Refresh the CatalogCache before dropping the
  local collection
- SERVER-72301 Use ordered:false when inserting chunks in
  optimized path of create collection
- SERVER-72430 MigrationDestinationManager::report() may access
  null _migrationCloningProgress
- SERVER-73916 Improve ReshardingTest fixture error reporting
  when reshardCollection has already failed before any failpoints are
  waited on

### Query

SERVER-58712 Inconsistent update performance on collections
with multiple secondary indexes on same key

### Operations

- SERVER-67704 Add count of cpu sockets to FTDC metadata
- SERVER-67705 Add count of NUMA zones to FTDC metadata

### Build and Packaging

SERVER-38232 Mongod on Ubuntu 16/18 does not create a pid file

### Internals

- SERVER-49705 'permitted' file may have been deleted by
  'after_test'
- SERVER-54900 Blocking networking calls can delay sync-source
  resolution indefinitely
- SERVER-60839 Introduce a TemporarilyUnavailable error type
- SERVER-63104 Make it easy to run jsCore locally again in a
  world with tests tagged by feature flag
- SERVER-64764 $expr rewrite is not prepared to handle "$$ROOT"
- SERVER-65177 Elapsed initial sync time in
  TestRemainingInitialSyncEstimatedMillisMetric unit test can be 0 ms
- SERVER-65259 Cursor leak in aggregation that requires merging
  on shard
- SERVER-65881 Support sort-limit optimization with bounded
  sort stage
- SERVER-66050 findSelfInConfig should attempt fast path for
  every HostAndPort before trying slow path
- SERVER-66106 sharded_moveChunk_partitioned.js failed
  moveChunk check may be incorrect (only pre-6.0)
- SERVER-66466 Remove TransportLayerASIOTest dependence on
  ThreadContext
- SERVER-66570 Timeseries pushes down metaField-projections
  that can change semantics
- SERVER-67183 Higher throughput Chunk Migration - reimplement
  for fetching and insertion
- SERVER-67390 backup_restore.js should check for code -SIGINT
  due to unclean SIGINT
- SERVER-67406 Sorting a cursor on sharded coll returns
  documents that are missing $-prefixed fields
- SERVER-67446 Ensure consistent wildcardProjection and
  columnstoreProjection specs in catalog
- SERVER-68122 Investigate replicating the collection
  WiredTiger config string during initial sync
- SERVER-68388 Limit concurrency setting and update server
  parameter name
- SERVER-68434 Equality to null can incorrectly use a cached
  partial ixscan which does not cover the predicate
- SERVER-68576 We need to know how many sharded collections
  exist in a cluster
- SERVER-68647 Create feature flag
- SERVER-68648 Enable feature flag
- SERVER-68739 Add WiredTiger session statistic without
  affecting slow op statistics
- SERVER-68836 Properly handle NaN and 0 in for LDAPTimeoutMS
- SERVER-68853 Remove invariant that a session stat needs to be
  a slow op stat
- SERVER-68901 Incorrect $elemMatch query analysis in
  mongocryptd if document contains 2 different fields with the same name
- SERVER-69944 Resmoke's globstar.py does not properly parse 
  `*` before `**`
- SERVER-70139 listCollection returns duplicate view names
- SERVER-70323 Convert invariant to tassert in
  collection_sharding_runtime
- SERVER-70369 Create serverParameter for migrationConcurrency
- SERVER-70394 Fix self-swap in
  MultiPlanStage::removeRejectedPlans
- SERVER-70427 Remove chef+kitchen package test infrastructure
- SERVER-70553 Add module support to the mongo test runner
- SERVER-70566 Make assertion in backup_restore.js print error
  code
- SERVER-70594 Add updated build variants to sys-perf
- SERVER-70640 Add migrationConcurrency to serverStatus
- SERVER-70830 Unit test WiredTigerOperationStats
- SERVER-71006 Small window of inconsistency for reads after
  turning index to multikey
- SERVER-71020 Ensure aborting time series batch eventually
  removes bucket from catalog
- SERVER-71055 OplogOrder test can read stale all_durable
  timestamp after rolling back oplog entries
- SERVER-71191 Deadlock between index build setup, prepared
  transaction, and stepdown
- SERVER-71291 Variant "`*` Enterprise RHEL 8.0" should not
  have a .publish file
- SERVER-71373 Extend assert.soon timeout inside
  predictive_connpool.js
- SERVER-71399 Jumbo chunk flag isn't automatically cleared
  after a chunk split
- SERVER-71424 Fix failures in lint_fuzzer_sanity
- SERVER-71436 Range deleter must not aggressively spam the log
  when shard key index not found
- SERVER-71449 Fix log_successs_msg: not found in init.d on
  debian
- SERVER-71471 Improve jstestfuzz deployment to work with new
  node run/install
- SERVER-71533 Update legacy task generation to use new test
  stats location
- SERVER-71534 lint_fuzzer_sanity_all regression caused by
  running multiple instances of npm
- SERVER-71597 Fix race condition on createDatabase for case
  sensitive dbName
- SERVER-71632 Re-enable dropDatabase FSM test in stepdown
  suites
- SERVER-71648 [v5.0] txn_index_catalog_changes.js runs on
  storage engines that do not support snapshot reads
- SERVER-71691 Error 5643004 when using $setWindowFields in a
  facet
- SERVER-71759 dataSize command doesn't yield
- SERVER-71769 Add a new log message when a secondary node is
  skipping a two-phase index build
- SERVER-71939 Update BucketCatalogTest::Task class with
  failpoint
- SERVER-71950 Fail and log the operation when out-of-order
  keys are detected in WiredTiger
- SERVER-71969 Update system_perf.yml for compile-variant and
  compile_variant.
- SERVER-72005 Enable TSBS on 2022-11 sys-perf variants
- SERVER-72046 Concurrent chunk migration testing
- SERVER-72091 Enable auth-delay sys-perf variant
- SERVER-72143 Fix sys-perf logkeeper links on 5.0 and 4.4
- SERVER-72176 MetadataManagerTest must reset
  orphanCleanupDelaySecs to the default value on teardown
- SERVER-72185 TSBS perf test definition depends on a personal
  github repo
- SERVER-72222 MapReduce with single reduce optimization fails
  when merging results in sharded cluster
- SERVER-72276 Remove all outdated entries from
  backports_required_for_multiversion_tests.yml
- SERVER-72288 microbenchmark tests fail after "Enable M1 Mac
  support for DSI"
- SERVER-72449 backup_restore.js should check for code 2 when
  killing child resmoke client
- SERVER-72512 Indexes reported as valid when unable to return
  inconsistencies due to memory limit
- SERVER-72535 Sharded clusters allow creating the 'admin',
  'local', and 'config' databases with alternative casings
- SERVER-72576 Notarize archive-dist binaries on macOS
- SERVER-72613 Speed up taking core dumps with the hang
  analyzer
- SERVER-72619 Refactor and add more testing for
  migration_chunk_cloner_source changes
- SERVER-72620 $indexStats doesn't include the "shard" field
  when run on unsharded collections
- SERVER-72677 Full validation doesn't always report
  information about indexes
- SERVER-72825 Remove all outdated entries from
  backports_required_for_multiversion_tests.yml
- SERVER-72868 Complete TODO listed in SERVER-30949
- SERVER-72877 Mongos retargeting logic in stepdown hooks
  should skip views
- SERVER-72910 [v5.0] Backport wtRCToStatus changes from
  SERVER-60839
- SERVER-73176 Only print error message if there were in fact
  errors in getHostFQDNs
- SERVER-73183
  WiredTigerKVEngine::getSanitizedStorageOptionsForSecondaryReplication
  should skip inMemory
- SERVER-73216 Upgrade BlackDuck to Detect v8
- SERVER-73228 Remove active directory server from
  jstests/external_auth/ldap_mongos_health_checking.js
- SERVER-73232 Change the default log-verbosity for
  _killOperations
- SERVER-73264 Fix wrong invariant in
  MigrationChunkClonerSource::commitClone
- SERVER-73389 Checkpoint vector clock in drop database
  coordinator
- SERVER-73481 Validate does not detect out-of-order keys with
  {full: false}
- SERVER-73636 Coverity analysis defect 135025: Inefficient
  vector resizing with reserve.
- SERVER-73706 Save WTRecordStoreUassertOutOfOrder fail point
  state to prevent concurrency bugs in testing
- SERVER-73719 Comment out Legacy Build Variants in Sys-perf
- SERVER-73745 Zero initialize IndexKeyBucket struct
- WT-8290 Adding a new API to the session to return the
  rollback reason
- WT-8379 Do not disable eviction during shutdown
- WT-8651 Allow checkpoint scrub during shutdown
- WT-8652 Do not skip the final metadata checkpoint when
  shutdown configured with use_timestamp=true
- WT-9268 Delay deletion of the history store record to
  reconciliation
- WT-9428 Fix two asserts in rec_visibility.c
- WT-9592 Rollback to stable should also clear
  WT_UPDATE_TO_DELETE_FROM_HS flag
- WT-9705 Fix accidentally freeing update on the update chain
  in prepared commit
- WT-9751 Fix a memory leak in reconciliation after aborted
  eviction
- WT-9765 Fix handling a prepared commit after a prepared
  rollback with eviction failure
- WT-9792 Fix RTS to remove globally visible update of the data
  store update from the history store
- WT-9805 Save the updates need to be deleted from history
  store and delete them later
- WT-9926 A crash during startup from backup can lose metadata
- WT-10081 Fix failure format configs for older branch
- WT-10250 Remove certain Evergreen builders for release
  branches
- WT-10257 Fix
  data-validation-stress-test-checkpoint-fp-hs-insert-s7 in 5.0
- WT-10291 Ensure failure configs task executes test format
  once per configuration.
- WT-10461 Fix key out of order in skip list on weakly ordered
  architecture
- WT-10584 Add missing read barriers in __cursor_skip_prev


## 5.0.14 Changelog

### Sharding

- SERVER-60143 Avoid clearing filtering metadata after failed
  metadata refresh
- SERVER-68139 Resharding command fails if the projection sort
  is bigger than 100MB
- SERVER-68361
  LogTransactionOperationsForShardingHandler::commit misses transferring
  documents from prepared and non-prepared transactions changing a
  document's shard key value
- SERVER-69134 Dropping a sharded collection doesn't get rid of
  the CSS entry
- SERVER-69444 Make the joining of concurrent critical section
  and refresh look the same between DSS and CSS
- SERVER-69700 Replication rollback fails
  resharding_coordinator_recovers_abort_decision.js
- SERVER-69756 Segmentation fault on abortReshardCollection
  issued right after reshardCollection cmd
- SERVER-70364 Retry configureFailPoint command on network
  error (resharding_coordinator_recovers_abort_decision.js)
- SERVER-70373 Invariant failure in case resharding metrics are
  not restored
- SERVER-70793 Make database metadata refresh first check new
  metadata under the IS lock before taking X lock
- SERVER-71092 shard_id_test.cpp relies on a pure behavior of
  std::string::compare function
- SERVER-71305 Legacy shard collection path waits on wrong
  opTime to be majority committed (5.0 and older)

### Query

- SERVER-66289 $out incorrectly throws BSONObj size error on
  v5.0.8
- SERVER-70381 _internalSearchIdLookup stage violates a 5.0
  precondition of the getOwnershipFilter function

### Operations

SERVER-67793 log_progress_msg in init.d does not print message

### Build and Packaging

- SERVER-48203 Support --install-action for Ninja builds
- SERVER-64289 Platform Support: Add support for RHEL7 PPC in
  5.0.X
- SERVER-69507 Rpath should only be set on dynamic builds

### Internals

- SERVER-54284 ExceptionFor<ErrorCodes::WriteConflict> should
  resolve to WriteConflictException
- SERVER-57072 Explore upgrading wheel on all platforms.
- SERVER-60016 serverStatus and collection stats should not
  block on the RSTL lock
- SERVER-61185 Use prefix_search for unique index lookup
- SERVER-63104 Make it easy to run jsCore locally again in a
  world with tests tagged by feature flag
- SERVER-63585 Fastcount gets out of sync when a delete
  rollbacks and another transaction deletes the same rows
- SERVER-66525 errexit prevents capturing pip install log
- SERVER-66972 Database critical section does not serialize
  with ongoing refreshes
- SERVER-67385 Range deletion tasks may be wrongly scheduled
  before ongoing queries on range finish on a shard primary
- SERVER-67538 Multi-doc transactions should fail if on an old,
  incompatible snapshot
- SERVER-67681 Create specific target for compile commands
- SERVER-68115 Bug fix for "elemMatchRootLength > 0" invariant
  trigger
- SERVER-68477 Improve NaN-handling for expireAfterSeconds TTL
  index parameter
- SERVER-68901 Incorrect $elemMatch query analysis in
  mongocryptd if document contains 2 different fields with the same name
- SERVER-69001 Initial sync should set the minValid document to
  the "stopTimestamp"
- SERVER-69133 remove redundant setting of hardlink install
  action
- SERVER-69281 Force minimum ninja version
- SERVER-69348 Commands must declare empty auth checks to be
  universally callable
- SERVER-69380 $_internalUnpackBucket stage can incorrectly
  swap with a $project if an inclusion projection has already been
  absorbed
- SERVER-69389 Command checkAuthorization may throw
  ErrorCodes::NamespaceNotFound for existing collection while trying to
  resolve UUID to namespace when the node is  shutting down.
- SERVER-69446 Increase electionTimeoutMillis in
  jstests/replsets/dbcheck_write_concern.js
- SERVER-69569 Python scripts failing in Evergreen tasks
- SERVER-69784 Fix instances of signed char misuse
- SERVER-69868 Return an error when starting a TransportLayer
  that is shutdown
- SERVER-69898 Wait for the critical section catch-up phase
  before refreshing the DB version
- SERVER-69912 SConstruct is executable by mistake
- SERVER-69926 errorcodes.py doesn't detect duplicate errors in
  MONGO_UNREACHABLE_TASSERT
- SERVER-69930 Unexpected error message in the logs attempting
  to refresh the version of a dropped database
- SERVER-70062 Log pertinent info about oplog entries in oplog
  rolled over restore failure
- SERVER-70160 Do not push down $match that needs whole
  document before $internalUnpackBucket
- SERVER-70299 Remove JSON.send command usage
- SERVER-70314 Adjust time series extended range tests to
  account for log retention limitations
- SERVER-70348 Remove EAGAIN for queryable WT and retry
  internally
- SERVER-70469 Use virtual env python in watchdog tests
- SERVER-70483 Update Resmoke to pass "evergreen_execution" up
  to logkeeper.
- SERVER-70484 Remove signal processing module from perf.yml
  and sys_perf.yml
- SERVER-70557 Increase timeout for integration_tests_sharded
  on s90x
- SERVER-70633 Make per shard cursors suite actually run tests
  in 5.0
- SERVER-70879 Fix race where multiple threads are turning an
  index multikey concurrently
- SERVER-71055 OplogOrder test can read stale all_durable
  timestamp after rolling back oplog entries
- WT-8234 Prevent eviction of internal pages while reconciling
  leaf pages which could refer to their memory
- WT-9323 Fix a race tracking whether a tree has updates after
  a checkpoint
- WT-9599 Acquire the hot backup lock to call fallocate in the
  block manager
- WT-9763 Return EBUSY if the time window of inserting record
  does not match with history store time window


## 5.0.13 Changelog

### Sharding

- SERVER-68094 Resharding with custom generated _id fails with projection error
- SERVER-68139 Resharding command fails if the projection sort is bigger than 100MB
- SERVER-68869 A retry of _configSvrReshardCollection can succeed causing resharding_coordinator_recovers_abort_decision.js to fail
- SERVER-69142 A retry of _shardsvrReshardCollection can cause DuplicateKey error (resharding_nonblocking_coordinator_rebuild.js)
- SERVER-69220 refineCollectionShardKey permits toggling current shard key fields between range-based and hashed, leading to data inconsistency
- SERVER-69384 Fix v5.0 legacy shardCollection path for implicitCreateIndex parameter
- SERVER-69700 Replication rollback fails resharding_coordinator_recovers_abort_decision.js

### Write Operations

SERVER-50454 Avoiding sending the "keyValue" field to drivers on duplicate key error

### Internals

- SERVER-58673 Enable featureFlagPerShardCursor
- SERVER-60551 Occasionally getting "Initialized wire specification" when connecting
- SERVER-61185 Use prefix_search for unique index lookup
- SERVER-62400 Add $_passthroughToShard parameter to AggregateCommandRequest
- SERVER-62681 Create change streams per shard cursor passthrough suite
- SERVER-62738 Give mongos the ability to passthrough to a specific shard
- SERVER-63772 Post Batch Resume token not sent on initial batch from per shard cursor change stream
- SERVER-63773 Per Shard cursor post batch resume token not set in getMore responses
- SERVER-63774 Pass optional dbVersion to runPipelineOnSpecificShard
- SERVER-63781 $sortKey not filtered out in initial batch from post batch resume token
- SERVER-65006 Write conflict on commitIndexBuild oplog entry insertion can cause multikey to fail to be set
- SERVER-66794 Add an in-memory flag for TS collections having dates outside years 1970-2038
- SERVER-67402 Linearizable reads can occasionally read with wrong read source
- SERVER-67538 Multi-doc transactions should fail if on an old, incompatible snapshot
- SERVER-67650 Resharding recipient can return remainingOperationTimeEstimatedSecs=0 when the oplog applier hasn't caught up with the oplog fetcher
- SERVER-67653 Resharding coordinator can incorrectly conclude that it can start the critical section although on one recipient the oplog applier hasn't caught up with the oplog fetcher
- SERVER-67725 Check catalog consistency on shards as precondition for rename
- SERVER-67916 Race during stepdown can trigger invariant in ReshardingMetrics
- SERVER-68003 Make experiment_unified_ninja.vars the default
- SERVER-68126 Check for negative maxChunkSize input value in AutoSplitVector 
- SERVER-68691 $graphLookup does not report variable references for 'restrictSearchWithMatch' filter
- SERVER-69002 [5.0] backport pm-2419 Per Shard Cursors via mongos
- SERVER-69108 SCCL can immediately return config and admin metadata without triggering a refresh
- SERVER-69547 Add multiversion_incompatible tag to show_raw_update_description*.js
- SERVER-69590 libunwind warnings on clang arm platforms
- SERVER-69611 Set the -ffp-contract=off compiler option by default
- SERVER-69693 Use lambda instead of repeating code in resharding coordinator
- SERVER-69785 robustify change_streams_per_shard_cursor.js
- WT-9870 Fix updating pinned timestamp whenever oldest timestamp is updated during recovery
