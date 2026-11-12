<!-- Converted from tutorial/remove-documents.txt (reStructuredText). Includes are inlined. -->

# Delete Documents

You can delete documents in MongoDB using the following methods:

- Your programming language's driver.
- The MongoDB Atlas UI. To learn more, see 
  delete-documents-atlas-ui.
- `MongoDB Compass`.

----------

→ Use the **Select your language** drop-down menu in the
upper-right to set the language of the following examples or select
MongoDB Compass.

----------

tabs:
  - id: shell
    content: |
      This page uses the following `mongosh` methods:

      - `db.collection.deleteMany()`
      - `db.collection.deleteOne()`

      The examples on this page use the `inventory` collection. To populate
      the `inventory` collection, run the following:

  - id: compass
    content: |

      This page uses MongoDB Compass to
      delete the documents.

      Populate the `inventory` collection with the following
      documents:

  - id: python
    content: |
      This page uses the following
      [PyMongo](https://pymongo.readthedocs.io/en/stable/index.html)
      Python driver methods:

      - `pymongo.collection.Collection.delete_many`
      - `pymongo.collection.Collection.delete_one`

      The examples on this page use the `inventory` collection. Connect to a
      test database in your MongoDB instance then create the `inventory`
      collection:

  - id: motor
    content: |
      This page uses the
      following [Motor](https://motor.readthedocs.io/en/stable/)
      driver methods:

      - `motor.motor_asyncio.AsyncIOMotorCollection.delete_many`
      - `motor.motor_asyncio.AsyncIOMotorCollection.delete_one`

      The examples on this page use the `inventory` collection. Connect to a
      test database in your MongoDB instance then create the `inventory`
      collection:

  - id: java-sync
    content: |
      This page uses the
      following Java Synchronous Driver methods:

      - com.mongodb.client.MongoCollection.deleteMany_

      - com.mongodb.client.MongoCollection.deleteOne_

      The examples on this page use the `inventory` collection. Connect to a
      test database in your MongoDB instance then create the `inventory`
      collection:

  - id: java-async
    content: |
      This page uses the
      following [Java Reactive Streams Driver](http://mongodb.github.io/mongo-java-driver-reactivestreams/1.6/) methods:

      - [com.mongodb.reactivestreams.client.MongoCollection.deleteMany](http://mongodb.github.io/mongo-java-driver-reactivestreams/1.6/javadoc/com/mongodb/reactivestreams/client/MongoCollection.html#deleteMany(org.bson.conversions.Bson))

      - [com.mongodb.reactivestreams.client.MongoCollection.deleteOne](http://mongodb.github.io/mongo-java-driver-reactivestreams/1.6/javadoc/com/mongodb/reactivestreams/client/MongoCollection.html#deleteOne(org.bson.conversions.Bson))

      The examples on this page use the `inventory` collection. Connect to a
      test database in your MongoDB instance then create the `inventory`
      collection:

  - id: nodejs
    content: |
      This page uses the
      following `MongoDB Node.js Driver` methods:

      - `Collection.deleteMany()`
      - `Collection.deleteOne()`

      The examples on this page use the `inventory` collection. Connect to a
      test database in your MongoDB instance then create the `inventory`
      collection:

  - id: php
    content: |
      This page uses the
      following  [MongoDB PHP Library](https://www.mongodb.com/docs/php-library/current/) methods:

      - `MongoDBCollection::deleteMany()`
      - `MongoDBCollection::deleteOne()`

      The examples on this page use the `inventory` collection. Connect to a
      test database in your MongoDB instance then create the `inventory`
      collection:

  - id: ruby
    content: |
      This page uses the
      following `MongoDB Ruby Driver` methods:

      - `Mongo::Collection#delete_many()`
      - `Mongo::Collection#delete_one()`

      The examples on this page use the `inventory` collection. Connect to a
      test database in your MongoDB instance then create the `inventory`
      collection:

  - id: scala
    content: |
      This page uses the
      following  [MongoDB Scala Driver](http://mongodb.github.io/mongo-scala-driver/) methods:

      - `collection.deleteMany()`

      - `collection.deleteOne()`

      The examples on this page use the `inventory` collection. Connect to a
      test database in your MongoDB instance then create the `inventory`
      collection:

  - id: csharp
    content: |
      This page uses the
      following `MongoDB C# Driver` methods:

      - `IMongoCollection.DeleteMany()`
      - `IMongoCollection.DeleteOne()`

      The examples on this page use the `inventory` collection. Connect to a
      test database in your MongoDB instance then create the `inventory`
      collection:

  - id: go
    content: |
      This page uses the
      following `MongoDB Go Driver` functions:

      - `Collection.DeleteMany`

      - `Collection.DeleteOne`

      The examples on this page use the `inventory` collection. Connect to a
      test database in your MongoDB instance then create the `inventory`
      collection:

tabs:
  - id: shell
    content: |

      ```javascript
      db.inventory.insertMany( [
         { item: "journal", qty: 25, size: { h: 14, w: 21, uom: "cm" }, status: "A" },
         { item: "notebook", qty: 50, size: { h: 8.5, w: 11, uom: "in" }, status: "P" },
         { item: "paper", qty: 100, size: { h: 8.5, w: 11, uom: "in" }, status: "D" },
         { item: "planner", qty: 75, size: { h: 22.85, w: 30, uom: "cm" }, status: "D" },
         { item: "postcard", qty: 45, size: { h: 10, w: 15.25, uom: "cm" }, status: "A" },
      ] );
      ```

  - id: compass
    content: |

      ```javascript
      [
          { "item": "journal", "qty": 25, "size": { "h": 14, "w": 21, "uom": "cm" }, "status": "A" },
          { "item": "notebook", "qty": 50, "size": { "h": 8.5, "w": 11, "uom": "in" }, "status": "P" },
          { "item": "paper", "qty": 100, "size": { "h": 8.5, "w": 11, "uom": "in" }, "status": "D" },
          { "item": "planner", "qty": 75, "size": { "h": 22.85, "w": 30, "uom": "cm" }, "status": "D" },
          { "item": "postcard", "qty": 45, "size": { "h": 10, "w": 15.25, "uom": "cm" }, "status": "A" }
      ]
      ```

      For instructions on inserting documents in MongoDB Compass, see
      Insert Documents.

      **Note:**

      For complete reference on inserting documents in MongoDB
      Compass, see the `Compass documentation`.

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

      (Code example not available offline: /driver-examples/node_remove.js)

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

<!-- This page was over 60 KB, so its sections are separate files. -->

## Sections (in `remove-documents.parts/`)

- `001-delete-all-documents.md`: Delete All Documents
- `002-delete-all-documents-that-match-a-condition-part-1.md`: Delete All Documents that Match a Condition (part 1)
- `003-delete-all-documents-that-match-a-condition-part-2.md`: Delete All Documents that Match a Condition (part 2)
- `004-delete-all-documents-that-match-a-condition-part-3.md`: Delete All Documents that Match a Condition (part 3) … Delete Behavior
