<!-- Converted from reference/alerts/disk-io-utilization.txt (reStructuredText). Includes are inlined. -->

# Fix IOPS Issues

System and disk alert conditions can 
indicate IOPS issues.

## Alert Conditions

`System: CPU (User) % is` measures the CPU usage of the 
processes on the node, normalized by the number of CPUs. This value is 
scaled to a range of 0-100%.

## Common Triggers

A few common events may trigger these alerts:

- Unoptimized queries

- A one-time event, such as an index build.

## Fix the Immediate Problem

Consider the following resolutions:

- Optimize your queries.

- Use the MongoDB Atlas Performance Advisor to view slow queries and suggested
  indexes.

## Implement a Long-Term Solution

- Review Indexing Strategies for
  possible further indexing improvements.

  **Note:**

  A temporary spike in disk utilization may result when creating new
  indexes.

- Analyze Query Performance
  to review how your queries are using your indexes.

- Use a faster disk drive with more hardware resources.

- Move operations from disks with large workloads to different disks.

## Monitor Your Progress

To observe high disk utilization, open the 
Hardware Metrics section of the Metrics tab and 
find the following metrics:

| Graph | Indicator |
|---|---|
| Disk IOPS | IOPS (Input/Output Operations per Second) value greater than the provisioned IOPS (Input/Output Operations per Second) value |
| Normalized System CPU | High IOWait curve IOWait measures the percentage of time the CPU runs idle waiting for an I/O operation to complete. |

To learn more, see 
View Deployment Metrics.
