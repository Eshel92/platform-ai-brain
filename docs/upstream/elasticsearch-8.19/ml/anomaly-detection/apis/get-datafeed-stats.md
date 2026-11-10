<!-- Converted from ml/anomaly-detection/apis/get-datafeed-stats.asciidoc (AsciiDoc). Includes are inlined. -->

# Get datafeed statistics API

**New API reference**
For the most up-to-date API details, refer to [Machine learning  anomaly detection APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-ml-anomaly).

Retrieves usage information for datafeeds.

## Request

`GET _ml/datafeeds/<feed_id>/_stats` +

`GET _ml/datafeeds/<feed_id>,<feed_id>/_stats` +

`GET _ml/datafeeds/_stats`  +

`GET _ml/datafeeds/_all/_stats`

## Prerequisites

Requires the `monitor_ml` cluster privilege. This privilege is included in the
`machine_learning_user` built-in role.

## Description

If the datafeed is stopped, the only information you receive is the
`datafeed_id` and the `state`.

**Important:** This API returns a maximum of 10,000 datafeeds.

## Path parameters

`<feed_id>`::
(Optional, string)
Identifier for the datafeed. It can be a datafeed identifier or a wildcard
expression.
You can get statistics for multiple datafeeds in a single API request by using a
comma-separated list of datafeeds or a wildcard expression. You can get
statistics for all datafeeds by using `_all`, by specifying `*` as the datafeed
identifier, or by omitting the identifier.

## Query parameters

`allow_no_match`::
(Optional, Boolean)
Specifies what to do when the request:
* Contains wildcard expressions and there are no datafeeds that match.
* Contains the `_all` string or no identifiers and there are no matches.
* Contains wildcard expressions and there are only partial matches.

The default value is `true`, which returns an empty `datafeeds` array when
there are no matches and the subset of results when there are partial matches.
If this parameter is `false`, the request returns a `404` status code when there
are no matches or only partial matches.

## Response body

The API returns an array of datafeed count objects. All of these properties are
informational; you cannot update their values.

`assignment_explanation`::
(string)
For started datafeeds only, contains messages relating to the selection of a
node.
`datafeed_id`::
(string)
A numerical character string that uniquely identifies the
datafeed. This identifier can contain lowercase alphanumeric characters (a-z
and 0-9), hyphens, and underscores. It must start and end with alphanumeric
characters.
`node`::
(object)
For started datafeeds only, this information pertains to the node upon which the
datafeed is started.
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
(string)
The node name. For example, `0-o0tOo`.

`transport_address`:::
(string)
The host and port where transport HTTP connections are accepted.

`running_state`::
(object) An object containing the running state for this datafeed. It is only
provided if the datafeed is started.
`real_time_configured`:::
(boolean) Indicates if the datafeed is "real-time"; meaning that the datafeed
has no configured `end` time.

`real_time_running`:::
(boolean) Indicates whether the datafeed has finished running on the available
past data. For datafeeds without a configured `end` time, this means that
the datafeed is now running on "real-time" data.

`search_interval`:::
(Optional, object) Provides the latest time interval the datafeed has searched.
=====
`start_ms`::::
The start time as an epoch in milliseconds.

`end_ms`::::
 The end time as an epoch in milliseconds.
=====

`state`::
(string)
The status of the datafeed, which can be one of the following values:
* `starting`: The datafeed has been requested to start but has not yet started.
* `started`: The datafeed is actively receiving data.
* `stopping`: The datafeed has been requested to stop gracefully and is
completing its final action.
* `stopped`: The datafeed is stopped and will not receive data until it is
re-started.
`timing_stats`::
(object) An object that provides statistical information about timing aspect of
this datafeed.
`average_search_time_per_bucket_ms`:::
(double)
The average search time per bucket, in milliseconds.
`bucket_count`:::
(long)
The number of buckets processed.
`exponential_average_search_time_per_hour_ms`:::
(double)
The exponential average search time per hour, in milliseconds.
`job_id`:::
Identifier for the anomaly detection job.
`search_count`:::
The number of searches run by the datafeed.
`total_search_time_ms`:::
The total time the datafeed spent searching, in milliseconds.

## Response codes

`404` (Missing resources)::
  If `allow_no_match` is `false`, this code indicates that there are no
  resources that match the request or only partial matches for the request.

## Examples

```console
GET _ml/datafeeds/datafeed-high_sum_total_sales/_stats
```

The API returns the following results:

```console-result
{
  "count" : 1,
  "datafeeds" : [
    {
      "datafeed_id" : "datafeed-high_sum_total_sales",
      "state" : "started",
      "node" : {
        "id" : "7bmMXyWCRs-TuPfGJJ_yMw",
        "name" : "node-0",
        "ephemeral_id" : "hoXMLZB0RWKfR9UPPUCxXX",
        "transport_address" : "127.0.0.1:9300",
        "attributes" : {
          "ml.machine_memory" : "17179869184",
          "ml.max_open_jobs" : "512"
        }
      },
      "assignment_explanation" : "",
      "timing_stats" : {
        "job_id" : "high_sum_total_sales",
        "search_count" : 7,
        "bucket_count" : 743,
        "total_search_time_ms" : 134.0,
        "average_search_time_per_bucket_ms" : 0.180349932705249,
        "exponential_average_search_time_per_hour_ms" : 11.514712961628677
      }
    }
  ]
}
```
