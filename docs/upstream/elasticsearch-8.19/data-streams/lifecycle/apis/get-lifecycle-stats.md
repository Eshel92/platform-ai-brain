<!-- Converted from data-streams/lifecycle/apis/get-lifecycle-stats.asciidoc (AsciiDoc). Includes are inlined. -->

### Get data stream lifecycle stats

**New API reference**
For the most up-to-date API details, refer to [Data stream APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-data-stream).

Gets stats about the execution of data stream lifecycle.

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the `monitor` or
`manage` cluster privilege to use this API.

#### Request

`GET _lifecycle/stats`

#### Description

Gets stats about the execution of the data stream lifecycle. The data stream level stats include only stats about data streams
managed by the data stream lifecycle.

#### Response body

`last_run_duration_in_millis`::
(Optional, long)
The duration of the last data stream lifecycle execution.
`time_between_starts_in_millis`::
(Optional, long)
The time passed between the start of the last two data stream lifecycle executions. This should amount approximately to
`data_streams.lifecycle.poll_interval`.
`data_stream_count`::
(integer)
The count of data streams currently being managed by the data stream lifecycle.
`data_streams`::
(array of objects)
Contains information about the retrieved data stream lifecycles.
**Properties of objects in `data_streams`**
`name`::
(string)
The name of the data stream.
`backing_indices_in_total`::
(integer)
The count of the backing indices of this data stream that are managed by the data stream lifecycle.
`backing_indices_in_error`::
(integer)
The count of the backing indices of this data stream that are managed by the data stream lifecycle and have encountered an error.

#### Examples

Let's retrieve the data stream lifecycle stats of a cluster that has already executed the lifecycle more than once:

```console
GET _lifecycle/stats?human&pretty
```

The response will look like the following:

```console-result
{
  "last_run_duration_in_millis": 2,
  "last_run_duration": "2ms",
  "time_between_starts_in_millis": 9998,
  "time_between_starts": "9.99s",
  "data_streams_count": 2,
  "data_streams": [
    {
      "name": "my-data-stream",
      "backing_indices_in_total": 2,
      "backing_indices_in_error": 0
    },
    {
      "name": "my-other-stream",
      "backing_indices_in_total": 2,
      "backing_indices_in_error": 1
    }
  ]
}
```
