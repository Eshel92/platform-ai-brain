<!-- Converted from security/authentication/user-lookup.asciidoc (AsciiDoc). Includes are inlined. -->

### Looking up users without authentication

Elasticsearch realms exist primarily to support
user authentication. 
Some realms authenticate users with a password (such as the
`native` and `ldap` realms), and other realms use
more complex authentication protocols (such as the `saml` and
`oidc` realms).
In each case, the _primary_ purpose of the realm is to establish the identity of
the user who has made a request to the Elasticsearch API.

However, some Elasticsearch features need to _look up_ a user without using their credentials.

- The `run_as` feature executes requests on behalf of
  another user. An authenticated user with `run_as` privileges can perform
  requests on behalf of another unauthenticated user.

- The delegated authorization feature links two realms
  together so that a user who authenticates against one realm can have the roles
  and metadata associated with a user from a different realm.

In each of these cases, a user must first authenticate to one realm and then
Elasticsearch will query the second realm to find another user.
The authenticated user credentials are used to authenticate in the first realm only,
The user in the second realm is retrieved by username, without needing credentials.

When Elasticsearch resolves a user using their credentials (as performed in the first realm),
it is known as _user authentication_.

When Elasticsearch resolves a user using the username only (as performed in the second realm),
it is known as _user lookup_.

See the run_as and delegated authorization
documentation to learn more about these features, including which realms and authentication
methods support `run_as` or delegated authorization. 
In both cases, only the following realms can be used for the user lookup:

* The reserved, `native` and `file` realms always 
support user lookup.
* The `ldap` realm supports user lookup when the realm is configured
in _user search_ mode. User lookup is not support
when the realm is configured with `user_dn_templates`.
* User lookup support in the `active_directory` realm
requires that the realm be configured with a `bind_dn` and a
bind password.

The `pki`, `saml`, `oidc`, `kerberos` and `jwt` realms do not support user
lookup.

**Note:** If you want to use a realm only for user lookup and prevent users from 
authenticating against that realm, you can configure the realm
and set `authentication.enabled` to `false`

The user lookup feature is an internal capability that is used to implement the
`run-as` and delegated authorization features - there are no APIs for user lookup.
If you wish to test your user lookup configuration, then you can do this with
`run_as`. Use the security-api-authenticate API, authenticate as a
`superuser` (e.g. the builtin `elastic` user) and specify the
`es-security-runas-user` request header.

**Note:** The security-api-get-user API and user-profile feature are alternative
      ways to retrieve information about a Elastic Stack user. Those APIs are not related
      to the user lookup feature.
