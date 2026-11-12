<!-- Part 1 of 10 of release-notes/7.0-changelog.md (split because the page is big). -->

## 7.0.48 Changelog

### Storage

#### WiredTiger

- WT-11269 Account for would-be aborted in-memory updates in
  RTS dry run
- WT-12096 __rec_validate_upd_chain(): Do not return EBUSY if
  globally visible.
- WT-13525 Migrate to AWS-based MacOS hosts
- WT-15838 Add logging if checkpoint is blocked by eviction for
  more than 1 minute
- WT-16959 Invalid access at address in __wt_ref_addr_copy
- WT-17598 Batch per-update cache atomics in
  __wti_page_inmem_updates

### Operations

- WT-15888 Increase verbosity of the proxy cell selected with
  child original assertion failure
- WT-16379 Crash during recovery due to corrupted journal file
  leads to repeated creation of new journal files on restart
- WT-17183 test_prepare20 fails due to corrupted logs

### Internals

- SERVER-98105 Pause drop pending ident reaper until backup
  cursor is closed
- SERVER-108215 Impose limits on the number of active
  multi-document transactions
- SERVER-117823 Add new queryable encryption metrics for
  insert, find, update, and delete
- SERVER-128131 Update enterprise-ubuntu2204-jepsen to specify
  itself as a compile variant
- SERVER-132098 Upgrade timelib and timezone data files to
  2026e
- SERVER-132514 Consolidate Evergreen retry setup and fix
  retries never applying
- SERVER-133297 Add FSM coverage for renameCollection racing
  with target collection creation when dropTarget is true
- SERVER-133299 Add FSM coverage for renameCollection racing
  with target collection creation when dropTarget is false
- SERVER-135389 Replace std::ranges::find with std::find in
  session_workflow_test.cpp in v7.0
- SERVER-137172 [v7.0] Disable LDAP TLS test in
  ldap_authz_bind.js on platforms with OpenSSL 3
- WT-10897 Make WT::compact command more test friendly in the
  MDB layer
- WT-10928 Compact prints "skipping compaction" even when the
  compaction was not skipped
- WT-12765 test_txn24.py has ROLLBACK failures on Mac and
  Windows
- WT-16780 Insufficient error context in WT_PANIC checkpoint
  failures in __wt_block_checkpoint_resolve


## 7.0.45 Changelog

### Sharding

SERVER-131805 Recovered cross-database renameCollection
participant can drop the target after stepdown

### Replication

SERVER-119766 Fix data race in oplogFetcherHighestFetchedOptime
metric

### Storage

#### WiredTiger

- WT-10884 restored_updp is not NULL in __wt_txn_read_
  upd_list_internal during RTS
- WT-12917 Potential memory corruption in
  __rts_btree_abort_ondisk_kv

### Build and Packaging

- SERVER-133234 Retry URL lookup in debugsymb_mapper when
  artifacts are not yet visible
- SERVER-133242 Retry Packages artifact lookup in package_test
  against Evergreen secondary lag (BF-45409)
- SERVER-133399 Ignore hermetic-container generated paths
- SERVER-134580 Presign custom build delivery URLs for 7 days
- SERVER-134698 Deliver custom builds to version-addressed
  paths with a manifest

### Internals

- SERVER-98185 upgrade "nongnu" libunwind to v1.8.1
- SERVER-104343 unsupportedSyncSource server parameter can
  cause invariant
- SERVER-107966 A SingleServerPingMonitor within the RSM can
  get disabled and never reenabled
- SERVER-124981 Do not log isEligibleSyncSource logs on
  arbiters
- SERVER-125978 Initializing FCV fails if any collections in
  the admin database have incomplete foreground index builds
- SERVER-127486 Harden geo code against GeoColl inputs with
  strict-winding polygons
- SERVER-128392 Duplicate insert into a clustered collection
  whose _id contains a Decimal128 throws a KeyString format error
- SERVER-132246 minWaitForStreamingHelloMillis default breaks
  spec-compliant drivers
- SERVER-132933 [v7.0] Wait for secondary to reach SECONDARY
  after restart in index_build_blocking_commit_duration_metrics.js
- SERVER-133047 Introduce step to bump MONGO_VERSION file after
  each server release
