<!-- Converted from tutorial/insert-documents.txt (reStructuredText). Includes are inlined. -->

# Insert Documents

----------

→ Use the **Select your language** drop-down menu in the
upper-right to set the language of the following examples or select
MongoDB Compass.

----------

This page provides examples of insert operations in MongoDB.

You can insert documents in MongoDB by using the following
methods:

- Your programming language's driver.
- The MongoDB Atlas UI. To learn more, see 
  insert-documents-atlas.
- `MongoDB Compass`.

**Note:** Creating a Collection

If the collection does not currently exist, insert operations will
create the collection.

## Insert Documents in the MongoDB Atlas UI

To insert a document in the MongoDB Atlas UI, complete the following steps.
To learn more about working with documents in the MongoDB Atlas UI, see
Create, View, Update, and Delete Documents.

**Step 1: In the MongoDB Atlas UI, go to the Clusters page for your project.**

**Warning:** Navigation Improvements In Progress

We're currently rolling out a new and improved navigation 
experience. If the following steps don't match your view in the 
Atlas UI, see `the preview Atlas documentation`.

a. If it's not already displayed, select the organization that
   contains your desired project from the `office` Organizations menu in the
   navigation bar.

#. If it's not already displayed, select your project
   from the Projects menu in the navigation bar.

#. If it's not already displayed, click Clusters in the 
   sidebar.

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

## Insert a Single Document

**shell:**

`db.collection.insertOne()` inserts a *single*
document into a collection.

The following example inserts a new document into the
`inventory` collection. If the document does not specify
an `_id` field, MongoDB adds the `_id` field with an
ObjectId value to the new document. See
write-op-insert-behavior.

**compass:**

To insert a single document using MongoDB Compass:

1. Navigate to the collection you wish to insert the document
   into:

   a. In the left-hand MongoDB Compass navigation pane, click
      the database to which your target collection belongs.

   b. From the database view, click the target collection name.

2. Click the Insert Document button:

   (Figure: /images/compass-insert-button.png)

3. For each field in the document, select the field type and
   fill in the field name and value. Add fields by clicking
   the last line number, then clicking
   Add Field After ...

   - For `Object` types, add nested fields by clicking the
     last field's number and selecting
     Add Field After ...

   - For `Array` types, add additional elements to the array
     by clicking the last element's line number and selecting
     Add Array Element After ...

4. Once all fields have been filled out, click Insert.

The following example inserts a new document into the
`test.inventory` collection:

**python:**

`pymongo.collection.Collection.insert_one` inserts a
*single* document into a
collection.

The following example inserts a new document into the
`inventory` collection. If the document does not specify
an `_id` field, the PyMongo driver adds the `_id` field
with an ObjectId value to the new document. See
write-op-insert-behavior.

**motor:**

`motor.motor_asyncio.AsyncIOMotorCollection.insert_one` inserts a
*single* document into a
collection.

The following example inserts a new document into the
`inventory` collection. If the document does not specify
an `_id` field, the Motor driver adds the `_id` field
with an ObjectId value to the new document. See
write-op-insert-behavior.

**java-sync:**

com.mongodb.client.MongoCollection.insertOne_
inserts a *single* document into
a collection.

The following example inserts a new document into the
`inventory` collection. If the document does not specify
an `_id` field, the driver adds the `_id` field with an
ObjectId value to the new document. See
write-op-insert-behavior.

**java-async:**

