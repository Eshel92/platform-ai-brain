<!-- Converted from reference/api/agents/get-agent-versions-global.txt (reStructuredText). Includes are inlined. -->

# Retrieve All Agent Versions

## Required Roles

You can successfully call this endpoint with any of the following
assigned roles:

- `Global Owner`
- `Global Monitoring Admin`

## Request

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

```http
GET /softwareComponents/versions/
```

### Request Path Parameters

This endpoint doesn't use HTTP request path parameters.

### Request Query Parameters

* - Name
  - Type
  - Necessity
  - Description
  - Default

* - pretty
  - boolean
  - Optional
  - Flag indicating whether the response body should be in a
    prettyprint format.
  - `false`

* - envelope
  - boolean
  - Optional
  - Flag that indicates whether or not to wrap the response in an
    envelope.

    Some API (Application Programming Interface) clients cannot access the HTTP (Hypertext Transfer Protocol) response headers or
    status code. To remediate this, set **envelope=true** in the
    query.

    For endpoints that return one result, the response body
    includes:

    | Name | Description |
    |---|---|
    | status | HTTP (Hypertext Transfer Protocol) response code |
    | envelope | Expected response body |

  - `false`

### Request Body Parameters

This endpoint doesn't use HTTP request body parameters.

## Response

| Name | Type | Description |
|---|---|---|
| `automationVersion` | string | Latest version of the MongoDB Agent. |
| `automationMinimumVersion` | string | Minimum supported version of the MongoDB Agent. |
| `biConnectorVersion` | string | Latest version of the `BI Connector`. |
| `biConnectorMinimumVersion` | string | Minimum supported version of the `BI Connector`. |
| `mongoDbToolsVersion` | string | Latest version of MongoDB Tools installed. |
| `links` | array of objects | .. include:: /includes/api/links-explanation.rst |

## Example Request

```sh
curl --user '{PUBLIC-KEY}:{PRIVATE-KEY}' --digest \
     --request GET "http://{opsManagerHost}:{port}/api/public/v1.0/softwareComponents/versions?pretty=true"
```

## Example Response

### Response Header

```http
HTTP/1.1 401 Unauthorized
Content-Type: application/json;charset=ISO-8859-1
Date: {dateInUnixFormat}
WWW-Authenticate: Digest realm="MMS Public API", domain="", nonce="{nonce}", algorithm=MD5, op="auth", stale=false
Content-Length: {requestLengthInBytes}
Connection: keep-alive
```

```http
HTTP/1.1 200 OK
Vary: Accept-Encoding
Content-Type: application/json
Strict-Transport-Security: max-age=300
Date: {dateInUnixFormat}
Connection: keep-alive
Content-Length: {requestLengthInBytes}
X-MongoDB-Service-Version: gitHash={gitHash}; versionString={ApplicationVersion}
```

### Response Body

```json
{
  "automationVersion": "10.14.0.6304",
  "automationMinimumVersion": "10.2.17.5964",
  "biConnectorVersion": "2.3.4",
  "biConnectorMinimumVersion": "2.3.1",
  "mongoDbToolsVersion": "100.0.1",
  "links": [
    {
      "href": "http://{opsManagerHost}:{port}/api/public/v1.0/agents/current",
      "rel": "self"
    }
  ]
}
```
