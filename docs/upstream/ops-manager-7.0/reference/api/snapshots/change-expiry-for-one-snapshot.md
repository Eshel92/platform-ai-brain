<!-- Converted from reference/api/snapshots/change-expiry-for-one-snapshot.txt (reStructuredText). Includes are inlined. -->

# Change the Expiry of One Snapshot

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

## Resource

```http
PATCH /groups/{PROJECT-ID}/clusters/{CLUSTER-ID}/snapshots/{SNAPSHOT-ID}
```

## Request Parameters

### Request Path Parameters

| Name | Type | Description |
|---|---|---|
| PROJECT-ID | string | Unique identifier of the `project` that owns the snapshot. |
| CLUSTER-ID | string | Unique identifier of the cluster that the snapshot represents. |
| SNAPSHOT-ID | string | Unique identifier of the snapshot. |

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
  - Description

* - doNotDelete
  - boolean
  - Indicator that the snapshot cannot be deleted.

    **Important:**

    You cannot set `doNotDelete` to `true` *and* set a
    timestamp for `expires` in the same request. If you do,
    Ops Manager returns an error: ``Cannot modify snapshot because of
    invalid fields.``

* - expires
  - timestamp
  - The date in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601?oldid=793821205) date
    and time format at UTC (Coordinated Universal Time) after
    which this snapshot can be deleted.

    If `doNotDelete` is set to `true`, any existing value in
    `expires` is removed.

    If `expires` is set to a timestamp at or before the current
    date and time, Ops Manager deletes the snapshot at its next
    opportunity. There is no guarantee that the snapshot would be
    deleted immediately.

    If the current `expires` timestamp has already passed, it
    cannot be edited.

## Response

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

### `links` Array

The `links` array includes one or more links to sub-resources and/or
related resources. The relations between URLs are explained in the [Web Linking Specification](http://tools.ietf.org/html/rfc5988)

| Relation | Description |
|---|---|
| self | The URL endpoint for this resource. |

## Example Request

```sh
curl --user "{PUBLIC-KEY}:{PRIVATE-KEY}" --digest \
 --header "Accept: application/json" \
 --header "Content-Type: application/json" \
 --include \
 --request PATCH "https://{opsManagerHost}:{port}/api/public/v1.0/groups/{PROJECT-ID}/clusters/{CLUSTER-ID}/snapshots/{SNAPSHOT-ID}?pretty=true" \
 --data '
 {
   "doNotDelete": true
 }'
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
  "id" : "{SNAPSHOT-ID}",
  "CLUSTER-ID" : "{CLUSTER-ID}",
  "complete" : true,
  "created" : {
    "date" : "2014-07-09T15:24:37Z",
    "increment" : 1
  },
  "doNotDelete" : true,
  "GROUP-ID" : "{PROJECT-ID}",
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
    "CLUSTER-ID" : "{CLUSTER-ID}",
    "dataSizeBytes" : 17344,
    "fileSizeBytes" : 67108864,
    "mongodVersion" : "2.6.3",
    "replicaSetName" : "rs0",
    "storageSizeBytes" : 10502144,
    "typeName" : "REPLICA_SET"
  } ],
}
```
