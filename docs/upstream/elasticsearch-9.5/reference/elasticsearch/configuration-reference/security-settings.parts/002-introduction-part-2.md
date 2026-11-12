<!-- Part 2 of 8 of reference/elasticsearch/configuration-reference/security-settings.md (split because the page is big). -->

:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) One or more LDAP URLs in the `ldap[s]://<server>:<port>` format. Defaults to `ldap://<domain_name>:389`. This setting is required when connecting using SSL/TLS or when using a custom port.

    To provide multiple URLs, use a YAML array (`["ldap://server1:636", "ldap://server2:636"]`) or comma-separated string (`"ldap://server1:636, ldap://server2:636"`).

    While both are supported, you can’t mix the `ldap` and `ldaps` protocols.

    If no URL is provided, Elasticsearch uses a default of `ldap://<domain_name>:389`. This default uses the `domain_name` setting value and assumes an unencrypted connection to port 389.


`load_balance.type`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) The behavior to use when there are multiple LDAP URLs defined. For supported values see [load balancing and failover types](#load-balancing). Defaults to `failover`.

`load_balance.cache_ttl`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) When using `dns_failover` or `dns_round_robin` as the load balancing type, this setting controls the amount of time to cache DNS lookups. Defaults to `1h`.

`domain_name`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) The domain name of Active Directory. If the `url` and the `user_search.base_dn` settings are not specified, the cluster can derive those values from this setting. Required.

`bind_dn`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) The DN of the user that is used to bind to Active Directory and perform searches. Defaults to Empty. Due to its potential security impact, `bind_dn` is not exposed via the [nodes info API](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-nodes-info).

`bind_password`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) The password for the user that is used to bind to Active Directory. Defaults to Empty. Due to its potential security impact, `bind_password` is not exposed via the [nodes info API](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-nodes-info).

    :::{admonition} Deprecated in 6.3
    Use `secure_bind_password` instead.
    :::

`secure_bind_password`
:   ([Secure](docs-content://deploy-manage/security/secure-settings.md), [Reloadable](docs-content://deploy-manage/security/secure-settings.md#reloadable-secure-settings)) The password for the user that is used to bind to Active Directory. Defaults to Empty.

`unmapped_groups_as_roles`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) If set to `true`, the names of any unmapped Active Directory groups are used as role names and assigned to the user. A group is considered *unmapped* when it is not referenced in any role-mapping files. API-based role mappings are not considered. Defaults to `false`.

`files.role_mapping`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) The [location](docs-content://deploy-manage/security.md) for the YAML role mapping configuration file. Defaults to `ES_PATH_CONF/role_mapping.yml`.

`user_search.base_dn`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) The context to search for a user. Defaults to the root of the Active Directory domain.

`user_search.scope`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) Specifies whether the user search should be `sub_tree`, `one_level` or `base`. `one_level` only searches users directly contained within the `base_dn`. `sub_tree` searches all objects contained under `base_dn`. `base` specifies that the `base_dn` is a user object, and that it is the only user considered. Defaults to `sub_tree`.

`user_search.filter`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) Specifies a filter to use to lookup a user given a username. The default filter looks up `user` objects with either `sAMAccountName` or `userPrincipalName`. If specified, this must be a valid LDAP user search filter. For example `(&(objectClass=user)(sAMAccountName={{0}}))`. For more information, see [Search Filter Syntax](https://msdn.microsoft.com/en-us/library/aa746475(v=vs.85).aspx).

`user_search.upn_filter`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) Specifies a filter to use to lookup a user given a user principal name. The default filter looks up `user` objects with a matching `userPrincipalName`. If specified, this must be a valid LDAP user search filter. For example, `(&(objectClass=user)(userPrincipalName={{1}}))`. `{{1}}` is the full user principal name provided by the user. For more information, see [Search Filter Syntax](https://msdn.microsoft.com/en-us/library/aa746475(v=vs.85).aspx).

`user_search.down_level_filter`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) Specifies a filter to use to lookup a user given a down level logon name (DOMAIN\user). The default filter looks up `user` objects with a matching `sAMAccountName` in the domain provided. If specified, this must be a valid LDAP user search filter. For example, `(&(objectClass=user)(sAMAccountName={{0}}))`. For more information, see [Search Filter Syntax](https://msdn.microsoft.com/en-us/library/aa746475(v=vs.85).aspx).

`user_search.pool.enabled`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) Enables or disables connection pooling for user search. When disabled a new connection is created for every search. The default is `true` when `bind_dn` is provided.

