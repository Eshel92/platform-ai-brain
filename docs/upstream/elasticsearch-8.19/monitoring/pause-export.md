<!-- Converted from monitoring/pause-export.asciidoc (AsciiDoc). Includes are inlined. -->

### Pausing data collection

To stop generating {monitoring} data in Elasticsearch, disable data collection:

```yaml
xpack.monitoring.collection.enabled: false
```

When this setting is `false`, Elasticsearch monitoring data is not collected and all 
monitoring data from other sources such as Kibana, Beats, and Logstash is ignored.

You can update this setting by using the 
[Cluster Update Settings API](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/cluster-update-settings.html).

If you want to collect data from sources such as Kibana, Beats, and Logstash but
not collect data about your Elasticsearch cluster, you can disable data collection
just for Elasticsearch:

```yaml
xpack.monitoring.collection.enabled: true
xpack.monitoring.elasticsearch.collection.enabled: false
```

If you want to separately disable a specific exporter, you can specify the 
`enabled` setting (which defaults to `true`) per exporter. For example:

```yaml
xpack.monitoring.exporters.my_http_exporter:
  type: http
  host: ["10.1.2.3:9200", "10.1.2.4:9200"]
  enabled: false <1>
```
<1> Disable the named exporter. If the same name as an existing exporter is not
    used, then this will create a completely new exporter that is completely
    ignored. This value can be set dynamically by using cluster settings.

**Note:** Defining a disabled exporter prevents the default exporter from being
      created.

To re-start data collection, re-enable these settings.
