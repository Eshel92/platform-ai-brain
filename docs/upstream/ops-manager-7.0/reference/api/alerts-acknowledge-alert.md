<!-- Converted from reference/api/alerts-acknowledge-alert.txt (reStructuredText). Includes are inlined. -->

# Acknowledge One Alert

**Note:**

Groups and projects are synonymous terms. Your `{PROJECT-ID}` is the
same as your project id. For existing groups, your group/project id
remains the same. This page uses the more familiar term group when
referring to descriptions. The endpoint remains as stated in the
document.

## Resource

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

```http
PATCH /groups/{PROJECT-ID}/alerts/{ALERT-ID}
```

### Request Path Parameters

| Parameter | Type | Necessity | Description |
|---|---|---|---|
| `PROJECT-ID` | string | Required | Unique identifier for the Project in which this alert is set. |
| `ALERT-ID` | string | Required | Unique identifier for the Alert. |

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

* - Field
  - Type
  - Necessity
  - Description

* - | `acknowledged`
    | `Until`
  - string
  - Conditional
  - Timestamp in ISO 8601 date and time format in UTC (Coordinated Universal Time) until which the alert should be acknowledged.

    - To acknowledge an alert "forever", set the field value to a
      large number of years in the future. Recommend setting to 100
      years in the future.

    - To unacknowledge an acknowledged alert, remove this parameter
      from your request.

* - | `acknowledgement`
    | `Comment`
  - string
  - Optional
  - Text description of the reason for this acknowledgement.

    Ops Manager displays the comment next to the message that the
    alert has been acknowledged.

## Response

The fields in the return document depend on the alert type:

* - Name
  - Type
  - Description

* - | `acknowledged`
    | `Until`
  - string
  - Timestamp in ISO 8601 date and time format in UTC (Coordinated Universal Time) until which the alert has been acknowledged.

    Ops Manager returns this value if the alert has been acknowledged.

* - | `acknowledgement`
    | `Comment`
  - string
  - Comment left by the user who acknowledged the alert.

    Ops Manager returns this value if the alert has been acknowledged.

* - | `acknowledging`
    | `Username`
  - string
  - Username of the user who acknowledged the alert.

    Ops Manager returns this value if the alert has been acknowledged.

* - `alertConfigId`
  - string
  - Unique identifier for the alert configuration that triggered
    this alert.

* - `clusterId`
  - string
  - Unique identifier for the cluster to which this alert applies.

    Ops Manager returns this value if
    `"eventTypeName" : "SHARDED_CLUSTER"`

* - `clusterName`
  - string
  - Name of the cluster to which this alert applies.

    Ops Manager returns this value if
    `"eventTypeName" : "SHARDED_CLUSTER"`

* - `created`
  - string
  - Timestamp in ISO 8601 date and time format in UTC (Coordinated Universal Time) when the alert was opened.

* - `currentValue`
  - object
  - Current value of the metric that triggered the alert.

    Ops Manager returns this value if
    `"eventTypeName" : "OUTSIDE_METRIC_THRESHOLD"`.

* - | `currentValue`
    | `.number`
  - number
  - Value of the metric.

* - | `currentValue`
    | `.units`
  - string
  - Units for the value. Value depends on the type of metric.

    For example, a metric that measures memory consumption would have a byte
    measurement, while a metric that measures time would have a
    time unit.

    Ops Manager can return:

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

* - `eventTypeName`
  - string
  - Name of the event that triggered the alert.

    Accepted values are: 

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

    - `ATTEMPT_KILLOP_AUDIT`
    - `ATTEMPT_KILLSESSION_AUDIT`
    - `DB_PROFILER_DISABLE_AUDIT`
    - `DB_PROFILER_ENABLE_AUDIT`
    - `DISABLE_HOST_AUDIT`
    - `HIDE_AND_DISABLE_HOST_AUDIT`
    - `HIDE_HOST_AUDIT`
    - `HOST_DOWN`
    - `HOST_DOWNGRADED`
    - `HOST_IP_CHANGED_AUDIT`
    - `HOST_NOW_PRIMARY`
    - `HOST_NOW_SECONDARY`
    - `HOST_NOW_STANDALONE`
    - `HOST_RECOVERED`
    - `HOST_RECOVERING`
    - `HOST_SECURITY_CHECKUP_NOT_MET`
    - `HOST_SSL_CERTIFICATE_CURRENT`
    - `HOST_SSL_CERTIFICATE_STALE`
    - `HOST_UP`
    - `HOST_UPGRADED`
    - `INSIDE_METRIC_THRESHOLD`
    - `NEW_HOST`
    - `OUTSIDE_METRIC_THRESHOLD`
    - `PAUSE_HOST_AUDIT`
    - `RESUME_HOST_AUDIT`
    - `UNDELETE_HOST_AUDIT`
    - `VERSION_BEHIND`
    - `VERSION_CHANGED`
    - `VERSION_CURRENT`

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
    - `JOINED_TEAM`
    - `REMOVED_FROM_TEAM`
    - `REQUESTED_TO_JOIN_GROUP`

    For a complete list of events included in the Ops Manager audit 
    log, see Audit Events.

