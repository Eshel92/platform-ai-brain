<!-- Converted from reference/api/restorejobs/get-one-single-restore-job-for-one-sccc-config-server.txt (reStructuredText). Includes are inlined. -->

# Get One Restore Job for One Legacy Mirrored Config Server

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

## Resource

```http
GET /groups/{PROJECT-ID}/hosts/{HOST-ID}/restoreJobs/{JOB-ID}
```

### Request Path Parameters

| Name | Type | Description |
|---|---|---|
| PROJECT-ID | string | Unique identifier of the `project` that owns the restore job. |
| HOST-ID | string | Unique identifier of the mirrored config server (SCCC (Sync Cluster Connection Configuration)) that the restore job represents. |
| JOB-ID | string | Unique identifier of the restore job. |

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
 --request GET "https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0/groups/{PROJECT-ID}/hosts/{HOST-ID}/restoreJobs/{JOB-ID}?pretty=true"
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
  "batchId" : "{BATCH-ID}",
  "created" : "2016-03-04T22:07:27Z",
  "delivery" : {
    "expirationHours" : 1,
    "expires" : "2016-03-04T23:07:27Z",
    "maxDownloads" : 1,
    "methodName" : "HTTP",
    "statusName" : "READY",
    "url" : "https://api-backup-qa.mongodb.com/backup/restore/v2/pull/{JOB-ID}/1976673072885966399/electron_0-1456098690-{JOB-ID}.tar.gz"
  },
  "encryptionEnabled" : false,
  "groupId" : "{PROJECT-ID}",
  "hostId" : "{HOST-ID}",
  "id" : "{JOB-ID}",
  "links" : [ {

  } ],
  "pointInTime" : false,
  "snapshotId" : "{SNAPSHOT-ID}",
  "statusName" : "FINISHED",
  "timestamp" : {
    "date" : "2017-04-19T21:14:25Z",
    "increment" : 1
  }
}
```
