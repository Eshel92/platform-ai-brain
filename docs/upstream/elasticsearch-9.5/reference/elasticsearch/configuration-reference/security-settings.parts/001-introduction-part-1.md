<!-- Part 1 of 8 of reference/elasticsearch/configuration-reference/security-settings.md (split because the page is big). -->

# Security settings in Elasticsearch [security-settings]


You configure `xpack.security` settings to [enable anonymous access](#anonymous-access-settings) and perform message authentication, [set up document and field level security](#field-document-security-settings), [configure realms](#realm-settings), [encrypt communications with SSL](#ssl-tls-settings),and [audit security events](/reference/elasticsearch/configuration-reference/auding-settings.md).

All of these settings can be added to the `elasticsearch.yml` configuration file, with the exception of the secure settings, which you add to the Elasticsearch keystore. For more information about creating and updating the Elasticsearch keystore, see [Secure settings](docs-content://deploy-manage/security/secure-settings.md).


### General security settings [general-security-settings]

`xpack.security.enabled`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) Defaults to `true`, which enables Elasticsearch security features on the node. This setting must be enabled to use Elasticsearch’s authentication, authorization and audit features.<br>

    If set to `false`, security features are disabled, which is not recommended. It also affects all Kibana instances that connect to this Elasticsearch instance; you do not need to disable security features in those `kibana.yml` files. For more information about disabling security features in specific Kibana instances, see [Kibana security settings](kibana://reference/configuration-reference/security-settings.md).


`xpack.security.autoconfiguration.enabled`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) Defaults to `true`, which enables [security auto configuration](docs-content://deploy-manage/deploy/self-managed/installing-elasticsearch.md).

    If set to `false`, security auto configuration is disabled, which is not recommended. When disabled, security is not configured automatically when starting Elasticsearch for the first time, which means that you must [manually configure security](docs-content://deploy-manage/security/manually-configure-security-in-self-managed-cluster.md).


`xpack.security.enrollment.enabled`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) Defaults to `false`. Controls enrollment (of nodes and Kibana) to a local node that’s been [autoconfigured for security](docs-content://deploy-manage/deploy/self-managed/installing-elasticsearch.md). When set to `true`, the local node can generate new enrollment tokens. Existing tokens can be used for enrollment if they are still valid.

    The security autoconfiguration process will set this to `true` unless an administrator sets it to `false` before starting Elasticsearch.


`xpack.security.hide_settings`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) A comma-separated list of settings that are omitted from the results of the [cluster nodes info API](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-nodes-info). You can use wildcards to include multiple settings in the list. For example, the following value hides all the settings for the ad1 active_directory realm: `xpack.security.authc.realms.active_directory.ad1.*`. The API already omits all `ssl` settings, `bind_dn`, and `bind_password` due to the sensitive nature of the information.

`xpack.security.fips_mode.enabled`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) Enables fips mode of operation. Set this to `true` if you run this Elasticsearch instance in a FIPS 140-2 enabled JVM. For more information, see [FIPS 140-2](docs-content://deploy-manage/security/fips-140-2.md). Defaults to `false`.

`xpack.security.fips_mode.required_providers`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) Optionally enforce specific Java JCE/JSSE security providers. For example, set this to `["BCFIPS", "BCJSSE"]` (case-insensitive) to require the Bouncy Castle FIPS JCE and JSSE security providers. Only applicable when `xpack.security.fips_mode.enabled` is set to `true`.


### Password hashing settings [password-hashing-settings]

`xpack.security.authc.password_hashing.algorithm`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) Specifies the hashing algorithm that is used for secure user credential storage. See [Table 2, Password hashing algorithms](#password-hashing-algorithms). If `xpack.security.fips_mode.enabled` is true (see [FIPS 140-2](docs-content://deploy-manage/security/fips-140-2.md)), defaults to `pbkdf2_stretch`. In all other cases, defaults to `bcrypt`.


### Anonymous access settings [anonymous-access-settings]

You can configure the following anonymous access settings in `elasticsearch.yml`. For more information, see [Enabling anonymous access](docs-content://deploy-manage/users-roles/cluster-or-deployment-auth/anonymous-access.md).

`xpack.security.authc.anonymous.username` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on Elastic Cloud Hosted")
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) The username (principal) of the anonymous user. Defaults to `_es_anonymous_user`.

`xpack.security.authc.anonymous.roles` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on Elastic Cloud Hosted")
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) The roles to associate with the anonymous user. Required.

