<!-- Part 9 of 18 of release-notes/index.md (split because the page is big). -->

## 9.2.5 [elasticsearch-9.2.5-release-notes]

### Features and enhancements [elasticsearch-9.2.5-features-enhancements]

ES|QL:
* `BlockSourceReader` should always apply source filtering [#136438](https://github.com/elastic/elasticsearch/pull/136438)

IdentityProvider:
* Support `LimitedRole` in idp role resolution [#140536](https://github.com/elastic/elasticsearch/pull/140536)

Inference:
* Add `max_batch_size` setting to EIS dense and sparse service settings [#141185](https://github.com/elastic/elasticsearch/pull/141185)

Snapshot/Restore:
* Retry bulk-delete items in GCS [#138951](https://github.com/elastic/elasticsearch/pull/138951) (issue: [#138364](https://github.com/elastic/elasticsearch/issues/138364))


### Fixes [elasticsearch-9.2.5-fixes]

Allocation:
* Handle deleted source index in allocation deciders [#140699](https://github.com/elastic/elasticsearch/pull/140699) (issue: [#140630](https://github.com/elastic/elasticsearch/issues/140630))

EQL:
* Fix `_index` on missing events in CCS [#140886](https://github.com/elastic/elasticsearch/pull/140886)

ES|QL:
* Fix folding of case() function with date period and time duration [#141157](https://github.com/elastic/elasticsearch/pull/141157)
* Use sub keyword block loader with `ignore_above` for text fields [#140622](https://github.com/elastic/elasticsearch/pull/140622)

ILM:
* Remove ILM-stopped-check before the cluster update in `migrateToDataTiersRouting` [#140892](https://github.com/elastic/elasticsearch/pull/140892) (issue: [#140885](https://github.com/elastic/elasticsearch/issues/140885))

Inference:
* [Inference API] Include rerank in supported tasks for IBM watsonx integration [#140331](https://github.com/elastic/elasticsearch/pull/140331) (issue: [#140328](https://github.com/elastic/elasticsearch/issues/140328))

Machine Learning:
* Disallow `max_number_of_allocations` > 1 for low priority model deployments [#140163](https://github.com/elastic/elasticsearch/pull/140163) (issue: [#111227](https://github.com/elastic/elasticsearch/issues/111227))

Packaging:
* Fix stderr leak in Docker ES process detection [#140701](https://github.com/elastic/elasticsearch/pull/140701)

Reindex:
* Disable `_delete_by_query` and `_update_by_query` for CCS/stateful [#140301](https://github.com/elastic/elasticsearch/pull/140301)

Search:
* Fix date fields sort formatting with missing values [#135899](https://github.com/elastic/elasticsearch/pull/135899) (issue: [#81960](https://github.com/elastic/elasticsearch/issues/81960))

Snapshot/Restore:
* Fix race condition in `CancellableRateLimitedFluxIterator` [#141323](https://github.com/elastic/elasticsearch/pull/141323)




## 9.1.10 [elasticsearch-9.1.10-release-notes]

### Features and enhancements [elasticsearch-9.1.10-features-enhancements]

Authorization:
* [Axonius] Add `manage`, `create_index`, `read`, `index`, `write`, `delete`, permission for third party agent indices `kibana_system` [#140046](https://github.com/elastic/elasticsearch/pull/140046)

Infra/Core:
* Upgrade lz4 dependency to 1.10.1 [#139221](https://github.com/elastic/elasticsearch/pull/139221)

Security:
* Upgrade Netty to 4.1.130.Final [#139669](https://github.com/elastic/elasticsearch/pull/139669)


### Fixes [elasticsearch-9.1.10-fixes]

Data streams:
* Bug fix: the filter of a data stream alias is not always properly removed [#139679](https://github.com/elastic/elasticsearch/pull/139679)
* Making sure that failure store document converter does not hang on unexpected exceptions [#139712](https://github.com/elastic/elasticsearch/pull/139712) (issue: [#139707](https://github.com/elastic/elasticsearch/issues/139707))

ES|QL:
* ESQL: Fix multi-value constant propagation after `STATS` [#139442](https://github.com/elastic/elasticsearch/pull/139442) (issue: [#135926](https://github.com/elastic/elasticsearch/issues/135926))

Inference:
* [Inference API] Fix auth exception listener not called bug [#139966](https://github.com/elastic/elasticsearch/pull/139966)

Infra/Core:
* Skip frozen nodes on disk watermark check [#140118](https://github.com/elastic/elasticsearch/pull/140118)

Infra/Node Lifecycle:
* Ensure initial state discovery does not block indefinitely on startup [#139467](https://github.com/elastic/elasticsearch/pull/139467)

Recovery:
* Revert "Attempt to clean up index before remote transfer" [#139569](https://github.com/elastic/elasticsearch/pull/139569)

Transform:
* Reduce task match load [#139857](https://github.com/elastic/elasticsearch/pull/139857) (issue: [#139252](https://github.com/elastic/elasticsearch/issues/139252))




## 9.2.4 [elasticsearch-9.2.4-release-notes]

### Features and enhancements [elasticsearch-9.2.4-features-enhancements]

Authorization:
* [Axonius] Add `manage`, `create_index`, `read`, `index`, `write`, `delete`, permission for third party agent indices `kibana_system` [#140046](https://github.com/elastic/elasticsearch/pull/140046)

Infra/Core:
* Upgrade lz4 dependency to 1.10.1 [#139221](https://github.com/elastic/elasticsearch/pull/139221)

Security:
* Upgrade Netty to 4.1.130.Final [#139669](https://github.com/elastic/elasticsearch/pull/139669)


### Fixes [elasticsearch-9.2.4-fixes]

Data streams:
* Bug fix: the filter of a data stream alias is not always properly removed [#139679](https://github.com/elastic/elasticsearch/pull/139679)
* Making sure that failure store document converter does not hang on unexpected exceptions [#139712](https://github.com/elastic/elasticsearch/pull/139712) (issue: [#139707](https://github.com/elastic/elasticsearch/issues/139707))

ES|QL:
* ESQL: Fix multi-value constant propagation after `STATS` [#139442](https://github.com/elastic/elasticsearch/pull/139442) (issue: [#135926](https://github.com/elastic/elasticsearch/issues/135926))
* ESQL: Prevent circular alias references in `DeduplicateAggs` [#139175](https://github.com/elastic/elasticsearch/pull/139175) (issues: [#138346](https://github.com/elastic/elasticsearch/issues/138346), [#139541](https://github.com/elastic/elasticsearch/issues/139541))
* Fix ABSENT/PRESENT on agg with false filter [#139609](https://github.com/elastic/elasticsearch/pull/139609)
* Fix ST_DISTANCE handling of invalid geometry literals that fold to null [#140116](https://github.com/elastic/elasticsearch/pull/140116) (issue: [#138594](https://github.com/elastic/elasticsearch/issues/138594))

Inference:
* [Inference API] Fix auth exception listener not called bug [#139966](https://github.com/elastic/elasticsearch/pull/139966)

Infra/Core:
* Skip frozen nodes on disk watermark check [#140118](https://github.com/elastic/elasticsearch/pull/140118)

Infra/Node Lifecycle:
* Ensure initial state discovery does not block indefinitely on startup [#139467](https://github.com/elastic/elasticsearch/pull/139467)

Machine Learning:
* Reject updating low-priority model deployments to more than 1 allocation [#139989](https://github.com/elastic/elasticsearch/pull/139989) (issue: [#111227](https://github.com/elastic/elasticsearch/issues/111227))

Mapping:
* Fix: IPv6 address parsing with non-zero offset in `InetAddresses` [#139460](https://github.com/elastic/elasticsearch/pull/139460)

Recovery:
* Revert "Attempt to clean up index before remote transfer" [#139569](https://github.com/elastic/elasticsearch/pull/139569)

Snapshot/Restore:
* Register `disable_chunked_encoding` S3 repo setting [#139788](https://github.com/elastic/elasticsearch/pull/139788)

Transform:
* Reduce task match load [#139857](https://github.com/elastic/elasticsearch/pull/139857) (issue: [#139252](https://github.com/elastic/elasticsearch/issues/139252))




## 9.1.9 [elasticsearch-9.1.9-release-notes]

### Features and enhancements [elasticsearch-9.1.9-features-enhancements]

Infra/Core:
* Bump lz4 dependency [#138806](https://github.com/elastic/elasticsearch/pull/138806)

Infra/Logging:
* Upgrade ECS logging layout [#138854](https://github.com/elastic/elasticsearch/pull/138854)

Ingest Node:
* Upgrading tika to 3.2.3 [#139267](https://github.com/elastic/elasticsearch/pull/139267)

Security:
* Improve security migration resilience by handling version conflicts [#137558](https://github.com/elastic/elasticsearch/pull/137558)


### Fixes [elasticsearch-9.1.9-fixes]

CCS:
* Fix: Correctly pickup MRT value for `msearch`'s search requests [#138583](https://github.com/elastic/elasticsearch/pull/138583)

Cluster Coordination:
* Avoid stack overflow in `IndicesClusterStateService` `applyClusterState` [#132536](https://github.com/elastic/elasticsearch/pull/132536)

Downsampling:
* Fix multi fields in downsampling [#138869](https://github.com/elastic/elasticsearch/pull/138869)

ES|QL:
* Fixes esql class cast bug in STATS at planning level [#137511](https://github.com/elastic/elasticsearch/pull/137511) (issues: [#133992](https://github.com/elastic/elasticsearch/issues/133992), [#136598](https://github.com/elastic/elasticsearch/issues/136598))
* [ES|QL] Compare query builders using identity [#139080](https://github.com/elastic/elasticsearch/pull/139080)

Inference:
* [Inference API] Use dimensions field in JinaAI `text_embedding` requests [#139413](https://github.com/elastic/elasticsearch/pull/139413)

Infra/Core:
* GET /_migration/deprecations doesn't check disk watermarks against correct settings values [#138115](https://github.com/elastic/elasticsearch/pull/138115) (issue: [#137005](https://github.com/elastic/elasticsearch/issues/137005))

Ingest Node:
* Handle individual doc parsing failure in bulk request with pipeline [#138624](https://github.com/elastic/elasticsearch/pull/138624) (issue: [#138445](https://github.com/elastic/elasticsearch/issues/138445))

Machine Learning:
* Correctly handle empty inputs in `chunkedInfer()` [#138632](https://github.com/elastic/elasticsearch/pull/138632)

Search:
* Added logic for individual shard failure handling for `CompoundRetrieverBuilder` and fixed how partial search results flag is passed through to `CompoundRetrieverBuilder` [#136732](https://github.com/elastic/elasticsearch/pull/136732)

Security:
* More reliable trigger for security index migration [#139028](https://github.com/elastic/elasticsearch/pull/139028)

Stats:
* Improving performance of stats APIs when the number of shards is very large [#138126](https://github.com/elastic/elasticsearch/pull/138126) (issue: [#97222](https://github.com/elastic/elasticsearch/issues/97222))




## 9.2.3 [elasticsearch-9.2.3-release-notes]

### Features and enhancements [elasticsearch-9.2.3-features-enhancements]

Infra/Core:
* Bump lz4 dependency [#138806](https://github.com/elastic/elasticsearch/pull/138806)

Infra/Logging:
* Upgrade ECS logging layout [#138854](https://github.com/elastic/elasticsearch/pull/138854)

Ingest Node:
* Upgrading tika to 3.2.3 [#139267](https://github.com/elastic/elasticsearch/pull/139267)

Security:
* Improve security migration resilience by handling version conflicts [#137558](https://github.com/elastic/elasticsearch/pull/137558)

Vector Search:
* Add node scoped `vectors.indexing.use_gpu` setting [#138738](https://github.com/elastic/elasticsearch/pull/138738)


### Fixes [elasticsearch-9.2.3-fixes]

Data streams:
* Improving performance of get data streams API by avoiding getting effective mappings [#138948](https://github.com/elastic/elasticsearch/pull/138948)

Downsampling:
* Fix downsampling with disabled subobjects [#138715](https://github.com/elastic/elasticsearch/pull/138715)
* Fix multi fields in downsampling [#138869](https://github.com/elastic/elasticsearch/pull/138869)

ES|QL:
* Do not pack non-dimension fields in TS [#138929](https://github.com/elastic/elasticsearch/pull/138929)
* Fix columns ordering when pruning an INLINE STATS [#136827](https://github.com/elastic/elasticsearch/pull/136827) (issue: [#136797](https://github.com/elastic/elasticsearch/issues/136797))
* Fix enrich and lookup join resolution based on min transport version [#137431](https://github.com/elastic/elasticsearch/pull/137431)
* Fixes esql class cast bug in STATS at planning level [#137511](https://github.com/elastic/elasticsearch/pull/137511) (issues: [#133992](https://github.com/elastic/elasticsearch/issues/133992), [#136598](https://github.com/elastic/elasticsearch/issues/136598))
* [ES|QL] Compare query builders using identity [#139080](https://github.com/elastic/elasticsearch/pull/139080)

Inference:
* [Inference API] Use dimensions field in JinaAI `text_embedding` requests [#139413](https://github.com/elastic/elasticsearch/pull/139413)

Infra/Core:
* GET /_migration/deprecations doesn't check disk watermarks against correct settings values [#138115](https://github.com/elastic/elasticsearch/pull/138115) (issue: [#137005](https://github.com/elastic/elasticsearch/issues/137005))

Machine Learning:
* Correctly handle empty inputs in `chunkedInfer()` [#138632](https://github.com/elastic/elasticsearch/pull/138632)

Mapping:
* Fix offset maths bug in `InetAddress` parsing [#139420](https://github.com/elastic/elasticsearch/pull/139420)

Search:
* Added logic for individual shard failure handling for `CompoundRetrieverBuilder` and fixed how partial search results flag is passed through to `CompoundRetrieverBuilder` [#136732](https://github.com/elastic/elasticsearch/pull/136732)
* Speed up `LeafCollector#setScorer` in `TopHitsAggregator` [#138883](https://github.com/elastic/elasticsearch/pull/138883)

Security:
* More reliable trigger for security index migration [#139028](https://github.com/elastic/elasticsearch/pull/139028)

Stats:
* Improving performance of stats APIs when the number of shards is very large [#138126](https://github.com/elastic/elasticsearch/pull/138126) (issue: [#97222](https://github.com/elastic/elasticsearch/issues/97222))

Vector Search:
* Disallow index types updates to bbq_disk, revert [#139061](https://github.com/elastic/elasticsearch/pull/139061)
