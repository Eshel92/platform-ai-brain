<!-- Converted from user/security/index.asciidoc (AsciiDoc). Includes are inlined. -->

## Security

The Elastic Stack security features enable you to easily secure a cluster. With
security, you can
password-protect your data as well as implement more advanced security measures
such as encrypting communications, role-based access control, IP filtering, and
auditing. For more information, see
[Secure a cluster](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/secure-cluster.html) and
Configuring Security in Kibana.

**Note:** There are security limitations that affect Kibana. For more information, refer to [Security](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/security-limitations.html).

### Required permissions

The `manage_security` cluster privilege is required to access all Security features.

### Users

To create and manage users, go to the *Users* management page using the navigation menu or the 
global search field.
You can also change their passwords and roles. For more information about
authentication and built-in users, see
[Setting up user authentication](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/setting-up-authentication.html).

### Roles

To manage roles, go to the *Roles* management page using the navigation menu or the 
global search field, or use
the [role APIs](https://www.elastic.co/docs/api/doc/kibana/group/endpoint-roles). For more information on configuring roles for Kibana, see Granting access to Kibana.

For a more holistic overview of configuring roles for the entire stack,
see [User authorization](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/authorization.html).

============================================================================
Managing roles that grant kibana-privileges using the Elasticsearch
[role management APIs](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/security-api.html#security-role-apis) is not supported. Doing so will likely
cause Kibana's authorization to behave unexpectedly.
============================================================================

(See `user/security/authorization/index.md`)
(See `user/security/authorization/kibana-privileges.md`)
(See `user/security/api-keys/index.md`)
(See `user/security/role-mappings/index.md`)
(See `user/security/fips-140-2.md`)
