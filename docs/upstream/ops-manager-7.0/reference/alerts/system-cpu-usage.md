<!-- Converted from reference/alerts/system-cpu-usage.txt (reStructuredText). Includes are inlined. -->

# Fix CPU Usage Issues

`System CPU` alerts indicate that the CPU usage of the MongoDB
process has reached a specified threshold. This threshold is specified
when the alert is created.

## Alert Conditions

You can configure the following alert conditions in the project-level 
alert settings page to trigger alerts.

System: CPU (Steal) %
  Occurs when the percentage of time the CPU is in a state of
  "involuntary wait" exceeds the specified threshold. CPU
  steal percentage is the percentage by which the CPU usage exceeds
  the guaranteed baseline CPU credit accumulation rate.

  **Note:**

  This alert typically triggers when all credits have been
  consumed on an [AWS burstable performance instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/burstable-performance-instances.html).

System: CPU (User) %
  Occurs when the CPU usage of the MongoDB process, as normalized by
  the number of CPUs, exceeds the specified threshold.

## Common Triggers

Unoptimized queries might lead to 
`System CPU` alerts.

## Fix the Immediate Problem

Consider adding one or more indexes
to improve query performance. For details on calculating suggested 
indexes, see Calculate Suggested Indexes.

## Implement a Long-Term Solution

Consider scaling your cluster with additional servers to
reduce the CPU usage percentage utilized by the current workload.
For example, you could
convert a replica set to a sharded cluster.
To learn more about sharded clusters, see
Sharding.

## Monitor Your Progress

View the Normalized System CPU chart to monitor CPU 
usage of all processes on the node, scaled to a range of 0-100% by 
dividing by the number of CPU cores.

Monitor CPU usage to determine whether data is retrieved from disk 
instead of memory.

To learn more, see View Cluster Metrics.
