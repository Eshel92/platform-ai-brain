<!-- Part 3 of 7 of settings/security-settings.md (split because the page is big). -->

##### Active Directory realm settings

In addition to the settings that are valid for all realms,
you can specify the following settings:

`url`::
(Static)
One or more LDAP URLs in the `ldap[s]://<server>:<port>` format. Defaults to
`ldap://<domain_name>:389`. This setting is required when connecting using
SSL/TLS or when using a custom port.
To provide multiple URLs, use a YAML array (`["ldap://server1:636", "ldap://server2:636"]`)
or comma-separated string (`"ldap://server1:636, ldap://server2:636"`).
While both are supported, you can't mix the `ldap` and `ldaps` protocols.
If no URL is provided, Elasticsearch uses a default of `ldap://<domain_name>:389`. This
default uses the `domain_name` setting value and assumes an unencrypted
connection to port 389.

`load_balance.type`::
(Static)
The behavior to use when there are multiple LDAP URLs defined. For supported
values see load balancing and failover types.
Defaults to `failover`.

`load_balance.cache_ttl`::
(Static)
When using `dns_failover` or `dns_round_robin` as the load balancing type,
this setting controls the amount of time to cache DNS lookups. Defaults
to `1h`.

`domain_name`::
(Static)
The domain name of Active Directory. If the `url` and the `user_search.base_dn`
settings are not specified, the cluster can derive those values from this
setting. Required.

`bind_dn`::
(Static)
The DN of the user that is used to bind to Active Directory and perform searches.
Defaults to Empty. Due to its potential security impact, `bind_dn` is not
exposed via the nodes info API.

`bind_password`::
(Static)
deprecated[6.3] Use `secure_bind_password` instead. The password for the user
that is used to bind to Active Directory. Defaults to Empty. Due to its
potential security impact, `bind_password` is not exposed via the
nodes info API.

`secure_bind_password`::
(Secure, Reloadable)
The password for the user that is used to bind to Active Directory.
Defaults to Empty.

`unmapped_groups_as_roles`::
(Static)
If set to `true`, the names of any unmapped Active Directory groups are used as
role names and assigned to the user. A group is considered _unmapped_ when it
is not referenced in any role-mapping files. API-based role mappings are not
considered. Defaults to `false`.

`files.role_mapping`::
(Static)
The location for the YAML
role mapping configuration file. Defaults to `ES_PATH_CONF/role_mapping.yml`.

`user_search.base_dn`::
(Static)
The context to search for a user. Defaults to the root
of the Active Directory domain.

`user_search.scope`::
(Static)
Specifies whether the user search should be `sub_tree`, `one_level` or `base`.
`one_level` only searches users directly contained within the `base_dn`.
`sub_tree` searches all objects contained under `base_dn`. `base`
specifies that the `base_dn` is a user object, and that it is the
only user considered. Defaults to `sub_tree`.

