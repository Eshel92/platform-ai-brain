<!-- Converted from reference/api/alert-configurations-create-config.txt (reStructuredText). Includes are inlined. -->

# Create an Alert Configuration

**Note:**

Groups and projects are synonymous terms. Your `{PROJECT-ID}` is the
same as your project id. For existing groups, your group/project id
remains the same. This page uses the more familiar term group when
referring to descriptions. The endpoint remains as stated in the
document.

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

## Resource

```none
POST /groups/{PROJECT-ID}/alertConfigs
```

### Request Path Parameters

All request path parameters are *required*.

| Parameter | Type | Description |
|---|---|---|
| PROJECT-ID | string | Unique identifier for this Project. |

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

**Note:**

Alert configurations vary. An alert configuration may only
include a subset of these elements.

* - Name
  - Type
  - Description

* - enabled
  - boolean
  - If omitted, the configuration is disabled.

* - | eventTypeName
    | *Required.*
  - string
  - The type of event that triggers an alert.

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

* - matchers.fieldName
  - string
  - Name of the field in the target object to match on.

    - Host alerts support these fields:

      - `HOSTNAME`
      - `PORT`
      - `HOSTNAME_AND_PORT`
      - `REPLICA_SET_NAME`
      - `TYPE_NAME`

    - Replica set alerts support these fields:

      - `REPLICA_SET_NAME`
      - `SHARD_NAME`
      - `CLUSTER_NAME`

    - Sharded cluster alerts support these fields:

      - `CLUSTER_NAME`
      - `SHARD_NAME`

    All other types of alerts do not support matchers.

* - matchers.operator
  - string
  - Operator to test the field's value. Accepted values are:

    - `EQUALS`
    - `NOT_EQUALS`
    - `CONTAINS`
    - `NOT_CONTAINS`
    - `STARTS_WITH`
    - `ENDS_WITH`
    - `REGEX`

* - matchers.value
  - string
  - Value to test with the specified operator.

    If `matchers.fieldName` is set to `TYPE_NAME`, you can match on
    the following values:

    - `PRIMARY`
    - `SECONDARY`
    - `STANDALONE`
    - `CONFIG`
    - `MONGOS`

* - matchers
  - object array
  - Rules to apply when matching an object against this alert 
    configuration. Only entities that match *all* these rules are 
    checked for an alert condition.

    You can filter using the `matchers` array only when the
    `eventTypeName` specifies an event for a host, replica set, 
    or sharded cluster.

* - metricThreshold.metricName
  - string
  - Name of the metric to check. Supports the same values as 
    the `metricName` field of the `alerts` resource.

* - metricThreshold.mode
  - string
  - Set to `AVERAGE` to compute the average of this metric.

* - metricThreshold.operator
  - string
  - Operator to apply when checking the current metric value
    against the threshold value. Accepted values are:

    - `GREATER_THAN`

    - `LESS_THAN`

* - metricThreshold.threshold
  - number
  - Threshold value outside of which an alert is triggered.

* - metricThreshold.units
  - string
  - Units for the threshold value. Depends on the type of 
    metric. 

    **Example:**

    A metric that measures memory consumption would have a 
    byte measurement, while a metric that measures time would 
    have a time unit.

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

* - metricThreshold
  - object
  - Threshold that will cause an alert to be triggered. 
    Required if `"eventTypeName" : "OUTSIDE_METRIC_THRESHOLD"`.

* - notifications.apiToken
  - string
  - Slack API token or Bot token.
    Required if `"notifications.typeName" : "SLACK"`.
    If the token later becomes invalid, Ops Manager sends an email to 
    the Project owner and eventually removes the token.

    After you create a third-party integration that requires an API or 
    integration key, the key appears partially redacted when you: 

    - View or edit the alert through the UI.
    - Query the third-party integration settings through the API (Application Programming Interface).

* - notifications.channelName
  - string
  - Slack channel name.
    Required if `"notifications.typeName" : "SLACK"`.