`xpack.security.authc.anonymous.authz_exception` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on Elastic Cloud Hosted")
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) When `true`, an HTTP 403 response is returned if the anonymous user does not have the appropriate permissions for the requested action. The user is not prompted to provide credentials to access the requested resource. When set to `false`, an HTTP 401 response is returned and the user can provide credentials with the appropriate permissions to gain access. Defaults to `true`.


### Automata Settings [security-automata-settings]

In places where the security features accept wildcard patterns (e.g. index patterns in roles, group matches in the role mapping API), each pattern is compiled into an Automaton. The follow settings are available to control this behaviour.

`xpack.security.automata.max_determinized_states`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) The upper limit on how many automaton states may be created by a single pattern. This protects against too-difficult (e.g. exponentially hard) patterns. Defaults to `100,000`.

`xpack.security.automata.cache.enabled`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) Whether to cache the compiled automata. Compiling automata can be CPU intensive and may slowdown some operations. The cache reduces the frequency with which automata need to be compiled. Defaults to `true`.

`xpack.security.automata.cache.size`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) The maximum number of items to retain in the automata cache. Defaults to `10,000`.

`xpack.security.automata.cache.ttl`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) The length of time to retain in an item in the automata cache (based on most recent usage). Defaults to `48h` (48 hours).


### Document and field level security settings [field-document-security-settings]

You can set the following document and field level security settings in `elasticsearch.yml`. For more information, see [Setting up field and document level security](docs-content://deploy-manage/users-roles/cluster-or-deployment-auth/controlling-access-at-document-field-level.md).

`xpack.security.dls_fls.enabled`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) Set to `false` to prevent document and field level security from being configured. Defaults to `true`.

`xpack.security.dls.bitset.cache.ttl`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) The time-to-live for cached `BitSet` entries for document level security. Document level security queries may depend on Lucene BitSet objects, and these are automatically cached to improve performance. Defaults to expire entries that are unused for `2h` (2 hours).

`xpack.security.dls.bitset.cache.size`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) The maximum memory usage of cached `BitSet` entries for document level security. Document level security queries may depend on Lucene BitSet objects, and these are automatically cached to improve performance. Can be configured as a raw number of bytes (such as `200mb` or `1g`) or a percentage of the node’s JVM heap memory (such as `5%`). When the default value is exceeded, the least recently used entries are evicted. Defaults to `10%` of the heap assigned to the node.


### Token service settings [token-service-settings]

You can set the following token service settings in `elasticsearch.yml`.

`xpack.security.authc.token.enabled`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) Set to `false` to disable the built-in token service. Defaults to `true` unless `xpack.security.http.ssl.enabled` is `false`. This prevents sniffing the token from a connection over plain http.

`xpack.security.authc.token.timeout`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) The length of time that a token is valid for. By default this value is `20m` or 20 minutes. The maximum value is 1 hour.


### API key service settings [api-key-service-settings]

You can set the following API key service settings in `elasticsearch.yml`.

`xpack.security.authc.api_key.enabled`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) Set to `false` to disable the built-in API key service. Defaults to `true`.

`xpack.security.authc.api_key.cache.ttl`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) The time-to-live for cached API key entries. A API key id and a hash of its API key are cached for this period of time. Specify the time period using the standard Elasticsearch [time units](/reference/elasticsearch/rest-apis/api-conventions.md#time-units). Defaults to `1d`.

`xpack.security.authc.api_key.cache.max_keys`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) The maximum number of API key entries that can live in the cache at any given time. Defaults to 10,000.

