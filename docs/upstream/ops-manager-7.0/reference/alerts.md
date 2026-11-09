<!-- Converted from reference/alerts.txt (reStructuredText). Includes are inlined. -->

# Review Alert Conditions

For each project or
global alert you create, you must
set a target and a condition or metric. The *target* points to what changed:
the Ops Manager component. If your *condition* becomes true or a *metric* meets
your set threshold, Ops Manager triggers an alert. To learn more, see 
alerts-workflow.

To set a condition:

#. Select a Target from the list.
#. Select a condition in the condition/metric list.

Ops Manager triggers an alert when the condition is `true` on the
specified target MongoDB instance.

To set a metric:

#. Select a Target type from the list.
#. Filter the Target type or select Any.
#. Select on a metric in the condition/metric list.
#. Select if this metric should be Below or
   Above the threshold.
#. Type a threshold value. All thresholds are numbers.
#. Select the unit of measure for the threshold.

Ops Manager triggers an alert when the metric threshold is met on the
specified target MongoDB instance.

## Host Alerts

When setting an alert for a host, select the host type that
applies to this alert and the condition that triggers this
alert.

### Host Types

For host type, set an alert for all or one of the
following types of MongoDB processes:

| Set Host Type to: | Alert Includes |
|---|---|
| Any type | All the types described in this table. |
| Standalone | Any mongod instance that is *neither* part of a replica set or sharded cluster *nor* used as a config server. |
| Primary | All replica set primaries. |
| Secondary | All replica set secondaries. |
| Arbiter | All replica set arbiters. |
| Mongos | All mongos instances. |
| Conf | All mongod instances used as config servers. |

### Host Alert Conditions

#### Change in Host Status

You can set an alert for when MongoDB instance changes. Host status
conditions include:

* - Condition
  - Alert Trigger

* - Host added
  - Ops Manager starts monitoring or managing a mongod or
    `mongos` process for the first time.

* - Host removed
  - Ops Manager stops monitoring or managing a mongod or
    `mongos` process for the first time.

* - Host added to replica set
  - Specified type of mongod process is added to a
    replica set.

* - Host removed from replica set
  - Specified type of mongod process is removed from
    a replica set.

* - Host has restarted
  - Ops Manager detects that a host has been restarted.

* - Restarts in Last Hour is
  - Ops Manager detects that the number of times a host restarted within
    the previous hour exceeds the specified threshold.

* - Host experienced a rollback
  - Ops Manager detects that a mongod on a host triggered a
    rollback.

    The following host types can't experience rollbacks:

    - arbiters
    - mongos

    To learn more, see Rollbacks During Replica Set Failover.

* - Host is recovering
  - A secondary enters the `RECOVERING` state. To
    learn more about the `RECOVERING` state, see
    Replica Set Member States.

* - Host does not have the latest version
  - Revision of MongoDB running on a host is two or more
    revisions behind the current stable release of MongoDB.

    For example, if the current stable release is MongoDB 4.0.9, a host
    running MongoDB 4.0.8 would not trigger an alert but a host
    running MongoDB version 4.0.7 would trigger an alert.

    To learn more about MongoDB version numbering, see
    MongoDB Version Numbers
    in the MongoDB manual.

* - Host's SSL certificate will expire after 21 days
  - SSL certificate for a MongoDB instance is 21 days from
    expiration. Ops Manager resends the alert every 24 hours until
    resolved or acknowledged. If you do not resolve or acknowledge
    the alert and the certificate expires, Ops Manager continues to send
    the alert. If the certificate expires, the Monitoring can
    no longer connect to the MongoDB instance.

|  |  |
|---|---|
| Host is down | Ops Manager does not receive a ping from a host for more than 4 minutes. Under normal operation, the Monitoring connects to each monitored host about once per minute. Ops Manager waits 4 minutes before triggering the alert to minimize false positives, as would occur during a host restart. If the host continues to be unreachable, the Monitoring eventually reduces ping frequency to every 5 minutes for a mongod and every 20 minutes for a mongos. If a mongod or mongos again becomes reachable, Ops Manager recognizes the process within 5 minutes. If Ops Manager Automation does not manage a mongos process and that process remains unreachable for 30 days, Ops Manager removes the process from the Deployment tab. However, if you restart the mongos process, Ops Manager detects it. To resolve this alert, see /reference/alerts/host-down. |

#### Advisor

You may set the Host Has Index Suggestions alert to receive
an alert if Performance Advisor has index
suggestions for the host.

If the query targeting ratio for
a host consistently exceeds 10,000 for a period of 10 minutes,
Performance Advisor checks the host for inefficient queries and
possible indexes to improve performance. If Performance Advisor
determines that the host would benefit from one or more indexes,
this alert triggers and directs you to create the suggested indexes.

This alert does not trigger for projects where Performance Advisor is
disabled.

