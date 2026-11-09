<!-- Converted from reference/command/abortTransaction.txt (reStructuredText). Includes are inlined. -->

# abortTransaction

## Definition

**`abortTransaction`**

Terminates the multi-document transaction and rolls back any data changes made by the
operations within the transaction. That is, the transaction ends
without saving any of the changes made by the operations in the
transaction.

   helper method

**Tip:**

In `mongosh`, this command can also be run through the `Session.abortTransaction`.

Helper methods are convenient for `mongosh` users, but they may not
return the same level of information as database commands.  In cases where
the convenience is not needed or the additional return fields are required,
use the database command.

To run the `abortTransaction`, the command must be run
against the `admin` database and run within a
`Session`.

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
     abortTransaction: 1, 
     txnNumber: <long>,
     writeConcern: <document>,
     autocommit: false,
     comment: <any>
   }
)
```

## Behavior

### Atomicity

When a transaction aborts, all data changes made by the writes in the
transaction are discarded without ever becoming visible and the
transaction ends.

### Security

If running with auditing, operations in an
aborted transaction are still audited.
