<!-- Converted from tutorial/nav/alerts.txt (reStructuredText). Includes are inlined. -->

# Configure and Resolve Alerts

Ops Manager issues alerts for the conditions configured in your 
alert settings. When a condition triggers an 
alert, you receive the alert at regular intervals until the alert 
resolves or Ops Manager cancels it.

## Alert Conditions

When you configure alerts, you specify alert conditions and thresholds. 
Review the possible alert conditions for 
which you can trigger alerts related to your clusters.

## Configure Alerts

To set which conditions trigger alerts and how Ops Manager notifies users, 
configure-alerts. You can configure alerts at the organization 
or project level. Ops Manager provides default alerts at the project 
level. You can clone existing alerts and configure maintenance window 
alerts.

## Resolve Alerts

When a condition triggers an alert, Ops Manager displays a warning symbol 
on the cluster and sends alert notifications. Resolve these
alerts and work to prevent alert conditions from occurring in the 
future. To learn how to fix the immediate problem, implement a 
long-term solution, and monitor your progress, see 
alerts-resolutions.

## Alerts Workflow

When an alert condition is met, the following 
alert lifecycle begins:

**Step 1: The alert condition is met.**

- For informational alerts like the 
  `User joined the organization`. 
  alert, Ops Manager sends notifications as soon as the condition is 
  met. These alerts don't appear in the Ops Manager UI. The 
  informational alerts workflow ends here.

- Otherwise, Ops Manager retrieves metrics at regular intervals 
  based on granularity. When the retrieved metrics indicate that 
  an alert condition is met, Ops Manager tracks the alert condition 
  until it ends, or until it remains past the amount of time 
  specified in the send if condition lasts at least 
  field.

  **Note:**

  If the alert condition ends between sampling periods, 
  Ops Manager doesn't track the alert condition or send any 
  notifications.

**Step 2: The alert condition remains past the amount of time specified in the send if condition lasts at least field.**

Ops Manager sends notifications. The alerts appear on the 
All Alerts tab (organization alerts) or the 
Open Alerts tab (project alerts).

**Step 3: The alert remains active until it resolves, or you disable or delete it.**

The following stages might occur:

- You acknowledge the alert. Ops Manager 
  sends no further notifications until either the acknowledgement 
  period ends, you resolve the alert condition, or you 
  unacknowledge the alert. If an alert condition ends during an 
  acknowledgment period, Ops Manager sends a notification.

- You unacknowledge an alert that 
  you previously acknowledged. After you unacknowledge an active 
  alert, Ops Manager resumes sending notifications at regular 
  intervals until the condition resolves or you delete, disable, 
  or re-acknowledge the alert.

- You disable the alert. 
  Ops Manager cancels active alerts related to the setting. A disabled 
  alert setting remains visible but grayed-out and you can later 
  re-enable it.

- You enable an alert that 
  you previously disabled.

- You delete the alert. Ops Manager 
  cancels active alerts related to the setting. A deleted alert 
  setting does not remain visible.

- The alert condition resolves. The alert appears on the 
  All Alerts tab (organization alerts) or the 
  Closed Alerts tab (project alerts).