`user_search.pool.size`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) The maximum number of connections to the Active Directory server to allow in the connection pool. Defaults to `20`.

`user_search.pool.initial_size`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) The initial number of connections to create to the Active Directory server on startup. Defaults to `0`. If the LDAP server is down, values greater than 0 could cause startup failures.

`user_search.pool.health_check.enabled`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) Enables or disables a health check on Active Directory connections in the connection pool. Connections are checked in the background at the specified interval. Defaults to `true`.

`user_search.pool.health_check.dn`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) The distinguished name to be retrieved as part of the health check. Defaults to the value of `bind_dn` if that setting is present. Otherwise, it defaults to the value of the `user_search.base_dn` setting.

`user_search.pool.health_check.interval`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) The interval to perform background checks of connections in the pool. Defaults to `60s`.

`group_search.base_dn`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) The context to search for groups in which the user has membership. Defaults to the root of the Active Directory domain.

`group_search.scope`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) Specifies whether the group search should be `sub_tree`, `one_level` or `base`.  `one_level` searches for groups directly contained within the `base_dn`. `sub_tree` searches all objects contained under `base_dn`. `base` specifies that the `base_dn` is a group object, and that it is the only group considered. Defaults to `sub_tree`.

`metadata`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) A list of additional LDAP attributes that should be loaded from the LDAP server and stored in the authenticated user’s metadata field.

`timeout.tcp_connect`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) The TCP connect timeout period for establishing an LDAP connection. An `s` at the end indicates seconds, or `ms` indicates milliseconds. Defaults to `5s` (5 seconds ).

`timeout.tcp_read`
:   :::{admonition} Deprecated in 7.7
    This is equivalent to and is deprecated in favor of `timeout.response` and they cannot be used simultaneously.
    :::

    ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) The TCP read timeout period after establishing an LDAP connection. An `s` at the end indicates seconds, or `ms` indicates milliseconds. Defaults to the value of `timeout.ldap_search`.

`timeout.response`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) The time interval to wait for the response from the AD server. An `s` at the end indicates seconds, or `ms` indicates milliseconds. Defaults to the value of `timeout.ldap_search`.

`timeout.ldap_search`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) The timeout period for an LDAP search. The value is specified in the request and is enforced by the receiving LDAP Server. An `s` at the end indicates seconds, or `ms` indicates milliseconds. Defaults to `5s` (5 seconds ).

`ssl.certificate`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) Specifies the path for the PEM encoded certificate (or certificate chain) that is associated with the key.

    This setting can be used only if `ssl.key` is set.

    This certificate is presented to clients when they connect.


`ssl.certificate_authorities`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) List of paths to PEM encoded certificate files that should be trusted.

    This setting and `ssl.truststore.path` cannot be used at the same time.

    You cannot use this setting and `ssl.truststore.path` at the same time.


`ssl.key`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) Path to a PEM encoded file containing the private key.

    If HTTP client authentication is required, it uses this file. You cannot use this setting and `ssl.keystore.path` at the same time.

    If the Active Directory server requires client authentication, it uses this file. You cannot use this setting and `ssl.keystore.path` at the same time.


`ssl.key_passphrase`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) The passphrase that is used to decrypt the private key. Since the key might not be encrypted, this value is optional.

    :::{admonition} Deprecated in 7.17.0
    Prefer `ssl.secure_key_passphrase` instead.
    :::

    You cannot use this setting and `ssl.secure_key_passphrase` at the same time.


