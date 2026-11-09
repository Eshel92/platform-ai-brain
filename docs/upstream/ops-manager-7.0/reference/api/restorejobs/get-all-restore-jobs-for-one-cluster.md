<!-- Converted from reference/api/restorejobs/get-all-restore-jobs-for-one-cluster.txt (reStructuredText). Includes are inlined. -->

# Get All Restore Jobs for One Cluster

Get all restore jobs for a cluster. `CLUSTER-ID` must be the ID of
either a replica set or a sharded cluster.

**Note:**

If you use the `BATCH-ID` query parameter, you can retrieve all
restore jobs in the specified batch. When creating a restore job for
a sharded cluster, Ops Manager creates a separate job for each shard, plus
another for the config server. Each of those jobs are part of a
batch. A restore job for a replica set, however, cannot be part of a
batch.

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

## Resources

```http
GET /groups/{PROJECT-ID}/clusters/{CLUSTER-ID}/restoreJobs
```

```http
GET /groups/{PROJECT-ID}/clusters/{CLUSTER-ID}/restoreJobs?batchId={BATCH-ID}
```

### Request Path Parameters

| Name | Type | Description |
|---|---|---|
| PROJECT-ID | string | Unique identifier of the `project` that owns the snapshot. |
| CLUSTER-ID | string | Unique identifier of the cluster that the snapshot represents. |

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
| BATCH-ID | string | Unique identifier of the batch. | `NONE` |

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

Each **result** is one cluster restore job.

* - Name
  - Type
  - Description

* - batchId
  - string
  - *Conditional:* sharded cluster only.
    Unique identifier of the batch to which this restore
    job belongs.

* - clusterId
  - string
  - *Conditional:* cluster only.
    Unique identifier of the cluster that the
    restore job represents.

* - created
  - string
  - Timestamp in ISO 8601 date and time format in UTC (Coordinated Universal Time) when the restore job was requested.

* - delivery
  - object
  - Method and details of how the restored snapshot data
    is delivered.

* - delivery.expirationHours
  - number
  - *Conditional:* `"delivery.methodName" : "HTTP"`.
    Number of hours the download URL (Uniform Resource Locator) is valid once the restore
    job is complete.

* - delivery.expires
  - string
  - *Conditional:* `"delivery.methodName" : "HTTP"`.
    Timestamp in ISO 8601 date and time format in UTC (Coordinated Universal Time) after which the URL (Uniform Resource Locator) is no longer available.

* - delivery.maxDownloads
  - number
  - *Conditional:* `"delivery.methodName" : "HTTP"`.
    Number of times the download URL (Uniform Resource Locator) can be used. This must be
    `1` or greater.

* - delivery.methodName
  - string
  - Means by which the data is delivered. Accepted values are:

    - `HTTP`

    **Important:**

    Restore delivery via SCP (secure copy) was removed in
    Ops Manager 4.0.

* - delivery.statusName
  - string
  - Current status of the downloadable file. Accepted values are:

    - `NOT_STARTED`
    - `IN_PROGRESS`
    - `READY`
    - `FAILED`
    - `INTERRUPTED`
    - `EXPIRED`
    - `MAX_DOWNLOADS_EXCEEDED`

* - delivery.url
  - string
  - *Conditional:* `"delivery.methodName" : "HTTP"`.
    URL (Uniform Resource Locator) from which the restored snapshot data can be
    downloaded.

* - encryptionEnabled
  - boolean
  - Flag indicating whether the restored snapshot data is
    encrypted.

* - groupId
  - string
  - Unique identifier of the `group` that owns the restore 
    job.

* - hashes
  - object array
  - If the corresponding `delivery.url` has been downloaded,
    each document in this array is a mapping of a restore file to
    a hashed checksum. This array is present *only after* the
    file is downloaded.

    For an `HTTP` restore, this array contains only a single
    object that represents the hash of the `.tar.gz` file.

* - hashes.fileName
  - string
  - Name of the snapshot file that has been hashed.

* - hashes.hash
  - string
  - Hash of the snapshot file.

* - hashes.typeName
  - string
  - Hashing algorithm used to compute the hash value. If 
    present, this value is `SHA1`.

* - hostId
  - string
  - *Conditional:* mirrored config server
    (SCCC (Sync Cluster Connection Configuration)).
    Unique identifier of the config server to which this 
    restore job belongs.

