<!-- Converted from reference/command/setUserWriteBlockMode.txt (reStructuredText). Includes are inlined. -->

# setUserWriteBlockMode (database command)

## Definition

**`setUserWriteBlockMode`**

**New in version:** 6.0

The `setUserWriteBlockMode` command blocks and unblocks writes to
the entire cluster.

During cluster-to-cluster sync, `mongosync`, the cluster-to-cluster 
synchronization tool, uses the `setUserWriteBlockMode` command
to block writes on the destination cluster.
For more information, see the HTTP API start command.

**Note:**

Users and applications with the
`bypassWriteBlockingMode` privilege can bypass the
block and continue to perform writes.

## Compatibility

This command is available in deployments hosted in the following environments: 

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas): The fully
  managed service for MongoDB deployments in the cloud

**Important:**

This command is not supported in M0 and Flex clusters.
For more information, see Unsupported Commands.

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Syntax

The command has the following syntax:

```javascript
db.adminCommand(
   {
     setUserWriteBlockMode: 1,
     global: <boolean>
   }
)
```

## Command Fields

The command takes the following fields:

| Field | Type | Description |
|---|---|---|
| `setUserWriteBlockMode` | integer | Set this field to `1`. |
| `global` | boolean | Blocks writes on a cluster when set to `true`.  To enable writes on a cluster, set `global: false`. |

     

## Required Access

To execute the `setUserWriteBlockMode` command, the user must
have the `setUserWriteBlockMode` privilege.

## Example

#. Enable user write block mode:

   ```javascript
   db.adminCommand( {
      setUserWriteBlockMode: 1,
      global: true
   } )
   ```

#. Add a record to the collection:

   ```javascript
   db.names.insertOne( { name: "George Washington Cable" } )
   ```

   The server blocks the write because the user write block is enabled.

   Example  Output:

   ```text
   MongoServerError: User writes blocked
   ```

#. Disable user write block mode:

   ```javascript
   db.adminCommand( {
      setUserWriteBlockMode: 1,
      global: false 
   } )
   ```

#. Add a record to the collection:

   ```javascript
   db.names.insertOne( { name: "George Washington Cable" } )
   ```

   The `insertOne()` method writes to a collection.  The
   server allows the write because the user write block is disabled.
