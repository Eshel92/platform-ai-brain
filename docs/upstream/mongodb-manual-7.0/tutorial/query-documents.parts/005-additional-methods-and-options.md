<!-- Part 5 of 5 of tutorial/query-documents.md (split because the page is big). -->

## Additional Methods and Options

**shell:**

You can also read documents from a collection with:

- The `db.collection.findOne` method
- The `$match` pipeline stage in an 
  aggregation pipeline

**Note:**

The `db.collection.findOne()` method performs the same 
operation as `db.collection.find()` with a limit of 1.

**compass:**

MongoDB Compass also accepts the
following query bar options:

|  |  |
|---|---|
| `Project` | Specify which fields to return in the resulting data. |
| `Sort` | Specify the sort order of the returned documents. |
| `Skip` | Specify the first n-number of documents to skip before returning the result set. |
| `Limit` | Specify the maximum number of documents to return. |

**c:**

You can also read documents from a collection with:

- [mongoc_find_and_modify_opts_t](https://mongoc.org/libmongoc/current/mongoc_find_and_modify_opts_t.html)

**python:**

You can also read documents from a collection with:

- `pymongo.collection.Collection.find_one`
- The `$match` pipeline stage in an
  aggregation pipeline. See the
  [PyMongo Aggregation Examples](https://pymongo.readthedocs.io/en/stable/examples/aggregation.html).

**Note:**

The `pymongo.collection.Collection.find_one`
method performs the same operation as the
the `pymongo.collection.Collection.find` method
with a limit of 1.

**motor:**

You can also read documents from a collection with:

- `pymongo.asynchronous.collection.AsyncCollection.find_one`
- The `$match` pipeline stage in an
  aggregation pipeline

**Note:**

The `pymongo.asynchronous.collection.AsyncCollection.find_one`
method performs the same operation as
`pymongo.asynchronous.collection.AsyncCollection.find`
with a limit of 1.

**java-sync:**

You can also read documents from a collection with the `$match`
pipeline stage in an aggregation pipeline. For more information, see the
Java Synchronous Driver Aggregation Examples.

**java-async:**

You can also read documents from a collection with the `$match`
pipeline stage in an aggregation pipeline. For more information, see the
Java Asynchronous Driver Aggregation Examples.

**kotlin-coroutine:**

You can also read documents from a collection with the `$match`
pipeline stage in an aggregation pipeline. For more information, see the
`Kotlin Coroutine Driver Find Operation Examples`.

**nodejs:**

You can also read documents from a collection with:

- `Collection.findOne()`
- The `$match` pipeline stage in an
  aggregation pipeline. For more information, see the
  `aggregation tutorial`.

**Note:**

The `Collection.findOne()`
method performs the same operation as
`Collection.find()`
with a limit of 1.

**php:**

You can also read documents from a collection with:

- `MongoDBCollection::findOne()`
- The `$match` pipeline stage in an
  aggregation pipeline. For more information, see the
  aggregation example.

**Note:**

The `MongoDBCollection::findOne()`
method performs the same operation as
`MongoDBCollection::find()`
with a limit of 1.

**ruby:**

You can also read documents from a collection with the `$match`
pipeline stage in an aggregation pipeline. For more information, see the
`aggregation examples`.

**scala:**

You can also read documents from a collection with the `$match`
pipeline stage in an aggregation pipeline. For more information, see the
`aggregate method`.

**csharp:**

You can also read documents from a collection with:

- `MongoCollection.FindOne()`
- The `$match` pipeline stage in an
  aggregation pipeline. For more information, see the
  [LINQ documentation](https://www.mongodb.com/docs/drivers/csharp/current/fundamentals/linq/).

**Note:**

The `MongoCollection.FindOne()`
method performs the same operation as
`MongoCollection.Find()`
with a limit of 1.

**go:**

You can also read documents from a collection with:

- `Collection.FindOne`
- The `$match` pipeline stage in an
  aggregation pipeline. For more information, see
  `Collection.Aggregate`.
