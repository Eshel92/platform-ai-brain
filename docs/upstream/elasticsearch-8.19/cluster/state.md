<!-- Converted from cluster/state.asciidoc (AsciiDoc). Includes are inlined. -->

### Cluster state API

**New API reference**
For the most up-to-date API details, refer to [Cluster APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-cluster).

Returns an internal representation of the cluster state for debugging or
diagnostic purposes.

#### Request

`GET /_cluster/state/<metrics>/<target>`

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the `monitor` or
`manage` cluster privilege to use this API.

#### Description

The _cluster state_ is an internal data structure which keeps track of a
variety of information needed by every node, including:

* The identity and attributes of the other nodes in the cluster

* Cluster-wide settings

* Index metadata, including the mapping and settings for each index

* The location and status of every shard copy in the cluster

The elected master node ensures that every node in the cluster has a copy of
the same cluster state. The cluster state API lets you retrieve a
representation of this internal state for debugging or diagnostic purposes. You
may need to consult the Elasticsearch source code to determine the precise meaning of
the response.

By default the cluster state API will route requests to the elected master node
since this node is the authoritative source of cluster states. You can also
retrieve the cluster state held on the node handling the API request by adding
the query parameter `?local=true`.

Elasticsearch may need to expend significant effort to compute a response to this API in
larger clusters, and the response may comprise a very large quantity of data.
If you use this API repeatedly, your cluster may become unstable.

**Warning:** The response is a representation of an internal data structure. Its
format is not subject to the same compatibility guarantees as other more stable
APIs and may change from version to version. **Do not query this API using
external monitoring tools.** Instead, obtain the information you require using
other more stable cluster APIs.

#### Path parameters

The cluster state can sometimes be very large, and Elasticsearch may consume significant
resources while computing a response to this API. To reduce the size of the
response, you can request only the part of the cluster state in which you are
interested:

`<metrics>`::
    (Optional, string) A comma-separated list of the following options:
  `_all`::
      Shows all metrics.
    
  `blocks`::
      Shows the `blocks` part of the response.

  `master_node`::
      Shows the `master_node` part of the response.
    
  `metadata`::
      Shows the `metadata` part of the response. If you supply a comma separated
      list of indices, the returned output will only contain metadata for these
      indices.

  `nodes`::
      Shows the `nodes` part of the response.

  `routing_nodes`::
      Shows the `routing_nodes` part of the response.

  `routing_table`::
      Shows the `routing_table` part of the response. If you supply a comma
      separated list of indices, the returned output will only contain the 
      routing table for these indices.
    
  `version`::
      Shows the cluster state version.

`<target>`::
(Optional, string) Comma-separated list of data streams, indices, and aliases
used to limit the request. Supports wildcards (`*`). To target all data streams
and indices, omit this parameter or use `*` or `_all`.

#### Query parameters

`allow_no_indices`::
    (Optional, Boolean) If `true`, the wildcard indices expression that resolves 
    into no concrete indices will be ignored. (This includes `_all` string or 
    when no indices have been specified).
Defaults to `true`.

`expand_wildcards`::
    (Optional, string) Whether to expand wildcard expression to concrete indices 
    that are open, closed or both. Available options: `open`, `closed`, `none`, 
    `all`.

`flat_settings`::
(Optional, Boolean) If `true`, returns settings in flat format. Defaults to
`false`.
`ignore_unavailable`::
    (Optional, Boolean) If `true`, unavailable indices (missing or closed) will 
    be ignored.

`local`::
(Optional, Boolean) If `true`, the request retrieves information from the local
node only. Defaults to `false`, which means information is retrieved from
the master node.
`master_timeout`::
(Optional, time units)
Period to wait for the master node. If the master node is not available before
the timeout expires, the request fails and returns an error. Defaults to `30s`.
Can also be set to `-1` to indicate that the request should never timeout.
`wait_for_metadata_version`::
    (Optional, integer) Waits for the metadata version to be equal or greater 
    than the specified metadata version.
    
`wait_for_timeout`::
    (Optional, time units) Specifies the maximum time to wait 
    for wait_for_metadata_version before timing out.

#### Examples

The following example returns only `metadata` and `routing_table` data for the
`foo` and `bar` data streams or indices:

```console
GET /_cluster/state/metadata,routing_table/foo,bar
```

The next example returns all available metadata for `foo` and `bar`:

```console
GET /_cluster/state/_all/foo,bar
```

This example returns only the `blocks` metadata:

```console
GET /_cluster/state/blocks
```
