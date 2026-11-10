<!-- Converted from monitoring/troubleshooting.asciidoc (AsciiDoc). Includes are inlined. -->

## Troubleshooting monitoring

Use the information in this section to troubleshoot common problems and find
answers for frequently asked questions. See also
{logstash-ref}/monitoring-troubleshooting.html[Troubleshooting monitoring in Logstash].

For issues that you cannot fix yourself … we’re here to help.
If you are an existing Elastic customer with a support contract, please create
a ticket in the
[Elastic Support portal](https://support.elastic.co/customers/s/login/).
Or post in the [Elastic forum](https://discuss.elastic.co/).

### No monitoring data is visible in Kibana

*Symptoms*:
There is no information about your cluster on the *Stack Monitoring* page in
Kibana.

*Resolution*:
Check whether the appropriate indices exist on the monitoring cluster. For
example, use the cat indices command to verify that
there is a `.monitoring-kibana*` index for your Kibana monitoring data and a
`.monitoring-es*` index for your Elasticsearch monitoring data. If you are collecting
monitoring data by using {metricbeat} the indices have `-mb` in their names. If
the indices do not exist, review your configuration. For example, see
monitoring-production.

### Monitoring data for some Elastic Stack nodes or instances is missing from Kibana

*Symptoms*:
The *Stack Monitoring* page in Kibana does not show information for some nodes or 
instances in your cluster.

*Resolution*:
Verify that the missing items have unique UUIDs. Each Elasticsearch node, Logstash node,
Kibana instance, Beat instance, and APM Server is considered unique based on its
persistent UUID, which is found in its `path.data` directory. Alternatively, you
can find the UUIDs in the product logs at startup.

In some cases, you can also retrieve this information via APIs:

* For Beat instances, use the HTTP endpoint to retrieve the `uuid` property.
For example, refer to
{filebeat-ref}/http-endpoint.html[Configure an HTTP endpoint for {filebeat} metrics].
* For Kibana instances, use the
[status endpoint](https://www.elastic.co/guide/en/kibana/8.19/access.html#status) to retrieve the `uuid` property.
* For Logstash nodes, use the
{logstash-ref}/monitoring-logstash.html[monitoring APIs root resource] to
retrieve the `id` property.

**Tip:** When you install Elasticsearch, Logstash, Kibana, APM Server, or Beats, their `path.data`
directory should be non-existent or empty; do not copy this directory from other
installations.
