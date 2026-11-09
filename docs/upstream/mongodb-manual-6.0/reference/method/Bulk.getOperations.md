<!-- Converted from reference/method/Bulk.getOperations.txt (reStructuredText). Includes are inlined. -->

# Bulk.getOperations()

**`Bulk.getOperations()`**

Returns an array of write operations executed through
`Bulk.execute()`. The returned write operations are in
groups as determined by MongoDB for execution. For information on
how MongoDB groups the list of bulk write operations, see
Bulk.execute() Behavior.

Only use `Bulk.getOperations()` after a
`Bulk.execute()`. Calling `Bulk.getOperations()`
before you call `Bulk.execute()` will result in an
*incomplete* list.

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

The following initializes a `Bulk()` operations builder on the
`items` collection, adds a series of write operations, executes the
operations, and then calls `getOperations()` on the
`bulk` builder object:

```javascript
var bulk = db.items.initializeUnorderedBulkOp();

for (var i = 1; i <= 1500; i++) {
    bulk.insert( { x: i } );
}

bulk.execute();
bulk.getOperations();
```

The `getOperations()` method returns an array with the
operations executed. The output shows that MongoDB divided the
operations into 2 groups, one with 1000 operations and one with 500.
For information on how MongoDB groups the list of bulk write
operations, see Bulk.execute() Behavior

Although the method returns all 1500 operations in the returned array,
this page omits some of the results for brevity.

```javascript
[
   {
      "originalZeroIndex" : 0,
      "batchType" : 1,
      "operations" : [
         { "_id" : ObjectId("53a8959f1990ca24d01c6165"), "x" : 1 },

         ... // Content omitted for brevity

         { "_id" : ObjectId("53a8959f1990ca24d01c654c"), "x" : 1000 }
      ]
   },
   {
      "originalZeroIndex" : 1000,
      "batchType" : 1,
      "operations" : [
         { "_id" : ObjectId("53a8959f1990ca24d01c654d"), "x" : 1001 },

         ... // Content omitted for brevity

         { "_id" : ObjectId("53a8959f1990ca24d01c6740"), "x" : 1500 }
      ]
   }
]
```

## Returned Fields

The array contains documents with the following fields:

**`originalZeroIndex`**

Specifies the order in which the operation was added to the bulk
operations builder, based on a zero index; e.g. first operation
added to the bulk operations builder will have
`originalZeroIndex` value of `0`.

**`batchType`**

Specifies the write operations type.

| `batchType` | Operation |
|---|---|
| 1 | Insert |
| 2 | Update |
| 3 | Remove |

**`operations`**

Array of documents that contain the details of the operation.

**See also:**

- `Bulk()`
- `Bulk.execute()`
