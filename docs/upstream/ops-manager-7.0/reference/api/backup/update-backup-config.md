<!-- Converted from reference/api/backup/update-backup-config.txt (reStructuredText). Includes are inlined. -->

# Update One Backup Configuration

**Note:**

Groups and projects are synonymous terms. Your `{PROJECT-ID}` is the
same as your project id. For existing groups, your group/project id
remains the same. This page uses the more familiar term group when
referring to descriptions. The endpoint remains as stated in the
document.

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

## Resource

```http
PATCH /groups/{projectId}/backupConfigs/{clusterId}
```

## Request Parameters

### Request Path Parameters

| Path Parameter | Type | Necessity | Description |
|---|---|---|---|
| projectId | string | Required | Unique 24-hexadecimal digit string that identifies the project that holds the cluster with the backup configuration you want to change. |
| clusterId | string | Required | Unique 24-hexadecimal digit string that identifies the cluster whose backup configuration you want to change. |

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

* - authMechanismName
  - string
  - Conditional
  - Authentication mechanism needed to connect to the sync source
    database. Ops Manager requires this parameter if the sync store uses authentication. Ops Manager accepts:

    - `MONGODB_CR` (This covers SCRAM-SHA-1, SCRAM-SHA-256, and MONGODB-CR.)
    - `GSSAPI`
    - `PLAIN`
    - `MONGODB_X509`
    - `NONE`

* - encryptionEnabled
  - boolean
  - Optional
  - Flag that indicates if encryption is enabled for the backup
    configuration. You must include the **syncSource** parameter
    when enabling encryption for a backup configuration. For
    existing backups in a project, enabling encryption requires an
    `initial sync` to recreate the backups’ head databases.

    FCV `4.2` and later use 
    backup cursors instead of
    `head databases`. For
    more information, see backup-daemon.

    For more information on backup encryption for FCV 4.2 or 
    later, see encrypt-snapshots.

* - excludedNamespaces
  - array of strings
  - Conditional
  -

    **Note:**

    Ops Manager accepts this parameter for backup jobs running MongoDB
    FCV 4.0 or earlier. Ops Manager ignores this parameter when
    backing up MongoDB databases running FCV (Feature Compatibility Version) 4.2 or later.

    List of database and collection names to *omit* from the backup.
    Each string represents one namespace. Namespaces use the format
    of **{database}** or **{database}.{collection}**.

    This parameter must meet the following conditions:

    - Ops Manager accepts this parameter or **includedNamespaces**, not
      both.

    - Ops Manager requires the new full list of excluded namespaces,
      including any already found in the array.

      - If your new list *removes* any namespaces from the existing
        array, set the **syncSource** parameter.

        - Removing an excluded namespace requires a full resync.
        - Without the **syncSource** parameter, the request fails.

      - If your new list only *adds* to the existing array, don't
        set **syncSource**.

* - includedNamespaces
  - array of strings
  - Conditional
  -

    **Note:**

    Ops Manager accepts this parameter for backup jobs running MongoDB
    FCV 4.0 or earlier. Ops Manager ignores this parameter when
    backing up MongoDB databases running FCV (Feature Compatibility Version) 4.2 or later.

    List of database and collection names to *include* from the
    backup. Each string represents one namespace. Namespaces use the
    format of **{database}** or **{database}.{collection}**.

    This parameter must meet the following conditions:

    - Ops Manager accepts this parameter or **excludedNamespaces**, not
      both.

    - Ops Manager requires the new full list of included namespaces,
      including any already found in the array.

      - If the new list adds any namespaces from existing array,
        set the **syncSource** parameter.

        - Adding an included namespace requires a full resync.
        - Without the **syncSource** parameter, the request fails.

      - If the new list only removes namespaces from the existing
        array, don't set **syncSource**.

* - password
  - string
  - Conditional
  - Password to use to connect to the sync source database. Ops Manager
    requires this parameter when the sync store `mongod` instances
    require clients to authenticate.

* - preferredMember
  - string
  - Optional
  - .. include:: /includes/fact-preferred-member.rst

* - provisioned
  - boolean
  - Conditional
  - Flag that indicates if Ops Manager has provisioned the resources
    needed to store a backup.

* - sslEnabled
  - boolean
  - Optional
  - Flag that indicates if TLS (Transport Layer Security) is enabled for the sync source
    database.

* - statusName
  - string
  - Optional
  - Current (or desired) status of the backup configuration. Ops Manager
    accepts:

    - **INACTIVE**
    - **PROVISIONING**
    - **STARTED**
    - **STOPPED**
    - **TERMINATING**

* - storageEngineName
  - string
  - Optional
  - Storage engine used for the backup. Ops Manager accepts:

    - **MEMORY_MAPPED**
    - **WIRED_TIGER**

* - syncSource
  - string
  - Conditional
  - `mongod` instance from which you retrieve backup data. Ops Manager
    accepts either a specific hostname or one of: **PRIMARY** and
    **SECONDARY**.

    Ops Manager requires this parameter if
    **"storageEngineName" : "WIRED_TIGER"**.

* - username
  - string
  - Conditional
  - Name of the user to use to connect to the sync source database.
    Ops Manager requires this parameter when the sync store `mongod`
    instances require clients to authenticate.

    Send this parameter to Ops Manager when updating the backup
    configuration for a replica set or sharded cluster that Ops Manager
    *doesn't* manage.

