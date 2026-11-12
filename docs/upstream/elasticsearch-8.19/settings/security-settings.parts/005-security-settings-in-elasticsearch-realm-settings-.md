<!-- Part 5 of 7 of settings/security-settings.md (split because the page is big). -->

##### Kerberos realm settings

In addition to the
settings that are valid for all realms, you can specify
the following settings:

`keytab.path` ::
(Static)
Specifies the path to the Kerberos keytab file that contains the
service principal used by this Elasticsearch node. This must be a location within the
Elasticsearch configuration directory and the file must have read permissions. Required.

`remove_realm_name` ::
(Static)
Set to `true` to remove the realm part of principal names.
Principal names in Kerberos have the form `user/instance@REALM`. If this option
is `true`, the realm part (`@REALM`) will not be included in the username.
Defaults to `false`.

`krb.debug`::
(Static)
Set to `true` to enable debug logs for the Java login module that
provides support for Kerberos authentication. Defaults to `false`.

`cache.ttl` ::
(Static)
The time-to-live for cached user entries. A user is cached for
this period of time. Specify the time period using the standard Elasticsearch
time units. Defaults to `20m`.

`cache.max_users` ::
(Static)
The maximum number of user entries that can live in the
cache at any given time. Defaults to 100,000.

`authorization_realms` ::
(Static)
The names of the realms that should be consulted for delegated authorization.
If this setting is used, then the Kerberos realm does not perform role mapping and
instead loads the user from the listed realms.
See authorization_realms.


##### OpenID Connect realm settings

In addition to the settings that are valid for all realms, you
can specify the following settings.

`op.issuer` ::
(Static)
A verifiable Identifier for your OpenID Connect Provider. An Issuer
Identifier is usually a case sensitive URL using the https scheme that contains
scheme, host, and optionally, port number and path components and no query or
fragment components. The value for this setting should be provided by your OpenID
Connect Provider.

`op.authorization_endpoint` ::
(Static)
The URL for the Authorization Endpoint at the
OpenID Connect Provider. The value for this setting should be provided by your OpenID
Connect Provider.

`op.token_endpoint` ::
(Static)
The URL for the Token Endpoint at the OpenID Connect Provider.
The value for this setting should be provided by your OpenID Connect Provider.

`op.userinfo_endpoint` ::
(Static)
The URL for the User Info Endpoint at the OpenID Connect Provider.
The value for this setting should be provided by your OpenID Connect Provider.

`op.endsession_endpoint` ::
(Static)
The URL for the End Session Endpoint at the OpenID Connect
Provider. The value for this setting should be provided by your OpenID Connect Provider.

`op.jwkset_path` ::
(Static)

The file name or URL to a JSON Web Key Set (JWKS) with the public key material used to verify
tokens and claims responses signed by the OpenID Connect Provider. A value is considered a file name
if it does not begin with `https` or `http`. The file name
is resolved relative to the Elasticsearch configuration directory.  Changes to the file are polled
at a frequency determined by the global Elasticsearch `resource.reload.interval.high`
setting, which defaults to 5 seconds.
If a URL is provided, then it must begin with `https://` or `http://`.
Elasticsearch automatically caches the retrieved JWK and will attempt to refresh the JWK upon signature verification
failure, as this might indicate that the OpenID Connect Provider has
rotated the signing keys.

`authorization_realms`::
(Static)
The names of the realms that should be consulted for delegated authorization.
If this setting is used, then the OpenID Connect realm does not perform role
mapping and instead loads the user from the listed realms.
See authorization_realms.

`rp.client_id` ::
(Static)
The OAuth 2.0 Client Identifier that was assigned to Elasticsearch during registration
at the OpenID Connect Provider.

`rp.client_secret`::
(Secure)
The OAuth 2.0 Client Secret that was assigned to Elasticsearch during registration
at the OpenID Connect Provider.

`rp.client_auth_method` ::
(Static)
The client authentication method used by Elasticsearch to authenticate
to the OpenID Connect Provider. Can be `client_secret_basic`, `client_secret_post`,
or `client_secret_jwt`. Defaults to `client_secret_basic`.

`rp.client_auth_jwt_signature_algorithm` ::
(Static)
The signature algorithm that Elasticsearch uses to sign the JWT with which it authenticates
as a client to the OpenID Connect Provider when `client_secret_jwt` is selected for
`rp.client_auth_method`. Can be either `HS256`, `HS384`, or `HS512`. Defaults to
`HS384`.

`rp.redirect_uri` ::
(Static)
The Redirect URI within Kibana. If you want to use the authorization code flow, this is the
`api/security/oidc/callback` endpoint of your Kibana server. If you want to use the implicit flow,  it is the `api/security/oidc/implicit` endpoint.
For example, `https://kibana.example.com/api/security/oidc/callback`.

`rp.response_type` ::
(Static)
OAuth 2.0 Response Type value that determines the authorization
processing flow to be used. Can be `code` for authorization code grant flow,
or one of `id_token`, `id_token token` for the implicit flow.

`rp.signature_algorithm` ::
(Static)
The signature algorithm that will be used by Elasticsearch in order to verify the
signature of the id tokens it will receive from the OpenID Connect Provider.
Allowed values are `HS256`, `HS384`, `HS512`, `ES256`, `ES384`, `ES512`,
`RS256`, `RS384`, `RS512`, `PS256`, `PS384`, `PS512`.
Defaults to `RS256`.

