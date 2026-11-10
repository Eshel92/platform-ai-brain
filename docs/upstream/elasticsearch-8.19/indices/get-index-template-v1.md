<!-- Converted from indices/get-index-template-v1.asciidoc (AsciiDoc). Includes are inlined. -->

### Get index template API

**Important:** This documentation is about legacy index templates, 
which are deprecated and will be replaced by the composable templates introduced in Elasticsearch 7.8. 
For information about composable templates, see index-templates.

**New API reference**
For the most up-to-date API details, refer to [Index APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-indices).

Retrieves information about one or more index templates.

```console
GET /_template/template_1
```

#### Request

`GET /_template/<index-template>`

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the
`manage_index_templates` or `manage` <<privileges-list-cluster,cluster
privilege>> to use this API.

#### Path parameters

`<index-template>`::
(Required, string)
Comma-separated list of index template names used to limit the request. Wildcard
(`*`) expressions are supported.
To return all index templates, omit this parameter
or use a value of `_all` or `*`.

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

#### Examples

##### Get multiple index templates

```console
GET /_template/template_1,template_2
```

##### Get index templates using a wildcard expression

```console
GET /_template/temp*
```

##### Get all index templates

```console
GET /_template
```
