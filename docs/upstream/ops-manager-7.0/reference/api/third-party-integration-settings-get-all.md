<!-- Converted from reference/api/third-party-integration-settings-get-all.txt (reStructuredText). Includes are inlined. -->

# Get All Configurations for Third-Party Service Integrations

**Note:**

Groups and projects are synonymous terms. Your `{PROJECT-ID}` is the
same as your project id. For existing groups, your group/project id
remains the same. This page uses the more familiar term group when
referring to descriptions. The endpoint remains as stated in the
document.

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

## Syntax

```http
GET /api/public/v1.0/groups/{GROUP-ID}/integrations
```

### Request Path Parameters

| Parameter | Necessity | Description |
|---|---|---|
| `{PROJECT-ID}` | Required | Project identifier. |

### Request Query Parameters

| Name | Type | Necessity | Description | Default |
|---|---|---|---|---|
| pageNum | number | Optional | One-based integer that returns a subsection of results. | `1` |
| itemsPerPage | number | Optional | Number of items to return per page, up to a maximum of 500. | `100` |
| pretty | boolean | Optional | Flag that indicates whether the response body should be in a prettyprint format. | `false` |
| envelope | boolean | Optional | Flag that indicates whether or not to wrap the response in an envelope. Some API (Application Programming Interface) clients cannot access the HTTP (Hypertext Transfer Protocol) response headers or status code. To remediate this, set `envelope : true` in the query. For endpoints that return a list of results, the `results` object is an envelope. Ops Manager adds the `status` field to the response body. | `false` |
| backupJobsEnabledOnly | boolean | Optional | Flag indicating whether to exclude daemons not enabled for backing up databases from the response. Set this to `false` to include daemon configurations with the `backupJobsEnabled` flag set to `false`. | `true` |

### Request Body Parameters

This endpoint doesn't use HTTP request body parameters.

## Response Elements

The response includes a `results` array which lists all third-party
integration configurations for the project as objects, and a
`totalCount` of the services integrated with the project.

Each third-party integration configuration object includes a `type`
property equal to its own integration type (e.g. ``"type":
"PAGER_DUTY"`` for the PagerDuty service). Additionally, each
third-party service configuration object provides details specific to
that service. The following lists the properties returned for each
third-party service configuration object:

* - Service
  - Result

* - PagerDuty
  - A returned PagerDuty integration configuration object
    contains the following fields:

    * - Property
      - Description

    * - `type`
      - `PAGER_DUTY`

    * - `serviceKey`
      - Your Service Key.

        After you create a third-party integration that requires an API or 
        integration key, the key appears partially redacted when you: 

        - View or edit the alert through the UI.
        - Query the third-party integration settings through the API (Application Programming Interface).

* - Slack
  - A returned Slack integration configuration object
    contains the following fields:

    * - Property
      - Description

    * - `type`
      - `SLACK`

    * - `apiToken`
      - Your API Token.

        After you create a third-party integration that requires an API or 
        integration key, the key appears partially redacted when you: 

        - View or edit the alert through the UI.
        - Query the third-party integration settings through the API (Application Programming Interface).

    * - `teamName`
      - Your team name. This field may not be present with a
        legacy Slack integration.

    * - `channelName`
      - The configured Slack channel name. An empty string if
        the value is not set.

* - Datadog

  - A returned Datadog integration configuration object
    contains the following fields:

    * - Property
      - Description

    * - `type`
      - `DATADOG`

    * - `apiKey`
      - Your API Key.

        After you create a third-party integration that requires an API or 
        integration key, the key appears partially redacted when you: 

        - View or edit the alert through the UI.
        - Query the third-party integration settings through the API (Application Programming Interface).

* - HipChat
  - A returned HipChat integration configuration object
    contains the following fields:

    * - Property
      - Description

    * - `type`
      - `HIP_CHAT`

    * - `notificationToken`
      - Notification token for your HipChat user account.

        After you create a third-party integration that requires an API or 
        integration key, the key appears partially redacted when you: 

        - View or edit the alert through the UI.
        - Query the third-party integration settings through the API (Application Programming Interface).

    * - `roomName`
      - Your HipChat room name.

