<!-- Converted from modules/indices/index_management.asciidoc (AsciiDoc). Includes are inlined. -->

### Index management settings

You can use the following cluster settings to enable or disable index management
features.

`action.auto_create_index` ::
(Dynamic)
Automatically create an index if it doesn't already exist and apply any configured index templates. Defaults to `true`.

`action.destructive_requires_name` ::
(Dynamic)
When set to `true`, you must specify the index name to delete an index. It is not possible to delete all indices with `_all` or use wildcards. Defaults to `true`.

`cluster.indices.close.enable` ::
(Dynamic)
Enables closing of open indices in Elasticsearch. If `false`, you
cannot close open indices. Defaults to `true`.
**Note:** Closed indices still consume a significant amount of disk space.

`stack.templates.enabled`::
(Dynamic)
If `true`, enables built-in index and component templates.
{fleet-guide}/fleet-overview.html[Elastic Agent] uses these templates to create data
streams. If `false`, Elasticsearch disables these index and component templates. Defaults
to `true`.

**Note:** It is not recommended to disable the built-in stack templates, as some functionality of Elasticsearch
or Kibana will not work correctly when disabled. Features like log and metric collection, as well as
Kibana reporting, may malfunction without the built-in stack templates. Stack templates should only
be disabled temporarily, if necessary, to resolve upgrade issues, then re-enabled after any issues
have been resolved.

This setting affects the following built-in index templates:

- `logs-*-*`
- `metrics-*-*`
- `synthetics-*-*`
- `profiling-*`
- `security_solution-*-*`
This setting also affects the following built-in component templates:

- `logs@mappings`
- `logs@settings`
- `metrics@mappings`
- `metrics@settings`
- `metrics@tsdb-settings`
- `synthetics@mapping`
- `synthetics@settings`

#### Reindex settings

`reindex.remote.whitelist` ::
(Static)
Specifies the hosts that can be reindexed from remotely. Expects a YAML array of `host:port` strings. Consists of a comma-delimited list of `host:port` entries. Defaults to `["\*.io:*", "\*.com:*"]`.

`reindex.ssl.certificate`::
Specifies the path to the PEM encoded certificate (or certificate chain) to be
used for HTTP client authentication (if required by the remote cluster)
This setting requires that `reindex.ssl.key` also be set.
You cannot specify both `reindex.ssl.certificate` and `reindex.ssl.keystore.path`.

`reindex.ssl.certificate_authorities`::
List of paths to PEM encoded certificate files that should be trusted.
You cannot specify both `reindex.ssl.certificate_authorities` and
`reindex.ssl.truststore.path`.

`reindex.ssl.key`::
Specifies the path to the PEM encoded private key associated with the
certificate used for client authentication (`reindex.ssl.certificate`).
You cannot specify both `reindex.ssl.key` and `reindex.ssl.keystore.path`.

`reindex.ssl.key_passphrase`::
Specifies the passphrase to decrypt the PEM encoded private key
(`reindex.ssl.key`) if it is encrypted.
deprecated:[7.17.0] Prefer `reindex.ssl.secure_key_passphrase` instead.
Cannot be used with `reindex.ssl.secure_key_passphrase`.

`reindex.ssl.keystore.key_password`::
The password for the key in the keystore (`reindex.ssl.keystore.path`).
Defaults to the keystore password.
deprecated:[7.17.0] Prefer `reindex.ssl.keystore.secure_key_password` instead.
This setting cannot be used with `reindex.ssl.keystore.secure_key_password`.

`reindex.ssl.keystore.password`::
The password to the keystore (`reindex.ssl.keystore.path`).
deprecated:[7.17.0] Prefer `reindex.ssl.keystore.secure_password` instead.
This setting cannot be used with `reindex.ssl.keystore.secure_password`.

`reindex.ssl.keystore.path`::
Specifies the path to the keystore that contains a private key and certificate
to be used for HTTP client authentication (if required by the remote cluster).
This keystore can be in "JKS" or "PKCS#12" format.
You cannot specify both `reindex.ssl.key` and `reindex.ssl.keystore.path`.

`reindex.ssl.keystore.type`::
The type of the keystore (`reindex.ssl.keystore.path`). Must be either `jks` or `PKCS12`.
If the keystore path ends in ".p12", ".pfx" or "pkcs12", this setting defaults
to `PKCS12`. Otherwise, it defaults to `jks`.

`reindex.ssl.secure_key_passphrase` (Secure)::
Specifies the passphrase to decrypt the PEM encoded private key
(`reindex.ssl.key`) if it is encrypted.
Cannot be used with `reindex.ssl.key_passphrase`.

`reindex.ssl.keystore.secure_key_password` (Secure)::
The password for the key in the keystore (`reindex.ssl.keystore.path`).
Defaults to the keystore password. This setting cannot be used with
`reindex.ssl.keystore.key_password`.

`reindex.ssl.keystore.secure_password` (Secure)::
The password to the keystore (`reindex.ssl.keystore.path`).
This setting cannot be used with `reindex.ssl.keystore.password`.

`reindex.ssl.truststore.password`::
The password to the truststore (`reindex.ssl.truststore.path`).
deprecated:[7.17.0] Prefer `reindex.ssl.truststore.secure_password` instead.
This setting cannot be used with `reindex.ssl.truststore.secure_password`.

`reindex.ssl.truststore.path`::
The path to the Java Keystore file that contains the certificates to trust.
This keystore can be in "JKS" or "PKCS#12" format.
You cannot specify both `reindex.ssl.certificate_authorities` and
`reindex.ssl.truststore.path`.

`reindex.ssl.truststore.secure_password` (Secure)::
The password to the truststore (`reindex.ssl.truststore.path`).
This setting cannot be used with `reindex.ssl.truststore.password`.

`reindex.ssl.truststore.type`::
The type of the truststore (`reindex.ssl.truststore.path`).
Must be either `jks` or `PKCS12`. If the truststore path ends in ".p12", ".pfx"
or "pkcs12", this setting defaults to `PKCS12`. Otherwise, it defaults to `jks`.

`reindex.ssl.verification_mode`::
Indicates the type of verification to protect against man in the middle attacks
and certificate forgery.
One of `full` (verify the hostname and the certificate path), `certificate`
(verify the certificate path, but not the hostname) or `none` (perform no
verification - this is strongly discouraged in production environments).
Defaults to `full`.
