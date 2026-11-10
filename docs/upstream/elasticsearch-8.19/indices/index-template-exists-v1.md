<!-- Converted from indices/index-template-exists-v1.asciidoc (AsciiDoc). Includes are inlined. -->

### Index template exists API

**Important:** This documentation is about <<indices-templates-v1,legacy index
templates>>, which are deprecated and will be replaced by the composable
templates introduced in Elasticsearch 7.8. For information about composable templates,
see index-templates.

**New API reference**
For the most up-to-date API details, refer to [Index APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-indices).

Checks if an legacy index template exists.

```console
HEAD /_template/template_1
```

#### Request

`HEAD /_template/<index-template>`

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the
`manage_index_templates` or `manage` <<privileges-list-cluster,cluster
privilege>> to use this API.

#### Description

Use the index template exists API
to determine whether one or more index templates exist.

Index templates define settings, mappings, 
and aliases that can be applied automatically to new indices. 

#### Path parameters

`<index-template>`::
(Required, string)
Comma-separated list of index template names used to limit the request. Wildcard
(`*`) expressions are supported.

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

#### Response codes

`200`::
Indicates all specified index templates exist.

`404`::
Indicates one or more specified index templates **do not** exist.
