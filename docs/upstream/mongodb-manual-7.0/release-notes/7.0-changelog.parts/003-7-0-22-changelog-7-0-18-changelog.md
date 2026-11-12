<!-- Part 3 of 10 of release-notes/7.0-changelog.md (split because the page is big). -->

## 7.0.22 Changelog

### Sharding

SERVER-99440 Add timeout parameter for check metadata
consistency database operation

### Replication

- SERVER-85915 Cannot select sync source because we are a voter
  and it is not
- SERVER-98831 Don't take replication mutex twice when
  processing heartbeats

### Internals

- SERVER-82755 Create feature flag
- SERVER-82756 Enable feature flag
- SERVER-83963 Return early in renameCollectionForApplyOps if
  sourceNss and targetNss are the same
- SERVER-85692 Ignore optimizationTimeMillis in a js test
- SERVER-85804 Support Proxy Protocol on Mongod
- SERVER-86268 Check collection options consistency between
  local and sharding catalog
- SERVER-87572 Add serverStatus() metric to count replanning
  events
- SERVER-89699 Properly detect when OpenLDAP includes
  MozNSS-compatible shims
- SERVER-89919 Add testing matrix to backup and restore
- SERVER-90472 Coverity analysis defect 155588: Using invalid
  iterator
- SERVER-91299 Refresh MultiCollectionAccessor after doing
  multi-planning
- SERVER-91374 Fix data race between getTerm and updateTerm in
  _doReplSetReconfig
- SERVER-92023 Extract only $readPreference from $queryOptions
  in mongo test shell
- SERVER-92419 shardedDataDistribution returns null for
  ownedSizeBytes if there are no documents
- SERVER-92476 planningTimeMicros can include work not related
  to planning
- SERVER-93213 Optimize
  getTimeseriesBucketsMayHaveMixedSchemaData to parse the storage engine
  option only once
- SERVER-93367 Reduce the number and the size of documents to
  insert in create_index_background tests
- SERVER-93432 Wait for failpoint before killing the op in
  fle2_contention_kill_parent.js
- SERVER-94193 Prevent insertions on
  all_shard_and_config_hosts_brought_down_one_by_one from timing out on
  slow variants
- SERVER-94530 Change ExpressionContext::getResolvedNamespaces
  invariant to a tassert
- SERVER-94650 Ban causal_consistency_shell_support.js from
  config-stepdown test suite
- SERVER-94657 The restore role should allow dropping
  system.views in any database
- SERVER-95430 Provide link to raw logs when parts of a task
  time out
- SERVER-95523 upsert does not handle DuplicateKey retry
  correctly
- SERVER-95524 Avoid retrying on duplicate key error for
  upserts in multidocument transactions
- SERVER-95682 Create feature flag
- SERVER-95683 Enable feature flag
- SERVER-96107 $lookup, $graphLookup, and $unionWith can read
  from the wrong database when run with $merge or $out
- SERVER-96197 ExpressionContext's _resolvedNamespaces can't
  distinguish between collections with the same name in different dbs
- SERVER-96269 Modify speculative authentication auditing
- SERVER-96503 Add more log lines to FCBIS
- SERVER-97403 Replace invariants with tasserts in document
  validation error generation
- SERVER-97462 Retrying skipped records can try deleting record
  without wuow
- SERVER-97662 Don't parameterize queries for SBE plan cache
  when the SBE plan cache is unreachable
- SERVER-97898 Expose proxy endpoints in AsioSession API
- SERVER-97903 Create AuditClientAttrs Client decoration
- SERVER-97908 Propagate AuditClientAttrs across Clients via
  ForwardableOperationMetadata
- SERVER-97920 Update AuditEventMongo and AuditEventOCSF to use
  AuditClientAttrs
- SERVER-98160 Register AuditClientObserver solely when
  auditing is enabled
- SERVER-98386 Shard does not correctly check the ShardVersion
  received for timeseries collections
- SERVER-98417 Add test for records in the skipped record
  tracker that are no longer found in the collection
- SERVER-98965 [v7.0] timeseries_reopened_bucket_insert.js
  manually creates buckets with embedded timestamps that do not match
  the control.min.timestamp
- SERVER-99236 Remote commands submitted by the
  BalancerCommandsScheduler should be interrupted when a step down
  occurs.
- SERVER-99488 Include sourceClient in connection accepted
  system log
- SERVER-99584 Add tests for AuditClientAttrs BSON
  (de)serialization methods
- SERVER-99616 $group can hit MONGO_verify
- SERVER-99660 Write end-to-end load balancer test for auditing
  mongo-formatted client IPs via proxy protocol
