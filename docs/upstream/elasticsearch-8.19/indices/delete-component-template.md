<!-- Converted from indices/delete-component-template.asciidoc (AsciiDoc). Includes are inlined. -->

### Delete component template API

**New API reference**
For the most up-to-date API details, refer to [Index APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-indices).

Deletes an existing component template.

```console
DELETE _component_template/template_1
```

The provided <component-template> may contain multiple template names separated by a comma.
If multiple template names are specified then there is no wildcard support and the
provided names should match completely with existing component templates.

#### Request

`DELETE /_component_template/<component-template>`

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the
`manage_index_templates` or `manage` <<privileges-list-cluster,cluster
privilege>> to use this API.

#### Description

Use the delete component template API to delete one or more component templates
Component templates are building blocks for constructing index templates
that specify index mappings, settings, and aliases.

#### Path parameters

`<component-template>`::
(Required, string)
Comma-separated list or wildcard expression of component template names
used to limit the request.

#### Query parameters

`master_timeout`::
(Optional, time units)
Period to wait for the master node. If the master node is not available before
the timeout expires, the request fails and returns an error. Defaults to `30s`.
Can also be set to `-1` to indicate that the request should never timeout.
