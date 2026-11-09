<!-- Converted from reference/api/admin/backup/daemonConfigs/get-one-backup-daemon-configuration-by-host.txt (reStructuredText). Includes are inlined. -->

# Get One Backup Daemon Configuration by ID

Retrieves the configuration of one backup daemon.

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0/admin/backup`

## Resource

```http
GET /daemon/configs/{MACHINE}/{HEAD-ROOT-DIRECTORY}
```

| Name | Type | Necessity | Description |
|---|---|---|---|
| MACHINE | string | Required | Hostname or IP address of the machine that serves the Backup Daemon. |
| HEAD-ROOT-DIRECTORY | string | Optional | Root-relative [URL-encoded path](https://en.wikipedia.org/wiki/Percent-encoding?oldid=810929127) of the head directory on this `Backup Daemon` host. May be omitted if the Backup Daemon has not been configured. |

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

* - `assignmentEnabled`
  - boolean
  - Flag indicating whether this `Backup Daemon` can be
    assigned backup jobs.

* - `backupJobsEnabled`
  - boolean
  - Flag indicating whether this `Backup Daemon` can be used
    to backup databases.

* - `configured`
  - boolean
  - Flag indicating whether this `Backup Daemon` is ready to
    use.

* - `garbageCollectionEnabled`
  - boolean
  - Flag indicating whether this `Backup Daemon` has garbage
    collection set.

* - `headDiskType`
  - string
  - Type of disk used to store the head directory.

    The accepted values for this option are:

    - `HDD`
    - `SSD`

* - `id`
  - string
  - Unique identifier of this `Backup Daemon`.

* - `labels`
  - array of strings
  - Array of tags to manage which backup jobs
    Ops Manager can assign to which
    `Backup Daemons`.

* - `links`
  - object array
  - .. include:: /includes/api/links-explanation.rst

* - `machine`
  - object
  - `Backup Daemon` host and its
    head directories.

* - `machine.headRootDirectory`
  - string
  - Root-relative path of the head directory on this
    `Backup Daemon` host.

* - `machine.machine`
  - string
  - Hostname or IP address of the `Backup Daemon` host.

* - `numWorkers`
  - number
  - Number of worker processes that can perform tasks (i.e.
    backup, restore, or groom) for the `Backup Daemon`.

* - `resourceUsageEnabled`
  - boolean
  - Flag indicating whether this `Backup Daemon` has its
    resource usage monitored.

* - `restoreQueryableJobsEnabled`
  - boolean
  - Flag indicating whether this `Backup Daemon` can perform
    queryable restores.

## Example Request

```sh
curl --user '{PUBLIC-KEY}:{PRIVATE-KEY}' --digest \ 
 --header 'Accept: application/json' \ 
 --include \ 
 --request GET 'https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0/admin/backup/daemon/configs/{MACHINE}/{HEAD-ROOT-DIRECTORY}?pretty=true' 
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
  "backupJobsEnabled" : false,
  "configured" : true,
  "garbageCollectionEnabled" : true,
  "headDiskType" : "SSD",
  "id" : "5991a422ad5df350005dd062",
  "labels" : [ "l1", "l2" ],
  "links" : [ {
    "href" : "https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0/admin/backup/daemon/configs/{MACHINE}/{HEAD-ROOT-DIRECTORY}",
    "rel" : "self"
  }],
  "machine" : {
    "headRootDirectory" : "/data/backup/",
    "machine" : "localhost"
  },
  "numWorkers" : 50,
  "resourceUsageEnabled" : true,
  "restoreJobsEnabled" : false,
  "restoreQueryableJobsEnabled" : true
}
```
