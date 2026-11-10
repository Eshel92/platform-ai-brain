<!-- Converted from security/authentication/ldap-realm.asciidoc (AsciiDoc). Includes are inlined. -->

### LDAP user authentication

You can configure the Elastic Stack security features to communicate with a
Lightweight Directory Access Protocol (LDAP) server to authenticate users. See
ldap-realm-configuration.

LDAP stores users and groups hierarchically, similar to the way folders are
grouped in a file system. An LDAP directory's hierarchy is built from containers
such as the _organizational unit_ (`ou`), _organization_ (`o`), and
_domain component_ (`dc`).

The path to an entry is a _Distinguished Name_ (DN) that uniquely identifies a
user or group. User and group names typically have attributes such as a
_common name_ (`cn`) or _unique ID_ (`uid`). A DN is specified as a string,
for example  `"cn=admin,dc=example,dc=com"` (white spaces are ignored).

The `ldap` realm supports two modes of operation, a user search mode
and a mode with specific templates for user DNs.

#### Mapping LDAP groups to roles

An integral part of a realm authentication process is to resolve the roles
associated with the authenticated user. Roles define the privileges a user has
in the cluster.

Since with the `ldap` realm the users are managed externally in the LDAP server,
the expectation is that their roles are managed there as well. In fact, LDAP
supports the notion of groups, which often represent user roles for different
systems in the organization.

The `ldap` realm enables you to map LDAP users to roles via their LDAP
groups or other metadata. This role mapping can be configured via the
add role mapping API or by using a
file stored on each node. When a user authenticates with LDAP, the privileges
for that user are the union of all privileges defined by the roles to which
the user is mapped.

#### Configuring an LDAP realm

To integrate with LDAP, you configure an `ldap` realm and map LDAP groups to
user roles.

. Determine which mode you want to use. The `ldap` realm supports two modes of 
operation, a user search mode and a mode with specific templates for user DNs. 
LDAP user search is the most common mode of operation. In this mode, a specific
user with permission to search the LDAP directory is used to search for the DN 
of the authenticating user based on the provided username and an LDAP attribute. 
Once found, the user is authenticated by attempting to bind to the LDAP server 
using the found DN and the provided password.

If your LDAP environment uses a few specific standard naming conditions for
users, you can use user DN templates to configure the realm. The advantage of
this method is that a search does not have to be performed to find the user DN.
However, multiple bind operations might be needed to find the correct user DN.

. To configure an `ldap` realm with user search:

.. Add a realm configuration to `elasticsearch.yml` under the
`xpack.security.authc.realms.ldap` namespace. At a minimum, you must specify
the `url` and `order` of the LDAP server, and set `user_search.base_dn` to the
container DN where the users are searched for.
See ref-ldap-settings for all of the options you can set for 
an `ldap` realm.
For example, the following snippet shows an LDAP realm configured with a user search:

```yaml
xpack:
  security:
    authc:
      realms:
        ldap:
          ldap1:
            order: 0
            url: "ldaps://ldap.example.com:636"
            bind_dn: "cn=ldapuser, ou=users, o=services, dc=example, dc=com"
            user_search:
              base_dn: "dc=example,dc=com"
              filter: "(cn={0})"
            group_search:
              base_dn: "dc=example,dc=com"
            files:
              role_mapping: "ES_PATH_CONF/role_mapping.yml"
            unmapped_groups_as_roles: false
```

The password for the `bind_dn` user should be configured by adding the appropriate
`secure_bind_password` setting to the Elasticsearch keystore.
For example, the following command adds the password for the example realm above:

```shell
bin/elasticsearch-keystore add \
xpack.security.authc.realms.ldap.ldap1.secure_bind_password
```

**Important:** When you configure realms in `elasticsearch.yml`, only the
realms you specify are used for authentication. If you also want to use the
`native` or `file` realms, you must include them in the realm chain.

. To configure an `ldap` realm with user DN templates:

.. Add a realm configuration to `elasticsearch.yml` in the
`xpack.security.authc.realms.ldap` namespace. At a minimum, you must specify
the `url` and `order` of the LDAP server, and specify at least one template
with the `user_dn_templates` option.
See ref-ldap-settings for all of the options you can set for an `ldap` realm.
For example, the following snippet shows an LDAP realm configured with user DN 
templates:

