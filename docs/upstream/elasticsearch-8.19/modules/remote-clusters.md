<!-- Converted from modules/remote-clusters.asciidoc (AsciiDoc). Includes are inlined. -->

## Remote clusters

You can connect a local cluster to other Elasticsearch clusters, known as _remote
clusters_. Remote clusters can be located in different datacenters or
geographic regions, and contain indices or data streams that can be replicated
with cross-cluster replication or searched by a local cluster using cross-cluster search.

### Cross-cluster replication

With cross-cluster replication, you ingest data to an index on a remote cluster. This
_leader_ index is replicated to one or more read-only _follower_ indices on your
local cluster. Creating a multi-cluster architecture with cross-cluster replication enables you to
configure disaster recovery, bring data closer to your users, or establish a
centralized reporting cluster to process reports locally.

### Cross-cluster search

Cross-cluster search enables you to run a search request
against one or more remote clusters. This capability provides each region with a
global view of all clusters, allowing you to send a search request from a local
cluster and return results from all connected remote clusters. For full cross-cluster search
capabilities, the local and remote cluster must be on the same
{subscriptions}[subscription level].

### Add remote clusters

**Note:** The instructions that follow describe how to create a remote connection from a
self-managed cluster. You can also set up cross-cluster search and cross-cluster replication from an
[Elasticsearch Service deployment](https://www.elastic.co/guide/en/cloud/current/ec-enable-ccs.html)
or from an [Elastic Cloud Enterprise deployment](https://www.elastic.co/guide/en/cloud-enterprise/current/ece-enable-ccs.html).

To add remote clusters, you can choose between
two security models and
two connection modes. Both security models are compatible
with either of the connection modes.

#### Security models

API key based security model::
For clusters on version 8.14 or later, you can use an API key to authenticate
and authorize cross-cluster operations to a remote cluster. This model offers
administrators of both the local and the remote cluster fine-grained access
controls. remote-clusters-api-key.

Certificate based security model::
Uses mutual TLS authentication for cross-cluster operations. User authentication
is performed on the local cluster and a user's role names are passed to the
remote cluster. In this model, a superuser on the local cluster gains total read
access to the remote cluster, so it is only suitable for clusters that are in
the same security domain. remote-clusters-cert.

#### Connection modes

Sniff mode::
In sniff mode, a cluster alias is registered with a name of your choosing and a
list of addresses of _seed_ nodes specified with the
`cluster.remote.<cluster_alias>.seeds` setting. When you register a remote
cluster using sniff mode, Elasticsearch retrieves from one of the seed nodes the
addresses of up to three _gateway nodes_. Each `remote_cluster_client` node in
the local Elasticsearch cluster then opens several TCP connections to the publish
addresses of the gateway nodes. This mode therefore requires that the gateway
nodes' publish addresses are accessible to nodes in the local cluster.
Sniff mode is the default connection mode. See remote-cluster-sniff-settings
for more information about configuring sniff mode.
The _gateway nodes_ selection depends on the following criteria:
* *version*: Remote nodes must be compatible with the cluster they are
registered to.
* *role*: By default, any non-master-eligible node can act as a
gateway node. Dedicated master nodes are never selected as gateway nodes.
* *attributes*: You can define the gateway nodes for a cluster by setting
`cluster.remote.node.attr.gateway` to `true`.
However, such nodes still have to satisfy the two above requirements.

Proxy mode::
In proxy mode, a cluster alias is registered with a name of your choosing and
the address of a TCP (layer 4) reverse proxy specified with the
`cluster.remote.<cluster_alias>.proxy_address` setting. You must configure this
proxy to route connections to one or more nodes of the remote cluster. When you
register a remote cluster using proxy mode, Elasticsearch opens several TCP connections
to the proxy address and uses these connections to communicate with the remote
cluster. In proxy mode Elasticsearch disregards the publish addresses of the remote
cluster nodes which means that the publish addresses of the remote cluster
nodes need not be accessible to the local cluster.
Proxy mode is not the default connection mode, so you must set
`cluster.remote.<cluster_alias>.mode: proxy` to use it. See
remote-cluster-proxy-settings for more information about configuring proxy
mode.
Proxy mode has the same <<gateway-nodes-selection, version compatibility
requirements>> as sniff mode.

(See `modules/cluster/remote-clusters-api-key.md`)
(See `modules/cluster/remote-clusters-cert.md`)
(See `modules/cluster/remote-clusters-migration.md`)
(See `modules/cluster/remote-clusters-settings.md`)
(See `modules/cluster/remote-clusters-troubleshooting.md`)
