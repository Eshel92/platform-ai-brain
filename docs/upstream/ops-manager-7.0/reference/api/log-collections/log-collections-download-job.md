<!-- Converted from reference/api/log-collections/log-collections-download-job.txt (reStructuredText). Includes are inlined. -->

# Download Logs from a Log Collection Job

**Note:**

Groups and projects are synonymous terms. Your `{PROJECT-ID}` is the
same as your project id. For existing groups, your group/project id
remains the same. This page uses the more familiar term group when
referring to descriptions. The endpoint remains as stated in the
document.

When you create a log collection job, Ops Manager starts a background job to
download the logs from the specified Ops Manager deployment.  Use this
endpoint to download a `.tar.gz` file stream for all logs associated
with the specified job.

You can download logs from both successful and failed log collection
jobs. If the job failed, all successful components are downloaded. The
logs are downloaded to the same directory where the request is
executed, and in the same format used when downloading logs through the
Ops Manager UI.

**Example:**

```sh
hostname/
    automation_agent/
        Automation-agent-verbose.log.2019-01-...
    mongos/
        ...
    myShard_1/
        27017/
            ...
        27018/
...
```

You cannot download logs from jobs in the `EXPIRED` or
`IN_PROGRESS` states.

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

## Resource

```http
GET /groups/{GROUP-ID}/logCollectionJobs/{JOB-ID}/download
```

### Request Path Parameters

| Name | Type | Necessity | Description |
|---|---|---|---|
| GROUP-ID | string | Required | Unique 24-hexadecimal digit string that identifies the log collection request job. |
| JOB-ID | string | Required | Unique identifier of the job for which to download the logs. You can obtain the `JOB-IDs` associated with your project by using the /reference/api/log-collections/log-collections-get-all endpoint. |

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

This endpoint does not have response elements.

## Example Request

```sh
curl --user "{username}:{apiKey}" --digest
     --header "Accept: application/json"
     --header "Accept: application/gzip"
     --output logs.tar.gz
     --request GET "https://<OpsManagerHost>:<Port>/api/public/v1.0/groups/{GROUP-ID}/logCollectionJobs/{JOB-ID}/download"
```

**Note:**

If you're using cURL to make requests, you must include the 
`--output` option and specify a file name to store
your logs.

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

This endpoint doesn't return a response body.
