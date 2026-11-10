<!-- Converted from tab-widgets/troubleshooting/data/add-tier-widget.asciidoc (AsciiDoc). Includes are inlined. -->

In order to get the shards assigned we need enable a new tier in the deployment.

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

. Determine which tier an index expects for assignment. Retrieve
the configured value for the `index.routing.allocation.include._tier_preference`
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
<1> Represents a comma-separated list of data tier node roles this index is allowed
to be allocated on, the first one in the list being the one with the higher priority
i.e. the tier the index is targeting.
e.g. in this example the tier preference is `data_warm,data_hot` so the index is
targeting the `warm` tier and more nodes with the `data_warm` role are needed in
the Elasticsearch cluster.

. Open your deployment's side navigation menu (placed under the Elastic logo in the upper left corner)
and go to **Manage this deployment**.

. From the right hand side, click to expand the **Manage** dropdown button and
select **Edit deployment** from the list of options.

. On the **Edit** page, click on **+ Add Capacity** for the tier you identified
you need to enable in your deployment. Choose the desired size and availability
zones for the new tier.

. Navigate to the bottom of the page and click the **Save** button.

In order to get the shards assigned you can add more nodes to your Elasticsearch cluster 
and assign the index's target tier node role to the new 
nodes. 

To determine which tier an index requires for assignment, use the get index setting
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

<1> Represents a comma-separated list of data tier node roles this index is allowed
to be allocated on, the first one in the list being the one with the higher priority
i.e. the tier the index is targeting.
e.g. in this example the tier preference is `data_warm,data_hot` so the index is
targeting the `warm` tier and more nodes with the `data_warm` role are needed in
the Elasticsearch cluster.
