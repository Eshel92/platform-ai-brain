<!-- Converted from modules/cluster/remote-clusters-cert.asciidoc (AsciiDoc). Includes are inlined. -->

### Add remote clusters using TLS certificate authentication

To add a remote cluster using TLS certificate authentication:

. Review the prerequisites
. remote-clusters-security-cert
. remote-clusters-connect-cert
. remote-clusters-privileges-cert

If you run into any issues, refer to remote-clusters-troubleshooting.

#### Prerequisites

. The Elasticsearch security features need to be enabled on both clusters, on every node.
Security is enabled by default. If it's disabled, set `xpack.security.enabled`
to `true` in `elasticsearch.yml`. Refer to general-security-settings.
. The local and remote clusters versions must be compatible.
** Any node can communicate with another node on the same
major version. For example, 7.0 can talk to any 7.x node.
** Only nodes on the last minor version of a certain major version can
communicate with nodes on the following major version. In the 6.x series, 6.8
can communicate with any 7.x node, while 6.7 can only communicate with 7.0.
** Version compatibility is
symmetric, meaning that if 6.7 can communicate with 7.0, 7.0 can also
communicate with 6.7. The following table depicts version compatibility between
local and remote nodes.
**Version compatibility table**
|====
| 9+^h| Local cluster
h| Remote cluster     | 5.0–5.5    | 5.6        | 6.0–6.6    | 6.7        | 6.8        | 7.0        | 7.1–7.16   | 7.17       | 8.0–{minor-version}
| 5.0–5.5             | ✓ | ✓ | ✗  | ✗  | ✗  | ✗  | ✗  | ✗  | ✗
| 5.6                 | ✓ | ✓ | ✓ | ✓ | ✓ | ✗  | ✗  | ✗  | ✗
| 6.0–6.6             | ✗  | ✓ | ✓ | ✓ | ✓ | ✗  | ✗  | ✗  | ✗
| 6.7                 | ✗  | ✓ | ✓ | ✓ | ✓ | ✓ | ✗  | ✗  | ✗
| 6.8                 | ✗  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✗
| 7.0                 | ✗  | ✗  | ✗  | ✓ | ✓ | ✓ | ✓ | ✓ | ✗
| 7.1–7.16            | ✗  | ✗  | ✗  | ✗  | ✓ | ✓ | ✓ | ✓ | ✗
| 7.17                | ✗  | ✗  | ✗  | ✗  | ✓ | ✓ | ✓ | ✓ | ✓
| 8.0–{minor-version} | ✗  | ✗  | ✗  | ✗  | ✗  | ✗  | ✗  | ✓ | ✓
|====

**Note:** This documentation is for Elasticsearch version {version}, which is not yet
released. The above compatibility table applies if both clusters are running a
released version of Elasticsearch, or if one of the clusters is running a released
version and the other is running a pre-release build with a later build date. A
cluster running a pre-release build of Elasticsearch can also communicate with remote
clusters running the same pre-release build. Running a mix of pre-release
builds is unsupported and typically will not work, even if the builds have the
same version number.

**Important:** Elastic only supports cross-cluster search on a subset of these configurations. See
ccs-supported-configurations.

#### Establish trust with a remote cluster

To use cross-cluster replication or cross-cluster search safely with remote clusters, enable security on all 
connected clusters and configure Transport Layer Security (TLS) on every node.
Configuring TLS security on the transport interface is minimally required for
remote clusters. For additional security, configure TLS on the
HTTP interface as well.

All connected clusters must trust one another and be mutually authenticated
with TLS on the transport interface. This means that the local cluster
trusts the certificate  authority (CA) of the remote cluster, and the remote
cluster trusts the CA of the local cluster. When establishing a connection, all
nodes will verify certificates from nodes on the other side. This mutual trust
is required to securely connect a remote cluster, because all connected nodes
effectively form a single security domain.

User authentication is performed on the local cluster and the user and user’s
roles names are passed to the remote clusters. A remote cluster checks the
user’s role names against its local role definitions to determine which indices
the user is allowed to access.

Before using cross-cluster replication or cross-cluster search with secured Elasticsearch clusters, complete the following 
configuration task:

. Configure Transport Layer Security (TLS) on every node to encrypt internode
traffic and authenticate nodes in the local cluster with nodes in all remote
clusters. Refer to 
set up basic security for the Elastic Stack for the required
steps to configure security.
**Note:** This procedure uses the same CA to generate certificates for all nodes.
Alternatively, you can add the certificates from the local cluster as a
trusted CA in each remote cluster. You must also add the certificates from
remote clusters as a trusted CA on the local cluster. Using the same CA to
generate certificates for all nodes simplifies this task.

#### Connect to a remote cluster

(See `modules/cluster/remote-clusters-connect.md`)
:!trust-mechanism: 

(See `security/authentication/remote-clusters-privileges-cert.md`)