- SERVER-133911 Create and include Jira ticket in pull request
  title for MONGO_VERSION bump PRs
- SERVER-134759 Debian 11 package repo EOL blocking v7.0
  release builds
- WT-10897 Make WT::compact command more test friendly in the
  MDB layer
- WT-10928 Compact prints "skipping compaction" even when the
  compaction was not skipped


## 7.0.43 Changelog

### Internals

SERVER-134063 Shred collection validator constants during
parsing


## 7.0.41 Changelog

### Replication

- SERVER-111885 Index Build Merging Spills conflicts with
  replSetGetStatus
- SERVER-122177 Ensure
  _createHorizonTopologyChangePromiseMapping() uses the correct index in
  cases of reconfig to remove a node

### Storage

#### WiredTiger

- WT-14034 Fix resolving the prepared key multiple times
  because of reserved updates
- WT-14267 test/format assert detects evicting an accessible
  internal page with an active split generation
- WT-15088 Commit may be rolled back after we have logged the
  transaction
- WT-15830 Add stats to track how many saved update list and
  total number of updates processed in __wti_rec_hs_insert_updates

### Operations

SERVER-112636 Remove superfluous FTDC logging

### Build and Packaging

SERVER-132775 Turn off remote execution and scons caching for
7.0 release variants on patches

### Internals

- SERVER-97615 Provide visibility into which ServerStatus
  section threw in FTDC thread
- SERVER-104464 Handle missing index idents during replica set
  startup recovery after unclean shutdown
- SERVER-106302 Provide visibility if aggregate FTDC object is
  too large
- SERVER-106644 Unnecessary error log message in the FTDC
  ServerStatus collector
- SERVER-111349 Rewrite RateLimitIsValidAfterQueueing unit test
- SERVER-111573 Add configuration to collstats to return full
  wiredtiger data source metrics
- SERVER-116263 _participants can be accessed concurrently in
  TransactionCoordinator
- SERVER-118419 Write ops with different dbVersions for a given
  db should not be batched together
- SERVER-118615 Use generated macos certificates in system CA
  tests
- SERVER-120949 Remove Tag Based FCV Generation
- SERVER-126298 Backport RHEL 10 to 8.3, 8.0, and 7.0
- SERVER-127346 Make session refresh have kExempt admission
  priority
- SERVER-127414 Track absolute napTime in DeferredToken
- SERVER-127946 Renew all test certs for 7.x, 8.x, 9.x
- SERVER-127985 Reject regex matches that do not lay on UTF-8
  character boundaries
- SERVER-128253 Integer overflow in query planner
  explodeForSort() can trigger mongod denial of service
- SERVER-130571 Limit use of $_internalIndexKey to internal
  clients only
- SERVER-130759 Adjust invariant condition to account for
  arbiter nodes
- SERVER-130785 Fix LDAP roles for pooled LDAP connections
- SERVER-130901 Limit JSON Pointer path depth to 255 for
  $jsonSchema.encryptMetadata.keyId
- SERVER-130926 Usage of strtoll in
  generateJSONSchemaArraySingleSchemaError can throw std::exception
- SERVER-131073 Query stats key for $searchMeta on mongos fails
  re-parse on $searchMeta.limit
- SERVER-131202 Fix aggregation pipeline updateLookup with
  dollar-prefixed fields
- SERVER-131229 enforce case-sensitivity in options validation
- SERVER-131326 Repeat stmtIds on writes crash the server
- SERVER-131378 Remove references to ubi8 distro from project
  settings to unblock Evergreen deletion
- SERVER-131420 Reject WiredTiger configString type overrides
  other than "type=file"
- SERVER-131423 Apply consistent redaction in reportState()
- SERVER-131562 Heap memory disclosure via mis-indexed
  tie-break vectors in the query multi-planner
- SERVER-131827 v7.0 does not tolerate v3 time-series buckets
  in collection validation
- SERVER-131860 Improve wiredtiger config string handling
- SERVER-131870 Fix heap use-after-free
- SERVER-132275 [v8.0] Reject $lookup with multiple pipeline
  arguments
- SERVER-132650 Make mongos use the configurable minimum
  timeout for pre-auth streamable hello


