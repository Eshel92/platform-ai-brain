<!-- Converted from user/monitoring/xpack-monitoring.asciidoc (AsciiDoc). Includes are inlined. -->

# Stack Monitoring

The Kibana {monitor-features} serve two separate purposes:

. To visualize monitoring data from across the Elastic Stack. You can view health and 
performance data for Elasticsearch, Logstash, {ents}, APM, and Beats in real time,
as well as analyze past performance. 
. To monitor Kibana itself and route that data to the monitoring cluster.

If you enable monitoring across the Elastic Stack, each monitored component is
considered unique based on its persistent UUID, which is written to the
`path.data` directory when the node or instance starts. 

For more information, see configuring-monitoring and 
[Monitor a cluster](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/monitor-elasticsearch-cluster.html).

Want to monitor your fleet of Elastic Agents, too? Use Fleet instead of the Stack
Monitoring UI. To learn more, refer to
{fleet-guide}/monitor-elastic-agent.html[Monitor Elastic Agents].
