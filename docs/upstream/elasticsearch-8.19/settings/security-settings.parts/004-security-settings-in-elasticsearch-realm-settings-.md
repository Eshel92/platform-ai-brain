<!-- Part 4 of 7 of settings/security-settings.md (split because the page is big). -->

##### SAML realm settings

In addition to the settings that are valid for all realms, you can specify
the following settings.

`idp.entity_id` ::
 (Static)
The Entity ID of the SAML Identity Provider. An Entity ID is a URI with a
maximum length of 1024 characters. It can be a URL (https://idp.example.com/) or
a URN (`urn:example.com:idp`) and can be found in the configuration or the SAML
metadata of the Identity Provider.

`idp.metadata.path` ::
(Static)
The path _(recommended)_ or URL to a SAML 2.0 metadata file describing the
capabilities and configuration of the Identity Provider.
If a path is provided, then it is resolved relative to the Elasticsearch config
directory.
If a URL is provided, then it must be either a `file` URL or a `https` URL.
Elasticsearch automatically polls this metadata resource and reloads
the IdP configuration when changes are detected.
File based resources are polled at a frequency determined by the global Elasticsearch
`resource.reload.interval.high` setting, which defaults to 5 seconds.
HTTPS resources are polled at a frequency determined by the realm's
`idp.metadata.http.refresh` and `idp.metadata.http.minimum_refresh` settings.
If the metadata resource is loaded from a file then the file must exist at node
startup, if it does not exist then the node will fail to start.
If the resource is loaded over HTTPS then (by default) the node will be tolerant
of a failure to load the resource - the node will start and will continue to
poll the URL for updates. The affected SAML realm will fail to authenticate
users until the problem is resolved. To force the node to fail if the metadata is
unavailable set `idp.metadata.http.fail_on_error` to `true`.

`idp.metadata.http.fail_on_error`::
(Static)
If set to `true`, the realm will fail on startup (and prevent the node from starting)
if it attempts to load metadata over HTTPS and that metadata is not available.
If set to `false` (the default), the node will start but the affected SAML realm will
not support user authentication until the metadata can be successfully loaded.
This setting is ignored if metadata is loaded from a file.

`idp.metadata.http.connect_timeout`::
(Static)
Controls the behavior of the HTTP client that is used for fetching the SAML 2.0 metadata file from a remote URL. Specifies the maximum time the client waits for a connection to be established. A value of zero means the timeout is not used. Defaults to `5s` (5 seconds).

`idp.metadata.http.read_timeout`::
(Static)
Controls the behavior of the HTTP client that is used for fetching the SAML 2.0 metadata file from a remote URL. Specifies the maximum time the client waits when requesting a connection from the connection manager. Defaults to `10s` (10 seconds).

`idp.metadata.http.refresh` ::
(Static)
Controls the frequency with which `https` metadata is checked for changes.
Defaults to `1h` (1 hour).
Under some circumstances Elasticsearch may determine that the metadata needs to be checked
more frequently. This may occur if previous attempts to load the metadata
encountered an error, or if the metadata indicates that it is due to expire in
less than the configured refresh interval. In these cases Elasticsearch will poll more
often, but never more frequently than `idp.metadata.http.minimum_refresh`.
If there is an attempt to authenticate against a realm that has not yet loaded
metadata successfully, that realm may attempt to load metadata outside of the
configured polling frequency.

`idp.metadata.http.minimum_refresh`::
(Static)
Controls the minimum frequency with which `https` metadata is checked for
changes. In regular operation Elasticsearch will use the value of
`idp.metadata.http.refresh` as the polling interval. However, under some
circumstances Elasticsearch may determine that it needs to poll more frequently.
In these cases, the `minimum_refresh` will set the minimum frequency at which
the metdata will be checked.
Defaults to `5m` (5 minutes) and must not be set to a value greater than
`idp.metadata.http.refresh`

`idp.use_single_logout` ::
(Static)
Indicates whether to utilise the Identity Provider's Single Logout service
(if one exists in the IdP metadata file).
Defaults to `true`.

`sp.entity_id` ::
(Static)
The Entity ID to use for this SAML Service Provider. This should be entered as a
URI. We recommend that you use the base URL of your Kibana instance. For example,
`https://kibana.example.com/`.

`sp.acs` ::
(Static)
The URL of the Assertion Consumer Service within Kibana. Typically this is the
"api/security/saml/callback" endpoint of your Kibana server. For example,
`https://kibana.example.com/api/security/saml/callback`.

`sp.logout` ::
(Static)
The URL of the Single Logout service within Kibana. Typically this is the
"logout" endpoint of your Kibana server. For example,
`https://kibana.example.com/logout`.

`attributes.principal` ::
(Static)
The Name of the SAML attribute that contains the user's principal (username).

`attributes.groups` ::
(Static)
The Name of the SAML attribute that contains the user's groups.

`attributes.name` ::
(Static)
The Name of the SAML attribute that contains the user's full name.

`attributes.mail` ::
(Static)
The Name of the SAML attribute that contains the user's email address.

`attributes.dn` ::
(Static)
The Name of the SAML attribute that contains the user's X.50
_Distinguished Name_.

`attribute_patterns.principal` ::
(Static)
A Java regular expression that is matched against the SAML attribute specified
by `attributes.principal` before it is applied to the user's _principal_ property.
The attribute value must match the pattern and the value of the first
_capturing group_ is used as the principal. For example, `^([^@]+)@example\\.com$`
matches email addresses from the "example.com" domain and uses the local-part as
the principal.

`attribute_patterns.groups` ::
(Static)
As per `attribute_patterns.principal`, but for the _group_ property.

`attribute_patterns.name` ::
(Static)
As per `attribute_patterns.principal`, but for the _name_ property.

`attribute_patterns.mail` ::
(Static)
As per `attribute_patterns.principal`, but for the _mail_ property.

`attribute_patterns.dn` ::
(Static)
As per `attribute_patterns.principal`, but for the _dn_ property.

`attribute_delimiters.groups` ::
(Static)
A plain string that is used as a delimiter to split a single-valued SAML
attribute specified by `attributes.groups` before it is applied to the user's
_groups_ property. For example, splitting the SAML attribute value
`engineering,elasticsearch-admins,employees` on a delimiter value of `,` will
result in `engineering`, `elasticsearch-admins`, and `employees` as the list of
groups for the user. The delimiter will always be split on, regardless of
escaping in the input string. This setting does not support multi-valued SAML
attributes. It cannot be used together with the `attribute_patterns` setting.
You can only configure this setting for the groups attribute.

`nameid_format` ::
(Static)
The NameID format that should be requested when asking the IdP to authenticate
the current user. The default is to not include the `nameid_format` attribute.

`nameid.allow_create` ::
(Static)
The value of the `AllowCreate` attribute of the
`NameIdPolicy` element in an authentication request. The default value is false.

`nameid.sp_qualifier` ::
(Static)
The value of the `SPNameQualifier` attribute of the
`NameIdPolicy` element in an authentication request. The default is to not
include the `SPNameQualifier` attribute.

`force_authn` ::
(Static)
Specifies whether to set the `ForceAuthn` attribute when requesting that the IdP
authenticate the current user. If set to `true`, the IdP is required to verify
the user’s identity, irrespective of any existing sessions they might have.
Defaults to `false`.

`populate_user_metadata` ::
(Static)
Specifies whether to populate the Elasticsearch user's metadata with the values that are
provided by the SAML attributes. Defaults to `true`.

`authorization_realms`::
(Static)
The names of the realms that should be consulted for delegated authorization.
If this setting is used, then the SAML realm does not perform role mapping and
instead loads the user from the listed realms.
See authorization_realms.

`allowed_clock_skew` ::
(Static)
The maximum amount of skew that can be tolerated between the IdP's clock and the
Elasticsearch node's clock.
Defaults to `3m` (3 minutes).

`req_authn_context_class_ref` ::
(Static)
A comma separated list of Authentication Context Class Reference values to be
included in the Requested Authentication Context when requesting the IdP to
authenticate the current user. The Authentication Context of the corresponding
authentication response should contain at least one of the requested values.
For more information, see
req-authn-context.


##### SAML realm signing settings

If a signing key is configured (that is, either `signing.key` or
`signing.keystore.path` is set), then Elasticsearch signs outgoing SAML messages.
Signing can be configured using the following settings:

`signing.saml_messages` ::
(Static)
A list of SAML message types that should be signed or `*` to sign all messages.
Each element in the list should be the local name of a SAML XML Element.
Supported element types are `AuthnRequest`, `LogoutRequest` and `LogoutResponse`.
Only valid if `signing.key` or `signing.keystore.path` is also specified.
Defaults to `*`.

`signing.key` ::
(Static)
Specifies the path to the PEM encoded private key to use for SAML message signing.
`signing.key` and `signing.keystore.path` cannot be used at the same time.

`signing.secure_key_passphrase` ::
(Secure)
Specifies the passphrase to decrypt the PEM encoded private key (`signing.key`)
if it is encrypted.

`signing.certificate` ::
(Static)
Specifies the path to the PEM encoded certificate (or certificate chain) that
corresponds to the `signing.key`. This certificate must also be included in the
Service Provider metadata or manually configured within the IdP to allow for
signature validation. This setting can only be used if `signing.key` is set.

`signing.keystore.path` ::
(Static)
The path to the keystore that contains a private key and certificate. It must be
either a Java keystore (jks) or a PKCS#12 file. You cannot use this setting and
`signing.key` at the same time.

`signing.keystore.type` ::
(Static)
The type of the keystore in `signing.keystore.path`.
Must be either `jks` or `PKCS12`. If the keystore path ends in ".p12", ".pfx",
or "pkcs12", this setting defaults to `PKCS12`. Otherwise, it defaults to `jks`.

`signing.keystore.alias` ::
(Static)
Specifies the alias of the key within the keystore that should be
used for SAML message signing. If the keystore contains more than one private
key, this setting must be specified.

`signing.keystore.secure_password` ::
(Secure)
The password to the keystore in `signing.keystore.path`.

`signing.keystore.secure_key_password` ::
(Secure)
The password for the key in the keystore (`signing.keystore.path`).
Defaults to the keystore password.


##### SAML realm encryption settings

If an encryption key is configured (that is, either `encryption.key` or
`encryption.keystore.path` is set), then Elasticsearch publishes an encryption
certificate when generating metadata and attempts to decrypt incoming SAML
content. Encryption can be configured using the following settings:

`encryption.key` ::
(Static)
Specifies the path to the PEM encoded private key to use for SAML message
decryption.
`encryption.key` and `encryption.keystore.path` cannot be used at the same time.

`encryption.secure_key_passphrase`::
(Secure)
Specifies the passphrase to decrypt the PEM encoded private key
(`encryption.key`) if it is encrypted.

`encryption.certificate` ::
(Static)
Specifies the path to the PEM encoded certificate (or certificate chain) that is
associated with the `encryption.key`. This certificate must also be included in
the Service Provider metadata or manually configured within the IdP to enable
message encryption. This setting can be used only if `encryption.key` is set.

`encryption.keystore.path` ::
(Static)
The path to the keystore that contains a private key and certificate. It must be
either a Java keystore (jks) or a PKCS#12 file. You cannot use this setting and
`encryption.key` at the same time.

`encryption.keystore.type` ::
(Static)
The type of the keystore (`encryption.keystore.path`).
Must be either `jks` or `PKCS12`. If the keystore path ends in ".p12", ".pfx",
or "pkcs12", this setting defaults to `PKCS12`. Otherwise, it defaults to `jks`.

`encryption.keystore.alias` ::
(Static)
Specifies the alias of the key within the keystore (`encryption.keystore.path`)
that should be used for SAML message decryption. If not specified, all compatible
key pairs from the keystore are considered as candidate keys for decryption.

`encryption.keystore.secure_password`::
(Secure)
The password to the keystore (`encryption.keystore.path`).

`encryption.keystore.secure_key_password`::
(Secure)
The password for the key in the keystore (`encryption.keystore.path`). Only a
single password is supported. If you are using multiple decryption keys,
they cannot have individual passwords.


##### SAML realm SSL settings

If you are loading the IdP metadata over SSL/TLS (that is, `idp.metadata.path`
is a URL using the `https` protocol), the following settings can be used to
configure SSL.

**Note:** These settings are not used for any purpose other than loading metadata
over https.

`ssl.key` ::
(Static)
Path to a PEM encoded file containing the private key.
If HTTP client authentication is required, it uses this file. You cannot use
this setting and `ssl.keystore.path` at the same time.

`ssl.key_passphrase` ::
(Static)
The passphrase that is used to decrypt the private key. Since the key might not
be encrypted, this value is optional. deprecated:[7.17.0] Prefer `ssl.secure_key_passphrase` instead.
You cannot use this setting and `ssl.secure_key_passphrase` at the same time.

`ssl.secure_key_passphrase`::
(Secure)
The passphrase that is used to decrypt the private key. Since the key might not
be encrypted, this value is optional.
You cannot use this setting and `ssl.key_passphrase` at the same time.

`ssl.certificate` ::
(Static)
Specifies the path for the PEM encoded certificate (or certificate chain) that is
associated with the key.
This setting can be used only if `ssl.key` is set.

`ssl.certificate_authorities` ::
(Static)
List of paths to PEM encoded certificate files that should be trusted.
This setting and `ssl.truststore.path` cannot be used at the same time.

`ssl.keystore.path` ::
(Static)
The path for the keystore file that contains a private key and certificate.
It must be either a Java keystore (jks) or a PKCS#12 file. You cannot use this
setting and `ssl.key` at the same time.

`ssl.keystore.type` ::
(Static)
The format of the keystore file. It must be either `jks` or `PKCS12`. If the
keystore path ends in ".p12", ".pfx", or ".pkcs12", this setting defaults
to `PKCS12`. Otherwise, it defaults to `jks`.

`ssl.keystore.password` ::
(Static)
The password for the keystore. deprecated:[7.17.0] Prefer `ssl.keystore.secure_password` instead.

`ssl.keystore.secure_password`::
(Secure)
The password for the keystore.
You cannot use this setting and `ssl.keystore.password` at the same time.

`ssl.keystore.key_password`::
(Static)
The password for the key in the keystore. The default is the keystore password.
deprecated:[7.17.0] Prefer `ssl.keystore.secure_key_password` instead.
You cannot use this setting and `ssl.keystore.secure_password` at the same time.
You cannot use this setting and `ssl.keystore.secure_key_password` at the same
time.

`ssl.keystore.secure_key_password`::
(Secure)
The password for the key in the keystore. The default is the keystore password.
You cannot use this setting and `ssl.keystore.key_password` at the same time.

`ssl.truststore.path` ::
(Static)
The path for the keystore that contains the certificates to trust. It must be
either a Java keystore (jks) or a PKCS#12 file.
You cannot use this setting and `ssl.certificate_authorities` at the same time.

`ssl.truststore.type` ::
(Static)
The format of the truststore file. It must be either `jks` or `PKCS12`. If the
file name ends in ".p12", ".pfx" or "pkcs12", the default is `PKCS12`.
Otherwise, it defaults to `jks`.

`ssl.truststore.password` ::
(Static)
The password for the truststore. deprecated:[7.17.0] Prefer `ssl.truststore.secure_password` instead.
You cannot use this setting and `ssl.truststore.secure_password` at the same
time.

`ssl.truststore.secure_password`::
(Secure)
Password for the truststore.
This setting cannot be used with `ssl.truststore.password`.

`ssl.verification_mode` ::
(Static)
Controls the verification of certificates.
**Valid values**
=====
`full`::
Validates that the provided certificate: has an issue date that's
within the `not_before` and `not_after` dates; chains to a trusted Certificate
Authority (CA); has a `hostname` or IP address that matches the names within
the certificate.

`certificate`::
Validates the provided certificate and verifies that it's signed by a
trusted authority (CA), but doesn't check the certificate `hostname`.

`none`::
Performs no certificate validation.
**Important:** Setting certificate validation to `none` disables many security
benefits of SSL/TLS, which is very dangerous. Only set this value if instructed
by Elastic Support as a temporary diagnostic mechanism when attempting to
resolve TLS errors.
=====
Defaults to `full`.

`ssl.supported_protocols` ::
(Static)
Supported protocols with versions. Valid protocols: `SSLv2Hello`,
`SSLv3`, `TLSv1`, `TLSv1.1`, `TLSv1.2`, `TLSv1.3`. If the JVM's SSL provider supports TLSv1.3,
the default is `TLSv1.3,TLSv1.2,TLSv1.1`. Otherwise, the default is
`TLSv1.2,TLSv1.1`.
Elasticsearch relies on your JDK’s implementation of SSL and TLS.
View jdk-tls-versions for more information.
**Note:** If `xpack.security.fips_mode.enabled` is `true`, you cannot use `SSLv2Hello`
or `SSLv3`. See fips-140-compliance.

`ssl.cipher_suites` ::
(Static)
Supported cipher suites vary depending on which version of Java you use. For
example, for version 12 the default value is `TLS_AES_256_GCM_SHA384`,
`TLS_AES_128_GCM_SHA256`, `TLS_CHACHA20_POLY1305_SHA256`,
`TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384`, `TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256`,
`TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384`, `TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256`,
`TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256`, `TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256`,
`TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA384`, `TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256`,
`TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384`, `TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256`,
`TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA`, `TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA`,
`TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA`, `TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA`,
`TLS_RSA_WITH_AES_256_GCM_SHA384`, `TLS_RSA_WITH_AES_128_GCM_SHA256`,
`TLS_RSA_WITH_AES_256_CBC_SHA256`, `TLS_RSA_WITH_AES_128_CBC_SHA256`,
`TLS_RSA_WITH_AES_256_CBC_SHA`, `TLS_RSA_WITH_AES_128_CBC_SHA`.
For more information, see Oracle's
[Java Cryptography Architecture documentation](https://docs.oracle.com/en/java/javase/11/security/oracle-providers.html#GUID-7093246A-31A3-4304-AC5F-5FB6400405E2).
