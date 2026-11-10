<!-- Converted from cat/anomaly-detectors.asciidoc (AsciiDoc). Includes are inlined. -->

### cat anomaly detectors API

**New API reference**
For the most up-to-date API details, refer to [Compact and aligned text (CAT) APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-cat)..

**Important:**
cat APIs are only intended for human consumption using the command line or Kibana
console. They are _not_ intended for use by applications. For application
consumption, use the
get anomaly detection job statistics API.

Returns configuration and usage information about anomaly detection jobs.

#### Request

`GET /_cat/ml/anomaly_detectors/<job_id>` +

`GET /_cat/ml/anomaly_detectors`

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have `monitor_ml`,
`monitor`, `manage_ml`, or `manage` cluster privileges to use this API. See
security-privileges and {ml-docs-setup-privileges}.

#### Description

**Note:** This API returns a maximum of 10,000 jobs.

For more information about anomaly detection, see
{ml-docs}/ml-ad-finding-anomalies.html[Finding anomalies].

#### Path parameters

`<job_id>`::
(Optional, string)
Identifier for the anomaly detection job.

#### Query parameters

`allow_no_match`::
(Optional, Boolean)
Specifies what to do when the request:
* Contains wildcard expressions and there are no jobs that match.
* Contains the `_all` string or no identifiers and there are no matches.
* Contains wildcard expressions and there are only partial matches.

The default value is `true`, which returns an empty `jobs` array
when there are no matches and the subset of results when there are partial
matches. If this parameter is `false`, the request returns a `404` status code
when there are no matches or only partial matches.
`bytes`::
(Optional, byte size units) Unit used to display byte values.
`format`::
(Optional, string) Short version of the
[HTTP accept header](https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html).
Valid values include JSON, YAML, etc.
`h`::
(Optional, string) Comma-separated list of column names to display.
If you do not specify which columns to include, the API returns the default
columns. If you explicitly specify one or more columns, it returns only the
specified columns.
Valid columns are:

`assignment_explanation`, `ae`:::
For open anomaly detection jobs only, contains messages relating to the selection
of a node to run the job.
`buckets.count`, `bc`, `bucketsCount`:::
(Default)
The number of bucket results produced by the job.
`buckets.time.exp_avg`, `btea`, `bucketsTimeExpAvg`:::
Exponential moving average of all bucket processing times, in milliseconds.
`buckets.time.exp_avg_hour`, `bteah`, `bucketsTimeExpAvgHour`:::
Exponentially-weighted moving average of bucket processing times
calculated in a 1 hour time window, in milliseconds.
`buckets.time.max`, `btmax`, `bucketsTimeMax`:::
Maximum among all bucket processing times, in milliseconds.
`buckets.time.min`, `btmin`, `bucketsTimeMin`:::
Minimum among all bucket processing times, in milliseconds.
`buckets.time.total`, `btt`, `bucketsTimeTotal`:::
Sum of all bucket processing times, in milliseconds.
`data.buckets`, `db`, `dataBuckets`:::
The number of buckets processed.
`data.earliest_record`, `der`, `dataEarliestRecord`:::
The timestamp of the earliest chronologically input document.
`data.empty_buckets`, `deb`, `dataEmptyBuckets`:::
The number of buckets which did not contain any data. If your data
contains many empty buckets, consider increasing your `bucket_span` or using
functions that are tolerant to gaps in data such as `mean`, `non_null_sum` or
`non_zero_count`.
`data.input_bytes`, `dib`, `dataInputBytes`:::
The number of bytes of input data posted to the anomaly detection job.
`data.input_fields`, `dif`, `dataInputFields`:::
The total number of fields in input documents posted to the anomaly detection job. This
count includes fields that are not used in the analysis. However, be aware that
if you are using a datafeed, it extracts only the required fields from the
documents it retrieves before posting them to the job.
`data.input_records`, `dir`, `dataInputRecords`:::
The number of input documents posted to the anomaly detection job.
`data.invalid_dates`, `did`, `dataInvalidDates`:::
The number of input documents with either a missing date field or a date that
could not be parsed.
`data.last`, `dl`, `dataLast`:::
The timestamp at which data was last analyzed, according to server time.
`data.last_empty_bucket`, `dleb`, `dataLastEmptyBucket`:::
The timestamp of the last bucket that did not contain any data.
`data.last_sparse_bucket`, `dlsb`, `dataLastSparseBucket`:::
The timestamp of the last bucket that was considered sparse.
`data.latest_record`, `dlr`, `dataLatestRecord`:::
The timestamp of the latest chronologically input document.
`data.missing_fields`, `dmf`, `dataMissingFields`:::
The number of input documents that are missing a field that the anomaly detection job is
configured to analyze. Input documents with missing fields are still processed
because it is possible that not all fields are missing.
**Note:** If you are using datafeeds or posting data to the job in JSON format, a
high `missing_field_count` is often not an indication of data issues. It is not
necessarily a cause for concern.

