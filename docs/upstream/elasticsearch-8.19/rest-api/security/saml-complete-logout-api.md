<!-- Converted from rest-api/security/saml-complete-logout-api.asciidoc (AsciiDoc). Includes are inlined. -->

### SAML complete logout API

**New API reference**
For the most up-to-date API details, refer to [Security APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-security).

Verifies the logout response sent from the SAML IdP.

**Note:** This API is intended for use by custom web applications other than Kibana.
If you are using Kibana, see the saml-guide-stack.

#### Request

`POST /_security/saml/complete_logout`

#### Description

The SAML IdP may send a logout response back to the SP after handling
the SP-initiated SAML Single Logout.
This API verifies the response by ensuring the content is relevant
and validating its signature. An empty response is returned if
the verification process is successful.
The response can be sent by the IdP with either the HTTP-Redirect or
the HTTP-Post binding. The caller of this API must prepare the request
accordingly so that this API can handle either of them.

Elasticsearch exposes all the necessary SAML related functionality via the SAML APIs.
These APIs are used internally by Kibana in order to provide SAML based
authentication, but can also be used by other custom web applications or other
clients. See also SAML authenticate API,
SAML prepare authentication API,
SAML invalidate API, and
SAML logout API.

#### Request body

`realm`::
  (Required, string) The name of the SAML realm in Elasticsearch for which the configuration is
  used to verify the logout response.

`ids`::
  (Required, array) A json array with all the valid SAML Request Ids that the caller of
  the API has for the current user.

`query_string`::
  (Optional, string) If the SAML IdP sends the logout response with the HTTP-Redirect
  binding, this field must be set to the query string of the redirect URI.

`queryString`::
deprecated:[7.14.0, "Use query_string instead"]
  See `query_string`

`content`::
  (Optional, string) If the SAML IdP sends the logout response with the HTTP-Post
  binding, this field must be set to the value of the `SAMLResponse` form parameter
  from the logout response.

#### Examples

The following example verifies the logout response sent by the SAML IdP
using the HTTP-Redirect binding:

```console
POST /_security/saml/complete_logout
{
  "realm": "saml1",
  "ids": [ "_1c368075e0b3..." ],
  "query_string": "SAMLResponse=fZHLasMwEEVbfb1bf...&SigAlg=http%3A%2F%2Fwww.w3.org%2F2000%2F09%2Fxmldsig%23rsa-sha1&Signature=CuCmFn%2BLqnaZGZJqK..."
}
```

If the logout response is sent with the HTTP-Post binding, it can be verified
as the follows:

```console
POST /_security/saml/complete_logout
{
  "realm": "saml1",
  "ids": [ "_1c368075e0b3..." ],
  "content": "PHNhbWxwOkxvZ291dFJlc3BvbnNlIHhtbG5zOnNhbWxwPSJ1cm46..."
}
```

The API returns an empty response on success.
