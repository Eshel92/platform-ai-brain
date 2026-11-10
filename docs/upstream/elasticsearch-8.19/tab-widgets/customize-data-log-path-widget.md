<!-- Converted from tab-widgets/customize-data-log-path-widget.asciidoc (AsciiDoc). Includes are inlined. -->

Linux and macOS installations support Unix-style paths:

```yaml
path:
  data: /var/data/elasticsearch
  logs: /var/log/elasticsearch
```

Windows installations support DOS paths with escaped backslashes:

```yaml
path:
  data: "C:\\Elastic\\Elasticsearch\\data"
  logs: "C:\\Elastic\\Elasticsearch\\logs"
```