`data.out_of_order_timestamps`, `doot`, `dataOutOfOrderTimestamps`:::
The number of input documents that have a timestamp chronologically
preceding the start of the current anomaly detection bucket offset by
the latency window. This information is applicable only when you provide
data to the anomaly detection job by using the post data API.
These out of order documents are discarded, since jobs require time
series data to be in ascending chronological order.
`data.processed_fields`, `dpf`, `dataProcessedFields`:::
The total number of fields in all the documents that have been processed by the
anomaly detection job. Only fields that are specified in the detector configuration
object contribute to this count. The timestamp is not included in this count.
`data.processed_records`, `dpr`, `dataProcessedRecords`:::
(Default)
The number of input documents that have been processed by the anomaly detection job.
This value includes documents with missing fields, since they are nonetheless
analyzed. If you use datafeeds and have aggregations in your search query, the
`processed_record_count` is the number of aggregation results processed, not the
number of Elasticsearch documents.
`data.sparse_buckets`, `dsb`, `dataSparseBuckets`:::
The number of buckets that contained few data points compared to the expected
number of data points. If your data contains many sparse buckets, consider using
a longer `bucket_span`.
`forecasts.memory.avg`, `fmavg`, `forecastsMemoryAvg`:::
The average memory usage in bytes for forecasts related to the anomaly detection job.

`forecasts.memory.max`, `fmmax`, `forecastsMemoryMax`:::
The maximum memory usage in bytes for forecasts related to the anomaly detection job.

`forecasts.memory.min`, `fmmin`, `forecastsMemoryMin`:::
The minimum memory usage in bytes for forecasts related to the anomaly detection job.

`forecasts.memory.total`, `fmt`, `forecastsMemoryTotal`:::
The total memory usage in bytes for forecasts related to the anomaly detection job.

`forecasts.records.avg`, `fravg`, `forecastsRecordsAvg`:::
The average number of `model_forecast` documents written for forecasts related
to the anomaly detection job.

`forecasts.records.max`, `frmax`, `forecastsRecordsMax`:::
The maximum number of `model_forecast` documents written for forecasts related
to the anomaly detection job.

`forecasts.records.min`, `frmin`, `forecastsRecordsMin`:::
The minimum number of `model_forecast` documents written for forecasts related
to the anomaly detection job.

`forecasts.records.total`, `frt`, `forecastsRecordsTotal`:::
The total number of `model_forecast` documents written for forecasts related to
the anomaly detection job.

`forecasts.time.avg`, `ftavg`, `forecastsTimeAvg`:::
The average runtime in milliseconds for forecasts related to the anomaly detection job.

`forecasts.time.max`, `ftmax`, `forecastsTimeMax`:::
The maximum runtime in milliseconds for  forecasts related to the anomaly detection job.

`forecasts.time.min`, `ftmin`, `forecastsTimeMin`:::
The minimum runtime in milliseconds for forecasts related to the anomaly detection job.

`forecasts.time.total`, `ftt`, `forecastsTimeTotal`:::
The total runtime in milliseconds for forecasts related to the anomaly detection job.

`forecasts.total`, `ft`, `forecastsTotal`:::
(Default)
The number of individual forecasts currently available for the job. A value of
`1` or more indicates that forecasts exist.
`id`:::
(Default)
Identifier for the anomaly detection job.
`model.bucket_allocation_failures`, `mbaf`, `modelBucketAllocationFailures`:::
The number of buckets for which new entities in incoming data were not processed
due to insufficient model memory. This situation is also signified by a
`hard_limit: memory_status` property value.
`model.by_fields`, `mbf`, `modelByFields`:::
The number of `by` field values that were analyzed by the models. This value is
cumulative for all detectors in the job.
`model.bytes`, `mb`, `modelBytes`:::
(Default)
The number of bytes of memory used by the models. This is the maximum value
since the last time the model was persisted. If the job is closed, this value
indicates the latest size.
`model.bytes_exceeded`, `mbe`, `modelBytesExceeded`:::
The number of bytes over the high limit for memory usage at the last allocation
failure.
`model.categorization_status`, `mcs`, `modelCategorizationStatus`:::
The status of categorization for the job. Contains one of the following values:
* `ok`: Categorization is performing acceptably well (or not being used at all).
* `warn`: Categorization is detecting a distribution of categories that suggests
the input data is inappropriate for categorization. Problems could be that there
is only one category, more than 90% of categories are rare, the number of
categories is greater than 50% of the number of categorized documents, there are
no frequently matched categories, or more than 50% of categories are dead.