- SERVER-99678 Add proxyPort CLI to mongod
- SERVER-99817 Time-series bucket rounding for pre-1970 dates
  is incorrect in some cases for millisecond precision
- SERVER-99834 Support non-OCS client on mongos loadBalancer
  port
- SERVER-99836 Use proxied source remote endpoint in
  shouldOverrideMaxConns
- SERVER-100182 Fallback to netstat if ss is not supported in
  variant
- SERVER-100468 Write end-to-end load balancer test for
  auditing OCSF-formatted client IPs via proxy protocol
- SERVER-100609 Resolve sbom schema reference spdx.schema.json
  to a local copy
- SERVER-100840 Fix queries in abt_translation_bm
- SERVER-101078 Do not close connection sending
  loadBalanced:true in mongod
- SERVER-101164 Use pyinstaller binaries for db-contrib-tool
- SERVER-101170 CheckMetadataConsistency to not use
  MONGO_UNREACHABLE
- SERVER-101230 Coverity analysis defect 155126: Using invalid
  iterator
- SERVER-101242 Fix race condition in
  ConnectionInterface::getTimesUsed()
- SERVER-101296 Remove aws_e2e_ecs.js test
- SERVER-101337 Exhaust responses should assert that they are
  an OP_MSG
- SERVER-101389 MockServerStreamTest cancel tests should wait
  for operations to finish after cancel
- SERVER-101530 Add the ability to change the catalog cache
  size at startup via Server Parameter
- SERVER-101700 setup_spawnhost_coredump script is failing to
  run on Evergreen hosts
- SERVER-101716 read_through_cache.h function throws exception
  on noexcept method
- SERVER-102276 [v7.0] Coverity analysis defect 169621: Data
  race condition
- SERVER-102338 [v7.0] -- Coverity analysis defect 169091: Data
  race condition
- SERVER-102735 Upgrade db-contrib-tool to 1.0.0
- SERVER-102787 Add mongo and OCSF audit tests behind load
  balancer for standalone and replset
- SERVER-102872 Use OS-specific db-contrib-tool pyinstaller
  builds for PPC
- SERVER-103286 Add retries when getting info from ss and
  netstat
- SERVER-103749 CheckOrphansAreDeletedHelpers must account for
  lazy recovery of unfinished migrations
- SERVER-103824 Add jstest that uses different IP for proxy
  server and source client
- SERVER-103862 proxy_protocol_connect.js isn't running
  assertions
- SERVER-104205 more specific parsing of "netstat" output in
  proxy sharding tests
- SERVER-105553 [7.0] Add ddl_view_events.js entry to
  backports_required_for_multiversion_tests.yml
- SERVER-105611 Upgrade MozJS/Spidermonkey to ESR 128.11
- SERVER-105903 [v7.0] Duplicate equality predicate prevents
  index suffix from satisfying sort
- SERVER-106050 [v7.0] Collection validation does not check
  time ordering correctly for time-series v3 buckets
- SERVER-106122 Remove loadTest and reduce load from fuzzTest
  on proxy protocol testing
- SERVER-106297 Implement getProxiedSrcRemoteAddr in
  grpc_session


## 7.0.21 Changelog

### Query

- SERVER-95672 Indexes on array fields that contain subarrays
  does not include some results
- SERVER-97629 Replace invariant with tassert when yielding

### Storage

#### WiredTiger

- WT-13216 Assess the use of cache eviction check in compact

### Operations

WT-12012 Restore original verbose levels if gen_drain becomes
unstuck after increasing verbose levels

### Build and Packaging

SERVER-51366 Configure folders created by installer

### Internals

- SERVER-73498 Add time spent in the multi-planner to the
  explain output
- SERVER-82762 All the accesses to the state of the AutoMerger
  should be protected by a mutex
- SERVER-88891 Delete tenant migration and shard split / merge
  passthrough and integration tests
- SERVER-90449 Prevent TTL Monitor from running collMod during
  rollback and initial sync fuzzers
- SERVER-90997 Relax the assertion when the document is not
  found in doDeleteRecord()
- SERVER-91272 Do not printStackTrace that does not warrant
  Atlas Failure Monitor
- SERVER-91314 Kill spillable queries when disk space is low
- SERVER-91774 Linter that checks require_fcv_* tags are <=
  current version
- SERVER-91933 Data race accessing
  CollectionTruncateMarkers::_minBytesPerMarker
- SERVER-92137 Make sure timeseries inserts perform a
  ShardVersion check before inspecting the existence of the buckets
  collection
