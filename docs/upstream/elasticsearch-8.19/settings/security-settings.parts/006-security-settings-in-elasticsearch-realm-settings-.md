<!-- Part 6 of 7 of settings/security-settings.md (split because the page is big). -->

##### JWT realm settings

In addition to the settings that are valid for all realms, you
can specify the following settings.

`token_type` ::
(Static)
The token type, `id_token` or `access_token`, that the JWT realm uses to verify
incoming JWTs. Defaults to `id_token`.

`allowed_audiences` ::
(Static)
A list of allowed JWT audiences that Elasticsearch should verify. Elasticsearch will only consume
JWTs that were intended for any of these audiences, as denoted by the `aud`
claim in the JWT).
The audiences are compared with exact string matches and do not support wildcards or regex.
Examples of `aud` claim are `https://example.com/client1`
and `other_service,elasticsearch`. When `token_type` is `access_token`, the audiences can
be optionally denoted by a different claim in the JWT if `aud` does not exist.
See also `fallback_claims.aud`.

`allowed_clock_skew` ::
(Static)
The maximum allowed clock skew to be taken into consideration when validating
JWTs with regards to their creation, not before, and expiration times.

`allowed_issuer` ::
(Static)
A verifiable Identifier for your JWT Issuer. An Issuer
Identifier is usually a case sensitive URL using the https scheme that contains
scheme, host, and optionally, port number and path components and no query or
fragment components. However, it can be any string. The value for this setting
should be provided by your JWT Issuer.
The issuer is compared with exact string matches and do not support wildcards or regex.
Examples of `iss` claim are `https://example.com:8443/jwt` and `issuer123`.

`allowed_subjects` ::
(Static)
A list of allowed JWT subjects that Elasticsearch should verify. Elasticsearch will only consume
JWTs that were issued for any of these subjects, as denoted by the `sub`
claim in the JWT.
The subjects are compared with exact string matches and do not support wildcards or regex.
Examples of `sub` claim are `https://example.com/user1`
and `user_1,user2`.
When `token_type` is `access_token`, this setting is mandatory and the subject can be
optionally denoted by a different claim in the JWT if `sub` does not exist.
See also `fallback_claims.sub`.

`fallback_claims.sub` ::
(Static)
The alternative claim to look for the subject information if the `sub` claim
does not exist. It is configurable only when the `token_type` is `access_token`.
The fallback is applied everywhere the `sub` claim is used.

`fallback_claims.aud` ::
(Static)
The alternative claim to look for the audiences information if the `aud` claim
does not exist. It is configurable only when the `token_type` is `access_token`.
The fallback is applied everywhere the `aud` claim is used.

`required_claims` ::
(Static)
Additional claims and associated values that Elasticsearch should verify.
This is a group setting that takes key/value pairs, where the key is a string
and the value must be either a string or an array of strings.
The values are compared with exact string matches and do not support wildcards or regex.

For example:

```yaml
xpack.security.authc.realms.jwt.jwt1:
  required_claims:
    token_use: "id"
    versions: ["1.0", "2.0"]
```

`allowed_signature_algorithms` ::
(Static)
A list of signature algorithms that will be used by Elasticsearch in order to verify the
signature of the JWT it will receive from the JWT Issuer.
Defaults to `RS256`. Examples are `HS512,RS512,ES512` and `ES384`.
Allowed values are `HS256`, `HS384`, `HS512`, `ES256`, `ES384`, `ES512`,
`RS256`, `RS384`, `RS512`, `PS256`, `PS384`, `PS512`.

`authorization_realms`::
(Static)
The names of the realms that should be consulted for delegated authorization.
If this setting is used, then the JWT realm does not perform role
mapping and instead loads the user from the listed realms.
See authorization_realms.

`claims.dn` ::
(Static)
The name of the JWT claim that contains the user's Distinguished Name (DN),
which uniquely identifies a user or group.

`claim_patterns.dn` ::
(Static)
Accepts the same Java regular expression as
`claim_patterns.principal`, but for the `dn`
property.

`claims.groups` ::
(Static)
The name of the JWT claim that contains the user's groups, such as `groups` and
`roles`.

`claim_patterns.group` ::
(Static)
Accepts the same Java regular expression as
`claim_patterns.principal`, but for the `group`
property.

