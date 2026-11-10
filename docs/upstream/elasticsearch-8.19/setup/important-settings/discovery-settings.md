<!-- Converted from setup/important-settings/discovery-settings.asciidoc (AsciiDoc). Includes are inlined. -->

#### Discovery and cluster formation settings

Configure two important discovery and cluster formation settings before going
to production so that nodes in the cluster can discover each other and elect a
master node.

##### `discovery.seed_hosts`

Out of the box, without any network configuration, Elasticsearch will bind to
the available loopback addresses and scan local ports `9300` to `9305` to
connect with other nodes running on the same server. This behavior provides an
auto-clustering experience without having to do any configuration.

When you want to form a cluster with nodes on other hosts, use the
static `discovery.seed_hosts` setting. This setting
provides a list of other nodes in the cluster
that are master-eligible and likely to be live and contactable to seed
the discovery process. This setting
accepts a YAML sequence or array of the addresses of all the master-eligible
nodes in the cluster. Each address can be either an IP address or a hostname
that resolves to one or more IP addresses via DNS.

```yaml
discovery.seed_hosts:
   - 192.168.1.10:9300
   - 192.168.1.11 <1>
   - seeds.mydomain.com <2>
   - [0:0:0:0:0:ffff:c0a8:10c]:9301 <3>
```
<1> The port is optional and defaults to `9300`, but can
    be overridden.
<2> If a hostname resolves to multiple IP addresses, the node will attempt to
    discover other nodes at all resolved addresses.
<3> IPv6 addresses must be enclosed in square brackets.

If your master-eligible nodes do not have fixed names or addresses, use an
alternative hosts provider to find their addresses
dynamically.

##### `cluster.initial_master_nodes`

When you start an Elasticsearch cluster for the first time, a
cluster bootstrapping step
determines the set of master-eligible nodes whose votes are counted in the
first election. In development mode, with no discovery
settings configured, this step is performed automatically by the nodes
themselves.

Because auto-bootstrapping is inherently unsafe,
when starting a new cluster in production mode, you must explicitly list the
master-eligible nodes whose votes should be counted in the very first election.
You set this list using the `cluster.initial_master_nodes` setting on every
master-eligible node. Do not configure this setting on master-ineligible nodes.

**Important:** After the cluster forms successfully for the first time, remove the
`cluster.initial_master_nodes` setting from each node's configuration and never
set it again for this cluster. Do not configure this setting on nodes joining
an existing cluster. Do not configure this setting on nodes which are
restarting. Do not configure this setting when performing a full-cluster
restart. See modules-discovery-bootstrap-cluster.

```yaml
discovery.seed_hosts:
   - 192.168.1.10:9300
   - 192.168.1.11
   - seeds.mydomain.com
   - [0:0:0:0:0:ffff:c0a8:10c]:9301
cluster.initial_master_nodes: <1>
   - master-node-a
   - master-node-b
   - master-node-c
```
<1> Identify the initial master nodes by their `node.name`, which
defaults to their hostname. Ensure that the value in
`cluster.initial_master_nodes` matches the `node.name` exactly. If you use a
fully-qualified domain name (FQDN) such as `master-node-a.example.com` for your
node names, then you must use the FQDN in this list. Conversely, if `node.name`
is a bare hostname without any trailing qualifiers, you must also omit the
trailing qualifiers in `cluster.initial_master_nodes`.

See bootstrapping a cluster and
discovery and cluster formation settings.
