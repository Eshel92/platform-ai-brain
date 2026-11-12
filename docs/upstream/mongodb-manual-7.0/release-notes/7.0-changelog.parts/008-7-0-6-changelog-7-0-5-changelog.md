<!-- Part 8 of 10 of release-notes/7.0-changelog.md (split because the page is big). -->

## 7.0.6 Changelog

### Sharding

- SERVER-75537 Handle direct operations against shards
- SERVER-76337 Add a server status metric to track unauthorized
  direct connections to shards
- SERVER-76984 Remove check for !_isInternalClient() in service
  entry point
- SERVER-77027 Only check for direct shard connections if
  sharding is enabled
- SERVER-81508 Potential double-execution of write statements
  when ShardCannotRefreshDueToLocksHeld is thrown
- SERVER-83146 Bulk write operation might fail with
  NamespaceNotFound
- SERVER-83775 Do not balance data between shards owning more
  than the ideal data size

### Replication

SERVER-79191 continuous_initial_sync.py Can Be in Rollback
During FSM Teardown

### Query

SERVER-84595 Delete invalid test
jstests/noPassthrough/out_majority_read_replset.js

### Aggregation

SERVER-82929 $listSearchIndexes requires find privilege action
rather than listSearchIndexes privilege action as it intended

### Storage

WT-11062 Safe free the ref addr to allow concurrent access

#### WiredTiger

- WT-11845 Fix transaction visibility issue with truncate

### Build and Packaging

SERVER-62957 Add reshardCollection change stream event

### Internals

- SERVER-69413 Documentation Updates
- SERVER-72703 Downgrade $out's db lock to MODE_IX
- SERVER-72839 Server skips peer certificate validation if
  neither CAFile nor clusterCAFile is provided
- SERVER-74875 Implement immutable ordered map and set
- SERVER-75497 Convert ordered containers in CollectionCatalog
  to immutable
- SERVER-75613 Add GDB pretty printers for immutable data
  structures
- SERVER-75851 Add typedef for immutable vector
- SERVER-76463 Ensure Sharding DDL locks acquired outside a
  coordinator wait for DDL recovery
- SERVER-77801 Remove
  sharded_collections_jscore_passthrough_with_config_shard from the
  macOS hosts
- SERVER-78188 Permit default use of multithreaded LDAP
  connection pool with libldap and OpenSSL 1.1.1
- SERVER-78311 mongos does not report writeConcernError in
  presence of writeErrors for insert command
- SERVER-78662 Deadlock with index build, step down, prepared
  transaction, and MODE_IS coll lock
- SERVER-78911 Always suppress "Different user name was
  supplied to saslSupportedMechs" log during X.509 intracluster auth
- SERVER-79150 Reduce ScopedSetShardRole scope to setup stage
  of index build
- SERVER-79192 Fix migration_coordinator_commit_failover.js to
  use awaitReplicationBeforeStepUp: false
- SERVER-79202 PinnedConnectionTaskExecutor can hang when
  shutting down
- SERVER-79214 Orphaned documents cause failures in indexu.js
- SERVER-79286 Create a query knob
- SERVER-79400 Implement number of documents tie breaking
  heuristics
- SERVER-79972 Investigate making core dump archival faster
- SERVER-80150 Log negotiated network compressor with client
  metadata
- SERVER-80233 Implement index prefix heuristic
- SERVER-80275 Add log line for detailed plan scoring
- SERVER-80310 Update sysperf to allow running individual genny
  tasks on waterfall
- SERVER-80645 Amazon 2023 community packages fail to install
- SERVER-80978 Fix potential deadlock between
  TTLMonitor::onStepUp and prepared transaction
- SERVER-81021 Improve index prefix heuristic by taking into
  account closed intervals
- SERVER-81181 Enable featureFlagCheckForDirectShardOperations
- SERVER-81246 FLE WriteConcernError behavior unclear
- SERVER-81534 DDL locks musn't be acquired during step down or
  shutdown
- SERVER-82053 Use index hint for time series bucket reopening
  query
- SERVER-82221 listCollections and listIndexes should include
  commit-pending namespaces