`xpack.security.authc.api_key.cache.hash_algo`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting), Expert) The hashing algorithm that is used for the in-memory cached API key credentials. For possible values, see [Table 1, Cache hash algorithms](#cache-hash-algo). Defaults to `ssha256`.

$$$api-key-service-settings-delete-retention-period$$$

`xpack.security.authc.api_key.delete.retention_period`
:   ([Dynamic](docs-content://deploy-manage/stack-settings.md#dynamic-cluster-setting)) Invalidated or expired API keys older than the retention period are eligible for deletion. Defaults to `7d`.

::::{note}
Large real-time clock inconsistency across cluster nodes can cause problems with evaluating the API key retention period. That is, if the clock on the node invalidating the API key is significantly different than the one performing the deletion, the key may be retained for longer or shorter than the configured retention period.
::::


`xpack.security.authc.api_key.delete.interval`
:   ([Dynamic](docs-content://deploy-manage/stack-settings.md#dynamic-cluster-setting), Expert) Cluster nodes schedule the automatic deletion of invalidated or expired API keys that are older than the retention period. This setting controls the minimum time interval between two such deletion jobs. Defaults to `24h`.

    ::::{note}
    This is a low-level setting that currently controls the interval between deletion jobs triggered per-node, not across the cluster.
    ::::


`xpack.security.authc.api_key.delete.timeout`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting), Expert) Sets the timeout of the internal search and delete call.

`xpack.security.authc.api_key.hashing.algorithm`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) Specifies the hashing algorithm that is used for securing API key credentials. See [Table 3, Secure token hashing algorithms](#secure-token-hashing-algorithms). Defaults to `ssha256`.


### Security domain settings [security-domain-settings]

You configure security domain settings in the `xpack.security.authc.domains` namespace in `elasticsearch.yml`.

For example:

```yaml
xpack:
  security:
    authc:
      domains:
        my_domain: <1>
          realms: [ 'default_native', 'saml1' ] <2>
```

1. Specifies the name of the security domain
2. Specifies the realms that belong to the domain



### Realm settings [realm-settings]

`xpack.security.authc.realms.saml.*` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on Elastic Cloud Hosted")
:   To learn more on how to enable SAML and related user settings, check [secure your clusters with SAML](docs-content://deploy-manage/users-roles/cluster-or-deployment-auth/saml.md).

`xpack.security.authc.realms.oidc.*` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on Elastic Cloud Hosted")
:   To learn more on how to enable OpenID Connect and related user settings, check [secure your clusters with OpenID Connect](docs-content://deploy-manage/users-roles/cluster-or-deployment-auth/openid-connect.md).

`xpack.security.authc.realms.kerberos.*` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on Elastic Cloud Hosted")
:   To learn more on how to enable Kerberos and relate user settings, check [secure your clusters with Kerberos](docs-content://deploy-manage/users-roles/cluster-or-deployment-auth/kerberos.md).

`xpack.security.authc.realms.jwt.*` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on Elastic Cloud Hosted")
:   To learn more on how to enable JWT and related user settings, check [secure your clusters with JWT](docs-content://deploy-manage/users-roles/cluster-or-deployment-auth/jwt.md).

::::{note}
All SAML, OpenID Connect, Kerberos, and JWT settings are allowlisted.
::::

You configure realm settings in the `xpack.security.authc.realms` namespace in `elasticsearch.yml`.

For example:

```yaml
xpack.security.authc.realms:

    native.realm1: <1>
        order: 0 <2>
        ...

    ldap.realm2:
        order: 1
        ...

    active_directory.realm3:
        order: 2
        ...
    ...
```

1. Specifies the type of realm (for example, `native`, `ldap`, `active_directory`, `pki`, `file`, `kerberos`, `saml`) and the realm name. This information is required.
2. Specifies priority of a realm in the realm chain. This information is required.


The valid settings vary depending on the realm type. For more information, see [*User authentication*](docs-content://deploy-manage/users-roles/cluster-or-deployment-auth/user-authentication.md).


#### Settings valid for all realms [ref-realm-settings]

`order`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) The priority of the realm within the realm chain. Realms with a lower order are consulted first. The value must be unique for each realm. This setting is required.

`enabled`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) Indicates whether a realm is enabled. You can use this setting to disable a realm without removing its configuration information. Defaults to `true`.


#### Native realm settings [ref-native-settings]

In addition to the [settings that are valid for all realms](#ref-realm-settings), you can specify the following optional settings:

`cache.ttl`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) The time-to-live for cached user entries. A user and a hash of its credentials are cached for this period of time. Specify the time period using the standard Elasticsearch [time units](/reference/elasticsearch/rest-apis/api-conventions.md#time-units). Defaults to `20m`.

`cache.max_users`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) The maximum number of user entries that can live in the cache at any given time. Defaults to 100,000.

`cache.hash_algo`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting), Expert) The hashing algorithm that is used for the in-memory cached user credentials. For possible values, see [Table 1, Cache hash algorithms](#cache-hash-algo). Defaults to `ssha256`.

`authentication.enabled`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) If set to `false`, disables authentication support in this realm, so that it only supports user lookups. (See the [run as](docs-content://deploy-manage/users-roles/cluster-or-deployment-auth/submitting-requests-on-behalf-of-other-users.md) and [authorization realms](docs-content://deploy-manage/users-roles/cluster-or-deployment-auth/realm-chains.md#authorization_realms) features). Defaults to `true`.


#### File realm settings [ref-users-settings]

In addition to the [settings that are valid for all realms](#ref-realm-settings), you can specify the following settings:

`cache.ttl`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) The time-to-live for cached user entries. A user and a hash of its credentials are cached for this configured period of time. Defaults to `20m`. Specify values using the standard Elasticsearch [time units](/reference/elasticsearch/rest-apis/api-conventions.md#time-units). Defaults to `20m`.

`cache.max_users`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) The maximum number of user entries that can live in the cache at a given time. Defaults to 100,000.

`cache.hash_algo`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting), Expert) The hashing algorithm that is used for the in-memory cached user credentials. See [Table 1, Cache hash algorithms](#cache-hash-algo). Defaults to `ssha256`.

`authentication.enabled`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) If set to `false`, disables authentication support in this realm, so that it only supports user lookups. (See the [run as](docs-content://deploy-manage/users-roles/cluster-or-deployment-auth/submitting-requests-on-behalf-of-other-users.md) and [authorization realms](docs-content://deploy-manage/users-roles/cluster-or-deployment-auth/realm-chains.md#authorization_realms) features). Defaults to `true`.


#### LDAP realm settings [ref-ldap-settings]

In addition to the [Settings valid for all realms](#ref-realm-settings), you can specify the following settings:

`url`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) One or more LDAP URLs in the `ldap[s]://<server>:<port>` format. Required.

    To provide multiple URLs, use a YAML array (`["ldap://server1:636", "ldap://server2:636"]`) or comma-separated string (`"ldap://server1:636, ldap://server2:636"`).

    While both are supported, you can’t mix the `ldap` and `ldaps` protocols.


`load_balance.type`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) The behavior to use when there are multiple LDAP URLs defined. For supported values see [load balancing and failover types](#load-balancing). Defaults to `failover`.

`load_balance.cache_ttl`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) When using `dns_failover` or `dns_round_robin` as the load balancing type, this setting controls the amount of time to cache DNS lookups. Defaults to `1h`.

`bind_dn`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) The DN of the user that is used to bind to the LDAP and perform searches. Only applicable in user search mode. If not specified, an anonymous bind is attempted. Defaults to Empty. Due to its potential security impact, `bind_dn` is not exposed via the [nodes info API](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-nodes-info).

`bind_password`
:   :::{admonition} Deprecated in 6.3
    Use `secure_bind_password` instead.
    :::

    ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) The password for the user that is used to bind to the LDAP directory. Defaults to Empty. Due to its potential security impact, `bind_password` is not exposed via the [nodes info API](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-nodes-info).

`secure_bind_password`
:   ([Secure](docs-content://deploy-manage/security/secure-settings.md), [Reloadable](docs-content://deploy-manage/security/secure-settings.md#reloadable-secure-settings)) The password for the user that is used to bind to the LDAP directory. Defaults to Empty.

`user_dn_templates`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) The DN template that replaces the user name with the string `{{0}}`. This setting is multivalued; you can specify multiple user contexts. Required to operate in user template mode. If `user_search.base_dn` is specified, this setting is not valid. For more information on the different modes, see [LDAP user authentication](docs-content://deploy-manage/users-roles/cluster-or-deployment-auth/ldap.md).

`authorization_realms`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) The names of the realms that should be consulted for delegated authorization. If this setting is used, then the LDAP realm does not perform role mapping and instead loads the user from the listed realms. The referenced realms are consulted in the order that they are defined in this list. See [Delegating authorization to another realm](docs-content://deploy-manage/users-roles/cluster-or-deployment-auth/realm-chains.md#authorization_realms).

    ::::{note}
    If any settings starting with `user_search` are specified, the `user_dn_templates` settings are ignored.
    ::::


`user_group_attribute`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) Specifies the attribute to examine on the user for group membership. If any `group_search` settings are specified, this setting is ignored. Defaults to `memberOf`.

`user_full_name_attribute`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) Specifies the attribute to examine on the user for the full name of the user. Defaults to `cn`.

`user_email_attribute`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) Specifies the attribute to examine on the user for the email address of the user. Defaults to `mail`.

`user_search.base_dn`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) Specifies a container DN to search for users. Required to operated in user search mode. If `user_dn_templates` is specified, this setting is not valid. For more information on the different modes, see [LDAP user authentication](docs-content://deploy-manage/users-roles/cluster-or-deployment-auth/ldap.md).

`user_search.scope`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) The scope of the user search. Valid values are `sub_tree`, `one_level` or `base`. `one_level` only searches objects directly contained within the `base_dn`. `sub_tree` searches all objects contained under `base_dn`. `base` specifies that the `base_dn` is the user object, and that it is the only user considered. Defaults to `sub_tree`.

`user_search.filter`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) Specifies the filter used to search the directory in attempts to match an entry with the username provided by the user. Defaults to `(uid={{0}})`. `{{0}}` is substituted with the username provided when searching.

