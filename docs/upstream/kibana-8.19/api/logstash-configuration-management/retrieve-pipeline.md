<!-- Converted from api/logstash-configuration-management/retrieve-pipeline.asciidoc (AsciiDoc). Includes are inlined. -->

### Retrieve pipeline API

experimental[] Retrieve a centrally-managed Logstash pipeline.

#### Request

`GET <kibana host>:<port>/api/logstash/pipeline/<id>`

#### Path parameters

`id`::
  (Required, string) The pipeline ID.

#### Example

The API returns the following:

```sh
{
  "id": "hello-world",
  "description": "Just a simple pipeline",
  "username": "elastic",
  "pipeline": "input { stdin {} } output { stdout {} }",
  "settings": {
    "queue.type": "persistent"
  }
}
```