## Response

| Name | Type | Description |
|---|---|---|
| authMechanismName | string | Name of the authentication mechanism to use when connecting to the sync source database. Ops Manager returns this parameter if the sync store uses authentication. |
| clusterId | string | Unique identifier of the cluster to which this backup configuration applies. |
| encryptionEnabled | boolean | Flag that indicates if encryption is enabled for the backup configuration. You must include the **syncSource** field when enabling encryption for a backup configuration. For existing backups in a project, enabling encryption requires an `initial sync` to recreate the backups’ head databases. FCV `4.2` and later use backup cursors instead of `head databases`. For more information, see backup-daemon. For more information on backup encryption for FCV 4.2 or later, see encrypt-snapshots. |
| excludedNamespaces | array of strings | List of database names and collection names to omit from the backup. Each string is a namespace in the form of **{database}** or **{database}.{collection}**. |
| includedNamespaces | array of strings | List of database names and collection names to include in the backup. Each string is a namespace in the form of **{database}** or **{database}.{collection}**. |
| preferredMember | string | .. include:: /includes/fact-preferred-member.rst |
| projectId | string | Unique identifier of the project that owns this backup configuration. |
| provisioned | boolean | Flag that indicates if Ops Manager has provisioned the resources needed to store a backup. Ops Manager returns this parameter when the amount of data to be backed up exceeds a certain threshold. |
| sslEnabled | boolean | Flag that indicates if TLS (Transport Layer Security) is enabled for the sync source database. |
| statusName | string | Current status of the backup configuration. |
| storageEngineName | string | Storage engine used for the backup. |

## Example Request

**basic:**

```sh
curl --user "{publicKey}:{privateKey}" --digest \
     --header "Accept: application/json" \
     --header "Content-Type: application/json" \
     --include --request PATCH "https://<OpsManagerHost>:<Port>/api/public/v1.0/groups/{projectId}/backupConfigs/{clusterId}" \
     --data '
       {
         "statusName": "STARTED",
         "storageEngineName": "WIRED_TIGER",
         "syncSource": "primary"
       }'
```

**members:**

When each snapshot starts, Ops Manager selects a replica set member
to run the snapshot. This automatically selected member should have the 
least performance impact on the replica set. You can override the 
default selection.

**Important:**

Use default selection whenever possible. This choice
ensures backup availability.

The following request sets the preferred member.

```sh
curl --user "{publicKey}:{privateKey}" --digest \
     --header "Accept: application/json" \
     --header "Content-Type: application/json" \
     --include --request PATCH "https://<OpsManagerHost>:<Port>/api/public/v1.0/groups/{projectId}/backupConfigs/{clusterId}" \
     --data '
       {
         "preferredMember":"{HOSTNAME}:{PORT}"
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

**basic:**

```json
{
  "authMechanismName" : "NONE",
  "clusterId" : "{clusterId}",
  "encryptionEnabled" : false,
  "excludedNamespaces" : [ ],
  "groupId" : "{projectId}",
  "links" : [ {
    "href" : "http://<OpsManagerHost>:<Port>/api/public/v1.0/groups/{projectId}/backupConfigs/{clusterId}",
    "rel" : "self"
   }, {
    "href" : "http://<OpsManagerHost>:<Port>/api/public/v1.0/groups/{projectId}/clusters/{clusterId}",
    "rel" : "http://mms.mongodb.com/cluster"
  }, {
    "href" : "http://<OpsManagerHost>:<Port>/api/public/v1.0/groups/{projectId}",
    "rel" : "http://mms.mongodb.com/group"
  }, {
    "href" : "http://<OpsManagerHost>:<Port>/api/public/v1.0/groups/{projectId}/backupConfigs/{clusterId}/snapshotSchedule",
    "rel" : "http://mms.mongodb.com/snapshotSchedule"
  } ],
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

The following response includes preferred member.

```json
{
  "authMechanismName" : "NONE",
  "clusterId" : "{clusterId}",
  "encryptionEnabled" : false,
  "excludedNamespaces" : [ ],
  "groupId" : "{projectId}",
  "links" : [ {
    "href" : "http://<OpsManagerHost>:<Port>/api/public/v1.0/groups/{projectId}/backupConfigs/{clusterId}",
    "rel" : "self"
   }, {
    "href" : "http://<OpsManagerHost>:<Port>/api/public/v1.0/groups/{projectId}/clusters/{clusterId}",
    "rel" : "http://mms.mongodb.com/cluster"
  }, {
    "href" : "http://<OpsManagerHost>:<Port>/api/public/v1.0/groups/{projectId}",
    "rel" : "http://mms.mongodb.com/group"
  }, {
    "href" : "http://<OpsManagerHost>:<Port>/api/public/v1.0/groups/{projectId}/backupConfigs/{clusterId}/snapshotSchedule",
    "rel" : "http://mms.mongodb.com/snapshotSchedule"
  } ],
  "sslEnabled" : false,
  "statusName" : "STARTED",
  "storageEngineName" : "WIRED_TIGER",
  "preferredMember":"{HOSTNAME}:{PORT}"
}
```
