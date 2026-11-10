<!-- Converted from rest-api/security/saml-prepare-authentication-api.asciidoc (AsciiDoc). Includes are inlined. -->

### SAML prepare authentication API

**New API reference**
For the most up-to-date API details, refer to [Security APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-security).

Creates a SAML authentication request (`<AuthnRequest>`) as a URL string, based on the configuration of the respective SAML realm in Elasticsearch.

**Note:** This API is intended for use by custom web applications other than Kibana.
If you are using Kibana, see the saml-guide-stack.

#### Request

`POST /_security/saml/prepare`

#### Description

This API returns a URL pointing to the SAML Identity
Provider. You can use the URL to redirect the browser of the user in order to
continue the authentication process. The URL includes a single parameter named `SAMLRequest`,
which contains a SAML Authentication request that is deflated and
Base64 encoded. If the configuration dictates that SAML authentication requests
should be signed, the URL has two extra parameters named `SigAlg` and
`Signature`. These parameters contain the algorithm used for the signature and
the signature value itself.
It also returns a random string that uniquely identifies this SAML Authentication request. The
caller of this API needs to store this identifier as it needs to used in a following step of
the authentication process (see SAML authenticate API).

Elasticsearch exposes all the necessary SAML related functionality via the SAML APIs.
These APIs are used internally by Kibana in order to provide SAML based
authentication, but can also be used by other custom web applications or other
clients. See also SAML authenticate API,
SAML invalidate API,
SAML logout API, and
SAML complete logout API.

#### Request body

`acs`::
  (Optional, string) The Assertion Consumer Service URL that matches the one of the SAML
  realms in Elasticsearch. The realm is used to generate the authentication request.
  You must specify either this parameter or the `realm` parameter.

`realm`::
  (Optional, string) The name of the SAML realm in Elasticsearch for which the configuration is
  used to generate the authentication request. You must specify either this parameter or the `acs`
  parameter.

`relay_state`::
  (Optional, string) A string that will be included in the redirect URL that this API returns
  as the `RelayState` query parameter. If the Authentication Request is signed, this value is
  used as part of the signature computation.

#### Response body

`id`::
  (string) A unique identifier for the SAML Request to be stored by the caller
  of the API.

`realm`::
  (string) The name of the Elasticsearch realm that was used to construct the
  authentication request.

`redirect`::
  (string) The URL to redirect the user to.

#### Examples

The following example generates a SAML authentication request for the SAML realm with name `saml1`

```console
POST /_security/saml/prepare
{
  "realm" : "saml1"
}
```

The following example generates a SAML authentication request for the SAML realm with an Assertion
Consuming Service URL matching `https://kibana.org/api/security/saml/callback

```console
POST /_security/saml/prepare
{
  "acs" : "https://kibana.org/api/security/saml/callback"
}
```

This API returns the following response:

```js
{
  "redirect": "https://my-idp.org/login?SAMLRequest=fVJdc6IwFP0rmbwDgUKLGbFDtc462%2B06FX3Yl50rBJsKCZsbrPbXL6J22hdfk%2FNx7zl3eL%2BvK7ITBqVWCfVdRolQuS6k2iR0mU2dmN6Phgh1FTQ8be2rehH%2FWoGWdESF%2FPST0NYorgElcgW1QG5zvkh%2FPfHAZbwx2upcV5SkiMLYzmqsFba1MAthdjIXy5enhL5a23DPOyo6W7kGBa7cwhZ2gO7G8OiW%2BR400kORt0bag7fzezAlk24eqcD2OxxlsNN5O3MdsW9c6CZnbq7rntF4d3s0D7BaHTZhIWN52P%2BcjiuGRbDU6cdj%2BEjJbJLQv4N4ADdhxBiEZbQuWclY4Q8iABbCXczCdSiKMAC%2FgyO2YqbQgrIJDZg%2FcFjsMD%2Fzb3gUcBa5sR%2F9oWR%2BzuJBqlPG14Jbn0DIf2TZ3Jn%2FXmSUrC5ddQB6bob37uZrJdeF4dIDHV3iuhb70Ptq83kOz53ubDLXlcwPJK0q%2FT42AqxIaAkVCkqm2tRgr49yfJGFU%2FZQ3hy3QyuUpd7obPv97kb%2FAQ%3D%3D"}",
  "realm": "saml1",
  "id": "_989a34500a4f5bf0f00d195aa04a7804b4ed42a1"
}
```
