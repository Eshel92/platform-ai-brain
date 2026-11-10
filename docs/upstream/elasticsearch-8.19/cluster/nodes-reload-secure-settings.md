<!-- Converted from cluster/nodes-reload-secure-settings.asciidoc (AsciiDoc). Includes are inlined. -->

### Nodes reload secure settings API

**New API reference**
For the most up-to-date API details, refer to [Cluster APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-cluster).

Reloads the keystore on nodes in the cluster.

#### Request

`POST /_nodes/reload_secure_settings` +
`POST /_nodes/<node_id>/reload_secure_settings`

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the `manage`
cluster privilege to use this API.

#### Description

Secure settings are stored in an on-disk keystore. Certain
of these settings are reloadable. That is, you
can change them on disk and reload them without restarting any nodes in the
cluster. When you have updated reloadable secure settings in your keystore, you
can use this API to reload those settings on each node.

When the Elasticsearch keystore is password protected and not simply obfuscated, you must
provide the password for the keystore when you reload the secure settings.
Reloading the settings for the whole cluster assumes that all nodes' keystores
are protected with the same password; this method is allowed only when
inter-node communications are encrypted. Alternatively, you can
reload the secure settings on each node by locally accessing the API and passing
the node-specific Elasticsearch keystore password.

#### Path parameters

`<node_id>`::
    (Optional, string) The names of particular nodes in the cluster to target.
    For example, `nodeId1,nodeId2`. For node selection options, see
    cluster-nodes.

**Note:** Elasticsearch requires consistent secure settings across the cluster nodes, but
this consistency is not enforced. Hence, reloading specific nodes is not
standard. It is justifiable only when retrying failed reload operations.

#### Request body

`secure_settings_password`::
  (Optional, string) The password for the Elasticsearch keystore.

#### Examples

The following examples assume a common password for the Elasticsearch keystore on every
node of the cluster:

```console
POST _nodes/reload_secure_settings
{
  "secure_settings_password":"keystore-password"
}
POST _nodes/nodeId1,nodeId2/reload_secure_settings
{
  "secure_settings_password":"keystore-password"
}
```

The response contains the `nodes` object, which is a map, keyed by the
node id. Each value has the node `name` and an optional `reload_exception`
field. The `reload_exception` field is a serialization of the exception
that was thrown during the reload process, if any.

```console-result
{
  "_nodes": {
    "total": 1,
    "successful": 1,
    "failed": 0
  },
  "cluster_name": "my_cluster",
  "nodes": {
    "pQHNt5rXTTWNvUgOrdynKg": {
      "name": "node-0"
    }
  }
}
```
