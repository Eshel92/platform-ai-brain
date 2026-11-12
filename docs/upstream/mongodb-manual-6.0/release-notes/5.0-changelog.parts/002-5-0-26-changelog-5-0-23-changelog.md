<!-- Part 2 of 12 of release-notes/5.0-changelog.md (split because the page is big). -->

## 5.0.26 Changelog

### Sharding

- SERVER-65802 mongos returns inconsistent error code when
  renameCollection target already exists
- SERVER-84368 CreateIndex fails with StaleConfig if run from a
  stale mongos against a sharded non-empty collection

### Query

SERVER-83602 $or -> $in MatchExpression rewrite should not
generate $or directly nested in another $or

### Storage

WT-11062 Safe free the ref addr to allow concurrent access

### Internals

- SERVER-56661 Increase default close_handle_minimum in
  WiredTiger from 250 to 2000
- SERVER-60603 Allow connection reset errors without assertion
  in ASIOSession::ensureSync()
- SERVER-68128 Exceptions thrown while generating command
  response lead to network error
- SERVER-69005 $internalBoundedSort should not accept empty
  sort pattern
- SERVER-72703 Downgrade $out's db lock to MODE_IX
- SERVER-75355 Improve explain with Queryable Encryption
- SERVER-79235 rolling_index_builds_interrupted.js checkLog
  relies on clearRawMongoProgramOutput
- SERVER-79286 Create a query knob
- SERVER-79400 Implement number of documents tie breaking
  heuristics
- SERVER-79575 Fix numa node counting
- SERVER-80233 Implement index prefix heuristic
- SERVER-80275 Add log line for detailed plan scoring
- SERVER-81021 Improve index prefix heuristic by taking into
  account closed intervals
- SERVER-82476 Disable diagnostics latches by default
- SERVER-84336 Timeseries inserts can leave dangling BSONObj in
  WriteBatches in certain cases
- SERVER-84612 Define a version for immer
- SERVER-84615 Define a version for linenoise
- SERVER-85534 Checkpoint the vector clock after committing
  shard collection
- SERVER-85633 Add lock around res_ninit call
- SERVER-85843 A write operation may fail with
  NamespaceNotFound if the database has been concurrently dropped
  (sharding-only)
- SERVER-85869 Exhaustive find on config shard can return stale
  data
- SERVER-85973 Update README.third_party.md to indicate that
  Valgrind is licensed under BSD-4-Clause
- SERVER-86017 Backport multi-planner tie breaking improvements
  to v6.0
- SERVER-86214 add all bazel-* output dirs to git ignore
- SERVER-86388 Remove fle_drivers_integration.js test from 6.0
- SERVER-86395 Investigate DuplicateKey error while recovering
  convertToCapped from stable checkpoint
- SERVER-86403 Fix THP startup warnings
- SERVER-86433 Clear memory in the data_union stored on the
  endpoint before use
- SERVER-86562 Backport multi-planner tie breaking improvements
  to v5.0
- SERVER-86619 Document::shouldSkipDeleted() accesses string
  without checking for missing string
- SERVER-86622 Resharding coordinator use possibly stale
  database info
- SERVER-86632 plan_cache_drop_database.js should catch
  DatabaseDropPending errors
- SERVER-86717 Resharding should validate user provided zone
  range doesn't include $-prefixed fields.
- SERVER-87198 [5.0] Make shard registry reads fallback to
  majority readConcern if snapshot reads fail
- SERVER-87224 Enable diagnostic latching in test variants on
  old branches
- SERVER-87259 [v5.0] Fix for atlas azure intel variant
- SERVER-87415 Remove run_command__simple workload from
  sys-perf
- SERVER-87544 Fix up gitignore to permit git awareness of
  enterprise module
- SERVER-87567 The SessionWorkflow  should correctly return a
  response error on malformed requests
- SERVER-87610 Relax shardVersionRetry tripwires on the
  namespace of received stale exceptions
- SERVER-87626 [v5.0] Add san_options to buildvariant config
- SERVER-87653 Prevent latch_analyzer.js from being run as part
  of the parallelTester
- WT-9057 Null address read in compact walk
- WT-12077 Incorrect hardware checksum calculation on zSeries
  for buffers on stack