#### Asserts

You may set alerts for how many assertion errors per second the
instance has created.

**Note:** How It Is Measured

MongoDB reports on opscounters using the `asserts` document that
the
serverStatus
command returns.

Assert metrics include:

| Metric | Alert Trigger |
|---|---|
| Asserts: Regular is | Rate of regular asserts meets your specified threshold. |
| Asserts: Warning is | Rate of warnings meets your specified threshold. |
| Asserts: Msg is | Rate of message asserts meets your specified threshold. Message asserts are internal server errors. Stack traces are logged for these. |
| Asserts: User is | Rate of asserts users create meets your specified threshold. |

**Note:**

You can create charts for a selection of these metrics in Ops Manager. 

1. From the Ops Manager project's Deployment view, click the 
   List tab.
#. Click the process for which you want to monitor. 
#. Click the Status tab.
#. Scroll down to the list of available metrics and select the 
   desired metric(s) to chart. 

To learn more about creating charts for host metrics in 
Ops Manager, see /tutorial/view-diagnostics and click the
MongoDB Process Metrics tab.

#### Average Execution Time

**Important:** Applies to MongoDB 3.4 or later only

The following metrics apply only to deployments running MongoDB
version 3.4 or later.

You may set alerts for how long operations take to complete. Execution
time metrics include:

| Metric | Alert Trigger |
|---|---|
| Average Execution Time: Commands is | Average execution time for command operations meets your specified threshold. |
| Average Execution Time: Reads is | Average execution time for read operations meets your specified threshold. |
| Average Execution Time: Writes is | Average execution time for write operations meets your specified threshold. |

#### Document Metrics

You may set alerts for how many MongoDB documents are processed per
second. Document processing metrics include:

| Metric | Alert Trigger |
|---|---|
| Document Metrics: Deleted is | Average rate per second of documents deleted meets your specified threshold. |
| Document Metrics: Inserted is | Average rate per second of documents inserted meets your specified threshold. |
| Document Metrics: Returned is | Average rate per second of documents returned meets your specified threshold. |
| Document Metrics: Update is | Average rate per second of documents updated meets your specified threshold. |

**Note:**

You can create charts for a selection of these metrics in Ops Manager. 

1. From the Ops Manager project's Deployment view, click the 
   List tab.
#. Click the process for which you want to monitor. 
#. Click the Status tab.
#. Scroll down to the list of available metrics and select the 
   desired metric(s) to chart. 

To learn more about creating charts for host metrics in 
Ops Manager, see /tutorial/view-diagnostics and click the
MongoDB Process Metrics tab.

#### Query Targeting

You may set alerts for how fast MongoDB scans items during queries and
how many items are scanned compared to documents returned. Query
execution time metrics include:

**Note:** How It Is Measured

MongoDB measures query performance based on the explain command.

**`Query Targeting: Scanned is`**

Average rate per second to scan index items during queries
and query-plan evaluations meets your specified threshold.

**`Query Targeting: Scanned Objects is`**

Average rate per second to scan documents meets your
specified threshold.

**`Query Targeting: Scanned / Returned is`**

Ratio of index items scanned to documents returned meets the
specified threshold.

**`Query Targeting: Scanned Objects / Returned is`**

Ratio of documents scanned to documents returned meets the
specified threshold.

**Note:**

You can create charts for a selection of these metrics in Ops Manager. 

1. From the Ops Manager project's Deployment view, click the 
   List tab.
#. Click the process for which you want to monitor. 
#. Click the Status tab.
#. Scroll down to the list of available metrics and select the 
   desired metric(s) to chart. 

To learn more about creating charts for host metrics in 
Ops Manager, see /tutorial/view-diagnostics and click the
MongoDB Process Metrics tab.

#### Opcounter

You may set alerts for how many database operations are completed per
second.

**Note:** How It Is Measured

MongoDB reports on opscounters using the `opscounters` document that the
serverStatus command returns.

Operation metrics include:

| Condition | Alert Trigger |
|---|---|
| Opcounter: Cmd is | Average rate of commands performed per second meets your specified threshold. |
| Opcounter: Delete is | Average rate of deletes performed per second meets your specified threshold. |
| Opcounter: Getmores is | Average rate of getMores performed per second meets your specified threshold. On a primary, this number can be high even if the query count is low. The secondaries "getMore" from the primary as part of replication. |
| Opcounter: Insert is | Average rate of inserts performed per second meets your specified threshold. |
| Opcounter: Query is | Average rate of queries performed per second meets your specified threshold. |
| Opcounter: Update is | Average rate of updates performed per second meets your specified threshold. |

**Note:**

You can create charts for a selection of these metrics in Ops Manager. 

1. From the Ops Manager project's Deployment view, click the 
   List tab.
#. Click the process for which you want to monitor. 
#. Click the Status tab.
#. Scroll down to the list of available metrics and select the 
   desired metric(s) to chart. 