## 7.0.40 Changelog

### Storage

#### WiredTiger

- WT-16515 Fix statistics for clean pages seen and queued by
  eviction

### Internals

- SERVER-117854 GranularityRounderPowersOfTwo should assert for
  inf numbers
- SERVER-129680 Fix Coverity build failure:
  libmessage_filter_hooks.so built with empty source list causes objcopy
  failure
- SERVER-129794 make evergreen bazel builds (not test) retry in
  all cases
- SERVER-129843 Rewrite OCSP server to be compatible with
  pyOpenSSL==19.0.0
- SERVER-129923 bucket_exceed_uncompressed_mem_limit.js builds
  a >200MB uncompressed bucket that the shell now rejects before insert
- SERVER-130084 Add support for "just log" semantics from
  message filter hooks


## 7.0.39 Changelog

### Sharding

SERVER-116284 Ensure MultiStatementTransactionRequestsSender
sends commitTransaction to all shards before processing results

### Replication

SERVER-106165 Majority secondaries lagging for 30s post a
failover breaching read/write SLA

### Storage

#### WiredTiger

- WT-14648 Fix log subsystem returning EBUSY from conn->close()
- WT-15739 Fix reconciliation leaking overflow pages

### Build and Packaging

SERVER-111406 Change Stream breaks on document with top-level
$v

### Internals

- SERVER-79172 KMIP Server problems with python upgrade
- SERVER-94001 Continue with logical session cache refresh
  process even if refresh fails
- SERVER-99692 Add MSI installation sanity check testing
- SERVER-100441 mongos findAndModify implementation tries to
  abort a non-existent txn
- SERVER-102082 Make
  multi_collection_transaction_placement_conflict_workaround.js
  insensitive to data races caused by dangling transactions
- SERVER-106903 Make QueryAnalysisCoordinator::onSamplerDelete
  less error prone
- SERVER-108626 Coverity analysis defect 156320: Uninitialized
  scalar field
- SERVER-109609 allDurableTimestamp is kTimestampOne after
  initial sync and did not advance while/before transitioning to primary
- SERVER-112342 ServerStatus should have a parameter to exclude
  all fields
- SERVER-113865 (Replication) Audit all non-runtime settable
  server parameters
- SERVER-115250 Pause JWKSetRefreshJob during quiesce time
- SERVER-115307 Always log optime when replication fails to
  apply an operation
- SERVER-115585 Handle FTDC BSON exceeding standard size
- SERVER-116272 Schema Validation: New Collections
- SERVER-118514 DelayableTimeoutCallback ignores earlier
  timeout values
- SERVER-122627 Fix signed/unsigned comparison in
  bsoncolumn_util.cpp
- SERVER-126140 Remove Copybara tasks from non-master branches.
- SERVER-126162 Upgrade MozJS to ESR 140.11.0
- SERVER-126781 [v7.0] Upgrade passlib package in v7.0
- SERVER-126803 Use internal client+writeConcern in
  exchange_keyrange_maxkey.js
- SERVER-126816 [v7.0] Add no_selinux tag to
  command_let_variables.js
- SERVER-127032 Fix AttributeError crash in IDL compatibility
  checker when comparing unstable fields with mismatched array types
- SERVER-127419 Initial message filter plugin loader
- SERVER-127726 Fix bit_test_disabled_in_sbe.js in the v7.0
  branch
- SERVER-129129 Remove GRPC variants from 7.0
- SERVER-129278 fix 7.0 msi signing permissions
- WT-12657 Add checkpoint cleanup utility thread


## 7.0.37 Changelog

### Security

SERVER-128125 Align bsonObjToArray ownership semantics with
bsonGetImmutable


## 7.0.36 Changelog

### Internals

- SERVER-127984 Speed up isMetadataFieldName with compile-time
  field matching
- WT-12657 Add checkpoint cleanup utility thread


## 7.0.35 Changelog

### Security

SERVER-123370 LDAP query password is logged when set through
setParameter

### Replication

- SERVER-103123 Update term on startup based on replica set
  config's term
- SERVER-115594 Skip acquiring tickets when deleting txn
  coordinator doc

### Query

SERVER-86326 Increase max regex pattern length to 32k

