<!-- Converted from reference/method/Bulk.execute.txt (reStructuredText). Includes are inlined. -->

# Bulk.execute() (mongosh method)

**Tip:**

MongoDB also provides `db.collection.bulkWrite()` for 
performing bulk write operations.

## Description

**`Bulk.execute()`**

Executes the list of operations built by the `Bulk()`
operations builder.

`Bulk.execute()` accepts the following parameter:

| Parameter | Type | Description |
|---|---|---|
| `writeConcern` | document | Optional. write concern document for the bulk operation as a whole. Omit to use default. For a standalone `mongod` server, the write concern defaults to `{ w: majority }`. With a replica set, the default write concern is `{ w: majority }` unless modified as part of the replica set configuration, or potentially if the replica set contains multiple arbiters. See bulk-execute-ex-write-concern for an example. Do not explicitly set the write concern for the operation if run in a transaction. To use write concern with transactions, see transactions-write-concern. |

:returns: A `BulkWriteResult` object that contains the
   status of the operation.

After execution, you cannot re-execute the `Bulk()`
object without reinitializing. See
`db.collection.initializeUnorderedBulkOp()` and
`db.collection.initializeOrderedBulkOp()`.

## Compatibility

This command is available in deployments hosted in the following
environments: 

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas): The fully
  managed service for MongoDB deployments in the cloud

**Note:**

This command is supported in all MongoDB Atlas clusters.
For information on Atlas support for all commands, see 
Unsupported Commands.

   

## Behavior

### Ordered Operations

When executing an `ordered` list of operations, MongoDB
groups the operations by the `operation type` and
contiguity; i.e. *contiguous* operations of the same type are grouped
together. For example, if an ordered list has two insert operations
followed by an update operation followed by another insert operation,
MongoDB groups the operations into three separate groups: first group
contains the two insert operations, second group contains the update
operation, and the third group contains the last insert operation. This
behavior is subject to change in future versions.

`Bulk()` operations in `mongosh` and comparable
methods in the drivers do not have a limit for the number of operations
in a group. To see how the operations are grouped for bulk operation
execution, call `Bulk.getOperations()` *after* the execution.

**See also:**

- `Write Command Batch Limit Size`

Executing an `ordered` list of operations on a
sharded collection will generally be slower than executing an
`unordered` list
since with an ordered list, each operation must wait for the previous
operation to finish.

### Unordered Operations

When executing an `unordered` list of operations,
MongoDB groups the operations. With an unordered bulk operation, the
operations in the list may be reordered to increase performance. As
such, applications should not depend on the ordering when performing
`unordered` bulk
operations.

`Bulk()` operations in `mongosh` and comparable
methods in the drivers do not have a limit for the number of operations
in a group. To see how the operations are grouped for bulk operation
execution, call `Bulk.getOperations()` *after* the execution.

**See also:**

- `Write Command Batch Limit Size`

### Transactions

`Bulk()` can be used inside distributed transactions.

For `Bulk.insert()` operations, the collection must already exist.

For `Bulk.find.upsert()`, if the operation results in an
upsert, the collection must already exist.

Do not explicitly set the write concern for the operation if run in
a transaction. To use write concern with transactions, see
transactions-write-concern.

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

## Examples

### Execute Bulk Operations

The following initializes a `Bulk()` operations builder on the
`items` collection, adds a series of insert operations, and executes
the operations:

```javascript
var bulk = db.items.initializeUnorderedBulkOp();
bulk.insert( { item: "abc123", status: "A", defaultQty: 500, points: 5 } );
bulk.insert( { item: "ijk123", status: "A", defaultQty: 100, points: 10 } );
bulk.execute( );
```

The operation returns the following `BulkWriteResult()` object:

```javascript
BulkWriteResult({
  acknowledged: true,
  insertedCount: 2,
  insertedIds: {
    '0': ObjectId("64e61e3b84ff8808cd43a92c"),
    '1': ObjectId("64e61e3b84ff8808cd43a92d")
  },
  matchedCount: 0,
  modifiedCount: 0,
  deletedCount: 0,
  upsertedCount: 0,
  upsertedIds: {}
})
```

For details on the return object, see `BulkWriteResult()`. For
details on the batches executed, see `Bulk.getOperations()`.

### Override Default Write Concern

The following operation to a replica set specifies a write
concern of `"w: 1"` with a `wtimeout` of 5000 
milliseconds such that the method returns after the writes propagate 
to a majority of the voting replica set members or the method times out 
after five seconds.

```javascript
var bulk = db.items.initializeUnorderedBulkOp();
bulk.insert( { item: "efg123", status: "A", defaultQty: 100, points: 0 } );
bulk.insert( { item: "xyz123", status: "A", defaultQty: 100, points: 0 } );
bulk.execute( { w: 1, wtimeout: 5000 } );
```

The operation returns the following `BulkWriteResult()` object:

```javascript
BulkWriteResult({
  acknowledged: true,
  insertedCount: 2,
  insertedIds: {
    '0': ObjectId("64e61e3b84ff8808cd43a92c"),
    '1': ObjectId("64e61e3b84ff8808cd43a92d")
  },
  matchedCount: 0,
  modifiedCount: 0,
  deletedCount: 0,
  upsertedCount: 0,
  upsertedIds: {}
})
```

**See also:**

`Bulk()` for a listing of methods available for bulk
operations.
