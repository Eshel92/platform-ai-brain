<!-- Converted from data-streams/lifecycle/apis/put-lifecycle.asciidoc (AsciiDoc). Includes are inlined. -->

### Set the lifecycle of a data stream

**New API reference**
For the most up-to-date API details, refer to [Data stream APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-data-stream).

Configures the data stream lifecycle for the targeted data streams.

#### Prerequisites

If the Elasticsearch security features are enabled, you must have the `manage_data_stream_lifecycle` index privilege or higher to use this API.
For more information, see security-privileges.

#### Request

`PUT _data_stream/<data-stream>/_lifecycle`

#### Description

Configures the data stream lifecycle for the targeted data streams. If multiple data streams are provided but at least one of them
does not exist, then the update of the lifecycle will fail for all of them and the API will respond with `404`.

#### Path parameters

`<data-stream>`::
(Required, string) Comma-separated list of data streams used to limit the request. Supports wildcards (`*`).
To target all data streams use `*` or `_all`.

#### Query parameters

`expand_wildcards`::
(Optional, string)
Type of data stream that wildcard patterns can match. Supports
comma-separated values, such as `open,hidden`. Valid values are:

`all`, `hidden`::
Match any data stream, including hidden ones.

`open`, `closed`::
Matches any non-hidden data stream. Data streams cannot be closed.

`none`::
Wildcard patterns are not accepted.
Defaults to `open`.

#### Request body

`lifecycle`::
(Required, object)
**Properties of `lifecycle`**
`data_retention`::
(Optional, string)
If defined, every document added to this data stream will be stored at least for this time frame. Any time after this
duration the document could be deleted. When empty, every document in this data stream will be stored indefinitely.

`enabled`::
(Optional, boolean)
If defined, it turns data stream lifecycle on/off (`true`/`false`) for this data stream.
A data stream lifecycle that's disabled (`enabled: false`) will have no effect on the
data stream. Defaults to `true`.

`downsampling`::
(Optional, array)
An optional array of downsampling configuration objects, each defining an `after`
interval representing when the backing index is meant to be downsampled (the time 
frame is calculated since the index was rolled over, i.e. generation time) and
a `fixed_interval` representing the downsampling interval (the minimum `fixed_interval`
value is `5m`). A maximum number of 10 downsampling rounds can be configured.
See configuration example below.

#### Examples

The following example sets the lifecycle of `my-data-stream`:

```console
PUT _data_stream/my-data-stream/_lifecycle
{
  "data_retention": "7d"
}
```

When the lifecycle is successfully updated in all data streams, you receive the following result:

```console-result
{
  "acknowledged": true
}
```

#### Examples

The following example configures two downsampling rounds, the first one starting
one day after the backing index is rolled over (or later, if the index is still 
within its write-accepting time bounds) with an interval
of `10m`, and a second round starting 7 days after rollover at an interval of `1d`:

```console
PUT _data_stream/my-weather-sensor-data-stream/_lifecycle
{
    "downsampling": [
      {
        "after": "1d",
        "fixed_interval": "10m"
      },
      {
        "after": "7d",
        "fixed_interval": "1d"
      }
    ]
}
```
