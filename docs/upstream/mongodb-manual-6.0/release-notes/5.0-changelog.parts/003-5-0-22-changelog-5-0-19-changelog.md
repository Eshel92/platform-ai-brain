<!-- Part 3 of 12 of release-notes/5.0-changelog.md (split because the page is big). -->

## 5.0.22 Changelog

### Sharding

- SERVER-40459 Optimize the construction of the balancer's
  collection distribution status histogram
- SERVER-79086 Deletion of ReshardingCoordinatorService state
  document is not idempotent
- SERVER-79327 Missing verification in refine collection shard
  key
- SERVER-79682 ShardsvrReshardCollection Can Hang If Stepdown
  Occurs Shortly After Stepping Up
- SERVER-80236 Race in migration source registration and
  capturing writes for xferMods for deletes
- SERVER-80712 Avoid leaving the replica set shard partitioned
  at the end of linearizable_read_concern.js

### Operations

- SERVER-58534 Collect FCV in FTDC
- SERVER-68548 mongo shell version 4.4.15 logging asio message
  despite --quiet flag
- SERVER-77610 Log session id associated with the backup cursor

### Internals

- SERVER-52149 Create feature flag for Make taking self-managed
  backups in 4.4+ as safe as possible
- SERVER-52452 Enable feature flag for Make taking self-managed
  backups in 4.4+ as safe as possible
- SERVER-60156 Add a way to bypass storageValid() for
  time-series updates
- SERVER-60176 Delta-updates should only validate the diff for
  storage
- SERVER-68132 Remove Feature Flag for PM-2076
- SERVER-68791 Expand the stacktrace API to return a loggable
  BSONObj
- SERVER-71053 Fix dataSize can be negative and incorrect on
  rollback
- SERVER-73470 Log index inconsistencies detected by queries in
  the health log
- SERVER-73497 Create an interface for the HealthLog
- SERVER-74303 Add a sizeStorer call to the onRollback handler
  for dataSize and numRecords changes
- SERVER-76341 Add range deletion throughput statistic
- SERVER-77638 Add logging on completion of resharding
- SERVER-78149 Implement the mongos fsync (lock : true) command
- SERVER-78150 Implement the mongos fsyncUnlock command
- SERVER-78151 Add fsyncLock status to the mongos currentOp
  command
- SERVER-78153 Unlock the config server primary via the mongos
  fsyncUnlock command
- SERVER-78156 Test the mongos fsync with lock command with
  distributed transactions
- SERVER-78217 Renaming view return wrong error on sharded
  cluster (2nd attempt)
- SERVER-78252 Block chunk migrations for hashed shard keys if
  you don’t have the shard key index
- SERVER-78253 Allow folks with hashed shard keys to drop the
  hashed index
- SERVER-78342 nReturned in slow query is incorrect when no
  docs are matched
- SERVER-78384 mongos should allow --port 0
- SERVER-78505 Database cache does not use the 'allowLocks'
  option correctly
- SERVER-78529 Create feature flag
- SERVER-78530 Enable feature flag
- SERVER-78687 Set up copybara syncing between 10gen/mongo and
  10gen/mongo-copybara
- SERVER-78793 Add a timeout to the mongos FSync Lock Command
- SERVER-79025 Mongos Fsync with lock command should use mongos
  fsyncUnlock command
- SERVER-79126 Pin pyyaml in another place
- SERVER-79251 Test dropping hashed shard key index mid chunk
  migration aborts migration
- SERVER-79471 Mirrored reads should include databaseVersion in
  addition to shardVersion
- SERVER-79552 $group rewrite for timeseries returns incorrect
  result if referencing the metaField in an object
- SERVER-79632 Stop range deletion when hashed shard key index
  does not exist
- SERVER-79781 TestGetDestinedRecipientThrowsOnBlockedRefresh
  should not run two refreshes without resetting the catalog cache
  loader mock return value
- SERVER-79926 Investigate OCSP failure possibilities
- SERVER-79975 [Classic] Optimize large group keys
- SERVER-80021 Make $convert round-trip correctly between
  double and string
