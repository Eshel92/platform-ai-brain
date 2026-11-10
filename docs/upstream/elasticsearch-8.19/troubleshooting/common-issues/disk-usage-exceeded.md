<!-- Converted from troubleshooting/common-issues/disk-usage-exceeded.asciidoc (AsciiDoc). Includes are inlined. -->

### Fix watermark errors

When a data node is critically low on disk space and has reached the
flood-stage disk usage watermark, the following
error is logged: `Error: disk usage exceeded flood-stage watermark, index has read-only-allow-delete block`. 

To prevent a full disk, when a node reaches this watermark, Elasticsearch blocks writes
to any index with a shard on the node. If the block affects related system
indices, Kibana and other Elastic Stack features may become unavailable. For example, 
this could induce Kibana's `Kibana Server is not Ready yet` 
[error message](https://www.elastic.co/guide/en/kibana/8.19/access.html#not-ready). 

Elasticsearch will automatically remove the write block when the affected node's disk
usage falls below the high disk watermark. 
To achieve this, Elasticsearch attempts to rebalance some of the affected node's shards 
to other nodes in the same data tier.

****
If you're using Elastic Cloud Hosted, then you can use AutoOps to monitor your cluster. AutoOps significantly simplifies cluster management with performance recommendations, resource utilization visibility, real-time issue detection and resolution paths. For more information, refer to [Monitor with AutoOps](https://www.elastic.co/guide/en/cloud/current/ec-autoops.html).
****

#### Monitor rebalancing

To verify that shards are moving off the affected node until it falls below high 
watermark., use the cat shards API and cat recovery API: 

```console
GET _cat/shards?v=true

GET _cat/recovery?v=true&active_only=true
```

If shards remain on the node keeping it about high watermark, use the 
cluster allocation explanation API to get an 
explanation for their allocation status.

```console
GET _cluster/allocation/explain
{
  "index": "my-index",
  "shard": 0,
  "primary": false
}
```

#### Temporary Relief

To immediately restore write operations, you can temporarily increase 
disk watermarks and remove the 
write block.

```console
PUT _cluster/settings
{
  "persistent": {
    "cluster.routing.allocation.disk.watermark.low": "90%",
    "cluster.routing.allocation.disk.watermark.low.max_headroom": "100GB",
    "cluster.routing.allocation.disk.watermark.high": "95%",
    "cluster.routing.allocation.disk.watermark.high.max_headroom": "20GB",
    "cluster.routing.allocation.disk.watermark.flood_stage": "97%",
    "cluster.routing.allocation.disk.watermark.flood_stage.max_headroom": "5GB",
    "cluster.routing.allocation.disk.watermark.flood_stage.frozen": "97%",
    "cluster.routing.allocation.disk.watermark.flood_stage.frozen.max_headroom": "5GB"
  }
}

PUT */_settings?expand_wildcards=all
{
  "index.blocks.read_only_allow_delete": null
}
```

When a long-term solution is in place, to reset or reconfigure the disk watermarks:

```console
PUT _cluster/settings
{
  "persistent": {
    "cluster.routing.allocation.disk.watermark.low": null,
    "cluster.routing.allocation.disk.watermark.low.max_headroom": null,
    "cluster.routing.allocation.disk.watermark.high": null,
    "cluster.routing.allocation.disk.watermark.high.max_headroom": null,
    "cluster.routing.allocation.disk.watermark.flood_stage": null,
    "cluster.routing.allocation.disk.watermark.flood_stage.max_headroom": null,
    "cluster.routing.allocation.disk.watermark.flood_stage.frozen": null,
    "cluster.routing.allocation.disk.watermark.flood_stage.frozen.max_headroom": null
  }
}
```

#### Resolve

To resolve watermark errors permanently, perform one of the following actions:

* Horizontally scale nodes of the affected data tiers.

* Vertically scale existing nodes to increase disk space.

* Delete indices using the delete index API, either
permanently if the index isn't needed, or temporarily to later 
restore.

* update related ILM policy to push indices 
through to later data tiers

**Tip:** On Elasticsearch Service and Elastic Cloud Enterprise, indices may need to be temporarily deleted via
its {cloud}/ec-api-console.html[Elasticsearch API Console] to later
snapshot restore in order to resolve
cluster health `status:red` which will block
{cloud}/ec-activity-page.html[attempted changes]. If you experience issues
with this resolution flow on Elasticsearch Service, kindly reach out to
[Elastic Support](https://support.elastic.co) for assistance.

### Prevent watermark errors

To avoid watermark errors in future, perform one of the following actions:

* If you're using Elasticsearch Service, Elastic Cloud Enterprise, or Elastic Cloud on Kubernetes: Enable autoscaling.

* Set up [stack monitoring alerts](https://www.elastic.co/guide/en/kibana/8.19/kibana-alerts.html) on top of
Elasticsearch monitoring to be notified before
the flood-stage watermark is reached.
