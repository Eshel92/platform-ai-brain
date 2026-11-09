<!-- Converted from reference/api/admin/backup/daemonConfigs/create-one-backup-daemon-configuration.txt (reStructuredText). Includes are inlined. -->

# Create One Backup Daemon Configuration

Configures a new `Backup Daemon`.

**Note:**

Use this endpoint when you configure a `Backup Daemon` for the
first time. Ensure that the Backup Daemon process is running before
you configure it using this endpoint.

If you have already configured the Backup Daemon, update it using the
om-update-one-backup-daemon-config endpoint.

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0/admin/backup`

## Resource

```http
PUT /daemon/configs/{MACHINE}
```

### Request Path Parameters

| Name | Type | Necessity | Description |
|---|---|---|---|
| MACHINE | string | Required | Hostname or IP address of the machine that serves the Backup Daemon. |

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

* - `assignmentEnabled`
  - boolean
  - Optional
  - Flag indicating whether this `Backup Daemon` can be
    assigned backup jobs.

* - `backupJobsEnabled`
  - boolean
  - Optional
  - Flag indicating whether this `Backup Daemon` can be used
    to backup databases.

* - `configured`
  - boolean
  - Optional
  - Flag indicating whether this `Backup Daemon` is ready to
    use.

* - `garbageCollectionEnabled`
  - boolean
  - Optional
  - Flag indicating whether this `Backup Daemon` has garbage
    collection set.

* - `headDiskType`
  - string
  - Optional
  - Type of disk used to store the head directory.

    The accepted values for this option are:

    - `HDD`
    - `SSD`

* - `labels`
  - array of strings
  - Optional
  - Array of tags to manage which
    backup jobs Ops Manager can assign to which
    `Backup Daemons`.

    Setting these tags limits which backup jobs this Backup Daemon
    can process. If omitted, this Backup Daemon can only process
    backup jobs for projects that do not use labels to filter their
    jobs.

* - `machine`
  - object
  - Required
  - `Backup Daemon` host and its
    head directories.

* - `machine.headRootDirectory`
  - string
  - Optional
  - Root-relative path of the head directory on this
    `Backup Daemon` host. This directory must end with a slash
    (`/`). If you omit the slash, the Backup Daemon generates a
    Java Exception error.

* - `machine.machine`
  - string
  - Required
  - Hostname or IP address of the `Backup Daemon` host.

* - `numWorkers`
  - number
  - Optional
  - Number of worker processes that can perform tasks
    (i.e. backup, restore, or groom) for the `Backup Daemon`.

* - `resourceUsageEnabled`
  - boolean
  - Optional
  - Flag indicating whether this `Backup Daemon` has its
    resource usage monitored.

* - `restoreQueryableJobsEnabled`
  - boolean
  - Optional
  - Flag indicating whether this `Backup Daemon` can perform
    queryable restores.

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
     --header 'Content-Type: application/json' \
     --include \
     --request PUT 'https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0/admin/backup/daemon/configs/{MACHINE}/?pretty=true' \
     --data '{
       "assignmentEnabled" : true,
       "backupJobsEnabled" : false,
       "configured" : true,
       "garbageCollectionEnabled" : true,
       "headDiskType" : "SSD",
       "labels" : [ "l1", "l2" ],
       "machine" : {
         "headRootDirectory" : "/data/backup/",
         "machine" : "localhost"
       },
       "numWorkers" : 50,
       "resourceUsageEnabled" : true,
       "restoreQueryableJobsEnabled" : true
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
  "backupJobsEnabled" : false,
  "configured" : true,
  "garbageCollectionEnabled" : true,
  "headDiskType" : "SSD",
  "id" : "{BACKUP-DAEMON-ID}",
  "labels" : [ "l1", "l2" ],
  "links" : [ {
    "href" : "https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0/admin/backup/daemon/configs/{MACHINE}/<machine.headRootDirectory>",
    "rel" : "self"
  }],
  "machine" : {
    "headRootDirectory" : "/data/backup/",
    "machine" : "localhost"
  },
  "numWorkers" : 50,
  "resourceUsageEnabled" : true,
  "restoreQueryableJobsEnabled" : true
}
```
