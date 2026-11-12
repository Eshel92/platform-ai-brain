<!-- Part 1 of 7 of settings/security-settings.md (split because the page is big). -->

### Security settings in Elasticsearch

You configure `xpack.security` settings to
enable anonymous access and perform message
authentication,
set up document and field level security,
configure realms,
encrypt communications with SSL,and
audit security events.

All of these settings can be added to the `elasticsearch.yml` configuration file,
with the exception of the secure settings, which you add to the Elasticsearch keystore.
For more information about creating and updating the Elasticsearch keystore, see
secure-settings.


#### General security settings

`xpack.security.enabled`::
(Static)
Defaults to `true`, which enables Elasticsearch security features on the node.
This setting must be enabled to use Elasticsearch's authentication,
authorization and audit features. +
If set to `false`, security features are disabled, which is not recommended.
It also affects all Kibana instances that connect to this Elasticsearch instance; you do
not need to disable security features in those `kibana.yml` files. For more
information about disabling security features in specific Kibana instances, see
[Kibana security settings](https://www.elastic.co/guide/en/kibana/8.19/security-settings-kb.html).

`xpack.security.autoconfiguration.enabled`::
(Static)
Defaults to `true`, which enables
security auto configuration.
If set to `false`, security auto configuration is disabled, which is not
recommended. When disabled, security is not configured automatically when
starting Elasticsearch for the first time, which means that you must
manually configure security.

`xpack.security.enrollment.enabled`::
(Static)
Defaults to `false`. Controls enrollment (of nodes and Kibana) to a local node
that's been autoconfigured for security.
When set to `true`, the local node can generate new enrollment tokens. Existing
tokens can be used for enrollment if they are still valid.
The security autoconfiguration process will set this to `true` unless
an administrator sets it to `false` before starting Elasticsearch.

`xpack.security.hide_settings`::
(Static)
A comma-separated list of settings that are omitted from the results of the
cluster nodes info API. You can use wildcards to include
multiple settings in the list. For example, the following value hides all the
settings for the ad1 active_directory realm:
`xpack.security.authc.realms.active_directory.ad1.*`.
The API already omits all `ssl` settings, `bind_dn`, and `bind_password` due to
the sensitive nature of the information.

`xpack.security.fips_mode.enabled`::
(Static)
Enables fips mode of operation. Set this to `true` if you run this Elasticsearch instance in a FIPS 140-2 enabled JVM. For more information, see fips-140-compliance. Defaults to `false`.

`xpack.security.fips_mode.required_providers`::
(Static)
Optionally enforce specific Java JCE/JSSE security providers. For example, set this to `["BCFIPS", "BCJSSE"]` (case-insensitive) to require
the Bouncy Castle FIPS JCE and JSSE security providers. Only applicable when `xpack.security.fips_mode.enabled` is set to `true`.


#### Password hashing settings

`xpack.security.authc.password_hashing.algorithm`::
(Static)
Specifies the hashing algorithm that is used for secure user credential storage.
See password-hashing-algorithms.
If `xpack.security.fips_mode.enabled` is true (see fips-140-compliance), defaults to `pbkdf2_stretch`.
In all other cases, defaults to `bcrypt`.


#### Anonymous access settings

You can configure the following anonymous access settings in
`elasticsearch.yml`. For more information, see anonymous-access.

`xpack.security.authc.anonymous.username`::
(Static)
The username (principal) of the anonymous user. Defaults to `_es_anonymous_user`.

`xpack.security.authc.anonymous.roles`::
(Static)
The roles to associate with the anonymous user. Required.

`xpack.security.authc.anonymous.authz_exception`::
(Static)
When `true`, an HTTP 403 response is returned if the anonymous user
does not have the appropriate permissions for the requested action. The
user is not prompted to provide credentials to access the requested
resource. When set to `false`, an HTTP 401 response is returned and the user
can provide credentials with the appropriate permissions to gain
access. Defaults to `true`.


#### Automata Settings

In places where the security features accept wildcard patterns (e.g. index
patterns in roles, group matches in the role mapping API), each pattern is
compiled into an Automaton. The follow settings are available to control this
behaviour.

`xpack.security.automata.max_determinized_states`::
(Static)
The upper limit on how many automaton states may be created by a single pattern.
This protects against too-difficult (e.g. exponentially hard) patterns.
Defaults to `100,000`.

`xpack.security.automata.cache.enabled`::
(Static)
Whether to cache the compiled automata. Compiling automata can be CPU intensive
and may slowdown some operations. The cache reduces the frequency with which
automata need to be compiled.
Defaults to `true`.

`xpack.security.automata.cache.size`::
(Static)
The maximum number of items to retain in the automata cache.
Defaults to `10,000`.

`xpack.security.automata.cache.ttl`::
(Static)
The length of time to retain in an item in the automata cache (based on most
recent usage).
Defaults to `48h` (48 hours).


#### Document and field level security settings

You can set the following document and field level security
settings in `elasticsearch.yml`. For more information, see
field-and-document-access-control.

`xpack.security.dls_fls.enabled`::
(Static)
Set to `false` to prevent document and field level security
from being configured. Defaults to `true`.

`xpack.security.dls.bitset.cache.ttl`::
(Static)
The time-to-live for cached `BitSet` entries for document level security.
Document level security queries may depend on Lucene BitSet objects, and these are
automatically cached to improve performance. Defaults to expire entries that are
unused for `2h` (2 hours).

`xpack.security.dls.bitset.cache.size`::
(Static)
The maximum memory usage of cached `BitSet` entries for document level security.
Document level security queries may depend on Lucene BitSet objects, and these are
automatically cached to improve performance. Can be configured as a raw number
of bytes (such as `200mb` or `1g`) or a percentage of the node's JVM heap
memory (such as `5%`). When the default value is exceeded, the least recently
used entries are evicted. Defaults to `10%` of the heap assigned to the node.


#### Token service settings

You can set the following token service settings in
`elasticsearch.yml`.

`xpack.security.authc.token.enabled`::
(Static)
Set to `false` to disable the built-in token service. Defaults to `true` unless
 `xpack.security.http.ssl.enabled` is `false`. This prevents sniffing the token
  from a connection over plain http.

`xpack.security.authc.token.timeout`::
(Static)
The length of time that a token is valid for. By default this value is `20m` or
20 minutes. The maximum value is 1 hour.


#### API key service settings

You can set the following API key service settings in
`elasticsearch.yml`.

`xpack.security.authc.api_key.enabled`::
(Static)
Set to `false` to disable the built-in API key service. Defaults to `true`.

`xpack.security.authc.api_key.cache.ttl`::
(Static)
The time-to-live for cached API key entries. A API key id and a hash of its
API key are cached for this period of time. Specify the time period using
the standard Elasticsearch time units. Defaults to `1d`.

`xpack.security.authc.api_key.cache.max_keys`::
(Static)
The maximum number of API key entries that can live in the
cache at any given time. Defaults to 10,000.

`xpack.security.authc.api_key.cache.hash_algo`::
(Static, Expert)
The hashing algorithm that is used for the
in-memory cached API key credentials. For possible values, see cache-hash-algo.
Defaults to `ssha256`.

`xpack.security.authc.api_key.delete.retention_period`::
(Dynamic)
Invalidated or expired API keys older than the retention period are eligible for deletion.
Defaults to `7d`.

**Note:** Large real-time clock inconsistency across cluster nodes can cause problems
with evaluating the API key retention period. That is, if the clock on the node
invalidating the API key is significantly different than the one performing the deletion,
the key may be retained for longer or shorter than the configured retention period.

`xpack.security.authc.api_key.delete.interval`::
(Dynamic, Expert)
Cluster nodes schedule the automatic deletion of invalidated or expired API keys
that are older than the retention period.
This setting controls the minimum time interval between two such deletion jobs.
Defaults to `24h`.
**Note:** This is a low-level setting that currently controls the interval between
deletion jobs triggered per-node, not across the cluster.

`xpack.security.authc.api_key.delete.timeout`::
(Static, Expert)
Sets the timeout of the internal search and delete call.

`xpack.security.authc.api_key.hashing.algorithm`::
(Static)
Specifies the hashing algorithm that is used for securing API key credentials.
See secure-token-hashing-algorithms. Defaults to `ssha256`.


#### Security domain settings

You configure security domain settings in the `xpack.security.authc.domains`
namespace in `elasticsearch.yml`.

For example:

```yaml
xpack:
  security:
    authc:
      domains:
        my_domain: <1>
          realms: [ 'default_native', 'saml1' ] <2>
```
<1> Specifies the name of the security domain
<2> Specifies the realms that belong to the domain


#### Realm settings

You configure realm settings in the `xpack.security.authc.realms`
namespace in `elasticsearch.yml`.

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
<1> Specifies the type of realm (for example, `native`, `ldap`,
`active_directory`, `pki`, `file`, `kerberos`, `saml`) and the realm name. This
information is required.
<2> Specifies priority of a realm in the realm chain. This information
is required.

The valid settings vary depending on the realm type. For more
information, see setting-up-authentication.


##### Settings valid for all realms

`order`::
(Static)
The priority of the realm within the realm chain. Realms with a lower order are
consulted first. The value must be unique for each realm. This setting is required.

`enabled`::
(Static)
Indicates whether a realm is enabled. You can use this setting to disable a
realm without removing its configuration information. Defaults to `true`.


##### Native realm settings

In addition to the settings that are valid for all realms,
you can specify the following optional settings:

`cache.ttl`::
(Static)
The time-to-live for cached user entries. A user and a hash of its
credentials are cached for this period of time. Specify the time period using
the standard Elasticsearch time units. Defaults to `20m`.

`cache.max_users`::
(Static)
The maximum number of user entries that can live in the
cache at any given time. Defaults to 100,000.

`cache.hash_algo`::
(Static, Expert)
The hashing algorithm that is used for the
in-memory cached user credentials. For possible values, see cache-hash-algo.
Defaults to `ssha256`.

`authentication.enabled`::
(Static)
If set to `false`, disables authentication support in
this realm, so that it only supports user lookups.
(See the run as and
authorization realms features).
Defaults to `true`.


##### File realm settings

In addition to the settings that are valid for all realms, you can specify
the following settings:

`cache.ttl`::
(Static)
The time-to-live for cached user entries. A user and a hash of its credentials
are cached for this configured period of time. Defaults to `20m`. Specify values
using the standard Elasticsearch time units.
Defaults to `20m`.

`cache.max_users`::
(Static)
The maximum number of user entries that can live in the cache at a given time.
Defaults to 100,000.

`cache.hash_algo`::
(Static, Expert)
The hashing algorithm that is used for the in-memory cached
user credentials. See cache-hash-algo. Defaults to `ssha256`.

`authentication.enabled`::
(Static)
If set to `false`, disables authentication support in
this realm, so that it only supports user lookups.
(See the run as and
authorization realms features).
Defaults to `true`.
