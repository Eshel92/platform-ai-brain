<!-- Converted from tutorial/profile-database.txt (reStructuredText). Includes are inlined. -->

# Profile Databases

**Note:** **Available only with the MongoDB Agent with Automation**

This feature is available only with the MongoDB Agent with Automation. To learn 
more about the MongoDB Agent with Automation, see
add-mdb-processes.

A database profiler
gathers statistics about writes, cursors, and commands on one running
`mongod` instance.

Ops Manager can collect and display statistics from any of your `mongod`
instances that have profiling enabled. Ops Manager displays this data in the
Profiler section of an instance's Metrics page.
To access an instance's metrics, click the Metrics button
for that instance.

The Profiler displays one aspect, like *Operation Execution
Time*, that could slow database operations over a set time frame. It
displays this data in both a chart and a table that each can filter on
aspect and time frame. The Profiler suggests indexes for your databases
to improve the performance of slow operations.

## Considerations

**Important:** Please read the following considerations before you enable profiling.

### Security

Profile data may include sensitive information including the content of
database queries. Ensure that exposing this data to Ops Manager is consistent
with your information security practices.

### `system.profile` Collection

The MongoDB profiler stores data in the
`system.profile <<database>.system.profile>` collection. Ops Manager
caps this collection to 1 MB as a default.
You may increase the size of this collection up to 4 MB.

When collecting data from the profiler, Ops Manager ignores operations on
the `system.profile <<database>.system.profile>` collection,
such as Monitoring queries of the
`system.profile <<database>.system.profile>` collection.

### Resource Consumption Impact

The profiler consumes resources which may slow MongoDB performance.
Consider the resource impact before enabling profiling.

#### Data Collection

Every minute, the agent queries the
`system.profile <<database>.system.profile>` collection for the
last 20 documents created. Monitoring sends
those documents to Ops Manager.

**See also:**

Database Profiler
in the MongoDB Manual.

Ops Manager samples profile documents until it samples either all documents
returned or 4 MB of returned document data. This 4 MB limit may be
reached if you increase the collection's size to 4 MB *and* your
database creates large
profiler documents.

Monitoring tries to minimize its effect on the monitored systems.
If polling profile data slows database performance, Ops Manager throttles how
often it collects data.

#### Data Display

Ops Manager displays no more than 10,000 data points in the
Profiler charts.

### Time to Propagate Changes to the MongoDB Agent

With profiling enabled, configuration changes made in Ops Manager can
take up to 2 minutes to propagate to the agent and 1 more minute before
profiling data appears in the Ops Manager interface.

### Rolling Restart of `mongod` Processes

Ops Manager performs a `rolling restart` of the `mongod` processes in
your cluster when you enable or disable database profiling. If your
cluster is a replica set, a replica set election occurs as a byproduct of the restart.
This one-time operation is in addition to the time required to
propogate configuration changes to the Automation.

## Enable Profiling

As of Ops Manager version 4.4, Ops Manager always enables profiling. Your
`mongod` instance collects profile data for operations longer than
the slow operation threshold and
reports them to Ops Manager. The threshold for slow operations applies to the entire `mongod` instance. Ops Manager defaults this threshold to 100 ms.

## Profiler Interface

The Profiler has two sections to the page that display database profile
information: a chart and a table. Each can display different data.

### Profiling Chart

#### Set Chart Filters

Above the chart, select the metric and time period you want to see.

1. Select the metric from the Display menu. Accepted
   options are:

   - Operation Execution Time (default)
   - Keys Examined
   - Docs Returned
   - Examined:Returned Ratio
   - Num Yields
   - Response Length

#. Select the time period from the View Last menu.
   Accepted options are:

   - 24 hr (default)
   - 12 hr
   - 6 hr
   - 1 hr
   - 15 min

#### Request Index Suggestions

Based on the Profiler data, you may want to improve the performance of
slow queries.

1. Click Calculate Suggested Indexes to direct Ops Manager to
   analyze your databases.

#. After the analysis completes, the
   Suggested Indexes for Improving Query Performance modal
   displays.

   This modal offers suggested indexes with the appropriate database
   commands to created those indexes.

#. After you have finished using the suggested indexes, click
   OK to close the modal.

### Profiling Table

Above the table, select the namespace, operation type, and metric you
wish to profile:

1. Click All Namespaces to change which combination of
   databases and collections to profile.

#. Click All Operations to change which operations you want
   to profile.

#. Click Operation Execution Time to change which metric
   you want to profile. Accepted options are:

   - Operation Execution Time (default)
   - Keys Examined
   - Docs Returned
   - Examined:Returned Ratio
   - Num Yields
   - Response Length
