<!-- Converted from reference/command/addShard.txt (reStructuredText). Includes are inlined. -->

# addShard (database command)

## Definition

**`addShard`**

Adds a shard replica set to a sharded cluster.

**Tip:**

In `mongosh`, this command can also be run through the `sh.addShard` helper method.

Helper methods are convenient for `mongosh` users, but they may not
return the same level of information as database commands.  In cases where
the convenience is not needed or the additional return fields are required,
use the database command.

## Compatibility

This command is available in deployments hosted in the following environments: 

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

**Note:**

This command is not supported in [MongoDB Atlas](https://www.mongodb.com/docs/atlas). See [Modify your Atlas Sharded Cluster](https://www.mongodb.com/docs/atlas/scale-cluster/#modify-the-number-of-shards)
to add or remove shards from your Atlas cluster.

## Syntax

The command has the following syntax:

```javascript
db.adminCommand(
   { 
     addShard: "<replica_set>/<hostname><:port>", 
     name: "<shard_name>" 
   } 
)
```

### Command Fields

**Note:**

Starting in version 6.2, MongoDB removes the `maxSize` field 
from the `addShard` command. As a result:

- Running `addShard` with the `maxSize` field returns 
  an `InvalidOptions` error.

- New documents in the `shards` collection no longer 
  include the `maxSize` field.

- Any pre-existing `maxSize` field entries are ignored.

The command contains the following fields:

* - Field

  - Type

  - Description

* - `addShard`

  - string

  - The replica set name, hostname, and port of at least one member of
    the shard's replica set. Any additional replica set member hostnames
    must be comma separated. For example:

    ```bash
    <replica_set>/<hostname><:port>,<hostname><:port>, ...
    ```

* - `name`

  - string

  - Optional. A name for the shard. If this is not specified, MongoDB
    automatically provides a unique name.
           
The `addShard` command stores shard configuration
information in the config database. Always run
`addShard` when using the `admin` database.

## Considerations

### Storage

The shard that you add to your sharded cluster must be empty. 

### Balancing

When you add a shard to a sharded cluster, you affect the balance of
chunks among the shards of a cluster for all existing sharded
collections. The balancer will begin migrating chunks so that the
cluster will achieve balance. See sharding-internals-balancing for
more information.

### Hidden Members

**Important:** You cannot include a hidden member in the seed list provided to
`addShard`.

## Required Access

You must have the `addShard` action on a
cluster resource to run the `addShard` command. The `clusterAdmin` or
`clusterManager` built-in roles contain the
`addShard` action and grant privileges to run the `addShard` command.

## Examples

The following command adds a replica set as a shard:

```javascript
use admin
db.runCommand( { addShard: "repl0/mongodb3.example.net:27327"} )
```

**Warning:**

Do not use `localhost` for the hostname unless your
config server is also running on
`localhost`.
