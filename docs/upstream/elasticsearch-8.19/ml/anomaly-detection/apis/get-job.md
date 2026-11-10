<!-- Converted from ml/anomaly-detection/apis/get-job.asciidoc (AsciiDoc). Includes are inlined. -->

# Get anomaly detection jobs API

**New API reference**
For the most up-to-date API details, refer to [Machine learning  anomaly detection APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-ml-anomaly).

Retrieves configuration information for anomaly detection jobs.

## Request

`GET _ml/anomaly_detectors/<job_id>` +

`GET _ml/anomaly_detectors/<job_id>,<job_id>` +

`GET _ml/anomaly_detectors/` +

`GET _ml/anomaly_detectors/_all`

## Prerequisites

Requires the `monitor_ml` cluster privilege. This privilege is included in the
`machine_learning_user` built-in role.

## Description

**Important:** This API returns a maximum of 10,000 jobs.

## Path parameters

`<job_id>`::
(Optional, string)
Identifier for the anomaly detection job. It can be a job identifier, a group
name, or a wildcard expression. You can get information for multiple
anomaly detection jobs in a single API request by using a group name, a comma-separated
list of jobs, or a wildcard expression. You can get information for all
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
`exclude_generated`::
(Optional, Boolean)
Indicates if certain fields should be removed from the configuration on
retrieval. This allows the configuration to be in an acceptable format to be retrieved
and then added to another cluster. Default is false.

## Response body

The API returns an array of anomaly detection job resources. For the full list of
properties, see create anomaly detection jobs API.

`blocked`::
(object) When present, it explains that a task is executed on the job
that blocks it from opening.
**Properties of `blocked`**
`reason`:::
(string) The reason the job is blocked. Values may be `delete`, `reset`, `revert`.
Each value means the corresponding action is being executed.

`task_id`:::
(string) The task id of the blocking action. You can use the tasks API to
monitor progress.

`create_time`::
(string) The time the job was created. For example, `1491007356077`. This
property is informational; you cannot change its value.

`datafeed_config`::
(object) The datafeed configured for the current anomaly detection job.
**Properties of `datafeed_config`**
`authorization`:::
(Optional, object)
The security privileges that the datafeed uses to run its queries. If
{stack-security-features} were disabled at the time of the most recent update to
the datafeed, this property is omitted.
**Properties of `authorization`**
=====
`api_key`:::
(object) If an API key was used for the most recent update to the datafeed, its
name and identifier are listed in the response.
**Properties of `api_key`**
======
`id`::::
(string) The identifier for the API key.

`name`::::
(string) The name of the API key.
======

`roles`:::
(array of strings) If a user ID was used for the most recent update to the
datafeed, its roles at the time of the update are listed in the response.

`service_account`:::
(string) If a service account was used for the most recent update to the datafeed,
the account name is listed in the response.
=====

`datafeed_id`:::
(Optional, string)
A numerical character string that uniquely identifies the
datafeed. This identifier can contain lowercase alphanumeric characters (a-z
and 0-9), hyphens, and underscores. It must start and end with alphanumeric
characters.
`aggregations`:::
(Optional, object)
If set, the datafeed performs aggregation searches. Support for aggregations is
limited and should be used only with low cardinality data. For more information,
see
{ml-docs}/ml-configuring-aggregation.html[Aggregating data for faster performance].
`chunking_config`:::
(Optional, object)
Datafeeds might be required to search over long time periods, for several
months or years. This search is split into time chunks in order to ensure the
load on Elasticsearch is managed. Chunking configuration controls how the size of these
time chunks are calculated and is an advanced configuration option.
**Properties of `chunking_config`**
=====
`mode`:::
(string)
There are three available modes:
* `auto`: The chunk size is dynamically calculated. This is the default and
recommended value when the datafeed does not use aggregations.
* `manual`: Chunking is applied according to the specified `time_span`. Use this
mode when the datafeed uses aggregations.
* `off`: No chunking is applied.
`time_span`:::
(time units)
The time span that each search will be querying. This setting is only applicable
when the mode is set to `manual`. For example: `3h`.
=====

`delayed_data_check_config`:::
(Optional, object)
Specifies whether the datafeed checks for missing data and the size of the
window. For example: `{"enabled": true, "check_window": "1h"}`.
The datafeed can optionally search over indices that have already been read in
an effort to determine whether any data has subsequently been added to the
index. If missing data is found, it is a good indication that the `query_delay`
option is set too low and the data is being indexed after the datafeed has passed
that moment in time. See
{ml-docs}/ml-delayed-data-detection.html[Working with delayed data].
This check runs only on real-time datafeeds.
**Properties of `delayed_data_check_config`**
=====
`check_window`::
(time units)
The window of time that is searched for late data. This window of time ends with
the latest finalized bucket. It defaults to `null`, which causes an appropriate
`check_window` to be calculated when the real-time datafeed runs. In particular,
the default `check_window` span calculation is based on the maximum of `2h` or
`8 * bucket_span`.
`enabled`::
(Boolean)
Specifies whether the datafeed periodically checks for delayed data. Defaults to
`true`.
=====

`frequency`:::
(Optional, time units)
The interval at which scheduled queries are made while the datafeed runs in real
time. The default value is either the bucket span for short bucket spans, or,
for longer bucket spans, a sensible fraction of the bucket span. For example:
`150s`. When `frequency` is shorter than the bucket span, interim results for
the last (partial) bucket are written then eventually overwritten by the full
bucket results. If the datafeed uses aggregations, this value must be divisible
by the interval of the date histogram aggregation.
`indices`:::
(Required, array)
An array of index names. Wildcards are supported. For example:
`["it_ops_metrics", "server*"]`.
**Note:** If any indices are in remote clusters then the master nodes and the machine learning nodes need to have the
`remote_cluster_client` role.

