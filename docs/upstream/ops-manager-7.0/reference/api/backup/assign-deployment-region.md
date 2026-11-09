<!-- Converted from reference/api/backup/assign-deployment-region.txt (reStructuredText). Includes are inlined. -->

# Assign Deployment Region to One Shard

**Note:**

Groups and projects are synonymous terms. Your `{PROJECT-ID}` is the
same as your project id. For existing groups, your group/project id
remains the same. This page uses the more familiar term group when
referring to descriptions. The endpoint remains as stated in the
document.

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

## Resource

```http
PATCH /groups/{PROJECT-ID}/backupConfigs/{CLUSTER-ID}
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

| Name | Type | Necessity | Description |
|---|---|---|---|
| `deploymentConfigs` | array of objects | Required | Specification objects for the cluster members for which to assign deployment regions. |
| \| `deploymentConfigs` \| `.rsId` | string | Required | Replica set label that identifies the shard. |
| \| `deploymentConfigs` \| `.deploymentId` | string | Required | Unique identifier that references the deployment region to assign to the shard. |
| `multiRegionBackupEnabled` | boolean | Required | Flag that indicates whether multi-region backup is enabled for the cluster. |

## Response

* - Name
  - Type
  - Description

* - `authMechanismName`
  - string
  - Authentication mechanism needed to connect to the sync source
    database. Ops Manager requires this parameter if the sync store uses
    authentication. Ops Manager returns one of the following: 

    - `MONGODB_CR` (This covers SCRAM-SHA-1, SCRAM-SHA-256, and MONGODB-CR.)
    - `GSSAPI`
    - `PLAIN`
    - `MONGODB_X509`
    - `NONE`

* - `clusterId`
  - string
  - Unique 24-hexadecimal digit string that identifies the 
    cluster that is configured for backup.

* - `encryptionEnabled`
  - boolean
  - Flag that indicates whether encryption is enabled for the 
    backup configuration. 

* - `excludedNamespaces`
  - array of strings
  - List of database names and collection names omitted from
    the backup. Each string specifies a namespace of the form
    `{database}` or `{database}.{collection}`.

* - `groupId`
  - string
  - Unique 24-hexadecimal digit string that identifies the 
    project that owns this backup configuration.

* - `includedNamespaces`
  - string array
  - List of database names and collection names included in
    the backup. Each string specifies a namespace of the form 
    `{database}` or `{database}.{collection}`. Any namespace
    **not listed** in this array **is not to be backed up**. 

* - `links`
  - object array
  - .. include:: /includes/api/links-explanation.rst

* - `multiRegionBackupEnabled`
  - boolean 
  - Flag that indicates whether multi-region backup is enabled for the cluster.

* - `multiRegionMisconfigured`
  - boolean 
  - Flag that indicates whether multi-region backup, if enabled, is in
    the `Misconfigured` state. The value can be one of the following: 

    - `true` - the status is `Misconfigured` and Ops Manager won't take
      any new snapshots although Ops Manager continues oplog tailing 
      uninterrupted for the cluster members with assigned regions.
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
  - Flag that indicates whether TLS (Transport Layer Security) is enabled for the sync 
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

```sh
curl --user "{publicKey}:{privateKey}" --digest \
     --header "Accept: application/json" \
     --include \
     --request PATCH "https://{opsManagerHost}:{port}/api/public/v1.0/admin/backup/backupDeployments/?pretty=true"
     --data '
       {
         "multiRegionBackupEnabled" : true,
         "deploymentConfigs": [
           {"rsId":"myShard_2", "deploymentId":"NY_NJ"},
         ]
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
  "authMechanismName" : "NONE",
  "clusterId" : "{CLUSTER-ID}",
  "encryptionEnabled" : false,
  "excludedNamespaces" : [ ],
  "groupId" : "{PROJECT-ID}",
  "links" : [ ],
  "multiRegionBackupEnabled" : true,
  "multiRegionMisconfigured" : false,
  "sslEnabled" : false,
  "statusName" : "STARTED",
  "storageEngineName" : "WIRED_TIGER"
}
```