`user_search.filter`::
(Static)
Specifies a filter to use to lookup a user given a username. The default
filter looks up `user` objects with either `sAMAccountName` or
`userPrincipalName`. If specified, this must be a valid LDAP user search filter.
For example `(&(objectClass=user)(sAMAccountName={0}))`. For more information,
see
[Search Filter Syntax](https://msdn.microsoft.com/en-us/library/aa746475(v=vs.85).aspx).

`user_search.upn_filter`::
(Static)
Specifies a filter to use to lookup a user given a user principal name.
The default filter looks up `user` objects with
a matching `userPrincipalName`. If specified, this
must be a valid LDAP user search filter. For example,
`(&(objectClass=user)(userPrincipalName={1}))`. `{1}` is the full user principal name
provided by the user. For more information, see
[Search Filter Syntax](https://msdn.microsoft.com/en-us/library/aa746475(v=vs.85).aspx).

`user_search.down_level_filter`::
(Static)
Specifies a filter to use to lookup a user given a down level logon name
(DOMAIN\user). The default filter looks up `user` objects with a matching
`sAMAccountName` in the domain provided. If specified, this
must be a valid LDAP user search filter. For example,
`(&(objectClass=user)(sAMAccountName={0}))`. For more information, see
[Search Filter Syntax](https://msdn.microsoft.com/en-us/library/aa746475(v=vs.85).aspx).

`user_search.pool.enabled`::
(Static)
Enables or disables connection pooling for user search. When
disabled a new connection is created for every search. The
default is `true` when `bind_dn` is provided.

`user_search.pool.size`::
(Static)
The maximum number of connections to the Active Directory server to allow in the
connection pool. Defaults to `20`.

`user_search.pool.initial_size`::
(Static)
The initial number of connections to create to the Active Directory server on startup.
Defaults to `0`. If the LDAP server is down, values greater than 0
could cause startup failures.

`user_search.pool.health_check.enabled`::
(Static)
Enables or disables a health check on Active Directory connections in the connection
pool. Connections are checked in the background at the specified interval.
Defaults to `true`.

`user_search.pool.health_check.dn`::
(Static)
The distinguished name to be retrieved as part of the health check.
Defaults to the value of `bind_dn` if that setting is present. Otherwise, it
defaults to the value of the `user_search.base_dn` setting.

`user_search.pool.health_check.interval`::
(Static)
The interval to perform background checks of connections in the pool.
Defaults to `60s`.

`group_search.base_dn`::
(Static)
The context to search for groups in which the user has membership. Defaults
to the root of the Active Directory domain.

`group_search.scope`::
(Static)
Specifies whether the group search should be `sub_tree`, `one_level` or
`base`.  `one_level` searches for groups directly contained within the
`base_dn`. `sub_tree` searches all objects contained under `base_dn`.
`base` specifies that the `base_dn` is a group object, and that it is
the only group considered. Defaults to `sub_tree`.

`metadata`::
(Static)
A list of additional LDAP attributes that should be loaded from the
LDAP server and stored in the authenticated user's metadata field.

`timeout.tcp_connect`::
(Static)
The TCP connect timeout period for establishing an LDAP connection.
An `s` at the end indicates seconds, or `ms` indicates milliseconds.
Defaults to `5s` (5 seconds ).

`timeout.tcp_read`::
(Static)
deprecated[7.7] The TCP read timeout period after establishing an LDAP
connection. This is equivalent to and is deprecated in favor of
`timeout.response` and they cannot be used simultaneously. An `s` at the end
indicates seconds, or `ms` indicates milliseconds. Defaults to the value of
`timeout.ldap_search`.

`timeout.response`::
(Static)
The time interval to wait for the response from the AD server. An `s` at the
end indicates seconds, or `ms` indicates milliseconds. Defaults to the value of
`timeout.ldap_search`.

`timeout.ldap_search`::
(Static)
The timeout period for an LDAP search. The value is specified in the request
and is enforced by the receiving LDAP Server.
An `s` at the end indicates seconds, or `ms` indicates milliseconds.
Defaults to `5s` (5 seconds ).

`ssl.certificate`::
(Static)
Specifies the path for the PEM encoded certificate (or certificate chain) that is
associated with the key.
This setting can be used only if `ssl.key` is set.
This certificate is presented to clients when they connect.

`ssl.certificate_authorities`::
(Static)
List of paths to PEM encoded certificate files that should be trusted.
This setting and `ssl.truststore.path` cannot be used at the same time.
You cannot use this setting and `ssl.truststore.path` at the same time.

`ssl.key`::
(Static)
Path to a PEM encoded file containing the private key.
If HTTP client authentication is required, it uses this file. You cannot use
this setting and `ssl.keystore.path` at the same time.
If the Active Directory server requires client authentication, it uses this file.
You cannot use this setting and `ssl.keystore.path` at the same time.

`ssl.key_passphrase`::
(Static)
The passphrase that is used to decrypt the private key. Since the key might not
be encrypted, this value is optional. deprecated:[7.17.0] Prefer `ssl.secure_key_passphrase` instead.
You cannot use this setting and `ssl.secure_key_passphrase` at the same time.
`ssl.secure_key_passphrase`::
(Secure)
The passphrase that is used to decrypt the private key. Since the key might not
be encrypted, this value is optional.
`ssl.keystore.key_password`::
(Static)
The password for the key in the keystore. The default is the keystore password.
deprecated:[7.17.0] Prefer `ssl.keystore.secure_key_password` instead.
You cannot use this setting and `ssl.keystore.secure_password` at the same time.
`ssl.keystore.secure_key_password`::
(Secure)
The password for the key in the keystore. The default is the keystore password.
`ssl.keystore.password`::
(Static)
The password for the keystore. deprecated:[7.17.0] Prefer `ssl.keystore.secure_password` instead.
`ssl.secure_keystore.password`::
(Secure)
The password for the keystore.

`ssl.keystore.path`::
(Static)
The path for the keystore file that contains a private key and certificate.
It must be either a Java keystore (jks) or a PKCS#12 file. You cannot use this
setting and `ssl.key` at the same time.
You cannot use this setting and `ssl.key` at the same time.

`ssl.keystore.type`::
(Static)
The format of the keystore file. It must be either `jks` or `PKCS12`. If the
keystore path ends in ".p12", ".pfx", or ".pkcs12", this setting defaults
to `PKCS12`. Otherwise, it defaults to `jks`.
`ssl.truststore.password`::
(Static)
The password for the truststore. deprecated:[7.17.0] Prefer `ssl.truststore.secure_password` instead.
You cannot use this setting and `ssl.truststore.secure_password` at the same
time.
`ssl.truststore.secure_password`::
(Secure)
Password for the truststore.
`ssl.truststore.path`::
(Static)
The path for the keystore that contains the certificates to trust. It must be
either a Java keystore (jks) or a PKCS#12 file.
You cannot use this setting and `ssl.certificate_authorities` at the same time.
You cannot use this setting and `ssl.certificate_authorities` at the same time.

`ssl.truststore.type`::
(Static)
The format of the truststore file. It must be either `jks` or `PKCS12`. If the
file name ends in ".p12", ".pfx" or "pkcs12", the default is `PKCS12`.
Otherwise, it defaults to `jks`.
`ssl.verification_mode`::
(Static)
Indicates the type of verification when using `ldaps` to protect against man
in the middle attacks and certificate forgery.
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
`ssl.supported_protocols`::
(Static)
Supported protocols with versions. Valid protocols: `SSLv2Hello`,
`SSLv3`, `TLSv1`, `TLSv1.1`, `TLSv1.2`, `TLSv1.3`. If the JVM's SSL provider supports TLSv1.3,
the default is `TLSv1.3,TLSv1.2,TLSv1.1`. Otherwise, the default is
`TLSv1.2,TLSv1.1`.
Elasticsearch relies on your JDK’s implementation of SSL and TLS.
View jdk-tls-versions for more information.
**Note:** If `xpack.security.fips_mode.enabled` is `true`, you cannot use `SSLv2Hello`
or `SSLv3`. See fips-140-compliance.

`ssl.cipher_suites`::
(Static)
Specifies the cipher suites that should be supported when
communicating with the Active Directory server.
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

`cache.ttl`::
(Static)
Specifies the time-to-live for cached user entries. A user and a hash of its
credentials are cached for this configured period of time. Use the
standard Elasticsearch time units).
Defaults to `20m`.

`cache.max_users`::
(Static)
Specifies the maximum number of user entries that the cache can contain.
Defaults to `100000`.

`cache.hash_algo`::
(Static, Expert)
Specifies the hashing algorithm that is used for
the in-memory cached user credentials. See cache-hash-algo. Defaults to `ssha256`.

`authentication.enabled`::
(Static)
If set to `false`, disables authentication support in
this realm, so that it only supports user lookups.
(See the run as and
authorization realms features).
Defaults to `true`.

`follow_referrals`::
(Static)
If set to `true`, Elasticsearch follows referrals returned by the LDAP server.
Referrals are URLs returned by the server that are to be used to continue the
LDAP operation (such as `search`). Defaults to `true`.


##### PKI realm settings

In addition to the settings that are valid for all realms, you can specify
the following settings:

`username_pattern`::
(Static)
The regular expression pattern used to extract the username from the
certificate DN. The username is used for auditing and logging. The username can also be used
with the role mapping API and authorization delegation.
The first match group is the used as the username.
Defaults to `CN=(.*?)(?:,|$)`.

`certificate_authorities`::
(Static)
List of paths to the PEM certificate files that should be used to authenticate a
user's certificate as trusted. Defaults to the trusted certificates configured
for SSL. This setting cannot be used with `truststore.path`.

`truststore.algorithm`::
(Static)
Algorithm for the truststore. Defaults to `SunX509`.

`truststore.password`::
(Static)
The password for the truststore. deprecated:[7.17.0] Prefer `ssl.truststore.secure_password` instead.
You cannot use this setting and `ssl.truststore.secure_password` at the same
time.
If `truststore.path` is set, this setting is required.

`truststore.secure_password`::
(Secure)
Password for the truststore.
`truststore.path`::
(Static)
The path of a truststore to use. Defaults to the trusted certificates configured
for SSL. This setting cannot be used with `certificate_authorities`.

`files.role_mapping`::
(Static)
Specifies the location of the
YAML role mapping configuration file.
Defaults to `ES_PATH_CONF/role_mapping.yml`.

`authorization_realms`::
(Static)
The names of the realms that should be consulted for delegated authorization.
If this setting is used, then the PKI realm does not perform role mapping and
instead loads the user from the listed realms.
See authorization_realms.

`cache.ttl`::
(Static)
Specifies the time-to-live for cached user entries. A user and a hash of its
credentials are cached for this period of time. Use the
standard Elasticsearch time units).
Defaults to `20m`.

`cache.max_users`::
(Static)
Specifies the maximum number of user entries that the cache can contain.
Defaults to `100000`.

`delegation.enabled`::
(Static)
Generally, in order for the clients to be authenticated by the PKI realm they
must connect directly to Elasticsearch. That is, they must not pass through proxies
which terminate the TLS connection. In order to allow for a *trusted* and
*smart* proxy, such as Kibana, to sit before Elasticsearch and terminate TLS
connections, but still allow clients to be authenticated on Elasticsearch by this realm,
you need to toggle this to `true`. Defaults to `false`. If delegation is
enabled, then either `truststore.path` or `certificate_authorities` setting
must be defined. For more details, see <<pki-realm-for-proxied-clients,
Configuring authentication delegation for PKI realms>>.
