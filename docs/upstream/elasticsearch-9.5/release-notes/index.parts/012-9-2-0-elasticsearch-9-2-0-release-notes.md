<!-- Part 12 of 18 of release-notes/index.md (split because the page is big). -->

## 9.2.0 [elasticsearch-9.2.0-release-notes]

### Highlights [elasticsearch-9.2.0-highlights]

::::{dropdown} Enable Failure Store for new logs data streams
The [Failure Store](docs-content://manage-data/data-store/data-streams/failure-store.md) is now enabled by default for new logs data streams matching the pattern `logs-*-*`. This means that such data streams will now store invalid documents in a
dedicated failure index instead of rejecting them, allowing better visibility and control over data quality issues without loosing data. This can be [enabled manually](docs-content://manage-data/data-store/data-streams/failure-store.md#set-up-failure-store-existing) for existing data streams. 
Note: With the failure store enabled, the http response code clients receive when indexing invalid documents will change from `400 Bad Request` to `201 Created`, with an additional response attribute `"failure_store" : "used"`.
::::

::::{dropdown} Add support for Lookup Join on Multiple Fields
Add support for Lookup Join on Multiple Fields e.g. FROM index1
| LOOKUP JOIN lookup_index on field1, field2
::::

::::{dropdown} Safely prevent overwriting objects in S3 repositories
Earlier versions of Elasticsearch had a small risk of inadvertently overwriting an object in an [AWS S3 snapshot
repository](docs-content://deploy-manage/tools/snapshot-and-restore/s3-repository.md) which, if it happened, might corrupt the
repository contents. From version 9.2.0 onwards, Elasticsearch uses S3's [conditional write
feature](https://docs.aws.amazon.com/AmazonS3/latest/userguide/conditional-writes.html) to prevent this corruption.

If you are using a snapshot repository with type `s3` backed by some storage which is not AWS S3, but which is fully S3-compatible,
then you will also get the benefits of this corruption protection by upgrading to 9.2.0 or later. Refer to [S3-compatible
services](docs-content://deploy-manage/tools/snapshot-and-restore/s3-repository.md#repository-s3-compatible-services) for more
information about using Elasticsearch with S3-compatible storage services.
::::

::::{dropdown} Add support for expressions with LOOKUP JOIN in tech preview
Enable Lookup Join on Expression Tech Preview
FROM index1 | LOOKUP JOIN lookup_index on left_field1 > right_field1 AND left_field2 <= right_field2
::::

::::{dropdown} Release DiskBBQ(`bbq_disk`) index type for `dense_vector` fields
This provides a new index type called DiskBBQ (`bbq_disk`).
DiskBBQ is a cluster based format that provides:
  - faster and cheaper indexing than HNSW
  - Better behavior in lower memory environments (degrades linearly, not exponentially)
  - Is near HNSW for QPS when the index is in memory

Current restrictions:
  - only floating point values are allowed currently
  - quantization is only to a single bit, so not recommended for low dimensionality vectors
  - all other restrictions that exist for `dense_vector` fields still apply

To utilize the format, its just like any other:

```yaml
PUT vectors
 {
   "mappings": {
     "properties": {
       "vector": {"type": "dense_vector", "index_options": {"type": "disk_bbq"}
     }
   }
 }
```

 Querying is just like any other field.

```yaml
POST vectors/_search{
  "query": {
    "knn": {
      "field": "vector",
      "query_vector": <vector>,
      "k": 3
    }
  }
}
```

`num_candidates` can be used for tuning approximate nature of the search.
Or, more granular control can be provided by setting `visit_percentage` directly.
::::

::::{dropdown} Enable INLINE STATS in non-snapshot builds
This effectively releases INLINE STATS into tech preview.
- Enable the lexing/grammar for INLINE STATS in non-snapshot builds.
- Enable more tests with FORK and INLINE STATS
::::

::::{dropdown} Allow direct IO for BBQ rescoring
BBQ rescoring performance can be drastically affected by the amount of available
off-heap RAM for use by the system page cache. When there is not enough off-heap RAM
to fit all the vector data in memory, BBQ search latencies can be affected by as much as 5000x.
Specifying the `vector.rescoring.directio=true` Java option on all vector search
nodes modifies rescoring to use direct IO, which eliminates these very high latencies
from searches in low-memory scenarios, at a cost of a reduction
in vector search performance for BBQ indices when the vectors do all fit in memory.

This option is released in 9.1 as a tech preview whilst we analyse its effect
for a variety of use cases.
::::

::::{dropdown} Add remote index support to LOOKUP JOIN
Queries containing LOOKUP JOIN now can be preformed on cross-cluster indices, for example:

```yaml
FROM logs-*, remote:logs-* | LOOKUP JOIN clients on ip | SORT timestamp | LIMIT 100
```
::::

::::{dropdown} New lucene 10.3.0 release
- Improved performance for lexical, vector and primary-key searches
- Use optimistic-with-checking KNN Query execution strategy in place of cross-thread global queue min-score checking. Improves performance and consistency.
- Bulk scoring added for floating point vectors in HNSW. Improving query latency and indexing throughput
- Multiple improvements to HNSW graph traversal and storage
::::

### Features and enhancements [elasticsearch-9.2.0-features-enhancements]

Allocation:
* Add second max queue latency stat to `ClusterInfo` [#132675](https://github.com/elastic/elasticsearch/pull/132675)

Authentication:
* Add attribute count to `SamlAttribute` `toString` [#131173](https://github.com/elastic/elasticsearch/pull/131173)
* Allow configuring SAML private attributes [#133154](https://github.com/elastic/elasticsearch/pull/133154)
* Correct slow log user for RCS 2.0 [#130140](https://github.com/elastic/elasticsearch/pull/130140)

Authorization:
* Add DLS stats to `_security/stats` [#135271](https://github.com/elastic/elasticsearch/pull/135271)
* Add hits and misses timing stats to DLS cache [#133314](https://github.com/elastic/elasticsearch/pull/133314)
* Add new `/_security/stats` endpoint [#134835](https://github.com/elastic/elasticsearch/pull/134835)
* Expose existing DLS cache x-pack usage statistics [#132845](https://github.com/elastic/elasticsearch/pull/132845)
* Lazy compute and cache `grantsAll` per privilege [#136684](https://github.com/elastic/elasticsearch/pull/136684)
* [Cyera] Add `manage`, `create_index`, `read`, `index`, `write`, `delete`, permission for third party agent indices `kibana_system` [#134894](https://github.com/elastic/elasticsearch/pull/134894) (issue: [#134183](https://github.com/elastic/elasticsearch/issues/134183))
* [Security] Add entity store and asset criticality index privileges to built in Editor, Viewer and Kibana System roles [#129662](https://github.com/elastic/elasticsearch/pull/129662)

Codec:
* Push down compute engine value loading of long based singleton numeric doc value to the es819 tsdb doc values codec. [#132622](https://github.com/elastic/elasticsearch/pull/132622)
* Push down loading of singleton dense double based field types to the … [#133397](https://github.com/elastic/elasticsearch/pull/133397)
* Skip iterating DISI when reading metric values [#133365](https://github.com/elastic/elasticsearch/pull/133365)

Data streams:
* DLM: Better `max_age` rollover for tiny retentions [#134941](https://github.com/elastic/elasticsearch/pull/134941) (issue: [#130960](https://github.com/elastic/elasticsearch/issues/130960))
* ES-11331 streams params restriction [#132967](https://github.com/elastic/elasticsearch/pull/132967)
* Enable Failure Store for new logs-*-* data streams [#131261](https://github.com/elastic/elasticsearch/pull/131261) (issue: [#131105](https://github.com/elastic/elasticsearch/issues/131105))
* Enable failure store for newly created OTel data streams [#131395](https://github.com/elastic/elasticsearch/pull/131395)
* Only Allow Enabling Streams If No Conflicting Indices Exist [#132064](https://github.com/elastic/elasticsearch/pull/132064)
* Restrict Indexing To Child Streams When Streams Is Enabled [#132011](https://github.com/elastic/elasticsearch/pull/132011)

Distributed:
* Run `TransportClusterStateAction` on local node [#129872](https://github.com/elastic/elasticsearch/pull/129872)

Downsampling:
* [Downsampling++] Add time series telemetry in xpack usage [#134214](https://github.com/elastic/elasticsearch/pull/134214) (issue: [#133953](https://github.com/elastic/elasticsearch/issues/133953))

ES|QL:
* Accept unsigned longs on MAX and MIN aggregations [#131694](https://github.com/elastic/elasticsearch/pull/131694)
* Add Dependency Checker for `LogicalLocalPlanOptimizer` [#130409](https://github.com/elastic/elasticsearch/pull/130409)
* Add SET instruction [#134029](https://github.com/elastic/elasticsearch/pull/134029)
* Add checks that optimizers do not modify the layout [#130855](https://github.com/elastic/elasticsearch/pull/130855) (issue: [#125576](https://github.com/elastic/elasticsearch/issues/125576))
* Add fast path for single value in VALUES aggregator [#130510](https://github.com/elastic/elasticsearch/pull/130510)
* Add optimized path for intermediate values aggregator [#131390](https://github.com/elastic/elasticsearch/pull/131390)
* Add query heads priority to `SliceQueue` [#133245](https://github.com/elastic/elasticsearch/pull/133245)
* Add remote index support to LOOKUP JOIN [#129013](https://github.com/elastic/elasticsearch/pull/129013)
* Add support for LOOKUP JOIN on multiple fields [#131559](https://github.com/elastic/elasticsearch/pull/131559)
* Add support for RLIKE (LIST) with pushdown [#129929](https://github.com/elastic/elasticsearch/pull/129929)
* Add support for `include_execution_metadata` parameter [#134446](https://github.com/elastic/elasticsearch/pull/134446)
* Add support for expressions with LOOKUP JOIN in tech preview [#134952](https://github.com/elastic/elasticsearch/pull/134952)
* Add telemetry support for Lookup Join On Expression [#134942](https://github.com/elastic/elasticsearch/pull/134942)
* Adding Contains ESQL String function [#133016](https://github.com/elastic/elasticsearch/pull/133016)
* Adds the `v_hamming` function for calculating the Hamming distance between two dense vectors [#132959](https://github.com/elastic/elasticsearch/pull/132959) (issue: [#132056](https://github.com/elastic/elasticsearch/issues/132056))
* Adopt a "LogicalPlan" approach to running multiple sub-queries (with INLINESTATS so far) [#128917](https://github.com/elastic/elasticsearch/pull/128917)
* Allow pruning columns added by `InlineJoin` [#131204](https://github.com/elastic/elasticsearch/pull/131204)
* Allow remote enrich after LOOKUP JOIN [#131940](https://github.com/elastic/elasticsearch/pull/131940)
* Consider min/max from predicates when transform date_trunc/bucket to `round_to` [#131341](https://github.com/elastic/elasticsearch/pull/131341)
* Consider min/max from predicates when transform date_trunc/bucket to `round_to` option 2 [#132143](https://github.com/elastic/elasticsearch/pull/132143)
* ES|QL - Allow multivalued query parameters [#134317](https://github.com/elastic/elasticsearch/pull/134317)
* ES|QL - KNN function [#135709](https://github.com/elastic/elasticsearch/pull/135709)
* ES|QL - add `dense_vector` field type [#135604](https://github.com/elastic/elasticsearch/pull/135604)
* ES|QL Absent and `AbsentOverTime` functions [#134475](https://github.com/elastic/elasticsearch/pull/134475) (issue: [#131069](https://github.com/elastic/elasticsearch/issues/131069))
* Enable `date` `date_nanos` implicit casting [#133369](https://github.com/elastic/elasticsearch/pull/133369)
* Esql `mv_contains` function [#133636](https://github.com/elastic/elasticsearch/pull/133636)
* Esql skip null metrics [#133087](https://github.com/elastic/elasticsearch/pull/133087) (issue: [#129524](https://github.com/elastic/elasticsearch/issues/129524))
* Fail `profile` on text response formats [#128627](https://github.com/elastic/elasticsearch/pull/128627)
* Implement `v_magnitude` function [#132765](https://github.com/elastic/elasticsearch/pull/132765) (issue: [#132768](https://github.com/elastic/elasticsearch/issues/132768))
* Improve Expanding Lookup Join performance by pushing a filter to the right side of the lookup join [#133166](https://github.com/elastic/elasticsearch/pull/133166)
* Improve cpu utilization with dynamic slice size in doc partitioning [#132774](https://github.com/elastic/elasticsearch/pull/132774)
* Integrate LIKE/RLIKE LIST with `ReplaceStringCasingWithInsensitiveRegexMatch` rule [#131531](https://github.com/elastic/elasticsearch/pull/131531)
* LOOKUP JOIN with expressions [#134098](https://github.com/elastic/elasticsearch/pull/134098)
* Make FUSE available in release builds [#135603](https://github.com/elastic/elasticsearch/pull/135603)
* Make INLINESTATS (and subplans) work with CCS [#134323](https://github.com/elastic/elasticsearch/pull/134323) (issue: [#124748](https://github.com/elastic/elasticsearch/issues/124748))
* Make `_tsid` available in metadata [#135204](https://github.com/elastic/elasticsearch/pull/135204) (issue: [#133205](https://github.com/elastic/elasticsearch/issues/133205))
* Performance improvements for Lookup Join on Expression [#135036](https://github.com/elastic/elasticsearch/pull/135036)
* Remove unnecessary calls to Fold [#130944](https://github.com/elastic/elasticsearch/pull/130944) (issue: [#119756](https://github.com/elastic/elasticsearch/issues/119756))
* Replace "representable" type error messages [#131775](https://github.com/elastic/elasticsearch/pull/131775)
* Replace `RoundTo` linear search evaluator with manual evaluators [#131733](https://github.com/elastic/elasticsearch/pull/131733)
* Rewrite `RoundTo` to `QueryAndTags` [#132512](https://github.com/elastic/elasticsearch/pull/132512)
* Run single phase aggregation when possible [#131485](https://github.com/elastic/elasticsearch/pull/131485)
* Some optimizations for constant blocks [#132456](https://github.com/elastic/elasticsearch/pull/132456)
* Speed up loading keyword fields with index sorts [#132950](https://github.com/elastic/elasticsearch/pull/132950)
* Speed up reading multivalued keywords [#131061](https://github.com/elastic/elasticsearch/pull/131061)
* Substitue `date_trunc` with `round_to` when the pre-calculated rounding points are available [#128639](https://github.com/elastic/elasticsearch/pull/128639)
* Support filters on inlinestats [#132934](https://github.com/elastic/elasticsearch/pull/132934)
* Support geohash, geotile and geohex grid types [#129581](https://github.com/elastic/elasticsearch/pull/129581)
* Support geohash, geotile and geohex grid types in ST_INTERSECTS and ST_DISJOINT [#133546](https://github.com/elastic/elasticsearch/pull/133546)
* Take INLINE STATS out of snapshot [#135403](https://github.com/elastic/elasticsearch/pull/135403)

ILM+SLM:
* Add `age_in_millis` to ILM Explain Response [#128866](https://github.com/elastic/elasticsearch/pull/128866) (issue: [#103659](https://github.com/elastic/elasticsearch/issues/103659))
* Enhancement: ILM sets `indexing_complete` to true from `ReadOnly` action [#129945](https://github.com/elastic/elasticsearch/pull/129945)
* ILM: Force merge on zero-replica cloned index before snapshotting for searchable snapshots [#133954](https://github.com/elastic/elasticsearch/pull/133954) (issue: [#75478](https://github.com/elastic/elasticsearch/issues/75478))

Indices APIs:
* Add index mode to resolve index response [#132858](https://github.com/elastic/elasticsearch/pull/132858)
* Add mode filter to _resolve/index [#133616](https://github.com/elastic/elasticsearch/pull/133616)

Inference:
* Added support to configure query timeout for inference [#131551](https://github.com/elastic/elasticsearch/pull/131551)

Infra/Core:
* Add .integration_knowledge system index for usage by AI assistants [#132506](https://github.com/elastic/elasticsearch/pull/132506)
* Extend kibana-system permissions to manage security entities [#133968](https://github.com/elastic/elasticsearch/pull/133968)
* Make `SecureString` comparisons constant time [#135053](https://github.com/elastic/elasticsearch/pull/135053)
* Support Fields API in conditional ingest processors [#131581](https://github.com/elastic/elasticsearch/pull/131581)
* Use java8 variant of apm-agent [#132651](https://github.com/elastic/elasticsearch/pull/132651)

Infra/Metrics:
* Upgrade apm-agent to 1.55.0 [#131510](https://github.com/elastic/elasticsearch/pull/131510)

Ingest Node:
* Add `copy_from` option to the Append processor [#132003](https://github.com/elastic/elasticsearch/pull/132003)
* Add classes to represent raw docs sampling configs [#134585](https://github.com/elastic/elasticsearch/pull/134585)
* Add option for Append Processor to skip/allow empty values [#105718](https://github.com/elastic/elasticsearch/pull/105718) (issue: [#104813](https://github.com/elastic/elasticsearch/issues/104813))
* Add recover_failure_document processor to remediate failurestore docs [#133360](https://github.com/elastic/elasticsearch/pull/133360)
* Adding a `merge_type` parameter to the ingest simulate API [#132210](https://github.com/elastic/elasticsearch/pull/132210) (issue: [#131608](https://github.com/elastic/elasticsearch/issues/131608))
* Adding simulate ingest effective mapping [#132833](https://github.com/elastic/elasticsearch/pull/132833)
* Component Templates: Add created and modified date [#131536](https://github.com/elastic/elasticsearch/pull/131536)
* Enable failure store for newly created APM datastreams [#131296](https://github.com/elastic/elasticsearch/pull/131296)
* Handle structured log messages [#131027](https://github.com/elastic/elasticsearch/pull/131027) (issue: [#130333](https://github.com/elastic/elasticsearch/issues/130333))
* Index template: Add created_date and modified_date [#132083](https://github.com/elastic/elasticsearch/pull/132083)
* Pipelines: Add `created_date` and `modified_date` [#130847](https://github.com/elastic/elasticsearch/pull/130847)
* Remove ingest conditionals `_type` deprecation warning [#134851](https://github.com/elastic/elasticsearch/pull/134851)

License:
* Improve scalability of get-license action [#134457](https://github.com/elastic/elasticsearch/pull/134457)

Machine Learning:
* Add ContextualAI Rerank Service Implementation to the Inference API [#134933](https://github.com/elastic/elasticsearch/pull/134933)
* Add `RerankRequestChunker` [#130485](https://github.com/elastic/elasticsearch/pull/130485)
* Add support for dimensions in google vertex ai request [#132689](https://github.com/elastic/elasticsearch/pull/132689)
* Added AI21 Completion and Chat Completion support to the Inference Plugin [#113757](https://github.com/elastic/elasticsearch/pull/113757)
* Added Google Model Garden Anthropic Completion and Chat Completion support to the Inference Plugin [#134080](https://github.com/elastic/elasticsearch/pull/134080)
* Added Llama provider support to the Inference Plugin [#130092](https://github.com/elastic/elasticsearch/pull/130092)
* Adding custom headers support openai text embeddings [#134960](https://github.com/elastic/elasticsearch/pull/134960)
* Adding headers support for OpenAI chat completion [#134504](https://github.com/elastic/elasticsearch/pull/134504)
* Block trained model updates from inference [#130940](https://github.com/elastic/elasticsearch/pull/130940) (issue: [#129999](https://github.com/elastic/elasticsearch/issues/129999))
* Cache Inference Endpoints [#133860](https://github.com/elastic/elasticsearch/pull/133860) (issue: [#133135](https://github.com/elastic/elasticsearch/issues/133135))
* Enable force inference endpoint deleting for invalid models and after stopping model deployment fails [#129090](https://github.com/elastic/elasticsearch/pull/129090)
* Remove upper limit for chunking settings [#133718](https://github.com/elastic/elasticsearch/pull/133718)
* Support Gemini thinking budget in inference API [#133599](https://github.com/elastic/elasticsearch/pull/133599)
* Supporting more timestamp formats in `_text_structure/find_structure` [#133745](https://github.com/elastic/elasticsearch/pull/133745)
* Track inference deployments [#131442](https://github.com/elastic/elasticsearch/pull/131442)
* [ML] Add Azure AI Rerank support to the Inference Plugin [#129848](https://github.com/elastic/elasticsearch/pull/129848)
* [ML] Add IBM watsonx Completion and Chat Completion support to the Inference Plugin [#129146](https://github.com/elastic/elasticsearch/pull/129146)

Mapping:
* Add new `pattern_text` field mapper in tech preview [#135370](https://github.com/elastic/elasticsearch/pull/135370)
* Adds transport-only flag to always include indices in the field caps transport response [#133074](https://github.com/elastic/elasticsearch/pull/133074)
* Improve block loader for source only runtime IP fields [#135393](https://github.com/elastic/elasticsearch/pull/135393)
* Improve block loader for source only runtime date fields [#135373](https://github.com/elastic/elasticsearch/pull/135373)
* Improve block loader for source only runtime fields of type double [#134629](https://github.com/elastic/elasticsearch/pull/134629)
* Improve block loader for source only runtime fields of type keyword [#135026](https://github.com/elastic/elasticsearch/pull/135026)
* Improve block loader for source only runtime fields of type long [#134117](https://github.com/elastic/elasticsearch/pull/134117)
* Optimize `dotCount` in expanding dot parser [#135263](https://github.com/elastic/elasticsearch/pull/135263)
* Runtime fields: pass down runtime field name as source filter when source mode is synthetic [#133897](https://github.com/elastic/elasticsearch/pull/133897)
* Use optimized field visitor for ignored source queries [#135039](https://github.com/elastic/elasticsearch/pull/135039)

Network:
* Add audit logging for stream content [#130594](https://github.com/elastic/elasticsearch/pull/130594)
* Allow adjustment of transport TLS handshake timeout [#130909](https://github.com/elastic/elasticsearch/pull/130909)
* Differentiate between initial and reconnect RCS connections [#134415](https://github.com/elastic/elasticsearch/pull/134415)
* Expose HTTP connection metrics to telemetry [#130939](https://github.com/elastic/elasticsearch/pull/130939)
* Return 429 instead of 500 for timeout handlers [#133111](https://github.com/elastic/elasticsearch/pull/133111)

Performance:
* Optimize `BytesArray::indexOf,` which is used heavily in ndjson parsing [#135087](https://github.com/elastic/elasticsearch/pull/135087)

Relevance:
* Add support for extended search usage telemetry [#135306](https://github.com/elastic/elasticsearch/pull/135306)
* Add support for weighted RRF in retrievers [#130658](https://github.com/elastic/elasticsearch/pull/130658)
* Enable `chunk_rescorer` in `text_similarity_reranker` [#135198](https://github.com/elastic/elasticsearch/pull/135198)
* Support querying multiple indices with the simplified RRF retriever [#134822](https://github.com/elastic/elasticsearch/pull/134822)
* Support querying multiple indices with the simplified linear retriever [#133720](https://github.com/elastic/elasticsearch/pull/133720)
* Support semantic reranking using contextual snippets instead of entire field text [#129369](https://github.com/elastic/elasticsearch/pull/129369)
* Text similarity reranker chunks and scores snippets [#133576](https://github.com/elastic/elasticsearch/pull/133576)

Search:
* Add executor name attribute to cache miss metrics [#135635](https://github.com/elastic/elasticsearch/pull/135635)
* Add file extension metadata to cache miss counter from `SharedBlobCacheService` [#134374](https://github.com/elastic/elasticsearch/pull/134374)
* Add relevant attributes to search took time APM metrics [#134232](https://github.com/elastic/elasticsearch/pull/134232)
* Add relevant attributes to shard search latency APM metrics [#134798](https://github.com/elastic/elasticsearch/pull/134798)
* Add support for per-field weights in simplified RRF retriever syntax [#132680](https://github.com/elastic/elasticsearch/pull/132680)
* Add time range bucketing attribute to APM shard search latency metrics [#135524](https://github.com/elastic/elasticsearch/pull/135524)
* Add top level normalizer for linear retriever [#129693](https://github.com/elastic/elasticsearch/pull/129693)
* Adds sparse vector index options settings to semantic_text field [#131058](https://github.com/elastic/elasticsearch/pull/131058)
* DFS search phase per shard duration APM metric [#135652](https://github.com/elastic/elasticsearch/pull/135652)
* Introduce new rescorer based on script [#74274](https://github.com/elastic/elasticsearch/pull/74274) (issue: [#52338](https://github.com/elastic/elasticsearch/issues/52338))
* Refresh potential lost connections at query start for `_search` [#130463](https://github.com/elastic/elasticsearch/pull/130463)
* Refresh potential lost connections at query start for field caps [#131517](https://github.com/elastic/elasticsearch/pull/131517)
* Support nested fields for term vectors API when using artificial documents [#92568](https://github.com/elastic/elasticsearch/pull/92568) (issue: [#91902](https://github.com/elastic/elasticsearch/issues/91902))
* Update to lucene 10.3.1 [#136030](https://github.com/elastic/elasticsearch/pull/136030)
* Upgrade elasticsearch to lucene 10.3.0 [#133980](https://github.com/elastic/elasticsearch/pull/133980)

Searchable Snapshots:
* Add cache miss and read metrics [#132497](https://github.com/elastic/elasticsearch/pull/132497)
* Add epoch blob-cache metric [#132547](https://github.com/elastic/elasticsearch/pull/132547)

Security:
* Add `LoadedSecureSettings` for keeping temporary secure settings loaded [#134349](https://github.com/elastic/elasticsearch/pull/134349)
* Add read permissions for osquery manager result indices [#130824](https://github.com/elastic/elasticsearch/pull/130824)
* Add signing configuration for cross cluster api keys [#134137](https://github.com/elastic/elasticsearch/pull/134137)
* Add trust configuration for cross cluster api keys [#134893](https://github.com/elastic/elasticsearch/pull/134893)
* Do not pass `ProjectMetadata` to lazy index permissions builder [#135337](https://github.com/elastic/elasticsearch/pull/135337)

Snapshot/Restore:
* Add extension points to remediate index metadata in during snapshot restore [#131706](https://github.com/elastic/elasticsearch/pull/131706)
* Expose S3 connection max idle time as a setting [#125552](https://github.com/elastic/elasticsearch/pull/125552)
* Improve lost-increment message in repo analysis [#131200](https://github.com/elastic/elasticsearch/pull/131200)
* Safely prevent overwriting objects in S3 repositories [#133030](https://github.com/elastic/elasticsearch/pull/133030) (issue: [#128565](https://github.com/elastic/elasticsearch/issues/128565))

Store:
* Add new `CachePopulationReason` [#130593](https://github.com/elastic/elasticsearch/pull/130593)
* Improve `ShardLockObtainFailedException` message [#134198](https://github.com/elastic/elasticsearch/pull/134198)

TLS:
* Add 'SslProfileExtension' SPI interface [#134609](https://github.com/elastic/elasticsearch/pull/134609)
* Add reload listener to `SslProfile` [#135244](https://github.com/elastic/elasticsearch/pull/135244)

TSDB:
* Add index setting that disables the `index.dimensions` based routing and `_tsid` creation strategy [#135673](https://github.com/elastic/elasticsearch/pull/135673)
* Add ordinal range encode for tsid [#133018](https://github.com/elastic/elasticsearch/pull/133018)
* Adds an OTLP metrics endpoint (`_otlp/v1/metrics`) as tech preview [#135401](https://github.com/elastic/elasticsearch/pull/135401)
* Improve TSDB ingestion by hashing dimensions only once, using a new auto-populeted `index.dimensions` private index setting [#135402](https://github.com/elastic/elasticsearch/pull/135402)

Vector Search:
* Add 'profile' support for knn query on HNSW with early termination [#135342](https://github.com/elastic/elasticsearch/pull/135342)
* Add GPUPlugin for indexing vectors on GPU [#135545](https://github.com/elastic/elasticsearch/pull/135545)
* Add low-level optimized Neon, AVX2, and AVX 512 float32 vector operations [#130635](https://github.com/elastic/elasticsearch/pull/130635)
* Add support for retrieving semantic_text's indexed chunks via fields API [#132410](https://github.com/elastic/elasticsearch/pull/132410)
* Add usage stats for `semantic_text` fields [#135262](https://github.com/elastic/elasticsearch/pull/135262)
* Allow direct IO for BBQ rescoring [#125921](https://github.com/elastic/elasticsearch/pull/125921)
* Allow including semantic field embeddings in `_source` [#134717](https://github.com/elastic/elasticsearch/pull/134717)
* Enable caching of all filters in `knn` queries [#134458](https://github.com/elastic/elasticsearch/pull/134458)
* Enable semantic search CCS when ccs_minimize_roundtrips=true [#135309](https://github.com/elastic/elasticsearch/pull/135309)
* Ensure vectors are always included in reindex actions [#130834](https://github.com/elastic/elasticsearch/pull/130834)
* Release DiskBBQ(`bbq_disk`) index type for `dense_vector` fields [#135299](https://github.com/elastic/elasticsearch/pull/135299)
* Remove vectors from `_source` transparently [#130382](https://github.com/elastic/elasticsearch/pull/130382)
* Speed up (filtered) KNN queries for flat vector fields [#130251](https://github.com/elastic/elasticsearch/pull/130251)
* Speed up `OptimizedScalarQuantizer` [#131599](https://github.com/elastic/elasticsearch/pull/131599)
* Support kNN filter on nested metadata [#113949](https://github.com/elastic/elasticsearch/pull/113949) (issues: [#128803](https://github.com/elastic/elasticsearch/issues/128803), [#106994](https://github.com/elastic/elasticsearch/issues/106994))
* Support using the semantic query across multiple inference IDs [#133675](https://github.com/elastic/elasticsearch/pull/133675)
* Wrap ES KNN queries with PatienceKNN query [#127223](https://github.com/elastic/elasticsearch/pull/127223)


### Fixes [elasticsearch-9.2.0-fixes]

Allocation:
* Make forecast write load accurate when shard numbers change [#129990](https://github.com/elastic/elasticsearch/pull/129990)

Analysis:
* Adding check for `isIndexed` in text fields when generating field exists queries to avoid ISE when field is stored but not indexed or with `doc_values` [#130531](https://github.com/elastic/elasticsearch/pull/130531)
* Avoid internal server error when suggester requires unigrams but no unigrams are provided, return bad request instead [#132321](https://github.com/elastic/elasticsearch/pull/132321) (issue: [#131928](https://github.com/elastic/elasticsearch/issues/131928))

Authorization:
* Drop project-id from threadcontext for CCS [#136664](https://github.com/elastic/elasticsearch/pull/136664)

Cluster Coordination:
* Avoid stack overflow in `IndicesClusterStateService` `applyClusterState` [#132536](https://github.com/elastic/elasticsearch/pull/132536)

Codec:
* Fix disk usage estimation for SORTED_SET doc values [#133722](https://github.com/elastic/elasticsearch/pull/133722)

Data streams:
* Add existing shards allocator settings to failure store allowed list [#131056](https://github.com/elastic/elasticsearch/pull/131056)
* Fix service destination template file name [#133403](https://github.com/elastic/elasticsearch/pull/133403)
* Using index setting providers for data stream setting validation [#136214](https://github.com/elastic/elasticsearch/pull/136214) (issue: [#136166](https://github.com/elastic/elasticsearch/issues/136166))

Distributed:
* Fix race condition in `RemoteClusterService.collectNodes()` [#131937](https://github.com/elastic/elasticsearch/pull/131937)

ES|QL:
* Add error message when using inline stats on TS [#136348](https://github.com/elastic/elasticsearch/pull/136348) (issue: [#136092](https://github.com/elastic/elasticsearch/issues/136092))
* Avoid rewrite `round_to` with expensive queries [#135987](https://github.com/elastic/elasticsearch/pull/135987)
* Create new block when filter `OrdinalBytesRefBlock` [#136444](https://github.com/elastic/elasticsearch/pull/136444) (issue: [#136423](https://github.com/elastic/elasticsearch/issues/136423))
* Fix FORK with union-types [#134033](https://github.com/elastic/elasticsearch/pull/134033) (issue: [#133973](https://github.com/elastic/elasticsearch/issues/133973))
* Fix `AsyncOperator` status values and add emitted rows [#132738](https://github.com/elastic/elasticsearch/pull/132738)
* Fix a breaker bug [#136105](https://github.com/elastic/elasticsearch/pull/136105) (issues: [#135224](https://github.com/elastic/elasticsearch/issues/135224), [#135260](https://github.com/elastic/elasticsearch/issues/135260))
* Fix alias id when drop all aggregates [#135247](https://github.com/elastic/elasticsearch/pull/135247)
* Fix async operator warnings not always sent when blocking [#132744](https://github.com/elastic/elasticsearch/pull/132744) (issues: [#130642](https://github.com/elastic/elasticsearch/issues/130642), [#132554](https://github.com/elastic/elasticsearch/issues/132554), [#132778](https://github.com/elastic/elasticsearch/issues/132778), [#130296](https://github.com/elastic/elasticsearch/issues/130296), [#132555](https://github.com/elastic/elasticsearch/issues/132555), [#131563](https://github.com/elastic/elasticsearch/issues/131563), [#131148](https://github.com/elastic/elasticsearch/issues/131148), [#132604](https://github.com/elastic/elasticsearch/issues/132604), [#128030](https://github.com/elastic/elasticsearch/issues/128030))
* Fix bug in topn [#133601](https://github.com/elastic/elasticsearch/pull/133601) (issues: [#133600](https://github.com/elastic/elasticsearch/issues/133600), [#133574](https://github.com/elastic/elasticsearch/issues/133574), [#133607](https://github.com/elastic/elasticsearch/issues/133607))
* Fix lookup index resolution when field-caps returns empty mapping [#132138](https://github.com/elastic/elasticsearch/pull/132138) (issue: [#132105](https://github.com/elastic/elasticsearch/issues/132105))
* Fix projection generation when pruning left join [#135446](https://github.com/elastic/elasticsearch/pull/135446)
* Fix union types lost attributes in `StubRelation` for inlinestats [#135547](https://github.com/elastic/elasticsearch/pull/135547)
* Fix: prevent duplication of "invalid index name" string in the final exception error message [#130027](https://github.com/elastic/elasticsearch/pull/130027)
* Fixes `countDistinctWithConditions` in csv-spec tests [#135097](https://github.com/elastic/elasticsearch/pull/135097) (issue: [#134380](https://github.com/elastic/elasticsearch/issues/134380))
* Handle right hand side of Inline Stats coming optimized with `LocalRelation` shortcut [#135011](https://github.com/elastic/elasticsearch/pull/135011)
* Limit when we push topn to lucene [#134497](https://github.com/elastic/elasticsearch/pull/134497)
* Make `ResolveUnionTypes` rule stateless [#136492](https://github.com/elastic/elasticsearch/pull/136492)
* Mark LOOKUP JOIN as `ExecutesOn.Any` by default [#133064](https://github.com/elastic/elasticsearch/pull/133064)
* Pass fix size instead of `maxPageSize` to `LuceneTopNOperator` scorer [#135767](https://github.com/elastic/elasticsearch/pull/135767)
* Replace any Attribute type when pushing down past Project [#135295](https://github.com/elastic/elasticsearch/pull/135295) (issue: [#134407](https://github.com/elastic/elasticsearch/issues/134407))
* Telemetry with inlinestats [#134309](https://github.com/elastic/elasticsearch/pull/134309)
* Throw 4xx instead of 5xx for ESQL malformed query params [#134879](https://github.com/elastic/elasticsearch/pull/134879) (issue: [#134618](https://github.com/elastic/elasticsearch/issues/134618))
* TopNOperator, release Row on failure [#130330](https://github.com/elastic/elasticsearch/pull/130330) (issue: [#130215](https://github.com/elastic/elasticsearch/issues/130215))
* [main]Prepare Index Like fix for backport to 9.1 and 8.19 [#130947](https://github.com/elastic/elasticsearch/pull/130947)

ILM+SLM:
* Add origin to client in SLM task [#135484](https://github.com/elastic/elasticsearch/pull/135484)
* Avoid counting snapshot failures twice in SLM [#136759](https://github.com/elastic/elasticsearch/pull/136759)
* Avoid running asynchronous ILM actions while ILM is stopped [#133683](https://github.com/elastic/elasticsearch/pull/133683) (issues: [#99859](https://github.com/elastic/elasticsearch/issues/99859), [#81234](https://github.com/elastic/elasticsearch/issues/81234), [#85097](https://github.com/elastic/elasticsearch/issues/85097))
* Correctly update SLM stats with master shutdown [#134152](https://github.com/elastic/elasticsearch/pull/134152)
* Fix log formatting in `SnapshotLifecycleTask` [#136709](https://github.com/elastic/elasticsearch/pull/136709)

Indices APIs:
* Reindex-from-remote: Validate basic auth params [#136501](https://github.com/elastic/elasticsearch/pull/136501) (issue: [#135925](https://github.com/elastic/elasticsearch/issues/135925))
* Updating `TransportSimulateIndexTemplateAction.resolveTemplate()` to account for data stream overrides [#132131](https://github.com/elastic/elasticsearch/pull/132131) (issue: [#131425](https://github.com/elastic/elasticsearch/issues/131425))

Infra/Core:
* Fix offset handling in Murmur3Hasher [#133193](https://github.com/elastic/elasticsearch/pull/133193)

Infra/Scripting:
* Fixed GeneralScriptException to return 400 http status code [#133659](https://github.com/elastic/elasticsearch/pull/133659)

Ingest Node:
* Add support for flexible access pattern to `NormalizeForStreamProcessor` [#134524](https://github.com/elastic/elasticsearch/pull/134524)
* Fix append processor `ignore_empty_values` edge case [#136649](https://github.com/elastic/elasticsearch/pull/136649)
* Fixing conditional processor mutability bugs [#134936](https://github.com/elastic/elasticsearch/pull/134936)

Logs:
* Fix logsdb settings provider mapping filters [#136119](https://github.com/elastic/elasticsearch/pull/136119) (issue: [#136107](https://github.com/elastic/elasticsearch/issues/136107))

Machine Learning:
* Add exception for perform embedding inference requests with query provided [#131641](https://github.com/elastic/elasticsearch/pull/131641)
* Adjust jinaai rerank response parser to handle document field as string or object [#136751](https://github.com/elastic/elasticsearch/pull/136751)
* Allow timeout during trained model download process [#129003](https://github.com/elastic/elasticsearch/pull/129003)
* Clean up inference indices on failed endpoint creation [#136577](https://github.com/elastic/elasticsearch/pull/136577) (issue: [#123726](https://github.com/elastic/elasticsearch/issues/123726))
* Cohere service Model Id field is required [#136017](https://github.com/elastic/elasticsearch/pull/136017)
* Ensure queued `AbstractRunnables` are notified when executor stops [#135966](https://github.com/elastic/elasticsearch/pull/135966) (issue: [#134651](https://github.com/elastic/elasticsearch/issues/134651))
* Fix model assignment error handling and assignment explanation generation [#133916](https://github.com/elastic/elasticsearch/pull/133916)
* Implementing latency improvements for EIS integration [#133861](https://github.com/elastic/elasticsearch/pull/133861)
* Improve memory estimation methods accuracy in `TrainedModelAssignmentRebalancer` and related classes [#133930](https://github.com/elastic/elasticsearch/pull/133930)
* Inference API disable partial search results [#132362](https://github.com/elastic/elasticsearch/pull/132362)
* Release cluster state [#136769](https://github.com/elastic/elasticsearch/pull/136769) (issue: [#123243](https://github.com/elastic/elasticsearch/issues/123243))
* Remove rate limit field from services API for EIS [#135838](https://github.com/elastic/elasticsearch/pull/135838)
* Return 429 status when `RequestExecutorService` queue full [#134178](https://github.com/elastic/elasticsearch/pull/134178)
* Sync Inference with Trained Model stats [#130544](https://github.com/elastic/elasticsearch/pull/130544) (issue: [#130339](https://github.com/elastic/elasticsearch/issues/130339))

Mapping:
* Store full path in `_ignored` when ignoring dynamic array field [#136315](https://github.com/elastic/elasticsearch/pull/136315)
* [Downsampling++] Allow merging of passthrough mappers with object mappers under certain conditions [#135431](https://github.com/elastic/elasticsearch/pull/135431)

Network:
* Fix `NullPointerException` in transport trace logger [#132243](https://github.com/elastic/elasticsearch/pull/132243)

Search:
* Adjust date docvalue formatting to return 4xx instead of 5xx [#132414](https://github.com/elastic/elasticsearch/pull/132414)
* Apply source excludes early when retrieving the `_inference_fields` [#135897](https://github.com/elastic/elasticsearch/pull/135897)
* Correct exception for missing nested path [#132408](https://github.com/elastic/elasticsearch/pull/132408)
* Handle special regex cases for version fields [#132511](https://github.com/elastic/elasticsearch/pull/132511)
* Initialize `TermsEnum` eagerly [#136279](https://github.com/elastic/elasticsearch/pull/136279)
* Support returning default `index_options` for `semantic_text` fields when `include_defaults` is true [#129967](https://github.com/elastic/elasticsearch/pull/129967)
* Switch to Sending a Bad Request User When Function Score Query Generates Negative Scores [#133357](https://github.com/elastic/elasticsearch/pull/133357) (issue: [#133358](https://github.com/elastic/elasticsearch/issues/133358))
* Tests for FORK's evaluation of field names used in `field_caps` resolve calls [#131723](https://github.com/elastic/elasticsearch/pull/131723)

Security:
* Configurable HTTP read and connect timeouts for url based SAML metadata resolution [#136058](https://github.com/elastic/elasticsearch/pull/136058)
* Optimize Index Permission Automatons for Has Privileges [#136625](https://github.com/elastic/elasticsearch/pull/136625)

TSDB:
* Fix warning when creating an OTel data stream [#133952](https://github.com/elastic/elasticsearch/pull/133952) (issue: [#132918](https://github.com/elastic/elasticsearch/issues/132918))

Transform:
* Fix stuck in STOPPING by retrying the startup task indefinitely until it succeeds [#132048](https://github.com/elastic/elasticsearch/pull/132048) (issue: [#128221](https://github.com/elastic/elasticsearch/issues/128221))

Vector Search:
* Bugfix 136545 [#136556](https://github.com/elastic/elasticsearch/pull/136556)
* Bugfix/disable matches highlight knn [#136563](https://github.com/elastic/elasticsearch/pull/136563)
* Cardinality Aggregator Throws `UnsupportedOperationException` When Field Type is Vector [#135994](https://github.com/elastic/elasticsearch/pull/135994)
* Fix _inference_fields handling on old indices [#136312](https://github.com/elastic/elasticsearch/pull/136312) (issue: [#136130](https://github.com/elastic/elasticsearch/issues/136130))
* Have top level knn searches tracked in query stats [#132548](https://github.com/elastic/elasticsearch/pull/132548)
