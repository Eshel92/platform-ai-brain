<!-- Converted from reference/api/organizations/organization-get-one.txt (reStructuredText). Includes are inlined. -->

# Get One Organization

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

## Resource

```http
GET /orgs/{ORG-ID}
```

### Request Path Parameters

| Path Element | Type | Description |
|---|---|---|
| ORG-ID | string | *(Required.)* The unique identifier for the organization whose information you want to retrieve. |

### Request Query Parameters

The following query parameters are optional:

* - Name
  - Type
  - Description
  - Default

* - `pretty`
  - boolean
  - Flag indicating whether the response body should be in a
    prettyprint format.
  - `false`

* - `envelope`
  - boolean
  - Flag indicating whether or not to wrap the response in an
    envelope.

    Some API clients cannot access the HTTP response headers or
    status code. To remediate this, set `envelope=true` in the
    query.

    For endpoints that return one result, the response body
    includes:

    | Name | Description |
    |---|---|
    | `status` | HTTP (Hypertext Transfer Protocol) response code |
    | `envelope` | Expected response body |

  - `false`

* - `includeDeletedOrgs`
  - boolean
  - Flag indicating whether the response body contains deleted
    organizations.

    Ops Manager honors the value of this parameter only if the user who
    makes the request has a global role. 

    If set to `true` or omitted, users assigned a global
    role receive deleted projects in the response.
    If set to `false` or if the user does not have a global owner
    role, the response does not contain deleted organizations.
  - `true`

### Request Body Parameters

This endpoint doesn't use HTTP request body parameters.

## Response

| Name | Type | Description |
|---|---|---|
| id | string | Unique identifier for the organization. |
| isDeleted | boolean | Flag indicating if the organization is deleted. |
| name | string | Name of the organization. |
| links | object array | .. include:: /includes/api/links-explanation.rst |

## Example Request

```sh
curl --user '{PUBLIC-KEY}:{PRIVATE-KEY}' --digest \ 
 --header 'Accept: application/json' \ 
 --include \ 
 --request GET "https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0/orgs/{ORG-ID}/"
```

### Example Response

#### Response Header

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

#### Response Body

```json
{
   "id" : "{ORG-ID}",
   "isDeleted": false,
   "links": [{

   }],
   "name" : "Customer Application Support"
}
```