- SERVER-82261 setup_spawnhost_coredump script may miss core
  dump from crashed process on Windows
- SERVER-82353 Multi-document transactions can miss documents
  when movePrimary runs concurrently
- SERVER-82365 Optimize the construction of the balancer's
  collection distribution status histogram (2nd attempt)
- SERVER-82450 MongoServerError: batched writes must generate a
  single applyOps entry
- SERVER-82627 ReshardingDataReplication does not join the
  ReshardingOplogFetcher thread pool causing invariant failure.
- SERVER-82640 Upload mongod --version output to S3 during
  server compilation in Evergreen
- SERVER-82815 Expose server’s index key creation via
  aggregation
- SERVER-83050 Create a deployment of mongodb on
  AL2-openssl-1.1.1
- SERVER-83119 Secondary replica crashes on clustered
  collection if notablescan is enabled
- SERVER-83145 Shared buffer fragment incorrectly tracks memory
  usage in freeUnused()
- SERVER-83192 Always include zero cpuNanos in profiler
- SERVER-83296 Remove column data from BSON fuzzer
- SERVER-83337 Re-enable wt_size_storer_cleanup_replica_set.js
  on macOS
- SERVER-83369 Index creation does not enforce type of
  bucketSize field
- SERVER-83454 Range Deleter Service registration and
  de-registration should not rely on onCommit ordering guarantees
- SERVER-83492 Remove limit and skip values from SBE plan cache
  key if possible
- SERVER-83567 Push in classic stores missing values.
- SERVER-83610 Consider reducing privileges required for
  $documents
- SERVER-83639 Add exception for fuzzer for BSONColumn
  validation
- SERVER-83738 db-contrib-tool fails to get release json
  sometimes
- SERVER-83825 increase log verbosity for write conflict
  retries in index_build_operation_metrics.js:
- SERVER-83874 Move primary operation doesn't drop
  db.system.views on the donor
- SERVER-83955 Fix wrong warning messages in ReplSetGetStatus
  command
- SERVER-83959 When preparing SBE plan, correctly pass
  preparingFromCache argument
- SERVER-84063 Remove BlackDuck from Security Daily Cron
- SERVER-84130 Incorrect bucket-level filter optimization when
  some events in the bucket are missing the field
- SERVER-84147 Update vscode workspace from true to explicit
- SERVER-84186 Add benchmark that runs math operations in
  Timeseries to sys perf
- SERVER-84233 Support BSON MinKey and MaxKey in BSONColumn
- SERVER-84313 Exclude
  coordinate_txn_recover_on_stepup_with_tickets_exhausted.js from
  sharding multiversion suites on 7.0
- SERVER-84336 Timeseries inserts can leave dangling BSONObj in
  WriteBatches in certain cases
- SERVER-84337 Backport new variants added to perf.yml over to
  sys-perf-7.0 and sys-perf-4.4
- SERVER-84338 Top level $or queries may lead to invalid SBE
  plan cache entry which returns wrong results
- SERVER-84353 The test for stepDown deadlock with read ticket
  exhaustion is flaky
- SERVER-84410 Do an initial refresh of the other mongos in
  txn_with_several_routers.js
- SERVER-84436 Handle skip + limit sum overflowing int64_t in
  SBE
- SERVER-84468 Fix deadlock when running
  runTransactionOnShardingCatalog()
- SERVER-84534 [7.0] Blocklist plan_cache_sbe.js from
  replica_sets_initsync_jscore_passthrough
- SERVER-84548 Using ShardServerCatalogCacheLoader on configsvr
  causes excessive WT data handles / memory usage
- SERVER-84567 writeQueryStats should log an error rather than
  uassert when the feature flag is disabled
- SERVER-84722 Create undocumented server parameter to skip
  document validation on insert code path for internal usage
- SERVER-84723 Sharded multi-document transactions can observe
  partial effects of concurrent DDL operations
- SERVER-84732 Fix typo in mongo-perf standalone inMemory ARM
  AWS test
- SERVER-84806 Ignore reshardCollection change event after
  v6.0->v7.0 upgrade in test
- SERVER-85167 Size storer can be flushed concurrently with
  being destructed for rollback
