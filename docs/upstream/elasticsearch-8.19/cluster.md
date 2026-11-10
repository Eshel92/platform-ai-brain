<!-- Converted from cluster.asciidoc (AsciiDoc). Includes are inlined. -->

## Cluster APIs

**New API reference**
For the most up-to-date API details, refer to [Cluster APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-cluster).

### Node specification

Some cluster-level APIs may operate on a subset of the nodes which can be
specified with _node filters_. For example, the Task Management,
Nodes Stats, and Nodes Info APIs
can all report results from a filtered set of nodes rather than from all nodes.

_Node filters_ are written as a comma-separated list of individual filters,
each of which adds or removes nodes from the chosen subset. Each filter can be
one of the following:

* `_all`, to add all nodes to the subset.
* `_local`, to add the local node to the subset.
* `_master`, to add the currently-elected master node to the subset.
* a node id or name, to add this node to the subset.
* an IP address or hostname, to add all matching nodes to the subset.
* a pattern, using `*` wildcards, which adds all nodes to the subset
  whose name, address or hostname matches the pattern.
* `master:true`, `data:true`, `ingest:true`, `voting_only:true`, `ml:true`, or
  `coordinating_only:true`, which respectively add to the subset all
  master-eligible nodes, all data nodes, all ingest nodes, all voting-only
  nodes, all machine learning nodes, and all coordinating-only nodes.
* `master:false`, `data:false`, `ingest:false`, `voting_only:false`, `ml:false`,
  or `coordinating_only:false`, which respectively remove from the subset all
  master-eligible nodes, all data nodes, all ingest nodes, all voting-only
  nodes, all machine learning nodes, and all coordinating-only nodes.
* a pair of patterns, using `*` wildcards, of the form `attrname:attrvalue`,
  which adds to the subset all nodes with a custom node attribute whose name
  and value match the respective patterns. Custom node attributes are
  configured by setting properties in the configuration file of the form
  `node.attr.attrname: attrvalue`.

**Note:** node filters run in the order in which they are given, which is important
if using filters that remove nodes from the set. For example
`_all,master:false` means all the nodes except the master-eligible ones, but
`master:false,_all` means the same as `_all` because the `_all` filter runs
after the `master:false` filter.

**Note:** if no filters are given, the default is to select all nodes. However, if
any filters are given then they run starting with an empty chosen subset. This
means that filters such as `master:false` which remove nodes from the chosen
subset are only useful if they come after some other filters. When used on its
own, `master:false` selects no nodes.

Here are some examples of the use of node filters with the
Nodes Info APIs.

```console
# If no filters are given, the default is to select all nodes
GET /_nodes
# Explicitly select all nodes
GET /_nodes/_all
# Select just the local node
GET /_nodes/_local
# Select the elected master node
GET /_nodes/_master
# Select nodes by name, which can include wildcards
GET /_nodes/node_name_goes_here
GET /_nodes/node_name_goes_*
# Select nodes by address, which can include wildcards
GET /_nodes/10.0.0.3,10.0.0.4
GET /_nodes/10.0.0.*
# Select nodes by role
GET /_nodes/_all,master:false
GET /_nodes/data:true,ingest:true
GET /_nodes/coordinating_only:true
GET /_nodes/master:true,voting_only:false
# Select nodes by custom attribute (e.g. with something like `node.attr.rack: 2` in the configuration file)
GET /_nodes/rack:2
GET /_nodes/ra*:2
GET /_nodes/ra*:2*
```

(See `cluster/allocation-explain.md`)
(See `cluster/get-settings.md`)
(See `cluster/health.md`)
(See `health/health.md`)
(See `cluster/reroute.md`)
(See `cluster/state.md`)
(See `cluster/stats.md`)
(See `cluster/update-settings.md`)
(See `cluster/nodes-usage.md`)
(See `cluster/nodes-hot-threads.md`)
(See `cluster/nodes-info.md`)
(See `cluster/prevalidate-node-removal.md`)
(See `cluster/nodes-reload-secure-settings.md`)
(See `cluster/nodes-stats.md`)
(See `cluster/cluster-info.md`)
(See `cluster/pending.md`)
(See `cluster/remote-info.md`)
(See `cluster/tasks.md`)
(See `cluster/voting-exclusions.md`)
(See `cluster/update-desired-nodes.md`)
(See `cluster/get-desired-nodes.md`)
(See `cluster/delete-desired-nodes.md`)
(See `cluster/get-desired-balance.md`)
(See `cluster/delete-desired-balance.md`)
