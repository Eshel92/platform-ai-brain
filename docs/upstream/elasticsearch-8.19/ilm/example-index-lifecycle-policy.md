<!-- Converted from ilm/example-index-lifecycle-policy.asciidoc (AsciiDoc). Includes are inlined. -->

### Tutorial: Customize built-in ILM policies

Elasticsearch includes the following built-in ILM policies:

- `logs@lifecycle`
- `metrics@lifecycle`
- `synthetics@lifecycle`

Elastic Agent uses these policies to manage backing indices for its data streams.
This tutorial shows you how to use Kibana’s **Index Lifecycle Policies** to
customize these policies based on your application's performance, resilience,
and retention requirements.

#### Scenario

You want to send log files to an Elasticsearch cluster so you can visualize and analyze
the data. This data has the following retention requirements:

* When the primary shard size of the write index reaches 50GB or the index is 30 days old, roll over to a new index.
* After rollover, keep indices in the hot data tier for 30 days.
* 30 days after rollover:
** Move indices to the warm data tier.
** Set replica shards to 1.
** Force merge multiple index segments to free up the
space used by deleted documents.
* Delete indices 90 days after rollover.

#### Prerequisites

To complete this tutorial, you'll need:

* An Elasticsearch cluster with hot and warm data tiers.

** Elasticsearch Service:
Elastic Stack deployments on Elasticsearch Service include a hot tier by default. To add a warm
tier, edit your deployment and click **Add capacity** for the warm data tier.
(Figure: images/ilm/tutorial-ilm-ess-add-warm-data-tier.png)

** Self-managed cluster:
Assign `data_hot` and `data_warm` roles to nodes as described in
data-tiers.
For example, include the `data_warm` node role in the `elasticsearch.yml` file
of each node in the warm tier:
```yaml
node.roles: [ data_warm ]
```

* A host with Elastic Agent installed and configured to send logs to your Elasticsearch
cluster.

#### Duplicate the policy

Elastic Agent uses data streams with an index pattern of `logs-*-*` to store log
monitoring data. The managed `logs@lifecycle` ILM policy automatically manages
backing indices for these data streams. 

If you don't want to use the policy defaults, then you can customize the managed policy and then save it as a new policy. You can then use the new policy in related component templates and index templates.

**Caution:** You should never edit managed policies directly. Changes to managed policies might be rolled back or overwritten.

To save the `logs@lifecycle` policy as a new policy in Kibana:

. Open the menu and go to **Stack Management** > **Index Lifecycle Policies**.
. Toggle **Include managed system policies**.
. Select the `logs@lifecycle` policy.
. On the **Edit policy logs** page, toggle **Save as new policy**, and then provide a new name for the policy, for example, `logs-custom`.

The `logs@lifecycle` policy uses the recommended rollover defaults: Start writing to a new
index when the primary shard size of the current write index reaches 50GB or the index becomes 30 days old.

To view or change the rollover settings, click **Advanced settings** for the hot
phase. Then disable **Use recommended defaults** to display the rollover
settings.

(Figure: images/ilm/tutorial-ilm-hotphaserollover-default.png)

#### Modify the policy

The default `logs@lifecycle` policy is designed to prevent the creation of many tiny daily
indices. You can modify your copy of the policy to meet your performance requirements and
manage resource usage.

. Activate the warm phase and click **Advanced settings**.
.. Set **Move data into phase when** to **30 days old**. This moves indices to
the warm tier 30 days after rollover.

.. Enable **Set replicas** and change **Number of replicas** to **1**.

.. Enable **Force merge data** and set **Number of segments** to **1**.

(Figure: images/ilm/tutorial-ilm-modify-default-warm-phase-rollover.png)

. In the warm phase, click the trash icon to enable the delete phase.
(Figure: images/ilm/tutorial-ilm-enable-delete-phase.png)
In the delete phase, set **Move data into phase when** to **90 days old**. This
deletes indices 90 days after rollover.
(Figure: images/ilm/tutorial-ilm-delete-rollover.png)

. Click **Save as new policy**.

**Tip:** Copies of managed ILM policies are also marked as **Managed**. You can use the Create or update lifecycle policy API to update the `_meta.managed` parameter to `false`.

#### Apply the policy

To apply your new ILM policy to the `logs` index template, create or edit the `logs@custom` component template. 

A `*@custom` component template allows you to customize the mappings and settings of managed index templates, without having to override managed index templates or component templates. This type of component template is automatically picked up by the index template. Learn more.

. Click on the **Component Template** tab and click **Create component template**.
. Under **Logistics**, name the component template `logs@custom`.
. Under **Index settings**, set the ILM policy name created in the previous step:
```JSON
{
    "index": {
        "lifecycle": {
            "name": "logs-custom"
        }
    }
}
```
. Continue to **Review**, and then click **Save component template**.
. Click the **Index Templates**, tab, and then select the `logs` index template.
. In the summary, view the **Component templates** list. `logs@custom` should be listed.
