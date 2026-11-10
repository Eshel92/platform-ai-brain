<!-- Converted from monitoring/how-monitoring-works.asciidoc (AsciiDoc). Includes are inlined. -->

## How monitoring works

Each monitored Elastic Stack component is considered unique in the cluster based on
its persistent UUID, which is written to the `path.data`
directory when the node or instance starts.

Monitoring documents are just ordinary JSON documents built by monitoring each
Elastic Stack component at a specified collection interval. If you want to alter how
these documents are structured or stored, refer to config-monitoring-indices.

You can use Elastic Agent or {metricbeat} to collect monitoring data and to ship it
directly to the monitoring cluster.

To learn how to collect monitoring data, refer to:

* One of the following topics depending on how you want to collect monitoring
data from Elasticsearch:
** configuring-elastic-agent: Uses a single agent to
gather logs and metrics. Can be managed from a central location in Fleet.
** configuring-metricbeat: Uses a lightweight Beats
shipper to gather metrics. May be preferred if you have an existing investment
in Beats or are not yet ready to use Elastic Agent.
** collecting-monitoring-data: Uses internal exporters to
gather metrics. Not recommended. If you have previously configured legacy
collection methods, you should migrate to using Elastic Agent or {metricbeat}.
* [Monitoring Kibana](https://www.elastic.co/guide/en/kibana/8.19/xpack-monitoring.html)
* {logstash-ref}/configuring-logstash.html[Monitoring Logstash]
* {enterprise-search-ref}/monitoring.html[Monitoring {ents}]
* Monitoring Beats:
** {auditbeat-ref}/monitoring.html[{auditbeat}]
** {filebeat-ref}/monitoring.html[{filebeat}]
** {heartbeat-ref}/monitoring.html[{heartbeat}]
** {metricbeat-ref}/monitoring.html[{metricbeat}]
** {packetbeat-ref}/monitoring.html[{packetbeat}]
** {winlogbeat-ref}/monitoring.html[{winlogbeat}]
* {apm-guide-ref}/monitor-apm.html[Monitoring APM Server]
* {fleet-guide}/monitor-elastic-agent.html[Monitoring Elastic Agents]
Fleet-managed agents) or
{fleet-guide}/elastic-agent-monitoring-configuration.html[Configure monitoring for standalone Elastic Agents]
