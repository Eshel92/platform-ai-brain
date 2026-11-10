<!-- Converted from rest-api/security/oidc-logout-api.asciidoc (AsciiDoc). Includes are inlined. -->

### OpenID Connect logout API

**New API reference**
For the most up-to-date API details, refer to [Security APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-security).

Submits a request to invalidate a refresh token and an access token that was
generated as a response to a call to `/_security/oidc/authenticate`.

#### Request

`POST /_security/oidc/logout`

#### Description

If the OpenID Connect authentication realm in Elasticsearch is accordingly configured,
the response to this call will contain a URI pointing to the End Session
Endpoint of the OpenID Connect Provider in order to perform Single Logout.

Elasticsearch exposes all the necessary OpenID Connect related functionality via the
OpenID Connect APIs. These APIs are used internally by Kibana in order to provide
OpenID Connect based authentication, but can also be used by other, custom web
applications or other clients. See also
OpenID Connect authenticate API
and
OpenID Connect prepare authentication API.

#### Request body

`access_token`::
  (Required, string) The value of the access token to be invalidated as part of the logout.

`refresh_token`::
  (Optional, string) The value of the refresh token to be invalidated as part of the logout.

#### Examples

The following example performs logout

```console
POST /_security/oidc/logout
{
  "token" : "dGhpcyBpcyBub3QgYSByZWFsIHRva2VuIGJ1dCBpdCBpcyBvbmx5IHRlc3QgZGF0YS4gZG8gbm90IHRyeSB0byByZWFkIHRva2VuIQ==",
  "refresh_token": "vLBPvmAB6KvwvJZr27cS"
}
```

The following example output of the response contains the URI pointing to the
End Session Endpoint of the OpenID Connect Provider with all the parameters of
the Logout Request, as HTTP GET parameters:

```js
{
  "redirect" : "https://op-provider.org/logout?id_token_hint=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c&post_logout_redirect_uri=http%3A%2F%2Foidc-kibana.elastic.co%2Floggedout&state=lGYK0EcSLjqH6pkT5EVZjC6eIW5YCGgywj2sxROO"
}
```
