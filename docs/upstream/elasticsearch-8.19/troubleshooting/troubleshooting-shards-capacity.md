<!-- Converted from troubleshooting/troubleshooting-shards-capacity.asciidoc (AsciiDoc). Includes are inlined. -->

## Troubleshooting shards capacity health issues

Elasticsearch limits the maximum number of shards to be held per node using the
`cluster.max_shards_per_node` and
`cluster.max_shards_per_node.frozen` settings.
The current shards capacity of the cluster is available in the
health API shards capacity section.

(See `tab-widgets/troubleshooting/troubleshooting-shards-capacity-widget.md`)
****
If you're using Elastic Cloud Hosted, then you can use AutoOps to monitor your cluster. AutoOps significantly simplifies cluster management with performance recommendations, resource utilization visibility, real-time issue detection and resolution paths. For more information, refer to [Monitor with AutoOps](https://www.elastic.co/guide/en/cloud/current/ec-autoops.html).
****
