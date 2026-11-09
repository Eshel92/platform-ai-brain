<!-- Converted from core/system-alerts.txt (reStructuredText). Includes are inlined. -->

# Manage System Alerts

System alerts are internal health checks that monitor the health of
Ops Manager itself, including the health of backing databases,
`Backup Daemons`, and backed-up
deployments. Ops Manager runs health checks every
five minutes.

To view the list of system alerts:

#. Click the Admin link at the top of the Ops Manager
   UI (user interface).

#. Click the Alerts tab.

#. Click the Open Alerts link under
   System Alerts.

Disabled system alerts are grayed out.

If you have the
`Global Owner`
role, you can
modify notification settings
or disable a system alert.

## System Alert Components

Each system alert consists of three components:

* - Component
  - Examples

* - A condition that triggers the alert
  - 
    - A blockstore is using too much disk space.
    - An Ops Manager backing database had startup warnings.

* - A list of recipients of the alert
  - 
    - Ops Manager user or role: Ops Manager Administrators
    - Email address: `admin@example.com`
    - Slack channel: `#alerts`

* - A method by which the alert is sent
  - 
    - Email
    - Slack
    - SMS

When the alert is enabled and its trigger condition is met, Ops Manager
sends an alert to the specified recipients using the specified medium
for that alert. For a list of the notification options, see the
**Select the alert recipients and delivery methods** step in the
edit-system-alert-notification procedure on this page.

By default, Ops Manager enables *all* alerts and sends the alerts to the
*email address* specified in the Admin Email Address field
in the Ops Manager configuration options.

## Available System Alerts

Ops Manager provides the following system alerts:

### Alert Processing

| Alert Type | Alert Message | Description |
|---|---|---|
| `ORDINARY_ALERT_PROCESSING_DISABLED` | .. alert:: Ordinary alert processing is disabled |  |
| `ORDINARY_ALERT_PROCESSING_ENABLED` | .. alert:: Ordinary alert processing is enabled |  |

### Backup

| Alert Type | Alert Message | Description |
|---|---|---|
| `OPLOG_TTL_RESIZE` | .. alert:: Backup oplog TTL was resized | Sent when the Backup Daemon has fallen so far behind in applying oplog entries that Ops Manager has extended the period of time it stores the oplog entries. By default, Ops Manager stores oplog entries in the Oplog Store for 24 hours. If the Daemon has not yet applied an oplog entry an hour before its expiration, Ops Manager extends the storage period for another three hours. Ops Manager can continue to extend the storage period up to 14 days. If you receive this alert: #. Check that your Backup Daemon is running. #. Check that your Backup Daemon runs on sufficiently performant hardware to apply oplog entries in a timely manner. |
| `THEFT_FAILED` | .. alert:: Backup was not moved successfully | Sent when a backup job migration to a new Backup Daemon fails. The backup job continues to run on the original Backup Daemon. For more information on moving jobs, see jobs-page. |

### Backup Daemon

| Alert Type | Alert Message | Description |
|---|---|---|
| `DAEMON_DOWN` | .. alert:: Backup Daemon is down | Sent when the Backup Daemon has not pinged Ops Manager for more than 15 minutes. |
| `DAEMON_UP` | .. alert:: Backup Daemon is up |  |
| `LOW_HEAD_FREE_SPACE` | .. alert:: Backup Daemon has low free head space | Sent when the disk partition on which the local copy of a backed-up replica set is stored has less than 1 GB of free space remaining. Follow the edit-system-alert-notification procedure to change this space limit. |
| `LOW_HEAD_FREE_SPACE_PERCENT` | .. alert:: Backup Daemon has low free head space percentage | Sent when the disk partition on which the local copy of a backed-up replica set is stored has less than 10 percent of free space remaining. Follow the edit-system-alert-notification procedure to change this percentage. |
| `SUFFICIENT_HEAD_FREE_SPACE` | .. alert:: Backup Daemon has sufficient free head space |  |

### Blockstore

