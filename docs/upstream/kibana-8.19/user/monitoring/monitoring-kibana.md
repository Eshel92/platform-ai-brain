<!-- Converted from user/monitoring/monitoring-kibana.asciidoc (AsciiDoc). Includes are inlined. -->

# Collect monitoring data using legacy collectors

If you enable the Elastic {monitor-features} in your cluster, you can
optionally collect metrics about Kibana.

=========================
Elastic Agent and {metricbeat} are the recommended methods for collecting and shipping
monitoring data to a monitoring cluster.

If you have previously configured legacy collection methods, you should migrate
to using Elastic Agent or {metricbeat} collection. Do not use legacy collection
alongside other collection methods.

For more information, refer to monitoring-elastic-agent and
monitoring-metricbeat.
=========================

The following method involves sending the metrics to the production cluster,
which ultimately routes them to the monitoring cluster.

To learn about monitoring in general, see
[Monitor a cluster](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/monitor-elasticsearch-cluster.html).

. Set the `xpack.monitoring.collection.enabled` setting to `true` on each
node in the production cluster. By default, it is is disabled (`false`).
**Note:** You can specify this setting in either the `elasticsearch.yml` on each
node or across the cluster as a dynamic cluster setting. If
{stack-security-features} are enabled, you must have `monitor` cluster
privileges to view the cluster settings and `manage` cluster privileges to
change them.

** To update the cluster settings in Kibana:

... Open Kibana in your web browser.
By default, if you are running Kibana locally, go to `http://localhost:5601/`.

If security features are enabled, log in.

... Go to the *Stack Monitoring* page using the 
global search field. If data collection is
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

. Verify that `monitoring.enabled` and
`monitoring.kibana.collection.enabled` are set to `true` in the
`kibana.yml` file. These are the default values. For
more information, see Monitoring settings in Kibana.

. Identify where to send monitoring data. Kibana automatically
sends metrics to the Elasticsearch cluster specified in the `elasticsearch.hosts` setting
in the `kibana.yml` file. This property has a default value of
`http://localhost:9200`. +
===============================
In production environments, we strongly recommend using a separate cluster
(referred to as the _monitoring cluster_) to store the data. Using a separate
monitoring cluster prevents production cluster outages from impacting your
ability to access your monitoring data. It also prevents monitoring activities
from impacting the performance of your production cluster.

If security features are enabled on the production cluster, use an HTTPS
URL such as `<PRODUCTION_CLUSTER_URL>:9200` in this setting.
===============================

. If security features are enabled on the production cluster:

.. Verify that there is a
valid user ID and password in the `elasticsearch.username` and
`elasticsearch.password` settings in the `kibana.yml` file. These values are
used when Kibana sends monitoring data to the production cluster.

.. Configure encryption for traffic between Kibana and Elasticsearch.

. Start Kibana.

. View the monitoring data in Kibana.
