<!-- Converted from monitoring/configuring-elastic-agent.asciidoc (AsciiDoc). Includes are inlined. -->

## Collecting Elasticsearch monitoring data with Elastic Agent

In 8.5 and later, you can use Elastic Agent to collect data about Elasticsearch and ship it to
the monitoring cluster, rather than using {metricbeat}
or routing it through exporters as described in collecting-monitoring-data.

### Prerequisites

* (Optional) Create a monitoring cluster as described in monitoring-production.

* Create a user on the production cluster that has the
`remote_monitoring_collector` [built-in role](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/built-in-roles.html).

### Add Elasticsearch monitoring data

To collect Elasticsearch monitoring data, add an Elasticsearch integration to an Elastic Agent and
deploy it to the host where Elasticsearch is running.

. Go to the Kibana home page and click **Add integrations**.
. In the query bar, search for and select the **Elasticsearch** integration for
Elastic Agent.
. Read the overview to make sure you understand integration requirements and
other considerations.
. Click **Add Elasticsearch**.
**Tip:** If you're installing an integration for the first time, you may be prompted
to install Elastic Agent. Click **Add integration only (skip agent installation)**.

. Configure the integration name and optionally add a description. Make sure you
configure all required settings:
.. Under **Collect Elasticsearch logs**, modify the log paths to match your Elasticsearch
environment.
.. Under **Collect Elasticsearch metrics**, make sure the hosts setting points to
your Elasticsearch host URLs. By default, the integration collects Elasticsearch monitoring
metrics from `localhost:9200`. If that host and port number are not correct,
update the `hosts` setting. If you configured Elasticsearch to use encrypted
communications, you must access it via HTTPS. For example, use a `hosts` setting
like `https://localhost:9200`.
.. Expand **Advanced options**. If the Elastic security features are enabled,
enter the username and password of a user that has the
`remote_monitoring_collector` role.
.. Specify the scope:
** Specify `cluster` if each entry in the hosts list indicates a single
endpoint for a distinct Elasticsearch cluster (for example, a load-balancing proxy
fronting the cluster that directs requests to the master-ineligible nodes in the
cluster).
** Otherwise, accept the default scope, `node`. If this scope is set, you
will need to install Elastic Agent on each Elasticsearch node to collect all metrics. Elastic Agent
will collect most of the metrics from the elected master of the cluster, so you
must scale up all your master-eligible nodes to account for this extra load. Do
not use this `node` if you have dedicated master nodes.
. Choose where to add the integration policy. Click **New hosts** to add it to
new agent policy or **Existing hosts** to add it to an existing agent policy.
. Click **Save and continue**. This step takes a minute or two to complete. When
it's done, you'll have an agent policy that contains an integration for
collecting monitoring data from Elasticsearch.
. If an Elastic Agent is already assigned to the policy and deployed to the host where
Elasticsearch is running, you're done. Otherwise, you need to deploy an Elastic Agent. To
deploy an Elastic Agent:
.. Go to **Fleet -> Agents**, then click **Add agent**.
.. Follow the steps in the **Add agent** flyout to download, install,
and enroll the Elastic Agent. Make sure you choose the agent policy you created
earlier.
. Wait a minute or two until incoming data is confirmed.
. [View the monitoring data in Kibana](https://www.elastic.co/guide/en/kibana/8.19/monitoring-data.html).
