<!-- Converted from reference/api/restorejobs/create-one-restore-job-for-one-cluster.txt (reStructuredText). Includes are inlined. -->

# Create One Restore Job for One Cluster

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

## Resource

```http
POST /groups/{PROJECT-ID}/clusters/{CLUSTER-ID}/restoreJobs
```

### Request Path Parameters

| Name | Type | Description |
|---|---|---|
| `PROJECT-ID` | string | Unique identifier of the project that owns the job. |
| `CLUSTER-ID` | string | Unique identifier of the cluster that the job represents. |

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

**http:**

| Name | Type | Necessity | Description |
|---|---|---|---|
| `delivery` | object | Required | Method and details of how the restored snapshot data is delivered. |
| \| `delivery` \| `.expires` | string | Conditional | Timestamp in ISO 8601 date and time format in UTC (Coordinated Universal Time) after which the URL (Uniform Resource Locator) is no longer available. If you set `delivery.expires`, you can't set `delivery.expirationHours`. |
| \| `delivery` \| `.expirationHours` | number | Conditional | Number of hours the download URL (Uniform Resource Locator) is valid once the restore job is complete. If you set `delivery.expirationHours`, you can't set `delivery.expires`. |
| \| `delivery` \| `.maxDownloads` | number | Required | Number of times the download URL (Uniform Resource Locator) can be used. This must be `1` or greater. |
| \| `delivery` \| `.methodName` | string | Required | Means by which Ops Manager delivers the data. Set to `HTTP`. |
| `snapshotId` | string | Required | Unique identifier of the snapshot to restore. |

**automated:**

**Note:** Condition

If you set ``"delivery.methodName" :
AUTOMATED_RESTORE"``, you must set
`delivery.targetGroupId` and
`delivery.targetClusterId`.

**auto-snapshot:**

Create an automated restore from a snapshot.

* - Name
  - Type
  - Necessity
  - Description

* - `delivery`
  - object
  - Required
  - Method and details of how the restored snapshot data
    is delivered.

* - | `delivery`
    | `.methodName`
  - string
  - Required
  - Means by which Ops Manager delivers the data. Set to
    `AUTOMATED_RESTORE`.

    The response shows the `"delivery.methodName" : "HTTP"`. An
    automated restore uses the `HTTP` method to deliver the
    restore job to the target host.

    **Important:**

    Restore delivery via SCP (secure copy) was removed in
    Ops Manager 4.0.

* - | `delivery`
    | `.targetClusterId`
  - string
  - Required
  - Unique identifier of the target cluster. Use the `clusterId`
    returned in the response body of the
    Get All Snapshots
    and Get a Snapshot
    endpoints.

    If backup is not enabled on the target cluster, the
    Get All Snapshots
    endpoint returns an empty `results` array without
    `clusterId` elements, and the
    Get a Snapshot
    endpoint also does not return a `clusterId` element.

* - | `delivery`
    | `.targetGroupId`
  - string
  - Required
  - Unique identifier of the project that contains the destination
    cluster for the restore job.

* - `snapshotId`
  - string
  - Required
  - Unique identifier of the snapshot to restore.

**auto-oplog:**

Create an automated restore from an Oplog timestamp.

Oplog Restores work with Replica Sets using any MongoDB
version or Sharded Clusters using FCV of 4.2 or
later.

* - Name
  - Type
  - Necessity
  - Description

* - `delivery`
  - object
  - Required
  - Method and details of how the restored snapshot data
    is delivered.

* - | `delivery`
    | `.methodName`
  - string
  - Required
  - Means by which Ops Manager delivers the data. Set to
    `AUTOMATED_RESTORE`.

    The response shows the `"delivery.methodName" : "HTTP"`. An
    automated restore uses the `HTTP` method to deliver the
    restore job to the target host.

    **Important:**

    Restore delivery via SCP (secure copy) was removed in
    Ops Manager 4.0.

