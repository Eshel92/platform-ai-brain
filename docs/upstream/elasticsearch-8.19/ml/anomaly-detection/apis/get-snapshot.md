<!-- Converted from ml/anomaly-detection/apis/get-snapshot.asciidoc (AsciiDoc). Includes are inlined. -->

# Get model snapshots API

**New API reference**
For the most up-to-date API details, refer to [Machine learning  anomaly detection APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-ml-anomaly).

Retrieves information about model snapshots.

## Request

`GET _ml/anomaly_detectors/<job_id>/model_snapshots` +

`GET _ml/anomaly_detectors/<job_id>/model_snapshots/<snapshot_id>`

## Prerequisites

Requires the `monitor_ml` cluster privilege. This privilege is included in the
`machine_learning_user` built-in role.

## Path parameters

`<job_id>`::
(Required, string)
Identifier for the anomaly detection job.
`<snapshot_id>`::
(Optional, string)
Identifier for the model snapshot.
You can get information for multiple snapshots by using a comma-separated list
or a wildcard expression. You can get all snapshots by using `_all`, by
specifying `*` as the snapshot ID, or by omitting the snapshot ID.

## Query parameters

`desc`::
  (Optional, Boolean) If true, the results are sorted in descending order.
  Defaults to `false`.

`end`::
  (Optional, date) Returns snapshots with timestamps earlier than this time.
  Defaults to unset, which means results are not limited to specific timestamps.

`from`::
  (Optional, integer) Skips the specified number of snapshots. Defaults to `0`.

`size`::
  (Optional, integer) Specifies the maximum number of snapshots to obtain.
  Defaults to `100`.

`sort`::
  (Optional, string) Specifies the sort field for the requested snapshots. By
  default, the snapshots are sorted by their timestamp.

`start`::
  (Optional, string) Returns snapshots with timestamps after this time. Defaults
  to unset, which means results are not limited to specific timestamps.

## Request body

You can also specify the query parameters in the request body; the exception are
`from` and `size`, use `page` instead:

`page`::
**Properties of `page`**

`from`:::
(Optional, integer) Skips the specified number of snapshots. Defaults to `0`.

`size`:::
(Optional, integer) Specifies the maximum number of snapshots to obtain.
Defaults to `100`.

## Response body

The API returns an array of model snapshot objects, which have the following
properties:

`description`::
(string) An optional description of the job.

`job_id`::
(string) A numerical character string that uniquely identifies the job that
  the snapshot was created for.

`latest_record_time_stamp`::
(date) The timestamp of the latest processed record.

`latest_result_time_stamp`::
(date) The timestamp of the latest bucket result.

`min_version`::
(string) The minimum machine learning configuration version number required to be
able to restore the model snapshot.

**Note:** From Elasticsearch 8.10.0,  a new version number is used to
track the configuration and state changes in the machine learning plugin. This new
version number is decoupled from the product version and will increment
independently. The `min_version` value represents the new version number.

`model_size_stats`::
(object) Summary information describing the model.
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
(long) The number of buckets for which entities were not processed due to memory
limit constraints.

`categorized_doc_count`:::
(long) The number of documents that have had a field categorized.

`categorization_status`:::
(string) The status of categorization for this job.
Contains one of the following values.
* `ok`: Categorization is performing acceptably well (or not being
used at all).
* `warn`: Categorization is detecting a distribution of categories
that suggests the input data is inappropriate for categorization.
Problems could be that there is only one category, more than 90% of
categories are rare, the number of categories is greater than 50% of
the number of categorized documents, there are no frequently
matched categories, or more than 50% of categories are dead.

`dead_category_count`:::
(long) The number of categories created by categorization that will
never be assigned again because another category's definition
makes it a superset of the dead category.  (Dead categories are a
side effect of the way categorization has no prior training.)

`failed_category_count`:::
(long)
The number of times that categorization wanted to create a new category but
couldn't because the job had hit its `model_memory_limit`. This count does not
track which specific categories failed to be created. Therefore you cannot use
this value to determine the number of unique categories that were missed.
`frequent_category_count`:::
(long) The number of categories that match more than 1% of categorized
documents.

`job_id`:::
(string)
Identifier for the anomaly detection job.
`log_time`:::
(date) The timestamp that the `model_size_stats` were recorded, according to
server-time.

`memory_status`:::
(string) The status of the memory in relation to its `model_memory_limit`.
Contains one of the following values.
* `hard_limit`: The internal models require more space than the configured
memory limit. Some incoming data could not be processed.
* `ok`: The internal models stayed below the configured value.
* `soft_limit`: The internal models require more than 60% of the configured
memory limit and more aggressive pruning will be performed in order to try to
reclaim space.

`model_bytes`:::
(long) An approximation of the memory resources required for this analysis.

`model_bytes_exceeded`:::
(long) The number of bytes over the high limit for memory usage at the last allocation failure.

`model_bytes_memory_limit`:::
(long) The upper limit for memory usage, checked on increasing values.

`peak_model_bytes`:::
(long) The highest recorded value for the model memory usage.

`rare_category_count`:::
(long) The number of categories that match just one categorized document.

`result_type`:::
(string) Internal. This value is always `model_size_stats`.

`timestamp`:::
(date) The timestamp that the `model_size_stats` were recorded, according to the
bucket timestamp of the data.

`total_by_field_count`:::
(long) The number of _by_ field values analyzed. Note that these are counted
separately for each detector and partition.

`total_category_count`:::
(long) The number of categories created by categorization.

`total_over_field_count`:::
(long) The number of _over_ field values analyzed. Note that these are counted
separately for each detector and partition.

`total_partition_field_count`:::
(long) The number of _partition_ field values analyzed.

`retain`::
(Boolean)
If `true`, this snapshot will not be deleted during automatic cleanup of
snapshots older than `model_snapshot_retention_days`. However, this snapshot
will be deleted when the job is deleted. The default value is `false`.
`snapshot_id`::
(string) A numerical character string that uniquely identifies the model
snapshot. For example: "1491852978".

`snapshot_doc_count`::
(long) For internal use only.

`timestamp`::
(date) The creation timestamp for the snapshot.

## Examples

```console
GET _ml/anomaly_detectors/high_sum_total_sales/model_snapshots
{
  "start": "1575402236000"
}
```

In this example, the API provides a single result:
```js
{
  "count" : 1,
  "model_snapshots" : [
    {
      "job_id" : "high_sum_total_sales",
      "min_version" : "6.4.0",
      "timestamp" : 1575402237000,
      "description" : "State persisted due to job close at 2019-12-03T19:43:57+0000",
      "snapshot_id" : "1575402237",
      "snapshot_doc_count" : 1,
      "model_size_stats" : {
        "job_id" : "high_sum_total_sales",
        "result_type" : "model_size_stats",
        "model_bytes" : 1638816,
        "model_bytes_exceeded" : 0,
        "model_bytes_memory_limit" : 10485760,
        "total_by_field_count" : 3,
        "total_over_field_count" : 3320,
        "total_partition_field_count" : 2,
        "bucket_allocation_failures_count" : 0,
        "memory_status" : "ok",
        "categorized_doc_count" : 0,
        "total_category_count" : 0,
        "frequent_category_count" : 0,
        "rare_category_count" : 0,
        "dead_category_count" : 0,
        "categorization_status" : "ok",
        "log_time" : 1575402237000,
        "timestamp" : 1576965600000
      },
      "latest_record_time_stamp" : 1576971072000,
      "latest_result_time_stamp" : 1576965600000,
      "retain" : false
    }
  ]
}
```
