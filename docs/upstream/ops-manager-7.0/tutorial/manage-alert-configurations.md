<!-- Converted from tutorial/manage-alert-configurations.txt (reStructuredText). Includes are inlined. -->

# Configure Alert Settings

## Overview

An alert configuration defines the conditions
that trigger an alert and the alert's notification methods. This
tutorial describes how to create and manage the alert configurations for
a specified project. To create and manage global alert configurations, see
/tutorial/manage-global-alerts.

## Considerations

### SMS Delivery

Many factors may affect alert delivery, including do not call lists,
caps for messages sent or delivered, delivery time of day, and message
caching.

Check with your telephone service contract for the costs associated
with receiving text messages.

If you choose SMS, Ops Manager sends alert text messages to all users in the
project who have a mobile number associated with their user account.

### Alert Intervals

You can create multiple alert configurations with different
frequencies. The minimum frequency for an alert is 5 minutes.

The time between re-notifications increases by the frequency amount
every alert cycle up to a maximum of 24 hours. For example, if the
frequency amount is 5 minutes, and the alert condition is first
triggered at 9am, subsequent alerts occur at 9:05am, 9:15am, 9:30am,
etc.

You can set the time to elapse before Ops Manager sends an alert after an
alert condition occurs. This helps eliminate false positives.

## Default Alert Configurations

**org:**

Ops Manager provides no default alerts for organizations.

**project:**

Ops Manager creates the following alert configurations for a project
automatically upon creation of the project:

- User joined the project (`JOINED_GROUP`)

- Host's SSL certificate will expire within 30 days (`HOST_SSL_CERTIFICATE_STALE`)

- Monitoring is down (`MONITORING_AGENT_DOWN`)

If you enable Backup, Ops Manager creates the following alert
configurations for the project, if they do not already exist:

- Backup oplog is behind (`OPLOG_BEHIND`)

- Backup requires a resync (`RESYNC_REQUIRED`)

- Cluster is missing an active mongos (`CLUSTER_MONGOS_IS_MISSING`)

- Host has security recommendations

- Query Targeting: Scanned Objects / Returned is

  **Note:**

  The default configuration sends an alert only if the 
  ratio of documents scanned to documents returned meets or 
  exceeds the specified threshold for at least 10 minutes.

## Recommended Alert Configurations

To effectively monitor your deployment, consider configuring the
following alerts:

### Recommended Host Alerts

- *Host is recovering*: Triggers when a MongoDB instance
  enters RECOVERING mode.

- *Replication Lag is*: Monitors the lag time of secondaries
  behind the primary.

- *Tickets Available: Writes/Reads*: Flags potential
  performance issues for the WiredTiger storage engine.

- *Replication Oplog*: Monitors the oplog window size.

- *Host is down*: Triggers when a host becomes unreachable.

- *Queues: Readers/Writers is*: Tracks operations waiting on
  locks.

- *Page faults is*: Investigate if consistently high
  (> 1000 avg/sec).

- *Host is exposed to the public Internet*: Triggers when
  authentication and firewall protection are missing.

- *Host does not have the latest version*: Triggers when the
  MongoDB version is outdated by two or more revisions.

### Recommended Replica Set Alerts

- *Replica set elected a new primary*: Triggers during an
  election event.

- *Number of unhealthy members > n*: Triggers when more
  than n members are unhealthy.

### Recommended Sharded Cluster Alerts

- *Cluster missing an active mongos*

### Recommended Agent Alerts

- *Monitoring Agent is down*

- *Backup Agent is down*

### Recommended Backup Alerts

When you use the Backup component, configure the following
alerts:

- *Backup oplog is behind*

- *Backup requires a resync*

**Note:**

Tune these alerts for your specific workload and usage
patterns.

## Default Settings for Notification Options

**org:**

You can configure default settings for the following
notification options:

- Ops Manager Organization

- Ops Manager User

- Email

- SMS

- HipChat

- Slack

- PagerDuty

- Datadog

- VictorOps

- Opsgenie

**project:**

You can configure default settings for the following
notification options:

- Ops Manager Organization

- Ops Manager User

- Email

- SMS

- HipChat

- Slack

- PagerDuty

- Datadog

- VictorOps

- Opsgenie

To configure default settings for one of the above notification
options, click Integrations under Projects in
the sidebar. Locate the notification option and enter the default
values.

