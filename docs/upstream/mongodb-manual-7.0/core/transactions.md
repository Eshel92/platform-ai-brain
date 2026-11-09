<!-- Converted from core/transactions.txt (reStructuredText). Includes are inlined. -->

# Transactions

MongoDB supports multi-document ACID transactions. Transactions provide
atomicity, consistency, isolation, and durability according to the
configured read and write concern settings. You can use transactions
across multiple operations, collections, databases, documents, and
shards. Transactions are available in all supported MongoDB versions.

In MongoDB, an operation on a single document is atomic. The MongoDB
document model supports embedding related data within a single document,
which reduces the need for multi-document transactions. When your
application requires atomicity across multiple documents, use
transactions.

## Transactions API

Use the language selector to set the language of the
following example.

This example highlights the key components of the transactions API. In
particular, it uses the callback API. The callback API:

- starts a transaction
- executes the specified operations
- commits the result or ends the transaction on error

Errors in server-side operations, such as the `DuplicateKeyError`,
can end the transaction and result in a command error to alert
the user that the transaction has ended. This behavior is expected
and occurs even if the client never calls `Session.abortTransaction()`. 
To incorporate custom error handling, use the Core API
on your transaction.

The callback API incorporates retry logic for certain errors. The 
driver tries to rerun the transaction after a TransientTransactionError or UnknownTransactionCommitResult commit error. 

Starting in MongoDB 6.2, the server does not retry the transaction if
it receives a TransactionTooLargeForCache error.

**Important:**

- Use the MongoDB driver for your MongoDB version.

- When using drivers, each operation in the transaction must pass
  the session to each operation.

- Operations in a transaction use transaction-level read
  concern, transaction-level
  write concern, and
  transaction-level read preference.

- You can create collections in transactions implicitly or 
  explicitly. See transactions-create-collections-indexes.

(Code example not available offline: /driver-examples/test_examples.py)

This example highlights the key components of the transactions API. In
particular, it uses the callback API. The callback API:

- starts a transaction
- executes the specified operations
- commits the result or ends the transaction on error

Errors in server-side operations, such as the `DuplicateKeyError`,
can end the transaction and result in a command error to alert
the user that the transaction has ended. This behavior is expected
and occurs even if the client never calls `Session.abortTransaction()`. 
To incorporate custom error handling, use the Core API
on your transaction.

The callback API incorporates retry logic for certain errors. The 
driver tries to rerun the transaction after a TransientTransactionError or UnknownTransactionCommitResult commit error. 

Starting in MongoDB 6.2, the server does not retry the transaction if
it receives a TransactionTooLargeForCache error.

**Important:**

- Use the MongoDB driver for your MongoDB version.

- When using drivers, each operation in the transaction must pass
  the session to each operation.

- Operations in a transaction use transaction-level read
  concern, transaction-level
  write concern, and
  transaction-level read preference.

- You can create collections in transactions implicitly or 
  explicitly. See transactions-create-collections-indexes.

```java
String uri = "<your-connection-string>";
/*
  For a replica set, include the replica set name and a seedlist of the members in the URI string; e.g.
  String uri = "mongodb://mongodb0.example.com:27017,mongodb1.example.com:27017/admin?replicaSet=myRepl";
  For a sharded cluster, connect to the mongos instances.
  For example:
  String uri = "mongodb://mongos0.example.com:27017,mongos1.example.com:27017:27017/admin";
 */

final MongoClient client = MongoClients.create(uri);

/*
    Create collections.
 */

client.getDatabase("sample_mflix").getCollection("movies")
        .withWriteConcern(WriteConcern.MAJORITY).insertOne(new Document("title", "test"));
client.getDatabase("sample_mflix").getCollection("comments")
        .withWriteConcern(WriteConcern.MAJORITY).insertOne(new Document("text", "test"));

/* Step 1: Start a client session. */

final ClientSession clientSession = client.startSession();

/* Step 2: Optional. Define options to use for the transaction. */

TransactionOptions txnOptions = TransactionOptions.builder()
        .writeConcern(WriteConcern.MAJORITY)
        .build();

/* Step 3: Define the sequence of operations to perform inside the transactions. */

TransactionBody<String> txnBody = new TransactionBody<String>() {
    public String execute() {
        MongoCollection<Document> coll1 = client.getDatabase("sample_mflix").getCollection("movies");
        MongoCollection<Document> coll2 = client.getDatabase("sample_mflix").getCollection("comments");

        /*
           Important:: You must pass the session to the operations.
         */
        coll1.insertOne(clientSession, new Document("title", "test 2"));
        coll2.insertOne(clientSession, new Document("text", "test 2"));
        return "Inserted into collections in the same database";
    }
};
try {
    /*
       Step 4: Use .withTransaction() to start a transaction,
       execute the callback, and commit (or abort on error).
    */

    clientSession.withTransaction(txnBody, txnOptions);
} catch (RuntimeException e) {
    // some error handling
} finally {
    clientSession.close();
}
```

