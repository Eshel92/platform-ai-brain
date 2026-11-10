<!-- Converted from cat/count.asciidoc (AsciiDoc). Includes are inlined. -->

### cat count API

**New API reference**
For the most up-to-date API details, refer to [Compact and aligned text (CAT) APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-cat)..

**Important:**
cat APIs are only intended for human consumption using the command line or Kibana 
console. They are _not_ intended for use by applications. For application 
consumption, use the count API.

Provides quick access to a document count for a data stream, an index, or an
entire cluster.

**Note:** The document count only includes live documents, not deleted documents
which have not yet been removed by the merge process.

#### Request

`GET /_cat/count/<target>`

`GET /_cat/count`

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the `read`
index privilege for any data stream, index, or alias
you retrieve.

#### Path parameters

`<target>`::
(Optional, string) Comma-separated list of data streams, indices, and aliases
used to limit the request. Supports wildcards (`*`). To target all data streams
and indices, omit this parameter or use `*` or `_all`.

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
`s`::
(Optional, string) Comma-separated list of column names or column aliases used
to sort the response.
`v`::
(Optional, Boolean) If `true`, the response includes column headings.
Defaults to `false`.

#### Examples

##### Example with an individual data stream or index

The following `count` API request retrieves the document count for the 
`my-index-000001` data stream or index.

```console
GET /_cat/count/my-index-000001?v=true
```

The API returns the following response:

```txt
epoch      timestamp count
1475868259 15:24:20  120
```

##### Example with all data streams and indices in a cluster

The following `count` API request retrieves the document count for all data
streams and indices in the cluster.

```console
GET /_cat/count?v=true
```

The API returns the following response:

```txt
epoch      timestamp count
1475868259 15:24:20  121
```
