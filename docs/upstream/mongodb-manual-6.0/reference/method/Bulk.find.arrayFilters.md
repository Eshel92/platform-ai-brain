<!-- Converted from reference/method/Bulk.find.arrayFilters.txt (reStructuredText). Includes are inlined. -->

# Bulk.find.arrayFilters()

## Description

**`Bulk.find.arrayFilters(<array of filter documents>)`**

Determines which array elements to modify for an update operation on
an array field:

```javascript
Bulk.find(<query>).arrayFilters([ <filter1>, ... ]).updateOne(<update>);
Bulk.find(<query>).arrayFilters([ <filter1>, ... ]).update(<update>);
```

In the update document, use the `$[<identifier>]` filtered
positional operator to define an identifier, which you then reference
in the array filter documents. You cannot have an array filter
document for an identifier if the identifier is not included in the
update document.

The `<identifier>` must begin with a lowercase letter and
contain only alphanumeric characters.

You can include the same identifier multiple times in the update
document; however, for each distinct identifier (`$[identifier]`)
in the update document, you must specify **exactly one**
corresponding array filter document. That is, you cannot specify
multiple array filter documents for the same identifier. For
example, if the update statement includes the identifier `x`
(possibly multiple times), you cannot specify the following for
`arrayFilters` that includes 2 separate filter documents for `x`:

```javascript
// INVALID

[
  { "x.a": { $gt: 85 } },
  { "x.b": { $gt: 80 } }
]
```

However, you can specify compound conditions on the same identifier
in a single filter document, such as in the following examples:

```javascript
// Example 1
[
  { $or: [{"x.a": {$gt: 85}}, {"x.b": {$gt: 80}}] }
]
// Example 2
[
  { $and: [{"x.a": {$gt: 85}}, {"x.b": {$gt: 80}}] }
]
// Example 3
[
  { "x.a": { $gt: 85 }, "x.b": { $gt: 80 } }
]
```

Append to `Bulk.find()` method to specify the array filters
for the `updateOne()` and
`update()` operations.

## Compatibility

This command is available in deployments hosted in the following
environments: 

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas?tck=docs_server): The fully
  managed service for MongoDB deployments in the cloud

**Note:**

This command is supported in all MongoDB Atlas clusters.
For information on Atlas support for all commands, see 
Unsupported Commands.

   

## Example

```javascript
var bulk = db.coll.initializeUnorderedBulkOp();
bulk.find({}).arrayFilters( [ { "elem.grade": { $gt: 85 } } ] ).updateOne( { $set: { "grades.$[elem].mean" : 70 } } );
bulk.execute();
```

**See also:**

- `db.collection.initializeUnorderedBulkOp()`
- `db.collection.initializeOrderedBulkOp()`
- `Bulk.find.update()`
- `Bulk.find.updateOne()`
- `Bulk.execute()`
- All Bulk Methods