`rp.requested_scopes` ::
(Static)
The scope values that will be requested by the OpenID Connect Provider as
part of the Authentication Request. Optional, defaults to `openid`

`rp.post_logout_redirect_uri` ::
(Static)
The Redirect URI (usually within Kibana) that the OpenID Connect Provider
should redirect the browser to after a successful Single Logout.

`claims.principal`::
(Static)
The name of the OpenID Connect claim that contains the user's principal (username).

`claims.groups` ::
(Static)
The name of the OpenID Connect claim that contains the user's groups.

`claims.name` ::
(Static)
The name of the OpenID Connect claim that contains the user's full name.

`claims.mail` ::
(Static)
The name of the OpenID Connect claim that contains the user's email address.

`claims.dn` ::
(Static)
The name of the OpenID Connect claim that contains the user's X.509
_Distinguished Name_.

`claim_patterns.principal` ::
(Static)
A Java regular expression that is matched against the OpenID Connect claim specified
by `claims.principal` before it is applied to the user's _principal_ property.
The attribute value must match the pattern and the value of the first
_capturing group_ is used as the principal. For example, `^([^@]+)@example\\.com$`
matches email addresses from the "example.com" domain and uses the local-part as
the principal.

`claim_patterns.groups` ::
(Static)
As per `claim_patterns.principal`, but for the _group_ property.

`claim_patterns.name` ::
(Static)
As per `claim_patterns.principal`, but for the _name_ property.

`claim_patterns.mail` ::
(Static)
As per `claim_patterns.principal`, but for the _mail_ property.

`claim_patterns.dn` ::
(Static)
As per `claim_patterns.principal`, but for the _dn_ property.

`allowed_clock_skew` ::
(Static)
The maximum allowed clock skew to be taken into consideration when validating
id tokens with regards to their creation and expiration times.
Defaults to `60s`.

`populate_user_metadata` ::
(Static)
Specifies whether to populate the Elasticsearch user's metadata with the values that are
provided by the OpenID Connect claims. Defaults to `true`.

`http.proxy.host`::
(Static)
Specifies the address of the proxy server that will be used by the internal
http client for all back-channel communication to the OpenID Connect Provider
endpoints. This includes requests to the Token Endpoint, the Userinfo Endpoint
and requests to fetch the JSON Web Key Set from the OP if `op.jwkset_path` is
set as a URL.

`http.proxy.scheme`::
(Static)
Specifies the protocol to use to connect to the proxy server that will be
used by the http client for all back-channel communication to the OpenID
Connect Provider endpoints. Defaults to `http`. Allowed values are
`http` or `https`.

`http.proxy.port`::
(Static)
Specifies the port of the proxy server that will be used by the http
client for all backchannel communication to the OpenID Connect Provider
endpoints. Defaults to `80`.

`http.connect_timeout` ::
(Static)
Controls the behavior of the http client used for back-channel communication to
the OpenID Connect Provider endpoints. Specifies the timeout until a connection
 is established. A value of zero means the timeout is not used. Defaults to `5s`.

`http.connection_read_timeout` ::
(Static)
Controls the behavior of the http client used for back-channel communication to
the OpenID Connect Provider endpoints. Specifies the timeout used when
requesting a connection from the connection manager. Defaults to `5s`

`http.socket_timeout` ::
(Static)
Controls the behavior of the http client used for back-channel communication to
the OpenID Connect Provider endpoints. Specifies the socket timeout (SO_TIMEOUT)
in milliseconds, which is the timeout for waiting for data or, put differently,
a maximum period inactivity between two consecutive data packets). Defaults to
`5s`.

`http.max_connections` ::
(Static)
Controls the behavior of the http client used for back-channel communication to
the OpenID Connect Provider endpoints. Specifies the maximum number of
connections allowed across all endpoints.
Defaults to `200`.

`http.max_endpoint_connections` ::
(Static)
Controls the behavior of the http client used for back-channel communication to
the OpenID Connect Provider endpoints. Specifies the maximum number of
connections allowed per endpoint.
Defaults to `200`.

`http.tcp.keep_alive` ::
(Static)
Whether to enable TCP keepalives on HTTP connections used for back-channel communication
to the OpenID Connect Provider endpoints. Defaults to `true`.

`http.connection_pool_ttl` ::
(Static)
Controls the behavior of the http client used for back-channel communication to
the OpenID Connect Provider endpoints. Specifies the time-to-live of connections
in the connection pool (default to 3 minutes). A connection is closed if it is
idle for more than the specified timeout.

The server can also set the `Keep-Alive` HTTP response header. The effective
time-to-live value is the smaller value between this setting and the `Keep-Alive`
response header. Configure this setting to `-1` to let the server dictate the value.
If the header is not set by the server and the setting has value of `-1`,
the time-to-live is infinite and connections never expire.


##### OpenID Connect realm SSL settings

The following settings can be used to configure SSL for all outgoing http connections
to the OpenID Connect Provider endpoints.

**Note:** These settings are _only_ used for the back-channel communication between
Elasticsearch and the OpenID Connect Provider

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
You cannot use this setting and `ssl.truststore.password` at the same time.

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
