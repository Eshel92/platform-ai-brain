<!-- Converted from tab-widgets/troubleshooting/data/total-shards-per-node-widget.asciidoc (AsciiDoc). Includes are inlined. -->

In order to get the shards assigned we'll need to increase the number of shards 
that can be collocated on a node. 
We'll achieve this by inspecting the configuration for the `index.routing.allocation.total_shards_per_node` 
index setting and increasing the configured value for the
indices that have shards unassigned.

**Use Kibana**

. Log in to the {ess-console}[Elastic Cloud console].

. On the **Elasticsearch Service** panel, click the name of your deployment. 

**Note:** If the name of your deployment is disabled your Kibana instances might be
unhealthy, in which case please contact [Elastic Support](https://support.elastic.co).
If your deployment doesn't include Kibana, all you need to do is 
{cloud}/ec-access-kibana.html[enable it first].

. Open your deployment's side navigation menu (placed under the Elastic logo in the upper left corner)
and go to **Dev Tools > Console**.
(Figure: images/kibana-console.png)

. Inspect the `index.routing.allocation.total_shards_per_node` index setting 
for the index with unassigned shards:
```console
GET /my-index-000001/_settings/index.routing.allocation.total_shards_per_node?flat_settings
```
The response will look like this:
```console-result
{
  "my-index-000001": {
    "settings": {
      "index.routing.allocation.total_shards_per_node": "1" <1>
    }
  }
}
```
<1> Represents the current configured value for the total number of shards
that can reside on one node for the `my-index-000001` index.

. Increase the value for the total number of shards 
that can be assigned on one node to a higher value:
```console
PUT /my-index-000001/_settings
{
  "index" : {
    "routing.allocation.total_shards_per_node" : "2" <1>
  }
}
```

<1> The new value for the `total_shards_per_node` configuration for the `my-index-000001` index
is increased from the previous value of `1` to `2`. 
The `total_shards_per_node` configuration can also be set to `-1`, which 
represents no upper bound with regards to how many shards of the same 
index can reside on one node.

In order to get the shards assigned you can add more nodes to your Elasticsearch cluster 
and assing the index's target tier node role to the new 
nodes. 

To inspect which tier is an index targeting for assignment, use the get index setting
API to retrieve the configured value for the `index.routing.allocation.include._tier_preference`
setting:

```console
GET /my-index-000001/_settings/index.routing.allocation.include._tier_preference?flat_settings
```

The response will look like this:

```console-result
{
  "my-index-000001": {
    "settings": {
      "index.routing.allocation.include._tier_preference": "data_warm,data_hot" <1>
    }
  }
}
```

<1> Represents a comma separated list of data tier node roles this index is allowed
to be allocated on, the first one in the list being the one with the higher priority
i.e. the tier the index is targeting.
e.g. in this example the tier preference is `data_warm,data_hot` so the index is
targeting the `warm` tier and more nodes with the `data_warm` role are needed in
the Elasticsearch cluster.

Alternatively, if adding more nodes to the Elasticsearch cluster is not desired,
inspecting the configuration for the `index.routing.allocation.total_shards_per_node` 
index setting and increasing the configured value will 
allow more shards to be assigned on the same node.

. Inspect the `index.routing.allocation.total_shards_per_node` index setting 
for the index with unassigned shards:
```console
GET /my-index-000001/_settings/index.routing.allocation.total_shards_per_node?flat_settings
```

The response will look like this:

```console-result
{
  "my-index-000001": {
    "settings": {
      "index.routing.allocation.total_shards_per_node": "1" <1>
    }
  }
}
```

<1> Represents the current configured value for the total number of shards
that can reside on one node for the `my-index-000001` index.

. Increase the total number of shards that can be assigned on one node or
reset the value to unbounded (`-1`):
```console
PUT /my-index-000001/_settings
{
  "index" : {
    "routing.allocation.total_shards_per_node" : -1
  }
}
```
