<!-- Converted from tab-widgets/jvm-memory-pressure-widget.asciidoc (AsciiDoc). Includes are inlined. -->

From your deployment menu, click **Elasticsearch**. Under **Instances**, each
instance displays a **JVM memory pressure** indicator. When the JVM memory
pressure reaches 75%, the indicator turns red.

You can also use the nodes stats API to calculate the
current JVM memory pressure for each node.

```console
GET _nodes/stats?filter_path=nodes.*.jvm.mem.pools.old
```

Use the response to calculate memory pressure as follows:

JVM Memory Pressure = `used_in_bytes` / `max_in_bytes`

To calculate the current JVM memory pressure for each node, use the
nodes stats API.

```console
GET _nodes/stats?filter_path=nodes.*.jvm.mem.pools.old
```

Use the response to calculate memory pressure as follows:

JVM Memory Pressure = `used_in_bytes` / `max_in_bytes`