* - Opsgenie
  - A returned Opsgenie integration configuration object
    contains the following fields:

    * - Property
      - Description

    * - `type`
      - `OPS_GENIE`

    * - `apiKey`
      - Your API Key.

        After you create a third-party integration that requires an API or 
        integration key, the key appears partially redacted when you: 

        - View or edit the alert through the UI.
        - Query the third-party integration settings through the API (Application Programming Interface).

    * - `region`
      - Indicates which API (Application Programming Interface) URL (Uniform Resource Locator) to use, either `US` or
        `EU`. Opsgenie defaults to `US`.

    To set `region` to `EU`, you must set a
    customer setting of
    `opsgenie.api.url`.

* - VictorOps
  - A returned VictorOps integration configuration object
    contains the following fields:

    * - Property
      - Description

    * - `type`
      - `VICTOR_OPS`

    * - `apiKey`
      - Your API Key.

        After you create a third-party integration that requires an API or 
        integration key, the key appears partially redacted when you: 

        - View or edit the alert through the UI.
        - Query the third-party integration settings through the API (Application Programming Interface).

    The configuration object may also contain the following
    fields, depending on your configuration:

    | Property | Description |
    |---|---|
    | `routingKey` | An optional field returned if you have a Routing Key configured. |

* - Webhook Settings
  - A returned webhook configuration object
    contains the following fields:

    | Property | Description |
    |---|---|
    | `type` | `WEBHOOK` |
    | `url` | Your webhook URL. After creating a webhook notification, the URL is partially redacted when you view or edit the alert, and the secret is completely redacted. |

    The configuration object may also contain the following
    fields, depending on your configuration:

    | Property | Description |
    |---|---|
    | `secret` | An optional field returned if your webhook is configured with a secret. |

* - Microsoft Teams
  - A returned Microsoft Teams configuration object will
    contain the following fields:

    | Property | Description |
    |---|---|
    | `type` | `MICROSOFT_TEAMS` |
    | `microsoftTeamsWebhookUrl` | Your Microsoft Teams incoming webhook URL. When you view or edit the alert for a webhook notification, the URL appears partially redacted, and the secret appears completely redacted. |

* - Prometheus
  - A returned Prometheus configuration object will
    contain the following fields:

    | Property | Description |
    |---|---|
    | `type` | `PROMETHEUS` |
    | `username` | Your Prometheus username. |
    | `listenAddress` | The IP address and port your Prometheus instance will reach out to. |
    | `serviceDiscovery` | Indicates which service discovery method is used, either `file` or `http`. |
    | `scheme` | Your Prometheus protocol scheme configured for requests, either `http` or `https`. If you configure `https`, you must specify `tlsPemPath`. |
    | `enabled` | Whether your cluster has Prometheus enabled. |

    The configuration object may also contain the following
    fields, depending on your configuration:

    | Property | Description |
    |---|---|
    | `tlsPemPassword` | An optional field returned if you have a password for your PEM file. |
    | `tlsPemPath` | An optional field returned if you have an absolute path to your PEM file. |

## Example Request

```sh
curl --user "{PUBLIC-KEY}:{PRIVATE-KEY}" --digest \
     --header "Accept: application/json" \
     --include \
     --request GET "https://cloud.mongodb.com/api/public/v1.0/groups/{PROJECT-ID}/integrations"
```

## Example Response

```json
{
  "links": [
    {
      "href": "https://cloud.mongodb.com/api/public/v1.0/groups/{PROJECT-ID}/integrations?pageNum=1&itemsPerPage=100",
      "rel": "self"
    }
  ],
  "results": [
    {
      "serviceKey": "******7890",
      "type": "PAGER_DUTY"
    },
    {
      "apiToken": "******7890",
      "channelName": "My Channel",
      "teamName": "My Team",
      "type": "SLACK"
    },
  ],
  "totalCount": 2
 }
```
