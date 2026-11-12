<!-- Part 2 of 18 of release-notes/index.md (split because the page is big). -->

## 9.3.5 [elasticsearch-9.3.5-release-notes]

### Features and enhancements [elasticsearch-9.3.5-features-enhancements]

Infra/Logging:
* Upgrade to log4j 2.26.0 [#132166](https://github.com/elastic/elasticsearch/pull/132166) (issue: [#132035](https://github.com/elastic/elasticsearch/issues/132035))

Machine Learning:
* Better messaging regarding OOM process termination [#2841](https://github.com/elastic/ml-cpp/pull/2841)
* Improve adherence to memory limits for the bucket gatherer [#2848](https://github.com/elastic/ml-cpp/pull/2848)
* Report the actual memory usage of the autodetect process [#2846](https://github.com/elastic/ml-cpp/pull/2846)
* Restrict file system access for pytorch models [#2851](https://github.com/elastic/ml-cpp/pull/2851)
* Update the PyTorch library to version 2.7.1 [#2863](https://github.com/elastic/ml-cpp/pull/2863)

Packaging:
* Bump bundled JDK to Java 26.0.1 [#147424](https://github.com/elastic/elasticsearch/pull/147424)

Search:
* Add logging tracking to _xpack/usage [#148087](https://github.com/elastic/elasticsearch/pull/148087)

Security:
* Update elastic-apm-agent-java8 to 1.55.6 [#148271](https://github.com/elastic/elasticsearch/pull/148271)


### Fixes [elasticsearch-9.3.5-fixes]

Aggregations:
* Aggs: Account aggs uncompressed size on coordinator reduction [#148885](https://github.com/elastic/elasticsearch/pull/148885) (issue: [#147190](https://github.com/elastic/elasticsearch/issues/147190))
* Aggs: Fix auto_date_histogram/date_histogram inside a global agg [#147427](https://github.com/elastic/elasticsearch/pull/147427) (issue: [#92570](https://github.com/elastic/elasticsearch/issues/92570))
* Fix `ArrayIndexOutOfBoundsException` in `date_histogram` with `hard_bounds` outside data [#148765](https://github.com/elastic/elasticsearch/pull/148765) (issue: [#148763](https://github.com/elastic/elasticsearch/issues/148763))

CCR:
* Fix CCR follow to handle `indexing_complete` race [#145304](https://github.com/elastic/elasticsearch/pull/145304)

Data streams:
* Update failure store redirect logic to exclude backpressure exceptions [#148154](https://github.com/elastic/elasticsearch/pull/148154)

Distributed:
* Fix `FsBlobContainer.moveBlobAtomic` fallback on CIFS filesystems [#148777](https://github.com/elastic/elasticsearch/pull/148777) (issue: [#148811](https://github.com/elastic/elasticsearch/issues/148811))
* Fix race in FsBlobContainer.moveBlobAtomic by replacing move op with hard link [#147405](https://github.com/elastic/elasticsearch/pull/147405) (issue: [#147171](https://github.com/elastic/elasticsearch/issues/147171))

EQL:
* Fix management of PIT close failures after successful query [#146634](https://github.com/elastic/elasticsearch/pull/146634) (issues: [#146263](https://github.com/elastic/elasticsearch/issues/146263), [#146187](https://github.com/elastic/elasticsearch/issues/146187))

ES|QL:
* Disallow empty lists in named params, only [#147748](https://github.com/elastic/elasticsearch/pull/147748) (issue: [#147448](https://github.com/elastic/elasticsearch/issues/147448))
* Do not enable doc-partitioning for count [#143544](https://github.com/elastic/elasticsearch/pull/143544) (issue: [#134512](https://github.com/elastic/elasticsearch/issues/134512))
* Fix ArrayIndexOutOfBoundsException in centroid grouping evaluateFinal [#148815](https://github.com/elastic/elasticsearch/pull/148815) (issue: [#141318](https://github.com/elastic/elasticsearch/issues/141318))
* Fix FROM *_logs index name validation [#149395](https://github.com/elastic/elasticsearch/pull/149395) (issue: [#146073](https://github.com/elastic/elasticsearch/issues/146073))
* Fix `_index` LIKE with ? wildcard [#147462](https://github.com/elastic/elasticsearch/pull/147462) (issue: [#146364](https://github.com/elastic/elasticsearch/issues/146364))
* Fix deriv aggregation function intermediate state [#146160](https://github.com/elastic/elasticsearch/pull/146160) (issue: [#141305](https://github.com/elastic/elasticsearch/issues/141305))
* Fix errors in blockloaders when filtering nulls on histograms [#148983](https://github.com/elastic/elasticsearch/pull/148983) (issue: [#147854](https://github.com/elastic/elasticsearch/issues/147854))
* Fix nullify under join and enrich [#145743](https://github.com/elastic/elasticsearch/pull/145743) (issue: [#141827](https://github.com/elastic/elasticsearch/issues/141827))
* Node-reduce driver should not release search contexts on failure [#145960](https://github.com/elastic/elasticsearch/pull/145960) (issue: [#145509](https://github.com/elastic/elasticsearch/issues/145509))
* Normalize `_timeseries` to JSON for stored source [#148716](https://github.com/elastic/elasticsearch/pull/148716) (issue: [#148414](https://github.com/elastic/elasticsearch/issues/148414))
* Report correct location for SET errors [#147582](https://github.com/elastic/elasticsearch/pull/147582) (issue: [#145873](https://github.com/elastic/elasticsearch/issues/145873))
* Restore TEXT field size estimate for Enrich and `LookupJoin` [#147357](https://github.com/elastic/elasticsearch/pull/147357)
* Use search threadpool for coordination in ES|QL [#149034](https://github.com/elastic/elasticsearch/pull/149034)

Inference:
* Honor task settings for Amazon Bedrock and Google Vertex chat completion [#149268](https://github.com/elastic/elasticsearch/pull/149268) (issue: [#148792](https://github.com/elastic/elasticsearch/issues/148792))
* Implement `RerankingInferenceService` for Elastic service [#148365](https://github.com/elastic/elasticsearch/pull/148365)
* Make similarity required for `SageMaker` `ElasticTextEmbeddingPayload` [#146885](https://github.com/elastic/elasticsearch/pull/146885)
* [Inference API] Fix inference initialization thread exhaustion [#147063](https://github.com/elastic/elasticsearch/pull/147063)
* [Inference API] Fixing potential NPE if `InferenceContext` is null [#148921](https://github.com/elastic/elasticsearch/pull/148921)
* [Inference API] Use image/jpeg instead of image/jpg for inference validation MIME type [#148793](https://github.com/elastic/elasticsearch/pull/148793)

Infra/Core:
* Fix potential OOME on `SearchResponse#toString()` for extemely large responses [#147267](https://github.com/elastic/elasticsearch/pull/147267)
* Use `toTruncatedString` in chunked objects `toString` [#147860](https://github.com/elastic/elasticsearch/pull/147860) (issue: [#143694](https://github.com/elastic/elasticsearch/issues/143694))

Machine Learning:
* Preserve zero-allocation trained-model deployments in cluster state during ML-node shutdown rebalances [#146910](https://github.com/elastic/elasticsearch/pull/146910) (issue: [#146806](https://github.com/elastic/elasticsearch/issues/146806))

SQL:
* Fix REPLACE with empty pattern [#148616](https://github.com/elastic/elasticsearch/pull/148616)

Search:
* Async Search: Ensure cleanup is also done against aliases [#146356](https://github.com/elastic/elasticsearch/pull/146356) (issue: [#146184](https://github.com/elastic/elasticsearch/issues/146184))
* Default `exclude_inference_fields` to `exclude_vectors` at REST [#148527](https://github.com/elastic/elasticsearch/pull/148527) (issue: [#146425](https://github.com/elastic/elasticsearch/issues/146425))
* Fix: correctly serialise sparse field pruning options in mixed cluster scenarios [#147823](https://github.com/elastic/elasticsearch/pull/147823)
* Pass `CircuitBreakingException` through `SearchExecutionContext#toQuery` [#148607](https://github.com/elastic/elasticsearch/pull/148607)
* Update `RuleQueryBuilder` to eagerly rewrite organic query [#149323](https://github.com/elastic/elasticsearch/pull/149323) (issue: [#146106](https://github.com/elastic/elasticsearch/issues/146106))

Transform:
* Exclude clusters in license check [#143146](https://github.com/elastic/elasticsearch/pull/143146) (issues: [#114514](https://github.com/elastic/elasticsearch/issues/114514), [#114509](https://github.com/elastic/elasticsearch/issues/114509))
* Only run next search once [#148268](https://github.com/elastic/elasticsearch/pull/148268) (issue: [#147716](https://github.com/elastic/elasticsearch/issues/147716))
* Propagate deprecation warnings [#147934](https://github.com/elastic/elasticsearch/pull/147934) (issues: [#82935](https://github.com/elastic/elasticsearch/issues/82935), [#82936](https://github.com/elastic/elasticsearch/issues/82936))

Vector Search:
* Fix gpu close resource ordering [#149054](https://github.com/elastic/elasticsearch/pull/149054)
* Fix integer overflow in CuVSResourceManager.estimateNNDescentMemory [#147559](https://github.com/elastic/elasticsearch/pull/147559)
* GPU codec: fall back to CPU graph build on flush when GPU is busy [#149373](https://github.com/elastic/elasticsearch/pull/149373)

Watcher:
* Clear watch schedules when starting trigger engine [#145325](https://github.com/elastic/elasticsearch/pull/145325) (issues: [#137562](https://github.com/elastic/elasticsearch/issues/137562), [#131964](https://github.com/elastic/elasticsearch/issues/131964))
* Fix race in `TickerScheduleTriggerEngine` by checking watcher to node allocation [#147678](https://github.com/elastic/elasticsearch/pull/147678) (issue: [#146874](https://github.com/elastic/elasticsearch/issues/146874))




## 9.4.1 [elasticsearch-9.4.1-release-notes]

### Features and enhancements [elasticsearch-9.4.1-features-enhancements]

Machine Learning:
* Add EuroBERT and Jina v5 ops to graph validation allowlist [#3015](https://github.com/elastic/ml-cpp/pull/3015)
* Better error handling regarding quantiles state documents [#2894](https://github.com/elastic/ml-cpp/pull/2894)
* Better handling of invalid JSON state documents [#2895](https://github.com/elastic/ml-cpp/pull/2895)
* Better messaging regarding OOM process termination [#2841](https://github.com/elastic/ml-cpp/pull/2841)
* Downgrade log severity for a batch of recoverable errors [#2889](https://github.com/elastic/ml-cpp/pull/2889)
* Harden pytorch_inference with TorchScript model graph validation [#3008](https://github.com/elastic/ml-cpp/pull/3008) (issue: [#2890](https://github.com/elastic/ml-cpp/issues/2890))
* Improve adherence to memory limits for the bucket gatherer [#2848](https://github.com/elastic/ml-cpp/pull/2848)
* Report the actual memory usage of the autodetect process [#2846](https://github.com/elastic/ml-cpp/pull/2846)
* Restrict file system access for pytorch models [#2851](https://github.com/elastic/ml-cpp/pull/2851)
* Update the PyTorch library to version 2.7.1 [#2863](https://github.com/elastic/ml-cpp/pull/2863)

Packaging:
* Bump bundled JDK to Java 26.0.1 [#147424](https://github.com/elastic/elasticsearch/pull/147424)
* Update bundled JDK to Java 26 [#146167](https://github.com/elastic/elasticsearch/pull/146167)

Security:
* Update elastic-apm-agent-java8 to 1.55.6 [#148271](https://github.com/elastic/elasticsearch/pull/148271)


### Fixes [elasticsearch-9.4.1-fixes]

Data streams:
* Update failure store redirect logic to exclude backpressure exceptions [#148154](https://github.com/elastic/elasticsearch/pull/148154)

ES|QL:
* Bugfix - Block Loader Pushdown + Union Types [#147940](https://github.com/elastic/elasticsearch/pull/147940)
* Disallow empty lists in named params, only [#147748](https://github.com/elastic/elasticsearch/pull/147748) (issue: [#147448](https://github.com/elastic/elasticsearch/issues/147448))
* ES|QL query approximation: enforce minimum number of sampled source rows [#147886](https://github.com/elastic/elasticsearch/pull/147886)

Inference:
* Implement `RerankingInferenceService` for Elastic service [#148365](https://github.com/elastic/elasticsearch/pull/148365)
* [Inference API] Fix inference initialization thread exhaustion [#147063](https://github.com/elastic/elasticsearch/pull/147063)

Machine Learning:
* Fix flaky CIoManagerTest/testFileIoGood test [#3017](https://github.com/elastic/ml-cpp/pull/3017)

Vector Search:
* [DiskBBQ] Check that precondition should not be overwritten on update [#148111](https://github.com/elastic/elasticsearch/pull/148111) (issue: [#148004](https://github.com/elastic/elasticsearch/issues/148004))

Watcher:
* Fix race in `TickerScheduleTriggerEngine` by checking watcher to node allocation [#147678](https://github.com/elastic/elasticsearch/pull/147678) (issue: [#146874](https://github.com/elastic/elasticsearch/issues/146874))




## 9.4.0 [elasticsearch-9.4.0-release-notes]
