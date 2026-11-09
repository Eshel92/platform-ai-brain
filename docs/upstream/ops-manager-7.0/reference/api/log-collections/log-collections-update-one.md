<!-- Converted from reference/api/log-collections/log-collections-update-one.txt (reStructuredText). Includes are inlined. -->

# Extend a Log Collection Job

**Note:**

Groups and projects are synonymous terms. Your `{PROJECT-ID}` is the
same as your project id. For existing groups, your group/project id
remains the same. This page uses the more familiar term group when
referring to descriptions. The endpoint remains as stated in the
document.

When you create a log collection job, Ops Manager starts a background job to
download the logs from the specified Ops Manager deployment. Each job is
created with a specified expiration date. Use this endpoint to extend
the expiration date of an existing log collection job.

You cannot extend the duration of log collection jobs which have already
expired.

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

## Resource

```http
PATCH /groups/{GROUP-ID}/logCollectionJobs/{JOB-ID}
```

### Request Path Parameters

| Name | Type | Necessity | Description |
|---|---|---|---|
| GROUP-ID | string | Required | Unique 24-hexadecimal digit string that identifies the log collection request job. |
| JOB-ID | string | Required | Unique 24-hexadecimal digit string that identifies the log collection job to retry. Use the /reference/api/log-collections/log-collections-get-all endpoint to obtain the IDs associated with your project. |

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
| expirationDate | string | Required | Timestamp, in the number of seconds that have elapsed since the [UNIX epoch](https://en.wikipedia.org/wiki/Unix_time?oldid=828172017) when this job expires. This can be up to 6 months from the time the job was created. You cannot specify a date which precedes the time the request is made. |

## Response

This endpoint doesn't return a response body.

## Example Request

```sh
curl --user "{PUBLIC-KEY}:{PRIVATE-KEY}" --digest \
     --header "Accept: application/json" \
     --header "Content-Type: application/json" \
     --include \
     --request PATCH "https://<OpsManagerHost>:<Port>/api/public/v1.0/groups/{GROUP-ID}/logCollectionJobs/{JOB-ID}?pretty=true" \
     --data '
      {
        "expirationDate": "2019-04-06T12:02:54Z"
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

This endpoint doesn't return a response body.
