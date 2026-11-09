<!-- Converted from reference/alerts/backup-oplog-is-behind.txt (reStructuredText). Includes are inlined. -->

# Fix Backup Oplog Issues

The Ops Manager backup service has not received an oplog from the 
MongoDB Agent for at least an hour.

## Alert Conditions

You can configure alert conditions in the project-level 
alert settings page to trigger alerts.

To learn more about the alert condition, see 
Backup oplog is behind.

## Common Triggers

- MongoDB Agent is down.

- MongoDB Agent is overloaded.

- MongoDB Agent can't reach the replica set.

- MongoDB Agent can't reach or successfully send data to Ops Manager.

- MongoDB Agent is continuously restarting.

## Fix the Immediate Problem

Check the MongoDB Agent logs in Ops Manager and 
on the MongoDB Agent host to find out which of these occurred.

## Implement a Long-Term Solution

Manage your MongoDB Agent settings.

## Monitor Your Progress

View the {mdbagent+} status on the Agents tab to monitor 
your progress.

To learn more, see view-agent-status.
