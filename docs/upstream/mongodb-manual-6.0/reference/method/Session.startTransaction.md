<!-- Converted from reference/method/Session.startTransaction.txt (reStructuredText). Includes are inlined. -->

# Session.startTransaction()

## Definition

**`Session.startTransaction(<options>)`**

Starts a multi-document transaction
associated with the session. At any given time, you can have at most
one open transaction for a session.

**Changed in version:** 4.2

Starting in MongoDB 4.2, multi-document transactions are available
for both sharded clusters and replica sets.

**Important:**

Within a transaction, you can only specify read and write (CRUD)
operations on **existing** collections. For example, a
multi-document transaction cannot include an insert operation
that would result in the creation of a new collection.

The `Session.startTransaction()` method can take a document
with the following options:

```javascript
{ readConcern: { level: <level>}, writeConcern: { w: <value>, j: <boolean>, wtimeout: <number> } }
```

* - Option
  - Description

* - `readConcern`

  - *Optional.* A document that specifies the read concern for all operations in the transaction,
    overriding operation-specific read concern.

    You can specify one of the following read concern levels:

    - `"snapshot"`

    - `"local"`

    - `"majority"`

    For `"local"` and `"majority"` read
    concern, MongoDB may sometimes substitute a stronger read
    concern.

* - `writeConcern`

  - *Optional*. A document that specifies the write concern for the transaction. This write concern
    applies to the transaction commit and abort operations.

    The operations within the transaction use `"w:
    1" <`, overriding operation-specific write concern.

    If you commit using `"w: 1" <` write
    concern, your transaction can be rolled back during the
    failover process.

    For MongoDB Drivers, transactions use the client-level write
    concern as the default.

## Compatibility

This method is available in deployments hosted in the following environments: 

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas?tck=docs_server): The fully
  managed service for MongoDB deployments in the cloud

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Behavior

### Operations Supported within a Transaction

**Note:**

If running with access control, you
must have privileges for the operations in the transaction.

For multi-document transactions:

- You can create collections and indexes in transactions. For
  details, see transactions-create-collections-indexes

- The collections used in a transaction can be in different
  databases.

  **Note:**

  You cannot create new collections in cross-shard write transactions.
  For example, if you write to an existing collection in one shard and
  implicitly create a collection in a different shard, MongoDB cannot
  perform both operations in the same transaction.

- You cannot write to capped
  collections.

- You cannot use read concern `"snapshot"` when reading
  from a capped collection.
  (Starting in MongoDB 5.0)

- You cannot read/write to collections in the `config`, `admin`,
  or `local` databases.

- You cannot write to `system.*` collections.

- You cannot return the supported operation's query plan using 
  `explain` or similar commands.

- For cursors created outside of a transaction, you cannot call
  `getMore` inside the transaction.

- For cursors created in a transaction, you cannot call
  `getMore` outside the transaction.

- .. include:: /includes/extracts/transactions-killop-change.rst

* - Method
  - Command
  - Note

* - `db.collection.aggregate()` 
  - `aggregate`
  - Excluding the following stages:

    - `$collStats`
    - `$currentOp`
    - `$indexStats`
    - `$listLocalSessions`
    - `$listSessions`
    - `$merge`
    - `$out`
    - `$planCacheStats`
    - `$unionWith`

* - `db.collection.countDocuments()` 
  -

  - Excluding the following query operator expressions:

    - `$where`
    - `$near`
    - `$nearSphere`

    The method uses the `$match` aggregation stage for the
    query and `$group` aggregation stage with a
    `$sum` expression to perform the count.

* - `db.collection.distinct()`
  - `distinct`
  - Available on unsharded collections.

    | For sharded collections, use the aggregation pipeline with the
      `$group` stage. See transactions-operations-distinct.

* - `db.collection.find()`
  - `find`
  - 

* - | `db.collection.deleteMany()`
    | `db.collection.deleteOne()`
    | `db.collection.remove()`

  - `delete`
  - 

* - | `db.collection.findOneAndDelete()`
    | `db.collection.findOneAndReplace()`
    | `db.collection.findOneAndUpdate()`

  - `findAndModify`

  - If the update or replace operation is run with `upsert: true` on a 
    non-existing collection, the collection is implicitly created.

    For more details, see transactions-operations-ddl.

* - | `db.collection.insertMany()`
    | `db.collection.insertOne()`

  - `insert`

  - If run on a non-existing collection, the collection is implicitly 
    created.

    For more details, see transactions-operations-ddl.

* - | `db.collection.updateOne()`
    | `db.collection.updateMany()`
    | `db.collection.replaceOne()`

  - `update`

  - If run on a non-existing collection, the collection is implicitly 
    created.

    For more details, see transactions-operations-ddl.