- WT-12379 Incorrect python version on Windows on 6.0
- WT-12402 Add stats to track when eviction server skips
  walking a tree
- WT-12438 Stop using Ubuntu 18.04 Power Evergreen distro on
  5.0
- WT-12447 Fix incorrect version of Python in the CMake Windows
  build on 5.0

   


## 5.0.25 Changelog

### Sharding

- SERVER-76536 Increase
  receiveChunkWaitForRangeDeleterTimeoutMS in concurrency suites
- SERVER-81508 Potential double-execution of write statements
  when ShardCannotRefreshDueToLocksHeld is thrown

### Replication

SERVER-56756 Primary cannot stepDown when experiencing disk
failures

### Storage

#### WiredTiger

- WT-10017 Remove the unstable historical versions at the end
  of rollback to stable
- WT-12316 Fix timing stress options in test/format for 6.0 and
  older branches

### Build and Packaging

SERVER-85156 dbCheck throws unexpected "invalidate" change
stream event [5.0]

### Internals

- SERVER-62763 Fix data-type used for passing options to
  setsockopt
- SERVER-64444 listIndexes fails on invalid pre-5.0 index spec
  after upgrade
- SERVER-66036 Improve future validity semantics
- SERVER-68674 Vendor an immutable/persistent data structure
  library
- SERVER-69413 Documentation Updates
- SERVER-71520 Dump all thread stacks on RSTL acquisition
  timeout
- SERVER-72839 Server skips peer certificate validation if
  neither CAFile nor clusterCAFile is provided
- SERVER-74874 Add typedef for immutable unordered map and set
- SERVER-74875 Implement immutable ordered map and set
- SERVER-74876 Evaluate which immer memory policy to use
- SERVER-74946 Convert containers in CollectionCatalog for
  collection lookup to immutable
- SERVER-74947 Convert containers in CollectionCatalog for view
  lookup to immutable
- SERVER-74951 Convert containers in CollectionCatalog for
  profile settings to immutable
- SERVER-75263 Add immer benchmarks
- SERVER-75497 Convert ordered containers in CollectionCatalog
  to immutable
- SERVER-75613 Add GDB pretty printers for immutable data
  structures
- SERVER-75851 Add typedef for immutable vector
- SERVER-76789 Add immer to README.third_party.md
- SERVER-76932 Add a way for a thread to know when the
  SignalHandler thread is done with printAllThreadStacks
- SERVER-77694 cannot compile immer header with --opt=off
- SERVER-78911 Always suppress "Different user name was
  supplied to saslSupportedMechs" log during X.509 intracluster auth
- SERVER-80150 Log negotiated network compressor with client
  metadata
- SERVER-80279 Commit on non-existing transaction then proceed
  to continue can trigger an invariant
- SERVER-80978 Fix potential deadlock between
  TTLMonitor::onStepUp and prepared transaction
- SERVER-81133 Speedup logic to persist routing table cache
- SERVER-82093 Release mongo v5 on amazon 2023
- SERVER-82353 Multi-document transactions can miss documents
  when movePrimary runs concurrently
- SERVER-82627 ReshardingDataReplication does not join the
  ReshardingOplogFetcher thread pool causing invariant failure.
- SERVER-82815 Expose server’s index key creation via
  aggregation
- SERVER-83050 Create a deployment of mongodb on
  AL2-openssl-1.1.1
- SERVER-83337 Re-enable wt_size_storer_cleanup_replica_set.js
  on macOS
- SERVER-83369 Index creation does not enforce type of
  bucketSize field
- SERVER-83564 Make sure the process field is indexed in
  config.locks
- SERVER-84063 Remove BlackDuck from Security Daily Cron
- SERVER-84722 Create undocumented server parameter to skip
  document validation on insert code path for internal usage
- SERVER-84749 Remove
  sharding_update_v1_oplog_jscore_passthrough from macOS variants
- SERVER-84772 Delete stitch-related tasks in enterprise
  variant
- SERVER-85167 Size storer can be flushed concurrently with
  being destructed for rollback
- SERVER-85263 Report escaped client application name
- SERVER-85306 Update sys-perf config to use HTTPs github links
  rather than SSH
- SERVER-85364 [6.0] Convert resource map in CollectionCatalog
  to immutable
- SERVER-85365 [6.0] Convert shadow catalog in
  CollectionCatalog to immutable
