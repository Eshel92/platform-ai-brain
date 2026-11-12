<!-- Part 6 of 18 of release-notes/index.md (split because the page is big). -->

## 9.3.4 [elasticsearch-9.3.4-release-notes]

### Features and enhancements [elasticsearch-9.3.4-features-enhancements]

Aggregations:
* Bump heap usage limits for INLINE STATS [#144679](https://github.com/elastic/elasticsearch/pull/144679)

ES|QL:
* Skip time series field type merge for non-TS agg queries [#143262](https://github.com/elastic/elasticsearch/pull/143262)

Packaging:
* Update bundled JDK to Java 26 [#146167](https://github.com/elastic/elasticsearch/pull/146167)


### Fixes [elasticsearch-9.3.4-fixes]

EQL:
* Fix propagation of filters on join keys for missing events [#145813](https://github.com/elastic/elasticsearch/pull/145813) (issue: [#145402](https://github.com/elastic/elasticsearch/issues/145402))

ES|QL:
* Do not discard disjunction conditions when is null/is not null might invalidate them [#145941](https://github.com/elastic/elasticsearch/pull/145941)
* Don't use a Literal for `constant_keyword` fields when used inside full-text functions [#145632](https://github.com/elastic/elasticsearch/pull/145632) (issue: [#145570](https://github.com/elastic/elasticsearch/issues/145570))
* ESQL - Fix performance loading source when vectors are excluded [#146223](https://github.com/elastic/elasticsearch/pull/146223) (issue: [#145799](https://github.com/elastic/elasticsearch/issues/145799))
* Fix handling of values on the time bucket boundaries for ES|QL increase [#145794](https://github.com/elastic/elasticsearch/pull/145794)
* Fix nested fields loading under NULLIFY [#145741](https://github.com/elastic/elasticsearch/pull/145741) (issue: [#142616](https://github.com/elastic/elasticsearch/issues/142616))
* Fix rate/increase single-value bucket handling for delta temporality [#146518](https://github.com/elastic/elasticsearch/pull/146518)
* Fix starts_with/ends_with with special chars [#146348](https://github.com/elastic/elasticsearch/pull/146348) (issue: [#130851](https://github.com/elastic/elasticsearch/issues/130851))
* Keywords mv count fix [#145390](https://github.com/elastic/elasticsearch/pull/145390)

Infra/Core:
* Throw a 400 error for malformed parsing input when missing element end [#145777](https://github.com/elastic/elasticsearch/pull/145777)

Ingest Node:
* Fix pipeline resolution cache for bulk requests [#144648](https://github.com/elastic/elasticsearch/pull/144648)
* Fix waiting for enrich policy execution for users without the `monitor` privilege [#145751](https://github.com/elastic/elasticsearch/pull/145751)

Machine Learning:
* Omit uncomputed model stats [#146186](https://github.com/elastic/elasticsearch/pull/146186)

Mapping:
* Fix match only text decoding surrogate pairs [#146567](https://github.com/elastic/elasticsearch/pull/146567) (issue: [#146538](https://github.com/elastic/elasticsearch/issues/146538))

Reindex:
* Restore initial thread context during reindex etc [#146134](https://github.com/elastic/elasticsearch/pull/146134)

Search:
* Add cancellation support to `IndicesRequestCache` [#141708](https://github.com/elastic/elasticsearch/pull/141708)
* Collapse pathological regex quantifier stacking to prevent NFA construction OOM [#145452](https://github.com/elastic/elasticsearch/pull/145452)
* Fix `terminate_after` not honored for aggs when size=0 [#146199](https://github.com/elastic/elasticsearch/pull/146199) (issue: [#126665](https://github.com/elastic/elasticsearch/issues/126665))
* Fix bug parsing "request" parameter in clear cache API, it should clear the request cache only [#145726](https://github.com/elastic/elasticsearch/pull/145726)
* Use query circuit breaker for wildcard/regexp determinization [#145427](https://github.com/elastic/elasticsearch/pull/145427) (issue: [#145128](https://github.com/elastic/elasticsearch/issues/145128))

Snapshot/Restore:
* Use `IllegalArgumentException` over `RepositoryException` for readonly-repository checks [#140200](https://github.com/elastic/elasticsearch/pull/140200)

TSDB:
* Replace `IllegalStateException` with `IllegalArgumentException` for conflicting time series metadata [#142370](https://github.com/elastic/elasticsearch/pull/142370)

Vector Search:
* Fix NPE in GPU resource pool when CuVSResources creation fails [#146632](https://github.com/elastic/elasticsearch/pull/146632)
* Fix NPE when having double nested field with knn query [#146933](https://github.com/elastic/elasticsearch/pull/146933) (issue: [#141830](https://github.com/elastic/elasticsearch/issues/141830))
* [DiskBBQ] Fix `offHeap` size for empty indices [#146347](https://github.com/elastic/elasticsearch/pull/146347)
* [DiskBBQ] Wait for queue saturation in `MaxScoreTopKnnCollector` [#145341](https://github.com/elastic/elasticsearch/pull/145341)




## 9.2.8 [elasticsearch-9.2.8-release-notes]

### Features and enhancements [elasticsearch-9.2.8-features-enhancements]

Authentication:
* Improve SAML error handling by adding metadata [#137598](https://github.com/elastic/elasticsearch/pull/137598) (issue: [#128179](https://github.com/elastic/elasticsearch/issues/128179))
* In-response-to in saml successful response [#137599](https://github.com/elastic/elasticsearch/pull/137599) (issue: [#128179](https://github.com/elastic/elasticsearch/issues/128179))

Security:
* Skip automaton construction for literal resource strings in application privilege checks [#144685](https://github.com/elastic/elasticsearch/pull/144685)


### Fixes [elasticsearch-9.2.8-fixes]

CAT APIs:
* Fix `ArrayIndexOutOfBoundsException` in cat nodes for partial load average arrays [#144859](https://github.com/elastic/elasticsearch/pull/144859)

CCR:
* CCR follower index needs to copy transport version from CCR leader index [#145035](https://github.com/elastic/elasticsearch/pull/145035)

ES|QL:
* Cancel async query on expiry [#143016](https://github.com/elastic/elasticsearch/pull/143016) (issue: [#142662](https://github.com/elastic/elasticsearch/issues/142662))
* Reduce `LuceneOperator.Status` memory consumption with large QueryDSL queries [#143175](https://github.com/elastic/elasticsearch/pull/143175) (issue: [#143164](https://github.com/elastic/elasticsearch/issues/143164))

FIPS:
* Fix createLDAPCertStore failing in FIPS mode [#144453](https://github.com/elastic/elasticsearch/pull/144453) (issues: [#144376](https://github.com/elastic/elasticsearch/issues/144376), [#144377](https://github.com/elastic/elasticsearch/issues/144377))

Geo:
* Fix `geo_centroid` over `geo_shape` merging multiple shards [#144637](https://github.com/elastic/elasticsearch/pull/144637) (issue: [#144504](https://github.com/elastic/elasticsearch/issues/144504))

Infra/Core:
* Fix system index mapping update for reindexed indices after migration [#144782](https://github.com/elastic/elasticsearch/pull/144782) (issue: [#144764](https://github.com/elastic/elasticsearch/issues/144764))

Machine Learning:
* Fix anomaly detection jobs stuck in opening by continously retrying to set the state to opened. [#139668](https://github.com/elastic/elasticsearch/pull/139668)
* [Inference API] Support chunking settings for sparse embeddings in custom service [#138776](https://github.com/elastic/elasticsearch/pull/138776)

Search:
* Fix `ArrayIndexOutOfBoundsException` in fetch phase with partial results [#144385](https://github.com/elastic/elasticsearch/pull/144385) (issue: [#140495](https://github.com/elastic/elasticsearch/issues/140495))
* Fix circuit breaker leak in percolator query construction [#144827](https://github.com/elastic/elasticsearch/pull/144827)
* Fix request cache invalidation to use ES cache helper consistently [#144581](https://github.com/elastic/elasticsearch/pull/144581)
* Fix wrong return value in `ContextIndexSearcher.totalTermFreq` [#144333](https://github.com/elastic/elasticsearch/pull/144333)

Snapshot/Restore:
* Fix up exception messages in `AzureBlobStore` [#144654](https://github.com/elastic/elasticsearch/pull/144654)

Vector Search:
* [DiskBBQ] Fix index sorting on flush [#144938](https://github.com/elastic/elasticsearch/pull/144938)
* [DiskBBQ] Fix index sorting on flush (2nd attempt) [#145076](https://github.com/elastic/elasticsearch/pull/145076)

Watcher:
* Validate Watcher Proxy Allowlist [#144759](https://github.com/elastic/elasticsearch/pull/144759)




## 9.3.3 [elasticsearch-9.3.3-release-notes]

### Features and enhancements [elasticsearch-9.3.3-features-enhancements]

Security:
* Skip automaton construction for literal resource strings in application privilege checks [#144685](https://github.com/elastic/elasticsearch/pull/144685)


### Fixes [elasticsearch-9.3.3-fixes]

CAT APIs:
* Fix `ArrayIndexOutOfBoundsException` in cat nodes for partial load average arrays [#144859](https://github.com/elastic/elasticsearch/pull/144859)

CCR:
* CCR follower index needs to copy transport version from CCR leader index [#145035](https://github.com/elastic/elasticsearch/pull/145035)

ES|QL:
* Cancel async query on expiry [#143016](https://github.com/elastic/elasticsearch/pull/143016) (issue: [#142662](https://github.com/elastic/elasticsearch/issues/142662))
* Don't over-alloc when unpacking dimension values [#144525](https://github.com/elastic/elasticsearch/pull/144525)
* ESQL: Fix incorrectly optimized fork with nullify unmapped_fields [#143030](https://github.com/elastic/elasticsearch/pull/143030) (issue: [#142762](https://github.com/elastic/elasticsearch/issues/142762))
* ESQL: Fix null comparison type checking [#140660](https://github.com/elastic/elasticsearch/pull/140660) (issue: [#140460](https://github.com/elastic/elasticsearch/issues/140460))
* Fix field caps incorrectly synthesizing object parents under subobjects:false passthrough mappers [#144183](https://github.com/elastic/elasticsearch/pull/144183) (issue: [#144179](https://github.com/elastic/elasticsearch/issues/144179))
* Reduce `LuceneOperator.Status` memory consumption with large QueryDSL queries [#143175](https://github.com/elastic/elasticsearch/pull/143175) (issue: [#143164](https://github.com/elastic/elasticsearch/issues/143164))

FIPS:
* Fix createLDAPCertStore failing in FIPS mode [#144453](https://github.com/elastic/elasticsearch/pull/144453) (issues: [#144376](https://github.com/elastic/elasticsearch/issues/144376), [#144377](https://github.com/elastic/elasticsearch/issues/144377))

Geo:
* Fix `geo_centroid` over `geo_shape` merging multiple shards [#144637](https://github.com/elastic/elasticsearch/pull/144637) (issue: [#144504](https://github.com/elastic/elasticsearch/issues/144504))

Infra/Core:
* Fix system index mapping update for reindexed indices after migration [#144782](https://github.com/elastic/elasticsearch/pull/144782) (issue: [#144764](https://github.com/elastic/elasticsearch/issues/144764))

Machine Learning:
* Fix "reset anomaly detection API" crashing when only colliding indices exist [#144545](https://github.com/elastic/elasticsearch/pull/144545) (issue: [#144544](https://github.com/elastic/elasticsearch/issues/144544))

Mapping:
* Lazily create matcher in `BinaryDvConfirmedQuery` [#144698](https://github.com/elastic/elasticsearch/pull/144698)

Search:
* Fix `ArrayIndexOutOfBoundsException` in fetch phase with partial results [#144385](https://github.com/elastic/elasticsearch/pull/144385) (issue: [#140495](https://github.com/elastic/elasticsearch/issues/140495))
* Fix circuit breaker leak in percolator query construction [#144827](https://github.com/elastic/elasticsearch/pull/144827)
* Fix request cache invalidation to use ES cache helper consistently [#144581](https://github.com/elastic/elasticsearch/pull/144581)
* Fix wrong return value in `ContextIndexSearcher.totalTermFreq` [#144333](https://github.com/elastic/elasticsearch/pull/144333)

Snapshot/Restore:
* Fix up exception messages in `AzureBlobStore` [#144654](https://github.com/elastic/elasticsearch/pull/144654)

Vector Search:
* Fix `dense_vector` default index options when using BFLOAT16 [#145202](https://github.com/elastic/elasticsearch/pull/145202) (issue: [#145204](https://github.com/elastic/elasticsearch/issues/145204))
* [DiskBBQ] Fix index sorting on flush [#144938](https://github.com/elastic/elasticsearch/pull/144938)
* [DiskBBQ] Fix index sorting on flush (2nd attempt) [#145076](https://github.com/elastic/elasticsearch/pull/145076)




## 9.2.7 [elasticsearch-9.2.7-release-notes]

### Features and enhancements [elasticsearch-9.2.7-features-enhancements]

Authentication:
* Bump Kiota Libs [#143556](https://github.com/elastic/elasticsearch/pull/143556)

Authorization:
* [JupiterOne] Add `manage`, `create_index`, `read`, `index`, `write`, `delete`, permission for third party agent indices `kibana_system` [#140049](https://github.com/elastic/elasticsearch/pull/140049)
* [Sentinel One] Add `manage`, `create_index`, `read`, `index`, `write`, `delete`, permission for third-party agent indices in the `Kibana system` to support the unified alert data stream. [#142648](https://github.com/elastic/elasticsearch/pull/142648)

Monitoring:
* Apm-server: update monitor mappings to include new TBS metrics [#140700](https://github.com/elastic/elasticsearch/pull/140700)

Search:
* Fix nested object float arrays being mapped to dense vectors when they are mapped in dynamic template mappings [#143733](https://github.com/elastic/elasticsearch/pull/143733) (issue: [#143732](https://github.com/elastic/elasticsearch/issues/143732))

Transform:
* Skip checkpoint query filter when `runtime_mappings` are present [#142452](https://github.com/elastic/elasticsearch/pull/142452)


### Fixes [elasticsearch-9.2.7-fixes]

Aggregations:
* Fix `ClassCastException` when merging `TopHits` with mixed sort field types [#141919](https://github.com/elastic/elasticsearch/pull/141919) (issue: [#141714](https://github.com/elastic/elasticsearch/issues/141714))

Data streams:
* Apm-data: explicit map of `timestamp.us` to long [#143173](https://github.com/elastic/elasticsearch/pull/143173)

ES|QL:
* ESQL - enable zero_terms_query option in MATCH function [#143668](https://github.com/elastic/elasticsearch/pull/143668) (issue: [#143070](https://github.com/elastic/elasticsearch/issues/143070))
* Promptly clean up CCS exchange sinks [#143325](https://github.com/elastic/elasticsearch/pull/143325)

Machine Learning:
* Fix Duplicate ML Model Allocations on Same Node [#142872](https://github.com/elastic/elasticsearch/pull/142872)
* Fixed stats API to use correct allocation count for `required_native_memory_bytes` calculation [#143077](https://github.com/elastic/elasticsearch/pull/143077) (issue: [#107831](https://github.com/elastic/elasticsearch/issues/107831))

SQL:
* Fix `QlIllegalArgumentException` with non-foldable date range queries [#142386](https://github.com/elastic/elasticsearch/pull/142386) (issue: [#137365](https://github.com/elastic/elasticsearch/issues/137365))

Search:
* Add circuit breaker for query construction to prevent OOM from automaton-based queries [#142150](https://github.com/elastic/elasticsearch/pull/142150)
* Add timeout support for KNN searches in the DFS phase [#142925](https://github.com/elastic/elasticsearch/pull/142925)

Security:
* Disable CAE in microsoft-graph-authz plugin [#142848](https://github.com/elastic/elasticsearch/pull/142848) (issue: [#142743](https://github.com/elastic/elasticsearch/issues/142743))
* Fix use-after-free in `SearchApplicationIndexService` buffer lifecycle [#143134](https://github.com/elastic/elasticsearch/pull/143134)

Snapshot/Restore:
* Fix cancellation race in `CancellableRateLimitedFluxIterator` [#141974](https://github.com/elastic/elasticsearch/pull/141974)

Transform:
* [ML]Fix latest transforms disregarding updates when sort and sync fields are non-monotonic [#142856](https://github.com/elastic/elasticsearch/pull/142856) (issue: [#90643](https://github.com/elastic/elasticsearch/issues/90643))
