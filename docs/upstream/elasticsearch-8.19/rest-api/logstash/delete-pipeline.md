<!-- Converted from rest-api/logstash/delete-pipeline.asciidoc (AsciiDoc). Includes are inlined. -->

### Delete Logstash pipeline API

**New API reference**
For the most up-to-date API details, refer to [Logstash APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-logstash).

This API deletes a pipeline used for
{logstash-ref}/logstash-centralized-pipeline-management.html[Logstash Central
Management].

#### Request

`DELETE _logstash/pipeline/<pipeline_id>`

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the
`manage_logstash_pipelines` cluster privilege to use this API.

#### Description

Deletes a Logstash pipeline.

#### Path parameters

`<pipeline_id>`::
  (Required, string) Identifier for the Pipeline.

#### Examples

The following example deletes the Pipeline named `my_pipeline`:

```console
PUT _logstash/pipeline/my_pipeline
{
  "description": "Sample Pipeline for illustration purposes",
  "last_modified": "2021-01-02T02:50:51.250Z",
  "pipeline_metadata": {
    "type": "logstash_pipeline",
    "version": "1"
  },
  "username": "elastic",
  "pipeline": "input {}\n filter { grok {} }\n output {}",
  "pipeline_settings": {
    "pipeline.workers": 1,
    "pipeline.batch.size": 125,
    "pipeline.batch.delay": 50,
    "queue.type": "memory",
    "queue.max_bytes": "1gb",
    "queue.checkpoint.writes": 1024
  }
}
```

```console
DELETE _logstash/pipeline/my_pipeline
```

If the request succeeds, you receive an empty response with an appropriate
status code.