| Alert Type | Alert Message | Description |
|---|---|---|
| `BALANCER_OFF` | .. alert:: Blockstore does not have a running balancer |  |
| `BALANCER_ON` | .. alert:: Blockstore has a running balancer | Sent when a sharded blockstore is running the sharded cluster balancer. You should disable the balancer on a sharded blockstore. To disable the balancer, see sharding-balancing-disable-temporarily. |
| `INSIDE_SPACE_USED_THRESHOLD` | .. alert:: Blockstore space used within threshold |  |
| `OUTSIDE_SPACE_USED_THRESHOLD` | .. alert:: Blockstore space used exceeds threshold | Sent when the disk space the `blockstore` uses exceeds the configured `threshold` setting. The default threshold is 85% of the total disk capacity on which the blockstore is stored. You can change the `mms.alerts.OutsideSpaceUsedThreshold.maximumSpaceUsedPercent` value in the Ops Manager configuration. |

### Cron Job

| Alert Type | Alert Message | Description |
|---|---|---|
| `CRON_JOB_COMPLETED` | .. alert:: Cron job has completed successfully |  |
| `CRON_JOB_FAILED` | .. alert:: Cron job has failed |  |

### Cron Job Status

| Alert Type | Alert Message | Description |
|---|---|---|
| `CRON_JOB_DISABLED` | .. alert:: Cron job disabled |  |
| `CRON_JOB_ENABLED` | .. alert:: Cron job enabled |  |

### Database Process

| Alert Type | Alert Message | Description |
|---|---|---|
| `BACKING_DATABASE_PROCESS_DOWN` | .. alert:: Detected a problem connecting to a database backing the system | Sent when Ops Manager cannot connect to a backing database and run the ping command. |
| `BACKING_DATABASE_PROCESS_NO_STARTUP_WARNINGS` | .. alert:: Detected no startup warnings on the databases backing the system |  |
| `BACKING_DATABASE_PROCESS_STARTUP_WARNINGS` | .. alert:: Detected startup warnings on a database backing the system | Sent when the MongoDB `process` hosting a backing database contains `startupWarnings` in its log files. |
| `BACKING_DATABASE_PROCESS_UP` | .. alert:: Successfully connected to a database backing the system |  |
| `BACKINGDB_DEFAULTRW_CONCERN_VERIFICATION_FAILED` | .. alert:: AppDB default Read/Write concerns are not set to recommended values | Sent when the read concern for the backing databases is *not* `"local"` and the write concern is *not* `w: "majority"`. |

### Log

| Alert Type | Alert Message | Description |
|---|---|---|
| `LOG_DEBUG_OVERRIDE_ACTIVE` | .. alert:: Production logger overridden with a DEBUG level |  |

## Modify Notification Settings for a System Alert

**Step 1: Click the Admin link in the top right corner of Ops Manager.**

Ops Manager displays the Admin link only if you have
administrative privileges.

**Step 2: Select the Alerts tab and then the System Alert Settings page.**

**Step 3: On the line for the alert, click the ellipsis icon and select Edit.**

**Step 4: Set the desired alert trigger values (Optional).**

You can edit the values that trigger certain system alerts. These values
are found in the Alert If section of the following alerts:

| Alert | Field | Default |
|---|---|---|
| `Backup Daemon has low free head space` | Backup daemon free head space is below | 1 GB |
| `Backup Daemon has low free head space percentage` | Backup daemon free head space percentage is below | 10 |

**Step 5: Select the alert recipients and delivery methods.**

In the Send to section, configure notifications. To add
notifications or recipients, click Add and select from
the options listed below. To test a notification, click the test
link that appears after you configure the notification and ensure
that the service you are testing receives the message.

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

## Disable a System Alert

**Step 1: Click the Admin link in the top right corner of Ops Manager.**

Ops Manager displays the Admin link only if you have
administrative privileges.

**Step 2: Select the Alerts tab and then the System Alert Settings page.**

**Step 3: Disable the alert.**

On the line for the system alert that you want to disable, click the
ellipsis icon and select Disable.
