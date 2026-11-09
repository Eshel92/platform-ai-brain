<!-- Converted from tutorial/insert-documents.txt (reStructuredText). Includes are inlined. -->

# Create Documents

In MongoDB, a Create operation consists of inserting documents into a collection. This page provides examples.

You can insert documents in MongoDB by using the following
methods:

- Your programming language's driver.
- The MongoDB Atlas UI. To learn more, see 
  insert-documents-atlas.
- `MongoDB Compass`.

**Note:** Creating a Collection

Inserting a document into a collection that doesn't exist creates that collection.

## Insert a Single Document

`db.collection.insertOne()` inserts a *single*
document into a collection.

This example inserts one document into `inventory`. 
If the document does not specify `_id`, MongoDB adds one. 
See write-op-insert-behavior.

```javascript
db.movies.insertOne({
   title: "The Substance",
   genres: ["Drama", "Horror", "Sci-Fi"],
   runtime: 140,
   rated: "R",
   year: 2024,
   directors: ["Coralie Fargeat"],
   cast: ["Demi Moore", "Margaret Qualley"],
   type: "movie"
})
```

`insertOne()` returns a document that
includes the newly inserted document's `_id` field value. For
an example of a return document, see
db.collection.insertOne() reference.

```javascript
db.movies.find( { title: "The Substance" } )
```

## Insert a Single Document

`pymongo.collection.Collection.insert_one` inserts a
*single* document into a
collection.

The following example inserts a new document into the
`inventory` collection. If the document does not specify
an `_id` field, the PyMongo driver adds the `_id` field
with an ObjectId value to the new document. See
write-op-insert-behavior.

(Code example not available offline: /driver-examples/test_examples.py)

`insert_one` returns an
instance of `pymongo.results.InsertOneResult` whose
`inserted_id` field contains the `_id` of the newly
inserted document.

To retrieve the document that you just inserted, query the collection:

(Code example not available offline: /driver-examples/test_examples.py)

## Insert a Single Document

`motor.motor_asyncio.AsyncIOMotorCollection.insert_one` inserts a
*single* document into a
collection.

The following example inserts a new document into the
`inventory` collection. If the document does not specify
an `_id` field, the Motor driver adds the `_id` field
with an ObjectId value to the new document. See
write-op-insert-behavior.

(Code example not available offline: /driver-examples/test_examples_motor.py)

`insert_one` returns an
instance of `pymongo.results.InsertOneResult` whose
`inserted_id` field contains the `_id` of the newly
inserted document.

To retrieve the document that you just inserted, query the collection:

(Code example not available offline: /driver-examples/test_examples_motor.py)

## Insert a Single Document

`IMongoCollection.insertOne()`      
inserts a *single* document into
a collection.

This example inserts one document into `inventory`. If the document 
does not specify `_id`, MongoDB adds one. 
See write-op-insert-behavior.

(Code example not available offline: /driver-examples/DocumentationSamples.java)

