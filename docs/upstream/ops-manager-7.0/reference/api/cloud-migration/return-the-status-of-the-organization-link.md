<!-- Converted from reference/api/cloud-migration/return-the-status-of-the-organization-link.txt (reStructuredText). Includes are inlined. -->

# Return the Status of the Connection between Organizations

Return the status of the connection between the specified source Ops Manager
organization and the target MongoDB Atlas organization.

## Required Roles

Your API Key must have the `Organization Owner` role to
successfully call this resource.

## Request

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

```http
GET /orgs/{orgId}/liveExport/migrationLink/status
```

### Request Path Parameters

| Name | Type | Necessity | Description |
|---|---|---|---|
| orgId | string | Required | Unique 24-hexadecimal digit string that identifies the source organization that contains the projects to be migrated to MongoDB Atlas. |

### Request Query Parameters

The following query parameters are optional:

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
| status | string | State of the connection that exists between this organization and the target cluster in the MongoDB Atlas organization. Response returns `"SYNCED"` or `"NOT_SYNCED"`. |

## Example Request

```sh
curl --user '{USERNAME}:{APIKEY}' --digest \
     --header 'Accept: application/json' \
     --header 'Content-Type: application/json' \
     --include \
     --request GET 'https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0/orgs/{orgId}/liveExport/migrationLink/status?pretty=true'
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
  "status": "SYNCED"
}
```
