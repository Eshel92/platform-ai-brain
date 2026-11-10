<!-- Converted from indices/downsample-data-stream.asciidoc (AsciiDoc). Includes are inlined. -->

### Downsample index API

**New API reference**
For the most up-to-date API details, refer to [Data stream APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-data-stream).

Aggregates a time series (TSDS) index and stores
pre-computed statistical summaries (`min`, `max`, `sum`, `value_count` and
`avg`) for each metric field grouped by a configured time interval. For example,
a TSDS index that contains metrics sampled every 10 seconds can be downsampled
to an hourly index. All documents within an hour interval are summarized and
stored as a single document in the downsample index.

```console
POST /my-time-series-index/_downsample/my-downsampled-time-series-index
{
    "fixed_interval": "1d"
}
```

Check the Downsampling documentation for an overview, details about the downsampling process, and examples of running downsampling manually and as part of an ILM policy.

#### Request

`POST /<source-index>/_downsample/<output-downsampled-index>`

#### Prerequisites

* Only indices in a time series data stream are supported.

* If the Elasticsearch security features are enabled, you must have the `all`
or `manage` index privilege for the data stream.

* Neither field nor document level security can be defined on the source index.

* The source index must be read only (`index.blocks.write: true`).

#### Path parameters

`<source-index>`::
(Optional, string) Name of the time series index to downsample.

`<output-downsampled_index>`::
(Required, string) Name of the index to create. 

Index names must meet the following criteria:

- Lowercase only
- Cannot include `\`, `/`, `*`, `?`, `"`, `<`, `>`, `|`, ` ` (space character), `,`, `#`
- Indices prior to 7.0 could contain a colon (`:`), but that's been deprecated and won't be supported in 7.0+
- Cannot start with `-`, `_`, `+`
- Cannot be `.` or `..`
- Cannot be longer than 255 bytes (note it is bytes, so multi-byte characters will count towards the 255 limit faster)
- Names starting with `.` are deprecated, except for hidden indices and internal indices managed by plugins

#### Query parameters

`fixed_interval`:: (Required, time units) The interval at which
to aggregate the original time series index. For example, `60m` produces a
document for each 60 minute (hourly) interval. This follows standard time
formatting syntax as used elsewhere in Elasticsearch.
**Note:** Smaller, more granular intervals take up proportionally more space.
