<!-- Converted from rest-api/security.asciidoc (AsciiDoc). Includes are inlined. -->

## Security APIs

**New API reference**
For the most up-to-date API details, refer to [Security APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-security).

To use the security APIs, you must set `xpack.security.enabled` to `true` in
the `elasticsearch.yml` file.

Use the following APIs to perform security activities.

* security-api-authenticate
* security-api-clear-cache
* security-api-delegate-pki-authentication
* security-api-has-privileges
* security-api-ssl
* security-api-get-builtin-privileges
* security-api-get-settings
* security-api-update-settings
* security-api-get-user-privileges

### Application privileges

Use the following APIs to add, update, retrieve, and remove application
privileges:

* Create or update privileges
* Clear privileges cache
* Delete privileges
* Get privileges

### Role mappings

Use the following APIs to add, remove, update, and retrieve role mappings:

* Create or update role mappings
* Delete role mappings
* Get role mappings

### Roles

Use the following APIs to add, remove, update, and retrieve roles in the native realm:

* Create or update roles
* Bulk create or update roles
* Clear roles cache
* Delete roles
* Bulk delete roles
* Get roles
* Query roles

### Tokens

Use the following APIs to create and invalidate bearer tokens for access
without requiring basic authentication:

* Get token
* Invalidate token

### API Keys

Use the following APIs to create and update API keys for access via the REST interface
without requiring basic authentication:

* Create REST API key
* Grant REST API key
* Update REST API key
* Bulk update REST API keys

Use the following APIs to create and update cross-cluster API keys for
API key based remote cluster access:

* Create Cross-Cluster API key
* Update Cross-Cluster API key

Use the following APIs to retrieve and invalidate API keys of all types:

* Get API key
* Invalidate API key
* Query API key
* Clear API key cache

### Users

Use the following APIs to add, remove, update, or retrieve users in the
native realm:

* Create or update users
* Change passwords
* Delete users
* Disable users
* Enable users
* Get users
* Query users

### Service Accounts

Use the following APIs to list service accounts and manage the service tokens:

* security-api-get-service-accounts
* security-api-create-service-token
* security-api-delete-service-token
* security-api-get-service-credentials

### OpenID Connect

Use the following APIs to authenticate users against an OpenID Connect
authentication realm when using a custom web application other than Kibana

* Prepare an authentication request
* Submit an authentication response
* Logout an authenticated user

### SAML

Use the following APIs to authenticate users against a SAML authentication
realm when using a custom web application other than Kibana

* Prepare an authentication request
* Submit an authentication response
* Logout an authenticated user
* Submit a logout request from the IdP
* Verify a logout response from the IdP
* Generate SAML metadata

### Enrollment

Use the following APIs to enable new nodes to join an existing cluster with
security enabled, or to enable a Kibana instance to configure itself to
communicate with a secured Elasticsearch cluster.

* Enroll a new node
* Enroll a new Kibana instance

### User Profile

Use the following APIs to retrieve and manage user profiles.

* Activate user profile
* Get user profile
* Update user profile data
* Enable user profile
* Disable user profile
* Suggest user profile
* Has Privileges user profile

(See `rest-api/security/authenticate.md`)
(See `rest-api/security/change-password.md`)
(See `rest-api/security/clear-cache.md`)
(See `rest-api/security/clear-roles-cache.md`)
(See `rest-api/security/clear-privileges-cache.md`)
(See `rest-api/security/clear-api-key-cache.md`)
(See `rest-api/security/clear-service-token-caches.md`)
(See `rest-api/security/create-api-keys.md`)
(See `rest-api/security/put-app-privileges.md`)
(See `rest-api/security/create-role-mappings.md`)
(See `rest-api/security/create-roles.md`)
(See `rest-api/security/bulk-create-roles.md`)
(See `rest-api/security/bulk-delete-roles.md`)
(See `rest-api/security/create-users.md`)
(See `rest-api/security/create-service-token.md`)
(See `rest-api/security/delegate-pki-authentication.md`)
(See `rest-api/security/delete-app-privileges.md`)
(See `rest-api/security/delete-role-mappings.md`)
(See `rest-api/security/delete-roles.md`)
(See `rest-api/security/delete-service-token.md`)
(See `rest-api/security/delete-users.md`)
(See `rest-api/security/disable-users.md`)
(See `rest-api/security/enable-users.md`)
(See `rest-api/security/enroll-kibana.md`)
(See `rest-api/security/enroll-node.md`)
(See `rest-api/security/get-api-keys.md`)
(See `rest-api/security/get-app-privileges.md`)
(See `rest-api/security/get-builtin-privileges.md`)
(See `rest-api/security/get-role-mappings.md`)
(See `rest-api/security/get-roles.md`)
(See `rest-api/security/query-role.md`)
(See `rest-api/security/get-service-accounts.md`)
(See `rest-api/security/get-service-credentials.md`)
(See `rest-api/security/get-settings.md`)
(See `rest-api/security/get-tokens.md`)
(See `rest-api/security/get-user-privileges.md`)
(See `rest-api/security/get-users.md`)
(See `rest-api/security/grant-api-keys.md`)
(See `rest-api/security/has-privileges.md`)
(See `rest-api/security/invalidate-api-keys.md`)
(See `rest-api/security/invalidate-tokens.md`)
(See `rest-api/security/oidc-prepare-authentication-api.md`)
(See `rest-api/security/oidc-authenticate-api.md`)
(See `rest-api/security/oidc-logout-api.md`)
(See `rest-api/security/query-api-key.md`)
(See `rest-api/security/query-user.md`)
(See `rest-api/security/update-api-key.md`)
(See `rest-api/security/update-settings.md`)
(See `rest-api/security/bulk-update-api-keys.md`)
(See `rest-api/security/saml-prepare-authentication-api.md`)
(See `rest-api/security/saml-authenticate-api.md`)
(See `rest-api/security/saml-logout-api.md`)
(See `rest-api/security/saml-invalidate-api.md`)
(See `rest-api/security/saml-complete-logout-api.md`)
(See `rest-api/security/saml-sp-metadata.md`)
(See `rest-api/security/ssl.md`)
(See `rest-api/security/activate-user-profile.md`)
(See `rest-api/security/disable-user-profile.md`)
(See `rest-api/security/enable-user-profile.md`)
(See `rest-api/security/get-user-profile.md`)
(See `rest-api/security/suggest-user-profile.md`)
(See `rest-api/security/update-user-profile-data.md`)
(See `rest-api/security/has-privileges-user-profile.md`)
(See `rest-api/security/create-cross-cluster-api-key.md`)
(See `rest-api/security/update-cross-cluster-api-key.md`)