- SERVER-80100 Fix typo in excluding
  compound_wildcard_index_hiding.js and sparse_index_internal_expr.js
- SERVER-80140 Use the $currentOp to verify that
  fsyncLockWorker threads are waiting for the lock
- SERVER-80157 ExclusionProjectionExecutor forces Document
  cache to load excluded fields
- SERVER-80203 Normalization of time-series meta field can
  break insert targeting
- SERVER-80234 Catalog cache unit tests of allowLocks should
  block the refresh
- SERVER-80484 Disable libfuzzer on v5.0
- SERVER-80491 Expose more granular metrics around balancing
  round
- SERVER-80499 Fix use-after-free in planShardedSearch
- SERVER-80643 large_events_failed_metric.js fails because
  change steram pre-images are not supported in v5.0
- SERVER-80678 Remove an outdated test case
- SERVER-80703 Avoid traversing routing table in
  MigrationDestinationManager
- SERVER-80737 [5.0] slow_query_log_stats_not_block_on_RSTL.js
  requires lock-free reads support
- SERVER-80809 Make _logOplogEntriesForInvalidResults resilient
  to non-existing oplog
- SERVER-80982 Rename collection coordinator should use the
  view catalog to check if a view exists
- SERVER-81106 Recipient shard doesn't wait for the collection
  version to be locally persisted before starting the cloning phase
- SERVER-81155 Use move semantic to avoid copying all chunks in
  createCollection coordinator
- SERVER-81201 Limiting the memory usage during the cloning
  phase on the recipient shard
- SERVER-81202 Use host environment when signing
- SERVER-81431 Add canaries_only task to older mongo branches
- SERVER-81904 Address test-only issue in UpdateChunkMapRandom
  unit test
- SERVER-81966 Avoid modification of previous ChunkMap
  instances during refresh
- SERVER-81985 FlushRoutingTableCacheUpdates command should not
  be allowed on databases
- SERVER-82003 powercycle tests are missing variables
- SERVER-82070 Classic window function $stdDevSamp handles
  empty window frame incorrectly
- WT-8614 Make format.sh more verbose for failure diagnosis
- WT-10207 Fix log slot flags and remove debugging added for
  WT-9796
- WT-10624 Fix regression on x86 for search and insert
- WT-11064 Skip globally visible tombstones as part of update
  obsolete check
- WT-11168 Remove the page image reuse logic
- WT-11359 Update spinlock tasks to limit disk usage


## 5.0.21 Changelog

### Sharding

- SERVER-60466 Support drivers gossiping signed $clusterTimes
  to replica set --shardsvrs before addShard is run
- SERVER-67529 Resharding silently skips documents with all
  MaxKey values for their fields under the new shard key pattern
- SERVER-78036 Handle the race between the getting and setting
  of the LogicalTimeValidator during sharding initialization
- SERVER-79771 Make Resharding Operation Resilient to
  NetworkInterfaceExceededTimeLimit

### Internals

- SERVER-50606 NetworkInterfaceTest needs to be more permissive
  with async op timeout
- SERVER-59419 OperationContext::_ignoreInterrupts can be
  written to without synchronization by IgnoreInterruptionsGuard
  destructor
- SERVER-61732 Prevent threads spawned outside
  ThreadContextTest from updating test counters
- SERVER-69793 Disable memory underflow check in the query
  system
- SERVER-71627 Refreshed cached collection route info will
  severely block all client request when a cluster with 1 million chunks
- SERVER-73394 Remove misleading operationsBlockedByRefresh
  metrics
- SERVER-75255 Remove all outdated entries from
  backports_required_for_multiversion_tests.yml
- SERVER-77382 Null embedded metaField for creating a
  time-series collection leads to invalid BSON index spec
- SERVER-78369 ignoreUnknownIndexOptions doesn't account for
  the 'weights' index field
- SERVER-78950 Use sequential time series bucket IDs when
  possible
- SERVER-78971 Skip shutting down Grid::getExecutorPool() when
  TestProctor is disabled
- SERVER-78987 Remove the free monitoring code from
  mongodb/mongo repo
- SERVER-79022 Update ASIO's Git hash in README.third_party.md
- SERVER-79252 Add the system-perf bootstrap file to the task
  Files section
