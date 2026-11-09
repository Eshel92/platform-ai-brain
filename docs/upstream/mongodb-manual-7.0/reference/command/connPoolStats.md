<!-- Converted from reference/command/connPoolStats.txt (reStructuredText). Includes are inlined. -->

# connPoolStats (database command)

## Definition

**`connPoolStats`**

The command `connPoolStats` returns information
regarding the open outgoing connections from the current database
instance to other members of the sharded cluster or 
replica set.

To run `connPoolStats`, use the `db.runCommand( { <command> } )` method.

**Note:**

`connPoolStats` only returns meaningful results for
`mongos` instances and for `mongod` instances
in sharded clusters.

## Compatibility

This command is available in deployments hosted in the following environments: 

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas): The fully
  managed service for MongoDB deployments in the cloud

**Note:**

This command is supported in all MongoDB Atlas clusters.
For information on Atlas support for all commands, see 
Unsupported Commands.

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Syntax

The command has the following syntax:

```javascript
db.runCommand( 
   {
     connPoolStats: 1
   }  
)
```

The value of the argument (i.e. `1` ) does not affect the
output of the command.
   

## Behavior

`connPoolStats` includes aggregated statistics in its
output:

- The `hosts` field displays the information
  aggregated by host.

- The `pools` field displays the information
  aggregated by pool.

**Note:**

To avoid interference with any running operations,
`connPoolStats` does not take any locks. As such, the
counts may change slightly as `connPoolStats` gathers
information, resulting in slight differences between the
`hosts` and `pools`
connection counts.

## Example

The following operation uses the `db.runCommand()` method to
run the `connPoolStats` command on a `mongos` of a
sharded cluster. The sharded cluster has 2 shards, each a single-member
replica set, and a config server replica set. The `mongos`
runs on a 4-core machine.

```javascript
db.runCommand( { "connPoolStats" : 1 } )
```

The command returns the output of the following form:

**Note:**

The `connPoolStats` output varies depending on the
deployment and the member against which you run
`connPoolStats` among other factors.

