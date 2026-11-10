<!-- Converted from cat/nodeattrs.asciidoc (AsciiDoc). Includes are inlined. -->

### cat nodeattrs API

**New API reference**
For the most up-to-date API details, refer to [Compact and aligned text (CAT) APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-cat)..

**Important:**
cat APIs are only intended for human consumption using the command line or Kibana 
console. They are _not_ intended for use by applications. For application 
consumption, use the nodes info API.

Returns information about custom node attributes.

#### Request

`GET /_cat/nodeattrs`

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the `monitor` or
`manage` cluster privilege to use this API.

#### Query parameters

`format`::
(Optional, string) Short version of the
[HTTP accept header](https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html).
Valid values include JSON, YAML, etc.
`h`::
(Optional, string) Comma-separated list of column names to display.
If you do not specify which columns to include, the API returns the default columns in the order listed below. If you explicitly specify one or more columns, it only returns the specified columns.

Valid columns are:

`node`,`name`::
(Default) Name of the node, such as `DKDM97B`.

`host`, `h`::
(Default) Host name, such as `n1`.

`ip`, `i`::
(Default) IP address, such as `127.0.1.1`.

`attr`, `attr.name`::
(Default) Attribute name, such as `rack`.

`value`, `attr.value`::
(Default) Attribute value, such as `rack123`.

`id`, `nodeId`::
ID of the node, such as `k0zy`.

`pid`, `p`::
Process ID, such as `13061`.

`port`, `po`::
Bound transport port, such as `9300`.

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

##### Example with default columns

```console
GET /_cat/nodeattrs?v=true
```

The API returns the following response:

```txt
node    host      ip        attr     value
...
node-0 127.0.0.1 127.0.0.1 testattr test
...
```

The `node`, `host`, and `ip` columns provide basic information about each node.
The `attr` and `value` columns return custom node attributes, one per line.

##### Example with explicit columns

The following API request returns the `name`, `pid`, `attr`, and `value`
columns.

```console
GET /_cat/nodeattrs?v=true&h=name,pid,attr,value
```

The API returns the following response:

```txt
name    pid   attr     value
...
node-0 19566 testattr test
...
```
