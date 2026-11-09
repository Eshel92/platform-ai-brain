<!-- Converted from reference/command/cleanupReshardCollection.txt (reStructuredText). Includes are inlined. -->

# cleanupReshardCollection

## Definition

**`cleanupReshardCollection`**

**New in version:** 5.0

The `cleanupReshardCollection` command cleans up metadata
of a failed resharding operation. You
only need to run this command if a primary failover occurred while you
ran a resharding operation.

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
     cleanupReshardCollection: "<database>.<collection>"
   }
)
```

## Example

### Clean up a Failed Resharding Operation

The following example cleans up metadata of a failed resharding
operation on the `sales.orders` collection:

```javascript
db.adminCommand({
  cleanupReshardCollection: "sales.orders"
})
```

**See also:**

sharding-resharding
