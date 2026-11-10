<!-- Converted from cat/datafeeds.asciidoc (AsciiDoc). Includes are inlined. -->

### cat datafeeds API

**New API reference**
For the most up-to-date API details, refer to [Compact and aligned text (CAT) APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-cat)..

**Important:**
cat APIs are only intended for human consumption using the command line or Kibana 
console. They are _not_ intended for use by applications. For application 
consumption, use the get datafeed statistics API.

Returns configuration and usage information about datafeeds.

#### Request

`GET /_cat/ml/datafeeds/<feed_id>` +

`GET /_cat/ml/datafeeds`

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have `monitor_ml`,
`monitor`, `manage_ml`, or `manage` cluster privileges to use this API. See
security-privileges and {ml-docs-setup-privileges}.

#### Description

Datafeeds retrieve data from Elasticsearch for analysis by anomaly detection jobs. For more 
information, see {ml-docs}/ml-dfeeds.html[Datafeeds].

**Note:** This API returns a maximum of 10,000 jobs.

#### Path parameters

`<feed_id>`::
(Optional, string)
A numerical character string that uniquely identifies the
datafeed. This identifier can contain lowercase alphanumeric characters (a-z
and 0-9), hyphens, and underscores. It must start and end with alphanumeric
characters.

#### Query parameters

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
For started datafeeds only, contains messages relating to the selection of a
node.
`buckets.count`, `bc`, `bucketsCount`:::
(Default)
The number of buckets processed.
`id`:::
(Default)
A numerical character string that uniquely identifies the
datafeed. This identifier can contain lowercase alphanumeric characters (a-z
and 0-9), hyphens, and underscores. It must start and end with alphanumeric
characters.
`node.address`, `na`, `nodeAddress`:::
The network address of the node.
For started datafeeds only, this information pertains to the node upon which the
datafeed is started.
`node.ephemeral_id`, `ne`, `nodeEphemeralId`:::
The ephemeral ID of the node.
For started datafeeds only, this information pertains to the node upon which the
datafeed is started.
`node.id`, `ni`, `nodeId`:::
The unique identifier of the node.
For started datafeeds only, this information pertains to the node upon which the
datafeed is started.
`node.name`, `nn`, `nodeName`:::
The node name.
For started datafeeds only, this information pertains to the node upon which the
datafeed is started.
`search.bucket_avg`, `sba`, `searchBucketAvg`:::
The average search time per bucket, in milliseconds.
`search.count`, `sc`, `searchCount`:::
(Default)
The number of searches run by the datafeed.
`search.exp_avg_hour`, `seah`, `searchExpAvgHour`:::
The exponential average search time per hour, in milliseconds.
`search.time`, `st`, `searchTime`:::
The total time the datafeed spent searching, in milliseconds.
`state`, `s`:::
(Default)
The status of the datafeed, which can be one of the following values:
* `starting`: The datafeed has been requested to start but has not yet started.
* `started`: The datafeed is actively receiving data.
* `stopping`: The datafeed has been requested to stop gracefully and is
completing its final action.
* `stopped`: The datafeed is stopped and will not receive data until it is
re-started.
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
GET _cat/ml/datafeeds?v=true
```

```console-result
id                              state buckets.count search.count
datafeed-high_sum_total_sales stopped 743          7
datafeed-low_request_rate     stopped 1457         3
datafeed-response_code_rates  stopped 1460         18
datafeed-url_scanning         stopped 1460         18
```
