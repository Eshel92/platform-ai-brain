<!-- Converted from security/authentication/overview.asciidoc (AsciiDoc). Includes are inlined. -->

## User authentication

Authentication identifies an individual. To gain access to restricted resources,
a user must prove their identity, via passwords, credentials, or some other
means (typically referred to as authentication tokens).

The Elastic Stack authenticates users by identifying the users behind the requests
that hit the cluster and verifying that they are who they claim to be. The
authentication process is handled by one or more authentication services called
_realms_.

You can use the native support for managing and authenticating users, or
integrate with external user management systems such as LDAP and Active
Directory.

The {stack-security-features} provide built-in realms such as `native`,`ldap`,
`active_directory`, `pki`, `file`, `saml`, `kerberos`, `oidc`, and `jwt`. If
none of the built-in realms meet your needs, you can also build your own
custom realm and plug it into the Elastic Stack.

When security features are enabled, depending on the realms you've configured,
you must attach your user credentials to the requests sent to Elasticsearch. For example,
when using realms that support usernames and passwords you can simply attach
[basic auth](https://en.wikipedia.org/wiki/Basic_access_authentication) header to the requests.

The security features provide two services: the token service and the API key
service. You can use these services to exchange the current authentication for
a token or key. This token or key can then be used as credentials for authenticating
new requests.
The API key service is enabled by default.
The token service is enabled by default when TLS/SSL is enabled for HTTP.

include::built-in-users.asciidoc[][]
(See `security/authentication/service-accounts.md`)
(See `security/authentication/internal-users.md`)
(See `security/authentication/token-authentication-services.md`)
(See `security/authentication/user-profile.md`)
(See `security/authentication/realms.md`)
(See `security/authentication/realm-chains.md`)
(See `security/authentication/security-domain.md`)
(See `security/authentication/active-directory-realm.md`)
(See `security/authentication/file-realm.md`)
(See `security/authentication/ldap-realm.md`)
(See `security/authentication/native-realm.md`)
(See `security/authentication/oidc-realm.md`)
(See `security/authentication/pki-realm.md`)
(See `security/authentication/saml-realm.md`)
(See `security/authentication/kerberos-realm.md`)
(See `security/authentication/jwt-realm.md`)
(See `security/authentication/custom-realm.md`)
(See `security/authentication/anonymous-access.md`)
(See `security/authentication/user-lookup.md`)
(See `security/authentication/user-cache.md`)
(See `security/authentication/saml-guide.md`)
(See `security/authentication/oidc-guide.md`)