* - | `delivery`
    | `.targetClusterId`
  - string
  - Required
  - Unique identifier of the target cluster. Use the `clusterId`
    returned in the response body of the
    Get All Snapshots
    and Get a Snapshot
    endpoints.

    If backup is not enabled on the target cluster, the
    Get All Snapshots
    endpoint returns an empty `results` array without
    `clusterId` elements, and the
    Get a Snapshot
    endpoint also does not return a `clusterId` element.

* - | `delivery`
    | `.targetGroupId`
  - string
  - Required
  - Unique identifier of the project that contains the destination
    cluster for the restore job.

* - `oplogTs`
  - string
  - Required
  - Oplog timestamp given as a
    Timestamp in the number of seconds that have elapsed since the [UNIX epoch](https://en.wikipedia.org/wiki/Unix_time?oldid=828172017). When paired with `oplogInc`, they represent the
    point in time to which your data will be restored.

    Run a query against `local.oplog.rs` on your
    replica set to find the desired timestamp.

    If you provide this setting, this endpoint restores all data up
    to *and including* this Oplog timestamp to the database you
    specified in the `delivery` object.

* - `oplogInc`
  - string
  - Required
  - 32-bit incrementing ordinal that represents operations within a
    given second. When paired with `oplogTs`, they represent the
    point in time to which your data will be restored.

    If you provide this setting, this endpoint restores all data up
    to *and including* this Oplog timestamp to the database you
    specified in the `delivery` object.

**auto-pit:**

Create an automated restore from a specific point in time.

PIT Restores work with Replica Sets using any MongoDB
version or Sharded Clusters using FCV of 4.2 or
later.

* - Name
  - Type
  - Necessity
  - Description

* - `delivery`
  - object
  - Required
  - Method and details of how the restored snapshot data
    is delivered.

* - | `delivery`
    | `.methodName`
  - string
  - Required
  - Means by which Ops Manager delivers the data. Set to
    `AUTOMATED_RESTORE`.

    The response shows the `"delivery.methodName" : "HTTP"`. An
    automated restore uses the `HTTP` method to deliver the
    restore job to the target host.

    **Important:**

    Restore delivery via SCP (secure copy) was removed in
    Ops Manager 4.0.

* - | `delivery`
    | `.targetClusterId`
  - string
  - Required
  - Unique identifier of the target cluster. Use the `clusterId`
    returned in the response body of the
    Get All Snapshots
    and Get a Snapshot
    endpoints.

    If backup is not enabled on the target cluster, the
    Get All Snapshots
    endpoint returns an empty `results` array without
    `clusterId` elements, and the
    Get a Snapshot
    endpoint also does not return a `clusterId` element.

* - | `delivery`
    | `.targetGroupId`
  - string
  - Required
  - Unique identifier of the project that contains the destination
    cluster for the restore job.

* - `pointInTimeUTCMillis`
  - long
  - Required
  - timestamp in the number of milliseconds that have elapsed since the [UNIX epoch](https://en.wikipedia.org/wiki/Unix_time?oldid=828172017) that represents the point in time to which your
    data will be restored. This timestamp must be within last 24
    hours of the current time.

    If you provide this setting, this endpoint restores all data up
    to this `Point in Time` to the
    database you specified in the `delivery` object.

**auto-checkpoint:**

Create an automated restore from a checkpoint. Checkpoint
restores work for
sharded clusters running MongoDB
clusters with an FCV of 4.0 or earlier.

**Important:**

Don't use checkpoint restores for MongoDB clusters with
an FCV (Feature Compatibility Version) of 4.2 or later.

| Name | Type | Necessity | Description |
|---|---|---|---|
| `checkpointId` | string | Required | Unique identifier for the sharded cluster checkpoint that represents the point in time to which your data will be restored. If you provide this setting, this endpoint restores all data up to this `checkpoint` to the database you specified in the `delivery` object. |
| `delivery` | object | Required | Method and details of how the restored snapshot data is delivered. |
| \| `delivery` \| `.methodName` | string | Required | Means by which Ops Manager delivers the data. Set to `AUTOMATED_RESTORE`. The response shows the `"delivery.methodName" : "HTTP"`. An automated restore uses the `HTTP` method to deliver the restore job to the target host. |
| \| `delivery` \| `.targetClusterId` | string | Required | Unique identifier of the target cluster. Use the `clusterId` returned in the response body of the Get All Snapshots and Get a Snapshot endpoints. If backup is not enabled on the target cluster, the Get All Snapshots endpoint returns an empty `results` array without `clusterId` elements, and the Get a Snapshot endpoint also does not return a `clusterId` element. |
| \| `delivery` \| `.targetGroupId` | string | Required | Unique identifier of the project that contains the destination cluster for the restore job. |

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

Each **result** is one cluster restore job. This array includes one
restore job only.

**http:**

* - Name
  - Type
  - Description

* - `batchId`
  - string
  - Unique identifier of the batch to which this restore
    job belongs. Returned if snapshot was from a sharded cluster.

* - `clusterId`
  - string
  - Unique identifier of the cluster that the restore job
    represents. Returned if snapshot was from a replica set or
    sharded cluster.

* - `created`
  - string
  - Timestamp in ISO 8601 date and time format in UTC (Coordinated Universal Time) when the restore job was requested.

* - `delivery`
  - object
  - Method and details of how the restored snapshot data
    is delivered.

* - | `delivery`
    | `.authBearer`
  - string
  - Authorization bearer for requests to `urlV2`. Value must  
    be `Bearer`. 

* - | `delivery`
    | `.authHeader`
  - string
  - Authorization header for requests to `urlV2`. Value must 
    be `Authorization`.

* - | `delivery`
    | `.authValue`
  - string
  - Value for the bearer for requests to `urlV2`. The 
    `authValue` for the bearer must be the token value.

* - | `delivery`
    | `.expirationHours`
  - number
  - Number of hours the download URL (Uniform Resource Locator) is valid once the restore
    job is complete.

* - | `delivery`
    | `.expires`
  - string
  - Timestamp in ISO 8601 date and time format in UTC (Coordinated Universal Time) after which the URL (Uniform Resource Locator) is no longer available.

* - | `delivery`
    | `.maxDownloads`
  - number
  - Number of times the download URL (Uniform Resource Locator) can be used. This must be
    `1` or greater.

* - | `delivery`
    | `.methodName`
  - string
  - Means by which the data is delivered. Returns `HTTP`.

* - | `delivery`
    | `.statusName`
  - string
  - Current status of the downloadable file. Accepted values are:

    - `NOT_STARTED`
    - `IN_PROGRESS`
    - `READY`
    - `FAILED`
    - `INTERRUPTED`
    - `EXPIRED`
    - `MAX_DOWNLOADS_EXCEEDED`

* - | `delivery`
    | `.url`
  - string
  - URL (Uniform Resource Locator) from which the restored snapshot data can be
    downloaded.

* - | `delivery`
    | `.urlV2`
  - string
  - URL (Uniform Resource Locator) from which the restored snapshot data can be
    securely downloaded. Requests to this URL (Uniform Resource Locator) must include the 
    `authHeader`, `authBearer`, and `authValue` in the HTTP 
    request header. The request header for securely downloading 
    from `urlv2` must be in the following format:

    ```sh
    "<authHeader>:<authBearer> <authValue>" <urlV2>
    ```

    **Example:**

    ```sh
    curl -H "Authorization: Bearer {AUTH-TOKEN}" \
         https://{OPSMANAGER-HOST}:{PORT}/backup/restore/v3/pull/{restoreJobId}/{filename}"
    ```

* - `groupId`
  - string
  - Unique identifier of the `group` that owns the restore
    job.

* - `hashes`
  - array of objects
  - If the corresponding `delivery.url` has been downloaded, this
    array returns a single object that represents the hash of
    the `.tar.gz` file.

* - | `hashes`
    | `.fileName`
  - string
  - Name of the snapshot file that has been hashed.

* - | `hashes`
    | `.hash`
  - string
  - Hash of the snapshot file.

* - | `hashes`
    | `.typeName`
  - string
  - Hashing algorithm used to compute the hash value. If returned,
    value is set to `SHA1`.

* - `hostId`
  - string
  - Unique identifier of the config server to which this
    restore job belongs. Returned if config server was a
    SCCC (Sync Cluster Connection Configuration).

* - `id`
  - string
  - Unique identifier of the restore job.

* - `links`
  - array of objects
  - .. include:: /includes/api/links-explanation.rst

* - `pointInTime`
  - boolean
  - Flag indicating if the snapshot was from a point in time.

* - `snapshotId`
  - string
  - Unique identifier of the snapshot to restore.

* - `statusName`
  - string
  - Current status of the job. Accepted values are:

    - `FINISHED`
    - `IN_PROGRESS`
    - `BROKEN`
    - `KILLED`

* - `timestamp`
  - object
  - Timestamp of the Oplog entry when the snapshot was created.

* - | `timestamp`
    | `.date`
  - string
  - Timestamp in ISO 8601 date and time format in UTC (Coordinated Universal Time) of the latest oplog entry in the restored
    snapshot.

* - | `timestamp`
    | `.increment`
  - string
  - Order of all operations completed at the latest oplog entry in
    the restored snapshot.

**automated:**

**auto-snapshot:**

* - Name
  - Type
  - Description

* - `batchId`
  - string
  - Unique identifier of the batch to which this restore
    job belongs. Returned if snapshot was from a sharded cluster.

* - `clusterId`
  - string
  - Unique identifier of the cluster that the restore job
    represents. Returned if snapshot was from a replica set or
    sharded cluster.

* - `created`
  - string
  - Timestamp in ISO 8601 date and time format in UTC (Coordinated Universal Time) when the restore job was requested.

* - `delivery`
  - object
  - Method and details of how the restored snapshot data
    is delivered.

* - | `delivery`
    | `.methodName`
  - string
  - Means by which the data is delivered. Returns `HTTP`.

* - | `delivery`
    | `.targetClusterId`
  - string
  - Unique identifier of the destination cluster to perform the
    restore job.

* - | `delivery`
    | `.targetGroupId`
  - string
  - Unique identifier of the project that contains the
    destination cluster for the restore job.

* - `groupId`
  - string
  - Unique identifier of the `group` that owns the restore
    job.

* - `hostId`
  - string
  - Unique identifier of the config server to which this
    restore job belongs. Returned if config server was a
    SCCC (Sync Cluster Connection Configuration).

* - `id`
  - string
  - Unique identifier of the restore job.

* - `links`
  - object array
  - .. include:: /includes/api/links-explanation.rst

* - `pointInTime`
  - boolean
  - Flag indicating if the snapshot was from a point in time.

* - `snapshotId`
  - string
  - Unique identifier of the snapshot to restore.

* - `statusName`
  - string
  - Current status of the job. Accepted values are:

    - `FINISHED`
    - `IN_PROGRESS`
    - `BROKEN`
    - `KILLED`

* - `timestamp`
  - object
  - Timestamp of the Oplog entry when the snapshot was created.

* - | `timestamp`
    | `.date`
  - string
  - Timestamp in ISO 8601 date and time format in UTC (Coordinated Universal Time) of the latest oplog entry in the restored
    snapshot.

* - | `timestamp`
    | `.increment`
  - string
  - Order of all operations completed at the latest oplog entry in
    the restored snapshot.

**auto-oplog:**

* - Name
  - Type
  - Description

* - `batchId`
  - string
  - Unique identifier of the batch to which this restore
    job belongs. Returned if snapshot was from a sharded cluster.

* - `clusterId`
  - string
  - Unique identifier of the cluster that the restore job
    represents. Returned if snapshot was from a replica set or
    sharded cluster.

* - `created`
  - string
  - Timestamp in ISO 8601 date and time format in UTC (Coordinated Universal Time) when the restore job was requested.

* - `delivery`
  - object
  - Method and details of how the restored snapshot data
    is delivered.

* - | `delivery`
    | `.methodName`
  - string
  - Means by which the data is delivered. Returns `HTTP`.

* - | `delivery`
    | `.targetClusterId`
  - string
  - Unique identifier of the destination cluster to perform the
    restore job.

* - | `delivery`
    | `.targetGroupId`
  - string
  - Unique identifier of the project that contains the
    destination cluster for the restore job.

* - `groupId`
  - string
  - Unique identifier of the `group` that owns the restore
    job.

* - `hostId`
  - string
  - Unique identifier of the config server to which this
    restore job belongs. Returned if config server was a
    SCCC (Sync Cluster Connection Configuration).

* - `id`
  - string
  - Unique identifier of the restore job.

* - `links`
  - object array
  - .. include:: /includes/api/links-explanation.rst

* - `pointInTime`
  - boolean
  - Flag indicating if the snapshot was from a point in time.

* - `snapshotId`
  - string
  - Unique identifier of the snapshot to restore.

* - `statusName`
  - string
  - Current status of the job. Accepted values are:

    - `FINISHED`
    - `IN_PROGRESS`
    - `BROKEN`
    - `KILLED`

* - `timestamp`
  - object
  - Timestamp of the Oplog entry when the snapshot was created.

* - | `timestamp`
    | `.date`
  - string
  - Timestamp in ISO 8601 date and time format in UTC (Coordinated Universal Time) of the latest oplog entry in the restored
    snapshot.

* - | `timestamp`
    | `.increment`
  - string
  - Order of all operations completed at the latest oplog entry in
    the restored snapshot.

**auto-pit:**

* - Name
  - Type
  - Description

* - `batchId`
  - string
  - Unique identifier of the batch to which this restore
    job belongs. Returned if snapshot was from a sharded cluster.

* - `clusterId`
  - string
  - Unique identifier of the cluster that the restore job
    represents. Returned if snapshot was from a replica set or
    sharded cluster.

* - `created`
  - string
  - Timestamp in ISO 8601 date and time format in UTC (Coordinated Universal Time) when the restore job was requested.

* - `delivery`
  - object
  - Method and details of how the restored snapshot data
    is delivered.

* - | `delivery`
    | `.methodName`
  - string
  - Means by which the data is delivered. Returns `HTTP`.

* - | `delivery`
    | `.targetClusterId`
  - string
  - Unique identifier of the destination cluster to perform the
    restore job.

* - | `delivery`
    | `.targetGroupId`
  - string
  - Unique identifier of the project that contains the
    destination cluster for the restore job.

* - `groupId`
  - string
  - Unique identifier of the `group` that owns the restore
    job.

* - `hostId`
  - string
  - Unique identifier of the config server to which this
    restore job belongs. Returned if config server was a
    SCCC (Sync Cluster Connection Configuration).

* - `id`
  - string
  - Unique identifier of the restore job.

* - `links`
  - object array
  - .. include:: /includes/api/links-explanation.rst

* - `pointInTime`
  - boolean
  - Flag indicating if the snapshot was from a point in time.

* - `snapshotId`
  - string
  - Unique identifier of the snapshot to restore.

* - `statusName`
  - string
  - Current status of the job. Accepted values are:

    - `FINISHED`
    - `IN_PROGRESS`
    - `BROKEN`
    - `KILLED`

* - `timestamp`
  - object
  - Timestamp of the Oplog entry when the snapshot was created.

* - | `timestamp`
    | `.date`
  - string
  - Timestamp in ISO 8601 date and time format in UTC (Coordinated Universal Time) of the latest oplog entry in the restored
    snapshot.

* - | `timestamp`
    | `.increment`
  - string
  - Order of all operations completed at the latest oplog entry in
    the restored snapshot.

**auto-checkpoint:**

* - Name
  - Type
  - Description

* - `batchId`
  - string
  - Unique identifier of the batch to which this restore
    job belongs. Returned if snapshot was from a sharded cluster.

* - `checkpointId`
  - string
  - Unique identifier for the sharded cluster checkpoint
    that represents the point in time to which your data will be
    restored.

* - `clusterId`
  - string
  - Unique identifier of the cluster that the restore job
    represents. Returned if snapshot was from a replica set or
    sharded cluster.

* - `created`
  - string
  - Timestamp in ISO 8601 date and time format in UTC (Coordinated Universal Time) when the restore job was requested.

* - `delivery`
  - object
  - Method and details of how the restored snapshot data
    is delivered.

* - | `delivery`
    | `.methodName`
  - string
  - Means by which the data is delivered. Returns `HTTP`.

* - | `delivery`
    | `.targetClusterId`
  - string
  - Unique identifier of the destination cluster to perform the
    restore job.

* - | `delivery`
    | `.targetGroupId`
  - string
  - Unique identifier of the project that contains the
    destination cluster for the restore job.

* - `groupId`
  - string
  - Unique identifier of the `group` that owns the restore
    job.

* - `hostId`
  - string
  - Unique identifier of the config server to which this
    restore job belongs. Returned if config server was a
    SCCC (Sync Cluster Connection Configuration).

* - `id`
  - string
  - Unique identifier of the restore job.

* - `links`
  - object array
  - .. include:: /includes/api/links-explanation.rst

* - `pointInTime`
  - boolean
  - Flag indicating if the snapshot was from a point in time.

* - `statusName`
  - string
  - Current status of the job. Accepted values are:

    - `FINISHED`
    - `IN_PROGRESS`
    - `BROKEN`
    - `KILLED`

* - `timestamp`
  - object
  - Timestamp of the Oplog entry when the snapshot was created.

* - | `timestamp`
    | `.date`
  - string
  - Timestamp in ISO 8601 date and time format in UTC (Coordinated Universal Time) of the latest oplog entry in the restored
    snapshot.

* - | `timestamp`
    | `.increment`
  - string
  - Order of all operations completed at the latest oplog entry in
    the restored snapshot.

## Example Request

**http:**

Create a restore job that transfers a compressed snapshot
using HTTP (Hypertext Transfer Protocol).

```sh
curl --user "{PUBLIC-KEY}:{PRIVATE-KEY}" --digest \
  --header "Accept: application/json" \
  --header "Content-Type: application/json" \
  --include \
  --request POST "https://<OpsManagerHost>:<Port>/api/public/v1.0/groups/{PROJECT-ID}/clusters/{CLUSTER-ID}/restoreJobs?pretty=true" \
  --data '
   {
     "delivery" : {
       "expirationHours" : "1",
       "maxDownloads" : "1",
       "methodName" : "HTTP"
     },
     "snapshotId" : "{SNAPSHOT-ID}"
   }'
```

**automated:**

**auto-snapshot:**

Create an automated restore from a snapshot.

```sh
curl --user "{PUBLIC-KEY}:{PRIVATE-KEY}" --digest \
     --header "Accept: application/json" \
     --header "Content-Type: application/json" \
     --request POST "https://<OpsManagerHost>:<Port>/api/public/v1.0/groups/{PROJECT-ID}/clusters/{CLUSTER-ID}/restoreJobs?pretty=true" \
     --data '
       {
         "delivery" : {
           "methodName" : "AUTOMATED_RESTORE",
           "targetGroupId" : "{TARGET-PROJECT-ID}",
           "targetClusterId" : "{TARGET-CLUSTER-ID}"
         },
         "snapshotId": "{SNAPSHOT-ID}"
       }'
```

**auto-oplog:**

Create an automated restore from an Oplog timestamp.

```sh
curl --user "{PUBLIC-KEY}:{PRIVATE-KEY}" --digest \
  --header "Accept: application/json" \
  --header "Content-Type: application/json" \
  --include \
  --request POST "https://<OpsManagerHost>:<Port>/api/public/v1.0/groups/{PROJECT-ID}/clusters/{CLUSTER-ID}/restoreJobs?pretty=true" \
  --data '
   {
     "delivery" : {
       "methodName" : "AUTOMATED_RESTORE",
       "targetGroupId" : "{TARGET-PROJECT-ID}",
       "targetClusterId" : "{TARGET-CLUSTER-ID}"
     },
     "oplogTs" : "1536610288",
     "oplogInc" : "1"
   }'
```

**auto-pit:**

Create an automated restore from a specific point in time.

```sh
curl --user "{PUBLIC-KEY}:{PRIVATE-KEY}" --digest \
  --header "Accept: application/json" \
  --header "Content-Type: application/json" \
  --include \
  --request POST "https://<OpsManagerHost>:<Port>/api/public/v1.0/groups/{PROJECT-ID}/clusters/{CLUSTER-ID}/restoreJobs?pretty=true" \
  --data '
   {
     "delivery" : {
       "methodName" : "AUTOMATED_RESTORE",
       "targetGroupId" : "{TARGET-PROJECT-ID}",
       "targetClusterId" : "{TARGET-CLUSTER-ID}"
     },
     "pointInTimeUTCMillis" : "1536610288000"
   }'
```

**auto-checkpoint:**

Create an automated restore from a checkpoint. Valid for
sharded clusters running MongoDB
clusters with an FCV (Feature Compatibility Version) of 4.0 or earlier only.

**Important:**

Don't use checkpoint restores for MongoDB clusters with
an FCV (Feature Compatibility Version) of 4.2 or later.

```sh
curl --user "{PUBLIC-KEY}:{PRIVATE-KEY}" --digest \
  --header "Accept: application/json" \
  --header "Content-Type: application/json" \
  --include \
  --request POST "https://<OpsManagerHost>:<Port>/api/public/v1.0/groups/{PROJECT-ID}/clusters/{CLUSTER-ID}/restoreJobs?pretty=true" \
  --data '
   {
     "delivery" : {
       "methodName" : "AUTOMATED_RESTORE",
       "targetGroupId" : "{TARGET-PROJECT-ID}",
       "targetClusterId" : "{TARGET-CLUSTER-ID}"
     },
     "checkpointId" : "{CHECKPOINT-ID}"
   }'
```

## Example Responses

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

**http:**

```json
{
  "links" : [ {
    "href" : "https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0/groups/{PROJECT-ID}/clusters/{CLUSTER-ID}/restoreJobs?pretty=true&pageNum=1&itemsPerPage=100",
    "rel" : "self"
  } ],
  "results" : [ {
    "batchId": "{BATCH-ID}",
    "clusterId": "{CLUSTER-ID}",
    "created": "2018-09-20T15:00:00Z",
    "delivery": {
      "authBearer": "Bearer",
      "authHeader": "Authorization",
      "expirationHours": 1,
      "maxDownloads": 1,
      "methodName": "HTTP",
      "statusName": "READY"
    },
    "encryptionEnabled": false,
    "groupId": "{PROJECT-ID}",
    "id": "{RESTORE-JOB-ID}",
    "links": [{
      "href": "https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0/groups/{PROJECT-ID}/clusters/{CLUSTER-NAME}/restoreJobs/{RESTORE-JOB-ID}",
      "rel": "self"
    }],
    "pointInTime": false,
    "snapshotId": "{SNAPSHOT-ID}",
    "statusName": "FINISHED",
    "timestamp": {
      "date": "2018-09-15T15:53:00Z",
      "increment": 1
    }
  } ],
  "totalCount" : 1,
  "url": "{DOWNLOAD-URL}",
  "urlV2": "https://{OPSMANAGER-HOST}:{PORT}/backup/restore/v3/pull/{restoreJobId}/{filename}"
}
```

**automated:**

**auto-snapshot:**

```json
{
  "links" : [ {
    "href" : "https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0/groups/{PROJECT-ID}/clusters/{CLUSTER-ID}/restoreJobs?pretty=true&pageNum=1&itemsPerPage=100",
    "rel" : "self"
  } ],
  "results" : [ {
    "batchId" : "{BATCH-ID}",
    "clusterId" : "{CLUSTER-ID}",
    "created" : "2020-04-21T03:49:57Z",
    "delivery" : {
      "expirationHours" : 1,
      "expires" : "2020-04-21T04:49:57Z",
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
    "snapshotId" : "{SNAPSHOT-ID}",
    "statusName" : "FINISHED",
    "timestamp" : {
      "date" : "2020-04-18T15:14:25Z",
      "increment" : 1
    }
  } ],
  "totalCount" : 1
}
```

**auto-oplog:**

```json
{
  "links" : [ {
    "href" : "https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0/groups/{PROJECT-ID}/clusters/{CLUSTER-ID}/restoreJobs?pretty=true&pageNum=1&itemsPerPage=100",
    "rel" : "self"
  } ],
  "results" : [ {
    "batchId": "{BATCH-ID}",
    "clusterId": "{CLUSTER-ID}",
    "created": "2018-09-20T15:01:00Z",
    "delivery": {
      "methodName": "HTTP",
      "statusName": "READY"
    },
    "encryptionEnabled": false,
    "groupId": "{PROJECT-ID}",
    "id": "{RESTORE-JOB-ID}",
    "links": [{
      "href": "https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0/groups/{PROJECT-ID}/clusters/{CLUSTER-NAME}/restoreJobs/{RESTORE-JOB-ID}",
      "rel": "self"
    }],
    "pointInTime": false,
    "snapshotId": "{SNAPSHOT-ID}",
    "statusName": "FINISHED",
    "timestamp": {
      "date": "2018-09-15T15:53:00Z",
      "increment": 1
    }
  } ],
  "totalCount" : 1
}
```

**auto-pit:**

```json
{
  "links" : [ {
    "href" : "https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0/groups/{PROJECT-ID}/clusters/{CLUSTER-ID}/restoreJobs?pretty=true&pageNum=1&itemsPerPage=100",
    "rel" : "self"
  } ],
  "results" : [ {
    "batchId": "{BATCH-ID}",
    "clusterId": "{CLUSTER-ID}",
    "created": "2018-09-20T15:02:00Z",
    "delivery": {
      "methodName": "HTTP",
      "statusName": "READY"
    },
    "encryptionEnabled": false,
    "groupId": "{PROJECT-ID}",
    "id": "{RESTORE-JOB-ID}",
    "links": [{
      "href": "https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0/groups/{PROJECT-ID}/clusters/{CLUSTER-NAME}/restoreJobs/{RESTORE-JOB-ID}",
      "rel": "self"
    }],
    "snapshotId": "{SNAPSHOT-ID}",
    "statusName": "FINISHED",
    "timestamp": {
      "date": "2018-09-15T15:53:00Z",
      "increment": 1
    }
  } ],
  "totalCount" : 1
}
```

**auto-checkpoint:**

```json
{
  "links" : [ {
    "href" : "https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0/groups/{PROJECT-ID}/clusters/{CLUSTER-ID}/restoreJobs?pretty=true&pageNum=1&itemsPerPage=100",
    "rel" : "self"
  } ],
  "results" : [ {
    "batchId": "{BATCH-ID}",
    "clusterId": "{CLUSTER-ID}",
    "created": "2018-09-20T15:03:00Z",
    "delivery": {
      "methodName": "HTTP",
      "statusName": "READY"
    },
    "encryptionEnabled": false,
    "groupId": "{PROJECT-ID}",
    "id": "{RESTORE-JOB-ID}",
    "links": [{
      "href": "https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0/groups/{PROJECT-ID}/clusters/{CLUSTER-NAME}/restoreJobs/{RESTORE-JOB-ID}",
      "rel": "self"
    }],
    "snapshotId": "{SNAPSHOT-ID}",
    "statusName": "FINISHED",
    "timestamp": {
      "date": "2018-09-15T15:53:00Z",
      "increment": 1
    }
  } ],
  "totalCount" : 1
}
```