`claims.mail` ::
(Static)
The name of the JWT claim that contains the user's e-mail address.

`claim_patterns.mail` ::
(Static)
Accepts the same Java regular expression as
`claim_patterns.principal`, but for the `mail`
property.

`claims.name` ::
(Static)
The name of the JWT claim that contains the user's username.

`claim_patterns.name` ::
(Static)
Accepts the same Java regular expression as
`claim_patterns.principal`, but for the `name`
property.

`claims.principal`::
(Static)
The name of the JWT claim that contains the user's principal (username), such as
`sub`, `name`, `email`, and `dn`.

`claim_patterns.principal` ::
(Static)
An optional Java regular expression that is matched against the JWT claim specified
by `claims.principal` before it is applied to the user's `principal` property.
The value must match the pattern and the value of the first
_capturing group_ is used as the principal. For example, `^([^@]+)@example\\.com$`
matches email addresses from the `example.com` domain and uses the local-part as
the principal. Another example is `sub` which may not need a pattern setting.

`client_authentication.type` ::
(Static)
Specifies whether to use `shared_secret` or `none` to authenticate
incoming client requests. If this value is `shared_secret`, the client is
authenticated using an HTTP request header that must match a pre-configured
secret value. The client must provide this shared secret with every request in
the `ES-Client-Authentication` header. If this value is `none`, then the
request header `ES-Client-Authentication` is ignored. Defaults to
`shared_secret`.
Enabling client authentication is recommended. If JWT bearer
tokens are shared with other clients or services, client authentication
restricts which ones are allowed to submit those JWTs to Elasticsearch.

`client_authentication.shared_secret` ::
(Secure, reloadable)
Secret value string for client authentication.
Required if `client_authentication.type` is `shared_secret`.

`client_authentication.rotation_grace_period`::
(Static)
Sets the grace period for how long after rotating the `client_authentication.shared_secret`
is valid. `client_authentication.shared_secret` can be rotated by updating the
keystore then calling the reload API.
Defaults to `1m`.

`http.connect_timeout` ::
(Static)
Sets the timeout for the HTTP client that is used for fetching the JSON Web Key
Set from a remote URL. A value of zero means the timeout is not used. Defaults
to `5s`.

`http.connection_read_timeout` ::
(Static)
Specifies the HTTP timeout used when requesting a connection from the connection
manager. Defaults to `5s`.

`http.socket_timeout` ::
(Static)
Specifies the maximum socket timeout (SO_TIMEOUT) for the HTTP client to wait
for inactivity between two consecutive data packets. Defaults to `5s`.

`http.max_connections` ::
(Static)
Specifies the maximum number of connections allowed across all endpoints.

`http.max_endpoint_connections` ::
(Static)
Specifies the maximum number of connections allowed per endpoint.

`jwt.cache.size`::
(Static)
Specifies the maximum number of JWT cache entries. If clients use a different
JWT for every request, set to `0` to disable the JWT cache. Defaults to `100000`.

`jwt.cache.ttl`::
(Static)
Specifies the time-to-live for the period of time to cache JWT entries.
JWTs can only be cached if client authentication is successful (or disabled).
Uses the standard Elasticsearch time units. If clients use a different JWT
for every request, set to `0` to disable the JWT cache. Defaults to `20m`.

`pkc_jwkset_path` ::
(Static)
The file name or URL to a JSON Web Key Set (JWKS) with the public key material that
the JWT Realm uses for verifying token signatures. A value is considered a file name
if it does not begin with `https`. The file name
is resolved relative to the Elasticsearch configuration directory. If a URL is provided, then
it must begin with `https://` (`http://` is not supported).
Elasticsearch automatically caches the JWK set and will attempt to refresh the
JWK set upon signature verification failure, as this might indicate that the JWT Provider has
rotated the signing keys.

`hmac_jwkset` ::
(Secure)
Contents of a JSON Web Key Set (JWKS), including the secret key that the JWT
realm uses to verify token signatures. This format supports multiple keys and
optional attributes, and is preferred over the `hmac_key` setting. Cannot be
used in conjunction with the `hmac_key` setting. Refer to
Configure Elasticsearch to use a JWT realm.

