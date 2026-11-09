<!-- Converted from reference/api/admin/backup/groups/update-one-backup-group-configuration.txt (reStructuredText). Includes are inlined. -->

# Update One Project Backup Jobs Configuration

Updates the configuration of one project's backup jobs.

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0/admin/backup`

## Resource

```http
PUT /groups/{PROJECT-ID}
```

### Request Path Parameters

| Name | Type | Description |
|---|---|---|
| PROJECT-ID | string | The unique identifier that represents this project and its backup job configuration. |

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

* - daemonFilter
  - object array
  - *Optional.* An array of pairs of `Backup Daemon` hosts and 
    their head directories that to which  
    this project's backup jobs are limited. If omitted, all available 
    Backup Daemons are used.

* - daemonFilter.headRootDirectory
  - string
  - *Optional.* The root-relative path of the head directory 
    on this `Backup Daemon` host.

* - daemonFilter.machine
  - string
  - The host address for one `Backup Daemon` host.

* - id
  - string
  - The unique identifier that represents this project and its 
    backup job configuration.

* - kmipClientCertPassword
  - string
  - *Optional.* The password that encrypts the 
    KMIP (Key Management Interoperability Protocol)
    client certificate.

* - kmipClientCertPath
  - string
  - *Optional.* The root-relative path on the `Backup Daemon` 
    host that stores the 
    KMIP (Key Management Interoperability Protocol)
    client certificate.

* - labelFilter
  - array of strings
  - *Optional.* An array of tags that limits which 
    `Backup Daemons` and 
    `snapshot stores` can process 
    backup jobs for this project.

    If a snapshot store or any Backup Daemon has the same `labels` 
    set as this `labelFilter`, they can process backup jobs for 
    this project.

    If omitted, the project's backup jobs can use any available 
    Backup Daemon or snapshot store.

* - oplogStoreFilter
  - array of objects
  - *Optional.* An array of unique identifiers representing 
    `Oplog stores` that may 
    be used with this project's backup jobs. If omitted, all 
    available oplog stores may be used.

* - oplogStoreFilter.id
  - string
  - Unique identifier representing an
    `oplog store` that may be used 
    with this project's backup jobs.

    Retrieve the `id` of the oplog store you want to use with 
    Get All Oplog Configurations.

* - oplogStoreFilter.type
  - string
  - Type of `oplog store` to use. The 
    only supported value is `oplogStore`.

* - snapshotStoreFilter
  - array of objects
  - *Optional.* Array of unique identifiers representing specific 
    `snapshot stores` and their types that can 
    be used with this project's backup jobs. If omitted, all 
    available snapshot stores are used.

* - snapshotStoreFilter.id
  - string
  - *Optional.* The unique identifier representing specific 
    `snapshot stores` that can be 
    used with this project's backup jobs.

* - snapshotStoreFilter.type
  - string
  - *Optional.* The type of the specific snapshot store given as 
    `snapshotStoreFilter.id`.

    The accepted values for this option are:

    - `s3blockstore`
    - `blockstore`
    - `fileSystemStore`

* - syncStoreFilter
  - array of strings
  - *Optional.* An array of sync store filters that can be used with 
    this project's backup jobs. If omitted, all available sync stores
    are used.

## Response

* - Name
  - Type
  - Description

* - daemonFilter
  - object array
  - An array of pairs of `Backup Daemon` hosts and 
    their head directories that to which  
    this project's backup jobs are limited.

* - daemonFilter.headRootDirectory
  - string
  - The root-relative path of the head directory on this 
    `Backup Daemon` host.

* - daemonFilter.machine
  - string
  - The host address for one `Backup Daemon` host.

* - id
  - string
  - The unique identifier that represents this project and its 
    backup job configuration.

* - kmipClientCertPassword
  - string
  - The password that encrypts the 
    KMIP (Key Management Interoperability Protocol)
    client certificate.

* - kmipClientCertPath
  - string
  - The path to the directory on the `Backup Daemon` host that 
    stores the KMIP (Key Management Interoperability Protocol) 
    client certificate.

* - links
  - object array
  - .. include:: /includes/api/links-explanation.rst

* - labelFilter
  - array of strings
  - An array of tags that limits which 
    `Backup Daemons` and 
    `snapshot stores` can process 
    backup jobs for this project.

* - oplogStoreFilter
  - array of objects
  - An array of unique identifiers representing 
    `Oplog stores` that may be used 
    with this project's backup jobs.

* - oplogStoreFilter.id
  - string
  - Unique identifier representing an
    `oplog store` that may be used 
    with this project's backup jobs.

* - oplogStoreFilter.type
  - string
  - Type of `oplog store` to use. This 
    value is always `oplogStore`.

* - snapshotStoreFilter
  - array of objects
  - Array of unique identifiers representing specific 
    `snapshot stores` and their types that can 
    be used with this project's backup jobs. If omitted, all 
    available snapshot stores are used.

* - snapshotStoreFilter.id
  - string
  - The unique identifier representing specific 
    `snapshot stores` that can be 
    used with this project's backup jobs.

* - snapshotStoreFilter.type
  - string
  - The type of the specific snapshot store given as 
    `snapshotStoreFilter.id`.

    The accepted values for this option are:

    - `s3blockstore`
    - `blockstore`
    - `fileSystemStore`

* - syncStoreFilter
  - array of strings
  - An array of sync store filters that can be used with this 
    project's backup jobs. If omitted, all available sync stores 
    are used.

## Example Request

```sh
curl --user '{PUBLIC-KEY}:{PRIVATE-KEY}' --digest \
 --header 'Accept: application/json' \
 --header 'Content-Type: application/json' \
 --include \
 --request PUT 'https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0/admin/backup/groups/{PROJECT-ID}?pretty=true' \
 --data '{
  "daemonFilter" : [ {
     "headRootDirectory" : "/data/backup",
     "machine" : "http://backup.example.com"
   } ],
   "id" : "{PROJECT-ID}",
   "kmipClientCertPassword" : "P4$$w0rD",
   "kmipClientCertPath" : "/certs/kmip",
   "labelFilter" : [ "label1", "label2" ],
   "oplogStoreFilter" : [ {
     "id" : "oplog1",
     "type" : "oplogStore"
   } ],
   "snapshotStoreFilter" : [ {
     "id" : "sPid",
     "type" : "s3blockstore"
   } ],
   "syncStoreFilter" : [ "s1", "s2" ]
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
  "daemonFilter" : [ {
    "headRootDirectory" : "/data/backup",
    "machine" : "http://backup.example.com"
  } ],
  "id" : "{PROJECT-ID}",
  "kmipClientCertPassword" : "P4$$w0rD",
  "kmipClientCertPath" : "/certs/kmip",
  "labelFilter" : [ "label1", "label2" ],
  "links" : [ {
    "href" : "https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0/admin/backup/groups/{PROJECT-ID}",
    "rel" : "self"
  }, {
    "href" : "https://{OPSMANAGER-HOST}:{PORT}/api/public/groups/{PROJECT-ID}",
    "rel" : "http://mms.mongodb.com/group"
  } ],
  "oplogStoreFilter" : [ {
    "id" : "oplog1",
    "type" : "oplogStore"
  } ],
  "snapshotStoreFilter" : [ {
    "id" : "sPid",
    "type" : "s3blockstore"
  } ],
  "syncStoreFilter" : [ "s1", "s2" ]
}
```
