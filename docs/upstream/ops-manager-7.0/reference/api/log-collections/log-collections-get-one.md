<!-- Converted from reference/api/log-collections/log-collections-get-one.txt (reStructuredText). Includes are inlined. -->

# Get One Log Collection Job

**Note:**

Groups and projects are synonymous terms. Your `{PROJECT-ID}` is the
same as your project id. For existing groups, your group/project id
remains the same. This page uses the more familiar term group when
referring to descriptions. The endpoint remains as stated in the
document.

When you create a log collection job, Ops Manager starts a background job to
download the logs from the specified Ops Manager deployment.  Use this
endpoint to retrieve a single log collection job by its unique
identifier.

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

## Resource

```http
GET /groups/{GROUP-ID}/logCollectionJobs/{JOB-ID}
```

### Request Path Parameters

| Name | Type | Necessity | Description |
|---|---|---|---|
| GROUP-ID | string | Required | Unique 24-hexadecimal digit string that identifies the log collection request job. |
| JOB-ID | string | Required | Unique 24-hexadecimal digit string that identifies the log collection job to retry. Use the /reference/api/log-collections/log-collections-get-all endpoint to obtain the IDs associated with your project. |

### Request Query Parameters

* - Name
  - Type
  - Description
  - Default

* - pageNum
  - integer
  - Page number (1-index based).
  - `1`

* - itemsPerPage
  - integer
  - Number of items to return per page, up to a maximum of 500.
  - `100`

* - pretty
  - boolean
  - Indicates whether the response body should be in a
    prettyprint format.
  - `false`

* - envelope
  - boolean
  - Indicates whether or not to wrap the response in an envelope.

    Some API (Application Programming Interface) clients cannot access the HTTP (Hypertext Transfer Protocol) response headers or
    status code. To remediate this, set `"envelope" : true` in the
    query.

    For endpoints that return one result, response body
    includes:

    | status | HTTP (Hypertext Transfer Protocol) response code |
    |---|---|
    | envelope | Expected response body |

    For endpoints that return a list of results, the `results`
    object is an envelope. Ops Manager adds the `status` field to the
    response body.
  - None

|  |  |  |  |
|---|---|---|---|
| verbose | Boolean | If true, returns all child jobs in the response. A log collection job contains child jobs for each log type and MongoDB process included in the request. | `false` |

### Request Body Parameters

This endpoint doesn't use HTTP request body parameters.

## Response

* - Name
  - Type
  - Description

* - childJobs
  - array
  - List of child jobs associated with this request. Included in the
    response if you set tthe **verbose** query parameter to
    `true`.

* - childJobs[n].errorMessage
  - string
  - Error message showing why this child job failed, if applicable.

* - childJobs[n].finishDate
  - string
  - Timestamp in ISO 8601 date and time format in UTC (Coordinated Universal Time) when this child job finished.

* - childJobs[n].hostName
  - string
  - Name of the host from whom the child job collects the logs.

* - childJobs[n].logCollectionType
  - string
  - Type of log this child job collects. Returns one of the
    following values:

    - `AUTOMATION_AGENT`
    - `BACKUP_AGENT`
    - `MONITORING_AGENT`
    - `MONGODB`
    - `FTDC`

* - childJobs[n].path
  - string
  - Path to the process in the deployment for which this child job
    collects logs. MongoDB Atlas uses these paths to build the directory
    hierarchy in the compressed archive file.

    | logCollectionType | Path |
    |---|---|
    | AUTOMATION_AGENT | `<hostname>/automation_agent` |
    | BACKUP_AGENT | `<hostname>/automation_agent` |
    | MONITORING_AGENT | `<hostname>/automation_agent` |
    | MONGODB | `<hostname>/<port>/<mongodb>` |
    | FTDC | `<hostname>/<port>/<ftdc>` |

* - childJobs[n].startDate
  - string
  - Timestamp in ISO 8601 date and time format in UTC (Coordinated Universal Time) when this child job started.

* - childJobs[n].status
  - string
  - Status of this child job. This resource returns one of the
    following values:

    - `SUCCESS`
    - `FAILURE`
    - `IN_PROGRESS`
    - `MARKED_FOR_EXPIRY`
    - `EXPIRED`

* - childJobs[n].uncompressedDiskSpaceBytes
  - number
  - Total uncompressed disk space in bytes that this child job uses.