This example highlights the key components of the transactions API. In
particular, it uses the callback API. The callback API:

- starts a transaction
- executes the specified operations
- commits the result or ends the transaction on error

Errors in server-side operations, such as the `DuplicateKeyError`,
can end the transaction and result in a command error to alert
the user that the transaction has ended. This behavior is expected
and occurs even if the client never calls `Session.abortTransaction()`. 
To incorporate custom error handling, use the Core API
on your transaction.

The callback API incorporates retry logic for certain errors. The 
driver tries to rerun the transaction after a TransientTransactionError or UnknownTransactionCommitResult commit error. 

Starting in MongoDB 6.2, the server does not retry the transaction if
it receives a TransactionTooLargeForCache error.

**Important:**

- Use the MongoDB driver for your MongoDB version.

- When using drivers, each operation in the transaction must pass
  the session to each operation.

- Operations in a transaction use transaction-level read
  concern, transaction-level
  write concern, and
  transaction-level read preference.

- You can create collections in transactions implicitly or 
  explicitly. See transactions-create-collections-indexes.

(Code example not available offline: /driver-examples/node_transactions.js)

This example highlights the key components of the transactions API. In
particular, it uses the callback API. The callback API:

- starts a transaction
- executes the specified operations
- commits the result or ends the transaction on error

Errors in server-side operations, such as the `DuplicateKeyError`,
can end the transaction and result in a command error to alert
the user that the transaction has ended. This behavior is expected
and occurs even if the client never calls `Session.abortTransaction()`. 
To incorporate custom error handling, use the Core API
on your transaction.

The callback API incorporates retry logic for certain errors. The 
driver tries to rerun the transaction after a TransientTransactionError or UnknownTransactionCommitResult commit error. 

Starting in MongoDB 6.2, the server does not retry the transaction if
it receives a TransactionTooLargeForCache error.

**Important:**

- Use the MongoDB driver for your MongoDB version.

- When using drivers, each operation in the transaction must pass
  the session to each operation.

- Operations in a transaction use transaction-level read
  concern, transaction-level
  write concern, and
  transaction-level read preference.

- You can create collections in transactions implicitly or 
  explicitly. See transactions-create-collections-indexes.

(Code example not available offline: /driver-examples/DocumentationExamplesTest.php)

This example highlights the key components of the transactions API. In
particular, it uses the callback API. The callback API:

- starts a transaction
- executes the specified operations
- commits the result or ends the transaction on error

Errors in server-side operations, such as the `DuplicateKeyError`,
can end the transaction and result in a command error to alert
the user that the transaction has ended. This behavior is expected
and occurs even if the client never calls `Session.abortTransaction()`. 
To incorporate custom error handling, use the Core API
on your transaction.

The callback API incorporates retry logic for certain errors. The 
driver tries to rerun the transaction after a TransientTransactionError or UnknownTransactionCommitResult commit error. 

Starting in MongoDB 6.2, the server does not retry the transaction if
it receives a TransactionTooLargeForCache error.

**Important:**

- Use the MongoDB driver for your MongoDB version.

- When using drivers, each operation in the transaction must pass
  the session to each operation.

