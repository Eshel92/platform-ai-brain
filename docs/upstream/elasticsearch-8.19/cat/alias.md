<!-- Converted from cat/alias.asciidoc (AsciiDoc). Includes are inlined. -->

### cat aliases API

**New API reference**
For the most up-to-date API details, refer to [Compact and aligned text (CAT) APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-cat)..

**Important:**
cat APIs are only intended for human consumption using the command line or the 
Kibana console. They are _not_ intended for use by applications. For application 
consumption, use the aliases API.

Retrieves the cluster's index aliases, including filter and routing
information. The API does not return data stream aliases.

#### Request

`GET _cat/aliases/<alias>`

`GET _cat/aliases`

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the
`view_index_metadata` or `manage` index privilege
for any alias you retrieve.

#### Path parameters

`<alias>`::
(Optional, string) Comma-separated list of aliases to retrieve. Supports
wildcards (`*`). To retrieve all aliases, omit this parameter or use `*` or
`_all`.

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
`s`::
(Optional, string) Comma-separated list of column names or column aliases used
to sort the response.
`v`::
(Optional, Boolean) If `true`, the response includes column headings.
Defaults to `false`.
`expand_wildcards`::
(Optional, string)
Type of index that wildcard patterns can match. If the request can target data
streams, this argument determines whether wildcard expressions match hidden data
streams. Supports comma-separated values, such as `open,hidden`. Valid values
are:

`all`::
Match any data stream or index, including hidden ones.

`open`::
Match open, non-hidden indices. Also matches any non-hidden data stream.

`closed`::
Match closed, non-hidden indices. Also matches any non-hidden data stream. Data
streams cannot be closed.

`hidden`::
Match hidden data streams and hidden indices. Must be combined with `open`,
`closed`, or both.

`none`::
Wildcard patterns are not accepted.

#### Examples

```console
GET _cat/aliases?v=true
```

The API returns the following response:

```txt
alias  index filter routing.index routing.search is_write_index
alias1 test1 -      -            -              -
alias2 test1 *      -            -              -
alias3 test1 -      1            1              -
alias4 test1 -      2            1,2            -
```

This response shows that `alias2` has configured a filter, and specific routing
configurations in `alias3` and `alias4`.

If you only want to get information about specific aliases, you can specify 
the aliases in comma-delimited format as a URL parameter, e.g., 
/_cat/aliases/alias1,alias2.
