<!-- Converted from indices/get-component-template.asciidoc (AsciiDoc). Includes are inlined. -->

### Get component template API

**New API reference**
For the most up-to-date API details, refer to [Index APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-indices).

Retrieves information about one or more component templates.

```console
PUT /_component_template/template_1
{
  "template": {
    "settings": {
      "index.number_of_replicas": 0
    },
    "mappings": {
      "properties": {
        "@timestamp": {
          "type": "date"
        }
      }
    }
  }
}
```

```console
DELETE /_component_template/template_*
```

```console
GET /_component_template/template_1
```

#### Request

`GET /_component_template/<component-template>`

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the
`manage_index_templates` or `manage` <<privileges-list-cluster,cluster
privilege>> to update templates, or the `monitor` cluster privilege to retrieve templates.

#### Path parameters

`<component-template>`::
(Optional, string)
Comma-separated list of component template names used to limit the request.
Wildcard (`*`) expressions are supported.

#### Query parameters

`flat_settings`::
(Optional, Boolean) If `true`, returns settings in flat format. Defaults to
`false`.
`local`::
(Optional, Boolean) If `true`, the request retrieves information from the local
node only. Defaults to `false`, which means information is retrieved from
the master node.
`master_timeout`::
(Optional, time units)
Period to wait for the master node. If the master node is not available before
the timeout expires, the request fails and returns an error. Defaults to `30s`.
Can also be set to `-1` to indicate that the request should never timeout.
`include_defaults`::
(Optional, Boolean) Functionality in preview:[]. If `true`, return all default settings in the response.
Defaults to `false`.

#### Examples

##### Get component templates using a wildcard expression

```console
GET /_component_template/temp*
```

##### Get all component templates

```console
GET /_component_template
```
