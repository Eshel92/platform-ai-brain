<!-- Part 2 of 10 of release-notes/7.0-changelog.md (split because the page is big). -->

## 7.0.31 Changelog

### Query

- SERVER-95374 Compound wildcard indexes can incorrectly push
  down predicates during union or planning
- SERVER-113319 $match pushdown past a renamed field is done
  incorrectly when the expression root is a renamed field path
  expression

### Schema

WT-14140 Unnecessary schema lock taken for active "file:"
dhandles that are not swept

### Storage

- SERVER-108699 Check BSON size in collection validation
- WT-12349 Fix __wt_modify_reconstruct_from_upd_list behaviour
  with read-uncommitted snapshot
- WT-12535 Optimize time spent in __wt_update_obsolete_check()
- WT-15803 Fix ref not unlocked in error cases

#### WiredTiger

- WT-13612 Time aggregate merge logic incorrect for chunk
  merge, page split scenario
- WT-13627 Assertion failed: 'ts == 1 || ts == 0'. out-of-order
  timestamp update detected
- WT-14273 Report a stat for how long it's been since a page
  was last queued for eviction
- WT-14843 Add stats to track eviction pages seen and queued

### Internals

- SERVER-55068 Max incoming connections currently set to 80% of
  max open files, but each connection consumes 2 file descriptors
- SERVER-60823 runCommandWithRetries in JS test framework
  exceeds JS interpreter recursion limit
- SERVER-78241 Truncated log line shows number of remaining
  strings instead of truncated strings
- SERVER-82688 mongod crash, bug fix when connections >
  wiredtiger's session_max
- SERVER-86278 Investigate discrepancy between ShardLocal and
  ShardRemote aggregations
- SERVER-88234 Fix write concern metrics tests
- SERVER-89870 Rate limit JWKManager::getValidator
- SERVER-91045 Load JWKs immediately at startup regardless of
  JWKSMinimumQuiescePeriodSecs
- SERVER-91503 Improve NoSuchTransaction error message for
  transactions
- SERVER-93154 Emit abortIndexBuild change event
- SERVER-93560 Avoid hot-path logging in txn override
- SERVER-96103 Fix argument quoting in Windows shell
  ProgramRunner
- SERVER-99623 High CPU usage in range deleter service
- SERVER-101491 Quiesce in JWKFetcherImpl when remote returns
  5xx error
- SERVER-101758 Adding a new local-only task executor for node
  local tasks
- SERVER-102927 evergreen/failed_unittests_gather.sh misses
  .debug symbol file due to earlier error in the script
- SERVER-103148 Prevent writeConcernError from going out of
  scope in DBDirectClient helpers
- SERVER-103774 Disallow compound wildcard indexes from being
  used as a shard key index
- SERVER-104810 Support PS256 JWS Signing Algorithms for OIDC
- SERVER-106194 CheckMetadataConsistency is not reading chunks
  with snapshot read concern
- SERVER-106310 Add more logging to invariant failure when
  trying to set commit timestamp for transaction
- SERVER-106360 Disable stacktrace symbolization for resmoke
  tasks by default
- SERVER-106778 RSA_PSS_SALTLEN_DIGEST not supported in older
  OpenSSL
- SERVER-107304 Make Pipeline::dispose() idempotent
- SERVER-110149 Coverity analysis defect 176559: Using a moved
  object
- SERVER-110442 Capture Information about index build durations
- SERVER-110953 Check no orphaned document is present on a
  recipient shard before starting cloning a range
- SERVER-112229 Backport gitignore for new auto_header tool
- SERVER-112529 Temporarily disable external_data_source.js in
  concurrency_compute_mode
- SERVER-113153 Make query multiversion fuzzers on LTS versions
  deterministic
- SERVER-113431 Pin copybara to a specific tag
- SERVER-113545 Wait for lastCommittedOpTime to be initialized
  after restart in api_version_prepare_txn.js
- SERVER-113700 Update copybara to v20251110
- SERVER-114017 move_primary_setFCV.js test creates database at
  latest FCV instead of downgraded FCV
