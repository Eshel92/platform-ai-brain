<!-- Part 7 of 18 of release-notes/index.md (split because the page is big). -->

## 9.3.2 [elasticsearch-9.3.2-release-notes]

### Features and enhancements [elasticsearch-9.3.2-features-enhancements]

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


### Fixes [elasticsearch-9.3.2-fixes]

Aggregations:
* Fix `ClassCastException` when merging `TopHits` with mixed sort field types [#141919](https://github.com/elastic/elasticsearch/pull/141919) (issue: [#141714](https://github.com/elastic/elasticsearch/issues/141714))

CCS:
* Fix: `_resolve/index API` should be able to accept an empty body [#143159](https://github.com/elastic/elasticsearch/pull/143159)

Data streams:
* Apm-data: explicit map of `timestamp.us` to long [#143173](https://github.com/elastic/elasticsearch/pull/143173)
* Expand DLM user to allow interaction with .workflows-events [#143958](https://github.com/elastic/elasticsearch/pull/143958)

ES|QL:
* Account for missing `StubRelation` due to `SurrogateExpressions` replacement [#142882](https://github.com/elastic/elasticsearch/pull/142882) (issue: [#142219](https://github.com/elastic/elasticsearch/issues/142219))
* ESQL - enable zero_terms_query option in MATCH function [#143668](https://github.com/elastic/elasticsearch/pull/143668) (issue: [#143070](https://github.com/elastic/elasticsearch/issues/143070))
* Fix KQL/QSTR with unmapped fields in NULLIFY mode [#143399](https://github.com/elastic/elasticsearch/pull/143399) (issues: [#142968](https://github.com/elastic/elasticsearch/issues/142968), [#142959](https://github.com/elastic/elasticsearch/issues/142959))
* Fix incorrect nullify with unmapped fields [#142300](https://github.com/elastic/elasticsearch/pull/142300) (issue: [#141870](https://github.com/elastic/elasticsearch/issues/141870))
* Fix nullify where in stats [#144029](https://github.com/elastic/elasticsearch/pull/144029) (issue: [#143991](https://github.com/elastic/elasticsearch/issues/143991))
* Fix unresolved name pattern [#143210](https://github.com/elastic/elasticsearch/pull/143210)
* Promptly clean up CCS exchange sinks [#143325](https://github.com/elastic/elasticsearch/pull/143325)
* Skip nullifying aliases for Aggregate groups. [#141340](https://github.com/elastic/elasticsearch/pull/141340)
* TS command ignores aliases in BY [#143489](https://github.com/elastic/elasticsearch/pull/143489)

Highlighting:
* Fix `UnsupportedOperationException` when using a `plain` highlighter with a query on a field used for index sorting (`index.sort.*`).  [#143680](https://github.com/elastic/elasticsearch/pull/143680)

Machine Learning:
* Fix Duplicate ML Model Allocations on Same Node [#142872](https://github.com/elastic/elasticsearch/pull/142872)
* Fixed stats API to use correct allocation count for `required_native_memory_bytes` calculation [#143077](https://github.com/elastic/elasticsearch/pull/143077) (issue: [#107831](https://github.com/elastic/elasticsearch/issues/107831))

Mapping:
* Apply the source filter on metadata field mappers when loading from synthetic source [#143726](https://github.com/elastic/elasticsearch/pull/143726) (issue: [#143464](https://github.com/elastic/elasticsearch/issues/143464))

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

Vector Search:
* Fix GPU merge `ClassCastException` with wrapped directories [#143531](https://github.com/elastic/elasticsearch/pull/143531)




## 9.2.6 [elasticsearch-9.2.6-release-notes]

### Features and enhancements [elasticsearch-9.2.6-features-enhancements]

Packaging:
* Updating bundled jdk version to 25.0.2+10 [#142500](https://github.com/elastic/elasticsearch/pull/142500)


### Fixes [elasticsearch-9.2.6-fixes]

Cluster Coordination:
* Suppress success callback when failing master task [#142042](https://github.com/elastic/elasticsearch/pull/142042)

ES|QL:
* Avoid a possible NPE by throwing an EIAE instead with more info [#141711](https://github.com/elastic/elasticsearch/pull/141711) (issue: [#141267](https://github.com/elastic/elasticsearch/issues/141267))
* Deep copy `BytesRef` when creating a constant vector block [#141242](https://github.com/elastic/elasticsearch/pull/141242) (issues: [#140615](https://github.com/elastic/elasticsearch/issues/140615), [#140809](https://github.com/elastic/elasticsearch/issues/140809), [#140621](https://github.com/elastic/elasticsearch/issues/140621))
* Dynamically grow hash in linear counting in HLL [#142047](https://github.com/elastic/elasticsearch/pull/142047) (issue: [#41847](https://github.com/elastic/elasticsearch/issues/41847))
* ESQL fix TO_IP leading_zeros=octal parsing [#141776](https://github.com/elastic/elasticsearch/pull/141776) (issue: [#141627](https://github.com/elastic/elasticsearch/issues/141627))
* Fix IP_PREFIX function leaking data in scratch [#141940](https://github.com/elastic/elasticsearch/pull/141940) (issue: [#141628](https://github.com/elastic/elasticsearch/issues/141628))
* Fix NPE with null field parameter [#142328](https://github.com/elastic/elasticsearch/pull/142328) (issue: [#142281](https://github.com/elastic/elasticsearch/issues/142281))
* Fix bug with multiple spatial aggs filtering in ES|QL [#142332](https://github.com/elastic/elasticsearch/pull/142332) (issue: [#142329](https://github.com/elastic/elasticsearch/issues/142329))

Inference:
* [Inference API] Do not write "task" field in Jina embedding request if unsupported [#142181](https://github.com/elastic/elasticsearch/pull/142181)
* [Inference API] Fix `ChunkingSettings` field missing from `ModelConfigurations` equals method [#142238](https://github.com/elastic/elasticsearch/pull/142238)
* [Inference API] Prevent trailing slashes from being included in URLs [#141692](https://github.com/elastic/elasticsearch/pull/141692)

Infra/Core:
* Reindexing older indices with percolator fields clears migration assistant errors [#141539](https://github.com/elastic/elasticsearch/pull/141539)

Infra/Logging:
* Fix cluster name in ECS upgrade [#141792](https://github.com/elastic/elasticsearch/pull/141792)

Machine Learning:
* Add missing `job_id` filter to Anomaly Detection data deleter [#138160](https://github.com/elastic/elasticsearch/pull/138160)
* Reduce locking when persisting ML job statistics [#141519](https://github.com/elastic/elasticsearch/pull/141519) (issue: [#140511](https://github.com/elastic/elasticsearch/issues/140511))

Mapping:
* Allow shadowing time series metrics and dimension in non time series indexing [#141549](https://github.com/elastic/elasticsearch/pull/141549) (issue: [#140882](https://github.com/elastic/elasticsearch/issues/140882))

Ranking:
* Fixing for NPE when there is no query specified for the standard retriever [#142479](https://github.com/elastic/elasticsearch/pull/142479) (issue: [#142336](https://github.com/elastic/elasticsearch/issues/142336))
* Implement comprehensive top N parameter handling for text similarity reranker [#142039](https://github.com/elastic/elasticsearch/pull/142039)

Search:
* Ensure Rewriteable.rewriteAndFetch listeners are not executed on transport threads [#141904](https://github.com/elastic/elasticsearch/pull/141904)
* Fix Top Hits Incompatible Field Types on Sort Across Indices [#142046](https://github.com/elastic/elasticsearch/pull/142046) (issue: [#141906](https://github.com/elastic/elasticsearch/issues/141906))
* Fix handling empty collapse construct [#141973](https://github.com/elastic/elasticsearch/pull/141973) (issue: [#139299](https://github.com/elastic/elasticsearch/issues/139299))
* Prevent large CancelTasksRequest descriptions by truncating nodes and actions [#141815](https://github.com/elastic/elasticsearch/pull/141815)
* Reduce cancellation check interval in `CancellableBulkScorer` for better responsiveness [#141747](https://github.com/elastic/elasticsearch/pull/141747)

Snapshot/Restore:
* Ensure paused shard snapshot can be deleted [#141408](https://github.com/elastic/elasticsearch/pull/141408)

Transform:
* Fix transform producing empty dest index when source query references runtime fields [#142450](https://github.com/elastic/elasticsearch/pull/142450) (issue: [#113156](https://github.com/elastic/elasticsearch/issues/113156))
* Fix transform validation to reject PUT and `_start` when user lacks remote index permissions [#142403](https://github.com/elastic/elasticsearch/pull/142403) (issue: [#95367](https://github.com/elastic/elasticsearch/issues/95367))




## 9.3.1 [elasticsearch-9.3.1-release-notes]

### Features and enhancements [elasticsearch-9.3.1-features-enhancements]

ES|QL:
* Fix ILM's 'skipping policy' logging level [#141890](https://github.com/elastic/elasticsearch/pull/141890) (issue: [#141876](https://github.com/elastic/elasticsearch/issues/141876))

Packaging:
* Updating bundled jdk version to 25.0.2+10 [#142500](https://github.com/elastic/elasticsearch/pull/142500)


### Fixes [elasticsearch-9.3.1-fixes]

Allocation:
* Don't overwrite decision with `NOT_PREFERRED` unless its an improvement [#141565](https://github.com/elastic/elasticsearch/pull/141565)

Cluster Coordination:
* Suppress success callback when failing master task [#142042](https://github.com/elastic/elasticsearch/pull/142042)

Data streams:
* Allow `include_source_on_error` param on logs streams [#141391](https://github.com/elastic/elasticsearch/pull/141391) (issue: [#141360](https://github.com/elastic/elasticsearch/issues/141360))

ES|QL:
* Avoid a possible NPE by throwing an EIAE instead with more info [#141711](https://github.com/elastic/elasticsearch/pull/141711) (issue: [#141267](https://github.com/elastic/elasticsearch/issues/141267))
* Deep copy `BytesRef` when creating a constant vector block [#141242](https://github.com/elastic/elasticsearch/pull/141242) (issues: [#140615](https://github.com/elastic/elasticsearch/issues/140615), [#140809](https://github.com/elastic/elasticsearch/issues/140809), [#140621](https://github.com/elastic/elasticsearch/issues/140621))
* Dynamically grow hash in linear counting in HLL [#142047](https://github.com/elastic/elasticsearch/pull/142047) (issue: [#41847](https://github.com/elastic/elasticsearch/issues/41847))
* ESQL fix TO_IP leading_zeros=octal parsing [#141776](https://github.com/elastic/elasticsearch/pull/141776) (issue: [#141627](https://github.com/elastic/elasticsearch/issues/141627))
* Fix IP_PREFIX function leaking data in scratch [#141940](https://github.com/elastic/elasticsearch/pull/141940) (issue: [#141628](https://github.com/elastic/elasticsearch/issues/141628))
* Fix NPE with null field parameter [#142328](https://github.com/elastic/elasticsearch/pull/142328) (issue: [#142281](https://github.com/elastic/elasticsearch/issues/142281))
* Fix TS bug when grouping on aliases [#141568](https://github.com/elastic/elasticsearch/pull/141568)
* Fix bug with multiple spatial aggs filtering in ES|QL [#142332](https://github.com/elastic/elasticsearch/pull/142332) (issue: [#142329](https://github.com/elastic/elasticsearch/issues/142329))
* Fix injected attributes's IDs in `UnionAll` branches [#141262](https://github.com/elastic/elasticsearch/pull/141262)
* Remove incorrect inline stats pruning [#141056](https://github.com/elastic/elasticsearch/pull/141056) (issues: [#140757](https://github.com/elastic/elasticsearch/issues/140757), [#139359](https://github.com/elastic/elasticsearch/issues/139359))

Inference:
* [Inference API] Do not write "task" field in Jina embedding request if unsupported [#142181](https://github.com/elastic/elasticsearch/pull/142181)
* [Inference API] Fix `ChunkingSettings` field missing from `ModelConfigurations` equals method [#142238](https://github.com/elastic/elasticsearch/pull/142238)
* [Inference API] Prevent trailing slashes from being included in URLs [#141692](https://github.com/elastic/elasticsearch/pull/141692)

Infra/Core:
* Reindexing older indices with percolator fields clears migration assistant errors [#141539](https://github.com/elastic/elasticsearch/pull/141539)

Infra/Logging:
* Fix cluster name in ECS upgrade [#141792](https://github.com/elastic/elasticsearch/pull/141792)

Machine Learning:
* Evict old models from the cache before loading new [#140844](https://github.com/elastic/elasticsearch/pull/140844)
* Reduce locking when persisting ML job statistics [#141519](https://github.com/elastic/elasticsearch/pull/141519) (issue: [#140511](https://github.com/elastic/elasticsearch/issues/140511))

Mapping:
* Allow shadowing time series metrics and dimension in non time series indexing [#141549](https://github.com/elastic/elasticsearch/pull/141549) (issue: [#140882](https://github.com/elastic/elasticsearch/issues/140882))

Ranking:
* Fixing for NPE when there is no query specified for the standard retriever [#142479](https://github.com/elastic/elasticsearch/pull/142479) (issue: [#142336](https://github.com/elastic/elasticsearch/issues/142336))
* Implement comprehensive top N parameter handling for text similarity reranker [#142039](https://github.com/elastic/elasticsearch/pull/142039)

SQL:
* Fix `QlIllegalArgumentException` with non-foldable date range queries [#142386](https://github.com/elastic/elasticsearch/pull/142386) (issue: [#137365](https://github.com/elastic/elasticsearch/issues/137365))

Search:
* Ensure Rewriteable.rewriteAndFetch listeners are not executed on transport threads [#141904](https://github.com/elastic/elasticsearch/pull/141904)
* Fix Top Hits Incompatible Field Types on Sort Across Indices [#142046](https://github.com/elastic/elasticsearch/pull/142046) (issue: [#141906](https://github.com/elastic/elasticsearch/issues/141906))
* Fix handling empty collapse construct [#141973](https://github.com/elastic/elasticsearch/pull/141973) (issue: [#139299](https://github.com/elastic/elasticsearch/issues/139299))
* Prevent large CancelTasksRequest descriptions by truncating nodes and actions [#141815](https://github.com/elastic/elasticsearch/pull/141815)
* Reduce cancellation check interval in `CancellableBulkScorer` for better responsiveness [#141747](https://github.com/elastic/elasticsearch/pull/141747)

Security:
* Fix built-in roles sync to retry on lock contention instead of silently discarding pending updates [#142433](https://github.com/elastic/elasticsearch/pull/142433)

Snapshot/Restore:
* Ensure paused shard snapshot can be deleted [#141408](https://github.com/elastic/elasticsearch/pull/141408)
* Terminate GCS retries when node is shutting down [#142193](https://github.com/elastic/elasticsearch/pull/142193)
* Terminate S3 get blob retries when node is shutting down [#142186](https://github.com/elastic/elasticsearch/pull/142186)

Transform:
* Fix transform producing empty dest index when source query references runtime fields [#142450](https://github.com/elastic/elasticsearch/pull/142450) (issue: [#113156](https://github.com/elastic/elasticsearch/issues/113156))
* Fix transform validation to reject PUT and `_start` when user lacks remote index permissions [#142403](https://github.com/elastic/elasticsearch/pull/142403) (issue: [#95367](https://github.com/elastic/elasticsearch/issues/95367))

Vector Search:
* [GPU] Handle segments too big for MSAI segment access [#141872](https://github.com/elastic/elasticsearch/pull/141872) (issue: [#141746](https://github.com/elastic/elasticsearch/issues/141746))