Ops Manager will fill in the default values automatically when a user
selects that option when creating an alert configuration. If the key,
token, or URL (Uniform Resource Locator) that is used to send the notification becomes invalid,
Ops Manager will send an email to the project owner and will eventually
remove the key, token, or URL (Uniform Resource Locator).

## Create an Alert Configuration

When you create a new alert, you can clone an existing alert.

**org:**

**Step 1: Navigate to the Alerts page for your organization.**

a. If it is not already displayed, select your desired organization
   from the `office` Organizations menu in the
   navigation bar.

#. Click Alerts in the sidebar.

**Step 2: Choose whether to create a new alert setting or clone an existing one.**

To create a new alert:

a. Click Add Alert.

To clone an existing alert setting:

a. Click the Alert Settings tab.
#. Locate the alert setting you want to clone.
#. Click ellipsis-h then Clone in that alert
   setting's row.

**Step 3: Choose the Target.**

Click User or Billing under
Select a Target.

**Step 4: Choose the Condition.**

**Step 5: Select the Notification Method.**

Under the Add Notification Method heading, click the
button for the particular notification method you want to use.

| Notification Option | User Alerts | Billing Alerts | Description |
|---|---|---|---|
| Ops Manager Organization | check | check | .. include:: /includes/alert-notifications/org.rst |
| Ops Manager User | check | check | .. include:: /includes/alert-notifications/user.rst |
| Email | check | check | Sends the alert to any email address you provide. |
| Mobile Number | check | check | .. include:: /includes/alert-notifications/sms-onprem.rst |
| Slack | check | check | .. include:: /includes/alert-notifications/slack.rst |
| PagerDuty |  | check | .. include:: /includes/alert-notifications/pagerduty.rst |
| Datadog | check | check | .. include:: /includes/alert-notifications/datadog.rst |
| VictorOps |  | check | .. include:: /includes/alert-notifications/victorops.rst |
| Opsgenie |  | check | .. include:: /includes/alert-notifications/opsgenie.rst |

**Step 6: Click Save.**

**project:**

**Step 1: Navigate to the Alerts page for your project.**

a. If it is not already displayed, select the organization that
   contains your desired project from the `office` Organizations menu in the
   navigation bar.

#. If it is not already displayed, select your desired project
   from the Projects menu in the navigation bar.

#. Click the `bell` Project Alerts icon in the
   navigation bar, or click Alerts in the sidebar.

**Step 2: Choose whether to create a new alert setting or clone an existing one.**

To create a new alert without cloning an existing setting:

a. Click Add.
#. Select New Alert.

To clone an existing alert setting:

a. Click the Alert Settings tab.
#. Locate the alert setting you want to clone.
#. Click ellipsis-h then Clone in that alert
   setting's row.

**Step 3: Select the condition that triggers the alert.**

In the Alert if section, select the target component and
the condition. To learn more about alert conditions, see
/reference/alert-types.

**Step 4: Apply the alert only to specific targets.**

If the options in the For section are available, you can
optionally filter the alert to apply only to a subset of the targets. 
The filter uses a logical `OR` operator between each condition.

The matches field can use regular expressions.

**Step 5: Select the alert recipients and delivery methods.**

In the Send to section:

a. (Optional) To help reduce the false positives that Ops Manager 
   sends, in the send if condition lasts 
   at least field, specify the minutes to elapse before the 
   condition sends the alert. The next alert check that runs after
   the specified time elapses sends the alert.

#. (Optional) In the resend after field, specify the 
   minutes to elapse before the condition resends the alert.

#. Click Add and select
   from the options described in the following table.

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

**Step 6: Click Save.**

## Delete an Alert Configuration

**org:**

**Step 1: Navigate to Alert Settings.**

a. If it is not already displayed, select your desired organization
   from the `office` Organizations menu in the
   navigation bar.

#. Click Alerts in the sidebar.

#. Click the Alert Settings tab.

**Step 2: Choose the alert setting to delete.**

a. On the row for a specific alert, click ellipsis-h
   then Delete.
#. Click Delete in the Delete Alert modal or
   click Cancel to leave the alert as configured.

   **Note:**

   If you have not logged in within the five minutes of pushing
   Delete, you need to re-enter your password, then
   click Delete again.

**project:**

**Step 1: Navigate to the Alert Settings tab.**

a. If it is not already displayed, select the organization that
   contains your desired project from the `office` Organizations menu in the
   navigation bar.

#. If it is not already displayed, select your desired project
   from the Projects menu in the navigation bar.

#. Click the `bell` Project Alerts icon in the
   navigation bar, or click Alerts in the sidebar.

