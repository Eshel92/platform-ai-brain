<!-- Converted from reference/alerts/replication-lag.txt (reStructuredText). Includes are inlined. -->

# Fix Replication Lag

At time `T`, the last write operation applied on the specified
secondary of replica set `ABC` was behind the most recent
operation applied on the primary.

## Alert Conditions

You can configure alert conditions in the project-level 
alert settings page to trigger alerts.

To learn more about the alert condition, see 
Replication Lag is.

## Common Triggers

- An idle replica set. The reported replication lag is actually just the
  time since the last write. Replication lag is calculated between the
  last operation time on the primary and the time of the last operation
  received by the secondary. If a replica set is only written to once
  every 10 minutes, the replication lag will be 10 minutes just after 
  the write is made to the primary and just prior to the next write 
  being replicated to the secondary.

- The secondary is under-provisioned, which means it needs more 
  allocated resources, and cannot keep up with the primary
  (common if using secondaries for read scaling).

- There is insufficient bandwidth, or some other networking problem,
  between the primary and secondary.

## Fix the Immediate Problem

- Adjust the settings for this alert to only trigger if the replication
  lag persists for longer than 2 minutes. This will reduce the chances 
  of a false positive.

- Resolve networking issues between the primary and secondary.

To learn more, see Troubleshoot Replica Sets in the MongoDB manual.

## Implement a Long-Term Solution

- Increase bandwidth between the primary and secondary.

- Move (or upgrade in place) the secondary to a machine that is
  identically (or better) provisioned to the current primary.

## Monitor Your Progress

View the following charts to monitor your progress:

- Network
  
  Monitor network metrics to track network performance.

- Replication Headroom
  
  Monitor replication headroom to determine whether the secondary might fall off the oplog.

- Replication Lag

  Monitor replication lag to determine whether the secondary might fall off the oplog.

To learn more, see 
View Deployment Metrics.