- SERVER-85171 split unittest tasks up
- SERVER-85206 Improve performance of full_range.js and
  explicit_range.js
- SERVER-85260 SBE $mergeObjects crashes server with undefined
  input
- SERVER-85263 Report escaped client application name
- SERVER-85306 Update sys-perf config to use HTTPs github links
  rather than SSH
- SERVER-85419 Balancer pollutes logs in case no suitable
  recipient is found during draining
- SERVER-85453 ExternalDataSourceScopeGuard should not be
  compatible with multiple plan executors
- SERVER-85530 Refresh Test Certificates
- SERVER-85633 Add lock around res_ninit call
- SERVER-85652 Update DSI atlas azure tasks to use an AL2
  compile artifact.
- SERVER-85693 Fix potential access violation in
  User::validateRestrictions
- SERVER-85714 BSONColumn validator need to treat MinKey and
  MaxKey as uncompressed
- SERVER-85771 Make $bucketAuto more robust in the case of an
  empty string for the groupBy field
- SERVER-85848 $redact inhibits change stream optimization
- SERVER-85956 Query Stats 7.0 Backport Batch #1
- SERVER-85984 The test for inserting docs larger than the user
  max is flaky
- SERVER-86027 Tag
  insert_docs_larger_than_max_user_size_standalone.js with
  requires_persistence and requires_replication
- SERVER-86081 Sys-perf missing required parameters due to
  Evergreen Redaction
- SERVER-86096 Add queryable encryption workloads to 7.0
  project on Evergreen
- SERVER-86116 CreateCollectionCoordinator may fail to create
  the chunk metadata on commit time.
- SERVER-86118 Backport Query Stats to 7.0 Batch #2
- SERVER-86298 Query Stats 7.0 Backport Batch #3
- SERVER-86363 Make container registry login silent
- SERVER-86432 Backport Query Stats to 7.0 Batch #4
- WT-11777 Fix units of __wt_timer_evaluate() calls: logging
  and progress period
- WT-11987 Table's version number dropped to
  version=(major=1,minor=0)
- WT-12043 Remove obsolete HAVE_DIAGNOSTIC ifdefs to avoid
  memory leak
- WT-12077 Incorrect hardware checksum calculation on zSeries
  for buffers on stack
- WT-12147 Temporarily disable clang-analyzer
- WT-12211 Fix PATH env variable in hang analyzer to generate
  python core dump (7.0)


## 7.0.5 Changelog

### Sharding

- SERVER-73763 Resharding does not extend zone ranges for
  config.tag docs, leading to config server primary fassert loop from
  duplicate key error
- SERVER-82838 ReshardingOplogApplier uses {w: "majority",
  wtimeout: 60000} write concern when persisting resharding oplog
  application progress
- SERVER-82883 Recovering TransactionCoordinator on stepup may
  block acquiring read/write tickets while participants are in the
  prepared state
- SERVER-82953
  CreateCollectionCoordinator::checkIfOptionsConflict  should be more
  verbose
- SERVER-83061 Remove partially-released vestiges of ShardRole
  API from 7.0

### Query

SERVER-83470 Introduce internalQueryFrameworkControl setting
for 6.0-style engine selection logic

### Storage

SERVER-33494 WT SizeStorer never deletes old entries

### Internals

- SERVER-65082 Remove feature flag for Time-series Metric
  Indexes
- SERVER-65666 Do not create chunks on draining shards when
  sharding a new collection
- SERVER-70338 Query yield accesses the storage engine without
  locks during shutdown and rollback
- SERVER-70974 Fix early-exits triggered when user specifies
  TCP Fast Open server parameters
- SERVER-75033 Capture core dumps from test failures on macOS
- SERVER-76560 Time series collections not always honoring
  expireAfterSeconds correctly
- SERVER-77311 Add a new log message when a secondary node is
  skipping a two-phase index build with a subset of indexes built
- SERVER-77728 Robustify wildcard_index_validindex.js test
- SERVER-77827 Allow restore role to drop system.views
- SERVER-78065 Create feature flag
- SERVER-78066 Enable feature flag
- SERVER-78998 Refactor checking the value of
  'internalQueryFrameworkControl' throughout query code
