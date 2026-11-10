<!-- Converted from monitoring/configuring-filebeat.asciidoc (AsciiDoc). Includes are inlined. -->

## Collecting Elasticsearch log data with {filebeat}

You can use {filebeat} to monitor the Elasticsearch log files, collect log events, and
ship them to the monitoring cluster. Your recent logs are visible on the
*Monitoring* page in Kibana.

**Important:** If you're using Elastic Agent, do not deploy {filebeat} for log collection.
Instead, configure the Elasticsearch integration to collect logs.

. Verify that Elasticsearch is running and that the monitoring cluster is ready to
receive data from {filebeat}.
**Tip:** In production environments, we strongly recommend using a separate cluster 
(referred to as the _monitoring cluster_) to store the data. Using a separate 
monitoring cluster prevents production cluster outages from impacting your 
ability to access your monitoring data. It also prevents monitoring activities 
from impacting the performance of your production cluster. See
monitoring-production.

. Identify which logs you want to monitor. 
The {filebeat} Elasticsearch module can handle
audit logs,
deprecation logs,
gc logs, server logs, and 
slow logs.
For more information about the location of your Elasticsearch logs, see the
path.logs setting.

**Important:** If there are both structured (`*.json`) and unstructured (plain text)
versions of the logs, you must use the structured logs. Otherwise, they might
not appear in the appropriate context in Kibana.

. {filebeat-ref}/filebeat-installation-configuration.html[Install {filebeat}] on the Elasticsearch
nodes that contain logs that you want to monitor.

. Identify where to send the log data.
For example, specify Elasticsearch output information for your monitoring cluster in
the {filebeat} configuration file (`filebeat.yml`):

```yaml
output.elasticsearch:
  # Array of hosts to connect to.
  hosts: ["http://es-mon-1:9200", "http://es-mon-2:9200"] <1>

  # Optional protocol and basic auth credentials.
  #protocol: "https"
  #username: "elastic"
  #password: "changeme"
```
<1> In this example, the data is stored on a monitoring cluster with nodes 
`es-mon-1` and `es-mon-2`. 

If you configured the monitoring cluster to use encrypted communications, you
must access it via HTTPS. For example, use a `hosts` setting like
`https://es-mon-1:9200`.

**Important:** The Elasticsearch {monitor-features} use ingest pipelines, therefore the
cluster that stores the monitoring data must have at least one 
ingest node.
 
If Elasticsearch security features are enabled on the monitoring cluster, you must
provide a valid user ID and password so that {filebeat} can send metrics 
successfully. 

For more information about these configuration options, see 
{filebeat-ref}/elasticsearch-output.html[Configure the Elasticsearch output].

. Optional: Identify where to visualize the data.
{filebeat} provides example Kibana dashboards, visualizations and searches. To
load the dashboards into the appropriate Kibana instance, specify the
`setup.kibana` information in the {filebeat} configuration file
(`filebeat.yml`) on each node:

```yaml
setup.kibana:
  host: "localhost:5601"
  #username: "my_kibana_user"
  #password: "YOUR_PASSWORD"
```

**Tip:** In production environments, we strongly recommend using a dedicated Kibana 
instance for your monitoring cluster.

If security features are enabled, you must provide a valid user ID and
password so that {filebeat} can connect to Kibana: 

.. Create a user on the monitoring cluster that has the 
`kibana_admin` built-in role or equivalent
privileges.

.. Add the `username` and `password` settings to the Elasticsearch output information in 
the {filebeat} configuration file. The example shows a hard-coded password, but
you should store sensitive values in the
{filebeat-ref}/keystore.html[secrets keystore].

See {filebeat-ref}/setup-kibana-endpoint.html[Configure the Kibana endpoint].

. Enable the Elasticsearch module and set up the initial {filebeat} environment on each
node.
For example:

```
filebeat modules enable elasticsearch
filebeat setup -e
```

For more information, see  
{filebeat-ref}/filebeat-module-elasticsearch.html[Elasticsearch module]. 

. Configure the Elasticsearch module in {filebeat} on each node.
If the logs that you want to monitor aren't in the default location, set the
appropriate path variables in the `modules.d/elasticsearch.yml` file. See
{filebeat-ref}/filebeat-module-elasticsearch.html#configuring-elasticsearch-module[Configure the Elasticsearch module].

**Important:** If there are JSON logs, configure the `var.paths` settings to point
to them instead of the plain text logs.

. {filebeat-ref}/filebeat-starting.html[Start {filebeat}] on each node. 
**Note:** Depending on how you’ve installed {filebeat}, you might see errors related
to file ownership or permissions when you try to run {filebeat} modules. See
{beats-ref}/config-file-permissions.html[Config file ownership and permissions].

. Check whether the appropriate indices exist on the monitoring cluster.
For example, use the cat indices command to verify
that there are new `filebeat-*` indices. 

**Tip:** If you want to use the *Monitoring* UI in Kibana, there must also be 
`.monitoring-*` indices. Those indices are generated when you collect metrics
about Elastic Stack products. For example, see configuring-metricbeat.

. [View the monitoring data in Kibana](https://www.elastic.co/guide/en/kibana/8.19/monitoring-data.html).