`user_search.attribute`
:   :::{admonition} Deprecated in 5.6
     Use `user_search.filter` instead.
     :::

     ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) The attribute to match with the username sent with the request. Defaults to `uid`.

`user_search.pool.enabled`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) Enables or disables connection pooling for user search. If set to `false`, a new connection is created for every search. The default is `true` when `bind_dn` is set.

`user_search.pool.size`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) The maximum number of connections to the LDAP server to allow in the connection pool. Defaults to `20`.

`user_search.pool.initial_size`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) The initial number of connections to create to the LDAP server on startup. Defaults to `0`. If the LDAP server is down, values greater than `0` could cause startup failures.

`user_search.pool.health_check.enabled`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) Enables or disables a health check on LDAP connections in the connection pool. Connections are checked in the background at the specified interval. Defaults to `true`.

`user_search.pool.health_check.dn`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) The distinguished name that is retrieved as part of the health check. Defaults to the value of `bind_dn` if present; if not, falls back to `user_search.base_dn`.

`user_search.pool.health_check.interval`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) The interval to perform background checks of connections in the pool. Defaults to `60s`.

`group_search.base_dn`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) The container DN to search for groups in which the user has membership. When this element is absent, Elasticsearch searches for the attribute specified by `user_group_attribute` set on the user in order to determine group membership.

