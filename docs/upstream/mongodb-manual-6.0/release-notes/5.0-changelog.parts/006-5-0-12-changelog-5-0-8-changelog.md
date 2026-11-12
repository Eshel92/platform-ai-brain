<!-- Part 6 of 12 of release-notes/5.0-changelog.md (split because the page is big). -->

## 5.0.12 Changelog

### Sharding

- SERVER-63732 Add new implicitlyCreateIndex and enforceUniquenessCheck to shardCollection command
- SERVER-64142 Add new enforceUniqueness to refineCollectionShardKey command
- SERVER-68728 Add addl. activation condition for interruptBeforeProcessingPrePostImageOriginatingOp fail point
- SERVER-68869 A retry of _configSvrReshardCollection can succeed causing resharding_coordinator_recovers_abort_decision.js to fail
- SERVER-69142 A retry of _shardsvrReshardCollection can cause DuplicateKey error (resharding_nonblocking_coordinator_rebuild.js)

### Replication

SERVER-62636 setFeatureCompatibilityVersion 4.4 succeeds on 5.0 binVersion that has indexes with conflicting options

### Internals

- SERVER-58176 Mongos does not validate readConcern on insert/update/delete commands
- SERVER-58966 timeseries_granularity.js and timeseries_timestamp_rounding.js collide on test namespaces in parallel suite
- SERVER-59834 $group with allowDiskUse doesn't clean up _tmp files
- SERVER-60958 Avoid server hang in chunk migration when step-down event occurs
- SERVER-63843 Don't allow recursive doLog in synchronous signal handlers
- SERVER-63852 getThreadName() should not crash
- SERVER-64573 Make implicitlyCreateIndex and enforceUniquenessCheck fields optional
- SERVER-64741 Create mongos appendOplogNote command
- SERVER-65006 Write conflict on commitIndexBuild oplog entry insertion can cause multikey to fail to be set
- SERVER-65382 AutoSplitVector should not use clientReadable to reorder shard key fields
- SERVER-66794 Add an in-memory flag for TS collections having dates outside years 1970-2038
- SERVER-67126 Remove LOGV2 call from printStackTrace no-LOGV2 codepath
- SERVER-67280 Ensure HealthObserver::periodicCheckImpl() implementations handle exceptions and return an appropriate failing health check status when one occurs
- SERVER-67725 Check catalog consistency on shards as precondition for rename
- SERVER-67814 Track the number of time-series collections with dates outside 1970-2038 in serverStatus
- SERVER-67939 run_dbcheck_background.js should be resilient to CappedPositionLost
- SERVER-68039 Old pymongo version 3.10.1 on MongoDB v5.0 causes Invariant failure (message.operation() == dbMsg) after connection reset by peer
- SERVER-68399 Fix parsing of safeint version numbers in blackduck_hub.py
- SERVER-68482 [5.0] Add TSAN exclusion to getFlowControlStats
- SERVER-68538 Typo in dependencies list in RPM config forces to fail installing mongodb enterprise in amazon linux 1
- SERVER-68540 Add docker_incompatible tag for jscore tests
- SERVER-68694 Investigate the locking around the compact command
- SERVER-68737 remove multiversion test from debian11 5.0
- SERVER-68766 Add option to re-enable single value MapReduce optimization
- SERVER-68925 Reintroduce check table logging settings at startup (revert SERVER-43664)
- SERVER-69052 Ensure bucket collection is valid when checking for extended range
- SERVER-69141 [6.1] Move forward pinned TSBS version


## 5.0.11 Changelog

### Sharding

- SERVER-56185 Investigate possible improvements with session migration and a chunk migration's critical section
- SERVER-61985 resharding_coordinator_recovers_abort_decision.js may report resharding operation as succeeding due to primary shard retrying _configsvrReshardCollection and running a second resharding operation
- SERVER-64340 Warn if balancer is disabled while draining shard
- SERVER-67492 Failed chunk migrations can lead recipient shard to have divergent config.transactions records between primary and secondaries
- SERVER-68431 resharding_test_fixture doesn't configure failpoints for all nodes of config server
- SERVER-68495 Resharding a collection with a very large number of zones configured may stall on config server primary indefinitely
- SERVER-68628 Retrying a failed resharding operation after a primary failover can lead to server crash or lost writes
- SERVER-68728 Add addl. activation condition for interruptBeforeProcessingPrePostImageOriginatingOp fail point

