<!-- Converted from reference/api/restorejobs/create-one-restore-job-for-one-sccc-config-server.txt (reStructuredText). Includes are inlined. -->

# Create One Restore Job for One Legacy Mirrored Config Server

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

## Resource

```http
POST /groups/{PROJECT-ID}/hosts/{HOST-ID}/restoreJobs
```

### Request Path Parameters

| Name | Type | Description |
|---|---|---|
| PROJECT-ID | string | Unique identifier of the `project` that owns the job. |
| HOST-ID | string | Unique identifier of the mirrored config server (SCCC (Sync Cluster Connection Configuration)) that the job represents. |

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

* - Name
  - Type
  - Necessity
  - Description

* - `checkpointId`
  - string
  - Conditional
  - Unique identifier for the sharded cluster checkpoint
    that represents the point in time to which your data will be
    restored.

    Conditions:

    - Set `"delivery.methodName" : "AUTOMATED_RESTORE"`.
    - Run Sharded Clusters using FCV of 4.0 or earlier.
    - Can't set `oplogInc`, `oplogTs`, or
      `pointInTimeUTCMillis`.

    If you provide this setting, this endpoint restores all data up
    to this `checkpoint` to the database you
    specified in the `delivery` object.

* - `delivery`
  - object
  - Required
  - Method and details of how the restored snapshot data
    is delivered.

* - | `delivery`
    | `.expires`
  - string
  - Conditional
  - Timestamp in ISO 8601 date and time format in UTC (Coordinated Universal Time) after which the URL (Uniform Resource Locator) is no longer available.

    `delivery.methodName" : "HTTP"`

* - | `delivery`
    | `.expirationHours`
  - number
  - Conditional
  - Number of hours the download URL (Uniform Resource Locator) is valid once the restore
    job is complete.

    `delivery.methodName" : "HTTP"`

* - | `delivery`
    | `.maxDownloads`
  - number
  - Conditional
  - Number of times the download URL (Uniform Resource Locator) can be used. This must be
    `1` or greater.

    `delivery.methodName" : "HTTP"`

* - | `delivery`
    | `.methodName`
  - string
  - Required
  - Means by which Ops Manager delivers the data. Accepted values are:

    - `AUTOMATED_RESTORE`
    - `HTTP`

    If you set `"delivery.methodName" : "AUTOMATED_RESTORE"`,
    you must also set:

    - `delivery.targetGroupId` and
    - `delivery.targetClusterId`

    In addition, the response shows the `delivery.methodName`
    as `HTTP`. An automated restore uses the `HTTP` method
    to deliver the restore job to the target host.

    **Important:**

    Restore delivery via SCP (secure copy) was removed in
    Ops Manager 4.0.

* - | `delivery`
    | `.targetClusterId`
  - string
  - Conditional
  - Unique identifier of the target cluster. Use the `clusterId`
    returned in the response body of the
    Get All Snapshots
    and Get a Snapshot
    endpoints.

    `delivery.methodName" : "AUTOMATED_RESTORE"`.

    If backup is not enabled on the target cluster, the
    Get All Snapshots
    endpoint returns an empty `results` array without
    `clusterId` elements, and the
    Get a Snapshot
    endpoint also does not return a `clusterId` element.

* - | `delivery`
    | `.targetGroupId`
  - string
  - Conditional
  - Unique identifier of the project that contains the destination
    cluster for the restore job.

    `delivery.methodName" : "AUTOMATED_RESTORE"`

