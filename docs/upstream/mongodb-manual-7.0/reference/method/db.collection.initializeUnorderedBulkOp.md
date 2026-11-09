<!-- Converted from reference/method/db.collection.initializeUnorderedBulkOp.txt (reStructuredText). Includes are inlined. -->

# db.collection.initializeUnorderedBulkOp() (mongosh method)

**Tip:**

MongoDB also provides the `db.collection.bulkWrite()` method for 
performing bulk write operations.

## Definition

**`db.collection.initializeUnorderedBulkOp()`**

**Important:** `mongosh` Method

This page documents a `mongosh` method. This is *not*
the documentation for a language-specific driver, such as Node.js.

For MongoDB API drivers, refer to the language-specific
`MongoDB driver documentation`.

Initializes and returns a new `Bulk()` operations builder
for a collection. The builder constructs an *unordered* list of
write operations that MongoDB executes in bulk.

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

### Order of Operation

With an *unordered* operations list, MongoDB can execute in parallel
the write operations in the list and in any order. If the order of
operations matter, use
`db.collection.initializeOrderedBulkOp()` instead.

### Execution of Operations

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

### Error Handling

If an error occurs during the processing of one of the write
operations, MongoDB will continue to process remaining write operations
in the list.

## Example

The following initializes a `Bulk()` operations builder and
adds a series of insert operations to add multiple documents:

```javascript
var bulk = db.users.initializeUnorderedBulkOp();
bulk.insert( { user: "abc123", status: "A", points: 0 } );
bulk.insert( { user: "ijk123", status: "A", points: 0 } );
bulk.insert( { user: "mop123", status: "P", points: 0 } );
bulk.execute();
```

**See also:**

- `db.collection.initializeOrderedBulkOp()`
- `Bulk()`
- `Bulk.insert()`
- `Bulk.execute()`