- SERVER-114337 Index build lastCommittedMillis should be int64
- SERVER-114363 Capture index build blocking replication
  metrics
- SERVER-114867 Define RSA_PSS_SALTLEN_DIGEST if not defined by
  OpenSSL
- SERVER-115398 Differentiate between steady-state replication
  and startup recovery for lastTimeBetweenCommitOplogAndCommitMillis
- SERVER-115917 Set specific Visual Studio and MSVC install
  version
- SERVER-115962 Balancer does not make progress when the most
  loaded shard is already balanced within its zones
- SERVER-118428 mongocryptd rejects large messages
- SERVER-118713 [v7.0.30] Can not create timeseries 2dsphere
  index with a non-system user
- SERVER-118849 Double free in SBE hash table spill
- SERVER-119317 Improve object lifecycle of MD5 hash state
- SERVER-119319 Fix ExpressionContext use-after-free bug
- SERVER-119396 Adjust maximum buffer size for ingress network
  messages
- WT-11529 Stop allowing checkpoint cursors to attempt eviction
- WT-13746 Conflict between RTS and eviction regarding
  btree->rec_max_timestamp (take 2)
- WT-15251 Skip test_sweep04 on 8.0


## 7.0.30 Changelog

### Internals

SERVER-118713 [v7.0.30] Can not create timeseries 2dsphere
index with a non-system user


## 7.0.29 Changelog

### Sharding

SERVER-94315 Shard filtering bug with collation

### Internals

- SERVER-99119 Change geo-related invariants to tasserts
- SERVER-112952 tighten profile command auth check
- SERVER-113532 [8.0] Introduce a new CursorResponseBsonSize
  limit of 16MB+32KB
- SERVER-113685 Segfault for query on compound wildcard index
- SERVER-113897 Report existence of invalid compound wildcard
  index
- SERVER-113900 Add run-time check to plan enumerator code
- SERVER-114695 Update default value for pending connections
- SERVER-114838 Lock Manager is susceptible to an adversarial
  DDOS attack
- SERVER-115296 Redact ResourceId raw values from error
  messages
- SERVER-115693 Fix detecting current git repo on windows
- SERVER-116206 Better exception handling for message compressors
- SERVER-116210 Adjust the maximum buffer size for ingress requests
- SERVER-116211 Cap memory allocated by network buffers


## 7.0.28 Changelog

### Internals

SERVER-115508 Make minimally sized buffers for uncompressed
Messages


## 7.0.26 Changelog

### Query

- SERVER-98461 findAndModify where query does not have shard
  key does not return WCE on failure
- SERVER-103519 Ensure update and bulkWrite commands return WCE
  in sharded cluster case

### Storage

#### WiredTiger

- WT-9575 Pages with updates newer to the oldest txn id are not
  queued for eviction

### Build and Packaging

SERVER-112367 [v7.0] Fix spurious multiversion change stream
test failure

### Internals

- SERVER-76547 Create command on a time-series collection is
  not idempotent
- SERVER-77172 "abortExpiredTransactions" thread can get stuck
  if it fails to checkout a session
- SERVER-82071 Prevent users from specifying a lower max than
  min bound in merge chunks command
- SERVER-82180 Capped inserts on the primary can have a
  different natural ordering from secondaries
- SERVER-82243 Fix data race in lookupARecords
- SERVER-84081 FLE2 write error hides write concern error
- SERVER-86299 Test and fix FLE2 writeConcernError reporting in
  sharded writes
- SERVER-86591 Enhance InitialSync Error Handling for Transient
  Network Issues
- SERVER-86727 Consider changing
  MigrationDestinationManager::cloneCollectionIndexesAndOptions to not
  take DB MODE_X lock
- SERVER-87194 Force merge chunk command to only accept
  non-empty ranges
- SERVER-89039 Support a command that returns after an index
  build has started
- SERVER-90495 Support start or resume from deleted recordId on
  natural order scan
- SERVER-92236 Chunk migrations should use short lived
  cancellation sources