```javascript
{
   "numClientConnections" : <num>,
   "numAScopedConnections" : <num>,
   "totalInUse" : <num>,
   "totalAvailable" : <num>,
   "totalLeased" : <num>,
   "totalCreated" : <num>,
   "totalRefreshing" : <num>,
   "replicaSetMatchingStrategy" : <string>,
   "acquisitionWaitTimes" : {  // Added in MongoDB 6.3
      "(-inf, 0ms)" : { "count" : <num> },
      "[0ms, 50ms)" : { "count" : <num> },
      "[50ms, 100ms)" : { "count" : <num> },
      "[100ms, 150ms)" : { "count" : <num> },
      "[150ms, 200ms)" : { "count" : <num> },
      "[200ms, 250ms)" : { "count" : <num> },
      "[250ms, 300ms)" : { "count" : <num> },
      "[300ms, 350ms)" : { "count" : <num> },
      "[350ms, 400ms)" : { "count" : <num> },
      "[400ms, 450ms)" : { "count" : <num> },
      "[450ms, 500ms)" : { "count" : <num> },
      "[500ms, 550ms)" : { "count" : <num> },
      "[550ms, 600ms)" : { "count" : <num> },
      "[600ms, 650ms)" : { "count" : <num> },
      "[650ms, 700ms)" : { "count" : <num> },
      "[700ms, 750ms)" : { "count" : <num> },
      "[750ms, 800ms)" : { "count" : <num> },
      "[800ms, 850ms)" : { "count" : <num> },
      "[850ms, 900ms)" : { "count" : <num> },
      "[900ms, 950ms)" : { "count" : <num> },
      "[950ms, 1000ms)" : { "count" : <num> },
      "[1000ms, inf)" : { "count" : <num> },
      "totalCount" : <num>
   },
   "pools" : {
      "NetworkInterfaceTL-TaskExecutorPool-0" : {
         "poolInUse" : <num>,
         "poolAvailable" : <num>,
         "poolLeased" : <num>,
         "poolCreated" : <num>,
         "poolRefreshing" : <num>, 
         "acquisitionWaitTimes" : <document>,  // Added in MongoDB 6.3
         "cfg1.example.net:27019" : {
            "inUse" : <num>,
            "available" : <num>,
            "leased" : <num>,
            "created" : <num>,
            "refreshing" : <num>,
            "acquisitionWaitTimes" : <document>  // Added in MongoDB 6.3
         },
      },
      "NetworkInterfaceTL-TaskExecutorPool-1" : {
         "poolInUse" : <num>,
         "poolAvailable" : <num>,
         "poolLeased" : <num>,
         "poolCreated" : <num>,
         "poolRefreshing" : <num>,
         "acquisitionWaitTimes" : <document>,  // Added in MongoDB 6.3
         "cfg1.example.net:27019" : {
            "inUse" : <num>,
            "available" : <num>,
            "leased" : <num>,
            "created" : <num>,
            "refreshing" : <num>,
            "acquisitionWaitTimes" : <document>  // Added in MongoDB 6.3
         }
      },
      "NetworkInterfaceTL-TaskExecutorPool-2" : {
         "poolInUse" : <num>,
         "poolAvailable" : <num>,
         "poolLeased" : <num>,
         "poolCreated" : <num>,
         "poolRefreshing" : <num>, 
         "acquisitionWaitTimes" : <document>,  // Added in MongoDB 6.3
         "cfg1.example.net:27019" : {
            "inUse" : <num>,
            "available" : <num>,
            "leased" : <num>,
            "created" : <num>,
            "refreshing" : <num>,
            "acquisitionWaitTimes" : <document>  // Added in MongoDB 6.3
         }
      },
      "NetworkInterfaceTL-TaskExecutorPool-3" : {
         "poolInUse" : <num>,
         "poolAvailable" : <num>,
         "poolLeased" : <num>,
         "poolCreated" : <num>,
         "poolRefreshing" : <num>, 
         "acquisitionWaitTimes" : <document>,  // Added in MongoDB 6.3
         "cfg1.example.net:27019" : {
            "inUse" : <num>,
            "available" : <num>,
            "leased" : <num>,
            "created" : <num>,
            "refreshing" : <num>,
            "acquisitionWaitTimes" : <document>  // Added in MongoDB 6.3
         }
      },
      "NetworkInterfaceTL-ShardRegistry" : {
         "poolInUse" : <num>,
         "poolAvailable" : <num>,
         "poolLeased" : <num>,
         "poolCreated" : <num>,
         "poolRefreshing" : <num>, 
         "acquisitionWaitTimes" : <document>,  // Added in MongoDB 6.3
         "cfg1.example.net:27019" : {
            "inUse" : <num>,
            "available" : <num>,
            "leased" : <num>,
            "created" : <num>,
            "refreshing" : <num>,
            "acquisitionWaitTimes" : <document>  // Added in MongoDB 6.3
         },
         "cfg2.example.net:27019" : {
            "inUse" : <num>,
            "available" : <num>,
            "leased" : <num>,
            "created" : <num>,
            "refreshing" : <num>,
            "acquisitionWaitTimes" : <document>  // Added in MongoDB 6.3
         },
         "cfg3.example.net:27019" : {
            "inUse" : <num>,
            "available" : <num>,
            "leased" : <num>,
            "created" : <num>,
            "refreshing" : <num>,
            "acquisitionWaitTimes" : <document>  // Added in MongoDB 6.3
         },
         "shard1.example.net:27018" : {
            "inUse" : <num>,
            "available" : <num>,
            "leased" : <num>,
            "created" : <num>,
            "refreshing" : <num>,
            "acquisitionWaitTimes" : <document>  // Added in MongoDB 6.3
         },
         "shard2.example.net:27018" : {
            "inUse" : <num>,
            "available" : <num>,
            "leased" : <num>,
            "created" : <num>,
            "refreshing" : <num>,
            "acquisitionWaitTimes" : <document>  // Added in MongoDB 6.3
         }
      },
      "global" : {
         "poolInUse" : <num>,
         "poolAvailable" : <num>,
         "poolLeased" : <num>,
         "poolCreated" : <num>,
         "poolRefreshing" : <num>, 
         "acquisitionWaitTimes" : <document>,  // Added in MongoDB 6.3
         "cfg3.example.net:27019" : {
            "inUse" : <num>,
            "available" : <num>,
            "leased" : <num>,
            "created" : <num>,
            "refreshing" : <num>,
            "acquisitionWaitTimes" : <document>  // Added in MongoDB 6.3
         },
         "cfg1.example.net:27019" : {
            "inUse" : <num>,
            "available" : <num>,
            "leased" : <num>,
            "created" : <num>,
            "refreshing" : <num>,
            "acquisitionWaitTimes" : <document>  // Added in MongoDB 6.3
         },
         "cfg2.example.net:27019" : {
            "inUse" : <num>,
            "available" : <num>,
            "leased" : <num>,
            "created" : <num>,
            "refreshing" : <num>,
            "acquisitionWaitTimes" : <document>  // Added in MongoDB 6.3
         },
         "shard2.example.net:27018" : {
            "inUse" : <num>,
            "available" : <num>,
            "leased" : <num>,
            "created" : <num>,
            "refreshing" : <num>,
            "acquisitionWaitTimes" : <document>  // Added in MongoDB 6.3
         },
         "shard1.example.net:27018" : {
            "inUse" : <num>,
            "available" : <num>,
            "leased" : <num>,
            "created" : <num>,
            "refreshing" : <num>,
            "acquisitionWaitTimes" : <document>  // Added in MongoDB 6.3
         }
      }
   },
   "hosts" : {
      "cfg3.example.net:27019" : {
         "inUse" : <num>,
         "available" : <num>,
         "leased" : <num>,
         "created" : <num>,
         "refreshing" : <num>,
         "acquisitionWaitTimes" : <document>  // Added in MongoDB 6.3
      },
      "cfg1.example.net:27019" : {
         "inUse" : <num>,
         "available" : <num>,
         "leased" : <num>,
         "created" : <num>,
         "refreshing" : <num>,
         "acquisitionWaitTimes" : <document>  // Added in MongoDB 6.3
      },
      "cfg2.example.net:27019" : {
         "inUse" : <num>,
         "available" : <num>,
         "leased" : <num>,
         "created" : <num>,
         "refreshing" : <num>,
         "acquisitionWaitTimes" : <document>  // Added in MongoDB 6.3
      },
      "shard2.example.net:27018" : {
         "inUse" : <num>,
         "available" : <num>,
         "leased" : <num>,
         "created" : <num>,
         "refreshing" : <num>,
         "acquisitionWaitTimes" : <document>  // Added in MongoDB 6.3
      },
      "shard1.example.net:27018" : {
         "inUse" : <num>,
         "available" : <num>,
         "leased" : <num>,
         "created" : <num>,
         "refreshing" : <num>,
         "acquisitionWaitTimes" : <document>  // Added in MongoDB 6.3
      }
   },
   "replicaSets" : {
      "csRS" : {
         "hosts" : [
            {
               "addr" : "cfg1.example.net:27019",
               "ok" : <bool>,
               "ismaster" : <bool>,
               "hidden" : <bool>,
               "secondary" : <bool>,
               "pingTimeMillis" : <num>
            },
            {
               "addr" : "cfg2.example.net:27019",
               "ok" : <bool>,
               "ismaster" : <bool>,
               "hidden" : <bool>,
               "secondary" : <bool>,
               "pingTimeMillis" : <num>
            },
            {
               "addr" : "cfg3.example.net:27019",
               "ok" : <bool>,
               "ismaster" : <bool>,
               "hidden" : <bool>,
               "secondary" : <bool>,
               "pingTimeMillis" : <num>
            }
         ]
      },
      "shardB" : {
         "hosts" : [
            {
               "addr" : "shard2.example.net:27018",
               "ok" : <bool>,
               "ismaster" : <bool>,
               "hidden" : <bool>,
               "secondary" : <bool>,
               "pingTimeMillis" : <num>
            }
         ]
      },
      "shardA" : {
         "hosts" : [
            {
               "addr" : "shard1.example.net:27018",
               "ok" : <bool>,
               "ismaster" : <bool>,
               "hidden" : <bool>,
               "secondary" : <bool>,
               "pingTimeMillis" : <num>
            }
         ]
      }
   },
   "ok" : 1,
   "$clusterTime" : {
      "clusterTime" : <timestamp>,
      "signature" : <document>
   },
   "operationTime" : <timestamp>
}
```

