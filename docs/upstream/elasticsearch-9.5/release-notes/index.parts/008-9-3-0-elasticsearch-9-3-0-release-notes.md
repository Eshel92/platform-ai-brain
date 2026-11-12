<!-- Part 8 of 18 of release-notes/index.md (split because the page is big). -->

## 9.3.0 [elasticsearch-9.3.0-release-notes]

### Highlights [elasticsearch-9.3.0-highlights]

::::{dropdown} Add CEF processor to Ingest node
The `cef` ingest processor parses a CEF (Common Event Format) message into a structured JSON object. It follows the CEF specification to extract fields such as device vendor, device product, device version, signature ID, name, severity, and extension fields. This allows users to easily analyze and visualize CEF-formatted logs within Elasticsearch and Kibana.
::::

::::{dropdown} Evaluate time series aggregation functions over sliding windows
Time series aggregations in ES|QL can be optionally calculated over a sliding time window. Using a window
larger than the time bucket interval reduces jitter in dashboards, by taking a larger number of data points into
account.

Windows can be specified in all supported time series aggregations, as a second argument. For instance, the
following ES|QL query calculates the average rate of requests per host every minute, using a 10-minute window:

TS metrics
| WHERE TRANGE(1h)
| STATS avg(rate(requests, 10m)) BY TBUCKET(1m), host

Acceptable window values are currently limited to multiples of the time bucket value (e.g. `BUCKET` or `TBUCKET`),
as specified in the BY-clause. If no window is provided, it's implicitly set to the time bucket value,
matching existing behavior.
::::

::::{dropdown} New exponential_histogram field type for native OpenTelemetry exponential histogram support
A new `exponential_histogram` field type has been added to Elasticsearch, providing native support for
OpenTelemetry exponential histograms.

Exponential histograms offer an efficient way to collect distributions (e.g. response times) at a high compression
ratio while still maintaining good accuracy for percentile estimation. They can be easily collected via
OpenTelemetry SDKs, as the only required configuration is the maximum allowed number of buckets. The actual buckets will be
chosen automatically based on the observed values.

The new `exponential_histogram` field type is supported in ES|QL.
It can be aggregated using the `PERCENTILES`, `AVG`, `MIN`, `MAX` and `SUM` functions.
::::

::::{dropdown} New dense_vector options for storing bfloat16 vectors and utilising on-disk rescoring
New options have been added to the `dense_vector` field type.

The first is support for storing vectors in bfloat16 format.
This is a floating-point format that utilises two bytes per value rather than four, halving the storage space
required compared to `element_type: float`. This can be specified with `element_type: bfloat16`
when creating the index, for all `dense_vector` indexing types.

Float values are automatically rounded to two bytes when writing to disk, so this format can be used
with original source vectors at two- or four-byte precision. BFloat16 values are zero-expanded back to four-byte floats
when read into memory. Using `bfloat16` will cause a loss of precision compared to
the original vector values, as well as a small performance hit due to converting between `bfloat16` and `float`
when reading and writing vectors; however this may be counterbalanced by a corresponding decrease in I/O,
depending on your workload.

The second option is to enable on-disk rescoring. When rescoring vectors during kNN searches, the raw vectors
are read into memory. When the vector data is larger than the amount of available RAM, this might cause the OS
to evict some in-memory pages that then need to be paged back in immediately afterwards. This can cause
a significant slowdown in search speed. Enabling on-disk rescoring causes rescoring to use raw vector data
on-disk during rescoring, and to not read it into memory first. This can significantly increase search performance
in such low-memory situations.

Enable on-disk rescoring using the `on_disk_rescore: true` index option.
::::

::::{dropdown} Add compression for binary doc values
Add compression for binary doc values using Zstd and blocks with a variable number of values.

Block-wise LZ4 compression was previously added to Lucene in LUCENE-9211 and removed in LUCENE-9378 due to query performance issues.
This approach stored a constant number of values per block (specifically 32 values).
This made it easy to map a given value index (e.g., docId) to the block containing it by doing blockId = docId / 32.
Unfortunately, if values are very large, we must still have exactly 32 values per block, and (de)compressing a block could cause very high memory usage.
As a result, we had to keep the number of values small, meaning that in the average case, a block was much smaller than ideal.

To overcome the issues of blocks with a constant number of values, this PR adds block-wise compression with a variable number of values per block.
It stores a minimum of 1 document per block and stops adding values when the size of a block exceeds a threshold or the number of values exceeds a threshold.
Like the previous version, it stores an array of addresses for the start of each block.
Additionally, it stores a parallel array with the docId at the start of each block.
When looking up a given docId, if it is not in the current block, we binary search the array of docId starts to find the blockId containing the value.
We then look up the address of the block.
After this, decompression works very similarly to the code from LUCENE-9211; the main difference being that Zstd(1) is used instead of LZ4.

The introduction of binary doc value compression transparently affects wildcard field types, like URLs that are common in access logs, which will now compress much better.
::::

::::{dropdown} Enable doc_values skippers
Doc_values skippers add a sparse index to doc_values fields, allowing efficient
querying and filtering on a field without having to build a separate BKD or terms
index.  These are now enabled automatically on any field configured with
index=false and doc_values=true if the index setting `index.mapping.use_doc_values_skipper`
is set to `true` (default `false`, or `true` for TSDB indexes).

TSDB indexes now default to using skippers in place of indexes for their
@timestamp, dimension and  _tsid fields, greatly reducing their on-disk
footprint.  To disable skippers in TSDB indexes, set `index.mapping.use_doc_values_skipper`
to `false`.
::::

::::{dropdown} Enable large numeric blocks for TSDB codec
The size of numeric blocks gets increased from 128 to 512, for indices with [index.mode:time-series].
This mostly improves compression for multi-values in fields using sorted-set doc values, such as keyword and
ip fields, as run-length encoding covers more data for the same storage footprint.
::::

### Features and enhancements [elasticsearch-9.3.0-features-enhancements]

