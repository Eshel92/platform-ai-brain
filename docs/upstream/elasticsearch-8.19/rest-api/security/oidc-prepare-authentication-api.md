<!-- Converted from rest-api/security/oidc-prepare-authentication-api.asciidoc (AsciiDoc). Includes are inlined. -->

### OpenID Connect prepare authentication API

**New API reference**
For the most up-to-date API details, refer to [Security APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-security).

Creates an oAuth 2.0 authentication request as a URL string based on the
configuration of the respective OpenID Connect authentication realm in Elasticsearch.

#### Request

`POST /_security/oidc/prepare`

#### Description

The response of this API is a URL pointing to the Authorization Endpoint of the
configured OpenID Connect Provider and can be used to redirect the browser of
the user in order to continue the authentication process.

Elasticsearch exposes all the necessary OpenID Connect related functionality via the
OpenID Connect APIs. These APIs are used internally by Kibana in order to provide
OpenID Connect based authentication, but can also be used by other, custom web
applications or other clients. See also
OpenID Connect authenticate API
and OpenID Connect logout API.

#### Request body

The following parameters can be specified in the body of the request:

`realm`::
  (Optional, string) The name of the OpenID Connect realm in Elasticsearch the configuration of which should
be used in order to generate the authentication request. Cannot be specified
when `iss` is specified. One of `realm`, `iss` is required.

`state`::
  (Optional, string) Value used to maintain state between the authentication request and the
response, typically used as a Cross-Site Request Forgery mitigation. If the
caller of the API doesn't provide a value, Elasticsearch will generate one with
sufficient entropy itself and return it in the response.

`nonce`::
  (Optional, string) Value used to associate a Client session with an ID Token and to mitigate
replay attacks. If the caller of the API doesn't provide a value, Elasticsearch will
generate one with sufficient entropy itself and return it in the response.

`iss`::
  (Optional, string) In the case of a 3rd Party initiated Single Sign On, this is the Issuer
Identifier for the OP that the RP is to send the Authentication Request to.
Cannot be specified when `realm` is specified. One of `realm`, `iss` is required.

`login_hint`::
  (Optional, string) In the case of a 3rd Party initiated Single Sign On, a string value to be
included in the authentication request, as the `login_hint` parameter. This
parameter is not valid when `realm` is specified

#### Examples

The following example generates an authentication request for the OpenID Connect
Realm `oidc1`:

```console
POST /_security/oidc/prepare
{
  "realm" : "oidc1"
}
```

The following example output of the response contains the URI pointing to the Authorization Endpoint of the OpenID Connect Provider with all the parameters of
the Authentication Request, as HTTP GET parameters:

```console-result
{
  "redirect" : "http://127.0.0.1:8080/c2id-login?scope=openid&response_type=id_token&redirect_uri=https%3A%2F%2Fmy.fantastic.rp%2Fcb&state=4dbrihtIAt3wBTwo6DxK-vdk-sSyDBV8Yf0AjdkdT5I&nonce=WaBPH0KqPVdG5HHdSxPRjfoZbXMCicm5v1OiAj0DUFM&client_id=elasticsearch-rp",
  "state" : "4dbrihtIAt3wBTwo6DxK-vdk-sSyDBV8Yf0AjdkdT5I",
  "nonce" : "WaBPH0KqPVdG5HHdSxPRjfoZbXMCicm5v1OiAj0DUFM",
  "realm" : "oidc1"
}
```

The following example generates an authentication request for the OpenID Connect
Realm `oidc1`, where the values for the state and the nonce have been generated
by the client:

```console
POST /_security/oidc/prepare
{
  "realm" : "oidc1",
  "state" : "lGYK0EcSLjqH6pkT5EVZjC6eIW5YCGgywj2sxROO",
  "nonce" : "zOBXLJGUooRrbLbQk5YCcyC8AXw3iloynvluYhZ5"
}
```

The following example output of the response contains the URI pointing to the Authorization Endpoint of the OpenID Connect Provider with all the parameters of
the Authentication Request, as HTTP GET parameters:

```console-result
{
  "redirect" : "http://127.0.0.1:8080/c2id-login?scope=openid&response_type=id_token&redirect_uri=https%3A%2F%2Fmy.fantastic.rp%2Fcb&state=lGYK0EcSLjqH6pkT5EVZjC6eIW5YCGgywj2sxROO&nonce=zOBXLJGUooRrbLbQk5YCcyC8AXw3iloynvluYhZ5&client_id=elasticsearch-rp",
  "state" : "lGYK0EcSLjqH6pkT5EVZjC6eIW5YCGgywj2sxROO",
  "nonce" : "zOBXLJGUooRrbLbQk5YCcyC8AXw3iloynvluYhZ5",
  "realm" : "oidc1"
}
```

The following example generates an authentication request for a 3rd party
initiated single sign on, specifying the issuer that should be used for matching
the appropriate OpenID Connect Authentication realm:

```console
POST /_security/oidc/prepare
{
  "iss" : "http://127.0.0.1:8080",
  "login_hint": "this_is_an_opaque_string"
}
```

The following example output of the response contains the URI pointing to the Authorization Endpoint of the OpenID Connect Provider with all the parameters of
the Authentication Request, as HTTP GET parameters:

```console-result
{
  "redirect" : "http://127.0.0.1:8080/c2id-login?login_hint=this_is_an_opaque_string&scope=openid&response_type=id_token&redirect_uri=https%3A%2F%2Fmy.fantastic.rp%2Fcb&state=4dbrihtIAt3wBTwo6DxK-vdk-sSyDBV8Yf0AjdkdT5I&nonce=WaBPH0KqPVdG5HHdSxPRjfoZbXMCicm5v1OiAj0DUFM&client_id=elasticsearch-rp",
  "state" : "4dbrihtIAt3wBTwo6DxK-vdk-sSyDBV8Yf0AjdkdT5I",
  "nonce" : "WaBPH0KqPVdG5HHdSxPRjfoZbXMCicm5v1OiAj0DUFM",
  "realm" : "oidc1"
}
```
