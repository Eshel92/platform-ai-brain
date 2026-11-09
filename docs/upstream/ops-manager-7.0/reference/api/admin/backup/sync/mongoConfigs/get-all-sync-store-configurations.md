<!-- Converted from reference/api/admin/backup/sync/mongoConfigs/get-all-sync-store-configurations.txt (reStructuredText). Includes are inlined. -->

# Get All Sync Store Configurations

Retrieves the configurations of all sync stores.

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0/admin/backup`

## Resource

```http
GET /sync/mongoConfigs
```

### Request Path Parameters

This endpoint doesn't use HTTP request path parameters.

### Request Query Parameters

| Name | Type | Necessity | Description | Default |
|---|---|---|---|---|
| pageNum | number | Optional | One-based integer that returns a subsection of results. | `1` |
| itemsPerPage | number | Optional | Number of items to return per page, up to a maximum of 500. | `100` |
| pretty | boolean | Optional | Flag that indicates whether the response body should be in a prettyprint format. | `false` |
| envelope | boolean | Optional | Flag that indicates whether or not to wrap the response in an envelope. Some API (Application Programming Interface) clients cannot access the HTTP (Hypertext Transfer Protocol) response headers or status code. To remediate this, set `envelope : true` in the query. For endpoints that return a list of results, the `results` object is an envelope. Ops Manager adds the `status` field to the response body. | `false` |
| backupJobsEnabledOnly | boolean | Optional | Flag indicating whether to exclude daemons not enabled for backing up databases from the response. Set this to `false` to include daemon configurations with the `backupJobsEnabled` flag set to `false`. | `true` |

|  |  |  |  |
|---|---|---|---|
| assignableOnly | boolean | Flag indicating whether this sync store can be assigned new backup jobs. | `true` |

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

Each **result** is one sync store.

* - Name
  - Type
  - Description

* - assignmentEnabled
  - boolean
  - Flag indicating whether this sync store can be assigned
    backup jobs.

* - encryptedCredentials
  - boolean
  - Flag indicating whether the username and password for this 
    sync store were encrypted using the 
    credentialstool.

* - id
  - string
  - The unique name that labels this sync store.

* - labels
  - array of strings
  - Array of tags to manage which 
    backup jobs Ops Manager can assign to which 
    `sync stores`. 

* - links
  - object array
  - .. include:: /includes/api/links-explanation.rst

* - maxCapacityGB
  - number
  - .. include:: /includes/api/maxCapacityGB-description.rst

* - uri
  - string
  - A comma-separated list of hosts in the `<hostname:port>`
    format that can be used to access this sync store.

* - ssl
  - boolean
  - Flag indicating whether this sync store only accepts 
    connections encrypted using 
    TLS (Transport Layer Security).

* - usedSize
  - number
  - The amount of backup capacity in MB (megabytes) that
    the existing backups consume.

* - writeConcern
  - string
  - The write concern used for this sync store.

    The accepted values for this option are:

    - `ACKNOWLEDGED`
    - `W2`
    - `JOURNALED`
    - `MAJORITY`

    To learn about write acknowledgement levels in MongoDB, see 
    Write Concern.

## Example Request

```sh
curl --user '{PUBLIC-KEY}:{PRIVATE-KEY}' --digest \ 
 --header 'Accept: application/json' \ 
 --include \ 
 --request GET 'https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0/admin/backup/sync/mongoConfigs?pretty=true' 
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
  "links" : [ {
    "href" : "http://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0/admin/backup/sync/mongoConfigs?pretty=true&pageNum=1&itemsPerPage=100",
    "rel" : "self"
  } ],
  "results" : [ {
    "assignmentEnabled" : true,
    "encryptedCredentials" : false,
    "id" : "{CONFIG-ID}",
    "labels" : [ "l1", "l2" ],
    "links" : [ {
      "href" : "https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0/admin/backup/sync/mongoConfigs/{SYNCSTORE-ID}",
      "rel" : "self"
    }],
    "maxCapacityGB" : 8,
    "uri" : "mongodb://localhost:27017",
    "ssl" : true,
    "usedSize" : 222,
    "writeConcern" : "W2"
  } ],
  "totalCount" : 1
}
```
