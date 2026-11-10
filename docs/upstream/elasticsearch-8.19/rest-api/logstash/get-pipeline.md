<!-- Converted from rest-api/logstash/get-pipeline.asciidoc (AsciiDoc). Includes are inlined. -->

### Get pipeline API

**New API reference**
For the most up-to-date API details, refer to [Logstash APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-logstash).

This API retrieves pipelines used for
{logstash-ref}/logstash-centralized-pipeline-management.html[Logstash Central
Management].

#### Request

`GET _logstash/pipeline`

`GET _logstash/pipeline/<pipeline_id>`

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the
`manage_logstash_pipelines` cluster privilege to use this API.

#### Description

Retrieve one or more Logstash pipelines.

#### Path parameters

`<pipeline_id>`::
  (Optional, string) Comma-separated list of pipeline identifiers.

#### Examples

The following example retrieves the pipeline named `my_pipeline`:

```console
PUT _logstash/pipeline/my_pipeline
{
  "description": "Sample pipeline for illustration purposes",
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
GET _logstash/pipeline/my_pipeline
```

If the request succeeds, the body of the response contains the pipeline definition:

```console-result
{
  "my_pipeline": {
    "description": "Sample pipeline for illustration purposes",
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
}
```
