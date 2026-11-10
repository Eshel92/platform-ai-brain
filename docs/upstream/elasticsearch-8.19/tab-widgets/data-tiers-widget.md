<!-- Converted from tab-widgets/data-tiers-widget.asciidoc (AsciiDoc). Includes are inlined. -->

. Log in to the {ess-trial}[Elasticsearch Service Console].

. Add or select your deployment from the Elasticsearch Service home page or the deployments
page.

. From your deployment menu, select **Edit deployment**.

. To enable a data tier, click **Add capacity**.

**Enable autoscaling**

{cloud}/ec-autoscaling.html[Autoscaling] automatically adjusts your deployment's
capacity to meet your storage needs. To enable autoscaling, select **Autoscale
this deployment** on the **Edit deployment** page. Autoscaling is only available
for Elasticsearch Service.

To assign a node to a data tier, add the respective node role to
the node's `elasticsearch.yml` file. Changing an existing node's roles requires
a rolling restart.

```yaml
# Content tier
node.roles: [ data_content ]

# Hot tier
node.roles: [ data_hot ]

# Warm tier
node.roles: [ data_warm ]

# Cold tier
node.roles: [ data_cold ]

# Frozen tier
node.roles: [ data_frozen ]
```

We recommend you use dedicated nodes in the frozen tier. If needed, you can
assign other nodes to more than one tier.

```yaml
node.roles: [ data_content, data_hot, data_warm ]
```

Assign your nodes any other roles needed for your cluster. For example, a small
cluster may have nodes with multiple roles.

```yaml
node.roles: [ master, ingest, ml, data_hot, transform ]
```
