<!-- Converted from setup/install/xpack-indices.asciidoc (AsciiDoc). Includes are inlined. -->

Some commercial features automatically create indices within Elasticsearch.
By default, Elasticsearch is configured to allow automatic index creation, and no
additional steps are required. However, if you have disabled automatic index
creation in Elasticsearch, you must configure
`action.auto_create_index` in `elasticsearch.yml` to allow
the commercial features to create the following indices:

```yaml
action.auto_create_index: .monitoring*,.watches,.triggered_watches,.watcher-history*,.ml*
```

=============================================================================
If you are using [Logstash](https://www.elastic.co/products/logstash)
or [Beats](https://www.elastic.co/products/beats) then you will most likely
require additional index names in your `action.auto_create_index` setting, and
the exact value will depend on your local configuration. If you are unsure of
the correct value for your environment, you may consider setting the value to
 `*` which will allow automatic creation of all indices.
=============================================================================