## Output

**`connPoolStats.totalAvailable`**

Reports the total number of available outgoing connections from the 
current `mongod` / `mongos` instance to other members
of the sharded cluster or replica set.

**`connPoolStats.totalLeased`**

Reports the total number of connections borrowed from a pool and 
expected to return. These connections might not remain active 
through the duration of a lease, and are excluded from the related 
metrics. These connections are unavailble through the 
duration of the lease.

**`connPoolStats.totalCreated`**

Reports the total number of outgoing connections ever created by the
current `mongod` / `mongos` instance to other members
of the sharded cluster or replica set.

**`connPoolStats.totalInUse`**

Reports the total number of outgoing connections from the current
`mongod` / `mongos` instance to other members of the
sharded cluster or replica set that are currently in use.

**`connPoolStats.totalRefreshing`**

Reports the total number of outgoing connections from the
current `mongod` / `mongos` instance to other
members of the sharded cluster or replica set that
are currently being refreshed.

**`connPoolStats.totalWasNeverUsed`**

Reports the total number of outgoing connections from the
current `mongod` / `mongos` instance to other
members of the sharded cluster or replica set that
were closed having never been used.

**`connPoolStats.replicaSetMatchingStrategy`**

**New in version:** 5.0

On a `mongos` instance, this value reports the policy
used by the instance to determine the minimum size limit of its
connection pools to nodes within replica sets.

