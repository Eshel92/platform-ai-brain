<!-- Converted from tab-widgets/troubleshooting/data/increase-cluster-shard-limit-widget.asciidoc (AsciiDoc). Includes are inlined. -->

In order to get the shards assigned we'll need to increase the number of shards 
that can be collocated on a node in the cluster.
We'll achieve this by inspecting the system-wide `cluster.routing.allocation.total_shards_per_node` 
cluster setting and increasing the configured value.

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

. Inspect the `cluster.routing.allocation.total_shards_per_node` cluster setting:
```console
GET /_cluster/settings?flat_settings
```
The response will look like this:
```console-result
{
  "persistent": {
    "cluster.routing.allocation.total_shards_per_node": "300" <1>
  },
  "transient": {}
}
```

<1> Represents the current configured value for the total number of shards
that can reside on one node in the system.

. Increase the value for the total number of shards 
that can be assigned on one node to a higher value:
```console
PUT _cluster/settings
{
  "persistent" : {
    "cluster.routing.allocation.total_shards_per_node" : 400 <1>
  }
}
```

<1> The new value for the system-wide `total_shards_per_node` configuration
is increased from the previous value of `300` to `400`. 
The `total_shards_per_node` configuration can also be set to `null`, which 
represents no upper bound with regards to how many shards can be 
collocated on one node in the system. 

In order to get the shards assigned you can add more nodes to your Elasticsearch cluster 
and assign the index's target tier node role to the new 
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
inspecting the system-wide `cluster.routing.allocation.total_shards_per_node` 
cluster setting and increasing the configured value:

. Inspect the `cluster.routing.allocation.total_shards_per_node` cluster setting 
for the index with unassigned shards:
```console
GET /_cluster/settings?flat_settings
```
The response will look like this:
```console-result
{
  "persistent": {
    "cluster.routing.allocation.total_shards_per_node": "300" <1>
  },
  "transient": {}
}
```

<1> Represents the current configured value for the total number of shards
that can reside on one node in the system.

. Increase the value for the total number of shards 
that can be assigned on one node to a higher value:
```console
PUT _cluster/settings
{
  "persistent" : {
    "cluster.routing.allocation.total_shards_per_node" : 400 <1>
  }
}
```

<1> The new value for the system-wide `total_shards_per_node` configuration
is increased from the previous value of `300` to `400`. 
The `total_shards_per_node` configuration can also be set to `null`, which 
represents no upper bound with regards to how many shards can be 
collocated on one node in the system.
