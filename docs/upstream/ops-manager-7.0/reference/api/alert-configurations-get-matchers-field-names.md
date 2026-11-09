<!-- Converted from reference/api/alert-configurations-get-matchers-field-names.txt (reStructuredText). Includes are inlined. -->

# Get All Alert Configuration Matchers Field Names

**Note:**

Groups and projects are synonymous terms. Your `{PROJECT-ID}` is the
same as your project id. For existing groups, your group/project id
remains the same. This page uses the more familiar term group when
referring to descriptions. The endpoint remains as stated in the
document.

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

Get all field names that the `matchers.fieldName` parameter accepts 
when you create 
or update 
an Alert Configuration.

## Required Roles

You can successfully call this endpoint with any assigned role.

## Request

```none
GET /alertConfigs/matchers/fieldNames
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

The response returns an array of strings that the `matchers.fieldName`
parameter accepts when you create or 
update 
an Alert Configuration.

## Example Request

```sh
curl --user '{PUBLIC-KEY}:{PRIVATE-KEY}' --digest \
  --header 'Accept: application/json' \
  --include \
  --request GET "https://<ops-manager-host>/api/public/v1.0/alertConfigs/matchers/fieldNames"
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
[
    "TYPE_NAME",
    "HOSTNAME",
    "PORT",
    "HOSTNAME_AND_PORT",
    "REPLICA_SET_NAME",
    "SHARD_NAME",
    "CLUSTER_NAME"
]
```
