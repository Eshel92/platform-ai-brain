<!-- Converted from security/ccs-clients-integrations/monitoring.asciidoc (AsciiDoc). Includes are inlined. -->

### Monitoring and security

The Elastic Stack {monitor-features} consist of two components:
an agent that you install on each Elasticsearch and Logstash node, and a Monitoring UI
in Kibana. The monitoring agent collects and indexes metrics from the nodes
and you visualize the data through the Monitoring dashboards in Kibana. The agent
can index data on the same Elasticsearch cluster, or send it to an external
monitoring cluster.

To use the {monitor-features} with the security features enabled, you need to
[set up Kibana to work with the security features](https://www.elastic.co/guide/en/kibana/8.19/using-kibana-with-security.html)
and create at least one user for the Monitoring UI. If you are using an external
monitoring cluster, you also need to configure a user for the monitoring agent
and configure the agent to use the appropriate credentials when communicating
with the monitoring cluster.

For more information, see:

* monitoring-production
* [Configuring monitoring in Kibana](https://www.elastic.co/guide/en/kibana/8.19/monitoring-xpack-kibana.html)
* {logstash-ref}/configuring-logstash.html[Configuring monitoring for Logstash nodes]
