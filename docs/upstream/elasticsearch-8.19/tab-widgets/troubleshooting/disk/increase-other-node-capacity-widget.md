<!-- Converted from tab-widgets/troubleshooting/disk/increase-other-node-capacity-widget.asciidoc (AsciiDoc). Includes are inlined. -->

. Log in to the {ess-console}[Elastic Cloud console].
. On the **Elasticsearch Service** panel, click the gear under the `Manage deployment` column that corresponds to the
name of your deployment.
. Go to `Actions > Edit deployment` and then go to the `Coordinating instances` or the `Machine Learning instances`
section depending on the roles listed in the diagnosis:
(Figure: images/troubleshooting/disk/increase-disk-capacity-other-node.png)

. Choose a larger than the pre-selected capacity configuration from the drop-down menu and click `save`. Wait for
the plan to be applied and the problem should be resolved.

In order to increase the disk capacity of any other node, you will need to replace the instance that has run out of
space with one of higher disk capacity.

. First, retrieve the disk threshold that will indicate how much disk space is needed. The relevant threshold is
the high watermark and can be retrieved via the following command:
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
```
The above means that in order to resolve the disk shortage we need to either drop our disk usage below the 90% or have
more than 150GB available, read more how this threshold works here.

. The next step is to find out the current disk usage, this will allow to calculate how much extra space is needed.
In the following example, we show only a machine learning node for readability purposes:
```console
GET /_cat/nodes?v&h=name,node.role,disk.used_percent,disk.used,disk.avail,disk.total
```
The response will look like this:
```console-result
name                node.role disk.used_percent disk.used disk.avail disk.total
instance-0000000000     l                 85.31    3.4gb     500mb       4gb
```

. The desired situation is to drop the disk usage below the relevant threshold, in our example 90%. Consider adding
some padding, so it will not go over the threshold soon. Assuming you have the new node ready, add this node to the
cluster.

. Verify that the new node has joined the cluster:
```console
GET /_cat/nodes?v&h=name,node.role,disk.used_percent,disk.used,disk.avail,disk.total
```
The response will look like this:
```console-result
name                node.role disk.used_percent disk.used disk.avail disk.total
instance-0000000000     l                 85.31    3.4gb     500mb       4gb
instance-0000000001     l                 41.31    3.4gb     4.5gb       8gb
```
. Now you can remove the out of disk space instance.