- SERVER-79217 Race in PrimaryOnlyServiceMongoDTest::stepUp
  causes invariant failure
- SERVER-79235 rolling_index_builds_interrupted.js checkLog
  relies on clearRawMongoProgramOutput
- SERVER-79274 FCV checks can be racy if FCV is uninitialized
  in between the checks
- SERVER-79762 Fix initial_sync_chooses_correct_sync_source.js
  to wait initial sync node to find primary before starting initial sync
- SERVER-79810 make JournalFlusher::waitForJournalFlush()
  interruptible when waiting for write concern
- SERVER-79864 TTL deleter does not correctly handle time
  series collections with extended range dates
- SERVER-79919 write js test for SERVER-79810
- SERVER-79924 Use an accurate 'isCount' flag to encode a
  CanonicalQuery for SBE plan cache
- SERVER-80363 server default writeConcern is not honored when
  wtimeout is set
- SERVER-80368 Robustify hidden_index.js and
  compound_wildcard_index_filter.js
- SERVER-80660 Log a summary of where mongodb spent time during
  startup and shutdown
- SERVER-80789 Make AutoGetOplog behave consistently in replica
  set node started as standalone
- SERVER-80901 Audit gFeatureFlagServerlessChangeStreams
- SERVER-80922 Object field order is undefined when using
  $setWindowField
- SERVER-80974 Unclean shutdown while dropping local.*
  collection and indexes can make the catalog inconsistent
- SERVER-81046 add requireSequenceTokens to
  SearchCommand.CursorOptions
- SERVER-81143 export_import_concurrency.js should check for
  code 2 when killing child resmoke client
- SERVER-81229 Move primary may not cleanup cloned collections
  on failure
- SERVER-81371 movePrimary's clone phase failure may be retried
  indefinitely if database contains sharded views
- SERVER-81375 Disable internal transactions resharding tests
  in CSRS stepdown suite
- SERVER-81396 "Enterprise RHEL 8.3 s390x Shared" build variant
  is overwriting the binaries of "Enterprise RHEL 8.3 s390x"
  (non-Shared)
- SERVER-81400 Structural validation for BSONColumn
- SERVER-81442 Poke WT oplog reclamation thread periodically
- SERVER-81517 deny list validate_db_metadata_command.js from
  migrations suite
- SERVER-81591 Ensure that the secondary being stepped up in
  stopReplicationAndEnforceNewPrimaryToCatchUp is not stale
- SERVER-81603 Set the stream worker thread of the balancer as
  interruptible to support a correct stepdown of the config server
- SERVER-81606 Exclude untimestamped catalog durability test
  from in-memory variants
- SERVER-81631 Make authorizationClaim OIDC IdP configuration
  field optional
- SERVER-81949 Sync from 10gen/mongo to mongodb/mongo on v4.4
  with copybara
- SERVER-81978 repl::applyCommand_inlock does not handle
  TemporarilyUnavailable and TransactionTooLargeForCache exceptions
- SERVER-82036 Relax startup recovery invariant for unfinished
  single-phase index builds
- SERVER-82043 Enhancement of Commit Message Validation for
  10gen/mongo Commits
- SERVER-82073 Fix merge chunk command generation in
  collection_defragmentation.js
- SERVER-82090 Reduce scope of synchronization for
  archive-based reopening
- SERVER-82111 In sharded_agg_helpers.cpp move invariant below
  response status check
- SERVER-82143 Make clientId OIDC IdP configuration field
  optional
- SERVER-82197 Incorrect query results in SBE if $group spills
  in presence of collation
- SERVER-82223 Commit handler in FCV op observer is susceptible
  to interruption
- SERVER-82313 Fix cancelling txn api from the caller
- SERVER-82365 Optimize the construction of the balancer's
  collection distribution status histogram (2nd attempt)
- SERVER-82368 Match top/bottom N accumulators in SBE and
  Classic
- SERVER-82391 [v4.4] Only allow github Apps Copybara Syncer:
  10gen-to-Mongodb to syncs new commits to mongodb/mongo