On a `mongod` instance, this value reports the policy
used by the instance to determine the minimum size limit of its
connection pools to nodes within *other* replica sets.

The policy for `mongos` and `mongod` can be
set with the `ShardingTaskExecutorPoolReplicaSetMatching`
parameter.

**Note:**

If the `ShardingTaskExecutorPoolReplicaSetMatching` is
set to `"automatic"`, the
`replicaSetMatchingStrategy` still describes
the actual policy being used, not `"automatic"`. To find the
value of the
`ShardingTaskExecutorPoolReplicaSetMatching`, use
`getParameter` which returns the value of the server
parameter:

```javascript
db.adminCommand( { getParameter : 1, "ShardingTaskExecutorPoolReplicaSetMatching" : 1 } )
```

**`connPoolStats.acquisitionWaitTimes`**

**New in version:** 6.3

Document reports a histogram with the wait times for requests to
acquire a connection from `mongos` to
`mongod`:

- The document contains time ranges in milliseconds and the number of
  connection requests in each range.

- `-inf` is negative infinity and connection requests in the
  range `(-inf, 0ms)` did not wait.

- `inf` is positive infinity and connection requests in the
  range `[1000ms, inf)` waited a time greater than or equal to
  1,000 milliseconds.

- `totalCount` is the total number of connection requests for all
  time ranges.

```javascript
"acquisitionWaitTimes" : {
   "(-inf, 0ms)" : { "count" : <num> },
   "[0ms, 50ms)" : { "count" : <num> },
   "[50ms, 100ms)" : { "count" : <num> },
   "[100ms, 150ms)" : { "count" : <num> },
   "[150ms, 200ms)" : { "count" : <num> },
   "[200ms, 250ms)" : { "count" : <num> },
   "[250ms, 300ms)" : { "count" : <num> },
   "[300ms, 350ms)" : { "count" : <num> },
   "[350ms, 400ms)" : { "count" : <num> },
   "[400ms, 450ms)" : { "count" : <num> },
   "[450ms, 500ms)" : { "count" : <num> },
   "[500ms, 550ms)" : { "count" : <num> },
   "[550ms, 600ms)" : { "count" : <num> },
   "[600ms, 650ms)" : { "count" : <num> },
   "[650ms, 700ms)" : { "count" : <num> },
   "[700ms, 750ms)" : { "count" : <num> },
   "[750ms, 800ms)" : { "count" : <num> },
   "[800ms, 850ms)" : { "count" : <num> },
   "[850ms, 900ms)" : { "count" : <num> },
   "[900ms, 950ms)" : { "count" : <num> },
   "[950ms, 1000ms)" : { "count" : <num> },
   "[1000ms, inf)" : { "count" : <num> },
   "totalCount" : <num>
}
```

**`connPoolStats.numClientConnection`**

Reports the number of active and stored outgoing **synchronous**
connections from the current `mongod` / `mongos` instance
to other members of the sharded cluster or replica set.

These connections are a part of a pool that is a subset of the data 
reported by `totalAvailable`, 
`totalCreated`, and `totalInUse`.

**`connPoolStats.numAScopedConnection`**

Reports the number of active and stored outgoing **scoped
synchronous** connections from the current
`mongod` / `mongos` instance to other members of the
sharded cluster or replica set.

These connections are a part of a pool that is a subset of the data 
reported by `totalAvailable`, 
`totalCreated`, and `totalInUse`.

**`connPoolStats.pools`**

Reports on connection statistics (in
use/available/created/refreshing) grouped by the connection pools. A
`mongod` or `mongos` has two distinct families of
outgoing connection pools:

- DBClient-based pools (the "write path") and

- NetworkInterfaceTL-based pools (the "read path").

For each pool, the command returns a document that resembles the
following:

```none
{
  "poolInUse" : <num>,
  "poolAvailable" : <num>,
  "poolLeased" : <num>,
  "poolCreated" : <num>,
  "poolRefreshing" : <num>,
  "acquisitionWaitTimes" : <document>,  // Added in MongoDB 6.3
  "[host1]" : {
     "inUse" : <num>, "available" : <num>, "leased" : <num>, "created" : <num>, "refreshing" : <num>,
     "acquisitionWaitTimes" : <document>  // Added in MongoDB 6.3
  },
  "[host2]" : {
     "inUse" : <num>, "available" : <num>, "leased" : <num>, "created" : <num>, "refreshing" : <num>,
     "acquisitionWaitTimes" : <document>  // Added in MongoDB 6.3
  },
  ...
}
```