`model.categorized_doc_count`, `mcdc`, `modelCategorizedDocCount`:::
The number of documents that have had a field categorized.
`model.dead_category_count`, `mdcc`, `modelDeadCategoryCount`:::
The number of categories created by categorization that will never be assigned
again because another category's definition makes it a superset of the dead
category. (Dead categories are a side effect of the way categorization has no
prior training.)
`model.failed_category_count`, `mdcc`, `modelFailedCategoryCount`:::
The number of times that categorization wanted to create a new category but
couldn't because the job had hit its `model_memory_limit`. This count does not
track which specific categories failed to be created. Therefore you cannot use
this value to determine the number of unique categories that were missed.
`model.frequent_category_count`, `mfcc`, `modelFrequentCategoryCount`:::
The number of categories that match more than 1% of categorized documents.
`model.log_time`, `mlt`, `modelLogTime`:::
The timestamp when the model stats were gathered, according to server time.

`model.memory_limit`, `mml`, `modelMemoryLimit`:::
The upper limit for model memory usage, checked on increasing values.
`model.memory_status`, `mms`, `modelMemoryStatus`:::
(Default)
The status of the mathematical models, which can have one of the following
values:
* `ok`: The models stayed below the configured value.
* `soft_limit`: The models used more than 60% of the configured memory limit
and older unused models will be pruned to free up space. Additionally, in
categorization jobs no further category examples will be stored.
* `hard_limit`: The models used more space than the configured memory limit.
As a result, not all incoming data was processed.
`model.output_memory_allocator_bytes`, `momab`, `modelOutputMemoryAllocatorBytes`:::
The amount of memory, in bytes, used to output anomaly detection job documents.
`model.over_fields`, `mof`, `modelOverFields`:::
The number of `over` field values that were analyzed by the models. This value
is cumulative for all detectors in the job.
`model.partition_fields`, `mpf`, `modelPartitionFields`:::
The number of `partition` field values that were analyzed by the models. This
value is cumulative for all detectors in the job.
`model.rare_category_count`, `mrcc`, `modelRareCategoryCount`:::
The number of categories that match just one categorized document.
`model.timestamp`, `mt`, `modelTimestamp`:::
The timestamp of the last record when the model stats were gathered.
`model.total_category_count`, `mtcc`, `modelTotalCategoryCount`:::
The number of categories created by categorization.
`node.address`, `na`, `nodeAddress`:::
The network address of the node.
Contains properties for the node that runs the job. This information is
available only for open jobs.
`node.ephemeral_id`, `ne`, `nodeEphemeralId`:::
The ephemeral ID of the node.
Contains properties for the node that runs the job. This information is
available only for open jobs.
`node.id`, `ni`, `nodeId`:::
The unique identifier of the node.
Contains properties for the node that runs the job. This information is
available only for open jobs.
`node.name`, `nn`, `nodeName`:::
The node name.
Contains properties for the node that runs the job. This information is
available only for open jobs.
`opened_time`, `ot`:::
For open jobs only, the elapsed time for which the job has been open.
`state`, `s`:::
(Default)
The status of the anomaly detection job, which can be one of the following values:
* `closed`: The job finished successfully with its model state persisted. The
job must be opened before it can accept further data.
* `closing`: The job close action is in progress and has not yet completed. A
closing job cannot accept further data.
* `failed`: The job did not finish successfully due to an error. This situation
can occur due to invalid input data, a fatal error occurring during the
analysis, or an external interaction such as the process being killed by the
Linux out of memory (OOM) killer. If the job had irrevocably failed, it must be
force closed and then deleted. If the datafeed can be corrected, the job can be
closed and then re-opened.
* `opened`: The job is available to receive and process data.
* `opening`: The job open action is in progress and has not yet completed.
`help`::
(Optional, Boolean) If `true`, the response includes help information. Defaults
to `false`.
`s`::
(Optional, string) Comma-separated list of column names or column aliases used
to sort the response.
`time`::
(Optional, time units)
Unit used to display time values.
`v`::
(Optional, Boolean) If `true`, the response includes column headings.
Defaults to `false`.

#### Examples

```console
GET _cat/ml/anomaly_detectors?h=id,s,dpr,mb&v=true
```

```console-result
id                        s dpr   mb
high_sum_total_sales closed 14022 1.5mb
low_request_rate     closed 1216  40.5kb
response_code_rates  closed 28146 132.7kb
url_scanning         closed 28146 501.6kb
```
