<!-- Converted from reference/api/performance-advisor/get-slow-queries.txt (reStructuredText). Includes are inlined. -->

# Get Slow Query Logs

Retrieves log lines for slow queries as determined by the
Performance Advisor.

**Note:**

Performance Advisor users must have the necessary access
privileges to view performance
data. Users who do not have the necessary permissions will not be
able to view any log data in the `slowQueryLogs` API endpoint
responses.

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

## Resource

```http
GET /groups/{PROJECT-ID}/hosts/{HOST-ID}/performanceAdvisor/slowQueryLogs
```

### Request Path Parameters

| Parameter | Type | Description |
|---|---|---|
| PROJECT-ID | string | *(Required.)* Unique identifier of the project that owns this MongoDB process. |
| HOST-ID | string | *(Required.)* Unique identifier of the host for the MongoDB process. |

### Request Query Parameters

All parameters are optional.

* - pretty
  - boolean
  - Indicates whether the response body should be in a
    [prettyprint](https://en.wikipedia.org/wiki/Prettyprint?oldid=791126873) format.
  - `false`

* - envelope
  - boolean
  - Indicates whether or not to wrap the response in an
    envelope.
  - `false`

* - since
  - long
  - Point in time from which to retrieve slow query logs,
    stated in [milliseconds since epoch](https://currentmillis.com/).
  - previous 24 hours

* - duration
  - long
  - Length of time in milliseconds during which to find
    slow query logs among the managed namespaces in the cluster.
  - up to the present time

* - namespaces
  - string
  - Namespaces from which to retrieve suggested slow query logs.
    A namespace consists of the database and collection resource
    separated by a `.`, such as `<database>.<collection>`.

    To specify multiple namespaces, pass the parameter multiple times
    using an ampersand (`&`) as a delimiter, once for each
    namespace.

    For example:

    ```
    ?namespaces=data.stocks&namespaces=data.zips&pretty=true
    ```

  - all

* - nLogs
  - long
  - Maximum number of log lines to return.
  - `20000`

### Request Body Parameters

This endpoint doesn't use HTTP request body parameters.

## Response

| Name | Type | Description |
|---|---|---|
| slowQueries | array of documents | A list of documents with information about slow queries as detected by the Performance Advisor. |
| slowQueries[n].line | string | The raw log line pertaining to the slow query. |
| slowQueries[n].namespace | string | The namespace in which the slow query ran. |

## Example Request

```sh
curl --user '{PUBLIC-KEY}:{PRIVATE-KEY}' --digest \
 --header 'Accept: application/json' \
 --include \
 --request GET 'https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0/groups/{PROJECT-ID}/hosts/{HOST-ID}/performanceAdvisor/slowQueryLogs?pretty=true'
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
  "slowQueries" : [ {
    "line" : "2018-08-16T22:53:43.447+0000 I COMMAND  [conn10614] command myDb.users appName: \"MongoDB Shell\" command: find { find: \"users\", filter: { emails: \"tocde@fijoow.to\" }, lsid: { id: UUID(\"832b4b0e-085a-480e-b470-16a0994dc7cb\") }, $clusterTime: { clusterTime: Timestamp(1534460016, 1)...",
   "namespace" : "myDb.users"
  }, {
    "line" : "2018-08-16T22:54:32.705+0000 I COMMAND  [conn10614] command myDb.users appName: \"MongoDB Shell\" command: find { find: \"users\", filter: { emails: \"la@sa.kp\" }, lsid: { id: UUID(\"832b4b0e-085a-480e-b470-16a0994dc7cb\") }, $clusterTime: { clusterTime: Timestamp(1534460056, 1), ...",
    "namespace" : "myDb.users"
  } ]
}
```
