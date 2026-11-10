<!-- Converted from setup/important-settings/network-host.asciidoc (AsciiDoc). Includes are inlined. -->

#### Network host setting

By default, Elasticsearch only binds to loopback addresses such as `127.0.0.1` and
`[::1]`. This is sufficient to run a cluster of one or more nodes on a single
server for development and testing, but a
resilient production cluster must involve
nodes on other servers. There are many network settings but
usually all you need to configure is `network.host`:

```yaml
network.host: 192.168.1.10
```

**Important:** When you provide a value for `network.host`, Elasticsearch assumes that you
are moving from development mode to production mode, and upgrades a number of
system startup checks from warnings to exceptions. See the differences between
development and production modes.