- SERVER-79261 Add logging to ping monitor
- SERVER-79382 Reset bucket OID counter when encountering a
  collision
- SERVER-79397 Fix and test logic to internally retry time
  series inserts on OID collision
- SERVER-79609 Fix findAndModify_upsert.js test to accept
  StaleConfig error
- SERVER-79651 Only use two node replicasets in initial sync
  performance tests
- SERVER-79861 Delete rosetta builders
- SERVER-79885 Oplog fetching getMore should not set null
  lastKnownCommittedOpTime if it is not using exhaust cursors
- SERVER-80183 Remove operationTime check from
  store_retryable_find_and_modify_images_in_side_collection.js
- SERVER-80302 capped_large_docs.js is not resilient to
  replication rollback
- SERVER-80488 Avoid traversing routing table in balancer split
  chunk policy
- SERVER-80499 Fix use-after-free in planShardedSearch
- WT-7492 Ignore the evict drain wait msg in stdout.txt for
  test_cursor_random
- WT-10380 Fix expected warning output in test_cursor_random:
  Eviction took more than 1 minute
- WT-10432 Fix expected warning output for test_hs20 on macos
- WT-10759 Do not retry to force evict history store pages
  during reconciliation
- WT-11051 Fix newest start durable timestamp comparison in
  aggregate timestamp validation
- WT-11221 Python tests fails due to unexpected "Eviction took
  more than 1 minute" warning in standard output


## 5.0.20 Changelog

### Sharding

- SERVER-44422 Allow findAndModify and delete one to target by
  query instead of extracted shard key
- SERVER-62987 Wrong replication logic on refreshes on
  secondary nodes

### Internals

- SERVER-54344 Interruptible's Atomic timer parameter is not
  typesafe
- SERVER-58618 Sleep intervals in interruptible_test cause
  imprecision
- SERVER-58958 Temporarily disable
  Interruptible::WaitUntilDeadline test
- SERVER-58959 Fix and reenable
  Interruptible::WaitUntilDeadline test
- SERVER-71335 Debug symbols of server binaries used by
  system_perf.yml are archived in S3
- SERVER-73841 Enable feature flag
- SERVER-74143 A slow query report should not require the rstl
  lock to return storage statistics
- SERVER-74451 Implement limit pushdown to mongot cursor
- SERVER-74453 Implement support for getMore against a mongot
  cursor created with a user-defined limit
- SERVER-74701 Add checksum verification for blackduck
  installer
- SERVER-74954 Incorrect result when contained $or rewrites
  $elemMatch extra condition
- SERVER-75648 Add limit pushdown info to explain output
- SERVER-76299 Report writeConflicts in serverStatus on
  secondaries
- SERVER-76404 Call the no-prefetch TaskExecutorCursor if there
  is an extractable limit
- SERVER-76828 Increase test coverage for RoutingTableHistory
  and ChunkMap
- SERVER-77299 Pooled LDAP connections may reference
  out-of-scope memory after timeout
- SERVER-77654 Having more constraints on time-series
  collection timeField name
- SERVER-77856 Provide Atlas with a way to choose a specific
  initial sync sync source
- SERVER-78229 createIndexes should acquire the CollectionLock
  of the targeted nss before accessing the parent DatabaseShardingState
- SERVER-78251 move_chunk_deferred_lookup.js can fail if mongos
  RSM is stale after stepup
- SERVER-78333 DocumentSourceSearchMeta on 5.0/4.4 don't
  correctly specify involved collections
- SERVER-78410 Suppress debug election log messages in rollback
  resumable index build tests
- SERVER-78434 never implicitly shard a view in
  implicitly_shard_accessed_collections.js
- SERVER-78525 Update
  jstests/noPassthrough/metadata_size_estimate.js to use a smaller
  document size
- SERVER-78676 Replace c-string constructor with fill
  constructor in CurrentOpExhaustCursorTestFixture::initTestCollection
  on v5.0
- SERVER-78751 $collStats should check for presence of time
  series options rather than relying on namespace checks