To learn more about creating charts for host metrics in 
Ops Manager, see /tutorial/view-diagnostics and click the
MongoDB Process Metrics tab.

#### Opcounter - Repl

You may set alerts for how many database operations per second are
replicated to a MongoDB secondaries.

**Note:** How It Is Measured

MongoDB reports on opscounters using the `opscountersRepl`
document of that the serverStatus command returns.

Replication operation metrics include:

| Metric | Alert Trigger |
|---|---|
| Opcounter: Repl Cmd is | Average rate of replicated commands applied per second meets your threshold. |
| Opcounter: Repl Delete is | Average rate of replicated deletes applied per second meets your threshold. |
| Opcounter: Repl Insert is | Average rate of replicated inserts applied per second meets your threshold. |
| Opcounter: Repl Update is | Average rate of replicated updates applied per second meets your threshold. |

**Note:**

You can create charts for a selection of these metrics in Ops Manager. 

1. From the Ops Manager project's Deployment view, click the 
   List tab.
#. Click the process for which you want to monitor. 
#. Click the Status tab.
#. Scroll down to the list of available metrics and select the 
   desired metric(s) to chart. 

To learn more about creating charts for host metrics in 
Ops Manager, see /tutorial/view-diagnostics and click the
MongoDB Process Metrics tab.

#### Memory

You may set alerts for how much memory a MongoDB instance uses. Set
this threshold in bits, kilobits, megabits, gigabits, bytes, kilobytes,
megabytes, gigabytes, terabytes or petabytes.

**Note:** How It Is Measured

MongoDB reports on memory using the `mem` document that the
serverStatus command returns.

Memory metrics include:

| Metric | Alert Trigger |
|---|---|
| Memory: Resident is | Resident memory size for the `mongod` process meets your specified threshold. Over time on a dedicated database host, the resident memory may approach the amount of RAM on the host. |
| Memory: Virtual is | Virtual memory size for the `mongod` process meets your specified threshold. You can use this alert to flag excessive memory outside of memory mapping. |
| Memory: Mapped is | Mapped memory size for the `mongod` process meets your specified threshold. As MongoDB memory-maps all the data files, the size of mapped memory should approach total database size. |
| Memory: Computed is | Virtual memory size for the `mongod` process that is not accounted for by memory-mapping meets your specified threshold. If this number is very high (multiple gigabytes), it indicates that excessive memory is being used outside of memory mapping. |

**Note:**

You can create charts for a selection of these metrics in Ops Manager. 

1. From the Ops Manager project's Deployment view, click the 
   List tab.
#. Click the process for which you want to monitor. 
#. Click the Status tab.
#. Scroll down to the list of available metrics and select the 
   desired metric(s) to chart. 

To learn more about creating charts for host metrics in 
Ops Manager, see /tutorial/view-diagnostics and click the
MongoDB Process Metrics tab.

#### Security

Security metrics include:

| Metric | Alert Trigger |
|---|---|
| Host has security recommendations | Authentication or TLS (Transport Layer Security) is disabled. |

#### Swap

Swap metrics include:

| Metric | Alert Trigger |
|---|---|
| Swap Usage: Used is | The total amount swap space in use has reached the specified threshold. |
| Swap Usage: Max Used is | Maximum total amount of swap space in use reaches the specified threshold. |
| Swap Usage: Free is | The amount of available swap space has dropped below the specified threshold. |
| Swap Usage: Max Free is | Maximum amount of available swap space drops below the specified threshold. |

#### WiredTiger Cache

You may set alerts for how much WiredTiger cache a MongoDB instance
uses. Set this threshold in bits, kilobits, megabits, gigabits, bytes,
kilobytes, megabytes, gigabytes, terabytes or petabytes.

**Note:** How It Is Measured

MongoDB reports on memory using the `cache` document that the
serverStatus command returns.

WiredTiger cache metrics include:

| Metric | Alert Trigger |
|---|---|
| Cache: Bytes Read Into Cache is | Average rate of bytes per second read into WiredTiger's cache meets your specified threshold. |
| Cache: Bytes Written From Cache is | Average rate of bytes per second written from WiredTiger's cache meets your specified threshold. |
| Cache: Dirty Bytes is | Number of tracked dirty bytes currently in the WiredTiger cache. |
| Cache: Used Bytes is | Number of bytes currently in the WiredTiger cache. |

**Note:**

You can create charts for a selection of these metrics in Ops Manager. 

1. From the Ops Manager project's Deployment view, click the 
   List tab.
#. Click the process for which you want to monitor. 
#. Click the Status tab.
#. Scroll down to the list of available metrics and select the 
   desired metric(s) to chart. 

To learn more about creating charts for host metrics in 
Ops Manager, see /tutorial/view-diagnostics and click the
MongoDB Process Metrics tab.

