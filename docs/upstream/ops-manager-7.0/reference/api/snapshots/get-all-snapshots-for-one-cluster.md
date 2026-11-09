<!-- Converted from reference/api/snapshots/get-all-snapshots-for-one-cluster.txt (reStructuredText). Includes are inlined. -->

# Get All Snapshots for One Cluster

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

## Resource

```http
GET /groups/{PROJECT-ID}/clusters/{CLUSTER-ID}/snapshots
```

## Request Parameters

### Request Path Parameters

| Name | Type | Description |
|---|---|---|
| PROJECT-ID | string | Unique identifier of the `project` that owns the snapshot. |
| CLUSTER-ID | string | Unique identifier of the cluster that the snapshot represents. |

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

Each **result** is one sync store.

* - `Name`
  - Type
  - Description

* - `clusterId`
  - string
  - Unique identifier of the cluster the snapshot
    represents.

* - `clusterName`
  - string
  - Label that identifies the cluster.

* - `complete`
  - boolean
  - Flag that indicates the snapshot has been created. This
    is `false` if the snapshot creation job is still in progress.

* - `created`
  - document
  - Components of a timestamp.

* - | `created`
    | `.date`
  - timestamp
  - iso8601-time when the snapshot was taken.

* - | `created`
    | `.increment`
  - integer
  - Operation order in which this snapshot took place at
    this exact point in time. To learn how timestamps work in
    MongoDB, see document-bson-type-timestamp.

* - `doNotDelete`
  - boolean
  - Flag that indicates the snapshot cannot be deleted.

* - `expires`
  - timestamp
  - Timestamp in ISO 8601 date and time format in UTC (Coordinated Universal Time) at UTC (Coordinated Universal Time) after which this snapshot can be
    deleted.

    If `doNotDelete` is set to `true`, any value in `expires`
    is removed.

    If the `expires` value is earlier than the current date and
    time, it cannot be edited.

* - `groupId`
  - string
  - Unique identifier of the `project` that owns the
    snapshot.

* - `id`
  - string
  - Unique identifier of the snapshot.

* - | `isPossibly`
    | `Inconsistent`
  - boolean
  - Flag that indicates the consistency of this snapshot. 
    `isPossiblyInconsistent` appears for
    sharded cluster snapshots only.

    To take a snapshot of a sharded cluster in a consistent
    state, the Backup temporarily turns off the
    balancer before creating the snapshot. In some cases, it
    cannot turn off the balancer in a timely manner. The snapshot is
    then created with the balancer still running.

    If this happens, the snapshot may be in an inconsistent state
    (e.g., chunk migrations may be in progress).

* - | `lastOplog`
    | `AppliedTimestamp`
  - document
  - Components of the
    timestamp  of the last
    oplog entry was applied.

* - | `lastOplog`
    | `AppliedTimestamp`
    | `.date`
  - timestamp
  - Timestamp in ISO 8601 date and time format in UTC (Coordinated Universal Time) at UTC (Coordinated Universal Time) when the last oplog was applied.

* - | `lastOplog`
    | `AppliedTimestamp`
    | `.increment`
  - integer
  - Operation order in which last oplog was applied at
    this exact point in time. To learn how timestamps work in
    MongoDB, see document-bson-type-timestamp.

* - `links`
  - object array
  - .. include:: /includes/api/links-explanation.rst

* - `namespaceFilterList`
  - object
  - namespaces that are included or excluded
    from this snapshot.

* - | `namespaceFilterList`
    | `.filterList`
  - string array
  - Comma-separated list of any combination of databases or
    namespaces that are exclusively included or
    explicitly excluded from the snapshot.

    The default value is an empty array (`[]`).

* - | `namespaceFilterList`
    | `.filterType`
  - string
  - Label that determines how namespaces are
    filtered for this snapshot.

    - If this value is set to `blacklist`, namespaces in
      `namespaceFilterList.filterList` are excluded from the
      snapshot.
    - If this value is set to `whitelist`, only namespaces in
      `namespaceFilterList.filterList` are included in the
      snapshot.

    The default value is `blacklist`.

* - `missingShards`
  - array of objects
  - List of shards that the snapshot is missing. `missingShards` appears for 
    sharded cluster snapshots only.

    In steady state, this array is empty. If the Backup cannot
    connect to a shard when a snapshot is created, the shard
    is omitted from the snapshot. Each document in the array
    is a **cluster** document containing a `self` link.

* - | `missingShards`
    | `.id`
  - string
  - Unique identifier of the missing shard.

* - | `missingShards`
    | `.groupId`
  - string
  - Unique identifier of the project that owns the missing
    shard.

* - | `missingShards`
    | `.typeName`
  - string
  - Type of server that the missing shard represents:

    - `CONFIG_SERVER_REPLICA_SET`
    - `REPLICA_SET`