`group_search.scope`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) Specifies whether the group search should be `sub_tree`, `one_level` or `base`.  `one_level` only searches objects directly contained within the `base_dn`. `sub_tree` searches all objects contained under `base_dn`. `base` specifies that the `base_dn` is a group object, and that it is the only group considered. Defaults to  `sub_tree`.

`group_search.filter`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) Specifies a filter to use to look up a group. When not set, the realm searches for `group`, `groupOfNames`, `groupOfUniqueNames`, or `posixGroup` with the attributes `member`, `memberOf`, or `memberUid`. Any instance of `{{0}}` in the filter is replaced by the user attribute defined in `group_search.user_attribute`.

`group_search.user_attribute`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) Specifies the user attribute that is fetched and provided as a parameter to the filter. If not set, the user DN is passed into the filter. Defaults to Empty.

`unmapped_groups_as_roles`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) If set to `true`, the names of any unmapped LDAP groups are used as role names and assigned to the user. A group is considered to be *unmapped* if it is not referenced in a [role-mapping file](docs-content://deploy-manage/users-roles/cluster-or-deployment-auth/mapping-users-groups-to-roles.md#mapping-roles-file). API-based role mappings are not considered. Defaults to `false`.

`files.role_mapping`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) The [location](docs-content://deploy-manage/security.md) for the [YAML role mapping configuration file](docs-content://deploy-manage/users-roles/cluster-or-deployment-auth/mapping-users-groups-to-roles.md). Defaults to `ES_PATH_CONF/role_mapping.yml`.

`follow_referrals`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) Specifies whether Elasticsearch should follow referrals returned by the LDAP server. Referrals are URLs returned by the server that are to be used to continue the LDAP operation (for example, search). Defaults to `true`.

