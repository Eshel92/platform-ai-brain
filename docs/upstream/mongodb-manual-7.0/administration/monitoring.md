<!-- Converted from administration/monitoring.txt (reStructuredText). Includes are inlined. -->

# Monitoring a Self-Managed MongoDB Deployment

Monitoring is a critical component of all database administration. A
firm grasp of MongoDB's reporting will allow you to assess the state
of your database and maintain your deployment without crisis.
Additionally, a sense of MongoDB's normal operational parameters will
allow you to diagnose problems before they escalate to failures.

This document presents an overview of the available monitoring utilities
and the reporting statistics
available in MongoDB. It also introduces diagnostic strategies
and suggestions for monitoring replica sets and
sharded clusters.

## Monitoring Strategies

MongoDB provides various methods for collecting data about the state of
a running MongoDB instance:

- MongoDB distributes a set of utilities that provides real-time
  reporting of database activities.

- MongoDB provides various database commands that return statistics regarding the current
  database state with greater fidelity.

- [MongoDB Atlas](https://www.mongodb.com/atlas/database)
  is a cloud-hosted database-as-a-service for running, monitoring, and
  maintaining MongoDB deployments. 
  
- [MongoDB Cloud Manager](https://www.mongodb.com/products/tools/cloud-manager) is a hosted service that monitors running MongoDB
  deployments to collect data and provide visualization and alerts
  based on that data.
  
- MongoDB Ops Manager is an on-premises solution available in
  MongoDB Enterprise Advanced
  that monitors running MongoDB deployments to collect data and provide
  visualization and alerts based on that data.

Each strategy can help answer different questions and is useful in
different contexts. These methods are complementary.

## MongoDB Reporting Tools

This section provides an overview of the reporting methods distributed
with MongoDB. It also offers examples of the kinds of questions that
each method is best suited to help you address.

### Utilities

The MongoDB distribution includes a number of utilities that quickly
return statistics about instances' performance and activity. Typically,
these are most useful for diagnosing issues and assessing normal
operation.

#### `mongostat`

`mongostat` captures and returns the counts of database
operations by type (e.g. insert, query, update, delete, etc.). These
counts report on the load distribution on the server.

Use `mongostat` to understand the distribution of operation
types and to inform capacity planning. See the `mongostat`
reference page for details.

#### `mongotop`

`mongotop` tracks and reports the current read and write
activity of a MongoDB instance, and reports these statistics on a per
collection basis.

Use `mongotop` to check if your database activity and use
match your expectations. See the `mongotop` reference page
for details.

### Commands

MongoDB includes a number of commands that report on the state of the
database.

These data may provide a finer level of granularity than the utilities
discussed above. Consider using their output in scripts and programs to
develop custom alerts, or to modify the behavior of your application in
response to the activity of your instance. The `db.currentOp`
method is another useful tool for identifying the database instance's
in-progress operations.

#### `serverStatus`

The `serverStatus` command, or `db.serverStatus()`
from the shell, returns a general overview of the status of the
database, detailing disk usage, memory use, connection, journaling,
and index access. The command returns quickly and does not impact
MongoDB performance.

`serverStatus` outputs an account of the state of a MongoDB
instance. This command is rarely run directly. In most cases, the data
is more meaningful when aggregated, as one would see with monitoring
tools including [MongoDB Cloud Manager](https://www.mongodb.com/products/tools/cloud-manager) and Ops Manager. Nevertheless, all
administrators should be familiar with the data provided by
`serverStatus`.

#### `dbStats`

The `dbStats` command, or `db.stats()` from the shell,
returns a document that addresses storage use and data volumes. The
`dbStats` reflect the amount of
storage used, the quantity of data contained in the database, and
object, collection, and index counters.

Use this data to monitor the state and storage capacity
of a specific database. This output also allows you to compare
use between databases and to determine the average
document size in a database.

#### `collStats`

The `collStats` or `db.collection.stats()` from the
shell that provides statistics that resemble `dbStats` on
the collection level, including a count of the objects in the
collection, the size of the collection, the amount of disk space used
by the collection, and information about its indexes.

#### `replSetGetStatus`

The `replSetGetStatus` command (`rs.status()` from
the shell) returns an overview of your replica set's status. The replSetGetStatus document details the
state and configuration of the replica set and statistics about its members.

Use this data to ensure that replication is properly configured,
and to check the connections between the current host and the other members
of the replica set.

#### Hosted (SaaS) Monitoring Tools

These are monitoring tools provided as a hosted service, usually through
a paid subscription.

| Name | Notes |
|---|---|
| [MongoDB Cloud Manager](https://www.mongodb.com/products/tools/cloud-manager) | MongoDB Cloud Manager is a cloud-based suite of services for managing MongoDB deployments. MongoDB Cloud Manager provides monitoring, backup, and automation functionality. For an on-premises solution, see also Ops Manager, available in MongoDB Enterprise Advanced. |
| [VividCortex](https://www.vividcortex.com/) | VividCortex provides deep insights into MongoDB [production database workload and query performance](https://www.vividcortex.com/product/how-it-works) -- in one-second resolution. Track latency, throughput, errors, and more to ensure scalability and exceptional performance of your application on MongoDB. |
| [Server Density](http://www.serverdensity.com) | [Dashboard for MongoDB](http://www.serverdensity.com/mongodb-monitoring/), MongoDB specific alerts, replication failover timeline and iPhone, iPad and Android mobile apps. |
| [Application Performance Management](http://ibmserviceengage.com) | IBM has an Application Performance Management SaaS offering that includes monitor for MongoDB and other applications and middleware. |
| [New Relic](http://newrelic.com/) | New Relic offers full support for application performance management. In addition, New Relic Plugins and Insights enable you to view monitoring metrics from Cloud Manager in New Relic. |
| [Datadog](https://www.datadoghq.com/) | [Infrastructure monitoring](http://docs.datadoghq.com/integrations/mongodb/) to visualize the performance of your MongoDB deployments. |
| [SPM Performance Monitoring](https://sematext.com/spm) | [Monitoring, Anomaly Detection and Alerting](https://sematext.com/spm/integrations/mongodb-monitoring/) SPM monitors all key MongoDB metrics together with infrastructure incl. Docker and other application metrics, e.g. Node.js, Java, NGINX, Apache, HAProxy or Elasticsearch. SPM provides correlation of metrics and logs. |
| [Pandora FMS](http://www.pandorafms.com/) | Pandora FMS provides the [PandoraFMS-mongodb-monitoring](http://blog.pandorafms.org/how-to-monitor-mongodb-or-how-to-keep-your-users-happy/) plugin to monitor MongoDB. |

## Process Logging

During normal operation, `mongod` and `mongos`
instances report a live account of all server activity and operations
to either
standard output or a log file. The following runtime settings
control these options.

- `quiet`. Limits the amount of information written to the
  log or output.

- `verbosity`. Increases the amount of information written to
  the log or output. You can also modify the logging verbosity during
  runtime with the `logLevel` parameter or the
  `db.setLogLevel()` method in the shell.

- `path`. Enables logging to a file, rather than the standard
  output. You must specify the full path to the log file when adjusting
  this setting.

- `logAppend`. Adds information to a log
  file instead of overwriting the file.

**Note:**

You can specify these configuration operations as the command line
arguments to mongod or mongos

For example:

```javascript
mongod -v --logpath /var/log/mongodb/server1.log --logappend
```

Starts a `mongod` instance in `verbose` mode, appending data to the log file at
`/var/log/mongodb/server1.log/`.

The following database commands also
affect logging:

- `getLog`. Displays recent messages from the
  `mongod` process log.

- `logRotate`. Rotates the log files for `mongod`
  processes only. See /tutorial/rotate-log-files.

### Log Redaction

*Available in MongoDB Atlas and MongoDB Enterprise only*

A `mongod` or `mongos` running with 
`redactClientLogData` redacts any message accompanying a given log
event before logging, leaving only metadata, source files, or line numbers 
related to the event. `redactClientLogData` prevents 
potentially sensitive information from entering the system log at the cost of 
diagnostic detail.

For example, the following operation inserts a document into a
`mongod` running without log redaction. The `mongod`
has the log verbosity level set to 
`1`:

```javascript
db.clients.insertOne( { "name" : "Joe", "PII" : "Sensitive Information" } )
```

This operation produces the following log event:

```javascript
{
   "t": { "$date": "2024-07-19T15:36:55.024-07:00" },
   "s": "I",
   "c": "COMMAND",
   ...
   "attr": {
      "type": "command",
      ...
      "appName": "mongosh 2.2.10",
      "command": {
         "insert": "clients",
         "documents": [
            {
               "name": "Joe",
               "PII": "Sensitive Information",
               "_id": { "$oid": "669aea8792c7fd822d3e1d8c" }
            }
         ],
         "ordered": true,
         ...
      }
      ...
   }
}
```

When `mongod` runs with `redactClientLogData` and
performs the same insert operation, it produces the following log event:

```javascript
{
   "t": { "$date": "2024-07-19T15:36:55.024-07:00" },
   "s": "I",
   "c": "COMMAND",
   ...
   "attr": {
      "type": "command",
      ...
      "appName": "mongosh 2.2.10",
      "command": {
         "insert": "###",
         "documents": [
            {
               "name": "###",
               "PII": "###",
               "_id": "###"
            }
         ],
         "ordered": "###",
         ...
      }
      ...
   }
}
```

Use `redactClientLogData` in conjunction with 
security-encryption-at-rest and transport-encryption to assist 
compliance with regulatory requirements.

## Diagnosing Performance Issues

As you develop and operate applications with MongoDB, you may want to
analyze the performance of the database as the application.
performance discusses some of the operational factors that can 
influence performance.

## Replication and Monitoring

Beyond the basic monitoring requirements for any MongoDB instance, for
replica sets, administrators must monitor *replication
lag*. "Replication lag" refers to the amount of time that it takes to
copy (i.e. replicate) a write operation on the primary to a
secondary. Some small delay period may be acceptable, but
significant problems emerge as replication lag grows, including:

- Growing cache pressure on the primary.

- Operations that occurred during the period of lag are not
  replicated to one or more secondaries. If you're using replication
  to ensure data persistence, exceptionally long delays may impact the
  integrity of your data set.

- If the replication lag exceeds the length of the operation
  log (oplog) then MongoDB will have to perform an initial
  sync on the secondary, copying all data from the primary and
  rebuilding all indexes. [#oplog]_ This is uncommon under normal circumstances,
  but if you configure the oplog to be smaller than the default,
  the issue can arise.

  **Note:**

  The size of the oplog is only configurable during the first
  run using the `--oplogSize` argument to
  the `mongod` command, or preferably, the
  `oplogSizeMB` setting
  in the MongoDB configuration file. If you do not specify this on the
  command line before running with the `--replSet`
  option, `mongod` will create a default sized oplog.

  By default, the oplog is 5 percent of total available disk space
  on 64-bit systems. For more information about changing the oplog
  size, see the /tutorial/change-oplog-size.

### Flow Control

Starting in MongoDB 4.2, administrators can limit the rate at which
the primary applies its writes with the goal of keeping the `majority
committed` lag under
a configurable maximum value `flowControlTargetLagSeconds`.

By default, flow control is `enabled`.

See also: replica-set-replication-lag.

### Replica Set Status

Replication issues are most often the result of network connectivity
issues between members, or the result of a primary that does not
have the resources to support application and replication traffic. To
check the status of a replica, use the `replSetGetStatus` or
the following helper in the shell:

```javascript
rs.status()
```

The `replSetGetStatus` reference provides a more in-depth
overview view of this output. In general, watch the value of
`optimeDate`, and pay particular attention
to the time difference between the primary and the
secondary members.

### Slow Application of Oplog Entries

Secondary members of a replica set now log oplog entries that take longer than the slow operation
threshold to apply. These slow oplog messages:

- Are logged for the secondaries in the
  `diagnostic log`.

- Are logged under the `REPL` component with the text
  `applied op: <oplog entry> took <num>ms`.

- Do not depend on the log levels (either at the system or component
  level)

- Do not depend on the profiling level.

- Are affected by `slowOpSampleRate`.

The profiler does not capture slow oplog entries.

## Sharding and Monitoring

In most cases, the components of sharded clusters
benefit from the same monitoring and analysis as all other MongoDB
instances. In addition, clusters require further monitoring to ensure
that data is effectively distributed among nodes and that sharding
operations are functioning appropriately.

**See also:**

See the /sharding documentation for more
information.

### Config Servers

The config database maintains a map identifying which
documents are on which shards. The cluster updates this map as
chunks move between shards. When a configuration
server becomes inaccessible, certain sharding operations become
unavailable, such as moving chunks and starting `mongos`
instances. However, clusters remain accessible from already-running
`mongos` instances.

Because inaccessible configuration servers can seriously impact
the availability of a sharded cluster, you should monitor your
configuration servers to ensure that the cluster remains well
balanced and that `mongos` instances can restart.

[MongoDB Cloud Manager](https://www.mongodb.com/products/tools/cloud-manager) and Ops Manager monitor config servers and can
create notifications if a config server becomes inaccessible. See the
`MongoDB Cloud Manager documentation` and `Ops Manager documentation` for more information.

### Balancing and Chunk Distribution

The most effective sharded cluster deployments evenly balance
chunks among the shards. To facilitate this, MongoDB
has a background balancer process that distributes data to ensure that
chunks are always optimally distributed among the shards.

Issue the `db.printShardingStatus()` or `sh.status()`
command to the `mongos` from within `mongosh`.
This returns an overview of the entire cluster including the
database name, and a list of the chunks.

### Stale Locks

To check the lock status of the database, connect to a
`mongos` instance using `mongosh`. Issue the
following command sequence to switch to the `config` database and
display all outstanding locks on the shard database:

```javascript
use config
db.locks.find()
```

The balancing process takes a special "balancer" lock that prevents
other balancing activity from transpiring. In the `config` database,
use the following command to view the "balancer" lock.

```javascript
db.locks.find( { _id : "balancer" } )
```

The primary of the CSRS config server holds the "balancer" lock, using a process 
ID named "ConfigServer". This lock is never released. To determine if the 
balancer is running, see sharding-balancing-is-running.

## Storage Node Watchdog

**Note:**

The Storage Node Watchdog is available in 
both the Community and MongoDB Enterprise editions.

The Storage Node Watchdog monitors the following MongoDB directories to
detect filesystem unresponsiveness:

* The `--dbpath` directory
* The `journal` directory inside the `--dbpath` 
  directory
* The directory of `--logpath` file
* The directory of `--auditPath` file

**Note:**

Starting in MongoDB 6.1, journaling is always enabled. As a result, MongoDB 
removes the `storage.journal.enabled` option and the corresponding 
`--journal` and `--nojournal` command-line options.

By default, the Storage Node Watchdog is disabled. You can only enable
the Storage Node Watchdog on a `mongod` at startup time by
setting the `watchdogPeriodSeconds` parameter to an integer
greater than or equal to 60. However, once enabled, you can pause the
Storage Node Watchdog and restart during runtime. See
`watchdogPeriodSeconds` parameter for details.

If any of the filesystems containing the monitored directories become
unresponsive, the Storage Node Watchdog terminates the
`mongod` and exits with a status code of 61. If the
`mongod` is the primary of a replica set, the
termination initiates a failover, allowing another member to
become primary.

Once a `mongod` has terminated, it may not be possible to cleanly
restart it on the *same* machine.

**Note:** Symlinks

If any of its monitored directories is a symlink to other volumes, the
Storage Node Watchdog does not monitor the symlink target.

For example, if the `mongod` uses
`storage.directoryPerDB: true` (or
`--directoryperdb`) and symlinks a
database directory to another volume, the Storage Node Watchdog does
not follow the symlink to monitor the target.

The maximum time the Storage Node Watchdog can
take to detect an unresponsive filesystem and terminate is nearly *twice* the
value of `watchdogPeriodSeconds`.
