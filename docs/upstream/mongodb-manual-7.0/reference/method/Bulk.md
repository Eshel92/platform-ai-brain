<!-- Converted from reference/method/Bulk.txt (reStructuredText). Includes are inlined. -->

# Bulk() (mongosh method)

**Tip:**

MongoDB also provides the `db.collection.bulkWrite()` method for 
performing bulk write operations.

## Description

**`Bulk()`**

Bulk operations builder used to construct a list of write operations
to perform in bulk for a single collection. To instantiate the
builder, use either the
`db.collection.initializeOrderedBulkOp()` or the
`db.collection.initializeUnorderedBulkOp()` method.

## Compatibility

This command is available in deployments hosted in the following
environments: 

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas): The fully
  managed service for MongoDB deployments in the cloud

**Note:**

This command is supported in all MongoDB Atlas clusters.
For information on Atlas support for all commands, see 
Unsupported Commands.

  

## Ordered and Unordered Bulk Operations

The builder can construct the list of operations as *ordered* or
*unordered*.

### Ordered Operations

With an *ordered* operations list, MongoDB executes the write
operations in the list serially. If an error occurs during the
processing of one of the write operations, MongoDB will return without
processing any remaining write operations in the list.

Use `db.collection.initializeOrderedBulkOp()` to create a
builder for an ordered list of write commands.

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

With an *unordered* operations list, MongoDB can execute in parallel,
as well as in a nondeterministic order, the write operations in the
list. If an error occurs during the processing of one of the write
operations, MongoDB will continue to process remaining write operations
in the list.

Use `db.collection.initializeUnorderedBulkOp()` to create a
builder for an unordered list of write commands.

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

 

## Methods

The `Bulk()` builder has the following methods:

| Name | Description |
|---|---|
| `Bulk.insert()` | Adds an insert operation to a list of operations. |
| `Bulk.find()` | Specifies the query condition for an update or a remove operation. |
| `Bulk.find.delete()` | Adds a multiple document delete operation to a list of operations. |
| `Bulk.find.deleteOne()` | Adds a single document delete operation to a list of operations. |
| `Bulk.find.remove()` | An alias for `Bulk.find.delete()`. |
| `Bulk.find.removeOne()` | An alias for `Bulk.find.deleteOne()`. |
| `Bulk.find.replaceOne()` | Adds a single document replacement operation to a list of operations. |
| `Bulk.find.updateOne()` | Adds a single document update operation to a list of operations. |
| `Bulk.find.update()` | Adds a `multi` update operation to a list of operations. |
| `Bulk.find.upsert()` | Specifies `upsert: true` for an update operation. |
| `Bulk.execute()` | Executes a list of operations in bulk. |
| `Bulk.getOperations()` | Returns an array of write operations executed in the `Bulk()` operations object. |
| `Bulk.toJSON()` | Returns a JSON document that contains the number of operations and batches in the `Bulk()` operations object. |
| `Bulk.toString()` | Returns the `Bulk.toJSON()` results as a string. |
