<!-- Part 4 of 12 of release-notes/5.0-changelog.md (split because the page is big). -->

## 5.0.18 Changelog

### Sharding

- SERVER-72146 Make chunk migrations metrics more accessible
  from Atlas
- SERVER-76004 Remove incorrect sharding tassert in
  getOwnershipFilter function
- SERVER-76516 Fix Concurrent Access of Clock in
  ReshardingRecipientServiceTest in 5.0 Branch

### Query

SERVER-48196 Upgrade the timelib to the latest to update the
built-in timezone files to the latest

### Internals

- SERVER-54150 Recovery from a stable checkpoint should fassert
  on oplog application failures
- SERVER-57056 Syslog severity set incorrectly for INFO
  messages
- SERVER-60375 Deny list move_chunk_remove_shard.js from
  sharding_csrs_continuous_config_stepdown
- SERVER-62053 Add retry for errors in AWS server-side
  conversation
- SERVER-63865 Handle missing index idents during standalone
  startup recovery after unclean shutdown
- SERVER-66009 Ban $search when running in update pipeline
  (stub process interface is present)
- SERVER-68338 sync_source_changes.js needs to wait for
  heartbeat
- SERVER-71089 Run signing tasks on a single distro
- SERVER-71249 Remove buildvariant task overrides for .publish
  tags
- SERVER-72686 Add support for $collStats agg stage on
  timeseries collection
- SERVER-73007 CURL_OPT_SEEKFUNCTION not set for multi-pass
  authentication
- SERVER-73385 RenameCollectionCoordinator wrongly releases
  critical section for destination ns.
- SERVER-73390 Mitigate database version regression bug on drop
  database
- SERVER-74344 Ban use of sparse indexes on internal comparison
  expression unless explicitly hinted
- SERVER-74997 Reduce the timeout of tlsOCSPVerifyTimeoutSecs
  to 4 seconds
- SERVER-75010 Implement no-op planShardedSearch in 5.0
- SERVER-75082 Make balancer migrations throttling configurable
- SERVER-75360 Include $search result count (total hits) in
  slow query log
- SERVER-75369 Fix the overflow of total possible enumeration
  count in LockstepOr enumeration strategy
- SERVER-75479 Use system python on macos for ssl tests
- SERVER-75626 Special handling for macosx venv
- SERVER-75652 Migrate from notary client to garasign for push
  task
- SERVER-75987 Synchronize the connection and server threads in
  transport_layer_test
- SERVER-76039 PauseDuringStateTransitions guard needs correct
  initialization in DropsTemporaryReshardingCollectionOnAbort
- SERVER-76063 Update the getFreeMonitoringStatus command to
  always return state: disabled
- SERVER-76139 sync_source_changes.js should wait for node to
  no longer be newly added before asserting on selected sync source
- SERVER-76179 "/var/run/mongodb/"mongod.pid" deleted on each
  Mongod shutdown
- SERVER-76274 Move microbenchmarks to their own task distro
- SERVER-76278 Log extra migration information
- SERVER-76378 Use estimated impersonation metadata size in
  calculating block chunks
- SERVER-76421 [5.0] ttl_expire_nan_upgrade.js checks indexes
  on node before it becomes secondary
- SERVER-76498 Update push task to run on rhel8.7-small
- SERVER-76599 Exclude
  jstests/sharding/balancer_collection_status.js from step-down suites
- SERVER-76600 Increase timeouts for
  aggregation_timeseries_fuzzer on tsan/asan variants
- SERVER-76619 Add setParameter to enable libcurl's verbose
  logging
- SERVER-76690 Special handling for PYTHONPATH when activate
  venv
- SERVER-76695
  initial_sync_nodes_maintain_and_gossip_commit_point.js should wait
  longer for initial sync node to advance commit point
- SERVER-76698 Disable Curl Connection Pooling for STS requests
- SERVER-76699 Add configurable retry count in AWS IAM code
- SERVER-76718 [v5.0] Push mongocryptd and create packages for
  RHEL 7 PPC in 5.0
- SERVER-76721 Robustify plan_cache_stats_shard_and_host.js to
  count plan cache entries only for specific plan cache key
- SERVER-76767 Disable 4.0 upgrade tests on v5.0 branch
- WT-8570 Do not increase oldest ID during recovery
- WT-8689 Switch Evergreen zSeries builder to RHEL distro
- WT-8702 Limit oldest id to recovered checkpoint snapshot in
  recovery
- WT-10551 Incremental backup may omit modified blocks
- WT-10932 Disable many-collection-test on release branches


## 5.0.17 Changelog

### Sharding

- SERVER-73229 Logical sessions cache refresh ignores write
  errors from updating session document, leading to cursors being killed
  early
- SERVER-73877 Wait for shard to have a primary before doing a
  migration in prepare_transaction_then_migrate.js

