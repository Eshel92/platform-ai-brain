<!-- Converted from user/monitoring/monitoring-metricbeat.asciidoc (AsciiDoc). Includes are inlined. -->

# Collect Kibana monitoring data with {metricbeat}

In 6.4 and later, you can use {metricbeat} to collect data about Kibana
and ship it to the monitoring cluster, rather than routing it through the
production cluster as described in monitoring-kibana.

(Figure: user/monitoring/images/metricbeat.png)

To learn about monitoring in general, see
[Monitor a cluster](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/monitor-elasticsearch-cluster.html).

. Disable the default collection of Kibana monitoring metrics. +
Add the following setting in the Kibana configuration file (`kibana.yml`):

```yaml
monitoring.kibana.collection.enabled: false
```

Leave the `monitoring.enabled` set to its default value (`true`).
For more information, see
Monitoring settings in Kibana.

. Start Kibana.

. Set the `xpack.monitoring.collection.enabled` setting to `true` on
each node in the production cluster. By default, it is disabled (`false`).
**Note:** You can specify this setting in either the `elasticsearch.yml` on each
node or across the cluster as a dynamic cluster setting. If Elasticsearch
security features are enabled, you must have `monitor` cluster privileges to
view the cluster settings and `manage` cluster privileges to change them.

** In Kibana:

... Open Kibana in your web browser.
If you are running Kibana locally, go to `http://localhost:5601/`.

If the Elastic security features are enabled, log in.

... In the side navigation, click *Stack Monitoring*. If data collection is
disabled, you are prompted to turn it on.

** From the Console or command line, set `xpack.monitoring.collection.enabled`
to `true` on the production cluster. +
For example, you can use the following APIs to review and change this setting:

```js
GET _cluster/settings

PUT _cluster/settings
{
  "persistent": {
    "xpack.monitoring.collection.enabled": true
  }
}
```

For more information, see [Monitoring settings in Elasticsearch](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/monitoring-settings.html)
and [Cluster update settings](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/cluster-update-settings.html).

. {metricbeat-ref}/metricbeat-installation-configuration.html[Install {metricbeat}] on the
same server as Kibana.

. Enable the Kibana X-Pack module in {metricbeat}. +
For example, to enable the default configuration in the `modules.d` directory,
run the following command:

```
metricbeat modules enable kibana-xpack
```

For more information, see
{metricbeat-ref}/configuration-metricbeat.html[Specify which modules to run] and
{metricbeat-ref}/metricbeat-module-kibana.html[Kibana module].

. Configure the Kibana X-Pack module in {metricbeat}. +
The `modules.d/kibana-xpack.yml` file contains the following settings:

```yaml
- module: kibana
  metricsets:
    - stats
  period: 10s
  hosts: ["localhost:5601"]
  #basepath: ""
  #username: "user"
  #password: "secret"
  xpack.enabled: true
```

By default, the module collects Kibana monitoring metrics from `localhost:5601`.
If that host and port number are not correct, you must update the `hosts`
setting. If you configured Kibana to use encrypted communications, you must
access it via HTTPS. For example, use a `hosts` setting like
`https://localhost:5601`.

If the Elastic security features are enabled, you must also provide a user
ID and password so that {metricbeat} can collect metrics successfully:

.. Create a user on the production cluster that has the
`remote_monitoring_collector` [built-in role](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/built-in-roles.html).
Alternatively, use the `remote_monitoring_user`
[built-in user](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/built-in-users.html).

.. Add the `username` and `password` settings to the Kibana module configuration
file.

. Optional: Disable the system module in {metricbeat}.
By default, the {metricbeat-ref}/metricbeat-module-system.html[system module] is
enabled. The information it collects, however, is not shown on the *Monitoring*
page in Kibana. Unless you want to use that information for other purposes, run
the following command:

```
metricbeat modules disable system
```

. Identify where to send the monitoring data. +
**Tip:** In production environments, we strongly recommend using a separate cluster
(referred to as the _monitoring cluster_) to store the data. Using a separate
monitoring cluster prevents production cluster outages from impacting your
ability to access your monitoring data. It also prevents monitoring activities
from impacting the performance of your production cluster.

For example, specify the Elasticsearch output information in the {metricbeat}
configuration file (`metricbeat.yml`):

```yaml
output.elasticsearch:
  # Array of hosts to connect to.
  hosts: ["<HOST_1>:9200", "<HOST_2>:9200"] <1>

  # Optional protocol and basic auth credentials.
  #protocol: "https"
  #username: "elastic"
  #password: "changeme"
```
<1> In this example, the data is stored on a monitoring cluster with nodes
`es-mon-1` and `es-mon-2`.

If you configured the monitoring cluster to use encrypted communications, you
must access it via HTTPS. For example, use a `hosts` setting like
`<HOST_URL>:9200`.

**Important:** The Elasticsearch {monitor-features} use ingest pipelines. The
cluster that stores the monitoring data must have at least one node with the
`ingest` role.

If the Elasticsearch security features are enabled on the monitoring cluster, you
must provide a valid user ID and password so that {metricbeat} can send metrics
successfully:

.. Create a user on the monitoring cluster that has the
`remote_monitoring_agent` [built-in role](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/built-in-roles.html).
Alternatively, use the `remote_monitoring_user`
[built-in user](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/built-in-users.html).

.. Add the `username` and `password` settings to the Elasticsearch output information in
the {metricbeat} configuration file.

For more information about these configuration options, see
{metricbeat-ref}/elasticsearch-output.html[Configure the Elasticsearch output].

. {metricbeat-ref}/metricbeat-starting.html[Start {metricbeat}].

. View the monitoring data in Kibana.
