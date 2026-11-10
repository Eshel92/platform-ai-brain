---
mapped_pages:
  - https://www.elastic.co/guide/en/elasticsearch/reference/current/allocation-total-shards.html
applies_to:
  stack: all
---

# Total shards per node [allocation-total-shards]

::::{admonition} Settings supported in Serverless
Elastic Cloud Serverless projects [restrict the available Elasticsearch settings](docs-content://deploy-manage/deploy/elastic-cloud/differences-from-other-elasticsearch-offerings.md#elasticsearch-differences-serverless-settings-availability) to a supported subset, identified with a `Serverless` badge next to the setting name. For a complete list of available index settings, refer to the [Serverless index settings list](/reference/elasticsearch/index-settings/serverless.md).
::::
The cluster-level shard allocator tries to spread the shards of a single index across as many nodes as possible. However, depending on how many shards and indices you have, and how big they are, it may not always be possible to spread shards evenly.

The following *dynamic* setting allows you to specify a hard limit on the total number of shards from a single index allowed per node:

$$$total-shards-per-node$$$

`index.routing.allocation.total_shards_per_node`
:   The maximum number of shards (replicas and primaries) that will be allocated to a single node. Defaults to unbounded.

With the following cluster level setting, you can also limit the amount of shards a node can have regardless of the index. This setting applies across all indices on a node and can be set at runtime using the [update cluster settings](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-cluster-put-settings) API:

$$$cluster-total-shards-per-node$$$

`cluster.routing.allocation.total_shards_per_node`
:   ([Dynamic](docs-content://deploy-manage/stack-settings.md#dynamic-cluster-setting)) Maximum number of primary and replica shards allocated to each node. Defaults to `-1` (unlimited).

Elasticsearch checks this setting during shard allocation. For example, a cluster has a `cluster.routing.allocation.total_shards_per_node` setting of `100` and three nodes with the following shard allocations:

* Node A: 100 shards
* Node B: 98 shards
* Node C: 1 shard

If node C fails, Elasticsearch reallocates its shard to node B. Reallocating the shard to node A would exceed node A’s shard limit.


::::{warning}
These settings impose a hard limit which can result in some shards not being allocated.

Use with caution.

::::