`ssl.secure_key_passphrase`
:   ([Secure](docs-content://deploy-manage/security/secure-settings.md)) The passphrase that is used to decrypt the private key. Since the key might not be encrypted, this value is optional.

`ssl.keystore.key_password`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) The password for the key in the keystore. The default is the keystore password.

    :::{admonition} Deprecated in 7.17.0
    Prefer `ssl.keystore.secure_key_password` instead.
    :::

    You cannot use this setting and `ssl.keystore.secure_password` at the same time.


`ssl.keystore.secure_key_password`
:   ([Secure](docs-content://deploy-manage/security/secure-settings.md)) The password for the key in the keystore. The default is the keystore password.

`ssl.keystore.password`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) The password for the keystore.

    :::{admonition} Deprecated in 7.17.0
    Prefer `ssl.keystore.secure_password` instead.
    :::

`ssl.secure_keystore.password`
:   ([Secure](docs-content://deploy-manage/security/secure-settings.md)) The password for the keystore.

`ssl.keystore.path`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) The path for the keystore file that contains a private key and certificate.

    It must be either a Java keystore (jks) or a PKCS#12 file. You cannot use this setting and `ssl.key` at the same time.

    You cannot use this setting and `ssl.key` at the same time.


`ssl.keystore.type`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) The format of the keystore file. It must be either `jks` or `PKCS12`. If the keystore path ends in ".p12", ".pfx", or ".pkcs12", this setting defaults to `PKCS12`. Otherwise, it defaults to `jks`.

`ssl.truststore.password`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) The password for the truststore.

    :::{admonition} Deprecated in 7.17.0
    Prefer `ssl.truststore.secure_password` instead.
    :::

    You cannot use this setting and `ssl.truststore.secure_password` at the same time.


`ssl.truststore.secure_password`
:   ([Secure](docs-content://deploy-manage/security/secure-settings.md)) Password for the truststore.

`ssl.truststore.path`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) The path for the keystore that contains the certificates to trust. It must be either a Java keystore (jks) or a PKCS#12 file.

    You cannot use this setting and `ssl.certificate_authorities` at the same time.

    You cannot use this setting and `ssl.certificate_authorities` at the same time.


`ssl.truststore.type`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) The format of the truststore file. It must be either `jks` or `PKCS12`. If the file name ends in ".p12", ".pfx" or "pkcs12", the default is `PKCS12`. Otherwise, it defaults to `jks`.

`ssl.verification_mode`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) Indicates the type of verification when using `ldaps` to protect against man in the middle attacks and certificate forgery.

     Defaults to `full`.

    **Valid values**:
    * `full`:   Validates that the provided certificate: has an issue date that’s within the `not_before` and `not_after` dates; chains to a trusted Certificate Authority (CA); has a `hostname` or IP address that matches the names within the certificate.
    * `certificate`:   Validates the provided certificate and verifies that it’s signed by a trusted authority (CA), but doesn’t check the certificate `hostname`.
    * `none`:   Performs no certificate validation.

      ::::{important}
      Setting certificate validation to `none` disables many security benefits of SSL/TLS, which is very dangerous. Only set this value if instructed by Elastic Support as a temporary diagnostic mechanism when attempting to resolve TLS errors.
      ::::

