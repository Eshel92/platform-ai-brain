<!-- Converted from reference/api/admin/backup/groups/get-all-backup-group-configurations.txt (reStructuredText). Includes are inlined. -->

# Get All Project Backup Jobs Configurations

Retrieves the configurations of all project's backup jobs.

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0/admin/backup`

## Resource

```http
GET /groups
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

Each **result** is one project's backup jobs.

* - Name
  - Type
  - Description

* - daemonFilter
  - object array
  - An array of pairs of `Backup Daemon` hosts and 
    their head directories that to which  
    this project's backup jobs are limited.

* - daemonFilter.headRootDirectory
  - string
  - The root-relative path of the head directory on this 
    `Backup Daemon` host.

* - daemonFilter.machine
  - string
  - The host address for one `Backup Daemon` host.

* - id
  - string
  - The unique identifier that represents this project and its 
    backup job configuration.

* - kmipClientCertPassword
  - string
  - The password that encrypts the 
    KMIP (Key Management Interoperability Protocol)
    client certificate.

* - kmipClientCertPath
  - string
  - The path to the directory on the `Backup Daemon` host that 
    stores the KMIP (Key Management Interoperability Protocol) 
    client certificate.

* - links
  - object array
  - .. include:: /includes/api/links-explanation.rst

* - labelFilter
  - array of strings
  - An array of tags that limits which 
    `Backup Daemons` and 
    `snapshot stores` can process 
    backup jobs for this project.

* - oplogStoreFilter
  - array of objects
  - An array of unique identifiers representing 
    `Oplog stores` that may be used 
    with this project's backup jobs.

* - oplogStoreFilter.id
  - string
  - Unique identifier representing an
    `oplog store` that may be used 
    with this project's backup jobs.

* - oplogStoreFilter.type
  - string
  - Type of `oplog store` to use. This 
    value is always `oplogStore`.

* - snapshotStoreFilter
  - array of objects
  - Array of unique identifiers representing specific 
    `snapshot stores` and their types that can 
    be used with this project's backup jobs. If omitted, all 
    available snapshot stores are used.

* - snapshotStoreFilter.id
  - string
  - The unique identifier representing specific 
    `snapshot stores` that can be 
    used with this project's backup jobs.

* - snapshotStoreFilter.type
  - string
  - The type of the specific snapshot store given as 
    `snapshotStoreFilter.id`.

    The accepted values for this option are:

    - `s3blockstore`
    - `blockstore`
    - `fileSystemStore`

* - syncStoreFilter
  - array of strings
  - An array of sync store filters that can be used with this 
    project's backup jobs. If omitted, all available sync stores 
    are used.

## Example Request

```sh
curl --user '{PUBLIC-KEY}:{PRIVATE-KEY}' --digest \
 --header 'Accept: application/json' \
 --include \
 --request GET 'https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0/admin/backup/groups?pretty=true'
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
    "href" : "http://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0/admin/backup/groups?pretty=true&pageNum=1&itemsPerPage=100",
    "rel" : "self"
  } ],
  "results" : [ {
    "daemonFilter" : [ {
      "headRootDirectory" : "/data/backup",
      "machine" : "http://backup.example.com"
    } ],
    "id" : "{PROJECT-ID}",
    "kmipClientCertPassword" : "P4$$w0rD",
    "kmipClientCertPath" : "/certs/kmip",
    "labelFilter" : [ "label1", "label2" ],
    "links" : [ {
      "href" : "https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0/admin/backup/groups/{PROJECT-ID}",
      "rel" : "self"
    }, {
      "href" : "https://{OPSMANAGER-HOST}:{PORT}/api/public/groups/{PROJECT-ID}",
      "rel" : "http://mms.mongodb.com/group"
    } ],
    "oplogStoreFilter" : [ {
      "id" : "oplog1",
      "type" : "oplogStore"
    } ],
    "snapshotStoreFilter" : [ {
      "id" : "sPid",
      "type" : "s3blockstore"
    } ],
    "syncStoreFilter" : [ "s1", "s2" ]
  } ],
  "totalCount" : 1
}
```
