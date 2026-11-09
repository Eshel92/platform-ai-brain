<!-- Converted from tutorial/nav/alert-resolutions.txt (reStructuredText). Includes are inlined. -->

# Resolve Alerts

Ops Manager issues an alert for each condition configured in your 
alert settings when an
alert condition occurs, such as an
unresponsive host or an outdated agent. To view all alert 
notifications, click Alerts in Ops Manager.

When a condition triggers an alert, you receive the alert at regular
intervals until the alert resolves or Ops Manager cancels it. You can
acknowledge an alert for a period of time, but if the alert condition
persists, you will again receive notifications once the acknowledgment
period ends.

You can temporarily suspend alerts on a resource by creating an alert
maintenance window.
For example, you can create a maintenance window
that suspends host alerts while you shut down hosts for maintenance.

Ops Manager administrators define alert configurations on a per-project or multi-project basis.

To learn more, see alerts-workflow and manage-alerts.

## Resolved Alerts

Alerts resolve when the alert condition no longer applies. For example,
if a replica set's primary goes down, Ops Manager issues an alert
that the replica set does not have a primary. When a new primary is
elected, the alert condition no longer applies, and the alert will
resolve. Ops Manager sends a notification of the alert's resolution.

## Cancelled Alerts

Ops Manager cancels an alert if the alert configuration that triggered the
alert is deleted, disabled, edited, or if the open alert becomes
invalid. Some examples of an alert becoming invalid are:

- There is an open "Host Down" alert, and then you delete the target
  host.

- There is an open "Replication Lag" alert, and the target host becomes
  the primary.

- There is an open "Replica set has no primary" alert for a replica set
  whose name is "rs0," and the target replica set is renamed to "rs1."

When an alert is canceled, Ops Manager does **not** send a notification and
does not record an entry on the Ops Manager Alerts lists.