`hmac_key` ::
(Secure)
Contents of a single JSON Web Key (JWK), including the secret key that the JWT
realm uses to verify token signatures. This format only supports a single key
without attributes, and cannot be used with the `hmac_jwkset` setting. This
format is compatible with OIDC. The HMAC key must be a UNICODE string, where
the key bytes are the UTF-8 encoding of the UNICODE string.
The `hmac_jwkset` setting is preferred. Refer to
Configure Elasticsearch to use a JWT realm.

`populate_user_metadata` ::
(Static)
Specifies whether to populate the Elasticsearch user's metadata with the values that are
provided by the JWT claims. Defaults to `true`.


##### JWT realm SSL settings

The following settings can be used to configure SSL for fetching the JSON Web
Key Set from a remote URL.

**Note:** These settings are _only_ used for the back-channel communication between
Elasticsearch and the JWT Issuer.

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


##### Load balancing and failover

The static `load_balance.type` setting can have the
following values:

* `failover`: The URLs specified are used in the order that they are specified.
The first server that can be connected to will be used for all subsequent
connections. If a connection to that server fails then the next server that a
connection can be established to will be used for subsequent connections.
* `dns_failover`: In this mode of operation, only a single URL may be specified.
This URL must contain a DNS name. The system will be queried for all IP
addresses that correspond to this DNS name. Connections to the Active Directory
or LDAP server will always be tried in the order in which they were retrieved.
This differs from `failover` in that there is no reordering of the list and if a
server has failed at the beginning of the list, it will still be tried for each
subsequent connection.
* `round_robin`: Connections will continuously iterate through the list of
provided URLs. If a server is unavailable, iterating through the list of URLs
will continue until a successful connection is made.
* `dns_round_robin`: In this mode of operation, only a single URL may be
specified. This URL must contain a DNS name. The system will be queried for all
IP addresses that correspond to this DNS name. Connections will continuously
iterate through the list of addresses. If a server is unavailable, iterating
through the list of URLs will continue until a successful connection is made.


#### General TLS settings

`xpack.security.ssl.diagnose.trust`::
(Static)
Controls whether to output diagnostic messages for SSL/TLS trust failures.
If this is `true` (the default), a message will be printed to the Elasticsearch
log whenever an SSL connection (incoming or outgoing) is rejected due to a failure
to establish trust.
This diagnostic message contains information that can be used to determine the
cause of the failure and assist with resolving the problem.
Set to `false` to disable these messages.

##### TLS/SSL key and trusted certificate settings

The following settings are used to specify a private key, certificate, and the
trusted certificates that should be used when communicating over an SSL/TLS
connection. If no trusted certificates are configured, the default certificates
that are trusted by the JVM will be trusted along with the certificate(s)
associated with a key in the same context. The key and certificate must be in
place for connections that require client authentication or when acting as a
SSL enabled server.

Storing trusted certificates in a PKCS#12 file, although supported, is
uncommon in practice. The `elasticsearch-certutil` tool,
as well as Java's `keytool`, are designed to generate PKCS#12 files that
can be used both as a keystore and as a truststore, but this may not be the
case for container files that are created using other tools. Usually,
PKCS#12 files only contain secret and private entries. To confirm that
a PKCS#12 container includes trusted certificate ("anchor") entries look for
`2.16.840.1.113894.746875.1.1: <Unsupported tag 6>` in the
`openssl pkcs12 -info` output, or `trustedCertEntry` in the
`keytool -list` output.

:verifies!:

(See `settings/ssl-settings.md`)
:client-auth-default!:

(See `settings/ssl-settings.md`)

:verifies!:

(See `settings/ssl-settings.md`)

:server!:

(See `settings/ssl-settings.md`)

##### Transport profile TLS/SSL settings

The same settings that are available for the default transport
are also available for each transport profile. By default, the settings for a
transport profile will be the same as the default transport unless they
are specified.

As an example, lets look at the key setting. For the default transport
this is `xpack.security.transport.ssl.key`. In order to use this setting in a
transport profile, use the prefix `transport.profiles.$PROFILE.xpack.security.` and
append the portion of the setting after `xpack.security.transport.`. For the key
setting, this would be `transport.profiles.$PROFILE.xpack.security.ssl.key`.
