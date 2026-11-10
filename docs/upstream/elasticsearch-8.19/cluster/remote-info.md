<!-- Converted from cluster/remote-info.asciidoc (AsciiDoc). Includes are inlined. -->

### Remote cluster info API

**New API reference**
For the most up-to-date API details, refer to [Cluster APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-cluster).

Returns configured remote cluster information.

#### Request

`GET /_remote/info`

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the `monitor` or
`manage` cluster privilege to use this API.

#### Description

The cluster remote info API allows you to retrieve information about configured
remote clusters. It returns connection and endpoint information keyed
by the configured remote cluster alias.

**Tip:** This API returns information that reflects current state on the local cluster.
The `connected` field does not necessarily reflect whether a remote cluster is
down or unavailable, only whether there is currently an open connection to it.
Elasticsearch does not spontaneously try to reconnect to a disconnected remote
cluster. To trigger a reconnection, attempt a cross-cluster search,
ES|QL cross-cluster search, or try the
resolve cluster endpoint.

#### Response body

`mode`::
    Connection mode for the remote cluster. Returned values are `sniff` and
    `proxy`.

`connected`::
    True if there is at least one open connection to the remote cluster. When
    false, it means that the cluster no longer has an open connection to the
    remote cluster. It does not necessarily mean that the remote cluster is
    down or unavailable, just that at some point a connection was lost.

`initial_connect_timeout`::
	The initial connect timeout for remote cluster connections.

`skip_unavailable`::
Whether a cross-cluster search skips the remote cluster if its nodes are unavailable during the
search. If `true`, a cross-cluster search also ignores errors returned by the remote cluster.
Refer to skip-unavailable-clusters.

`seeds`::
    Initial seed transport addresses of the remote cluster when sniff mode is
    configured.

`num_nodes_connected`::
    Number of connected nodes in the remote cluster when sniff mode is
    configured.

`max_connections_per_cluster`::
    Maximum number of connections maintained for the remote cluster when sniff
    mode is configured.

`proxy_address`::
    Address for remote connections when proxy mode is configured.

`num_proxy_sockets_connected`::
    Number of open socket connections to the remote cluster when proxy mode
    is configured.

`max_proxy_socket_connections`::
    The maximum number of socket connections to the remote cluster when proxy
    mode is configured.

`cluster_credentials`::
This field presents and has value of `::es_redacted::` only when the
remote cluster is configured with the API key based model.
Otherwise, the field is not present.
