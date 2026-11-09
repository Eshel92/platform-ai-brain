<!-- Converted from reference/method/sh.addShard.txt (reStructuredText). Includes are inlined. -->

# sh.addShard() (mongosh method)

## Definition

**`sh.addShard(<url>)`**

Adds a shard replica set to a sharded cluster. This method
must be run on a `mongos` instance.

**Important:** `mongosh` Method

This page documents a `mongosh` method. This is *not*
the documentation for database commands or language-specific drivers,
such as Node.js. 

For the database command, see the `addShard` command.

For MongoDB API drivers, refer to the language-specific
`MongoDB driver documentation`.

The `sh.addShard()` method has the following parameter:

* - Parameter

  - Type

  - Description

* - `host`

  - string

  - The replica set name, hostname, and port of at least one member of
    the shard's replica set. Any additional replica set member hostnames
    must be comma separated. For example:

    ```bash
    <replica_set>/<hostname><:port>,<hostname><:port>, ...
    ```

The `sh.addShard()` method has the following prototype form:

```javascript
sh.addShard("<replica_set>/<hostname><:port>")
```

**Warning:**

Do not use `localhost` for the hostname unless your
config server
is also running on `localhost`.

`mongos` installed from official Debian and Red Hat or CentOS packages have the `bind_ip`
configuration set to `127.0.0.1` by default.

`mongos`  uses
`"majority"`  for the 
`addShard` command and its helper
`sh.addShard()`.

## Compatibility

This method is available in deployments hosted in the following environments: 

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas): The fully
  managed service for MongoDB deployments in the cloud

**Important:**

This command is not supported in M0 and Flex clusters.
For more information, see Unsupported Commands.

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Considerations

### Balancing

When you add a shard to a sharded cluster, you affect the balance of
chunks among the shards of a cluster for all existing sharded
collections. The balancer will begin migrating chunks so that the
cluster will achieve balance. See sharding-internals-balancing for
more information.

### Hidden Members

**Important:** You cannot include a hidden member in the seed list provided to
`sh.addShard()`.

## Example

To add a shard, specify the name of the replica set and
the hostname of at least one member of the replica set, as a seed. If
you specify additional hostnames, all must be members of the same
replica set.

The following example adds a replica set named `repl0` and specifies
one member of the replica set:

```javascript
sh.addShard("repl0/mongodb3.example.net:27327")
```
