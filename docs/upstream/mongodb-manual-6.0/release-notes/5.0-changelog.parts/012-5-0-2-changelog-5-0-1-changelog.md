<!-- Part 12 of 12 of release-notes/5.0-changelog.md (split because the page is big). -->

## 5.0.2 Changelog

### Security

SERVER-57727 Race conditions in x509_invalid.js

### Sharding

- SERVER-47372 config.cache collections can remain even after collection has been dropped
- SERVER-48651 Avoid lock timeout errors in refine_collection_shard_key_basic.js
- SERVER-50521 Write reshardBegin no-op oplog entry after temporary resharding collection is created
- SERVER-54948 Calling shardCollection after enableSharding from a different MongoS is not causally consistent
- SERVER-55574 Migration distlock acquisition fails to catch status
- SERVER-56647 Make dropDatabase resilient to network partitions
- SERVER-56648 Make dropCollection resilient to network partitions
- SERVER-56649 Make renameCollection resilient to network partitions
- SERVER-56650 Make createCollection resilient to network partitions
- SERVER-57204 Extend the _configsvrSetAllowMigrations command to take the collection uuid to make it idempotent
- SERVER-57380 Improve "InvalidOptions: read concern level snapshot is only valid in a transaction" message during cluster incompatibility
- SERVER-57488 Create command to remove tags matching a ns from config.tags that can be run as retryable write
- SERVER-57496 Proactively evict cached entries after drop database/collection
- SERVER-57559 Implement LSID cache for DDL coordinators
- SERVER-57759 Run movePrimary command before sharding the source collection in the ReshardingTest fixture
- SERVER-57850 Increase timeout when waiting for migration on authCommands.js
- SERVER-57870 Drop database sharded FSM doesn't guarantee that operations will be completed
- SERVER-57944 Targeter is not being clean completely after failed refresh on batch write executor
- SERVER-58021 mongos should retry write upon getting ShardCannotRefreshDueToLocksHeld error from shard
- SERVER-58048 Resharding's initial split points for hashed shard keys don't match the sampled values
- SERVER-58089 Coverity analysis defect 120194: Uninitialized pointer field
- SERVER-58115 Outdated information can remain in the catalog cache after a collection is renamed
- SERVER-58143 shardsvrDropCollectionParticipant should be killable on stepdown
- SERVER-58167 Use scoped database critical section during dropDatabase
- SERVER-58266 Stop forcing database version refreshes in chunk manager targeter
- SERVER-58271 Stop forcing collection version refreshes in chunk manager targeter
- SERVER-58273 Solve deadlock caused by uninterruptible lock guard in drop db participant command
- SERVER-58321 Check recipient document existence instead of donor twice in resharding abort command
- SERVER-58364 ShardServerCatalogCacheLoader::waitForCollectionFlush should be interruptible
- SERVER-58465 Fix the cleanup of the Routing Info in the rename operation
- SERVER-58535 _shardsvrRenameCollection should be interrupted on stepdown
- SERVER-58589 Remove ShardingFullDDLSupportTimestampedVersion feature flag 
- SERVER-58624 Change the resharding critical section timeout value for reshard_collection_basic.js
- SERVER-58649 Do not assume that the collection is always sharded in ShardServerProcessInterface::checkRoutingInfoEpochOrThrow method
- SERVER-58747 The ShardServerCatalogCacheLoader doesn't interrupt ongoing operations on step up 
- SERVER-58749 Drop database coordinator must acquire collection distributed lock 
- SERVER-58775 Mark ConfigsvrSetAllowMigrationsCommand's opCtx as killable on stepdown

### Replication

- SERVER-37904 Allow a node to override the cluster chaining (enabled/disabled) setting
- SERVER-58258 Wait for initial sync to clear state before asserting 'replSetGetStatus' reply has no 'initialSync' field
- SERVER-58625 Add multi_update tag to geo_update1.js to exclude from certain passthrough suites