* - `groupId`
  - string
  - Unique identifier of the group for which this alert was opened.

* - `hostId`
  - string
  - unique identifier for the host to which the metric pertains.

    Ops Manager returns this value if `"eventTypeName"` was set to one
    of the following:

    - `HOST_DOWN`
    - `OUTSIDE_METRIC_THRESHOLD`
    - `REPLICA_SET`

* - `hostnameAndPort`
  - string
  - Hostname and port of each host to which the alert applies. This
    can be a hostname, an FQDN (fully qualified domain name), an IPv4 (Internet Protocol version 4) address, or an IPv6 (Internet Protocol version 6)
    address.

    Ops Manager returns this value if `"eventTypeName"` was set to one
    of the following:

    - `HOST_DOWN`
    - `OUTSIDE_METRIC_THRESHOLD`
    - `REPLICA_SET`

* - `id`
  - string
  - Unique identifier for the alert.

* - `lastNotified`
  - string
  - Timestamp in ISO 8601 date and time format in UTC (Coordinated Universal Time) when the last notification was sent for this
    alert. Ops Manager returns this value if notifications have been sent.

* - `links`
  - array of objects
  - .. include:: /includes/api/links-explanation.rst

* - `metricName`
  - string
  - Name of the measurement whose value went outside the
    threshold.

    Ops Manager returns this value if `"eventTypeName"` was set to
    `OUTSIDE_METRIC_THRESHOLD`.

    For possible values, see measurement-types-for-alerts-api.

* - `replicaSetName`
  - string
  - Name of the replica set.

    Ops Manager returns this value if `"eventTypeName"` was set to one
    of the following:

    - `BACKUP`
    - `HOST_DOWN`
    - `OUTSIDE_METRIC_THRESHOLD`
    - `REPLICA_SET`

* - `resolved`
  - string
  - Timestamp in ISO 8601 date and time format in UTC (Coordinated Universal Time) when the alert was closed.

    Ops Manager returns this value if `"status" : "CLOSED"`.

* - `status`
  - string
  - Current state of the alert. Ops Manager can return one of the
    following:

    - `TRACKING`

      The alert condition exists but has not persisted beyond the
      defined notification delay. For details, see
      api-alert-status.

    - `OPEN`
    - `CLOSED`
    - `CANCELLED`

* - `sourceTypeName`
  - string
  - Type of host being backed up when ``"eventTypeName" :
    "BACKUP"``. Ops Manager can return one of the following:

    - `REPLICA_SET`
    - `SHARDED_CLUSTER`
    - `CONFIG_SERVER`

* - `tags`
  - string array
  - Identifying labels set for this alert.

* - `updated`
  - string
  - Timestamp in ISO 8601 date and time format in UTC (Coordinated Universal Time) when the alert was last updated.

## Example Request

```sh
curl --user "{PUBLIC-KEY}:{PRIVATE-KEY}" --digest \
     --header "Accept: application/json" \
     --header "Content-Type: application/json" \
     --include \
     --request PATCH "https://<ops-manager-host>/api/public/v1.0/groups/{PROJECT-ID}/alerts/{ALERT-CONFIG-ID}"
     --data '
       {
         "acknowledgedUntil": "2016-04-15T00:00:00-0400",
         "acknowledgementComment": "This is normal. Please ignore."
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

```json
{
  "id" : "{ALERT-CONFIG-ID}",
  "groupId" : "{PROJECT-ID}",
  "eventTypeName" : "OUTSIDE_METRIC_THRESHOLD",
  "status" : "OPEN",
  "acknowledgedUntil" : "2014-04-15T04:00:00Z",
  "acknowledgementComment" : "This is normal. Please ignore.",
  "acknowledgingUsername" : "someuser@example.com",
  "created" : "2014-04-03T20:28:14Z",
  "updated" : "2014-04-03T20:33:14Z",
  "lastNotified" : "2014-04-03T20:33:23Z",
  "metricName": "ASSERTS_REGULAR",
  "currentValue" : {
    "number" : 0.0,
    "units" : "RAW"
  },
  "links" : []
}
```
