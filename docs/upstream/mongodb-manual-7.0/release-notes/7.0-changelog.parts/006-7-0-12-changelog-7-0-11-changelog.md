<!-- Part 6 of 10 of release-notes/7.0-changelog.md (split because the page is big). -->

## 7.0.12 Changelog

### Aggregation

SERVER-89344 Fix explain output for '$unionWith' queries

### Storage

#### WiredTiger

- WT-10994 Make sweep server respect WT_DHANDLES_DROPPED flag
  plus prevent user creating a bulk cursor when a transaction is running
- WT-11194 Fixing format load when reverse is enabled
- WT-11273 Prevent hs_search stress point with pareto and
  predictable replay
- WT-11941 Incorrect timing statistics for eviction and
  reconciliation
- WT-12110 Disable timestamp_abort backup tests in the
  compatibility mode
- WT-12736 Mark the page clean after re-instantiating the page
  with prepared updates.

### Internals

- SERVER-58300 Generalize the concept of a shard-local
  collection
- SERVER-64574 Upgrade MozJS/Spidermonkey to the latest ESR
- SERVER-72019 Upgrade Mongo C Driver and mitigate CVE
- SERVER-72090 system.users can be renamed to regular
  collections and vice versa
- SERVER-81331 Spilling in SBE may lead to read on destroyed
  catalog object
- SERVER-81596 Fix Race in
  index_operations_abort_concurrent_outgoing_migrations.js
- SERVER-82205 Make shell dbHash comparison to exclude
  encryption options
- SERVER-82668 Remove fsync_deadlock.js from the
  sharding_csrs_continuous_config_stepdown suite
- SERVER-83377 Make timeseries_dynamic_bucket_sizing.js more
  robust
- SERVER-83712 Do not add $in length to plan cache key if there
  is no sort
- SERVER-84009 [7.0] Clean up query stats perf testing
- SERVER-84011 [7.0] Enable feature flag
- SERVER-84054 create default attribute for
  ENABLE_ENTERPRISE_TESTS
- SERVER-84315 Introduce new flag to control spilling strategy
  in $group
- SERVER-86674 Primary catch-up may believe it is caught up
  when it is not
- SERVER-87267 Increase bucket_catalog memory usage threshold
  for timeseries_dynamic_bucket_sizing.js
- SERVER-87343 Add awaitReplication() before stepping up
  secondary in range_deletions_has_index.js
- SERVER-87817 The mongo instance returns an error
  (MongoCommandException, Location50811) in version 7.0.6, but works
  fine in version 6.0.12.
- SERVER-87818 The mongo instance crashes in version 7.0.6, but
  works fine in version 6.0.12
- SERVER-88172 Config can be used as primary shard even in
  cluster with dedicated config server
- SERVER-88264 Add an option to enable warnings for direct
  connections on single shard clusters
- SERVER-88417 processReshardingFieldsForRecipientCollection
  can use stale db info and incorrectly creates a recipient
- SERVER-88832 Periodically check for interrupt in dbStats
- SERVER-89466 Update MozJS ASANHandles to support tracking
  multithreaded memory allocations
- SERVER-89496 Collect change stream queries using
  $_passthroughToShard for query stats
- SERVER-89499 Remove shard-lite, standalone, 1-node replica
  set and m60-like variants
- SERVER-89723 Adapt validation for authorization_endpoint,
  token_endpoint, device_authorization_endpoint
- SERVER-89812 Fix C1001 Internal Compiler Error when compiling
  mozjs on MSVC
- SERVER-89970 Reduce flakiness of hedged_reads.js
- SERVER-89994 Allow direct shard operations which acquire
  locks only on non-user collections
- SERVER-90086 Fix direct_shard_connection_auth checks for
  directConnectionChecksWithSingleShard
- SERVER-90100 Suppress false-positive leak from libresolv
- SERVER-90122 Construct a CycloneDX document for 7.0
- SERVER-90164 Prevent tests that hang while collecting
  minidumps from running on Windows
- SERVER-90168 Disable LTO buildvariants that are incompatible
  with Bazel
- SERVER-90173 Serialize ObjectId SBE type to key string
  correctly
- SERVER-90184 Only load included SASL plugins on Windows
- SERVER-90311 Update README.third_party.md mozjs with latest
  version
- SERVER-90394 Make the test update_node_clustertime_replset.js
  more resilient to $$NOW
- SERVER-90427 Remove the (without diagnostic latches) variant
- SERVER-90438 Coverity analysis defect 155571: Using a moved
  object
- SERVER-90485 $sort does not work as expected when used in
  conjunction with includeArrayIndex