#### B-tree

**Important:** Applies to MongoDB 2.2 to 2.6 only

These metrics only triggers alerts on deployments running MongoDB
versions 2.2 through 2.6.

You may set alerts for how many btree operations on the MongoDB
instance are completed per second. B-Tree metrics include:

| Metric | Alert Trigger |
|---|---|
| B-tree: accesses is | Number of accesses to B-tree indexes meets your specified threshold. |
| B-tree: hits is | Number of times a B-tree page was in memory meets your specified threshold. |
| B-tree: misses is | Number of times a B-tree page was *not* in memory meets your specified threshold. |
| B-tree: miss ratio is | Ratio of misses to hits meets your specified threshold. |

#### Effective Lock %

**Important:** Applies to MongoDB 2.2 to 2.6 only

This metric only triggers alerts on deployments running MongoDB
versions 2.2 through 2.6.

You may set alerts for what percentage of time the MongoDB instance is
write locked. Effective Lock percentage metrics
include:

| Metric | Alert Trigger |
|---|---|
| Effective Lock % is | If the percent of total time the instance is write locked meets your specified threshold. |

#### Background Flush Average

**Important:** Applies to databases running MMAPv1 only

This metric only triggers alerts on deployments running MMAPv1
storage engines for their MongoDB databases.

You may set an alert for how long in milliseconds the average flush on
the MongoDB instance take to complete. A flush is the writing of data
to disk from memory.

**Note:** How It Is Measured

MongoDB reports on average background flush time using the
`backgroundFlushing.average_ms` value that the
serverStatus command
returns.

Background flush average metrics include:

| Metric | Alert Trigger |
|---|---|
| Background Flush Average is | Average time for background flushes meets your specified threshold. |

#### Connections

You may set alerts for the active connections to the MongoDB instance.

**Note:** How It Is Measured

MongoDB reports on memory using the `connections` document that
the serverStatus command
returns.

Connection metrics include:

* - Metric
  - Alert Trigger

* - Connections is
  - Number of active host connections meets your specified
    threshold.

* - Connections % of configured limit is
  - Percentage of active host connections to the total number of
    possible connections meets your specified threshold. The
    default value for MongoDB versions 2.6.0 and 3.0.0 is `65536`
    and the default value for MongoDB versions greater than (`>`)
    3.0.0,  is `1000000`. You can override the default value two
    ways: 

    - Use the mongod `--maxConnns` to set
      the maximum number of simultaneous connections for `mongod`.
      To learn more, see mongod Core Options. 

    - Update the `net.maxIncomingConnections` field in the
      MongoDB configuration file. To learn more, see net
      Options.

**Note:**

You can create charts for a selection of these metrics in Ops Manager. 

1. From the Ops Manager project's Deployment view, click the 
   List tab.
#. Click the process for which you want to monitor. 
#. Click the Status tab.
#. Scroll down to the list of available metrics and select the 
   desired metric(s) to chart. 

To learn more about creating charts for host metrics in 
Ops Manager, see /tutorial/view-diagnostics and click the
MongoDB Process Metrics tab.

#### Queues

You may set alerts for the operations waiting on locks.

**Note:** How It Is Measured

MongoDB reports on memory using the `globalLock.currentQueue`
document that the
serverStatus
command returns.

Queue metrics include:

| Metric | Alert Trigger |
|---|---|
| Queues: Total is | Number of operations waiting on a lock of any type meets your specified threshold. |
| Queues: Readers is | Number of reader operations waiting on a lock of any type meets your specified threshold. |
| Queues: Writers is | Number of writer operations waiting on a lock of any type meets your specified threshold. |

**Note:**

You can create charts for a selection of these metrics in Ops Manager. 

1. From the Ops Manager project's Deployment view, click the 
   List tab.
#. Click the process for which you want to monitor. 
#. Click the Status tab.
#. Scroll down to the list of available metrics and select the 
   desired metric(s) to chart. 

To learn more about creating charts for host metrics in 
Ops Manager, see /tutorial/view-diagnostics and click the
MongoDB Process Metrics tab.

#### Page Faults

**Important:** Applies to MongoDB 2.2 to 2.6 only

The Accesses Not In Memory: Total is and
Page Fault Exceptions Thrown: Total is metrics only
trigger alerts on deployments running MongoDB versions 2.2 through
2.6.

You may set alerts for page faults.

**Note:** How It Is Measured

MongoDB reports on memory using the `extra_info.page_faults`
document that the
serverStatus command
returns.

MongoDB 2.2 through 2.6 reported on the
Accesses Not In Memory: Total is and
Page Fault Exceptions Thrown: Total is metrics using
the `recordStats` document that the
serverStatus command
returned.

Page Fault metrics include:

