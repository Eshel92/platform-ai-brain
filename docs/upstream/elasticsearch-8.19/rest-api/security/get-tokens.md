<!-- Converted from rest-api/security/get-tokens.asciidoc (AsciiDoc). Includes are inlined. -->

### Get token API

**New API reference**
For the most up-to-date API details, refer to [Security APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-security).

Creates a bearer token for access without requiring basic authentication.

#### Request

`POST /_security/oauth2/token`

#### Prerequisites

* To use this API, you must have the `manage_token` cluster privilege.

#### Description

The tokens are created by the Elasticsearch Token Service, which is automatically enabled
when you configure TLS on the HTTP interface. See encrypt-http-communication. Alternatively,
you can explicitly enable the `xpack.security.authc.token.enabled` setting. When
you are running in production mode, a bootstrap check prevents you from enabling
the token service unless you also enable TLS on the HTTP interface.

The get token API takes the same parameters as a typical OAuth 2.0 token API
except for the use of a JSON request body.

A successful get token API call returns a JSON structure that contains the access
token, the amount of time (seconds) that the token expires in, the type, and the
scope if available.

The tokens returned by the get token API have a finite period of time for which
they are valid and after that time period, they can no longer be used. That time
period is defined by the `xpack.security.authc.token.timeout` setting. For more
information, see token-service-settings.

If you want to invalidate a token immediately, you can do so by using the
invalidate token API.

#### Request body

The following parameters can be specified in the body of a POST request and
pertain to creating a token:

`grant_type`::
(Required, string) The type of grant.
Supported grant types are: `password`, `_kerberos`,
`client_credentials` and `refresh_token`.

`client_credentials`:::
This grant type implements the Client Credentials Grant of OAuth2. It is geared
for machine to machine communication and is not suitable or designed for the
self-service user creation of tokens. It generates only access tokens that
cannot be refreshed. The premise is that the entity that uses
`client_credentials` has constant access to a set of (client, not end-user)
credentials and can authenticate itself at will.

`_kerberos`:::
This grant type is supported internally and implements SPNEGO based Kerberos
support. The `_kerberos` grant type may change from version to version.

`password`:::
This grant type implements the Resource Owner Password Credentials Grant of
OAuth2. In this grant, a trusted client exchanges the end user's credentials
for an access token and (possibly) a refresh token. The request needs to be made
by an authenticated user but happens _on behalf_ of another authenticated user
(the one whose credentials are passed as request parameters). This grant type is
not suitable or designed for the self-service user creation of tokens.

`refresh_token`:::
This grant type implements the Refresh Token Grant of OAuth2.
In this grant a user exchanges a previously issued refresh token for a new access token and a new refresh token.

`password`::
(Optional^*^, string) The user's password. If you specify the `password` grant type, this
parameter is required. This parameter is not valid with any other supported
grant type.

`kerberos_ticket`::
(Optional^*^, string) The base64 encoded kerberos ticket. If you specify the
`_kerberos` grant type, this parameter is required. This parameter is not valid
with any other supported grant type.

`refresh_token`::
(Optional^*^, string) The string that was returned when you created the token,
which enables you to extend its life. If you specify the `refresh_token` grant
type, this parameter is required. This parameter is not valid with any other
supported grant type.

`scope`::
(Optional, string) The scope of the token. Currently tokens are only issued for a scope of
`FULL` regardless of the value sent with the request.

`username`::
(Optional^*^, string) The username that identifies the user. If you specify the `password`
grant type, this parameter is required. This parameter is not valid with any
other supported grant type.

#### Examples

The following example obtains a token using the `client_credentials` grant type,
which simply creates a token as the authenticated user:

```console
POST /_security/oauth2/token
{
  "grant_type" : "client_credentials"
}
```

The following example output contains the access token, the amount of time (in
seconds) that the token expires in, and the type:

```console-result
{
  "access_token" : "dGhpcyBpcyBub3QgYSByZWFsIHRva2VuIGJ1dCBpdCBpcyBvbmx5IHRlc3QgZGF0YS4gZG8gbm90IHRyeSB0byByZWFkIHRva2VuIQ==",
  "type" : "Bearer",
  "expires_in" : 1200,
  "authentication" : {
    "username" : "test_admin",
    "roles" : [
      "superuser"
    ],
    "full_name" : null,
    "email" : null,
    "metadata" : { },
    "enabled" : true,
    "authentication_realm" : {
      "name" : "file",
      "type" : "file"
    },
    "lookup_realm" : {
      "name" : "file",
      "type" : "file"
    },
    "authentication_type" : "realm"
  }
}
```

The token returned by this API can be used by sending a request with an
`Authorization` header with a value having the prefix "Bearer " followed
by the value of the `access_token`.

