<!-- Converted from scripting/apis/get-script-contexts-api.asciidoc (AsciiDoc). Includes are inlined. -->

### Get script contexts API

**New API reference**
For the most up-to-date API details, refer to [Script APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-script).

Retrieves a list of supported script contexts and their methods.

```console
GET _script_context
```

#### Request

`GET _script_context`

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the `manage`
cluster privilege to use this API.
