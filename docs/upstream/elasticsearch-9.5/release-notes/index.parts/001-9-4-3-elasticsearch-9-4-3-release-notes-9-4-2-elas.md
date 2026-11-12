<!-- Part 1 of 18 of release-notes/index.md (split because the page is big). -->

## 9.4.3 [elasticsearch-9.4.3-release-notes]

### Features and enhancements [elasticsearch-9.4.3-features-enhancements]

ES|QL:
* Add filter capture for ESQL query [#149535](https://github.com/elastic/elasticsearch/pull/149535)
* Upgrade Apache Iceberg to 1.10.2 [#151664](https://github.com/elastic/elasticsearch/pull/151664)

Inference:
* [Inference] Add requires org.apache.commons.lang3 to module-info [#151794](https://github.com/elastic/elasticsearch/pull/151794)

Infra/Logging:
* Add query filter logging to SQL and EQL queries [#150127](https://github.com/elastic/elasticsearch/pull/150127)

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


### Fixes [elasticsearch-9.4.3-fixes]

Aggregations:
* Fix AVLTreeDigest CDF monotonicity for penultimate centroid [#151181](https://github.com/elastic/elasticsearch/pull/151181) (issue: [#151012](https://github.com/elastic/elasticsearch/issues/151012))
* Fix non-monotonic T-Digest centroids caused by floating-point errors [#151979](https://github.com/elastic/elasticsearch/pull/151979)

ES|QL:
* Avoid long overflows on AVG by casting to double [#148519](https://github.com/elastic/elasticsearch/pull/148519) (issue: [#99575](https://github.com/elastic/elasticsearch/issues/99575))
* Carry over synthetic attributes from conversions to the `Project` above `UnionAll` [#149775](https://github.com/elastic/elasticsearch/pull/149775) (issue: [#149509](https://github.com/elastic/elasticsearch/issues/149509))
* Fix `ValuesReader` assertion error [#149683](https://github.com/elastic/elasticsearch/pull/149683)
* Fix subquery/fork with inline stats pruning [#149783](https://github.com/elastic/elasticsearch/pull/149783) (issue: [#149589](https://github.com/elastic/elasticsearch/issues/149589))
* Fix wildcard view resolution losing duplicate copies [#149418](https://github.com/elastic/elasticsearch/pull/149418) (issue: [#149416](https://github.com/elastic/elasticsearch/issues/149416))
* Make subquery with counter type not present in all branches behave more consistently [#150704](https://github.com/elastic/elasticsearch/pull/150704) (issues: [#150640](https://github.com/elastic/elasticsearch/issues/150640), [#150641](https://github.com/elastic/elasticsearch/issues/150641), [#150644](https://github.com/elastic/elasticsearch/issues/150644), [#150645](https://github.com/elastic/elasticsearch/issues/150645))
* Resolve surrogates in union type field resolution before plan serialization [#151633](https://github.com/elastic/elasticsearch/pull/151633) (issue: [#151475](https://github.com/elastic/elasticsearch/issues/151475))

Infra/Core:
* Pass through `includeSourceInError` [#142335](https://github.com/elastic/elasticsearch/pull/142335)

Machine Learning:
* Fix bug causing incorrect error on force deleting already deleted model [#107188](https://github.com/elastic/elasticsearch/pull/107188) (issue: [#105420](https://github.com/elastic/elasticsearch/issues/105420))
* Fix flaky CIoManagerTest/testFileIoGood test [#3017](https://github.com/elastic/ml-cpp/pull/3017)
* Revert "[ML] Add extra validation in `trained_model` creation" [#152000](https://github.com/elastic/elasticsearch/pull/152000)

Mapping:
* Don't allow runtime fields to shadow fields used in index sort [#150636](https://github.com/elastic/elasticsearch/pull/150636) (issue: [#149500](https://github.com/elastic/elasticsearch/issues/149500))

Reindex:
* Fix division of `max_docs` between slices in reindex [#150808](https://github.com/elastic/elasticsearch/pull/150808)

SQL:
* Fix CLI tests failures due to unconsumed output [#145967](https://github.com/elastic/elasticsearch/pull/145967) (issues: [#143646](https://github.com/elastic/elasticsearch/issues/143646), [#143645](https://github.com/elastic/elasticsearch/issues/143645))

Search:
* Guard against null zeroTermsQuery in cross_fields multi_match [#149935](https://github.com/elastic/elasticsearch/pull/149935) (issue: [#149934](https://github.com/elastic/elasticsearch/issues/149934))
* Ids Query: Throw `IllegalArgumentException` [#151234](https://github.com/elastic/elasticsearch/pull/151234) (issue: [#150305](https://github.com/elastic/elasticsearch/issues/150305))

Security:
* Run remote child task cancellation as system user [#150560](https://github.com/elastic/elasticsearch/pull/150560)

TSDB:
* Fix prefix escape for synthetic id [#150433](https://github.com/elastic/elasticsearch/pull/150433) (issue: [#150389](https://github.com/elastic/elasticsearch/issues/150389))

Vector Search:
* Fix GPU SQ format name to match CPU equivalent [#149512](https://github.com/elastic/elasticsearch/pull/149512) (issue: [#148975](https://github.com/elastic/elasticsearch/issues/148975))




## 9.3.7 [elasticsearch-9.3.7-release-notes]

### Features and enhancements [elasticsearch-9.3.7-features-enhancements]

Inference:
* [Inference] Add requires org.apache.commons.lang3 to module-info [#151794](https://github.com/elastic/elasticsearch/pull/151794)

Machine Learning:
* Better messaging regarding OOM process termination [#2841](https://github.com/elastic/ml-cpp/pull/2841)
* Improve adherence to memory limits for the bucket gatherer [#2848](https://github.com/elastic/ml-cpp/pull/2848)
* Report the actual memory usage of the autodetect process [#2846](https://github.com/elastic/ml-cpp/pull/2846)
* Restrict file system access for pytorch models [#2851](https://github.com/elastic/ml-cpp/pull/2851)
* Update the PyTorch library to version 2.7.1 [#2863](https://github.com/elastic/ml-cpp/pull/2863)


### Fixes [elasticsearch-9.3.7-fixes]

ES|QL:
* Resolve surrogates in union type field resolution before plan serialization [#151633](https://github.com/elastic/elasticsearch/pull/151633) (issue: [#151475](https://github.com/elastic/elasticsearch/issues/151475))

Infra/Core:
* Pass through `includeSourceInError` [#142335](https://github.com/elastic/elasticsearch/pull/142335)

Machine Learning:
* Fix bug causing incorrect error on force deleting already deleted model [#107188](https://github.com/elastic/elasticsearch/pull/107188) (issue: [#105420](https://github.com/elastic/elasticsearch/issues/105420))
* Revert "[ML] Add extra validation in `trained_model` creation" [#152000](https://github.com/elastic/elasticsearch/pull/152000)




## 9.3.6 [elasticsearch-9.3.6-release-notes]

### Features and enhancements [elasticsearch-9.3.6-features-enhancements]

Authorization:
* Update the built-in `kibana_system` role to grant `manage`, `create_index`, `read`, `index`, `write`, and `delete` privileges on the `axonius.alert_finding` and `axonius.incident` indices, replacing the previous `axonius.alert_and_incident` index [#149797](https://github.com/elastic/elasticsearch/pull/149797)

Data streams:
* [otel-data] Explicitly map `http.response.status_code` as long [#149631](https://github.com/elastic/elasticsearch/pull/149631)

Inference:
* Upgrade commons-lang3 version for the inference plugin [#150242](https://github.com/elastic/elasticsearch/pull/150242)

Machine Learning:
* Better messaging regarding OOM process termination [#2841](https://github.com/elastic/ml-cpp/pull/2841)
* Improve adherence to memory limits for the bucket gatherer [#2848](https://github.com/elastic/ml-cpp/pull/2848)
* Report the actual memory usage of the autodetect process [#2846](https://github.com/elastic/ml-cpp/pull/2846)
* Restrict file system access for pytorch models [#2851](https://github.com/elastic/ml-cpp/pull/2851)
* Update the PyTorch library to version 2.7.1 [#2863](https://github.com/elastic/ml-cpp/pull/2863)

Network:
* Upgrade netty to 4.1.135.Final [#151099](https://github.com/elastic/elasticsearch/pull/151099)

Security:
* Optimize literal action automaton builds [#151093](https://github.com/elastic/elasticsearch/pull/151093) (issues: [#123872](https://github.com/elastic/elasticsearch/issues/123872), [#105723](https://github.com/elastic/elasticsearch/issues/105723))


### Fixes [elasticsearch-9.3.6-fixes]

Analysis:
* Fix Nynorsk stemmer `UnsupportedOperationException`. The `light_nynorsk` and `minimal_nynorsk` stemmers no longer fail with an HTTP 500 error during index creation due to passing an immutable map to Lucene's analysis factory. [#150345](https://github.com/elastic/elasticsearch/pull/150345)

Authentication:
* Move SAML metadata resolution to background thread [#144381](https://github.com/elastic/elasticsearch/pull/144381) (issue: [#138031](https://github.com/elastic/elasticsearch/issues/138031))

ES|QL:
* Catch `StackOverflowError` in deeply nested RLIKE patterns [#150238](https://github.com/elastic/elasticsearch/pull/150238) (issue: [#149838](https://github.com/elastic/elasticsearch/issues/149838))
* Enforce limit for max nested functions [#149971](https://github.com/elastic/elasticsearch/pull/149971)
* Fix wrong warning in expressions with unrolled multivalues [#145968](https://github.com/elastic/elasticsearch/pull/145968)
* [ESQL] Refactor Greatest and Least functions to use evaluator map [#128429](https://github.com/elastic/elasticsearch/pull/128429) (issue: [#114036](https://github.com/elastic/elasticsearch/issues/114036))

ILM:
* Truncate error for ILM's `step_info` instead of string [#150413](https://github.com/elastic/elasticsearch/pull/150413)

Inference:
* Validate inference embedding model before checking for existing uses [#150150](https://github.com/elastic/elasticsearch/pull/150150) (issues: [#147062](https://github.com/elastic/elasticsearch/issues/147062), [#150084](https://github.com/elastic/elasticsearch/issues/150084))
* When a streaming inference request is canceled, immediately release apache client networking resources [#149987](https://github.com/elastic/elasticsearch/pull/149987)
* [Inference API] Fix Streaming publisher shutdown race condition [#150789](https://github.com/elastic/elasticsearch/pull/150789) (issue: [#150742](https://github.com/elastic/elasticsearch/issues/150742))

Infra/Core:
* Don't apply time zones to epoch-based timestamps [#148663](https://github.com/elastic/elasticsearch/pull/148663)
* Filter `_source` field names by code point [#151146](https://github.com/elastic/elasticsearch/pull/151146)
* Fix OS stats for cgroup paths containing colons [#151095](https://github.com/elastic/elasticsearch/pull/151095)

Machine Learning:
* Add extra validation in `trained_model` creation [#150227](https://github.com/elastic/elasticsearch/pull/150227)

Query Languages:
* EQL/SQL: Enforce max expression depth checks [#150003](https://github.com/elastic/elasticsearch/pull/150003)

Search:
* Add IT covering search during rolling restart [#149667](https://github.com/elastic/elasticsearch/pull/149667) (issue: [#86927](https://github.com/elastic/elasticsearch/issues/86927))

Security:
* Make Automatons wildcard code-point aware [#151143](https://github.com/elastic/elasticsearch/pull/151143)

TSDB:
* Fix OTLP histogram handling for single-count histograms without bucket boundaries [#151411](https://github.com/elastic/elasticsearch/pull/151411)

Transform:
* Honor `ClusterHealth` timeout when waiting for transform internal index shards [#149462](https://github.com/elastic/elasticsearch/pull/149462) (issue: [#149400](https://github.com/elastic/elasticsearch/issues/149400))




## 9.4.2 [elasticsearch-9.4.2-release-notes]

### Features and enhancements [elasticsearch-9.4.2-features-enhancements]

Infra/Logging:
* Upgrade to log4j 2.26.0 [#132166](https://github.com/elastic/elasticsearch/pull/132166) (issue: [#132035](https://github.com/elastic/elasticsearch/issues/132035))

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

Search:
* Add logging tracking to _xpack/usage [#148087](https://github.com/elastic/elasticsearch/pull/148087)


### Fixes [elasticsearch-9.4.2-fixes]

Aggregations:
* Aggs: Account aggs uncompressed size on coordinator reduction [#148885](https://github.com/elastic/elasticsearch/pull/148885) (issue: [#147190](https://github.com/elastic/elasticsearch/issues/147190))
* Aggs: Fix auto_date_histogram/date_histogram inside a global agg [#147427](https://github.com/elastic/elasticsearch/pull/147427) (issue: [#92570](https://github.com/elastic/elasticsearch/issues/92570))
* Fix `ArrayIndexOutOfBoundsException` in `date_histogram` with `hard_bounds` outside data [#148765](https://github.com/elastic/elasticsearch/pull/148765) (issue: [#148763](https://github.com/elastic/elasticsearch/issues/148763))

CCR:
* Fix CCR follow to handle `indexing_complete` race [#145304](https://github.com/elastic/elasticsearch/pull/145304)

Distributed:
* Fix `FsBlobContainer.moveBlobAtomic` fallback on CIFS filesystems [#148777](https://github.com/elastic/elasticsearch/pull/148777) (issue: [#148811](https://github.com/elastic/elasticsearch/issues/148811))

ES|QL:
* Disallow casting to snapshot-only type [#148813](https://github.com/elastic/elasticsearch/pull/148813) (issue: [#147867](https://github.com/elastic/elasticsearch/issues/147867))
* Fix "optimized incorrectly" error from project reorder [#149053](https://github.com/elastic/elasticsearch/pull/149053) (issue: [#148612](https://github.com/elastic/elasticsearch/issues/148612))
* Fix ArrayIndexOutOfBoundsException in centroid grouping evaluateFinal [#148815](https://github.com/elastic/elasticsearch/pull/148815) (issue: [#141318](https://github.com/elastic/elasticsearch/issues/141318))
* Fix FROM *_logs index name validation [#149395](https://github.com/elastic/elasticsearch/pull/149395) (issue: [#146073](https://github.com/elastic/elasticsearch/issues/146073))
* Fix `InvalidMappedField` equals/hashCode and lazy error message [#146117](https://github.com/elastic/elasticsearch/pull/146117) (issue: [#145907](https://github.com/elastic/elasticsearch/issues/145907))
* Fix errors in blockloaders when filtering nulls on histograms [#148983](https://github.com/elastic/elasticsearch/pull/148983) (issue: [#147854](https://github.com/elastic/elasticsearch/issues/147854))
* Lucene `TermsEnum` and `PostingsEnum` may only be used from acquiring thread [#149297](https://github.com/elastic/elasticsearch/pull/149297)
* Node-reduce driver should not release search contexts on failure [#145960](https://github.com/elastic/elasticsearch/pull/145960) (issue: [#145509](https://github.com/elastic/elasticsearch/issues/145509))
* Normalize `_timeseries` to JSON for stored source [#148716](https://github.com/elastic/elasticsearch/pull/148716) (issue: [#148414](https://github.com/elastic/elasticsearch/issues/148414))
* Use search threadpool for coordination in ES|QL [#149034](https://github.com/elastic/elasticsearch/pull/149034)

Inference:
* Honor task settings for Amazon Bedrock and Google Vertex chat completion [#149268](https://github.com/elastic/elasticsearch/pull/149268) (issue: [#148792](https://github.com/elastic/elasticsearch/issues/148792))
* [Inference API] Fix NPE for Inference usage when referencing a embedding task type [#149636](https://github.com/elastic/elasticsearch/pull/149636)
* [Inference API] Fixing potential NPE if `InferenceContext` is null [#148921](https://github.com/elastic/elasticsearch/pull/148921)
* [Inference API] Use image/jpeg instead of image/jpg for inference validation MIME type [#148793](https://github.com/elastic/elasticsearch/pull/148793)

Infra/Core:
* Pin server-launcher native -march to x86-64-v2 [#148542](https://github.com/elastic/elasticsearch/pull/148542) (issue: [#148326](https://github.com/elastic/elasticsearch/issues/148326))
* Use `toTruncatedString` in chunked objects `toString` [#147860](https://github.com/elastic/elasticsearch/pull/147860) (issue: [#143694](https://github.com/elastic/elasticsearch/issues/143694))

Infra/Logging:
* Monitor exceptions in processing queries and log them as failures [#148362](https://github.com/elastic/elasticsearch/pull/148362)

Machine Learning:
* Fix flaky CIoManagerTest/testFileIoGood test [#3017](https://github.com/elastic/ml-cpp/pull/3017)

PromQL:
* Default PromQL index to metrics-* [#148489](https://github.com/elastic/elasticsearch/pull/148489)
* Default Prometheus discovery APIs to metrics-* [#148770](https://github.com/elastic/elasticsearch/pull/148770)

SQL:
* Fix REPLACE with empty pattern [#148616](https://github.com/elastic/elasticsearch/pull/148616)

Search:
* Default `exclude_inference_fields` to `exclude_vectors` at REST [#148527](https://github.com/elastic/elasticsearch/pull/148527) (issue: [#146425](https://github.com/elastic/elasticsearch/issues/146425))
* Fix UOE in CanMatch empty-shards skipped-by-cluster map [#148754](https://github.com/elastic/elasticsearch/pull/148754)
* Fix synonym reloads not propagating through AnalyzerWrapper subclasses [#147695](https://github.com/elastic/elasticsearch/pull/147695) (issue: [#146914](https://github.com/elastic/elasticsearch/issues/146914))
* Pass `CircuitBreakingException` through `SearchExecutionContext#toQuery` [#148607](https://github.com/elastic/elasticsearch/pull/148607)
* Update `RuleQueryBuilder` to eagerly rewrite organic query [#149323](https://github.com/elastic/elasticsearch/pull/149323) (issue: [#146106](https://github.com/elastic/elasticsearch/issues/146106))

Transform:
* Only run next search once [#148268](https://github.com/elastic/elasticsearch/pull/148268) (issue: [#147716](https://github.com/elastic/elasticsearch/issues/147716))
* Propagate deprecation warnings [#147934](https://github.com/elastic/elasticsearch/pull/147934) (issues: [#82935](https://github.com/elastic/elasticsearch/issues/82935), [#82936](https://github.com/elastic/elasticsearch/issues/82936))

Vector Search:
* Fix gpu close resource ordering [#149054](https://github.com/elastic/elasticsearch/pull/149054)
* GPU codec: fall back to CPU graph build on flush when GPU is busy [#149373](https://github.com/elastic/elasticsearch/pull/149373)