- SERVER-92275 Improve test to check that list collections is
  consistent with the durable catalog
- SERVER-93153 Emit startIndexBuild change event
- SERVER-93400 timeseries_insert_mixed_schema_bucket.js needs
  to guard against collmod timing
- SERVER-93672 Fix concat error in multiversionconstants.py
- SERVER-94327 Add unittest for killAllExpiredTransactions
- SERVER-94618 Replace optional chaining syntax in
  create_indexes_return_on_start.js
- SERVER-95423 Count insertion failures in SASL SCRAM cache
- SERVER-95919 Asserts that all the aggregation stages have
  auth tests
- SERVER-96839 Pass writeConcern from UMCs into UMCTransaction
- SERVER-97201 Add a metric in FTDC for replication coordinator
  mutex wait time
- SERVER-97641 Remove LdapHealthObserver unit test's dependency
  on ldaptest.10gen.cc
- SERVER-98729 Fix shutdown race condition in
  repl_monitor_refresh.js
- SERVER-99868 Improve debuggability of
  batch_write_exec/batch_write_op
- SERVER-99915 FLE2 findAndModify should also return WCE from
  transaction API result
- SERVER-100528 Investigate all commands that accept write
  concern for WCE handling
- SERVER-100936 Mongos must return WCE as a top-level error for
  create collection
- SERVER-100937 Mongos must return WCE on dropIndexes
- SERVER-100938 Mongos must return WCE on createIndexes
- SERVER-100939 Mongos should return WCE on no-op
  setFeatureCompatibilityVersion
- SERVER-100942 setDefaultRWConcernDefault must return WCE
- SERVER-100943 abortTransaction must wait for write concern
  and return WCEs on failure
- SERVER-101178 Apply important upstream ICU fixes to our
  vendored copy
- SERVER-101386 Test all commands that accept write concern
  against timeseries collections
- SERVER-101387 Test all commands that accept write concern
  against FLE collections
- SERVER-102266 7.0 -- Coverity analysis defect 169977: Data
  race condition
- SERVER-102428 Logical initial sync allocates double
  maxIndexBuildMemoryUsageMegabytes
- SERVER-102477 Revert change preventing tuning
  taskExecutorPoolSize on 7.0+
- SERVER-102571 Check against WriteConcernError category when
  processing QE transactions
- SERVER-102670 [v8.1] Incorrect ordered time-series insert
  error handling
- SERVER-102983 Logical initial sync reports compounding index
  build memory use
- SERVER-103664 Ensure Operations Are Quiesced Before Stopping
  Secondaries in
  mongos_writes_wait_for_write_concern_sharded_addl_crud_ops.js
- SERVER-103742 opWriteConcernCounters can illegally embed a
  NUL bytes into ServerStatus
- SERVER-103960 Impose a proper check on the field path to
  ensure the number of parts not exceeding 255
- SERVER-104220 Router must take into account drop collection
  write concern error
- SERVER-104543 Don't fail stacktrace collection if we're
  unable to resolve a symbol
- SERVER-104839 Add a new log line that contains both metadata
  and authentication info
- SERVER-105041 [v8.0] Pin the MSVC version on released
  branches
- SERVER-105263 Resmoke blocks completion of passing tests on
  symbolization of failing tests from other jobs
- SERVER-105424 Handle yield and restore in direct shard
  connection warnings
- SERVER-105528 Fix FLE2 findAndModify write concern error
  reporting in mongod
- SERVER-106075 Prepared Transactions with apiVersion Fail to
  Resume After Primary Failover
- SERVER-106162 [test-only] Reevaluate ignoring write concern
  errors in drop FSM state
- SERVER-106354 Missing resource lock acquisition when applying
  batch of inserts to a capped collection
- SERVER-106492 Include multiplanner metrics in FTDC
- SERVER-106589 Provision more memory for index builds during
  initial sync
- SERVER-106875 Really deregister all collections when closing
  CollectionCatalog