* - notifications.datadogApiKey
  - string
  - DataDog API Key. Found in the DataDog dashboard.
    Required if `"notifications.typeName" : "DATADOG"`.    

    After you create a third-party integration that requires an API or 
    integration key, the key appears partially redacted when you: 

    - View or edit the alert through the UI.
    - Query the third-party integration settings through the API (Application Programming Interface).

* - notifications.delayMin
  - number
  - Number of minutes to wait after an alert condition is 
    detected before sending out the first notification.

* - notifications.emailAddress
  - string
  - Email address to which to send notification.
    Required if `"notifications.typeName" : "EMAIL"`.

* - notifications.emailEnabled
  - boolean
  - Determines if email notifications should be sent.
    Required if:

    - `"notifications.typeName" : "GROUP"`
    - `"notifications.typeName" : "USER"`

* - notifications.intervalMin
  - number
  - Number of minutes to wait between successive notifications 
    for unacknowledged alerts that are not resolved.

* - notifications.webhookSecret
  - string
  - A value used to authenticate with the Webhook that accepts 
    and forwards the notification. You can explicitly declare 
    a secret only in a request that has both:

    - A `notifications.typeName` of `WEBHOOK`

    - An explicitly declared `notifications.webhookURL`

    You can configure a `webhookSecret` for a default 
    `webhookURL` only either on the 
    Integrations 
    page, or with the Integrations API.

    To explicitly declare a `webhookURL` without a 
    `webhookSecret`, omit this field.

    After creating a webhook notification, the URL is
    partially redacted when you view or edit the alert, and the
    secret is completely redacted.

* - notifications.webhookUrl
  - string
  - URL (Uniform Resource Locator) for the webhook that triggers this notification. If you do not
    explicitly declare a `webhookUrl`, your request will use
    the default `webhookUrl` set either on the
    Integrations
    page, or with the Integrations API.

    After creating a webhook notification, the URL is
    partially redacted when you view or edit the alert, and the
    secret is completely redacted.

* - notifications.webhookHeadersTemplate
  - string
  - Template for custom headers to include in webhook notifications.
    You can use variables in the template that are replaced with
    alert-specific values when the notification is sent.

* - notifications.webhookBodyTemplate
  - string
  - Template for the body content of webhook notifications.
    You can use variables in the template that are replaced with
    alert-specific values when the notification is sent.

* - notifications.microsoftTeamsWebhookUrl
  - string
  - Microsoft Teams channel incoming webhook URL.
    Required if `"notifications.typeName" : "MICROSOFT_TEAMS"`.

    When you view or edit the alert for a webhook 
    notification, the URL appears partially redacted, and the
    secret appears completely redacted.

* - notifications.mobileNumber
  - string
  - Mobile number to send SMS messages to.
    Required if `"notifications.typeName" : "SMS"`.

* - notifications.notificationToken
  - string
  - A HipChat API token.
    Required if `"notifications.typeName" : "HIP_CHAT"`.
    If the token later becomes invalid, Ops Manager sends an email to 
    the Project owner and eventually removes the token.

    After you create a third-party integration that requires an API or 
    integration key, the key appears partially redacted when you: 

    - View or edit the alert through the UI.
    - Query the third-party integration settings through the API (Application Programming Interface).

* - notifications.role
  - string
  - Ops Manager role in current Project.
    Required if `"notifications.typeName" : "GROUP"`.

* - notifications.roomName
  - string
  - HipChat room name.
    Required if `"notifications.typeName" : "HIP_CHAT"`.

* - notifications.serviceKey
  - string
  - PagerDuty integration key.
    Required if `"notifications.typeName" : "PAGER_DUTY"`.

    After you create a third-party integration that requires an API or 
    integration key, the key appears partially redacted when you: 

    - View or edit the alert through the UI.
    - Query the third-party integration settings through the API (Application Programming Interface).

* - notifications.smsEnabled
  - boolean
  - Flag indicating SMS notifications must be sent.
    Required if:

    - `"notifications.typeName" : "GROUP"`
    - `"notifications.typeName" : "USER"`

* - notifications.teamId
  - string
  - Unique identifier of a team.

