<!-- Converted from migration/transient-settings-migration-guide.asciidoc (AsciiDoc). Includes are inlined. -->

### Transient settings migration guide

We no longer recommend using transient cluster settings. You can use transient
settings to make temporary configuration changes to a cluster. However, a
cluster restart or cluster instability can unexpectedly clear these settings,
leading to a potentially undesired cluster configuration.

To avoid this risk, reset any transient settings you've configured on
your cluster. Convert any transient setting you'd like to keep to a persistent
setting, which persists across cluster restarts and cluster instability. You
should also update any custom workflows and applications to use persistent
settings instead of transient settings.

**Important:** Some Elastic products may use transient settings when performing
specific operations. Only reset transient settings configured by you, your
users, or your custom workflows and applications.

To reset and convert transient settings:

. Get a list of any configured transient settings using the
cluster get settings API.
```console
GET _cluster/settings?flat_settings=true&filter_path=transient
```
The API returns transient settings in the `transient` object. If this object is
empty, your cluster has no transient settings, and you can skip the remaining
steps.
```console-result
{
  "persistent": { ... },
  "transient": {
    "cluster.indices.close.enable": "false",
    "indices.recovery.max_bytes_per_sec": "50mb"
  }
}
```

. Copy any settings you'd like to convert into the `persistent` object of a
cluster update settings API request. In the same
request, reset any transient settings by assigning them a `null` value.
```console
PUT _cluster/settings
{
  "persistent": {
    "cluster.indices.close.enable": false,
    "indices.recovery.max_bytes_per_sec": "50mb"
  },
  "transient": {
    "*": null
  }
}
```

. Use the cluster get settings API to confirm your
cluster has no remaining transient settings.
```console
GET _cluster/settings?flat_settings=true
```
If the `transient` object is empty, your cluster has no transient settings.
```console-result
{
  "persistent": {
    "cluster.indices.close.enable": "false",
    "indices.recovery.max_bytes_per_sec": "50mb",
    ...
  },
  "transient": {
  }
}
```
