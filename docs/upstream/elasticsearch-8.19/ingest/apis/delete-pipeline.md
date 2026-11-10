<!-- Converted from ingest/apis/delete-pipeline.asciidoc (AsciiDoc). Includes are inlined. -->

### Delete pipeline API

**New API reference**
For the most up-to-date API details, refer to [Ingest APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-ingest).

Deletes one or more existing ingest pipeline.

```console
DELETE /_ingest/pipeline/my-pipeline-id
```

#### Request

`DELETE /_ingest/pipeline/<pipeline>`

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the
`manage_pipeline`, `manage_ingest_pipelines`, or `manage`
cluster privilege to use this API.

#### Path parameters

`<pipeline>`::
(Required, string) Pipeline ID or wildcard expression of pipeline IDs
used to limit the request.

To delete all ingest pipelines in a cluster,
use a value of `*`.

#### Query parameters

`master_timeout`::
(Optional, time units)
Period to wait for the master node. If the master node is not available before
the timeout expires, the request fails and returns an error. Defaults to `30s`.
Can also be set to `-1` to indicate that the request should never timeout.

`timeout`::
(Optional, time units) Period to wait for a response from all relevant nodes in the cluster after updating the cluster metadata.
If no response is received before the timeout expires, the cluster metadata update still applies but the response will indicate that it was not completely acknowledged.
Defaults to `30s`.
Can also be set to `-1` to indicate that the request should never timeout.

#### Examples

##### Delete a specific ingest pipeline

```console
DELETE /_ingest/pipeline/pipeline-one
```

##### Delete ingest pipelines using a wildcard expression

```console
DELETE /_ingest/pipeline/pipeline-*
```

##### Delete all ingest pipelines

```console
DELETE /_ingest/pipeline/*
```
