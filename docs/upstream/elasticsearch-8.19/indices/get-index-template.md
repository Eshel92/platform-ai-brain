<!-- Converted from indices/get-index-template.asciidoc (AsciiDoc). Includes are inlined. -->

### Get index template API [[getting-templates]]

**New API reference**
For the most up-to-date API details, refer to [Index APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-indices).

Returns information about one or more index templates.

```console
GET /_index_template/template_1
```

#### Request

`GET /_index_template/<index-template>`

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the
`manage_index_templates` or `manage` <<privileges-list-cluster,cluster
privilege>> to use this API, or the `monitor` cluster privilege to retrieve templates.

#### Path parameters

(Optional, string) The name of the template to return. Accepts wildcard
expressions. If omitted, all templates are returned.

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

##### Get index templates using a wildcard expression

```console
GET /_index_template/temp*
```

##### Get all index templates

```console
GET /_index_template
```
