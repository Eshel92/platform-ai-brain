<!-- Converted from tutorial/update-documents.txt (reStructuredText). Includes are inlined. -->

# Update Documents

In MongoDB, an Update operation consists of adding, removing, or modifying
fields in one or more documents. This page provides examples.

You can update documents in MongoDB using the following methods:

- Your programming language's driver
- The MongoDB Atlas UI (see update-documents-atlas-ui)
- `MongoDB Compass`
- An aggregation pipeline (see Update a Document with Aggregation Pipeline)

----------

→ Use the **Select your language** drop-down menu in the
upper-right to set the language of the following examples.

----------

   `inventory` collection. Connect to a test database in your MongoDB
   instance then create the `inventory` collection:

**shell:**

This page uses the following `mongosh` methods:

- `db.collection.updateOne(<filter>, <update>, <options>)`

- `db.collection.updateMany(<filter>, <update>, <options>)`

- `db.collection.replaceOne(<filter>, <update>, <options>)`

**compass:**

This page uses MongoDB Compass to
update the documents.

The examples on this page use the `inventory` collection.
Populate the `inventory` collection with the following
documents:

**c:**

This page uses the following [MongoDB C Driver](https://mongoc.org/libmongoc/current/index.html)
methods:

- [mongoc_collection_update_one](https://mongoc.org/libmongoc/current/mongoc_collection_update_one.html)
- [mongoc_collection_replace_one](https://mongoc.org/libmongoc/current/mongoc_collection_replace_one.html)

The examples on this page use the

**python:**

This page uses the following
[PyMongo](https://pymongo.readthedocs.io/en/stable/index.html)
Python driver methods:

- `pymongo.collection.Collection.update_one`

- `pymongo.collection.Collection.update_many`

- `pymongo.collection.Collection.replace_one`

The examples on this page use the

**motor:**

This page uses the
following [Motor](https://motor.readthedocs.io/en/stable/)
driver methods:

- `motor.motor_asyncio.AsyncIOMotorCollection.update_one`

- `motor.motor_asyncio.AsyncIOMotorCollection.update_many`

- `motor.motor_asyncio.AsyncIOMotorCollection.replace_one`

The examples on this page use the

**java-sync:**

This page uses the
following Java Synchronous Driver methods:

- com.mongodb.client.MongoCollection.updateOne_

- com.mongodb.client.MongoCollection.updateMany_

- com.mongodb.client.MongoCollection.replaceOne_

The examples on this page use the

**java-async:**

This page uses the
following [Java Reactive Streams Driver](http://mongodb.github.io/mongo-java-driver-reactivestreams/1.6/) methods:

- [com.mongodb.reactivestreams.client.MongoCollection.updateOne](http://mongodb.github.io/mongo-java-driver-reactivestreams/1.6/javadoc/com/mongodb/reactivestreams/client/MongoCollection.html#updateOne(org.bson.conversions.Bson,%20org.bson.conversions.Bson))

- [com.mongodb.reactivestreams.client.MongoCollection.updateMany](http://mongodb.github.io/mongo-java-driver-reactivestreams/1.6/javadoc/com/mongodb/reactivestreams/client/MongoCollection.html#updateMany(org.bson.conversions.Bson,%20org.bson.conversions.Bson))

- [com.mongodb.reactivestreams.client.MongoCollection.replaceOne](http://mongodb.github.io/mongo-java-driver-reactivestreams/1.6/javadoc/com/mongodb/reactivestreams/client/MongoCollection.html#replaceOne(org.bson.conversions.Bson,%20TDocument))

The examples on this page use the

**kotlin-coroutine:**

This page uses the
following `Kotlin Coroutine Driver` methods:

- [MongoCollection.updateOne()](https://mongodb.github.io/mongo-java-driver/{+java-driver-version+}/apidocs/driver-kotlin-coroutine/mongodb-driver-kotlin-coroutine/com.mongodb.kotlin.client.coroutine/-mongo-collection/update-one.html)
- [MongoCollection.updateMany()](https://mongodb.github.io/mongo-java-driver/{+java-driver-version+}/apidocs/driver-kotlin-coroutine/mongodb-driver-kotlin-coroutine/com.mongodb.kotlin.client.coroutine/-mongo-collection/update-many.html)
- [MongoCollection.replaceOne()](https://mongodb.github.io/mongo-java-driver/{+java-driver-version+}/apidocs/driver-kotlin-coroutine/mongodb-driver-kotlin-coroutine/com.mongodb.kotlin.client.coroutine/-mongo-collection/replace-one.html)

The examples on this page use the

**Note:**

The examples in this guide use the `Updates` and `Filters` builder factory classes. These classes
provide helper methods to construct update documents and filter documents. To learn more about the
`Updates` builder, see the kotlin-updates-builders guide. To learn more about the `Filters`
builder, see the `Filters Builders` guide.

**nodejs:**

This page uses the
following `MongoDB Node.js Driver` methods:

- `Collection.updateOne()`

- `Collection.updateMany()`

- `Collection.replaceOne()`

The examples on this page use the

**php:**

This page uses the following  [MongoDB PHP Library](https://www.mongodb.com/docs/php-library/current/) methods:

- `MongoDBCollection::updateOne()`

- `MongoDBCollection::updateMany()`

- `MongoDBCollection::replaceOne()`

The examples on this page use the

**ruby:**

This page uses the following `MongoDB Ruby Driver` methods:

- `Mongo::Collection#update_one()`

- `Mongo::Collection#update_many()`

- `Mongo::Collection#replace_one()`

The examples on this page use the

**scala:**

This page uses the following  [MongoDB Scala Driver](http://mongodb.github.io/mongo-scala-driver/) methods:

- `collection.updateOne()`

- `collection.updateMany()`

- `collection.replaceOne()`

The examples on this page use the

**csharp:**

This page uses the following `MongoDB .NET/C# Driver` methods:

- `IMongoCollection.UpdateOne()`

- `IMongoCollection.UpdateMany()`

- `IMongoCollection.ReplaceOne()`

The examples on this page use the

**go:**

This page uses the following `MongoDB Go Driver` functions:

- `Collection.UpdateOne`

- `Collection.UpdateMany`

- `Collection.ReplaceOne`

The examples on this page use the

tabs:
  - id: shell
    content: |

      The following examples use the `movies` collection 
      from the `sample_mflix` database. To learn how to
      load the sample dataset into your deployment, see
      Load Sample Data.

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

  - id: c
    content: |

      (Code example not available offline: /driver-examples/test-mongoc-sample-commands.c)

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

  - id: kotlin-coroutine
    content: |

      (Code example not available offline: /driver-examples/kotlin_examples.kt)

  - id: nodejs
    content: |
      (Code example not available offline: /driver-examples/node_update.js)

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

      ```csharp
      var documents = new[]
      {
          new BsonDocument
          {
              { "item", "canvas" },
              { "qty", 100 },
              { "size", new BsonDocument { { "h", 28 }, { "w", 35.5 }, { "uom", "cm" } } },
              { "status", "A" }
          },
          new BsonDocument
          {
              { "item", "journal" },
              { "qty", 25 },
              { "size", new BsonDocument { { "h", 14 }, { "w", 21 }, { "uom", "cm" } } },
              { "status", "A" }
          },
          new BsonDocument
          {
              { "item", "mat" },
              { "qty", 85 },
              { "size", new BsonDocument { { "h", 27.9 }, { "w", 35.5 }, { "uom", "cm" } } },
              { "status", "A" }
          },
          new BsonDocument
          {
              { "item", "mousepad" },
              { "qty", 25 },
              { "size", new BsonDocument { { "h", 19 }, { "w", 22.85 }, { "uom", "cm" } } },
              { "status", "P" }
          },
          new BsonDocument
          {
              { "item", "notebook" },
              { "qty", 50 },
              { "size", new BsonDocument { { "h", 8.5 }, { "w", 11 }, { "uom", "in" } } },
              { "status", "P" } },
          new BsonDocument
          {
              { "item", "paper" },
              { "qty", 100 },
              { "size", new BsonDocument { { "h", 8.5 }, { "w", 11 }, { "uom", "in" } } },
              { "status", "D" }
          },
          new BsonDocument
          {
              { "item", "planner" },
              { "qty", 75 },
              { "size", new BsonDocument { { "h", 22.85 }, { "w", 30 }, { "uom", "cm" } } },
              { "status", "D" }
          },
          new BsonDocument
          {
              { "item", "postcard" },
              { "qty", 45 },
              { "size", new BsonDocument { { "h", 10 }, { "w", 15.25 }, { "uom", "cm" } } },
              { "status", "A" }
          },
          new BsonDocument
          {
              { "item", "sketchbook" },
              { "qty", 80 },
              { "size", new BsonDocument { { "h", 14 }, { "w", 21 }, { "uom", "cm" } } },
              { "status", "A" }
          },
          new BsonDocument
          {
              { "item", "sketch pad" },
              { "qty", 95 },
              { "size", new BsonDocument { { "h", 22.85 }, { "w", 30.5 }, { "uom", "cm" } } }, { "status", "A" } },
      };
      collection.InsertMany(documents);
      ```

  - id: go
    content: |
      (Code example not available offline: /driver-examples/go_examples.go)

<!-- This page was over 60 KB, so its sections are separate files. -->

## Sections (in `update-documents.parts/`)

- `001-update-documents-in-a-collection.md`: Update Documents in a Collection
- `002-update-a-document-with-mongodb-atlas-behavior.md`: Update a Document with MongoDB Atlas … Behavior