### Query

- SERVER-43155 Queries which exceed maxTimeMS may return NetworkInterfaceExceededTimeLimit
- SERVER-66072 $match sampling and $group aggregation strange behavior

### Build and Packaging

- SERVER-61894 Support the 'showRawUpdateDescription' option in change stream specs
- SERVER-63159 Implement the $_internalApplyOplogUpdate aggregation stage

### Internals

- SERVER-60607 improve handling of large/NaN values for geo index version
- SERVER-60958 Avoid server hang in chunk migration when step-down event occurs
- SERVER-61321 Improve handling of large/NaN values for text index version
- SERVER-62747 proxy_protocol_connect.js needs to use the loopback address for Docker containers
- SERVER-65262 Expand usage of WT numerical timestamp API
- SERVER-65884 $lookup from time-series can place $sequentialCache after correlated $match
- SERVER-66023 Do not constantly reset election and liveness timers
- SERVER-66310 Make  ExpressionSetUnion::isCommutative() collation aware
- SERVER-66548 $lookup sequential cache can incorrectly treat a $facet as non-correlated 
- SERVER-66651 Role "restore" not sufficient for mongorestore --preserveUUID
- SERVER-66726 Fix serialization in killAllSessionsByPattern
- SERVER-66841 LOGV2: invalid JSON when truncation happens at a backslash character
- SERVER-66938 Drastically simplify command to generate ninja files
- SERVER-67122 Add warning when building with --module=ninja that it is deprecated
- SERVER-67296 Mark the OpCtx of the configsvr commands used to commit chunk-related DDL ops as interruptible
- SERVER-67305 Lock-free reads setup should validate writes permitted before and after setting up snapshot.
- SERVER-67523 Must clear _nextCall on reschedule failure in delayable_timeout_callback
- SERVER-67532 Fail less in OplogServerStatusSection
- SERVER-67683 Change some of the modes in fast and opt builds
- SERVER-67845 Acquire critical section in rename "check preconditions" phase only if target not sharded
- SERVER-67939 run_dbcheck_background.js should be resilient to CappedPositionLost
- SERVER-68041 Robustify merge_write_concern.js and add diagnostic log
- SERVER-68130 AutoSplitVector could generate response bigger than BSONObjMaxUserSize
- SERVER-68158 serverstatus_indexbulkbuilder.js should run listIndexes on primary after creating indexes
- SERVER-68184 Use Number instead of NumberLong when indexing in checkWritesOfCommittedTxns
- SERVER-68193 Sharding DDL coordinator can lock itself out in distlock retry loop
- SERVER-68487 add BSONElement method to check for NaN field values
- SERVER-68511 movePrimary might introduce sharding metadata inconsistency in MongoDB 5.0+
- SERVER-68522 Prevent 5.0 binary from starting in FCV 4.4 with misconfigured TTL index
- SERVER-68540 Add docker_incompatible tag for jscore tests
- SERVER-68574 Switch to the new logkeeper cluster
- SERVER-68737 remove multiversion test from debian11 5.0
- WT-8847 Add tombstone to WT_SAVE_UPD to truncate the update list upon page restore
- WT-9004 Fix memory leak in update restore eviction
- WT-9302 Deprecated object_target_size as a config in api_data.py
- WT-9311 Ensure log messages clearly identify storage HW corruption
- WT-9477 Don't allow checkpoint triggering internal page split which leads to corrupted internal page in the checkpoint
- WT-9500 Fix RTS to use cell time window instead of key/value timestamps of HS update


## 5.0.10 Changelog

### Sharding

