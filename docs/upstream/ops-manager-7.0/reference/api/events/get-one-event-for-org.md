<!-- Converted from reference/api/events/get-one-event-for-org.txt (reStructuredText). Includes are inlined. -->

# Get One Organization Event

## Required Roles

Your API Key must have the `Organization Member` role to
successfully call this resource.

## Request

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

```http
GET /orgs/{orgId}/events/{eventId}
```

### Request Path Parameters

| Name | Type | Description |
|---|---|---|
| orgId | string | Unique identifier of the organization associated with the desired event. |
| eventId | string | Unique identifier of the desired event. |

### Request Query Parameters

The following query parameters are optional:

| Query Parameter | Type | Description | Default |
|---|---|---|---|
| pretty | boolean | Displays response in a [prettyprint](https://en.wikipedia.org/wiki/Prettyprint?oldid=791126873) format. | `false` |
| envelope | boolean | Specifies whether or not to wrap the response in an envelope. | `false` |
| includeRaw | boolean | Specifies whether to include the `raw` document in the output. The `raw` document contains additional meta information about the event. IMPORTANT: The values in the `raw` document differ depending on the resource that the event applies to. Use this field with caution, as its structure may vary across resource types. | `false` |

### Request Body Parameters

This endpoint doesn't use HTTP request body parameters.

## Response

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
  - Relevant units for the value.

    **Example:**

    A metric that measures memory consumption would have a byte measurement, while a metric that measures time would have a time unit.

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

* - raw
  - document
  - Additional meta information about the event. This field only
    appears when the `includeRaw` query parameter is `true`.

    IMPORTANT: The values in the `raw` document differ depending
    on the resource that the event applies to. Use this field with caution, 
    as its structure may vary across resource types.

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
     --request GET "https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0/orgs/{orgId}/events/{eventId}?pretty=true" \
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
