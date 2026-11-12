<!-- Part 2 of 8 of victoriametrics/Cluster-VictoriaMetrics.md (split because the page is big). -->

## Cluster setup

A minimal cluster setup consists of the following components:

- a single `vmstorage` node with `-retentionPeriod` and `-storageDataPath` flags
- a single `vminsert` node with `-storageNode=<vmstorage_host>`
- a single `vmselect` node with `-storageNode=<vmstorage_host>`

> The [Enterprise version of VictoriaMetrics](https://docs.victoriametrics.com/victoriametrics/enterprise/) supports automatic discovery and updating of `vmstorage` nodes.
> See [automatic vmstorage discovery](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/#automatic-vmstorage-discovery) for details.

Prefer running many small `vmstorage` nodes over a few big `vmstorage` nodes. For example, prefer running at least 10 (or more) `vmstorage` nodes for better [load distribution and availability](#cluster-availability). If you need fewer `vmstorage` nodes, consider using the [single-node version](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/) of VictoriaMetrics instead. See more on [choosing between single-node and cluster versions](https://docs.victoriametrics.com/victoriametrics/faq/#which-victoriametrics-type-is-recommended-for-use-in-production---single-node-or-cluster).

If you run multiple nodes of `vminsert` or `vmselect`, use an HTTP load balancer such as [vmauth](https://docs.victoriametrics.com/victoriametrics/vmauth/)
or `nginx` in front of them. It must contain the following routing configs according to [the URL format](#url-format):

- requests starting with `/insert` must be routed to port `8480` on `vminsert` nodes.
- requests starting with `/select` must be routed to port `8481` on `vmselect` nodes.

> Ports may be altered by setting `-httpListenAddr` on the corresponding nodes.

See an example of the [vmauth configuration for a VictoriaMetrics cluster](https://docs.victoriametrics.com/vmauth/index.html#load-balancer-for-victoriametrics-cluster).

It is recommended setting up [monitoring](#monitoring) for the cluster.

The following tools can simplify cluster setup:

- [An example docker-compose config for VictoriaMetrics cluster](https://github.com/VictoriaMetrics/VictoriaMetrics/tree/master/deployment/docker#victoriametrics-cluster)
- [Helm charts for VictoriaMetrics](https://github.com/VictoriaMetrics/helm-charts)
- [Kubernetes operator for VictoriaMetrics](https://github.com/VictoriaMetrics/operator)

It is possible manually setting up a toy cluster on a single host. In this case every cluster component - `vminsert`, `vmselect` and `vmstorage` - must have distinct values for `-httpListenAddr` command-line flag. This flag specifies http address for accepting http requests for [monitoring](#monitoring) and [profiling](#profiling). `vmstorage` node must have distinct values for the following additional command-line flags in order to prevent resource usage clash:

- `-storageDataPath` - every `vmstorage` node must have a dedicated data storage.
- `-vminsertAddr` - every `vmstorage` node must listen for a distinct tcp address for accepting data from `vminsert` nodes.
- `-vmselectAddr` - every `vmstorage` node must listen for a distinct tcp address for accepting requests from `vmselect` nodes.

### Cluster availability

VictoriaMetrics cluster architecture prioritizes availability over data consistency.
This means that the cluster remains available for data ingestion and data querying
if some of its components are temporarily unavailable.

VictoriaMetrics cluster remains available if the following conditions are met:

- HTTP load balancer must stop routing requests to unavailable `vminsert` and `vmselect` nodes
  ([vmauth](https://docs.victoriametrics.com/victoriametrics/vmauth/) stops routing requests to unavailable nodes).

- At least a single `vminsert` node must remain available in the cluster for processing the ingestion workload.
  The remaining active `vminsert` nodes must have enough compute capacity (CPU, RAM, network bandwidth)
  for handling the ingestion workload. Otherwise, ingestion could stop or be delayed.
  See [capacity planning](#capacity-planning) and [cluster resizing](#cluster-resizing-and-scalability) docs for more details.

- At least a single `vmselect` node must remain available in the cluster for processing query workload.
  The remaining active `vmselect` nodes must have enough compute capacity (CPU, RAM, network bandwidth, disk IO)
  for handling the query workload.
  If the remaining active `vmselect` nodes do not have enough resources for processing the query workload,
  then arbitrary query failures and latency increases may occur during query processing.
  See [capacity planning](#capacity-planning) and [cluster resizing](#cluster-resizing-and-scalability) docs for more details.

- At least a single `vmstorage` node must remain available in the cluster for accepting newly ingested data
  and for processing incoming read queries. The remaining active `vmstorage` nodes must have enough compute capacity
  (CPU, RAM, network bandwidth, disk IO, free disk space) for handling the workload.
  If the remaining active `vmstorage` nodes do not have enough resources for processing the workload,
  then arbitrary failures and delays may occur during data ingestion and query processing.
  See [capacity planning](#capacity-planning) and [cluster resizing](#cluster-resizing-and-scalability) docs for more details.

The cluster works in the following way when some of `vmstorage` nodes are unavailable:

- `vminsert` [re-routes](https://victoriametrics.com/blog/vminsert-how-it-works/#31-rerouting) newly ingested data from
  unavailable `vmstorage` nodes to remaining healthy `vmstorage` nodes. This guarantees that the newly ingested data is
  properly saved if the healthy `vmstorage` nodes have enough CPU, RAM, disk I/O, and network bandwidth for processing
  the increased data ingestion workload. During re-routing, healthy `vmstorage` nodes will experience higher resource usage
  and an increase in the number of [active time series](https://docs.victoriametrics.com/victoriametrics/faq/#what-is-an-active-time-series).

- `vmselect` continues serving queries if at least a single `vmstorage` nodes is available.
  It marks responses as partial for queries served from the remaining healthy `vmstorage` nodes,
  since such responses may miss historical data stored on the temporarily unavailable `vmstorage` nodes.
  Every partial JSON response contains `"isPartial": true` option.
  If you prefer consistency over availability, then run `vmselect` nodes with `-search.denyPartialResponse` command-line flag.
  In this case `vmselect` returns an error if at least a single `vmstorage` node is unavailable.
  Another option is to pass `deny_partial_response=1` query arg to requests to `vmselect` nodes.

  `vmselect` also accepts `-replicationFactor=N` command-line flag. This flag instructs `vmselect` to return full response
  if less than `-replicationFactor` vmstorage nodes are unavailable during querying, since it assumes that the remaining
  `vmstorage` nodes contain the full data. See [these docs](#replication-and-data-safety) for details.

  It is also possible to configure independent replication factor per distinct `vmstorage` groups - see [these docs](#vmstorage-groups-at-vmselect).

`vmselect` doesn't serve partial responses for API handlers returning [raw datapoints](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#raw-samples),
since users usually expect this data is always complete. The following handlers return raw samples:

- [`/api/v1/export*` endpoints](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#how-to-export-time-series)
- [`/api/v1/query`](https://docs.victoriametrics.com/victoriametrics/url-examples/#apiv1query) when the `query` contains [series selector](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#filtering)
  ending with some duration in square brackets. For example, `/api/v1/query?query=up[1h]&time=2024-01-02T03:00:00Z`.
  This query returns [raw samples](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#raw-samples) for [time series](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#time-series)
  with the `up` name on the time range `(2024-01-02T02:00:00 .. 2024-01-02T03:00:00]`. See [this article](https://valyala.medium.com/analyzing-prometheus-data-with-external-tools-5f3e5e147639)
  for details.

Data replication can be used for increasing storage durability. See [these docs](#replication-and-data-safety) for details.

### Multi-level cluster setup

`vmselect` nodes can be queried by other `vmselect` nodes if they run with `-clusternativeListenAddr` command-line flag.
For example, if `vmselect` is started with `-clusternativeListenAddr=:8401`, then it can accept queries from another `vmselect` nodes at TCP port 8401
in the same way as `vmstorage` nodes do. This allows chaining `vmselect` nodes and building multi-level cluster topologies.
For example, the top-level `vmselect` node can query second-level `vmselect` nodes in different availability zones (AZ),
while the second-level `vmselect` nodes can query `vmstorage` nodes in local AZ. See also [vmstorage groups at vmselect](#vmstorage-groups-at-vmselect).

`vminsert` nodes can accept data from another `vminsert` nodes if they run with `-clusternativeListenAddr` command-line flag.
For example, if `vminsert` is started with `-clusternativeListenAddr=:8400`, then it can accept data from another `vminsert` nodes at TCP port 8400
in the same way as `vmstorage` nodes do. This allows chaining `vminsert` nodes and building multi-level cluster topologies.
For example, the top-level `vminsert` node can replicate data among the second level of `vminsert` nodes located in distinct availability zones (AZ),
while the second-level `vminsert` nodes can spread the data among `vmstorage` nodes in local AZ.

The multi-level cluster setup for `vminsert` nodes has the following shortcomings because of synchronous replication and data sharding:

- Data ingestion speed is limited by the slowest link to AZ.
- `vminsert` nodes at top level re-route incoming data to the remaining AZs when some AZs are temporarily unavailable. This results in data gaps at AZs which were temporarily unavailable.

These issues are addressed by [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/) when it runs in front of AZs
to [replicate](https://docs.victoriametrics.com/victoriametrics/vmagent/#replication-and-high-availability) or [shard](https://docs.victoriametrics.com/victoriametrics/vmagent/#sharding-among-remote-storages)
data stream. If AZ is temporarily unavailable, `vmagent` [buffers](https://docs.victoriametrics.com/victoriametrics/vmagent/#on-disk-persistence)
its data on-disk (see `--remoteWrite.maxDiskUsagePerURL`) without affecting other destinations. The buffered data is sent to AZ as soon as it becomes available.

See the [cluster instability troubleshooting guide](https://docs.victoriametrics.com/victoriametrics/troubleshooting/#cluster-instability) for details on diagnosing and mitigating networking problems.

### vmstorage groups at vmselect

`vmselect` can be configured to query multiple distinct groups of `vmstorage` nodes with individual `-replicationFactor` per each group.
The following format for `-storageNode` command-line flag value should be used for assigning a particular `addr` of `vmstorage` to a particular `groupName` -
`-storageNode=groupName/addr`. The `groupName` can contain arbitrary value. The only rule is that every `vmstorage` group must have an unique name.

For example, the following command runs `vmselect`, which continues returning full responses if up to one node per each group is temporarily unavailable
because the given `-replicationFactor=2` is applied individually per each group:

```bash
/path/to/vmselect \
 -replicationFactor=2 \
 -storageNode=g1/host1,g1/host2,g1/host3 \
 -storageNode=g2/host4,g2/host5,g2/host6 \
 -storageNode=g3/host7,g3/host8,g3/host9
```

It is possible specifying distinct `-replicationFactor` per each group via the following format - `-replicationFactor=groupName:rf`.
For example, the following command runs `vmselect`, which uses `-replicationFactor=3` for the group `g1`, `-replicationFactor=2` for the group `g2`
and `-replicationFactor=1` for the group `g3`:

```bash
/path/to/vmselect \
 -replicationFactor=g1:3 \
 -storageNode=g1/host1,g1/host2,g1/host3 \
 -replicationFactor=g2:2 \
 -storageNode=g2/host4,g2/host5,g2/host6 \
 -replicationFactor=g3:1 \
 -storageNode=g3/host4,g3/host5,g3/host6
```

If every ingested sample is replicated across multiple `vmstorage` groups, then pass `-globalReplicationFactor=N` command-line flag to `vmselect`,
so it could continue returning full responses if up to `N-1` `vmstorage` groups are temporarily unavailable.
For example, the following command runs `vmselect`, which continues returning full responses if any number of `vmstorage` nodes
in a single `vmstorage` group are temporarily unavailable:

```bash
/path/to/vmselect \
 -globalReplicationFactor=2 \
 -storageNode=g1/host1,g1/host2,g1/host3 \
 -storageNode=g2/host4,g2/host5,g2/host6 \
 -storageNode=g3/host7,g3/host8,g3/host9
```

It is OK to mix `-replicationFactor` and `-globalReplicationFactor`. For example, the following command runs `vmselect`, which continues returning full responses
if any number of `vmstorage` nodes in a single `vmstorage` group are temporarily unavailable and the remaining groups contain up to two unavailable `vmstorage` node:

```bash
/path/to/vmselect \
 -globalReplicationFactor=2 \
 -replicationFactor=3 \
 -storageNode=g1/host1,g1/host2,g1/host3 \
 -storageNode=g2/host4,g2/host5,g2/host6 \
 -storageNode=g3/host7,g3/host8,g3/host9
```

See also [multi-level cluster setup](#multi-level-cluster-setup).

### Automatic vmstorage discovery

`vminsert` and `vmselect` components in [enterprise version of VictoriaMetrics](https://docs.victoriametrics.com/victoriametrics/enterprise/) support
the following approaches for automatic discovery of `vmstorage` nodes:

- file-based discovery - put the list of `vmstorage` nodes into a file - one node address per each line - and then pass `-storageNode=file:/path/to/file-with-vmstorage-list`
  to `vminsert` and `vmselect`. It is possible to read the list of vmstorage nodes from http or https urls.
  For example, `-storageNode=file:http://some-host/vmstorage-list` would read the list of storage nodes
  from `http://some-host/vmstorage-list`.
  The list of discovered `vmstorage` nodes is automatically updated when the file contents changes.
  The update frequency can be controlled with `-storageNode.discoveryInterval` command-line flag.

- [DNS SRV](https://en.wikipedia.org/wiki/SRV_record) - pass `srv+some-name` value to `-storageNode` command-line flag.
  In this case the provided `some-name` is resolved into tcp addresses of `vmstorage` nodes.
  The list of discovered `vmstorage` nodes is automatically updated at `vminsert` and `vmselect`
  when it changes behind the `some-name` DNS SRV record.
  The update frequency can be controlled with `-storageNode.discoveryInterval` command-line flag.

It is possible passing multiple `file` and DNS SRV names to `-storageNode` command-line flag. In this case all these names
are resolved to tcp addresses of `vmstorage` nodes to connect to.
For example, `-storageNode=file:/path/to/local-vmstorage-list -storageNode='srv+vmstorage-hot' -storageNode='srv+vmstorage-cold'`.

It is OK to pass regular static `vmstorage` addresses together with `file` and DNS SRV addresses at `-storageNode`. For example,
`-storageNode=vmstorage1,vmstorage2 -storageNode='srv+vmstorage-autodiscovery'`.

The discovered addresses can be filtered with optional `-storageNode.filter` command-line flag, which can contain arbitrary regular expression filter.
For example, `-storageNode.filter='^[^:]+:8400$'` would leave discovered addresses ending with `8400` port only, e.g. the default port used
for sending data from `vminsert` to `vmstorage` node according to `-vminsertAddr` command-line flag.

The currently discovered `vmstorage` nodes can be [monitored](#monitoring) with `vm_rpc_vmstorage_is_reachable` and `vm_rpc_vmstorage_is_read_only` metrics.

Discovery mechanism could be also used together with [vmstorage group](#vmstorage-groups-at-vmselect). Consider the following example:

```bash
/path/to/vmselect \
  -globalReplicationFactor=2 \
  -storageNode=g1/file:/path/to/file-with-vmstorage-list/ \      # Group g1: static list from file
  -storageNode=g2/srv+vmstorage-autodiscovery \                  # Group g2: nodes discovered dynamically via SRV records
  -storageNode=g3/host7,g3/host8,g3/host9                        # Group g3: statically defined hostnames
```

Each `-storageNode` parameter assigns one or more storage nodes to a specific group (e.g., `g1`, `g2`, `g3`).
The automatically discovered nodes retain the [vmstorage group](#vmstorage-groups-at-vmselect) prefix to maintain consistent group mapping.

### Reading from single-node VictoriaMetrics

For executing queries, `vmselect` node is configured with `-storageNode=<vmstorage_host1>,<vmstorage_host2>...` command-line flag, listing all `vmstorage` nodes to query. VictoriaMetrics single-node can be queried by `vmselect` too {{% available_from "v1.147.0" %}}. This makes possible the following use cases:
1. Querying data from single-node and cluster installations at the same time.
2. Querying data from multiple single-nodes at the same time.

By default, the single-node VictoriaMetrics can't be queried by `vmselect`. Enable this functionality by configuring the `-vmselectAddr` command-line flag for single-node VictoriaMetrics. It will start the `vmselect RPC server` that accepts requests and serves responses in the cluster format.

Cluster format assumes [multitenancy](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/#multitenancy), and single-node VictoriaMetrics [does not support multitenancy](https://docs.victoriametrics.com/victoriametrics/#multi-tenancy). But with `-vmselectAddr` enabled, single-node VictoriaMetrics assumes all the data it stores belongs to `"0:0"` tenant. This default tenant can be changed by specifying extra `-accountID` and `-projectID` command-line flags for single-node VictoriaMetrics.

For example, the following command will start a single-node that listens for `vmselect` RPC requests on the `8401` port. The requests must be either `/multitenant/` (i.e., [read data from all tenants](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/#multitenant-reads)) or for `"12:34"` tenant. Otherwise, the single-node will return an empty result:
```sh
./victoria-metrics-single-node -storageDataPath=/data -vmselectAddr=:8401 -accountID=12 -projectID=34
```

> The `tenantID` configuration is not persisted in any way and is enforced only at runtime. Thus, it is safe to change the `-accountID` and `-projectID` flag values at any time.

To make the `vmselect` node query data from a single-node and `vmstorage` nodes at the same time, simply list their addresses in the `-storageNode` command-line flag:
```sh
/path/to/vmselect \
 -storageNode=<single-node-host:8401> \
 -storageNode=<vmstorage-1:8401>  \
 -storageNode=<vmstorage-2:8401> 
```

You can configure `vmselect` to read from as many single-nodes and `vmstorage` nodes as you want. `vmselect` will treat such single-nodes as regular `vmstorage` nodes, apply  [deduplication](https://docs.victoriametrics.com/Cluster-VictoriaMetrics/#deduplication), cache results, etc.
