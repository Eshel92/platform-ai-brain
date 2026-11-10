<!-- Converted from watcher/encrypting-data.asciidoc (AsciiDoc). Includes are inlined. -->

## Encrypting sensitive data in Watcher

Watches might have access to sensitive data such as HTTP basic authentication
information or details about your SMTP email service. You can encrypt this
data by generating a key and adding some secure settings on each node in your
cluster.

Every `password` field that is used in your watch within an HTTP basic
authentication block - for example within a webhook, an HTTP input or when using
the reporting email attachment - will not be stored as plain text anymore. Also
be aware, that there is no way to configure your own fields in a watch to be
encrypted.

To encrypt sensitive data in Watcher:

. Use the elasticsearch-syskeygen command to create a system key file.

. Copy the `system_key` file to all of the nodes in your cluster.
**Important:** The system key is a symmetric key, so the same key must be used on
every node in the cluster.

. Set the `xpack.watcher.encrypt_sensitive_data` setting:

```sh
xpack.watcher.encrypt_sensitive_data: true
```

. Set the
`xpack.watcher.encryption_key` setting in the
Elasticsearch keystore on each node in the cluster.
For example, run the following command to import the `system_key` file on
each node:

```sh
bin/elasticsearch-keystore add-file xpack.watcher.encryption_key <filepath>/system_key
```

. Delete the `system_key` file on each node in the cluster.

**Note:** Existing watches are not affected by these changes. Only watches that you
create after following these steps have encryption enabled.
