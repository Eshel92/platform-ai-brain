<!-- Converted from reference/api/global-alert-configurations-toggle-one.txt (reStructuredText). Includes are inlined. -->

# Enable or Disable One Global Alert Configuration

Enable or disable one global alert configuration identified by its 
`GLOBAL-ALERT-CONFIG-ID`.

## Required Roles

You can successfully call this endpoint with any of the following 
assigned roles:

- `Global Owner`
- `Global Monitoring Admin`

## Request

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

```http
PUT /globalAlertConfigs/{GLOBAL-ALERT-CONFIG-ID}
```

### Request Path Parameters

| Name | Type | Necessity | Description |
|---|---|---|---|
| `{GLOBAL-ALERT-CONFIG-ID}` | string | Required | Unique identifier of the global alert configuration you want to enable or disable. |

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

* - Body Parameter
  - Type
  - Necessity
  - Description

* - `enabled`
  - boolean
  - Required
  - Toggle indicating whether the global alert configuration is 
    enabled or disabled:

    - Set to `true` to enable a global alert configuration. 
    - Set to `false` to disable a global alert configuration.

## Response

* - Name
  - Type
  - Description

* - `created`
  - string
  - Timestamp in ISO 8601 date and time format in UTC (Coordinated Universal Time) when the alert configuration was created.

* - `enabled`
  - boolean
  - Toggle that specifies whether the alert configuration is enabled.

* - `eventTypeName`
  - string
  - Type of event for which this alert configuration triggers
    an alert.

    To review the types of events that generate alerts, see
    Alert Types.

    For a complete list of events included in the Ops Manager audit log, see
    Audit Events.

* - `forAllGroups`
  - boolean
  - Toggle that specifies whether the global alert configuration 
    applies to all groups. Also affects whether you can use the 
    `tags` array to target the configuration to specific groups.

    If `true`, the configuration applies to all groups. You can 
    target the alert configuration to specific groups through the 
    `tags` array.

    If `false`, the configuration applies only to the groups
    specified in the `groupIds` array. You must specify at 
    least one project in the `groupIds` array. You can't use the 
    `tags` array for this alert configuration.

* - `groupIds`
  - array of strings
  - IDs of the groups to which this alert configuration applies. 
    This field applies only if `forAllGroups` is set to `false`.

* - `id`
  - string
  - Unique identifier of the alert configuration.

* - `matchers`
  - array of objects
  - Rules to apply when matching an object against this global alert
    configuration. Ops Manager only checks entities that match *all* these 
    rules for an alert condition.

    You can filter using the `matchers` array only when the
    `eventTypeName` specifies an event for a host, replica set, or
    sharded cluster.

* - `matchers.fieldName`
  - string
  - Name of the field in the target object on which to match.

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

* - `matchers.operator`
  - string
  - Operator to test the field's value. Possible values are:

    - `EQUALS`
    - `NOT_EQUALS`
    - `CONTAINS`
    - `NOT_CONTAINS`
    - `STARTS_WITH`
    - `ENDS_WITH`
    - `REGEX`

* - `matchers.value`
  - string
  - Value to test with the specified operator.

    If `matchers.fieldName` is set to `TYPE_NAME`, you can match on
    the following values:

    - `PRIMARY`
    - `SECONDARY`
    - `STANDALONE`
    - `CONFIG`
    - `MONGOS`

* - `metricThreshold`
  - object
  - Threshold that causes this alert configuration to trigger
    an alert. Only present if `eventTypeName` is set to 
    `OUTSIDE_METRIC_THRESHOLD`.

* - `metricThreshold.metricName`
  - string
  - Name of the metric to check. Supports the same values as the
    `metricName` field of the `globalAlerts` resource. For a list 
    of possible values, see 
    measurement-types-for-global-alerts-api.

* - `metricThreshold.mode`
  - string
  - This is set to `AVERAGE` and computes the current metric value 
    as an average.

* - `metricThreshold.operator`
  - string
  - Operator to apply when checking the current metric value 
    against `metricThreshold.threshold`. Possible values are:

    - `GREATER_THAN`
    - `LESS_THAN`

* - `metricThreshold.threshold`
  - number
  - Threshold value outside of which this alert configuration
    triggers an alert.

* - `metricThreshold.units`
  - string
  - Units for `metricThreshold.threshold`. The units depend on
    the type of metric. 

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

* - `notifications`
  - array of objects
  - Notifications Ops Manager sends when it detects an alert that this 
    alert configuration describes.

* - `notifications.apiToken`
  - string
  - Slack API token or Bot token. Only present for `SLACK`
    notifications. If the token later becomes invalid, Ops Manager sends an
    email to the project owner and removes the token.

    After you create a third-party integration that requires an API or 
    integration key, the key appears partially redacted when you: 

    - View or edit the alert through the UI.
    - Query the third-party integration settings through the API (Application Programming Interface).

