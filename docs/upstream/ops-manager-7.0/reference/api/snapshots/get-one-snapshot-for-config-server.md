<!-- Converted from reference/api/snapshots/get-one-snapshot-for-config-server.txt (reStructuredText). Includes are inlined. -->

# Get One Snapshot for One Config Server

**Important:** Deprecated when using MongoDB 3.4

As of MongoDB 3.4, mirrored config server deployments (also known
as SCCC (Sync Cluster Connection Config)) are no longer
supported. The following API method works with
SCCC (Sync Cluster Connection Config) config servers only.
Replica set config servers (also known as
CSRS (Config Server Replica Set)). use the
/reference/api/snapshots/get-one-snapshot-for-one-cluster
method. Config servers must be deployed as replica sets (also known as
CSRS (Config Server Replica Set)). For more information, see
replset-config-servers in the MongoDB Server Manual.

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

## Resource

```http
GET /groups/{PROJECT-ID}/hosts/{HOST-ID}/snapshots/{SNAPSHOT-ID}
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

This endpoint doesn't use HTTP request body parameters.

## Response

* - Name
  - Type
  - Description

* - clusterId
  - objectId
  - ID of the cluster the snapshot represents.

* - clusterName
  - string
  - Label that identifies the cluster.

* - complete
  - boolean
  - Indicator that the snapshot has been created. This is
    `false` if the snapshot creation job is still in progress.

* - created
  - document
  - The components of a timestamp.

* - created.date
  - timestamp
  - The exact point in time when the snapshot was taken in
    [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601?oldid=793821205)
    date and time format at UTC (Coordinated Universal Time).

* - created.increment
  - integer
  - The operation order in which this snapshot took place at
    this exact point in time. To learn how timestamps work in
    MongoDB, see document-bson-type-timestamp.

* - doNotDelete
  - boolean
  - Indicator that the snapshot cannot be deleted.

    If `doNotDelete` is set to `true`, any value in `expires`
    is ignored.

* - expires
  - timestamp
  - The date in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601?oldid=793821205) date
    and time format at UTC (Coordinated Universal Time) after
    which this snapshot can be deleted.

    If `doNotDelete` is set to `true`, any value in `expires`
    is removed.

    If the `expires` value is earlier than the current date and
    time, it can no longer be edited.

* - groupId
  - objectId
  - ID of the `project` that owns the snapshot.

* - id
  - objectId
  - ID of the snapshot.

* - lastOplogAppliedTimestamp
  - document
  - The components of the
    timestamp  of the last
    oplog entry was applied.

* - lastOplogAppliedTimestamp.date
  - timestamp
  - The exact point in time when the last oplog was applied
    in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601?oldid=793821205) date
    and time format at UTC (Coordinated Universal Time).

* - lastOplogAppliedTimestamp.increment
  - integer
  - The operation order in which last oplog was applied at
    this exact point in time. To learn how timestamps work in
    MongoDB, see document-bson-type-timestamp.

* - links
  - object array
  - .. include:: /includes/api/links-explanation.rst

* - namespaceFilterList
  - object array
  - The namespaces that are included or excluded
    from this snapshot.

* - namespaceFilterList.filterList
  - string array
  - A comma-separated list of any combination of databases or
    namespaces that are exclusively included or
    explicitly excluded from the snapshot.

    The default value is an empty array (`[]`).

* - namespaceFilterList.filterType
  - string
  - A value that determines how namespaces are
    filtered for this snapshot.

    - If this value is set to `blacklist`, namespaces in
      `namespaceFilterList.filterList` are excluded from the
      snapshot.
    - If this value is set to `whitelist`, only namespaces in
      `namespaceFilterList.filterList` are included in the
      snapshot.

    The default value is `blacklist`.

* - parts
  - object array
  - The individual parts that comprise the complete snapshot.
    This array contains a single document.

* - parts.completedTime
  - string
  - Date and time when the snapshot completed.

* - parts.dataSizeBytes
  - number
  - The total size of the data in the snapshot in bytes.

* - parts.encryptionEnabled
  - boolean
  - Indicator of the state of encryption of the snapshot
    data.

* - parts.fcv
  - string
  - Number that indicates the feature compatibility version of
    MongoDB that the replica set primary ran when MongoDB Cloud
    created the snapshot.

* - parts.fileSizeBytes
  - number
  - The total size of the data files in bytes.

* - parts.hostId
  - string
  - ID of a config server.

* - parts.machineId
  - string
  - Hostname and port that indicate the node on which MongoDB Cloud created the snapshot.

* - parts.masterKeyUUID
  - objectId
  - The KMIP (Key Management Interoperability Protocol)
    master key ID used to encrypt the snapshot data.
    `parts.masterKeyUUID` appears only if this snapshot has
    `parts.encryptionEnabled : true`.

* - parts.mongodVersion
  - string
  - The version of `mongod` that was running when the
    snapshot was created.

* - parts.replicaState
  - string
  - The node's role at the time when snapshot process began.

* - parts.storageSizeBytes
  - number
  - The total size of space allocated for document storage.

* - parts.typeName
  - string
  - The type of server that the part represents:

    - `CONFIG_SERVER`

## Example Request

```sh
curl --user "{PUBLIC-KEY}:{PRIVATE-KEY}" --digest \
 --header "Accept: application/json" \
 --include \
 --request GET "https://{opsManagerHost}:{port}/api/public/v1.0/groups/{PROJECT-ID}/hosts/{HOST-ID}/snapshots?pretty=true"
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
  "CLUSTER-ID" : "{CLUSTER-ID}",
  "complete" : true,
  "created" : {
    "date" : "2016-08-21T23:47:38Z",
    "increment" : 1
  },
  "doNotDelete" : false,
  "expires" : "2017-08-20T23:47:38Z",
  "GROUP-ID" : "{PROJECT-ID}",
  "HOST-ID" : "{HOST-ID}",
  "id" : "{SNAPSHOT-ID}",
  "lastOplogAppliedTimestamp" : {
    "date" : "2017-08-21T09:14:51Z",
    "increment" : 1
  },
  "links" : [ {
    "href" : "https://{opsManagerHost}:{port}/api/public/v1.0/groups/{PROJECT-ID}/hosts/{HOST-ID}/snapshots/{SNAPSHOT-ID}",
    "rel" : "self"
  } ],
  "namespaceFilterList" : {
    "filterList" : [ ],
    "filterType" : "blacklist"
  },
  "parts" : [ {
    "dataSizeBytes" : 503779557,
    "encryptionEnabled" : false,
    "fileSizeBytes" : 2855605344,
    "HOST-ID" : "{HOST-ID}",
    "mongodVersion" : "4.0.9",
    "storageSizeBytes" : 547516416,
    "typeName" : "REPLICA_SET"
  } ]
}
```
