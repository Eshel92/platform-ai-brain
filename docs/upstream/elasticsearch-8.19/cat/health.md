<!-- Converted from cat/health.asciidoc (AsciiDoc). Includes are inlined. -->

### cat health API

**New API reference**
For the most up-to-date API details, refer to [Compact and aligned text (CAT) APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-cat)..

**Important:**
cat APIs are only intended for human consumption using the command line or Kibana
console. They are _not_ intended for use by applications. For application
consumption, use the cluster health API.

Returns the health status of a cluster, similar to the <<cluster-health,cluster
health>> API.

#### Request

`GET /_cat/health`

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the `monitor` or
`manage` cluster privilege to use this API.

#### Description

You can use the cat health API to get the health status of a cluster.

This API is often used to check malfunctioning clusters. To help you
track cluster health alongside log files and alerting systems, the API returns
timestamps in two formats:

* `HH:MM:SS`, which is human-readable but includes no date information.
* [Unix `epoch` time](https://en.wikipedia.org/wiki/Unix_time), which is
machine-sortable and includes date information. This is useful for cluster
recoveries that take multiple days.

You can use the cat health API to verify cluster health across multiple nodes.
See cat-health-api-example-across-nodes.

You also can use the API to track the recovery of a large cluster
over a longer period of time. See cat-health-api-example-large-cluster.

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
`s`::
(Optional, string) Comma-separated list of column names or column aliases used
to sort the response.
`time`::
(Optional, time units)
Unit used to display time values.
`ts` (timestamps)::
(Optional, Boolean) If `true`, returns `HH:MM:SS` and
[Unix `epoch`](https://en.wikipedia.org/wiki/Unix_time) timestamps. Defaults to
`true`.

`v`::
(Optional, Boolean) If `true`, the response includes column headings.
Defaults to `false`.

#### Examples

##### Example with a timestamp

By default, the cat health API returns `HH:MM:SS` and
[Unix `epoch`](https://en.wikipedia.org/wiki/Unix_time) timestamps. For example:

```console
GET /_cat/health?v=true
```

The API returns the following response:

```txt
epoch      timestamp cluster       status node.total node.data shards pri relo init unassign unassign.pri pending_tasks max_task_wait_time active_shards_percent
1475871424 16:17:04  elasticsearch green           1         1      1   1    0    0        0            0             0                  -                100.0%
```

##### Example without a timestamp

You can use the `ts` (timestamps) parameter to disable timestamps. For example:

```console
GET /_cat/health?v=true&ts=false
```

The API returns the following response:

```txt
cluster       status node.total node.data shards pri relo init unassign unassign.pri pending_tasks max_task_wait_time active_shards_percent
elasticsearch green           1         1      1   1    0    0        0            0             0                  -                100.0%
```

**Note**: The reported number of unassigned primary shards may be lower than the true value if your cluster contains nodes running a version below 8.16. For a more accurate count in this scenario, please use the cluster health API.

##### Example across nodes

You can use the cat health API to verify the health of a cluster across nodes.
For example:

```sh
% pssh -i -h list.of.cluster.hosts curl -s localhost:9200/_cat/health
[1] 20:20:52 [SUCCESS] es3.vm
1384309218 18:20:18 foo green 3 3 3 3 0 0 0 0 0
[2] 20:20:52 [SUCCESS] es1.vm
1384309218 18:20:18 foo green 3 3 3 3 0 0 0 0 0
[3] 20:20:52 [SUCCESS] es2.vm
1384309218 18:20:18 foo green 3 3 3 3 0 0 0 0 0
```

##### Example with a large cluster

You can use the cat health API to track the recovery of a large cluster over a
longer period of time. You can do this by including the cat health API request
in a delayed loop. For example:

```sh
% while true; do curl localhost:9200/_cat/health; sleep 120; done
1384309446 18:24:06 foo red 3 3 20 20 0 0 1812 1121 0
1384309566 18:26:06 foo yellow 3 3 950 916 0 12 870 421 0
1384309686 18:28:06 foo yellow 3 3 1328 916 0 12 492 301 0
1384309806 18:30:06 foo green 3 3 1832 916 4 0 0 0
^C
```

In this example, the recovery took roughly six minutes, from `18:24:06` to
`18:30:06`. If this recovery took hours, you could continue to monitor the
number of `UNASSIGNED` shards, which should drop. If the number of `UNASSIGNED`
shards remains static, it would indicate an issue with the cluster recovery.
