<!-- Converted from api/logstash-configuration-management/delete-pipeline.asciidoc (AsciiDoc). Includes are inlined. -->

### Delete Logstash pipeline API

experimental[] Delete a centrally-managed Logstash pipeline.

#### Request

`DELETE <kibana host>:<port>/api/logstash/pipeline/<id>`

#### Path parameters

`id`::
  (Required, string) The pipeline ID.

#### Response code

`204 No Content`::
    Indicates a successful call.

#### Example

```sh
$ curl -X DELETE api/logstash/pipeline/hello-world
```