* - | `missingShards`
    | `.clusterName`
  - string
  - Name of the cluster for the missing shard.

* - | `missingShards`
    | `.shardName`
  - string
  - Name of the missing shard.

* - | `missingShards`
    | `.replicaSetName`
  - string
  - Name of the replica set in the missing shard.

* - | `missingShards`
    | `.lastHeartbeat`
  - timestamp
  - Timestamp in ISO 8601 date and time format in UTC (Coordinated Universal Time) at UTC (Coordinated Universal Time) when the last heartbeat was received
    from the missing shard.

* - `parts`
  - array of objects
  - Individual parts that comprise the complete snapshot.

    - For a replica set, this array contains a single
      document.
    - For a sharded cluster, this array contains one
      document for each shard plus one document for the
      config server.

* - | `parts`
    | `.clusterId`
  - string
  - Unique identifier of the replica set.

* - | `parts`
    | `.completedTime`
  - string
  - Date and time when the snapshot completed.

* - | `parts`
    | `.compressionSetting`
  - string
  - Method of compression for the snapshot.

* - | `parts`
    | `.dataSizeBytes`
  - number
  - Total size of the data in the snapshot in bytes.

* - | `parts`
    | `.encryptionEnabled`
  - boolean
  - Indicator of the state of encryption of the snapshot
    data.

* - | `parts`
    | `.fcv`
  - string
  - Number that indicates the feature compatibility version of
    MongoDB that the replica set primary ran when MongoDB Cloud
    created the snapshot.

* - | `parts`
    | `.fileSizeBytes`
  - number
  - Total size of the data files in bytes.

* - | `parts`
    | `.machineId`
  - string
  - Hostname and port that indicate the node on which MongoDB Cloud created the snapshot.

* - | `parts`
    | `.masterKeyUUID`
  - string
  - KMIP (Key Management Interoperability) master key ID used to encrypt the snapshot data. 
    `parts.masterKeyUUID` appears only if this snapshot has
    `parts.encryptionEnabled : true`.

* - | `parts`
    | `.mongodVersion`
  - string
  - Version of `mongod` that the replica set
    primary was running when the snapshot was
    created.

* - | `parts`
    | `.replicaSetName`
  - string
  - Name of the replica set.

* - | `parts`
    | `.replicaState`
  - string
  - The node's role at the time when snapshot process began.

* - | `parts`
    | `.storageSizeBytes`
  - number
  - Total size of space allocated for document storage.

* - | `parts`
    | `.typeName`
  - string
  - Type of server that the part represents:

    - `REPLICA_SET`
    - `CONFIG_SERVER_REPLICA_SET`

## Example Request

```sh
curl --user "{PUBLIC-KEY}:{PRIVATE-KEY}" --digest \
 --header "Accept: application/json" \
 --include \
 --request GET "https://{opsManagerHost}:{port}/api/public/v1.0/groups/{PROJECT-ID}/clusters/{CLUSTER-ID}/snapshots?pretty=true"
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
  "links" : [ {
    "href" : "https://{opsManagerHost}:{port}/api/public/v1.0/groups/{PROJECT-ID}/clusters/{CLUSTER-ID}/snapshots?pretty=true&pageNum=1&itemsPerPage=100",
    "rel" : "self"
  } ],
  "results" : [ {
    "clusterId" : "{CLUSTER-ID}",
    "complete" : true,
    "created" : {
      "date" : "2016-08-21T23:47:38Z",
      "increment" : 1
    },
    "doNotDelete" : false,
    "expires" : "2017-08-20T23:47:38Z",
    "groupId" : "{PROJECT-ID}",
    "id" : "{SNAPSHOT-ID}",
    "lastOplogAppliedTimestamp" : {
      "date" : "2017-08-21T09:14:51Z",
      "increment" : 1
    },
    "links" : [ {
      "href" : "https://{opsManagerHost}:{port}/api/public/v1.0/groups/{PROJECT-ID}/clusters/{CLUSTER-ID}/snapshots/{SNAPSHOT-ID}",
      "rel" : "self"
    } ],
    "namespaceFilterList" : {
      "filterList" : [ ],
      "filterType" : "blacklist"
    },
    "parts" : [ {
      "clusterId" : "{CLUSTER-ID}",
      "compressionSetting" : "GZIP",
      "dataSizeBytes" : 503779557,
      "encryptionEnabled" : false,
      "fileSizeBytes" : 2855605344,
      "mongodVersion" : "4.0.9",
      "replicaSetName" : "proton",
      "storageSizeBytes" : 547516416,
      "typeName" : "REPLICA_SET"
    } ]
  }, {
  } ],
  "totalCount" : 28
}
```
