<!-- Converted from cat/templates.asciidoc (AsciiDoc). Includes are inlined. -->

### cat templates API

**New API reference**
For the most up-to-date API details, refer to [Compact and aligned text (CAT) APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-cat)..

**Important:**
cat APIs are only intended for human consumption using the command line or Kibana 
console. They are _not_ intended for use by applications. For application 
consumption, use the get index template API.

Returns information about index templates in a cluster.
You can use index templates to apply index settings
and field mappings to new indices at creation.

#### Request

`GET /_cat/templates/<template_name>`

`GET /_cat/templates`

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the `monitor` or
`manage` cluster privilege to use this API.

#### Path parameters

`<template_name>`::
(Optional, string) The name of the template to return. Accepts wildcard
expressions. If omitted, all templates are returned.

#### Query parameters

`format`::
(Optional, string) Short version of the
[HTTP accept header](https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html).
Valid values include JSON, YAML, etc.
`h`::
(Optional, string) Comma-separated list of column names to display.
`help`::
(Optional, Boolean) If `true`, the response includes help information. Defaults
to `false`.
`local`::
(Optional, Boolean) If `true`, the request retrieves information from the local
node only. Defaults to `false`, which means information is retrieved from
the master node.
`master_timeout`::
(Optional, time units)
Period to wait for the master node. If the master node is not available before
the timeout expires, the request fails and returns an error. Defaults to `30s`.
Can also be set to `-1` to indicate that the request should never timeout.
`s`::
(Optional, string) Comma-separated list of column names or column aliases used
to sort the response.
`v`::
(Optional, Boolean) If `true`, the response includes column headings.
Defaults to `false`.

#### Examples

```console
GET _cat/templates/my-template-*?v=true&s=name
```

The API returns the following response:

```txt
name          index_patterns order version composed_of
my-template-0 [te*]          500           []
my-template-1 [tea*]         501           []
my-template-2 [teak*]        502   7       []
```