`IMongoCollection.insertOne()` 
returns an instance of [InsertOneResult](https://mongodb.github.io/mongo-java-driver/{+java-driver-version+}/apidocs/driver-core/com/mongodb/client/result/InsertOneResult.html).
You can access the `_id` field of the inserted document by
calling the [getInsertedId()](https://mongodb.github.io/mongo-java-driver/{+java-driver-version+}/apidocs/driver-core/com/mongodb/client/result/InsertOneResult.html#getInsertedId()) method on the result.

To retrieve the document that you just inserted, query the collection:

(Code example not available offline: /driver-examples/DocumentationSamples.java)

## Insert a Single Document

[com.mongodb.reactivestreams.client.MongoCollection.insertOne](https://mongodb.github.io/mongo-java-driver/{+java-driver-version+}/apidocs/driver-reactive-streams/com/mongodb/reactivestreams/client/MongoCollection.html#insertOne(TDocument))      
inserts a *single* document into
a collection with the [Java Reactive Streams Driver](https://www.mongodb.com/docs/languages/java/reactive-streams-driver/current/):

```json
{ item: "canvas", qty: 100, tags: ["cotton"], size: { h: 28, w: 35.5, uom: "cm" } }
```

This example inserts one document into `inventory`. If the document 
does not specify `_id`, MongoDB adds one. 
See write-op-insert-behavior.

(Code example not available offline: /driver-examples/AsyncDocumentationSamples.java)

[com.mongodb.reactivestreams.client.MongoCollection.insertOne](https://mongodb.github.io/mongo-java-driver/{+java-driver-version+}/apidocs/driver-reactive-streams/com/mongodb/reactivestreams/client/MongoCollection.html#insertOne(TDocument))      
returns a [Publisher](http://www.reactive-streams.org/reactive-streams-1.0.1-javadoc/org/reactivestreams/Publisher.html)
object. The `Publisher` inserts the document into a collection when subscribers request data.

To retrieve the document that you just inserted, query the collection:

(Code example not available offline: /driver-examples/AsyncDocumentationSamples.java)

## Insert a Single Document

[MongoCollection.insertOne](https://mongodb.github.io/mongo-java-driver/{+java-driver-version+}/apidocs/driver-kotlin-coroutine/mongodb-driver-kotlin-coroutine/com.mongodb.kotlin.client.coroutine/-mongo-collection/insert-one.html)
inserts a *single* document into
a collection.

This example inserts one document into `inventory`. 
If the document does not specify `_id`, MongoDB adds one. 
See write-op-insert-behavior.

(Code example not available offline: /driver-examples/kotlin_examples.kt)

[MongoCollection.insertOne](https://mongodb.github.io/mongo-java-driver/{+java-driver-version+}/apidocs/driver-kotlin-coroutine/mongodb-driver-kotlin-coroutine/com.mongodb.kotlin.client.coroutine/-mongo-collection/insert-one.html) returns an
instance of [InsertOneResult](https://mongodb.github.io/mongo-java-driver/{+java-driver-version+}/apidocs/driver-core/com/mongodb/client/result/InsertOneResult.html).
You can access the `_id` field of the inserted document by
accessing the `insertedId` field of the result.

To retrieve the document that you just inserted, query the collection:  

(Code example not available offline: /driver-examples/kotlin_examples.kt)

## Insert a Single Document

`Collection.insertOne()`
inserts a *single* document into a
collection.

The following example inserts a new document into the
`inventory` collection. If the document does not specify
an `_id` field, the Node.js driver adds the `_id` field
with an ObjectId value to the new document. See
write-op-insert-behavior.

(Code example not available offline: /driver-examples/node_insert.js)

`insertOne()` returns a
promise that provides a `result`.  The `result.insertedId`
promise contains the `_id` of the newly inserted document.

To retrieve the document that you just inserted, query the collection:

(Code example not available offline: /driver-examples/node_insert.js)

## Insert a Single Document

`MongoDBCollection::insertOne()`
inserts a *single* document into a
collection.

This example inserts one document into `inventory`. 
If the document does not specify `_id`, MongoDB adds one. 
See write-op-insert-behavior.

(Code example not available offline: /driver-examples/DocumentationExamplesTest.php)

Upon successful insert, the
`insertOne()`
method returns an instance of
`MongoDBInsertOneResult`
whose
`getInsertedId()`
method returns the `_id` of the newly inserted document.

To retrieve the document that you just inserted, query the collection:

(Code example not available offline: /driver-examples/DocumentationExamplesTest.php)

## Insert a Single Document

`Mongo::Collection#insert_one()`
inserts a *single* document into a
collection.

This example inserts one document into `inventory`. If the document 
does not specify `_id`, MongoDB adds one. 
See write-op-insert-behavior.

(Code example not available offline: /driver-examples/shell_examples_spec.rb)

Upon successful insert, the
`insert_one()`
method returns an instance of
`Mongo::Operation::Result`, whose
`inserted_id` attribute contains the `_id` of the newly
inserted document.

To retrieve the document that you just inserted, query the collection:

(Code example not available offline: /driver-examples/shell_examples_spec.rb)

## Insert a Single Document

`collection.insertOne()`
inserts a *single* document into a
collection.

This example inserts one document into `inventory`. 
If the document does not specify `_id`, MongoDB adds one. 
See write-op-insert-behavior.

(Code example not available offline: /driver-examples/DocumentationExampleSpec.scala)

Upon successful insert, the
`collection.insertOne()`
method returns an instance of
`collection.insertOne().results();` whose
`inserted_id` attribute contains the `_id` of the newly
inserted document.

To retrieve the document that you just inserted, query the collection:

(Code example not available offline: /driver-examples/DocumentationExampleSpec.scala)

## Insert a Single Document

`IMongoCollection.InsertOne()`
inserts a *single* document into a
collection.

This example inserts one document into `inventory`. 
If the document does not specify `_id`, MongoDB adds one. 
See write-op-insert-behavior.

```csharp
var document = new BsonDocument
{
    { "item", "canvas" },
    { "qty", 100 },
    { "tags", new BsonArray { "cotton" } },
    { "size", new BsonDocument { { "h", 28 }, { "w", 35.5 }, { "uom", "cm" } } }
};
collection.InsertOne(document);
```

To retrieve the document that you just inserted, query the collection:

```csharp
var filter = Builders<BsonDocument>.Filter.Eq("item", "canvas");
var result = collection.Find(filter).ToList();
```

## Insert a Single Document

The following example inserts a new document into the
`inventory` collection. If the document does not specify
an `_id` field, the C driver adds the `_id` field
with an ObjectId value to the new document. For more information, see
write-op-insert-behavior.

(Code example not available offline: /driver-examples/test-mongoc-sample-commands.c)

[mongoc_collection_insert_one](https://mongoc.org/libmongoc/current/mongoc_collection_insert_one.html) 
returns `true` if successful, or returns `false` and sets error if 
there are invalid arguments or a server or network error.

To retrieve the document that you just inserted, query the collection:

(Code example not available offline: /driver-examples/test-mongoc-sample-commands.c)

## Insert a Single Document

`Collection.InsertOne`
inserts a *single* document into a
collection.

This example inserts one document into `inventory`. 
If the document does not specify `_id`, MongoDB adds one. 
See write-op-insert-behavior.

(Code example not available offline: /driver-examples/go_examples.go)

`Collection.InsertOne`
function returns an instance of
`InsertOneResult` whose
`InsertedID` attribute contains the `_id` of the newly
inserted document.

To retrieve the document that you just inserted, query the collection:

(Code example not available offline: /driver-examples/go_examples.go)

## Insert a Single Document

To insert a single document using MongoDB Compass:

1. Navigate to the collection you wish to insert the document
   into:

   a. In the left-hand MongoDB Compass navigation pane, click
      the database to which your target collection belongs.
   #. From the database view, click the target collection name.

#. Click the Add Data button, then click Insert document:

   (Figure: /images/compass-insert-button-new.png)

#. Paste in your document. For example, you can paste the following code into Compass
   to insert a `canvas` document into the `inventory` collection:

   ```json
   {
     "item": "canvas",
     "qty": 100,
     "tags": ["cotton"],
     "size": {
       "h": 28,
       "w": 35.5,
       "uom": "cm"
     }
   }  
   ```

#. Click Insert.

The following example inserts a new document into the test.inventory collection:

(Figure: /images/compass-insert-document-inventory-new.png)

**Note:**

MongoDB Compass generates the `_id` field and its value
automatically. The generated
ObjectId consists of a
unique randomly generated hexadecimal value.

You can change this value prior to inserting your document
so long as it remains unique and is a valid `ObjectId`.
For more information on the `_id` field, see
_id Field.

To retrieve the document that you just inserted, query the collection by specifying a filter in the MongoDB Compass query bar
and clicking Find to execute the query. 

The following filter specifies that MongoDB Compass only return
documents where the `item` field is equal to `canvas`. For more information on the 
MongoDB Compass Query Bar, see Query Bar.

(Figure: /images/compass-query-collection-new.png)

## Insert Multiple Documents

`db.collection.insertMany()` can insert *multiple*
documents into a collection. Pass an
array of documents to the method.

This example inserts multiple documents into `inventory`. 
If documents do not specify `_id`, MongoDB adds one for each document. 
See write-op-insert-behavior.

```javascript
db.movies.insertMany([
   {
      title: "Oppenheimer",
      genres: ["Biography", "Drama", "History"],
      runtime: 180,
      rated: "R",
      year: 2023,
      directors: ["Christopher Nolan"],
      cast: ["Cillian Murphy", "Emily Blunt", "Matt Damon"],
      type: "movie"
   },
   {
      title: "Barbie",
      genres: ["Adventure", "Comedy", "Fantasy"],
      runtime: 114,
      rated: "PG-13",
      year: 2023,
      directors: ["Greta Gerwig"],
      cast: ["Margot Robbie", "Ryan Gosling"],
      type: "movie"
   },
   {
      title: "Poor Things",
      genres: ["Comedy", "Drama", "Romance"],
      runtime: 141,
      rated: "R",
      year: 2023,
      directors: ["Yorgos Lanthimos"],
      cast: ["Emma Stone", "Mark Ruffalo", "Willem Dafoe"],
      type: "movie"
   }
])
```

`insertMany()` returns a document that includes
the newly inserted documents `_id` field values. See the
reference for an example.

To retrieve the inserted documents, query the collection:

```javascript
db.movies.find( { year: 2023 } )
```

## Insert Multiple Documents

`pymongo.collection.Collection.insert_many` can insert
*multiple* documents into a
collection. Pass an iterable of documents to the method.

This example inserts multiple documents into `inventory`. 
If documents do not specify `_id`, MongoDB adds one for each document. 
See write-op-insert-behavior.

(Code example not available offline: /driver-examples/test_examples.py)

`insert_many` returns
an instance of `pymongo.results.InsertManyResult`
whose `inserted_ids` field is a list containing the `_id`
of each newly inserted document.

To retrieve the inserted documents, query the collection:

(Code example not available offline: /driver-examples/test_examples.py)

## Insert Multiple Documents

`motor.motor_asyncio.AsyncIOMotorCollection.insert_many`
can insert *multiple* documents
into a collection. Pass an iterable of documents to the method.

This example inserts multiple documents into `inventory`. 
If documents do not specify `_id`, MongoDB adds one for each document. 
See write-op-insert-behavior.

(Code example not available offline: /driver-examples/test_examples_motor.py)

`insert_many`
returns an instance of `pymongo.results.InsertManyResult`
whose `inserted_ids` field is a list containing the `_id`
of each newly inserted document.

To retrieve the inserted documents, query the collection:

(Code example not available offline: /driver-examples/test_examples_motor.py)

## Insert Multiple Documents

`IMongoCollection.insertMany()`       
can insert *multiple* documents
into a collection. Pass a list of documents to the method.

This example inserts multiple documents into `inventory`. 
If documents do not specify `_id`, MongoDB adds one for each document. 
See write-op-insert-behavior.

(Code example not available offline: /driver-examples/DocumentationSamples.java)

To retrieve the inserted documents, query the collection:

(Code example not available offline: /driver-examples/DocumentationSamples.java)

## Insert Multiple Documents

[com.mongodb.reactivestreams.client.MongoCollection.insertMany](https://mongodb.github.io/mongo-java-driver/{+java-driver-version+}/apidocs/driver-reactive-streams/com/mongodb/reactivestreams/client/MongoCollection.html#insertMany(java.util.List))      
inserts the following documents with the [Java Reactive Streams Driver](https://www.mongodb.com/docs/languages/java/reactive-streams-driver/current/):

```json
{ item: "journal", qty: 25, tags: ["blank", "red"], size: { h: 14, w: 21, uom: "cm" } }
{ item: "mat", qty: 85, tags: ["gray"], size: { h: 27.9, w: 35.5, uom: "cm" } }
{ item: "mousepad", qty: 25, tags: ["gel", "blue"], size: { h: 19, w: 22.85, uom: "cm" } }
```

This example inserts multiple documents into `inventory`. 
If documents do not specify `_id`, MongoDB adds one for each document. 
See write-op-insert-behavior.

(Code example not available offline: /driver-examples/AsyncDocumentationSamples.java)

[com.mongodb.reactivestreams.client.MongoCollection.insertMany](https://mongodb.github.io/mongo-java-driver/{+java-driver-version+}/apidocs/driver-reactive-streams/com/mongodb/reactivestreams/client/MongoCollection.html#insertMany(java.util.List))      
returns a [Publisher](http://www.reactive-streams.org/reactive-streams-1.0.1-javadoc/org/reactivestreams/Publisher.html)
object. The `Publisher` inserts the document into a collection
when subscribers request data.

To retrieve the inserted documents, query the collection:

(Code example not available offline: /driver-examples/AsyncDocumentationSamples.java)

## Insert Multiple Documents

[MongoCollection.insertMany](https://mongodb.github.io/mongo-java-driver/{+java-driver-version+}/apidocs/driver-kotlin-coroutine/mongodb-driver-kotlin-coroutine/com.mongodb.kotlin.client.coroutine/-mongo-collection/insert-many.html)
inserts *multiple* documents
into a collection. Pass a list of documents as a parameter to the method.

This example inserts multiple documents into `inventory`. 
If documents do not specify `_id`, MongoDB adds one for each document. 
See write-op-insert-behavior.

(Code example not available offline: /driver-examples/kotlin_examples.kt)

[MongoCollection.insertMany()](https://mongodb.github.io/mongo-java-driver/{+java-driver-version+}/apidocs/driver-kotlin-coroutine/mongodb-driver-kotlin-coroutine/com.mongodb.kotlin.client.coroutine/-mongo-collection/insert-many.html)
returns an `InsertManyResult` instance. The `insertedIds`
field of `InsertManyResult` contains the `_id` values of the
inserted documents.

To retrieve the inserted documents, query the collection:

(Code example not available offline: /driver-examples/kotlin_examples.kt)

## Insert Multiple Documents

`Collection.insertMany()`
can insert *multiple* documents
into a collection. Pass an array of documents to the method.

This example inserts multiple documents into `inventory`. 
If documents do not specify `_id`, MongoDB adds one for each document. 
See write-op-insert-behavior.

(Code example not available offline: /driver-examples/node_insert.js)

`insertMany()` returns a
promise that provides a `result`. The `result.insertedIds`
field contains an array with the `_id` of each newly inserted
document.

To retrieve the inserted documents, query the collection:

(Code example not available offline: /driver-examples/node_query.js)

## Insert Multiple Documents

`MongoDBCollection::insertMany()`
can insert *multiple* documents into a
collection. Pass an array of documents to the method.

The following example inserts three new documents into the
This example inserts multiple documents into `inventory`. 
If documents do not specify `_id`, MongoDB adds one for each document. 
See write-op-insert-behavior.

(Code example not available offline: /driver-examples/DocumentationExamplesTest.php)

Upon successful insert, the
`insertMany()`
method
returns an instance of
`MongoDBInsertManyResult`
whose
`getInsertedIds()`
method returns the `_id` of each newly inserted document.

To retrieve the inserted documents, query the collection:

(Code example not available offline: /driver-examples/DocumentationExamplesTest.php)

## Insert Multiple Documents

`Mongo::Collection#insert_many()`
can insert *multiple* documents into a
collection. Pass an array of documents to the method.

This example inserts multiple documents into `inventory`. 
If documents do not specify `_id`, MongoDB adds one for each document. 
See write-op-insert-behavior.

(Code example not available offline: /driver-examples/shell_examples_spec.rb)

Upon successful insert, the
`insert_many()` method
returns an instance of
`Mongo::BulkWrite::Result`
whose `inserted_ids` attribute is a list containing the
`_id` of each newly inserted document.

To retrieve the inserted documents, query the collection:

(Code example not available offline: /driver-examples/shell_examples_spec.rb)

## Insert Multiple Documents

`collection.insertMany()<insertMany(documents:Seq[_`
can insert *multiple* documents into a
collection.

This example inserts multiple documents into `inventory`. 
If documents do not specify `_id`, MongoDB adds one for each document. 
See write-op-insert-behavior.

(Code example not available offline: /driver-examples/DocumentationExampleSpec.scala)

Upon successful insert, the
`insertMany()<insertMany(documents:Seq[_`
method returns an [Observable](http://mongodb.github.io/mongo-scala-driver/2.1/reference/observables/) with a type parameter indicating when
the operation has completed or with either a
`com.mongodb.DuplicateKeyException` or
`com.mongodb.MongoException`.

To retrieve the inserted documents, query the collection:

(Code example not available offline: /driver-examples/DocumentationExampleSpec.scala)

## Insert Multiple Documents

`IMongoCollection.InsertMany()`
can insert *multiple* documents
into a collection. Pass an enumerable collection of documents
to the method.

This example inserts multiple documents into `inventory`. 
If documents do not specify `_id`, MongoDB adds one for each document. 
See write-op-insert-behavior.

```csharp
var documents = new BsonDocument[]
{
    new BsonDocument
    {
        { "item", "journal" },
        { "qty", 25 },
        { "tags", new BsonArray { "blank", "red" } },
        { "size", new BsonDocument { { "h", 14 }, { "w", 21 }, {  "uom", "cm"} } }
    },
    new BsonDocument
    {
        { "item", "mat" },
        { "qty", 85 },
        { "tags", new BsonArray { "gray" } },
        { "size", new BsonDocument { { "h", 27.9 }, { "w", 35.5 }, {  "uom", "cm"} } }
    },
    new BsonDocument
    {
        { "item", "mousepad" },
        { "qty", 25 },
        { "tags", new BsonArray { "gel", "blue" } },
        { "size", new BsonDocument { { "h", 19 }, { "w", 22.85 }, {  "uom", "cm"} } }
    },
};
collection.InsertMany(documents);
```

To retrieve the inserted documents, query the collection:

```csharp
var filter = Builders<BsonDocument>.Filter.Empty;
var result = collection.Find(filter).ToList();
```

## Insert Multiple Documents

[mongoc_bulk_operation_insert_with_opts](https://mongoc.org/libmongoc/current/mongoc_bulk_operation_insert_with_opts.html) 
inserts *multiple* documents into a
collection. You must pass an iterable of documents to the method.

This example inserts multiple documents into `inventory`. 
If documents do not specify `_id`, MongoDB adds one for each document. 
See write-op-insert-behavior.

(Code example not available offline: /driver-examples/test-mongoc-sample-commands.c)

[mongoc_bulk_operation_insert_with_opts](https://mongoc.org/libmongoc/current/mongoc_bulk_operation_insert_with_opts.html) 
returns `true` on success, or `false` if passed invalid arguments. 

To retrieve the inserted documents, use 
[mongoc_collection_find_with_opts](https://mongoc.org/libmongoc/current/mongoc_collection_find_with_opts.html) to 
query the collection:

(Code example not available offline: /driver-examples/test-mongoc-sample-commands.c)

Clean up any open resources by calling the following methods, as appropriate:

- [bson_destroy](http://mongoc.org/libbson/current/bson_destroy.html)

- [mongoc_bulk_operation_destroy](https://mongoc.org/libmongoc/current/mongoc_bulk_operation_destroy.html)

- [mongoc_collection_destroy](https://mongoc.org/libmongoc/current/mongoc_collection_destroy)

- [mongoc_cursor_destroy](https://mongoc.org/libmongoc/current/mongoc_cursor_destroy.html),

## Insert Multiple Documents

`Collection.InsertMany`
can insert *multiple* documents into a
collection.

This example inserts multiple documents into `inventory`. 
If documents do not specify `_id`, MongoDB adds one for each document. 
See write-op-insert-behavior.

(Code example not available offline: /driver-examples/go_examples.go)

To retrieve the inserted documents, query the collection:

(Code example not available offline: /driver-examples/go_examples.go)

## Insert Multiple Documents

For instructions on inserting documents using MongoDB Compass, see
Insert Documents. You can paste the following 
documents into the Insert Document dialog in Compass to 
insert multiple `item` documents into the `inventory` collection:

```javascript
[
    { "item": "canvas", "qty": 100, "size": { "h": 28, "w": 35.5, "uom": "cm" }, "status": "A" },
    { "item": "journal", "qty": 25, "size": { "h": 14, "w": 21, "uom": "cm" }, "status": "A" },
    { "item": "mat", "qty": 85, "size": { "h": 27.9, "w": 35.5, "uom": "cm" }, "status": "A" },
    { "item": "mousepad", "qty": 25, "size": { "h": 19, "w": 22.85, "uom": "cm" }, "status": "P" },
    { "item": "notebook", "qty": 50, "size": { "h": 8.5, "w": 11, "uom": "in" }, "status": "P" },
    { "item": "paper", "qty": 100, "size": { "h": 8.5, "w": 11, "uom": "in" }, "status": "D" },
    { "item": "planner", "qty": 75, "size": { "h": 22.85, "w": 30, "uom": "cm" }, "status": "D" },
    { "item": "postcard", "qty": 45, "size": { "h": 10, "w": 15.25, "uom": "cm" }, "status": "A" },
    { "item": "sketchbook", "qty": 80, "size": { "h": 14, "w": 21, "uom": "cm" }, "status": "A" },
    { "item": "sketch pad", "qty": 95, "size": { "h": 22.85, "w": 30.5, "uom": "cm" }, "status": "A" }
]
```

To view the newly inserted documents, specify a filter of `{}` in the 
MongoDB Compass query bar and click Find to view your documents.

(Figure: /images/compass-select-all-new.png)

## Insert Documents in the MongoDB Atlas UI

To insert a document in the MongoDB Atlas UI, complete the following steps.
To learn more about working with documents in the MongoDB Atlas UI, see
Create, View, Update, and Delete Documents.

**Step 1: In the MongoDB Atlas UI, go to the Clusters page for your project.**

a. If it's not already displayed, select the organization that
   contains your desired project from the `office` Organizations menu in the
   navigation bar.

#. If it's not already displayed, select your project
   from the Projects menu in the navigation bar.

#. In the sidebar, click Clusters under 
   the Database heading.

   The [Clusters](https://cloud.mongodb.com/go?l=https%3A%2F%2Fcloud.mongodb.com%2Fv2%2F%3Cproject%3E%23%2Fclusters) page displays.

**Step 2: Navigate to the collection**

a. For the cluster to which you want to add documents,
   click Browse Collections.
#. In the left navigation pane, select the database.
#. In the left navigation pane, select the collection.

**Step 3: Add the documents**

a. Click Insert Document.
#. Click the {} icon, which opens the JSON view.
#. Paste the document array into the text entry field. For
   example, the following entry creates four documents, each of
   which contain three fields:

   ```
   [
      { "prodId": 100, "price": 20, "quantity": 125 },
      { "prodId": 101, "price": 10, "quantity": 234 },
      { "prodId": 102, "price": 15, "quantity": 432 },
      { "prodId": 103, "price": 17, "quantity": 320 }
   ]
   ```

**Step 4: Click Insert.**

MongoDB Atlas adds the documents to the collection.

## Insert Behavior

### Collection Creation

If the collection does not currently exist, insert operations
create the collection.

### `_id` Field

In MongoDB, each document stored in a standard collection requires a unique
_id field that acts as a primary key. If an inserted
document omits the `_id` field, the MongoDB driver automatically
generates an objectid for the `_id` field.

This also applies to documents inserted through update
operations with upsert: true.

**Note:** Atomicity and Write Acknowledgement

MongoDB write operations are atomic on the level of a single document. 
For more information, see transactions-write-atomicity. 

You can also use write concerns to specify the level of acknowledgment 
requested from MongoDB for write operations. For more information, 
see write-concern.

**See also:**

- `db.collection.insertOne()`

- `db.collection.insertMany()`

- Collection Methods

**See also:**

- `pymongo.collection.Collection.insert_one`

- `pymongo.collection.Collection.insert_many`

- additional-inserts

**See also:**

- `motor.motor_asyncio.AsyncIOMotorCollection.insert_one`

- `motor.motor_asyncio.AsyncIOMotorCollection.insert_many`

- additional-inserts

**See also:**

- `IMongoCollection.insertOne()`

- `IMongoCollection.insertMany()`

- Additional Java Synchronous Driver Write Examples

**See also:**

- [com.mongodb.reactivestreams.client.MongoCollection.insertOne](https://mongodb.github.io/mongo-java-driver/{+java-driver-version+}/apidocs/driver-reactive-streams/com/mongodb/reactivestreams/client/MongoCollection.html#insertOne(TDocument))

- [com.mongodb.reactivestreams.client.MongoCollection.insertMany](https://mongodb.github.io/mongo-java-driver/{+java-driver-version+}/apidocs/driver-reactive-streams/com/mongodb/reactivestreams/client/MongoCollection.html#insertMany(java.util.List))

- [Java Reactive Streams Driver](https://www.mongodb.com/docs/languages/java/reactive-streams-driver/current/)

**See also:**

- [MongoCollection.insertOne](https://mongodb.github.io/mongo-java-driver/{+java-driver-version+}/apidocs/driver-kotlin-coroutine/mongodb-driver-kotlin-coroutine/com.mongodb.kotlin.client.coroutine/-mongo-collection/insert-one.html)

- [MongoCollection.insertMany](https://mongodb.github.io/mongo-java-driver/{+java-driver-version+}/apidocs/driver-kotlin-coroutine/mongodb-driver-kotlin-coroutine/com.mongodb.kotlin.client.coroutine/-mongo-collection/insert-many.html)

- `Kotlin Driver Write Operation Examples`

**See also:**

- `Collection.insertOne()`

- `Collection.insertMany()`

- additional-inserts

**See also:**

- `MongoDBCollection::insertOne()`

- `MongoDBCollection::insertMany()`

- additional-inserts

**See also:**

- `Mongo::Collection#insert_one()`

- `Mongo::Collection#insert_many()`

**See also:**

- `collection.insertOne()`

- `collection.insertMany()<insertMany(documents:Seq[_`

- additional-inserts

**See also:**

- `IMongoCollection.InsertOne()`

- `IMongoCollection.InsertMany()`

- additional-inserts

**See also:**

- [mongoc_bulk_operation_insert_with_opts](https://mongoc.org/libmongoc/current/mongoc_bulk_operation_insert_with_opts.html) 

- additional-inserts

**See also:**

- `Collection.InsertOne`

- `Collection.InsertMany`

- additional-inserts