- SERVER-92239 change streams don't survive stepdowns when a
  rollback also occurs.
- SERVER-92259 Namespace resolution from UUID does not check
  pending commit namespaces
- SERVER-92273 [v7.0] ListCollections has inconsistent behavior
  for commit pending namespaces (7.0 only)
- SERVER-92673 Increase assertion timeout of health observer
  tests
- SERVER-92797 Fix behavior when running next() over a closed
  exhaust cursor
- SERVER-92806 Plan cache entry ignores index collation with
  $elemMatch
- SERVER-93389 WiredTigerSessionCache does not properly dispose
  of sessions released after rollback
- SERVER-93497 Move user cache invalidation from OpObserver to
  onCommit handlers
- SERVER-93771 Set enterprise-rhel-81-ppc64le timeouts on
  variant level
- SERVER-93917 [v7.0] Evaluate whether array -> object
  interleaved bug applies to 7.0 and prior
- SERVER-93963 Replace ?. syntax in
  query_by_uuid_commit_pending.js
- SERVER-94156 Support upsert duplicate key retry if unique
  index has collation
- SERVER-94272 Reduce powercycle timeouts to meet Evergreen
  constraints
- SERVER-94649 Increase logging of direct shard connection
  errors and warnings
- SERVER-94662 Retry pipx install db-contrib-tool
- SERVER-94731 Emit change stream events for the system.views
  collection (when showSystemEvents is enabled)
- SERVER-94970 sharded $searchMeta queries in a $lookup and
  $unionWith fail by hitting an unreachable_tassert
- SERVER-95311 Determine default value for
  reshardingDelayBeforeRemainingOperationTimeQueryMillis
- SERVER-95610 Update version check for
  reshardingDelayBeforeRemainingOperationTimeQueryMillis in servers.js
- SERVER-95775 Update MSI to reference libsasl2.dll instead of
  libsasl.dll
- SERVER-95869 Transform
  CommandOnShardedViewNotSupportedOnMongod into
  CommandNotSupportedOnView on all code paths
- SERVER-96404 Improve variable names in $map and $filter
  serialization
- SERVER-97044 Fix an issue where change streams might
  incorrectly output a "drop" event during resharding or unsharding of a
  collection that is or was using zone sharding
- SERVER-97254 $jsonSchema parser should not use empty strings
  to distinguish between top level schemas and sub schemas
- SERVER-97405 Add server parameter to skip oplog sampling
- SERVER-97726 Prevent deleting ident directories concurrently
  with creation
- SERVER-98349 Avoid mongos to sleep for 3 secs before shutting
  down
- SERVER-98555 Fix Jepsen and Antithesis to https cloning
- SERVER-98937 Handle interruptions while accessing ASIO
  sockets
- SERVER-101519 fix dbCheck test to not error out when a view
  is used after a collection
- SERVER-101807 Log the oplog entry when we throw
  OplogOutOfOrder
- SERVER-101880 [v7.0] Remove "openssl 1.1.1" distros
  references from evergreen
- SERVER-102115 Add RHEL9 enterprise as target for curator
- SERVER-102941 [v7.0] Collection validation should not enforce
  sortedness for v3 time-series buckets
- SERVER-103093 [v7.0] Move dismissDisposal() of
  _mergingPipeline from DocumentSourceInternalSearchRemoteMongot
  constructor
- SERVER-103275 Upgrade MozJS from ESR 128.8 to latest version
  (ESR 128.10)
- SERVER-103607 [v7.0] Ensure events are replicated prior to
  testing in change-stream_null_existence_eq_rewrite_test
- SERVER-104118 Update Okta OIDC authentication script
- SERVER-104206 Add does_not_support_causal_consistency tag to
  timeseries_lastpoint_top.js
- SERVER-104693 [v7.0] Add pointers to sys-perf's compiles.yml


## 7.0.20 Changelog

### Storage

#### WiredTiger

- WT-11199 The sweep server is not reconfigured correctly
- WT-12280 Access evict_aggressive_score atomically
- WT-13283 Fix the cache aggressive mode not to show the
  garbage value

### Internals

- SERVER-60823 runCommandWithRetries in JS test framework
  exceeds JS interpreter recursion limit
- SERVER-84770 Change stream tests do not recover from
  resumable change stream errors
- SERVER-90724 fsm_workloads/agg_unionWith_interrupt_cleanup.js
  incorrectly uses shard name as replica set name when constructing a
  connection string
- SERVER-93120 FTDC collection blocked on locked backupCursor
  state read
- SERVER-95237 Make update_replace_id.js test robust
- SERVER-96128 Remove references to linkbench in
  system_perf.yml