`ssl.supported_protocols`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) Supported protocols with versions. Valid protocols: `SSLv2Hello`, `SSLv3`, `TLSv1`, `TLSv1.1`, `TLSv1.2`, `TLSv1.3`. If the JVM’s SSL provider supports TLSv1.3, the default is `TLSv1.3,TLSv1.2,TLSv1.1`. Otherwise, the default is `TLSv1.2,TLSv1.1`.

    Elasticsearch relies on your JDK’s implementation of SSL and TLS. View [Supported SSL/TLS versions by JDK version](docs-content://deploy-manage/security/supported-ssltls-versions-by-jdk-version.md) for more information.

    ::::{note}
    If `xpack.security.fips_mode.enabled` is `true`, you cannot use `SSLv2Hello` or `SSLv3`. See [FIPS 140-2](docs-content://deploy-manage/security/fips-140-2.md).
    ::::


`ssl.cipher_suites`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) Specifies the cipher suites that should be supported when communicating with the Active Directory server. Supported cipher suites vary depending on which version of Java you use. For example, for version 12 the default value is `TLS_AES_256_GCM_SHA384`, `TLS_AES_128_GCM_SHA256`, `TLS_CHACHA20_POLY1305_SHA256`, `TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384`, `TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256`, `TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384`, `TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256`, `TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256`, `TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256`, `TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA384`, `TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256`, `TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384`, `TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256`, `TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA`, `TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA`, `TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA`, `TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA`, `TLS_RSA_WITH_AES_256_GCM_SHA384`, `TLS_RSA_WITH_AES_128_GCM_SHA256`, `TLS_RSA_WITH_AES_256_CBC_SHA256`, `TLS_RSA_WITH_AES_128_CBC_SHA256`, `TLS_RSA_WITH_AES_256_CBC_SHA`, `TLS_RSA_WITH_AES_128_CBC_SHA`.

    For more information, see Oracle’s [Java Cryptography Architecture documentation](https://docs.oracle.com/en/java/javase/11/security/java-cryptography-architecture-jca-reference-guide.html).


`cache.ttl`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) Specifies the time-to-live for cached user entries. A user and a hash of its credentials are cached for this configured period of time. Use the standard Elasticsearch [time units](/reference/elasticsearch/rest-apis/api-conventions.md#time-units)). Defaults to `20m`.

`cache.max_users`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) Specifies the maximum number of user entries that the cache can contain. Defaults to `100000`.

`cache.hash_algo`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting), Expert) Specifies the hashing algorithm that is used for the in-memory cached user credentials. See [Table 1, Cache hash algorithms](#cache-hash-algo). Defaults to `ssha256`.

`authentication.enabled`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) If set to `false`, disables authentication support in this realm, so that it only supports user lookups. (See the [run as](docs-content://deploy-manage/users-roles/cluster-or-deployment-auth/submitting-requests-on-behalf-of-other-users.md) and [authorization realms](docs-content://deploy-manage/users-roles/cluster-or-deployment-auth/realm-chains.md#authorization_realms) features). Defaults to `true`.

`follow_referrals`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) If set to `true`, Elasticsearch follows referrals returned by the LDAP server. Referrals are URLs returned by the server that are to be used to continue the LDAP operation (such as `search`). Defaults to `true`.


#### PKI realm settings [ref-pki-settings]

In addition to the [settings that are valid for all realms](#ref-realm-settings), you can specify the following settings:

`username_pattern`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) The regular expression pattern used to extract the username from the certificate DN. The username is used for auditing and logging. The username can also be used with the [role mapping API](docs-content://deploy-manage/users-roles/cluster-or-deployment-auth/mapping-users-groups-to-roles.md) and [authorization delegation](docs-content://deploy-manage/users-roles/cluster-or-deployment-auth/authorization-delegation.md). The first match group is the used as the username. Defaults to `CN=(.*?)(?:,|$)`.

    This setting is ignored if either `username_rdn_oid` or `username_rdn_name` is set.

`username_rdn_oid`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) The relative distinguished name (RDN) attribute OID used to extract the username from the certificate DN. The username is used for auditing and logging. The username can also be used with the [role mapping API](docs-content://deploy-manage/users-roles/cluster-or-deployment-auth/mapping-users-groups-to-roles.md) and [authorization delegation](docs-content://deploy-manage/users-roles/cluster-or-deployment-auth/authorization-delegation.md). The value of the most specific RDN matching this attribute OID is used as the username.

    This setting takes precedent over `username_pattern`. You cannot use this setting and `username_rdn_name` at the same time.

`username_rdn_name`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) The relative distinguished name (RDN) attribute name used to extract the username from the certificate DN. The username is used for auditing and logging. The username can also be used with the [role mapping API](docs-content://deploy-manage/users-roles/cluster-or-deployment-auth/mapping-users-groups-to-roles.md) and [authorization delegation](docs-content://deploy-manage/users-roles/cluster-or-deployment-auth/authorization-delegation.md). The value of the most specific RDN matching this attribute name is used as the username.

    This setting takes precedent over `username_pattern`. You cannot use this setting and `username_rdn_oid` at the same time.

`certificate_authorities`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) List of paths to the PEM certificate files that should be used to authenticate a user’s certificate as trusted. Defaults to the trusted certificates configured for SSL. This setting cannot be used with `truststore.path`.

`truststore.algorithm`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) Algorithm for the truststore. Defaults to `SunX509`.

