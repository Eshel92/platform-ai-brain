<!-- Converted from reference/command/abortReshardCollection.txt (reStructuredText). Includes are inlined. -->

# abortReshardCollection (database command)

## Definition

**`abortReshardCollection`**

**New in version:** 5.0

During a resharding operation, you can
abort the operation with the `abortReshardCollection`
command.

You can abort a resharding operation at
any point until the commit phase. If the resharding operation has reached the commit phase before you run the
`abortReshardCollection` command, the command returns an
error.

   helper method

**Tip:**

In `mongosh`, this command can also be run through the `sh.abortReshardCollection`.

Helper methods are convenient for `mongosh` users, but they may not
return the same level of information as database commands.  In cases where
the convenience is not needed or the additional return fields are required,
use the database command.

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
db.adminCommand(
   {
     abortReshardCollection: "<database>.<collection>"
   } 
)
```

## Example

### Abort a Resharding Operation

The following example aborts a running resharding operation on the `sales.orders` collection:

```javascript
db.adminCommand({
  abortReshardCollection: "sales.orders"
})
```

**See also:**

sharding-resharding
