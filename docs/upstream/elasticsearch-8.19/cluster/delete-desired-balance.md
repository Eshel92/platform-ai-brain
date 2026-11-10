<!-- Converted from cluster/delete-desired-balance.asciidoc (AsciiDoc). Includes are inlined. -->

### Reset desired balance API

**Note:** {cloud-only}

**New API reference**
For the most up-to-date API details, refer to [Cluster APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-cluster).

Discards the current desired balance and computes a new desired balance starting from the current allocation of shards.
This can sometimes help Elasticsearch find a desired balance which needs fewer shard movements to achieve, especially if the
cluster has experienced changes so substantial that the current desired balance is no longer optimal without Elasticsearch having
detected that the current desired balance will take more shard movements to achieve than needed. However, this API
imposes a heavy load on the elected master node and may not always have the expected effect. Calling this API should
never be necessary. Consider instead <<shards-rebalancing-heuristics,increasing the value of
`cluster.routing.allocation.balance.threshold`>> to avoid excessive shard movements.

#### Request

```console
DELETE /_internal/desired_balance
```