- SERVER-106965 [v8.0] create shared scons cache directory
- SERVER-106988 [v8.0] Fix ninja + icecream generation
- SERVER-107361 Rollover determination in the bucket catalog
  can fail to check mixed schema for large measurements
- SERVER-107429 [v7.0] Prepare SPM-4070 7.0 branch for release
- SERVER-107852 Server SBOM rebuild to master/v8.x/v7.0
- SERVER-107924 Make RateLimitIsValidAfterQueueing test
  resilient to slow machines
- SERVER-108366 Prepared Transactions with apiVersion
- SERVER-108565: Improve handling of oversized writes to time series 
  collections.
- SERVER-108800 Use retryable session for config writes in
  check_metadata_consistency.js
- SERVER-109435 Improve error collection for
  mongod_proxy_protocol.js
- SERVER-109493 Disable "uncaught exception in noexcept"
  Coverity check
- SERVER-110119 Coverity analysis defect 176642: Using a moved
  object
- SERVER-110124 Coverity analysis defect 176627: Using a moved
  object
- SERVER-110130 Coverity analysis defect 176613: Using a moved
  object
- SERVER-110132 Coverity analysis defect 176604: Using a moved
  object
- SERVER-110133 Coverity analysis defect 176603: Using a moved
  object
- SERVER-110141 Coverity analysis defect 176586: Using a moved
  object
- SERVER-110146 Coverity analysis defect 176577: Using a moved
  object
- SERVER-110161 Correct $_startAt behavior to stop skipping
  documents
- SERVER-110252 Add delays in
  audit_remote_local_intermediate.js
- SERVER-110425 Develop and add an Evergreen task to upload
  SBOM to Kondukto using SilkBomb for master, v7.0, v8.0, v8.1, v8.2
- SERVER-110618 Coverity 7.0 QI Batch Fixes
- SERVER-110675 python dep is breaking 7.0 builds
- SERVER-110890 Coverity analysis defect 175049: Logically dead
  code
- SERVER-111135 Retry configureFailPoint in rollback_test.js
- SERVER-111427 Load SASL before locking code pages
- SERVER-111460 Pin code pages for mongos
- SERVER-112035 Downgrade proxy protocol disconnected to INFO
- SERVER-112375 [v7.0] Tag timeseries_create.js with
  requires_fcv_70
- SERVER-112467 Track and report the number of pending proxy
  connections
- SERVER-113256 [Summary] write concern error reporting issues


## 7.0.25 Changelog

### Internals

SERVER-105873 QueryPlannerParams should not maintain pointers
owned by the IndexCatalogEntry


## 7.0.24 Changelog

### Storage

#### WiredTiger

- WT-14391 Check eviction server is running before opening HS
- WT-14653 Add logs/stats to reconciliation for tracking HS
  updates

### Internals

- SERVER-92411 Test all the document-source aggregation stages
  have auth checks
- SERVER-99146 [v8.0] Disallow committing imports of
  ShardingTest and ReplSetTest on 8.0 and lower branches
- SERVER-99693 Fix hang analyzer crash when process_ids is
  empty
- SERVER-102017 [v8.0] Log startup warning when
  disableJavaScriptJIT is set
- SERVER-102224 7.0 -- Coverity analysis defect 170751:
  Uninitialized scalar field
- SERVER-102483 [v7.0] Fix data races in UserAcquisitionStats
  class in 7.0
- SERVER-103505 Handle metadata errors in
  WiredTigerUtil::setTableLogging
- SERVER-103642 Rename sdp-triager to devprod-build-automation
- SERVER-103741 Add profile collection metrics
- SERVER-103783 Fix expected NAN string on windows in IDL test
- SERVER-104771 [v7.0] Initial sync fails when the source has
  TTL indexes on a capped collection
- SERVER-105219 Increase timeout for s390x
- SERVER-105336 [7.0] Remove multiversion tasks from Debian 11
  variants
- SERVER-108091 [v8.0] Fix race in
  jstests/noPassthrough/indexbg_killop_stepdown.js in 7.0 and 8.0
- SERVER-108449 Fix allowed_requesters for SAST report
  generation
