<!-- Part 11 of 18 of release-notes/index.md (split because the page is big). -->

## 9.2.1 [elasticsearch-9.2.1-release-notes]

### Features and enhancements [elasticsearch-9.2.1-features-enhancements]

Authorization:
* [Sentinel One] Add `manage`, `create_index`, `read`, `index`, `write`, `delete`, permission for third-party agent indices in the `Kibana system` to support the threat event data stream. [#137222](https://github.com/elastic/elasticsearch/pull/137222) (issue: [#240901](https://github.com/elastic/elasticsearch/issues/240901))

ES|QL:
* Enable new data types with created version [#136327](https://github.com/elastic/elasticsearch/pull/136327)

ILM+SLM:
* Allow opting out of force-merging on a cloned index in ILM's searchable snapshot action [#137375](https://github.com/elastic/elasticsearch/pull/137375)

Infra/Core:
* Upgrade ASM to 9.9 [#136963](https://github.com/elastic/elasticsearch/pull/136963)

Infra/Plugins:
* Error if installed plugin is inside plugins folder [#137398](https://github.com/elastic/elasticsearch/pull/137398) (issue: [#27401](https://github.com/elastic/elasticsearch/issues/27401))

Packaging:
* Update bundled JDK to Java 25.0.1+8 [#137640](https://github.com/elastic/elasticsearch/pull/137640)

Search:
* Adjust GPU graph building params [#137074](https://github.com/elastic/elasticsearch/pull/137074)


### Fixes [elasticsearch-9.2.1-fixes]

Aggregations:
* Reject invalid `reverse_nested` aggs [#137047](https://github.com/elastic/elasticsearch/pull/137047)

Allocation:
* Allow allocating clones over low watermark [#137399](https://github.com/elastic/elasticsearch/pull/137399)
* Handle indices with zero/missing uptime correctly in write-load calculation [#136929](https://github.com/elastic/elasticsearch/pull/136929)

Authorization:
* Grants `kibana_system` the ability to forcemerge certain indices [#135795](https://github.com/elastic/elasticsearch/pull/135795)
* Handle ._original stored fields with fls [#137442](https://github.com/elastic/elasticsearch/pull/137442)

Data streams:
* Taking additional settings providers into account for data stream effective settings [#137407](https://github.com/elastic/elasticsearch/pull/137407) (issue: [#137381](https://github.com/elastic/elasticsearch/issues/137381))

ES|QL:
* ESQL: Fix double release in inline stats when `LocalRelation` is reused [#136467](https://github.com/elastic/elasticsearch/pull/136467) (issue: [#135679](https://github.com/elastic/elasticsearch/issues/135679))
* ESQL: Fix lookup join filter pushdown to use semantic equality [#136818](https://github.com/elastic/elasticsearch/pull/136818) (issue: [#136599](https://github.com/elastic/elasticsearch/issues/136599))
* Extends constant MVs handling with warnings to general binary comparisons [#137387](https://github.com/elastic/elasticsearch/pull/137387)
* Fix `ReplaceAliasingEvalWithProject` in case of shadowing [#137025](https://github.com/elastic/elasticsearch/pull/137025) (issue: [#137019](https://github.com/elastic/elasticsearch/issues/137019))
* Fix handling equality with MV constants properly [#137032](https://github.com/elastic/elasticsearch/pull/137032) (issues: [#136998](https://github.com/elastic/elasticsearch/issues/136998), [#136939](https://github.com/elastic/elasticsearch/issues/136939))
* Make equals include ids for Alias, `TypedAttribute` [#132455](https://github.com/elastic/elasticsearch/pull/132455) (issues: [#131509](https://github.com/elastic/elasticsearch/issues/131509), [#132634](https://github.com/elastic/elasticsearch/issues/132634))
* Return `ConstNullBlock` in `FromAggMetricDouble` [#136773](https://github.com/elastic/elasticsearch/pull/136773)
* Return a better error message when Timestamp is renamed in TS queries [#136231](https://github.com/elastic/elasticsearch/pull/136231) (issue: [#134994](https://github.com/elastic/elasticsearch/issues/134994))

Geo:
* Fix `ignore_unmapped` setting when using `geo_shape` query with a pre-indexed shape [#136961](https://github.com/elastic/elasticsearch/pull/136961) (issue: [#136954](https://github.com/elastic/elasticsearch/issues/136954))

ILM+SLM:
* Remove `auto_expand_replicas` setting during index clone in `searchable_snapshot` [#137111](https://github.com/elastic/elasticsearch/pull/137111)

Indices APIs:
* Fix mapping conflicts in clone/split/shrink APIs [#137096](https://github.com/elastic/elasticsearch/pull/137096)
* Reindex-from-remote: Fail on manual slicing param [#137275](https://github.com/elastic/elasticsearch/pull/137275) (issue: [#136269](https://github.com/elastic/elasticsearch/issues/136269))

Infra/Node Lifecycle:
* Start readiness service after http is started [#136729](https://github.com/elastic/elasticsearch/pull/136729)

Ingest Node:
* Fix illegal_access_exception: class com.maxmind.db.Decoder from `ip_location` processor [#137479](https://github.com/elastic/elasticsearch/pull/137479)
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
* Disallow `max_inner_product`, swap `dot_product` for `cosine` for int8_hnsw GPU type [#136881](https://github.com/elastic/elasticsearch/pull/136881)
* Make `MutableSearchResponse` ref-counted to prevent use-after-close in async search [#134359](https://github.com/elastic/elasticsearch/pull/134359)
* Remove early phase failure in batched [#136889](https://github.com/elastic/elasticsearch/pull/136889) (issue: [#134151](https://github.com/elastic/elasticsearch/issues/134151))

TSDB:
* Enable `_otlp` usage with `create_doc`, `auto_configure` privileges [#137325](https://github.com/elastic/elasticsearch/pull/137325)

Vector Search:
* Use Suppliers To Get Inference Results In Semantic Queries [#136720](https://github.com/elastic/elasticsearch/pull/136720) (issue: [#136621](https://github.com/elastic/elasticsearch/issues/136621))




## 9.1.6 [elasticsearch-9.1.6-release-notes]

### Features and enhancements [elasticsearch-9.1.6-features-enhancements]

Authorization:
* Lazy compute and cache `grantsAll` per privilege [#136684](https://github.com/elastic/elasticsearch/pull/136684)

Infra/Core:
* Use java8 variant of apm-agent [#132651](https://github.com/elastic/elasticsearch/pull/132651)


### Fixes [elasticsearch-9.1.6-fixes]

Authorization:
* Drop project-id from threadcontext for CCS [#136664](https://github.com/elastic/elasticsearch/pull/136664)

ES|QL:
* Make `ResolveUnionTypes` rule stateless [#136492](https://github.com/elastic/elasticsearch/pull/136492)

Indices APIs:
* Reindex-from-remote: Validate basic auth params [#136501](https://github.com/elastic/elasticsearch/pull/136501) (issue: [#135925](https://github.com/elastic/elasticsearch/issues/135925))

Logs:
* Fix logsdb settings provider mapping filters [#136119](https://github.com/elastic/elasticsearch/pull/136119) (issue: [#136107](https://github.com/elastic/elasticsearch/issues/136107))

Machine Learning:
* Adjust jinaai rerank response parser to handle document field as string or object [#136751](https://github.com/elastic/elasticsearch/pull/136751)
* Clean up inference indices on failed endpoint creation [#136577](https://github.com/elastic/elasticsearch/pull/136577) (issue: [#123726](https://github.com/elastic/elasticsearch/issues/123726))
* Cohere service Model Id field is required [#136017](https://github.com/elastic/elasticsearch/pull/136017)
* Ensure queued `AbstractRunnables` are notified when executor stops [#135966](https://github.com/elastic/elasticsearch/pull/135966) (issue: [#134651](https://github.com/elastic/elasticsearch/issues/134651))
* Release cluster state [#136769](https://github.com/elastic/elasticsearch/pull/136769) (issue: [#123243](https://github.com/elastic/elasticsearch/issues/123243))

Mapping:
* Store full path in `_ignored` when ignoring dynamic array field [#136315](https://github.com/elastic/elasticsearch/pull/136315)

Search:
* Initialize `TermsEnum` eagerly [#136279](https://github.com/elastic/elasticsearch/pull/136279)

Security:
* Configurable HTTP read and connect timeouts for url based SAML metadata resolution [#136058](https://github.com/elastic/elasticsearch/pull/136058)
* Optimize Index Permission Automatons for Has Privileges [#136625](https://github.com/elastic/elasticsearch/pull/136625)

Transform:
* Allow dynamic updates to frequency [#136757](https://github.com/elastic/elasticsearch/pull/136757) (issue: [#133321](https://github.com/elastic/elasticsearch/issues/133321))

Vector Search:
* Cardinality Aggregator Throws `UnsupportedOperationException` When Field Type is Vector [#135994](https://github.com/elastic/elasticsearch/pull/135994)
