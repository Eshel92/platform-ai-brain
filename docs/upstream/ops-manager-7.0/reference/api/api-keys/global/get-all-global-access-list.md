<!-- Converted from reference/api/api-keys/global/get-all-global-access-list.txt (reStructuredText). Includes are inlined. -->

# Get All Access List Entries for a Global API Key

Return all Global Access List Entries for Ops Manager.

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

## Resource

```http
GET /admin/accessList
```

## Required Roles

Requires that the API (Application Programming Interface) Key calling this endpoint have the
`Global Owner` role.

Requires that the API (Application Programming Interface) Key calling this endpoint have the
`Global Read Only` role.

## Request Parameters

### Request Path Parameters

This endpoint doesn't use HTTP request path parameters.

### Request Query Parameters

The following query parameters are optional:

| Name | Type | Necessity | Description | Default |
|---|---|---|---|---|
| pageNum | number | Optional | One-based integer that returns a subsection of results. | `1` |
| itemsPerPage | number | Optional | Number of items to return per page, up to a maximum of 500. | `100` |
| pretty | boolean | Optional | Flag that indicates whether the response body should be in a prettyprint format. | `false` |
| envelope | boolean | Optional | Flag that indicates whether or not to wrap the response in an envelope. Some API (Application Programming Interface) clients cannot access the HTTP (Hypertext Transfer Protocol) response headers or status code. To remediate this, set `envelope : true` in the query. For endpoints that return a list of results, the `results` object is an envelope. Ops Manager adds the `status` field to the response body. | `false` |
| backupJobsEnabledOnly | boolean | Optional | Flag indicating whether to exclude daemons not enabled for backing up databases from the response. Set this to `false` to include daemon configurations with the `backupJobsEnabled` flag set to `false`. | `true` |

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

Each **result** is one Global Access List Entry.

| Name | Type | Description |
|---|---|---|
| `cidrBlock` | string | Range of IP addresses in an access list in IPv4 (Internet Protocol version 4) or IPv6 (Internet Protocol version 6) CIDR (Classless Inter-Domain Routing) notation. |
| `created` | string | Timestamp, in the number of seconds that have elapsed since the [UNIX epoch](https://en.wikipedia.org/wiki/Unix_time?oldid=828172017) when you added this CIDR (Classless Inter-Domain Routing) block to the Global Access List. |
| `description` | string | Explanation of the purpose of this Global Access List Entry. |
| `id` | string | Unique identifier for this Global Access List Entry. |
| `type` | string | Scope of the Global Access List Entry. |
| `updated` | string | Timestamp, in the number of seconds that have elapsed since the [UNIX epoch](https://en.wikipedia.org/wiki/Unix_time?oldid=828172017) when you last changed the CIDR (Classless Inter-Domain Routing) block of this Global Access List Entry. |

## Example Request

```sh
curl --user "{PUBLIC-KEY}:{PRIVATE-KEY}" --digest \
  --header "Accept: application/json" \
  --header "Content-Type: application/json" \
  --request GET "https://<OpsManagerHost>:<Port>/api/public/v1.0/admin/accessList?pretty=true"
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
  "results" : [ {
    "cidrBlock" : "251.207.34.78/32",
    "created" : "2019-09-05T04:02:46Z",
    "description" : "Test Global Access List Entry 1",
    "id" : "5d4d7b9cf20ce440466a30bd",
    "type" : "GLOBAL_ROLE",
    "updated" : "2019-09-05T04:02:46Z"
  }, {
    "cidrBlock" : "2001:db8::/48",
    "created" : "2019-09-05T04:02:46Z",
    "description" : "Test Global Access List Entry 2",
    "id" : "5d6fe33787d9d6689b3427ec",
    "type" : "GLOBAL_ROLE",
    "updated" : "2019-09-05T04:02:46Z"
  } ]
  "totalCount" : 2
}
```
