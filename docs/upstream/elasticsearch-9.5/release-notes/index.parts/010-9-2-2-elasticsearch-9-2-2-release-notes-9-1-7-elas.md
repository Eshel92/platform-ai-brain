<!-- Part 10 of 18 of release-notes/index.md (split because the page is big). -->

## 9.2.2 [elasticsearch-9.2.2-release-notes]

### Features and enhancements [elasticsearch-9.2.2-features-enhancements]

Authorization:
* [IRONSCALES] Add `manage`, `create_index`, `read`, `index`, `write`, `delete`, permission for third party agent indices `kibana_system` [#138094](https://github.com/elastic/elasticsearch/pull/138094) (issue: [#138093](https://github.com/elastic/elasticsearch/issues/138093))

ES|QL:
* Do not calculate query plan diff when not needed [#137721](https://github.com/elastic/elasticsearch/pull/137721)

Security:
* Upgrade UnboundID LDAP SDK to 7.0.3 [#138053](https://github.com/elastic/elasticsearch/pull/138053)

Snapshot/Restore:
* Upgrading commons-lang3 version for repository-hdfs plugin [#138589](https://github.com/elastic/elasticsearch/pull/138589)

Vector Search:
* Use IVF_PQ for GPU index build for large datasets [#137126](https://github.com/elastic/elasticsearch/pull/137126)


### Fixes [elasticsearch-9.2.2-fixes]

Aggregations:
* Break on `FieldData` when building global ordinals [#108875](https://github.com/elastic/elasticsearch/pull/108875) (issue: [#97075](https://github.com/elastic/elasticsearch/issues/97075))

Data streams:
* Fixing get data stream API when data stream index mode has been changed to `time_series` [#137852](https://github.com/elastic/elasticsearch/pull/137852)
* Prevent passing a pipeline to a logs stream bulk index request body [#137992](https://github.com/elastic/elasticsearch/pull/137992)

Downsampling:
* Fix: Downsample returns appropriate error when target index gets deleted unexpectedly. [#138228](https://github.com/elastic/elasticsearch/pull/138228)

ES|QL:
* ES|QL - Full text functions accept null as field parameter [#137430](https://github.com/elastic/elasticsearch/pull/137430) (issue: [#136608](https://github.com/elastic/elasticsearch/issues/136608))
* Fix StringIndexOutOfBoundsException in COMPLETION command when options are omitted. [#138363](https://github.com/elastic/elasticsearch/pull/138363) (issue: [#138361](https://github.com/elastic/elasticsearch/issues/138361))
* Fix integer overflow in block memory estimation [#138132](https://github.com/elastic/elasticsearch/pull/138132)
* Handle index deletion while querying in ES|QL [#137702](https://github.com/elastic/elasticsearch/pull/137702) (issue: [#135863](https://github.com/elastic/elasticsearch/issues/135863))
* Handle serialization of null blocks in `AggregateMetricDoubleBlock` [#138539](https://github.com/elastic/elasticsearch/pull/138539)

ILM+SLM:
* ILM Explain: valid JSON on truncated step info [#137638](https://github.com/elastic/elasticsearch/pull/137638) (issue: [#135458](https://github.com/elastic/elasticsearch/issues/135458))

Indices APIs:
* Serverless filtering create from [#137850](https://github.com/elastic/elasticsearch/pull/137850)

Infra/Core:
* Fix for GET /_migration/deprecations doesn't check deprecated affix settings correctly [#137976](https://github.com/elastic/elasticsearch/pull/137976) (issue: [#137008](https://github.com/elastic/elasticsearch/issues/137008))
* Fix for GET /_migration/deprecations doesn't report node deprecations if low watermark exceeded and GET /_migration/deprecations doesn't report node-level failures properly [#137964](https://github.com/elastic/elasticsearch/pull/137964) (issues: [#137010](https://github.com/elastic/elasticsearch/issues/137010), [#137004](https://github.com/elastic/elasticsearch/issues/137004))

Infra/Settings:
* Fix default value for some settings when filtered [#137652](https://github.com/elastic/elasticsearch/pull/137652) (issue: [#136333](https://github.com/elastic/elasticsearch/issues/136333))
* Restore API: Fix file settings handling [#137585](https://github.com/elastic/elasticsearch/pull/137585) (issue: [#122429](https://github.com/elastic/elasticsearch/issues/122429))

Ingest Node:
* Change `DatabaseNodeService` error logs to warnings [#138438](https://github.com/elastic/elasticsearch/pull/138438)
* Handle individual doc parsing failure in bulk request with pipeline [#138624](https://github.com/elastic/elasticsearch/pull/138624) (issue: [#138445](https://github.com/elastic/elasticsearch/issues/138445))
* Improve concurrency design of `GeoIpDownloader` [#137660](https://github.com/elastic/elasticsearch/pull/137660) (issues: [#135158](https://github.com/elastic/elasticsearch/issues/135158), [#130681](https://github.com/elastic/elasticsearch/issues/130681), [#135132](https://github.com/elastic/elasticsearch/issues/135132), [#133597](https://github.com/elastic/elasticsearch/issues/133597))

Machine Learning:
* Add validation for updating `num_threads` [#138122](https://github.com/elastic/elasticsearch/pull/138122) (issue: [#137129](https://github.com/elastic/elasticsearch/issues/137129))
* Bump anomalies index template version to install latest [#138097](https://github.com/elastic/elasticsearch/pull/138097)
* Fix ML calendar event update scalability issues [#136886](https://github.com/elastic/elasticsearch/pull/136886)
* Fix parsing of Google Model Garden Anthropic `message_start` event during `chat_completion` operation [#137926](https://github.com/elastic/elasticsearch/pull/137926)

Mapping:
* Fix `index.mapping.pattern_text.disable_templating` not registered issue [#138265](https://github.com/elastic/elasticsearch/pull/138265)
* Reject mappings that (eventually) set dimension and metric in the same field [#138308](https://github.com/elastic/elasticsearch/pull/138308)

Network:
* Convert `BytesTransportResponse` when proxying response from/to local node [#135873](https://github.com/elastic/elasticsearch/pull/135873)

Relevance:
* Fix semantic highlighting when using a `knn` query with minimum `similarity` and when using `bbq_disk` [#138140](https://github.com/elastic/elasticsearch/pull/138140)

Search:
* Fix Bug in `RankDocRetrieverBuilder` when `from` is set to Default (-1) [#137637](https://github.com/elastic/elasticsearch/pull/137637)
* Fix: add missing `vector_similarity_support` in InferenceFeatures [#138644](https://github.com/elastic/elasticsearch/pull/138644)
* Handle Query Timeouts During Collector Initialization in `QueryPhase` [#138084](https://github.com/elastic/elasticsearch/pull/138084)
* [LTR] Fix feature display order when using explain [#137671](https://github.com/elastic/elasticsearch/pull/137671)

Security:
* Principal Extraction from Certificate RDN Attribute Value in PKI Realm [#137230](https://github.com/elastic/elasticsearch/pull/137230)

Snapshot/Restore:
* Add length validation for `rename_replacement` parameter in snapshot restore request [#137859](https://github.com/elastic/elasticsearch/pull/137859)

TSDB:
* OTLP: return correct response type for partial successes [#137718](https://github.com/elastic/elasticsearch/pull/137718)

Vector Search:
* Fixing sorted indices for GPU built indices [#138138](https://github.com/elastic/elasticsearch/pull/138138)
* Update to Lucene 10.3.2 [#138230](https://github.com/elastic/elasticsearch/pull/138230) (issue: [#135718](https://github.com/elastic/elasticsearch/issues/135718))
* [Vector Search] Fix  wrong vector docvalue_fields [#137862](https://github.com/elastic/elasticsearch/pull/137862)




## 9.1.8 [elasticsearch-9.1.8-release-notes]

### Features and enhancements [elasticsearch-9.1.8-features-enhancements]

Authorization:
* [IRONSCALES] Add `manage`, `create_index`, `read`, `index`, `write`, `delete`, permission for third party agent indices `kibana_system` [#138094](https://github.com/elastic/elasticsearch/pull/138094) (issue: [#138093](https://github.com/elastic/elasticsearch/issues/138093))

Security:
* Upgrade UnboundID LDAP SDK to 7.0.3 [#138053](https://github.com/elastic/elasticsearch/pull/138053)

Snapshot/Restore:
* Upgrading commons-lang3 version for repository-hdfs plugin [#138589](https://github.com/elastic/elasticsearch/pull/138589)


### Fixes [elasticsearch-9.1.8-fixes]

Aggregations:
* Break on `FieldData` when building global ordinals [#108875](https://github.com/elastic/elasticsearch/pull/108875) (issue: [#97075](https://github.com/elastic/elasticsearch/issues/97075))

Downsampling:
* Fix: Downsample returns appropriate error when target index gets deleted unexpectedly. [#138228](https://github.com/elastic/elasticsearch/pull/138228)

ES|QL:
* Fix integer overflow in block memory estimation [#138132](https://github.com/elastic/elasticsearch/pull/138132)
* Handle index deletion while querying in ES|QL [#137702](https://github.com/elastic/elasticsearch/pull/137702) (issue: [#135863](https://github.com/elastic/elasticsearch/issues/135863))

ILM+SLM:
* ILM Explain: valid JSON on truncated step info [#137638](https://github.com/elastic/elasticsearch/pull/137638) (issue: [#135458](https://github.com/elastic/elasticsearch/issues/135458))

Indices APIs:
* Serverless filtering create from [#137850](https://github.com/elastic/elasticsearch/pull/137850)

Infra/Core:
* Fix for GET /_migration/deprecations doesn't check deprecated affix settings correctly [#137976](https://github.com/elastic/elasticsearch/pull/137976) (issue: [#137008](https://github.com/elastic/elasticsearch/issues/137008))

Infra/Settings:
* Fix default value for some settings when filtered [#137652](https://github.com/elastic/elasticsearch/pull/137652) (issue: [#136333](https://github.com/elastic/elasticsearch/issues/136333))
* Restore API: Fix file settings handling [#137585](https://github.com/elastic/elasticsearch/pull/137585) (issue: [#122429](https://github.com/elastic/elasticsearch/issues/122429))

Ingest Node:
* Improve concurrency design of `GeoIpDownloader` [#137660](https://github.com/elastic/elasticsearch/pull/137660) (issues: [#135158](https://github.com/elastic/elasticsearch/issues/135158), [#130681](https://github.com/elastic/elasticsearch/issues/130681), [#135132](https://github.com/elastic/elasticsearch/issues/135132), [#133597](https://github.com/elastic/elasticsearch/issues/133597))

Machine Learning:
* Bump anomalies index template version to install latest [#138097](https://github.com/elastic/elasticsearch/pull/138097)
* Fix ML calendar event update scalability issues [#136886](https://github.com/elastic/elasticsearch/pull/136886)

Mapping:
* Reject mappings that (eventually) set dimension and metric in the same field [#138308](https://github.com/elastic/elasticsearch/pull/138308)

Network:
* Convert `BytesTransportResponse` when proxying response from/to local node [#135873](https://github.com/elastic/elasticsearch/pull/135873)

Relevance:
* Fix semantic highlighting when using a `knn` query with minimum `similarity` [#138140](https://github.com/elastic/elasticsearch/pull/138140)

Search:
* Fix Bug in `RankDocRetrieverBuilder` when `from` is set to Default (-1) [#137637](https://github.com/elastic/elasticsearch/pull/137637)
* Handle Query Timeouts During Collector Initialization in `QueryPhase` [#138084](https://github.com/elastic/elasticsearch/pull/138084)

Security:
* Add User Profile Size Limit Enforced During Profile Updates [#137712](https://github.com/elastic/elasticsearch/pull/137712)
* Principal Extraction from Certificate RDN Attribute Value in PKI Realm [#137230](https://github.com/elastic/elasticsearch/pull/137230)

Snapshot/Restore:
* Add length validation for `rename_replacement` parameter in snapshot restore request [#137859](https://github.com/elastic/elasticsearch/pull/137859)

Vector Search:
* [Vector Search] Fix  wrong vector docvalue_fields [#137862](https://github.com/elastic/elasticsearch/pull/137862)




## 9.1.7 [elasticsearch-9.1.7-release-notes]

### Features and enhancements [elasticsearch-9.1.7-features-enhancements]

Authorization:
* [Cyera] Add `manage`, `create_index`, `read`, `index`, `write`, `delete`, permission for third party agent indices `kibana_system` [#134894](https://github.com/elastic/elasticsearch/pull/134894) (issue: [#134183](https://github.com/elastic/elasticsearch/issues/134183))
* [Sentinel One] Add `manage`, `create_index`, `read`, `index`, `write`, `delete`, permission for third-party agent indices in the `Kibana system` to support the threat event data stream. [#137222](https://github.com/elastic/elasticsearch/pull/137222) (issue: [#240901](https://github.com/elastic/elasticsearch/issues/240901))

Infra/Core:
* Upgrade ASM to 9.9 [#136963](https://github.com/elastic/elasticsearch/pull/136963)

Infra/Plugins:
* Error if installed plugin is inside plugins folder [#137398](https://github.com/elastic/elasticsearch/pull/137398) (issue: [#27401](https://github.com/elastic/elasticsearch/issues/27401))

Packaging:
* Update bundled JDK to Java 25.0.1+8 [#137640](https://github.com/elastic/elasticsearch/pull/137640)


### Fixes [elasticsearch-9.1.7-fixes]

Authorization:
* Grants `kibana_system` the ability to forcemerge certain indices [#135795](https://github.com/elastic/elasticsearch/pull/135795)
* Handle ._original stored fields with fls [#137442](https://github.com/elastic/elasticsearch/pull/137442)

ES|QL:
* Fix `ReplaceAliasingEvalWithProject` in case of shadowing [#137025](https://github.com/elastic/elasticsearch/pull/137025) (issue: [#137019](https://github.com/elastic/elasticsearch/issues/137019))

Geo:
* Fix `ignore_unmapped` setting when using `geo_shape` query with a pre-indexed shape [#136961](https://github.com/elastic/elasticsearch/pull/136961) (issue: [#136954](https://github.com/elastic/elasticsearch/issues/136954))

Indices APIs:
* Reindex-from-remote: Fail on manual slicing param [#137275](https://github.com/elastic/elasticsearch/pull/137275) (issue: [#136269](https://github.com/elastic/elasticsearch/issues/136269))

Infra/Node Lifecycle:
* Start readiness service after http is started [#136729](https://github.com/elastic/elasticsearch/pull/136729)

Ingest Node:
* Improve concurrency design of `EnterpriseGeoIpDownloader` [#134223](https://github.com/elastic/elasticsearch/pull/134223) (issue: [#126124](https://github.com/elastic/elasticsearch/issues/126124))

Machine Learning:
* Do not create inference endpoint if ID is used in existing mappings [#137055](https://github.com/elastic/elasticsearch/pull/137055) (issue: [#124272](https://github.com/elastic/elasticsearch/issues/124272))
* Perform query field validation for rerank task type [#137219](https://github.com/elastic/elasticsearch/pull/137219)

Mapping:
* Fix dropped ignore above fields [#137394](https://github.com/elastic/elasticsearch/pull/137394) (issue: [#137360](https://github.com/elastic/elasticsearch/issues/137360))
* Fixed geo point block loader slowness [#136147](https://github.com/elastic/elasticsearch/pull/136147)

Recovery:
* Catch exceptions from `mapperService` in `StoreRecovery.recoverFromLocalShards` [#137077](https://github.com/elastic/elasticsearch/pull/137077)

Search:
* Make `MutableSearchResponse` ref-counted to prevent use-after-close in async search [#134359](https://github.com/elastic/elasticsearch/pull/134359)
* Remove early phase failure in batched [#136889](https://github.com/elastic/elasticsearch/pull/136889) (issue: [#134151](https://github.com/elastic/elasticsearch/issues/134151))
* [LTR] Fix feature display order when using explain [#137671](https://github.com/elastic/elasticsearch/pull/137671)
