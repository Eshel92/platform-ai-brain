<!-- Converted from indices/delete-index-template.asciidoc (AsciiDoc). Includes are inlined. -->

### Delete index template API

**New API reference**
For the most up-to-date API details, refer to [Index APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-indices).

Deletes an index template.

```console
DELETE /_index_template/my-index-template
```

#### Request

`DELETE /_index_template/<index-template>`

The provided <index-template> may contain multiple template names separated by a comma.
If multiple template names are specified then there is no wildcard support and the
provided names should match completely with existing templates.

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the
`manage_index_templates` or `manage` <<privileges-list-cluster,cluster
privilege>> to use this API.

#### Description

Use the delete index template API to delete one or more index templates.
Index templates define settings, mappings,
and aliases that can be applied automatically to new indices.

#### Path parameters

`<index-template>`::
(Required, string)
Comma-separated list of index template names used to limit the request. Wildcard
(`*`) expressions are supported.

#### Query parameters

`master_timeout`::
(Optional, time units)
Period to wait for the master node. If the master node is not available before
the timeout expires, the request fails and returns an error. Defaults to `30s`.
Can also be set to `-1` to indicate that the request should never timeout.