`truststore.password`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) The password for the truststore.

    :::{admonition} Deprecated in 7.17.0
    Prefer `ssl.truststore.secure_password` instead.
    :::

    You cannot use this setting and `ssl.truststore.secure_password` at the same time.


If `truststore.path` is set, this setting is required.

`truststore.secure_password`
:   ([Secure](docs-content://deploy-manage/security/secure-settings.md)) Password for the truststore.

`truststore.path`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) The path of a truststore to use. Defaults to the trusted certificates configured for SSL. This setting cannot be used with `certificate_authorities`.

`files.role_mapping`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) Specifies the [location](docs-content://deploy-manage/security.md) of the [YAML role mapping configuration file](docs-content://deploy-manage/users-roles/cluster-or-deployment-auth/mapping-users-groups-to-roles.md). Defaults to `ES_PATH_CONF/role_mapping.yml`.

`authorization_realms`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) The names of the realms that should be consulted for delegated authorization. If this setting is used, then the PKI realm does not perform role mapping and instead loads the user from the listed realms. See [Delegating authorization to another realm](docs-content://deploy-manage/users-roles/cluster-or-deployment-auth/realm-chains.md#authorization_realms).

`cache.ttl`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) Specifies the time-to-live for cached user entries. A user and a hash of its credentials are cached for this period of time. Use the standard Elasticsearch [time units](/reference/elasticsearch/rest-apis/api-conventions.md#time-units)). Defaults to `20m`.

`cache.max_users`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) Specifies the maximum number of user entries that the cache can contain. Defaults to `100000`.

