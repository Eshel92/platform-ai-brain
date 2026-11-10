<!-- Converted from cluster/health.asciidoc (AsciiDoc). Includes are inlined. -->

### Cluster health API

**New API reference**
For the most up-to-date API details, refer to [Cluster APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-cluster).

Returns the health status of a cluster.

#### Request

`GET /_cluster/health/<target>`

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the `monitor` or
`manage` cluster privilege to use this API.

#### Description

The cluster health API returns a simple status on the health of the
cluster. You can also use the API to get the health status of only specified
data streams and indices. For data streams, the API retrieves the health status
of the stream's backing indices.

The cluster health status is: `green`, `yellow` or `red`. On the shard level, a
`red` status indicates that the specific shard is not allocated in the cluster,
`yellow` means that the primary shard is allocated but replicas are not, and
`green` means that all shards are allocated. The index level status is
controlled by the worst shard status. The cluster status is controlled by the
worst index status.

One of the main benefits of the API is the ability to wait until the cluster
reaches a certain high water-mark health level. For example, the following will
wait for 50 seconds for the cluster to reach the `yellow` level (if it reaches
the `green` or `yellow` status before 50 seconds elapse, it will return at that
point):

```console
GET /_cluster/health?wait_for_status=yellow&timeout=50s
```

#### Path parameters

`<target>`::
(Optional, string)
Comma-separated list of data streams, indices, and index aliases used to limit
the request. Wildcard expressions (`*`) are supported.
To target all data streams and indices in a cluster, omit this parameter or use
`_all` or `*`.

#### Query parameters

`level`::
    (Optional, string) Can be one of `cluster`, `indices` or `shards`. Controls
    the details level of the health information returned. Defaults to `cluster`.

`local`::
(Optional, Boolean) If `true`, the request retrieves information from the local
node only. Defaults to `false`, which means information is retrieved from
the master node.
`master_timeout`::
(Optional, time units)
Period to wait for the master node. If the master node is not available before
the timeout expires, the request fails and returns an error. Defaults to `30s`.
Can also be set to `-1` to indicate that the request should never timeout.

`timeout`::
(Optional, time units) Period to wait for a response from all relevant nodes in the cluster after updating the cluster metadata.
If no response is received before the timeout expires, the cluster metadata update still applies but the response will indicate that it was not completely acknowledged.
Defaults to `30s`.
Can also be set to `-1` to indicate that the request should never timeout.
`wait_for_active_shards`::
    (Optional, string) A number controlling to how many active shards to wait
    for, `all` to wait for all shards in the cluster to be active, or `0` to not
    wait. Defaults to `0`.

`wait_for_events`::
    (Optional, string) Can be one of `immediate`, `urgent`, `high`, `normal`,
    `low`, `languid`. Wait until all currently queued events with the given
    priority are processed.

`wait_for_no_initializing_shards`::
    (Optional, Boolean) A boolean value which controls whether to wait (until
    the timeout provided) for the cluster to have no shard initializations.
    Defaults to false, which means it will not wait for initializing shards.

`wait_for_no_relocating_shards`::
    (Optional, Boolean) A boolean value which controls whether to wait (until
    the timeout provided) for the cluster to have no shard relocations. Defaults
    to false, which means it will not wait for relocating shards.

`wait_for_nodes`::
    (Optional, string) The request waits until the specified number `N` of
    nodes is available. It also accepts `>=N`, `<=N`, `>N` and `<N`.
    Alternatively, it is possible to use `ge(N)`, `le(N)`, `gt(N)` and
    `lt(N)` notation.

`wait_for_status`::
    (Optional, string) One of `green`, `yellow` or `red`. Will wait (until the
    timeout provided) until the status of the cluster changes to the one
    provided or better, i.e. `green` > `yellow` > `red`. By default, will not
    wait for any status.

#### Response body

`cluster_name`::
    (string) The name of the cluster.

`status`::
(string)
Health status of the cluster, based on the state of its primary and replica
shards. Statuses are:

  * `green`:
    All shards are assigned.

  * `yellow`:
    All primary shards are assigned, but one or more replica shards are
    unassigned. If a node in the cluster fails, some data could be unavailable
    until that node is repaired.

  * `red`:
    One or more primary shards are unassigned, so some data is unavailable. This
    can occur briefly during cluster startup as primary shards are assigned.
`timed_out`::
    (Boolean) If `false` the response returned within the period of
    time that is specified by the `timeout` parameter (`30s` by default).

`number_of_nodes`::
    (integer) The number of nodes within the cluster.

`number_of_data_nodes`::
    (integer) The number of nodes that are dedicated data nodes.

`active_primary_shards`::
    (integer) The number of active primary shards.

`active_shards`::
    (integer) The total number of active primary and replica shards.

`relocating_shards`::
    (integer) The number of shards that are under relocation.

`initializing_shards`::
    (integer) The number of shards that are under initialization.

`unassigned_shards`::
    (integer) The number of shards that are not allocated.

`unassigned_primary_shards`::
    (integer) The number of shards that are primary but not allocated. **Note**: This number may be lower than the true value if your cluster contains nodes running a version below 8.16. For a more accurate count in this scenario, please use the cluster health API.

`delayed_unassigned_shards`::
    (integer) The number of shards whose allocation has been delayed by the
    timeout settings.

`number_of_pending_tasks`::
    (integer) The number of cluster-level changes that have not yet been
    executed.

`number_of_in_flight_fetch`::
    (integer) The number of unfinished fetches.

`task_max_waiting_in_queue_millis`::
    (integer) The time expressed in milliseconds since the earliest initiated task
    is waiting for being performed.

`active_shards_percent_as_number`::
    (float) The ratio of active shards in the cluster expressed as a percentage.

#### Examples

```console
GET _cluster/health
```

The API returns the following response in case of a quiet single node cluster
with a single index with one shard and one replica:

```console-result
{
  "cluster_name" : "testcluster",
  "status" : "yellow",
  "timed_out" : false,
  "number_of_nodes" : 1,
  "number_of_data_nodes" : 1,
  "active_primary_shards" : 1,
  "active_shards" : 1,
  "relocating_shards" : 0,
  "initializing_shards" : 0,
  "unassigned_shards" : 1,
  "unassigned_primary_shards" : 0,
  "delayed_unassigned_shards": 0,
  "number_of_pending_tasks" : 0,
  "number_of_in_flight_fetch": 0,
  "task_max_waiting_in_queue_millis": 0,
  "active_shards_percent_as_number": 50.0
}
```

The following is an example of getting the cluster health at the
`shards` level:

```console
GET /_cluster/health/my-index-000001?level=shards
```