| Metric | Alert Trigger |
|---|---|
| Accesses Not In Memory: Total is | Rate of disk accesses meets your specified threshold. MongoDB must access data on disk if your working set does not fit in memory. This metric is found on the host's `Record Stats` chart. |
| Page Fault Exceptions Thrown: Total is | Rate of page fault exceptions thrown meets your specified threshold. This metric is found on the host's `Record Stats` chart. |
| Page Faults is | Rate of page faults (whether or not an exception is thrown) meets your specified threshold. This metric is found on the host's `Page Faults` chart. |

**Note:**

You can create charts for a selection of these metrics in Ops Manager. 

1. From the Ops Manager project's Deployment view, click the 
   List tab.
#. Click the process for which you want to monitor. 
#. Click the Status tab.
#. Scroll down to the list of available metrics and select the 
   desired metric(s) to chart. 

To learn more about creating charts for host metrics in 
Ops Manager, see /tutorial/view-diagnostics and click the
MongoDB Process Metrics tab.

#### Cursors

You may set alerts for the number of open and timed-out
cursors for a MongoDB process.

**Note:** How It Is Measured

MongoDB reports on memory using the `metrics.cursor` document that
the serverStatus command
returns.

Cursor metrics include:

| Metric | Alert Trigger |
|---|---|
| Cursors: Client Cursors Size is | Amount of memory the host uses to maintain cursors meets your specified threshold. |
| Cursors: Open is | Number of cursors the host is maintaining for clients meets the specified threshold. |
| Cursors: Timed Out is | Number of timed-out cursors the host is maintaining for clients meets your specified threshold. |

**Note:**

You can create charts for a selection of these metrics in Ops Manager. 

1. From the Ops Manager project's Deployment view, click the 
   List tab.
#. Click the process for which you want to monitor. 
#. Click the Status tab.
#. Scroll down to the list of available metrics and select the 
   desired metric(s) to chart. 

To learn more about creating charts for host metrics in 
Ops Manager, see /tutorial/view-diagnostics and click the
MongoDB Process Metrics tab.

#### Network

You may set alerts for the network throughput for a MongoDB process.

**Note:** How It Is Measured

MongoDB reports on memory using the `network` document that the
serverStatus command returns.

Network metrics include:

* - Metric
  - Alert Trigger

* - Network: Bytes In is
  - Number of bytes sent *to* the database host meets your
    specified threshold.

* - Network: Bytes Out is
  - Number of bytes sent *from* the database host meets your
    specified threshold.

* - Network: Num Requests is
  - Number of requests sent *to* the database host meets your
    specified threshold.

**Note:**

You can create charts for a selection of these metrics in Ops Manager. 

1. From the Ops Manager project's Deployment view, click the 
   List tab.
#. Click the process for which you want to monitor. 
#. Click the Status tab.
#. Scroll down to the list of available metrics and select the 
   desired metric(s) to chart. 

To learn more about creating charts for host metrics in 
Ops Manager, see /tutorial/view-diagnostics and click the
MongoDB Process Metrics tab.

#### Replication Oplog

You may set alerts for the replication oplogs for a MongoDB process.

**Note:** How It Is Measured

MongoDB reports on the Replication Oplog using the `oplog`
document that the
serverStatus command
returns combined with results from
rs.status() and
rs.conf().

Replication oplog metrics include:

| Metric | Alert Trigger |
|---|---|
| Replication Headroom is | Difference between the sync source's replication oplog window and the secondary's replication lag meets your specified threshold. A secondary can go into `RECOVERING` if this value goes to `0`. |
| Replica Time is | Approximate amount of time in milliseconds available in the primary's replication oplog meets your specified threshold. |
| Oplog Data Per Hour is | Average rate of gigabytes of oplog the primary generates per hour meets your specified threshold. |
| Replication Lag is | Approximate number of seconds the secondary is behind the primary in write application. Only accurate if the lag is larger than 1-2 seconds, as the precision of this statistic is limited. |

**Note:**

You can create charts for a selection of these metrics in Ops Manager. 

1. From the Ops Manager project's Deployment view, click the 
   List tab.
#. Click the process for which you want to monitor. 
#. Click the Status tab.
#. Scroll down to the list of available metrics and select the 
   desired metric(s) to chart. 

To learn more about creating charts for host metrics in 
Ops Manager, see /tutorial/view-diagnostics and click the
MongoDB Process Metrics tab.

#### Operations Scan and Order

You may set alerts for the scan and order operations for a MongoDB
process.

**Note:** How It Is Measured

MongoDB reports on the Replication Oplog using the
`metrics.operation.scanAndOrder` document that the
serverStatus
command returns.

Operations metrics include:

| Metric | Alert Trigger |
|---|---|
| Operations: Scan and Order is | Average rate per second over your specified threshold of queries that return sorted results that cannot perform the sort operation using an index. |

#### DB Storage

You may set alerts for the amount of data storage used. Database
storage metrics include:

