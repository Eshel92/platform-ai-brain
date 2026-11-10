<!-- Converted from troubleshooting/disk/fix-data-node-out-of-disk.asciidoc (AsciiDoc). Includes are inlined. -->

## Fix data nodes out of disk

Elasticsearch is using data nodes to distribute your data inside the cluster. If one or more of these nodes are running
out of space, Elasticsearch takes action to redistribute your data within the nodes so all nodes have enough available
disk space. If Elasticsearch cannot facilitate enough available space in a node, then you will need to intervene in one
of two ways:

. Increase the disk capacity of your cluster
. Reduce the disk usage by decreasing your data volume

### Increase the disk capacity of data nodes

In order to increase the disk capacity of the data nodes in your cluster:

. Log in to the {ess-console}[Elastic Cloud console].
. On the **Elasticsearch Service** panel, click the gear under the `Manage deployment` column that corresponds to the
name of your deployment.
. If autoscaling is available but not enabled, please enable it. You can do this by clicking the button
`Enable autoscaling` on a banner like the one below:
(Figure: images/troubleshooting/disk/autoscaling_banner.png)
Or you can go to `Actions > Edit deployment`, check the checkbox `Autoscale` and click `save` at the bottom of the page.
(Figure: images/troubleshooting/disk/enable_autoscaling.png)

. If autoscaling has succeeded the cluster should return to `healthy` status. If the cluster is still out of disk,
please check if autoscaling has reached its limits. You will be notified about this by the following banner:
(Figure: images/troubleshooting/disk/autoscaling_limits_banner.png)
or you can go to `Actions > Edit deployment` and look for the label `LIMIT REACHED` as shown below:
(Figure: images/troubleshooting/disk/reached_autoscaling_limits.png)
If you are seeing the banner click `Update autoscaling settings` to go to the `Edit` page. Otherwise, you are already
in the `Edit` page, click `Edit settings` to increase the autoscaling limits. After you perform the change click `save`
at the bottom of the page.

In order to increase the data node capacity in your cluster, you will need to calculate the amount of extra disk space
needed.

. First, retrieve the relevant disk thresholds that will indicate how much space should be available. The
relevant thresholds are the high watermark for all the tiers apart from the frozen
one and the frozen flood stage watermark for the frozen tier. The following
example demonstrates disk shortage in the hot tier, so we will only retrieve the high watermark:
```console
GET _cluster/settings?include_defaults&filter_path=*.cluster.routing.allocation.disk.watermark.high*
```
The response will look like this:
```console-result
{
  "defaults": {
    "cluster": {
      "routing": {
        "allocation": {
          "disk": {
            "watermark": {
              "high": "90%",
              "high.max_headroom": "150GB"
            }
          }
        }
      }
    }
  }
}
```
The above means that in order to resolve the disk shortage we need to either drop our disk usage below the 90% or have
more than 150GB available, read more on how this threshold works here.

. The next step is to find out the current disk usage, this will indicate how much extra space is needed. For simplicity,
our example has one node, but you can apply the same for every node over the relevant threshold.
```console
GET _cat/allocation?v&s=disk.avail&h=node,disk.percent,disk.avail,disk.total,disk.used,disk.indices,shards
```
The response will look like this:
```console-result
node                disk.percent disk.avail disk.total disk.used disk.indices shards
instance-0000000000           91     4.6gb       35gb    31.1gb       29.9gb    111
```

. The high watermark configuration indicates that the disk usage needs to drop below 90%. To achieve this, 2
things are possible:
- to add an extra data node to the cluster (this requires that you have more than one shard in your cluster), or
- to extend the disk space of the current node by approximately 20% to allow this node to drop to 70%. This will give
enough space to this node to not run out of space soon.

. In the case of adding another data node, the cluster will not recover immediately. It might take some time to
relocate some shards to the new node. You can check the progress here:
```console
GET /_cat/shards?v&h=state,node&s=state
```
If in the response the shards' state is `RELOCATING`, it means that shards are still moving. Wait until all shards turn
to `STARTED` or until the health disk indicator turns to `green`.

### Decrease the disk usage of data nodes

In order to decrease the disk usage in your cluster without losing any data, you can try reducing the replicas of indices.

