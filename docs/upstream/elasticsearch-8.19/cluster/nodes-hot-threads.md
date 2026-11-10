<!-- Converted from cluster/nodes-hot-threads.asciidoc (AsciiDoc). Includes are inlined. -->

### Nodes hot threads API

**New API reference**
For the most up-to-date API details, refer to [Cluster APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-cluster).

Returns the hot threads on each selected node in the cluster.

#### Request

`GET /_nodes/hot_threads` +

`GET /_nodes/<node_id>/hot_threads`

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the `monitor` or
`manage` cluster privilege to use this API.

#### Description

This API yields a breakdown of the hot threads on each selected node in the
cluster. The output is plain text with a breakdown of each node's top hot 
threads.

#### Path parameters

`<node_id>`::
(Optional, string) Comma-separated list of node IDs or names used to limit
returned information.

#### Query parameters

`ignore_idle_threads`::
		(Optional, Boolean) If true, known idle threads (e.g. waiting in a socket 
		select, or to get a task from an empty queue) are filtered out. Defaults to 
		true.

`interval`::
		(Optional, time units) The interval to do the second 
		sampling of threads. Defaults to `500ms`.
		
`snapshots`::
		(Optional, integer) Number of samples of thread stacktrace. Defaults to 
		`10`.

`threads`::
		(Optional, integer) Specifies the number of hot threads to provide 
                information for. Defaults to `3`. If you are using this API for
                troubleshooting, set this parameter to a large number (e.g.
                `9999`) to get information about all the threads in the system.

`timeout`::
		(Optional, time units) Specifies how long to wait for a
                response from each node. If omitted, waits forever.

`type`::
		(Optional, string) The type to sample. Available options are `block`, `cpu`, and 
		`wait`. Defaults to `cpu`.

#### Examples

```console
GET /_nodes/hot_threads
GET /_nodes/nodeId1,nodeId2/hot_threads
```
