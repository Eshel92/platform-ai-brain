<!-- Converted from ml/anomaly-detection/apis/get-job-stats.asciidoc (AsciiDoc). Includes are inlined. -->

# Get anomaly detection job statistics API

**New API reference**
For the most up-to-date API details, refer to [Machine learning  anomaly detection APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-ml-anomaly).

Retrieves usage information for anomaly detection jobs.

## Request

`GET _ml/anomaly_detectors/<job_id>/_stats`

`GET _ml/anomaly_detectors/<job_id>,<job_id>/_stats` +

`GET _ml/anomaly_detectors/_stats` +

`GET _ml/anomaly_detectors/_all/_stats`

## Prerequisites

Requires the `monitor_ml` cluster privilege. This privilege is included in the 
`machine_learning_user` built-in role.

## Description

**Important:** This API returns a maximum of 10,000 jobs.

## Path parameters

`<job_id>`::
(Optional, string)
Identifier for the anomaly detection job. It can be a job identifier, a group
name, or a wildcard expression. You can get statistics for multiple
anomaly detection jobs in a single API request by using a group name, a comma-separated
list of jobs, or a wildcard expression. You can get statistics for all
anomaly detection jobs by using `_all`, by specifying `*` as the job identifier, or by
omitting the identifier.

## Query parameters

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

## Response body

The API returns the following information about the operational progress of a
job:

`assignment_explanation`::
(string)
For open anomaly detection jobs only, contains messages relating to the selection
of a node to run the job.
[[datacounts]]`data_counts`::
(object) An object that describes the quantity of input to the job and any
related error counts. The `data_count` values are cumulative for the lifetime of
a job. If a model snapshot is reverted or old results are deleted, the job
counts are not reset.
**Properties of `data_counts`**
`bucket_count`:::
(long)
The number of bucket results produced by the job.
`earliest_record_timestamp`:::
(date)
The timestamp of the earliest chronologically input document.
`empty_bucket_count`:::
(long)
The number of buckets which did not contain any data. If your data
contains many empty buckets, consider increasing your `bucket_span` or using
functions that are tolerant to gaps in data such as `mean`, `non_null_sum` or
`non_zero_count`.
`input_bytes`:::
(long)
The number of bytes of input data posted to the anomaly detection job.
`input_field_count`:::
(long)
The total number of fields in input documents posted to the anomaly detection job. This
count includes fields that are not used in the analysis. However, be aware that
if you are using a datafeed, it extracts only the required fields from the
documents it retrieves before posting them to the job.
`input_record_count`:::
(long)
The number of input documents posted to the anomaly detection job.
`invalid_date_count`:::
(long)
The number of input documents with either a missing date field or a date that
could not be parsed.
`job_id`:::
(string)
Identifier for the anomaly detection job.
`last_data_time`:::
(date)
The timestamp at which data was last analyzed, according to server time.
`latest_empty_bucket_timestamp`:::
(date)
The timestamp of the last bucket that did not contain any data.
`latest_record_timestamp`:::
(date)
The timestamp of the latest chronologically input document.
`latest_sparse_bucket_timestamp`:::
(date)
The timestamp of the last bucket that was considered sparse.
`log_time`:::
(date) The timestamp of the `data_counts` according to server time.

`missing_field_count`:::
(long)
The number of input documents that are missing a field that the anomaly detection job is
configured to analyze. Input documents with missing fields are still processed
because it is possible that not all fields are missing.
**Note:** If you are using datafeeds or posting data to the job in JSON format, a
high `missing_field_count` is often not an indication of data issues. It is not
necessarily a cause for concern.

The value of `processed_record_count` includes this count.

`out_of_order_timestamp_count`:::
(long)
The number of input documents that have a timestamp chronologically
preceding the start of the current anomaly detection bucket offset by
the latency window. This information is applicable only when you provide
data to the anomaly detection job by using the post data API.
These out of order documents are discarded, since jobs require time
series data to be in ascending chronological order.
`processed_field_count`:::
The total number of fields in all the documents that have been processed by the
anomaly detection job. Only fields that are specified in the detector configuration
object contribute to this count. The timestamp is not included in this count.
`processed_record_count`:::
(long)
The number of input documents that have been processed by the anomaly detection job.
This value includes documents with missing fields, since they are nonetheless
analyzed. If you use datafeeds and have aggregations in your search query, the
`processed_record_count` is the number of aggregation results processed, not the
number of Elasticsearch documents.
`sparse_bucket_count`:::
(long)
The number of buckets that contained few data points compared to the expected
number of data points. If your data contains many sparse buckets, consider using
a longer `bucket_span`.

`deleting`::
(Boolean)
Indicates that the process of deleting the job is in progress but not yet
completed. It is only reported when `true`.