`delegation.enabled`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) Generally, in order for the clients to be authenticated by the PKI realm they must connect directly to Elasticsearch. That is, they must not pass through proxies which terminate the TLS connection. In order to allow for a **trusted** and **smart** proxy, such as Kibana, to sit before Elasticsearch and terminate TLS connections, but still allow clients to be authenticated on Elasticsearch by this realm, you need to toggle this to `true`. Defaults to `false`. If delegation is enabled, then either `truststore.path` or `certificate_authorities` setting must be defined. For more details, see [Configuring authentication delegation for PKI realms](docs-content://deploy-manage/users-roles/cluster-or-deployment-auth/pki.md#pki-realm-for-proxied-clients).


#### SAML realm settings [ref-saml-settings]

In addition to the [settings that are valid for all realms](#ref-realm-settings), you can specify the following settings.

`idp.entity_id` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on Elastic Cloud Hosted")
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) The Entity ID of the SAML Identity Provider. An Entity ID is a URI with a maximum length of 1024 characters. It can be a URL ([https://idp.example.com/](https://idp.example.com/)) or a URN (`urn:example.com:idp`) and can be found in the configuration or the SAML metadata of the Identity Provider.

`idp.metadata.path` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on Elastic Cloud Hosted")
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) The path *(recommended)* or URL to a SAML 2.0 metadata file describing the capabilities and configuration of the Identity Provider. If a path is provided, then it is resolved relative to the Elasticsearch config directory. If a URL is provided, then it must be either a `file` URL or a `https` URL.

    Elasticsearch automatically polls this metadata resource and reloads the IdP configuration when changes are detected. File based resources are polled at a frequency determined by the global Elasticsearch `resource.reload.interval.high` setting, which defaults to 5 seconds. HTTPS resources are polled at a frequency determined by the realm’s `idp.metadata.http.refresh` and `idp.metadata.http.minimum_refresh` settings.

    If the metadata resource is loaded from a file then the file must exist at node startup, if it does not exist then the node will fail to start. If the resource is loaded over HTTPS then (by default) the node will be tolerant of a failure to load the resource - the node will start and will continue to poll the URL for updates. The affected SAML realm will fail to authenticate users until the problem is resolved. To force the node to fail if the metadata is unavailable set `idp.metadata.http.fail_on_error` to `true`.


`idp.metadata.http.fail_on_error`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) If set to `true`, the realm will fail on startup (and prevent the node from starting) if it attempts to load metadata over HTTPS and that metadata is not available. If set to `false` (the default), the node will start but the affected SAML realm will not support user authentication until the metadata can be successfully loaded. This setting is ignored if metadata is loaded from a file.

`idp.metadata.http.connect_timeout` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on Elastic Cloud Hosted") {applies_to}`stack: ga 9.1`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) Controls the behavior of the HTTP client that is used for fetching the SAML 2.0 metadata file from a remote URL. Specifies the maximum time the client waits for a connection to be established. A value of zero means the timeout is not used. Defaults to `5s`.

`idp.metadata.http.read_timeout` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on Elastic Cloud Hosted") {applies_to}`stack: ga 9.1`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) Controls the behavior of the HTTP client that is used for fetching the SAML 2.0 metadata file from a remote URL. Specifies the maximum time the client waits when requesting a connection from the connection manager. Defaults to `10s`.

`idp.metadata.http.refresh` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on Elastic Cloud Hosted")
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) Controls the frequency with which `https` metadata is checked for changes. Defaults to `1h` (1 hour).

    Under some circumstances Elasticsearch may determine that the metadata needs to be checked more frequently. This may occur if previous attempts to load the metadata encountered an error, or if the metadata indicates that it is due to expire in less than the configured refresh interval. In these cases Elasticsearch will poll more often, but never more frequently than `idp.metadata.http.minimum_refresh`. If there is an attempt to authenticate against a realm that has not yet loaded metadata successfully, that realm may attempt to load metadata outside of the configured polling frequency.


`idp.metadata.http.minimum_refresh`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) Controls the minimum frequency with which `https` metadata is checked for changes. In regular operation Elasticsearch will use the value of `idp.metadata.http.refresh` as the polling interval. However, under some circumstances Elasticsearch may determine that it needs to poll more frequently. In these cases, the `minimum_refresh` will set the minimum frequency at which the metadata will be checked. Defaults to `5m` (5 minutes) and must not be set to a value greater than `idp.metadata.http.refresh`

`idp.use_single_logout` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on Elastic Cloud Hosted")
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) Indicates whether to utilise the Identity Provider’s Single Logout service (if one exists in the IdP metadata file). Defaults to `true`.

`sp.entity_id` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on Elastic Cloud Hosted")
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) The Entity ID to use for this SAML Service Provider. This should be entered as a URI. We recommend that you use the base URL of your Kibana instance. For example, `https://kibana.example.com/`.

`sp.acs` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on Elastic Cloud Hosted")
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) The URL of the Assertion Consumer Service within Kibana. Typically this is the "api/security/saml/callback" endpoint of your Kibana server. For example, `https://kibana.example.com/api/security/saml/callback`.

`sp.logout` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on Elastic Cloud Hosted")
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) The URL of the Single Logout service within Kibana. Typically this is the "logout" endpoint of your Kibana server. For example, `https://kibana.example.com/logout`.

`attributes.principal` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on Elastic Cloud Hosted")
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) The Name of the SAML attribute that contains the user’s principal (username).

`attributes.groups` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on Elastic Cloud Hosted")
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) The Name of the SAML attribute that contains the user’s groups.

`attributes.name` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on Elastic Cloud Hosted")
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) The Name of the SAML attribute that contains the user’s full name.

`attributes.mail` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on Elastic Cloud Hosted")
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) The Name of the SAML attribute that contains the user’s email address.

