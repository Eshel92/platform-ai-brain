<!-- Part 3 of 8 of victoriametrics/Cluster-VictoriaMetrics.md (split because the page is big). -->

## High availability

The database is considered highly available if it continues accepting new data and processing incoming queries when some of its components are temporarily unavailable.
VictoriaMetrics cluster is highly available according to this definition - see [cluster availability docs](#cluster-availability).

It is recommended to run all the components for a single cluster in the same subnetwork with high bandwidth, low latency and low error rates.
This improves cluster performance and availability. It isn't recommended spreading components for a single cluster
across multiple availability zones, since cross-AZ network usually has lower bandwidth, higher latency and higher
error rates comparing the network inside a single AZ.

If you need multi-AZ setup, then it is recommended running independent clusters in each AZ and setting up
[vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/) in front of these clusters, so it could replicate incoming data
into all the cluster - see [these docs](https://docs.victoriametrics.com/victoriametrics/vmagent/#multitenancy) for details.
Then an additional `vmselect` nodes can be configured for reading the data from multiple clusters according to [these docs](#multi-level-cluster-setup).
If one cluster misses samples that are available in another, see [how to recover missing metrics](https://docs.victoriametrics.com/guides/recovering-missing-metrics/).

See [VMDistributed](https://docs.victoriametrics.com/operator/resources/vmdistributed/) Kubernetes operator resource for an example.


## Replication and data safety

By default, VictoriaMetrics offloads replication to the underlying storage pointed by `-storageDataPath` such as [Google compute persistent disk](https://cloud.google.com/compute/docs/disks#pdspecs),
which guarantees data durability. VictoriaMetrics supports application-level replication if replicated durable persistent disks cannot be used for some reason.

The replication can be enabled by passing `-replicationFactor=N` command-line flag to `vminsert`. This instructs `vminsert` to store `N` copies for every ingested sample
on `N` distinct `vmstorage` nodes. This guarantees that all the stored data remains available for querying if up to `N-1` `vmstorage` nodes are unavailable. See [how `vminsert` replicates each sample to `N` `vmstorage` nodes](https://victoriametrics.com/blog/vminsert-how-it-works/#4-replication-and-sending-data-to-vmstorage) for details.

Passing `-replicationFactor=N` command-line flag to `vmselect` instructs it to not mark responses as `partial` if less than `-replicationFactor` vmstorage nodes are unavailable during the query.
See [cluster availability docs](#cluster-availability) for details.

The cluster must contain at least `2*N-1` `vmstorage` nodes, where `N` is replication factor, in order to maintain the given replication factor
for newly ingested data when `N-1` of storage nodes are unavailable.

VictoriaMetrics stores timestamps with millisecond precision, so `-dedup.minScrapeInterval=1ms` command-line flag must be passed to `vmselect` nodes when the replication is enabled,
so they could de-duplicate replicated samples obtained from distinct `vmstorage` nodes during querying. If duplicate data is pushed to VictoriaMetrics
from identically configured [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/) instances or Prometheus instances, then the `-dedup.minScrapeInterval` must be set
to `scrape_interval` from scrape configs according to [deduplication docs](#deduplication).

Note that [replication doesn't save from disaster](https://medium.com/@valyala/speeding-up-backups-for-big-time-series-databases-533c1a927883),
so it is recommended performing regular backups. See [these docs](#backups) for details.

Note that the replication increases resource usage - CPU, RAM, disk space, network bandwidth - by up to `-replicationFactor=N` times, because `vminsert` stores `N` copies
of incoming data to distinct `vmstorage` nodes and `vmselect` needs to de-duplicate the replicated data obtained from `vmstorage` nodes during querying.
So it is more cost-effective to offload the replication to underlying replicated durable storage pointed by `-storageDataPath`
such as [Google Compute Engine persistent disk](https://cloud.google.com/compute/docs/disks/#pdspecs), which is protected from data loss and data corruption.
It also provides consistently high performance and [may be resized](https://cloud.google.com/compute/docs/disks/add-persistent-disk) without downtime.
HDD-based persistent disks should be enough for the majority of use cases. It is recommended using durable replicated persistent volumes in Kubernetes.


## Cluster resizing and scalability

Make sure you read [capacity planning docs](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/#capacity-planning) first.

### Scaling up

Cluster performance and capacity can be scaled up in two ways:

- By adding more resources (CPU, RAM, disk IO, disk space, network bandwidth) to existing nodes in the cluster (aka vertical scalability).
- By adding more nodes to the cluster (aka horizontal scalability).

> [!NOTE] Warning
> All VictoriaMetrics components read the available CPU and memory limits only once at startup. They use these values to size caches, buffers and concurrency limits.
> Without a restart, a component doesn't use the added resources after a scale-up,
> and it may be killed by the OOM killer after the memory limit is decreased.
> Self-monitoring metrics such as `vm_available_memory_bytes` and `vm_available_cpu_cores` also keep reporting the limits read at startup.
> So we do not recommend using in-place vertical scaling without restarts (such as Kubernetes VPA in [InPlaceOrRecreate](https://kubernetes.io/docs/concepts/workloads/autoscaling/vertical-pod-autoscale/#updateMode-InPlaceOrRecreate) mode).
> Make sure components are restarted after their CPU or memory limits are changed.

General recommendations for cluster scalability:

- Adding more CPU and RAM to existing `vmselect` nodes improves the performance for heavy queries, which process big number of time series with big number of raw samples.
  See [this article on how to detect and optimize heavy queries](https://valyala.medium.com/how-to-optimize-promql-and-metricsql-queries-85a1b75bf986).

- Adding more `vmselect` nodes increases the maximum possible queries rate, since the incoming concurrent requests may be split among bigger number of `vmselect` nodes.

- Adding more `vminsert` nodes increases the maximum possible data ingestion speed, since the ingested data may be split among bigger number of `vminsert` nodes.

- Adding more CPU and RAM to existing `vmstorage` nodes (aka vertical scaling) increases the number
  of [active time series](https://docs.victoriametrics.com/victoriametrics/faq/#what-is-an-active-time-series) the cluster can handle. This also increases query performance over time series with [high churn rate](https://docs.victoriametrics.com/victoriametrics/faq/#what-is-high-churn-rate). Scaling vertically is a preferred way to scale cluster if you already have big number of shards (30+) and scaling up is not limited by resource constraints like CPU, RAM or disk space. Otherwise, scale horizontally.

- Adding more `vmstorage` nodes (aka horizontal scaling) improves cluster performance and capacity, since every `vmstorage` node contains lower number of time series when the number of `vmstorage` nodes increases.

  The cluster stability is also improved with the number of `vmstorage` nodes, since active `vmstorage` nodes need to handle lower additional workload
  when some of `vmstorage` nodes become unavailable. For example, if one node out of 3 nodes is unavailable, then `1/3=33%` of the load is re-distributed across 2 remaining nodes,
  so per-node workload increase is `(1/3/2)/(1/3) = 1/2 = 50%`.
  If one node out of 10 nodes is unavailable, then `1/10=10%` of the load is re-distributed across 9 remaining nodes, so per-node workload increase is `(1/10/9)/(1/10) = 1/9 =~ 11%`. This is why it is recommended to have 10 or more `vmstorage` nodes.

Steps to add `vmstorage` node:

1. Start new `vmstorage` node with the same `-retentionPeriod` as existing nodes in the cluster.
1. Gradually restart all the `vmselect` nodes with new `-storageNode` arg containing `<new_vmstorage_host>`.
1. Gradually restart all the `vminsert` nodes with new `-storageNode` arg containing `<new_vmstorage_host>`.

To handle uneven disk space usage distribution after adding new `vmstorage` node it is possible to update `vminsert` configuration to route newly ingested metrics only to new storage nodes. Once disk usage will be similar configuration can be updated to include all nodes again. Note that `vmselect` nodes need to reference all storage nodes for querying.
See more at [rebalancing docs](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/#rebalancing).

### Scaling down

Since `vmstorage` nodes are stateful, scaling down the cluster requires redistributing existing accumulated data from the removed nodes to the remaining nodes. This is a time- and resource-consuming process that is better avoided by scaling down vertically or by following the [capacity planning docs](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/#capacity-planning) and picking the right number of shards from the beginning.

To remove a `vmstorage` node from the cluster, follow these steps:
1. Remove `vmstorage` from the [`-storageNode` command-line flag](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/#cluster-setup) on all `vminsert` nodes. This ensures that no new data is ingested into the removed node.
1. Keep the configuration of `vmselect` nodes unchanged, so they continue to read data from the removed `vmstorage` node.
1. Decide how to keep the data from the removed `vmstorage` node available:
   - The easiest way is to keep the removed `vmstorage` node until its `-retentionPeriod` is reached. It won't receive new data but will continue serving read queries for what it already stores. This approach requires no additional work, but keeps the resources of the removed node occupied. Once `-retentionPeriod` is reached, the `vmstorage` node can be removed from `vmselect`'s `-storageNode` configuration and decommissioned. No re-distribution or migration is required in this case.
   - Try migrating the data from the removed node by re-ingesting it into the remaining nodes. See how to do it below.

Please note that migrating big volumes of data is a time- and resource-consuming process, as data has to be read and ingested via the native /export and /import APIs. To re-ingest data from the removed `vmstorage` node to the remaining nodes, follow these steps:
1. Set [deduplication](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/#deduplication) on `vmselect` and `vmstorage` nodes via the command-line flag `-dedup.minScrapeInterval=1ms`. This ensures that `vmselect` and `vmstorage` nodes deduplicate identical samples during migration.
2. Set up a separate temporary `vmselect` node configured to read data **only from the removed node**. Adjust the `-search.maxExportDuration`, `-search.maxExportSeries`, and `-search.maxSeries` limits on the temporary `vmselect` to higher values. You might hit these limits during migration, and error logs on the temporary `vmselect` will identify which limit was hit.
3. Use [vmctl](https://docs.victoriametrics.com/victoriametrics/vmctl/victoriametrics/) to read data from the removed node via new temporary vmselect and write it to the remaining nodes via existing vminserts:
```sh
 ./vmctl vm-native --vm-native-src-addr=http://<new-vmselect>:8481/ \
  --vm-native-dst-addr=http://<vminsert>:8480/ \
  --vm-native-filter-match='{__name__!=""}' \
  --vm-native-filter-time-start='2026-08-01T00:00:00Z' \
  --vm-native-step-interval=day \
  --vm-intercluster
```

  - Run vmctl in the same network as cluster for the best performance
  - If you have load balancer like vmauth in front of vminsert nodes, specify its address in `--vm-native-dst-addr`. This will ensure that import requests will be distributed across all vminserts.
  - Specify `--vm-native-filter-match` or `--vm-native-filter-time-start` if you want to migrate only a subset of data. See more about [vmctl configuration](https://docs.victoriametrics.com/victoriametrics/vmctl/victoriametrics/#configuration).
4. Wait for migration to complete. See how to [monitor migration process](https://docs.victoriametrics.com/victoriametrics/vmctl/#monitoring-the-migration-process) and [migration tips](https://docs.victoriametrics.com/victoriametrics/vmctl/#migration-tips). It is OK to restart migration and re-ingest the same data again if main `vmselect` and `vmstorage` nodes have deduplication enabled.
5. Once migration is completed, remove `vmstorage` from [`-storageNode` command-line flag](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/#cluster-setup) on all `vmselect` nodes. Verify that read queries are still returning expected results.
6. Remove and decommission the temporary `vmselect` node, and `vmstorage` that had to be removed.
