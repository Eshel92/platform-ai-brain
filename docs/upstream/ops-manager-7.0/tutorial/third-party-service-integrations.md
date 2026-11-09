<!-- Converted from tutorial/third-party-service-integrations.txt (reStructuredText). Includes are inlined. -->

# Third-Party Service Integrations

You can integrate Ops Manager with third-party monitoring services to
view and analyze performance metrics
that Ops Manager collects about your cluster.

## Required Access

To view or modify third-party integration settings, you must have
`Project Monitoring Admin` access to the project.

**Warning:**

If you are integrating with Slack, before proceeding, you must
complete the steps to integrate with Slack.

## View / Modify Third-Party Settings

To modify third-party integration settings:

**Step 1: Navigate to the Integrations page for your project.**

a. If it is not already displayed, select the organization that
   contains your desired project from the `office` Organizations menu in the
   navigation bar.

#. If it is not already displayed, select your desired project
   from the Projects menu in the navigation bar.

#. Next to the Projects menu, expand the
   Options menu, then click Integrations.

**Step 2: Click Configure for the third-party service you want to modify.**

You can set the following:

* - Setting

  - Description

* - PagerDuty Integration Key

  - Default service key for alert notifications sent to a
    [PagerDuty](http://www.pagerduty.com/?utm_source=mongodb&utm_medium=docs&utm_campaign=partner)
    account. Ops Manager enters the key by default when you add a
    PagerDuty notification to an alert configuration. If you add
    PagerDuty notifications and if the key used to send the
    notifications becomes invalid, Ops Manager sends an email to the
    project owner and eventually removes the key.

    You can add PagerDuty notifications only for alerts that require
    user acknowledgement. Informational alerts, such as the alert
    that a replica set has elected a new primary, cannot use
    PagerDuty notification.

    Users can acknowledge PagerDuty alert notifications only from
    the PagerDuty dashboard.

    **Important:**

    Changing the Integration Key doesn't change any alerts that use this
    integration. Those alerts still use the previous Integration Key.

    Remove and re-add each PagerDuty notification(s) to use the new key.

    All new PagerDuty keys use their [Events API v2](https://developer.pagerduty.com/docs/ZG9jOjExMDI5NTgw-events-api-v2-overview). 
    If you have an Events API v1 key, you can continue to use that key 
    with Ops Manager. 

* - HipChat Settings

  - Default room and API (Application Programming Interface) token for alert notifications sent to
    a HipChat account. Ops Manager enters the values by default when
    you add a HipChat notification to an alert configuration.
    If you add HipChat notifications and the token used to send
    notifications becomes invalid, Ops Manager sends an email to the
    `Project Owner` and eventually removes the token.

* - Slack Settings

    **Important:**

    Before proceeding, you must complete the steps to 
    integrate with Slack.

  - Team name, API token and a channel name for
    alert notifications sent to a Slack account. You can
    configure a Slack integration with OAuth2 by clicking
    Configure and then Sign in with Slack.

    When you sign in, you are taken to a Slack landing
    page where you may select a workspace and configure permissions.
    After configuring Slack to connect to Ops Manager, your API token
    is automatically generated and maintained. You will be
    redirected back to the Integrations page.

    After initially configuring Slack with Ops Manager, you can
    Edit or Remove the integration. Editing
    the integration will display your team name and API (Application Programming Interface) token, and
    allow you to change your channel name.

    **Important:** Legacy Token Deprecation

    Legacy tokens are deprecated and will be removed in a future
    version of Ops Manager. You cannot edit a legacy token
    integration. Instead, you must reconfigure your Slack
    integration with OAuth2.

* - VictorOps Settings

  - Sets an API key and Routing key for alert notifications sent to
    a Splunk On-Call (formerly VictorOps) account. Ops Manager uses
    this information as the default settings when configuring
    alerts.

    - If you have a Splunk On-Call account, enter the following
      information:

      - [Splunk On-Call REST Endpoint Integration Routing API Key](https://help.victorops.com/knowledge-base/rest-endpoint-integration-guide/)
      - [Splunk On-Call Routing Key](https://help.victorops.com/knowledge-base/routing-keys/) (optional)

    - If you don't have a Splunk On-Call account,
      [sign up for one](https://www.splunk.com/en_us/download/on-call.html).

* - Opsgenie API Key

  - API (Application Programming Interface) key for alert notifications sent to an Opsgenie
    account. Ops Manager uses this value as the default
    [OpsGenie Alert API](https://docs.opsgenie.com/docs/alert-api) 
    key when configuring alerts.

    Enter the following information from your Opsgenie account. If
    you do not have an existing Opsgenie account, you can
    [sign up](https://www.opsgenie.com/signup).

    - Opsgenie API Key
    - API Region (United States only)

* - Datadog Settings

  - Configuration Ops Manager uses to send metric data about your
    deployment to Datadog. You can view these metrics in your
    Datadog dashboards.     

    Enter the following information from your Datadog account to
    have Datadog begin tracking your Ops Manager metric data. If you
    do not have an existing Datadog account, you can sign up at
    [DataDog](https://app.datadoghq.com/signup).

    - Datadog API Key

      You might see an inaccurate health status in the following 
      scenarios:

      - If you have a network partition and the MongoDB Agent lives 
        on an isolated nde in a replica set, only pings from the 
        isolated node reach Datadog. The isolated node and 
        Ops Manager UI report the other nodes as down.
      - If you have a network partition and the MongoDB Agent lives 
        outside the impacted nodes, pings from all the nodes reach 
        Datadog, but report different statuses.
      - If all nodes are unresponsive or their state is hanging, no 
        new pings come in. The Ops Manager UI reports these nodes as 
        down, but Datadog reports them as healthy and the status 
        gets older.

      **Important:**

      If the health status is `1`, but no other metrics appear 
      in Datadog, the replica set might be down.

    **Note:**

    To allow Ops Manager to send deployment metrics to Datadog, 
    an admin must set `mms.featureFlag.monitoring.dataDogMetrics = enabled` 
    in the `conf-mms.properties` file, or 
    in the custom configuration.

    This feature flag is not enabled by default. 

    If you update this parameter via Ops Manager Admin Panel UI, 
    you do not need to restart Ops Manager Application to be in effect.

* - Webhook Settings

  - Configure webhook notifications for alert processing. You can set:

    - Webhook URL: Endpoint to which Ops Manager sends alerts
      for programmatic processing. Ops Manager sends an alert as an HTTP (Hypertext Transfer Protocol)
      POST request in which the request body contains a JSON (Javascript Object Notation)
      document that uses the same format as the Ops Manager API (Application Programming Interface)
      Alerts resource.

    - Webhook Secret: Optional secret key for webhook
      authentication and security.

    - Webhook Headers Template: Optional FreeMarker template
      for customizing HTTP headers sent with webhook requests. You can
      use variables like `{{eventTypeName}}` and `{{groupName}}` to
      include alert-specific information.

    - Webhook Body Template: Optional FreeMarker template
      for customizing the request body content. You can use variables
      like `{{eventTypeName}}` and `{{groupName}}` to include
      alert-specific information. This allows you to adapt the payload
      structure to match your target system's requirements.

    Ops Manager adds a request header called `X-MMS-Event` to
    distinguish between various alert states. The possible values
    for this header are:

    |  |  |
    |---|---|
    | `alert.open` | The alert was just opened. |
    | `alert.close` | The alert was resolved. |
    | `alert.update` | A previously opened alert is still open. |
    | `alert.acknowledge` | The alert was acknowledged. |
    | `alert.cancel` | The alert became invalid and was canceled. |
    | `alert.inform` | Represents an informational alert, which is a point-in-time event, such as "Primary Elected." |

    If you specify a key in the Webhook Secret field,
    MongoDB Ops Manager adds the `X-MMS-Signature` request header. This
    header contains the base64-encoded HMAC (hash-based message authentication code)-SHA-1 signature of the
    request body. MongoDB Ops Manager creates the signature using the provided
    secret.

    To send alert notifications to a Webhook, select the Webhook
    notification option when creating or editing an
    alert configuration. If you add a Webhook notification and
    the URL (Uniform Resource Locator) or optional key becomes invalid, Ops Manager sends an email
    to the `Project Owner` and eventually removes the
    Webhook settings.

    You can test your webhook configuration using the Test Alert
    button in the alert configuration interface.

    If your webhook requires HTTPS, you must
    import your CA certificate into the Ops Manager trust store.

    For more information about webhook templating, see
    om-webhook-templating.

* - CA Flowdock Settings

  - Sets default values for alert notifications sent to Flowdock.
    Ops Manager enters the values by default when you add a Flowdock
    notification to an alert configuration. If you add Flowdock
    notifications, and if credentials to send notifications become
    invalid, MongoDB Atlas sends an email to the project owner and
    eventually removes the credentials.

    Enter the following information from your CA Flowdock account. If
    you do not have an existing CA Flowdock account, you can
    [sign up](https://www.flowdock.com/signup).

    - Org Name
    - Flow Name
    - API Token

* - Microsoft Teams Webhook URL

  - Configures Ops Manager to send alerts about your project to 
    your [Microsoft Teams](https://www.microsoft.com/en-us/microsoft-teams/group-chat-software/)  
    channel. You can view these alerts in the 
    [Adaptive Card](https://docs.microsoft.com/en-us/microsoftteams/platform/task-modules-and-cards/cards/cards-reference#adaptive-card/) 
    displayed in your channel.

    To send alert notifications to a Microsoft Teams channel,
    you must create a Microsoft Teams incoming webhook. 
    After creating the webhook, you can use the automatically
    generated URL to configure your Microsoft Teams integration
    in Ops Manager.

    To setup the integration, see 
    Integrate with Microsoft Teams.

* - Prometheus Settings

  - Configures Ops Manager to send metric data about your deployment
    to your [Prometheus](https://prometheus.io/) instance. To setup the integration, see
    prometheus-integration-mms.

## Build Monitoring Integrations

You can build a monitoring integration using the Ops Manager 
API monitoring and alerts endpoints.
