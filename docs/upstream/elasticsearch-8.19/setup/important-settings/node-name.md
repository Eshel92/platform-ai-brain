<!-- Converted from setup/important-settings/node-name.asciidoc (AsciiDoc). Includes are inlined. -->

Elasticsearch uses `node.name` as a human-readable identifier for a
particular instance of Elasticsearch. This name is included in the response
of many APIs. The node name defaults to the hostname of the machine when
Elasticsearch starts, but can be configured explicitly in
`elasticsearch.yml`:

```yaml
node.name: prod-data-2
```
