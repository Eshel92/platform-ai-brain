<!-- Converted from tab-widgets/multi-data-path-widget.asciidoc (AsciiDoc). Includes are inlined. -->

Linux and macOS installations support multiple Unix-style paths in `path.data`:

```yaml
path:
  data:
    - /mnt/elasticsearch_1
    - /mnt/elasticsearch_2
    - /mnt/elasticsearch_3
```

Windows installations support multiple DOS paths in `path.data`:

```yaml
path:
  data:
    - "C:\\Elastic\\Elasticsearch_1"
    - "E:\\Elastic\\Elasticsearch_1"
    - "F:\\Elastic\\Elasticsearch_3"
```