[com.mongodb.reactivestreams.client.MongoCollection.insertOne](http://mongodb.github.io/mongo-java-driver-reactivestreams/1.6/javadoc/com/mongodb/reactivestreams/client/MongoCollection.html#insertOne(TDocument))
inserts a *single* document into
a collection with the [Java Reactive Streams Driver](http://mongodb.github.io/mongo-java-driver-reactivestreams/1.6/):

```json
{ item: "canvas", qty: 100, tags: ["cotton"], size: { h: 28, w: 35.5, uom: "cm" } }
```

The following example inserts the document above into the
`inventory` collection. If the document does not specify
an `_id` field, the driver adds the `_id` field with an
ObjectId value to the new document. See
write-op-insert-behavior.

**nodejs:**

`Collection.insertOne()`
inserts a *single* document into a
collection.

The following example inserts a new document into the
`inventory` collection. If the document does not specify
an `_id` field, the Node.js driver adds the `_id` field
with an ObjectId value to the new document. See
write-op-insert-behavior.

**php:**

`MongoDBCollection::insertOne()`
inserts a *single* document into a
collection.

The following example inserts a new document into the
`inventory` collection. If the document does not specify
an `_id` field, the PHP driver adds the `_id` field
with an ObjectId value to the new document. See
write-op-insert-behavior.

**ruby:**

`Mongo::Collection#insert_one()`
inserts a *single* document into a
collection.

The following example inserts a new document into the
`inventory` collection. If the document does not specify
an `_id` field, the Ruby driver adds the `_id` field
with an ObjectId value to the new document. See
write-op-insert-behavior.

**scala:**

`collection.insertOne()`
inserts a *single* document into a
collection.

The following example inserts a new document into the
`inventory` collection. If the document does not specify
an `_id` field, the Scala driver adds the `_id` field
with an ObjectId value to the new document. See
write-op-insert-behavior.

**csharp:**

`IMongoCollection.InsertOne()`
inserts a *single* document into a
collection.

The following example inserts a new document into the
`inventory` collection. If the document does not specify
an `_id` field, the C# driver adds the `_id` field
with an ObjectId value to the new document. See
write-op-insert-behavior.

**go:**

`Collection.InsertOne`
inserts a *single* document into a
collection.

The following example inserts a new document into the
`inventory` collection. If the document does not specify
an `_id` field, the driver adds the `_id` field
with an ObjectId value to the new document. See
write-op-insert-behavior.

tabs:
  - id: shell
    content: |

      ```javascript
      db.inventory.insertOne(
         { item: "canvas", qty: 100, tags: ["cotton"], size: { h: 28, w: 35.5, uom: "cm" } }
      )
      ```

  - id: compass
    content: |
      (Figure: /images/compass-insert-document-inventory.png)

  - id: python
    content: |

      (Code example not available offline: /driver-examples/test_examples.py)

  - id: motor
    content: |

      (Code example not available offline: /driver-examples/test_examples_motor.py)

  - id: java-sync
    content: |

      (Code example not available offline: /driver-examples/DocumentationSamples.java)

  - id: java-async
    content: |

      (Code example not available offline: /driver-examples/AsyncDocumentationSamples.java)

  - id: nodejs
    content: |

      (Code example not available offline: /driver-examples/node_insert.js)

  - id: php
    content: |

      (Code example not available offline: /driver-examples/DocumentationExamplesTest.php)

  - id: ruby
    content: |

      (Code example not available offline: /driver-examples/shell_examples_spec.rb)

  - id: scala
    content: |

      (Code example not available offline: /driver-examples/DocumentationExampleSpec.scala)

  - id: csharp
    content: |

      (Code example not available offline: /driver-examples/DocumentationExamples.cs)

  - id: go
    content: |
      (Code example not available offline: /driver-examples/go_examples.go)

**shell:**

`insertOne()` returns a document that
includes the newly inserted document's `_id` field value. For
an example of a return document, see
db.collection.insertOne() reference.

**compass:**

**Note:**

MongoDB Compass generates the `_id` field and its value
automatically. The generated
ObjectId consists of a
unique randomly generated hexadecimal value.

You can change this value prior to inserting your document
so long as it remains unique and is a valid `ObjectId`.
For more information on the `_id` field, see
_id Field.

**python:**

`insert_one` returns an
instance of `pymongo.results.InsertOneResult` whose
`inserted_id` field contains the `_id` of the newly
inserted document.

**motor:**

`insert_one` returns an
instance of `pymongo.results.InsertOneResult` whose
`inserted_id` field contains the `_id` of the newly
inserted document.

**java-sync:**

[com.mongodb.client.MongoCollection.insertOne](https://mongodb.github.io/mongo-java-driver/4.11/apidocs/mongodb-driver-sync/com/mongodb/client/MongoCollection.html#insertOne(TDocument)) returns an
instance of [InsertOneResult](https://mongodb.github.io/mongo-java-driver/4.11/apidocs/mongodb-driver-core/com/mongodb/client/result/InsertOneResult.html).
You can access the `_id` field of the inserted document by
calling the [getInsertedId()](https://mongodb.github.io/mongo-java-driver/4.11/apidocs/mongodb-driver-core/com/mongodb/client/result/InsertOneResult.html#getInsertedId()) method on the result.

**nodejs:**

`insertOne()` returns a
promise that provides a `result`.  The `result.insertedId`
promise contains the `_id` of the newly inserted document.

**php:**

Upon successful insert, the
`insertOne()`
method returns an instance of
`MongoDBInsertOneResult`
whose
`getInsertedId()`
method returns the `_id` of the newly inserted document.

**ruby:**

Upon successful insert, the
`insert_one()`
method returns an instance of
`Mongo::Operation::Result`, whose
`inserted_id` attribute contains the `_id` of the newly
inserted document.

**scala:**

Upon successful insert, the
`collection.insertOne()`
method returns an instance of
`collection.insertOne().results();` whose
`inserted_id` attribute contains the `_id` of the newly
inserted document.

**csharp:**

**go:**

`Collection.InsertOne`
function returns an instance of
`InsertOneResult` whose
`InsertedID` attribute contains the `_id` of the newly
inserted document.

To retrieve the document that you just inserted, query the collection:

tabs:
  - id: shell
    content: |

      ```javascript
      db.inventory.find( { item: "canvas" } )
      ```

  - id: compass
    content: |
      (Figure: /images/compass-query-collection.png)

      Specify a filter in the MongoDB Compass query bar and click
      Find to execute the query.

      The above filter specifies that MongoDB Compass only return
      documents where the `item` field is equal to `canvas`.

      For more information on the MongoDB Compass Query Bar, see the
      Compass Query Bar
      documentation.

  - id: python
    content: |

      (Code example not available offline: /driver-examples/test_examples.py)

  - id: motor
    content: |

      (Code example not available offline: /driver-examples/test_examples_motor.py)

  - id: java-sync
    content: |

      (Code example not available offline: /driver-examples/DocumentationSamples.java)

  - id: java-async
    content: |

      (Code example not available offline: /driver-examples/AsyncDocumentationSamples.java)

  - id: nodejs
    content: |
      (Code example not available offline: /driver-examples/node_insert.js)

  - id: php
    content: |

      (Code example not available offline: /driver-examples/DocumentationExamplesTest.php)

  - id: ruby
    content: |

      (Code example not available offline: /driver-examples/shell_examples_spec.rb)

  - id: scala
    content: |

      (Code example not available offline: /driver-examples/DocumentationExampleSpec.scala)

  - id: csharp
    content: |

      (Code example not available offline: /driver-examples/DocumentationExamples.cs)

  - id: go
    content: |
      (Code example not available offline: /driver-examples/go_examples.go)

## Insert Multiple Documents

----------

→ Use the **Select your language** drop-down menu in the
upper-right to set the language of the examples on this page.

----------

**shell:**

`db.collection.insertMany()` can insert *multiple*
documents into a collection. Pass an
array of documents to the method.

The following example inserts three new documents into the
`inventory` collection. If the documents do not specify an
`_id` field, MongoDB adds the `_id` field with an ObjectId
value to each document. See write-op-insert-behavior.

**compass:**

**python:**

`pymongo.collection.Collection.insert_many` can insert
*multiple* documents into a
collection. Pass an iterable of documents to the method.

The following example inserts three new documents into the
`inventory` collection. If the documents do not specify an
`_id` field, the PyMongo driver adds the `_id` field with
an ObjectId value to each document. See write-op-insert-behavior.

**motor:**

`motor.motor_asyncio.AsyncIOMotorCollection.insert_many`
can insert *multiple* documents
into a collection. Pass an iterable of documents to the method.

The following example inserts three new documents into the
`inventory` collection. If the documents do not specify an
`_id` field, the PyMongo driver adds the `_id` field with
an ObjectId value to each document. See write-op-insert-behavior.

**java-sync:**

com.mongodb.client.MongoCollection.insertMany_
can insert *multiple* documents
into a collection. Pass a list of documents to the method.

The following example inserts three new documents into the
`inventory` collection. If the documents do not specify an
`_id` field, the driver adds the `_id` field with
an ObjectId value to each document. See write-op-insert-behavior.

**java-async:**

[com.mongodb.reactivestreams.client.MongoCollection.html.insertMany](http://mongodb.github.io/mongo-java-driver-reactivestreams/1.6/javadoc/com/mongodb/reactivestreams/client/MongoCollection.html#insertMany(java.util.List))
inserts the following documents with the [Java Reactive Streams Driver](http://mongodb.github.io/mongo-java-driver-reactivestreams/1.6/):

```json
{ item: "journal", qty: 25, tags: ["blank", "red"], size: { h: 14, w: 21, uom: "cm" } }
{ item: "mat", qty: 85, tags: ["gray"], size: { h: 27.9, w: 35.5, uom: "cm" } }
{ item: "mousepad", qty: 25, tags: ["gel", "blue"], size: { h: 19, w: 22.85, uom: "cm" } }
```

The following example inserts three new documents into the
`inventory` collection. If the documents do not specify an
`_id` field, the driver adds the `_id` field with
an ObjectId value to each document. See write-op-insert-behavior.

**nodejs:**

`Collection.insertMany()`
can insert *multiple* documents
into a collection. Pass an array of documents to the method.

The following example inserts three new documents into the
`inventory` collection. If the documents do not specify an
`_id` field, the Node.js driver adds the `_id` field with
an ObjectId value to each document. See
write-op-insert-behavior.

**php:**

`MongoDBCollection::insertMany()`
can insert *multiple* documents into a
collection. Pass an array of documents to the method.

The following example inserts three new documents into the
`inventory` collection. If the documents do not specify an
`_id` field, the PHP driver adds the `_id` field with
an ObjectId value to each document. See write-op-insert-behavior.

**ruby:**

`Mongo::Collection#insert_many()`
can insert *multiple* documents into a
collection. Pass an array of documents to the method.

The following example inserts three new documents into the
`inventory` collection. If the documents do not specify an
`_id` field, the Ruby driver adds the `_id` field with
an ObjectId value to each document. See write-op-insert-behavior.

**scala:**

`collection.insertMany()<insertMany(documents:Seq[_`
can insert *multiple* documents into a
collection.

The following example inserts three new documents into the
`inventory` collection. If the documents do not specify an
`_id` field, the Scala driver adds the `_id` field with
an ObjectId value to each document. See write-op-insert-behavior.

**csharp:**

`IMongoCollection.InsertMany()`
can insert *multiple* documents
into a collection. Pass an enumerable collection of documents
to the method.

The following example inserts three new documents into the
`inventory` collection. If the documents do not specify an
`_id` field, the driver adds the `_id` field with
an ObjectId value to each document. See write-op-insert-behavior.

**go:**

`Collection.InsertMany`
can insert *multiple* documents into a
collection.

The following example inserts three new documents into the
`inventory` collection. If the documents do not specify an
`_id` field, the driver adds the `_id` field with
an ObjectId value to each document. See write-op-insert-behavior.

tabs:
  - id: shell
    content: |

      ```javascript
      db.inventory.insertMany([
         { item: "journal", qty: 25, tags: ["blank", "red"], size: { h: 14, w: 21, uom: "cm" } },
         { item: "mat", qty: 85, tags: ["gray"], size: { h: 27.9, w: 35.5, uom: "cm" } },
         { item: "mousepad", qty: 25, tags: ["gel", "blue"], size: { h: 19, w: 22.85, uom: "cm" } }
      ])
      ```

  - id: compass
    content: |

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

      For instructions on inserting documents using MongoDB Compass, see
      Insert Documents.

  - id: python
    content: |

      (Code example not available offline: /driver-examples/test_examples.py)

  - id: motor
    content: |

      (Code example not available offline: /driver-examples/test_examples_motor.py)

  - id: java-sync
    content: |

      (Code example not available offline: /driver-examples/DocumentationSamples.java)

  - id: java-async
    content: |

      (Code example not available offline: /driver-examples/AsyncDocumentationSamples.java)

  - id: nodejs
    content: |
      (Code example not available offline: /driver-examples/node_insert.js)

  - id: php
    content: |

      (Code example not available offline: /driver-examples/DocumentationExamplesTest.php)

  - id: ruby
    content: |

      (Code example not available offline: /driver-examples/shell_examples_spec.rb)

  - id: scala
    content: |

      (Code example not available offline: /driver-examples/DocumentationExampleSpec.scala)

  - id: csharp
    content: |

      (Code example not available offline: /driver-examples/DocumentationExamples.cs)

  - id: go
    content: |
      (Code example not available offline: /driver-examples/go_examples.go)

**shell:**

`insertMany()` returns a document that includes
the newly inserted documents `_id` field values. See the
reference for an example.

To retrieve the inserted documents, query the collection:

**python:**

`insert_many` returns
an instance of `pymongo.results.InsertManyResult`
whose `inserted_ids` field is a list containing the `_id`
of each newly inserted document.

To retrieve the inserted documents, query the collection:

**motor:**

`insert_many`
returns an instance of `pymongo.results.InsertManyResult`
whose `inserted_ids` field is a list containing the `_id`
of each newly inserted document.

To retrieve the inserted documents, query the collection:

**java-sync:**

To retrieve the inserted documents, query the collection:

**java-async:**

[com.mongodb.reactivestreams.client.MongoCollection.html.insertMany](http://mongodb.github.io/mongo-java-driver-reactivestreams/1.6/javadoc/com/mongodb/reactivestreams/client/MongoCollection.html#insertMany(java.util.List))
returns a [Publisher](http://www.reactive-streams.org/reactive-streams-1.0.1-javadoc/org/reactivestreams/Publisher.html)
object. The `Publisher` inserts the document into a collection
when subscribers request data.

To retrieve the inserted documents, query the collection:

**nodejs:**

`insertMany()` returns a
promise that provides a `result`. The `result.insertedIds`
field contains an array with the `_id` of each newly inserted
document.

To retrieve the inserted documents, query the collection:

**php:**

Upon successful insert, the
`insertMany()`
method
returns an instance of
`MongoDBInsertManyResult`
whose
`getInsertedIds()`
method returns the `_id` of each newly inserted document.

To retrieve the inserted documents, query the collection:

**ruby:**

Upon successful insert, the
`insert_many()` method
returns an instance of
`Mongo::BulkWrite::Result`
whose `inserted_ids` attribute is a list containing the
`_id` of each newly inserted document.

To retrieve the inserted documents, query the collection:

**scala:**

Upon successful insert, the
`insertMany()<insertMany(documents:Seq[_`
method returns an [Observable](http://mongodb.github.io/mongo-scala-driver/2.1/reference/observables/) with a type parameter indicating when
the operation has completed or with either a
`com.mongodb.DuplicateKeyException` or
`com.mongodb.MongoException`.

To retrieve the inserted documents, query the collection:

**csharp:**

To retrieve the inserted documents, query the collection:

**go:**

To retrieve the inserted documents, query the collection:

tabs:
  - id: shell
    content: |

      ```javascript
      db.inventory.find( {} )
      ```

  - id: compass
    content: |

      (Figure: /images/compass-select-all.png)

  - id: python
    content: |

      (Code example not available offline: /driver-examples/test_examples.py)

  - id: motor
    content: |

      (Code example not available offline: /driver-examples/test_examples_motor.py)

  - id: java-sync
    content: |

      (Code example not available offline: /driver-examples/DocumentationSamples.java)

  - id: java-async
    content: |

      (Code example not available offline: /driver-examples/AsyncDocumentationSamples.java)

  - id: nodejs
    content: |
      (Code example not available offline: /driver-examples/node_query.js)

  - id: php
    content: |

      (Code example not available offline: /driver-examples/DocumentationExamplesTest.php)

  - id: ruby
    content: |

      (Code example not available offline: /driver-examples/shell_examples_spec.rb)

  - id: scala
    content: |

      (Code example not available offline: /driver-examples/DocumentationExampleSpec.scala)

  - id: csharp
    content: |

      (Code example not available offline: /driver-examples/DocumentationExamples.cs)

  - id: go
    content: |
      (Code example not available offline: /driver-examples/go_examples.go)

## Insert Behavior

### Collection Creation

If the collection does not currently exist, insert operations will
create the collection.

### `_id` Field

In MongoDB, each document stored in a standard collection requires a unique
_id field that acts as a primary key. If an inserted
document omits the `_id` field, the MongoDB driver automatically
generates an objectid for the `_id` field.

This also applies to documents inserted through update
operations with upsert: true.

### Atomicity

All write operations in MongoDB are atomic on the level of a single
document. For more information on MongoDB and atomicity, see
/core/write-operations-atomicity

### Write Acknowledgement

With write concerns, you can specify the level of acknowledgment
requested from MongoDB for write operations. For details, see
/reference/write-concern.

**shell:**

**See also:**

- `db.collection.insertOne()`

- `db.collection.insertMany()`

- additional-inserts

**python:**

**See also:**

- `pymongo.collection.Collection.insert_one`

- `pymongo.collection.Collection.insert_many`

- additional-inserts

**motor:**

**See also:**

- `motor.motor_asyncio.AsyncIOMotorCollection.insert_one`

- `motor.motor_asyncio.AsyncIOMotorCollection.insert_many`

- additional-inserts

**java-sync:**

**See also:**

- com.mongodb.client.MongoCollection.insertOne_

- com.mongodb.client.MongoCollection.insertMany_

- Additional Java Synchronous Driver Write Examples

**java-async:**

**See also:**

- [com.mongodb.reactivestreams.client.MongoCollection.insertOne](http://mongodb.github.io/mongo-java-driver-reactivestreams/1.6/javadoc/com/mongodb/reactivestreams/client/MongoCollection.html#insertOne(TDocument))

- [com.mongodb.reactivestreams.client.MongoCollection.html.insertMany](http://mongodb.github.io/mongo-java-driver-reactivestreams/1.6/javadoc/com/mongodb/reactivestreams/client/MongoCollection.html#insertMany(java.util.List))

- [Java Reactive Streams Driver Quick Tour](http://mongodb.github.io/mongo-java-driver-reactivestreams/1.6/getting-started/quick-tour/)

**nodejs:**

**See also:**

- `Collection.insertOne()`

- `Collection.insertMany()`

- additional-inserts

**php:**

**See also:**

- `MongoDBCollection::insertOne()`

- `MongoDBCollection::insertMany()`

- additional-inserts

**ruby:**

**See also:**

- `Mongo::Collection#insert_one()`

- `Mongo::Collection#insert_many()`

**scala:**

**See also:**

- `collection.insertOne()`

- `collection.insertMany()<insertMany(documents:Seq[_`

- additional-inserts

**csharp:**

**See also:**

- `IMongoCollection.InsertOne()`

- `IMongoCollection.InsertMany()`

- additional-inserts

**go:**

**See also:**

- `Collection.InsertOne`

- `Collection.InsertMany`

- additional-inserts