`indices_options`:::
(Optional, object)
Specifies index expansion options that are used during search.
For example:
```
{
   "expand_wildcards": ["all"],
   "ignore_unavailable": true,
   "allow_no_indices": "false",
   "ignore_throttled": true
}
```
For more information about these options, see api-multi-index.
`job_id`:::
(Required, string)
Identifier for the anomaly detection job.
`max_empty_searches`:::
(Optional,integer)
If a real-time datafeed has never seen any data (including during any initial
training period) then it will automatically stop itself and close its associated
job after this many real-time searches that return no documents. In other words,
it will stop after `frequency` times `max_empty_searches` of real-time
operation. If not set then a datafeed with no end time that sees no data will
remain started until it is explicitly stopped. By default this setting is not
set.
`query`:::
(Optional, object)
The Elasticsearch query domain-specific language (DSL). This value corresponds to the
query object in an Elasticsearch search POST body. All the options that are supported by
Elasticsearch can be used, as this object is passed verbatim to Elasticsearch. By default, this
property has the following value: `{"match_all": {"boost": 1}}`.
`query_delay`:::
(Optional, time units)
The number of seconds behind real time that data is queried. For example, if
data from 10:04 a.m. might not be searchable in Elasticsearch until 10:06 a.m., set this
property to 120 seconds. The default value is randomly selected between `60s`
and `120s`. This randomness improves the query performance when there are
multiple jobs running on the same node. For more information, see
{ml-docs}/ml-delayed-data-detection.html[Handling delayed data].
`runtime_mappings`:::
(Optional, object)
Specifies runtime fields for the datafeed search.
For example:
```
{
  "day_of_week": {
    "type": "keyword",
    "script": {
      "source": "emit(doc['@timestamp'].value.dayOfWeekEnum.getDisplayName(TextStyle.FULL, Locale.ENGLISH))"
    }
  }
}
```

`script_fields`:::
(Optional, object)
Specifies scripts that evaluate custom expressions and returns script fields to
the datafeed. The detector configuration objects in a job can contain functions
that use these script fields. For more information, see
{ml-docs}/ml-configuring-transform.html[Transforming data with script fields]
and Script fields.
`scroll_size`:::
(Optional, unsigned integer)
The `size` parameter that is used in Elasticsearch searches when the datafeed does not use
aggregations. The default value is `1000`. The maximum value is the value of
`index.max_result_window` which is 10,000 by default.

`finished_time`::
(string) If the job closed or failed, this is the time the job finished,
otherwise it is `null`. This property is informational; you cannot change its
value.

`job_type`::
(string) Reserved for future use, currently set to `anomaly_detector`.

`job_version`::
(string) The machine learning configuration version number at which the job was created.

**Note:** From Elasticsearch 8.10.0,  a new version number is used to
track the configuration and state changes in the machine learning plugin. This new
version number is decoupled from the product version and will increment
independently. The `job_version` value represents the new version number.

`model_snapshot_id`::
(string)
A numerical character string that uniquely identifies the model snapshot. For
example, `1575402236000`.

## Response codes

`404` (Missing resources)::
  If `allow_no_match` is `false`, this code indicates that there are no
  resources that match the request or only partial matches for the request.

## Examples

```console
GET _ml/anomaly_detectors/high_sum_total_sales
```

The API returns the following results:

```js
{
  "count": 1,
  "jobs": [
    {
      "job_id" : "high_sum_total_sales",
      "job_type" : "anomaly_detector",
      "job_version" : "8.4.0",
      "create_time" : 1655852735889,
      "finished_time" : 1655852745980,
      "model_snapshot_id" : "1575402237",
      "custom_settings" : {
        "created_by" : "ml-module-sample",
        ...
      },
      "datafeed_config" : {
        "datafeed_id" : "datafeed-high_sum_total_sales",
        "job_id" : "high_sum_total_sales",
        "authorization" : {
          "roles" : [
            "superuser"
          ]
        },
        "query_delay" : "93169ms",
        "chunking_config" : {
          "mode" : "auto"
        },
        "indices_options" : {
          "expand_wildcards" : [
            "open"
          ],
          "ignore_unavailable" : false,
          "allow_no_indices" : true,
          "ignore_throttled" : true
        },
        "query" : {
          "bool" : {
            "filter" : [
              {
                "term" : {
                  "event.dataset" : "sample_ecommerce"
                }
              }
            ]
          }
        },
        "indices" : [
          "kibana_sample_data_ecommerce"
        ],
        "scroll_size" : 1000,
        "delayed_data_check_config" : {
          "enabled" : true
        }
      },
      "groups" : [
        "kibana_sample_data",
        "kibana_sample_ecommerce"
      ],
      "description" : "Find customers spending an unusually high amount in an hour",
      "analysis_config" : {
        "bucket_span" : "1h",
        "detectors" : [
          {
            "detector_description" : "High total sales",
            "function" : "high_sum",
            "field_name" : "taxful_total_price",
            "over_field_name" : "customer_full_name.keyword",
            "detector_index" : 0
          }
        ],
        "influencers" : [
          "customer_full_name.keyword",
          "category.keyword"
        ],
        "model_prune_window": "30d"
      },
      "analysis_limits" : {
        "model_memory_limit" : "13mb",
        "categorization_examples_limit" : 4
      },
      "data_description" : {
        "time_field" : "order_date",
        "time_format" : "epoch_ms"
      },
      "model_plot_config" : {
        "enabled" : true,
        "annotations_enabled" : true
      },
      "model_snapshot_retention_days" : 10,
      "daily_model_snapshot_retention_after_days" : 1,
      "results_index_name" : "shared",
      "allow_lazy_open" : false
    }
  ]
}
```