- Operations in a transaction use transaction-level read
  concern, transaction-level
  write concern, and
  transaction-level read preference.

- You can create collections in transactions implicitly or 
  explicitly. See transactions-create-collections-indexes.

```csharp
// For a replica set, include the replica set name and a seedlist of the members in the URI string; e.g.
// string uri = "mongodb://mongodb0.example.com:27017,mongodb1.example.com:27017/?replicaSet=myRepl";
// For a sharded cluster, connect to the mongos instances; e.g.
// string uri = "mongodb://mongos0.example.com:27017,mongos1.example.com:27017/";
var client = new MongoClient(connectionString);

// Prereq: Create collections.
var database1 = client.GetDatabase("mydb1");
var collection1 = database1.GetCollection<BsonDocument>("foo").WithWriteConcern(WriteConcern.WMajority);
collection1.InsertOne(new BsonDocument("abc", 0));

var database2 = client.GetDatabase("mydb2");
var collection2 = database2.GetCollection<BsonDocument>("bar").WithWriteConcern(WriteConcern.WMajority);
collection2.InsertOne(new BsonDocument("xyz", 0));

// Step 1: Start a client session.
using (var session = client.StartSession())
{
    // Step 2: Optional. Define options to use for the transaction.
    var transactionOptions = new TransactionOptions(
        writeConcern: WriteConcern.WMajority);

    // Step 3: Define the sequence of operations to perform inside the transactions
    var cancellationToken = CancellationToken.None; // normally a real token would be used
    result = session.WithTransaction(
        (s, ct) =>
        {
            try
            {
                collection1.InsertOne(s, new BsonDocument("abc", 1), cancellationToken: ct);
                collection2.InsertOne(s, new BsonDocument("xyz", 999), cancellationToken: ct);
            }
            catch (MongoWriteException)
            {
                // Do something in response to the exception
                throw; // NOTE: You must rethrow the exception otherwise an infinite loop can occur.
            }
            return "Inserted into collections in different databases";
        },
        transactionOptions,
        cancellationToken);
}
```

This example highlights the key components of the transactions API. In
particular, it uses the callback API. The callback API:

- starts a transaction
- executes the specified operations
- commits the result or ends the transaction on error

Errors in server-side operations, such as the `DuplicateKeyError`,
can end the transaction and result in a command error to alert
the user that the transaction has ended. This behavior is expected
and occurs even if the client never calls `Session.abortTransaction()`. 
To incorporate custom error handling, use the Core API
on your transaction.

The callback API incorporates retry logic for certain errors. The 
driver tries to rerun the transaction after a TransientTransactionError or UnknownTransactionCommitResult commit error. 

Starting in MongoDB 6.2, the server does not retry the transaction if
it receives a TransactionTooLargeForCache error.

**Important:**

- Use the MongoDB driver for your MongoDB version.

- When using drivers, each operation in the transaction must pass
  the session to each operation.

- Operations in a transaction use transaction-level read
  concern, transaction-level
  write concern, and
  transaction-level read preference.

- You can create collections in transactions implicitly or 
  explicitly. See transactions-create-collections-indexes.

(Code example not available offline: /driver-examples/test-mongoc-sample-commands.c)

This example highlights the key components of the transactions API. In
particular, it uses the callback API. The callback API:

- starts a transaction
- executes the specified operations
- commits the result or ends the transaction on error

Errors in server-side operations, such as the `DuplicateKeyError`,
can end the transaction and result in a command error to alert
the user that the transaction has ended. This behavior is expected
and occurs even if the client never calls `Session.abortTransaction()`. 
To incorporate custom error handling, use the Core API
on your transaction.

The callback API incorporates retry logic for certain errors. The 
driver tries to rerun the transaction after a TransientTransactionError or UnknownTransactionCommitResult commit error. 

Starting in MongoDB 6.2, the server does not retry the transaction if
it receives a TransactionTooLargeForCache error.

**Important:**

- Use the MongoDB driver for your MongoDB version.

- When using drivers, each operation in the transaction must pass
  the session to each operation.

- Operations in a transaction use transaction-level read
  concern, transaction-level
  write concern, and
  transaction-level read preference.

