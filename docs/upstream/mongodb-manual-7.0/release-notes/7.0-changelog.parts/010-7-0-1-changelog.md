<!-- Part 10 of 10 of release-notes/7.0-changelog.md (split because the page is big). -->

## 7.0.1 Changelog

### Security

- SERVER-78723 Resharding a QE collection fails because of
  __safeContent__
- SERVER-78830 Add count of CSFLE and QE Collections to
  serverStatus
- SERVER-79641 Mirrored read should attach
  encryptionInformation from the original command

### Sharding

- SERVER-62987 Wrong replication logic on refreshes on
  secondary nodes
- SERVER-67529 Resharding silently skips documents with all
  MaxKey values for their fields under the new shard key pattern
- SERVER-78913 Make the periods of query sampling periodic jobs
  configurable at runtime

### Query

SERVER-80256 QueryPlannerAnalysis::explodeForSort should not
assume that index scans produce disjoint results

### Internals

- SERVER-71627 Refreshed cached collection route info will
  severely block all client request when a cluster with 1 million chunks
- SERVER-73866 Re-enable agg_merge_when_not_matched_insert.js
  in config_fuzzer passthrough suites
- SERVER-74701 Add checksum verification for blackduck
  installer
- SERVER-75120 libunwind stacktrace issues with --dbg=on on
  arm64
- SERVER-76299 Report writeConflicts in serverStatus on
  secondaries
- SERVER-76339 Increase ShardedClusterFixture's timeout when
  starting/stopping balancer
- SERVER-76433 Copy search_view.js test from 5.0 to all later
  branches
- SERVER-77029 Set syncdelay in TestOplogTruncation before
  starting the checkpoint thread
- SERVER-77183 $project followed by $group gives incorrect
  results sometimes
- SERVER-77223 dbcheck_detects_data_corruption.js needs to wait
  for primary to log healthlog entry
- SERVER-77382 Null embedded metaField for creating a
  time-series collection leads to invalid BSON index spec
- SERVER-77823 Pseudocode for throughput probing
- SERVER-78095 Relax the assertion checking for
  update_multifield_multiupdate.js FSM workload
- SERVER-78369 ignoreUnknownIndexOptions doesn't account for
  the 'weights' index field
- SERVER-78498 Make the balancer failpoint smarter
- SERVER-78525 Update
  jstests/noPassthrough/metadata_size_estimate.js to use a smaller
  document size
- SERVER-78696 Only clear shard filtering metadata before
  releasing the critical section in collmod participants
- SERVER-78769 The asynchronous stop sequence of the Balancer
  may survive the shutdown of the mongod (and raise false memory leak
  notifications).
- SERVER-78782 Complete TODO listed in SERVER-75120
- SERVER-78813 Commit point propagation fails indefinitely with
  exhaust cursors with null lastCommitted optime
- SERVER-78862 Fix serialization of nested $elemMatch's
- SERVER-78888 Unschedule Mix js
- SERVER-78950 Use sequential time series bucket IDs when
  possible
- SERVER-79021 Update Boost's entry in README.third_party.md to
  1.79.0
- SERVER-79022 Update ASIO's Git hash in README.third_party.md
- SERVER-79023 Update C-Ares' entry in README.third_party.md to
  1.19.1
- SERVER-79033 Image collection invalidation for missing
  namespace during initial sync always attempts upsert
- SERVER-79082 Make analyzeShardKey tests not assert number of
  orphaned documents <= total number of documents
- SERVER-79103 Core dumps are not generated if stopping
  balancer fails
- SERVER-79126 Pin pyyaml in another place
- SERVER-79138 Fix data race in AuthorizationSessionTest
  fixture
- SERVER-79252 Add the system-perf bootstrap file to the task
  Files section
- SERVER-79261 Add logging to ping monitor
- SERVER-79316 [7.0] Do not run packager on dynamically linked
  variants
- SERVER-79357 CheckMetadataConsistency is not reading chunks
  with snapshot read concern
- SERVER-79370 Throughput probing statistics not always updated
  correctly
- SERVER-79372 Fix incorrect assertion about number of cursors
  opened
- SERVER-79382 Reset bucket OID counter when encountering a
  collision
- SERVER-79397 Fix and test logic to internally retry time
  series inserts on OID collision
- SERVER-79447 The balancer stop sequence may cause the config
  server to crash on step down
- SERVER-79509 Add testing of transitional FCVs with
  removeShard and transitionToDedicatedConfigServer
- SERVER-79515 Update task generator
- SERVER-79607 ShardRegistry shutdown should not wait
  indefinitely on outstanding network requests
- SERVER-79609 Fix findAndModify_upsert.js test to accept
  StaleConfig error
- SERVER-79651 Only use two node replicasets in initial sync
  performance tests
- SERVER-79777 Increase the diff window for the sample size in
  sample_rate_sharded.js
- SERVER-79885 Oplog fetching getMore should not set null
  lastKnownCommittedOpTime if it is not using exhaust cursors
- SERVER-79937 Avoid majority reads within the
  BalancerDefragmentationPolicy
- SERVER-79944 Make analyze_shard_key.js not assert that the
  number of sampled queries observed via analyzeShardKey and
  $listSampledQueries is non-decreasing
- SERVER-79950 Fix commitPreparedTransaction to not be
  interruptible in commitSplitTxn and reacquireTicket
- SERVER-79981 resize_tickets.js fails in  Fixed Concurrent
  Transactions test suite
- SERVER-80153 UBsan core dumps are not being uploaded properly
- SERVER-80183 Remove operationTime check from
  store_retryable_find_and_modify_images_in_side_collection.js
- SERVER-80207 Use 4-byte counter for tracking time series
  bucket direct writes
- SERVER-80224 Fix failing asserts in
  stale_mongos_updates_and_removes.js and extract_shard_key_values.js on
  7.0
- WT-10714 Select an explicitly labeled perf distro for
  performance tests
- WT-11202 Remove the connection level operation_timeout_ms
  configuration
- WT-11221 Python tests fails due to unexpected "Eviction took
  more than 1 minute" warning in standard output
- WT-11312 Fix incorrect flag check for accurate force eviction
  stat
- WT-11359 Update spinlock tasks to limit disk usage
- WT-11419 Increment cc_pages_removed when detecting a deleted
  page to remove