| Metric | Alert Trigger |
|---|---|
| DB Storage is | Amount of on-disk storage space used by extents meets your specified threshold. |
| DB Data Size is | Actual data size in the database meets your specified threshold. |

**Note:**

You can create charts for a selection of these metrics in Ops Manager. 

1. From the Ops Manager project's Deployment view, click the 
   List tab.
#. Click the process for which you want to monitor. 
#. Click the Status tab.
#. Scroll down to the list of available metrics and select the 
   desired metric(s) to chart. 

To learn more about creating charts for host metrics in 
Ops Manager, see /tutorial/view-diagnostics and click the
MongoDB Process Metrics tab.

#### Journaling

You may set alerts for the amount of journaling storage used.
Journaling metrics include:

| Metric | Alert Trigger |
|---|---|
| Journaling Commits in Write Lock is | Rate of commits that occurred while the database was in write lock meets your specified threshold. |
| Journaling MB is | Average amount of data in megabytes Ops Manager writes to the recovery log per second meets your specified threshold. |
| Journaling Write Data Files MB is | Average rate of data in megabytes Ops Manager writes to the databases datafiles per second meets your specified threshold. As these writes are already journaled, they can occur lazily, and thus the number indicated here may be lower than the amount physically written to disk. |

**Note:**

You can create charts for a selection of these metrics in Ops Manager. 

1. From the Ops Manager project's Deployment view, click the 
   List tab.
#. Click the process for which you want to monitor. 
#. Click the Status tab.
#. Scroll down to the list of available metrics and select the 
   desired metric(s) to chart. 

To learn more about creating charts for host metrics in 
Ops Manager, see /tutorial/view-diagnostics and click the
MongoDB Process Metrics tab.

#### WiredTiger Storage Engine

You may set alerts for WiredTiger tickets.

**Note:** How It Is Measured

MongoDB reports on WiredTiger using the
`wiredTiger.cache` and
`wiredTiger.concurrentTransactions` documents that the
serverStatus command returns.

WiredTiger storage engine conditions include:

| Metric | Alert Trigger |
|---|---|
| Tickets Available: Reads is | Number of read tickets available to the WiredTiger storage engine meet your specified threshold. |
| Tickets Available: Writes is | Number of write tickets available to the WiredTiger storage engine meet your specified threshold. |

**Note:**

You can create charts for a selection of these metrics in Ops Manager. 

1. From the Ops Manager project's Deployment view, click the 
   List tab.
#. Click the process for which you want to monitor. 
#. Click the Status tab.
#. Scroll down to the list of available metrics and select the 
   desired metric(s) to chart. 

To learn more about creating charts for host metrics in 
Ops Manager, see /tutorial/view-diagnostics and click the
MongoDB Process Metrics tab.

#### System and Disk Alerts

You may set alerts for compute and disk utilization. System resource
conditions include:

| Metric | Alert Trigger |
|---|---|
| System: CPU (Steal) % is | *Applicable when the EC2 instance credit balance is exhausted.* The percentage of time the CPU is in a state of "involuntary wait". CPU steal percentage is the percentage by which the CPU usage exceeds the guaranteed baseline CPU credit accumulation rate. This alert typically triggers when all credits have been consumed on an [AWS burstable performance instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/burstable-performance-instances.html). |
| System: Max CPU (Steal) % is | Maximum percentage of time that the CPU is in a state of "involuntary wait" exceeds the specified threshold. |
| System: CPU (User) % is | CPU usage of the MongoDB process, scaled to a range of 0-100% by dividing by the number of CPUs. |
| System: Max CPU (User) % is | Maximum CPU usage of the MongoDB process, scaled to a range of 0-100% by dividing by the number of CPUs exceeds the specified threshold. |
| System Memory: Used is | Total system memory used for the `mongod` minus buffers, cached, and free memory meets the specified threshold. |
| System Memory: Max Used is | Maximum system memory usage value meets the specified threshold. |
| System Memory: Available is | Available system memory usage for the `mongod` has dropped below the specified threshold. |
| System Memory: Max Available is | Maximum amount of available system memory drops below the specified threshold. |
| Disk space % used on Data Partition is | Percentage of disk space used on any partition that contains the MongoDB collection's data. |
| Max disk space % used on Data Partition is | Maximum percentage of disk space used on any partition that contains the MongoDB collection's data exceeds the specified threshold. |
| Disk space % used on Index Partition is | Percentage of disk space used on any partition that contains the MongoDB index data. |
| Max disk space % used on Index Partition is | Maximum percentage of disk space used on any partition that contains the MongoDB index data exceeds the specified threshold. |
| Disk space % used on Journal Partition is | Percentage of disk space used on the partition that contains the MongoDB journal, if journaling is enabled. |
| Max disk space % used on Journal Partition is | Maximum percentage of disk space used on the partition that contains the MongoDB journal exceeds the specified threshold. |
| System Network In is | Number of bytes per second sent *to* the database host meets the specified threshold. |
| Max System Network In is | Maximum number of bytes sent *to* MongoDB meets the specified threshold. |
| System Network Out is | Number of bytes per second sent *from* the database host meets your specified threshold. |
| Max System Network Out is | Maximum number of bytes sent *from* MongoDB meets the specified threshold. |