- You can create collections in transactions implicitly or 
  explicitly. See transactions-create-collections-indexes.

(Code example not available offline: /driver-examples/cpp-with-transaction.cpp)

This example highlights the key components of the transactions API. In
particular, it uses the callback API. The callback API:

- starts a transaction
- executes the specified operations
- commits the result or ends the transaction on error

Errors in server-side operations, such as the `DuplicateKeyError`,
can end the transaction and result in a command error to alert
the user that the transaction has ended. This behavior is expected
and occurs even if the client never calls `Session.abortTransaction()`. 
To incorporate custom error handling, use the Core API
on your transaction.

The callback API incorporates retry logic for certain errors. The 
driver tries to rerun the transaction after a TransientTransactionError or UnknownTransactionCommitResult commit error. 

Starting in MongoDB 6.2, the server does not retry the transaction if
it receives a TransactionTooLargeForCache error.

**Important:**

- Use the MongoDB driver for your MongoDB version.

- When using drivers, each operation in the transaction must pass
  the session to each operation.

- Operations in a transaction use transaction-level read
  concern, transaction-level
  write concern, and
  transaction-level read preference.

- You can create collections in transactions implicitly or 
  explicitly. See transactions-create-collections-indexes.

(Code example not available offline: /driver-examples/test_examples_motor.py)

This example highlights the key components of the transactions API. In
particular, it uses the callback API. The callback API:

- starts a transaction
- executes the specified operations
- commits the result or ends the transaction on error

Errors in server-side operations, such as the `DuplicateKeyError`,
can end the transaction and result in a command error to alert
the user that the transaction has ended. This behavior is expected
and occurs even if the client never calls `Session.abortTransaction()`. 
To incorporate custom error handling, use the Core API
on your transaction.

The callback API incorporates retry logic for certain errors. The 
driver tries to rerun the transaction after a TransientTransactionError or UnknownTransactionCommitResult commit error. 

Starting in MongoDB 6.2, the server does not retry the transaction if
it receives a TransactionTooLargeForCache error.

**Important:**

- Use the MongoDB driver for your MongoDB version.

- When using drivers, each operation in the transaction must pass
  the session to each operation.

- Operations in a transaction use transaction-level read
  concern, transaction-level
  write concern, and
  transaction-level read preference.

- You can create collections in transactions implicitly or 
  explicitly. See transactions-create-collections-indexes.

(Code example not available offline: /driver-examples/with_transactions_examples_spec.rb)

This example highlights the key components of the transactions API. In
particular, it uses the callback API. The callback API:

- starts a transaction
- executes the specified operations
- commits the result or ends the transaction on error

Errors in server-side operations, such as the `DuplicateKeyError`,
can end the transaction and result in a command error to alert
the user that the transaction has ended. This behavior is expected
and occurs even if the client never calls `Session.abortTransaction()`. 
To incorporate custom error handling, use the Core API
on your transaction.

The callback API incorporates retry logic for certain errors. The 
driver tries to rerun the transaction after a TransientTransactionError or UnknownTransactionCommitResult commit error. 

Starting in MongoDB 6.2, the server does not retry the transaction if
it receives a TransactionTooLargeForCache error.

**Important:**

- Use the MongoDB driver for your MongoDB version.

- When using drivers, each operation in the transaction must pass
  the session to each operation.

- Operations in a transaction use transaction-level read
  concern, transaction-level
  write concern, and
  transaction-level read preference.

- You can create collections in transactions implicitly or 
  explicitly. See transactions-create-collections-indexes.

(Code example not available offline: /driver-examples/mod.rs)

This example highlights the key components of the transactions API. In
particular, it uses the callback API. The callback API:

- starts a transaction
- executes the specified operations
- commits the result or ends the transaction on error

Errors in server-side operations, such as the `DuplicateKeyError`,
can end the transaction and result in a command error to alert
the user that the transaction has ended. This behavior is expected
and occurs even if the client never calls `Session.abortTransaction()`. 
To incorporate custom error handling, use the Core API
on your transaction.

