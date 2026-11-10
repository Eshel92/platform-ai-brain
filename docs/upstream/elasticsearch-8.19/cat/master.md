<!-- Converted from cat/master.asciidoc (AsciiDoc). Includes are inlined. -->

### cat master API

**New API reference**
For the most up-to-date API details, refer to [Compact and aligned text (CAT) APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-cat)..

**Important:**
cat APIs are only intended for human consumption using the command line or Kibana 
console. They are _not_ intended for use by applications. For application 
consumption, use the nodes info API.

Returns information about the master node, including the ID, bound IP address,
and name.

#### Request

`GET /_cat/master`

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
GET /_cat/master?v=true
```

The API returns the following response:

```txt
id                     host      ip        node
YzWoH_2BT-6UjVGDyPdqYg 127.0.0.1 127.0.0.1 YzWoH_2
```

This information is also available via the `nodes` command, but this
is slightly shorter when all you want to do, for example, is verify
all nodes agree on the master:

```sh
% pssh -i -h list.of.cluster.hosts curl -s localhost:9200/_cat/master
[1] 19:16:37 [SUCCESS] es3.vm
Ntgn2DcuTjGuXlhKDUD4vA 192.168.56.30 H5dfFeA
[2] 19:16:37 [SUCCESS] es2.vm
Ntgn2DcuTjGuXlhKDUD4vA 192.168.56.30 H5dfFeA
[3] 19:16:37 [SUCCESS] es1.vm
Ntgn2DcuTjGuXlhKDUD4vA 192.168.56.30 H5dfFeA
```