**Note:**

You can create charts for a selection of these metrics in Ops Manager. 

1. From the Ops Manager project's Deployment view, click the 
   List tab.
#. Click the process for which you want to monitor. 
#. Click the Status tab.
#. Scroll down to the list of available metrics and select the 
   desired metric(s) to chart. 

To learn more about creating charts for host metrics in 
Ops Manager, see /tutorial/view-diagnostics and click the
MongoDB Process Metrics tab.

## Replica Set Alerts

You may set alerts about the status of the primary and the
number of healthy members in a replica set. Replica set
conditions include:

| Condition | Alert Trigger |
|---|---|
| Replica set elected a new primary | A set elects a new primary. Each time Ops Manager receives a ping, it inspects the output of the replica set's rs.status() method for the status of each replica set member. From this output, Ops Manager determines which replica set member is the primary. If the primary found in the ping data is different than the current primary known to Ops Manager, this alert triggers. Receiving this alert does not always mean that the set elected a *new* primary. This alert may also trigger when the same primary is re- elected. This can happen when Ops Manager processes a ping in the midst of an election. |
| Replica set has no primary | A replica set does not have a primary. Specifically, when none of the members of a replica set have a status of `PRIMARY`, the alert triggers. For example, this condition may arise when a set has an even number of voting members resulting in a tie. If the Monitoring collects data during an election for primary, this alert might send a false positive. To prevent such false positives, set the alert configuration's after waiting interval (in the configuration's Send to section). For resolutions, see /reference/alerts/no-primary. |

Replica set metrics include:

| Metric | Alert Trigger |
|---|---|
| Number of healthy members is | A replica set has fewer healthy members than your specified threshold. |
| Number of unhealthy members is | A replica set has more unhealthy members than your specified threshold. |
| Number of elections in last hour is > X | Number of elections that have occurred in the last hour exceeded the user-specified value of `X`. The value of `X` is set when you create the alert. This alert may indicate that the cluster's replication is not in a healthy state, as evidenced by constant elections. |

**Note:**

A replica set member is healthy if you run
rs.status() for that
replica set and the result returns `PRIMARY` or
`SECONDARY` for that member. Hidden secondaries and
arbiters are not counted.

## Sharded Cluster Alerts

You may set an alert for a `mongos` missing from a
sharded cluster. Sharded cluster conditions include:

| Condition | Alert Trigger |
|---|---|
| Cluster is missing an active mongos | Ops Manager cannot reach **any** `mongos` for the cluster. |

## Agent Alerts

You may set alerts for agent status or versioning. Agent conditions
include:

* - Condition
  - Alert Trigger

* - Automation is down
  - No Automation is detected for at least 1 minute. Under
    normal operation, the Automation sends a ping to Ops Manager
    roughly once every 10 seconds. If Ops Manager does not receive a ping
    for at least 1 minute, this alert triggers. 

    This alert triggers only if the Automation is managing a
    MongoDB process or agent module.

* - Monitoring is down
  - No Monitoring is detected for at least 7 minutes. Under
    normal operation, the Monitoring sends a ping to Ops Manager
    roughly once per minute. If Ops Manager does not receive a ping for at
    least 7 minutes, this alert triggers. However, this alert never
    triggers for a project that has no hosts configured.

    **Important:**

    When the Monitoring is down, Ops Manager triggers no other alerts
    for any host. For example: if a host is down there is no Monitoring to send data to Ops Manager that could trigger new alerts.

* - Monitoring does not have the latest version
  - Monitoring is not running the latest version of the
    software.

* - Backup is down
  - Backup for a project with at least one active replica
    set or cluster is down for more than 1 hour.

    To resolve this alert:

    #. To see which host serves the Backup,
       click Deployment, then the Servers tab.

    #. Check the Backup log file on that host.

* - Backup does not have the latest version
  - Backup is not running the latest version of the
    software.

* - Backup has too many conf call failures
  - The cluster topology known to monitoring does not match the backup
    configuration from conf calls the Backup
    makes. 

    The number of attempts meets the threshold you specified in
    `maximumFailedConfCalls`
    setting.

    **Note:** Global alert only

## Backup Alerts

You may set alerts for backup oplog, resync and inconsistencies. Backup
conditions include:

* - Condition
  - Alert Trigger

* - Backup oplog is behind
  - Most recent oplog data received by Ops Manager is more
    than 75 minutes old.

    To resolve this alert, see
    /reference/alerts/backup-oplog-is-behind.