- SERVER-90513 Check whether SSL_get0_verified_chain returns
  null before consuming it
- SERVER-90543 Transaction participant should hold client lock
  when configuring opCtx
- SERVER-90599 Remove unused link to liblzma (work ticket)
- SERVER-90657 [v7.0] Fix ignore_dbcheck_in_startup_recovery.js
  on 7.0
- SERVER-90678 Tag sharded incremental backups tests as
  resource intensive and skip running on smaller variants
- SERVER-90681 Fix data race over the chunk jumbo flag
- SERVER-90747 Handle $elemMatch with empty path in plan
  enumerator correctly
- SERVER-90770 On 6.0 and 7.0, $unionWith $search queries error
  for unsharded collections on a sharded cluster.
- SERVER-90777 Revert SERVER-71520
- SERVER-90830 Add retries to cloneing QA.git
- SERVER-90833 Fix incorrect bounded sort optimization when
  time field is renamed by $addFields
- SERVER-90853 Implement a linter for the sbom (for v7.0)
- SERVER-90866 [v7.0] Fix DeleteStage swallowing NEED_YIELD
- SERVER-90869 Disallow dotted full-path renames for
  '$elemMatch' expressions
- SERVER-90870 Update mongotmock and fix any tests
- SERVER-90891 uassert any attempt to add Decimal to V0 key
  string
- SERVER-90928 Make copybara prune out extra lines on commit
  messages
- SERVER-90985 AddToSetNode::init() should uassert if argument
  to $each is invalid BSON
- SERVER-90988 PrepareExecutionHelper destructor should use the
  cached value of CanonicalQuery::toStringShort that I specifically
  added just for that destructor to use
- SERVER-90991 Bump timeout on
  compile_and_run_unittests_*_quarter
- SERVER-91066 Set migrationCommitVersionError failpoint on all
  configsvr nodes in migration_coordinator_failover_include.js
- SERVER-91068 Remove read_ticket_exhaustion_with_stepdown test
- SERVER-91094 Make backports require codeowners
- SERVER-91166 Transactions in retryable_write_error_labels.js
  should update different documents
- SERVER-91176 Call awaitNodesAgreeOnAppliedOpTime in
  ignore_dbcheck_in_startup_recovery.js
- SERVER-91178 Handle a snapshot read performed at a timestamp
  before collection drop
- SERVER-91179 Skip jstests directory in codeowners for v7.0,
  v6.0, and v5.0
- SERVER-91182 Make schedule_global_auto_tasks and related
  "patch only"
- SERVER-91186 Move sys-perf to running on RHEL 9.4 machines.
- SERVER-91222 Make cluster_time_across_add_shard.js
  temporarily retry on KeyNotFound error after restarting the replica
  set
- SERVER-91256 Fix v7.0 sbom format and activate linter
- SERVER-91275 fix AL2023-arm64-cron-only-mongot-integration
  variant
- SERVER-91291 Skip
  etc/backports_required_for_multiversion_tests.yml in codeowners
- SERVER-91322 set evergreen config options in the
  multiversion-config subcommand
- SERVER-91324 Pin jepsen clones to a specific tag
- SERVER-91362 Performance: Do not copy JS "scope" object if a
  cached JsExecution exists
- SERVER-91407 Create SBOM for crypt_shared library for 7.0
- SERVER-91423 [v7.0] add detect_evergreen_config function
- SERVER-91435 Regenerate test certs with legacy flag
- SERVER-91494 Avoid past-the-end access of group by field in
  DocumentSourceBucket
- SERVER-91507 Update the sbom with mozjs new version on 7.0
- SERVER-91531 index_drop_before_running.js should wait for
  replication before asserting index drop on secondary
- SERVER-91558 Make HedgeCancellationTest resilient to
  operation interruption
- SERVER-91679 [v7.0] Pin puremagic library to 1.23
- WT-11092 Update s_clang_format to automatically download
  aarch64 binaries
- WT-11109 wt_wrap_open_cursor returns WT_NOTFOUND in
  test/format for a checkpoint cursor
- WT-12708 Evaluation/Revision of eviction random traversal
- WT-12863 Update the eviction target page check for selection
  of tree in eviction walk


## 7.0.11 Changelog

### Aggregation

SERVER-90297 Empty field match expression causes change stream
optimization rewrite failure

### Storage

#### WiredTiger

- WT-12900 Upload test/format failing CONFIG to Evergreen

### Internals

- SERVER-76231 Validate should not fail immediately when it
  detects out-of-order keys
- SERVER-76232 Do not crash when index inconsistencies are
  detected in WiredTiger