* - notifications.typeName
  - string
  - Type of alert notification. Accepted values are:

    - `DATADOG`
    - `EMAIL`
    - `GROUP` (Project)
    - `HIPCHAT`
    - `ORG`
    - `PAGER_DUTY`
    - `SLACK`
    - `SMS` (Twilio integration must be configured)
    - `USER`
    - `WEBHOOK`

* - notifications.username
  - string
  - Name of an Ops Manager user to which to send notifications. 
    Specify a user in the Project that owns the alert
    configuration. 
    Required if `"notifications.typeName" : "USER"`.

* - | notifications
    | *Required*
  - object array
  - Notifications to send when an alert condition is 
    detected.

* - threshold.operator
  - string
  - Operator to apply when checking the current metric value
    against the threshold value.

    - `GREATER_THAN`

    - `LESS_THAN`

* - threshold.threshold
  - number
  - Threshold value outside of which an alert is triggered.

* - threshold
  - object
  - Threshold that will cause an alert to be triggered.
    Required if:

    - `"eventTypeName" : "TOO_FEW_HEALTHY_MEMBERS"`

    - `"eventTypeName" : TOO_MANY_UNHEALTHY_MEMBERS`

## Response

The response includes the alert configuration details:

**Note:**

Alert configurations vary. An alert configuration may only
include a subset of these elements.

* - Name
  - Type
  - Description

* - created
  - string
  - Timestamp in ISO 8601 date and time format in UTC (Coordinated Universal Time) when this alert configuration was created.

* - enabled
  - boolean
  - Flag indicating this alert configuration enabled.

* - eventTypeName
  - string
  - Type of event that triggers an alert.

* - groupId
  - string
  - Unique identifier of the Project that owns this alert
    configuration.

* - id
  - string
  - Unique identifier of the alert configuration.

* - links
  - array of objects
  - .. include:: /includes/links-explanation.rst

* - matchers
  - array of objects
  - Rules to apply when matching an object against this alert
    configuration.

* - | matchers
    | .[n].fieldName
  - string
  - Name of the field in the target object that you wanted this
    configuration to match.

* - | matchers
    | .[n].operator
  - string
  - Comparison operator to apply when checking the current metric
    value against `matcher.[n].value`.

* - | matchers
    | .[n].value
  - string
  - Value to match or exceed using `matchers.[n].operator`.

* - metricThreshold
  - object
  - Value and means of comparison that triggers an alert.

* - | metricThreshold
    | .metricName
  - string
  - Name of the metric to check. Supports the same values as
    the `metricName` field of the `alerts` resource.

* - | metricThreshold
    | .mode
  - string
  - Average value of this metric.

* - | metricThreshold
    | .operator
  - string
  - Comparison operator that Ops Manager applied when checking the
    current metric value against the threshold value.

* - | metricThreshold
    | .threshold
  - number
  - Value of `metricThreshold.metricName` that, when exceeded,
    triggers an alert.

* - | metricThreshold
    | .units
  - string
  - Units of capacity or time that define the scope of the
    `metricThreshold.threshold`.

* - notifications
  - array of objects
  - One or more targets for Ops Manager to send notifications when
    an alert condition is detected.

* - | notifications.[n]
    | .apiToken
  - string
  - Slack API token token. Ops Manager returns this value if you
    set `notifications.[n].typeName` to `SLACK`.

    After you create a third-party integration that requires an API or 
    integration key, the key appears partially redacted when you: 

    - View or edit the alert through the UI.
    - Query the third-party integration settings through the API (Application Programming Interface).

* - | notifications.[n]
    | .channelName
  - string
  - Slack channel name. Ops Manager returns this value if you set
    `notifications.[n].typeName` to `SLACK`.

* - | notifications.[n]
    | .datadogApiKey
  - string
  - DataDog API Key. Ops Manager returns this value if you set
    `notifications.[n].typeName` to `DATADOG`.

    After you create a third-party integration that requires an API or 
    integration key, the key appears partially redacted when you: 

    - View or edit the alert through the UI.
    - Query the third-party integration settings through the API (Application Programming Interface).

* - | notifications.[n]
    | .delayMin
  - number
  - Number of minutes to wait after an alert condition is
    detected before sending out the first notification.

