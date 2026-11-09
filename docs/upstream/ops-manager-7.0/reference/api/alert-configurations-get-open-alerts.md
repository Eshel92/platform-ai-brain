<!-- Converted from reference/api/alert-configurations-get-open-alerts.txt (reStructuredText). Includes are inlined. -->

# Get Open Alerts for Alert Configuration

**Note:**

Groups and projects are synonymous terms. Your `{PROJECT-ID}` is the
same as your project id. For existing groups, your group/project id
remains the same. This page uses the more familiar term group when
referring to descriptions. The endpoint remains as stated in the
document.

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

## Resource

```http
GET /groups/{PROJECT-ID}/alertConfigs/{ALERT-CONFIG-ID}/alerts
```

### Request Path Parameters

All request path parameters are *required*.

| Parameter | Type | Description |
|---|---|---|
| PROJECT-ID | string | Unique identifier for this Project. |
| ALERT-CONFIG-ID | string | Unique identifier for this alert configuration. |

### Request Query Parameters

The following query parameters are optional:

| Name | Type | Necessity | Description | Default |
|---|---|---|---|---|
| pageNum | number | Optional | One-based integer that returns a subsection of results. | `1` |
| itemsPerPage | number | Optional | Number of items to return per page, up to a maximum of 500. | `100` |
| pretty | boolean | Optional | Flag that indicates whether the response body should be in a prettyprint format. | `false` |
| envelope | boolean | Optional | Flag that indicates whether or not to wrap the response in an envelope. Some API (Application Programming Interface) clients cannot access the HTTP (Hypertext Transfer Protocol) response headers or status code. To remediate this, set `envelope : true` in the query. For endpoints that return a list of results, the `results` object is an envelope. Ops Manager adds the `status` field to the response body. | `false` |
| backupJobsEnabledOnly | boolean | Optional | Flag indicating whether to exclude daemons not enabled for backing up databases from the response. Set this to `false` to include daemon configurations with the `backupJobsEnabled` flag set to `false`. | `true` |

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

Each **result** is one alert configuration.

**Note:**

Alert details vary. An alert may only include a subset of these
elements.

* - Name
  - Type
  - Description

* - acknowledgedUntil
  - string
  - Timestamp in ISO 8601 date and time format in UTC (Coordinated Universal Time) when through which the alert has been
    acknowledged. Populated if the alert has been acknowledged.

* - acknowledgingUsername
  - string
  - Username of the user who acknowledged the alert. Populated if
    the alert has been acknowledged.

* - acknowledgementComment
  - string
  - Comment user who acknowledged the alert left. Populated
    if the alert has been acknowledged.

* - alertConfigId
  - string
  - Unique identifier of the alert configuration that triggered
    this alert.

* - clusterId
  - string
  - Unique identifier of the cluster to which this alert applies.
    Populated for `BACKUP`, `REPLICA_SET`, and `CLUSTER`
    alerts.

* - clusterName
  - string
  - Name the cluster to which this alert applies.
    Populated for `BACKUP`, `REPLICA_SET`, and `CLUSTER`
    alerts.

* - created
  - string
  - Timestamp in ISO 8601 date and time format in UTC (Coordinated Universal Time) when the alert was opened.

* - currentValue
  - object
  - Current value of the metric that triggered the alert. Populated
    for `HOST_METRIC` alerts.

* - currentValue.number
  - number
  - Value of the metric.

* - currentValue.units
  - string
  - Units for the value. Depends on the type of metric.

    For example, a metric that measures memory consumption would have
    a byte measurement, while a metric that measures time would have
    a time unit. Accepted values are:

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