```shell
curl -H "Authorization: Bearer dGhpcyBpcyBub3QgYSByZWFsIHRva2VuIGJ1dCBpdCBpcyBvbmx5IHRlc3QgZGF0YS4gZG8gbm90IHRyeSB0byByZWFkIHRva2VuIQ==" http://localhost:9200/_cluster/health
```

The following example obtains a token for the `test_admin` user using the
`password` grant type. This request needs to be made by an authenticated user with sufficient privileges that may
or may not be the same as the one whose username is passed in the `username` parameter:

```console
POST /_security/oauth2/token
{
  "grant_type" : "password",
  "username" : "test_admin",
  "password" : "x-pack-test-password"
}
```

The following example output contains the access token, the amount of time (in
seconds) that the token expires in, the type, and the refresh token:

```console-result
{
  "access_token" : "dGhpcyBpcyBub3QgYSByZWFsIHRva2VuIGJ1dCBpdCBpcyBvbmx5IHRlc3QgZGF0YS4gZG8gbm90IHRyeSB0byByZWFkIHRva2VuIQ==",
  "type" : "Bearer",
  "expires_in" : 1200,
  "refresh_token": "vLBPvmAB6KvwvJZr27cS",
  "authentication" : {
    "username" : "test_admin",
    "roles" : [
      "superuser"
    ],
    "full_name" : null,
    "email" : null,
    "metadata" : { },
    "enabled" : true,
    "authentication_realm" : {
      "name" : "file",
      "type" : "file"
    },
    "lookup_realm" : {
      "name" : "file",
      "type" : "file"
    },
    "authentication_type" : "realm"
  }
}
```

To extend the life of an existing token obtained using the `password` grant type,
you can call the API again with the refresh token within 24 hours of the token's
creation. For example:

```console
POST /_security/oauth2/token
{
  "grant_type": "refresh_token",
  "refresh_token": "vLBPvmAB6KvwvJZr27cS"
}
```

The API will return a new token and refresh token. Each refresh token may only
be used one time.

```console-result
{
  "access_token" : "dGhpcyBpcyBub3QgYSByZWFsIHRva2VuIGJ1dCBpdCBpcyBvbmx5IHRlc3QgZGF0YS4gZG8gbm90IHRyeSB0byByZWFkIHRva2VuIQ==",
  "type" : "Bearer",
  "expires_in" : 1200,
  "refresh_token": "vLBPvmAB6KvwvJZr27cS",
  "authentication" : {
    "username" : "test_admin",
    "roles" : [
      "superuser"
    ],
    "full_name" : null,
    "email" : null,
    "metadata" : { },
    "enabled" : true,
    "authentication_realm" : {
      "name" : "file",
      "type" : "file"
    },
    "lookup_realm" : {
      "name" : "file",
      "type" : "file"
    },
    "authentication_type" : "token"
  }
}
```

The following example obtains a access token and refresh token using the `kerberos` grant type,
which simply creates a token in exchange for the base64 encoded kerberos ticket:

```js
POST /_security/oauth2/token
{
  "grant_type" : "_kerberos",
  "kerberos_ticket" : "YIIB6wYJKoZIhvcSAQICAQBuggHaMIIB1qADAgEFoQMCAQ6iBtaDcp4cdMODwOsIvmvdX//sye8NDJZ8Gstabor3MOGryBWyaJ1VxI4WBVZaSn1WnzE06Xy2"
}
```

The API will return a new token and refresh token if kerberos authentication is successful.
Each refresh token may only be used one time. When the mutual authentication is requested in the Spnego GSS context,
 a base64 encoded token will be returned by the server in the `kerberos_authentication_response_token`
 for clients to consume and finalize the authentication.

```js
{
  "access_token" : "dGhpcyBpcyBub3QgYSByZWFsIHRva2VuIGJ1dCBpdCBpcyBvbmx5IHRlc3QgZGF0YS4gZG8gbm90IHRyeSB0byByZWFkIHRva2VuIQ==",
  "type" : "Bearer",
  "expires_in" : 1200,
  "refresh_token": "vLBPvmAB6KvwvJZr27cS"
  "kerberos_authentication_response_token": "YIIB6wYJKoZIhvcSAQICAQBuggHaMIIB1qADAg",
  "authentication" : {
    "username" : "test_admin",
    "roles" : [
      "superuser"
    ],
    "full_name" : null,
    "email" : null,
    "metadata" : { },
    "enabled" : true,
    "authentication_realm" : {
      "name" : "file",
      "type" : "file"
    },
    "lookup_realm" : {
      "name" : "file",
      "type" : "file"
    },
    "authentication_type" : "realm"
  }
}
```
