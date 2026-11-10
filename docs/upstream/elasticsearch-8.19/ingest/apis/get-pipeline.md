<!-- Converted from ingest/apis/get-pipeline.asciidoc (AsciiDoc). Includes are inlined. -->

### Get pipeline API

**New API reference**
For the most up-to-date API details, refer to [Ingest APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-ingest).

Returns information about one or more ingest pipelines.
This API returns a local reference of the pipeline.

```console
GET /_ingest/pipeline/my-pipeline-id
```

#### Request

`GET /_ingest/pipeline/<pipeline>`

`GET /_ingest/pipeline`

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the
`read_pipeline`, `manage_pipeline`, `manage_ingest_pipelines`, or `manage`
cluster privilege to use this API.

#### Path parameters

`<pipeline>`::
(Optional, string)
Comma-separated list of pipeline IDs to retrieve. Wildcard (`*`) expressions are
supported.
To get all ingest pipelines, omit this parameter or use `*`.

#### Query parameters

`master_timeout`::
(Optional, time units)
Period to wait for the master node. If the master node is not available before
the timeout expires, the request fails and returns an error. Defaults to `30s`.
Can also be set to `-1` to indicate that the request should never timeout.

#### Examples

##### Get information for a specific ingest pipeline

```console
GET /_ingest/pipeline/my-pipeline-id
```

The API returns the following response:

```console-result
{
  "my-pipeline-id" : {
    "description" : "describe pipeline",
    "version" : 123,
    "processors" : [
      {
        "set" : {
          "field" : "foo",
          "value" : "bar"
        }
      }
    ]
  }
}
```