- SERVER-57519 Make ARS use causally consistent ShardRegistry::getShard() function
- SERVER-62272 Adding schema validation to a collection can prevent chunk migrations of failing documents
- SERVER-62432 Ensure safe access to ShardingDDLCoordinator instance state documents
- SERVER-62656 Decouple mongos-to-config-server connection pool sizing from mongos-to-shard-server connection pool sizing
- SERVER-63243 Range deleter must not clean up orphan ranges in a round-robin fashion
- SERVER-64433 A new topology time could be gossiped without being majority committed
- SERVER-65027 Resharding commands permit extra options without returning an error
- SERVER-65821 Deadlock during setFCV when there are prepared transactions that have not persisted commit/abort decision
- SERVER-65925 shardsvrCommitReshardCollection should check for transient errors when joining
- SERVER-65930 DDL coordinators and rename participant initial checkpoint may incur in DuplicateKey error
- SERVER-66046 Resharding coordinator won't automatically abort the resharding operation when a recipient shard errors during its applying phase
- SERVER-66618 Ensure ReshardingCoordinator has aborted in resharding_coordinator_recovers_abort_decision.js
- SERVER-66866 The range deleter waits between batches while holding the collection IX lock
- SERVER-67457 Resharding operation aborted in the midst of contacting participants may stall on config server primary indefinitely

### JavaScript

SERVER-61234 JS object-based types are not properly auto-serialized when directly returned by server-side JS functions

### Build and Packaging

SERVER-66627 Backport the install-devcore target

### Internals

- SERVER-57938 Skip polygon validation for stored GeoJSON when query has $geoIntersect and a 2dsphere index
- SERVER-58257 Add better diagnostics to predictive_connpool.js
- SERVER-59658 Improve logging to reflect that sharding metadata refresh waiting on replication
- SERVER-61856 Upgrade libunwind to 1.6.2+
- SERVER-62386 Coverity analysis defect 121298: Parse warning
- SERVER-62716 Handle spurious finishWaitingForOneOpTime in WaitForMajorityServiceTest
- SERVER-63271 serverStatus can fail the server
- SERVER-63493 update-shard-key tests failing due to transaction lock timeouts
- SERVER-63971 Change server parameter to default to read-your-writes behavior after 2PC transaction
- SERVER-64215 Interrupt OplogBufferMock::waitForData on shutdown
- SERVER-64244 RunDBCheckInBackground should be resilient to interrupts
- SERVER-64509 Fix ShardRegistry threadpool shutdown order
- SERVER-64627 Need general method to handle in-memory state after initial sync
- SERVER-64628 More testing of adding nodes to sharded sets
- SERVER-64659 Report in serverStatus number of file descriptors used during index builds
- SERVER-64725 Make ShardRegistry::periodicReloader interruptible
- SERVER-64797 Use WT's new numerical timestamp API
- SERVER-65100 Increase memory block size for BSONColumn
- SERVER-65131 Disable opportunistic read targeting (except for hedged reads)
- SERVER-65313 Use BatchedCollectionCatalogWriter during startup recovery
- SERVER-65371 MigrationSourceManager running on secondary node may trip invariant
- SERVER-65399 'commitIndexBuild' oplog entry is a no-op for unfinished index builds not restarted
- SERVER-65723 Add tunable parameter to improve batching on secondaries
- SERVER-65777 "revokePrivilegesFromRole" param.ns missing user object in audit log 
- SERVER-65797 Remove invalid index specs in memory before parsing for listIndexes
- SERVER-66087 Call curl_global_init before threading enabled
- SERVER-66111 Curl implementation of HTTPClient should respect default timeouts
- SERVER-66319 dbcheck_no_history_on_secondary.js disables dbCheck failpoint too early
- SERVER-66379 $or to $in conversion flawed
- SERVER-66384 Enable command line customization of NINJA_BUILDDIR
- SERVER-66418 Bad projection created during dependency analysis due to string order assumption
- SERVER-66433 Backport deadline waiting for overlapping range deletion to finish to pre-v5.1 versions
- SERVER-66461 Run notarization earlier in the build process
- SERVER-66520 add index build UUID to BackgroundOperationInProgress error messages
- SERVER-66556 Prevent potential race when releasing cursors during shutdown
- SERVER-66559 Expand the internalQueryMaxAddToSetBytes param from 32 to 64 bits
- SERVER-66658 Shard registry might be accessed before initialization
- SERVER-66727 Time-series bucket can be created that violates max time-span
- SERVER-66769 Update spawnhost setup script to support Windows hosts via cygwin
- SERVER-66799 Fix getParameterWithDetails.js failure on ephemeralForTest
- SERVER-66843 Use defensive programming in DeadlineFuture destructor
- SERVER-66860 FSM tests should not reuse same database names
- SERVER-66902 Multiversion setup is consistently failing on the mongodb-mongo-v5.0 Evergreen project
- SERVER-66955 Remove JSON.send usage in perf projects
- SERVER-67014 Say that "the client driver may require an upgrade" in warning message for deprecated op codes in 5.0
- SERVER-67106 The _flushRoutingTableCacheUpdates() command should be able to also serve requests referencing collection views.
- SERVER-67167 DIsable or_to_in.js from running in the parallel suite
- SERVER-67220 [5.0] set_fcv_prepared_transaction.js is not resilient to StaleConfig errors
- SERVER-67405 Handle empty string for is_patch evergreen expansion
- SERVER-67513 Disable or_to_in for jsCore_compatibility for v5.0 
- WT-8425 Push updates with the same commit timestamps in the out_of_order_ts_updates vector in hs_rec.c.
- WT-8669 Assert that the timestamps are not OOO in __hs_insert_record 
- WT-9249 Compare and fix the start durable timestamp if it is greater than ooo timestamp
- WT-9251 Perform log flush before the metadata checkpoint


