<!-- Converted from reference/api/organizations/organization-get-all.txt (reStructuredText). Includes are inlined. -->

# Get All Organizations

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

## Resource

```http
GET /orgs
```

## Request Parameters

### Request Path Parameters

This endpoint doesn't use HTTP request path parameters.

### Request Query Parameters

The following query parameters are optional:

| Name | Type | Description | Default |
|---|---|---|---|
| `pageNum` | integer | Page number (1-based). | `1` |
| `itemsPerPage` | integer | Number of items to return per page, up to a maximum of 500. | `100` |
| `pretty` | boolean | Displays response in a [prettyprint](https://en.wikipedia.org/wiki/Prettyprint?oldid=791126873) format. | `false` |
| `envelope` | boolean | Specifies whether or not to wrap the response in an envelope. | `false` |
| `name` | string | Filters results based on the specified organization name. Performs a case-insensitive search for organizations which exactly match the specified `name`. For example, if you specify a `name` query parameter of `org1`, Ops Manager returns organizations named `org1` and `Org1`, but would not return an organization named `org123`. | None |
| `includeDeletedOrgs` | boolean | Flag indicating whether the response body contains deleted organizations. Ops Manager honors the value of this parameter only if the user who makes the request has a global role. If set to `true` or omitted, users assigned a global role receive deleted projects in the response. If set to `false` or if the user does not have a global owner role, the response does not contain deleted organizations. | `true` |

### Request Body Parameters

This endpoint doesn't use HTTP request body parameters.

## Response

### Response Document

The response JSON (Javascript Object Notation) document includes an array of result
objects, an array of link objects and a count of the total
number of result objects retrieved.

| Name | Type | Description |
|---|---|---|
| `results` | array | Array includes one object for each item detailed in the results-embedded-document-get-all section. |
| `links` | array | Array includes one or more links to sub-resources and/or related resources. The relations between URL (Uniform Resource Locator)\s are explained in the Web Linking Specification. |
| `totalCount` | number | Integer count of the total number of items in the result set. It may be greater than the number of objects in the results array if the entire result set is paginated. |

### `results` Embedded Document

Each **result** is one organization.

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
 --request GET "https://{OPSMANAGER-HOST}/api/public/v1.0/orgs/"
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
  "links" : [{
    "href" : "https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0/orgs",
    "rel" : "self"
  }],
  "results" : [{
    "id" : "5a2add1cfd9f3cfb17053317",
    "isDeleted": false,
    "links": [{
      "href": "https://cloud.mongodb.com/api/public/v1.0/orgs/5a2add1cfd9f3cfb17053317",
      "rel": "self"
  }],
  "name" : "Internal Application Support"
   }, 
   {
     "id" : "5a2add1cfd9f3cfb17053318",
     "isDeleted": false,
     "links": [{
       "href": "https://cloud.mongodb.com/api/public/v1.0/orgs/5a2add1cfd9f3cfb17053318",
       "rel": "self"
     }],
     "name" : "Customer Application Support"
     }, 
     {
       "id" : "5a2add1cfd9f3cfb17053319",
       "isDeleted": false,
       "links": [{
         "href": "https://cloud.mongodb.com/api/public/v1.0/orgs/5a2add1cfd9f3cfb17053319",
         "rel": "self"
       }],
       "name" : "Research and Development"
     } 
  ],
  "totalCount" : 3
}
```