`attributes.dn` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on Elastic Cloud Hosted")
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) The Name of the SAML attribute that contains the user’s X.50 *Distinguished Name*.

`attribute_patterns.principal` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on Elastic Cloud Hosted")
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) A Java regular expression that is matched against the SAML attribute specified by `attributes.principal` before it is applied to the user’s *principal* property. The attribute value must match the pattern and the value of the first *capturing group* is used as the principal. For example, `^([^@]+)@example\\.com$` matches email addresses from the "example.com" domain and uses the local-part as the principal.

`attribute_patterns.groups` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on Elastic Cloud Hosted")
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) As per `attribute_patterns.principal`, but for the *group* property.

`attribute_patterns.name` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on Elastic Cloud Hosted")
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) As per `attribute_patterns.principal`, but for the *name* property.

`attribute_patterns.mail` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on Elastic Cloud Hosted")
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) As per `attribute_patterns.principal`, but for the *mail* property.

`attribute_patterns.dn` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on Elastic Cloud Hosted")
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) As per `attribute_patterns.principal`, but for the *dn* property.

`attribute_delimiters.groups` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on Elastic Cloud Hosted")
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) A plain string that is used as a delimiter to split a single-valued SAML attribute specified by `attributes.groups` before it is applied to the user’s *groups* property. For example, splitting the SAML attribute value `engineering,elasticsearch-admins,employees` on a delimiter value of `,` will result in `engineering`, `elasticsearch-admins`, and `employees` as the list of groups for the user. The delimiter will always be split on, regardless of escaping in the input string. This setting does not support multi-valued SAML attributes. It cannot be used together with the `attribute_patterns` setting. You can only configure this setting for the groups attribute.

`nameid_format` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on Elastic Cloud Hosted")
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) The NameID format that should be requested when asking the IdP to authenticate the current user. The default is to not include the `nameid_format` attribute.

`nameid.allow_create` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on Elastic Cloud Hosted")
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) The value of the `AllowCreate` attribute of the `NameIdPolicy` element in an authentication request. The default value is false.

`nameid.sp_qualifier` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on Elastic Cloud Hosted")
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) The value of the `SPNameQualifier` attribute of the `NameIdPolicy` element in an authentication request. The default is to not include the `SPNameQualifier` attribute.

`force_authn` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on Elastic Cloud Hosted")
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) Specifies whether to set the `ForceAuthn` attribute when requesting that the IdP authenticate the current user. If set to `true`, the IdP is required to verify the user’s identity, irrespective of any existing sessions they might have. Defaults to `false`.

`populate_user_metadata` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on Elastic Cloud Hosted")
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) Specifies whether to populate the Elasticsearch user’s metadata with the values that are provided by the SAML attributes. Defaults to `true`.

`authorization_realms`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) The names of the realms that should be consulted for delegated authorization. If this setting is used, then the SAML realm does not perform role mapping and instead loads the user from the listed realms. See [Delegating authorization to another realm](docs-content://deploy-manage/users-roles/cluster-or-deployment-auth/realm-chains.md#authorization_realms).

`allowed_clock_skew` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on Elastic Cloud Hosted")
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) The maximum amount of skew that can be tolerated between the IdP’s clock and the Elasticsearch node’s clock. Defaults to `3m` (3 minutes).

`req_authn_context_class_ref` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on Elastic Cloud Hosted")
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) A comma separated list of Authentication Context Class Reference values to be included in the Requested Authentication Context when requesting the IdP to authenticate the current user. The Authentication Context of the corresponding authentication response should contain at least one of the requested values.

    For more information, see [Requesting specific authentication methods](docs-content://deploy-manage/users-roles/cluster-or-deployment-auth/saml.md#req-authn-context).



#### SAML realm signing settings [ref-saml-signing-settings]

If a signing key is configured (that is, either `signing.key` or `signing.keystore.path` is set), then Elasticsearch signs outgoing SAML messages. Signing can be configured using the following settings:

`signing.saml_messages` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on Elastic Cloud Hosted")