### Query

- SERVER-54078 [SBE] Improve perf of the bestbuy_agg_merge_wordcount benchmark suite
- SERVER-58127 Fix benchRun() memory leak for parsing benchRun() args under exception
- SERVER-58372 Robustify deprecated_wire_ops_mongos.js

### Storage

- SERVER-50287 drop_index.js fails when run in passthrough suite with stepdown
- SERVER-56019 timeseries_index.js hangs in burn_in_tests burn_in:replica_sets_initsync_jscore_passthrough subtask
- SERVER-56877 insert operations may fail to set index to multikey after aborted multikey catalog update

### Operations

SERVER-58510 Fix 'use after free' issue in getExecutorForSimpleDistinct() function

### Build and Packaging

- SERVER-54729 MongoDB Enterprise Debian/Ubuntu packages should depend on libsasl2-modules and libsasl2-modules-gssapi-mit
- SERVER-55446 Stand up an Apple Silicon compile-only builder on the Xcode 12 enabled hosts.

### Internals

- SERVER-56446 Can't use ReplSetTest.restart() in _auth suites with waitForConnect: false
- SERVER-56568 Disable vptr UBSAN checks in dynamic builds and remove LIBDEPS_TYPEINFO
- SERVER-56620 Nodes should explicitly clear arbiter durableOpTimeAndWalltime
- SERVER-56625 validate cachedir race condition when cleaning bad cachefile
- SERVER-56980 Robustify jstests/core/query_hash_stability.js
- SERVER-57002 Refactor Evergreen task creation to support building multiple tasks
- SERVER-57003 Generate all tasks for a build variant in a single task
- SERVER-57064 Log create index and dropIndex(es) on mongos 
- SERVER-57176 The 'validateFeaturesAsPrimary' flag should be set to false while a node is in recovery phase
- SERVER-57268 add multikey query to validate_multikey_restart.js
- SERVER-57302 Generate implicit multiversion tests uses invalid name
- SERVER-57327 evergreen ninja builders fail to copy install file
- SERVER-57396 Enable visibility support by default on platforms where it is applicable
- SERVER-57425 Avoid killing opCtx while holding the SessionCatalog mutex
- SERVER-57450 Newly added tests do not show up in generated dynamic resmoke suites
- SERVER-57474 profile_operation_metrics.js not resilient to query yielding
- SERVER-57521 FCV change unconditionally closes outgoing connections that have not finished their hello handshake
- SERVER-57576 validate_cache_dir should print the stacktrace
- SERVER-57580 Simplify multiversion handling in evergreen.yml and task generation
- SERVER-57642 Invariant Failure on src/mongo/db/query/plan_yield_policy.cpp 75 | Aborting
- SERVER-57650 Make MigrationChunkClonerSource interruptible when waiting response to recipient commands
- SERVER-57676 Wait for a checkpoint before releasing the "hangOplogCapMaintainerThread" in oplog_rollover.js
- SERVER-57729 Cannot drop time-series collection if buckets collection does not exist
- SERVER-57742 Create a non-specialized version of the OperationLatencyHistogram class
- SERVER-57750 use a more distinct read command in quiesce_mode.js so that internal ops don't set off the failpoint
- SERVER-57756 Race between concurrent stepdowns and applying transaction oplog entry
- SERVER-57771 SBE explain does not report correct trial period statistics for a winning sort plan in "allPlansExecution" section
- SERVER-57790 Minimise the impact of FCV upgrade/downgrade between 4.4 and 5.0 with large routing tables
- SERVER-57798 Direct user to MongoDB Compass download page when failing to install MongoDB Compass due to a connection issue using ./install_compass
- SERVER-57837 Adding TSBS to system_perf.yml
- SERVER-57869 Shell getShardDistribution helper does not accumulate chunk counts on 5.0.0-rc1
- SERVER-57926 Adjust log level from the evergreen scons splunk task
- SERVER-57928 create_collection.js  should use a dedicated database name and avoid dropping the test database
- SERVER-57951 Incorrect data files archived by hook_test_archival.py
- SERVER-57983 Integer overflow for $range in Classic Engine
- SERVER-58020 cache-dir: prevent same buildsig with different content race condition
- SERVER-58022 tenant_migration_resume_oplog_application.js should account for resumeTokens being part of an application batch
- SERVER-58086 Investigate why debug symbols are not marked for download in some tasks
- SERVER-58087 Reduce overhead of activated generated tasks
- SERVER-58159 Extend relaxation of index ident reconciliation invariant for single-phase index builds
- SERVER-58169 Log timestamps info on hitting invariants around stable timestamp calculation
- SERVER-58187 Improve Connection Reaper and MongoLDAP performance
- SERVER-58191 [Migrate Protocol] Allow delete_during_migrate.js to tolerate chunk migration failures due to timeout in catchup phase in slow variants.
- SERVER-58197 Pass ranges by reference when constructing a Sorter from existing ranges
- SERVER-58202 mark several tests as requires_sharding
- SERVER-58208 Allow top-level $graphLookup stages to run in parallel on shards
- SERVER-58249 findAndModify_flip_location.js should account for racey upserts when run in multiversion suites against 4.4 binaries
- SERVER-58250 Inefficient usage of memory tracking map for $group and $setWindowFields
- SERVER-58280 initial sync hangs on hiding dropped index when index builds are active
- SERVER-58283 Add a new versioning file to set MONGO_VERSION and MONGO_GIT_HASH
- SERVER-58332 pipeline MemoryUsageTracker: change StringMap to unordered_map for pointer stability
- SERVER-58335 Remove SBE build variants from the 5.0 branch
- SERVER-58357 [ephemeralForTest] TemporaryKVRecordStore fails to register commit handler in WCE loop
- SERVER-58395 Resharding metrics should set donorState/RecipientState to kUnused if they are not initialized for currentOp report.
- SERVER-58400 Generated timeouts need to take repeated execution into account
- SERVER-58480 Add the necessary parameters to the ContinuousTenantMigration hook to allow for proper transient error retry 
- SERVER-58515 [ephemeralForTest] disable parallel task in EFT builder
- SERVER-58532 Take when a build is ASAN into account when calculating timeouts
- SERVER-58576 Improve tests for task generation
- SERVER-58651 Kill ssh tunnel process in exit handler in powercycle
- SERVER-58662 Disable tsbs on variants with older versions of mongodb
- SERVER-58707 Move `bench_test*.js` tests out of parallel test job 
- SERVER-58734 Add evergreen task for new change stream fuzzer
- SERVER-58746 Build failure on macOS 10.12; mongodb 5.0.0 requires macOS 10.13+?
- SERVER-58794 _configsvrCreateDatabase and _flushDatabaseCacheUpdates should accept any API version parameters
- SERVER-58816 errors_on_committed_transaction.js incompatible with multiversion tests in v5.0
- SERVER-58936 Unique index constraints may not be enforced
- WT-6280 Fail eviction if out of order handling races with checkpoint
- WT-6729 Quiesce eviction prior running rollback to stable's active transaction check
- WT-6782 test_prepare_hs02 WT_ROLLBACK failure: conflict between concurrent operations
- WT-6902 Metadata subpage for Architecture Guide
- WT-6914 Write "database files" subpage for Architecture Guide
- WT-7279 Allow multiple terminate calls for storage source extension
- WT-7343 Write a script that executes many-collection-test.py
- WT-7473 Resolve "TODO: tiered" comments in code
- WT-7507 Update salvage for a history store and timestamp world
- WT-7520 Add start and stop values to automatic flag generation code
- WT-7524 Refactor functions to obtain checkpoint list; Clear delete on skipping checkpoints
- WT-7539 Add a configuration option that allows the user to specify debug modes.
- WT-7543 Pass in the correct test name when constructing the default config path
- WT-7553 Loosen the restrictions around evicting fast-truncate pages to avoid cache-stuck failures
- WT-7556 Fix test_rollback_to_stable10 failure cache_hs_ondisk is 0
- WT-7603 Sort statistics to fix JSON output
- WT-7605 Drop support for million-collection-test
- WT-7609 Report on time taken to start and shutdown the database in many-coll-test
- WT-7616 Create a pass or fail test based on many collection workgen workload
- WT-7619 Add a new optimization to skip pages in cursor traversal when all entries on the page are deleted
- WT-7626 We only ensure update restore eviction happened in test debug mode09
- WT-7628 Return an error message when supplied invalid command line args in the test framework
- WT-7629 Run clang format on .cxx files in the codebase.
- WT-7632 Fix invalid argument in test_rollback_to_stable14
- WT-7640 Fix test_backup02 failure where checkpoint tables differ due to checkpoint cursor not supported
- WT-7660 Rename poc_test to base_test in the cpp test framework and add insert_operation logic
- WT-7667 Fix workgen JSON output
- WT-7668 Overload the update method for the hs_cleanup test
- WT-7670 Modify test tag format and tag additional python tests
- WT-7676 Reformat wtperf backup to only read in files instead of wt_copy_and_sync
- WT-7679 Create an evergreen test for many-dhandle-stress
- WT-7683 Add python test hook to call flush_tier() during connection.close()
- WT-7687 Stop tiered manager thread before internal thread
- WT-7689 Fix double free in __curhs_insert
- WT-7690 Fix coverity error when enum is compared against 0 (incr_backup:table_changes)
- WT-7692 fix make check test failure on osx10 14 cmake
- WT-7696 Fix coverity error - Unused variable in _rollback_to_stable_btree_apply_all
- WT-7698 Decrease max_latency value in many dhandles scenario for workgen
- WT-7703 Fix timeout in test_checkpoint_snapshot04 
- WT-7705 Add an assert to ensure that there are no updates on the new disk image in update restore
- WT-7707 Simplify insert splits to use the splitting WT_REFs key
- WT-7708 Add an assert to ensure the durable timestamp is larger than stable timestamp at the end of prepared commit
- WT-7715 Fix uninitialized bool in txn_ckpt.c
- WT-7717 Change macros in local_store.c to use WT namespace
- WT-7719 Change default value of ENABLE_STRICT to "OFF" (CMake Usability Improvements)
- WT-7720 Update POSIX CMAKE doxygen documentation (CMake Usability Improvements)
- WT-7723 Delete the updates in the history store if they are rolled back or is the first stable update on the update chain
- WT-7724 Fix race when running concurrent checkpoint and flush_tier
- WT-7725 Add missing brackets around parameter in macro definition
- WT-7726 Separating out the validation portion from the database model
- WT-7727 Fix null pointer passed to memcpy() during 'format' test.
- WT-7729 Fix to write out correct tiered information on checkpoint
- WT-7730 Shifting the oldest and stable timestamps to match the commit timestamp format
- WT-7732 Add a timeout configuration for flush_tier
- WT-7739 Switch back to using MacOS 10.14 for Evergreen compile task
- WT-7741 Fix misaligned address in crc32-x86.c
- WT-7742 Fix misaligned address in wt3184_dup_index_collator/main.c
- WT-7743 Fix integer overflow within wt2999_join_extractor csuite test
- WT-7744 Fix null pointer within wt3338_partial_update csuite
- WT-7746 Improve directory syncing with CMake helper 'create_test_executable' 
- WT-7748 Fix CMake library probes for libraries not on the default linker path
- WT-7749 Assorted fixes for (and from) building and testing on NetBSD
- WT-7751 Add an assert to ensure we never select an update that has been written to the history store for data store
- WT-7752 Update packing code according to documentation
- WT-7754 Fix race when updating block manager file handle
- WT-7755 YSCB: Add a native implementation of YCSB to WTPERF.
- WT-7756 RTS to clear the HS flag of an update following tombstone 
- WT-7758 Force evict a page when the update chain is too long
- WT-7761 Improve debug_print to include timestamp, thread_id and reorder args in cppsuite.
- WT-7762 Create stressful configs for the two tests add them to evergreen.
- WT-7763 Coverity issues found in the stress testing framework
- WT-7765 Fix signed integer overflow in intpack-test3
- WT-7766 Fix null pointer passed to memset in test_wt3338_partial_update
- WT-7767 Code cleanup for curhs_remove and __txn_fixup_prepared_update
- WT-7770 Fix issue linking TCMalloc in CMake
- WT-7776 Add a hard limit on the number of modify updates before we instantiate a complete update
- WT-7778 Fix null dereferencing, and return of incorrect allocation size
- WT-7780 Guarantee log message sequencing in the test framework.
- WT-7781 Avoid skipping python tests for 3rd party ext libraries in CMake builds
- WT-7782 Separate implementation from headers in cppsuite test framework
- WT-7784 Enable RTS to use checkpoint snapshot on timestamp tables
- WT-7787 Don't read pages for checkpoint cleanup when the cache is in aggressive mode 
- WT-7789 Change tiered python tests to fail without extension library
- WT-7795 Fix CppSuite failure "expected ) before PRIxMAX"
- WT-7796 Scan the tracking table and delete parts of it that are obsolete.
- WT-7797 Disable postrun stats in CppSuite testing
- WT-7799 Do not report failure of wiredtiger_open in python tests to output
- WT-7802 Remove data store same transaction update squash logic
- WT-7804 Fix test_hs24 committing mixed mode update from the wrong value
- WT-7807 Remove unused arg in backup_config
- WT-7811 Fix test_hs24 not commiting from 0 timestamp
- WT-7813 Stop inserting to history store if we see a prepared update
- WT-7815 Properly initialize prev_upd_ts for ordered timestamp assertion
- WT-7817 Make tiered storage address cookies backward compatible
- WT-7825 Fix test_hs24 key order
- WT-7831 Clear transaction ids from previous run when repack the cell
- WT-7832 Add an encryptor extension that uses the libsodium cryptography library.
- WT-7836 Fixing a number of small issues in the cppsuite test framework
- WT-7837 Clear updates structure in wt_hs_insert_updates to avoid firing assert
- WT-7841 add "only unencrypted" checksum configuration, switch checksum default to "on"
- WT-7843 Add missing macros to define PRIxMAX
- WT-7846 Disable test_tiered08
- WT-7851 Fix illegal checksum configuration in compatibility-test-for-newer-releases
- WT-7852 Don't release eviction server lock when evicting pages
- WT-7856 Enable flush test with open cursor in test_tiered04
- WT-7864 Add support to run.py for running lists/ranges of scenarios in a test
- WT-7865 Disable timeout assert while waiting for eviction to quiesce prior to RTS and test
- WT-7870 Fix measurement of cyclomatic code complexity
- WT-7871 Remove comment that is no longer true
- WT-7874 Remove two other stale comments
- WT-7883 Remove incorrect wt_free statement
- WT-7889 Find/replace existing uses of WT with WiredTiger in reference guide
- WT-7890 Fix CMake syntax error in config_lib


## 5.0.1 Changelog

### Replication

SERVER-58398 Tenant migration hung indefinitely

### Internals

- SERVER-58142 TenantOplogBatcher should transition to complete when the next batch callback is called with error status
- SERVER-58171 Changing time-series granularity does not update view definition
- SERVER-58489 Collection creation stuck in an infinite writeConflictRetry loop when having a duplicate name as a view
- SERVER-58546 Add log message to applyOps to preview which oplog entries will be applied
