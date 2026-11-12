<!-- Part 5 of 18 of release-notes/index.md (split because the page is big). -->

### Fixes [elasticsearch-9.4.0-fixes]

Aggregations:
* Aggs: Fix class cast exceptions in pipeline aggs [#140069](https://github.com/elastic/elasticsearch/pull/140069) (issues: [#137624](https://github.com/elastic/elasticsearch/issues/137624), [#136173](https://github.com/elastic/elasticsearch/issues/136173))

Allocation:
* Allow allocation to replacement target node on vacate completion [#140150](https://github.com/elastic/elasticsearch/pull/140150)
* Handle not preferred in replica shards allocator [#142575](https://github.com/elastic/elasticsearch/pull/142575) (issue: [#142424](https://github.com/elastic/elasticsearch/issues/142424))

CCR:
* Fix `FollowingEngine#lookupPrimaryTerm` when sequence numbers are disabled [#143935](https://github.com/elastic/elasticsearch/pull/143935)

CCS:
* Always error out if CCS expression shows up when CCS is not supported [#139009](https://github.com/elastic/elasticsearch/pull/139009) (issue: [#138987](https://github.com/elastic/elasticsearch/issues/138987))
* CPS: Copy existing resolved index expressions when constructing a new `SearchRequest` from an existing one [#139596](https://github.com/elastic/elasticsearch/pull/139596)
* Fix: ensure CPS project routing appears in the right places for `_msearch/template` [#140166](https://github.com/elastic/elasticsearch/pull/140166)

Codec:
* Ensure bloom filter is not shared across threads [#146002](https://github.com/elastic/elasticsearch/pull/146002)
* Fix NPE when querying `pattern_text` field in segment with no field values [#142767](https://github.com/elastic/elasticsearch/pull/142767)
* Share the same doc values producer for `IdBloomFilterSupplier` and TSDBSyntheticIdFieldsProducer [#147910](https://github.com/elastic/elasticsearch/pull/147910)

Data streams:
* [One workflow] Make workflows system data stream hidden [#146713](https://github.com/elastic/elasticsearch/pull/146713)

Distributed:
* Do not attempt marking store as corrupted if the check is rejected due to shutdown [#145209](https://github.com/elastic/elasticsearch/pull/145209) (issue: [#123773](https://github.com/elastic/elasticsearch/issues/123773))
* Ensure that the buffer used for ES93BloomFilterStoredFieldsFormat is zeroed [#139034](https://github.com/elastic/elasticsearch/pull/139034)
* Fix race in FsBlobContainer.moveBlobAtomic by replacing move op with hard link [#147405](https://github.com/elastic/elasticsearch/pull/147405) (issue: [#147171](https://github.com/elastic/elasticsearch/issues/147171))

Downsampling:
* Fix downsampling configuration validation [#141873](https://github.com/elastic/elasticsearch/pull/141873) (issue: [#141541](https://github.com/elastic/elasticsearch/issues/141541))

EQL:
* Fix management of PIT close failures after successful query [#146634](https://github.com/elastic/elasticsearch/pull/146634) (issues: [#146263](https://github.com/elastic/elasticsearch/issues/146263), [#146187](https://github.com/elastic/elasticsearch/issues/146187))
* Fix propagation of filters on join keys for missing events [#145813](https://github.com/elastic/elasticsearch/pull/145813) (issue: [#145402](https://github.com/elastic/elasticsearch/issues/145402))

ES|QL:
* AMD return 0 on Count with no rows [#144462](https://github.com/elastic/elasticsearch/pull/144462) (issue: [#141852](https://github.com/elastic/elasticsearch/issues/141852))
* Account for field readers in breaker [#140666](https://github.com/elastic/elasticsearch/pull/140666)
* Added missing ST_SIMPLIFY error test and fixed bug with missing errors [#143480](https://github.com/elastic/elasticsearch/pull/143480)
* Better error on some queries missing timestamps [#141503](https://github.com/elastic/elasticsearch/pull/141503) (issue: [#140606](https://github.com/elastic/elasticsearch/issues/140606))
* Better estimation on loading large text field from `_source` [#143105](https://github.com/elastic/elasticsearch/pull/143105) (issue: [#141550](https://github.com/elastic/elasticsearch/issues/141550))
* Better validation for fulltext functions after LIMIT BY [#147682](https://github.com/elastic/elasticsearch/pull/147682) (issue: [#147681](https://github.com/elastic/elasticsearch/issues/147681))
* Catch `DateTimeException` in `EsqlDataTypeConverter` [#137744](https://github.com/elastic/elasticsearch/pull/137744) (issue: [#137741](https://github.com/elastic/elasticsearch/issues/137741))
* Cleanup and bug fixes in NDJSON datasource [#143969](https://github.com/elastic/elasticsearch/pull/143969)
* Correctly manage NULL data type for SUM [#144942](https://github.com/elastic/elasticsearch/pull/144942) (issue: [#144914](https://github.com/elastic/elasticsearch/issues/144914))
* Do not enable doc-partitioning for count [#143544](https://github.com/elastic/elasticsearch/pull/143544) (issue: [#134512](https://github.com/elastic/elasticsearch/issues/134512))
* Do not push sort on many keyword fields to lucene [#142700](https://github.com/elastic/elasticsearch/pull/142700) (issues: [#140134](https://github.com/elastic/elasticsearch/issues/140134), [#141083](https://github.com/elastic/elasticsearch/issues/141083))
* Don't use a Literal for `constant_keyword` fields when used inside full-text functions [#145632](https://github.com/elastic/elasticsearch/pull/145632) (issue: [#145570](https://github.com/elastic/elasticsearch/issues/145570))
* ESQL - Fix performance loading source when vectors are excluded [#146223](https://github.com/elastic/elasticsearch/pull/146223) (issue: [#145799](https://github.com/elastic/elasticsearch/issues/145799))
* ESQL: Preserve type conflict error metadata for subqueries [#143954](https://github.com/elastic/elasticsearch/pull/143954) (issue: [#142499](https://github.com/elastic/elasticsearch/issues/142499))
* ESQL: Validate unsupported grouping types earlier [#147650](https://github.com/elastic/elasticsearch/pull/147650) (issue: [#147596](https://github.com/elastic/elasticsearch/issues/147596))
* Fix Analyzer infinite loop for subquery referencing indices with empty mappings [#141371](https://github.com/elastic/elasticsearch/pull/141371) (issue: [#141029](https://github.com/elastic/elasticsearch/issues/141029))
* Fix BUCKET date rounding selection [#144425](https://github.com/elastic/elasticsearch/pull/144425)
* Fix CSV-escaped quotes rendering in generated ES|QL docs examples [#143449](https://github.com/elastic/elasticsearch/pull/143449)
* Fix CsvIT overflow tests failing on JDK 25 due to missing OmitStackTraceInFastThrow flag [#145415](https://github.com/elastic/elasticsearch/pull/145415) (issues: [#145415](https://github.com/elastic/elasticsearch/issues/145415), [#145424](https://github.com/elastic/elasticsearch/issues/145424))
* Fix Decay cast to Double to be a cast to Number instead [#144118](https://github.com/elastic/elasticsearch/pull/144118) (issue: [#143351](https://github.com/elastic/elasticsearch/issues/143351))
* Fix ES:QL Driver logging for 4xx errors and cancellations [#140905](https://github.com/elastic/elasticsearch/pull/140905) (issue: [#138008](https://github.com/elastic/elasticsearch/issues/138008))
* Fix ESQL TS requests with LIMIT 0 [#144031](https://github.com/elastic/elasticsearch/pull/144031) (issue: [#144024](https://github.com/elastic/elasticsearch/issues/144024))
* Fix KNN with LIMIT BY [#146844](https://github.com/elastic/elasticsearch/pull/146844)
* Fix LIMIT after all columns are dropped [#143463](https://github.com/elastic/elasticsearch/pull/143463) (issue: [#142473](https://github.com/elastic/elasticsearch/issues/142473))
* Fix MMR NPE when initial doc has a null vector [#146005](https://github.com/elastic/elasticsearch/pull/146005) (issue: [#142939](https://github.com/elastic/elasticsearch/issues/142939))
* Fix NPE on query log when CCS remotes are unavailable [#142933](https://github.com/elastic/elasticsearch/pull/142933) (issue: [#142915](https://github.com/elastic/elasticsearch/issues/142915))
* Fix TBUCKET(n) on empty filter range [#146366](https://github.com/elastic/elasticsearch/pull/146366) (issue: [#146354](https://github.com/elastic/elasticsearch/issues/146354))
* Fix `_index` LIKE with ? wildcard [#147462](https://github.com/elastic/elasticsearch/pull/147462) (issue: [#146364](https://github.com/elastic/elasticsearch/issues/146364))
* Fix async logging consistency and severity [#142401](https://github.com/elastic/elasticsearch/pull/142401) (issues: [#142374](https://github.com/elastic/elasticsearch/issues/142374), [#142316](https://github.com/elastic/elasticsearch/issues/142316))
* Fix bzip2 decompressor and NDJSON error recovery [#143844](https://github.com/elastic/elasticsearch/pull/143844)
* Fix checks to define if a JOIN is remote [#139461](https://github.com/elastic/elasticsearch/pull/139461)
* Fix datasource test failures on Windows and FIPS [#143417](https://github.com/elastic/elasticsearch/pull/143417)
* Fix deriv aggregation function intermediate state [#146160](https://github.com/elastic/elasticsearch/pull/146160) (issue: [#141305](https://github.com/elastic/elasticsearch/issues/141305))
* Fix false circular view reference with shared wildcards [#146144](https://github.com/elastic/elasticsearch/pull/146144) (issues: [#146097](https://github.com/elastic/elasticsearch/issues/146097), [#146118](https://github.com/elastic/elasticsearch/issues/146118))
* Fix handling of values on the time bucket boundaries for ES|QL increase [#145794](https://github.com/elastic/elasticsearch/pull/145794)
* Fix more views exclusions bugs [#147323](https://github.com/elastic/elasticsearch/pull/147323)
* Fix nested fields loading under NULLIFY [#145741](https://github.com/elastic/elasticsearch/pull/145741) (issue: [#142616](https://github.com/elastic/elasticsearch/issues/142616))
* Fix null folding of nested COALESCE [#140028](https://github.com/elastic/elasticsearch/pull/140028)
* Fix nullify under join and enrich [#145743](https://github.com/elastic/elasticsearch/pull/145743) (issue: [#141827](https://github.com/elastic/elasticsearch/issues/141827))
* Fix rate/increase single-value bucket handling for delta temporality [#146518](https://github.com/elastic/elasticsearch/pull/146518)
* Fix starts_with/ends_with with special chars [#146348](https://github.com/elastic/elasticsearch/pull/146348) (issue: [#130851](https://github.com/elastic/elasticsearch/issues/130851))
* Fix to tdigest implicit eval [#140690](https://github.com/elastic/elasticsearch/pull/140690) (issue: [#140670](https://github.com/elastic/elasticsearch/issues/140670))
* Forbid MV_EXPAND before full text functions [#143249](https://github.com/elastic/elasticsearch/pull/143249) (issue: [#143121](https://github.com/elastic/elasticsearch/issues/143121))
* Identify correctly a renamed attribute in full text functions as a field attribute [#143893](https://github.com/elastic/elasticsearch/pull/143893) (issue: [#143859](https://github.com/elastic/elasticsearch/issues/143859))
* KQL and QSTR were incorrectly rejected when used before SAMPLE [#145456](https://github.com/elastic/elasticsearch/pull/145456)
* Keywords mv count fix [#145390](https://github.com/elastic/elasticsearch/pull/145390)
* Loading unmapped fields on synthetic `_source` [#144112](https://github.com/elastic/elasticsearch/pull/144112) (issue: [#143916](https://github.com/elastic/elasticsearch/issues/143916))
* Log compute engine server failures as ERROR [#142330](https://github.com/elastic/elasticsearch/pull/142330) (issue: [#139883](https://github.com/elastic/elasticsearch/issues/139883))
* Make unmapped_fields="load" automatically trigger for partially mapped KEYWORD fields, and allow projecting partially mapped non-KEYWORD fields [#144228](https://github.com/elastic/elasticsearch/pull/144228) (issues: [#145206](https://github.com/elastic/elasticsearch/issues/145206), [#141994](https://github.com/elastic/elasticsearch/issues/141994))
* Prevent pushdown of unmapped fields in filters and sorts [#143460](https://github.com/elastic/elasticsearch/pull/143460) (issues: [#141920](https://github.com/elastic/elasticsearch/issues/141920), [#141925](https://github.com/elastic/elasticsearch/issues/141925))
* Propagate ambiguous field type errors correctly [#143737](https://github.com/elastic/elasticsearch/pull/143737) (issue: [#142761](https://github.com/elastic/elasticsearch/issues/142761))
* Propagate converted fields through projections [#137923](https://github.com/elastic/elasticsearch/pull/137923)
* Propagate empty local relation past joins [#144826](https://github.com/elastic/elasticsearch/pull/144826) (issue: [#144329](https://github.com/elastic/elasticsearch/issues/144329))
* Prune `no_fields` from project in subquery [#145164](https://github.com/elastic/elasticsearch/pull/145164) (issue: [#145148](https://github.com/elastic/elasticsearch/issues/145148))
* Report correct location for SET errors [#147582](https://github.com/elastic/elasticsearch/pull/147582) (issue: [#145873](https://github.com/elastic/elasticsearch/issues/145873))
* Restore TEXT field size estimate for Enrich and `LookupJoin` [#147357](https://github.com/elastic/elasticsearch/pull/147357)
* SUM long overflow fix [#141272](https://github.com/elastic/elasticsearch/pull/141272) (issue: [#110437](https://github.com/elastic/elasticsearch/issues/110437))
* Split aggs results [#139973](https://github.com/elastic/elasticsearch/pull/139973)
* Use standard logic for conflicting types in TS [#141496](https://github.com/elastic/elasticsearch/pull/141496) (issue: [#141379](https://github.com/elastic/elasticsearch/issues/141379))
* [TEST] Fix discrepancy in docs & kibana generation [#141651](https://github.com/elastic/elasticsearch/pull/141651) (issue: [#141199](https://github.com/elastic/elasticsearch/issues/141199))
* `DocValuesBlockLoader` should return `ConstantNullsReader` rather than null [#140136](https://github.com/elastic/elasticsearch/pull/140136)
* overflowing division in ROW gives wrong error message [#138973](https://github.com/elastic/elasticsearch/pull/138973) (issue: [#138798](https://github.com/elastic/elasticsearch/issues/138798))

Engine:
* Fix `ShardFieldStats.liveDocsBytes` [#142711](https://github.com/elastic/elasticsearch/pull/142711)

Highlighting:
* Fix BoundedBreakIteratorScanner IllegalStateException when used with SplittingBreakIterator during highlighting [#143440](https://github.com/elastic/elasticsearch/pull/143440)

Indices APIs:
* Correctly ignore system indices when validating dot-prefixed indices [#128868](https://github.com/elastic/elasticsearch/pull/128868)

Inference:
* Fix RecursiveChunkingSettings.validate() logic bug where separator validation was skipped [#145314](https://github.com/elastic/elasticsearch/pull/145314) (issue: [#144815](https://github.com/elastic/elasticsearch/issues/144815))
* Make similarity required for `SageMaker` `ElasticTextEmbeddingPayload` [#146885](https://github.com/elastic/elasticsearch/pull/146885)
* Validate base64 embedding inputs use data URI format [#145038](https://github.com/elastic/elasticsearch/pull/145038) (issue: [#144900](https://github.com/elastic/elasticsearch/issues/144900))
* [Inference API] Fix NPE in multimodal check [#144107](https://github.com/elastic/elasticsearch/pull/144107)
* [Inference API] Use 504 for timeout REST status code response [#145838](https://github.com/elastic/elasticsearch/pull/145838)
* [Inference] Correctly preserve class information for internal endpoints on update [#142380](https://github.com/elastic/elasticsearch/pull/142380)

Infra/Core:
* Fix potential OOME on `SearchResponse#toString()` for extemely large responses [#147267](https://github.com/elastic/elasticsearch/pull/147267)

Ingest Node:
* Fix pipeline resolution cache for bulk requests [#144648](https://github.com/elastic/elasticsearch/pull/144648)
* Fix waiting for enrich policy execution for users without the `monitor` privilege [#145751](https://github.com/elastic/elasticsearch/pull/145751)

Logs:
* Fixed a bug where match only text delegates loading to an incorrect parent keyword field [#141399](https://github.com/elastic/elasticsearch/pull/141399)

Machine Learning:
* Fix AD job update overrides `categorization_examples_limit` with default [#140524](https://github.com/elastic/elasticsearch/pull/140524)
* Fix NPE when preview datafeed checks `date_nanos` for an unmapped time field [#144909](https://github.com/elastic/elasticsearch/pull/144909) (issue: [#144888](https://github.com/elastic/elasticsearch/issues/144888))
* Fix flaky CIoManagerTest/testFileIoGood test [#3017](https://github.com/elastic/ml-cpp/pull/3017)
* Fix validation of anomaly detection job config [#139946](https://github.com/elastic/elasticsearch/pull/139946) (issue: [#29843](https://github.com/elastic/elasticsearch/issues/29843))
* Handle null columns in ES|QL CHANGE_POINT [#144388](https://github.com/elastic/elasticsearch/pull/144388) (issue: [#142858](https://github.com/elastic/elasticsearch/issues/142858))
* Omit uncomputed model stats [#146186](https://github.com/elastic/elasticsearch/pull/146186)
* Preserve zero-allocation trained-model deployments in cluster state during ML-node shutdown rebalances [#146910](https://github.com/elastic/elasticsearch/pull/146910) (issue: [#146806](https://github.com/elastic/elasticsearch/issues/146806))
* Reduce priority of clear-cache tasks [#139685](https://github.com/elastic/elasticsearch/pull/139685)

Mapping:
* Date fields with ignore malformed do not ignore object and array values [#143533](https://github.com/elastic/elasticsearch/pull/143533) (issue: [#109539](https://github.com/elastic/elasticsearch/issues/109539))
* Don't serialize endpoint metadata in semantic text mappings [#145021](https://github.com/elastic/elasticsearch/pull/145021) (issue: [#144969](https://github.com/elastic/elasticsearch/issues/144969))
* Drop deprecation warnings when updating a mapping in the cluster state applier [#144040](https://github.com/elastic/elasticsearch/pull/144040) (issues: [#142544](https://github.com/elastic/elasticsearch/issues/142544), [#142964](https://github.com/elastic/elasticsearch/issues/142964), [#142410](https://github.com/elastic/elasticsearch/issues/142410), [#143884](https://github.com/elastic/elasticsearch/issues/143884), [#142477](https://github.com/elastic/elasticsearch/issues/142477))
* Fix match only text decoding surrogate pairs [#146567](https://github.com/elastic/elasticsearch/pull/146567) (issue: [#146538](https://github.com/elastic/elasticsearch/issues/146538))
* Re-use previously seen dynamically-created Mappers during document parsing [#143377](https://github.com/elastic/elasticsearch/pull/143377)
* Resolve *.geo.location as geopoint in otel dynamic mappings [#141397](https://github.com/elastic/elasticsearch/pull/141397) (issue: [#140506](https://github.com/elastic/elasticsearch/issues/140506))

PromQL:
* PromQL: absent labels must match empty-string label matchers [#146116](https://github.com/elastic/elasticsearch/pull/146116)

Reindex:
* Restore initial thread context during reindex etc [#146134](https://github.com/elastic/elasticsearch/pull/146134)

SQL:
* Fix NPE in aggregations [#139829](https://github.com/elastic/elasticsearch/pull/139829)
* Fix SQL client parsing of array header values [#143408](https://github.com/elastic/elasticsearch/pull/143408) (issues: [#143018](https://github.com/elastic/elasticsearch/issues/143018), [#143019](https://github.com/elastic/elasticsearch/issues/143019))
* Refresh PIT id after each response [#141736](https://github.com/elastic/elasticsearch/pull/141736)

Search:
* Add cancellation support to `IndicesRequestCache` [#141708](https://github.com/elastic/elasticsearch/pull/141708)
* Adjust the formula for "adaptive replica selection" [#144562](https://github.com/elastic/elasticsearch/pull/144562)
* Async Search: Ensure cleanup is also done against aliases [#146356](https://github.com/elastic/elasticsearch/pull/146356) (issue: [#146184](https://github.com/elastic/elasticsearch/issues/146184))
* Bugfix for CCS BWC in `SearchShardsAction` [#145820](https://github.com/elastic/elasticsearch/pull/145820)
* Bugfix: Deleted async search won't show on any API [#140385](https://github.com/elastic/elasticsearch/pull/140385) (issue: [#132423](https://github.com/elastic/elasticsearch/issues/132423))
* Collapse pathological regex quantifier stacking to prevent NFA construction OOM [#145452](https://github.com/elastic/elasticsearch/pull/145452)
* Fix `terminate_after` not honored for aggs when size=0 [#146199](https://github.com/elastic/elasticsearch/pull/146199) (issue: [#126665](https://github.com/elastic/elasticsearch/issues/126665))
* Fix bug parsing "request" parameter in clear cache API, it should clear the request cache only [#145726](https://github.com/elastic/elasticsearch/pull/145726)
* Fix nested aggregation `top_hits` with query `inner_hits` [#137351](https://github.com/elastic/elasticsearch/pull/137351) (issue: [#136893](https://github.com/elastic/elasticsearch/issues/136893))
* Fix pooled `SearchHits` leak in `MergeResult#writeTo` on transport version mismatch [#146431](https://github.com/elastic/elasticsearch/pull/146431) (issue: [#146420](https://github.com/elastic/elasticsearch/issues/146420))
* Fix: correctly serialise sparse field pruning options in mixed cluster scenarios [#147823](https://github.com/elastic/elasticsearch/pull/147823)
* Fixes an edge case in "_terms_enum" API for ip fields [#144308](https://github.com/elastic/elasticsearch/pull/144308) (issue: [#142811](https://github.com/elastic/elasticsearch/issues/142811))
* Fixes bug that prevented retrieving _inference_fields via _source_includes [#141534](https://github.com/elastic/elasticsearch/pull/141534) (issue: [#141075](https://github.com/elastic/elasticsearch/issues/141075))
* PIT: Throw error when unknown transport version is parsed [#141811](https://github.com/elastic/elasticsearch/pull/141811) (issue: [#140457](https://github.com/elastic/elasticsearch/issues/140457))
* Record stats for "adaptive replica selection" in batched queries [#144563](https://github.com/elastic/elasticsearch/pull/144563) (issue: [#144146](https://github.com/elastic/elasticsearch/issues/144146))
* Record stats for adaptive replica selection in dfs queries [#145070](https://github.com/elastic/elasticsearch/pull/145070)
* Remove Lucene99FlatBulkScoringVectorsReader [#146071](https://github.com/elastic/elasticsearch/pull/146071)
* Return 404 instead of 500 when scroll/PIT references nodes that have left the cluster. [#142405](https://github.com/elastic/elasticsearch/pull/142405)
* Update constant-value fields to support normalized wildcard queries [#141784](https://github.com/elastic/elasticsearch/pull/141784) (issue: [#138778](https://github.com/elastic/elasticsearch/issues/138778))
* Use query circuit breaker for wildcard/regexp determinization [#145427](https://github.com/elastic/elasticsearch/pull/145427) (issue: [#145128](https://github.com/elastic/elasticsearch/issues/145128))

Searchable Snapshots:
* Fix `SharedBytes` mmap leak by closing parent arena on close [#142460](https://github.com/elastic/elasticsearch/pull/142460)

Security:
* This changes extends the `read` index privilege to consistently cover all actions required to run cross-cluster search (CCS) queries. Users with the `read` index privilege will be able to run CCS queries irrespective of the `ccs_minimize_roundtrips` query parameter. [#141376](https://github.com/elastic/elasticsearch/pull/141376)

Snapshot/Restore:
* Ensure deletion of snapshot clone propagate state changes [#142192](https://github.com/elastic/elasticsearch/pull/142192)
* Finalize failed clone entries [#143024](https://github.com/elastic/elasticsearch/pull/143024) (issue: [#142919](https://github.com/elastic/elasticsearch/issues/142919))
* Fix incorrect totalTime when shard snapshot never started [#142361](https://github.com/elastic/elasticsearch/pull/142361)
* Fix read/write counts for copy in repo analysis [#140086](https://github.com/elastic/elasticsearch/pull/140086) (issue: [#126569](https://github.com/elastic/elasticsearch/issues/126569))
* Limit heap used tracking `IndexMetadata` deletions [#140394](https://github.com/elastic/elasticsearch/pull/140394) (issue: [#140018](https://github.com/elastic/elasticsearch/issues/140018))
* Synthesize `ShardId` for `SnapshotInfo` of failed clones [#142920](https://github.com/elastic/elasticsearch/pull/142920)
* Terminate Azure retries when node is shutting down [#142187](https://github.com/elastic/elasticsearch/pull/142187)
* Use `IllegalArgumentException` over `RepositoryException` for readonly-repository checks [#140200](https://github.com/elastic/elasticsearch/pull/140200)

Store:
* Fix potential NPE in `SyntheticIdField` empty token stream [#140556](https://github.com/elastic/elasticsearch/pull/140556) (issues: [#140624](https://github.com/elastic/elasticsearch/issues/140624), [#140665](https://github.com/elastic/elasticsearch/issues/140665), [#140492](https://github.com/elastic/elasticsearch/issues/140492))

TSDB:
* Replace `IllegalStateException` with `IllegalArgumentException` for conflicting time series metadata [#142370](https://github.com/elastic/elasticsearch/pull/142370)
* Retrieve routing hash from synthetic id for translog operations [#140221](https://github.com/elastic/elasticsearch/pull/140221)

Task Management:
* Ensure cancellation reason visible when task is canceled [#144629](https://github.com/elastic/elasticsearch/pull/144629) (issue: [#142079](https://github.com/elastic/elasticsearch/issues/142079))

Transform:
* Exclude clusters in license check [#143146](https://github.com/elastic/elasticsearch/pull/143146) (issues: [#114514](https://github.com/elastic/elasticsearch/issues/114514), [#114509](https://github.com/elastic/elasticsearch/issues/114509))

Vector Search:
* Check for support for native vector ops before calling them [#142036](https://github.com/elastic/elasticsearch/pull/142036) (issue: [#141863](https://github.com/elastic/elasticsearch/issues/141863))
* Fix AVX-512 fpclass mask to classify negative infinity as negative in MIP scoring [#142514](https://github.com/elastic/elasticsearch/pull/142514) (issue: [#142289](https://github.com/elastic/elasticsearch/issues/142289))
* Fix BBQ and INT4 bulk scorers to use sparse vector resolution [#145779](https://github.com/elastic/elasticsearch/pull/145779) (issue: [#145797](https://github.com/elastic/elasticsearch/issues/145797))
* Fix NPE in GPU resource pool when CuVSResources creation fails [#146632](https://github.com/elastic/elasticsearch/pull/146632)
* Fix NPE when having double nested field with knn query [#146933](https://github.com/elastic/elasticsearch/pull/146933) (issue: [#141830](https://github.com/elastic/elasticsearch/issues/141830))
* Fix `PosixCloseableMappedByteBuffer.slice()` to preserve concrete type [#147903](https://github.com/elastic/elasticsearch/pull/147903)
* Fix int overflow in vector similarity bounds checks for segments larger than 2GB [#143241](https://github.com/elastic/elasticsearch/pull/143241) (issue: [#143232](https://github.com/elastic/elasticsearch/issues/143232))
* Fix integer overflow in CuVSResourceManager.estimateNNDescentMemory [#147559](https://github.com/elastic/elasticsearch/pull/147559)
* Fix intercepted query cases that can create orphaned unique async action consumers [#145577](https://github.com/elastic/elasticsearch/pull/145577) (issue: [#145444](https://github.com/elastic/elasticsearch/issues/145444))
* Only use `MemorySegment` scorers when slices can be obtained from the `IndexInput` [#145343](https://github.com/elastic/elasticsearch/pull/145343)
* [DiskBBQ] Fix `offHeap` size for empty indices [#146347](https://github.com/elastic/elasticsearch/pull/146347)
* [DiskBBQ] Fix bug in `NeighborQueue#popRawAndAddRaw` [#145324](https://github.com/elastic/elasticsearch/pull/145324)
* [DiskBBQ] Wait for queue saturation in `MaxScoreTopKnnCollector` [#145341](https://github.com/elastic/elasticsearch/pull/145341)

Watcher:
* Clear watch schedules when starting trigger engine [#145325](https://github.com/elastic/elasticsearch/pull/145325) (issues: [#137562](https://github.com/elastic/elasticsearch/issues/137562), [#131964](https://github.com/elastic/elasticsearch/issues/131964))
