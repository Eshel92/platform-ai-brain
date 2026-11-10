<!-- Converted from ml/anomaly-detection/apis/put-datafeed.asciidoc (AsciiDoc). Includes are inlined. -->

# Create datafeeds API

**New API reference**
For the most up-to-date API details, refer to [Machine learning  anomaly detection APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-ml-anomaly).

Instantiates a datafeed.

## Request

`PUT _ml/datafeeds/<feed_id>`

## Prerequisites

* You must create an anomaly detection job before you create a datafeed.
* Requires the following privileges:
** cluster: `manage_ml` (the `machine_learning_admin` built-in role grants this 
  privilege)
** source index configured in the datafeed: `read`

## Description

{ml-docs}/ml-ad-run-jobs.html#ml-ad-datafeeds[Datafeeds] retrieve data from 
Elasticsearch for analysis by an anomaly detection job. You can associate only one datafeed to 
each anomaly detection job.

The datafeed contains a query that runs at a defined interval (`frequency`). If
you are concerned about delayed data, you can add a delay (`query_delay`) at
each interval. See {ml-docs}/ml-delayed-data-detection.html[Handling delayed data].

**Important:**
* You must use Kibana, this API, or the create anomaly detection jobs API
to create a datafeed. Do not add a datafeed directly to the `.ml-config` index
using the Elasticsearch index API. If Elasticsearch security features are enabled, do not give
users `write` privileges on the `.ml-config` index.
* When Elasticsearch security features are enabled, your datafeed remembers which roles
the user who created it had at the time of creation and runs the query using
those same roles. If you provide
secondary authorization headers, those
credentials are used instead.

## Path parameters

`<feed_id>`::
(Required, string)
A numerical character string that uniquely identifies the
datafeed. This identifier can contain lowercase alphanumeric characters (a-z
and 0-9), hyphens, and underscores. It must start and end with alphanumeric
characters.

## Query parameters

`allow_no_indices`::
(Optional, Boolean) If `true`, wildcard indices expressions that resolve into no
concrete indices are ignored. This includes the `_all` string or when no indices
are specified. Defaults to `true`.

`expand_wildcards`::
(Optional, string)
Type of index that wildcard patterns can match. If the request can target data
streams, this argument determines whether wildcard expressions match hidden data
streams. Supports comma-separated values, such as `open,hidden`. Valid values
are:

`all`::
Match any data stream or index, including hidden ones.

`open`::
Match open, non-hidden indices. Also matches any non-hidden data stream.

`closed`::
Match closed, non-hidden indices. Also matches any non-hidden data stream. Data
streams cannot be closed.

`hidden`::
Match hidden data streams and hidden indices. Must be combined with `open`,
`closed`, or both.

`none`::
Wildcard patterns are not accepted.
Defaults to `open`.

`ignore_throttled`::
(Optional, Boolean) If `true`, concrete, expanded or aliased indices are
ignored when frozen. Defaults to `true`.
deprecated:[7.16.0]
`ignore_unavailable`::
(Optional, Boolean) If `true`, unavailable indices (missing or closed) are
ignored. Defaults to `false`.

## Request body

`aggregations`::
(Optional, object)
If set, the datafeed performs aggregation searches. Support for aggregations is
limited and should be used only with low cardinality data. For more information,
see
{ml-docs}/ml-configuring-aggregation.html[Aggregating data for faster performance].
`chunking_config`::
(Optional, object)
Datafeeds might be required to search over long time periods, for several
months or years. This search is split into time chunks in order to ensure the
load on Elasticsearch is managed. Chunking configuration controls how the size of these
time chunks are calculated and is an advanced configuration option.
**Properties of `chunking_config`**
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

`delayed_data_check_config`::
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

`frequency`::
(Optional, time units)
The interval at which scheduled queries are made while the datafeed runs in real
time. The default value is either the bucket span for short bucket spans, or,
for longer bucket spans, a sensible fraction of the bucket span. For example:
`150s`. When `frequency` is shorter than the bucket span, interim results for
the last (partial) bucket are written then eventually overwritten by the full
bucket results. If the datafeed uses aggregations, this value must be divisible
by the interval of the date histogram aggregation.
`indices`::
(Required, array)
An array of index names. Wildcards are supported. For example:
`["it_ops_metrics", "server*"]`.
**Note:** If any indices are in remote clusters then the master nodes and the machine learning nodes need to have the
`remote_cluster_client` role.

`indices_options`::
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
`job_id`::
(Required, string)
Identifier for the anomaly detection job.
`max_empty_searches`::
(Optional,integer)
If a real-time datafeed has never seen any data (including during any initial
training period) then it will automatically stop itself and close its associated
job after this many real-time searches that return no documents. In other words,
it will stop after `frequency` times `max_empty_searches` of real-time
operation. If not set then a datafeed with no end time that sees no data will
remain started until it is explicitly stopped. By default this setting is not
set.
`query`::
(Optional, object)
The Elasticsearch query domain-specific language (DSL). This value corresponds to the
query object in an Elasticsearch search POST body. All the options that are supported by
Elasticsearch can be used, as this object is passed verbatim to Elasticsearch. By default, this
property has the following value: `{"match_all": {"boost": 1}}`.
`query_delay`::
(Optional, time units)
The number of seconds behind real time that data is queried. For example, if
data from 10:04 a.m. might not be searchable in Elasticsearch until 10:06 a.m., set this
property to 120 seconds. The default value is randomly selected between `60s`
and `120s`. This randomness improves the query performance when there are
multiple jobs running on the same node. For more information, see
{ml-docs}/ml-delayed-data-detection.html[Handling delayed data].
`runtime_mappings`::
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

`script_fields`::
(Optional, object)
Specifies scripts that evaluate custom expressions and returns script fields to
the datafeed. The detector configuration objects in a job can contain functions
that use these script fields. For more information, see
{ml-docs}/ml-configuring-transform.html[Transforming data with script fields]
and Script fields.
`scroll_size`::
(Optional, unsigned integer)
The `size` parameter that is used in Elasticsearch searches when the datafeed does not use
aggregations. The default value is `1000`. The maximum value is the value of
`index.max_result_window` which is 10,000 by default.

## Examples

Create a datafeed for an anomaly detection job (`test-job`):

```console
PUT _ml/datafeeds/datafeed-test-job?pretty
{
  "indices": [
    "kibana_sample_data_logs"
  ],
  "query": {
    "bool": {
      "must": [
        {
          "match_all": {}
        }
      ]
    }
  },
  "job_id": "test-job"
}
```

When the datafeed is created, you receive the following results:

```console-result
{
  "datafeed_id" : "datafeed-test-job",
  "job_id" : "test-job",
  "authorization" : {
    "roles" : [
      "superuser"
    ]
  },
  "query_delay" : "91820ms",
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
      "must" : [
        {
          "match_all" : { }
        }
      ]
    }
  },
  "indices" : [
    "kibana_sample_data_logs"
  ],
  "scroll_size" : 1000,
  "delayed_data_check_config" : {
    "enabled" : true
  }
}
```