* - id
  - string
  - Unique identifier of the restore job.

* - links
  - object array
  - .. include:: /includes/api/links-explanation.rst

* - masterKeyUUID
  - string
  - *Conditional:* `"encryptionEnabled" : true`.
    KMIP (Key Management Interoperability) master key ID
    used to encrypt the snapshot data.

* - pointInTime
  - boolean
  - Flag indicating that the job for a 
    PIT (point-in-time) restore.

* - snapshotId
  - string
  - Unique identifier of the snapshot to restore.

* - statusName
  - string
  - Current status of the job. Accepted values are:

    - `FINISHED`
    - `IN_PROGRESS`
    - `BROKEN`
    - `KILLED`

* - timestamp
  - object
  - Timestamp of the Oplog entry when the snapshot was created.

* - timestamp.date
  - string
  - Timestamp in ISO 8601 date and time format in UTC (Coordinated Universal Time) of the latest oplog entry in the restored
    snapshot.

* - timestamp.increment
  - string
  - Order of all operations completed at the latest oplog entry in
    the restored snapshot.

## Example Request

```sh
curl --user "{PUBLIC-KEY}:{PRIVATE-KEY}" --digest \
 --header "Accept: application/json" \
 --include \
 --request GET "https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0/groups/{PROJECT-ID}/clusters/{CLUSTER-ID}/restoreJobs?pretty=true"
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
    "href" : "https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0/groups/{PROJECT-ID}/clusters/{CLUSTER-ID}/restoreJobs?pretty=true&pageNum=1&itemsPerPage=100",
    "rel" : "self"
  } ],
  "results" : [ {
    "batchId" : "{BATCH-ID}",
    "clusterId" : "{CLUSTER-ID}",
    "created" : "2017-04-21T03:49:57Z",
    "delivery" : {
      "expirationHours" : 1,
      "expires" : "2017-04-21T04:49:57Z",
      "maxDownloads" : 1,
      "methodName" : "HTTP",
      "statusName" : "READY",
      "url" : "https://{OPSMANAGER-HOST}:{PORT}/backup/restore/v2/pull/{JOB-ID}/OTY0ZmFiNmEzZjEzNGUyMTlhZjJjNjM3NGMyNGM4ZTM=/electron_0-1492636465-{JOB-ID}.tar.gz"
    },
    "encryptionEnabled" : false,
    "groupId" : "{PROJECT-ID}",
    "id" : "{JOB-ID}",
    "links" : [ {
      "href" : "https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0/groups/{PROJECT-ID}/clusters/{CLUSTER-ID}/restoreJobs/{JOB-ID}",
      "rel" : "self"
    } ],
    "pointInTime" : false,
    "snapshotId" : "{SNAPSHOT-ID}",
    "statusName" : "FINISHED",
    "timestamp" : {
      "date" : "2017-04-18T15:14:25Z",
      "increment" : 1
    }
  }, {
    "batchId" : "{BATCH-ID}",
    "clusterId" : "{CLUSTER-ID}",
    "created" : "2017-04-18T19:21:23Z",
    "delivery" : {
      "expirationHours" : 1,
      "expires" : "2017-04-18T20:21:23Z",
      "maxDownloads" : 1,
      "methodName" : "HTTP",
      "statusName" : "READY",
      "url" : "https://{OPSMANAGER-HOST}:{PORT}/backup/restore/v2/pull/{JOB-ID}/NWRlMTk4NzgxYzNjNDIzOTg2Yzc3YzkyODYxYjNjMzY=/electron_0-1492528465-{JOB-ID}.tar.gz"
    },
    "encryptionEnabled" : false,
    "groupId" : "{PROJECT-ID}",
    "id" : "{JOB-ID}",
    "links" : [ {
      "href" : "https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0/groups/{PROJECT-ID}/clusters/{CLUSTER-ID}/restoreJobs/{JOB-ID}",
      "rel" : "self"
    } ],
    "pointInTime" : false,
    "snapshotId" : "{SNAPSHOT-ID}",
    "statusName" : "FINISHED",
    "timestamp" : {
      "date" : "2017-04-19T21:14:25Z",
      "increment" : 1
    }
  } ],
  "totalCount" : 2
}
```