* - eventTypeName
  - string
  - Name of the event that triggered the alert.

    Values include:

    **Agent**

    - `AUTOMATION_AGENT_DOWN`
    - `AUTOMATION_AGENT_UP`
    - `BACKUP_AGENT_CONF_CALL_FAILURE`
    - `BACKUP_AGENT_DOWN`
    - `BACKUP_AGENT_UP`
    - `BACKUP_AGENT_VERSION_BEHIND`
    - `BACKUP_AGENT_VERSION_CURRENT`
    - `MONITORING_AGENT_DOWN`
    - `MONITORING_AGENT_UP`
    - `MONITORING_AGENT_VERSION_BEHIND`
    - `MONITORING_AGENT_VERSION_CURRENT`
    - `NEW_AGENT`

    **Alerts**

    - `WEBHOOK_TEMPLATE_RENDER_FAILED`

    **Automation Configuration**

    - `AUTOMATION_CONFIG_PUBLISHED_AUDIT`

    **Backup**

    - `BAD_CLUSTERSHOTS`
    - `CLUSTER_BLACKLIST_UPDATED_AUDIT`
    - `CLUSTER_CHECKKPOINT_UPDATED_AUDIT`
    - `CLUSTER_CREDENTIAL_UPDATED_AUDIT`
    - `CLUSTER_SNAPSHOT_SCHEDULE_UPDATED_AUDIT`
    - `CLUSTER_STATE_CHANGED_AUDIT`
    - `CLUSTER_STORAGE_ENGINE_UPDATED_AUDIT`
    - `CLUSTERSHOT_DELETED_AUDIT`
    - `CLUSTERSHOT_EXPIRY_UPDATED_AUDIT`
    - `CONSISTENT_BACKUP_CONFIGURATION`
    - `GOOD_CLUSTERSHOT`
    - `INCONSISTENT_BACKUP_CONFIGURATION`
    - `INITIAL_SYNC_FINISHED_AUDIT`
    - `INITIAL_SYNC_STARTED_AUDIT`
    - `OPLOG_BEHIND`
    - `OPLOG_CURRENT`
    - `RESTORE_REQUESTED_AUDIT`
    - `RESYNC_PERFORMED`
    - `RESYNC_REQUIRED`
    - `RS_BLACKLIST_UPDATED_AUDIT`
    - `RS_CREDENTIAL_UPDATED_AUDIT`
    - `RS_ROTATE_MASTER_KEY_AUDIT`
    - `RS_SNAPSHOT_SCHEDULE_UPDATED_AUDIT`
    - `RS_STATE_CHANGED_AUDIT`
    - `RS_STORAGE_ENGINE_UPDATED_AUDIT`
    - `SNAPSHOT_DELETED_AUDIT`
    - `SNAPSHOT_EXPIRY_UPDATED_AUDIT`
    - `SYNC_PENDING_AUDIT`
    - `SYNC_REQUIRED_AUDIT`

    **BI Connector**

    - `BI_CONNECTOR_DOWN`
    - `BI_CONNECTOR_UP`

    **Cluster**

    - `CLUSTER_MONGOS_IS_MISSING`
    - `CLUSTER_MONGOS_IS_PRESENT`
    - `SHARD_ADDED`
    - `SHARD_REMOVED`

    **Data Explorer Accessed**

    - `DATA_EXPLORER`
    - `DATA_EXPLORER_CRUD`

    **Host**

    - `ADD_HOST_AUDIT`
    - `ADD_HOST_TO_REPLICA_SET_AUDIT`
    - `DELETE_HOST_AUDIT`
    - `HOST_DOWN`
    - `HOST_RECOVERING`
    - `HOST_RESTARTED`
    - `HOST_ROLLBACK`
    - `HOST_SSL_CERTIFICATE_STALE`
    - `OUTSIDE_METRIC_THRESHOLD`
    - `REMOVE_HOST_FROM_REPLICA_SET_AUDIT`
    - `UNDELETE_HOST_AUDIT`
    - `VERSION_BEHIND`

    **Organization**

    - `ALL_ORG_USERS_HAVE_MFA`
    - `ORG_API_KEY_ADDED`
    - `ORG_API_KEY_DELETED`
    - `ORG_EMPLOYEE_ACCESS_RESTRICTED`
    - `ORG_EMPLOYEE_ACCESS_UNRESTRICTED`
    - `ORG_PUBLIC_API_ACCESS_LIST_NOT_REQUIRED`
    - `ORG_PUBLIC_API_ACCESS_LIST_REQUIRED`
    - `ORG_RENAMED`
    - `ORG_TWO_FACTOR_AUTH_OPTIONAL`
    - `ORG_TWO_FACTOR_AUTH_REQUIRED`
    - `ORG_USERS_WITHOUT_MFA`

    **Project**

    - `ALL_USERS_HAVE_MULTI_FACTOR_AUTH`
    - `USERS_WITHOUT_MULTI_FACTOR_AUTH`

    **Replica Set**

    - `CONFIGURATION_CHANGED`
    - `ENOUGH_HEALTHY_MEMBERS`
    - `MEMBER_ADDED`
    - `MEMBER_REMOVED`
    - `MULTIPLE_PRIMARIES`
    - `NO_PRIMARY`
    - `ONE_PRIMARY`
    - `PRIMARY_ELECTED`
    - `TOO_FEW_HEALTHY_MEMBERS`
    - `TOO_MANY_ELECTIONS`
    - `TOO_MANY_UNHEALTHY_MEMBERS`

    **Team**

    - `TEAM_ADDED_TO_GROUP`
    - `TEAM_CREATED`
    - `TEAM_DELETED`
    - `TEAM_NAME_CHANGED`
    - `TEAM_REMOVED_FROM_GROUP`
    - `TEAM_ROLES_MODIFIED`
    - `TEAM_UPDATED`
    - `USER_ADDED_TO_TEAM`

    **User**

    - `INVITED_TO_GROUP`
    - `INVITED_TO_ORG`
    - `JOIN_GROUP_REQUEST_APPROVED_AUDIT`
    - `JOIN_GROUP_REQUEST_DENIED_AUDIT`
    - `JOINED_GROUP`
    - `JOINED_ORG`
    - `JOINED_TEAM`
    - `REMOVED_FROM_GROUP`
    - `REMOVED_FROM_ORG`
    - `REMOVED_FROM_TEAM`
    - `REQUESTED_TO_JOIN_GROUP`
    - `USER_ROLES_CHANGED_AUDIT`

    To review the full list of events that generate alerts and their 
    descriptions, see Alert Types. For a 
    complete list of events included in the Ops Manager audit log, see
    Audit Events.

