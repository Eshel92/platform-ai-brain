<!-- Converted from reference/api/admin/backup/oplog/s3Configs/delete-one-s3-oplog-configuration.txt (reStructuredText). Includes are inlined. -->

# Delete One S3-Compatible Oplog Configuration

Deletes the configuration of one S3-compatible oplog store.

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0/admin/backup`

## Resource

```http
DELETE /oplog/s3Configs/{S3-OPLOG-CONFIG-ID}
```

### Request Path Parameters

| Name | Type | Description |
|---|---|---|
| S3-OPLOG-CONFIG-ID | string | The unique identifier that represents this S3 Oplog configuration. |

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

This endpoint does not have response elements.

## Example Request

```sh
curl --user '{USERNAME}:{APIKEY}' --digest \ 
 --include \ 
 --request DELETE 'https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0/admin/backup/oplog/s3Configs/{S3-OPLOG-CONFIG-ID}' 
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

This endpoint doesn't return a response body.