* - | notifications.[n]
    | .emailAddress
  - string
  - Email address to which to send notification. Ops Manager
    returns this value if you set `notifications.[n].typeName`
    to `EMAIL`.

* - | notifications.[n]
    | .emailEnabled
  - boolean
  - Flag indicating email notifications must be sent. Ops Manager
    returns this value if you set `notifications.[n].typeName`
    to `ORG`, `GROUP`, or `USER`.

* - | notifications.[n]
    | .intervalMin
  - number
  - Number of minutes to wait between successive notifications
    for unacknowledged alerts that are not resolved.

* - | notifications.[n]
    | .microsoftTeamsWebhookUrl
  - string
  - Microsoft Teams channel incoming webhook URL.
    Ops Manager returns this value if
    you set `notifications.[n].typeName` to `MICROSOFT_TEAMS`.

    When you view or edit the alert for a webhook 
    notification, the URL appears partially redacted, and the
    secret appears completely redacted.

* - | notifications.[n]
    | .mobileNumber
  - string
  - Mobile number to which alert notifications are sent.
    Ops Manager returns this value if you set
    `notifications.[n].typeName` to `SMS`.

* - | notifications.[n]
    | .notificationToken
  - string
  - HipChat API token. Ops Manager returns this value if you set
    `notifications.[n].typeName` to `HIP_CHAT`.

    If the token later becomes invalid, MongoDB Atlas sends an email to the
    `Project Owner` and eventually removes the token.

    After you create a third-party integration that requires an API or 
    integration key, the key appears partially redacted when you: 

    - View or edit the alert through the UI.
    - Query the third-party integration settings through the API (Application Programming Interface).

