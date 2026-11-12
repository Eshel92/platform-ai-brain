<!-- Part 16 of 18 of release-notes/index.md (split because the page is big). -->

## 9.1.0 [elasticsearch-9.1.0-release-notes]

### Highlights [elasticsearch-9.1.0-highlights]

::::{dropdown} Upgrade `repository-s3` to AWS SDK v2
In earlier versions of Elasticsearch the `repository-s3` plugin was based on the AWS SDK v1. AWS will withdraw support for this SDK before the end of the life of Elasticsearch 9.1 so we have migrated this plugin to the newer AWS SDK v2.
The two SDKs are not quite compatible, so please check the breaking changes documentation and test the new version thoroughly before upgrading any production workloads.
::::

::::{dropdown} Add ability to redirect ingestion failures on data streams to a failure store
Documents that encountered ingest pipeline failures or mapping conflicts
would previously be returned to the client as errors in the bulk and
index operations. Many client applications are not equipped to respond
to these failures. This leads to the failed documents often being
dropped by the client which cannot hold the broken documents
indefinitely. In many end user workloads, these failed documents
represent events that could be critical signals for observability or
security use cases.

To help mitigate this problem, data streams can now maintain a "failure
store" which is used to accept and hold documents that fail to be
ingested due to preventable configuration errors. The data stream's
failure store operates like a separate set of backing indices with their
own mappings and access patterns that allow Elasticsearch to accept
documents that would otherwise be rejected due to unhandled ingest
pipeline exceptions or mapping conflicts.

Users can enable redirection of ingest failures to the failure store on
new data streams by specifying it in the new `data_stream_options` field
inside of a component or index template:

```yaml
PUT _index_template/my-template
{
  "index_patterns": ["logs-test-*"],
  "data_stream": {},
  "template": {
    "data_stream_options": {
      "failure_store": {
        "enabled": true
      }
    }
  }
}
```

Existing data streams can be configured with the new data stream
`_options` endpoint:

```yaml
PUT _data_stream/logs-test-apache/_options
{
  "failure_store": {
    "enabled": "true"
  }
}
```

When redirection is enabled, any ingestion related failures will be
captured in the failure store if the cluster is able to, along with the
timestamp that the failure occurred, details about the error
encountered, and the document that could not be ingested. Since failure
stores are a kind of Elasticsearch index, we can search the data stream
for the failures that it has collected. The failures are not shown by
default as they are stored in different indices than the normal data
stream data. In order to retrieve the failures, we use the `_search` API
along with a new bit of index pattern syntax, the `::` selector.

```yaml
POST logs-test-apache::failures/_search
```

This index syntax informs the search operation to target the indices in
its failure store instead of its backing indices. It can be mixed in a
number of ways with other index patterns to include their failure store
indices in the search operation:

```yaml
POST logs-*::failures/_search
POST logs-*,logs-*::failures/_search
POST *::failures/_search
POST _query
{
  "query": "FROM my_data_stream*::failures"
}
```
::::

::::{dropdown} Mark Token Pruning for Sparse Vector as GA
Token pruning for sparse_vector queries has been live since 8.13 as tech preview.
As of 8.19.0 and 9.1.0, this is now generally available.
::::

::::{dropdown} Upgrade to lucene 10.2.2
* Reduce NeighborArray on-heap memory during HNSW graph building
* Fix IndexSortSortedNumericDocValuesRangeQuery for integer sorting
* ValueSource.fromDoubleValuesSource(dvs).getSortField() would throw errors when used if the DoubleValuesSource needed scores
----
::::

::::{dropdown} Release FORK in tech preview
Fork is a foundational building block that allows multiple branches of execution.
Conceptually, fork is:
- a bifurcation of the stream, with all data going to each fork branch, followed by
- a merge of the branches, enhanced with a discriminator column called FORK:

Example:

```yaml
FROM test
| FORK
( WHERE content:"fox" )
( WHERE content:"dog" )
| SORT _fork
```

The FORK command add a discriminator column called `_fork`:

```yaml
| id  | content   | _fork |
|-----|-----------|-------|
| 3   | brown fox | fork1 |
| 4   | white dog | fork2 |
```
::::

::::{dropdown} ES|QL cross-cluster querying is now generally available
The ES|QL Cross-Cluster querying feature has been in technical preview since 8.13.
As of releases 8.19.0 and 9.1.0 this is now generally available.
This feature allows you to run ES|QL queries across multiple clusters.
::::

### Features and enhancements [elasticsearch-9.1.0-features-enhancements]

