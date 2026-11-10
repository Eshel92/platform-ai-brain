<!-- Converted from api/session-management/invalidate.asciidoc (AsciiDoc). Includes are inlined. -->

### Invalidate user sessions API

experimental[] Invalidates user sessions that match provided query.

#### Prerequisite

To use the invalidate user sessions API, you must be a `superuser`.

#### Request

`POST <kibana host>:<port>/api/security/session/_invalidate`

#### Request body

`match`::
(Required, string) Specifies how Kibana determines which sessions to invalidate. Can either be `all` to invalidate all existing sessions, or `query` to only invalidate sessions that match the query specified in the additional `query` parameter.

`query`::
(Optional, object) Specifies the query that Kibana uses to match the sessions to invalidate when the `match` parameter is set to `query`. You cannot use this parameter if `match` is set to `all`.
**Properties of `query`**
=====
`provider` :::
(Required, object) Describes the authentication providers for which to invalidate sessions.

`type` ::::
(Required, string) The authentication provider `type`.

`name` ::::
(Optional, string) The authentication provider `name`.

`username` :::
(Optional, string) The username for which to invalidate sessions.
=====

#### Response body

`total`::
(number) The number of successfully invalidated sessions.

#### Response codes

`200`::
  Indicates a successful call.

`403`::
  Indicates that the user may not be authorized to invalidate sessions for other users. Refer to prerequisites.

#### Examples

Invalidate all existing sessions:

```sh
$ curl -X POST api/security/session/_invalidate
{
  "match" : "all"
}
```

Invalidate sessions that were created by any SAML authentication provider:

```sh
$ curl -X POST api/security/session/_invalidate
{
  "match" : "query",
  "query": {
    "provider" : { "type": "saml" }
  }
}
```

Invalidate sessions that were created by the SAML authentication provider with the name `saml1`:

```sh
$ curl -X POST api/security/session/_invalidate
{
  "match" : "query",
  "query": {
    "provider" : { "type": "saml", "name": "saml1" }
  }
}
```

Invalidate sessions that were created by any OpenID Connect authentication provider for the user with the username `user@my-oidc-sso.com`:

```sh
$ curl -X POST api/security/session/_invalidate
{
  "match" : "query",
  "query": {
    "provider" : { "type": "oidc" },
    "username": "user@my-oidc-sso.com"
  }
}
```