The callback API incorporates retry logic for certain errors. The 
driver tries to rerun the transaction after a TransientTransactionError or UnknownTransactionCommitResult commit error. 

Starting in MongoDB 6.2, the server does not retry the transaction if
it receives a TransactionTooLargeForCache error.

**Important:**

- Use the MongoDB driver for your MongoDB version.

- When using drivers, each operation in the transaction must pass
  the session to each operation.

- Operations in a transaction use transaction-level read
  concern, transaction-level
  write concern, and
  transaction-level read preference.

- You can create collections in transactions implicitly or 
  explicitly. See transactions-create-collections-indexes.

(Code example not available offline: /driver-examples/go_examples.go)

This example uses the core API. Because the
core API does not incorporate retry logic for the
transient-transaction-error or
unknown-transaction-commit-result commit errors, the
example includes explicit logic to retry the transaction for
these errors:

**Note:**

When possible, use the callback API, which 
incorporates automatic retry logic. 

**Important:**

- Use the MongoDB driver for your MongoDB version.

- When using drivers, each operation in the transaction must pass
  the session to each operation.

- Operations in a transaction use transaction-level read
  concern, transaction-level
  write concern, and
  transaction-level read preference.

- You can create collections in transactions implicitly or 
  explicitly. See transactions-create-collections-indexes.

(Code example not available offline: /driver-examples/DocumentationTransactionsExampleSpec.scala)

**See also:**

For an example in `mongosh`, see
txn-mongo-shell-example.

## Transactions and Atomicity

For situations that require atomicity of reads and writes to multiple
documents (in a single or multiple collections), MongoDB supports
distributed transactions, including transactions on replica sets and 
sharded clusters.

Distributed transactions are atomic:

- Transactions either apply all data changes or roll back the changes.

- If a transaction commits, all data changes made in the transaction
  are saved and are visible outside of the transaction.

  Until a transaction commits, the data changes made in the
  transaction are not visible outside the transaction.

  However, when a transaction writes to multiple shards, not all
  outside read operations need to wait for the result of the committed
  transaction to be visible across the shards. For example, if a
  transaction is committed and write 1 is visible on shard A but write
  2 is not yet visible on shard B, an outside read at read concern
  `"local"` can read the results of write 1 without
  seeing write 2.

- When a transaction aborts, all data changes made in the transaction
  are discarded without ever becoming visible.

**Important:**

In most cases, a distributed transaction incurs a greater
performance cost over single document writes, and the
availability of distributed transactions should not be a
replacement for effective schema design. For many scenarios, the
denormalized data model (embedded documents and arrays) will continue to be optimal for your
data and use cases. That is, for many scenarios, modeling your data
appropriately will minimize the need for distributed
transactions. 

For additional transactions usage considerations
(such as runtime limit and oplog size limit), see also
production-considerations.

**See also:**

transactions-prod-consideration-outside-reads

## Transactions and Operations

Transactions can be used across multiple operations,
collections, databases, documents, and shards.

For transactions:

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

For a list of operations not supported in transactions, see
transactions-ops-restricted.

**Tip:**

When creating or dropping a collection immediately before
starting a transaction, if the collection is accessed within the
transaction, issue the create or drop operation with write
concern `"majority"` to ensure that the transaction
can acquire the required locks.

**See also:**

Transactions and Operations Reference

### Create Collections and Indexes in a Transaction

You can perform the following operations in a transaction 
if it is not a cross-shard write transaction:

- Create collections.

- Create indexes on new empty collections created earlier in the same
  transaction.

When creating a collection inside a transaction:

- You can implicitly create a collection, such as with:

  - an insert operation
    for a non-existent collection, or

  - an update/findAndModify operation with `upsert: true`
    for a non-existent collection.

- You can explicitly create a collection using the `create`
  command or its helper `db.createCollection()`.

