<!-- Converted from reference/command/commitTransaction.txt (reStructuredText). Includes are inlined. -->

# commitTransaction (database command)

## Definition

**`commitTransaction`**

Saves the changes made by the operations in the multi-document
transaction and ends the transaction. 

   `Session.withTransaction`
   helper methods

**Tip:**

In `mongosh`, this command can also be run through the `Session.commitTransaction` and.

Helper methods are convenient for `mongosh` users, but they may not
return the same level of information as database commands.  In cases where
the convenience is not needed or the additional return fields are required,
use the database command.

To run the `commitTransaction`, the command must be run
against the `admin` database and run within a
`Session`. 

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
     commitTransaction: 1, 
     txnNumber: <long>,
     writeConcern: <document>,
     autocommit: false,
     comment: <any>
   }
)
```

## Behavior

### Write Concern

When committing the transaction, the session uses the write
concern specified at the transaction start.
See `Session.startTransaction()`.

If you commit using the `"w: 1" <` write
concern, your transaction can be rolled back if there is a
failover..

### Atomicity

When a transaction commits, all data changes made in the transaction
are saved and visible outside the transaction. That is, a transaction
will not commit some of its changes while rolling back others.

Until a transaction commits, the data changes made in the
transaction are not visible outside the transaction.

However, when a transaction writes to multiple shards, not all
outside read operations need to wait for the result of the committed
transaction to be visible across the shards. For example, if a
transaction is committed and write 1 is visible on shard A but write
2 is not yet visible on shard B, an outside read at read concern
`"local"` can read the results of write 1 without
seeing write 2.
