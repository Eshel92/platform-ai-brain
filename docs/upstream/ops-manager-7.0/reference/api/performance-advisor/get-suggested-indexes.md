<!-- Converted from reference/api/performance-advisor/get-suggested-indexes.txt (reStructuredText). Includes are inlined. -->

# Get Suggested Indexes

Retrieves suggested indexes as determined by the
Performance Advisor.

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

## Resource

```http
GET /groups/{PROJECT-ID}/hosts/{HOST-ID}/performanceAdvisor/suggestedIndexes
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
  - Point in time from which to retrieve suggested indexes,
    stated in [milliseconds since epoch](https://currentmillis.com/).
  - previous 24 hours

* - duration
  - long
  - Length of time in milliseconds during which to find
    suggested indexes among the managed namespaces in the cluster.
  - up to the present time

* - namespaces
  - string
  - Namespaces from which to retrieve suggested indexes. A namespace
    consists of the database and collection resource separated by a
    `.`, such as `<database>.<collection>`.

    To specify multiple namespaces, pass the parameter multiple times
    using an ampersand (`&`) as a delimiter, once for each
    namespace.

    For example:

    ```
    ?namespaces=data.stocks&namespaces=data.zips&pretty=true
    ```

  - all

* - nIndexes
  - long
  - Maximum number of indexes to suggest.
  - unlimited

* - nExamples
  - long
  - Maximum number of examples queries to provide that will be
    improved by a suggested index.
  - 5

### Request Body Parameters

This endpoint doesn't use HTTP request body parameters.

## Response

* - Name
  - Type
  - Description

* - `shapes`
  - array of documents
  - Documents with information about the query shapes that are served by the
    suggested indexes.

* - `shapes[n].avgMs`
  - number
  - Average duration in milliseconds for the queries examined that
    match this shape.

* - `shapes[n].count`
  - number
  - Number of queries examined that match this shape.

* - `shapes[n].id`
  - objectId
  - Unique id for this shape. Exists only for the duration of the
    API request.

* - `shapes[n].inefficiencyScore`
  - number
  - Average number of documents read for every document returned
    by the query. For more information, see Understanding the
    Query Inefficiency Score.

* - `shapes[n].namespace`
  - string
  - Namespace searched by the queries in this shape.

* - `shapes[n].operations`
  - array of documents
  - Documents with specific information and log lines for individual
    queries.

* - `shapes[n].operations[n].predicates`
  - array of documents
  - Documents containing the search criteria used by the query.
    Values in key-value pairs will be redacted in these predicates
    unless the user has Project Data Access Read Only permissions or higher.

* - `shapes[n].operations[n].raw`
  - string
  - Raw log line produced by the query.

* - `shapes[n].operations[n].stats`
  - document
  - Query statistics.

* - `shapes[n].operations[n].stats.ms`
  - number
  - Duration in milliseconds of the query.

* - `shapes[n].operations[n].stats.nReturned`
  - number
  - Number of results returned by the query.

* - `shapes[n].stats.avgObjSize`
  - number
  - Average object size.

* - `shapes[n].stats.nScanned`
  - number
  - Number of documents read by the query.

* - `shapes[n].stats.ts`
  - number
  - Query timestamp, in seconds since epoch.

* - `suggestedIndexes`
  - array of documents
  - Documents with information about the indexes suggested by the
    Performance Advisor.

* - `suggestedIndexes[n].id`
  - objectId
  - Unique id for this suggested index.

* - `suggestedIndexes[n].impact`
  - array of objectIds
  - List of unique identifers which correspond the query
    shapes in this response which pertain to this suggested index.

    This field does not correspond to Impact in the
    Performance Advisor user
    interface.

* - `suggestedIndexes[n].index`
  - array of documents
  - Each array element is a document that specifies a key in the
    index and its sort order, ascending or descending.

    - A value of 1 indicates an ascending sort order.
    - A value of -1 indicates a descending sort order.

    Keys in indexes with multiple keys appear in the same order
    that they appear in the index.

* - `suggestedIndexes[n].index.<fieldname>`
  - string
  - Specific field to be indexed.

* - `suggestedIndexes[n].namespace`
  - string
  - Namespace of the suggested index.

* - `suggestedIndexes[n].weight`
  - number
  - Estimated performance improvement that the suggested
    index would provide. Corresponds to Impact in the Performance Advisor user interface.

## Example Request

```sh
curl --user '{PUBLIC-KEY}:{PRIVATE-KEY}' --digest \
 --header 'Accept: application/json' \
 --include \
 --request GET 'https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0/groups/{PROJECT-ID}/hosts/{HOST-ID}/performanceAdvisor/suggestedIndexes?pretty=true'
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
  "shapes" : [ {
    "avgMs" : 42,
    "count" : 2,
    "id" : "5b74689a80eef53f3388897e",
    "inefficiencyScore" : 50000,
    "namespace" : "test.users",
    "operations" : [ {
      "predicates" : [{ "find" : { "emails" : "la@sa.kp" } }],
      "raw" : "2018-08-15T17:14:11.115+0000 I COMMAND  [conn4576] command test.users appName: \"MongoDB Shell\" command: find { find: \"users\", filter: { emails: \"la@sa.kp\" }, lsid: { id: UUID(\"1a4e71d3-9b67-4e9c-b078-9fdf3fae9091\") }, $clusterTime: { clusterTime: Timestamp(1534353241, 1), signature: { hash: BinData(0, AB91938B7CF7BC87994A2909A98D87F29101EFA0), keyId: 6589681559618453505 } }, $db: \"test\" } planSummary: COLLSCAN keysExamined:0 docsExamined:50000 cursorExhausted:1 numYields:391 nreturned:1 reslen:339 locks:{ Global: { acquireCount: { r: 784 } }, Database: { acquireCount: { r: 392 } }, Collection: { acquireCount: { r: 392 } } } protocol:op_msg 34ms",
      "stats" : {
        "ms" : 34,
        "nReturned" : 1,
        "nScanned" : 50000,
        "ts" : 1534353251147
      }
    }, {
      "predicates" : [{ "find" : { "emails" : "tocde@fijoow.to" } }],
      "raw" : "2018-08-15T17:14:18.665+0000 I COMMAND  [conn4576] command test.users appName: \"MongoDB Shell\" command: find { find: \"users\", filter: { emails: \"tocde@fijoow.to\" }, lsid: { id: UUID(\"1a4e71d3-9b67-4e9c-b078-9fdf3fae9091\") }, $clusterTime: { clusterTime: Timestamp(1534353241, 1), signature: { hash: BinData(0, AB91938B7CF7BC87994A2909A98D87F29101EFA0), keyId: 6589681559618453505 } }, $db: \"test\" } planSummary: COLLSCAN keysExamined:0 docsExamined:50000 cursorExhausted:1 numYields:390 nreturned:1 reslen:342 locks:{ Global: { acquireCount: { r: 782 } }, Database: { acquireCount: { r: 391 } }, Collection: { acquireCount: { r: 391 } } } protocol:op_msg 36ms",
      "stats" : {
        "ms" : 36,
        "nReturned" : 1,
        "nScanned" : 50000,
        "ts" : 1534353258697
      }
    } ]
  } ],
  "suggestedIndexes" : [ {
    "id" : "5b74689a80eef53f3388897f",
    "impact" : [ "5b74689a80eef53f3388897e" ],
    "index" : [ {
      "emails" : 1
    } ],
    "namespace" : "test.users",
    "weight" : 37.220480901815623
  }, {
    "id" : "5b74689a80eef53f33888980",
    "impact" : [ "5b74689a80eef53f3388897d" ],
    "index" : [ {
      "email" : 1
    } ],
    "namespace" : "test.inventory",
    "weight" : 19.037578309966488
  } ]
}
```
