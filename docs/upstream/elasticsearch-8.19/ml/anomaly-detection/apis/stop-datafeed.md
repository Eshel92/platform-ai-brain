<!-- Converted from ml/anomaly-detection/apis/stop-datafeed.asciidoc (AsciiDoc). Includes are inlined. -->

# Stop datafeeds API

**New API reference**
For the most up-to-date API details, refer to [Machine learning  anomaly detection APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-ml-anomaly).

Stops one or more datafeeds.

## Request

`POST _ml/datafeeds/<feed_id>/_stop` +

`POST _ml/datafeeds/<feed_id>,<feed_id>/_stop` +

`POST _ml/datafeeds/_all/_stop`

## Prerequisites

Requires the `manage_ml` cluster privilege. This privilege is included in the 
`machine_learning_admin` built-in role.

## Description

A datafeed that is stopped ceases to retrieve data from Elasticsearch.
A datafeed can be started and stopped multiple times throughout its lifecycle.

## Path parameters

`<feed_id>`::
(Required, string)
Identifier for the datafeed. You can stop multiple datafeeds in a single API
request by using a comma-separated list of datafeeds or a wildcard expression.
You can close all datafeeds by using `_all` or by specifying `*` as the
identifier.

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
`force`::
  (Optional, Boolean) If true, the datafeed is stopped forcefully.

`timeout`::
  (Optional, time) Specifies the amount of time to wait until a datafeed stops.
  The default value is 20 seconds.

## Request body

You can also specify the query parameters (such as `allow_no_match` and
`force`) in the request body.

## Response codes

`404` (Missing resources)::
  If `allow_no_match` is `false`, this code indicates that there are no
  resources that match the request or only partial matches for the request.

## Examples

```console
POST _ml/datafeeds/datafeed-low_request_rate/_stop
{
  "timeout": "30s"
}
```

When the datafeed stops, you receive the following results:

```console-result
{
  "stopped": true
}
```
