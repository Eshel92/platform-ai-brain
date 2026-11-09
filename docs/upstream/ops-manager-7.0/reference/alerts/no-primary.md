<!-- Converted from reference/alerts/no-primary.txt (reStructuredText). Includes are inlined. -->

# Fix Lost Primary

At time `T`, no primary was detected in replica set `ABC`.

## Alert Conditions

You can configure alert conditions in the project-level 
alert settings page to trigger alerts.

To learn more about the alert condition, see 
Replica set has no primary.

## Common Triggers

- A network partition is preventing all members of the replica set from
  communicating with each other.

- There are not enough voting members in the replica set to keep a
  primary. A simple majority is required to have a primary. This can
  happen if too many hosts are down (or not responding) to replica set
  heartbeats.

- There is not an electable member when the primary goes down.

## Fix the Immediate Problem

- Ensure a majority of votes are available in the replica set. If hosts
  have been shut down permanently, ensure they are removed from the
  replica set configuration.

- Use basic ping tests from one host to another to ensure they can
  communicate with each other.

## Implement a Long-Term Solution

Make sure there is more than one data-bearing member with a priority
greater than 0.

To learn more, see Replica Set Elections in the MongoDB manual.

## Monitor Your Progress

View the following charts to monitor whether the deployment is 
exhausting resources:

- Normalized System CPU
  
  Monitor CPU usage to determine whether data is retrieved from disk 
  instead of memory.

- Disk IOPs

  Monitor whether disk IOPS approaches the maximum provisioned IOPS. 
  Determine whether the deployment can handle future workloads.

- Connections

  Monitor connections to determine whether the current connection 
  limits are sufficient

To learn more, see 
View Deployment Metrics.
