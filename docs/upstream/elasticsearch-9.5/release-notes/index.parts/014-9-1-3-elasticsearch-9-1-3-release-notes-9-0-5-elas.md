<!-- Part 14 of 18 of release-notes/index.md (split because the page is big). -->

## 9.1.3 [elasticsearch-9.1.3-release-notes]

### Highlights [elasticsearch-9.1.3-highlights]

::::{dropdown} Security advisory
The 9.1.3 release contains fixes for potential security vulnerabilities. Please see our [security advisory](https://discuss.elastic.co/c/announcements/security-announcements/31) for more details.
::::

### Features and enhancements [elasticsearch-9.1.3-features-enhancements]

Infra/REST API:
* Limit the depth of a filter [#133113](https://github.com/elastic/elasticsearch/pull/133113)

Ingest Node:
* Upgrading to tika 3.2.2 [#133410](https://github.com/elastic/elasticsearch/pull/133410)

Packaging:
* Update bundled JDK to Java 24.0.2+12 [#133119](https://github.com/elastic/elasticsearch/pull/133119)


### Fixes [elasticsearch-9.1.3-fixes]

Data streams:
* Force rollover on write to true when data stream indices list is empty [#133347](https://github.com/elastic/elasticsearch/pull/133347) (issue: [#133176](https://github.com/elastic/elasticsearch/issues/133176))

EQL:
* Better error message for sequences with only one clause plus UNTIL [#132638](https://github.com/elastic/elasticsearch/pull/132638)
* Fix sequences with conditions involving keys and non-keys [#133134](https://github.com/elastic/elasticsearch/pull/133134)

ES|QL:
* Fix update expiration for async query [#133021](https://github.com/elastic/elasticsearch/pull/133021) (issue: [#130619](https://github.com/elastic/elasticsearch/issues/130619))

Ingest Node:
* Change GeoIpCache and EnrichCache to LongAdder [#132922](https://github.com/elastic/elasticsearch/pull/132922)

License:
* Limit frequency of feature last-used time updates [#133004](https://github.com/elastic/elasticsearch/pull/133004)

Machine Learning:
* Disable child span for streaming tasks [#132945](https://github.com/elastic/elasticsearch/pull/132945)
* Improve EIS auth call logs and fix revocation bug [#132546](https://github.com/elastic/elasticsearch/pull/132546)
* Preserve lost thread context in node inference action. A lost context causes a memory leak if APM tracing is enabled [#132973](https://github.com/elastic/elasticsearch/pull/132973)
* Update EIS sparse and dense embedding max batch size to 16 [#132646](https://github.com/elastic/elasticsearch/pull/132646)
* [EIS] Rename the elser 2 default model and the default inference endpoint [#130336](https://github.com/elastic/elasticsearch/pull/130336)

Search:
* Don't fail search if bottom doc can't be formatted [#133188](https://github.com/elastic/elasticsearch/pull/133188) (issue: [#125321](https://github.com/elastic/elasticsearch/issues/125321))




## 9.1.2 [elasticsearch-9.1.2-release-notes]

### Features and enhancements [elasticsearch-9.1.2-features-enhancements]

Authorization:
* [ExtraHop & QualysGAV] Add `manage`, `create_index`, `read`, `index`, `write`, `delete`, permission for third party agent indices `kibana_system` [#132387](https://github.com/elastic/elasticsearch/pull/132387) (issue: [#131825](https://github.com/elastic/elasticsearch/issues/131825))


### Fixes [elasticsearch-9.1.2-fixes]

Aggregations:
:::{dropdown} Validates parent aggregation type in `bucket_script`
The `bucket_script` pipeline aggregation didn’t validate that its parent aggregation was a multi-bucket aggregation.
This caused a `ClassCastException` at runtime when the parent was not multi-bucket.
[#132320](https://github.com/elastic/elasticsearch/pull/132320) adds a validation step so the aggregation fails early, preventing the runtime error. (issue: [#132272](https://github.com/elastic/elasticsearch/issues/132272))
:::

Codec:
:::{dropdown} Uses local segment `fieldInfos` for TSDB merge stats
Merging shrink TSDB or LogsDB indices in versions 8.19 or 9.1+ could fail when using `addIndexes` to combine Lucene segments directly.
In these cases, the `fieldInfos` value could differ between shards and the merged segment, causing incorrect merge statistics.
PR [#132597](https://github.com/elastic/elasticsearch/pull/132597) updates the process to use `fieldInfos` from each segment instead of the merged segment, ensuring accurate stats and preventing merge failures.
:::

ES|QL:
:::{dropdown} Fixes for `COPY_SIGN` function in ESQL
The `COPY_SIGN` function has been updated to better support the literal `NULL` in parameters.
[#132459](https://github.com/elastic/elasticsearch/pull/132459)
:::

Mapping:
:::{dropdown} Calculates text string length correctly for code points outside BMP
Strings parsed with the optimized UTF-8 parsing path had incorrect length calculations for characters outside the basic multilingual plane (BMP).
These characters require two UTF-16 code units, but the optimized path did not account for this, causing mismatches with the non-optimized path.
[#132593](https://github.com/elastic/elasticsearch/pull/132593) fixes the calculation to ensure consistent and correct string lengths.
:::

Search:
:::{dropdown} Always stops the timer when profiling the fetch phase
Exceptions in fetch sub-phases (for example, `setNextReader`) left the profiling timer running, causing mismatched start/stop calls and errors.
[#132570](https://github.com/elastic/elasticsearch/pull/132570) ensures the `timer.stop()` call always stops.
:::




## 9.0.5 [elasticsearch-9.0.5-release-notes]

### Features and enhancements [elasticsearch-9.0.5-features-enhancements]

Engine:
* Track & log when there is insufficient disk space available to execute merges [#131711](https://github.com/elastic/elasticsearch/pull/131711)


### Fixes [elasticsearch-9.0.5-fixes]

Aggregations:
:::{dropdown} Validate parent aggregation type in `bucket_script`
The `bucket_script` pipeline aggregation didn’t validate that its parent aggregation was a multi-bucket aggregation.
This caused a `ClassCastException` at runtime when the parent was not multi-bucket.
[#132320](https://github.com/elastic/elasticsearch/pull/132320) adds a validation step so the aggregation fails early, preventing the runtime error. (issue: [#132272](https://github.com/elastic/elasticsearch/issues/132272))
:::

Data streams:
:::{dropdown} Disables auto-sharding for LOOKUP index mode
Auto-sharding for data streams caused unsupported replica scaling when the index mode was set to `LOOKUP`.
This happened because lookup mappers do not support scaling beyond one replica.
[#131429](https://github.com/elastic/elasticsearch/pull/131429) resolves this issue by disabling auto-sharding for data streams with `LOOKUP` index modes, avoiding unsupported replica settings.
:::

EQL:
:::{dropdown} Resolves EQL parsing failure for IP-mapped fields in `OR` expressions
Parsing EQL queries failed when comparing the same IP-mapped field to multiple values joined by an `OR` expression.
This occurred because lookup operators were internally rewritten into `IN` expressions, which are unsupported for IP-type fields.
[#132167](https://github.com/elastic/elasticsearch/pull/132167) resolves the issue and ensures EQL can now successfully parse and execute such or queries involving IP fields. (issue: [#118621](https://github.com/elastic/elasticsearch/issues/118621))
:::
:::{dropdown} Prevent double invocation of EQL listener
In some cases, the EQL listener could be resolved twice, potentially leading to unexpected behavior.
[#124918](https://github.com/elastic/elasticsearch/pull/124918) updates the control flow to exit early and ensure the listener is only invoked once.
:::

ES|QL:
:::{dropdown} Disallow remote `ENRICH` after `LOOKUP JOIN`
Combining a `LOOKUP JOIN` with remote `ENRICH` could trigger a `ClassCastException` due to pipeline breaker interactions when limits or top-N queries were involved. [#131426](https://github.com/elastic/elasticsearch/pull/131426) adds a validation that forbids remote `ENRICH` after `LOOKUP JOIN`, preventing the runtime error. (issue: [#129372](https://github.com/elastic/elasticsearch/issues/129372))
:::
:::{dropdown} Fix `mv_expand` inconsistent column order
The `mv_expand` command could return columns in a different order depending on query execution paths. Now, the new attribute generated by `mv_expand` preserves the original field positions in the output. [#129745](https://github.com/elastic/elasticsearch/pull/129745) (issue: [#129000](https://github.com/elastic/elasticsearch/issues/129000))
:::
:::{dropdown} Fixes `ConcurrentModificationException` caused by live operator list
A `ConcurrentModificationException` caused test failures in `CrossClusterAsyncEnrichStopIT.testEnrichAfterStop` under certain conditions.
This happened because the ES|QL driver added a live operator list to the `DriverStatus` object, which could be modified while the status was being serialized.
[#132260](https://github.com/elastic/elasticsearch/pull/132260) fixes the issue by copying the operator list before storing it, preventing concurrent changes during status reads.
(issue: [#131564](https://github.com/elastic/elasticsearch/issues/131564))
:::

Infra/Core:
:::{dropdown} Grants server module read/write permissions for deprecated `path.shared_data` setting
The server module is now granted read/write permissions for the deprecated `path.shared_data` setting.
[#131680](https://github.com/elastic/elasticsearch/pull/131680) resolves issues surfaced in internal testing and ensures compatibility with legacy configurations.
:::

Ingest Node:
:::{dropdown} Correctly handle `download_database_on_pipeline_creation` in default or final pipelines
A bug in the `download_database_on_pipeline_creation` setting caused geoip databases not to download when the geoip processor was referenced from a pipeline processor in a default or final pipeline.
This resulted in documents being tagged with `_geoip_database_unavailable_GeoLite2-City.mmdb` instead of having geo data.
[#131236](https://github.com/elastic/elasticsearch/pull/131236) resolves the issue and ensures geoip databases download correctly in this scenario.
:::
:::{dropdown} Fixes incorrect mapping resolution in simulate ingest API when `mapping_addition` is provided
When using the simulate ingest API with a `mapping_addition`, the system incorrectly ignored the existing mapping of the target index and instead applied the mapping from a matching index template, if one existed.
This caused mismatches between the index and simulation behavior.
[#132101](https://github.com/elastic/elasticsearch/pull/132101) resolves the issue and ensures that the index’s actual mapping is used when available, preserving consistency between simulation and execution.
:::

Machine Learning:
:::{dropdown} Fix memory usage estimation for ELSER models
Using the deployment ID instead of the model ID caused `isElserV1Or2Model` to fail for ELSER models, because deployment IDs don’t start with `.elser_model_2`.
[#131630](https://github.com/elastic/elasticsearch/pull/131630) updates the code to pass the model ID, ensuring memory usage is estimated correctly.
:::
:::{dropdown} Prevents double-counting of allocations in trained model deployment memory estimation
A recent refactor introduced a bug that caused the trained model memory estimation to double-count the number of allocations, leading to inflated memory usage projections.
[#131990](https://github.com/elastic/elasticsearch/pull/131990) resolves the issue by reverting the change and restoring accurate memory estimation for trained model deployments.
:::

Mapping:
:::{dropdown} Fixes decoding failure for non-ASCII field names in `_ignored_source`
A decoding error occurred when field names in `_ignored_source` contained non-ASCII characters.
This happened because `String.length()` was used to calculate the byte length of the field name, which only works correctly for ASCII characters.
[#132018](https://github.com/elastic/elasticsearch/pull/132018) resolves the issue by using the actual byte array length of the encoded field name, ensuring proper decoding regardless of character encoding.
:::

Search:
:::{dropdown} Correct shard status reporting in point-in-time responses
The Open PIT API incorrectly swapped the skipped and failed shard counts when partial search results were allowed. This caused the API to report failed shards as skipped and vice versa. [#131391](https://github.com/elastic/elasticsearch/pull/131391) fixes the field mapping so shard status is reported accurately. (issue: [#131026](https://github.com/elastic/elasticsearch/issues/131026))
:::
:::{dropdown} Fix missing removal of query cancellation callback in QueryPhase
A missing removal of a query cancellation callback caused unintended timeouts or cancellations in later search phases when `allow_partial_search_results` was enabled, which could lead to `ArrayIndexOutOfBoundsException` errors.
[#130279](https://github.com/elastic/elasticsearch/pull/130279) resolves the issue and ensures predictable search execution. (issue: [#130071](https://github.com/elastic/elasticsearch/issues/130071))
:::
:::{dropdown} Preserve `boost` and `queryName` for semantic queries
Query rewrite logic dropped `boost` and `queryName` values for `match`, `knn`, and `sparse_vector` queries on `semantic_text` fields, causing query weighting and naming to be lost. [#129282](https://github.com/elastic/elasticsearch/pull/129282) resolves the issue so these values are now preserved correctly during query rewriting.
:::

Snapshot/Restore:
:::{dropdown} Improve error handling when verifying an empty snapshot repository

Verifying the integrity of a brand-new snapshot repository without any index blobs failed with a low-level error because the repository generation was `-1`, which cannot be sent over the wire. [#131677](https://github.com/elastic/elasticsearch/pull/131677) updates the logic to reject such requests early with a clearer, more helpful error message.
:::