When creating an index inside a transaction [#create-existing-index]_, the
index to create must be on either:

- a non-existent collection. The collection is created as part of the
  operation.

- a new empty collection created earlier in the same transaction.

#### Restrictions

- .. include:: /includes/extracts/transactions-cross-shard-collection-restriction.rst

- .. include:: /includes/graphLookup-sharded-coll-transaction-note.rst

- For explicit creation of a collection or an index inside a
  transaction, the transaction read concern level must be
  `"local"`.
  
  To explicitly create collections and indexes, use the following
  commands and methods:

  | Command | Method |
  |---|---|
  | `create` | `db.createCollection()` |
  | `createIndexes` | \| `db.collection.createIndex()` \| `db.collection.createIndexes()` |

**See also:**

transactions-ops-restricted

### Count Operation

To perform a count operation within a transaction, use the
`$count` aggregation stage or the `$group` (with a
`$sum` expression) aggregation stage.

MongoDB drivers provide a collection-level API
`countDocuments(filter, options)` as a helper method that uses the
`$group` with a `$sum` expression
to perform a count. 

`mongosh` provides the
`db.collection.countDocuments()` helper method that uses the
`$group` with a `$sum` expression to perform a
count.

### Distinct Operation

To perform a distinct operation within a transaction:

- For unsharded collections, you can use the
  `db.collection.distinct()` method/the
  `distinct` command as well as the aggregation pipeline
  with the `$group` stage.

- For sharded collections, you cannot use the
  `db.collection.distinct()` method or the
  `distinct` command.

  To find the distinct values for a sharded collection, use the
  aggregation pipeline with the `$group` stage instead.
  For example:

  - Instead of `db.coll.distinct("x")`, use

    ```javascript
    db.coll.aggregate([ 
       { $group: { _id: null, distinctValues: { $addToSet: "$x" } } }, 
       { $project: { _id: 0 } } 
    ])
    ```

  - Instead of `db.coll.distinct("x", { status: "A" })`, use:

    ```javascript
    db.coll.aggregate([ 
       { $match: { status: "A" } },
       { $group: { _id: null, distinctValues: { $addToSet: "$x" } } }, 
       { $project: { _id: 0 } } 
    ])
    ```

  The pipeline returns a cursor to a document:

  ```javascript
  { "distinctValues" : [ 2, 3, 1 ] }
  ```

  Iterate the cursor to access the results document.

### Informational Operations

Informational commands, such as `hello`,
`buildInfo`, `connectionStatus` (and their
helper methods) are allowed in transactions; however, they cannot be
the first operation in the transaction.

### Restricted Operations

The following operations are not allowed in transactions:

- Creating new collections in cross-shard write transactions. For
  example, if you write to an existing collection in one shard and
  implicitly create a collection in a different shard, MongoDB cannot
  perform both operations in the same transaction.

- Explicit creation of collections, e.g.
  `db.createCollection()` method, and indexes, e.g.
  `db.collection.createIndexes()` and
  `db.collection.createIndex()` methods, when using a read
  concern level other than `"local"`.

- The `listCollections` and `listIndexes`
  commands and their helper methods.

- Other non-CRUD and non-informational operations, such as
  `createUser`, `getParameter`,
  `count`, etc. and their helpers.

**See also:**

- txn-prod-considerations-ddl

- Transactions and Operations Reference

## Transactions and Sessions

- Transactions are associated with a session.

- You can have at most one open transaction at a time for a session.

- When using the drivers, each operation in the transaction must be
  associated with the session. Refer to your driver specific
  documentation for details.

- If a session ends and it has an open transaction, the transaction
  aborts.

## Read Concern, Write Concern, and Read Preference

### Transactions and Read Preference

Operations in a transaction use the transaction-level read
preference.

Using the drivers, you can set the transaction-level read
preference at the transaction start:

- If the transaction-level read preference is unset, the transaction
  uses the session-level read preference.

- If transaction-level and the session-level read preference are unset,
  the transaction uses the client-level read preference. By default,
  the client-level read preference is `primary`.

Transactions that contain
read operations must use read preference `primary`. All
operations in a given transaction must route to the same member.

### Transactions and Read Concern

Operations in a transaction use the transaction-level
read concern. This means a read concern set at
the collection and database level is ignored inside the transaction.

You can set the transaction-level read concern
at the transaction start.

- If the transaction-level read concern is unset, the transaction-level
  read concern defaults to the session-level read concern.

- If transaction-level and the session-level read concern are unset,
  the transaction-level read concern defaults to the client-level read
  concern. By default, the client-level read concern is
  `"local"` for reads on the primary. See also:

  - transactions-read-preference
  - MongoDB Defaults

Transactions support the following read concern levels:

#### `"local"`

- Read concern `"local"` returns the most recent data
  available from the node but can be rolled back.

- .. include:: /includes/transactions/read-isolation-levels.rst

- For transactions on sharded cluster, `"local"` read
  concern cannot guarantee that the data is from the same snapshot
  view across the shards. If snapshot isolation is required, use
  transactions-read-concern-snapshot read concern.

- .. include:: /includes/extracts/transactions-create-collections-read-concern.rst

#### `"majority"`

- If the transaction commits with write concern "majority", read concern `"majority"`
  returns data that has been acknowledged by a majority of the replica
  set members and can't be rolled back. Otherwise, read concern
  `"majority"` provides no guarantees that read operations
  read majority-committed data.

- For transactions on sharded cluster, read concern
  `"majority"` can't guarantee that the data is from the 
  same snapshot view across the shards. If snapshot isolation is
  required, use read concern transactions-read-concern-snapshot.

#### `"snapshot"`

- Read concern `"snapshot"` returns data from a
  snapshot of majority committed data **if** the transaction commits
  with write concern "majority".

- If the transaction does not use write concern "majority" for the commit, the
  `"snapshot"` read concern provides **no** guarantee that
  read operations used a snapshot of majority-committed data.

- For transactions on sharded clusters, the
  `"snapshot"` view of the data **is** synchronized
  across shards.

### Transactions and Write Concern

Transactions use the transaction-level write concern to commit the write operations. Write
operations inside transactions must be run without an explicit write
concern specification and use the default write concern. At commit
time, the writes are committed using the transaction-level write
concern.

**Tip:**

Don't explicitly set the write concern for the individual write
operations inside a transaction. Setting write concerns for the
individual write operations inside a transaction returns an error.

You can set the transaction-level write concern
at the transaction start:

- If the transaction-level write concern is unset, the
  transaction-level write concern defaults to the session-level write
  concern for the commit.

- If the transaction-level write concern and the session-level write
  concern are unset, the transaction-level write concern defaults to the
  client-level write concern of:

  - `w: "majority"` in MongoDB 5.0 and later,
    with differences for deployments containing arbiters. See
    wc-default-behavior.

  - `w: 1 <`

**See also:**

MongoDB Defaults

Transactions support all write concern w
values, including:

#### `w: 1`

- Write concern `w: 1 <` returns
  acknowledgment after the commit has been applied to the primary.

  **Important:**

  When you commit with `w: 1 <`, your
  transaction can be rolled back if there is a failover.

- When you commit with `w: 1 <` write
  concern, transaction-level `"majority"` read concern
  provides **no** guarantees that read operations in the transaction
  read majority-committed data.

- When you commit with `w: 1 <` write
  concern, transaction-level `"snapshot"` read concern
  provides **no** guarantee that read operations in the transaction
  used a snapshot of majority-committed data.

#### `w: "majority"`

- Write concern `w: "majority"` returns
  acknowledgment after the commit has been applied to a majority of
  voting members.

- When you commit with `w: "majority"`
  write concern, transaction-level `"majority"` read
  concern guarantees that operations have read majority-committed
  data. For transactions on sharded clusters, this view of the
  majority-committed data is not synchronized across shards.

- When you commit with `w: "majority"`
  write concern, transaction-level `"snapshot"` read
  concern guarantees that operations have read from a synchronized
  snapshot of majority-committed data.

**Note:**

Regardless of the write concern specified for the
transaction, the commit operation for a
sharded cluster transaction includes some parts that use ``{w:
"majority", j: true}`` write concern.

The server parameter
`coordinateCommitReturnImmediatelyAfterPersistingDecision`
controls when transaction commit decisions are returned to the client.

The parameter was introduced in MongDB 5.0 with a default value of
`true`. In MongoDB 6.1 the default value changes to `false`. 

When `coordinateCommitReturnImmediatelyAfterPersistingDecision` is
`false`, the shard transaction coordinator
waits for all members to acknowledge a transaction commit before returning the commit decision to
the client.

If you specify a `"majority"` write concern for writes and the 
operation does not replicate to the  calculated majority
of replica set members before it returns a response, then the data eventually 
replicates or rolls back. See wc-wtimeout.

Regardless of the write concern specified for the
transaction, the driver applies
`w: "majority"` as the write concern when
retrying `commitTransaction`.

## Transactions Considerations

The following sections describe transaction requirements and
considerations that vary by deployment type, storage engine, and
MongoDB version.

### Production Considerations

For transactions in production environments, see
production-considerations. In addition, for sharded
clusters, see production-considerations-sharded.

### Arbiters

You cannot change a shard key using a transaction
if the replica set has an arbiter. Arbiters cannot participate in the
data operations required for multi-shard transactions.

Transactions whose write operations span multiple shards will error
and abort if any transaction operation reads from or writes to a
shard that contains an arbiter.

### Shard Configuration Restriction

You cannot run transactions on a sharded cluster that has a shard
with `writeConcernMajorityJournalDefault` set to `false`
(such as a shard with a voting member that uses the in-memory
storage engine).

**Note:**

Regardless of the write concern specified for the
transaction, the commit operation for a
sharded cluster transaction includes some parts that use ``{w:
"majority", j: true}`` write concern.

### Diagnostics

To obtain transaction status and metrics, use the following methods:

* - Source
  - Returns

* - | `db.serverStatus()` method
    | `serverStatus` command

  - Returns server-status-transactions metrics.

    Some `serverStatus` response fields are not returned on 
    MongoDB Atlas Free clusters or Flex clusters. For more information, see 
    free-shard-commands-with-limits in the MongoDB Atlas 
    documentation.

* - `$currentOp` aggregation pipeline

  - Returns:

    - `$currentOp.transaction` if an operation is part of a
      transaction.

    - Information on inactive sessions that are holding locks as part
      of a transaction.

    - `$currentOp.twoPhaseCommitCoordinator` metrics for
      sharded transactions that involves writes to multiple shards.

* - | `db.currentOp()` method
    | `currentOp` command

  - Returns:

    - `currentOp.transaction` if an operation is part of a
      transaction.

    - `currentOp.twoPhaseCommitCoordinator` metrics for
      sharded transactions that involves writes to multiple shards.

* - `mongod` and `mongos` log messages

  - Includes information on slow transactions (which are transactions
    that exceed the `operationProfiling.slowOpThresholdMs`
    threshold) in the `TXN` log component.

### Feature Compatibility Version (FCV)

To use transactions, the featureCompatibilityVersion
for all members of the deployment must be at least:

| Deployment | Minimum `featureCompatibilityVersion` |
|---|---|
| Replica Set | `4.0` |
| Sharded Cluster | `4.2` |

To check the FCV for a member, connect to the member and run the
following command:

```javascript
db.adminCommand( { getParameter: 1, featureCompatibilityVersion: 1 } )
```

For more information, see the
`setFeatureCompatibilityVersion` reference page.

### Storage Engines

Transactions are supported on replica sets and sharded
clusters where:

- the primary uses the WiredTiger storage engine, and

- the secondary members use either the WiredTiger storage engine or 
  the in-memory storage engines.

**Note:**

You cannot run transactions on a sharded cluster that has a shard
with `writeConcernMajorityJournalDefault` set to
`false`, such as a shard with a voting member that uses the
in-memory storage engine.

### Limit Critical Section Wait Time

Starting in MongoDB 5.2 (and 5.0.4):

- When a query accesses a shard, a chunk migration or DDL operation may hold the critical section for the
  collection.

- To limit the time a shard waits for a critical section within a
  transaction, use the
  `metadataRefreshInTransactionMaxWaitBehindCritSecMS`
  parameter.

## Learn More

- Drivers API
- Production Considerations
- Sharded Clusters
- Transactions and Operations
