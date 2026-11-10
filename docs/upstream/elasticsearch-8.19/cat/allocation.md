<!-- Converted from cat/allocation.asciidoc (AsciiDoc). Includes are inlined. -->

### cat allocation API

**New API reference**
For the most up-to-date API details, refer to [Compact and aligned text (CAT) APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-cat)..

**Important:**
cat APIs are only intended for human consumption using the command line or Kibana
console. They are _not_ intended for use by applications.

Provides a snapshot of the number of shards allocated to each data node
and their disk space.

#### Request

`GET /_cat/allocation/<node_id>`

`GET /_cat/allocation`

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the `monitor` or
`manage` cluster privilege to use this API.

#### Path parameters

`<node_id>`::
(Optional, string) Comma-separated list of node IDs or names used to limit
returned information.

#### Query parameters

`bytes`::
(Optional, byte size units) Unit used to display byte values.
`format`::
(Optional, string) Short version of the
[HTTP accept header](https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html).
Valid values include JSON, YAML, etc.
`local`::
(Optional, Boolean) If `true`, the request retrieves information from the local
node only. Defaults to `false`, which means information is retrieved from
the master node.
`master_timeout`::
(Optional, time units)
Period to wait for the master node. If the master node is not available before
the timeout expires, the request fails and returns an error. Defaults to `30s`.
Can also be set to `-1` to indicate that the request should never timeout.
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

#### Response body

`shards`::
Number of primary and replica shards assigned to the node.

`shards.undesired`::
Amount of shards that are scheduled to be moved elsewhere in the cluster
or -1 other than desired balance allocator is used

`write_load.forecast`::
Sum of index write load forecasts

`disk.indices.forecast`::
Sum of shard size forecasts

`disk.indices`::
Disk space used by the node's shards. Does not include disk space for the
translog or unassigned shards.
**Important:** This metric double-counts disk space for hard-linked files, such as
those created when shrinking,
splitting, or cloning an index.

`disk.used`::
Total disk space in use. Elasticsearch retrieves this metric from the node's operating
system (OS). The metric includes disk space for:

- Elasticsearch, including the translog and unassigned shards
- The node's OS
- Any other applications or files on the node

Unlike `disk.indices`, this metric does not double-count disk space for
hard-linked files.

`disk.avail`::
Free disk space available to Elasticsearch. Elasticsearch retrieves this metric from the node's
OS. Disk-based shard allocation uses this metric to assign
shards to nodes based on available disk space.

`disk.total`::
Total disk space for the node, including in-use and available space.

`disk.percent`::
Total percentage of disk space in use. Calculated as `disk.used` / `disk.total`.

`host`::
Network host for the node. Set using `network.host`.

`ip`::
IP address and port for the node.

`node`::
Name for the node. Set using `node.name`.

`node.role`, `r`, `role`, `nodeRole`::
Node roles

#### Examples

```console
GET /_cat/allocation?v=true
```

The API returns the following response:

```txt
shards shards.undesired write_load.forecast disk.indices.forecast disk.indices disk.used disk.avail disk.total disk.percent host      ip        node    node.role
     1                0                 0.0                  260b         260b    47.3gb     43.4gb    100.7gb           46 127.0.0.1 127.0.0.1 CSUXak2 himrst
```

This response shows a single shard is allocated to the one node available.
