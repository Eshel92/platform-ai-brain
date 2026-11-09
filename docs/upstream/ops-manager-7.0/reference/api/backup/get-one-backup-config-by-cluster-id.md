<!-- Converted from reference/api/backup/get-one-backup-config-by-cluster-id.txt (reStructuredText). Includes are inlined. -->

# Get One Backup Configuration from One Project

**Note:**

Groups and projects are synonymous terms. Your `{PROJECT-ID}` is the
same as your project id. For existing groups, your group/project id
remains the same. This page uses the more familiar term group when
referring to descriptions. The endpoint remains as stated in the
document.

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

## Resource

```http
GET /groups/{PROJECT-ID}/backupConfigs/{CLUSTER-ID}
```

## Request Parameters

### Request Path Parameters

| Parameter | Type | Necessity | Description |
|---|---|---|---|
| PROJECT-ID | string | Required | Unique 24-hexadecimal digit string that identifies the project that holds the cluster with the backup configuration you want to find. |
| CLUSTER-ID | string | Required | Unique 24-hexadecimal digit string that identifies the cluster whose backup configuration you want to find. |

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

* - `availableMembers`
  - string array
  - List of cluster members available for backup. Appears only 
    for member requests.

* - `clusterId`
  - string
  - Unique 24-hexadecimal digit string that identifies the 
    cluster to configure for backup.

* - `encryptionEnabled`
  - boolean
  - Flag that indicates whether encryption is enabled for the 
    backup configuration. You must include the `syncSource` 
    field when enabling encryption for a backup configuration. 
    For existing backups in a project, enabling encryption 
    requires an `initial sync` to recreate the backups’ 
    head databases.

    FCV `4.2` and later use 
    backup cursors instead of
    `head databases`. For
    more information, see backup-daemon.

    For more information on backup encryption for FCV 4.2 or 
    later, see encrypt-snapshots.

* - `excludedNamespaces`
  - string array
  - List of database names and collection names to omit from
    the backup. Each string is a namespace in the form of
    `{database}` or `{database}.{collection}`. If this field
    is present the `includedNamespaces` field cannot be
    present.

    You must send the new full list of excluded namespaces,
    including any that were already listed.

    If the new list removes any namespaces from the previous
    list, you must also set the `syncSource` field, as the
    removal of an excluded namespace necessitates a full resync.
    Without the `syncSource` field, the request will fail.

    If the new list only adds to the previous list, you do not
    need to set `syncSource`.

* - `groupId`
  - string
  - Unique 24-hexadecimal digit string that identifies the 
    project that owns this backup configuration.

* - `includedNamespaces`
  - string array
  - List of database names and collection names to include in
    the backup. Each string is a namespace in the form of
    `{database}` or `{database}.{collection}`. Any namespace
    **not listed** in this array **will not be backed up**. If
    this field is present the `excludedNamespaces` field cannot
    be present.

    You must send the new full list of included namespaces,
    including any that were already listed.

    If the new list adds any namespaces to the previous list, you
    must also set the `syncSource` field, as the addition of an
    included namespace necessitates a full resync. Without the
    `syncSource` field, the request will fail.

    If the new list only removes namespaces from the previous
    list, you do not need to set `syncSource`.

* - `links`
  - object array
  - .. include:: /includes/api/links-explanation.rst

* - `multiRegionBackupEnabled`
  - boolean 
  - Flag that indicates whether multi-region backup is enabled for the cluster.

* - `multiRegionMisconfigured`
  - boolean 
  - Flag that indicates whether multi-region backup, if enabled, is in
    `Misconfigured` state. The value can be one of the following: 

    - `true` - the status is `Misconfigured` and Ops Manager won't take
      any new snapshots although Ops Manager continues oplog tailing 
      uninterruptedly for the cluster members with assigned regions.
      You must select a deployment region for new cluster members for
      Ops Manager to resume taking new snapshots for all cluster members. 

    - `false` - the status is `Active`.

* - `preferredMember`
  - string
  - Cluster member manually designated as the preferred member 
    for backup. Appears only for member requests when the 
    preferred member is set with the UI or API.

* - `sslEnabled`
  - boolean
  - Flag that indentifies whether TLS (Transport Layer Security) is enabled for the sync 
    source database.

* - `statusName`
  - string
  - Current (or desired) status of the backup configuration.
    Possible values are:

    - `INACTIVE`
    - `PROVISIONING`
    - `STARTED`
    - `STOPPED`
    - `TERMINATING`

* - `storageEngineName`
  - string
  - Storage engine used for the backup. Possible values are:

    - `MEMORY_MAPPED`
    - `WIRED_TIGER`

## Example Request

**basic:**

```sh
curl --user "{PUBLIC-KEY}:{PRIVATE-KEY}" --digest \
     --header "Accept: application/json" \
     --include \
     --request GET "https://{opsManagerHost}:{port}/api/public/v1.0/groups/{PROJECT-ID}/backupConfigs/{CLUSTER-ID}"
```

**members:**

When each snapshot starts, Ops Manager selects a replica set member
to run the snapshot. This automatically selected member should have the 
least performance impact on the replica set. You can override the 
default selection.

**Important:**

Use default selection whenever possible. This choice
ensures backup availability.

The following request returns the available members.

```sh
curl --user "{PUBLIC-KEY}:{PRIVATE-KEY}" --digest \
     --header "Accept: application/json" \
     --include \
     --request GET "https://{opsManagerHost}:{port}/api/public/v1.0/groups/{PROJECT-ID}/backupConfigs/{CLUSTER-ID}/availableMembers?pretty=true"
```

### Example Response

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

**basic:**

```json
{
  "clusterId" : "{CLUSTER-ID}",
  "encryptionEnabled" : false,
  "excludedNamespaces" : [ ],
  "groupId" : "{PROJECT-ID}",
  "includedNamespaces" : [ ],
  "links" : [ ],
  "multiRegionBackupEnabled" : false,
  "multiRegionMisconfigured" : false,
  "sslEnabled" : false,
  "statusName" : "STARTED",
  "storageEngineName" : "WIRED_TIGER"
}
```

**members:**

When each snapshot starts, Ops Manager selects a replica set member
to run the snapshot. This automatically selected member should have the 
least performance impact on the replica set. You can override the 
default selection.

**Important:**

Use default selection whenever possible. This choice
ensures backup availability.

The following response includes the available members and the 
designated preferred member. If a preferred member is 
undefined, then it is excluded from the response.

```json
{
  "availableMembers" : [ "{HOSTNAME1}:{PORT1}", "{HOSTNAME2}:{PORT2}", "{HOSTNAME3}:{PORT3}"],
  "clusterId" : "{CLUSTER-ID}",
  "encryptionEnabled" : false,
  "excludedNamespaces" : [ ],
   "groupId" : "{PROJECT-ID}",
   "includedNamespaces" : [ ],
   "links" : [ ],
   "multiRegionBackupEnabled" : true,
   "multiRegionMisconfigured" : false,
   "sslEnabled" : false,
   "statusName" : "STARTED",
   "storageEngineName" : "WIRED_TIGER",
   "preferredMember" : "{HOSTNAME1}:{PORT1}"
 }
```
