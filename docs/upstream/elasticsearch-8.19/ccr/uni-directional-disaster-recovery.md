<!-- Converted from ccr/uni-directional-disaster-recovery.asciidoc (AsciiDoc). Includes are inlined. -->

### Tutorial: Disaster recovery based on uni-directional cross-cluster replication

Learn how to failover and failback between two clusters based on uni-directional cross-cluster replication. You can also visit ccr-disaster-recovery-bi-directional-tutorial to set up replicating data streams that automatically failover and failback without human intervention.

* Setting up uni-directional cross-cluster replication replicated from `clusterA`
to `clusterB`.
* Failover - If `clusterA` goes offline, `clusterB` needs to "promote" follower
indices to regular indices to allow write operations. All ingestion will need to
be redirected to `clusterB`, this is controlled by the clients (Logstash, Beats,
{agents}, etc). 
* Failback - When `clusterA` is back online, it assumes the role of a follower
and replicates the leader indices from `clusterB`.

(Figure: images/ccr-uni-directional-disaster-recovery.png)

**Note:** Cross-cluster replication provides functionality to replicate user-generated indices only.
Cross-cluster replication isn't designed for replicating system-generated indices or snapshot
settings, and can't replicate ILM or SLM policies across clusters.
Learn more in cross-cluster replication limitations.

#### Prerequisites

Before completing this tutorial,
set up cross-cluster replication to connect two 
clusters and configure a follower index. 

In this tutorial, `kibana_sample_data_ecommerce` is replicated from `clusterA` to `clusterB`.

```console
### On clusterB ###
PUT _cluster/settings
{
  "persistent": {
    "cluster": {
      "remote": {
        "clusterA": {
          "mode": "proxy",
          "skip_unavailable": "true",
          "server_name": "clustera.es.region-a.gcp.elastic-cloud.com",
          "proxy_socket_connections": "18",
          "proxy_address": "clustera.es.region-a.gcp.elastic-cloud.com:9400"
        }
      }
    }
  }
}
```

```console
### On clusterB ###
PUT /kibana_sample_data_ecommerce2/_ccr/follow?wait_for_active_shards=1
{
  "remote_cluster": "clusterA",
  "leader_index": "kibana_sample_data_ecommerce"
}
```

**Important:** Writes (such as ingestion or updates) should occur only on the leader
index. Follower indices are read-only and will reject any writes.

#### Failover when `clusterA` is down

. Promote the follower indices in `clusterB` into regular indices so 
that they accept writes. This can be achieved by:
* First, pause indexing following for the follower index.
* Next, close the follower index.
* Unfollow the leader index.
* Finally, open the follower index (which at this point is a regular index).

```console
### On clusterB ###
POST /kibana_sample_data_ecommerce2/_ccr/pause_follow
POST /kibana_sample_data_ecommerce2/_close           
POST /kibana_sample_data_ecommerce2/_ccr/unfollow    
POST /kibana_sample_data_ecommerce2/_open
```

. On the client side (Logstash, Beats, Elastic Agent), manually re-enable ingestion of
`kibana_sample_data_ecommerce2` and redirect traffic to the `clusterB`. You should
also redirect all search traffic to the `clusterB` cluster during
this time. You can simulate this by ingesting documents into this index. You should
notice this index is now writable.
```console
### On clusterB ###
POST kibana_sample_data_ecommerce2/_doc/
{
  "user": "kimchy"
}
```

#### Failback when `clusterA` comes back

When `clusterA` comes back, `clusterB` becomes the new leader and `clusterA` becomes the follower. 

. Set up remote cluster `clusterB` on `clusterA`.
```console
### On clusterA ###
PUT _cluster/settings
{
  "persistent": {
    "cluster": {
      "remote": {
        "clusterB": {
          "mode": "proxy",
          "skip_unavailable": "true",
          "server_name": "clusterb.es.region-b.gcp.elastic-cloud.com",
          "proxy_socket_connections": "18",
          "proxy_address": "clusterb.es.region-b.gcp.elastic-cloud.com:9400"
        }
      }
    }
  }
}
```

. Existing data needs to be discarded before you can turn any index into a
follower. Ensure the most up-to-date data is available on `clusterB` prior to
deleting any indices on `clusterA`.  
```console
### On clusterA ###
DELETE kibana_sample_data_ecommerce
```

. Create a follower index on `clusterA`, now following the leader index in
`clusterB`.  
```console
### On clusterA ###
PUT /kibana_sample_data_ecommerce/_ccr/follow?wait_for_active_shards=1
{ 
  "remote_cluster": "clusterB", 
  "leader_index": "kibana_sample_data_ecommerce2" 
}
```

. The index on the follower cluster now contains the updated documents.
```console
### On clusterA ###
GET kibana_sample_data_ecommerce/_search?q=kimchy
```
**Tip:** If a soft delete is merged away before it can be replicated to a follower the following process will fail due to incomplete history on the leader, see index.soft_deletes.retention_lease.period for more details.