- SERVER-82437 db.collection.getSearchIndexes(<indexName>)
  returns duplicate index
- SERVER-82447 $project incorrectly pushed down on timeseries
  when $project uses $getField on a measurement field
- SERVER-82449 [v4.4] Optimize copybara sync behavior for
  specific no-change scenarios
- SERVER-82555 Use shallow clone to speed up performance tests
- SERVER-82685 Increase reshardingCriticalSectionTimeoutMillis
  for store_historical_placement_data.js
- SERVER-82706 check_metadata_consistency.js should use
  retriable writes when contacting config server
- SERVER-82708 Update variants used to performance test stable
  branches
- SERVER-82730 The validate cmd can invariant on corrupted
  keystrings
- SERVER-82781 Simulate crash test hook may leave behind part
  of file when copying data
- SERVER-82791 createView fails with StaleConfig if a sharded
  collection already exists with the same namespace
- SERVER-82967 Stepdown after calling
  ActiveIndexBuilds::registerIndexBuild() during index build setup
  doesn't unregister itself
- SERVER-82984 FLE2 with upsert: true can have
  upsertedDocuments.size() == 1 and updateReply.getNModified() == 1 at
  the same time
- SERVER-83088 Make matchPattern optional for machine flow IdPs
- SERVER-83091 $or query can trigger an infinite loop during
  plan enumeration
- SERVER-83099 LDAPTimer::setTimeout may run callback inline
- SERVER-83107 Add 'type' field to search IndexDefinition
  struct
- SERVER-83150 Document::shred() does not copy document
  metadata
- SERVER-83161 Fix concurrent read to _errMsg from
  MigrationDestinationManager without acquiring mutex
- SERVER-83225 Fix
  untimestamped_catalog_writes_require_durability test
- SERVER-83257 IDPManager should make local shared_ptr copies
  atomically
- SERVER-83283 Modify copybara script to send slack message on
  failure
- SERVER-83336 Temporarily disable
  wt_size_storer_cleanup_replica_set.js on macOS
- SERVER-83354 Schedule copybara instance after each commit
  made
- SERVER-83389 aggregation_optimization_fuzzer fails on 6.0 and
  7.0 with a disabled disablePipelineOptimization failpoint
- SERVER-83429 Retryable FLE2 update and findAndModify fails on
  retry if document is removed
- SERVER-83485 Fix multikey-path serialization code used during
  validation
- SERVER-83494 [7.0] Fix range deleter unit test case
- SERVER-83499 Update metadata manager tests that expect a
  collection description to hold a range preserver
- SERVER-83580 Re-introduce balancer policy unittests with
  multiple chunks
- SERVER-83592 Add resmoke flag --enable_enterprise_tests
  enable enterprise js tests
- SERVER-83655 Restore legal client ns exception for
  admin.system.new_users
- SERVER-83685 Make internalQueryFrameworkControl
  "trySbeRestricted" the default query knob
- SERVER-83777 Cap $in length in plan cache key with
  internalQueryMaxScansToExplode + 1
- SERVER-83830 On Enterprise build creating a collection in a
  replica set with the storageEngine.inMemory option breaks secondaries
- SERVER-83866 Update BACKPORTS_REQUIRED_BASE_URL from
  mongodb/mongo to 10gen/mongo
- SERVER-83916 Add LSAN Suppression for threads leaked by
  unjoined thread pools
- SERVER-83952 Fix fuzzer failures for BSONColumn validation
- SERVER-84013 Incorrect results for index scan plan on query
  with duplicate predicates in nested $or
- SERVER-84087 Make sure ExecutorPool gets terminated after
  migrations have completed
- SERVER-84148 Fix timing issue in fle2_compact_setfcv.js test
- SERVER-84337 Backport new variants added to perf.yml over to
  sys-perf-7.0 and sys-perf-4.4
- WT-7929 Investigate a solution to avoid FTDC stalls during
  checkpoint
- WT-11584 Fix test_checkpoint_stats test
- WT-11698 Re-enable HS verification in v7.0
- WT-11774 Add diagnostic stat to investigate eviction server's
  inability to queue pages
- WT-12036 Workaround for lock contention on Windows
