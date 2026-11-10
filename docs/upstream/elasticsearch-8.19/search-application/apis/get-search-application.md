<!-- Converted from search-application/apis/get-search-application.asciidoc (AsciiDoc). Includes are inlined. -->

### Get Search Application

**New API reference**
For the most up-to-date API details, refer to [Search application APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-search_application).

beta::[]

Retrieves information about a search application.

#### Request

`GET _application/search_application/<name>`

#### Prerequisites

Requires the `manage_search_application` cluster privilege.

#### Path parameters

`<name>`::
(Required, string)

#### Response codes

`400`::
The `name` was not provided.

`404` (Missing resources)::
No Search Application matching `name` could be found.

#### Examples

The following example gets the Search Application named `my-app`:

```console
GET _application/search_application/my-app/
```

A sample response:

```console-result
{
  "name": "my-app",
  "indices": [ "index1", "index2" ],
  "updated_at_millis": 1682105622204,
  "template": {
    "script": {
      "source": {
        "query": {
          "query_string": {
            "query": "{{query_string}}",
            "default_field": "{{default_field}}"
          }
        }
      },
      "lang": "mustache",
      "options": {
        "content_type": "application/json;charset=utf-8"
      },
      "params": {
        "query_string": "*",
        "default_field": "*"
      }
    }
  }
}
```
