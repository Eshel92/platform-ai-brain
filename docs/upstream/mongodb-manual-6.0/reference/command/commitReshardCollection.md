<!-- Converted from reference/command/commitReshardCollection.txt (reStructuredText). Includes are inlined. -->

# commitReshardCollection

## Definition

**`commitReshardCollection`**

**New in version:** 5.0

During a resharding operation, MongoDB does not block writes until
the estimated duration to complete the resharding operation is
below **two seconds**.

If the current estimate is above two seconds but the time frame is
acceptable to you, you can finish resharding faster. The
`commitReshardCollection` command blocks writes early and
forces the resharding operation to complete.

   helper method

**Tip:**

In `mongosh`, this command can also be run through the `sh.commitReshardCollection`.

Helper methods are convenient for `mongosh` users, but they may not
return the same level of information as database commands.  In cases where
the convenience is not needed or the additional return fields are required,
use the database command.

## Compatibility

This command is available in deployments hosted in the following environments: 

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas?tck=docs_server): The fully
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
     commitReshardCollection: "<database>.<collection>"
   }
)
```

The `mongosh` provides a wrapper method
`sh.commitReshardCollection()`.

## Example

### Commit a Resharding Operation

The following command forces the resharding
operation on the `sales.orders` to block writes
and complete:

```javascript
db.adminCommand({
  commitReshardCollection: "sales.orders"
})
```

**See also:**

sharding-resharding
