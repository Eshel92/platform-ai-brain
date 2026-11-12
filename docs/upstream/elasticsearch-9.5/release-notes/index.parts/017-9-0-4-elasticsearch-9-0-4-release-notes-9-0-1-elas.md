<!-- Part 17 of 18 of release-notes/index.md (split because the page is big). -->

## 9.0.4 [elasticsearch-9.0.4-release-notes]

### Fixes [elasticsearch-9.0.4-fixes]

Aggregations:
* Aggs: Add cancellation checks to `FilterByFilter` aggregator [#130452](https://github.com/elastic/elasticsearch/pull/130452)

Distributed:
* Drain responses on completion for `TransportNodesAction` [#130303](https://github.com/elastic/elasticsearch/pull/130303)

ES|QL:
* Avoid O(N^2) in VALUES with ordinals grouping [#130576](https://github.com/elastic/elasticsearch/pull/130576)
* Avoid dropping aggregate groupings in local plans [#129370](https://github.com/elastic/elasticsearch/pull/129370) (issues: [#129811](https://github.com/elastic/elasticsearch/issues/129811), [#128054](https://github.com/elastic/elasticsearch/issues/128054))
* Fix `BytesRef2BlockHash` [#130705](https://github.com/elastic/elasticsearch/pull/130705)
* Fix wildcard drop after lookup join [#130448](https://github.com/elastic/elasticsearch/pull/130448) (issue: [#129561](https://github.com/elastic/elasticsearch/issues/129561))

Infra/Core:
* Reverse disordered-version warning message [#129904](https://github.com/elastic/elasticsearch/pull/129904)

Machine Learning:
* Check for model deployment in inference endpoints before stopping [#129325](https://github.com/elastic/elasticsearch/pull/129325) (issue: [#128549](https://github.com/elastic/elasticsearch/issues/128549))
* Fix timeout bug in DBQ deletion of unused and orphan ML data [#130083](https://github.com/elastic/elasticsearch/pull/130083)
* Including `max_tokens` through the Service API for Anthropic [#131113](https://github.com/elastic/elasticsearch/pull/131113)

Mapping:
* Make flattened synthetic source concatenate object keys on scalar/object mismatch [#129600](https://github.com/elastic/elasticsearch/pull/129600) (issue: [#122936](https://github.com/elastic/elasticsearch/issues/122936))

Relevance:
* Fix: `GET _synonyms` returns synonyms with empty rules [#131032](https://github.com/elastic/elasticsearch/pull/131032)

Search:
* Check field data type before casting when applying geo distance sort [#130924](https://github.com/elastic/elasticsearch/pull/130924) (issue: [#129500](https://github.com/elastic/elasticsearch/issues/129500))
* Fix msearch request parsing when index expression is null [#130776](https://github.com/elastic/elasticsearch/pull/130776) (issue: [#129631](https://github.com/elastic/elasticsearch/issues/129631))
* Fix text similarity reranker does not propagate min score correctly [#129223](https://github.com/elastic/elasticsearch/pull/129223)
* Throw a 400 when sorting for all types of range fields [#129725](https://github.com/elastic/elasticsearch/pull/129725)
* Trim to size lists created in source fetchers [#130521](https://github.com/elastic/elasticsearch/pull/130521)

Vector Search:
* Fix knn search error when dimensions are not set [#131081](https://github.com/elastic/elasticsearch/pull/131081) (issue: [#129550](https://github.com/elastic/elasticsearch/issues/129550))




## 9.0.3 [elasticsearch-9.0.3-release-notes]

### Features and enhancements [elasticsearch-9.0.3-features-enhancements]

Authorization:
* Fix unsupported privileges error message during role and API key creation [#129158](https://github.com/elastic/elasticsearch/pull/129158) (issue: [#128132](https://github.com/elastic/elasticsearch/issues/128132))

Engine:
* Threadpool merge executor is aware of available disk space [#127613](https://github.com/elastic/elasticsearch/pull/127613)
* Threadpool merge scheduler [#120869](https://github.com/elastic/elasticsearch/pull/120869)

Ingest Node:
* Update traces duration mappings with appropriate unit type [#129418](https://github.com/elastic/elasticsearch/pull/129418)

Snapshot/Restore:
* Update shardGenerations for all indices on snapshot finalization [#128650](https://github.com/elastic/elasticsearch/pull/128650) (issue: [#108907](https://github.com/elastic/elasticsearch/issues/108907))

Stats:
* Optimize sparse vector stats collection [#128740](https://github.com/elastic/elasticsearch/pull/128740)


### Fixes [elasticsearch-9.0.3-fixes]

Aggregations:
* Aggs: Fix significant terms not finding background docuemnts for nested fields [#128472](https://github.com/elastic/elasticsearch/pull/128472) (issue: [#101163](https://github.com/elastic/elasticsearch/issues/101163))

Authorization:
* Prevent invalid privileges in manage roles privilege [#128532](https://github.com/elastic/elasticsearch/pull/128532) (issue: [#127496](https://github.com/elastic/elasticsearch/issues/127496))

CCS:
* Handle the indices pattern `["*", "-*"]` when grouping indices by cluster name [#128610](https://github.com/elastic/elasticsearch/pull/128610)

ES|QL:
* Fix `FieldAttribute` name usage in `InferNonNullAggConstraint` [#128910](https://github.com/elastic/elasticsearch/pull/128910)
* Fix case insensitive comparisons to "" [#127532](https://github.com/elastic/elasticsearch/pull/127532) (issue: [#127431](https://github.com/elastic/elasticsearch/issues/127431))
* Support DATE_NANOS in LOOKUP JOIN [#127962](https://github.com/elastic/elasticsearch/pull/127962) (issue: [#127249](https://github.com/elastic/elasticsearch/issues/127249))
* Throw ISE instead of IAE for illegal block in page [#128960](https://github.com/elastic/elasticsearch/pull/128960)

IdentityProvider:
* Improve cache invalidation in IdP SP cache [#128890](https://github.com/elastic/elasticsearch/pull/128890)

Indices APIs:
* Avoid unnecessary determinization in index pattern conflict checks [#128362](https://github.com/elastic/elasticsearch/pull/128362)

Infra/Core:
* Update AbstractXContentParser to support parsers that don't provide text characters [#129005](https://github.com/elastic/elasticsearch/pull/129005)

Infra/Plugins:
* Add complete attribute to .fleet-agents docs [#127651](https://github.com/elastic/elasticsearch/pull/127651)

Machine Learning:
* Account for Java direct memory on machine learning nodes to prevent out-of-memory crashes. [#128742](https://github.com/elastic/elasticsearch/pull/128742)
* Ensure that anomaly detection job state update retries if master node is temoporarily unavailable [#129391](https://github.com/elastic/elasticsearch/pull/129391) (issue: [#126148](https://github.com/elastic/elasticsearch/issues/126148))
* Prevent ML data retention logic from failing when deleting documents in read-only indices [#125408](https://github.com/elastic/elasticsearch/pull/125408)

Mapping:
* Check prefixes when constructing synthetic source for flattened fields [#129580](https://github.com/elastic/elasticsearch/pull/129580) (issue: [#129508](https://github.com/elastic/elasticsearch/issues/129508))

Search:
* Fix NPE in semantic highlighter [#128989](https://github.com/elastic/elasticsearch/pull/128989) (issue: [#128975](https://github.com/elastic/elasticsearch/issues/128975))
* Fix inner hits + aggregations concurrency bug [#128036](https://github.com/elastic/elasticsearch/pull/128036) (issue: [#122419](https://github.com/elastic/elasticsearch/issues/122419))
* Fix minmax normalizer handling of single-doc result sets [#128689](https://github.com/elastic/elasticsearch/pull/128689)
* Fix missing highlighting in `match_all` queries for `semantic_text` fields [#128702](https://github.com/elastic/elasticsearch/pull/128702)

Searchable Snapshots:
* Adjust unpromotable shard refresh request validation to allow `RefreshResult.NO_REFRESH` [#129176](https://github.com/elastic/elasticsearch/pull/129176) (issue: [#129036](https://github.com/elastic/elasticsearch/issues/129036))

Security:
* Fix error message when changing the password for a user in the file realm [#127621](https://github.com/elastic/elasticsearch/pull/127621)




## 9.0.2 [elasticsearch-9.0.2-release-notes]

### Features and enhancements [elasticsearch-9.0.2-features-enhancements]

Authentication:
* Http proxy support in JWT realm [#127337](https://github.com/elastic/elasticsearch/pull/127337) (issue: [#114956](https://github.com/elastic/elasticsearch/issues/114956))

ES|QL:
* Limit Replace function memory usage [#127924](https://github.com/elastic/elasticsearch/pull/127924)


### Fixes [elasticsearch-9.0.2-fixes]

Aggregations:
* Fix a bug in `significant_terms` [#127975](https://github.com/elastic/elasticsearch/pull/127975)

Audit:
* Handle streaming request body in audit log [#127798](https://github.com/elastic/elasticsearch/pull/127798)

Codec:
* Use new source loader when lower `docId` is accessed [#128320](https://github.com/elastic/elasticsearch/pull/128320)

Data streams:
* Fix system data streams incorrectly showing up in the list of template validation problems [#128161](https://github.com/elastic/elasticsearch/pull/128161)

Downsampling:
* Downsampling does not consider passthrough fields as dimensions [#127752](https://github.com/elastic/elasticsearch/pull/127752) (issue: [#125156](https://github.com/elastic/elasticsearch/issues/125156))

ES|QL:
* Consider inlinestats when having `field_caps` check for field names [#127564](https://github.com/elastic/elasticsearch/pull/127564) (issue: [#127236](https://github.com/elastic/elasticsearch/issues/127236))
* Don't push down filters on the right hand side of an inlinejoin [#127383](https://github.com/elastic/elasticsearch/pull/127383)
* ESQL: Avoid unintended attribute removal [#127563](https://github.com/elastic/elasticsearch/pull/127563) (issue: [#127468](https://github.com/elastic/elasticsearch/issues/127468))
* ESQL: Fix alias removal in regex extraction with JOIN [#127687](https://github.com/elastic/elasticsearch/pull/127687) (issue: [#127467](https://github.com/elastic/elasticsearch/issues/127467))
* ESQL: Keep `DROP` attributes when resolving field names [#127009](https://github.com/elastic/elasticsearch/pull/127009) (issue: [#126418](https://github.com/elastic/elasticsearch/issues/126418))
* Ensure ordinal builder emit ordinal blocks [#127949](https://github.com/elastic/elasticsearch/pull/127949)
* Fix union types in CCS [#128111](https://github.com/elastic/elasticsearch/pull/128111)
* Fix validation NPE in Enrich and add extra @Nullable annotations [#128260](https://github.com/elastic/elasticsearch/pull/128260) (issues: [#126297](https://github.com/elastic/elasticsearch/issues/126297), [#126253](https://github.com/elastic/elasticsearch/issues/126253))

Geo:
* Added geometry validation for GEO types to exit early on invalid latitudes [#128259](https://github.com/elastic/elasticsearch/pull/128259) (issue: [#128234](https://github.com/elastic/elasticsearch/issues/128234))

Infra/Core:
* Add missing `outbound_network` entitlement to x-pack-core [#126992](https://github.com/elastic/elasticsearch/pull/126992) (issue: [#127003](https://github.com/elastic/elasticsearch/issues/127003))
* Check hidden frames in entitlements [#127877](https://github.com/elastic/elasticsearch/pull/127877)

Infra/Scripting:
* Avoid nested docs in painless execute api [#127991](https://github.com/elastic/elasticsearch/pull/127991) (issue: [#41004](https://github.com/elastic/elasticsearch/issues/41004))

Machine Learning:
* Append all data to Chat Completion buffer [#127658](https://github.com/elastic/elasticsearch/pull/127658)
* Fix services API Google Vertex AI Rerank location field requirement [#127856](https://github.com/elastic/elasticsearch/pull/127856)
* Pass timeout to chat completion [#128338](https://github.com/elastic/elasticsearch/pull/128338)
* Use internal user for internal inference action [#128327](https://github.com/elastic/elasticsearch/pull/128327)

Relevance:
* Fix: Add `NamedWriteable` for `RuleQueryRankDoc` [#128153](https://github.com/elastic/elasticsearch/pull/128153) (issue: [#126071](https://github.com/elastic/elasticsearch/issues/126071))

Security:
* Remove dangling spaces wherever found [#127475](https://github.com/elastic/elasticsearch/pull/127475)

Snapshot/Restore:
* Add missing entitlement to `repository-azure` [#128047](https://github.com/elastic/elasticsearch/pull/128047) (issue: [#128046](https://github.com/elastic/elasticsearch/issues/128046))

TSDB:
* Skip the validation when retrieving the index mode during reindexing a time series data stream [#127824](https://github.com/elastic/elasticsearch/pull/127824)

Vector Search:
* [9.x] Revert "Enable madvise by default for all builds" [#127921](https://github.com/elastic/elasticsearch/pull/127921)




## 9.0.1 [elasticsearch-9.0.1-release-notes]

### Features and enhancements [elasticsearch-9.0.1-features-enhancements]

Infra/Core:
* Validation checks on paths allowed for 'files' entitlements. Restrict the paths we allow access to, forbidding plugins to specify/request entitlements for reading or writing to specific protected directories. [#126852](https://github.com/elastic/elasticsearch/pull/126852)

Ingest Node:
* Updating tika to 2.9.3 [#127353](https://github.com/elastic/elasticsearch/pull/127353)

Search:
* Enable sort optimization on float and `half_float` [#126342](https://github.com/elastic/elasticsearch/pull/126342)

Security:
* Add Issuer to failed SAML Signature validation logs when available [#126310](https://github.com/elastic/elasticsearch/pull/126310) (issue: [#111022](https://github.com/elastic/elasticsearch/issues/111022))


### Fixes [elasticsearch-9.0.1-fixes]

Aggregations:
* Rare terms aggregation false **positive** fix [#126884](https://github.com/elastic/elasticsearch/pull/126884)

Allocation:
* Fix shard size of initializing restored shard [#126783](https://github.com/elastic/elasticsearch/pull/126783) (issue: [#105331](https://github.com/elastic/elasticsearch/issues/105331))

CCS:
* Cancel expired async search task when a remote returns its results [#126583](https://github.com/elastic/elasticsearch/pull/126583)

Data streams:
* [otel-data] Bump plugin version to release _metric_names_hash changes [#126850](https://github.com/elastic/elasticsearch/pull/126850)

ES|QL:
* Fix count optimization with pushable union types [#127225](https://github.com/elastic/elasticsearch/pull/127225) (issue: [#127200](https://github.com/elastic/elasticsearch/issues/127200))
* Fix join masking eval [#126614](https://github.com/elastic/elasticsearch/pull/126614)
* Fix sneaky bug in single value query [#127146](https://github.com/elastic/elasticsearch/pull/127146)
* No, line noise isn't a valid ip [#127527](https://github.com/elastic/elasticsearch/pull/127527)

ILM+SLM:
* Fix equality bug in `WaitForIndexColorStep` [#126605](https://github.com/elastic/elasticsearch/pull/126605)

Infra/CLI:
* Use terminal reader in keystore add command [#126729](https://github.com/elastic/elasticsearch/pull/126729) (issue: [#98115](https://github.com/elastic/elasticsearch/issues/98115))

Infra/Core:
* Fix: consider case sensitiveness differences in Windows/Unix-like filesystems for files entitlements [#126990](https://github.com/elastic/elasticsearch/pull/126990) (issue: [#127047](https://github.com/elastic/elasticsearch/issues/127047))
* Rework uniquify to not use iterators [#126889](https://github.com/elastic/elasticsearch/pull/126889) (issue: [#126883](https://github.com/elastic/elasticsearch/issues/126883))
* Workaround max name limit imposed by Jackson 2.17 [#126806](https://github.com/elastic/elasticsearch/pull/126806)

Machine Learning:
* Adding missing `onFailure` call for Inference API start model request [#126930](https://github.com/elastic/elasticsearch/pull/126930)
* Fix text structure NPE when fields in list have null value [#125922](https://github.com/elastic/elasticsearch/pull/125922)
* Leverage threadpool schedule for inference api to avoid long running thread [#126858](https://github.com/elastic/elasticsearch/pull/126858) (issue: [#126853](https://github.com/elastic/elasticsearch/issues/126853))

Ranking:
* Fix LTR rescorer with model alias [#126273](https://github.com/elastic/elasticsearch/pull/126273)
* LTR score bounding [#125694](https://github.com/elastic/elasticsearch/pull/125694)

Search:
* Fix npe when using source confirmed text query against missing field [#127414](https://github.com/elastic/elasticsearch/pull/127414)

TSDB:
* Improve resiliency of `UpdateTimeSeriesRangeService` [#126637](https://github.com/elastic/elasticsearch/pull/126637)

Task Management:
* Fix race condition in `RestCancellableNodeClient` [#126686](https://github.com/elastic/elasticsearch/pull/126686) (issue: [#88201](https://github.com/elastic/elasticsearch/issues/88201))

Vector Search:
* Fix `vec_caps` to test for OS support too (on x64) [#126911](https://github.com/elastic/elasticsearch/pull/126911) (issue: [#126809](https://github.com/elastic/elasticsearch/issues/126809))
* Fix bbq quantization algorithm but for differently distributed components [#126778](https://github.com/elastic/elasticsearch/pull/126778)