- SERVER-78789 Distribute roles in metadata sizing test
- SERVER-78828 LDAP host timing data can be inconsistent during
  sorting
- SERVER-78888 Unschedule Mix js
- SERVER-79136 Incorrect query result of $match + $group on
  metaField over time-series
- SERVER-79592 [v4.4, v5.0] Avoid server crash when using
  positional projection with collation
- WT-8340 Fix overflowed value in Btree atomic flags of 8 bit
  type
- WT-10197 Track eviction timeline
- WT-10424 cursor::search_near slow performance if many deleted
  items are present
- WT-10449 Do not save update chain when there are no updates
  to be written to the history store
- WT-10522 Fix a bug that leads to an unexpected aborted
  tombstone on update chain
- WT-10585 Record the location of the last key in key order
  check
- WT-10911 Investigate and update eviction timeline metrics
  that are showing up incorrectly
- WT-11031 Fix RTS to skip tables with no time window
  information in the checkpoint
- WT-11312 Fix incorrect flag check for accurate force eviction
  stat
- WT-11374 Fix comparison of txnid to timestamp in row_modify
  (v5.0)
- WT-11380 Temporarily disable compile-clang task on 5.0


## 5.0.19 Changelog

### Sharding

- SERVER-6491 Prevent dropping shard key index when alternative
  index doesn't exist
- SERVER-64950 Use a named ErrorCode when asserting that you
  can't drop the last shard key index
- SERVER-67732 mongod shutdown procedure doesn't shutdown the
  Grid::getExecutorPool()
- SERVER-73848 Hashed shard keys with zones can cause issues
  with resharding
- SERVER-76056 countDocsDeletedOnDonor name is misleading
- SERVER-76546 _migrateClone can deadlock with prepared
  transactions on secondaries
- SERVER-76948 Allow shard key fields to contain DBRefs
- SERVER-78050 Chunk Migration Can Lose Data If Processing
  Deferred Modifications
- SERVER-78414 Recipient shard in chunk migration can skip
  fetching changes to the migrated range, leading to lost writes

### Query

SERVER-75922 Partial unique indexes created on MongoDB 4.0 can
be missing index keys after upgrade to 4.2 and later, leading to
uniqueness violations

### Internals

- SERVER-62854 ShardingCatalogManager::removeShard should
  prevent concurrent remove shard commits
- SERVER-64706 Create Feature flag for PM-2802
- SERVER-67699 Add tracking for when change stream event
  exceeds 16Mb
- SERVER-70242 Intracluster X509 authentication can trigger
  "Different user name was supplied to saslSupportedMechs"
- SERVER-70973 Balancer should stop iterating collections when
  there are no more available shards
- SERVER-71387 Range-based window [+N, unbounded] can tassert
- SERVER-71985 Automatically retry time series insert on
  DuplicateKey error
- SERVER-73662 tlsClusterCAFile is not being used to validate
  client certificates on Windows
- SERVER-73707 Evergreen timeout calculation fixes and cleanups
- SERVER-73943 Pin code pages in memory in memory constrained
  systems
- SERVER-73959 Add option to TaskExecutorCursor to not
  pre-fetch documents
- SERVER-74471 Prune existing tests to stabilize the signal
  from the change stream perf suite
- SERVER-74551 WriteConflictException unnecessarily logged as
  warning during findAndModify after upgrade to mongo 5.0
- SERVER-74645 integration_tests_standalone[_audit] should not
  run a unqiue build
- SERVER-74806 Write size estimation logic does not account for
  runtime/let constants
- SERVER-74980 excessive logging of "Refreshed cached
  collection" log messages introduced in 5.0
- SERVER-75280 Make shard_keys_with_dollar_sign.js use long
  timeouts for resharding crit sec
- SERVER-75298 Reduce log error severity in sharding logging
  library
- SERVER-75392 Update rounding functions in S2 geometry library
- SERVER-75789 [v4.4] Require WT engine for
  read_ticket_exhaustion_with_stepdown test
- SERVER-76006 break compile_dist_test into small chunks in a
  new kind of task group
- SERVER-76180 [5.0] Remove TemporarilyUnavailable error code
  in transaction_too_large_for_cache.js