* - creationDate
  - string
  - Timestamp, in the number of seconds that have elapsed since the [UNIX epoch](https://en.wikipedia.org/wiki/Unix_time?oldid=828172017) when you created the log collection request job.

* - expirationDate
  - string
  - Timestamp, in the number of seconds that have elapsed since the [UNIX epoch](https://en.wikipedia.org/wiki/Unix_time?oldid=828172017) when the log collection request job expires.

* - groupId
  - string
  - Unique 24-hexadecimal digit string that identifies the
    `project` associated with log collection request.

* - id
  - string
  - Unique 24-hexadecimal digit string that identifies the log
    collection request job.

* - logTypes
  - array
  - List of log types included in this request. This resource
    returns one or more of the following values:

    - `AUTOMATION_AGENT`
    - `BACKUP_AGENT`
    - `MONITORING_AGENT`
    - `MONGODB`
    - `FTDC`

* - redacted
  - boolean
  - Flag that indicates whether the request replaces emails,
    hostnames, IP addresses, and namespaces in the response with
    random string values.

* - resourceName
  - string
  - Name of the resource for which you requested logs.

* - resourceType
  - string
  - Type of resource for which you requested logs. This resource
    returns one of the following values:

    - `CLUSTER`
    - `PROCESS`
    - `REPLICA_SET`

* - rootResourceName
  - string
  - Name of the complete deployment if you made the log request to a
    part of a deployment. Part of the deployment could be a replica
    set in a cluster or one shard of a sharded cluster.

* - rootResourceType
  - string
  - Type of the part of the complete deployment if you made the log
    request to a part of a deployment. Part of the deployment could
    be a replica set in a cluster or one shard of a sharded cluster.
    This resource returns one of the following values:

    - `CLUSTER`
    - `PROCESS`
    - `REPLICA_SET`

* - status
  - string
  - Status of the log collection request job. This resource returns
    one of the following values:

    - `SUCCESS`
    - `FAILURE`
    - `IN_PROGRESS`
    - `MARKED_FOR_EXPIRY`
    - `EXPIRED`

* - sizeRequestedPerFileBytes
  - number
  - Size for each log file in bytes.

* - uncompressedSizeTotalBytes
  - number
  - Total uncompressed size of the log data in bytes that this
    request returns.

* - userId
  - string
  - Unique 24-hexadecimal digit string that identifies the user
    executing the request.

* - downloadUrl
  - string
  - Internet address from which you download the logs from this
    request.

## Example Request

```sh
curl --user "{PUBLIC-KEY}:{PRIVATE-KEY}" --digest \
     --header "Accept: application/json" \
     --include \
     --request GET "https://<OpsManagerHost>:<Port>/api/public/v1.0/groups/{GROUP-ID}/logCollectionJobs/{JOB-ID}?verbose=true&pretty=true"
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
  "childJobs": [
    {
      "automationAgentId": "5c81086e014b76a3d85e1123",
      "errorMessage": null,
      "finishDate": "2019-03-07T12:02:57Z",
      "hostName": "server1.example.com",
      "logCollectionType": "AUTOMATION_AGENT",
      "path": "server1.example.com/automation_agent",
      "startDate": "2019-03-07T12:02:54Z",
      "status": "SUCCESS",
      "uncompressedDiskSpaceBytes": 12827
    },
    {
      "automationAgentId": "5c81086e014b76a3d85e1117",
      "errorMessage": null,
      "finishDate": "2019-03-07T12:02:57Z",
      "hostName": "server1.example.com:27027",
      "logCollectionType": "MONGODB",
      "path": "server1.example.com/27027/mongodb",
      "startDate": "2019-03-07T12:02:54Z",
      "status": "SUCCESS",
      "uncompressedDiskSpaceBytes": 9292
    },
    ...
  ],
  "creationDate": "2019-03-07T12:02:54Z",
  "downloadUrl": "https://<OpsManagerHost>:<Port>/api/public/v1.0/groups/{GROUP-ID}/logCollectionJobs/5c81086e014b76a3d85e1113/download",
  "expirationDate": "2019-05-06T12:02:54Z",
  "groupId": "5c8100bcf2a30b12ff88258f",
  "id": "5c81086e014b76a3d85e1113",
  "logTypes": [
    "AUTOMATION_AGENT",
    "MONGODB",
    "FTDC"
  ],
  "redacted": false,
  "resourceName": "myReplicaSet",
  "resourceType": "replicaset",
  "rootResourceName": "myReplicaSet",
  "rootResourceType": "replicaset",
  "sizeRequestedPerFileBytes": 1000,
  "status": "IN_PROGRESS",
  "uncompressedSizeTotalBytes": 44518,
  "userId": "5c80f75fcf09a246878f67a4"
}
```
