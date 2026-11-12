<!-- Part 7 of 12 of release-notes/5.0-changelog.md (split because the page is big). -->

## 5.0.7 Changelog

### Sharding

- SERVER-60109 Ensure vector clock is recovered on step-up
- SERVER-61249 refine_collection_shard_key_basic.js relies on a best-effort refresh that might not happen in case of failover
- SERVER-61444 Resharding uses of bumpCollectionVersionAndChangeMetadataInTxn are not idempotent
- SERVER-61755 Migration recovery should handle refined shard key
- SERVER-62072 _configsvrReshardCollection may return without having waited for unsetting "reshardingFields" to replicate to majority
- SERVER-62521 Distributed locks might not be released on definite error when using a DDL coordinator
- SERVER-62761 [v5.0] receiveChunkWaitForRangeDeleterTimeoutMS is being passed on 4.4 binaries
- SERVER-62906 Add a check in the createCollection/shardCollection path verifying the collection name length
- SERVER-62907 Vector clock components must survive CSRS non-rolling restart
- SERVER-63722 Rename collection participants get stuck upon errors different from stepdown/shutdown
- SERVER-63742 Default topology time in shard can lead to infinite refresh in shard registry
- SERVER-64517 RecoverableCriticalSection is not properly recovered on startup
- SERVER-64580 Step downs while sharding a collection in mixed binaries shards might crash the old binary

### Replication

SERVER-54374 Race between signalOplogWaiters and StorageEngine::loadCatalog

### Query

SERVER-40691 $nin:[[],...] queries are not indexed

### Operations

SERVER-21070 Add option to gather collection stats

### Internals