* - | `db.collection.bulkWrite()`
    | Various /reference/method/js-bulk
  - 
  - If run on a non-existing collection, the collection is implicitly 
    created.

    For more details, see transactions-operations-ddl.

Operations that affect the database catalog, such as creating or
dropping a collection or an index, are not allowed in multi-document	
transactions. For example, a multi-document transaction cannot include	
an insert operation that would result in the creation of a new	
collection. See transactions-ops-restricted.

Informational commands, such as `hello`,
`buildInfo`, `connectionStatus` (and their
helper methods) are allowed in transactions; however, they cannot be
the first operation in the transaction.

### Read Preference

Transactions support read preference
`primary`.

### Atomicity

While the transaction is open, no data changes made by operations in
the transaction is visible outside the transaction:

- When a transaction commits, all data changes made in the transaction
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

- When a transaction aborts, all data changes made by the writes in the
  transaction are discarded without ever becoming visible and the
  transaction ends.

## Example

Consider a scenario where as changes are made to an employee's record
in the `hr` database, you want to ensure that the `events`
collection in the `reporting` database are in sync with the `hr`
changes. That is, you want to ensure that these writes are done as a
single transaction, such that either both operations succeed or fail.

The `employees` collection in the `hr` database has the following
documents:

```javascript
{ "_id" : ObjectId("5af0776263426f87dd69319a"), "employee" : 3, "name" : { "title" : "Mr.", "name" : "Iba Ochs" }, "status" : "Active", "department" : "ABC" }
{ "_id" : ObjectId("5af0776263426f87dd693198"), "employee" : 1, "name" : { "title" : "Miss", "name" : "Ann Thrope" }, "status" : "Active", "department" : "ABC" }
{ "_id" : ObjectId("5af0776263426f87dd693199"), "employee" : 2, "name" : { "title" : "Mrs.", "name" : "Eppie Delta" }, "status" : "Active", "department" : "XYZ" }
```

The `events` collection in the `reporting` database has the
following documents:

```javascript
{ "_id" : ObjectId("5af07daa051d92f02462644a"), "employee" : 1, "status" : { "new" : "Active", "old" : null }, "department" : { "new" : "ABC", "old" : null } }
{ "_id" : ObjectId("5af07daa051d92f02462644b"), "employee" : 2, "status" : { "new" : "Active", "old" : null }, "department" : { "new" : "XYZ", "old" : null } }
{ "_id" : ObjectId("5af07daa051d92f02462644c"), "employee" : 3, "status" : { "new" : "Active", "old" : null }, "department" : { "new" : "ABC", "old" : null } }
```

The following example opens a transaction, updates an employee's status
to `Inactive` in the `employees` status and inserts a corresponding
document to the `events` collection, and commits the two operations
as a single transaction.

```javascript
// Runs the txnFunc and retries if TransientTransactionError encountered

function runTransactionWithRetry(txnFunc, session) {
    while (true) {
        try {
            txnFunc(session);  // performs transaction
            break;
        } catch (error) {
            // If transient error, retry the whole transaction
            if (error?.errorLabels?.includes("TransientTransactionError")  ) {
                print("TransientTransactionError, retrying transaction ...");
                continue;
            } else {
                throw error;
            }
        }
    }   
}

// Retries commit if UnknownTransactionCommitResult encountered

function commitWithRetry(session) {
    while (true) {
        try {
            session.commitTransaction(); // Uses write concern set at transaction start.
            print("Transaction committed.");
            break;
        } catch (error) {
            // Can retry commit
            if (error?.errorLabels?.includes("UnknownTransactionCommitResult") ) {
                print("UnknownTransactionCommitResult, retrying commit operation ...");
                continue;
            } else {
                print("Error during commit ...");
                throw error;
            }
       }
    }
}

// Updates two collections in a transactions

function updateEmployeeInfo(session) {
    employeesCollection = session.getDatabase("hr").employees;
    eventsCollection = session.getDatabase("reporting").events;

    session.startTransaction( { readConcern: { level: "snapshot" }, writeConcern: { w: "majority" } } );

    try{
        employeesCollection.updateOne( { employee: 3 }, { $set: { status: "Inactive" } } );
        eventsCollection.insertOne( { employee: 3, status: { new: "Inactive", old: "Active" } } );
    } catch (error) {
        print("Caught exception during transaction, aborting.");
        session.abortTransaction();
        throw error;
    }

    commitWithRetry(session);
}

// Start a session.
session = db.getMongo().startSession( { readPreference: { mode: "primary" } } );

try{
   runTransactionWithRetry(updateEmployeeInfo, session);
} catch (error) {
   // Do something with error
} finally {
   session.endSession();
}
```

**See also:**

- `Session.abortTransaction()`
- `Session.commitTransaction()`