* - | notifications.[n]
    | .opsGenieApiKey
  - string
  - [OpsGenie Alert API](https://docs.opsgenie.com/docs/alert-api) 
    key. Ops Manager returns this value if
    you set `notifications.[n].typeName` to `OPS_GENIE`.

    After you create a third-party integration that requires an API or 
    integration key, the key appears partially redacted when you: 

    - View or edit the alert through the UI.
    - Query the third-party integration settings through the API (Application Programming Interface).

* - | notifications.[n]
    | .opsGenieRegion
  - string
  - Region that indicates which API (Application Programming Interface) URL (Uniform Resource Locator) to use. Ops Manager
    returns this value if you set `notifications.[n].typeName`
    to `OPS_GENIE`.

* - | notifications.[n]
    | .roles
  - array of strings
  - Ops Manager role in current Project or Organization. Ops Manager
    returns this value if you set `notifications.[n].typeName`
    to `ORG` or `GROUP`.

* - | notifications.[n]
    | .roomName
  - string
  - HipChat room name. Ops Manager returns this value if
    `"notifications.typeName" : "HIP_CHAT`.

* - | notifications.[n]
    | .serviceKey
  - string
  - PagerDuty service key. Ops Manager returns this value if
    you set `notifications.[n].typeName` to `PAGER_DUTY`.

    After you create a third-party integration that requires an API or 
    integration key, the key appears partially redacted when you: 

    - View or edit the alert through the UI.
    - Query the third-party integration settings through the API (Application Programming Interface).

* - | notifications.[n]
    | .smsEnabled
  - boolean
  - Flag indicating text notifications must be sent. Ops Manager
    returns this value if you set `notifications.[n].typeName`
    to `ORG`, `GROUP`, or `USER`.

* - | notifications.[n]
    | .teamId
  - string
  - Unique identifier of the team that receives this
    notification.

* - | notifications.[n]
    | .teamName
  - string
  - Label for the team that receives this notification.

* - | notifications.[n]
    | .typeName
  - string
  - Means by which you want Ops Manager to send you notification of
    an alert.

* - | notifications.[n]
    | .username
  - string
  - Name of an Ops Manager user to which to send notifications.
    Ops Manager returns this value if you set
    `notifications.[n].typeName` to `USER`.

* - | notifications.[n]
    | .victorOpsApiKey
  - string
  - VictorOps API (Application Programming Interface) key.

    If the key later becomes invalid, MongoDB Atlas sends an email to the
    `Project Owner` and eventually removes the key.

    Ops Manager returns this value if you set
    `notifications.[n].typeName` to `VICTOR_OPS`.

    After you create a third-party integration that requires an API or 
    integration key, the key appears partially redacted when you: 

    - View or edit the alert through the UI.
    - Query the third-party integration settings through the API (Application Programming Interface).

* - | notifications.[n]
    | .victorOpsRoutingKey
  - string
  - VictorOps routing key.

    If the key later becomes invalid, MongoDB Atlas sends an email to the
    `Project Owner` and eventually removes the key.

    Ops Manager returns this value if you set
    `notifications.[n].typeName` to `VICTOR_OPS`.

* - | notifications.[n]
    | .webhookSecret
  - string
  - A value used to authenticate with the Webhook that accepts 
    and forwards the notification.

    Ops Manager returns this value if you set
    `notifications.[n].typeName` to `WEBHOOK` and either:

    - You set `notification.[n].webhookSecret` to a non-empty 
      string

    - You set a default `webhookSecret` either on the 
      Integrations page, or with
      the Integrations API

    After creating a webhook notification, the URL is
    partially redacted when you view or edit the alert, and the
    secret is completely redacted.

* - | notifications.[n]
    | .webhookUrl
  - string
  - URL (Uniform Resource Locator) for the webhook that triggers this notification.

    Ops Manager returns this value if you set
    `notifications.[n].typeName` to `WEBHOOK` and either:

    - You set `notification.[n].webhookURL` to a non-empty string

    - You set a default `webhookUrl` either on the
      Integrations page, or with
      the Integrations API

    After creating a webhook notification, the URL is
    partially redacted when you view or edit the alert, and the
    secret is completely redacted.

* - | notifications.[n]
    | .webhookHeadersTemplate
  - string
  - Template for custom headers to include in webhook notifications.
    Ops Manager returns this value if you set
    `notifications.[n].typeName` to `WEBHOOK` and provide a
    custom headers template.

* - | notifications.[n]
    | .webhookBodyTemplate
  - string
  - Template for the body content of webhook notifications.
    Ops Manager returns this value if you set
    `notifications.[n].typeName` to `WEBHOOK` and provide a
    custom body template.

* - | notifications.[n]
    | .id
  - string
  - Unique identifier of the notification configuration.

* - threshold
  - object
  - Threshold that triggers an alert. Ops Manager returns this
    value if `eventTypeName` is any value other than
    `OUTSIDE_METRIC_THRESHOLD`.

* - | threshold
    | .operator
  - string
  - Comparison operator that Ops Manager applied when checking the
    current metric value against the threshold value.

* - | threshold
    | .threshold
  - number
  - Value that, when exceeded, Ops Manager triggers an alert.

* - | threshold
    | .units
  - string
  - Units of capacity or time that define the scope of the
    `threshold.threshold`.

* - typeName
  - string
  - *This field is deprecated and is ignored.*

* - updated
  - string
  - Timestamp in ISO 8601 date and time format in UTC (Coordinated Universal Time) when this alert configuration was last
    updated.

## Example Request

```sh
curl --user "{PUBLIC-KEY}:{PRIVATE-KEY}" --digest \
 --header "Accept: application/json" \
 --header "Content-Type: application/json" \
 --include \
 --request POST "https://<ops-manager-host>/api/public/v1.0/groups/{PROJECT-ID}/alertConfigs" \
 --data '
   {
     "eventTypeName" : "RESYNC_REQUIRED",
     "enabled" : true,
     "notifications" : [ {
       "typeName" : "GROUP",
       "intervalMin" : 5,
       "delayMin" : 0,
       "smsEnabled" : false,
       "emailEnabled" : true
     } ]
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
  "created" : "2014-04-23T14:29:18Z",
  "enabled" : true,
  "groupId" : "{PROJECT-ID}",
  "id" : "{ALERT-CONFIG-ID}",
  "links" : [],
  "matchers" : [ ],
  "notifications" : [ {
    "delayMin" : 0,
    "emailEnabled" : true,
    "intervalMin" : 5,
    "smsEnabled" : false,
    "typeName" : "GROUP"
  } ],
  "updated" : "2014-04-23T14:29:18Z"
}
```