- SERVER-51456 Database Profiler outputs incorrect value of property "keysDeleted"  for a remove operation when a write conflict occurs
- SERVER-53993 Attach client strand before releasing the opCtx in AsyncCommandExecution tests
- SERVER-56300 Add append range functionality to BSON obj and array builders
- SERVER-56558 Robustify validate_db_metadata_command.js test
- SERVER-56931 instrument ASIO set_option failures better
- SERVER-57662 Wait for config.system.sessions collection to exist on the config server before refreshing logical session cache
- SERVER-58069 ASSERT_THAT matcher framework for unit tests
- SERVER-58152 Create Feature flag for Remove Faulty Mongos From Cluster Topology
- SERVER-58310 ThreadPoolTaskExecutor is memory unsafe when task cancellation occurs around the same time an exhaust network response is received
- SERVER-58499 Add a new error code LoadBalancerSupportMismatch
- SERVER-59220 Connectivity probes in ocsp_server_refresh.js should use fresh shells
- SERVER-59223 Improve ecs scp robustness
- SERVER-59290 Re-evaluate sync source after incrementing config version
- SERVER-59356 Create dummy FaultManager singleton, FaultStatus enum and dummy unit test
- SERVER-59357 Create dummy Fault class and dummy unit test for it
- SERVER-59358 Create FaultFacet interface, mock implementation and unit test running mock that imitates a failure
- SERVER-59360 Create HealthObserver interface, mock implementation and unit test invoking the periodic check with mocked failure
- SERVER-59361 Implement periodic health check thread pool
- SERVER-59362 Setup Fault Manager State Machine
- SERVER-59364 Should move to the OK state after performing a successful round of health checks when in the StartupCheck state
- SERVER-59365 Should not transition to OK state if initial health checks are not completed successfully
- SERVER-59366 Progress monitor for periodic health check
- SERVER-59367 Should create in-memory Fault instance when entering the TransientFault state
- SERVER-59370 Should Transition to ActiveFault state when in the TransientFault state for kActiveFaultDuration
- SERVER-59382 Enforce non-critical facets not entering ActiveFault state
- SERVER-59390 Should provide the ability to perform periodic health checks against config server
- SERVER-59397 implement randomization for health check periods
- SERVER-59496 Fault class should be a container of active fault facets
- SERVER-59522 HealthCheckStatus should track fault status and lifetime
- SERVER-59567 Periodic check should invoke observers, simulate HealthObserver Mock failure
- SERVER-59608 Coverity analysis defect 120502: Parse warning
- SERVER-59912 Initial no-op scaffolding of the Ldap health checker
- SERVER-60079 Common health observer code to incorporate generic patterns from Ldap observer
- SERVER-60316 FaultManager should start with periodic checks disabled
- SERVER-60412 Host memory limit check does not honor cgroups v2 
- SERVER-60587 Implement FaultFacet
- SERVER-61016 Swallow connection reset-related errors received during ASIOSession creation on outbound connection.
- SERVER-61095 Improve transport_layer_asio_test.cpp
- SERVER-61104 Robustify find_and_modify_invalid_query_params.js 
- SERVER-61220 Integration test for Progress monitor
- SERVER-61315 Ldap health check executor should support aborted tasks
- SERVER-61368 FaultManager test suite should use real thread pool
- SERVER-61438 Fix race in health_observer_test.cpp
- SERVER-61490 transport_layer_test: asio connect race
- SERVER-61592 Querying with ms precision does not return expected results (TS collection) 
- SERVER-61662 SCons configure checks should always run with verbosity
- SERVER-61706 make sure that the new config has reached all nodes in cluster_x509_rotate
- SERVER-61769 Attempting to run an aggregation with $out or $merge in a transaction on a sharded cluster leaves idle cursors open
- SERVER-61871 use tassert for state machine programmer errors
- SERVER-61872 Fix thread pool starvation in FaultManager
- SERVER-61873 LDAP health observer runtime params
- SERVER-61914 add fault facet details to FaultImpl::toBSON
- SERVER-61921 Link failure in noSSL mode in FaultManager
- SERVER-61956 fix data race when accessing the state machine's state
- SERVER-61977 Concurrent rollback and stepUp can cause a node to fetch from a timestamp before lastApplied once it has stepped down. 
- SERVER-62017 Enable all feature flags by default in the sys-perf all feature flags variant
- SERVER-62084 Serializer for FaultFacetType is broken
- SERVER-62085 Use more bits for hashedMultikeyMetadataPaths in validation
- SERVER-62096 /proc/<id>/smaps is not available
- SERVER-62098 Guard healthCheckContexts with mutex in fault_manager.cpp
- SERVER-62192 Handle feature flag disabled for implicit sharding accessed collection
- SERVER-62242 $indexOfArray does not work with duplicate values in array
- SERVER-62285 validate cachedir add push failure debug messages
- SERVER-62368 Range deleter must honor rangeDeleterBatchDelayMS
- SERVER-62379 Fix deadlock between ReplicationCoordinator and BackgroundSync on stepUp
- SERVER-62466 _lastTransitionTime stat field in FaultManager is never changed
- SERVER-62511 Race in dbcheck_no_history_on_secondary.js
- SERVER-62513 RunDBCheckInBackground should retry on Interrupt errors
- SERVER-62514 dbcheck_write_concern.js should prevent primary from stepping down
- SERVER-62569 IDL Compatibility Checker script doesn't properly handle array types
- SERVER-62651 Add enable all feature flags by default feature to Enable all feature flags by default to microbenchmark project.
- SERVER-62668 Synchronize access to ImpersonatedUserMetadata  in OperationContext.
- SERVER-62680 validate cachedir make local tmp to ensure successful copy
- SERVER-62682 PrimaryOnlyService Does Not Call _rebuildCV.notify_all() leading to calls to waitForConditionOrInterrupt not being triggered
- SERVER-62712 validate cachedir isolate cache errors to only the cache debug log file
- SERVER-62876 Stop testing tenant migrations with capped collections
- SERVER-62948 Ensure FTDC collectors don't have a read timestamp
- SERVER-63010 Ensure that unpacking measurements doesn't overwrite pushedown addFields that are computed on meta data
- SERVER-63073 Fix ShardNotFound handling in shard_removal_triggers_catalog_cache_invalidation.js
- SERVER-63079 Avoid using projection parser in $setWindowFields
- SERVER-63097 stepdown_race_with_transaction.js should use the "uses_transactions" tag.
- SERVER-63141 Difference in $lookup/$redact/$let behaviour with pipeline optimization
- SERVER-63197 Pin microbenchmarks genny version
- SERVER-63201 Relax restriction of deletion ops in applyOps command.
- SERVER-63203 Chunk splitter never splits if more than 8192 split points are found
- SERVER-63214 Ignore hash inconsistency between whole dbs when collection hash mismatch between image collections
- SERVER-63234 Better logging to explain LDAP health check flakiness
- SERVER-63239 Do not throw exception in AutoSplitVector on empty ranges
- SERVER-63240 clearJumboFlag might persist a ChunkVersion with a wrong format
- SERVER-63250 Fix implicitly sharding timeseries collections feature flag check
- SERVER-63279 Pushing predicates on the time-series metaField past unpacking can cause incorrect results
- SERVER-63288 Add debug log messages for queryable http calls
- SERVER-63417 Oplog fetcher should not retry when a node is known to be down
- SERVER-63428 Robustify oplog applying code for update operation
- SERVER-63432 Transferring large file to repo
- SERVER-63471 waitForPrimaryOnlyServices finish rebuilding before testing stepDown in no_disconnect_on_stepdown.js
- SERVER-63497 Fix icecream debugging
- SERVER-63505 Ensure arbiter recognizes primary node in rollback_views.js
- SERVER-63512 Use optimized (no isSelf calls) reconfiguration on heartbeat reconfig
- SERVER-63531 commitQuorum error message incorrectly says that only voting nodes are eligible 
- SERVER-63646 _raise_if_unsafe_exit uses wrong return_code
- SERVER-63859 Disallow collMod with expireAfterSeconds on a view
- SERVER-63876 [5.0] Secondary nodes crash when applying collMod with index.expireAfterSeconds option
- SERVER-63968 Prohibit enumeration of builtin roles on $external database
- SERVER-63974 Pin version of itsdangerous python dependency
- SERVER-63986 Disallow 4.x running update_with_dollar_fields.js
- SERVER-64182 Re-enabling health checks should check if another pending check was already scheduled
- SERVER-64304 Using --recoverFromOplogAsStandalone can result in index builds crashing the server
- SERVER-64369 Must not allow deletes from capped collections in FCV 4.4
- SERVER-64403 Find queries with SORT_MERGE collation-encode the missing sort attribute 
- SERVER-64555 [5.0] Allow new unique index data formats to exist
- WT-7922 Handle missing WiredTiger version file
- WT-7954 Use longer flush_tier timeout in test_tiered04
- WT-8074 Panic in reconciliation if inserting content into the history fails
- WT-8149 Updating metadata salvage csuite test to handle salvaging table metadata without salvaging file metadata
- WT-8198 Switch the bulk load cursor to a scratch buffer
- WT-8320 Select updates restored from history store irrespective of visibility
- WT-8362 Remove or rewrite HS entries of a key when OOO tombstone is written to datastore
- WT-8417 Restructure assert testing in search near 01 cpp for concurrency
- WT-8422 Clear the on-disk cell time window if it is obsolete
- WT-8424 Use consistent toolchain in little-endian
- WT-8477 Enforce the use of Pymongo 3.12.2 in our Evergreen tests
- WT-8598 Avoid checkpoint cleanup always on shutdown
- WT-8605 Disable the perf tests for non-develop branches in Evergreen
- WT-8649 WT_SESSION methods cannot release scratch buffers unless reset or closing
- WT-8743 Configure hs_cleanup configuration to stress the cache less
- WT-8753 Add tombstone when rolling back in-memory, prepared, reconciled updates
- WT-8799 Disable documentation update on mongodb-5.0
- WT-8874 Disable compatibility tests on mongodb-5.0
- WT-8879 Set the OOO flag when the selected tombstone is globally visible
- WT-8894 Find the path to the mongod executable for many-collection-test