[[forecastsstats]]`forecasts_stats`::
(object) An object that provides statistical information about forecasts
belonging to this job. Some statistics are omitted if no forecasts have been
made.
**Note:** Unless there is at least one forecast, `memory_bytes`, `records`,
`processing_time_ms` and `status` properties are omitted.
**Properties of `forecasts_stats`**
`forecasted_jobs`:::
(long) A value of `0` indicates that forecasts do not exist for this job. A
value of `1` indicates that at least one forecast exists.

`memory_bytes`:::
(object) The `avg`, `min`, `max` and `total` memory usage in bytes for forecasts
related to this job. If there are no forecasts, this property is omitted.

`records`:::
(object) The `avg`, `min`, `max` and `total` number of `model_forecast` documents
written for forecasts related to this job. If there are no forecasts, this
property is omitted.

`processing_time_ms`:::
(object) The `avg`, `min`, `max` and `total` runtime in milliseconds for
forecasts related to this job. If there are no forecasts, this property is omitted.

`status`:::
(object) The count of forecasts by their status. For example:
{"finished" : 2, "started" : 1}. If there are no forecasts, this property is omitted.

`total`:::
(long)
The number of individual forecasts currently available for the job. A value of
`1` or more indicates that forecasts exist.

`job_id`::
(string)
Identifier for the anomaly detection job.
[[modelsizestats]]`model_size_stats`::
(object) An object that provides information about the size and contents of the
model.
**Properties of `model_size_stats`**
`assignment_memory_basis`:::
(string)
Indicates where to find the memory requirement that is used to decide where the
job runs. The possible values are:
* `model_memory_limit`: The job's memory requirement is calculated on the basis
that its model memory will grow to the `model_memory_limit` specified in the
`analysis_limits` of its config.
* `current_model_bytes`: The job's memory requirement is calculated on the basis
that its current model memory size is a good reflection of what it will be in
the future.
* `peak_model_bytes`: The job's memory requirement is calculated on the basis
that its peak model memory size is a good reflection of what the model size will
be in the future.
`bucket_allocation_failures_count`:::
(long)
The number of buckets for which new entities in incoming data were not processed
due to insufficient model memory. This situation is also signified by a
`hard_limit: memory_status` property value.
`categorized_doc_count`:::
(long)
The number of documents that have had a field categorized.
`categorization_status`:::
(string)
The status of categorization for the job. Contains one of the following values:
* `ok`: Categorization is performing acceptably well (or not being used at all).
* `warn`: Categorization is detecting a distribution of categories that suggests
the input data is inappropriate for categorization. Problems could be that there
is only one category, more than 90% of categories are rare, the number of
categories is greater than 50% of the number of categorized documents, there are
no frequently matched categories, or more than 50% of categories are dead.

`dead_category_count`:::
(long)
The number of categories created by categorization that will never be assigned
again because another category's definition makes it a superset of the dead
category. (Dead categories are a side effect of the way categorization has no
prior training.)
`failed_category_count`:::
(long)
The number of times that categorization wanted to create a new category but
couldn't because the job had hit its `model_memory_limit`. This count does not
track which specific categories failed to be created. Therefore you cannot use
this value to determine the number of unique categories that were missed.
`frequent_category_count`:::
(long)
The number of categories that match more than 1% of categorized documents.
`job_id`:::
(string)
Identifier for the anomaly detection job.
`log_time`:::
(date) The timestamp of the `model_size_stats` according to server time.

`memory_status`:::
(string)
The status of the mathematical models, which can have one of the following
values:
* `ok`: The models stayed below the configured value.
* `soft_limit`: The models used more than 60% of the configured memory limit
and older unused models will be pruned to free up space. Additionally, in
categorization jobs no further category examples will be stored.
* `hard_limit`: The models used more space than the configured memory limit.
As a result, not all incoming data was processed.
`model_bytes`:::
(long)
The number of bytes of memory used by the models. This is the maximum value
since the last time the model was persisted. If the job is closed, this value
indicates the latest size.
`model_bytes_exceeded`:::
(long)
The number of bytes over the high limit for memory usage at the last allocation
failure.
`model_bytes_memory_limit`:::
(long)
The upper limit for model memory usage, checked on increasing values.
`peak_model_bytes`:::
(long)
The peak number of bytes of memory ever used by the models.
`rare_category_count`:::
(long)
The number of categories that match just one categorized document.
`result_type`:::
(string) For internal use. The type of result.

`total_by_field_count`:::
(long)
The number of `by` field values that were analyzed by the models. This value is
cumulative for all detectors in the job.
`total_category_count`:::
(long)
The number of categories created by categorization.
`total_over_field_count`:::
(long)
The number of `over` field values that were analyzed by the models. This value
is cumulative for all detectors in the job.
`total_partition_field_count`:::
(long)
The number of `partition` field values that were analyzed by the models. This
value is cumulative for all detectors in the job.
`timestamp`:::
(date)
The timestamp of the last record when the model stats were gathered.