* - Backup requires a resync
  - Replication process for a backup falls too far behind the
    oplog to catch up. This occurs when the host overwrites
    oplog entries that backup has not yet replicated. When this
    happens, you must resync backup, as described in the procedure
    /tutorial/resync-backup.

    Also, check the corresponding Backup log. If you see a
    "Failed Common Points" test, one of the following may have
    happened.

    - A significant rollback event occurred on the backed-up replica
      set.

    - oplog for the
      backed-up replica set was resized or deleted.

    - High oplog churn caused the agent to lose the tail of the
      oplog.

* - Inconsistent backup configuration has been detected
  - Ops Manager has detected that the configuration for a backup does not
    match the configuration of the MongoDB deployment it backs up.

    To resolve this alert, see /reference/alerts/inconsistent-backup.

* - Inconsistent cluster snapshot count is...
  - Ops Manager fails a consecutive number of times to successfully take a
    cluster snapshot. This alert is triggered when the number of
    attempts meets your specified threshold.

    The alert text may contain the reason for the problem. Common
    problems include:

    - There was no reachable `mongos`.
      To resolve this issue, ensure that there is at least one
      `mongos` showing on the Ops Manager
      Deployment page.

    - balancer could not be
      stopped. To resolve this issue, check the log files for the
      first config server
      to determine why the balancer will not stop.

    - Could not insert a token in one or more
      shards. To resolve
      this issue, ensure connectivity between the Backup and
      all shards.

* - Backup could not be assigned to a backup daemon

  - A backup job fails to bind to a Backup Daemon. 

    **Example:**

    Reasons that a job might fail to bind include, but are not
    limited to:

    - No primary is found for the backed-up replica
      set. At the time the binding occurred, the Monitoring did not detect a primary. Ensure that the replica
      set is healthy.

    - Not enough space is available on any Backup Daemon.

    In both cases, resolve the issue and then restart the
    initial sync of the backup.

    As an alternative, you can manually bind jobs to daemons
    through the Admin interface. See
    jobs-page for more information.

    **Note:** Global alert only

* - Backup has reached a high number of retries

  - Sends an alert if the same task fails repeatedly. This could
    happen, for example, during maintenance. Check the
    corresponding job log for an error message
    explaining the problem.

    Contact MongoDB Support if you need help interpreting the
    error message.

    **Note:** Global alert only

* - Backup is in an unexpected state

  - Something unexpected happened and the Backup state for the
    replica set is `broken`. You must resync the backed-up
    replica set, as described in the
    /tutorial/resync-backup procedure.

    In case of a `Backup is in an unexpected state` alert,
    check the corresponding job log for an
    error message explaining the problem. Contact MongoDB Support
    if you need help interpreting the error message.

    **Note:** Global alert only

* - Replica set has a late snapshot

  - A snapshot has failed to complete before the next snapshot is
    scheduled to begin. Check the job log in
    the Ops Manager Admin interface for any errors.

    **Note:** Global alert only

* - Sync slice transfer has not progressed in...

  - An `initial sync` has started but then subsequently
    stalled. Issues that can cause this, include, but are not
    limited to:

    - processes that are down (agents, ingest, backing databases)
    - network issues
    - incorrect authentication credentials

    **Note:** Global alert only

* - Backup job is busy for...

  - One backup job has been working for more hours within a
    24-hour period than your specified threshold.

    Different backup jobs share Backup Daemons or `snapshot stores`. Backup
    job execution time can vary. Long running backup jobs can
    cause the remaining jobs to fall behind or fail. Set this
    metric to how long you expect backups should take to complete
    in your deployment.

    You should check the corresponding job log
    for error messages. Contact MongoDB Support if you need help
    interpreting the error message.

    **Note:** Global alert only

## BI Connector Alerts

These alert conditions apply to use of the BI Connector with Ops Manager.

* - Condition
  - Alert Trigger

* - .. alert:: BI Connector is down
  - The Automation has not detected the BI Connector
    process for at least 4 minutes.

    **Important:**

    When the Automation is down, Ops Manager cannot
    trigger alerts for the BI Connector.

## User Alerts

You can set alerts for Ops Manager user addition, removal,
and role changes. These alerts apply to Ops Manager users,
not MongoDB database users. Ops Manager user conditions
include:

| Condition | Alert Trigger |
|---|---|
| User joined the project | An Ops Manager user joins the project. |
| User left the project | An Ops Manager user leaves the project. |
| User had their role changed | An Ops Manager user's roles have been changed. |

## Project Alerts

You may set alerts for user approval and authentication configuration.
Project conditions include:

| Condition | Alert Trigger |
|---|---|
| Users do not have two-factor authentication enabled | Project has users who have not set up two-factor authentication. |
| Security checkup alerts updated | The project's security checkup alerts changed. |
