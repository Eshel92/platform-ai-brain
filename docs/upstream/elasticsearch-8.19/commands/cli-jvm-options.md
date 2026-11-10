<!-- Converted from commands/cli-jvm-options.asciidoc (AsciiDoc). Includes are inlined. -->

#### JVM options

CLI tools run with 64MB of heap. For most tools, this value is fine. However, if
needed this can be overridden by setting the `CLI_JAVA_OPTS` environment variable.
For example, the following increases the heap size used by the
`pass:a[elasticsearch-{tool-name}]` tool to 1GB.

```shell
export CLI_JAVA_OPTS="-Xmx1g"
bin/elasticsearch-{tool-name} ...
```