- SERVER-109679 [v7.0] Disable
  connection_establishment_rate_limiting_stats.js on macos


## 7.0.23 Changelog

### Sharding

- SERVER-95324 Disable chunkMigrationConcurrency
- SERVER-105799 Ensure that failpoints used in
  check_metadata_consistency_timeout_tests.js are reached on slow
  machines

### Internals

- SERVER-52121 Create feature flag for Limit concurrent ingress
  connection handshakes
- SERVER-52424 Enable feature flag for Limit concurrent ingress
  connection handshakes
- SERVER-75523 Create clang-tidy rule banning use of
  "no_unique_address"
- SERVER-81797 Make our own portable implementation of atomic
  notify() and wait() with timeout support
- SERVER-86656 Create a reader-optimized reader-writer mutex
- SERVER-90424 A reader-friendly reader-writer mutex type
- SERVER-101135 priority_takeover_two_nodes_equal_priority.js
  should use lower electionTimeoutMillis
- SERVER-101381 query_with_txn_prepared.js should relax
  document count check
- SERVER-101495 auth_no_pri.js should use a lower
  electionTimeoutMillis
- SERVER-101581 Check socket state before accepting connection
  in ASIO
- SERVER-101800 Investigate OpenSSL 3 regression in HMAC
  functions
- SERVER-102719 Guarantee that FCBIS tests have non-0
  durationMillis
- SERVER-103934 FCBIS should be able to call
  KVEngine::cleanShutdown without leaking memory
- SERVER-104168 Vendor in folly token bucket util
- SERVER-104407 Introduce server parameters to tune connection
  establishment rate limiter
- SERVER-104408 Introduce admission::RateLimiter component
- SERVER-104412 Exempt prioritized connections from token
  acquisition
- SERVER-104413 Add metrics to admission::RateLimiter component
- SERVER-104415 Integrate connection establishment rate limiter
  into SessionWorkflow
- SERVER-104771 [v7.0] Initial sync fails when the source has
  TTL indexes on a capped collection
- SERVER-104811 Update "connections" server status section for
  maxEstablishing
- SERVER-104814 Add establishment timing metrics to
  IngressHandshakeMetrics
- SERVER-105502 Use assert.soon for metrics assertions in
  connection_establishment* tests
- SERVER-105526 Add additional debug logs and a deadline to
  ConcurrentTokenAcquisitionWithQueueing test
- SERVER-105670 Ensure ConcurrentTokenAcquisitionWithQueueing
  actually waits until all waiters are sleeping
- SERVER-105693 Make
  connection_establishment_rate_limiting_exemptions.js resilient to
  different connection closed errors
- SERVER-105753 Ensure connection establishment rate limiter UX
  consistency with operation rate limiter
- SERVER-106045 Rename burstSize => burstCapacitySecs parameter
- SERVER-106149 RateLimiter should return tokens to bucket upon
  rejection
- SERVER-106166 Don't append Inf to FTDC for
  totalAvailableTokens
- SERVER-106487 point_in_time_lookups_drop_pending.js is flaky
  when checking that a PIT read creates a new instance for the
  collection after a drop
- SERVER-106622 Do fuzzy assertions for all doubles in
  rate_limiter_util_test
- SERVER-106636 Use longer timeout when waiting for all threads
  to queue in ConcurrentTokenAcquisitionWithQueueing test
- SERVER-107208 [v7.0] Add basic testing for SERVER-107165
- SERVER-107217 [v7.0] Add robust testing for SERVER-107165
- SERVER-107245 [v7.0] Fix
  agg_yielding_during_runtime_planning.js
- SERVER-107272 Write Evergreen task for SAST report generation
- SERVER-107282 [v8.1] Update CODEOWNERS to expand test-only
  definition
- SERVER-107321 [v7.0] Prepare maxEstablishing backport branch
  for 7.0
- SERVER-107534 Introduce VersionedValue
- SERVER-108539 [v7.0] Remove faulty includes in
  MongoNoUniqueAddressCheck tidy check