### Write Operations

SERVER-75517 illegal format of _id possible via upsert

### Internals

- SERVER-66927 Remove reference to silentFail from mongo repo
- SERVER-73400 Use -large Evergreen distro for compiling on
  arm64 in sys-perf project
- SERVER-74647 Resharding state machine creation should be
  retried after interruption
- SERVER-74720 The default 'shardingStatistics' serverStatus
  section takes locks
- SERVER-74824 Add more expressive logging to
  map_reduce_drop.js
- SERVER-75066 Check for parent directory before writing to
  SCons cache
- SERVER-75172 Use unique collection name in
  partial_index_logical.js
- SERVER-75261 "listCollections" command fails with
  BSONObjectTooLarge error
- SERVER-75404 Designate $searchSortValues as metadata field on
  v5.0
- SERVER-75431 Get rid or fix best effort check for primary db
  on rename path in sharded clusters
- SERVER-75501 Don't run Sys-perf FCV variants on stable
  branches
- SERVER-75561 Report and log more detailed information when
  validate encounters multikey inconsistencies
- SERVER-75601 Make serverStatus apiversion field more robust
- SERVER-75618 check oplog fast count before restarting server
  in oplog_sampling.js
- SERVER-75745 Only log record and index metadata associated
  with missing or extra index keys
- SERVER-75795 Update aws_e2e_ec2.js for evergreen changes to
  AWS test identity
- SERVER-76098 Allow queries with $search and non-simple
  collations


## 5.0.16 Changelog

### Sharding

- SERVER-58466 Minor optimization on the CatalogCache: do not
  create a new routing table if the collection version hasn't changed
- SERVER-62036 Failures in preCacheMongosRoutingInfo() will
  cause mongos to fail startup
- SERVER-66542 Missing log/Update of the stats after the
  completion of a CatalogCache refresh
- SERVER-71368 Stop excluding tests that drop
  collection/database in sharded suites
- SERVER-73751 movePrimary shouldn't create indexes for sharded
  collections
- SERVER-74124 Disallow sharding with wildcard shard key
  pattern

### Query

SERVER-63049 Track usage of agg accumulators

### Write Operations

SERVER-75517 illegal format of _id possible via upsert

### Internals

- SERVER-51835 Mongos readPreferenceTags are not working as
  expected
- SERVER-59169 Use larger machines for large inMemory tests
- SERVER-60830 Missing index scan bound in time-series query
  rewrite
- SERVER-61100 Fix multiversion tests that assert
  last-lts/last-continuous incompatibility
- SERVER-61203 Add record metadata and history in validate
  output when corruption is detected
- SERVER-61909 Hang inserting or deleting document with large
  number of index entries
- SERVER-62665 Ensure TransportLayerASIO::TimerService can
  safely end the session
- SERVER-63637 Execution stats for $_internalBoundedSort
- SERVER-63699 Proof of Concept of bounded-sort stage for
  time-series
- SERVER-64093 Support spilling to disk in BoundedSorter
- SERVER-64347 Add support for descending sort to the bounded
  sorter
- SERVER-64348 Add support for compound sorts (meta, time) to
  the bounded sorter
- SERVER-64349 Add heuristic-based planning support for bucket
  unpacking with sort
- SERVER-64397 TimeSorter comparator int overflow
- SERVER-64451 Ensure we don't try to access BoundedSorter heap
  if it is empty
- SERVER-64602 Provide time-series bucket time bounds as
  document metadata for use by bounded sorter
- SERVER-64654 Enable Feature flag for PM-2786
- SERVER-64769 Make sure $_internalBoundedSort provides sort
  key for sharded mergesort
- SERVER-65050 BUS planning work for point query on meta data
- SERVER-65990 Test BUS w/ changing BucketMaxTimeSpan
- SERVER-66012 Use a WiredTiger version cursor to print
  metadata of extra index entries during validation
- SERVER-66469 Filtering timeseries with date-field does not
  include results from before 1970
- SERVER-66558 $sort does not rewrite to bounded sort when
  multiple index options are available
- SERVER-66793 Disable bucket unpacking with sort for clustered
  collections with out of order buckets
- SERVER-67446 Ensure consistent wildcardProjection and
  columnstoreProjection specs in catalog
- SERVER-67780 Incorrect $group rewrite for timeseries
  collection when the accumulator uses meta field
- SERVER-67950 Make stronger assertions in
  bucket_unpacking_with_sort_granularity_change.js
- SERVER-68328 Add ResumableChangeStreamError label to
  ReadConcernMajorityNotAvailableYet errors
- SERVER-68594 Add vscode format/lint on save
- SERVER-69952 Filtering on dates outside of the 32 bit epoch
  range returns wrong results
- SERVER-70167 Resumed create coordinator may incorrectly try
  to release the critical section
- SERVER-70747 Rename collection used in
  bucket_unpacking_with_sort_extended_range.js
