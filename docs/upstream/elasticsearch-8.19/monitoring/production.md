<!-- Converted from monitoring/production.asciidoc (AsciiDoc). Includes are inlined. -->

## Monitoring in a production environment

In production, you should send monitoring data to a separate _monitoring cluster_
so that historical data is available even when the nodes you are monitoring are
not.

=========================
Elastic Agent and {metricbeat} are the recommended methods for collecting and shipping
monitoring data to a monitoring cluster.

If you have previously configured legacy collection methods, you should migrate
to using Elastic Agent or
{metricbeat} collection. Do not use legacy collection
alongside other collection methods.
=========================

If you have at least a Gold Subscription, using a dedicated monitoring cluster
also enables you to monitor multiple clusters from a central location.

To store monitoring data in a separate cluster:

. Set up the Elasticsearch cluster you want to use as the monitoring cluster.
For example, you might set up a two host cluster with the nodes `es-mon-1` and
`es-mon-2`.
===============================
* Ideally the monitoring cluster and the production cluster run on the same
Elastic Stack version. However, a monitoring cluster on the latest release of
{major-version} also works with production clusters that use the same major
version. Monitoring clusters that use {major-version} also work with production
clusters that use the latest release of {prev-major-version}.
* There must be at least one ingest node in the monitoring
cluster; it does not need to be a dedicated ingest node.
===============================

.. (Optional) Verify that the collection of monitoring data is disabled on the
monitoring cluster. By default, the `xpack.monitoring.collection.enabled` setting
is `false`.
For example, you can use the following APIs to review and change this setting:

```console
GET _cluster/settings

PUT _cluster/settings
{
  "persistent": {
    "xpack.monitoring.collection.enabled": false
  }
}
```

.. If the Elasticsearch security features are enabled on the monitoring cluster, create
users that can send and retrieve monitoring data:
**Note:** If you plan to use Kibana to view monitoring data, username and password
credentials must be valid on both the Kibana server and the monitoring cluster.

*** If you plan to use Elastic Agent,
create a user that has the `remote_monitoring_collector`
built-in role and that the
monitoring related {fleet-guide}/install-uninstall-integration-assets.html#install-integration-assets[integration assets have been installed]
on the remote monitoring cluster. 

*** If you plan to use {metricbeat},
create a user that has the `remote_monitoring_collector` built-in role and a
user that has the `remote_monitoring_agent`
built-in role. Alternatively, use the
`remote_monitoring_user` built-in user.

*** If you plan to use HTTP exporters to route data through your production
cluster, create a user that has the `remote_monitoring_agent`
built-in role.
For example, the
following request creates a `remote_monitor` user that has the
`remote_monitoring_agent` role:

```console
POST /_security/user/remote_monitor
{
  "password" : "changeme",
  "roles" : [ "remote_monitoring_agent"],
  "full_name" : "Internal Agent For Remote Monitoring"
}
```

Alternatively, use the `remote_monitoring_user` built-in user.

. Configure your production cluster to collect data and send it to the
monitoring cluster:
** Elastic Agent collection methods
** {metricbeat} collection methods
** Legacy collection methods

. (Optional)
{logstash-ref}/configuring-logstash.html[Configure Logstash to collect data and send it to the monitoring cluster].

. (Optional) {enterprise-search-ref}/monitoring.html[Configure {ents} monitoring].

. (Optional) Configure the Beats to collect data and send it to the monitoring
cluster. Skip this step for Beats that are managed by Elastic Agent.
** {auditbeat-ref}/monitoring.html[Auditbeat]
** {filebeat-ref}/monitoring.html[Filebeat]
** {heartbeat-ref}/monitoring.html[Heartbeat]
** {metricbeat-ref}/monitoring.html[Metricbeat]
** {packetbeat-ref}/monitoring.html[Packetbeat]
** {winlogbeat-ref}/monitoring.html[Winlogbeat]

. (Optional) {apm-guide-ref}/monitor-apm.html[Configure APM Server monitoring]

. (Optional) Configure Kibana to collect data and send it to the monitoring cluster:
** [Elastic Agent collection methods](https://www.elastic.co/guide/en/kibana/8.19/monitoring-elastic-agent.html)
** [{metricbeat} collection methods](https://www.elastic.co/guide/en/kibana/8.19/monitoring-metricbeat.html)
** [Legacy collection methods](https://www.elastic.co/guide/en/kibana/8.19/monitoring-kibana.html)

. (Optional) Create a dedicated Kibana instance for monitoring, rather than using
a single Kibana instance to access both your production cluster and monitoring
cluster.
**Note:** If you log in to Kibana using SAML, Kerberos, PKI, OpenID Connect, or token
authentication providers, a dedicated Kibana instance is *required*. The security
tokens that are used in these contexts are cluster-specific; therefore you
cannot use a single Kibana instance to connect to both production and monitoring
clusters.

.. (Optional) Disable the collection of monitoring data in this Kibana instance.
Set the `xpack.monitoring.kibana.collection.enabled` setting to `false` in the
`kibana.yml` file. For more information about this setting, see
[Monitoring settings in Kibana](https://www.elastic.co/guide/en/kibana/8.19/monitoring-settings-kb.html).

. [Configure Kibana to retrieve and display the monitoring data](https://www.elastic.co/guide/en/kibana/8.19/monitoring-data.html).
