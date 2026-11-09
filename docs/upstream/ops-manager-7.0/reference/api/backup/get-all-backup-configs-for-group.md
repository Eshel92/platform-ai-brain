<!-- Converted from reference/api/backup/get-all-backup-configs-for-group.txt (reStructuredText). Includes are inlined. -->

# Get All Backup Configurations for One Project

**Note:**

Groups and projects are synonymous terms. Your `{PROJECT-ID}` is the
same as your project id. For existing groups, your group/project id
remains the same. This page uses the more familiar term group when
referring to descriptions. The endpoint remains as stated in the
document.

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

## Resource

```http
GET /groups/{PROJECT-ID}/backupConfigs
```

## Request Parameters

### Request Path Parameters

| Name | Type | Necessity | Description |
|---|---|---|---|
| PROJECT-ID | string | Required | Unique 24-hexadecimal digit string that identifies the project to which the backup configuration applies. |

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

* - Name
  - Type
  - Description

* - groupId
  - string
  - Unique 24-hexadecimal digit string that identifies the 
    project that owns this backup configuration.

* - clusterId
  - string
  - Unique 24-hexadecimal digit string that identifies the cluster 
    whose backup configuration you want to find.

* - statusName
  - string
  - Current (or desired) status of the backup configuration. 
    Possible values are:

    - `INACTIVE`
    - `PROVISIONING`
    - `STARTED`
    - `STOPPED`
    - `TERMINATING`

* - storageEngineName
  - string
  - Storage engine used for the backup. Possible values are:

    - `MEMORY_MAPPED`
    - `WIRED_TIGER`

|  |  |  |
|---|---|---|
| encryptionEnabled | boolean | Flag that indicates whether encryption is enabled for the backup configuration. You must include the `syncSource` field when enabling encryption for a backup configuration. For existing backups in a project, enabling encryption requires an `initial sync` to recreate the backups’ head databases. FCV `4.2` and later use backup cursors instead of `head databases`. For more information, see backup-daemon. For more information on backup encryption for FCV 4.2 or later, see encrypt-snapshots. |

|  |  |  |
|---|---|---|
| sslEnabled | boolean | Flag that indicates whether TLS (Transport Layer Security) is enabled for the sync source database. |
| excludedNamespaces | string array | List of database names and collection names to omit from the backup. Each string is a namespace in the form of `<database>` or `<database>.<collection>`. If this field is present the `includedNamespaces` field cannot be present. You must send the new full list of excluded namespaces, including any that were already listed. If the new list removes any namespaces from the previous list, you must also set the `syncSource` field, as the removal of an excluded namespace necessitates a full resync. Without the `syncSource` field, the request will fail. If the new list only adds to the previous list, you do not need to set `syncSource`. |
| includedNamespaces | string array | List of database names and collection names to include in the backup. Each string is a namespace in the form of `<database>` or `<database>.<collection>`. Any namespace **not listed** in this array **will not be backed up**. If this field is present the `excludedNamespaces` field cannot be present. You must send the new full list of included namespaces, including any that were already listed. If the new list adds any namespaces to the previous list, you must also set the `syncSource` field, as the addition of an included namespace necessitates a full resync. Without the `syncSource` field, the request will fail. If the new list only removes namespaces from the previous list, you do not need to set `syncSource`. |

## Example Request

```sh
curl --user "{PUBLIC-KEY}:{PRIVATE-KEY}" --digest \
     --header "Accept: application/json" \
     --include \
     --request GET "https://{opsManagerHost}:{port}/api/public/v1.0/groups/{PROJECT-ID}/backupConfigs"
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

```json
{
  "totalCount" : 3,
  "results" : [ {
    "groupId" : "{PROJECT-ID}",
    "clusterId" : "{CLUSTER-ID1}",
    "statusName" : "STARTED",
    "storageEngineName" : "WIRED_TIGER",
    "sslEnabled" : false,
    "excludedNamespaces" : [ ],
    "includedNamespaces" : [ ],
    "links" : [ ]
  }, {
    "groupId" : "{PROJECT-ID}",
    "clusterId" : "{CLUSTER-ID2}",
    "statusName" : "STARTED",
    "storageEngineName" : "MEMORY_MAPPED",
    "sslEnabled" : false,
    "excludedNamespaces" : [ ],
    "includedNamespaces" : [ ],
    "links" : [ ]
  }, {
    "groupId" : "{PROJECT-ID}",
    "clusterId" : "{CLUSTER-ID3}",
    "statusName" : "STOPPED",
    "storageEngineName" : "WIRED_TIGER",
    "sslEnabled" : false,
    "excludedNamespaces" : [ ],
    "includedNamespaces" : [ ],
    "links" : [ ]
  } ],
  "links" : [ ]
}
```
