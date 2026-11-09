<!-- Converted from reference/api/database-get-by-name.txt (reStructuredText). Includes are inlined. -->

# Get a Database by Name

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

## Resource

```http
GET /groups/{PROJECT-ID}/hosts/{HOST-ID}/databases/{DATABASE-NAME}
```

Retrieve a single database by name.

### Request Path Parameters

| Parameter | Type | Description |
|---|---|---|
| PROJECT-ID | string | *(Required.)* Unique identifier of the project that owns this MongoDB process. |
| HOST-ID | string | *(Required.)* Unique identifier of the host running the MongoDB process. |
| DATABASE-NAME | string | *(Required.)* The name of the MongoDB database. |

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
| `databaseName` | string | The name of the database. |
| `links` | array | Links to the group that the database belongs to, the MongoDB host running the database, and database measurements. The relations between URLs are explained in the [Web Linking Specification](https://tools.ietf.org/html/rfc5988). |

## Example Request

```sh
curl --user "{PUBLIC-KEY}:{PRIVATE-KEY}" --digest \
--header "Accept: application/json" \
--include \
--request GET "https://<ops-manager-host>/api/public/v1.0/groups/644d5895b911306f21034b/hosts/gd5b59198ec14bd142494/databases/test"
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
  "databaseName" : "test",
  "links" : []
}
```