### Catalog

- SERVER-107819 Concurrent createIndex+collMod can leave behind
  inconsistent collection options
- SERVER-118466 Prevent the TTL Monitor from spawning an
  unbounded amount of threads for sharding metadata recovery

### Storage

#### WiredTiger

- WT-15222 Failed to remove the updates from the history store
  with mixed mode delete on the insert list
- WT-15455 Don't skip prepared update pages during cursor walk

### Build and Packaging

WT-12353 Switch Windows Evergreen builder to Server 2022

### Internals

- SERVER-89711 proxy_protocol.js should handle errors when
  running proxyprotocol.server
- SERVER-90885 Better error handling for BackupFileCloner
- SERVER-95570 BatchedDeleteStage can sometimes find the record
  it is deleting twice
- SERVER-95583 SSLManagerWindows won't allow multiple CRLs from
  different issuers
- SERVER-102018 Audit invariants in Repl code base to add more
  information
- SERVER-103404 QueryAnalysisCoordinator Invariant Can Be
  Triggered When System Is Very Slow
- SERVER-111007 Validation should distinguish between root
  causes when finding mixed schema data
- SERVER-111603 Aggregation fuzzer tasks run out of memory
  while generating jstests
- SERVER-112792 Report existance of compound wildcard indexes
  prefixed by the shard key
- SERVER-112849 Fix uassert message in
  change_stream_ensure_resume_token_present_stage.cpp
- SERVER-113550 Fix ticket exhaustion issue in FLE2 aggregation
  and explain
- SERVER-113711 Rate Limit Log ID 4625501 (unable to establish
  remote cursors)
- SERVER-113923 Change index bounds builder check for multkey
  paths with $expr comparison from tassert to uassert
- SERVER-114045
  prepared_transaction_kill_during_step_up_refresh.js should wait for
  commit point to advance on new primary before committing transaction
- SERVER-114295 api_version_prepare_txn.js should wait for
  lastCommitted to advance on stepped up secondary
- SERVER-114806 Wildcard indexes may consume all memory allowed
  for the index build
- SERVER-115326 Don't reset logical session cache reaper
  metrics on beginning reap
- SERVER-115576 Resmoke should not rely on the mongo shell from
  an old version
- SERVER-115584 Handle unexpectedly large /proc/mountinfo files
- SERVER-117252 Remove 6.0 multiversion testing from all higher
  branches
- SERVER-117267 Run a checkpoint and retry when dropIdent fails
  in startup recovery due to dirty data
- SERVER-117433 Add private third party dependency directory
- SERVER-117755 Backport updated gitignore
- SERVER-119546 Remove oldcrypt from 8.0
- SERVER-119689 Pin docker-systemctl-replacement to a specific
  commit
- SERVER-120450 Upgrade MozJS to ESR 140.9
- SERVER-120668 Disallow $trim with too large mask string
- SERVER-121016 get monguard resmoke changes working on v7.0
- SERVER-121132 [v7.0] Temporary compressed bucket
  inconsistency during logical initial sync causing crash
- SERVER-122483 [MozJS] std::to_chars compile failure on macOS
  < 10.15
- SERVER-122791 Python typehint incompatibility in resmoke
  blocks MacOS builds on 7.0 branch
- SERVER-122807 7.0 python pip version fails to retry in some
  cases
- SERVER-123083 switch windows to python310 on 7.0
- SERVER-123107 Pin Windows SDK across master + all release
  branches
- SERVER-123440 GeometryCollection with strict-winding polygon
  causes 2dsphere index key generation crash
- SERVER-123507 Encrypted predicates inside a $vectorSearch
  prefilter should get replaced with encryption placeholders
- SERVER-123553 Change index key generation log line error to
  LOGV2_WARNING
- SERVER-123633 Fix handling of user $-prefixed fields
  colliding with internal metadata
- SERVER-123918 Validate runtimeConstants.userRoles in IDL
- SERVER-123951 $_internalConvertBucketIndexStats should not
  return PauseExecution on failed index conversion
- SERVER-124031 Ensure Exchange::getTargetConsumer correctly
  handles MaxKey
- SERVER-124190 Forbid aggregate "exchange" field from
  non-internal clients
