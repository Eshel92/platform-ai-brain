<!-- Converted from view-real-time-metrics.txt (reStructuredText). Includes are inlined. -->

# View Real Time Metrics

**Note:** **Availability**

Ops Manager can display real-time metrics for MongoDB deployments that
Automation manages. Collection of real time data requires the 
MongoDB Agent.

Ops Manager supports real-time metrics for `mongod` (replica sets and
shards) and `mongos` processes.

To view real-time metrics, click the Metrics button
for the desired deployment, then click Real Time.

Monitor deployment metrics to identify performance issues and 
determine whether your current deployment meets your 
requirements. To learn more about the metrics available to monitor 
your deployments, see review-available-metrics.

To access this feature, you must either:

- Belong to the project

- Have the Global Monitoring Admin role or the Global Owner role

In the upper-right corner, you can click to view the metrics in a 
Table or Graph.

## Enable or Disable Real-Time Performance Panel for a Project

**Note:** **Required Privileges**

To enable Real-Time Performance Panel for a project, 
you must have the `Project Owner` role for the project.

Ops Manager enables the **Real-Time Performance Panel** by default. To toggle
this setting:

**Step 1: Click Settings.**

**Step 2: Toggle the button next to Real-Time Performance Panel.**

## Table View

* - Fields

  - Displays

* - | Commands
    | Queries
    | Updates
    | Deletes
    | Inserts
    | GetMores

  - Number of the specified operations
    (commands, queries, etc.) that
    mongostat
    has reported.

* - | Time / Read
    | Time / Write
    | Time / Command

  - Latency metrics for current read requests,
    write requests, and other database commands. Available
    only for MongoDB 3.4+. To learn more, see `opLatencies`
    at serverStatus.

* - | Scanned / Returned
    | Scanned Objects / Returned

  - Ratio of documents and objects scanned to
    documents and objects returned in current queries. These
    metrics are useful in determining if and how a query
    uses an index. To learn more, see 
    Analyze Query Performance.

* - | Active Readers
    | Active Writers
    | Queued Readers
    | Queued Writers

  - Number of active reads, queued reads, active
    writes, and queued writes that
    mongostat
    has reported.

* - | Lag Time

  - Time required to replicate operations from
    the primary to the secondary members of a replica set.
    Available only for secondary members of a replica set.
    To learn more, see
    Replica Set Secondary Members.

* - | CPU
    | Disk IOPS
    | Sys Mem

  - Statistic depending on the operating system of the
    nodes in your cluster:

    * Linux: Displays the currently used percentage of CPU and disk
      capacity and the total physical memory usage, excluding buffers,
      cache and swap space, of the machine hosting MongoDB.

    * macOS: Displays the currently used percentage of CPU and disk
      capacity and the total physical memory usage, excluding cache and
      swap space, of the machine hosting MongoDB.

    * Windows:  Displays the currently used percentage of CPU and disk
      capacity and the total physical memory usage of the machine hosting
      MongoDB.

* - | Connections
    | Bytes In
    | Bytes Out

  - Number of current connections to the
    machine hosting MongoDB and the number of inbound and
    outbound bytes that
    mongostat
    has reported.

Click ellipsis-h to hide or display fields from
the table.

## Graph View

* - Chart
  - Displays

* - Connections, Network In, Network Out

  - Number of current connections to the machine
    hosting MongoDB and the number of inbound and outbound
    bytes that
    mongostat
    has reported.

* - CPU, Disk IOPS, and Sys Mem

  - Statistic depends on the operating system of the
    nodes in your cluster:

    * Linux: Displays the currently used percentage of CPU and disk
      capacity and the total physical memory usage, excluding buffers,
      cache and swap space, of the machine hosting MongoDB.

    * macOS: Displays the currently used percentage of CPU and disk
      capacity and the total physical memory usage, excluding cache and
      swap space, of the machine hosting MongoDB.

    * Windows:  Displays the currently used percentage of CPU and disk
      capacity and the total physical memory usage of the machine hosting
      MongoDB.

* - Operations

  - Number of operations as reported by
    mongostat.

* - Query Execution Times

  - Displays latency metrics for current read requests,
    write requests, and other database commands. Available
    only for MongoDB 3.4+. To learn more, see `opLatencies`
    at serverStatus.

* - Query Targeting

  - Ratio of documents and objects scanned to
    documents and objects returned in current queries. These
    metrics are useful in determining if and how a query
    uses an index. To learn more, see
    Analyze Query Performance.

* - Reads & Writes

  - Number of active reads, queued reads, active
    writes, and queued writes as reported by
    mongostat.

* - Replication Lag

  - Time required to replicate operations from
    the primary to the secondary members of a replica set.
    Available only for secondary members of a replica set.
    To learn more, see
    Replica Set Secondary Members.

* - Hottest Collections

  - Collections with the most operations that
    mongotop
    has reported. For each hot collection, the table also
    displays the Utilization Percent for the
    collection.

    Utilization Percent is calculated from the 
    read and write times that 
    mongotop
    has reported during a sample period. Specifically, the
    Utilization Percent is the percentage
    (rounded to the nearest 0.1%) of the read and write
    times for a collection relative to the read and write
    times for all collections in the deployment during the
    sample period. If no read and write operation occur
    during this period, the Utilization Percent
    may be 0%.

    The hottest collections correspond to the most current
    time displayed in the charts. That is, if the display is
    running (not paused), the collections correspond to
    the hottest collections at the current timestamp. If the
    display is paused, the collections correspond to the
    hottest collections at the paused time.

* - Slowest Operations

  - Slowest operations that the
    db.currentOp()
    has reported.

    The operations correspond to the most current time
    displayed in the charts. That is, if the display is
    running (not paused), the operations correspond to
    the slowest operations at the current timestamp. If the
    display is paused, the operations correspond to the
    slowest operations at the paused time.

    Click the operation to view the detailed JSON
    document that 
    db.currentOp()
    has reported for the operation.

    Users with the
    Data Access Admin
    role can access buttons to force stop an operation or
    an inactive transaction in the operation details panel:

    To stop a slow operation:

    #. Click the operation in the Slowest Operations 
       pane.

    #. Click Kill Op in the 
       Operation Details pane.

       Alternatively, click Kill Session if the
       operation is  an inactive transaction.

    #. Click Yes, terminate this operation in the
       Confirm Operation modal.

    To learn more about
    transactions, refer to
    the MongoDB manual.

To hide/show a metric in the graph, click the color box for
the metric.

## Read Exact Metrics from Graph View

If you pause the Graph view of the Real-Time
Performance Panel, you can hover over a line graph to see its
exact value, along with the slowest operations and hottest
collections, at a given moment in time.

## Stop and Restart Display

To stop the update of the metrics displayed, click
Pause. Pause only
stops the update of the displays and doesn't pause the
collection of the underlying data.

To restart the display updates, click Play.