- SERVER-76739 Archive data missing on evergreen task timeouts
- SERVER-76824 Do not run mr_single_reduce.js in stepdown
  suites
- SERVER-76826 $merge doesn't work with document that has
  dollar fields
- SERVER-76934 Update computeDiff() code should safely error
  when there are duplicate fields in the objects
- SERVER-76955 Add a multiversion_incompatible flag to
  fsm_workloads/map_reduce_drop.js in v5.0
- SERVER-76983 mongos shutdown procedure doesn't shutdown the
  CatalogCache
- SERVER-76988 Abort the reshardCollection operation when the
  zone information is too large
- SERVER-77018 Deadlock between dbStats and 2 index builds
- SERVER-77028 tlsClusterCAFile is not being used to validate
  client certificates on macOS
- SERVER-77039 Re-deny-list map_reduce_drop.js from
  SERVER-71368 changes
- SERVER-77074 mongod termination process should always
  shutdown and join the CatalogCached's thread pool
- SERVER-77168 mongod crashes when restoring time series
  collection with auth enabled
- SERVER-77196 NoPrefetch test in TaskExecutorCursorTest can
  deadlock
- SERVER-77226 Fix permissions-checking when pinning code
  segments
- SERVER-77266 createCollection command in
  rename_capped_collection_droptarget.js should ignore "cannot find ns"
  errors
- SERVER-77273 Add gcc IPA pass cp ICE to oom_retry tool
- SERVER-77298 Prevent fassert after killing opCtx as part of
  reconstructing prepared transactions after initial sync
- SERVER-77357 [v5.0] Add ubuntu22 variants
- SERVER-77383 ".msi.sha256" files have incorrect shasum
- SERVER-77518 Disable pin_code_segments.js on 6.0
  rhel-80-debug-ubsan
- SERVER-77527 mongodbtoolchain/v3 stdlib unsafe against
  self-moves
- SERVER-77534 Fix diff finder to handle deleted files
  correctly
- SERVER-77603 [5.0] remove publish tasks for ubuntu22 variants
- SERVER-77687 add ld OOM message to auto retry
- SERVER-77710 Fix data race in AuditManager
- SERVER-77769 SysPerf yml's compile-skip comment is
  incorrectly spaced
- SERVER-78080 Use fully random bytes for 8 low-order bytes of
  OID value for time series bucket _id
- SERVER-78126 For specific kinds of input, mongo::Value()
  always hashes to the same result on big-endian platforms
- SERVER-78314 Create documentSourceWriterBatchBuffer server
  parameter
- WT-7401 Silent test/format failure in the long-test Evergreen
  task
- WT-8536 Update the LLVM symbolizer path in the evergreen.yml
- WT-8539 Correct description for statistic for rolling back
  oldest pinned.
- WT-8601 Timestamps do not work with logged tables.
- WT-8709 RTS: Do not hold the oldest id of logged tables.
- WT-8822 Disable logging in failing configs
- WT-9117 test format exited with status 137 (Linux OOM killer)
- WT-9721 Format stress tests generate cores even when
  successful
- WT-10253 Run session dhandle sweep and session cursor sweep
  more often
- WT-10285 test format fails with status 137 (Linux OOM killer)
  during sanitizer runs
- WT-10469 Fix no timestamp tombstones not removing history
  store entries
- WT-10488 test_schema_abort failed with invalid argument
- WT-10512 Fix not inserting an out of order timestamp into the
  history store
- WT-10671 Reset statistics when retrying test in
  test_checkpoint04.py
- WT-10764 Add start and stop messages to rollback to stable
- WT-10900  Segmentation fault on unit-test-macos on macos-1100
- WT-10909 Simplify new test_backup29.py more
- WT-10920 Minor cleanup to test_backup29.py
- WT-11036 Add test of incremental backup after files are
  closed by dhandle sweep
- WT-11122 Disable FLCS scenario in the long-test task for 5.0
- WT-11140 Update Python path for Windows variants
- WT-11167 failed: format-stress-sanitizer-ppc-test on
  rhel8-ppc [wiredtiger-mongo-v5.0]: memory leak detected