* - `notifications.channelName`
  - string
  - Slack channel name. Only present for `SLACK` notifications.

* - `notifications.delayMin`
  - number
  - Number of minutes to wait after an alert condition is 
    detected before Ops Manager sends out the first notification.

* - `notifications.emailAddress`
  - string
  - Email address to which to send notification. Only present for
    `EMAIL` notifications.

* - `notifications.emailEnabled`
  - boolean
  - Toggle specifying whether Ops Manager sends email notifications. 
    Only present for `GROUP` and `USER` notifications.

* - `notifications.intervalMin`
  - number
  - Number of minutes to wait between successive notifications 
    for unacknowledged, unresolved alerts that this alert 
    configuration triggers.

* - | notifications.[n]
    | .webhookSecret
  - string
  - A value used to authenticate with the Webhook that accepts and
    forwards the notification.

    Ops Manager returns this value if you set
    `notifications.[n].typeName` to `WEBHOOK` and either:

    - You set `notification.[n].webhookSecret` to a non-empty 
      string

    - You set a default `webhookSecret` on the 
      Admin Console.

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

    - You set a default `webhookUrl` on the
      Admin Console page.

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

* - `notifications.microsoftTeamsWebhookUrl`
  - string
  - Microsoft Teams channel incoming webhook URL. Only present 
    for `MICROSOFT_TEAMS` notifications.

    When you view or edit the alert for a webhook 
    notification, the URL appears partially redacted, and the
    secret appears completely redacted.

* - `notifications.notificationToken`
  - string
  - HipChat API token. Only present for `HIP_CHAT` notifications.
    If the token later becomes invalid, Ops Manager sends an email to the 
    project owner and removes the token.

    After you create a third-party integration that requires an API or 
    integration key, the key appears partially redacted when you: 

    - View or edit the alert through the UI.
    - Query the third-party integration settings through the API (Application Programming Interface).

* - `notifications.roomName`
  - string
  - HipChat room name. Only present for `HIP_CHAT` notifications.

* - `notifications.serviceKey`
  - string
  - PagerDuty integration key. Only present for `PAGER_DUTY` 
    notifications. If the key later becomes invalid, Ops Manager sends an 
    email to the project owner and removes the key.

    After you create a third-party integration that requires an API or 
    integration key, the key appears partially redacted when you: 

    - View or edit the alert through the UI.
    - Query the third-party integration settings through the API (Application Programming Interface).

* - `notifications.smsEnabled`
  - boolean
  - Toggle specifying whether Ops Manager sends SMS notifications. Only 
    present for `GROUP` and `USER` notifications.

* - `notifications.typeName`
  - string
  - Type of alert notification this alert configuration triggers. 
    Possible values are:

    - `ADMIN`
    - `GROUP`
    - `USER`
    - `EMAIL`
    - `SMS` (Available only if Ops Manager is configured for Twilio integration.)
    - `HIPCHAT`
    - `SLACK`
    - `PAGER_DUTY`

* - `notifications.username`
  - string
  - Name of the Ops Manager user to whom to send notifications. Only
    present for `USER` notifications.

* - `threshold`
  - object
  - Threshold that causes this alert configuration to trigger
    an alert. Only present if `eventTypeName` is set to one of the 
    following values:

    - `TOO_FEW_HEALTHY_MEMBERS`
    - `TOO_MANY_UNHEALTHY_MEMBERS`

* - `threshold.operator`
  - string
  - Operator to apply when checking the current metric value against
    `threshold.threshold`. Possible values are:

    - `GREATER_THAN`
    - `LESS_THAN`

* - `threshold.threshold`
  - number
  - Threshold value outside of which this alert configuration
    triggers an alert.

* - `tags`
  - array of strings
  - Tags associated with this alert configuration.

* - `typeName`
  - string
  - *This field is deprecated and will be ignored.*

* - `updated`
  - string
  - Timestamp in ISO 8601 date and time format in UTC (Coordinated Universal Time) when this alert configuration was last updated.

## Example Request

```sh
curl --user "{PUBLIC-KEY}:{PRIVATE-KEY}" --digest \
     --header "Accept: application/json" \
     --header "Content-Type: application/json" \
     --include \
     --request PUT "https://<OpsManagerHost>:<Port>/api/public/v1.0/globalAlertConfigs/{GLOBAL-ALERT-CONFIG-ID}" \
     --data '{
       "enabled" : false
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
  "created": "2019-10-02T12:34:04Z",
  "enabled": false,
  "eventTypeName": "BACKUP_AGENT_DOWN",
  "forAllGroups": true,
  "groupIds": [],
  "id": "{GLOBAL-ALERT-CONFIG-ID}",
  "links": [
  ],
  "matchers": [],
  "notifications": [
    {
      "delayMin": 0,
      "intervalMin": 60,
      "typeName": "ADMIN"
    }
  ],
  "tags": [],
  "typeName": "AGENT",
  "updated": "2019-10-02T12:34:04Z"
}
```
