<!-- Converted from tutorial/manage-global-alerts.txt (reStructuredText). Includes are inlined. -->

# Manage Global Alerts

## Overview

A global alert applies the same
alert configuration to
multiple projects at once. When an alert condition occurs, Ops Manager
sends notification only to the affected project. Ops Manager sends
notification at regular intervals until you
resolve or cancel
the alert.

If you acknowledge a global alert, Ops Manager sends no further
notifications to the alert’s distribution list until the
acknowledgement period has passed or until the alert resolves. If the
alert condition ends during the acknowledgment period, Ops Manager sends a
notification of the resolution.

To access global alerts you must have the
`Global Owner` role or `Global Monitoring Admin` role.

**Note:** Default Global Alerts

When Ops Manager starts, it creates
default global alert configurations.
If you delete a default global alert configuration, Ops Manager
recreates it when the application restarts.

If you don't want to receive alerts from a default global alert
configuration, you must
disable that global alert configuration.

## View Global Alerts

**Step 1: Click the Admin link at the top of Ops Manager.**

**Step 2: Select the Alerts tab and then select Open Alerts under Global Alerts.**

**Step 3: Select one or more filters above the list and click Filter.**

| To filter by: | Do this: |
|---|---|
| Acknowledgement | Select the appropriate option in the All States drop-down list. |
| Project | Type the project's name in the Projects box. |
| Project Tags | Type the tag's name in the Tags box. Users with the `Global Owner` role can assign tags to projects. |
| Alert type (open alerts only) | Type the alert type in the Types box. The box autocompletes an alert type only if there is an open alert of that type. |
| Date | Select the dates in the From and To fields. |

**Step 4: Acknowledge or unacknowledge an alert.**

To acknowlege an alert, click Acknowledge on the line for
the alert, select the time period for the acknowledgement, and click
Acknowledge. Ops Manager sends no further notifications for the
selected period.

To "undo" an acknowledgment and again receive notifications if the alert
condition still applies, click Unacknowledge on the line for
the alert and click Confirm.

## Configure a Global Alert

**Step 1: Click the Admin link in the top right corner of Ops Manager.**

Ops Manager displays the Admin link only if you have
administrative privileges.

**Step 2: Select the Alerts tab, then the Global Alert Settings page.**

**Step 3: Click the Add Alert button.**

Ops Manager displays the alert configuration options.

**Step 4: Select the projects to which to apply the alert.**

If you specify tags, the alert  only applies to the projects that
have those tags. Users with the `Global Owner`
role can
assign tags to projects.

You can type the first few letters of a tag or project to locate it
in the drop-down list.

**Step 5: Select the condition that triggers the alert.**

In the Alert if section, select the target component and
the condition. For explanations of alert conditions, see
/reference/alerts.

**Step 6: Apply the alert only to specific targets. (Optional)**

If the options in the For section display, you can filter
the alert to apply to a subset of the targets.

The matches field supports regular expressions. Regular
expressions must match against an entire hostname.

**Example:**

To find hostnames involving `foo` using a regular expression,
you can filter for a hostname using one the following options:

| Hostname Description | `matches` Query |
|---|---|
| Starts with `foo` | `foo.*` |
| Ends with `foo` | `.*foo` |
| Contains `foo` | `.*foo.*` |

**Step 7: Select the alert recipients and delivery methods.**

In the Send to section, click Add to add
notifications or recipients. To help eliminate false positives, set
the time to elapse before the condition triggers the alert.

To test HipChat, Slack, PagerDuty, or Webhook integration, click the
Test Alert button that appears after you configure the
notification. For webhook notifications, this tests your custom
templates with sample data.

Which alert notification methods can be set depend on the scope
of the alert:

Project alerts
  Apply to one or more individual Organizations and Projects only.

Global alerts
  Apply to
  all Organizations and Projects.

System alerts
  Apply to the health of Ops Manager
  and its backing databases.

The alert notifications methods are as follows:

* - Notification Method
  - Project
  - Global
  - System
  - Description

* - Ops Manager Project
  - check
  - check
  -
  - .. include:: /includes/alert-notifications/project.rst

* - Ops Manager Organization
  - check
  - check
  -
  - .. include:: /includes/alert-notifications/org.rst

* - Ops Manager User
  - check
  -
  -
  - .. include:: /includes/alert-notifications/user.rst

* - Ops Manager Team
  - check
  -
  -
  - .. include:: /includes/alert-notifications/team.rst

* - SNMP (Simple Network Management Protocol) Host
  - check
  - check
  - check
  - Specify the hostname that will receive the v2c trap on
    standard port `162`. The MIB (management information base) file for SNMP (Simple Network Management Protocol) is
    [available for download](http://downloads.mongodb.com/on-prem-monitoring/MMS-10GEN-MIB.txt).

* - Email
  - check
  - check
  - check
  - Sends the alert to a specified email address.

* - [HipChat](https://www.atlassian.com/software/hipchat/enterprise/data-center)
  - check
  - check
  - check
  - Sends the alert to a HipChat room message stream. Enter the
    HipChat room name and API (Application Programming Interface) token.

* - [Slack](https://slack.com/)
  - check
  - check
  - check
  - .. include:: /includes/alert-notifications/slack.rst

* - [PagerDuty](https://www.pagerduty.com/)
  - check
  - check
  - check
  - .. include:: /includes/alert-notifications/pagerduty.rst

* - Webhook
  - check
  - check
  -
  - .. include:: /includes/alert-notifications/webhook.rst

    To use this method at the Global level:

    1. Navigate to the Ops Manager Config
       Miscellaneous tab of the
       Administration console.

    2. Update the `Webhook URL` and
       `Webhook Secret` settings.

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

* - [Datadog](https://www.datadoghq.com/)
  - check
  - check
  - check
  - .. include:: /includes/alert-notifications/datadog.rst

* - Administrators
  -
  - check
  - check
  - Sends the alert to the email address specified in the
    Admin Email Address field in the Ops Manager
    configuration options.

* - Global Alerts Summary Email
  -
  - check
  -
  - Sends a summary email of all global alerts to the specified
    email address.

**Step 8: Click Save.**

## Disable or Enable a Global Alert Configuration

**Step 1: Click the Admin link in the top right corner of Ops Manager.**

Ops Manager displays the Admin link only if you have
administrative privileges.

**Step 2: Click the Alerts tab, then click Global Alert Settings page.**

**Step 3: Choose the alert setting to disable.**

On the row for a specific alert, click ellipsis-h,
then click Disable.

Click ellipsis-h then Enable to re-enable the
alert at any time.

## Configure Webhook Templating for Global Alerts

Global alert configurations support webhook templating, allowing you to
customize the HTTP headers and request body content sent to your webhook
endpoints. This is particularly useful when you need to adapt the alert
payload to match different target systems across multiple projects.

For detailed information about webhook templating, including available 
template variables, regex helpers, and examples, see 
Configure Webhook Templating.

## Default Global Alerts

Each time Ops Manager starts, it creates global alert
configurations for the following conditions:

- Blockstore jobs have reached a high number of retries

- Sync slice transfer has not progressed in more than 60 minutes

- Inconsistent cluster snapshot count is above 5

- Backup is down

- Backup has too many conf call failures

- No daemon is available to take a queryable restore job

- Inconsistent backup configuration has been detected

- Backup requires a resync

- Replica set has a late snapshot

- Backup is in an unexpected state

- Backup has reached a high number of retries

- Backup could not be assigned to a backup daemon

If you do not want to receive alerts from a default global alert 
configuration, you must disable that global alert configuration.