```yaml
xpack:
  security:
    authc:
      realms:
        ldap:
          ldap1:
            order: 0
            url: "ldaps://ldap.example.com:636"
            user_dn_templates:
              - "cn={0}, ou=users, o=marketing, dc=example, dc=com"
              - "cn={0}, ou=users, o=engineering, dc=example, dc=com"
            group_search:
              base_dn: "dc=example,dc=com"
            files:
              role_mapping: "/mnt/elasticsearch/group_to_role_mapping.yml"
            unmapped_groups_as_roles: false
```

**Important:** The `bind_dn` setting is not used in template mode.
All LDAP operations run as the authenticating user.

. (Optional) Configure how the security features interact with multiple LDAP
servers. 
The `load_balance.type` setting can be used at the realm level. The Elasticsearch
security features support both failover and load balancing modes of operation.
See ref-ldap-settings.

. (Optional) To protect passwords, 
encrypt communications between Elasticsearch and the LDAP server. 

. Restart Elasticsearch. 

. Map LDAP groups to roles. 
The `ldap` realm enables you to map LDAP users to roles via their LDAP
groups, or other metadata. This role mapping can be configured via the
add role mapping API or by using a file stored
on each node. When a user authenticates with LDAP, the privileges
for that user are the union of all privileges defined by the roles to which
the user is mapped.

Within a mapping definition, you specify groups using their distinguished
names. For example, the following mapping configuration maps the LDAP
`admins` group to both the `monitoring` and `user` roles, and maps the
`users` group to the `user` role.

Configured via the role-mapping API:

```console
PUT /_security/role_mapping/admins
{
  "roles" : [ "monitoring" , "user" ],
  "rules" : { "field" : {
    "groups" : "cn=admins,dc=example,dc=com" <1>
  } },
  "enabled": true
}
```

<1> The LDAP distinguished name (DN) of the `admins` group.

```console
PUT /_security/role_mapping/basic_users
{
  "roles" : [ "user" ],
  "rules" : { "field" : {
    "groups" : "cn=users,dc=example,dc=com" <1>
  } },
  "enabled": true
}
```

<1> The LDAP distinguished name (DN) of the `users` group.

Or, alternatively, configured via the role-mapping file:
```yaml
monitoring: <1>
  - "cn=admins,dc=example,dc=com" <2>
user:
  - "cn=users,dc=example,dc=com" <3>
  - "cn=admins,dc=example,dc=com"
```
<1> The name of the mapped role.
<2> The LDAP distinguished name (DN) of the `admins` group.
<3> The LDAP distinguished name (DN) of the `users` group.

For more information, see 
mapping-roles-ldap and mapping-roles.

**Note:** The LDAP realm supports
authorization realms as an
alternative to role mapping.

. (Optional) Configure the `metadata` setting on the LDAP realm to include extra 
fields in the user's metadata. 
By default, `ldap_dn` and `ldap_groups` are populated in the user's metadata. 
For more information, see 
ldap-user-metadata. 

The example below includes the user's common name (`cn`) as an additional
field in their metadata.
```yaml
xpack:
  security:
    authc:
      realms:
        ldap:
          ldap1:
            order: 0
            metadata: cn
```

. Set up SSL to encrypt communications between Elasticsearch and LDAP. See tls-ldap. 

#### User metadata in LDAP realms

When a user is authenticated via an LDAP realm, the following properties are
populated in the user's _metadata_:

|=======================
| Field               | Description
| `ldap_dn`           | The distinguished name of the user.
| `ldap_groups`       | The distinguished name of each of the groups that were
                        resolved for the user (regardless of whether those
                        groups were mapped to a role).
|=======================

This metadata is returned in the
authenticate API, and can be used with
templated queries in roles.

Additional fields can be included in the user's metadata by configuring
the `metadata` setting on the LDAP realm. This metadata is available for use
with the role mapping API or in
templated role queries.

#### Load balancing and failover

The `load_balance.type` setting can be used at the realm level to configure how
the security features should interact with multiple LDAP servers. The
security features support both failover and load balancing modes of operation.

See load-balancing.

(See `security/authentication/../securing-communications/tls-ldap.md`)
