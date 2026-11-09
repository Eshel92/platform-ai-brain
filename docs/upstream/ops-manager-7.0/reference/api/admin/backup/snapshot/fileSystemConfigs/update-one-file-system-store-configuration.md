<!-- Converted from reference/api/admin/backup/snapshot/fileSystemConfigs/update-one-file-system-store-configuration.txt (reStructuredText). Includes are inlined. -->

# Update One File System Store Configuration

Updates the configuration of one file system store.

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0/admin/backup`

## Resource

```http
PUT /snapshot/fileSystemConfigs/{FILE-SYSTEM-CONFIG-ID}
```

### Request Path Parameters

| Path Parameter | Type | Necessity | Description |
|---|---|---|---|
| FILE-SYSTEM-CONFIG-ID | string | Required | Unique identifier that labels this file system store configuration. |

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

| Body Parameter | Type | Necessity | Description |
|---|---|---|---|
| assignmentEnabled | boolean | Optional | Flag that indicates whether this file system store can be assigned backup jobs. |
| labels | array of strings | Optional | Tags to manage which backup jobs Ops Manager can assign to which `file system stores`. Setting these tags limits which backup jobs this file system store can process. If omitted, this file system store can only process backup jobs for projects that do not use labels to filter their jobs. |
| loadFactor | number | Optional | Positive, non-zero integer that expresses how much backup work this `snapshot store` should perform compared to another snapshot store. Set this option only if you're using more than one snapshot store. To learn more about Load Factor, see Edit One Existing Blockstore. |
| mmapv1CompressionSetting | string | Optional | Compression setting if you use the MMAPv1 storage engine for your snaphots. Ops Manager accepts `NONE` or `GZIP`. Ops Manager sets this value to `NONE` by default. If the MongoDB runs FCV 4.2 or later, Ops Manager ignores this setting. IMPORTANT: MongoDB removed support for the MMAPv1 storage engine in MongoDB 4.2. If you edit your deployment's configuration to change your storage engine to storage-wiredtiger, Ops Manager restarts the MongoDB processes. |
| storePath | string | Required | Location where file system-based backups are stored on the file system store host. |
| wtCompressionSetting | string | Optional | Compression setting if you use the WiredTiger storage engine for your snaphots. Ops Manager accepts `NONE` or `GZIP`. Ops Manager sets this value to `GZIP` by default. If the MongoDB runs FCV 4.2 or later, Ops Manager ignores this setting. |

## Response

| Name | Type | Description |
|---|---|---|
| assignmentEnabled | boolean | Flag that indicates whether this file system store can be assigned backup jobs. |
| id | string | Unique identifier of this file system store. |
| labels | array of strings | Tags that manage which backup jobs Ops Manager can assign to which `file system stores`. |
| links | array of objects | .. include:: /includes/api/links-explanation.rst |
| loadFactor | number | Positive, non-zero integer that expresses how much backup work this `snapshot store` should perform compared to another snapshot store. Set this option only if you're using more than one snapshot store. To learn more about Load Factor, see Edit One Existing Blockstore. |
| mmapv1CompressionSetting | string | Compression setting if you use the MMAPv1 storage engine for your snaphots. Ops Manager may return `NONE` or `GZIP`. If the MongoDB runs FCV 4.2 or later, Ops Manager ignores this setting. IMPORTANT: MongoDB removed support for the MMAPv1 storage engine in MongoDB 4.2. If you edit your deployment's configuration to change your storage engine to storage-wiredtiger, Ops Manager restarts the MongoDB processes. |
| storePath | string | System root-relative directory path where file system-based backups are stored on the file system store host. |
| wtCompressionSetting | string | Compression setting if you use the WiredTiger storage engine for your snaphots. Ops Manager may return `NONE` or `GZIP`. If the MongoDB runs FCV 4.2 or later, Ops Manager ignores this setting. |

## Example Request

```sh
curl --user '{PUBLIC-KEY}:{PRIVATE-KEY}' --digest \
     --header 'Accept: application/json' \
     --header 'Content-Type: application/json' \
     --include \
     --request PUT 'https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0/admin/backup/snapshot/fileSystemConfigs/{FILE-SYSTEM-CONFIG-ID}?pretty=true' \
     --data '{
       "assignmentEnabled" : true,
       "labels" : [ "l1", "l2" ],
       "loadFactor" : 50,
       "mmapv1CompressionSetting" : "NONE",
       "storePath" : "/data/backup",
       "wtCompressionSetting" : "GZIP"
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
  "assignmentEnabled" : true,
  "id" : "{FILE-SYSTEM-STORE-CONFIG-ID}",
  "labels" : [ "l1", "l2" ],
  "links" : [ {
    "href" : "https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0/admin/backup/snapshot/fileSystemConfigs/{FILE-SYSTEM-CONFIG-ID}",
    "rel" : "self"
  }],
  "loadFactor" : 50,
  "mmapv1CompressionSetting" : "NONE",
  "storePath" : "/data/backup",
  "wtCompressionSetting" : "GZIP"
}
```
