<!-- Converted from reference/api/global-alerts-ack-one.txt (reStructuredText). Includes are inlined. -->

# Acknowledge One Global Alert

You can acknowledge one alert until the time and date you specify. 
You can also un-acknowledge an alert by specifying a date and time in 
the past.

## Required Roles

You can successfully call this endpoint with any of the following 
assigned roles:

- `Global Owner`
- `Global Monitoring Admin`

## Request

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

```http
PATCH /globalAlerts/{ALERT-ID}
```

### Request Path Parameters

| Name | Type | Description |
|---|---|---|
| `ALERT-ID` | string | Unique identifier of the maintenance window you want to acknowledge. |

### Request Query Parameters

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

| Body Parameter | Type | Necessity | Description |
|---|---|---|---|
| `acknowledgedUntil` | string | Required | Timestamp in ISO 8601 date and time format in UTC (Coordinated Universal Time) through which you acknowledge this alert. After this time passes, Ops Manager reverts the alert to un-acknowledged. To prevent the alert from resuming any time soon, set the date and time to some point in the distant future. To un-acknowledge an alert, specify a time and date in the past. |
| `acknowledgementComment` | string | Optional | Comment describing the alert acknowledgement. |

## Response

* - Name
  - Type
  - Description

* - `acknowledgedUntil`
  - string
  - Timestamp in ISO 8601 date and time format in UTC (Coordinated Universal Time) through which the alert has been acknowledged. 
    Ops Manager presents this field if a user acknowledged this alert.

* - `acknowledgementComment`
  - string
  - Comment that the user who acknowledged this alert left.
    Ops Manager presents this field if a user acknowledged this alert.

* - `acknowledgingUsername`
  - string
  - Ops Manager username of the user who acknowledged the alert.
    Ops Manager presents this field if a user acknowledged this alert.

* - `alertConfigId`
  - string
  - Unique identifier of the global alert configuration that triggered this alert.

* - `clusterId`
  - string
  - Unique identifier of the cluster to which this alert 
    applies. Ops Manager returns this field for global 
    alerts in the categories of:

    - backup
    - replica set
    - sharded cluster

* - `clusterName`
  - string
  - Name the cluster to which this alert applies. Ops Manager returns this field for global 
    alerts in the categories of:

    - backup
    - replica set
    - sharded cluster

* - `created`
  - string
  - Timestamp in ISO 8601 date and time format in UTC (Coordinated Universal Time) when the alert was created.

* - `currentValue`
  - object
  - Current value of the metric that triggered the alert.
    Ops Manager returns this field for global alerts in the category of
    host.

* - `currentValue.number`
  - number
  - Current value of the metric.

* - `currentValue.units`
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

* - `eventTypeName`
  - string
  - Name of the event that triggered the alert.

    To review the types of events that generate alerts, see
    Alert Types.

    For a complete list of events included in the Ops Manager audit log, see
    Audit Events.

* - `groupId`
  - string
  - Unique identifier of the project for which this alert was opened.

* - `hostId`
  - string
  - Unique identifier of the host to which the metric pertains.
    Ops Manager returns this field for global alerts in the categories of:

    - host
    - replica set

* - `hostnameAndPort`
  - string
  - Hostname and port of each host to which the alert applies. The
    hostname can be only a hostname, an FQDN (fully qualified domain name), an IPv4 (Internet Protocol version 4) address,
    or an IPv6 (Internet Protocol version 6) address. Ops Manager returns this field for global alerts in
    the categories of:

    - host
    - replica set

* - `id`
  - string
  - Unique identifier of the alert.

* - `lastNotified`
  - string
  - Timestamp in ISO 8601 date and time format in UTC (Coordinated Universal Time) when the last notification was sent for this
    alert. Ops Manager displays this if Ops Manager sent notifications.

* - `metricName`
  - string
  - Name of the measurement whose value went outside the threshold.
    Ops Manager returns this field if `"eventTypeName" : "OUTSIDE_METRIC_THRESHOLD"`.

    For possible values, see 
    measurement-types-for-global-alerts-api.

* - `replicaSetName`
  - string
  - Name of the replica set. Ops Manager returns this field for global 
    alerts in the categories of:

    - host
    - backup
    - replica set

* - `resolved`
  - string
  - Timestamp in ISO 8601 date and time format in UTC (Coordinated Universal Time) when the alert was closed. Ops Manager returns this field for global
    alerts when `"status" : "CLOSED"`.

* - `sourceTypeName`
  - string
  - Type of host being backed up. Ops Manager returns this field for global alerts in
    the category of backup. Possible values that can
    be returned include:

    - `REPLICA_SET`
    - `SHARDED_CLUSTER`
    - `CONFIG_SERVER`

* - `status`
  - string
  - Current state of the alert. Possible values that can be returned include:

    |  |  |
    |---|---|
    | `TRACKING` | Alert conditions exist, but the condition hasn't persisted for long enough to trigger an alert. |
    | `OPEN` | Alert is open. |
    | `CLOSED` | Alert is closed. |
    | `CANCELLED` | Alert is cancelled. |

* - `tags`
  - array of strings
  - Tags associated with this alert.

* - `typeName`
  - string
  - *This field is deprecated and will be ignored.*

* - `updated`
  - string
  - Timestamp in ISO 8601 date and time format in UTC (Coordinated Universal Time) when this alert was last updated.

## Example Request

```sh
curl --user "{PUBLIC-KEY}:{PRIVATE-KEY}" --digest \
     --header "Accept: application/json" \
     --header "Content-Type: application/json" \
     --include \
     --request PATCH "https://<OpsManagerHost>:<Port>/api/public/v1.0/globalAlerts/{ALERT-ID}" \
     --data '{
        "acknowledgedUntil":"2020-04-10T20:21:31Z",
        "acknowledgementComment":"test"
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
HTTP/1.1 201 Created
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
  "acknowledgedUntil": "2020-04-10T20:20:38Z",
  "acknowledgementComment": "test",
  "acknowledgingUsername": "rwqvzark",
  "alertConfigId": "{ALERT-CONFIG-ID}",
  "created": "2019-12-02T20:39:54Z",
  "eventTypeName": "BACKUP_AGENT_DOWN",
  "groupId": "{PROJECT-ID}",
  "id": "{ALERT-ID}",
  "lastNotified": "2020-04-09T20:21:31Z",
  "links": [
  ],
  "status": "OPEN",
  "tags": [],
  "typeName": "AGENT",
  "updated": "2020-04-10T19:14:38Z"
}
```
