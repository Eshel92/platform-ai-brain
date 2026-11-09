<!-- Converted from tutorial/troubleshoot-replica-sets.txt (reStructuredText). Includes are inlined. -->

# Troubleshoot Replica Sets

This section describes common strategies for troubleshooting
replica set deployments.

## Check Replica Set Status

To display the current state of the replica set and current state of
each member, run the `rs.status()` method in a
`mongosh` session that is connected to the replica set's
primary. For descriptions of the information displayed by
`rs.status()`, see /reference/command/replSetGetStatus.

**Note:**

The `rs.status()` method is a wrapper that runs the
`replSetGetStatus` database command.

## Check the Replication Lag

Replication lag is a delay between an operation on the primary
and the application of that operation from the oplog to the
secondary. Replication lag can be a significant issue and can
seriously affect MongoDB replica set deployments. Excessive
replication lag makes "lagged" members ineligible to quickly become
primary and increases the possibility that distributed read operations
will be inconsistent.

To check the current length of replication lag:

- In a `mongosh` session that is connected to the primary,
  call the `rs.printSecondaryReplicationInfo()` method.

  Returns the `syncedTo` value for each member,
  which shows the time when the last oplog entry was written to the
  secondary, as shown in the following example:

  ```none
  source: m1.example.net:27017
      syncedTo: Thu Apr 10 2014 10:27:47 GMT-0400 (EDT)
      0 secs (0 hrs) behind the primary 
  source: m2.example.net:27017
      syncedTo: Thu Apr 10 2014 10:27:47 GMT-0400 (EDT)
      0 secs (0 hrs) behind the primary 
  ```

  A delayed member may show as `0`
  seconds behind the primary when the inactivity period on the primary is
  greater than the `members[n].secondaryDelaySecs`
  value.

  **Note:**

  The `rs.status()` method is a wrapper around the
  `replSetGetStatus` database command.

  The `totalOplogSlotDurationMicros` in the slow query log message shows the 
  time between a write operation getting a commit timestamp to commit the 
  storage engine writes and actually committing. `mongod` supports 
  parallel writes. However, it commits write operations with commit 
  timestamps in any order. 

  **Example:**

  For example, consider the following writes with commit timestamps:

  - writeA with Timestamp1
  - writeB with Timestamp2
  - writeC with Timestamp3

  Suppose writeB commits first at Timestamp2. Replication is paused
  until writeA commits because writeA's oplog entry with Timestamp1 is
  required for replication to copy the oplog to secondary replica set
  members. 

