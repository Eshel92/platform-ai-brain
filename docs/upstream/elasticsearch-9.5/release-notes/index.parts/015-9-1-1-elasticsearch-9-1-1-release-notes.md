<!-- Part 15 of 18 of release-notes/index.md (split because the page is big). -->

## 9.1.1 [elasticsearch-9.1.1-release-notes]

### Fixes [elasticsearch-9.1.1-fixes]

Data streams:
:::{dropdown} Disables auto-sharding for LOOKUP index mode
Auto-sharding for data streams caused unsupported replica scaling when the index mode was set to `LOOKUP`.
This happened because lookup mappers do not support scaling beyond one replica.
[#131429](https://github.com/elastic/elasticsearch/pull/131429) resolves this issue by disabling auto-sharding for data streams with `LOOKUP` index mode, avoiding unsupported replica settings.
:::

EQL:
:::{dropdown} Resolves EQL parsing failure for IP-mapped fields in `OR` expressions
Parsing EQL queries failed when comparing the same IP-mapped field to multiple values joined by an `OR` expression.
This occurred because lookup operators were internally rewritten into `IN` expressions, which are unsupported for IP-type fields.
[#132167](https://github.com/elastic/elasticsearch/pull/132167) resolves the issue and ensures EQL can now successfully parse and execute such or queries involving IP fields. (issue: [#118621](https://github.com/elastic/elasticsearch/issues/118621))

ES|QL:
:::{dropdown} Fixes inconsistent equality and hashcode behavior for `ConstantNullBlock`
Inconsistent equality checks caused `constantNullBlock.equals(anyDoubleBlock)` to return false, even when `doubleBlock.equals(constantNullBlock)` returned true.
This asymmetry led to unreliable comparisons and mismatched hashcodes when `ConstantNullBlock` was functionally equivalent to other standard blocks.
[#131817](https://github.com/elastic/elasticsearch/pull/131817) resolves the issue and ensures both equality and hashcode functions are symmetric for these block types.
:::
:::{dropdown} Fixes `ConcurrentModificationException` caused by live operator list
A `ConcurrentModificationException` caused test failures in `CrossClusterAsyncEnrichStopIT.testEnrichAfterStop` under certain conditions.
This happened because the ES|QL driver added a live operator list to the `DriverStatus` object, which could be modified while the status was being serialized.
[#132260](https://github.com/elastic/elasticsearch/pull/132260) fixes the issue by copying the operator list before storing it, preventing concurrent changes during status reads.
(issue: [#131564](https://github.com/elastic/elasticsearch/issues/131564))
:::
:::{dropdown} Prevents null pointer exception for `to_lower` and `to_upper` with no parameters
Calling the `to_lower` or `to_upper` functions with no parameters caused a null pointer exception (NPE), instead of returning a clear error.
This behavior was a result of an older implementation of these functions.
[#131917](https://github.com/elastic/elasticsearch/pull/131917) resolves the issue and ensures that empty parameter calls now return the correct error message. (issue: [#131913](https://github.com/elastic/elasticsearch/issues/131913))
:::
:::{dropdown} Fixes `aggregate_metric_double` decoding and `mv_expand` behavior on multi-index queries
Sorting across multiple indices failed when one index contained an `aggregate_metric_double` field and another did not.
In this case, the missing field was encoded as `NullBlock` but later incorrectly decoded as `AggregateMetricDoubleBlock`, which expects four values. This mismatch caused decoding errors.
[#131658](https://github.com/elastic/elasticsearch/pull/131658) resolves the issue and also improves `mv_expand` by returning the input block unchanged for unsupported `AggregateMetricDoubleBlock` values, avoiding unnecessary errors.
:::
:::{dropdown} Fixes incorrect `ingest_took` value when combining bulk responses
Combining two `BulkResponse` objects with `ingest_took` set to `NO_INGEST_TOOK` resulted in a combined `ingest_took` value of `-2`, which was invalid.
This occurred because the combination logic failed to preserve the sentinel `NO_INGEST_TOOK` constant.
[#132088](https://github.com/elastic/elasticsearch/pull/132088) resolves the issue and ensures the result is correctly set to `NO_INGEST_TOOK` when applicable.
:::
:::{dropdown} Disallows remote ENRICH after FORK in query plans
An invalid combination of `FORK` followed by a remote-only `ENRICH` caused incorrect query planning and failed executions. [#131945](https://github.com/elastic/elasticsearch/pull/131945) resolves the issue by explicitly disallowing this combination, preventing invalid plans from being executed. (issue: [#131445](https://github.com/elastic/elasticsearch/issues/131445))
:::
:::{dropdown} Adds support for splitting large pages on load to avoid memory pressure
Loading large rows from a single segment occasionally created oversized pages when decoding values row-by-row, particularly for text and geo fields.
This could cause memory pressure or degraded performance.
[#131053](https://github.com/elastic/elasticsearch/pull/131053) resolves the issue by estimating the size of each page as rows are loaded.
If the estimated size exceeds a configurable `jumbo` threshold (defaulting to one megabyte), row loading stops early, the page is returned, and remaining rows are processed in subsequent iterations.
This prevents loading incomplete or oversized pages during data aggregation.
:::

Infra/Core:
:::{dropdown} Grants server module read/write permissions for deprecated `path.shared_data` setting
Grants the server module read/write access to the deprecated `path.shared_data` setting.
[#131680](https://github.com/elastic/elasticsearch/pull/131680) resolves issues surfaced in internal testing and ensures compatibility with legacy configurations.
:::

Ingest Node:
:::{dropdown} Fixes incorrect mapping resolution in simulate ingest API when `mapping_addition` is provided
When using the simulate ingest API with a `mapping_addition`, the system incorrectly ignored the existing mapping of the target index and instead applied the mapping from a matching index template, if one existed.
This caused mismatches between the index and simulation behavior.
[#132101](https://github.com/elastic/elasticsearch/pull/132101) resolves the issue and ensures that the index’s actual mapping is used when available, preserving consistency between simulation and execution.
:::

Machine Learning:
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
:::{dropdown} Fixes index sort compatibility for `date_nanos` fields in indices created before 7.14
Indices created prior to version 7.14 that used an index sort on a `date_nanos` field could not be opened in more recent versions due to a mismatch in the default `index.sort.missing` value.
A change in version 7.14 modified the default from `Long.MIN_VALUE` to `0L`, which caused newer versions to reject those older indices.
[#132162](https://github.com/elastic/elasticsearch/pull/132162) resolves the issue by restoring the expected default value for indices created before 7.14, allowing them to open successfully in newer versions. (issue: [#132040](https://github.com/elastic/elasticsearch/issues/132040))
:::
:::{dropdown} Fix missing removal of query cancellation callback in QueryPhase
The timeout cancellation callback registered in `QueryPhase` via `addQueryCancellation` was not removed after the query phase completed.
This caused unintended timeouts or cancellations during subsequent phases under specific conditions (such as large datasets, low timeouts, and partial search results enabled).
[#130279](https://github.com/elastic/elasticsearch/pull/130279) resolves the issue and ensures predictable behavior by reintroducing the cleanup logic. (issue: [#130071](https://github.com/elastic/elasticsearch/issues/130071))
:::
