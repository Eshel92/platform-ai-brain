<!-- Part 4 of 4 of cluster/nodes-stats.md (split because the page is big). -->

#### Examples

```console
# return just indices
GET /_nodes/stats/indices

# return just os and process
GET /_nodes/stats/os,process

# return just process for node with IP address 10.0.0.1
GET /_nodes/10.0.0.1/stats/process
```

All stats can be explicitly requested via `/_nodes/stats/_all` or
`/_nodes/stats?metric=_all`.

You can get information about indices stats on `node`, `indices`, or `shards`
level.

```console
# Fielddata summarized by node
GET /_nodes/stats/indices/fielddata?fields=field1,field2

# Fielddata summarized by node and index
GET /_nodes/stats/indices/fielddata?level=indices&fields=field1,field2

# Fielddata summarized by node, index, and shard
GET /_nodes/stats/indices/fielddata?level=shards&fields=field1,field2

# You can use wildcards for field names
GET /_nodes/stats/indices/fielddata?fields=field*
```

You can get statistics about search groups for searches executed on this node.

```console
# All groups with all stats
GET /_nodes/stats?groups=_all

# Some groups from just the indices stats
GET /_nodes/stats/indices?groups=foo,bar
```

##### Retrieve ingest statistics only

To return only ingest-related node statistics, set the `<metric>` path parameter to `ingest` and use the
`filter_path` query parameter.

```console
GET /_nodes/stats/ingest?filter_path=nodes.*.ingest
```

You can use the `metric` and `filter_path` query parameters to get the same response.

```console
GET /_nodes/stats?metric=ingest&filter_path=nodes.*.ingest
```

To further refine the response, change the `filter_path` value.
For example, the following request only returns ingest pipeline statistics.

```console
GET /_nodes/stats?metric=ingest&filter_path=nodes.*.ingest.pipelines
```
