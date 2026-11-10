<!-- Converted from tab-widgets/troubleshooting/disk/increase-data-node-capacity-widget.asciidoc (AsciiDoc). Includes are inlined. -->

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
