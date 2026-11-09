<!-- Converted from reference/api/usage/create-one-report.txt (reStructuredText). Includes are inlined. -->

# Get One Global Usage Report Archive

Retrieve a compressed report, in **zip** or **.tar.gz** format, of
server usage in a given timeframe.

## Required Roles

Your API Key must have the `Global Owner` role to
successfully call this resource.

## Request

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

```http
GET /usage/report
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

|  |  |  |  |  |
|---|---|---|---|---|
| startDate | string | Required | Date in ISO 8601 date format when the report starts. |  |
| endDate | string | Required | Date in ISO 8601 date format when the report ends. |  |
| fileFormat | String | Required | Compression format of the resulting report. Ops Manager accepts **zip** or **.tar.gz**. |  |
| redact | Boolean | Optional | Flag that indicates whether the response should censor all IP addresses, hostnames, organization names, and project names in the report. | **true** |

### Request Body Parameters

This endpoint doesn't use HTTP request body parameters.

## Response

This endpoint returns either a `.zip` or `.tar.gz` compressed file based on your **fileFormat** parameter.

## Example Request

```sh
curl --user "{publicApiKey}:{privateApiKey}" --digest \
     --header "Accept: application/gzip" \
     --include \
     --request GET "https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0/usage/report?startDate=2019-07-27&endDate=2020-07-28&fileFormat=zip"
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

This endpoint returns either a `.zip` or `.tar.gz` compressed file based on your **fileFormat** parameter.