## 5.0.9 Changelog

### Sharding

- SERVER-62175 Mongos fails to attach RetryableWrite Error Label For Command Interrupted In _parseCommand
- SERVER-62432 Ensure safe access to ShardingDDLCoordinator instance state documents
- SERVER-64822 Sharding an empty collection releases the critical section too early
- SERVER-66041 Chunk cloner must never consider too big a chunk with only one document

### Query

SERVER-63642 Add serverStatus metrics to measure multi-planning performance

### Build and Packaging

- SERVER-42470 Generate additional configuration for libunwind
- SERVER-64332 Notarize MongoDB builds for macos
- SERVER-66386 Update AMI images for package tests

### Internals

- SERVER-57546 Increase test-specific timeouts for roles lock acquisition
- SERVER-58337 Log deprecation warning and bump serverStatus counter upon receipt of OP_QUERY command
- SERVER-60758 Prevent dbVersion refreshes from failing transactions in txn_recover_decision_using_recovery_router.js
- SERVER-61018 Create a generic histogram type
- SERVER-61110 Fix locking in AuthorizationContract::contains
- SERVER-61460 Resmoke should merge config_svr options with mongod_options rather than overriding them
- SERVER-62941 Update FTDCServerStatusCommandCollector to include oplog metrics from serverStatus command
- SERVER-62992 Remove need for resmoke.ini
- SERVER-63254 Add Index usage metrics to serverStatus 
- SERVER-63796 Enable Feature flag for PM-2750
- SERVER-63850 Add the count command to API version 1
- SERVER-64664 ninja tool should not consider install files generated source
- SERVER-64815 Prevent buildindexes_false_commit_quorum.js from running in multiversion tests
- SERVER-65137 detect namespace changes when refreshing Collection after yielding
- SERVER-65166 Use compareOptimes in abort_in_progress_transactions_on_step_up.js
- SERVER-65184 Avoid concurrent election and stepdown in downgrade_default_write_concern_majority.js
- SERVER-65271 serverStatus should allow fine-grained metrics exclusion
- SERVER-65636 Remove limits on number of LDAP connections per host
- SERVER-65861 Remove enterprise-rhel-83-s390x from mh_variants on 5.0
- SERVER-65995 Reduce Evergreen cron frequency on older branches
- SERVER-66089 Initial sync should do transaction table read with a later afterClusterTime
- SERVER-66117 Disable qualify_shortname in mock libkrb5 configuration
- WT-8250 Increase the maximum expected space available after compaction in test_wt7989_compact_checkpoint
- WT-8450 Report stats in hs_cleanup_stress, don't validate them
- WT-8481 Split cppsuite search near tests and update their logging levels
- WT-8622 Read in last_ckpt_base_write_gen at start of recovery
- WT-8860 Save the mongod logs as a test artifact in many-collection-test 
- WT-9019 Disable cyclomatic-complexity test on 5.0
- WT-9029 Remove object_target_size option from WT_SESSION::create
- WT-9044 Disable code coverage measurement on mongodb-5.0
- WT-9054 Correctly configure split stress options in format.sh
- WT-9096 Fix search near returning wrong key/value sometimes when key doesn't exist


