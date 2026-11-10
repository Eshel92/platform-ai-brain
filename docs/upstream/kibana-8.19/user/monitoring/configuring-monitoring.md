<!-- Converted from user/monitoring/configuring-monitoring.asciidoc (AsciiDoc). Includes are inlined. -->

# Configure monitoring in Kibana

If you enable the {monitor-features} in your cluster, there are a few methods
available to collect metrics about Kibana:

* Elastic Agent collection: Uses a single agent to gather
logs and metrics. Can be managed from a central location in Fleet.

* {metricbeat} collection: Uses a lightweight Beats
shipper to gather metrics. May be preferred if you have an existing investment
in Beats or are not yet ready to use Elastic Agent.

* Legacy collection: Uses internal collectors to gather
metrics. Not recommended. If you have previously configured legacy collection
methods, you should migrate to using Elastic Agent or {metricbeat}.

You can also use Kibana to
visualize monitoring data from across the Elastic Stack.

To learn about monitoring in general, see
[Monitor a cluster](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/monitor-elasticsearch-cluster.html).
