<!-- Converted from indices/delete-index-template-v1.asciidoc (AsciiDoc). Includes are inlined. -->

### Delete index template API

**Important:** This documentation is about <<indices-templates-v1,legacy index
templates>>, which are deprecated and will be replaced by the composable
templates introduced in Elasticsearch 7.8. For information about composable templates,
see index-templates.

**New API reference**
For the most up-to-date API details, refer to [Index APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-indices).

Deletes a legacy index template.

```console
DELETE /_template/my-legacy-index-template
```

#### Request

`DELETE /_template/<legacy-index-template>`

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the
`manage_index_templates` or `manage` <<privileges-list-cluster,cluster
privilege>> to use this API.

#### Path parameters

`<legacy-index-template>`::
(Required, string)
The name of the legacy index template to delete. Wildcard (`*`)
expressions are supported.

#### Query parameters

`master_timeout`::
(Optional, time units)
Period to wait for the master node. If the master node is not available before
the timeout expires, the request fails and returns an error. Defaults to `30s`.
Can also be set to `-1` to indicate that the request should never timeout.