- Monitor the rate of replication by checking for non-zero or increasing
  oplog time values in the Replication Lag graph available in 
  [Cloud Manager](https://docs.cloudmanager.mongodb.com/reference/alerts/replication-lag/) 
  and in [Ops Manager](https://docs.opsmanager.mongodb.com/current/reference/alerts/replication-lag/).

### Replication Lag Causes

Possible causes of replication lag include:

- **Network Latency**

  Check the network routes between the members of your set to ensure
  that there is no packet loss or network routing issue.

  Use tools including `ping` to test latency between set
  members and `traceroute` to expose the routing of packets
  network endpoints.

- **Disk Throughput**

  If the file system and disk device on the secondary is
  unable to flush data to disk as quickly as the primary, then
  the secondary will have difficulty keeping state. Disk-related
  issues are incredibly prevalent on multi-tenant systems, including
  virtualized instances, and can be transient if the system accesses
  disk devices over an IP network (as is the case with Amazon's
  EBS system.)

  Use system-level tools to assess disk status, including
  `iostat` or `vmstat`.

- **Concurrency**

  In some cases, long-running operations on the primary can block
  replication on secondaries. For best results, configure write
  concern to require confirmation of replication to
  secondaries. This prevents write operations from
  returning if replication cannot keep up with the write load.

  You can also use the database profiler to see if there are slow queries or
  long-running operations that correspond to the incidences of lag.

- **Appropriate Write Concern**

  If you are performing a large data ingestion or bulk load operation
  that requires a large number of writes to the primary, particularly
  with `unacknowledged write concern
  <`, the secondaries will not be able to
  read the oplog fast enough to keep up with changes.

  To prevent this, request write acknowledgment
  write concern after every 100,
  1,000, or another interval to provide an opportunity for
  secondaries to catch up with the primary.

  For more information see:

  - Write Concern
  - Replica Set Write Concern
  - replica-set-oplog-sizing

### Flow Control

Starting in MongoDB 4.2, administrators can limit the rate at which
the primary applies its writes with the goal of keeping the `majority
committed` lag under
a configurable maximum value `flowControlTargetLagSeconds`.

By default, flow control is `enabled`.

With flow control enabled, as the lag grows close to the
`flowControlTargetLagSeconds`, writes on the primary must obtain
tickets before taking locks to apply writes. By limiting the number of
tickets issued per second, the flow control mechanism attempts to keep 
the lag under the target.

Replication lag can occur without the replica set receiving sufficient load
to engage flow control, such as in the case of an unresponsive 
secondary.

To view the status of flow control, run the following commands on the 
primary:

#. Run the `rs.printSecondaryReplicationInfo` method to determine if
   any nodes are lagging:

   ```javascript
   rs.printSecondaryReplicationInfo()    
   ```

   Example output:

   ```javascript
   source: 192.0.2.2:27017
   {
     syncedTo: 'Mon Jan 31 2022 18:58:50 GMT+0000 (Coordinated Universal Time)',
     replLag: '0 secs (0 hrs) behind the primary '
   }
   ---
   source: 192.0.2.3:27017
   {
     syncedTo: 'Mon Jan 31 2022 18:58:05 GMT+0000 (Coordinated Universal Time)',
     replLag: '45 secs (0 hrs) behind the primary '
   }
   ```

#. Run the `serverStatus` command and use the 
   `flowControl.isLagged` value to determine whether the
   replica set has engaged flow control:

   ```javascript
   db.runCommand( { serverStatus: 1 } ).flowControl.isLagged     
   ```

   Example output:

   ```javascript
   false
   ```

   
   If flow control has not engaged, investigate the secondary
   to determine the cause of the replication lag, such as limitations in 
   the hardware, network, or application.

For information on flow control statistics, see:

- `flowControl`

- `$currentOp.waitingForFlowControl` and `$currentOp.flowControlStats`

- `currentOp.waitingForFlowControl` and `currentOp.flowControlStats`

## Slow Application of Oplog Entries

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

## Test Connections Between all Members

All members of a replica set must be able to connect to every
other member of the set to support replication. Always verify
connections in both "directions."  Networking topologies and firewall
configurations can prevent normal and required connectivity, which can
block replication.

**Warning:**

Before you bind your instance to a publicly-accessible IP address,
you must secure your cluster from unauthorized access. For a complete
list of security recommendations, see
security-checklist. At minimum, consider
enabling authentication and hardening
network infrastructure.

MongoDB binaries, `mongod` and `mongos`, bind
to localhost by default. If the `net.ipv6` configuration file
setting or the `--ipv6` command line option is set for the binary,
the binary additionally binds to the localhost IPv6 address.

By default `mongod` and `mongos` that are
bound to localhost only accept connections from clients that are
running on the same computer. This binding behavior includes
`mongosh` and other members of your replica set or sharded
cluster. Remote clients cannot connect to binaries that are bound only
to localhost.

To override the default binding and bind to other IP addresses, use the
`net.bindIp` configuration file setting or the `--bind_ip`
command-line option to specify a list of hostnames or IP addresses.

**Warning:**

Starting in MongDB 5.0, [split horizon DNS](https://en.wikipedia.org/wiki/Split-horizon_DNS) nodes that are
only configured with an IP address fail startup validation and
report an error. See `disableSplitHorizonIPCheck`.

For example, the following `mongod` instance binds to both
the localhost and the hostname `My-Example-Associated-Hostname`, which is
associated with the IP address `198.51.100.1`:

```none
mongod --bind_ip localhost,My-Example-Associated-Hostname
```

In order to connect to this instance, remote clients must specify
the hostname  or its associated IP address `198.51.100.1`:

```none
mongosh --host My-Example-Associated-Hostname

mongosh --host 198.51.100.1
```

Consider the following example of a bidirectional test of networking:

**Example:** Given a replica set with three members running on three separate

hosts:

- `m1.example.net`
- `m2.example.net`
- `m3.example.net`

All three use the default port `27017`.

1. Test the connection from `m1.example.net` to the other hosts
   with the following operation set `m1.example.net`:

   ```bash
   mongosh --host m2.example.net --port 27017

   mongosh --host m3.example.net --port 27017
   ```

#. Test the connection from `m2.example.net` to the other two
   hosts with the following operation set from `m2.example.net`,
   as in:

   ```bash
   mongosh --host m1.example.net --port 27017

   mongosh --host m3.example.net --port 27017
   ```

   You have now tested the connection between
   `m2.example.net` and `m1.example.net` in both directions.

#. Test the connection from `m3.example.net` to the other two
   hosts with the following operation set from the
   `m3.example.net` host, as in:

   ```bash
   mongosh --host m1.example.net --port 27017

   mongosh --host m2.example.net --port 27017
   ```

If any connection, in any direction fails, check your networking
and firewall configuration and reconfigure your environment to
allow these connections.

## Socket Exceptions when Rebooting More than One Secondary

When you reboot members of a replica set, ensure that the set is able
to elect a primary during the maintenance. This means ensuring that a majority of
the set's `members[n].votes` are
available.

When a set's active members can no longer form a majority, the set's
primary steps down and becomes a secondary.  The primary
does not close client connections when it steps down.

Clients cannot write to the replica set until the members elect a new
primary.

**Example:** Given a three-member replica set where every member has

one vote, the set can elect a primary if at least two members
can connect to each other. If you reboot the two secondaries at
once, the primary steps down and becomes a secondary. Until at least
another secondary becomes available, i.e. at least one of the rebooted
secondaries also becomes available, the set has no primary and cannot
elect a new primary.

For more information on votes, see /core/replica-set-elections. For
related information on connection errors, see faq-keepalive.

## Check the Size of the Oplog

A larger oplog can give a replica set a greater tolerance for
lag, and make the set more resilient.

To check the size of the oplog for a given replica set member,
connect to the member in `mongosh` and run the
`rs.printReplicationInfo()` method.

The output displays the size of the oplog and the date ranges of the
operations contained in the oplog. In the following example, the oplog
is about 10 MB and is able to fit about 26 hours (94400 seconds) of
operations:

```javascript
configured oplog size:   10.10546875MB
log length start to end: 94400 (26.22hrs)
oplog first event time:  Mon Mar 19 2012 13:50:38 GMT-0400 (EDT)
oplog last event time:   Wed Oct 03 2012 14:59:10 GMT-0400 (EDT)
now:                     Wed Oct 03 2012 15:00:21 GMT-0400 (EDT)
```

The oplog should be long enough to hold all transactions for the
longest downtime you expect on a secondary. [#oplog]_ At a minimum, an oplog
should be able to hold minimum 24 hours of operations; however, many
users prefer to have 72 hours or even a week's work of operations.

For more information on how oplog size affects operations, see:

- replica-set-oplog-sizing,
- replica-set-delayed-members, and
- replica-set-replication-lag.

**Note:** You normally want the oplog to be the same size on all

members. If you resize the oplog, resize it on all members.

To change oplog size, see the /tutorial/change-oplog-size
tutorial.