- SERVER-85419 Balancer pollutes logs in case no suitable
  recipient is found during draining
- SERVER-85498 [5.0] Fix immutable_ordered_test on MacOS
- SERVER-85530 Refresh Test Certificates
- SERVER-85652 Update DSI atlas azure tasks to use an AL2
  compile artifact.
- SERVER-85693 Fix potential access violation in
  User::validateRestrictions
- SERVER-85771 Make $bucketAuto more robust in the case of an
  empty string for the groupBy field
- SERVER-85984 The test for inserting docs larger than the user 
  max relies on a specific order of documents in the oplog, but that
  order is not guaranteed
- SERVER-86027 Tag
  insert_docs_larger_than_max_user_size_standalone.js with
  requires_persistence and requires_replication
- SERVER-86062 [v5.0] directoryperdb.js relies on
  fsync/checkpointing behavior which does not hold when running with
  --nojournal
- SERVER-86081 Sys-perf missing required parameters due to
  Evergreen Redaction
- SERVER-86561 Increase benchmarks_orphaned from 3h to 4h
- WT-7712 commit and durable timestamps should be disallowed at
  stable timestamp
- WT-9824 Add testing to file manager WT connection
  configurations in test/format
- WT-11491 Log the WiredTiger time spent during startup and
  shutdown
- WT-11777 Fix units of __wt_timer_evaluate() calls: logging
  and progress period
- WT-12211 Fix PATH env variable in hang analyzer to generate
  python core dump (7.0)
- WT-12272 Remove unnecessary module in evergreen.yml


## 5.0.24 Changelog

### Sharding

- SERVER-50792 Return more useful errors when a shard key index
  can't be found for shardCollection/refineCollectionShardKey
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
- SERVER-83146 Bulk write operation might fail with
  NamespaceNotFound

### Replication

- SERVER-55465 Fix Invariant upon failed request for a vote
  from the current primary in the election dry-run of catchup takeover
- SERVER-70155 Add duration of how long an oplog slot is kept
  open to mongod "Slow query" log lines

### Catalog

SERVER-82129 FCV 5.0 Upgrade fails due to
config.cache.collections missing UUIDs for most collections

### Storage

SERVER-33494 WT SizeStorer never deletes old entries

### Internals

- SERVER-65666 Do not create chunks on draining shards when
  sharding a new collection
- SERVER-67766 Log index and collection successful drop
- SERVER-69063 Fix TCP keepalive option setting
- SERVER-69615 Rollback fuzzing in WiredTiger leads to size
  storer marked dirty at shutdown
- SERVER-74074 Exclude auth consistency workloads from
  concurrency simultaneous suites
- SERVER-77311 Add a new log message when a secondary node is
  skipping a two-phase index build with a subset of indexes built
- SERVER-77506 Sharded multi-document transactions can mismatch
  data and ShardVersion
- SERVER-77926 Add LSAN suppressions for executor worker
  threads
- SERVER-78009 shardSvrCommitReshardCollection command should
  fail recoverably if the node is shutting down
- SERVER-79864 TTL deleter does not correctly handle time
  series collections with extended range dates
- SERVER-79982 Batched catalog writers can run concurrently
  with  HistoricalCatalogIdTracker::cleanup() and lead to incorrect PIT
  find results.
- SERVER-80789 Make AutoGetOplog behave consistently in replica
  set node started as standalone
- SERVER-80886 $out may fail with a StaleDbVersion after a
  movePrimary
- SERVER-80974 Unclean shutdown while dropping local.*
  collection and indexes can make the catalog inconsistent
- SERVER-81143 export_import_concurrency.js should check for
  code 2 when killing child resmoke client
- SERVER-81442 Poke WT oplog reclamation thread periodically
- SERVER-81573 ExpressionNary::optimize crashes on initialized
  children in v4.4 and 5.0
- SERVER-81878 startupRecoveryForRestore may not play nicely
  with collection drop applied during startup recovery
- SERVER-81949 Sync from 10gen/mongo to mongodb/mongo on v4.4
  with copybara
- SERVER-82043 Enhancement of Commit Message Validation for
  10gen/mongo Commits
- SERVER-82111 In sharded_agg_helpers.cpp move invariant below
  response status check