**Note:** Reducing the replicas of an index can potentially reduce search throughput and data redundancy. However, it
can quickly give the cluster breathing room until a more permanent solution is in place.

**Use Kibana**

. Log in to the {ess-console}[Elastic Cloud console].

. On the **Elasticsearch Service** panel, click the name of your deployment.

**Note:** If the name of your deployment is disabled your Kibana instances might be
unhealthy, in which case please contact [Elastic Support](https://support.elastic.co).
If your deployment doesn't include Kibana, all you need to do is
{cloud}/ec-access-kibana.html[enable it first].
. Open your deployment's side navigation menu (placed under the Elastic logo in the upper left corner)
and go to **Stack Management > Index Management**.

. In the list of all your indices, click the `Replicas` column twice to sort the indices based on their number of
replicas starting with the one that has the most. Go through the indices and pick one by one the index with the
least importance and higher number of replicas.
**Warning:** Reducing the replicas of an index can potentially reduce search throughput and data redundancy.
. For each index you chose, click on its name, then on the panel that appears click `Edit settings`, reduce the
value of the `index.number_of_replicas` to the desired value and then click `Save`.
(Figure: images/troubleshooting/disk/reduce_replicas.png)
. Continue this process until the cluster is healthy again.

In order to estimate how many replicas need to be removed, first you need to estimate the amount of disk space that
needs to be released.

. First, retrieve the relevant disk thresholds that will indicate how much space should be released. The
relevant thresholds are the high watermark for all the tiers apart from the frozen
one and the frozen flood stage watermark for the frozen tier. The following
example demonstrates disk shortage in the hot tier, so we will only retrieve the high watermark:
```console
GET _cluster/settings?include_defaults&filter_path=*.cluster.routing.allocation.disk.watermark.high*
```
The response will look like this:
```console-result
{
  "defaults": {
    "cluster": {
      "routing": {
        "allocation": {
          "disk": {
            "watermark": {
              "high": "90%",
              "high.max_headroom": "150GB"
            }
          }
        }
      }
    }
  }
}
```
The above means that in order to resolve the disk shortage we need to either drop our disk usage below the 90% or have
more than 150GB available, read more on how this threshold works here.

. The next step is to find out the current disk usage; this will indicate how much space should be freed. For simplicity,
our example has one node, but you can apply the same for every node over the relevant threshold.
```console
GET _cat/allocation?v&s=disk.avail&h=node,disk.percent,disk.avail,disk.total,disk.used,disk.indices,shards
```
The response will look like this:
```console-result
node                disk.percent disk.avail disk.total disk.used disk.indices shards
instance-0000000000           91     4.6gb       35gb    31.1gb       29.9gb    111
```

. The high watermark configuration indicates that the disk usage needs to drop below 90%. Consider allowing some
padding, so the node will not go over the threshold in the near future. In this example, let's release approximately 7GB.

. The next step is to list all the indices and choose which replicas to reduce.
**Note:** The following command orders the indices with descending number of replicas and primary store size. We do this to
help you choose which replicas to reduce under the assumption that the more replicas you have the smaller the risk if
you remove a copy and the bigger the replica the more space will be released. This does not take into consideration any
functional requirements, so please see it as a mere suggestion.
```console
GET _cat/indices?v&s=rep:desc,pri.store.size:desc&h=health,index,pri,rep,store.size,pri.store.size
```
The response will look like:
```console-result
health index                                                      pri rep store.size pri.store.size
green  my_index                                                     2   3      9.9gb          3.3gb
green  my_other_index                                               2   3      1.8gb        470.3mb
green  search-products                                              2   3    278.5kb         69.6kb
green  logs-000001                                                  1   0      7.7gb          7.7gb
```
. In the list above we see that if we reduce the replicas to 1 of the indices `my_index` and  `my_other_index` we will
release the required disk space. It is not necessary to reduce the replicas of `search-products` and `logs-000001` does
not have any replicas anyway. Reduce the replicas of one or more indices with the <<indices-update-settings,
index update settings API>>:
**Warning:** Reducing the replicas of an index can potentially reduce search throughput and data redundancy.
```console
PUT my_index,my_other_index/_settings
{
  "index.number_of_replicas": 1
}
```
