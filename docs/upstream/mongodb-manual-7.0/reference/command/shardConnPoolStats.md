<!-- Converted from reference/command/shardConnPoolStats.txt (reStructuredText). Includes are inlined. -->

# shardConnPoolStats (database command)

## Definition

**`shardConnPoolStats`**

*Removed in MongoDB 5.0.* Use `connPoolStats` instead.

Returns information on the pooled and cached connections in the sharded
connection pool. The command also returns information on the per-thread
connection cache in the connection pool.

The `shardConnPoolStats` command uses the following syntax:

```javascript
{ shardConnPoolStats: 1 }
```

The sharded connection pool is specific to connections between members
in a sharded cluster. The `mongos` instances in a cluster use
the connection pool to execute client reads and writes. The
`mongod` instances in a cluster use the pool when issuing
`mapReduce` to query temporary collections on other shards.

When the cluster requires a connection, MongoDB pulls a connection from
the sharded connection pool into the per-thread connection cache.
MongoDB returns the connection to the connection pool after every
operation.

## Compatibility

This command is available in deployments hosted in the following environments: 

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas): The fully
  managed service for MongoDB deployments in the cloud

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Output

**`shardConnPoolStats.hosts`**

Displays connection status for each config server,
replica set, and standalone instance in
the cluster.

**`shardConnPoolStats.hosts.<host>.available`**

The number of connections available for this host to connect to the
`mongos`.

**`shardConnPoolStats.hosts.<host>.created`**

The number of connections the host has ever created to connect to
the `mongos`.

**`shardConnPoolStats.replicaSets`**

Displays information specific to replica sets.

**`shardConnPoolStats.replicaSets.<name>.host`**

Holds an array of documents that report on each replica set member.
These values derive from the replica set status values.

**`shardConnPoolStats.replicaSets.<name>.host[n].addr`**

The host address in the format `[hostname]:[port]`.

**`shardConnPoolStats.replicaSets.<name>.host[n].ok`**

This field is for internal use. Reports `false` when the
`mongos` either cannot connect to instance or received a
connection exception or error.

**`shardConnPoolStats.replicaSets.<name>.host[n].ismaster`**

The host is the replica set's primary if this is `true`.

**`shardConnPoolStats.replicaSets.<name>.host[n].hidden`**

The host is a hidden member of the replica set if this is
`true`.

**`shardConnPoolStats.replicaSets.<name>.host[n].secondary`**

The host is a hidden member of the replica set if this is
`true`.

The host is a secondary member of the replica set if this is
`true`.

**`shardConnPoolStats.replicaSets.<name>.host[n].pingTimeMillis`**

The latency, in milliseconds, from the `mongos` to this member.

**`shardConnPoolStats.replicaSets.<name>.host[n].tags`**

A `tags` document contains user-defined tag field and value pairs for
the replica set member.

```javascript
{ "<tag1>": "<string1>", "<tag2>": "<string2>",... }
```

- For read operations, you can specify a tag set in the read
  preference to direct the
  operations to replica set member(s) with the specified tag(s).

- For write operations, you can create a customize write concern using
  `settings.getLastErrorModes` and
  `settings.getLastErrorDefaults`.

For more information, see
replica-set-configuration-tag-sets.

**See also:**

`members[n].tags`

**`shardConnPoolStats.createdByType`**

The number connections in the cluster's connection pool.

**`shardConnPoolStats.createdByType.master`**

The number of connections to a shard.

**`shardConnPoolStats.createdByType.set`**

The number of connections to a replica set.

**`shardConnPoolStats.createdByType.sync`**

The number of connections to the config database.

**`shardConnPoolStats.totalAvailable`**

The number of connections available from the `mongos` to
the config servers, replica sets, and standalone `mongod`
instances in the cluster.

**`shardConnPoolStats.totalCreated`**

The number of connections the `mongos` has ever created to
other members of the cluster.

**`shardConnPoolStats.threads`**

Displays information on the per-thread connection cache.

**`shardConnPoolStats.threads.hosts`**

Displays each incoming client connection. For a `mongos`,
this array field displays one document per incoming client thread.
For a `mongod`, the array displays one entry per incoming
sharded `mapReduce` client thread.

**`shardConnPoolStats.threads.hosts.host`**

The host using the connection. The host can be a config
server, replica set, or standalone instance.

**`shardConnPoolStats.threads.hosts.created`**

The number of times the host pulled a connection from the pool.

**`shardConnPoolStats.threads.hosts.avail`**

The thread's availability.

**`shardConnPoolStats.threads.seenNS`**

The namespaces used on this connection thus far.
