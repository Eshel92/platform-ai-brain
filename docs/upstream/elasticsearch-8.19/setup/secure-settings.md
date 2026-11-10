<!-- Converted from setup/secure-settings.asciidoc (AsciiDoc). Includes are inlined. -->

### Secure settings

Some settings are sensitive, and relying on filesystem permissions to protect
their values is not sufficient. For this use case, Elasticsearch provides a
keystore and the `elasticsearch-keystore` tool to
manage the settings in the keystore.

**Important:** Only some settings are designed to be read from the keystore.
Adding unsupported settings to the keystore causes the validation in the
`_nodes/reload_secure_settings` API to fail and if not addressed, will
cause Elasticsearch to fail to start. To see whether a setting is supported in the
keystore, look for a "Secure" qualifier in the setting reference.

All the modifications to the keystore take effect only after restarting Elasticsearch.

These settings, just like the regular ones in the `elasticsearch.yml` config file,
need to be specified on each node in the cluster. Currently, all secure settings
are node-specific settings that must have the same value on every node.

### Reloadable secure settings

Just like the settings values in `elasticsearch.yml`, changes to the keystore
contents are not automatically applied to the running Elasticsearch node. Re-reading
settings requires a node restart. However, certain secure settings are marked as
*reloadable*. Such settings can be re-read and applied on a running node.

You can define these settings before the node is started, 
or call the Nodes reload secure settings API 
after the settings are defined to apply them to a running node. 

The values of all secure settings, *reloadable* or not, must be identical
across all cluster nodes. After making the desired secure settings changes,
using the `bin/elasticsearch-keystore add` command, call:

```console
POST _nodes/reload_secure_settings
{
  "secure_settings_password": "keystore-password" <1>
}
```

<1> The password that the Elasticsearch keystore is encrypted with.

This API decrypts, re-reads the entire keystore and validates all settings on
every cluster node, but only the *reloadable* secure settings are applied.
Changes to other settings do not go into effect until the next restart. Once
the call returns, the reload has been completed, meaning that all internal data
structures dependent on these settings have been changed. Everything should
look as if the settings had the new value from the start.

When changing multiple *reloadable* secure settings, modify all of them on each
cluster node, then issue a `reload_secure_settings`
call instead of reloading after each modification.

There are reloadable secure settings for:

* The Azure repository plugin
* {plugins}/discovery-ec2-usage.html#_configuring_ec2_discovery[The EC2 discovery plugin]
* The GCS repository plugin
* The S3 repository plugin
* monitoring-settings
* notification-settings
* JWT realm
* Active Directory realm
* LDAP realm
* Remote cluster credentials for the API key based security model
