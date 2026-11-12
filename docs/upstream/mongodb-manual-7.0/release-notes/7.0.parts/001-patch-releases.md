<!-- Part 1 of 3 of release-notes/7.0.md (split because the page is big). -->

## Patch Releases

### 7.0.48 - Upcoming

Issues fixed:

- SERVER-98105 Pause drop pending ident reaper until backup cursor
  is closed
- SERVER-108215 Impose limits on the number of active
  multi-document transactions
- SERVER-132098 Upgrade timelib and timezone data files to 2026e
- [All JIRA issues closed in 7.0.48](https://jira.mongodb.org/issues/?jql=project%20in%20(SERVER%2CTOOLS%2CWT)%20AND%20resolution%3D%27Fixed%27%20and%20fixversion%3D%277.0.48%27)
- 7.0.48-changelog

### 7.0.45 - Oct 13, 2026

This release contains important security and reliability improvements.

**Important:**

MongoDB 7.0.45 contains fixes for:

- [CVE-2026-96297](https://www.cve.org/CVERecord?id=CVE-2026-96297)
- [CVE-2026-103965](https://www.cve.org/CVERecord?id=CVE-2026-103965)

For the latest information about MongoDB security updates, see
MongoDB Security Bulletins.

Issues fixed:

- SERVER-104343 unsupportedSyncSource server parameter can
  cause invariant
- SERVER-107966 A SingleServerPingMonitor within the RSM can
  get disabled and never reenabled
- SERVER-119766 Fix data race in
  oplogFetcherHighestFetchedOptime metric
- SERVER-128392 Duplicate insert into a clustered collection
  whose _id contains a Decimal128 throws a KeyString format error
- SERVER-131805 Recovered cross-database renameCollection
  participant can drop the target after stepdown
- SERVER-132246 minWaitForStreamingHelloMillis default breaks
  spec-compliant drivers
- SERVER-132946 Heap-use-after-free in $_internalApplyOplogUpdate stage
  when reading via getMore after aggregate Invocation is destroyed
- SERVER-134618 Fix serialization of constant values in $bucket stage
- [All JIRA issues closed in 7.0.45](https://jira.mongodb.org/issues/?jql=project%20in%20(SERVER%2CTOOLS%2CWT)%20AND%20resolution%3D%27Fixed%27%20and%20fixversion%3D%277.0.45%27)
- 7.0.45-changelog

### 7.0.43 - Sept 11, 2026

This release contains important security and reliability improvements.

**Important:**

MongoDB 7.0.43 contains a fix for:

- [CVE-2026-89099](https://www.cve.org/CVERecord?id=CVE-2026-89099)

For the latest information about MongoDB security updates, see
MongoDB Security Bulletins.

   
Issues fixed:

- SERVER-134063 Shred collection validator constants during parsing
- [All JIRA issues closed in 7.0.43](https://jira.mongodb.org/issues/?jql=project%20in%20(SERVER%2CTOOLS%2CWT)%20AND%20resolution%3D%27Fixed%27%20and%20fixversion%3D%277.0.43%27)

### 7.0.41 - Sept 8, 2026

This release contains important security and reliability improvements.

**Important:**

MongoDB 7.0.41 contains fixes for:

- [CVE-2026-82054](https://www.cve.org/CVERecord?id=CVE-2026-82054)
- [CVE-2026-82053](https://www.cve.org/CVERecord?id=CVE-2026-82053)
- [CVE-2026-82076](https://www.cve.org/CVERecord?id=CVE-2026-82076)
- [CVE-2026-82075](https://www.cve.org/CVERecord?id=CVE-2026-82075)
- [CVE-2026-82074](https://www.cve.org/CVERecord?id=CVE-2026-82074)
- [CVE-2026-82071](https://www.cve.org/CVERecord?id=CVE-2026-82071)
- [CVE-2026-82070](https://www.cve.org/CVERecord?id=CVE-2026-82070)
- [CVE-2026-82068](https://www.cve.org/CVERecord?id=CVE-2026-82068)
- [CVE-2026-82067](https://www.cve.org/CVERecord?id=CVE-2026-82067)
- [CVE-2026-82066](https://www.cve.org/CVERecord?id=CVE-2026-82066)
- [CVE-2026-82065](https://www.cve.org/CVERecord?id=CVE-2026-82065)
- [CVE-2026-82064](https://www.cve.org/CVERecord?id=CVE-2026-82064)
- [CVE-2026-82063](https://www.cve.org/CVERecord?id=CVE-2026-82063)
- [CVE-2026-82060](https://www.cve.org/CVERecord?id=CVE-2026-82060)
- [CVE-2026-82052](https://www.cve.org/CVERecord?id=CVE-2026-82052)
- [CVE-2026-82059](https://www.cve.org/CVERecord?id=CVE-2026-82059)
- [CVE-2026-82058](https://www.cve.org/CVERecord?id=CVE-2026-82058)

For the latest information about MongoDB security updates, see
MongoDB Security Bulletins.

Issues fixed:

- SERVER-104464 Handle missing index idents during replica set
  startup recovery after unclean shutdown
- SERVER-111573 Add configuration to collstats to return full
  wiredtiger data source metrics
- SERVER-111885 Index Build Merging Spills conflicts with
  replSetGetStatus
- SERVER-127346 Make session refresh have kExempt admission
  priority
- SERVER-130571 Limit use of $_internalIndexKey to internal
  clients only
- SERVER-130926 Usage of strtoll in
  generateJSONSchemaArraySingleSchemaError can throw std::exception
- SERVER-130901 Limit JSON Pointer path depth to 255 for $jsonSchema.encryptMetadata.keyId
- SERVER-130785 Fix LDAP roles for pooled LDAP connections
- SERVER-128253 Integer overflow in query planner explodeForSort() can trigger mongod denial of service
- SERVER-132650 Make `mongos` use the configurable minimum timeout for pre-auth streamable hello
- SERVER-132275 [v8.0] Reject $lookup with multiple pipeline arguments
- SERVER-131860 Improve wiredtiger config string handling
- SERVER-131423 Apply consistent redaction in reportState()
- SERVER-131326 Repeat stmtIds on writes crash the server
- SERVER-131229 enforce case-sensitivity in options validation
- SERVER-131562 Heap memory disclosure via mis-indexed tie-break vectors in the query multi-planner
- SERVER-131420 Reject WiredTiger configString type overrides other than "type=file"
- SERVER-130759 Adjust invariant condition to account for arbiter nodes
- SERVER-131870 Fix heap use-after-free
- SERVER-131202 Fix aggregation pipeline updateLookup with dollar-prefixed fields
- SERVER-127985 Reject regex matches that do not lay on UTF-8 character boundaries

- [All JIRA issues closed in 7.0.41](https://jira.mongodb.org/issues/?jql=project%20in%20(SERVER%2CTOOLS%2CWT)%20AND%20resolution%3D%27Fixed%27%20and%20fixversion%3D%277.0.41%27)

- 7.0.41-changelog

### 7.0.40 - Aug 11, 2026

This release contains important security and reliability improvements.

**Important:**

MongoDB 7.0.40 contains fixes for:

- [CVE-2026-18688](https://www.cve.org/CVERecord?id=CVE-2026-18688)
- [CVE-2026-18690](https://www.cve.org/CVERecord?id=CVE-2026-18690)
- [CVE-2026-18691](https://www.cve.org/CVERecord?id=CVE-2026-18691)
- [CVE-2026-18693](https://www.cve.org/CVERecord?id=CVE-2026-18693)
- [CVE-2026-18694](https://www.cve.org/CVERecord?id=CVE-2026-18694)
- [CVE-2026-18695](https://www.cve.org/CVERecord?id=CVE-2026-18695)
- [CVE-2026-18696](https://www.cve.org/CVERecord?id=CVE-2026-18696)
- [CVE-2026-18697](https://www.cve.org/CVERecord?id=CVE-2026-18697)
- [CVE-2026-18698](https://www.cve.org/CVERecord?id=CVE-2026-18698)
- [CVE-2026-18699](https://www.cve.org/CVERecord?id=CVE-2026-18699)
- [CVE-2026-18700](https://www.cve.org/CVERecord?id=CVE-2026-18700)
- [CVE-2026-18701](https://www.cve.org/CVERecord?id=CVE-2026-18701)
- [CVE-2026-18702](https://www.cve.org/CVERecord?id=CVE-2026-18702)
- [CVE-2026-18705](https://www.cve.org/CVERecord?id=CVE-2026-18705)
- [CVE-2026-18708](https://www.cve.org/CVERecord?id=CVE-2026-18708)
- [CVE-2026-18709](https://www.cve.org/CVERecord?id=CVE-2026-18709)
- [CVE-2026-18712](https://www.cve.org/CVERecord?id=CVE-2026-18712)

For the latest information about MongoDB security updates, see
MongoDB Security Bulletins.

Issues fixed:

- SERVER-117854 GranularityRounderPowersOfTwo should assert for
  inf numbers
- SERVER-129460 Ensure valid `jsonSchema` in time series
  updates
- SERVER-129617 Better validation for `NaN` in
  `$percentile` and `$median`
- SERVER-129618 Disallow user-provided `$vectorSearch`
  arguments from overriding internally generated options
- SERVER-129994 Fix a malformed `FlatBSON` store caused by
  inserting duplicate field names
- SERVER-130110 Gate the internal-only
  `_internalSetObjToThis` field of `$function` behind an
  internal-client check
- SERVER-130111 Prevent invalid type conversion during match
  expression serialization
- SERVER-130117 Fix a heap use-after-free in collection
  validation for big polygons
- SERVER-130139 Account for the `o`-versus-UUID consistency
  check
- SERVER-130167 Stop the JavaScript scope from constructing
  delete requests by concatenating unsanitized `_id` fields
- SERVER-130188 Exclude partial indexes from `2dsphere`
  geometry skip-validation
- SERVER-130198 Increase the authorization requirement for
  `slowms` and `sampleRate` in the `profile` command
- SERVER-130264 Apply the intra-cluster SASL mechanism
  allowlist in egress connection setup
- SERVER-130266 Prohibit `$text` and `$near` in
  `$_internalSchemaCond`
- SERVER-130481 Allow the symbol type in
  `CommandHelpers::parseNsFromCommand`
- SERVER-130544 Enforce the internal user for
  `commitTransaction` and `abortTransaction` on prepared
  transactions
- SERVER-130633 Authorize `compactStructuredEncryptionData`
  and `cleanupStructuredEncryptionData` at database scope

- [All JIRA issues closed in 7.0.40](https://jira.mongodb.org/issues/?jql=project%20in%20(SERVER%2CTOOLS%2CWT)%20AND%20resolution%3D%27Fixed%27%20and%20fixversion%3D%277.0.40%27)

- 7.0.40-changelog

### 7.0.39 - July 22, 2026

This release contains important security and reliability improvements.

**Important:**

MongoDB 7.0.39 contains fixes for:

- [CVE-2026-9737](https://www.cve.org/CVERecord?id=CVE-2026-9737)
- [CVE-2026-13055](https://www.cve.org/CVERecord?id=CVE-2026-13055)
- [CVE-2026-13059](https://www.cve.org/CVERecord?id=CVE-2026-13059)
- [CVE-2026-13060](https://www.cve.org/CVERecord?id=CVE-2026-13060)
- [CVE-2026-13061](https://www.cve.org/CVERecord?id=CVE-2026-13061)
- [CVE-2026-13062](https://www.cve.org/CVERecord?id=CVE-2026-13062)
- [CVE-2026-13065](https://www.cve.org/CVERecord?id=CVE-2026-13065)
- [CVE-2026-13066](https://www.cve.org/CVERecord?id=CVE-2026-13066)
- [CVE-2026-13068](https://www.cve.org/CVERecord?id=CVE-2026-13068)
- [CVE-2026-13069](https://www.cve.org/CVERecord?id=CVE-2026-13069)
- [CVE-2026-13070](https://www.cve.org/CVERecord?id=CVE-2026-13070)
- [CVE-2026-13071](https://www.cve.org/CVERecord?id=CVE-2026-13071)
- [CVE-2026-13072](https://www.cve.org/CVERecord?id=CVE-2026-13072)
- [CVE-2026-13074](https://www.cve.org/CVERecord?id=CVE-2026-13074)
- [CVE-2026-13077](https://www.cve.org/CVERecord?id=CVE-2026-13077)
- [CVE-2026-13078](https://www.cve.org/CVERecord?id=CVE-2026-13078)

For the latest information about MongoDB security updates, see
MongoDB Security Bulletins.

Issues fixed:

- SERVER-123081 Handle compound wildcard index spec in
  `$_internalIndexKey`
- SERVER-127280 Reject expression-based `sortBy` in the
  `$linearFill` parser
- SERVER-127357 Check for duplicate `from` fields in
  `DocumentSourceGraphLookup::createFromBson()`
- SERVER-127566 Limit the contention factor that can be used
  for FLE2 fields
- SERVER-127689 Only allow internal clients to specify
  `$_internalPredicate`
- SERVER-127694 Add type checking for `DBPointer`
- SERVER-127831 Forbid external users from running FLE2
  commands with `crudProcessed` set to true
- SERVER-128198 Fix `mongos` `killCursors` to check
  authorization against the cursor's namespace instead of the request
  namespace
- SERVER-128341 Fix a server crash caused by sorting on a
  `$meta` expression
- SERVER-129103 Restrict target BinData subtypes in $convert and $constant/$literal
- SERVER-128362 Add a null check on the return value in
  `ocspClientCallback`
- SERVER-128433 Prevent external clients from setting
  `runtimeConstants.userRoles`
- SERVER-128473 Fix a use-after-free in `$function` caused by
  a missing `advanceGeneration()` call on retained BSON arguments
- SERVER-128494 Validate external BSON in
  `MultiBsonStreamCursor`
- SERVER-128517 Add a configurable minimum timeout for pre-auth
  streamable `hello` to prevent a hot loop from very small
  `maxAwaitTimeMS` values
- SERVER-128832 Guard `ImplScope` `ModuleLoader` creation
- SERVER-94001 Continue with logical session cache refresh
  process even if refresh fails
- SERVER-106165 Majority secondaries lagging for 30s post a
  failover breaching read/write SLA
- SERVER-116284 Ensure MultiStatementTransactionRequestsSender
  sends commitTransaction to all shards before processing results
- WT-12657 Add checkpoint cleanup utility thread
- [All JIRA issues closed in 7.0.39](https://jira.mongodb.org/issues/?jql=project%20in%20(SERVER%2CTOOLS%2CWT)%20AND%20resolution%3D%27Fixed%27%20and%20fixversion%3D%277.0.39%27)

- 7.0.39-changelog

### 7.0.37 - June 11, 2026

**Important:**

MongoDB 7.0.37 contains a fix for
[CVE-2026-11933](https://www.cve.org/CVERecord?id=CVE-2026-11933)

For the latest information about MongoDB security updates, see
MongoDB Security Bulletins.

Issues fixed:

- SERVER-128125 Align bsonObjToArray ownership semantics
  with bsonGetImmutable
- [All JIRA issues closed in 7.0.37](https://jira.mongodb.org/issues/?jql=project%20in%20(SERVER%2CTOOLS%2CWT)%20AND%20resolution%3D%27Fixed%27%20and%20fixversion%3D%277.0.37%27)

- 7.0.37-changelog

### 7.0.36 - June 10, 2026

Issues fixed:

- SERVER-127984 Speed up isMetadataFieldName with compile-time field 
  matching
- 7.0.36-changelog

### 7.0.35 - June 9, 2026

**Important:**

MongoDB 7.0.35 contains a fix for:

- [CVE-2026-9740](https://www.cve.org/CVERecord?id=CVE-2026-9740)
- [CVE-2026-9741](https://www.cve.org/CVERecord?id=CVE-2026-9741)
- [CVE-2026-9746](https://www.cve.org/CVERecord?id=CVE-2026-9746)
- [CVE-2026-9747](https://www.cve.org/CVERecord?id=CVE-2026-9747)
- [CVE-2026-9748](https://www.cve.org/CVERecord?id=CVE-2026-9748)
- [CVE-2026-9749](https://www.cve.org/CVERecord?id=CVE-2026-9749)
- [CVE-2026-9750](https://www.cve.org/CVERecord?id=CVE-2026-9750)
- [CVE-2026-9751](https://www.cve.org/CVERecord?id=CVE-2026-9751)
- [CVE-2026-9752](https://www.cve.org/CVERecord?id=CVE-2026-9752)
- [CVE-2026-9753](https://www.cve.org/CVERecord?id=CVE-2026-9753)

For the latest information about MongoDB security updates, see
MongoDB Security Bulletins.

Issues fixed:

- SERVER-86326 Increase max regex pattern length to 32k
- SERVER-111007 Validation should distinguish between root
  causes when finding mixed schema data
- SERVER-121132 Temporary compressed bucket inconsistency
  during logical initial sync causing crash
- SERVER-112792 Report existence of compound wildcard indexes
  prefixed by the shard key
- SERVER-126049 MozJS per-scope heap limit check uses
  process-global GC counter
- SERVER-125063 Prohibit nesting of BSONColumn inside BSONColumn
- SERVER-123507 Encrypted predicates inside a `$vectorSearch` 
  prefilter should get replaced with encryption placeholders 
- SERVER-124190 Forbid aggregate `exchange` field from non-internal 
  clients
- SERVER-123918 Validate `runtimeConstants.userRoles` in IDL
- SERVER-123951 `$_internalConvertBucketIndexStats` should not return
  PauseExecution on failed index conversion
- SERVER-124031 Ensure `Exchange::getTargetConsumer` correctly handles 
  MaxKey
- SERVER-123633 Fix handling of user $-prefixed fields colliding with 
  internal metadata
- SERVER-123370 LDAP query password is logged when set through 
  setParameter
- SERVER-123440 GeometryCollection with strict-winding polygon causes 
  2dsphere index key generation crash
- SERVER-124959 Validate doc diff array bounds and 
  `$_internalApplyOplogUpdate` BSON
- [All JIRA issues closed in 7.0.35](https://jira.mongodb.org/issues/?jql=project%20in%20(SERVER%2CTOOLS%2CWT)%20AND%20resolution%3D%27Fixed%27%20and%20fixversion%3D%277.0.35%27)
- 7.0.35-changelog

### 7.0.34 - May 12, 2026

**Important:**

MongoDB 7.0.34 contains a fix for:

- [CVE-2026-8053](https://www.cve.org/CVERecord?id=CVE-2026-8053)
- [CVE-2026-8199](https://www.cve.org/CVERecord?id=CVE-2026-8199)
- [CVE-2026-8200](https://www.cve.org/CVERecord?id=CVE-2026-8200)
- [CVE-2026-8201](https://www.cve.org/CVERecord?id=CVE-2026-8201)
- [CVE-2026-8202](https://www.cve.org/CVERecord?id=CVE-2026-8202)

For the latest information about MongoDB security updates, see
MongoDB Security Bulletins.

Issues fixed:

- SERVER-120668 Disallow `$trim` with too large mask string
- SERVER-121895 Improve redaction of validation errors
- SERVER-122032 Calling `replaceEncryptedFieldsInFilter` with positional projection results in use-after-free
- SERVER-122449 Improve `$bitSet` match expressions
- SERVER-126021 Undefined behavior when inserting data with duplicate field names into timeseries collections
- [All JIRA issues closed in 7.0.34](https://jira.mongodb.org/issues/?jql=project%20in%20(SERVER%2CTOOLS%2CWT)%20AND%20resolution%3D%27Fixed%27%20and%20fixversion%3D%277.0.34%27)
- 7.0.34-changelog

### 7.0.32 - Apr 29, 2026

**Important:**

MongoDB 7.0.32 contains a fix for:

- [CVE-2026-6914](https://www.cve.org/CVERecord?id=CVE-2026-6914)
- [CVE-2026-6915](https://www.cve.org/CVERecord?id=CVE-2026-6915)

For the latest information about MongoDB security updates, see
MongoDB Security Bulletins.

Issues fixed:

- SERVER-119679: Missing Authorization Check in updateUser
- SERVER-119981: Fix binDataClean() for deprecated type
- SERVER-105047: Query using $or and $ne on sharded collection can include orphan documents
- SERVER-110345: config.rangeDeletions docs for uncompleted range deletion tasks could get deleted due to non-exact delete filter
- SERVER-110423: $group can use a distinct scan on a sparse index, which hides null/missing results
- SERVER-110916: Use-after-move in targetShardsAndAddMergeCursors()
- SERVER-111486: $group can still use a distinct scan on a sparse index if an alternative index is available

- [All Jira issues closed in 7.0.32](https://jira.mongodb.org/issues/?jql=project%20in%20(SERVER%2C%20TOOLS%2C%20WT)%20AND%20resolution%20%3D%20Fixed%20AND%20fixVersion%20%3D%207.0.32)
- 7.0.32-changelog

### 7.0.31 - Mar 17, 2026

**Important:**

MongoDB 7.0.31 contains a fix for: 

- [CVE-2026-4147](https://www.cve.org/CVERecord?id=CVE-2026-4147)
- [CVE-2026-4148](https://www.cve.org/CVERecord?id=CVE-2026-4148)

For the latest information about MongoDB security updates, see
MongoDB Security Bulletins.

- SERVER-55068: Sets the `net.maxIncomingConnections`
  maximum on Linux systems to `(RLIMIT_NOFILE / 2) * 0.8`
- SERVER-82688: `mongod` crash, bug fix when connections exceed wiredtiger's `session_max`
- SERVER-95374: Compound wildcard indexes can incorrectly push down predicates during union or planning
- SERVER-103774: Disallow compound wildcard indexes from being used as a shard key index
- SERVER-110953: Check no orphaned document is present on a recipient shard before starting cloning a range
- SERVER-113319: `$match` pushdown past a renamed field is done incorrectly when the expression root is a renamed field path expression
- SERVER-115962: Balancer does not make progress when the most loaded shard is already balanced within its zones
- SERVER-118428: `mongocryptd` rejects large messages
- SERVER-119317: Improve object lifecycle of MD5 hash state
- SERVER-119319: Fix ExpressionContext use-after-free bug
- WT-14140: Unnecessary schema lock taken for active `"file:"` dhandles that are not swept
- [All Jira issues closed in 7.0.31](https://jira.mongodb.org/issues/?jql=project%20in%20(SERVER%2C%20TOOLS%2C%20WT)%20AND%20resolution%20%3D%20Fixed%20AND%20fixVersion%20%3D%207.0.31)
- 7.0.31-changelog

### 7.0.30 - Feb 10, 2026

- SERVER-118713 - Can not create timeseries 2dsphere index with a non-system user
- [All Jira issues closed in 7.0.30](https://jira.mongodb.org/issues/?jql=project%20in%20(SERVER%2C%20TOOLS%2C%20WT)%20AND%20resolution%20%3D%20Fixed%20AND%20fixVersion%20%3D%207.0.30)
- 7.0.30-changelog

### 7.0.29 - Jan 27, 2026

**Important:**

MongoDB 7.0.29 contains a fix for: 

- [CVE-2026-1847](https://www.cve.org/CVERecord?id=CVE-2026-1847)
- [CVE-2026-1848](https://www.cve.org/CVERecord?id=CVE-2026-1848)
- [CVE-2026-1849](https://www.cve.org/CVERecord?id=CVE-2026-1849)
- [CVE-2026-1850](https://www.cve.org/CVERecord?id=CVE-2026-1850)
- [CVE-2026-25609](https://www.cve.org/CVERecord?id=CVE-2026-25609)
- [CVE-2026-25610](https://www.cve.org/CVERecord?id=CVE-2026-25610)
- [CVE-2026-25611](https://www.cve.org/CVERecord?id=CVE-2026-25611)
- [CVE-2026-25612](https://www.cve.org/CVERecord?id=CVE-2026-25612)
- [CVE-2026-25613](https://www.cve.org/CVERecord?id=CVE-2026-25613)

For the latest information about MongoDB security updates, see
MongoDB Security Bulletins.

Issues fixed:

- SERVER-94315 - Shard filtering bug with collation
- SERVER-99119 - Change geo-related invariants to tasserts
- SERVER-102364 - Periodically check $reduce accumulated depth less than maxAllowableBSONDepth
- SERVER-112952 - tighten profile command auth check
- SERVER-113532 - [8.0] Introduce a new CursorResponseBsonSize limit of 16MB+32KB
- SERVER-113685 - Segfault for query on compound wildcard index
- SERVER-114695 - Update default value for pending connections
- SERVER-114838 - Lock Manager is susceptible to an adversarial DDOS attack
- SERVER-115296 - Redact ResourceId raw values from error messages
- SERVER-116206 - Better exception handling for message compressors
- SERVER-116210 - Adjust the maximum buffer size for ingress requests
- SERVER-116211 - Cap memory allocated by network buffers
- [All Jira issues closed in 7.0.29](https://jira.mongodb.org/issues/?jql=project%20in%20(SERVER%2C%20TOOLS%2C%20WT)%20AND%20resolution%20%3D%20Fixed%20AND%20fixVersion%20%3D%207.0.29)
- 7.0.29-changelog

### 7.0.28 - Dec 19, 2025

**Important:**

MongoDB 7.0.28 contains a fix for [CVE-2025-14847](https://www.cve.org/CVERecord?id=CVE-2025-14847). 

For the latest information about MongoDB security updates, see
MongoDB Security Bulletins.

Issues fixed:

- SERVER-115508: Make minimally sized buffers for uncompressed Messages
- 7.0.28-changelog

### 7.0.26 - Nov 21, 2025

**Important:**

MongoDB 7.0.26 includes fixes for [CVE-2025-12893](https://www.cve.org/CVERecord?id=CVE-2025-12893),
[CVE-2025-13507](https://www.cve.org/CVERecord?id=CVE-2025-13507),
[CVE-2025-13643](https://www.cve.org/CVERecord?id=CVE-2025-13643),
[CVE-2025-13644](https://www.cve.org/CVERecord?id=CVE-2025-13644),
and [CVE-2025-14345](https://www.cve.org/CVERecord?id=CVE-2025-14345).

For the latest information about MongoDB security updates, see
MongoDB Security Bulletins.  

Issues fixed:

- SERVER-77172: "abortExpiredTransactions" thread can get stuck
  if it fails to checkout a session
- SERVER-89039: Support a command that returns after an index
  build has started
- SERVER-92236: Chunk migrations should use short lived
  cancellation sources
- SERVER-102670: Incorrect ordered time-series insert
  error handling
- SERVER-107361: Rollover determination in the bucket catalog
  can fail to check mixed schema for large measurements
- SERVER-108565: Improve handling of oversized writes to time series 
  collections.
- SERVER-112467: Track and report the number of pending proxy
  connections
- WT-9575: Pages with updates newer to the oldest txn id are not
  queued for eviction
- SERVER-106589: Provision more memory for index builds during
  initial sync
- SERVER-102428: Logical initial sync allocates double
  `maxIndexBuildMemoryUsageMegabytes`
- SERVER-86591: Enhance InitialSync Error Handling for
  Transient Network Issues
- [All Jira issues closed in 7.0.26](https://jira.mongodb.org/issues/?jql=project%20in%20(SERVER%2C%20TOOLS%2C%20WT)%20AND%20resolution%20%3D%20Fixed%20AND%20fixVersion%20%3D%207.0.26)
- 7.0.26-changelog

### 7.0.25 - Oct 2, 2025

**Important:**

Use-after-free in the MongoDB server query planner may lead to a
crash or undefined behavior.

Description: an authorized user may crash the MongoDB server by
causing a buffer over-read. This can occur when running a DDL
operation while the queries run.

CVSS Score: 5.3

CWE: 416 Use After Free

Affected product versions: MongoDB Server 8.2.0, 8.0.14 to 8.0,
7.0.24 to 7.0, and earlier end-of-life major versions.

Issues fixed:

- SERVER-105873: QueryPlannerParams should not maintain
  pointers owned by IndexCatalogEntry
- [All Jira issues closed in 7.0.25](https://jira.mongodb.org/issues/?jql=project%20in%20(SERVER%2C%20TOOLS%2C%20WT)%20AND%20resolution%20%3D%20Fixed%20AND%20fixVersion%20%3D%207.0.25)
- 7.0.25-changelog

### 7.0.24 - Sep 10, 2025

Issues fixed:

- SERVER-103505: Handle metadata errors in
  WiredTigerUtil::setTableLogging
- SERVER-103741: Add profile collection metrics
- SERVER-104771: [v7.0] Initial sync fails when the source has
  TTL indexes on a capped collection
- WT-14391: Check eviction server is running before opening HS
- WT-14653: Add logs/stats to reconciliation for tracking HS
  updates
- [All Jira issues closed in 7.0.24](https://jira.mongodb.org/issues/?jql=project%20in%20(SERVER%2C%20TOOLS%2C%20WT)%20AND%20resolution%20%3D%20Fixed%20AND%20fixVersion%20%3D%207.0.24)
- 7.0.24-changelog

### 7.0.23 - Aug 13, 2025

Issues fixed: 

- SERVER-81797: Make our own portable implementation of atomic `notify()` and `wait()` with timeout support
- SERVER-86656: Create a reader-optimized reader-writer mutex
- SERVER-95324: Disable chunkMigrationConcurrency
- SERVER-101581: Check socket state before accepting connection in ASIO
- SERVER-103934: FCBIS should be able to call KVEngine::cleanShutdown without leaking memory
- [All Jira issues closed in 7.0.23](https://jira.mongodb.org/issues/?jql=project%20in%20(SERVER%2C%20TOOLS%2C%20WT)%20AND%20resolution%20%3D%20Fixed%20AND%20fixVersion%20%3D%207.0.23)
- 7.0.23-changelog 

### 7.0.22 - Jul 18, 2025

**Important:**

Due to CVE-2025-10061, in MongoDB 7.0 prior to 7.0.6, an authorized user can 
cause a crash in the MongoDB Server through a specially crafted $group 
query. This vulnerability is related to the incorrect handling of 
certain accumulator functions when additional parameters are specified 
within the $group operation. This vulnerability could lead to denial of 
service if triggered repeatedly. 

This issue affects the following MongoDB Server versions:

- 8.1.0 - 8.1.1
- 8.0.0 - 8.0.11
- 7.0.0 - 7.0.21
- 6.0.0 - 6.0.24

**CVSS Score**: 6.5

**CWE**: CWE-20 Improper Input Validation

**Important:** Malformed KMIP response may result in read access violation

Due to CVE-2025-12657, in MongoDB 7.0 prior to 7.0.6, the KMIP response 
parser built into `mongo` binaries is overly tolerant of 
certain malformed packets, and may parse them into invalid 
objects. Later reads of this object can result in read access 
violations.

This issue affects the following MongoDB Server versions:

- 8.0.0 - 8.0.9
- 7.0.0 - 7.0.21

**CVSS Score**: 5.9

**CWE**: CWE-754: Improper Check for Unusual or Exceptional Conditions

Issues fixed:

- SERVER-101230: Coverity analysis defect 155126: Using invalid iterator
- SERVER-95523: upsert does not handle DuplicateKey retry correctly
- SERVER-95524: Avoid retrying on duplicate key error for upserts in multidocument transactions
- SERVER-96197: ExpressionContext's _resolvedNamespaces can't distinguish between collections with the same name in different dbs
- SERVER-98386: Shard does not correctly check the ShardVersion received for timeseries collections
- SERVER-99616 $group can hit MONGO_verify
- [All Jira issues closed in 7.0.22](https://jira.mongodb.org/issues/?jql=project%20in%20(SERVER%2C%20TOOLS%2C%20WT)%20AND%20resolution%20%3D%20Fixed%20AND%20fixVersion%20%3D%207.0.22)
- 7.0.22-changelog 

### 7.0.21 - Jun 04, 2025

Issues fixed:

- SERVER-92806: Plan cache entry ignores index collation with $elemMatch
- SERVER-95672: Indexes on array fields that contain subarrays does not 
  include some results
- SERVER-97044: Fix an issue where change streams might incorrectly output 
  a "drop" event during resharding or unsharding of a collection that is or was 
  using zone sharding
- WT-12012: Restore original verbose levels if gen_drain becomes unstuck 
  after increasing verbose levels
- WT-13216: Assess the use of cache eviction check in compact
- [All Jira issues closed in 7.0.21](https://jira.mongodb.org/issues/?jql=project%20in%20(SERVER%2C%20TOOLS%2C%20WT)%20AND%20resolution%20%3D%20Fixed%20AND%20fixVersion%20%3D%207.0.21)
- 7.0.21-changelog 

### 7.0.20 - Apr 29, 2025

**Important:** Fix for incorrect handling of incomplete data may prevent mongos from accepting new connections

Due to CVE-2025-6714, in MongoDB 7.0 prior to 7.0.6,  MongoDB Server's `mongos`
component can become unresponsive to new connections due to incorrect handling of incomplete data. 
This issue affects sharded MongoDB clusters that are configured with load balancer support for `mongos`
using `HAProxy` on specified ports. 

This issue affects the following MongoDB Server versions:

- 8.0.0 - 8.0.8
- 7.0.0 - 7.0.19
- 6.0.0 - 6.0.22 

**CVSS Score**: 7.5

**CWE**: CWE-834 Excessive Iteration AND CWE-400 Uncontrolled Resource Consumption

Issues fixed:

- SERVER-93120: FTDC collection blocked on locked backupCursor state read
- SERVER-106753: Incorrect handling of incomplete data may prevent `mongos` from accepting new connections
- [All Jira issues closed in 7.0.20](https://jira.mongodb.org/issues/?jql=project%20in%20(SERVER%2C%20TOOLS%2C%20WT)%20AND%20resolution%20%3D%20Fixed%20AND%20fixVersion%20%3D%207.0.20)
- 7.0.20-changelog 

### 7.0.19 - Apr 14, 2025

**Important:** MongoDB Server may be susceptible to privilege escalation due to $mergeCursors stage

Due to CVE-2025-6713, in MongoDB 7.0 prior to 7.0.6, an unauthorized user may 
leverage a specially crafted aggregation pipeline to access data without 
proper authorization due to improper handling of the `$mergeCursors` stage 
in MongoDB Server. This may lead to access to data without further authorization.

This issue affects the following MongoDB Server versions:

- 8.0.0 - 8.0.6
- 7.0.0 - 7.0.18
- 6.0.0 - 6.0.21

**CVSS Score**: 7.7

**CWE**: CWE-285: Improper Authorization

Issues fixed:

- SERVER-106752 MongoDB Server may be susceptible to privilege escalation 
  due to `$mergeCursors` stage

### 7.0.18 - Mar 19, 2025

Issues fixed:

- SERVER-82037 Memory used by sorter spills can grow without
  bound
- SERVER-90689 Change THP startup warning checks to also look
  at process level settings before emitting warning
- SERVER-95452 Prevent CollectionRoutingInfoTargeter from
  iterating all chunk ranges during update and delete
- SERVER-98720 Add missing redact() calls to "Plan executor
  error" warning logs
- SERVER-100901 Relax user digest invariant to tassert in
  ShardingTaskExecutor
- [All Jira issues closed in 7.0.18](https://jira.mongodb.org/issues/?jql=project%20in%20(SERVER%2C%20TOOLS%2C%20WT)%20AND%20resolution%20%3D%20Fixed%20AND%20fixVersion%20%3D%207.0.18)
- 7.0.18-changelog 

### 7.0.17 - Feb 21, 2025

**Important:** Pre-Authentication Denial of Service Vulnerability in MongoDB Server's OIDC Authentication

Due to CVE-2025-6709, in MongoDB 7.0 prior to 7.0.6, MongoDB Server is 
susceptible to a denial of service vulnerability due to improper handling 
of specific date values in JSON input when using OIDC authentication. This 
can be reproduced using the mongo shell to send a malicious JSON payload 
leading to an invariant failure and server crash.

This issue affects the following MongoDB Server versions:

- 8.0.0 - 8.0.4
- 7.0.0 - 7.0.16

The same issue affects MongoDB Server v6.0, but an attacker can only induce denial of service 
after authenticating. This issue affects the following MongoDB Server versions:

- 6.0.0 - 6.0.20

**CVSS Score**: 7.5

**CWE**: CWE-20: Improper Input Validation

**Important:** Pre-authentication Denial of Service Stack Overflow Vulnerability in JSON Parsing via Excessive Recursion in MongoDB

Due to CVE-2025-6710, in MongoDB 7.0 prior to 7.0.6, MongoDB Server may be susceptible 
to stack overflow due to JSON parsing mechanism, where specifically crafted 
JSON inputs may induce unwarranted levels of recursion, resulting in excessive 
stack space consumption. Such inputs can lead to a stack overflow that causes 
the server to crash which could occur pre-authorisation.

This issue affects the following MongoDB Server versions:

- 8.0.0 - 8.0.4
- 7.0.0 - 7.0.16

The same issue affects MongoDB Server v6.0, but an attacker can only induce 
denial of service after authenticating. This issue affects the 
following MongoDB Server versions:

- 6.0.0 - 6.0.20

**CVSS Score**: 7.5

**CWE**: CWE-674: Uncontrolled Recursion

Issues fixed:

- SERVER-73641 Timeseries filtering can miss extended-range
  events when sharded
- SERVER-76883 Reduce chattiness of "Role does not exist" logs
  for externally sourced users
- SERVER-85627 Log information of interrupted thead in stepdown
  killOp
- SERVER-89614 $out doesn't clean up correctly between rename
  and dropping temp collection
- SERVER-106748 Pre-auth denial of service when accepting OIDC authentication
- SERVER-106749 Pre-authentication Denial of Service Stack Overflow Vulnerability 
  in JSON Parsing via Excessive Recursion in MongoDB

- [All Jira issues closed in 7.0.17](https://jira.mongodb.org/issues/?jql=project%20in%20(SERVER%2C%20TOOLS%2C%20WT)%20AND%20resolution%20%3D%20Fixed%20AND%20fixVersion%20%3D%207.0.17)
- 7.0.17-changelog

### 7.0.16 - Dec 20, 2024

Issues Fixed:

- SERVER-67816 Time-series bucket rounding for pre-1970 dates
  behaves unexpectedly
- SERVER-90672 Investigate potential bug in time-series insert
  path that allows for multiple buckets to have the same OIDs, across
  stripes
- SERVER-90893 listDatabases inconsistent with concurrent DDL
  operations
- SERVER-94559 Time-series measurement deletes update the
  minTime of a bucket
- SERVER-95067 Time-series inserts can generate multiple
  batches referencing the same bucket
- [All Jira issues closed in 7.0.16](https://jira.mongodb.org/issues/?jql=project%20in%20(SERVER%2C%20TOOLS%2C%20WT)%20AND%20resolution%20%3D%20Fixed%20AND%20fixVersion%20%3D%207.0.16)
- 7.0.16-changelog

### 7.0.15 - Oct 24, 2024

**Important:** Improper neutralization of null bytes may lead to buffer over-reads in MongoDB Server

In MongoDB 7.0 prior to 7.0.6, an authorized user may trigger crashes or 
receive the contents of buffer over-reads of Server memory by 
issuing specially crafted requests that construct malformed BSON 
in the MongoDB Server.

This issue affects MongoDB Server versions:

- 5.0.0 - 5.0.29
- 6.0.0 - 6.0.18
- 7.0.0 - 7.0.14
- 8.0.0 - 8.0.2

- SERVER-96419 Improper neutralization of null bytes may lead to buffer over-reads in MongoDB Server
- [All Jira issues closed in 7.0.15](https://jira.mongodb.org/issues/?jql=project%20in%20(SERVER%2C%20TOOLS%2C%20WT)%20AND%20resolution%20%3D%20Fixed%20AND%20fixVersion%20%3D%207.0.15)
- 7.0.15-changelog

### 7.0.14 - Aug 26, 2024

Issues Fixed:

- SERVER-82814 Support internal expr comparison operators when 
  determining clustered collection scan bounds
- SERVER-85892 $merge with pipeline after $documents returns 
  error
- SERVER-91195 Provide a generic backportable solution not to 
  miss top-level timeseries collection options
- SERVER-91625 Enable indexed plans for expressions with $$NOW, 
  $$CLUSTER_TIME and $$USER_ROLES
- WT-12643 Fix Eviction Server walk logic so that it's able to 
  evict all pages
- [All Jira issues closed in 7.0.14](https://jira.mongodb.org/browse/WT-13109?jql=project%20in%20(SERVER%2CTOOLS%2CWT)%20AND%20resolution%3D%27Fixed%27%20and%20(fixversion%3D7.0.13%20or%20fixversion%20%3D%207.0.14))
- 7.0.14-changelog

### 7.0.12 - Jun 28, 2024

**Important:** Fix for CSFLE and Queryable Encryption self-lookup may send values in subpipelines as plaintext instead of ciphertext

Due to CVE-2024-8013, in MongoDB 7.0 prior to 7.0.6, a bug in query analysis of 
certain complex self-referential `$lookup` subpipelines 
may result in literal values in expressions for encrypted fields 
being sent to the server malformed.

Should this occur, no documents are returned or written. 
This issue affects the `mongocryptd` binary and `mongo_crypt_v1` 
shared library in the following MongoDB Server versions:

- 7.3.0 - 7.3.3
- 7.0.0 - 7.0.11
- 6.0.0 - 6.0.16
- 5.0.0 - 5.0.28

**CVSS Score**: 2.2

**CWE**: CWE-319: Cleartext Transmission of Sensitive Information

Issues Fixed:

- SERVER-96254 CSFLE and Queryable Encryption self-lookup may 
  fail to encrypt values in subpipelines
- SERVER-64574 Upgrade MozJS/Spidermonkey to the latest ESR
- SERVER-86674 Primary catch-up may believe it is caught up when it 
  is not
- SERVER-90485 $sort does not work as expected when used in 
  conjunction with includeArrayIndex
- SERVER-91362 Performance: Do not copy JS "scope" object if a 
  cached JsExecution exists
- WT-12736 Mark the page clean after re-instantiating the page with 
  prepared updates
- [All Jira issues closed in 7.0.12](https://jira.mongodb.org/issues/?jql=project%20in%20(SERVER%2CTOOLS%2CWT)%20AND%20resolution%3D%27Fixed%27%20and%20fixversion%3D7.0.12)
- 7.0.12-changelog

### 7.0.11 - May 23, 2024

Issues Fixed:

- SERVER-85279 Don't run the FTDC collection stats
  collector on arbiters
- SERVER-89495 Disable test parameters even when no
  setParameters are specified
- SERVER-89625 Handle directoryPerDb and
  wiredTigerDirectoryForIndexes correctly when reporting
  namespaces and UUIDs during a backup
- SERVER-90288 Bitwise query operators should interpret
  lowest addressable byte in BinData as least significant byte
- WT-12609 Improve checkpoint cleanup and page eviction
  logic

- [All Jira issues closed in 7.0.11](https://jira.mongodb.org/issues/?jql=project%20in%20(SERVER%2CTOOLS%2CWT)%20AND%20resolution%3D%27Fixed%27%20and%20fixversion%3D7.0.11)
- 7.0.11-changelog

### 7.0.9 - Apr 26, 2024

Issues fixed: 

- SERVER-79637 Incorrect query results in $lookup with TS foreign collection 
  using a correlated predicate
- SERVER-82349 Mongo 7 crashes on applyOps index delete/drops without a collection UUID
- SERVER-86407 Validation does not produce complete results when it should
- SERVER-88173 BinData bit comparisons give wrong results in many cases
- WT-10807 Skip in-memory deleted pages as part of the tree walk

- [All Jira issues closed in 7.0.9](https://jira.mongodb.org/issues/?jql=project%20in%20(SERVER%2CTOOLS%2CWT)%20AND%20resolution%3D%27Fixed%27%20and%20fixversion%3D7.0.9)
- 7.0.9-changelog

### 7.0.8 - Apr 3, 2024

Issues fixed: 

- SERVER-78556 Return default of internalInsertMaxBatchSize to 64
- SERVER-79575 Fix numa node counting
- SERVER-86583 Non-transactional snapshot read on unsharded collection 
  may execute with mismatched sharding metadata
- SERVER-87666 Query shape for $documents is unique on each execution
- SERVER-88360 Remove "Sharding catalog and local catalog collection 
  uuid do not match" tripwire assertion
- [All Jira issues closed in 7.0.8](https://jira.mongodb.org/issues/?jql=project%20in%20(SERVER%2CTOOLS%2CWT)%20AND%20resolution%3D%27Fixed%27%20and%20fixversion%3D7.0.8)
- 7.0.8-changelog

### 7.0.7 - Mar 18, 2024

Issues fixed: 

- SERVER-84368 CreateIndex fails with StaleConfig if run from a 
  stale mongos against a sharded non-empty collection
- SERVER-84628 Startup warning in mongos for Read/Write Concern
- SERVER-85459 [v7.0] bucketRoundingSeconds param is accepted
  by nodes on FCV 6.0, binary 7.0
- SERVER-85869 Exhaustive find on config shard can return stale
  data
- SERVER-87061 Sharded multi-document transactions can observe
  partial effects of concurrent reshard operation
- [All Jira issues closed in 7.0.7](https://jira.mongodb.org/issues/?jql=project%20in%20(SERVER%2CTOOLS%2CWT)%20AND%20resolution%3D%27Fixed%27%20and%20fixversion%3D%277.0.7%27)
- 7.0.7-changelog

### 7.0.6 - Feb 28, 2024

**Important:** Fix for MongoDB Server may allow successful untrusted connection

Due to CVE-2024-1351, in MongoDB 7.0 prior to 7.0.6, under certain
configurations of `--tlsCAFile` and
`CAFile`, MongoDB Server may skip peer certificate
validation which may result in untrusted connections to succeed.

This may effectively reduce the security guarantees provided by TLS
and open connections that should have been closed due to failing
certificate validation. This issue affects the following MongoDB
Server versions:

- 7.0.0 - 7.0.5
- 6.0.0 - 6.0.13
- 5.0.0 - 5.0.24
- 4.4.0 - 4.4.28

**CVSS Score**: 8.8 

**CWE**: CWE-295: Improper Certificate Validation

Issues fixed: 

- SERVER-72703 Downgrade $out's db lock to MODE_IX
- SERVER-82353 Multi-document transactions can miss documents 
  when movePrimary runs concurrently
- SERVER-84338 Top level $or queries may lead to invalid SBE 
  plan cache entry which returns wrong results
- SERVER-84723 Sharded multi-document transactions can observe 
  partial effects of concurrent DDL operations
- WT-11062 Safe free the ref addr to allow concurrent access
- [All Jira issues closed in 7.0.6](https://jira.mongodb.org/issues/?jql=project%20in%20(SERVER%2CTOOLS%2CWT)%20AND%20resolution%3D%27Fixed%27%20and%20fixversion%3D%277.0.6%27)
- 7.0.6-changelog

### 7.0.5 - Jan 5, 2024

Issues fixed: 

- SERVER-33494 WT SizeStorer never deletes old entries
- SERVER-80363 server default writeConcern is not honored when 
  wtimeout is set
- SERVER-83091 $or query can trigger an infinite loop during 
  plan enumeration
- SERVER-83830 On Enterprise build creating a collection in a 
  replica set with the storageEngine.inMemory option breaks secondaries
- WT-7929 Investigate a solution to avoid FTDC stalls during 
  checkpoint
- [All Jira issues closed in 7.0.5](https://jira.mongodb.org/issues/?jql=project%20in%20(SERVER%2CTOOLS%2CWT)%20AND%20resolution%3D%27Fixed%27%20and%20fixversion%3D%277.0.5%27)
- 7.0.5-changelog

### 7.0.4 - Nov 27, 2023

Issues fixed: 

- SERVER-67962 Applying config.image_collection deletes needs
  better concurrency control
- SERVER-69244 $merge fails when session default read concern
  has been set to "majority"
- SERVER-79975 [Classic] Optimize large group keys
- SERVER-81133 Speedup logic to persist routing table cache
- SERVER-82446 $densify use case can result in documents
  outside of range
- [All Jira issues closed in 7.0.4](https://jira.mongodb.org/issues/?jql=project%20in%20(SERVER%2CTOOLS%2CWT)%20AND%20resolution%3D%27Fixed%27%20and%20fixversion%3D%277.0.4%27)
- 7.0.4-changelog

### 7.0.3 - Nov 9, 2023

Issues fixed: 

- SERVER-77506 Sharded multi-document transactions can
  mismatch data and ShardVersion 
- SERVER-79088 Improve SBE
  multi-planner performance for query which returns zero results 
- SERVER-81106 Recipient shard doesn't wait for the collection
  version to be locally persisted before starting the cloning phase 
- SERVER-81966 Avoid modification of previous ChunkMap instances
  during refresh 
- WT-11564 Fix RTS to read the newest
  transaction value only when it exists in the checkpoint 
- [All Jira issues closed in 7.0.3](https://jira.mongodb.org/issues/?jql=project%20in%20(SERVER%2CTOOLS%2CWT)%20AND%20resolution%3D%27Fixed%27%20and%20fixversion%3D%277.0.3%27)
- 7.0.3-changelog

### 7.0.2 - Sep 29, 2023

Issues fixed: 

- SERVER-74954 Incorrect result when contained $or rewrites $elemMatch 
  extra condition
- SERVER-79771 Make Resharding Operation Resilient to 
  NetworkInterfaceExceededTimeLimit
- SERVER-79912 CheckReplDBHash reports failure with system.buckets 
  collections due to invalid BSON
- SERVER-79982 Batched catalog writers can run concurrently with 
  HistoricalCatalogIdTracker::cleanup() and lead to incorrect PIT find results
- SERVER-80488 Avoid traversing routing table in balancer split chunk 
  policy
- [All Jira issues closed in 7.0.2](https://jira.mongodb.org/issues/?jql=project%20in%20(SERVER%2CTOOLS%2CWT)%20AND%20resolution%3D%27Fixed%27%20and%20fixversion%3D%277.0.2%27)
- 7.0.2-changelog

### 7.0.1 - Sep 5, 2023

Issues fixed: 

- SERVER-71627 Refreshing cached collection route info severely 
  blocks all client requests for a cluster with 1 million chunks
- SERVER-77183 $project followed by $group sometimes gives incorrect 
  results 
- SERVER-80256 QueryPlannerAnalysis::explodeForSort should not assume 
  that index scans produce disjoint results
- [All Jira issues closed in 7.0.1](https://jira.mongodb.org/issues/?jql=project%20in%20(SERVER%2CTOOLS%2CWT)%20AND%20resolution%3D%27Fixed%27%20and%20fixversion%3D%277.0.1%27)
- 7.0.1-changelog

### 7.0.0 - Aug 15, 2023
