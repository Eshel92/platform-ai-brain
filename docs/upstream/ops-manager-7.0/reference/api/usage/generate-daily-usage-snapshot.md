<!-- Converted from reference/api/usage/generate-daily-usage-snapshot.txt (reStructuredText). Includes are inlined. -->

# Generate Daily Usage Snapshot

If `MongoDB Usage UI` is set to On, you can
trigger this endpoint which tells Ops Manager to:

- **Generate a snapshot.** This snapshot of all deployments belonging
  to all projects and organizations includes the current information
  for each `mongod` and `mongos` process:

  - memory statistics
  - date
  - organization
  - project
  - IP (Internet Protocol)
  - IANA (Internet Assigned Numbers Authority) port

- **Calculate assignments.** This populates the `assignment`
  collection. The endpoint makes Ops Manager review the snapshot for that
  day and copy each process with an assigned server type. Ops Manager
  discovers the process's server type from its host. The host's server
  type could have been set in the admin page. If the host's server type
  was not set, Ops Manager assigns the project's default server type when
  the host was created to that host.

You might call this endpoint if you have no assignments in the
`assignments` collection but want to view the MongoDB Usage Admin UI.
This may happen in the following cases:

1. You enabled `MongoDB Usage Data Collection` but the
   automated job that collects the data has yet run for the first time.
2. You dropped or emptied the `assignments` collection.
3. You did not enable `MongoDB Usage Data Collection` because
   you wanted to collect usage data one time, not every day.

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

## Required Role

This resource requires the
API Key to have
the `Global Owner` role.

## Resource

```http
POST /usage/dailyCapture
```

### Request Path Parameters

This endpoint doesn't use HTTP request path parameters.

### Request Query Parameters

The following query parameters are optional:

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

### Request Body Parameters

This endpoint doesn't use HTTP request body parameters.

## Response

This endpoint does not have response elements.

## Example Request

```sh
curl --user "{PUBLIC-KEY}:{PRIVATE-KEY}" --digest \
     --header "Accept: application/json" \
     --header "Content-Type: application/json" \
     --include \
     --request POST "https://<OpsManagerHost>:<Port>/api/public/v1.0/usage/dailyCapture?pretty=true"
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