**Note:**

If there are no connections (in use/available/created/refreshing)
for a particular pool, the `connPoolStats` does not
return statistics for that pool.

**`connPoolStats.pools.NetworkInterfaceTL-TaskExecutorPool-[n]`**

Displays connection statics related to TaskExecutor pools.
Typically, there will be one TaskExecutorPool per core, e.g.
`pools.NetworkInterfaceTL-TaskExecutorPool-0` ...
`pools.NetworkInterfaceTL-TaskExecutorPool-7` 
for an 8-core processor.

**See also:**

`taskExecutorPoolSize`

**`connPoolStats.pools.NetworkInterfaceTL-ShardRegistry`**

*Available if the command is run on a member of a sharded cluster.*

Displays the pool statistics for the connections between the
current `mongod` / `mongos` instance and other
members of the sharded cluster.

**`connPoolStats.pools.NetworkInterfaceTL-Replication`**

*Available if the command is run on a member of a replica set.*

Displays the pool statistics for the connections between the
current `mongod` instance and the other members of the
replica set.

**`connPoolStats.pools.global`**

Displays the DBClient-based pool statistics.

**`connPoolStats.pools.[pool].poolWasNeverUsed`**

Displays the number of connections in this connection pool
that were closed having never been used.

**`connPoolStats.pools.[pool].acquisitionWaitTimes`**

**New in version:** 6.3

Reports the wait times for requests to acquire a connection from
`mongos` to `mongod`. For details, see
`connPoolStats.acquisitionWaitTimes`.

**`connPoolStats.hosts`**

Reports on connection statistics (in
use/available/created/refreshing) grouped by the hosts.

Contains documents that represent a report of connections
between the current `mongod` / `mongos` instance and
each member of the sharded cluster or replica set.

**`connPoolStats.hosts.[host].available`**

Reports the total number of connections available for connecting 
to the `[host]`.

**`connPoolStats.hosts.[host].leased`**

Reports the total number of connections to the host borrowed from 
a pool and expected to return. These connections might not remain 
active through the duration of a lease, and are excluded from the 
related metrics. These connections are unavailble through the 
duration of the lease.

**`connPoolStats.hosts.[host].created`**

Reports the number of connections to the `[host]`  ever created.

**`connPoolStats.hosts.[host].inUse`**

Reports the number of connections to the `[host]`
that are currently in use.

**`connPoolStats.hosts.[host].wasNeverUsed`**

Reports the total number of outgoing connections from `host` to 
other members of the sharded cluster or 
replica set that were closed having never been used.

**`connPoolStats.hosts.[host].acquisitionWaitTimes`**

**New in version:** 6.3

Reports the wait times for requests to acquire a connection from
`mongos` to `mongod`. For details, see
`connPoolStats.acquisitionWaitTimes`.

**`connPoolStats.replicaSets`**

Contains documents that represent a report of 
information related to each replica set connected to the current
`mongod` / `mongos`.

**`connPoolStats.replicaSets.replicaSet`**

Reports on each replica set connected to the 
current `mongod` / `mongos`.

**`connPoolStats.replicaSets.[replicaSets].hosts`**

Holds an array of documents that reports on each 
member in the replica set.

These values derive from the replica set status values.

**`connPoolStats.replicaSets.[replicaSet].hosts[n].addr`**

Reports the address for the member in the replica set 
in `[hostname]:[port]` format.

**`connPoolStats.replicaSets.[replicaSet].hosts[n].ok`**

Reports `false` when:

- the current `mongos` or `mongod` cannot connect
  to instance.

- the current `mongos` or `mongod` received a
  connection exception or error.

This field is for internal use.

**`connPoolStats.replicaSets.[replicaSet].hosts[n].ismaster`**

Reports `true` if this 
`host` is the
primary member of the replica set.

**`connPoolStats.replicaSets.[replicaSet].hosts[n].hidden`**

Reports `true` if this 
`host` is a 
hidden member of the replica set.

**`connPoolStats.replicaSets.[replicaSet].hosts[n].secondary`**

Reports `true` if this 
`host` is a
secondary member of the replica set.

**`connPoolStats.replicaSets.[replicaSet].hosts[n].pingTimeMillis`**

Reports the ping time in milliseconds from the `mongos` or
`mongod` to this 
`host`.

**`connPoolStats.replicaSets.[replicaSet].hosts[n].tags`**

Reports the `members[n].tags`, if this member of the set has
tags configured.

See also command-response for details on the `ok` status
field, the `operationTime` field and the `$clusterTime` field.

`host`