## 5.0.8 Changelog

### Sharding

- SERVER-62690 Shard is shutting down before finishing draining in test
- SERVER-65533 Operations with {readConcern:available} do not treat the collection as UNSHARDED

### Write Operations

SERVER-65261 Deleting from a capped collection via collection scan reports number of documents deleted incorrectly

### Build and Packaging

SERVER-44074 Platform Support: Add Enterprise RHEL 8 (zSeries)

### Internals

- SERVER-55173 Segmentation fault in WiredTigerSession::releaseCursor
- SERVER-56003 ninja + icecream with changing compilers doesn't regen run-icecc.sh
- SERVER-56731 Consider running server tests on newer SLES 12 service pack
- SERVER-58506 Command to expose settability for Server Parameters
- SERVER-60105 Inserts into timeseries collections are not observable from any opcounter
- SERVER-60485 Tasks which run on the MigrationUtilExecutor must not wait for shutdown to complete
- SERVER-61032 Convert all references to /opt/mongodbtoolchain/gdb to a versioned equivalent
- SERVER-61663 Dynamically split concurrency_metrics and concurrency_replication_metrics into smaller tasks
- SERVER-61879 Refreshes to recover migrations must never join ongoing refreshes
- SERVER-62205 Include sanity check for max chunk size argument of  [auto]splitVector
- SERVER-62229 Fix invariant when applying index build entries while recoverFromOplogAsStandalone=true
- SERVER-62299 Platform Support: Add support for Debian 11
- SERVER-63010 Ensure that unpacking measurements doesn't overwrite pushedown addFields that are computed on meta data
- SERVER-63387 StreamingCursor should return backup blocks in the order they were retrieved from the WiredTiger backup cursor
- SERVER-63479 Correct $$SEARCH_META ban in sharded environments
- SERVER-63531 commitQuorum incorrectly includes buildIndexes:false nodes and error message incorrectly says that only voting nodes are eligible
- SERVER-63910 Generalize this error message related to the critical section
- SERVER-64031 serverStatus should not take PBWM lock
- SERVER-64184 Track usage of allowDiskUse:true in agg command
- SERVER-64485 Use _id to determine the update type in extractUpdateType()
- SERVER-64554 abortIndexBuild oplog entry has no effect when run with --recoverFromOplogAsStandalone
- SERVER-64732 [v5.0] BSONColumn decompression of interleaved arrays
- SERVER-64757 Improve error messages when scons fails to generate-ninja on Windows
- SERVER-64983 Release Client lock before rolling back WT transaction in TransactionParticipant::_resetTransactionState
- SERVER-65024 Multiple documents with the same _id value make reIndex invariant
- SERVER-65032 Pin python package BaseResponse for ocsp suite
- SERVER-65182 Fix split_horizon_hostname_startup.js to use an assert.soon when getting the replsetconfig
- SERVER-65200 Package task not run as part of task group
- SERVER-65211 Use expansion to get binaries from the current branch
- SERVER-65284 Create collection coordinator should always perform cleanup on subsequent execution
- SERVER-65430 Disable capped_deletes.js on ephemeralForTest
- SERVER-65718 Fix mypy error
- WT-7662 Format timed out with prepare-conflict
- WT-8260 Create a Python suite test to validate new EVENT_HANDLER JSON format
- WT-8708 Fix timestamp usage error in test/checkpoint
- WT-8924 Don't check against on disk time window if there is an insert list when checking for conflicts in row-store
