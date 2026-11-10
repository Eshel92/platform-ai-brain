<!-- Converted from commands/reconfigure-node.asciidoc (AsciiDoc). Includes are inlined. -->

## elasticsearch-reconfigure-node

The `elasticsearch-reconfigure-node` tool reconfigures an Elasticsearch node that was installed
through an RPM or DEB package to join an existing cluster with security features enabled.

### Synopsis

```shell
bin/elasticsearch-reconfigure-node
[--enrollment-token] [-h, --help] [-E <KeyValuePair>]
[-s, --silent] [-v, --verbose]
```

### Description

When installing Elasticsearch with a DEB or RPM package, the current node is assumed to
be the first node in the cluster. Elasticsearch enables and configures security 
features on the node, generates a password for the `elastic` superuser, and 
configures TLS for the HTTP and transport layers.

Rather than form a single-node cluster, you can add a node to an existing 
cluster where security features are already enabled and configured. Before 
starting your new node, run the 
`elasticsearch-create-enrollment-token` tool
with the `-s node` option to generate an enrollment token on any node in your
existing cluster. On your new node, run the
`elasticsearch-reconfigure-node` tool and pass the enrollment token as a
parameter.

**Note:** This tool is intended only for use on DEB or RPM distributions of Elasticsearch.

You must run this tool with `sudo` so that it can edit the necessary
files in your Elasticsearch installation configuration directory that are owned by
`root:elasticsearch`.

### Parameters

`--enrollment-token`:: The enrollment token, which can be generated on any of the
nodes in an existing, secured cluster.

`-E <KeyValuePair>`:: Configures a standard Elasticsearch or X-Pack setting.

`-h, --help`:: Shows help information.

`-s, --silent`:: Shows minimal output.

`-v, --verbose`:: Shows verbose output.

(See `commands/cli-jvm-options.md`)
:!tool-name:

### Examples

The following example reconfigures an installed Elasticsearch node so that it can join an existing cluster when it starts for the first time.
```shell
sudo /usr/share/elasticsearch/elasticsearch-reconfigure-node --enrollment-token eyJ2ZXIiOiI4LjAuMCIsImFkciI6WyIxOTIuMTY4LjEuMTY6OTIwMCJdLCJmZ3IiOiI4NGVhYzkyMzAyMWQ1MjcyMmQxNTFhMTQwZmM2ODI5NmE5OWNiNmU0OGVhZjYwYWMxYzljM2I3ZDJjOTg2YTk3Iiwia2V5IjoiUy0yUjFINEJrNlFTMkNEY1dVV1g6QS0wSmJxM3hTRy1haWxoQTdPWVduZyJ9
```