- SERVER-124268 [TEST ONLY] [v7.0 ONLY] collMod interleave
  might cause a false positive in fsm test
- SERVER-124285 Improve SBOM generation automation and change
  sbom_linter owner
- SERVER-124308 Fix LDAPDNSResolverCache not updating cache
  correctly
- SERVER-124959 Validate doc diff array bounds and
  $_internalApplyOplogUpdate BSON
- SERVER-125063 Prohibit nesting of BSONColumn inside
  BSONColumn
- SERVER-125492 Reduce frequency of OpenSSL primary DRBG reseed
  attempts
- SERVER-125667 Fix windows aws creds on 7.0
- SERVER-125736 Backport .gitignore for
  resmoke_suites_derived.bzl
- SERVER-126049 MozJS per-scope heap limit check uses
  process-global GC counter


## 7.0.34 Changelog

### Internals

- SERVER-120668 Disallow $trim with too large mask string
- SERVER-121895 Improve redaction of validation errors
- SERVER-122032 Calling replaceEncryptedFieldsInFilter with
  positional projection results in use-after-free
- SERVER-122449 Improve $bitSet match expressions
- SERVER-124268 [TEST ONLY] [v7.0 ONLY] collMod interleave
  might cause a false positive in fsm test
- SERVER-126021 Undefined behavior when inserting data with
  duplicate field names into timeseries collections


## 7.0.32 Changelog

### Security

SERVER-119679 Missing Authorization Check in updateUser

### Replication

SERVER-79298 FCBIS should succeed in unhealthy set

### Query

- SERVER-110916 Use-after-move in
  targetShardsAndAddMergeCursors()
- SERVER-118546 Can not create timeseries 2dsphere index with a
  non-system user

### Internals

- SERVER-105047 Query using $or and $ne on sharded collection
  can include orphan documents
- SERVER-105416 Configs should be rejected if they make it
  impossible to elect a Primary
- SERVER-105662 Server: Reduce the need to request from git
  http endpoint for multiversion gen
- SERVER-105942 Add logging to ReplicaSetAwareService stepDown
  hook
- SERVER-107482 Handle top level StaleConfig errors in
  batch_write_op
- SERVER-108040 Update markFailed to check current step
- SERVER-108581 Find query remaining time is calculated
  incorrectly in mongos
- SERVER-108945 Handle $elemMatch with empty path under a
  contained $or correctly
- SERVER-109033 Coverity analysis defect 152012: Double lock
- SERVER-109200 Upgrade MozJS to ESR 140.3
- SERVER-109213 Increase logging when index bounds are deemed
  invalid
- SERVER-110118 Coverity analysis defect 176650: Using a moved
  object
- SERVER-110345 config.rangeDeletions docs for uncompleted
  range deletion tasks could get deleted due to non-exact delete filter
- SERVER-110423 $group can use a distinct scan on a sparse
  index, which hides null/missing results
- SERVER-111486 $group can still use a distinct scan on a
  sparse index if an alternative index is available
- SERVER-112955 Create alias for emergency releases
- SERVER-114165 Run Coverity scans only on staging version of
  release branches
- SERVER-114698 Fix ubsan error in
  VerifyMaxOpenSessionsBasedOnRlimit in v7.0
- SERVER-114731 Fix updatea.js and json_schema.js multiversion
  test on v7.0
- SERVER-116129 Internal transactions should never specify
  empty read concern
- SERVER-116130 forceSyncSource helper hangs on shardsvr due to
  implicit majority write concern
- SERVER-116327 Validate usage of invalid index types at
  creation time
- SERVER-117317 Upgrade MozJS to ESR 140.7
- SERVER-119413 configTerm is expected as an int32 but can be
  an int64
- SERVER-119546 Remove oldcrypt from 8.0
- SERVER-119961 MacOS 7.0 waterfall builds failing due to
  Python module installation issues
- SERVER-119981 Fix binDataClean() for deprecated type
- SERVER-120182 [v8.0] Properly lower ReplSetTest timeout in
  x509_extended_key_usage.js
- SERVER-122483 [MozJS] std::to_chars compile failure on macOS
  < 10.15
- WT-16698 Measure time taken by checkpoint cleanup