- SERVER-82223 Commit handler in FCV op observer is susceptible
  to interruption
- SERVER-82391 [v4.4] Only allow github Apps Copybara Syncer:
  10gen-to-Mongodb to syncs new commits to mongodb/mongo
- SERVER-82447 $project incorrectly pushed down on timeseries
  when $project uses $getField on a measurement field
- SERVER-82449 [v4.4] Optimize copybara sync behavior for
  specific no-change scenarios
- SERVER-82555 Use shallow clone to speed up performance tests
- SERVER-82640 Upload mongod --version output to S3 during
  server compilation in Evergreen
- SERVER-82708 Update variants used to performance test stable
  branches
- SERVER-82730 The validate cmd can invariant on corrupted
  keystrings
- SERVER-83091 $or query can trigger an infinite loop during
  plan enumeration
- SERVER-83161 Fix concurrent read to _errMsg from
  MigrationDestinationManager without acquiring mutex
- SERVER-83283 Modify copybara script to send slack message on
  failure
- SERVER-83336 Temporarily disable
  wt_size_storer_cleanup_replica_set.js on macOS
- SERVER-83354 Schedule copybara instance after each commit
  made
- SERVER-83485 Fix multikey-path serialization code used during
  validation
- SERVER-83494 [7.0] Fix range deleter unit test case
- SERVER-83592 Add resmoke flag --enable_enterprise_tests
  enable enterprise js tests
- SERVER-83655 Restore legal client ns exception for
  admin.system.new_users
- SERVER-83830 On Enterprise build creating a collection in a
  replica set with the storageEngine.inMemory option breaks secondaries
- SERVER-83874 Move primary operation doesn't drop
  db.system.views on the donor
- SERVER-83916 Add LSAN Suppression for threads leaked by
  unjoined thread pools
- SERVER-84013 Incorrect results for index scan plan on query
  with duplicate predicates in nested $or
- SERVER-84353 The test for stepDown deadlock with read ticket
  exhaustion is flaky
- SERVER-84435 Deploy enterprise module consolidation to branch
  v5.0
- SERVER-84457 [v5.0] Explicitly declare type of term field in
  sync source resolver query
- SERVER-84479 Amend burn_in test to tolerate absence of
  manifest
- SERVER-84576 [v5.0] Update 5.0 Readme
- WT-7929 Investigate a solution to avoid FTDC stalls during
  checkpoint
- WT-9257 test_checkpoint WT_NOTFOUND failure on CS
- WT-9821 Add option to verify to report all data corruption in
  a file
- WT-10601 Fix wt verify -c failure when first block on page is
  corrupt
- WT-10961 Fix OOO keys caused by racing deletion and insertion
  on left subtrees
- WT-10972 Eliminate long periods of silence when recovering
  with recovery_progress verbose messages enabled
- WT-11280 Generation tracking might not be properly
  synchronized
- WT-11774 Add diagnostic stat to investigate eviction server's
  inability to queue pages
- WT-12036 Workaround for lock contention on Windows


## 5.0.23 Changelog

### Internals

- SERVER-73430 Improve Hash, HMAC, and Crypto algo lookup for
  OpenSSL 3.0
- SERVER-75989 Add support for OpenSSL 3.0 FIPS
- SERVER-78108 POS interface should expose its shutdown state
- SERVER-78115 Shard primaries must commit a majority write
  before using new routing information from the config server
- SERVER-81581 Extend BlackDuck timeout
- SERVER-81942 ShardingDDLCoordinator should retry on
  LockTimeout errors
- SERVER-82204 Classic window functions first/last handle
  missing field incorrectly
- SERVER-82233 Update BACKPORTS_REQUIRED_BASE_URL from
  mongodb/mongo to 10gen/mongo
- SERVER-82613 Supress test in v5.0 multiversion
- SERVER-82799 Increase reshardingCriticalSectionTimeoutMillis
  for resharding_update_tag_zones.js
- SERVER-82990 Investigate powercycle failures on v6.0 and v5.0
- SERVER-83150 Document::shred() does not copy document
  metadata
- WT-11564 Fix RTS to read the newest transaction value only
  when it exists in the checkpoint
- WT-11584 Fix test_checkpoint_stats test
- WT-11602 Hide expected eviction failures from the application
  and don't rollback in case of errors
