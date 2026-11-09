<!-- Converted from reference/api/access-list-add-entries.txt (reStructuredText). Includes are inlined. -->

# Add Entries to an Access List

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

## Resource

```none
POST /users/{USER-ID}/accessList
```

### Request Path Parameters

| Parameter | Type | Description |
|---|---|---|
| USER-ID | string | *(Required.)* Unique identifier of the current user. To retrieve the ID of the current user, see Get All Users in One Project. |

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

The request body must be an array of access list entities, even if there
is only one. The only field that you need to specify for each request
object is the **IP-ADDRESS**.

If an IP address is already in the access list, it will be ignored.

If you specify a single IP address with the `/32` subnet mask, Ops Manager
does not store the `/32`, as the `/32` does not change the address.

**Example:**

An address of `12.34.56.78` is the same as `12.34.56.78/32`.

| Parameter | Type | Description |
|---|---|---|
| ipAddress | string | *(Required.)* The IP address or CIDR (Classless Inter-Domain Routing) block that you want to add to the specified user's access list. |

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

Each **result** is one access list.

| Name | Type | Description |
|---|---|---|
| `cidrBlock` | string | A CIDR-notated range of IP addresses. |
| `created` | date | The date this IP address was added to the access list. |
| `ipAddress` | string | An IP address in the access list. |
| `lastUsed` | date | The date of the most recent request that originated from this IP address. Note that this field is *only* updated when a resource that is protected by the access list is accessed. |
| `lastUsedAddress` | string | The address from which the last call to the API was issued. |
| `count` | number | The total number of requests that originated from this IP address. Note that this field is *only* updated when a resource that is protected by the access list is accessed. |
| `links` | array | Links to related sub-resources. All links arrays in responses contain at least one link called `self`. The relations between URLs are explained in the [Web Linking Specification](https://tools.ietf.org/html/rfc5988). |

## Example Request

```sh
curl --user '{PUBLIC-KEY}:{PRIVATE-KEY}' --digest \
--header 'Accept: application/json' \
--header 'Content-Type: application/json' \
--include \
--request POST "https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0/users/{USER-ID}/accessList" --data '
    [
      {
        "ipAddress" : "192.0.1.15",
        "comment" : "IP address for Application Server A"
      },
      {
        "cidrBlock" : "192.0.2.0/24",
        "comment" : "CIDR block for Application Server B - D"
      }
    ]'
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
HTTP/1.1 201 Created
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
  "totalCount" : 3,
  "results" : [ {
    "cidrBlock" : "12.34.56.78/32",
    "ipAddress" : "12.34.56.78",
    "created" : "2014-04-23T16:17:44Z",
    "lastUsed" : "2016-08-17T19:34:05Z",
    "lastUsedAddress" : "12.34.56.78",
    "count" : 0,
    "links" : []
  }, {
    "cidrBlock" : "76.54.32.10/32",
    "ipAddress" : "76.54.32.10",
    "created" : "2016-08-17T19:34:05Z",
    "count" : 0,
    "links" : []
  }, {
    "cidrBlock" : "2.3.4.5/32",
    "ipAddress" : "2.3.4.5",
    "created" : "2016-08-17T19:34:05Z",
    "count" : 0,
    "links" : []
  } ],
  "links" : []
}
```
