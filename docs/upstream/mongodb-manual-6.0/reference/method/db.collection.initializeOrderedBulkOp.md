<!-- Converted from reference/method/db.collection.initializeOrderedBulkOp.txt (reStructuredText). Includes are inlined. -->

# db.collection.initializeOrderedBulkOp()

**Tip:**

MongoDB also provides the `db.collection.bulkWrite()` method for 
performing bulk write operations.

## Definition

**`db.collection.initializeOrderedBulkOp()`**

**Important:** `mongosh` Method

This page documents a `mongosh` method. This is *not*
the documentation for a language-specific driver, such as Node.js.

For MongoDB API drivers, refer to the language-specific
`MongoDB driver documentation`.

Initializes and returns a new `Bulk()` operations builder
for a collection. The builder constructs an ordered list of write
operations that MongoDB executes in bulk.

:returns: new `Bulk()` operations builder object.

## Compatibility

This command is available in deployments hosted in the following
environments: 

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas?tck=docs_server): The fully
  managed service for MongoDB deployments in the cloud

**Note:**

This command is supported in all MongoDB Atlas clusters.
For information on Atlas support for all commands, see 
Unsupported Commands.

## Behavior

### Order of Operation

With an *ordered* operations list, MongoDB executes the write
operations in the list serially.

### Execution of Operations

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

### Error Handling

If an error occurs during the processing of one of the write
operations, MongoDB will return without processing any remaining write
operations in the list.

## Examples

The following initializes a `Bulk()` operations builder on the
`users` collection, adds a series of write operations, and executes
the operations:

```javascript
var bulk = db.users.initializeOrderedBulkOp();
bulk.insert( { user: "abc123", status: "A", points: 0 } );
bulk.insert( { user: "ijk123", status: "A", points: 0 } );
bulk.insert( { user: "mop123", status: "P", points: 0 } );
bulk.find( { status: "D" } ).delete();
bulk.find( { status: "P" } ).update( { $set: { comment: "Pending" } } );
bulk.execute();
```

**See also:**

- `db.collection.initializeUnorderedBulkOp()`
- `Bulk.find()`
- `Bulk.find.removeOne()`
- `Bulk.execute()`
