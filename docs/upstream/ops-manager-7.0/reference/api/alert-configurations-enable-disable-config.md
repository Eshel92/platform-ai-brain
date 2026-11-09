<!-- Converted from reference/api/alert-configurations-enable-disable-config.txt (reStructuredText). Includes are inlined. -->

# Enable/Disable Alert Configuration

**Note:**

Groups and projects are synonymous terms. Your `{PROJECT-ID}` is the
same as your project id. For existing groups, your group/project id
remains the same. This page uses the more familiar term group when
referring to descriptions. The endpoint remains as stated in the
document.

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

## Resource

```none
PATCH /groups/{PROJECT-ID}/alertConfigs/{ALERT-CONFIG-ID}
```

**Note:**

This endpoint updates the only the enabled/disabled state for the
alert configuration. To update more than just this configuration,
see /reference/api/alert-configurations-update-config.

### Request Path Parameters

All request path parameters are *required*.

| Parameter | Type | Description |
|---|---|---|
| PROJECT-ID | string | Unique identifier for this Project. |
| ALERT-CONFIG-ID | string | Unique identifier for this alert configuration. |

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

All request body parameters are *required*.

| Parameter | Type | Description |
|---|---|---|
| enabled | boolean | Specify `true` to enable;  `false`  to disable. |

## Response

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
curl --user '{PUBLIC-KEY}:{PRIVATE-KEY}' --digest \ 
 --header 'Content-Type: application/json' \ 
 --include \ 
 --request PATCH "https://<ops-manager-host>/api/public/v1.0/groups/{PROJECT-ID}/alertConfigs/{ALERT-CONFIG-ID}" \
 --data '
   {
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
  "created" : "2014-04-23T14:52:29Z",
  "enabled" : false,
  "groupId" : "{PROJECT-ID}",
  "id" : "{ALERT-CONFIG-ID}",
  "links" : [],
  "matchers" : [ {
    "fieldName" : "REPLICA_SET_NAME",
    "operator" : "EQUALS",
    "value" : "rs1"
  } ],
  "notifications" : [ {
    "delayMin" : 5,
    "emailAddress" : "sos@example.com",
    "intervalMin" : 60,
    "typeName" : "EMAIL"
  }, {
    "delayMin" : 60,
    "emailEnabled" : false,
    "intervalMin" : 120,
    "smsEnabled" : true,
    "typeName" : "GROUP"
  } ],
  "updated" : "2014-04-23T14:52:29Z"
}
```