#. Click the Alert Settings tab.

**Step 2: Choose the alert setting to delete.**

a. On the row for a specific alert, click ellipsis-h
   then Delete.
#. Click Confirm in the Confirm Delete modal
   or click Cancel to leave the alert as configured.

If you delete an alert setting, Ops Manager cancels active alerts related to
the setting. A deleted alert setting does not remain visible.

## Disable or Enable an Alert Configuration

**org:**

**Step 1: Navigate to Alert Settings.**

a. If it is not already displayed, select your desired organization
   from the `office` Organizations menu in the
   navigation bar.

#. Click Alerts in the sidebar.

#. Click the Alert Settings tab.

**Step 2: Choose the alert setting to disable.**

On the row for a specific alert, click ellipsis-h
then Disable.

Click ellipsis-h then Enable to re-enable the
alert at any time.

**project:**

**Step 1: Navigate to the Alert Settings tab.**

a. If it is not already displayed, select the organization that
   contains your desired project from the `office` Organizations menu in the
   navigation bar.

#. If it is not already displayed, select your desired project
   from the Projects menu in the navigation bar.

#. Click the `bell` Project Alerts icon in the
   navigation bar, or click Alerts in the sidebar.

#. Click the Alert Settings tab.

**Step 2: Choose the alert setting to disable.**

On the row for a specific alert, click ellipsis-h
then Disable.

**Note:**

Click ellipsis-h then Enable to re-enable the
alert at any time.

If you disable an alert setting, Ops Manager cancels active alerts related to
the setting. A disabled alert setting remains visible but grayed-out
and can be later re-enabled.

If you need to disable an alert only for a period of time, you can
suspend alerts.

## View the History of Changes to an Alert Configuration

**org:**

You can view all alerts, alert settings, and deleted alerts on 
the Organization Alerts page. To learn more, see 
alerts-workflow.

**Step 1: Navigate to the Alert Settings tab.**

a. If it is not already displayed, select your desired organization
   from the `office` Organizations menu in the
   navigation bar.

#. Click Alerts in the sidebar.

#. Click the Alert Settings tab.

**Step 2: On the line listing the alert configuration, click the ellipsis icon and select History.**

Ops Manager displays the history of changes to the alert configuration.

**project:**

You can view open alerts, closed alerts, and alert 
settings on the Project Alerts page. 
Ops Manager sends notifications for all alerts 
that appear on the Open tab. To learn more, 
see alerts-workflow.

**Step 1: Navigate to the Alert Settings tab.**

a. If it is not already displayed, select the organization that
   contains your desired project from the `office` Organizations menu in the
   navigation bar.

#. If it is not already displayed, select your desired project
   from the Projects menu in the navigation bar.

#. Click the `bell` Project Alerts icon in the
   navigation bar, or click Alerts in the sidebar.

#. Click the Alert Settings tab.

**Step 2: Click either the Active Alerts or Deleted Alerts filter, depending on the configuration's status.**

**Step 3: On the line listing the alert configuration, click the ellipsis icon and select History.**

Ops Manager displays the history of changes to the alert configuration.

## Test Alert Configurations

You can test your alert configurations to ensure they work correctly
before deploying them in production. This is particularly useful for
webhook notifications with custom templates.

**project:**

**Step 1: Navigate to Alert Settings**

Navigate to Alerts > Alert Settings.

**Step 2: Create or edit an alert configuration**

Create or edit an alert configuration.

**Step 3: Configure notification method**

In the Send to section, configure your notification
method (webhook, email, etc.).

**Step 4: Test the configuration**

Click the Test Alert button next to the notification
configuration.

**Step 5: Verify the test results**

Ops Manager sends a test notification with sample data to verify your
configuration works correctly.

For webhook notifications, the test includes:

- Sample alert data rendered through your custom templates
- Validation that your webhook endpoint is reachable
- Verification that custom headers and body templates render correctly

**global:**

**Step 1: Navigate to Global Alert Settings**

Navigate to Admin > Global Alert Settings.

**Step 2: Create or edit a global alert configuration**

Create or edit a global alert configuration.

**Step 3: Configure notification method**

In the Send to section, configure your notification
method.

**Step 4: Test the configuration**

Click the Test Alert button next to the notification
configuration.

**Step 5: Verify the test results**

Ops Manager sends a test notification to verify the configuration.

Global alert tests use sample data that represents the type of
alerts that would be generated across multiple projects.