* - `oplogTs`
  - string
  - Conditional
  - Oplog timestamp given as a
    Timestamp in the number of seconds that have elapsed since the [UNIX epoch](https://en.wikipedia.org/wiki/Unix_time?oldid=828172017). When paired with `oplogInc`, they represent the
    point in time to which your data will be restored.

    Run a query against `local.oplog.rs` on your
    replica set to find the desired timestamp.

    `"delivery.methodName" : "AUTOMATED_RESTORE"`
    *for Replica Sets Only.*

    If you set `oplogTs`, you:

    - Must set `oplogInc`.
    - Cannot set `checkpointId` or `pointInTimeUTCMillis`.

    If you provide this setting, this endpoint restores all data up
    to *and including* this Oplog timestamp to the database you
    specified in the `delivery` object.

* - `oplogInc`
  - string
  - Conditional
  - 32-bit incrementing ordinal
    that represents operations within a given second. When paired
    with `oplogTs`, they represent the point in time to which
    your data will be restored.

    `"delivery.methodName" : "AUTOMATED_RESTORE"`
    *for Replica Sets Only.*

    If you set `oplogInc`, you:

    - Must set `oplogTs`.
    - Cannot set `checkpointId` or `pointInTimeUTCMillis`.

    If you provide this setting, this endpoint restores all data up
    to *and including* this Oplog timestamp to the database you
    specified in the `delivery` object.

* - `pointInTimeUTCMillis`
  - long
  - Conditional
  - timestamp in the number of milliseconds that have elapsed since the [UNIX epoch](https://en.wikipedia.org/wiki/Unix_time?oldid=828172017) that represents the point in time to which your
    data will be restored. This timestamp must be within last 24
    hours of the current time.

    If you provide this setting, this endpoint restores all data up
    to this `Point in Time`  to the
    database you specified in the `delivery` object.

    `"delivery.methodName" : "AUTOMATED_RESTORE"`
    *for Replica Sets Only.*

    If you set `pointInTimeUTCMillis`, you cannot set
    `oplogInc`, `oplogTs`, or `checkpointId`.

* - `snapshotId`
  - string
  - Conditional
  - Unique identifier of the snapshot to restore.

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
    - `AUTOMATED_RESTORE`

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

* - delivery.targetClusterId
  - string
  - *Conditional:* `delivery.methodName" : "AUTOMATED_RESTORE"`.
    Unique identifier of the destination cluster to perform the 
    restore job. 

* - delivery.targetGroupId
  - string
  - *Conditional:* `delivery.methodName" : "AUTOMATED_RESTORE"`.
    Unique identifier of the project that contains the
    destination cluster for the restore job.

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

Create a restore job that transfers a compressed snapshot using HTTP (Hypertext Transfer Protocol).

```sh
curl --user "{PUBLIC-KEY}:{PRIVATE-KEY}" --digest \
 --header "Accept: application/json" \
 --header "Content-Type: application/json" \
 --include \
 --request POST "https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0/groups/{PROJECT-ID}/hosts/{HOST-ID}/restoreJobs?pretty=true" \
 --data '
  {
    "delivery" : {
      "expirationHours" : 1,
      "expires" : "2017-04-21T04:49:57Z",
      "maxDownloads" : 1,
      "methodName" : "HTTP",
      "statusName" : "READY",
      "url" : "https://restore.example.com/backup/restore/v2/pull/{JOB-ID}/OTY0ZmFiNmEzZjEzNGUyMTlhZjJjNjM3NGMyNGM4ZTM=/electron_0-1492636465-{JOB-ID}.tar.gz"
    },
    "snapshotId" : "{SNAPSHOT-ID}"
  }'
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
  "created" : "2017-08-25T16:22:15Z",
  "delivery" : {
    "expirationHours" : 1,
    "expires" : "2017-04-21T04:49:57Z",
    "maxDownloads" : 1,
    "methodName" : "HTTP",
    "statusName" : "READY",
    "url" : "https://restore.example.com/backup/restore/v2/pull/{JOB-ID}/OTY0ZmFiNmEzZjEzNGUyMTlhZjJjNjM3NGMyNGM4ZTM=/electron_0-1492636465-{JOB-ID}.tar.gz"
  },
  "encryptionEnabled" : true,
  "groupId" : "{PROJECT-ID}",
  "hostId" : "{HOST-ID}",
   "id" : "{JOB-ID}",
  "links" : [ {
    "href" : "https://cloud.mongodb.com/api/public/v1.0/groups/{PROJECT-ID}/hosts/{HOST-ID}/restoreJobs/{JOB-ID}",
    "rel" : "self"
  }, {
    "href" : "https://cloud.mongodb.com/api/public/v1.0/groups/{PROJECT-ID}/hosts/{HOST-ID}",
    "rel" : "http://mms.mongodb.com/cluster"
  }, {
    "href" : "https://cloud.mongodb.com/api/public/v1.0/groups/{PROJECT-ID}/hosts/{HOST-ID}/snapshots/{SNAPSHOT-ID}",
    "rel" : "http://mms.mongodb.com/snapshot"
  }, {
    "href" : "https://cloud.mongodb.com/api/public/v1.0/groups/{PROJECT-ID}",
    "rel" : "http://mms.mongodb.com/group"
  } ],
  "masterKeyUUID" : "{UUID}",
  "snapshotId" : "{SNAPSHOT-ID}",
  "statusName" : "IN_PROGRESS"
}
```