Allocation:
* Accumulate compute() calls and iterations between convergences [#126008](https://github.com/elastic/elasticsearch/pull/126008) (issue: [#100850](https://github.com/elastic/elasticsearch/issues/100850))
* Add `FailedShardEntry` info to shard-failed task source string [#125520](https://github.com/elastic/elasticsearch/pull/125520) (issue: [#102606](https://github.com/elastic/elasticsearch/issues/102606))
* Add cache support in `TransportGetAllocationStatsAction` [#124898](https://github.com/elastic/elasticsearch/pull/124898) (issue: [#110716](https://github.com/elastic/elasticsearch/issues/110716))
* Add cancellation support in `TransportGetAllocationStatsAction` [#127371](https://github.com/elastic/elasticsearch/pull/127371) (issue: [#123248](https://github.com/elastic/elasticsearch/issues/123248))
* Allow balancing weights to be set per tier [#126091](https://github.com/elastic/elasticsearch/pull/126091)
* Introduce `AllocationBalancingRoundSummaryService` [#120957](https://github.com/elastic/elasticsearch/pull/120957)
* More efficient sort in `tryRelocateShard` [#128063](https://github.com/elastic/elasticsearch/pull/128063)

Analysis:
* Synonyms API - Add refresh parameter to check synonyms index and reload analyzers [#126935](https://github.com/elastic/elasticsearch/pull/126935) (issue: [#121441](https://github.com/elastic/elasticsearch/issues/121441))

Authentication:
* Add Support for Providing a custom `ServiceAccountTokenStore` through `SecurityExtensions` [#126612](https://github.com/elastic/elasticsearch/pull/126612)
* Implement SAML custom attributes support for Identity Provider [#128176](https://github.com/elastic/elasticsearch/pull/128176)
* Permit at+jwt typ header value in jwt access tokens [#126687](https://github.com/elastic/elasticsearch/pull/126687) (issue: [#119370](https://github.com/elastic/elasticsearch/issues/119370))

Authorization:
* Add Microsoft Graph Delegated Authorization Realm Plugin [#127910](https://github.com/elastic/elasticsearch/pull/127910)
* Check `TooComplex` exception for `HasPrivileges` body [#128870](https://github.com/elastic/elasticsearch/pull/128870)
* Delegated authorization using Microsoft Graph (SDK) [#128396](https://github.com/elastic/elasticsearch/pull/128396)
* Fix unsupported privileges error message during role and API key crea… [#128858](https://github.com/elastic/elasticsearch/pull/128858) (issue: [#128132](https://github.com/elastic/elasticsearch/issues/128132))
* Granting `kibana_system` reserved role access to "all" privileges to `.adhoc.alerts*` and `.internal.adhoc.alerts*` indices [#127321](https://github.com/elastic/elasticsearch/pull/127321)
* [Security Solution] Add `read` index privileges to `kibana_system` role for Microsoft Defender integration indexes [#126803](https://github.com/elastic/elasticsearch/pull/126803)

CCS:
* Check if index patterns conform to valid format before validation [#122497](https://github.com/elastic/elasticsearch/pull/122497)

CRUD:
* Add `IndexingPressureMonitor` to monitor large indexing operations [#126372](https://github.com/elastic/elasticsearch/pull/126372)
* Enhance memory accounting for document expansion and introduce max document size limit [#123543](https://github.com/elastic/elasticsearch/pull/123543)

Codec:
* First step optimizing tsdb doc values codec merging [#125403](https://github.com/elastic/elasticsearch/pull/125403)
* Use default Lucene postings format when index mode is standard. [#128509](https://github.com/elastic/elasticsearch/pull/128509)

Data streams:
* Add ability to redirect ingestion failures on data streams to a failure store [#126973](https://github.com/elastic/elasticsearch/pull/126973)
* Add index mode to get data stream API [#122486](https://github.com/elastic/elasticsearch/pull/122486)
* Run `TransportGetDataStreamLifecycleAction` on local node [#125214](https://github.com/elastic/elasticsearch/pull/125214)
* Run `TransportGetDataStreamOptionsAction` on local node [#125213](https://github.com/elastic/elasticsearch/pull/125213)
* Run `TransportGetDataStreamsAction` on local node [#122852](https://github.com/elastic/elasticsearch/pull/122852)
* Update ecs@mappings.json with new GenAI fields [#129122](https://github.com/elastic/elasticsearch/pull/129122)
* [Failure store] Introduce dedicated failure store lifecycle configuration [#127314](https://github.com/elastic/elasticsearch/pull/127314)
* [Failure store] Introduce default retention for failure indices [#127573](https://github.com/elastic/elasticsearch/pull/127573)
* [apm-data] Enable 'date_detection' for all apm data streams [#128913](https://github.com/elastic/elasticsearch/pull/128913)

Distributed:
* Account for time taken to write index buffers in `IndexingMemoryController` [#126786](https://github.com/elastic/elasticsearch/pull/126786)

ES|QL:
* Add MATCH_PHRASE [#127661](https://github.com/elastic/elasticsearch/pull/127661)
* Add Support for LIKE (LIST) [#129170](https://github.com/elastic/elasticsearch/pull/129170)
* Add `documents_found` and `values_loaded` [#125631](https://github.com/elastic/elasticsearch/pull/125631)
* Add `suggested_cast` [#127139](https://github.com/elastic/elasticsearch/pull/127139)
* Add emit time to hash aggregation status [#127988](https://github.com/elastic/elasticsearch/pull/127988)
* Add initial grammar and changes for FORK [#121948](https://github.com/elastic/elasticsearch/pull/121948)
* Add initial grammar and planning for RRF (snapshot) [#123396](https://github.com/elastic/elasticsearch/pull/123396)
* Add local optimizations for `constant_keyword` [#127549](https://github.com/elastic/elasticsearch/pull/127549)
* Add optimization to purge join on null merge key [#127583](https://github.com/elastic/elasticsearch/pull/127583) (issue: [#125577](https://github.com/elastic/elasticsearch/issues/125577))
* Add support for LOOKUP JOIN on aliases [#128519](https://github.com/elastic/elasticsearch/pull/128519)
* Add support for parameters in LIMIT command [#128464](https://github.com/elastic/elasticsearch/pull/128464)
* Aggressive release of shard contexts [#129454](https://github.com/elastic/elasticsearch/pull/129454)
* Allow lookup join on mixed numeric fields [#128263](https://github.com/elastic/elasticsearch/pull/128263)
* Allow partial results in ES|QL [#121942](https://github.com/elastic/elasticsearch/pull/121942)
* Avoid `NamedWritable` in block serialization [#124394](https://github.com/elastic/elasticsearch/pull/124394)
* COMPLETION command grammar and logical plan [#126319](https://github.com/elastic/elasticsearch/pull/126319)
* Calculate concurrent node limit [#124901](https://github.com/elastic/elasticsearch/pull/124901)
* Change queries ID to be the same as the async [#127472](https://github.com/elastic/elasticsearch/pull/127472) (issue: [#127187](https://github.com/elastic/elasticsearch/issues/127187))
* Double parameter markers for identifiers [#122459](https://github.com/elastic/elasticsearch/pull/122459)
* ESQL: Enhanced `DATE_TRUNC` with arbitrary intervals [#120302](https://github.com/elastic/elasticsearch/pull/120302) (issue: [#120094](https://github.com/elastic/elasticsearch/issues/120094))
* ES|QL - Add COMPLETION command as a tech preview feature [#128948](https://github.com/elastic/elasticsearch/pull/128948) (issue: [#124405](https://github.com/elastic/elasticsearch/issues/124405))
* ES|QL - Add `match_phrase` full text function (tech preview) [#128925](https://github.com/elastic/elasticsearch/pull/128925)
* ES|QL - Allow full text functions to be used in STATS [#125479](https://github.com/elastic/elasticsearch/pull/125479) (issue: [#125481](https://github.com/elastic/elasticsearch/issues/125481))
* ES|QL cross-cluster querying is now generally available [#130032](https://github.com/elastic/elasticsearch/pull/130032)
* ES|QL slow log [#124094](https://github.com/elastic/elasticsearch/pull/124094)
* ES|QL: Support `::date` in inline cast [#123460](https://github.com/elastic/elasticsearch/pull/123460) (issue: [#116746](https://github.com/elastic/elasticsearch/issues/116746))
* Emit ordinal output block for values aggregate [#127201](https://github.com/elastic/elasticsearch/pull/127201)
* Fix sorting when `aggregate_metric_double` present [#125191](https://github.com/elastic/elasticsearch/pull/125191)
* Heuristics to pick efficient partitioning [#125739](https://github.com/elastic/elasticsearch/pull/125739)
* Implement runtime skip_unavailable=true [#121240](https://github.com/elastic/elasticsearch/pull/121240)
* Include failures in partial response [#124929](https://github.com/elastic/elasticsearch/pull/124929)
* Infer the score mode to use from the Lucene collector [#125930](https://github.com/elastic/elasticsearch/pull/125930)
* Introduce `AggregateMetricDoubleBlock` [#127299](https://github.com/elastic/elasticsearch/pull/127299)
* Introduce `allow_partial_results` setting in ES|QL [#122890](https://github.com/elastic/elasticsearch/pull/122890)
* Introduce a pre-mapping logical plan processing step [#121260](https://github.com/elastic/elasticsearch/pull/121260)
* Keep ordinals in conversion functions [#125357](https://github.com/elastic/elasticsearch/pull/125357)
* List/get query API [#124832](https://github.com/elastic/elasticsearch/pull/124832) (issue: [#124827](https://github.com/elastic/elasticsearch/issues/124827))
* Log partial failures [#129164](https://github.com/elastic/elasticsearch/pull/129164)
* Optimize ordinal inputs in Values aggregation [#127849](https://github.com/elastic/elasticsearch/pull/127849)
* Pragma to load from stored fields [#122891](https://github.com/elastic/elasticsearch/pull/122891)
* Push more `==`s on text fields to lucene [#126641](https://github.com/elastic/elasticsearch/pull/126641)
* Pushdown Lookup Join past Project [#129503](https://github.com/elastic/elasticsearch/pull/129503) (issue: [#119082](https://github.com/elastic/elasticsearch/issues/119082))
* Pushdown constructs doing case-insensitive regexes [#128393](https://github.com/elastic/elasticsearch/pull/128393) (issue: [#127479](https://github.com/elastic/elasticsearch/issues/127479))
* Pushdown for LIKE (LIST) [#129557](https://github.com/elastic/elasticsearch/pull/129557)
* ROUND_TO function [#128278](https://github.com/elastic/elasticsearch/pull/128278)
* Release FORK in tech preview [#129606](https://github.com/elastic/elasticsearch/pull/129606)
* Remove page alignment in exchange sink [#124610](https://github.com/elastic/elasticsearch/pull/124610)
* Render `aggregate_metric_double` [#122660](https://github.com/elastic/elasticsearch/pull/122660)
* Report `original_types` [#124913](https://github.com/elastic/elasticsearch/pull/124913)
* Report failures on partial results [#124823](https://github.com/elastic/elasticsearch/pull/124823)
* Retry ES|QL node requests on shard level failures [#120774](https://github.com/elastic/elasticsearch/pull/120774)
* Retry shard movements during ESQL query [#126653](https://github.com/elastic/elasticsearch/pull/126653)
* Run coordinating `can_match` in field-caps [#127734](https://github.com/elastic/elasticsearch/pull/127734)
* Skip unused STATS groups by adding a Top N `BlockHash` implementation [#127148](https://github.com/elastic/elasticsearch/pull/127148)
* Specialize ags `AddInput` for each block type [#127582](https://github.com/elastic/elasticsearch/pull/127582)
* Speed loading stored fields [#127348](https://github.com/elastic/elasticsearch/pull/127348)
* Support partial results in CCS in ES|QL [#122708](https://github.com/elastic/elasticsearch/pull/122708)
* Support subset of metrics in aggregate metric double [#121805](https://github.com/elastic/elasticsearch/pull/121805)
* Take double parameter markers for identifiers out of snapshot [#125690](https://github.com/elastic/elasticsearch/pull/125690)
* `ToAggregateMetricDouble` function [#124595](https://github.com/elastic/elasticsearch/pull/124595)
* `text ==` and `text !=` pushdown [#127355](https://github.com/elastic/elasticsearch/pull/127355)

Engine:
* Throttle indexing when disk IO throttling is disabled [#129245](https://github.com/elastic/elasticsearch/pull/129245)
* Track & log when there is insufficient disk space available to execute merges [#131711](https://github.com/elastic/elasticsearch/pull/131711)

Geo:
* Support explicit Z/M attributes using WKT geometry [#125896](https://github.com/elastic/elasticsearch/pull/125896) (issue: [#123111](https://github.com/elastic/elasticsearch/issues/123111))

Health:
* Add health indicator impact to `HealthPeriodicLogger` [#122390](https://github.com/elastic/elasticsearch/pull/122390)

ILM+SLM:
* Add `index.lifecycle.skip` index-scoped setting to instruct ILM to skip processing specific indices [#128736](https://github.com/elastic/elasticsearch/pull/128736)
* Batch ILM policy cluster state updates [#122917] [#126529](https://github.com/elastic/elasticsearch/pull/126529) (issue: [#122917](https://github.com/elastic/elasticsearch/issues/122917))
* Improve SLM Health Indicator to cover missing snapshot [#121370](https://github.com/elastic/elasticsearch/pull/121370)
* Optimize usage calculation in ILM policies retrieval API [#106953](https://github.com/elastic/elasticsearch/pull/106953) (issue: [#105773](https://github.com/elastic/elasticsearch/issues/105773))
* Process ILM cluster state updates on another thread [#123712](https://github.com/elastic/elasticsearch/pull/123712)
* Run `TransportExplainLifecycleAction` on local node [#122885](https://github.com/elastic/elasticsearch/pull/122885)
* Run `TransportGetLifecycleAction` on local node [#126002](https://github.com/elastic/elasticsearch/pull/126002)
* Run `TransportGetStatusAction` on local node [#129367](https://github.com/elastic/elasticsearch/pull/129367)
* Truncate `step_info` and error reason in ILM execution state and history [#125054](https://github.com/elastic/elasticsearch/pull/125054) (issue: [#124181](https://github.com/elastic/elasticsearch/issues/124181))

IdentityProvider:
* Add "extension" attribute validation to IdP SPs [#128805](https://github.com/elastic/elasticsearch/pull/128805)
* Add transport version support for IDP_CUSTOM_SAML_ATTRIBUTES_ADDED_8_19 [#128798](https://github.com/elastic/elasticsearch/pull/128798)

Indices APIs:
* Add RemoveBlock API to allow `DELETE /{index}/_block/{block}` [#129128](https://github.com/elastic/elasticsearch/pull/129128)
* Avoid creating known_fields for every check in Alias [#124690](https://github.com/elastic/elasticsearch/pull/124690)
* Run `TransportGetIndexAction` on local node [#125652](https://github.com/elastic/elasticsearch/pull/125652)
* Run `TransportGetMappingsAction` on local node [#122921](https://github.com/elastic/elasticsearch/pull/122921)
* Run `TransportGetSettingsAction` on local node [#126051](https://github.com/elastic/elasticsearch/pull/126051)
* Throw exception for unknown token in RestIndexPutAliasAction [#124708](https://github.com/elastic/elasticsearch/pull/124708)
* Throw exception for unsupported values type in Alias [#124737](https://github.com/elastic/elasticsearch/pull/124737)

Inference:
* Adding Google VertexAI chat completion integration [#128105](https://github.com/elastic/elasticsearch/pull/128105)
* Adding Google VertexAI completion integration [#128694](https://github.com/elastic/elasticsearch/pull/128694)
* [Inference API] Rename `model_id` prop to model in EIS sparse inference request body [#122272](https://github.com/elastic/elasticsearch/pull/122272)

Infra/CLI:
* Use logs dir as working directory [#124966](https://github.com/elastic/elasticsearch/pull/124966)

Infra/Core:
* Give Kibana user 'all' permissions for .entity_analytics.* indices [#123588](https://github.com/elastic/elasticsearch/pull/123588)
* Improve support for bytecode patching signed jars [#128613](https://github.com/elastic/elasticsearch/pull/128613)
* Permanently switch from Java SecurityManager to Entitlements. The Java SecurityManager has been deprecated since Java 17, and it is now completely disabled in Java 24. In order to retain an similar level of protection, Elasticsearch implemented its own protection mechanism, Entitlements. Starting with this version, Entitlements will permanently replace the Java SecurityManager. [#125117](https://github.com/elastic/elasticsearch/pull/125117)

Infra/Metrics:
* Add thread pool utilization metric [#120363](https://github.com/elastic/elasticsearch/pull/120363)
* Publish queue latency metrics from tracked thread pools [#120488](https://github.com/elastic/elasticsearch/pull/120488)

Infra/Settings:
* Allow float settings to be configured with other settings as default [#126751](https://github.com/elastic/elasticsearch/pull/126751)
* Allow passing several reserved state chunks in single process call [#124574](https://github.com/elastic/elasticsearch/pull/124574)
* Ensure config reload on ..data symlink switch for CSI driver support [#127628](https://github.com/elastic/elasticsearch/pull/127628)
* `FileWatchingService` shoudld not throw for missing file [#126264](https://github.com/elastic/elasticsearch/pull/126264)

Ingest Node:
* Adding `NormalizeForStreamProcessor` [#125699](https://github.com/elastic/elasticsearch/pull/125699)
* Run `TransportEnrichStatsAction` on local node [#121256](https://github.com/elastic/elasticsearch/pull/121256)

Logs:
* Conditionally force sequential reading in `LuceneSyntheticSourceChangesSnapshot` [#128473](https://github.com/elastic/elasticsearch/pull/128473)

Machine Learning:
* Add Custom inference service [#127939](https://github.com/elastic/elasticsearch/pull/127939)
* Add Telemetry for models without adaptive allocations [#129161](https://github.com/elastic/elasticsearch/pull/129161)
* Add `ModelRegistryMetadata` to Cluster State [#121106](https://github.com/elastic/elasticsearch/pull/121106)
* Add `none` chunking strategy to disable automatic chunking for inference endpoints [#129150](https://github.com/elastic/elasticsearch/pull/129150)
* Add recursive chunker [#126866](https://github.com/elastic/elasticsearch/pull/126866)
* Added Mistral Chat Completion support to the Inference Plugin [#128538](https://github.com/elastic/elasticsearch/pull/128538)
* Adding VoyageAI's v3.5 models [#128241](https://github.com/elastic/elasticsearch/pull/128241)
* Adding common rerank options to Perform Inference API [#125239](https://github.com/elastic/elasticsearch/pull/125239) (issue: [#111273](https://github.com/elastic/elasticsearch/issues/111273))
* Adding elser default endpoint for EIS [#122066](https://github.com/elastic/elasticsearch/pull/122066)
* Adding endpoint creation validation to `ElasticInferenceService` [#117642](https://github.com/elastic/elasticsearch/pull/117642)
* Adding integration for VoyageAI embeddings and rerank models [#122134](https://github.com/elastic/elasticsearch/pull/122134)
* Adding support for binary embedding type to Cohere service embedding type [#120751](https://github.com/elastic/elasticsearch/pull/120751)
* Adding support for specifying embedding type to Jina AI service settings [#121548](https://github.com/elastic/elasticsearch/pull/121548)
* Adding validation to `ElasticsearchInternalService` [#123044](https://github.com/elastic/elasticsearch/pull/123044)
* Bedrock Cohere Task Settings Support [#126493](https://github.com/elastic/elasticsearch/pull/126493) (issue: [#126156](https://github.com/elastic/elasticsearch/issues/126156))
* ES|QL SAMPLE aggregation function [#127629](https://github.com/elastic/elasticsearch/pull/127629)
* ES|QL `change_point` processing command [#120998](https://github.com/elastic/elasticsearch/pull/120998)
* ES|QL random sampling [#125570](https://github.com/elastic/elasticsearch/pull/125570)
* Expose `input_type` option at root level for `text_embedding` task type in Perform Inference API [#122638](https://github.com/elastic/elasticsearch/pull/122638) (issue: [#117856](https://github.com/elastic/elasticsearch/issues/117856))
* Improve exception for trained model deployment scale up timeout [#128218](https://github.com/elastic/elasticsearch/pull/128218)
* Increment inference stats counter for shard bulk inference calls [#129140](https://github.com/elastic/elasticsearch/pull/129140)
* Integrate `OpenAi` Chat Completion in `SageMaker` [#127767](https://github.com/elastic/elasticsearch/pull/127767)
* Integrate with `DeepSeek` API [#122218](https://github.com/elastic/elasticsearch/pull/122218)
* Limit the number of chunks for semantic text to prevent high memory usage [#123150](https://github.com/elastic/elasticsearch/pull/123150)
* Make Adaptive Allocations Scale to Zero configurable and set default to 24h [#128914](https://github.com/elastic/elasticsearch/pull/128914)
* Mark token pruning for sparse vector as GA [#128854](https://github.com/elastic/elasticsearch/pull/128854)
* Move to the Cohere V2 API for new inference endpoints [#129884](https://github.com/elastic/elasticsearch/pull/129884)
* Semantic Text Chunking Indexing Pressure [#125517](https://github.com/elastic/elasticsearch/pull/125517)
* Track memory used in the hierarchical results normalizer [#2831](https://github.com/elastic/elasticsearch/pull/2831)
* Upgrade AWS v2 SDK to 2.30.38 [#124738](https://github.com/elastic/elasticsearch/pull/124738)
* [Inference API] Propagate product use case http header to EIS [#124025](https://github.com/elastic/elasticsearch/pull/124025)
* [ML] Add HuggingFace Chat Completion support to the Inference Plugin [#127254](https://github.com/elastic/elasticsearch/pull/127254)
* [ML] Add Rerank support to the Inference Plugin [#127966](https://github.com/elastic/elasticsearch/pull/127966)
* [ML] Integrate SageMaker with OpenAI Embeddings [#126856](https://github.com/elastic/elasticsearch/pull/126856)
* `InferenceService` support aliases [#128584](https://github.com/elastic/elasticsearch/pull/128584)
* `SageMaker` Elastic Payload [#129413](https://github.com/elastic/elasticsearch/pull/129413)

Mapping:
* Add `index_options` to `semantic_text` field mappings [#119967](https://github.com/elastic/elasticsearch/pull/119967)
* Add block loader from stored field and source for ip field [#126644](https://github.com/elastic/elasticsearch/pull/126644)
* Do not respect synthetic_source_keep=arrays if type parses arrays [#127796](https://github.com/elastic/elasticsearch/pull/127796) (issue: [#126155](https://github.com/elastic/elasticsearch/issues/126155))
* Enable synthetic recovery source by default when synthetic source is enabled. Using synthetic recovery source significantly improves indexing performance compared to regular recovery source. [#122615](https://github.com/elastic/elasticsearch/pull/122615) (issue: [#116726](https://github.com/elastic/elasticsearch/issues/116726))
* Enable the use of nested field type with index.mode=time_series [#122224](https://github.com/elastic/elasticsearch/pull/122224) (issue: [#120874](https://github.com/elastic/elasticsearch/issues/120874))
* Exclude `semantic_text` subfields from field capabilities API [#127664](https://github.com/elastic/elasticsearch/pull/127664)
* Improved error message when index field type is invalid [#122860](https://github.com/elastic/elasticsearch/pull/122860)
* Introduce `FallbackSyntheticSourceBlockLoader` and apply it to keyword fields [#119546](https://github.com/elastic/elasticsearch/pull/119546)
* Refactor `SourceProvider` creation to consistently use `MappingLookup` [#128213](https://github.com/elastic/elasticsearch/pull/128213)
* Skip indexing points for `seq_no` in tsdb and logsdb [#128139](https://github.com/elastic/elasticsearch/pull/128139)
* Store arrays offsets for boolean fields natively with synthetic source [#125529](https://github.com/elastic/elasticsearch/pull/125529)
* Store arrays offsets for ip fields natively with synthetic source [#122999](https://github.com/elastic/elasticsearch/pull/122999)
* Store arrays offsets for keyword fields natively with synthetic source instead of falling back to ignored source. [#113757](https://github.com/elastic/elasticsearch/pull/113757)
* Store arrays offsets for numeric fields natively with synthetic source [#124594](https://github.com/elastic/elasticsearch/pull/124594)
* Store arrays offsets for unsigned long fields natively with synthetic source [#125709](https://github.com/elastic/elasticsearch/pull/125709)
* Update `sparse_vector` field mapping to include default setting for token pruning [#129089](https://github.com/elastic/elasticsearch/pull/129089)
* Use `FallbackSyntheticSourceBlockLoader` for `shape` and `geo_shape` [#124927](https://github.com/elastic/elasticsearch/pull/124927)
* Use `FallbackSyntheticSourceBlockLoader` for `unsigned_long` and `scaled_float` fields [#122637](https://github.com/elastic/elasticsearch/pull/122637)
* Use `FallbackSyntheticSourceBlockLoader` for boolean and date fields [#124050](https://github.com/elastic/elasticsearch/pull/124050)
* Use `FallbackSyntheticSourceBlockLoader` for number fields [#122280](https://github.com/elastic/elasticsearch/pull/122280)
* Use `FallbackSyntheticSourceBlockLoader` for point and `geo_point` [#125816](https://github.com/elastic/elasticsearch/pull/125816)
* Use `FallbackSyntheticSourceBlockLoader` for text fields [#126237](https://github.com/elastic/elasticsearch/pull/126237)

Network:
* Move HTTP content aggregation from Netty into `RestController` [#129302](https://github.com/elastic/elasticsearch/pull/129302) (issue: [#120746](https://github.com/elastic/elasticsearch/issues/120746))
* Remove first `FlowControlHandler` from HTTP pipeline [#128099](https://github.com/elastic/elasticsearch/pull/128099)
* Replace auto-read with proper flow-control in HTTP pipeline [#127817](https://github.com/elastic/elasticsearch/pull/127817)
* Set `connection: close` header on shutdown [#128025](https://github.com/elastic/elasticsearch/pull/128025) (issue: [#127984](https://github.com/elastic/elasticsearch/issues/127984))

Ranking:
* Adding ES|QL Reranker command in snapshot builds [#123074](https://github.com/elastic/elasticsearch/pull/123074)
* Leverage scorer supplier in `QueryFeatureExtractor` [#125259](https://github.com/elastic/elasticsearch/pull/125259)

Recovery:
* Move unpromotable relocations to its own transport action [#127330](https://github.com/elastic/elasticsearch/pull/127330)

Relevance:
* Add l2_norm normalization support to linear retriever [#128504](https://github.com/elastic/elasticsearch/pull/128504)
* Add pinned retriever [#126401](https://github.com/elastic/elasticsearch/pull/126401)
* Default new `semantic_text` fields to use BBQ when models are compatible [#126629](https://github.com/elastic/elasticsearch/pull/126629)
* Skip semantic_text embedding generation when no content is provided. [#123763](https://github.com/elastic/elasticsearch/pull/123763)
* Support configurable chunking in `semantic_text` fields [#121041](https://github.com/elastic/elasticsearch/pull/121041)

Search:
* Account for the `SearchHit` source in circuit breaker [#121920](https://github.com/elastic/elasticsearch/pull/121920) (issue: [#89656](https://github.com/elastic/elasticsearch/issues/89656))
* Add `bucketedSort` based on int [#128848](https://github.com/elastic/elasticsearch/pull/128848)
* Add initial version (behind snapshot) of `multi_match` function #121525 [#125062](https://github.com/elastic/elasticsearch/pull/125062) (issue: [#121525](https://github.com/elastic/elasticsearch/issues/121525))
* Add min score linear retriever [#129359](https://github.com/elastic/elasticsearch/pull/129359)
* ESQL - Enable telemetry for COMPLETION command [#127731](https://github.com/elastic/elasticsearch/pull/127731)
* Enable sort optimization on int, short and byte fields [#127968](https://github.com/elastic/elasticsearch/pull/127968) (issue: [#127965](https://github.com/elastic/elasticsearch/issues/127965))
* Introduce batched query execution and data-node side reduce [#121885](https://github.com/elastic/elasticsearch/pull/121885)
* Optimize memory usage in `ShardBulkInferenceActionFilter` [#124313](https://github.com/elastic/elasticsearch/pull/124313)
* Optionally allow text similarity reranking to fail [#121784](https://github.com/elastic/elasticsearch/pull/121784)
* Restore model registry validation for the semantic text field [#127285](https://github.com/elastic/elasticsearch/pull/127285)
* Return float[] instead of List<Double> in `valueFetcher` [#126702](https://github.com/elastic/elasticsearch/pull/126702)
* Simplified Linear Retriever [#129200](https://github.com/elastic/elasticsearch/pull/129200)
* Simplified RRF Retriever [#129659](https://github.com/elastic/elasticsearch/pull/129659)
* Upgrade to Lucene 10.2.0 [#126594](https://github.com/elastic/elasticsearch/pull/126594)
* Upgrade to Lucene 10.2.1 [#127343](https://github.com/elastic/elasticsearch/pull/127343)
* Upgrade to Lucene 10.2.2 [#129546](https://github.com/elastic/elasticsearch/pull/129546)
* Wrap remote errors with cluster name to provide more context [#123156](https://github.com/elastic/elasticsearch/pull/123156)

Snapshot/Restore:
* Add GCS telemetry with `ThreadLocal` [#125452](https://github.com/elastic/elasticsearch/pull/125452)
* Add `state` query param to Get snapshots API [#128635](https://github.com/elastic/elasticsearch/pull/128635) (issue: [#97446](https://github.com/elastic/elasticsearch/issues/97446))
* Allow missing shard stats for restarted nodes for `_snapshot/_status` [#128399](https://github.com/elastic/elasticsearch/pull/128399)
* GCS blob store: add `OperationPurpose/Operation` stats counters [#122991](https://github.com/elastic/elasticsearch/pull/122991)
* Improve get-snapshots message for unreadable repository [#128273](https://github.com/elastic/elasticsearch/pull/128273)
* Optimize shared blob cache evictions on shard removal Shared blob cache evictions occur on the cluster applier thread when shards are removed from a node. These can be expensive if a large number of shards are being removed. This change uses the context of the removal to avoid unnecessary evictions that might hold up the applier thread.  [#126581](https://github.com/elastic/elasticsearch/pull/126581)
* Retry when the server can't be resolved (Google Cloud Storage) [#123852](https://github.com/elastic/elasticsearch/pull/123852)
* Upgrade AWS Java SDK to 2.31.78 [#131050](https://github.com/elastic/elasticsearch/pull/131050)
* Upgrade to repository-gcs to use com.google.cloud:google-cloud-storage-bom:2.50.0 [#126087](https://github.com/elastic/elasticsearch/pull/126087)
* [Draft] Support concurrent multipart uploads in Azure [#128449](https://github.com/elastic/elasticsearch/pull/128449)

Stats:
* Run XPack usage actions on local node [#122933](https://github.com/elastic/elasticsearch/pull/122933)

Task Management:
* React more prompty to task cancellation while waiting for the cluster to unblock [#128737](https://github.com/elastic/elasticsearch/pull/128737) (issue: [#117971](https://github.com/elastic/elasticsearch/issues/117971))

Vector Search:
* Add bit vector support to semantic text [#123187](https://github.com/elastic/elasticsearch/pull/123187)
* Add dense vector off-heap stats to Node stats and Index stats APIs [#126704](https://github.com/elastic/elasticsearch/pull/126704)
* Add option to include or exclude vectors from `_source` retrieval [#128735](https://github.com/elastic/elasticsearch/pull/128735)
* Add panama implementations of byte-bit and float-bit script operations [#124722](https://github.com/elastic/elasticsearch/pull/124722) (issue: [#117096](https://github.com/elastic/elasticsearch/issues/117096))
* Adds implementations of dotProduct and cosineSimilarity painless methods to operate on float vectors for byte fields [#122381](https://github.com/elastic/elasticsearch/pull/122381) (issue: [#117274](https://github.com/elastic/elasticsearch/issues/117274))
* Allow zero for `rescore_vector.oversample` to indicate by-passing oversample and rescoring [#125599](https://github.com/elastic/elasticsearch/pull/125599)
* Define a default oversample value for dense vectors with bbq_hnsw/bbq_flat [#127134](https://github.com/elastic/elasticsearch/pull/127134)
* Improve HNSW filtered search speed through new heuristic [#126876](https://github.com/elastic/elasticsearch/pull/126876)
* Make `dense_vector` fields updatable to bbq_flat/bbq_hnsw [#128291](https://github.com/elastic/elasticsearch/pull/128291)
* Mark `rescore_vector` as generally available [#126038](https://github.com/elastic/elasticsearch/pull/126038)
* New `vector_rescore` parameter as a quantized index type option [#124581](https://github.com/elastic/elasticsearch/pull/124581)
* Panama vector accelerated optimized scalar quantization [#127118](https://github.com/elastic/elasticsearch/pull/127118)

Watcher:
* Run `TransportGetWatcherSettingsAction` on local node [#122857](https://github.com/elastic/elasticsearch/pull/122857)


### Fixes [elasticsearch-9.1.0-fixes]

Aggregations:
* Bypass competitive iteration in single filter bucket case [#127267](https://github.com/elastic/elasticsearch/pull/127267) (issue: [#127262](https://github.com/elastic/elasticsearch/issues/127262))
* Temporarily bypass competitive iteration for filters aggregation [#126956](https://github.com/elastic/elasticsearch/pull/126956)

Allocation:
* `DesiredBalanceReconciler` always returns `AllocationStats` [#122458](https://github.com/elastic/elasticsearch/pull/122458)

Analysis:
* Add refresh to synonyms put / delete APIs to wait for synonyms to be accessible and reload analyzers [#126314](https://github.com/elastic/elasticsearch/pull/126314) (issue: [#121441](https://github.com/elastic/elasticsearch/issues/121441))

Cluster Coordination:
* Disable logging in `ClusterFormationFailureHelper` on shutdown [#125244](https://github.com/elastic/elasticsearch/pull/125244) (issue: [#105559](https://github.com/elastic/elasticsearch/issues/105559))

Data streams:
* Move streams status actions to cluster:monitor group [#131015](https://github.com/elastic/elasticsearch/pull/131015)
* [apm-data] Set `event.dataset` if empty for logs [#129074](https://github.com/elastic/elasticsearch/pull/129074)

Distributed:
* Fix incorrect accounting of semantic text indexing memory pressure [#130221](https://github.com/elastic/elasticsearch/pull/130221)
* Modify the mechanism to pause indexing [#128405](https://github.com/elastic/elasticsearch/pull/128405)
* Pass `IndexReshardingMetadata` over the wire [#124841](https://github.com/elastic/elasticsearch/pull/124841)

ES|QL:
* Added Sample operator `NamedWritable` to plugin [#131541](https://github.com/elastic/elasticsearch/pull/131541)
* Disable a bugged commit [#127199](https://github.com/elastic/elasticsearch/pull/127199) (issue: [#127197](https://github.com/elastic/elasticsearch/issues/127197))
* Disallow remote enrich after lu join [#131426](https://github.com/elastic/elasticsearch/pull/131426) (issue: [#129372](https://github.com/elastic/elasticsearch/issues/129372))
* ESQL: Fix `NULL` handling in `IN` clause [#125832](https://github.com/elastic/elasticsearch/pull/125832) (issue: [#119950](https://github.com/elastic/elasticsearch/issues/119950))
* ESQL: Fix `mv_expand` inconsistent column order [#129745](https://github.com/elastic/elasticsearch/pull/129745) (issue: [#129000](https://github.com/elastic/elasticsearch/issues/129000))
* ESQL: Fix inconsistent results in using scaled_float field [#122586](https://github.com/elastic/elasticsearch/pull/122586) (issue: [#122547](https://github.com/elastic/elasticsearch/issues/122547))
* ESQL: Preserve single aggregate when all attributes are pruned [#126397](https://github.com/elastic/elasticsearch/pull/126397) (issue: [#126392](https://github.com/elastic/elasticsearch/issues/126392))
* ESQL: Retain aggregate when grouping [#126598](https://github.com/elastic/elasticsearch/pull/126598) (issue: [#126026](https://github.com/elastic/elasticsearch/issues/126026))
* Fail with 500 not 400 for `ValueExtractor` bugs [#126296](https://github.com/elastic/elasticsearch/pull/126296)
* Fix LIMIT NPE with null value [#130914](https://github.com/elastic/elasticsearch/pull/130914) (issue: [#130908](https://github.com/elastic/elasticsearch/issues/130908))
* Fix `PushQueriesIT.testLike()` fails [#129647](https://github.com/elastic/elasticsearch/pull/129647)
* Fix `PushQueryIT#testEqualityOrTooBig` [#129657](https://github.com/elastic/elasticsearch/pull/129657) (issue: [#129545](https://github.com/elastic/elasticsearch/issues/129545))
* Fix behavior for `_index` LIKE for ESQL [#130849](https://github.com/elastic/elasticsearch/pull/130849) (issue: [#129511](https://github.com/elastic/elasticsearch/issues/129511))
* Fix constant keyword optimization [#129278](https://github.com/elastic/elasticsearch/pull/129278)
* Fix conversion of a Lucene wildcard pattern to a regexp [#128750](https://github.com/elastic/elasticsearch/pull/128750) (issues: [#128677](https://github.com/elastic/elasticsearch/issues/128677), [#128676](https://github.com/elastic/elasticsearch/issues/128676))
* Fix functions emitting warnings with no source [#122821](https://github.com/elastic/elasticsearch/pull/122821) (issue: [#122588](https://github.com/elastic/elasticsearch/issues/122588))
* Fix queries with missing index, `skip_unavailable` and filters [#130344](https://github.com/elastic/elasticsearch/pull/130344)
* Fix transport versions [#127668](https://github.com/elastic/elasticsearch/pull/127668) (issue: [#127667](https://github.com/elastic/elasticsearch/issues/127667))
* Handle unavailable MD5 in ES|QL [#130158](https://github.com/elastic/elasticsearch/pull/130158)
* Improve error message for ( and [ [#124177](https://github.com/elastic/elasticsearch/pull/124177) (issue: [#124145](https://github.com/elastic/elasticsearch/issues/124145))
* Prevent search functions work with a non-STANDARD index [#130638](https://github.com/elastic/elasticsearch/pull/130638) (issues: [#130561](https://github.com/elastic/elasticsearch/issues/130561), [#129778](https://github.com/elastic/elasticsearch/issues/129778))
* Remove duplicated nested commands [#123085](https://github.com/elastic/elasticsearch/pull/123085)
* Resolve groupings in aggregate before resolving references to groupings in the aggregations [#127524](https://github.com/elastic/elasticsearch/pull/127524)
* Retrieve token text only when necessary [#126578](https://github.com/elastic/elasticsearch/pull/126578)
* Support avg on aggregate metric double [#130421](https://github.com/elastic/elasticsearch/pull/130421)
* TO_IP can handle leading zeros [#126532](https://github.com/elastic/elasticsearch/pull/126532) (issue: [#125460](https://github.com/elastic/elasticsearch/issues/125460))
* TO_LOWER processes all values [#124676](https://github.com/elastic/elasticsearch/pull/124676) (issue: [#124002](https://github.com/elastic/elasticsearch/issues/124002))
* Workaround for RLike handling of empty lang pattern [#128895](https://github.com/elastic/elasticsearch/pull/128895) (issue: [#128813](https://github.com/elastic/elasticsearch/issues/128813))

Highlighting:
* Fix semantic highlighting bug on flat quantized fields [#131525](https://github.com/elastic/elasticsearch/pull/131525) (issue: [#131443](https://github.com/elastic/elasticsearch/issues/131443))

ILM+SLM:
* Fix `PolicyStepsRegistry` cache concurrency issue [#126840](https://github.com/elastic/elasticsearch/pull/126840) (issue: [#118406](https://github.com/elastic/elasticsearch/issues/118406))
* Inject an unfollow action before executing a downsample action in ILM [#105773](https://github.com/elastic/elasticsearch/pull/105773) (issue: [#105773](https://github.com/elastic/elasticsearch/issues/105773))
* Prevent ILM from processing shrunken index before its execution state is copied over [#129455](https://github.com/elastic/elasticsearch/pull/129455) (issue: [#109206](https://github.com/elastic/elasticsearch/issues/109206))
* The follower index should wait until the time series end time passes before unfollowing the leader index. [#128361](https://github.com/elastic/elasticsearch/pull/128361) (issue: [#128129](https://github.com/elastic/elasticsearch/issues/128129))

Indices APIs:
* Using a temp `IndexService` for template validation [#129507](https://github.com/elastic/elasticsearch/pull/129507) (issue: [#129473](https://github.com/elastic/elasticsearch/issues/129473))

Infra/Core:
* Reduce Data Loss in System Indices Migration [#121327](https://github.com/elastic/elasticsearch/pull/121327)
* System data streams are not being upgraded in the feature migration API [#126409](https://github.com/elastic/elasticsearch/pull/126409) (issue: [#122949](https://github.com/elastic/elasticsearch/issues/122949))

Infra/Node Lifecycle:
* Better handling of node ids from shutdown metadata (avoid NPE on already removed nodes) [#128298](https://github.com/elastic/elasticsearch/pull/128298) (issue: [#100201](https://github.com/elastic/elasticsearch/issues/100201))

Infra/REST API:
* Fix NPE in APMTracer through `RestController` [#128314](https://github.com/elastic/elasticsearch/pull/128314)
* Improve handling of empty response [#125562](https://github.com/elastic/elasticsearch/pull/125562) (issue: [#57639](https://github.com/elastic/elasticsearch/issues/57639))

Infra/Scripting:
* Add a custom `toString` to `DynamicMap` [#126562](https://github.com/elastic/elasticsearch/pull/126562) (issue: [#70262](https://github.com/elastic/elasticsearch/issues/70262))
* Add leniency to missing array values in mustache [#126550](https://github.com/elastic/elasticsearch/pull/126550) (issue: [#55200](https://github.com/elastic/elasticsearch/issues/55200))
* Fix painless return type cast for list shortcut [#126724](https://github.com/elastic/elasticsearch/pull/126724)

Infra/Settings:
* Add retry for `AccessDeniedException` in `AbstractFileWatchingService` [#128653](https://github.com/elastic/elasticsearch/pull/128653)

Ingest Node:
* Correctly handle non-integers in nested paths in the remove processor [#127006](https://github.com/elastic/elasticsearch/pull/127006)
* Correctly handle nulls in nested paths in the remove processor [#126417](https://github.com/elastic/elasticsearch/pull/126417)
* Correctly handling `download_database_on_pipeline_creation` within a pipeline processor within a default or final pipeline [#131236](https://github.com/elastic/elasticsearch/pull/131236)
* apm-data: Use representative count as event.success_count if available [#119995](https://github.com/elastic/elasticsearch/pull/119995)

Logs:
* Force niofs for fdt tmp file read access when flushing stored fields [#130308](https://github.com/elastic/elasticsearch/pull/130308)

Machine Learning:
* Adding timeout to request for creating inference endpoint [#126805](https://github.com/elastic/elasticsearch/pull/126805)
* Change ModelLoaderUtils.split to return the correct number of chunks and ranges. [#126009](https://github.com/elastic/elasticsearch/pull/126009) (issue: [#121799](https://github.com/elastic/elasticsearch/issues/121799))
* Fix ELAND endpoints not updating dimensions [#126537](https://github.com/elastic/elasticsearch/pull/126537)
* Fix memory usage estimation for ELSER models [#131630](https://github.com/elastic/elasticsearch/pull/131630)
* Prevent get datafeeds stats API returning an error when local tasks are slow to stop [#125477](https://github.com/elastic/elasticsearch/pull/125477) (issue: [#104160](https://github.com/elastic/elasticsearch/issues/104160))
* Provide model size statistics as soon as an anomaly detection job is opened [#124638](https://github.com/elastic/elasticsearch/pull/124638) (issue: [#121168](https://github.com/elastic/elasticsearch/issues/121168))
* Return a Conflict status code if the model deployment is stopped by a user [#125204](https://github.com/elastic/elasticsearch/pull/125204) (issue: [#123745](https://github.com/elastic/elasticsearch/issues/123745))
* Revert endpoint creation validation for ELSER and E5 [#126792](https://github.com/elastic/elasticsearch/pull/126792)
* Updates to allow using Cohere binary embedding response in semantic search queries [#121827](https://github.com/elastic/elasticsearch/pull/121827)
* Use INTERNAL_INGEST for Inference [#127522](https://github.com/elastic/elasticsearch/pull/127522) (issue: [#127519](https://github.com/elastic/elasticsearch/issues/127519))

Mapping:
* Synthetic source: avoid storing multi fields of type text and `match_only_text` by default [#129126](https://github.com/elastic/elasticsearch/pull/129126)

Ranking:
* Restore `TextSimilarityRankBuilder` XContent output [#124564](https://github.com/elastic/elasticsearch/pull/124564)
* Return BAD_REQUEST when a field scorer references a missing field [#127229](https://github.com/elastic/elasticsearch/pull/127229) (issue: [#127162](https://github.com/elastic/elasticsearch/issues/127162))

Relevance:
* Fix: Allow non-score secondary sorts in pinned retriever sub-retrievers [#128323](https://github.com/elastic/elasticsearch/pull/128323)
* Prevent Query Rule Creation with Invalid Numeric Match Criteria [#122823](https://github.com/elastic/elasticsearch/pull/122823)

Search:
* Add Cluster Feature for L2 Norm [#129181](https://github.com/elastic/elasticsearch/pull/129181)
* Check positions on `MultiPhraseQueries` as well as phrase queries [#129326](https://github.com/elastic/elasticsearch/pull/129326) (issue: [#123871](https://github.com/elastic/elasticsearch/issues/123871))
* Filter out empty top docs results before merging [#126385](https://github.com/elastic/elasticsearch/pull/126385) (issue: [#126118](https://github.com/elastic/elasticsearch/issues/126118))
* Fix NPE in `SemanticTextHighlighter` [#129509](https://github.com/elastic/elasticsearch/pull/129509) (issue: [#129501](https://github.com/elastic/elasticsearch/issues/129501))
* Fix bug in point in time response [#131391](https://github.com/elastic/elasticsearch/pull/131391) (issue: [#131026](https://github.com/elastic/elasticsearch/issues/131026))
* Fix handling of auto expand replicas for stateless indices [#122365](https://github.com/elastic/elasticsearch/pull/122365)
* Fix query rewrite logic to preserve `boosts` and `queryName` for `match`, `knn`, and `sparse_vector` queries on semantic_text fields [#129282](https://github.com/elastic/elasticsearch/pull/129282)
* Improve execution of terms queries over wildcard fields [#128986](https://github.com/elastic/elasticsearch/pull/128986) (issue: [#128201](https://github.com/elastic/elasticsearch/issues/128201))
* Remove empty results before merging [#126770](https://github.com/elastic/elasticsearch/pull/126770) (issue: [#126742](https://github.com/elastic/elasticsearch/issues/126742))
* Simplified Linear & RRF Retrievers - Return error on empty fields param [#129962](https://github.com/elastic/elasticsearch/pull/129962)

Snapshot/Restore:
* Do not apply further shard snapshot status updates after shard snapshot is complete [#127250](https://github.com/elastic/elasticsearch/pull/127250)
* Fix computation of last block size in Azure concurrent multipart uploads [#128746](https://github.com/elastic/elasticsearch/pull/128746)
* Limit number of suppressed S3 deletion errors [#123630](https://github.com/elastic/elasticsearch/pull/123630) (issue: [#123354](https://github.com/elastic/elasticsearch/issues/123354))
* Run `newShardSnapshotTask` tasks concurrently [#126452](https://github.com/elastic/elasticsearch/pull/126452)
* Throw better exception if verifying empty repo [#131677](https://github.com/elastic/elasticsearch/pull/131677)

Suggesters:
* Support duplicate suggestions in completion field [#121324](https://github.com/elastic/elasticsearch/pull/121324) (issue: [#82432](https://github.com/elastic/elasticsearch/issues/82432))

TLS:
* Watch SSL files instead of directories [#129738](https://github.com/elastic/elasticsearch/pull/129738)

Transform:
* Check alias during update [#124825](https://github.com/elastic/elasticsearch/pull/124825)

Vector Search:
* Fix and test off-heap stats when using direct IO for accessing the raw vectors [#128615](https://github.com/elastic/elasticsearch/pull/128615)
* Fix filtered knn vector search when query timeouts are enabled [#129440](https://github.com/elastic/elasticsearch/pull/129440)
* Fix top level knn search with scroll [#126035](https://github.com/elastic/elasticsearch/pull/126035)
