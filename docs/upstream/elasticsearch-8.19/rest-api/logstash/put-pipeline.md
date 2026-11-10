<!-- Converted from rest-api/logstash/put-pipeline.asciidoc (AsciiDoc). Includes are inlined. -->

### Create or update Logstash pipeline API

**New API reference**
For the most up-to-date API details, refer to [Logstash APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-logstash).

This API creates or updates a Logstash pipeline used for
{logstash-ref}/logstash-centralized-pipeline-management.html[Logstash Central
Management].

#### Request

`PUT _logstash/pipeline/<pipeline_id>`

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the
`manage_logstash_pipelines` cluster privilege to use this API.

#### Description

Creates a Logstash pipeline. If the specified pipeline exists, the pipeline is
replaced.

#### Path parameters

`<pipeline_id>`::
(Required, string)
Identifier for the pipeline.
It must begin with a letter or underscore and can contain only letters, underscores, dashes, hyphens, and numbers.

#### Request body

`description`::
(Optional, string)
Description of the pipeline. This description is not used by Elasticsearch or Logstash.

`last_modified`::
(Required, string)
Date the pipeline was last updated. Must be in the `yyyy-MM-dd'T'HH:mm:ss.SSSZZ`
`strict_date_time` format.

`pipeline`::
(Required, string)
Configuration for the pipeline. For supported syntax, see the
{logstash-ref}/configuration-file-structure.html[Logstash configuration
documentation].

`pipeline_metadata`::
(Required, object)
Optional metadata about the pipeline. May have any contents. This metadata is
not generated or used by Elasticsearch or Logstash.

`pipeline_settings`::
(Required, object)
Settings for the pipeline. Supports only flat keys in dot notation. For
supported settings, see the {logstash-ref}/logstash-settings-file.html[Logstash
settings documentation].

`username`::
(Required, string)
User who last updated the pipeline.

#### Examples

The following example creates a new pipeline named `my_pipeline`:

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

If the request succeeds, you receive an empty response with an appropriate
status code.
