<!-- Converted from reference/api/events/get-all-events-global.txt (reStructuredText). Includes are inlined. -->

# Get All Global Events

## Required Roles

Your API Key must have the `Global Read Only` role to
successfully call this resource.

## Request

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

```http
GET /globalEvents
```

### Request Path Parameters

This endpoint doesn't use HTTP request path parameters.

### Request Query Parameters

#### Unique Query Parameters

This endpoint accepts the following query parameters to filter
returned events:

| Name | Type | Description | Default |
|---|---|---|---|
| minDate | string | Return only events for which the created date is greater than or equal to the specified Timestamp in ISO 8601 date and time format in UTC (Coordinated Universal Time). |  |
| maxDate | string | Return only events for which the created date is less than or equal to the specified Timestamp in ISO 8601 date and time format in UTC (Coordinated Universal Time). |  |
| eventType | string | Return only events of the specified types. Accepted values include: To review the types of events that generate alerts, see Alert Types. For a complete list of events included in the Ops Manager audit log, see Audit Events. |  |

#### Common Query Parameters

This endpoint also accepts the query parameters common to all endpoints
that return lists of values:

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

### Response Document

The response JSON (Javascript Object Notation) document includes an array of result
objects, an array of link objects and a count of the total
number of result objects retrieved.

| Name | Type | Description |
|---|---|---|
| `results` | array | Array includes one object for each item detailed in the results-embedded-document-get-all section. |
| `links` | array | Array includes one or more links to sub-resources and/or related resources. The relations between URL (Uniform Resource Locator)\s are explained in the Web Linking Specification. |
| `totalCount` | number | Integer count of the total number of items in the result set. It may be greater than the number of objects in the results array if the entire result set is paginated. |

### `results` Embedded Document

Each **result** is one event.

* - Name
  - Type
  - Description

* - alertId
  - string
  - Unique identifier for the alert associated with this event.

* - alertConfigId
  - string
  - Unique identifier for the alert configuration associated with
    the `alertId`.

* - apiKeyId
  - string
  - Unique identifier for the API Key
    that triggered this event.

    If this field is present in the response, Ops Manager does not return
    the `userId` field.

* - clusterId
  - string
  - Unique identifier of the cluster to which this event applies.

* - clusterName
  - string
  - Name of the cluster to which this event applies.

* - collection
  - string
  - Name of the collection on which the event occurred. This field
    can be present when the `eventTypeName` is either
    `DATA_EXPLORER` or `DATA_EXPLORER_CRUD`.

* - created
  - string
  - Timestamp in ISO 8601 date and time format in UTC (Coordinated Universal Time) when this event was triggered.

* - currentValue
  - object
  - Current value of the metric that triggered this event.

* - | currentValue
    | .number
  - number
  - Value of the metric.

* - | currentValue
    | .units
  - string
  - Units for `currentValue.number`. The units depend on the type of metric.

    Accepted values are:

    - `RAW`
    - `BITS`
    - `BYTES`
    - `KILOBITS`
    - `KILOBYTES`
    - `MEGABITS`
    - `MEGABYTES`
    - `GIGABITS`
    - `GIGABYTES`
    - `TERABYTES`
    - `PETABYTES`
    - `MILLISECONDS`
    - `SECONDS`
    - `MINUTES`
    - `HOURS`
    - `DAYS`

    For example, a metric that measures memory consumption can use `BYTES`, 
    while a metric that measures time can use `HOURS`. 

* - database
  - string
  - Name of the database on which the event occurred. This field
    can be present when the `eventTypeName` is either
    `DATA_EXPLORER` or `DATA_EXPLORER_CRUD`.

* - eventTypeName
  - string
  - Name of the circumstance that triggered this event.

    To review the types of events that generate alerts, see
    Alert Types.

    For a complete list of events included in the Ops Manager audit log, see
    Audit Events.

* - groupId
  - string
  - Unique identifier of the project in which this event occurred.

* - hostId
  - string
  - Unique identifier of the host on which this event occurred.

* - hostname
  - string
  - Hostname, FQDN (fully qualified domain name), IPv4 (Internet Protocol version 4) address, or IPv6 (Internet Protocol version 6) address of the host
    on which this event occurred.

* - id
  - string
  - Unique identifier for this event.

* - isGlobalAdmin
  - boolean
  - Flag indicating whether the user who triggered this event has
    the `Global Monitoring Administrator` role.

* - links
  - object array
  - .. include:: /includes/api/links-explanation.rst

* - metricName
  - string
  - Name of the measurement whose value went outside the threshold.

    For possible values, see below.

* - opType
  - string
  - Type of operation that generated the event. This field is
    present when the `eventTypeName` is either `DATA_EXPLORER`
    or `DATA_EXPLORER_CRUD`.

* - port
  - integer
  - Port of the host associated with this event.

* - publicKey
  - string
  - Public key associated with the
    API Key that triggered this event.

    If this field is present in the response, Ops Manager does not return
    the `username` field.

* - remoteAddress
  - string
  - IP address associated with the Ops Manager user (userId) who
    triggered the event.

* - replicaSetName
  - string
  - Name of the replica set.

* - shardName
  - string
  - Name of the shard associated with the event.

* - targetPublicKey
  - string
  - Public key of the API Key
    targeted by the event.

* - targetUsername
  - string
  - Username for the Ops Manager user targeted by this event.

* - teamId
  - string
  - Unique identifier for the Ops Manager team associated with this event.

* - userId
  - string
  - Unique identifier for the Ops Manager user who triggered this
    event.

    If this field is present in the response, Ops Manager does not
    return the `apiKeyId` field.

* - username
  - string
  - Username for the Ops Manager user who triggered this event.

    If this field is present in the response, Ops Manager does not return
    `publicKey` field.

* - accessListEntry
  - string
  - Access list entry of the API Key targeted by the event.

## Example Request

```console
curl --user "{publicKey}:{privateKey}" --digest \
     --header "Accept: application/json" \
     --include \
     --request GET "https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0/globalEvents?pretty=true"
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
  "alertConfigId": "{alertConfigId}",
  "alertId": "{alertId}",
  "clusterId": "{clusterId}",
  "clusterName": "Test Cluster",
  "created": "2018-06-11T12:34:56Z",
  "currentValue": {
    "number": 50,
    "units": "RAW"
  },
  "eventTypeName": "OUTSIDE_METRIC_THRESHOLD",
  "groupId": "{groupId}",
  "hostId": "{hostId}",
  "hostname": "db.example.com",
  "id": "{globalAlertId}",
  "isGlobalAdmin": false,
  "maintenanceWindowId": "{maintenanceWindowId}",
  "metricName": "OPCOUNTER_CMD",
  "orgId": "{orgId}",
  "port": 27017,
  "remoteAddress": "192.168.1.1",
  "replicaSetName": "rs1",
  "shardName": "sh1",
  "userId": "{userId}",
  "username": "john.doe@example.com",
  "targetUsername": "jane.doe@example.com",
  "teamId": "{teamId}"
}
```
