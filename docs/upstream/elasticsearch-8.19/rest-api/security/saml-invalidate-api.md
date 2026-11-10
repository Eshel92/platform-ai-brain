<!-- Converted from rest-api/security/saml-invalidate-api.asciidoc (AsciiDoc). Includes are inlined. -->

### SAML invalidate API

**New API reference**
For the most up-to-date API details, refer to [Security APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-security).

Submits a SAML LogoutRequest message to Elasticsearch for consumption.

**Note:** This API is intended for use by custom web applications other than Kibana.
If you are using Kibana, see the saml-guide-stack.

#### Request

`POST /_security/saml/invalidate`

#### Description

The logout request comes from the SAML IdP during an IdP initiated Single Logout.
The custom web application can use this API to have Elasticsearch process the `LogoutRequest`.
After successful validation of the request, Elasticsearch invalidates the access token
and refresh token that corresponds to that specific SAML principal and provides
a URL that contains a SAML LogoutResponse message, so that the user can be
redirected back to their IdP.

Elasticsearch exposes all the necessary SAML related functionality via the SAML APIs.
These APIs are used internally by Kibana in order to provide SAML based
authentication, but can also be used by other custom web applications or other
clients. See also SAML authenticate API,
SAML prepare authentication API,
SAML logout API, and
SAML complete logout API.

#### Request body

`acs`::
  (Optional, string) The Assertion Consumer Service URL that matches the one of the SAML
  realm in Elasticsearch that should be used. You must specify either this parameter or the `realm` parameter.

`query_string`::
  (Required, string) The query part of the URL that the user was redirected to by the SAML
  IdP to initiate the Single Logout. This query should include a single
  parameter named `SAMLRequest` that contains a SAML logout request that is
  deflated and Base64 encoded. If the SAML IdP has signed the logout request,
  the URL should include two extra parameters named `SigAlg` and `Signature`
  that contain the algorithm used for the signature and the signature value itself.
In order for Elasticsearch to be able to verify the IdP's signature, the value of the query_string field must be an exact match to the string provided by the browser.
The client application must not attempt to parse or process the string in any way.

`queryString`::
deprecated:[7.14.0, "Use query_string instead"]
  See `query_string`.

`realm`::
  (Optional, string) The name of the SAML realm in Elasticsearch the configuration. You must specify
  either this parameter or the `acs` parameter.

#### Response body

`invalidated`::
  (integer) The number of tokens that were invalidated as part of this logout.

`realm`::
  (string) The realm name of the SAML realm in Elasticsearch that authenticated the user.

`redirect`::
  (string) A SAML logout response as a parameter so that the user can be
  redirected back to the SAML IdP.

#### Examples

The following example invalidates all the tokens for realm `saml1` pertaining to
the user that is identified in the SAML Logout Request:

```console
POST /_security/saml/invalidate
{
  "query_string" : "SAMLRequest=nZFda4MwFIb%2FiuS%2BmviRpqFaClKQdbvo2g12M2KMraCJ9cRR9utnW4Wyi13sMie873MeznJ1aWrnS3VQGR0j4mLkKC1NUeljjA77zYyhVbIE0dR%2By7fmaHq7U%2BdegXWGpAZ%2B%2F4pR32luBFTAtWgUcCv56%2Fp5y30X87Yz1khTIycdgpUW9kY7WdsC9zxoXTvMvWuVV98YyMnSGH2SYE5pwALBIr9QKiwDGpW0oGVUznGeMyJZKFkQ4jBf5HnhUymjIhzCAL3KNFihbYx8TBYzzGaY7EnIyZwHzCWMfiDnbRIftkSjJr%2BFu0e9v%2B0EgOquRiiZjKpiVFp6j50T4WXoyNJ%2FEWC9fdqc1t%2F1%2B2F3aUpjzhPiXpqMz1%2FHSn4A&SigAlg=http%3A%2F%2Fwww.w3.org%2F2001%2F04%2Fxmldsig-more%23rsa-sha256&Signature=MsAYz2NFdovMG2mXf6TSpu5vlQQyEJAg%2B4KCwBqJTmrb3yGXKUtIgvjqf88eCAK32v3eN8vupjPC8LglYmke1ZnjK0%2FKxzkvSjTVA7mMQe2AQdKbkyC038zzRq%2FYHcjFDE%2Bz0qISwSHZY2NyLePmwU7SexEXnIz37jKC6NMEhus%3D",
  "realm" : "saml1"
}
```

```js
{
  "redirect" : "https://my-idp.org/logout/SAMLResponse=....",
  "invalidated" : 2,
  "realm" : "saml1"
}
```