- SERVER-71178 Create project branch and flag for PM-2786
- SERVER-71307 Aggregations with $search should fail if the
  resolved collation is non-simple
- SERVER-71328 Ensure correct filtering metadata on donor shard
  after multiple failures
- SERVER-71392 Track usage of JSON Schema for validation
- SERVER-71750 Revert refactor into
  handleWriteConflictException in writeConflictRetry loop
- SERVER-71751 Skip transaction_too_large_for_cache.js for
  in-memory variants
- SERVER-71950 Fail and log the operation when out-of-order
  keys are detected in WiredTiger
- SERVER-72194 oplog_rollover.js should wait for the durable
  timestamp to advance
- SERVER-72519 Add arm and intel Microbenchmark test variants
  to Sys Perf
- SERVER-72520 Decommission Microbenchmark performance tests
  that are running on CBI instances
- SERVER-72542 fullValidate should not return a count of items
- SERVER-72774 A node in quiesce mode can win election
- SERVER-73110 bucket_unpacking_with_sort_extended_range.js
  fails in sharded passthrough
- SERVER-73125 Builtin variable $$NOW is not available in
  document validation
- SERVER-73157 Move out_max_time_ms tests to serial_run suite
- SERVER-73232 Change the default log-verbosity for
  _killOperations
- SERVER-73390 Mitigate database version regression bug on drop
  database
- SERVER-73400 Use -large Evergreen distro for compiling on
  arm64 in sys-perf project
- SERVER-73481 Validate does not detect out-of-order keys with
  {full: false}
- SERVER-73521 [5.0] Backport setProfilingFilterGlobally
  command
- SERVER-73706 Save WTRecordStoreUassertOutOfOrder fail point
  state to prevent concurrency bugs in testing
- SERVER-73732 Complete TODO listed in SERVER-61100
- SERVER-73745 Zero initialize IndexKeyBucket struct
- SERVER-73822 Time-series $group rewrite ignores certain
  accumulators
- SERVER-74038 [Windows] Possible negative performance effects
  of SetProcessWorkingSetSize in SecureAllocator
- SERVER-74045 Allow turning on diagnostic log messages for
  validate
- SERVER-74103 Increase storage log verbosity in
  oplog_sampling.js
- SERVER-74104 [v5.0] Disable journal flusher in
  validate_out_of_order.js
- SERVER-74131 Multiplanning together with subplanning causes
  server crash in mapReduce queries
- SERVER-74137 [v5.0] Tag validate_out_of_order.js with
  requires_replication
- SERVER-74153 Fix blackduck_hub.sh 5.0 script
- SERVER-74156 Package plist files with macosx releases
- SERVER-74287 create scons OOM retry tool
- SERVER-74345 mongodb-org-server 4.4.19, 5.0.15, 6.0.5 not
  starting after upgrading from older version (Debian, RPM Packages)
- SERVER-74386 Don’t reset recordPreImages on collMod [6.0
  only]
- SERVER-74501 Fix MigrationBatchFetcher/Inserter completion
  reliance to not spawn an extra cleanup thread
- SERVER-74631 Log index spec when validation detects index key
  inconsistencies
- SERVER-74632 Log $collStats output when a collection fails
  validation
- SERVER-74642 Log additional information about the oplog entry
  that generated a document or index key when printing metadata
- SERVER-74647 Resharding state machine creation should be
  retried after interruption
- SERVER-74690 Change Atlas Real variants to use “2022-11”
  workload client
- SERVER-74824 Add more expressive logging to
  map_reduce_drop.js
- SERVER-74845 Create mechanism to ignore ignore fork option
  with systemd
- SERVER-74895 Expect command errors in validation when
  querying $collStats, and improve the error message
- SERVER-75172 Use unique collection name in
  partial_index_logical.js
- SERVER-75205 Deadlock between stepdown and restoring locks
  after yielding when all read tickets exhausted
- SERVER-75397 Make v5.0/v4.4 required variants run every other
  day
- SERVER-75404 Designate $searchSortValues as metadata field on
  v5.0
- SERVER-75431 Get rid or fix best effort check for primary db
  on rename path in sharded clusters
- SERVER-75561 Report and log more detailed information when
  validate encounters multikey inconsistencies
- SERVER-75618 check oplog fast count before restarting server
  in oplog_sampling.js
- WT-8333 Implement version cursor
- WT-8848 Add API to roll back and indicate that a transaction
  has exceeded a configurable limit of pinned dirty data
- WT-8981 Enable evergreen testing for RHEL8 on PPC
- WT-9629 Fix collection of compact progress statistics
- WT-9879 Fix overcounting of session txn dirty bytes statistic
- WT-10027 Session txn dirty statistic is incorrect
- WT-10062 Fix checkpoint cleanup not to skip the internal
  pages
