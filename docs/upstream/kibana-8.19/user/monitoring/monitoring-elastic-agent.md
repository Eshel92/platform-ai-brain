<!-- Converted from user/monitoring/monitoring-elastic-agent.asciidoc (AsciiDoc). Includes are inlined. -->

# Collect Kibana monitoring data with Elastic Agent

In 8.5 and later, you can use Elastic Agent to collect data about Kibana and ship it to
the monitoring cluster, rather than using {metricbeat}
or routing data through the production cluster as described in
monitoring-kibana.

To learn about monitoring in general, see
[Monitor a cluster](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/monitor-elasticsearch-cluster.html).

## Prerequisites

* Set up Elasticsearch monitoring and optionally create a monitoring cluster as described
in the [Elasticsearch monitoring documentation](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/monitoring-production.html).

* Create a user on the production cluster that has the
`remote_monitoring_collector` [built-in role](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/built-in-roles.html).

## Add Kibana monitoring data

To collect Kibana monitoring data, add a Kibana integration to an Elastic Agent and
deploy it to the host where Kibana is running.

. Go to the **Integrations** page.
**Note:** If you're using a monitoring cluster, use the Kibana instance connected to
the monitoring cluster.

. In the query bar, search for and select the **Kibana** integration for
Elastic Agent.

. Read the overview to make sure you understand integration requirements and
other considerations.
. Click **Add Kibana**.
**Tip:** If you're installing an integration for the first time, you may be prompted
to install Elastic Agent. Click **Add integration only (skip agent installation)**.

. Configure the integration name and optionally add a description. Make sure you
configure all required settings:
* Under **Collect Kibana logs**, modify the log paths to match your Kibana
environment.
* Under **Collect Kibana metrics**, make sure the hosts setting points to your
Kibana host URLs. By default, the integration collects Kibana monitoring metrics
from `localhost:5601`. If that host and port number are not correct, update the
`hosts` setting. If you configured Kibana to use encrypted communications, you
must access it via HTTPS. For example, use a `hosts` setting like
`https://localhost:5601`.
* If the Elastic security features are enabled, expand **Advanced options**
under the Hosts setting and enter the username and password of a user that has
the `remote_monitoring_collector` role.
. Choose where to add the integration policy. Click **New hosts** to add it to
new agent policy or **Existing hosts** to add it to an existing agent policy.
. Click **Save and continue**. This step takes a minute or two to complete. When
it's done, you'll have an agent policy that contains an integration for
collecting monitoring data from Kibana.
. If an Elastic Agent is already assigned to the policy and deployed to the host where
Kibana is running, you're done. Otherwise, you need to deploy an Elastic Agent. To
deploy an Elastic Agent:
.. Go to **Fleet -> Agents**, then click **Add agent**.
.. Follow the steps in the **Add agent** flyout to download, install,
and enroll the Elastic Agent. Make sure you choose the agent policy you created
earlier.
. Wait a minute or two until incoming data is confirmed.
. View the monitoring data in Kibana.