* - groupId
  - string
  - Unique identifier of the project that this alert was opened for.

* - hostId
  - string
  - Unique identifier of the host to which the metric pertains.
    Populated for `HOST`, `HOST_METRIC`, and `REPLICA_SET`
    alerts.

* - hostnameAndPort
  - string
  - Hostname and port of each host to which the alert applies.
    Populated for `HOST`, `HOST_METRIC`, and `REPLICA_SET`
    alerts.

* - id
  - string
  - Unique identifier for the alert.

* - lastNotified
  - string
  - Timestamp in ISO 8601 date and time format in UTC (Coordinated Universal Time) when the last notification was sent for this
    alert. Populated if notifications have been sent.

* - metricName
  - string
  - Name of the measurement whose value went outside the threshold.
    Populated if `"eventTypeName" : "OUTSIDE_METRIC_THRESHOLD"`.

    For accepted values, see measurement-types-for-alerts-api
    on this page.

* - replicaSetName
  - string
  - Name of the replica set.
    Populated for `HOST`, `HOST_METRIC`, `BACKUP`, and
    `REPLICA_SET` alerts.

* - resolved
  - string
  - Timestamp in ISO 8601 date and time format in UTC (Coordinated Universal Time) when the alert was closed. Populated if
    `"status" : "CLOSED"`.

* - sourceTypeName
  - string
  - For `BACKUP` alerts, the type of server being backed
    up. Accepted values are:

    - `REPLICA_SET`
    - `SHARDED_CLUSTER`
    - `CONFIG_SERVER`

* - status
  - string
  - Current state of the alert. Accepted values are:

    - `TRACKING`

      The alert condition exists but has not persisted beyond the defined
      notification delay. For details, see api-alert-status.

    - `OPEN`
    - `CLOSED`
    - `CANCELLED`

* - typeName
  - string
  - *This field is deprecated and will be ignored.*

* - updated
  - string
  - Timestamp in ISO 8601 date and time format in UTC (Coordinated Universal Time) when the alert was last updated.

## Example Request

```sh
curl --user '{PUBLIC-KEY}:{PRIVATE-KEY}' --digest \
  --header 'Accept: application/json' \
  --include \
  --request GET "https://<ops-manager-host>/api/public/v1.0/groups/{PROJECT-ID}/alertConfigs/{ALERT-CONFIG-ID}/alerts"
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
  "links" : [],
  "results" : [ {
    "acknowledgedUntil" : "2014-05-01T14:00:00Z",
    "alertConfigId":"{ALERT-CONFIG-ID}",
    "created" : "2014-04-22T15:57:13.562Z",
    "currentValue" : {
      "number" : 0.0,
      "units" : "RAW"
    },
    "eventTypeName" : "OUTSIDE_METRIC_THRESHOLD",
    "groupId" : "{PROJECT-ID}",
    "id" : "53569159300495c7702ee3a3",
    "lastNotified" : "2014-04-22T15:57:24.126Z",
    "links" : [],
    "metricName" : "ASSERT_REGULAR",
    "status" : "OPEN",
    "updated" : "2014-04-22T20:14:11.388Z"
  }, {
    "alertConfigId":"{ALERT-CONFIG-ID}",
    "created" : "2014-04-22T19:59:10.657Z",
    "currentValue" : {
      "number" : 0.0,
      "units" : "RAW"
    },
    "eventTypeName" : "OUTSIDE_METRIC_THRESHOLD",
    "groupId" : "{PROJECT-ID}",
    "id" : "5356ca0e300495c770333340",
    "lastNotified" : "2014-04-22T20:14:19.313Z",
    "links" : [],
    "metricName" : "ASSERT_REGULAR",
    "status" : "OPEN",
    "updated" : "2014-04-22T20:14:11.388Z"
  } ],
  "totalCount" : 2
}
```