- SERVER-77561 Rollout resmoke file system logging
- SERVER-79014 Update the hasKilledSessionError() helper to
  also check the writeError key for an Interrupt code
- SERVER-81454 Timeseries $geoNear throws unexpected error with
  lookup
- SERVER-82305 Have dbCheck ignore prepare conflicts on
  secondaries
- SERVER-82764 Make "planningTimeMicros" incorporate time from
  the multi-planner trial period
- SERVER-85279 Don't run the FTDC collection stats collector on
  arbiters
- SERVER-85446 Retry on network error in
  multiversionconstants.py
- SERVER-86280 Reclassify some collection validation
  warnings/errors
- SERVER-86904 Conflict between initial sync setting the oldest
  timestamp and resharding pinning the oldest timestamp
- SERVER-87059 Setting the cluster cardinality parameter may
  cause setFCV to fail on retry
- SERVER-87087 Validate unique index ordering check does not
  work for clustered collections
- SERVER-87373 prepareUnique index option FCV compatibility
  check shouldn't be performed during startup
- SERVER-87661 create LAST_GREEN binary for mongot
- SERVER-88072 Timeseries query errors instead of producing a
  correct response
- SERVER-88098 Add try/catch to notablescan.js to reduce
  testnoise
- SERVER-88263 Move direct connection warnings to the
  collection acquisition (and AutoGetCollection)
- SERVER-88318 Fail dbcheck if one batch failed waiting for
  write concern
- SERVER-88518 Re-evaluate the number and size of partitions in
  the query stats store.
- SERVER-88651 Ensure resharding metrics object still exists
  when reporting currentOp info
- SERVER-88694 Do not emit error logs for self-recovering
  scenarios in BalancerStatsRegistry
- SERVER-88978 Resharding coordinator should ensure
  participants have seen kAbort before dropping temp collection metadata
- SERVER-89418 CursorManager loses track of registered cursors
  for queries with multiple executors
- SERVER-89490 Return ErrorCodes::NetworkTimeout in LDAP
  connection pool
- SERVER-89495 Disable test parameters even when no
  setParameters are specified
- SERVER-89625 Handle directoryPerDb and
  wiredTigerDirectoryForIndexes correctly when reporting namespaces and
  UUIDs during a backup
- SERVER-89859 Make move_chunk_deferred_lookup.js more robust
  to slower variants
- SERVER-89904 Update Jepsen version for "jepsen-docker" tests
- SERVER-89930 Validates the $densify stage properly if
  'partitionByFields' contains the densifying field
- SERVER-89933 Remove shard split performance test
- SERVER-89939 Limit logs used for direct connection log
  ingestion to be once per hour
- SERVER-89943 Feature flag util must retry upon errors in
  suites with stepdowns and kill primary
- SERVER-89989 Extend sharded_backup_restore.js to perform
  incremental backups
- SERVER-90020 Explicitly use 1 config server for
  mongos_api_params_util tests
- SERVER-90053 [v7.0] Add SERVER-89921 TODOs to uncomment parts
  of the tests once relevant tickets are backported
- SERVER-90054 Make scoped_db_connection_test not flaky
- SERVER-90069 run_restore.js and run_restore_unsharded.js
  shouldn't enforce fast count
- SERVER-90090 Update Amazon 2 distros to the latest
- SERVER-90091 Robustify change stream split event tests
  against identical events
- SERVER-90112 Do not call FeatureFlag::isEnabled in
  audit::log*ClusterParameter
- SERVER-90116 Backup file cursors should require system
  authorization
- SERVER-90135 Ensure the Windows system CA stores are in a
  clean state at the start of ssl_linear tests
- SERVER-90170 Do not use jsTestName() in explain_skip.js
- SERVER-90187 Cleanup multiversion binaries before running
  resmoke tests
- SERVER-90199 Tag that index_startup_prepareunique.js tests
  requires replication.
- SERVER-90232 Modify multiversion suites to not run jstests
  that depend on building mongod with diagnostic latches
- SERVER-90238 [7.0] Enable query stats in the query stats
  passthroughs
- SERVER-90248 Insert _id field into audit config cluster
  parameter
- SERVER-90264 Remove slow step from compile
- SERVER-90288 Bitwise query operators should interpret lowest
  addressable byte in BinData as least significant byte
- SERVER-90320 Log connection statistics in
  WiredTigerStatsTest::EmptySession
- SERVER-90443 Update testing for enterprise aggregate stage
- SERVER-90630 Make packager aware of sbom json file
- WT-10802 Handle EBUSY error when checkpointing in test/format
- WT-11972 Refresh application thread snapshot if eviction
  didn't make progress
- WT-12609 Improve checkpoint cleanup and page eviction logic
