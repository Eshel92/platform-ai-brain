<!-- Converted from reference/api/admin/backup/daemonConfigs/get-all-backup-daemon-configurations.txt (reStructuredText). Includes are inlined. -->

# Get All Backup Daemon Configurations

Retrieves the configurations of all backup daemons.

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0/admin/backup`

## Resource

```http
GET /daemon/configs
```

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

Each **result** is one backup daemon.

* - Name
  - Type
  - Description

* - `assignmentEnabled`
  - boolean
  - Flag indicating whether this `Backup Daemon` can be
    assigned backup jobs.

* - `backupJobsEnabled`
  - boolean
  - Flag indicating whether this `Backup Daemon` can be used
    to backup databases.

* - `configured`
  - boolean
  - Flag indicating whether this `Backup Daemon` is ready to
    use.

* - `garbageCollectionEnabled`
  - boolean
  - Flag indicating whether this `Backup Daemon` has garbage
    collection set.

* - `headDiskType`
  - string
  - Type of disk used to store the head directory.

    The accepted values for this option are:

    - `HDD`
    - `SSD`

* - `id`
  - string
  - Unique identifier of this `Backup Daemon`.

* - `labels`
  - array of strings
  - Array of tags to manage which backup jobs
    Ops Manager can assign to which
    `Backup Daemons`.

* - `links`
  - object array
  - .. include:: /includes/api/links-explanation.rst

* - `machine`
  - object
  - `Backup Daemon` host and its
    head directories.

* - `machine.headRootDirectory`
  - string
  - Root-relative path of the head directory on this
    `Backup Daemon` host.

* - `machine.machine`
  - string
  - Hostname or IP address of the `Backup Daemon` host.

* - `numWorkers`
  - number
  - Number of worker processes that can perform tasks (i.e.
    backup, restore, or groom) for the `Backup Daemon`.

* - `resourceUsageEnabled`
  - boolean
  - Flag indicating whether this `Backup Daemon` has its
    resource usage monitored.

* - `restoreQueryableJobsEnabled`
  - boolean
  - Flag indicating whether this `Backup Daemon` can perform
    queryable restores.

## Example Request

```sh
curl --user '{PUBLIC-KEY}:{PRIVATE-KEY}' --digest \
     --header 'Accept: application/json' \
     --include \
     --request GET 'https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0/admin/backup/daemon/configs?pretty=true'
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
    "href" : "http://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0/admin/backup/daemon/configs?pretty=true&pageNum=1&itemsPerPage=100",
    "rel" : "self"
  } ],
  "results" : [ {
     "assignmentEnabled" : true,
     "backupJobsEnabled" : false,
     "configured" : true,
     "garbageCollectionEnabled" : true,
     "headDiskType" : "SSD",
     "id" : "{DAEMON-CONFIG}",
     "labels" : [ "l1", "l2" ],
     "links" : [ {
       "href" : "https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0/admin/backup/daemon/configs/{DAEMON-CONFIG}",
       "rel" : "self"
     }],
     "machine" : {
       "headRootDirectory" : "/data/backup/",
       "machine" : "localhost"
     },
     "numWorkers" : 50,
     "resourceUsageEnabled" : true,
     "restoreJobsEnabled" : false,
     "restoreQueryableJobsEnabled" : true
  } ],
  "totalCount" : 1
}
```
