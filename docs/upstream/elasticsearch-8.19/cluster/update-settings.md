<!-- Converted from cluster/update-settings.asciidoc (AsciiDoc). Includes are inlined. -->

### Cluster update settings API

**New API reference**
For the most up-to-date API details, refer to [Cluster APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-cluster).

Configures dynamic cluster settings.

#### Request

`PUT /_cluster/settings`

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the `manage`
cluster privilege to use this API.

#### Description

You can configure and update dynamic settings on a running cluster using the
cluster update settings API.
cluster update settings API.
You can also configure dynamic settings locally on an unstarted or shut down
node using `elasticsearch.yml`.

Updates made using the cluster update settings API can be _persistent_, which
apply across cluster restarts, or _transient_, which reset after a cluster
restart. You can also reset transient or persistent settings by assigning them
a `null` value using the API.

If you configure the same setting using multiple methods, Elasticsearch applies the
settings in following order of precedence:

1. Transient setting
2. Persistent setting
3. `elasticsearch.yml` setting
4. Default setting value

For example, you can apply a transient setting to override a persistent setting
or `elasticsearch.yml` setting. However, a change to an `elasticsearch.yml`
setting will not override a defined transient or persistent setting.

**Tip:**
If you use Elasticsearch Service, use the {cloud}/ec-add-user-settings.html[user settings]
feature to configure all cluster settings. This method lets Elasticsearch Service automatically
reject unsafe settings that could break your cluster.

If you run Elasticsearch on your own hardware, use the
cluster update settings API
cluster update settings API
to configure dynamic cluster settings. Only use `elasticsearch.yml` for static
cluster settings and node settings. The API doesn't require a restart and
ensures a setting's value is the same on all nodes.

**Warning:**
We no longer recommend using transient cluster settings. Use persistent cluster
settings instead. If a cluster becomes unstable, transient settings can clear
unexpectedly, resulting in a potentially undesired cluster configuration. See
the transient-settings-migration-guide.

#### Query parameters

`flat_settings`::
(Optional, Boolean) If `true`, returns settings in flat format. Defaults to
`false`.
`include_defaults`::
    (Optional, Boolean) If `true`, returns all default cluster settings.
    Defaults to `false`.

`master_timeout`::
(Optional, time units)
Period to wait for the master node. If the master node is not available before
the timeout expires, the request fails and returns an error. Defaults to `30s`.
Can also be set to `-1` to indicate that the request should never timeout.

`timeout`::
(Optional, time units) Period to wait for a response from all relevant nodes in the cluster after updating the cluster metadata.
If no response is received before the timeout expires, the cluster metadata update still applies but the response will indicate that it was not completely acknowledged.
Defaults to `30s`.
Can also be set to `-1` to indicate that the request should never timeout.

#### Examples

An example of a persistent update:

```console
PUT /_cluster/settings
{
  "persistent" : {
    "indices.recovery.max_bytes_per_sec" : "50mb"
  }
}
```

An example of a transient update:

**Warning:**
We no longer recommend using transient cluster settings. Use persistent cluster
settings instead. If a cluster becomes unstable, transient settings can clear
unexpectedly, resulting in a potentially undesired cluster configuration. See
the transient-settings-migration-guide.

```console
PUT /_cluster/settings?flat_settings=true
{
  "transient" : {
    "indices.recovery.max_bytes_per_sec" : "20mb"
  }
}
```

The response to an update returns the changed setting, as in this response to
the transient example:

```console-result
{
  ...
  "persistent" : { },
  "transient" : {
    "indices.recovery.max_bytes_per_sec" : "20mb"
  }
}
```

This example resets a setting:

```console
PUT /_cluster/settings
{
  "transient" : {
    "indices.recovery.max_bytes_per_sec" : null
  }
}
```

The response does not include settings that have been reset:

```console-result
{
  ...
  "persistent" : {},
  "transient" : {}
}
```

You can also reset settings using wildcards. For example, to reset
all dynamic `indices.recovery` settings:

```console
PUT /_cluster/settings
{
  "transient" : {
    "indices.recovery.*" : null
  }
}
```