Aggregations:
* Let terms queries rewrite to a filter on `constant_keyword` fields [#139106](https://github.com/elastic/elasticsearch/pull/139106)

Allocation:
* Allocation: add balancer round summary as metrics [#136043](https://github.com/elastic/elasticsearch/pull/136043)
* Allocation: add duration and count metrics for write load hotspot [#138465](https://github.com/elastic/elasticsearch/pull/138465)
* Iterate directly over contents of `RoutingNode` [#137694](https://github.com/elastic/elasticsearch/pull/137694)
* Shard started reroute high priority [#137306](https://github.com/elastic/elasticsearch/pull/137306)
* Simulate shards moved by explicit commands [#136066](https://github.com/elastic/elasticsearch/pull/136066)
* Track `shardStarted` events for simulation in `DesiredBalanceComputer` [#135597](https://github.com/elastic/elasticsearch/pull/135597)

Authentication:
* Additional DEBUG logging on authc failures [#137941](https://github.com/elastic/elasticsearch/pull/137941)
* Improve SAML error handling by adding metadata [#137598](https://github.com/elastic/elasticsearch/pull/137598) (issue: [#128179](https://github.com/elastic/elasticsearch/issues/128179))
* In-response-to in saml successful response [#137599](https://github.com/elastic/elasticsearch/pull/137599) (issue: [#128179](https://github.com/elastic/elasticsearch/issues/128179))

Authorization:
* [Axonius] Add `manage`, `create_index`, `read`, `index`, `write`, `delete`, permission for third party agent indices `kibana_system` [#139345](https://github.com/elastic/elasticsearch/pull/139345)
* [Security Solution] Add additional privileges to Kibana System role for `.endpoint-scripts-file*` indexes [#139245](https://github.com/elastic/elasticsearch/pull/139245)
* [Security Solution] Add privileges to Kibana System role for management of internal indexes in support of Elastic Defend features [#138993](https://github.com/elastic/elasticsearch/pull/138993)

CCS:
* Add support for `project_routing` for `_search` and `_async_search` [#137566](https://github.com/elastic/elasticsearch/pull/137566)
* CPS usage telemetry support [#137705](https://github.com/elastic/elasticsearch/pull/137705)
* CPS: Enable flatworld search and `project_routing` for `_msearch` [#138822](https://github.com/elastic/elasticsearch/pull/138822)
* Do not assume we hear back from all linked projects when validating resolved index expressions for CPS [#137916](https://github.com/elastic/elasticsearch/pull/137916)
* MRT should default to `true` for CPS searches [#138105](https://github.com/elastic/elasticsearch/pull/138105)

Cluster Coordination:
* Add `ThreadWatchdog` to `ClusterApplierService` [#134361](https://github.com/elastic/elasticsearch/pull/134361)
* Report recent tasks updates when master starved [#139518](https://github.com/elastic/elasticsearch/pull/139518)

Codec:
* Enable large numeric blocks for TSDB codec in production [#139503](https://github.com/elastic/elasticsearch/pull/139503)
* Improved bulk loading for binary doc values [#138631](https://github.com/elastic/elasticsearch/pull/138631)
* Integrate stored fields format bloom filter with synthetic `_id` [#138515](https://github.com/elastic/elasticsearch/pull/138515)
* Simple bulk loading of compressed binary doc values [#138541](https://github.com/elastic/elasticsearch/pull/138541)

Data streams:
* Adding `match_only_text` subfield to `*.display_name` fields in `ecs@mappings` to be compliant with the latest additions in ECS [#136265](https://github.com/elastic/elasticsearch/pull/136265)
* Support choosing the downsampling method in data stream lifecycle [#137023](https://github.com/elastic/elasticsearch/pull/137023)

Distributed:
* Disk usage don't include synthetic `_id` postings [#138745](https://github.com/elastic/elasticsearch/pull/138745)
* `TransportGetBasicStatusAction` runs on local [#137567](https://github.com/elastic/elasticsearch/pull/137567)

Downsampling:
* Add new sampling method to the Downsample API [#136813](https://github.com/elastic/elasticsearch/pull/136813)
* Move force merge from the downsampling request to the ILM action and allow users to disable it. [#135834](https://github.com/elastic/elasticsearch/pull/135834)

EQL:
* Accept `project_routing` as query parameter [#138559](https://github.com/elastic/elasticsearch/pull/138559)
* Enable CPS [#137833](https://github.com/elastic/elasticsearch/pull/137833)

ES|QL:
* Add CHUNK function [#134320](https://github.com/elastic/elasticsearch/pull/134320)
* Add MV_INTERSECTION Function [#139379](https://github.com/elastic/elasticsearch/pull/139379)
* Add TOP_SNIPPETS function to return the best snippets for a field [#138940](https://github.com/elastic/elasticsearch/pull/138940)
* Add TRANGE ES|QL function [#136441](https://github.com/elastic/elasticsearch/pull/136441) (issue: [#135599](https://github.com/elastic/elasticsearch/issues/135599))
* Add `m` alias for `minute` duration literal [#136448](https://github.com/elastic/elasticsearch/pull/136448) (issue: [#135552](https://github.com/elastic/elasticsearch/issues/135552))
* Add `time_zone` request param support to KQL and QSTR functions [#138695](https://github.com/elastic/elasticsearch/pull/138695)
* Add optional parameters support to KQL function [#135895](https://github.com/elastic/elasticsearch/pull/135895) (issue: [#135823](https://github.com/elastic/elasticsearch/issues/135823))
* Add support for Full Text Functions and Lucene pushable conditions on fields from the Lookup Index for Lookup Join [#136104](https://github.com/elastic/elasticsearch/pull/136104)
* Allow single fork branch [#136805](https://github.com/elastic/elasticsearch/pull/136805) (issue: [#135825](https://github.com/elastic/elasticsearch/issues/135825))
* Avoid retrieving unnecessary fields on node-reduce phase [#137920](https://github.com/elastic/elasticsearch/pull/137920) (issue: [#134363](https://github.com/elastic/elasticsearch/issues/134363))
* ESQL - Add planning detailed timing to profile information [#138564](https://github.com/elastic/elasticsearch/pull/138564)
* ES|QL - Add TOP_SNIPPETS as tech preview [#139272](https://github.com/elastic/elasticsearch/pull/139272)
* ES|QL - Add vector similarity functions [#139365](https://github.com/elastic/elasticsearch/pull/139365)
* ES|QL - KNN function options support k and visit_percentage parameters [#138372](https://github.com/elastic/elasticsearch/pull/138372)
* ES|QL - Remove vectors from `_source` when applicable [#138013](https://github.com/elastic/elasticsearch/pull/138013)
* ES|QL Update CHUNK to support `chunking_settings` as optional argument [#138123](https://github.com/elastic/elasticsearch/pull/138123)
* ES|QL completion command constant folding [#138112](https://github.com/elastic/elasticsearch/pull/138112) (issue: [#136863](https://github.com/elastic/elasticsearch/issues/136863))
* Enable nullify and fail unmapped resolution in tech-preview [#140528](https://github.com/elastic/elasticsearch/pull/140528)
* Enable score function in release builds [#136988](https://github.com/elastic/elasticsearch/pull/136988)
* Enable the TEXT_EMBEDDING function in non-snapshot build [#136103](https://github.com/elastic/elasticsearch/pull/136103)
* Feature/count by trunc with filter [#138765](https://github.com/elastic/elasticsearch/pull/138765)
* Fill in topn values if competitive [#135734](https://github.com/elastic/elasticsearch/pull/135734)
* Fix a validation message in `TimeSeriesGroupByAll` [#139882](https://github.com/elastic/elasticsearch/pull/139882)
* Fix slowness in `ValuesFromManyReader.estimatedRamBytesUsed` [#139397](https://github.com/elastic/elasticsearch/pull/139397)
* Further simplify `SingleValueMatchQuery` [#136195](https://github.com/elastic/elasticsearch/pull/136195)
* Fuse MV_MIN and MV_MAX and document process [#138029](https://github.com/elastic/elasticsearch/pull/138029)
* GROUP BY ALL [#137367](https://github.com/elastic/elasticsearch/pull/137367)
* Group by all optimization [#139130](https://github.com/elastic/elasticsearch/pull/139130)
* Implement `network_direction` function [#136133](https://github.com/elastic/elasticsearch/pull/136133)
* Improve performance when a single-valued field filter gets pushed down. (SingleValueMatchQuery) [#135714](https://github.com/elastic/elasticsearch/pull/135714)
* Improve value loading for `match_only_text` mapping [#137026](https://github.com/elastic/elasticsearch/pull/137026)
* Inference command: support for CCS [#139244](https://github.com/elastic/elasticsearch/pull/139244) (issue: [#136860](https://github.com/elastic/elasticsearch/issues/136860))
* Introduce a new interface to declare functions depending on the `@timestamp` attribute [#137040](https://github.com/elastic/elasticsearch/pull/137040) (issue: [#136772](https://github.com/elastic/elasticsearch/issues/136772))
* Introduce support for mapping-unavailable fields (Fork from #139417) [#140463](https://github.com/elastic/elasticsearch/pull/140463)
* Late materialization after TopN (Node level) [#132757](https://github.com/elastic/elasticsearch/pull/132757)
* Let `include_execution_metadata` always return data, also in local only [#137641](https://github.com/elastic/elasticsearch/pull/137641)
* Locale and timezone argument for `date_parse` [#136548](https://github.com/elastic/elasticsearch/pull/136548) (issue: [#132487](https://github.com/elastic/elasticsearch/issues/132487))
* Make field fusion generic [#137382](https://github.com/elastic/elasticsearch/pull/137382)
* Multiple patterns for grok command [#136541](https://github.com/elastic/elasticsearch/pull/136541) (issue: [#132486](https://github.com/elastic/elasticsearch/issues/132486))
* Optimize geogrid functions to read points from doc-values [#138917](https://github.com/elastic/elasticsearch/pull/138917)
* Pull `OrderBy` followed by `InlineJoin` on top of it [#137648](https://github.com/elastic/elasticsearch/pull/137648)
* Push down COUNT(*) BY DATE_TRUNC [#138023](https://github.com/elastic/elasticsearch/pull/138023)
* Push filters past inline stats [#137572](https://github.com/elastic/elasticsearch/pull/137572)
* Release CCS support for FORK [#139630](https://github.com/elastic/elasticsearch/pull/139630)
* Release CHUNK function as tech preview [#138621](https://github.com/elastic/elasticsearch/pull/138621)
* Release decay function [#137830](https://github.com/elastic/elasticsearch/pull/137830)
* Release histogram data type [#139703](https://github.com/elastic/elasticsearch/pull/139703)
* Run aggregations on aggregate metric double with default metric [#138647](https://github.com/elastic/elasticsearch/pull/138647) (issue: [#136297](https://github.com/elastic/elasticsearch/issues/136297))
* Support extra field (`outputField`) in TOP function. Values of `outputField` will be returned instead of values of `field` [#135434](https://github.com/elastic/elasticsearch/pull/135434) (issue: [#128630](https://github.com/elastic/elasticsearch/issues/128630))
* Support for parameters in LIKE and RLIKE [#138051](https://github.com/elastic/elasticsearch/pull/138051)
* Support window function in time-series aggregations [#138139](https://github.com/elastic/elasticsearch/pull/138139)
* Timezone support in DATE_TRUNC, BUCKET and TBUCKET [#137450](https://github.com/elastic/elasticsearch/pull/137450)
* Use a single array for buffering rate data points [#140855](https://github.com/elastic/elasticsearch/pull/140855)
* [ESQL][Inference] Introduce usage limits for COMPLETION and RERANK [#139074](https://github.com/elastic/elasticsearch/pull/139074)
* `BlockSourceReader` should always apply source filtering [#136438](https://github.com/elastic/elasticsearch/pull/136438)
* `DateDiff` timezone support [#138316](https://github.com/elastic/elasticsearch/pull/138316)

Geo:
* Bumps jts version to 1.20.0 [#138351](https://github.com/elastic/elasticsearch/pull/138351)

Health:
* Add settings for health indicator `shard_capacity` thresholds [#136141](https://github.com/elastic/elasticsearch/pull/136141) (issue: [#116697](https://github.com/elastic/elasticsearch/issues/116697))
* [HealthAPI] Deterministic shard availability key order [#138260](https://github.com/elastic/elasticsearch/pull/138260) (issue: [#138043](https://github.com/elastic/elasticsearch/issues/138043))

ILM:
* Support different downsampling methods through ILM [#136951](https://github.com/elastic/elasticsearch/pull/136951)

IdentityProvider:
* Support `LimitedRole` in idp role resolution [#140536](https://github.com/elastic/elasticsearch/pull/140536)

Indices APIs:
* Add convenience API key param to remote reindex [#135949](https://github.com/elastic/elasticsearch/pull/135949)
* Add small optimizations to `PUT _component_template` API [#135644](https://github.com/elastic/elasticsearch/pull/135644)
* Improve no-op check in PUT `_mapping` API [#138367](https://github.com/elastic/elasticsearch/pull/138367)

Inference:
* Add `max_batch_size` setting to EIS dense and sparse service settings [#141185](https://github.com/elastic/elasticsearch/pull/141185)
* [Inference] Implementing the completion task type on EIS [#137677](https://github.com/elastic/elasticsearch/pull/137677)

Infra/Plugins:
* Add `upgrade.rollbacks` mapping to .fleet-agents system index [#139363](https://github.com/elastic/elasticsearch/pull/139363)

Infra/REST API:
* Cat API: added endpoint for Circuit Breakers [#136890](https://github.com/elastic/elasticsearch/pull/136890)

Ingest:
* Logstashbridge: map ES logging to log4j backend [#135854](https://github.com/elastic/elasticsearch/pull/135854)

Ingest Node:
* Add CEF processor to Ingest node [#122491](https://github.com/elastic/elasticsearch/pull/122491) (issue: [#126201](https://github.com/elastic/elasticsearch/issues/126201))
* Bump `mustache.java` to 0.9.14 [#138923](https://github.com/elastic/elasticsearch/pull/138923)
* Bump jruby/joni to 2.2.6 [#139075](https://github.com/elastic/elasticsearch/pull/139075)

Machine Learning:
* Add "close_job" parameter to the stop datafeed API [#138634](https://github.com/elastic/elasticsearch/pull/138634) (issue: [#138010](https://github.com/elastic/elasticsearch/issues/138010))
* Add Embedding inference task type [#138198](https://github.com/elastic/elasticsearch/pull/138198)
* Add Google Model Garden's Meta, Mistral, Hugging Face and Ai21 providers support to Inference Plugin [#135701](https://github.com/elastic/elasticsearch/pull/135701)
* Add cached tokens to Unified API response [#136412](https://github.com/elastic/elasticsearch/pull/136412)
* Add daily task to manage .ml-state indices [#137653](https://github.com/elastic/elasticsearch/pull/137653)
* Add late chunking configuration for JinaAI embedding task settings [#137263](https://github.com/elastic/elasticsearch/pull/137263)
* Added Azure OpenAI chat_completion support to the Inference Plugin [#136624](https://github.com/elastic/elasticsearch/pull/136624)
* Added Groq chat completion support to the Inference plugin [#138251](https://github.com/elastic/elasticsearch/pull/138251)
* Added NVIDIA support to Inference Plugin [#132388](https://github.com/elastic/elasticsearch/pull/132388)
* Added OpenShift AI text_embedding, completion, chat_completion and rerank support to the Inference Plugin [#136624](https://github.com/elastic/elasticsearch/pull/136624)
* Nightly maintenance for anomaly detection results indices to keep to manageable size. [#136065](https://github.com/elastic/elasticsearch/pull/136065)
* Require basic licence for the Elastic Inference Service [#137434](https://github.com/elastic/elasticsearch/pull/137434)
* Transition EIS auth polling to persistent task on a single node [#136713](https://github.com/elastic/elasticsearch/pull/136713)

Mapping:
* Add `index.mapping.nested_parents.limit` and raise nested fields limit to 100 [#138961](https://github.com/elastic/elasticsearch/pull/138961)
* Add a dedicated field type for T-Digests [#139607](https://github.com/elastic/elasticsearch/pull/139607)
* Allow updating `inference_id` of `semantic_text` fields [#136120](https://github.com/elastic/elasticsearch/pull/136120)
* Default [semantic_text](/reference/elasticsearch/mapping-reference/semantic-text.md) fields to use [ELSER on EIS](docs-content://explore-analyze/elastic-inference/eis.md#elser-on-eis) when available [#134708](https://github.com/elastic/elasticsearch/pull/134708)
* Enable bfloat16 support for semantic text [#139347](https://github.com/elastic/elasticsearch/pull/139347)
* Enable new exponential histograms field type [#138492](https://github.com/elastic/elasticsearch/pull/138492)
* Improve block loader for source only runtime `geo_point` fields [#135883](https://github.com/elastic/elasticsearch/pull/135883)
* Improve bulk loading of binary doc values [#137995](https://github.com/elastic/elasticsearch/pull/137995)
* OTLP: store units in mappings [#134709](https://github.com/elastic/elasticsearch/pull/134709)
* Optionally ignore field when indexed field name exceeds length limit [#136143](https://github.com/elastic/elasticsearch/pull/136143) (issue: [#135700](https://github.com/elastic/elasticsearch/issues/135700))
* Remove DOC_VALUES_SKIPPER feature flag [#138723](https://github.com/elastic/elasticsearch/pull/138723)
* Remove feature flag to enable binary doc value compression [#138524](https://github.com/elastic/elasticsearch/pull/138524)
* Simple bulk loading for binary doc values [#137860](https://github.com/elastic/elasticsearch/pull/137860)
* T digest field type docs [#140478](https://github.com/elastic/elasticsearch/pull/140478)
* Use binary doc values for `pattern_text` args column [#139466](https://github.com/elastic/elasticsearch/pull/139466)
* Use existing `DocumentMapper` when creating new `MapperService` [#138489](https://github.com/elastic/elasticsearch/pull/138489)
* `AggregateMetricDouble` fields should not build BKD indexes [#138724](https://github.com/elastic/elasticsearch/pull/138724)

Monitoring:
* Add missing fields to the Logstash Stack Monitoring Template [#127053](https://github.com/elastic/elasticsearch/pull/127053) (issue: [#125499](https://github.com/elastic/elasticsearch/issues/125499))

Network:
* Limit concurrent TLS handshakes [#136386](https://github.com/elastic/elasticsearch/pull/136386)

Relevance:
* Add `chunk_rescorer` usage to output of explain and profile for `text_similarity_rank_retriever` [#137249](https://github.com/elastic/elasticsearch/pull/137249)

SQL:
* Add `project_routing` option [#138718](https://github.com/elastic/elasticsearch/pull/138718)
* Add project routing support to JDBC [#138756](https://github.com/elastic/elasticsearch/pull/138756)
* Enable CPS [#138803](https://github.com/elastic/elasticsearch/pull/138803)

Search:
* Add time range bucketing attribute to APM took time latency metrics [#135549](https://github.com/elastic/elasticsearch/pull/135549)
* Adds retriever for result diversification using MMR [#135873](https://github.com/elastic/elasticsearch/pull/135873)
* Allows Cross Project for close `PointInTime` [#138962](https://github.com/elastic/elasticsearch/pull/138962)
* Allows PIT to be cross project [#137966](https://github.com/elastic/elasticsearch/pull/137966)
* Allows field caps to be cross project [#137530](https://github.com/elastic/elasticsearch/pull/137530)
* Can match phase coordinator duration APM metric [#136828](https://github.com/elastic/elasticsearch/pull/136828)
* Can match search shard phase APM metric [#136646](https://github.com/elastic/elasticsearch/pull/136646)
* Coordinator phase duration APM metric attributes [#137409](https://github.com/elastic/elasticsearch/pull/137409)
* Dfs query phase coordinator metric [#136481](https://github.com/elastic/elasticsearch/pull/136481)
* Extend time range bucketing attributes to retrievers [#136072](https://github.com/elastic/elasticsearch/pull/136072)
* Fetch search phase coordinator duration APM metric [#136547](https://github.com/elastic/elasticsearch/pull/136547)
* Field caps to support `project_routing` also in the body of the request [#138681](https://github.com/elastic/elasticsearch/pull/138681)
* Field caps transport changes to return for each original expression what it was resolved to [#136632](https://github.com/elastic/elasticsearch/pull/136632)
* Improve retrying PIT contexts for read-only indices [#135231](https://github.com/elastic/elasticsearch/pull/135231)
* Speed up sorts on secondary sort fields [#137533](https://github.com/elastic/elasticsearch/pull/137533)
* Use DV rewrites where possible in Keyword queries [#137536](https://github.com/elastic/elasticsearch/pull/137536)

Searchable Snapshots:
* Allow fast blob-cache introspection by shard-id [#138282](https://github.com/elastic/elasticsearch/pull/138282)

Security:
* Add audit log testing for cert-based cross-cluster authentication [#137302](https://github.com/elastic/elasticsearch/pull/137302)
* Add periodic PKC JWK set reloading capability to JWT realm [#136996](https://github.com/elastic/elasticsearch/pull/136996)
* Adds certificate identity field to cross-cluster API keys [#134604](https://github.com/elastic/elasticsearch/pull/134604)
* Include Secure Setting Names and Keystore Modified Time in Reload API Response [#138052](https://github.com/elastic/elasticsearch/pull/138052) (issue: [#112268](https://github.com/elastic/elasticsearch/issues/112268))
* Send cross cluster api key signature as headers [#135674](https://github.com/elastic/elasticsearch/pull/135674)
* Validate certificate identity from cross cluster creds [#136299](https://github.com/elastic/elasticsearch/pull/136299)

Snapshot/Restore:
* Add a new setting for s3 API call timeout [#138072](https://github.com/elastic/elasticsearch/pull/138072)
* Retry bulk-delete items in GCS [#138951](https://github.com/elastic/elasticsearch/pull/138951) (issue: [#138364](https://github.com/elastic/elasticsearch/issues/138364))
* S3 `compareAndExchange` using conditional writes [#139228](https://github.com/elastic/elasticsearch/pull/139228)
* Use common retry logic for GCS [#138553](https://github.com/elastic/elasticsearch/pull/138553)

TSDB:
* Add ES93BloomFilterStoredFieldsFormat for efficient field existence checks [#137331](https://github.com/elastic/elasticsearch/pull/137331)
* Add TDigest histogram as metric to time series data streams [#139247](https://github.com/elastic/elasticsearch/pull/139247)
* Add support for merges in ES93BloomFilterStoredFieldsFormat [#137622](https://github.com/elastic/elasticsearch/pull/137622)
* GROUP BY ALL with the dimensions output [#138595](https://github.com/elastic/elasticsearch/pull/138595)
* Late materialization of dimension fields in time-series [#135961](https://github.com/elastic/elasticsearch/pull/135961)
* Minimize doc values fetches in TSDBSyntheticIdFieldsProducer [#139053](https://github.com/elastic/elasticsearch/pull/139053)
* Use a new synthetic `_id` format for time-series datastreams [#137274](https://github.com/elastic/elasticsearch/pull/137274)
* Use doc values skipper for @timestamp in synthetic `_id` postings #138568 [#138876](https://github.com/elastic/elasticsearch/pull/138876)
* Use doc values skipper for `_tsid` in synthetic `_id` postings [#138568](https://github.com/elastic/elasticsearch/pull/138568)

Transform:
* Preview index request [#137455](https://github.com/elastic/elasticsearch/pull/137455)

Vector Search:
* Add DirectIO bulk rescoring [#135380](https://github.com/elastic/elasticsearch/pull/135380)
* Add `on_disk_rescore: true` option to disk BBQ to rescore vectors on-disk without loading into memory [#135778](https://github.com/elastic/elasticsearch/pull/135778)
* Add bfloat16 support to `rank_vectors` [#139463](https://github.com/elastic/elasticsearch/pull/139463)
* Adding base64 indexing for vector values [#137072](https://github.com/elastic/elasticsearch/pull/137072)
* Allow `semantic_text` fields to use optional GPU indexing for HNSW and int8_hnsw [#138999](https://github.com/elastic/elasticsearch/pull/138999)
* Enable bfloat16 and on-disk rescoring for dense vectors [#138492](https://github.com/elastic/elasticsearch/pull/138492)
* Enable early termination for HNSW by default [#130564](https://github.com/elastic/elasticsearch/pull/130564)
* GPU: Restrict GPU indexing to FLOAT element types [#139084](https://github.com/elastic/elasticsearch/pull/139084)
* GPU: add support for cosine with cuvs 2025.12 [#139821](https://github.com/elastic/elasticsearch/pull/139821)
* Introduce an adaptive HNSW Patience collector [#138685](https://github.com/elastic/elasticsearch/pull/138685)
* Remove `gpu_vectors_indexing` feature flag [#139318](https://github.com/elastic/elasticsearch/pull/139318)
* Semantic search CCS support when ccs_minimize_roundtrips=false [#138982](https://github.com/elastic/elasticsearch/pull/138982)
* Upgrade cuvs-java to version 25.12 [#139747](https://github.com/elastic/elasticsearch/pull/139747)
* Use new bulk scoring dot product for max inner product [#139409](https://github.com/elastic/elasticsearch/pull/139409)
* Use the new merge executor for intra-merge parallelism [#137853](https://github.com/elastic/elasticsearch/pull/137853)
* [DiskBBQ] Add concurrency on KMeansLocal [#139239](https://github.com/elastic/elasticsearch/pull/139239)
* [DiskBBQ] Support for centroid filtering for restrictive filters [#137959](https://github.com/elastic/elasticsearch/pull/137959)
* [SIMD][ARM] Optimized native bulk dot product scoring for Int7 [#138552](https://github.com/elastic/elasticsearch/pull/138552)
* [SIMD][x64] Optimized native bulk dot product scoring for Int7 [#139069](https://github.com/elastic/elasticsearch/pull/139069)


### Fixes [elasticsearch-9.3.0-fixes]

Aggregations:
* Fix `SearchContext` CB memory accounting [#138002](https://github.com/elastic/elasticsearch/pull/138002)
* Use Double.compare to compare doubles in tdigest.Sort [#141049](https://github.com/elastic/elasticsearch/pull/141049)

Allocation:
* Allow relocation to NOT_PREFERRED node for evacuating shards [#140197](https://github.com/elastic/elasticsearch/pull/140197)
* Always prefer YES over NOT_PREFERRED when allocating unassigned shards [#138464](https://github.com/elastic/elasticsearch/pull/138464)
* Fix Decision.Type serialization BWC [#140199](https://github.com/elastic/elasticsearch/pull/140199)
* Handle deleted source index in allocation deciders [#140699](https://github.com/elastic/elasticsearch/pull/140699) (issue: [#140630](https://github.com/elastic/elasticsearch/issues/140630))
* Overall Decision for Deciders prioritizes THROTTLE [#140237](https://github.com/elastic/elasticsearch/pull/140237)

CCS:
* Set CPS index options only when not using PIT [#137728](https://github.com/elastic/elasticsearch/pull/137728)

Codec:
* Binary doc values have stale value offset array if block contains all empty values [#139922](https://github.com/elastic/elasticsearch/pull/139922)

Data streams:
* Exempt internal request markers from streams request param restrictions [#139386](https://github.com/elastic/elasticsearch/pull/139386) (issue: [#139367](https://github.com/elastic/elasticsearch/issues/139367))

Downsampling:
* Fix bug when downsampling exponential histograms with last value [#139808](https://github.com/elastic/elasticsearch/pull/139808)
* Sort the values of a legacy histogram during downsampling [#140771](https://github.com/elastic/elasticsearch/pull/140771) (issue: [#139382](https://github.com/elastic/elasticsearch/issues/139382))

EQL:
* Fix `_index` on missing events in CCS [#140886](https://github.com/elastic/elasticsearch/pull/140886)
* Fix `project_routing` [#139366](https://github.com/elastic/elasticsearch/pull/139366)

ES|QL:
* Add block loader for the `_id` field of time-series indices [#140102](https://github.com/elastic/elasticsearch/pull/140102) (issues: [#140033](https://github.com/elastic/elasticsearch/issues/140033), [#135689](https://github.com/elastic/elasticsearch/issues/135689))
* Add support for dot-separated attribute names (e.g. `foo.bar`) and for parameters (e.g. `??my_param`) in FUSE GROUP BY [#135901](https://github.com/elastic/elasticsearch/pull/135901)
* Addressing vector similarity concurrency issue with byte vectors [#137883](https://github.com/elastic/elasticsearch/pull/137883) (issue: [#137625](https://github.com/elastic/elasticsearch/issues/137625))
* Aggressively free topn [#140126](https://github.com/elastic/elasticsearch/pull/140126)
* Catch-and-rethrow `TooComplexToDeterminizeException` within ESQL [#137024](https://github.com/elastic/elasticsearch/pull/137024)
* Change FUSE KEY BY to receive a list of `qualifiedName` [#139071](https://github.com/elastic/elasticsearch/pull/139071)
* Do not skip a remote cluster base on the query's execution time status [#138332](https://github.com/elastic/elasticsearch/pull/138332)
* Do not use Min or Max as Top's surrogate when there is an `outputField` [#138380](https://github.com/elastic/elasticsearch/pull/138380) (issue: [#134083](https://github.com/elastic/elasticsearch/issues/134083))
* Don't allow MV_EXPAND prior to STATS with TS [#136931](https://github.com/elastic/elasticsearch/pull/136931) (issue: [#136928](https://github.com/elastic/elasticsearch/issues/136928))
* ESQL: Fix `INLINE STATS GROUP BY null` being incorrectly pruned [#140027](https://github.com/elastic/elasticsearch/pull/140027) (issue: [#139887](https://github.com/elastic/elasticsearch/issues/139887))
* ES|QL - fix ENRICH command when using dense_vector columns [#139774](https://github.com/elastic/elasticsearch/pull/139774) (issue: [#137699](https://github.com/elastic/elasticsearch/issues/137699))
* Fix Page.equals() [#136266](https://github.com/elastic/elasticsearch/pull/136266)
* Fix Present/Absent agg functions [#140671](https://github.com/elastic/elasticsearch/pull/140671)
* Fix aggregation on null value [#139797](https://github.com/elastic/elasticsearch/pull/139797) (issues: [#110257](https://github.com/elastic/elasticsearch/issues/110257), [#137544](https://github.com/elastic/elasticsearch/issues/137544))
* Fix attribute only in full text function not found [#137395](https://github.com/elastic/elasticsearch/pull/137395) (issue: [#137396](https://github.com/elastic/elasticsearch/issues/137396))
* Fix extent reading when missing [#140034](https://github.com/elastic/elasticsearch/pull/140034)
* Fix folding of case() function with date period and time duration [#141157](https://github.com/elastic/elasticsearch/pull/141157)
* Fix interpolation for data points at bucket boundaries [#139798](https://github.com/elastic/elasticsearch/pull/139798) (issue: [#139732](https://github.com/elastic/elasticsearch/issues/139732))
* Fix metrics for took between 1 and 10 hours [#139257](https://github.com/elastic/elasticsearch/pull/139257)
* Fix wrong pruning of plans with no output columns [#133405](https://github.com/elastic/elasticsearch/pull/133405)
* Fixes memory leak in `BytesRefLongBlockHash` [#137050](https://github.com/elastic/elasticsearch/pull/137050) (issue: [#137021](https://github.com/elastic/elasticsearch/issues/137021))
* Fixing bug when handling 1d literal vectors [#136891](https://github.com/elastic/elasticsearch/pull/136891) (issue: [#136364](https://github.com/elastic/elasticsearch/issues/136364))
* Manage INLINE STATS count(*) on result sets with no columns [#137017](https://github.com/elastic/elasticsearch/pull/137017)
* No `EsqlIllegalArgumentException` for invalid window values [#139470](https://github.com/elastic/elasticsearch/pull/139470)
* Prune `InlineJoin` right aggregations by delegating to the child plan [#139357](https://github.com/elastic/elasticsearch/pull/139357) (issue: [#138283](https://github.com/elastic/elasticsearch/issues/138283))
* Prune columns when using fork [#137907](https://github.com/elastic/elasticsearch/pull/137907) (issue: [#136365](https://github.com/elastic/elasticsearch/issues/136365))
* Pushing down eval expression when it requires data access [#136610](https://github.com/elastic/elasticsearch/pull/136610) (issue: [#133462](https://github.com/elastic/elasticsearch/issues/133462))
* Quantize ST_X, ST_Y and related functions [#140963](https://github.com/elastic/elasticsearch/pull/140963) (issue: [#139943](https://github.com/elastic/elasticsearch/issues/139943))
* Support date trunc in TS [#138947](https://github.com/elastic/elasticsearch/pull/138947)
* TS Disallow renaming into timestamp prior to implicit use [#137713](https://github.com/elastic/elasticsearch/pull/137713) (issue: [#137655](https://github.com/elastic/elasticsearch/issues/137655))
* Use DEFAULT_UNSORTABLE topN encoder for the TSID_DATA_TYPE [#137706](https://github.com/elastic/elasticsearch/pull/137706)
* Use sub keyword block loader with `ignore_above` for text fields [#140622](https://github.com/elastic/elasticsearch/pull/140622)
* Validate multiple GROK patterns individually [#137082](https://github.com/elastic/elasticsearch/pull/137082)
* [ES|QL]: Update Vector Similarity To Support BFLOAT16 [#139113](https://github.com/elastic/elasticsearch/pull/139113)

ILM:
* Remove ILM-stopped-check before the cluster update in `migrateToDataTiersRouting` [#140892](https://github.com/elastic/elasticsearch/pull/140892) (issue: [#140885](https://github.com/elastic/elasticsearch/issues/140885))

Indices APIs:
* Don't fail delete index API if an index is deleted during the request [#138015](https://github.com/elastic/elasticsearch/pull/138015) (issue: [#137422](https://github.com/elastic/elasticsearch/issues/137422))

Inference:
* [Inference API] Include rerank in supported tasks for IBM watsonx integration [#140331](https://github.com/elastic/elasticsearch/pull/140331) (issue: [#140328](https://github.com/elastic/elasticsearch/issues/140328))

Infra/Node Lifecycle:
* Fix readiness edge case on startup [#140791](https://github.com/elastic/elasticsearch/pull/140791) (issue: [#136955](https://github.com/elastic/elasticsearch/issues/136955))

Ingest Node:
* Respect flexible field access pattern in geoip and `ip_location` processors [#138728](https://github.com/elastic/elasticsearch/pull/138728)

Machine Learning:
* Add configurable `max_batch_size` for `GoogleVertexAI` embedding service settings [#138047](https://github.com/elastic/elasticsearch/pull/138047)
* Add missing `job_id` filter to Anomaly Detection data deleter [#138160](https://github.com/elastic/elasticsearch/pull/138160)
* ChangePointDetector now correctly detects when a constant function returns a different value [#128602](https://github.com/elastic/elasticsearch/pull/128602) (issue: [#127517](https://github.com/elastic/elasticsearch/issues/127517))
* Disallow `max_number_of_allocations` > 1 for low priority model deployments [#140163](https://github.com/elastic/elasticsearch/pull/140163) (issue: [#111227](https://github.com/elastic/elasticsearch/issues/111227))
* Fix anomaly detection jobs stuck in opening by continously retrying to set the state to opened. [#139668](https://github.com/elastic/elasticsearch/pull/139668)
* Preserve deployments with zero allocations during assignment planning [#137244](https://github.com/elastic/elasticsearch/pull/137244) (issue: [#137134](https://github.com/elastic/elasticsearch/issues/137134))
* Skip dataframes when disabled [#137220](https://github.com/elastic/elasticsearch/pull/137220)
* Switch `TextExpansionQueryBuilder` and `TextEmbeddingQueryVectorBuilder` to return 400 instead of 500 errors [#135800](https://github.com/elastic/elasticsearch/pull/135800)
* [Inference API] Add `ElasticInferenceServiceDenseTextEmbeddingsServiceSettings` to `InferenceNamedWriteablesProvider` [#138484](https://github.com/elastic/elasticsearch/pull/138484)
* [Inference API] Remove worst-case additional 50ms latency for non-rate limited requests [#136167](https://github.com/elastic/elasticsearch/pull/136167)
* [Inference API] Support chunking settings for sparse embeddings in custom service [#138776](https://github.com/elastic/elasticsearch/pull/138776)

Mapping:
* Don't store keyword multi fields when they trip `ignore_above` [#132962](https://github.com/elastic/elasticsearch/pull/132962)
* Fix `index.mapping.use_doc_values_skippers` defaults in serverless [#139526](https://github.com/elastic/elasticsearch/pull/139526)
* Fixed inconsistency in the `isSyntheticSourceEnabled` flag [#137297](https://github.com/elastic/elasticsearch/pull/137297)
* Provide defaults for index sort settings [#135886](https://github.com/elastic/elasticsearch/pull/135886) (issue: [#129062](https://github.com/elastic/elasticsearch/issues/129062))

Packaging:
* Fix stderr leak in Docker ES process detection [#140701](https://github.com/elastic/elasticsearch/pull/140701)

Reindex:
* Disable `_delete_by_query` and `_update_by_query` for CCS/stateful [#140301](https://github.com/elastic/elasticsearch/pull/140301)

Rollup:
* Fixing _rollup/data performance for a large number of indices [#138305](https://github.com/elastic/elasticsearch/pull/138305)

SQL:
* Do not attempt to canonicalize `InnerAggregate` [#136854](https://github.com/elastic/elasticsearch/pull/136854)
* More friendly exceptions for validation errors [#137560](https://github.com/elastic/elasticsearch/pull/137560)

Search:
* Delay automaton creation in `BinaryDvConfirmedQuery` to avoid OOM on queries against `WildCard` fields [#136086](https://github.com/elastic/elasticsearch/pull/136086)
* Ensure integer sorts are rewritten to long sorts for BWC indexes [#139293](https://github.com/elastic/elasticsearch/pull/139293) (issues: [#139127](https://github.com/elastic/elasticsearch/issues/139127), [#139128](https://github.com/elastic/elasticsearch/issues/139128))
* Fix date fields sort formatting with missing values [#135899](https://github.com/elastic/elasticsearch/pull/135899) (issue: [#81960](https://github.com/elastic/elasticsearch/issues/81960))

Security:
* Consistently prevent using exclusion prefix on its own [#139337](https://github.com/elastic/elasticsearch/pull/139337) (issue: [#45504](https://github.com/elastic/elasticsearch/issues/45504))
* Fixed a bug where dash-prefixed expressions were not consistently excluded during index resolution.
This impacted both specific index names and wildcard patterns (example: `-index, -logs-*`).
 [#138467](https://github.com/elastic/elasticsearch/pull/138467) (issues: [#64752](https://github.com/elastic/elasticsearch/issues/64752), [#83435](https://github.com/elastic/elasticsearch/issues/83435))

Snapshot/Restore:
* Fix race condition in `CancellableRateLimitedFluxIterator` [#141323](https://github.com/elastic/elasticsearch/pull/141323)
* Ignore abort-on-cleanup failure in S3 repo [#138569](https://github.com/elastic/elasticsearch/pull/138569)
* Introduce INDEX_SHARD_COUNT_FORMAT [#137210](https://github.com/elastic/elasticsearch/pull/137210) (issue: [#131822](https://github.com/elastic/elasticsearch/issues/131822))
* Prevent NPE when generating snapshot metrics before initial cluster state is set [#136350](https://github.com/elastic/elasticsearch/pull/136350)
* Support weaker consistency model for S3 MPUs [#138663](https://github.com/elastic/elasticsearch/pull/138663)
* Suppress Azure SDK error logs [#139729](https://github.com/elastic/elasticsearch/pull/139729)

Stats:
* Avoiding creating `DataStreamShardStats` objects with negative timestamps [#139854](https://github.com/elastic/elasticsearch/pull/139854)

Vector Search:
* Auto prefiltering for queries on dense `semantic_text` fields [#138989](https://github.com/elastic/elasticsearch/pull/138989)
* Corrects a seemingly simple bug where we pass `numCands` instead of k [#140839](https://github.com/elastic/elasticsearch/pull/140839)
* Disk bbq license enforcement [#139087](https://github.com/elastic/elasticsearch/pull/139087)
* DiskBBQ - missing min competitive similarity check on tail docs [#135851](https://github.com/elastic/elasticsearch/pull/135851)
* Ensure we parse `on_disk_rescore` as its valid to pass false [#141158](https://github.com/elastic/elasticsearch/pull/141158)
* Intercept filters to knn queries [#138457](https://github.com/elastic/elasticsearch/pull/138457) (issue: [#138410](https://github.com/elastic/elasticsearch/issues/138410))
