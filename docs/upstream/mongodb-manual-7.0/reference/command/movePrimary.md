<!-- Converted from reference/command/movePrimary.txt (reStructuredText). Includes are inlined. -->

# movePrimary (database command)

**`movePrimary`**

In a sharded cluster, `movePrimary` reassigns the
primary shard which holds all un-sharded collections in
the database.  `movePrimary` first changes the primary shard in
the cluster metadata, and then migrates all un-sharded collections to the
specified shard. Use the command with the following form:

```javascript
db.adminCommand( { movePrimary: <databaseName>, to: <newPrimaryShard> } )
```

For example, the following command moves the primary shard from `test` to
`shard0001`:

```javascript
db.adminCommand( { movePrimary : "test", to : "shard0001" } )
```

When the command returns, the database's primary shard location
has switched to the specified shard. To fully decommission a
shard, use the `removeShard` command.

`movePrimary` is an administrative command that is only
available for `mongos` instances.

**Warning:**

After starting `movePrimary`, do **not** perform any
read or write operations against any unsharded collection in that
database until the command completes. Read or write operations
issued against those collections during the migration can result
in unexpected behavior, including potential failure of the
migration operation or loss of data. 

## Compatibility

This command is available in deployments hosted in the following environments: 

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas): The fully
  managed service for MongoDB deployments in the cloud

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Considerations

`mongos` uses `"majority"` write concern for
`movePrimary`.

### Maintenance Windows

`movePrimary` may require a significant time to complete
depending on the size of the database and factors such as network health
or machine resources. During migration, attempts to write or perform any
DDL operations to the unsharded collections on the database being moved
fail with the error: `"movePrimary is in progress"`.

Consider scheduling a maintenance window during which applications stop
all reads and writes to the cluster. Issuing `movePrimary`
during planned downtime mitigates the risk of encountering undefined
behavior due to interleaving reads or writes to the unsharded
collections in the database. 

### Namespace Conflicts

`movePrimary` fails if the destination shard contains a
conflicting collection namespace. For example:

1. An administrator issues `movePrimary` to change the
   primary shard for the `hr` database.

#. A user or application issues a write operation against an unsharded
   collection in `hr` while `movePrimary` is moving that collection.
   The write operation creates the collection in the original primary
   shard.
  
#. An administrator later issues `movePrimary` to restore
   the original primary shard for the `hr` database.

#. `movePrimary` fails due to the conflicting namespace
   left behind from the interleaving write operation.

### Rebuilding Indexes

As part of the `movePrimary` operation, the destination shard must
rebuild indexes on the migrated collections after becoming the primary
shard. This may require a significant amount of time depending on
the number of indexes per collection and the amount of data to index.

See /core/index-creation for more information on the index
build process. 

## Additional Information

See /tutorial/remove-shards-from-cluster for a complete
procedure.