`metadata`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) A list of additional LDAP attributes that should be loaded from the LDAP server and stored in the authenticated user’s metadata field.

`timeout.tcp_connect`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) The TCP connect timeout period for establishing an LDAP connection. An `s` at the end indicates seconds, or `ms` indicates milliseconds. Defaults to `5s` (5 seconds ).

`timeout.tcp_read`
:   :::{admonition} Deprecated in 7.7
    This setting was deprecated in 7.7.
    :::

    ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) The TCP read timeout period after establishing an LDAP connection. This is equivalent to and is deprecated in favor of `timeout.response` and they cannot be used simultaneously. An `s` at the end indicates seconds, or `ms` indicates milliseconds.

`timeout.response`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) The time interval to wait for the response from the LDAP server. An `s` at the end indicates seconds, or `ms` indicates milliseconds. Defaults to the value of `timeout.ldap_search`.

`timeout.ldap_search`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) The timeout period for an LDAP search. The value is specified in the request and is enforced by the receiving LDAP Server. An `s` at the end indicates seconds, or `ms` indicates milliseconds. Defaults to `5s` (5 seconds ).

`ssl.key`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) Path to a PEM encoded file containing the private key.

    If HTTP client authentication is required, it uses this file. You cannot use this setting and `ssl.keystore.path` at the same time.

    If the LDAP server requires client authentication, it uses this file. You cannot use this setting and `ssl.keystore.path` at the same time.


`ssl.key_passphrase`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) The passphrase that is used to decrypt the private key. Since the key might not be encrypted, this value is optional.

    :::{admonition} Deprecated in 7.17.0
    Prefer `ssl.secure_key_passphrase` instead.
    :::

    You cannot use this setting and `ssl.secure_key_passphrase` at the same time.


`ssl.secure_key_passphrase`
:   ([Secure](docs-content://deploy-manage/security/secure-settings.md)) The passphrase that is used to decrypt the private key. Since the key might not be encrypted, this value is optional.

`ssl.certificate`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) Specifies the path for the PEM encoded certificate (or certificate chain) that is associated with the key.

    This setting can be used only if `ssl.key` is set.

    This certificate is presented to clients when they connect.


`ssl.certificate_authorities`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) List of paths to PEM encoded certificate files that should be trusted.

    This setting and `ssl.truststore.path` cannot be used at the same time.

    You cannot use this setting and `ssl.truststore.path` at the same time.


`ssl.keystore.path`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) The path for the keystore file that contains a private key and certificate.

    It must be either a Java keystore (jks) or a PKCS#12 file. You cannot use this setting and `ssl.key` at the same time.

    You cannot use this setting and `ssl.key` at the same time.


`ssl.keystore.type`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) The format of the keystore file. It must be either `jks` or `PKCS12`. If the keystore path ends in ".p12", ".pfx", or ".pkcs12", this setting defaults to `PKCS12`. Otherwise, it defaults to `jks`.

`ssl.keystore.password`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) The password for the keystore.

    :::{admonition} Deprecated in 7.17.0
    Prefer `ssl.keystore.secure_password` instead.
    :::

`ssl.keystore.secure_password`
:   ([Secure](docs-content://deploy-manage/security/secure-settings.md)) The password for the keystore.

`ssl.keystore.key_password`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) The password for the key in the keystore. The default is the keystore password.

    :::{admonition} Deprecated in 7.17.0
    Prefer `ssl.keystore.secure_key_password` instead.
    :::

    You cannot use this setting and `ssl.keystore.secure_password` at the same time.


`ssl.keystore.secure_key_password`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) The password for the key in the keystore. The default is the keystore password.

`ssl.truststore.path`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) The path for the keystore that contains the certificates to trust. It must be either a Java keystore (jks) or a PKCS#12 file.

    You cannot use this setting and `ssl.certificate_authorities` at the same time.

    You cannot use this setting and `ssl.certificate_authorities` at the same time.


`ssl.truststore.password`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) The password for the truststore.

    :::{admonition} Deprecated in 7.17.0
    Prefer `ssl.truststore.secure_password` instead.
    :::

    You cannot use this setting and `ssl.truststore.secure_password` at the same time.


