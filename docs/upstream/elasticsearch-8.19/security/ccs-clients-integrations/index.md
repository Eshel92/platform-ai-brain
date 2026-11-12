<!-- Converted from security/ccs-clients-integrations/index.asciidoc (AsciiDoc). Includes are inlined. -->

## Securing clients and integrations

You will need to update the configuration for several clients
to work with a secured Elasticsearch cluster.

The Elasticsearch security features enable you to secure your Elasticsearch cluster. But
Elasticsearch itself is only one product within the Elastic Stack. It is often the case that
other products in the Elastic Stack are connected to the cluster and therefore need to
be secured as well, or at least communicate with the cluster in a secured way:

* Apache Hadoop
* {auditbeat-ref}/securing-auditbeat.html[Auditbeat]
* {filebeat-ref}/securing-filebeat.html[Filebeat]
* {fleet-guide}/secure.html[Fleet & Elastic Agent]
* {heartbeat-ref}/securing-heartbeat.html[Heartbeat]
* [Kibana](https://www.elastic.co/guide/en/kibana/8.19/using-kibana-with-security.html)
* {logstash-ref}/ls-security.html[Logstash]
* {metricbeat-ref}/securing-metricbeat.html[Metricbeat]
* secure-monitoring
* {packetbeat-ref}/securing-packetbeat.html[Packetbeat]
* [Reporting](https://www.elastic.co/guide/en/kibana/8.19/secure-reporting.html)
* {winlogbeat-ref}/securing-winlogbeat.html[Winlogbeat]

(See `security/ccs-clients-integrations/http.md`)
(See `security/ccs-clients-integrations/hadoop.md`)
(See `security/ccs-clients-integrations/monitoring.md`)
