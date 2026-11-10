<!-- Converted from tab-widgets/troubleshooting/data/migrate-to-data-tiers-routing-guide.asciidoc (AsciiDoc). Includes are inlined. -->

In order to get the shards assigned we need to call the
migrate to data tiers routing API which will
resolve the conflicting routing configurations towards using the standardized
data tiers. This will also future-proof the system by migrating
the index templates and ILM policies if needed.

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

. First, let's stop index lifecycle management
```console
POST /_ilm/stop
```
The response will look like this:
```console-result
{
  "acknowledged": true
}
```

. Wait for index lifecycle management to stop. Check the status until it returns `STOPPED` as follows:
```console
GET /_ilm/status
```
When index lifecycle management has successfully stopped the response will look like this:
```console-result
{
  "operation_mode": "STOPPED"
}
```

. Migrate to data tiers
```console
POST /_ilm/migrate_to_data_tiers
```
The response will look like this:
```console-result
{
  "dry_run": false,
  "migrated_ilm_policies":["policy_with_allocate_action"], <1>
  "migrated_indices":["warm-index-to-migrate-000001"], <2>
  "migrated_legacy_templates":["a-legacy-template"], <3>
  "migrated_composable_templates":["a-composable-template"], <4>
  "migrated_component_templates":["a-component-template"] <5>
}
```
<1> The ILM policies that were updated.
<2> The indices that were migrated to tier preference routing.
<3> The legacy index templates that were updated to not contain custom routing settings for the
provided data attribute.
<4> The composable index templates that were updated to not contain custom routing settings for the
provided data attribute.
<5> The component templates that were updated to not contain custom routing settings for the
provided data attribute.

. Restart index lifecycle management
```console
POST /_ilm/start
```
The response will look like this:
```console-result
{
  "acknowledged": true
}
```

In order to get the shards assigned we need to make sure the deployment is
using the data tiers node roles and then call the
migrate to data tiers routing API which will
resolve the conflicting routing configurations towards using the standardized
data tiers. This will also future-proof the system by migrating
the index templates and ILM policies if needed.

. In case your deployment is not yet using data tiers assign data nodes
to the appropriate data tier.
Configure the appropriate roles for each data node to assign it to one or more
data tiers: `data_hot`, `data_content`, `data_warm`, `data_cold`, or `data_frozen`.
For example, the following setting configures a node to be a data-only
node in the hot and content tiers.
```yaml
node.roles [ data_hot, data_content ]
```

. Stop index lifecycle management
```console
POST /_ilm/stop
```

The response will look like this:
```console-result
{
  "acknowledged": true
}
```

. Wait for index lifecycle management to stop. Check the status until it returns `STOPPED` as follows:
```console
GET /_ilm/status
```
When index lifecycle management has successfully stopped the response will look like this:
```console-result
{
  "operation_mode": "STOPPED"
}
```

. Migrate to data tiers
```console
POST /_ilm/migrate_to_data_tiers
```

The response will look like this:
```console-result
{
  "dry_run": false,
  "migrated_ilm_policies":["policy_with_allocate_action"], <1>
  "migrated_indices":["warm-index-to-migrate-000001"], <2>
  "migrated_legacy_templates":["a-legacy-template"], <3>
  "migrated_composable_templates":["a-composable-template"], <4>
  "migrated_component_templates":["a-component-template"] <5>
}
```
<1> The ILM policies that were updated.
<2> The indices that were migrated to tier preference routing.
<3> The legacy index templates that were updated to not contain custom routing settings for the
provided data attribute.
<4> The composable index templates that were updated to not contain custom routing settings for the
provided data attribute.
<5> The component templates that were updated to not contain custom routing settings for the
provided data attribute.

. Restart index lifecycle management
```console
POST /_ilm/start
```
The response will look like this:
```console-result
{
  "acknowledged": true
}
```