`ssl.truststore.secure_password`
:   ([Secure](docs-content://deploy-manage/security/secure-settings.md)) Password for the truststore.

`ssl.truststore.type`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) The format of the truststore file. It must be either `jks` or `PKCS12`. If the file name ends in ".p12", ".pfx" or "pkcs12", the default is `PKCS12`. Otherwise, it defaults to `jks`.

`ssl.verification_mode`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) Indicates the type of verification when using `ldaps` to protect against man in the middle attacks and certificate forgery.

    Defaults to `full`.

    **Valid values**:
    * `full`: Validates that the provided certificate: has an issue date that’s within the `not_before` and `not_after` dates; chains to a trusted Certificate Authority (CA); has a `hostname` or IP address that matches the names within the certificate.
    * `certificate`: Validates the provided certificate and verifies that it’s signed by a trusted authority (CA), but doesn’t check the certificate `hostname`.
    * `none`: Performs no certificate validation.

      ::::{important}
      Setting certificate validation to `none` disables many security benefits of SSL/TLS, which is very dangerous. Only set this value if instructed by Elastic Support as a temporary diagnostic mechanism when attempting to resolve TLS errors.
      ::::

`ssl.supported_protocols`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) Supported protocols with versions. Valid protocols: `SSLv2Hello`, `SSLv3`, `TLSv1`, `TLSv1.1`, `TLSv1.2`, `TLSv1.3`. The default is `TLSv1.3,TLSv1.2`.

    Elasticsearch relies on your JDK’s implementation of SSL and TLS. View [Supported SSL/TLS versions by JDK version](docs-content://deploy-manage/security/supported-ssltls-versions-by-jdk-version.md) for more information.

    ::::{note}
    If `xpack.security.fips_mode.enabled` is `true`, you cannot use `SSLv2Hello` or `SSLv3`. See [FIPS 140-2](docs-content://deploy-manage/security/fips-140-2.md).
    ::::


`ssl.cipher_suites`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) Specifies the cipher suites that should be supported when communicating with the LDAP server. Supported cipher suites vary depending on which version of Java you use. For example, for version 12 the default value is `TLS_AES_256_GCM_SHA384`, `TLS_AES_128_GCM_SHA256`, `TLS_CHACHA20_POLY1305_SHA256`, `TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384`, `TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256`, `TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384`, `TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256`, `TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256`, `TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256`, `TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA384`, `TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256`, `TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384`, `TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256`, `TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA`, `TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA`, `TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA`, `TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA`, `TLS_RSA_WITH_AES_256_GCM_SHA384`, `TLS_RSA_WITH_AES_128_GCM_SHA256`, `TLS_RSA_WITH_AES_256_CBC_SHA256`, `TLS_RSA_WITH_AES_128_CBC_SHA256`, `TLS_RSA_WITH_AES_256_CBC_SHA`, `TLS_RSA_WITH_AES_128_CBC_SHA`.

    For more information, see Oracle’s [Java Cryptography Architecture documentation](https://docs.oracle.com/en/java/javase/11/security/java-cryptography-architecture-jca-reference-guide.html).


`cache.ttl`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) Specifies the time-to-live for cached user entries. A user and a hash of its credentials are cached for this period of time. Use the standard Elasticsearch [time units](/reference/elasticsearch/rest-apis/api-conventions.md#time-units). Defaults to  `20m`.

`cache.max_users`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) Specifies the maximum number of user entries that the cache can contain. Defaults to `100000`.

`cache.hash_algo`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting), Expert) Specifies the hashing algorithm that is used for the in-memory cached user credentials. See [Table 1, Cache hash algorithms](#cache-hash-algo). Defaults to `ssha256`.

`authentication.enabled`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) If set to `false`, disables authentication support in this realm, so that it only supports user lookups. (See the [run as](docs-content://deploy-manage/users-roles/cluster-or-deployment-auth/submitting-requests-on-behalf-of-other-users.md) and [authorization realms](docs-content://deploy-manage/users-roles/cluster-or-deployment-auth/realm-chains.md#authorization_realms) features). Defaults to `true`.


#### Active Directory realm settings [ref-ad-settings]

In addition to the [settings that are valid for all realms](#ref-realm-settings), you can specify the following settings:

`url`