- SERVER-100387 Make error code linter work with 6 digit SERVER
  ticket ids
- SERVER-100673 Add support for RHEL 9 zSeries
- SERVER-100723 Configure scheduled test builders on m8g/AL2023
  for MongoDB v6.0+
- SERVER-100856 ocsp_sharding_basic needs to have stapling
  disabled
- SERVER-102004 Update last_lts_mongos_commands.js &
  last_lts_mongod_commands.js
- SERVER-102116 Bump s390x concurrency to 16x
- SERVER-102389 remove unnecessary tests from
  backports.yml
- SERVER-102475 Update jstests/noPassthrough/spill_to_disk_server_status.js
- SERVER-102526 Upgrade MozJS to ESR 128.8
- SERVER-102547 Remove push, publish_packages, and crypt_push
  tasks from Graviton 4 variants in v7.0 and v8.0
- SERVER-103600 Fix database_versioning_all_commands.js
- SERVER-103828 Handle empty socket in peekASIOStream


## 7.0.19 Changelog

This release contains security or reliability improvements. The changelog will 
be updated when more information is available.


## 7.0.18 Changelog

### Query

SERVER-97470 findAndModify: Mongos WriteConcernError Behavior
Differs from Mongod

### Storage

#### WiredTiger

- WT-10849 failed: format-stress-test-1 on
  ubuntu2004-stress-tests-arm64 [wiredtiger @ 593bf276]
- WT-11448 Fix truncation mismatch verification test problem
- WT-12528 Add a stat when background compaction skips a file
  because of conflicting checkpoint
- WT-12846 Fix how compact walk handles EBUSY from checkpoint
  flush_lock
- WT-13642 Create separate statistics for dirty leaf/internal
  pages

### Build and Packaging

SERVER-95976 Introduce "matchCollectionUUIDForUpdateLookup"
parameter in the change stream stage

### Internals

- SERVER-71590 Coverity analysis defect 134195: Using invalid
  iterator
- SERVER-82037 Memory used by sorter spills can grow without
  bound
- SERVER-82367 Enqueued refreshes under the same
  inProgressLookup entry are always called with the same cached value in
  the ReadThroughCache
- SERVER-83221 Clustered Collections listIndexes should show
  TTL
- SERVER-87169 Running cluster level
  _configsvrCheckMetadataConsistency hits a mongo unreachable invariant
- SERVER-87433 Handle failover behavior for
  ReshardingRecipientService during abort
- SERVER-87729 [v7.0] Disable FCV-gating for
  featureFlagQueryStats
- SERVER-88400 shardedDataDistribution aggregation stage must
  not return null fields for timeseries
- SERVER-89315 Coverity analysis defect 147940: Different smart
  pointers managing same raw pointer
- SERVER-89320 Coverity analysis defect 139793: Overflowed
  integer argument
- SERVER-89322 Coverity analysis defect 149003: Overflowed
  integer argument
- SERVER-89328 Coverity analysis defect 147636: Using a moved
  object
- SERVER-89718 Coverity analysis defect 140718: Using invalid
  iterator
- SERVER-90176 OplogBufferLocalOplog cursor should not time out
- SERVER-90689 Change THP startup warning checks to also look
  at process level settings before emitting warning
- SERVER-91334 Onboard MongoDB Server to Papertrail Service for
  SSDLC Compliance
- SERVER-92292 Skip ticket acquisition for prepareTransaction
- SERVER-95452 Prevent CollectionRoutingInfoTargeter from
  iterating all chunk ranges during update and delete
- SERVER-97700 [v7.0] Validation should support timeseries v3
  bucket
- SERVER-98345 Update amazon2 distros to latest in sys-perf
  compiles
- SERVER-98473 Repoint sys-perf to use genny-tasks from DSI
- SERVER-98720 Add missing redact() calls to "Plan executor
  error" warning logs
- SERVER-99277 Sharding metadata invalidated on shard removal
- SERVER-99620 Create sys-perf AL2023 compiles
- SERVER-99833 [v7.0] Swap ubuntu20 ARM variant from running on
  ubuntu18 to running on ubuntu20
- SERVER-100901 Relax user digest invariant to tassert in
  ShardingTaskExecutor
- SERVER-101322 [v7.0] Coverity analysis defect 168904:
  Uninitialized scalar variable
- SERVER-101324 Coverity analysis defect 169043: Using invalid
  iterator
- SERVER-101461 Clarify numOrphanedDocs and numOwnedDocuments
  returned by $shardedDataDistribution will report num of buckets for
  timeseries collections
