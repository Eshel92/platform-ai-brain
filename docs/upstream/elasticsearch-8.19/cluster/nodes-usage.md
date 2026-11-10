<!-- Converted from cluster/nodes-usage.asciidoc (AsciiDoc). Includes are inlined. -->

### Nodes feature usage API

**New API reference**
For the most up-to-date API details, refer to [Cluster APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-cluster).

Returns information on the usage of features.

#### Request

`GET /_nodes/usage` +

`GET /_nodes/<node_id>/usage` +

`GET /_nodes/usage/<metric>` +

`GET /_nodes/<node_id>/usage/<metric>`

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the `monitor` or
`manage` cluster privilege to use this API.

#### Description

The cluster nodes usage API allows you to retrieve information on the usage
of features for each node. All the nodes selective options are explained
here.

#### Path parameters

`<metric>`::
    (Optional, string) Limits the information returned to the specific metrics.
    A comma-separated list of the following options:
    `_all`::
        Returns all stats.

    `rest_actions`::
        Returns the REST actions classname with a count of the number of times
        that action has been called on the node.

`<node_id>`::
(Optional, string) Comma-separated list of node IDs or names used to limit
returned information.

#### Query parameters

`timeout`::
(Optional, time units)
Period to wait for each node to respond. If a node does not respond before its
timeout expires, the response does not include its information. However, timed out
nodes are included in the response's `_nodes.failed` property. Defaults to no
timeout.

#### Examples

Rest action example:

```console
GET _nodes/usage
```

The API returns the following response:

```console-result
{
  "_nodes": {
    "total": 1,
    "successful": 1,
    "failed": 0
  },
  "cluster_name": "my_cluster",
  "nodes": {
    "pQHNt5rXTTWNvUgOrdynKg": {
      "timestamp": 1492553961812, <1>
      "since": 1492553906606, <2>
      "rest_actions": {
        "nodes_usage_action": 1,
        "create_index_action": 1,
        "document_get_action": 1,
        "search_action": 19, <3>
        "nodes_info_action": 36
      },
      "aggregations": {
        ...
      }
    }
  }
}
```
<1> Timestamp for when this nodes usage request was performed.
<2> Timestamp for when the usage information recording was started. This is
equivalent to the time that the node was started.
<3> Search action has been called 19 times for this node.
