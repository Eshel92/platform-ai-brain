<!-- Converted from scripting/apis/get-script-languages-api.asciidoc (AsciiDoc). Includes are inlined. -->

### Get script languages API

**New API reference**
For the most up-to-date API details, refer to [Script APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-script).

Retrieves a list of supported script languages
and their contexts.

```console
GET _script_language
```

#### Request

`GET _script_language`

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the `manage`
cluster privilege to use this API.
