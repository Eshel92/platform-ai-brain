<!-- Converted from monitoring/configuring-metricbeat.asciidoc (AsciiDoc). Includes are inlined. -->

## Collecting Elasticsearch monitoring data with {metricbeat}

In 6.5 and later, you can use {metricbeat} to collect data about Elasticsearch 
and ship it to the monitoring cluster, rather than routing it through exporters 
as described in collecting-monitoring-data.

Want to use Elastic Agent instead? Refer to configuring-elastic-agent.

(Figure: monitoring/images/metricbeat.png)

. {metricbeat-ref}/metricbeat-installation-configuration.html[Install
{metricbeat}]. Ideally install a single {metricbeat} instance configured with
`scope: cluster` and configure `hosts` to point to an endpoint (e.g. a
load-balancing proxy) which directs requests to the master-ineligible nodes in
the cluster. If this is not possible then install one {metricbeat} instance for
each Elasticsearch node in the production cluster and use the default `scope: node`.
When {metricbeat} is monitoring Elasticsearch with `scope: node` then you must install a
{metricbeat} instance for each Elasticsearch node. If you don't, some metrics will not
be collected. {metricbeat} with `scope: node` collects most of the metrics from
the elected master of the cluster, so you must scale up all your
master-eligible nodes to account for this extra load and you should not use
this mode if you have dedicated master nodes.

. Enable the Elasticsearch module in {metricbeat} on each Elasticsearch node.
For example, to enable the default configuration for the {stack-monitor-features}
in the `modules.d` directory, run the following command:

```
metricbeat modules enable elasticsearch-xpack
```

For more information, refer to 
{metricbeat-ref}/metricbeat-module-elasticsearch.html[Elasticsearch module]. 

. Configure the Elasticsearch module in {metricbeat} on each Elasticsearch node.
The `modules.d/elasticsearch-xpack.yml` file contains the following settings:

```yaml
  - module: elasticsearch
    xpack.enabled: true
    period: 10s
    hosts: ["http://localhost:9200"] <1>
    #scope: node <2>
    #username: "user"
    #password: "secret"
    #ssl.enabled: true
    #ssl.certificate_authorities: ["/etc/pki/root/ca.pem"]
    #ssl.certificate: "/etc/pki/client/cert.pem"
    #ssl.key: "/etc/pki/client/cert.key"
    #ssl.verification_mode: "full"
```
<1> By default, the module collects Elasticsearch monitoring metrics from
`http://localhost:9200`. If that host and port number are not correct, you must
update the `hosts` setting. If you configured Elasticsearch to use encrypted
communications, you must access it via HTTPS. For example, use a `hosts` setting
like `https://localhost:9200`.
<2> By default, `scope` is set to `node` and each entry in the `hosts` list
indicates a distinct node in an Elasticsearch cluster. If you set `scope` to `cluster`
then each entry in the `hosts` list indicates a single endpoint for a distinct
Elasticsearch cluster (for example, a load-balancing proxy fronting the cluster). You
should use `scope: cluster` if the cluster has dedicated master nodes, and
configure the endpoint in the `hosts` list not to direct requests to the
dedicated master nodes.

If Elastic security features are enabled, you must also provide a user ID
and password so that {metricbeat} can collect metrics successfully: 

.. Create a user on the production cluster that has the
`remote_monitoring_collector` built-in role. 
Alternatively, use the
`remote_monitoring_user` built-in user.

.. Add the `username` and `password` settings to the Elasticsearch module configuration
file. 

.. If TLS is enabled on the HTTP layer of your Elasticsearch cluster, you must either use https as the URL scheme in the `hosts` setting or add the `ssl.enabled: true` setting. Depending on the TLS configuration of your Elasticsearch cluster, you might also need to specify {metricbeat-ref}/configuration-ssl.html[additional ssl.*] settings.

. Optional: Disable the system module in {metricbeat}.
By default, the {metricbeat-ref}/metricbeat-module-system.html[system module] is
enabled. The information it collects, however, is not shown on the *Monitoring*
page in Kibana. Unless you want to use that information for other purposes, run
the following command:

```
metricbeat modules disable system
```

. Identify where to send the monitoring data.
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
  hosts: ["<ES_MONITORING_HOST1_URL>:9200", "<ES_MONITORING_HOST2_URL>:9200"] <1>
  
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
provide a valid user ID and password so that {metricbeat} can send metrics 
successfully: 

.. Create a user on the monitoring cluster that has the 
`remote_monitoring_agent` built-in role. 
Alternatively, use the 
`remote_monitoring_user` built-in user.

.. Add the `username` and `password` settings to the Elasticsearch output information in 
the {metricbeat} configuration file.

For more information about these configuration options, see 
{metricbeat-ref}/elasticsearch-output.html[Configure the Elasticsearch output].

. {metricbeat-ref}/metricbeat-starting.html[Start {metricbeat}] on each node. 

. [View the monitoring data in Kibana](https://www.elastic.co/guide/en/kibana/8.19/monitoring-data.html).