[[stats-node]]`node`::
(object) Contains properties for the node that runs the job. This information is
available only for open jobs.
**Properties of `node`**
`attributes`:::
(object)
Lists node attributes such as `ml.machine_memory` or `ml.max_open_jobs` settings.
`ephemeral_id`:::
(string)
The ephemeral ID of the node.
`id`:::
(string)
The unique identifier of the node.
`name`:::
(string) The node name.

`transport_address`:::
(string)
The host and port where transport HTTP connections are accepted.

`open_time`::
(string)
For open jobs only, the elapsed time for which the job has been open.
`state`::
(string)
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
[[timingstats]]`timing_stats`::
(object) An object that provides statistical information about timing aspect of
this job.
**Properties of `timing_stats`**
`average_bucket_processing_time_ms`:::
(double) Average of all bucket processing times in milliseconds.

`bucket_count`:::
(long)
The number of buckets processed.
`exponential_average_bucket_processing_time_ms`:::
(double)
Exponential moving average of all bucket processing times, in milliseconds.
`exponential_average_bucket_processing_time_per_hour_ms`:::
(double)
Exponentially-weighted moving average of bucket processing times
calculated in a 1 hour time window, in milliseconds.
`job_id`:::
(string)
Identifier for the anomaly detection job.
`maximum_bucket_processing_time_ms`:::
(double)
Maximum among all bucket processing times, in milliseconds.
`minimum_bucket_processing_time_ms`:::
(double)
Minimum among all bucket processing times, in milliseconds.
`total_bucket_processing_time_ms`:::
(double)
Sum of all bucket processing times, in milliseconds.

## Response codes

`404` (Missing resources)::
  If `allow_no_match` is `false`, this code indicates that there are no
  resources that match the request or only partial matches for the request.

## Examples

```console
GET _ml/anomaly_detectors/low_request_rate/_stats
```

The API returns the following results:
```js
{
  "count" : 1,
  "jobs" : [
    {
      "job_id" : "low_request_rate",
      "data_counts" : {
        "job_id" : "low_request_rate",
        "processed_record_count" : 1216,
        "processed_field_count" : 1216,
        "input_bytes" : 51678,
        "input_field_count" : 1216,
        "invalid_date_count" : 0,
        "missing_field_count" : 0,
        "out_of_order_timestamp_count" : 0,
        "empty_bucket_count" : 242,
        "sparse_bucket_count" : 0,
        "bucket_count" : 1457,
        "earliest_record_timestamp" : 1575172659612,
        "latest_record_timestamp" : 1580417369440,
        "last_data_time" : 1576017595046,
        "latest_empty_bucket_timestamp" : 1580356800000,
        "input_record_count" : 1216
      },
      "model_size_stats" : {
        "job_id" : "low_request_rate",
        "result_type" : "model_size_stats",
        "model_bytes" : 41480,
        "model_bytes_exceeded" : 0,
        "model_bytes_memory_limit" : 10485760,
        "total_by_field_count" : 3,
        "total_over_field_count" : 0,
        "total_partition_field_count" : 2,
        "bucket_allocation_failures_count" : 0,
        "memory_status" : "ok",
        "categorized_doc_count" : 0,
        "total_category_count" : 0,
        "frequent_category_count" : 0,
        "rare_category_count" : 0,
        "dead_category_count" : 0,
        "failed_category_count" : 0,
        "categorization_status" : "ok",
        "log_time" : 1576017596000,
        "timestamp" : 1580410800000
      },
      "forecasts_stats" : {
        "total" : 1,
        "forecasted_jobs" : 1,
        "memory_bytes" : {
          "total" : 9179.0,
          "min" : 9179.0,
          "avg" : 9179.0,
          "max" : 9179.0
        },
        "records" : {
          "total" : 168.0,
          "min" : 168.0,
          "avg" : 168.0,
          "max" : 168.0
        },
        "processing_time_ms" : {
          "total" : 40.0,
          "min" : 40.0,
          "avg" : 40.0,
          "max" : 40.0
        },
        "status" : {
          "finished" : 1
        }
      },
      "state" : "opened",
      "node" : {
        "id" : "7bmMXyWCRs-TuPfGJJ_yMw",
        "name" : "node-0",
        "ephemeral_id" : "hoXMLZB0RWKfR9UPPUCxXX",
        "transport_address" : "127.0.0.1:9300",
        "attributes" : {
          "ml.machine_memory" : "17179869184",
          "xpack.installed" : "true",
          "ml.max_open_jobs" : "512"
        }
      },
      "assignment_explanation" : "",
      "open_time" : "13s",
      "timing_stats" : {
        "job_id" : "low_request_rate",
        "bucket_count" : 1457,
        "total_bucket_processing_time_ms" : 1094.000000000001,
        "minimum_bucket_processing_time_ms" : 0.0,
        "maximum_bucket_processing_time_ms" : 48.0,
        "average_bucket_processing_time_ms" : 0.75085792724777,
        "exponential_average_bucket_processing_time_ms" : 0.5571716855800993,
        "exponential_average_bucket_processing_time_per_hour_ms" : 15.0
      }
    }
  ]
}
```
