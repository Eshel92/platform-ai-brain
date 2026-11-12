<!-- Converted from tutorial/project-fields-from-query-results.txt (reStructuredText). Includes are inlined. -->

# Project Fields to Return from Query

----------

→ Use the **Select your language** drop-down menu in the
upper-right to set the language of the following examples.

----------

→ Use the **Select your language** drop-down menu in the
upper-right to set the language of the following examples or select
MongoDB Compass.

----------

By default, queries in MongoDB return all fields in matching documents.
To limit the amount of data that MongoDB sends to applications, you can
include a projection document to specify or restrict fields to
return.

tabs:
  - id: shell
    content: |
      This page provides examples of query operations with projection using the
      `db.collection.find()` method in `mongosh`.

  - id: c
    content: |
      This page provides examples of query operations with projection using
      [mongoc_collection_find_with_opts](https://mongoc.org/libmongoc/current/mongoc_collection_find_with_opts.html).

      The examples on this page use the `inventory` collection. Connect to a
      test database in your MongoDB instance then create the `inventory`
      collection:

  - id: compass
    content: |
      This page provides examples of query operations with projection using
      MongoDB Compass. 

      The examples on this page use the `inventory` collection. Connect to a
      test database in your MongoDB instance then create the `inventory`
      collection:

  - id: python
    content: |
      This page provides examples of query operations with projection using the
      `pymongo.collection.Collection.find` method in the
      [PyMongo](https://www.mongodb.com/docs/languages/python/pymongo-driver/current/)
      Python driver.

      The examples on this page use the `inventory` collection. Connect to a
      test database in your MongoDB instance then create the `inventory`
      collection:

  - id: motor
    content: |

      This page provides examples of query operations with projection using the
      `pymongo.asynchronous.collection.AsyncCollection.find`
      method in the [PyMongo Async API](https://pymongo.readthedocs.io/en/stable/api/pymongo/asynchronous/index.html).

      The examples on this page use the `inventory` collection. Connect to a
      test database in your MongoDB instance then create the `inventory`
      collection:

  - id: java-sync
    content: |
      This page provides examples of query operations with projection using the
      com.mongodb.client.MongoCollection.find_ method in the MongoDB
      Java Synchronous Driver.

      **Tip:**

      The driver provides com.mongodb.client.model.Filters_
      helper methods to facilitate the creation of filter
      documents. The examples on this page use these methods to
      create the filter documents.

      The examples on this page use the `inventory` collection. Connect to a
      test database in your MongoDB instance then create the `inventory`
      collection:

  - id: java-async
    content: |
      This page provides examples of query operations with projection using the
      [com.mongodb.reactivestreams.client.MongoCollection.find](http://mongodb.github.io/mongo-java-driver-reactivestreams/1.6/javadoc/com/mongodb/reactivestreams/client/MongoCollection.html#find())
      method in the MongoDB [Java Reactive Streams Driver](http://mongodb.github.io/mongo-java-driver-reactivestreams/1.6/).

      The examples on this page use the `inventory` collection. Connect to a
      test database in your MongoDB instance then create the `inventory`
      collection:

  - id: kotlin-coroutine
    content: |
      This page provides examples of query operations with projection by using the
      [MongoCollection.find()](https://mongodb.github.io/mongo-java-driver/{+java-driver-version+}/apidocs/driver-kotlin-coroutine/mongodb-driver-kotlin-coroutine/com.mongodb.kotlin.client.coroutine/-mongo-collection/find.html) method in the MongoDB
      `Kotlin Coroutine Driver`.

      **Tip:**

      The driver provides [com.mongodb.client.model.Filters](https://mongodb.github.io/mongo-java-driver/{+java-driver-version+}/apidocs/driver-core/com/mongodb/client/model/Filters.html)
      helper methods to facilitate the creation of filter
      documents. The examples on this page use these methods to
      create the filter documents.

      The examples on this page use the `inventory` collection. Connect to a
      test database in your MongoDB instance then create the `inventory`
      collection:

  - id: nodejs
    content: |
      This page provides examples of query operations with projection using the
      `Collection.find()` method in
      the `MongoDB Node.js Driver`.

      The examples on this page use the `inventory` collection. Connect to a
      test database in your MongoDB instance then create the `inventory`
      collection:

  - id: php
    content: |
      This page provides examples of query operations with projection using the
      `MongoDBCollection::find()`
      method in the
      [MongoDB PHP Library](https://www.mongodb.com/docs/drivers/php-libraries/).

      The examples on this page use the `inventory` collection. Connect to a
      test database in your MongoDB instance then create the `inventory`
      collection:

  - id: ruby
    content: |
      This page provides examples of query operations with projection using the
      `Mongo::Collection#find()`
      method in the
      `MongoDB Ruby Driver`.

      The examples on this page use the `inventory` collection. Connect to a
      test database in your MongoDB instance then create the `inventory`
      collection:

  - id: scala
    content: |
      This page provides examples of query operations with projection using the
      `collection.find()` method
      in the
      [MongoDB Scala Driver](http://mongodb.github.io/mongo-scala-driver/).

      The examples on this page use the `inventory` collection. Connect to a
      test database in your MongoDB instance then create the `inventory`
      collection:

  - id: csharp
    content: |
      This page provides examples of query operations with projection using the
      `MongoCollection.Find()`
      method in the
      [MongoDB .NET/C# Driver](https://mongodb.github.io/mongo-csharp-driver/).

      The examples on this page use the `inventory` collection. Connect to a
      test database in your MongoDB instance then create the `inventory`
      collection:

  - id: go
    content: |
      This page provides examples of query operations with projection using the
      `Collection.Find`
      function in the
      [MongoDB Go Driver](https://github.com/mongodb/mongo-go-driver/).

      The examples on this page use the `inventory` collection. Connect to a
      test database in your MongoDB instance then create the `inventory`
      collection:

tabs:
  - id: shell
    content: |

      ```javascript
      db.inventory.insertMany( [
        { item: "journal", status: "A", size: { h: 14, w: 21, uom: "cm" }, instock: [ { warehouse: "A", qty: 5 } ] },
        { item: "notebook", status: "A",  size: { h: 8.5, w: 11, uom: "in" }, instock: [ { warehouse: "C", qty: 5 } ] },
        { item: "paper", status: "D", size: { h: 8.5, w: 11, uom: "in" }, instock: [ { warehouse: "A", qty: 60 } ] },
        { item: "planner", status: "D", size: { h: 22.85, w: 30, uom: "cm" }, instock: [ { warehouse: "A", qty: 40 } ] },
        { item: "postcard", status: "A", size: { h: 10, w: 15.25, uom: "cm" }, instock: [ { warehouse: "B", qty: 15 }, { warehouse: "C", qty: 35 } ] }
      ]);
      ```

  - id: compass
    content: |

      ```javascript
      [
          { "item": "journal", "status": "A", "size": { "h": 14, "w": 21, "uom": "cm" }, "instock": [ { "warehouse": "A", "qty": 5 } ] },
          { "item": "notebook", "status": "A", "size": { "h": 8.5, "w": 11, "uom": "in" }, "instock": [ { "warehouse": "C", "qty": 5 } ] },
          { "item": "paper", "status": "D", "size": { "h": 8.5, "w": 11, "uom": "in" }, "instock": [ { "warehouse": "A", "qty": 60 } ] },
          { "item": "planner", "status": "D", "size": { "h": 22.85, "w": 30, "uom": "cm" }, "instock": [ { "warehouse": "A", "qty": 40 } ] },
          { "item": "postcard", "status": "A", "size": { "h": 10, "w": 15.25, "uom": "cm" }, "instock": [ { "warehouse": "B", "qty": 15 }, { "warehouse": "C", "qty": 35 } ] }
      ]
      ```

      For instructions on inserting documents in MongoDB Compass,
      see Insert Documents.

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
      (Code example not available offline: /driver-examples/node_project.js)

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
              { "item", "journal" },
              { "status", "A" },
              { "size", new BsonDocument { { "h", 14 }, { "w", 21 }, { "uom", "cm" } } },
              { "instock", new BsonArray
                  {
                      new BsonDocument { { "warehouse", "A" }, { "qty", 5 } } }
                  }
          },
          new BsonDocument
          {
              { "item", "notebook" },
              { "status", "A" },
              { "size", new BsonDocument { { "h", 8.5 }, { "w", 11 }, { "uom", "in" } } },
              { "instock", new BsonArray
                  {
                      new BsonDocument { { "warehouse", "C" }, { "qty", 5 } } }
                  }
          },
          new BsonDocument
          {
              { "item", "paper" },
              { "status", "D" },
              { "size", new BsonDocument { { "h", 8.5 }, { "w", 11 }, { "uom", "in" } } },
              { "instock", new BsonArray
                  {
                      new BsonDocument { { "warehouse", "A" }, { "qty", 60 } } }
                  }
          },
          new BsonDocument
          {
              { "item", "planner" },
              { "status", "D" },
              { "size", new BsonDocument { { "h", 22.85 }, { "w", 30 }, { "uom", "cm" } } },
              { "instock", new BsonArray
                  {
                      new BsonDocument { { "warehouse", "A" }, { "qty", 40 } } }
                  }
          },
          new BsonDocument
          {
              { "item", "postcard" },
              { "status", "A" },
              { "size", new BsonDocument { { "h", 10 }, { "w", 15.25 }, { "uom", "cm" } } },
              { "instock", new BsonArray
                  {
                      new BsonDocument { { "warehouse", "B" }, { "qty", 15 } },
                      new BsonDocument { { "warehouse", "C" }, { "qty", 35 } } }
                  }
          }
      };
      collection.InsertMany(documents);
      ```

  - id: go
    content: |
      (Code example not available offline: /driver-examples/go_examples.go)

<!-- This page was over 60 KB, so its sections are separate files. -->

## Sections (in `project-fields-from-query-results.parts/`)

- `001-return-all-fields-in-matching-documents-suppress-s.md`: Return All Fields in Matching Documents … Suppress Specific Fields in Embedded Documents
- `002-projection-on-embedded-documents-in-an-array.md`: Projection on Embedded Documents in an Array
- `003-project-specific-array-elements-in-the-returned-ar.md`: Project Specific Array Elements in the Returned Array
- `004-project-fields-with-aggregation-expressions-additi.md`: Project Fields with Aggregation Expressions … Additional Considerations
