<!-- Converted from tutorial/query-documents.txt (reStructuredText). Includes are inlined. -->

# Read Documents

In MongoDB, a Read operation consists of querying the database. This page
provides examples.

You can query documents in MongoDB with the following methods:

- Your programming language's driver.
- The MongoDB Atlas UI. To learn more, see 
  query-documents-atlas-ui.
- `MongoDB Compass`.

----------

→ Use the **Select your language** drop-down menu in the
upper-right to set the language of the following examples or select
MongoDB Compass.

----------

tabs:
  - id: shell
    content: |
      This page provides examples of query operations using the
      `db.collection.find()` method in `mongosh`.

  - id: c
    content: |
      This page provides examples of query operations using
      [mongoc_collection_find_with_opts](https://mongoc.org/libmongoc/current/mongoc_collection_find_with_opts.html).

      The examples on this page use the `inventory` collection. Connect to a
      test database in your MongoDB instance then create the `inventory`
      collection:

  - id: compass
    content: |
      This page provides examples of query operations using
      MongoDB Compass. 

      The examples on this page use the `inventory` collection. Connect to a
      test database in your MongoDB instance then create the `inventory`
      collection:

  - id: python
    content: |
      This page provides examples of query operations using the
      `pymongo.collection.Collection.find` method in the
      [PyMongo](https://www.mongodb.com/docs/languages/python/pymongo-driver/current/)
      Python driver.

      The examples on this page use the `inventory` collection. Connect to a
      test database in your MongoDB instance then create the `inventory`
      collection:

  - id: motor
    content: |

      This page provides examples of query operations using the
      `pymongo.asynchronous.collection.AsyncCollection.find`
      method in the [PyMongo Async API](https://pymongo.readthedocs.io/en/stable/api/pymongo/asynchronous/index.html).

      The examples on this page use the `inventory` collection. Connect to a
      test database in your MongoDB instance then create the `inventory`
      collection:

  - id: java-sync
    content: |
      This page provides examples of query operations using the
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
      This page provides examples of query operations using the
      [com.mongodb.reactivestreams.client.MongoCollection.find](http://mongodb.github.io/mongo-java-driver-reactivestreams/1.6/javadoc/com/mongodb/reactivestreams/client/MongoCollection.html#find())
      method in the MongoDB [Java Reactive Streams Driver](http://mongodb.github.io/mongo-java-driver-reactivestreams/1.6/).

      The examples on this page use the `inventory` collection. Connect to a
      test database in your MongoDB instance then create the `inventory`
      collection:

  - id: kotlin-coroutine
    content: |
      This page provides examples of query operations by using the
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
      This page provides examples of query operations using the
      `Collection.find()` method in
      the `MongoDB Node.js Driver`.

      The examples on this page use the `inventory` collection. Connect to a
      test database in your MongoDB instance then create the `inventory`
      collection:

  - id: php
    content: |
      This page provides examples of query operations using the
      `MongoDBCollection::find()`
      method in the
      [MongoDB PHP Library](https://www.mongodb.com/docs/drivers/php-libraries/).

      The examples on this page use the `inventory` collection. Connect to a
      test database in your MongoDB instance then create the `inventory`
      collection:

  - id: ruby
    content: |
      This page provides examples of query operations using the
      `Mongo::Collection#find()`
      method in the
      `MongoDB Ruby Driver`.

      The examples on this page use the `inventory` collection. Connect to a
      test database in your MongoDB instance then create the `inventory`
      collection:

  - id: scala
    content: |
      This page provides examples of query operations using the
      `collection.find()` method
      in the
      [MongoDB Scala Driver](http://mongodb.github.io/mongo-scala-driver/).

      The examples on this page use the `inventory` collection. Connect to a
      test database in your MongoDB instance then create the `inventory`
      collection:

  - id: csharp
    content: |
      This page provides examples of query operations using the
      `MongoCollection.Find()`
      method in the
      [MongoDB .NET/C# Driver](https://mongodb.github.io/mongo-csharp-driver/).

      The examples on this page use the `inventory` collection. Connect to a
      test database in your MongoDB instance then create the `inventory`
      collection:

  - id: go
    content: |
      This page provides examples of query operations using the
      `Collection.Find`
      function in the
      [MongoDB Go Driver](https://github.com/mongodb/mongo-go-driver/).

      The examples on this page use the `inventory` collection. Connect to a
      test database in your MongoDB instance then create the `inventory`
      collection:

tabs:
  - id: shell
    content: |

      The examples on this page use data from the sample_mflix dataset. For details on how to load this dataset into your self-managed
      MongoDB deployment, see Load the Sample Dataset.
      If you made any modifications to the sample databases, you may need to drop and
      recreate the databases to run the examples on this page. 

  - id: compass
    content: |

      ```javascript
      [
          { "item": "journal", "qty": 25, "size": { "h": 14, "w": 21, "uom": "cm" }, "status": "A" },
          { "item": "notebook", "qty": 50, "size": { "h": 8.5, "w": 11, "uom": "in" }, "status": "A" },
          { "item": "paper", "qty": 100, "size": { "h": 8.5, "w": 11, "uom": "in" }, "status": "D" },
          { "item": "planner", "qty": 75, "size": { "h": 22.85, "w": 30, "uom": "cm" }, "status": "D" },
          { "item": "postcard", "qty": 45, "size": { "h": 10, "w": 15.25, "uom": "cm" }, "status": "A" }
      ]
      ```

      For instructions on inserting documents in MongoDB Compass, see
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

      ```csharp
      var documents = new BsonDocument[]
      {
          new BsonDocument
          {
              { "item", "journal" },
              { "qty", 25 },
              { "size", new BsonDocument { { "h", 14 }, { "w", 21 }, {  "uom", "cm"} } },
              { "status", "A" }
          },
          new BsonDocument
          {
              { "item", "notebook" },
              { "qty", 50 },
              { "size", new BsonDocument { { "h",  8.5 }, { "w", 11 }, {  "uom", "in"} } },
              { "status", "A" }
          },
          new BsonDocument
          {
              { "item", "paper" },
              { "qty", 100 },
              { "size", new BsonDocument { { "h",  8.5 }, { "w", 11 }, {  "uom", "in"} } },
              { "status", "D" }
          },
          new BsonDocument
          {
              { "item", "planner" },
              { "qty", 75 },
              { "size", new BsonDocument { { "h", 22.85 }, { "w", 30  }, {  "uom", "cm"} } },
              { "status", "D" }
          },
          new BsonDocument
          {
              { "item", "postcard" },
              { "qty", 45 },
              { "size", new BsonDocument { { "h", 10 }, { "w", 15.25 }, {  "uom", "cm"} } },
              { "status", "A" }
          },
      };
      collection.InsertMany(documents);
      ```

  - id: go
    content: |
      (Code example not available offline: /driver-examples/go_examples.go)

## Select All Documents in a Collection

tabs:
  - id: shell
    content: |
      To select all documents in the collection, pass an empty
      document as the query filter parameter to the find method. The
      query filter parameter determines the select criteria:

  - id: compass
    content: |
      To select all documents in the collection, pass an empty
      document as the query filter parameter to the
      query bar. The
      query filter parameter determines
      the select criteria:

  - id: c
    content: |
      To select all documents in the collection, pass an empty
      document as the query filter parameter to the find method. The
      query filter parameter determines the select criteria:

  - id: python
    content: |
      To select all documents in the collection, pass an empty
      document as the query filter parameter to the find method. The
      query filter parameter determines the select criteria:

  - id: motor
    content: |
      To select all documents in the collection, pass an empty
      document as the query filter parameter to the find method. The
      query filter parameter determines the select criteria:

  - id: java-sync
    content: |
      To select all documents in the collection, pass an empty
      document as the query filter parameter to the find method. The
      query filter parameter determines the select criteria:

  - id: java-async
    content: |
      To select all documents in the collection, pass an empty
      document as the query filter parameter to the find method. The
      query filter parameter determines the select criteria:

  - id: kotlin-coroutine
    content: |
      To select all documents in the collection, pass an empty
      document as the query filter parameter to the find method. The
      query filter parameter determines the select criteria:

  - id: nodejs
    content: |
      To select all documents in the collection, pass an empty
      document as the query filter parameter to the find method. The
      query filter parameter determines the select criteria:

  - id: php
    content: |
      To select all documents in the collection, pass an empty
      document as the query filter parameter to the find method. The
      query filter parameter determines the select criteria:

  - id: ruby
    content: |
      To select all documents in the collection, pass an empty
      document as the query filter parameter to the find method. The
      query filter parameter determines the select criteria:

  - id: scala
    content: |
      To select all documents in the collection, pass an empty
      document as the query filter parameter to the find method. The
      query filter parameter determines the select criteria:

  - id: csharp
    content: |
      To select all documents in the collection, pass an empty
      document as the query filter parameter to the find method. The
      query filter parameter determines the select criteria:

  - id: go
    content: |
      To select all documents in the collection, pass an empty
      document as the query filter parameter to the find method. The
      query filter parameter determines the select criteria:

tabs:
  - id: shell
    content: |

      ```javascript
      db.movies.find( {} )
      ```

  - id: compass
    content: |

      (Figure: /images/compass-select-all-new.png)

  - id: c
    content: |

      (Code example not available offline: /driver-examples/test-mongoc-sample-commands.c)

      Clean up any open resources by calling the following methods, as appropriate:

      - [bson_destroy](http://mongoc.org/libbson/current/bson_destroy.html)

      - [mongoc_bulk_operation_destroy](https://mongoc.org/libmongoc/current/mongoc_bulk_operation_destroy.html)

      - [mongoc_collection_destroy](https://mongoc.org/libmongoc/current/mongoc_collection_destroy)

      - [mongoc_cursor_destroy](https://mongoc.org/libmongoc/current/mongoc_cursor_destroy.html),

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

      ```csharp
      var filter = Builders<BsonDocument>.Filter.Empty;
      var result = collection.Find(filter).ToList();
      ```

  - id: go
    content: |
      (Code example not available offline: /driver-examples/go_examples.go)

This operation uses an empty query predicate of `{}`, which
corresponds to the following SQL statement:

tabs:
  - id: shell
    content: |

      ```sql
      SELECT * FROM movies
      ```

  - id: compass
    content: |

      ```sql
      SELECT * FROM inventory
      ```

  - id: c
    content: |

      ```sql
      SELECT * FROM inventory
      ```

  - id: python
    content: |

      ```sql
      SELECT * FROM inventory
      ```

  - id: motor
    content: |

      ```sql
      SELECT * FROM inventory
      ```

  - id: java-sync
    content: |

      ```sql
      SELECT * FROM inventory
      ```

  - id: java-async
    content: |

      ```sql
      SELECT * FROM inventory
      ```

  - id: kotlin-coroutine
    content: |

      ```sql
      SELECT * FROM inventory
      ```

  - id: nodejs
    content: |

      ```sql
      SELECT * FROM inventory
      ```

  - id: php
    content: |

      ```sql
      SELECT * FROM inventory
      ```

  - id: ruby
    content: |

      ```sql
      SELECT * FROM inventory
      ```

  - id: scala
    content: |

      ```sql
      SELECT * FROM inventory
      ```

  - id: csharp
    content: |

      ```sql
      SELECT * FROM inventory
      ```

  - id: go
    content: |

      ```sql
      SELECT * FROM inventory
      ```

tabs:
  - id: shell
    content: |
      For more information, see `find()`.

  - id: compass
    content: |
      For more information, see Query Bar.

  - id: c
    content: |
      For more information, see
      [mongoc_collection_find_with_opts](https://mongoc.org/libmongoc/current/mongoc_collection_find_with_opts.html).

  - id: python
    content: |
      For more information, see
      `find`.

  - id: motor
    content: |
      For more information, see
      `find`.

  - id: java-sync
    content: |
      For more information, see
      com.mongodb.client.MongoCollection.find_.

  - id: java-async
    content: |
      For more information, see
      [com.mongodb.reactivestreams.client.MongoCollection.find](http://mongodb.github.io/mongo-java-driver-reactivestreams/1.6/javadoc/com/mongodb/reactivestreams/client/MongoCollection.html#find()).

  - id: kotlin-coroutine
    content: |
      For more information, see
      [MongoCollection.find()](https://mongodb.github.io/mongo-java-driver/{+java-driver-version+}/apidocs/driver-kotlin-coroutine/mongodb-driver-kotlin-coroutine/com.mongodb.kotlin.client.coroutine/-mongo-collection/find.html).

  - id: nodejs
    content: |
      For more information, see `find()`.

  - id: php
    content: |
      For more information, see
      `find()`.

  - id: ruby
    content: |
      For more information, see
      `find()`.

  - id: scala
    content: |
      For more information, see
      `collection.find()`.

  - id: csharp
    content: |
      For more information, see
      `Find()`.

  - id: go
    content: |
      For more information, see
      `Collection.Find`.

## Specify Equality Condition

tabs:
  - id: shell
    content: |
      To specify equality conditions, use `<field>:<value>`
      expressions in the
      query filter document:

      ```javascript
      { <field1>: <value1>, ... }
      ```

  - id: compass
    content: |
      To specify equality conditions, use `<field>:<value>`
      expressions in the
      query filter document:

      ```javascript
      { <field1>: <value1>, ... }
      ```

  - id: c
    content: |
      To specify equality conditions, use `<field>:<value>`
      expressions in the
      query filter document: 

      ```c
      { <field1>: <value1>, ... } 
      ```

  - id: python
    content: |
      To specify equality conditions, use `<field>:<value>`
      expressions in the
      query filter document:

      ```python
      { <field1>: <value1>, ... }
      ```

  - id: motor
    content: |
      To specify equality conditions, use `<field>:<value>`
      expressions in the
      query filter document:

      ```python
      { <field1>: <value1>, ... }
      ```

  - id: java-sync
    content: |
      To specify equality conditions, use the
      `com.mongodb.client.model.Filters.eq_` method to create the
      query filter document:

      ```java
      and(eq( <field1>, <value1>), eq( <field2>, <value2>) ...)
      ```

  - id: java-async
    content: |
      To specify equality conditions, use the
      com.mongodb.client.model.Filters.eq_ method to create the
      query filter document:

      ```java
      and(eq( <field1>, <value1>), eq( <field2>, <value2>) ...)
      ```

  - id: kotlin-coroutine
    content: |
      To specify equality conditions, use the
      [Filters.eq()](https://mongodb.github.io/mongo-java-driver/{+java-driver-version+}/apidocs/driver-core/com/mongodb/client/model/Filters.html#eq(java.lang.String,TItem))
      method to create the query filter document:

      ```kotlin
      and(eq(<field1>, <value1>), eq(<field2>, <value2>) ...)
      ```

  - id: nodejs
    content: |
      To specify equality conditions, use `<field>:<value>`
      expressions in the
      query filter document:

      ```javascript
      { <field1>: <value1>, ... }
      ```

  - id: php
    content: |
      To specify equality conditions, use `<field> => <value>`
      expressions in the
      query filter document:

      ```php
      [ <field1> => <value1>, ... ]
      ```

  - id: ruby
    content: |
      To specify equality conditions, use `<field> => <value>`
      expressions in the
      query filter document:

      ```ruby
      { <field1> => <value1>, ... }
      ```

  - id: scala
    content: |
      To specify equality conditions, use the
      `com.mongodb.client.model.Filters.eq_` method to create the
      query filter document:

      ```scala
      and(equal(<field1>, <value1>), equal(<field2>, <value2>) ...)
      ```

  - id: csharp
    content: |
      To specify equality conditions, construct a filter using the
      `Eq` method:

      ```csharp
      Builders<BsonDocument>.Filter.Eq(<field>, <value>);
      ```

  - id: go
    content: |
      To specify equality conditions, use the `bson.D` type to create a
      filter document:

      ```go
      filter := bson.D{{"<field>", <value>}}
      ```

tabs:
  - id: shell
    content: |
      The following example selects all documents from the
      `sample_mflix.movies` collection where `rated`
      equals `"PG-13"`:

  - id: compass
    content: |
      The following example selects all documents from the
      `inventory` collection where `status` equals
      `"D"`:

  - id: c
    content: |
      The following example selects all documents from the
      `inventory` collection where `status` equals
      `"D"`:

  - id: python
    content: |
      The following example selects all documents from the
      `inventory` collection where `status` equals
      `"D"`:

  - id: motor
    content: |
      The following example selects all documents from the
      `inventory` collection where `status` equals
      `"D"`:

  - id: java-sync
    content: |
      The following example selects all documents from the
      `inventory` collection where `status` equals
      `"D"`:

  - id: java-async
    content: |
      The following example selects all documents from the
      `inventory` collection where `status` equals
      `"D"`:

  - id: kotlin-coroutine
    content: |
      The following example selects all documents from the
      `inventory` collection where `status` equals
      `"D"`:

  - id: nodejs
    content: |
      The following example selects all documents from the
      `inventory` collection where `status` equals
      `"D"`:

  - id: php
    content: |
      The following example selects all documents from the
      `inventory` collection where `status` equals
      `"D"`:

  - id: ruby
    content: |
      The following example selects all documents from the
      `inventory` collection where `status` equals
      `"D"`:

  - id: scala
    content: |
      The following example selects all documents from the
      `inventory` collection where `status` equals
      `"D"`:

  - id: csharp
    content: |
      The following example selects all documents from the
      `inventory` collection where `status` equals
      `"D"`:

  - id: go
    content: |
      The following example selects all documents from the
      `inventory` collection where `status` equals
      `"D"`:

tabs:
  - id: shell
    content: |

      ```javascript
      db.movies.find( { rated: "PG-13" } )
      ```

  - id: compass
    content: |
      Copy the following filter into the Compass query bar and click
      Find:

      ```javascript
      { status: "D" }
      ```

      **Note:**

      The MongoDB Compass query bar autocompletes the current query
      based on the keys in your collection's documents, including
      keys in embedded sub-documents.

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

      ```csharp
      var filter = Builders<BsonDocument>.Filter.Eq("status", "D");
      var result = collection.Find(filter).ToList();
      ```

  - id: go
    content: |
      (Code example not available offline: /driver-examples/go_examples.go)

tabs:
  - id: shell
    content: |
      This operation uses a query predicate of
      `{ rated: "PG-13" }`, which corresponds to the
      following SQL statement:

      ```sql
      SELECT * FROM movies WHERE rated = "PG-13"
      ```

  - id: compass
    content: |
      This operation uses a query predicate of
      `{ status: "D" }`, which corresponds to the
      following SQL statement:

      ```sql
      SELECT * FROM inventory WHERE status = "D"
      ```

  - id: c
    content: |
      This operation uses a query predicate of
      `{ status: "D" }`, which corresponds to the
      following SQL statement:

      ```sql
      SELECT * FROM inventory WHERE status = "D"
      ```

  - id: python
    content: |
      This operation uses a query predicate of
      `{ status: "D" }`, which corresponds to the
      following SQL statement:

      ```sql
      SELECT * FROM inventory WHERE status = "D"
      ```

  - id: motor
    content: |
      This operation uses a query predicate of
      `{ status: "D" }`, which corresponds to the
      following SQL statement:

      ```sql
      SELECT * FROM inventory WHERE status = "D"
      ```

  - id: java-sync
    content: |
      This operation uses a query predicate of
      `{ status: "D" }`, which corresponds to the
      following SQL statement:

      ```sql
      SELECT * FROM inventory WHERE status = "D"
      ```

  - id: java-async
    content: |
      This operation uses a query predicate of
      `{ status: "D" }`, which corresponds to the
      following SQL statement:

      ```sql
      SELECT * FROM inventory WHERE status = "D"
      ```

  - id: kotlin-coroutine
    content: |
      This operation uses a query predicate of
      `{ status: "D" }`, which corresponds to the
      following SQL statement:

      ```sql
      SELECT * FROM inventory WHERE status = "D"
      ```

  - id: nodejs
    content: |
      This operation uses a query predicate of
      `{ status: "D" }`, which corresponds to the
      following SQL statement:

      ```sql
      SELECT * FROM inventory WHERE status = "D"
      ```

  - id: php
    content: |
      This operation uses a query predicate of
      `{ status: "D" }`, which corresponds to the
      following SQL statement:

      ```sql
      SELECT * FROM inventory WHERE status = "D"
      ```

  - id: ruby
    content: |
      This operation uses a query predicate of
      `{ status: "D" }`, which corresponds to the
      following SQL statement:

      ```sql
      SELECT * FROM inventory WHERE status = "D"
      ```

  - id: scala
    content: |
      This operation uses a query predicate of
      `{ status: "D" }`, which corresponds to the
      following SQL statement:

      ```sql
      SELECT * FROM inventory WHERE status = "D"
      ```

  - id: csharp
    content: |
      This operation uses a query predicate of
      `{ status: "D" }`, which corresponds to the
      following SQL statement:

      ```sql
      SELECT * FROM inventory WHERE status = "D"
      ```

  - id: go
    content: |
      This operation uses a query predicate of
      `{ status: "D" }`, which corresponds to the
      following SQL statement:

      ```sql
      SELECT * FROM inventory WHERE status = "D"
      ```

## Specify Conditions Using Query Operators

tabs:
  - id: shell
    content: |
      A query filter document can
      use the query operators to specify
      conditions in the following form:

      ```javascript
      { <field1>: { <operator1>: <value1> }, ... }
      ```

  - id: c
    content: |
      A query filter document can
      use the query operators to specify
      conditions in the following form:

      ```c
      { <field1>: { <operator1>: <value1> }, ... } 
      ```

  - id: compass
    content: |
      A query filter document can
      use the query operators to specify
      conditions in the following form:

      ```javascript
      { <field1>: { <operator1>: <value1> }, ... }
      ```

  - id: python
    content: |
      A query filter document can
      use the query operators to specify
      conditions in the following form:

      ```python
      { <field1>: { <operator1>: <value1> }, ... }
      ```

  - id: motor
    content: |
      A query filter document can
      use the query operators to specify
      conditions in the following form:

      ```python
      { <field1>: { <operator1>: <value1> }, ... }
      ```

  - id: java-sync
    content: |

      In addition to the equality condition, MongoDB provides
      various query operators to specify
      filter conditions. Use the
      com.mongodb.client.model.Filters_ helper methods to
      facilitate the creation of filter documents. For example:

      ```java
      and(gte(<field1>, <value1>), lt(<field2>, <value2>), eq(<field3>, <value3>))
      ```

  - id: java-async
    content: |

      In addition to the equality condition, MongoDB provides
      various query operators to specify
      filter conditions. Use the
      com.mongodb.client.model.Filters_ helper methods to
      facilitate the creation of filter documents. For example:

      ```java
      and(gte(<field1>, <value1>), lt(<field2>, <value2>), eq(<field3>, <value3>))
      ```

  - id: kotlin-coroutine
    content: |

      In addition to the equality condition, MongoDB provides
      various query operators to specify
      filter conditions. Use the [com.mongodb.client.model.Filters](https://mongodb.github.io/mongo-java-driver/{+java-driver-version+}/apidocs/driver-core/com/mongodb/client/model/Filters.html) helper methods to
      facilitate the creation of filter documents. For example:

      ```kotlin
      and(gte(<field1>, <value1>), lt(<field2>, <value2>), eq(<field3>, <value3>))
      ```

  - id: nodejs
    content: |
      A query filter document can
      use the query operators to specify
      conditions in the following form:

      ```javascript
      { <field1>: { <operator1>: <value1> }, ... }
      ```

  - id: php
    content: |
      A query filter document can
      use the query operators to specify
      conditions in the following form:

      ```php
      [ <field1> => [ <operator1> => <value1> ], ... ]
      ```

  - id: ruby
    content: |
      A query filter document can
      use the query operators to specify
      conditions in the following form:

      ```ruby
      { <field1> => { <operator1> => <value1> }, ... }
      ```

  - id: scala
    content: |

      In addition to the equality condition, MongoDB provides
      various query operators to specify
      filter conditions. Use the
      `com.mongodb.client.model.Filters_` helper methods to
      facilitate the creation of filter documents. For example:

      ```scala
      and(gte(<field1>, <value1>), lt(<field2>, <value2>), equal(<field3>, <value3>))
      ```

  - id: csharp
    content: |
      In addition to the equality filter, MongoDB provides
      various query operators to specify
      filter conditions. Use the
      `FilterDefinitionBuilder`
      methods to create a filter document. For example:

      ```csharp
      var builder = Builders<BsonDocument>.Filter;
      builder.And(builder.Eq(<field1>, <value1>), builder.Lt(<field2>, <value2>));
      ```

  - id: go
    content: |
      In addition to the equality filter, MongoDB provides
      various query operators to specify
      filter conditions. Use the bson package to create query 
      operators for filter documents. For example:

      ```go
      filter := bson.D{
          {"$and", bson.A{
              bson.D{{"field1", bson.D{{"$eq", value1}}}},
              bson.D{{"field2", bson.D{{"$lt", value2}}}},
          }},
      }
      ```

tabs:
  - id: shell
    content: |
      The following example retrieves all documents from the
      `sample_mflix.movies` collection where `rated`
      equals either `"G"` or `"PG-13"`:

  - id: compass
    content: |
      The following example retrieves all documents from the
      `inventory` collection where `status` equals
      either `"A"` or `"D"`:

  - id: c
    content: |
      The following example retrieves all documents from the
      `inventory` collection where `status` equals
      either `"A"` or `"D"`:

  - id: python
    content: |
      The following example retrieves all documents from the
      `inventory` collection where `status` equals
      either `"A"` or `"D"`:

  - id: motor
    content: |
      The following example retrieves all documents from the
      `inventory` collection where `status` equals
      either `"A"` or `"D"`:

  - id: java-sync
    content: |
      The following example retrieves all documents from the
      `inventory` collection where `status` equals
      either `"A"` or `"D"`:

  - id: java-async
    content: |
      The following example retrieves all documents from the
      `inventory` collection where `status` equals
      either `"A"` or `"D"`:

  - id: kotlin-coroutine
    content: |
      The following example retrieves all documents from the
      `inventory` collection where `status` equals
      either `"A"` or `"D"`:

  - id: nodejs
    content: |
      The following example retrieves all documents from the
      `inventory` collection where `status` equals
      either `"A"` or `"D"`:

  - id: php
    content: |
      The following example retrieves all documents from the
      `inventory` collection where `status` equals
      either `"A"` or `"D"`:

  - id: ruby
    content: |
      The following example retrieves all documents from the
      `inventory` collection where `status` equals
      either `"A"` or `"D"`:

  - id: scala
    content: |
      The following example retrieves all documents from the
      `inventory` collection where `status` equals
      either `"A"` or `"D"`:

  - id: csharp
    content: |
      The following example retrieves all documents from the
      `inventory` collection where `status` equals
      either `"A"` or `"D"`:

  - id: go
    content: |
      The following example retrieves all documents from the
      `inventory` collection where `status` equals
      either `"A"` or `"D"`:

tabs:
  - id: shell
    content: |

      ```javascript
      db.movies.find( { rated: { $in: [ "G", "PG-13" ] } } )
      ```

  - id: compass
    content: |
      Copy the following filter into the Compass query bar and click
      Find:

      ```javascript
      { status: { $in: [ "A", "D" ] } }
      ```

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

      ```csharp
      var filter = Builders<BsonDocument>.Filter.In("status", new[] { "A", "D" });
      var result = collection.Find(filter).ToList();
      ```

  - id: go
    content: |
      (Code example not available offline: /driver-examples/go_examples.go)

**Note:**

Although you can use the `$or` operator for this query,
use the `$in` operator instead of `$or`
when performing equality checks on the same field.

tabs:
  - id: shell
    content: |
      The operation uses a query predicate of
      `{ rated: { $in: [ "G", "PG-13" ] } }`, which
      corresponds to the following SQL statement:

      ```sql
      SELECT * FROM movies WHERE rated in ("G", "PG-13")
      ```

  - id: compass
    content: |
      The operation uses a query predicate of
      `{ status: { $in: [ "A", "D" ] } }`, which
      corresponds to the following SQL statement:

      ```sql
      SELECT * FROM inventory WHERE status in ("A", "D")
      ```

  - id: c
    content: |
      The operation uses a query predicate of
      `{ status: { $in: [ "A", "D" ] } }`, which
      corresponds to the following SQL statement:

      ```sql
      SELECT * FROM inventory WHERE status in ("A", "D")
      ```

  - id: python
    content: |
      The operation uses a query predicate of
      `{ status: { $in: [ "A", "D" ] } }`, which
      corresponds to the following SQL statement:

      ```sql
      SELECT * FROM inventory WHERE status in ("A", "D")
      ```

  - id: motor
    content: |
      The operation uses a query predicate of
      `{ status: { $in: [ "A", "D" ] } }`, which
      corresponds to the following SQL statement:

      ```sql
      SELECT * FROM inventory WHERE status in ("A", "D")
      ```

  - id: java-sync
    content: |
      The operation uses a query predicate of
      `{ status: { $in: [ "A", "D" ] } }`, which
      corresponds to the following SQL statement:

      ```sql
      SELECT * FROM inventory WHERE status in ("A", "D")
      ```

  - id: java-async
    content: |
      The operation uses a query predicate of
      `{ status: { $in: [ "A", "D" ] } }`, which
      corresponds to the following SQL statement:

      ```sql
      SELECT * FROM inventory WHERE status in ("A", "D")
      ```

  - id: kotlin-coroutine
    content: |
      The operation uses a query predicate of
      `{ status: { $in: [ "A", "D" ] } }`, which
      corresponds to the following SQL statement:

      ```sql
      SELECT * FROM inventory WHERE status in ("A", "D")
      ```

  - id: nodejs
    content: |
      The operation uses a query predicate of
      `{ status: { $in: [ "A", "D" ] } }`, which
      corresponds to the following SQL statement:

      ```sql
      SELECT * FROM inventory WHERE status in ("A", "D")
      ```

  - id: php
    content: |
      The operation uses a query predicate of
      `{ status: { $in: [ "A", "D" ] } }`, which
      corresponds to the following SQL statement:

      ```sql
      SELECT * FROM inventory WHERE status in ("A", "D")
      ```

  - id: ruby
    content: |
      The operation uses a query predicate of
      `{ status: { $in: [ "A", "D" ] } }`, which
      corresponds to the following SQL statement:

      ```sql
      SELECT * FROM inventory WHERE status in ("A", "D")
      ```

  - id: scala
    content: |
      The operation uses a query predicate of
      `{ status: { $in: [ "A", "D" ] } }`, which
      corresponds to the following SQL statement:

      ```sql
      SELECT * FROM inventory WHERE status in ("A", "D")
      ```

  - id: csharp
    content: |
      The operation uses a query predicate of
      `{ status: { $in: [ "A", "D" ] } }`, which
      corresponds to the following SQL statement:

      ```sql
      SELECT * FROM inventory WHERE status in ("A", "D")
      ```

  - id: go
    content: |
      The operation uses a query predicate of
      `{ status: { $in: [ "A", "D" ] } }`, which
      corresponds to the following SQL statement:

      ```sql
      SELECT * FROM inventory WHERE status in ("A", "D")
      ```

For the complete list of MongoDB query operators, see
query-predicates-ref.

## Specify `AND` Conditions

A compound query can specify conditions for more than one field in the
collection's documents. Implicitly, a logical `AND` conjunction
connects the clauses of a compound query so that the query selects the
documents in the collection that match all the conditions.

tabs:
  - id: shell
    content: |
      The following example retrieves all documents in the
      `sample_mflix.movies` collection where `rated`
      equals `"G"` **and** `runtime` is less than
      (`$lt`) `90`:

  - id: compass
    content: |
      The following example retrieves all documents in the
      `inventory` collection where `status` equals
      `"A"` **and** `qty` is less than
      (`$lt`) `30`:

  - id: c
    content: |
      The following example retrieves all documents in the
      `inventory` collection where `status` equals
      `"A"` **and** `qty` is less than
      (`$lt`) `30`:

  - id: python
    content: |
      The following example retrieves all documents in the
      `inventory` collection where `status` equals
      `"A"` **and** `qty` is less than
      (`$lt`) `30`:

  - id: motor
    content: |
      The following example retrieves all documents in the
      `inventory` collection where `status` equals
      `"A"` **and** `qty` is less than
      (`$lt`) `30`:

  - id: java-sync
    content: |
      The following example retrieves all documents in the
      `inventory` collection where `status` equals
      `"A"` **and** `qty` is less than
      (`$lt`) `30`:

  - id: java-async
    content: |
      The following example retrieves all documents in the
      `inventory` collection where `status` equals
      `"A"` **and** `qty` is less than
      (`$lt`) `30`:

  - id: kotlin-coroutine
    content: |
      The following example retrieves all documents in the
      `inventory` collection where `status` equals
      `"A"` **and** `qty` is less than
      (`$lt`) `30`:

  - id: nodejs
    content: |
      The following example retrieves all documents in the
      `inventory` collection where `status` equals
      `"A"` **and** `qty` is less than
      (`$lt`) `30`:

  - id: php
    content: |
      The following example retrieves all documents in the
      `inventory` collection where `status` equals
      `"A"` **and** `qty` is less than
      (`$lt`) `30`:

  - id: ruby
    content: |
      The following example retrieves all documents in the
      `inventory` collection where `status` equals
      `"A"` **and** `qty` is less than
      (`$lt`) `30`:

  - id: scala
    content: |
      The following example retrieves all documents in the
      `inventory` collection where `status` equals
      `"A"` **and** `qty` is less than
      (`$lt`) `30`:

  - id: csharp
    content: |
      The following example retrieves all documents in the
      `inventory` collection where `status` equals
      `"A"` **and** `qty` is less than
      (`$lt`) `30`:

  - id: go
    content: |
      The following example retrieves all documents in the
      `inventory` collection where `status` equals
      `"A"` **and** `qty` is less than
      (`$lt`) `30`:

tabs:
  - id: shell
    content: |

      ```javascript
      db.movies.find( { rated: "G", runtime: { $lt: 90 } } )
      ```

  - id: compass
    content: |
      Copy the following filter into the Compass query bar and click
      Find:

      ```javascript
      { status: "A", qty: { $lt: 30 } }
      ```

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

      ```csharp
      var builder = Builders<BsonDocument>.Filter;
      var filter = builder.And(builder.Eq("status", "A"), builder.Lt("qty", 30));
      var result = collection.Find(filter).ToList();
      ```

  - id: go
    content: |
      (Code example not available offline: /driver-examples/go_examples.go)

tabs:
  - id: shell
    content: |
      The operation uses a query predicate of
      `{ rated: "G", runtime: { $lt: 90 } }`, which
      corresponds to the following SQL statement:

      ```sql
      SELECT * FROM movies WHERE rated = "G" AND runtime < 90
      ```

  - id: compass
    content: |
      The operation uses a query predicate of
      `{ status: "A", qty: { $lt: 30 } }`, which
      corresponds to the following SQL statement:

      ```sql
      SELECT * FROM inventory WHERE status = "A" AND qty < 30
      ```

  - id: c
    content: |
      The operation uses a query predicate of
      `{ status: "A", qty: { $lt: 30 } }`, which
      corresponds to the following SQL statement:

      ```sql
      SELECT * FROM inventory WHERE status = "A" AND qty < 30
      ```

  - id: python
    content: |
      The operation uses a query predicate of
      `{ status: "A", qty: { $lt: 30 } }`, which
      corresponds to the following SQL statement:

      ```sql
      SELECT * FROM inventory WHERE status = "A" AND qty < 30
      ```

  - id: motor
    content: |
      The operation uses a query predicate of
      `{ status: "A", qty: { $lt: 30 } }`, which
      corresponds to the following SQL statement:

      ```sql
      SELECT * FROM inventory WHERE status = "A" AND qty < 30
      ```

  - id: java-sync
    content: |
      The operation uses a query predicate of
      `{ status: "A", qty: { $lt: 30 } }`, which
      corresponds to the following SQL statement:

      ```sql
      SELECT * FROM inventory WHERE status = "A" AND qty < 30
      ```

  - id: java-async
    content: |
      The operation uses a query predicate of
      `{ status: "A", qty: { $lt: 30 } }`, which
      corresponds to the following SQL statement:

      ```sql
      SELECT * FROM inventory WHERE status = "A" AND qty < 30
      ```

  - id: kotlin-coroutine
    content: |
      The operation uses a query predicate of
      `{ status: "A", qty: { $lt: 30 } }`, which
      corresponds to the following SQL statement:

      ```sql
      SELECT * FROM inventory WHERE status = "A" AND qty < 30
      ```

  - id: nodejs
    content: |
      The operation uses a query predicate of
      `{ status: "A", qty: { $lt: 30 } }`, which
      corresponds to the following SQL statement:

      ```sql
      SELECT * FROM inventory WHERE status = "A" AND qty < 30
      ```

  - id: php
    content: |
      The operation uses a query predicate of
      `{ status: "A", qty: { $lt: 30 } }`, which
      corresponds to the following SQL statement:

      ```sql
      SELECT * FROM inventory WHERE status = "A" AND qty < 30
      ```

  - id: ruby
    content: |
      The operation uses a query predicate of
      `{ status: "A", qty: { $lt: 30 } }`, which
      corresponds to the following SQL statement:

      ```sql
      SELECT * FROM inventory WHERE status = "A" AND qty < 30
      ```

  - id: scala
    content: |
      The operation uses a query predicate of
      `{ status: "A", qty: { $lt: 30 } }`, which
      corresponds to the following SQL statement:

      ```sql
      SELECT * FROM inventory WHERE status = "A" AND qty < 30
      ```

  - id: csharp
    content: |
      The operation uses a query predicate of
      `{ status: "A", qty: { $lt: 30 } }`, which
      corresponds to the following SQL statement:

      ```sql
      SELECT * FROM inventory WHERE status = "A" AND qty < 30
      ```

  - id: go
    content: |
      The operation uses a query predicate of
      `{ status: "A", qty: { $lt: 30 } }`, which
      corresponds to the following SQL statement:

      ```sql
      SELECT * FROM inventory WHERE status = "A" AND qty < 30
      ```

See comparison operators for other
MongoDB comparison operators.

## Specify `OR` Conditions

Use the `$or` operator to specify a compound query
that joins each clause with a logical `OR` conjunction. The
query selects documents that match at least one
condition.

tabs:
  - id: shell
    content: |
      The following example retrieves all documents in the
      `sample_mflix.movies` collection where `rated`
      equals `"G"` **or** `runtime` is less than
      (`$lt`) `90`:

  - id: compass
    content: |
      The following example retrieves all documents in the
      collection where `status` equals `"A"` **or**
      `qty` is less than (`$lt`) `30`:

  - id: c
    content: |
      The following example retrieves all documents in the
      collection where `status` equals `"A"` **or**
      `qty` is less than (`$lt`) `30`:

  - id: python
    content: |
      The following example retrieves all documents in the
      collection where `status` equals `"A"` **or**
      `qty` is less than (`$lt`) `30`:

  - id: motor
    content: |
      The following example retrieves all documents in the
      collection where `status` equals `"A"` **or**
      `qty` is less than (`$lt`) `30`:

  - id: java-sync
    content: |
      The following example retrieves all documents in the
      collection where `status` equals `"A"` **or**
      `qty` is less than (`$lt`) `30`:

  - id: java-async
    content: |
      The following example retrieves all documents in the
      collection where `status` equals `"A"` **or**
      `qty` is less than (`$lt`) `30`:

  - id: kotlin-coroutine
    content: |
      The following example retrieves all documents in the
      collection where `status` equals `"A"` **or**
      `qty` is less than (`$lt`) `30`:

  - id: nodejs
    content: |
      The following example retrieves all documents in the
      collection where `status` equals `"A"` **or**
      `qty` is less than (`$lt`) `30`:

  - id: php
    content: |
      The following example retrieves all documents in the
      collection where `status` equals `"A"` **or**
      `qty` is less than (`$lt`) `30`:

  - id: ruby
    content: |
      The following example retrieves all documents in the
      collection where `status` equals `"A"` **or**
      `qty` is less than (`$lt`) `30`:

  - id: scala
    content: |
      The following example retrieves all documents in the
      collection where `status` equals `"A"` **or**
      `qty` is less than (`$lt`) `30`:

  - id: csharp
    content: |
      The following example retrieves all documents in the
      collection where `status` equals `"A"` **or**
      `qty` is less than (`$lt`) `30`:

  - id: go
    content: |
      The following example retrieves all documents in the
      collection where `status` equals `"A"` **or**
      `qty` is less than (`$lt`) `30`:

tabs:
  - id: shell
    content: |

      ```javascript
      db.movies.find( { $or: [ { rated: "G" }, { runtime: { $lt: 90 } } ] } )
      ```

  - id: compass
    content: |
      Copy the following filter into the Compass query bar and click
      Find:

      ```javascript
      { $or: [ { status: "A" }, { qty: { $lt: 30 } } ] }
      ```

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

      ```csharp
      var builder = Builders<BsonDocument>.Filter;
      var filter = builder.Or(builder.Eq("status", "A"), builder.Lt("qty", 30));
      var result = collection.Find(filter).ToList();
      ```

  - id: go
    content: |
      (Code example not available offline: /driver-examples/go_examples.go)

tabs:
  - id: shell
    content: |
      The operation uses a query predicate of
      `{ $or: [ { rated: 'G' }, { runtime: { $lt: 90 } } ] }`,
      which corresponds to the following SQL statement:

      ```sql
      SELECT * FROM movies WHERE rated = "G" OR runtime < 90
      ```

  - id: compass
    content: |
      The operation uses a query predicate of
      `{ $or: [ { status: 'A' }, { qty: { $lt: 30 } } ] }`,
      which corresponds to the following SQL statement:

      ```sql
      SELECT * FROM inventory WHERE status = "A" OR qty < 30
      ```

  - id: c
    content: |
      The operation uses a query predicate of
      `{ $or: [ { status: 'A' }, { qty: { $lt: 30 } } ] }`,
      which corresponds to the following SQL statement:

      ```sql
      SELECT * FROM inventory WHERE status = "A" OR qty < 30
      ```

  - id: python
    content: |
      The operation uses a query predicate of
      `{ $or: [ { status: 'A' }, { qty: { $lt: 30 } } ] }`,
      which corresponds to the following SQL statement:

      ```sql
      SELECT * FROM inventory WHERE status = "A" OR qty < 30
      ```

  - id: motor
    content: |
      The operation uses a query predicate of
      `{ $or: [ { status: 'A' }, { qty: { $lt: 30 } } ] }`,
      which corresponds to the following SQL statement:

      ```sql
      SELECT * FROM inventory WHERE status = "A" OR qty < 30
      ```

  - id: java-sync
    content: |
      The operation uses a query predicate of
      `{ $or: [ { status: 'A' }, { qty: { $lt: 30 } } ] }`,
      which corresponds to the following SQL statement:

      ```sql
      SELECT * FROM inventory WHERE status = "A" OR qty < 30
      ```

  - id: java-async
    content: |
      The operation uses a query predicate of
      `{ $or: [ { status: 'A' }, { qty: { $lt: 30 } } ] }`,
      which corresponds to the following SQL statement:

      ```sql
      SELECT * FROM inventory WHERE status = "A" OR qty < 30
      ```

  - id: kotlin-coroutine
    content: |
      The operation uses a query predicate of
      `{ $or: [ { status: 'A' }, { qty: { $lt: 30 } } ] }`,
      which corresponds to the following SQL statement:

      ```sql
      SELECT * FROM inventory WHERE status = "A" OR qty < 30
      ```

  - id: nodejs
    content: |
      The operation uses a query predicate of
      `{ $or: [ { status: 'A' }, { qty: { $lt: 30 } } ] }`,
      which corresponds to the following SQL statement:

      ```sql
      SELECT * FROM inventory WHERE status = "A" OR qty < 30
      ```

  - id: php
    content: |
      The operation uses a query predicate of
      `{ $or: [ { status: 'A' }, { qty: { $lt: 30 } } ] }`,
      which corresponds to the following SQL statement:

      ```sql
      SELECT * FROM inventory WHERE status = "A" OR qty < 30
      ```

  - id: ruby
    content: |
      The operation uses a query predicate of
      `{ $or: [ { status: 'A' }, { qty: { $lt: 30 } } ] }`,
      which corresponds to the following SQL statement:

      ```sql
      SELECT * FROM inventory WHERE status = "A" OR qty < 30
      ```

  - id: scala
    content: |
      The operation uses a query predicate of
      `{ $or: [ { status: 'A' }, { qty: { $lt: 30 } } ] }`,
      which corresponds to the following SQL statement:

      ```sql
      SELECT * FROM inventory WHERE status = "A" OR qty < 30
      ```

  - id: csharp
    content: |
      The operation uses a query predicate of
      `{ $or: [ { status: 'A' }, { qty: { $lt: 30 } } ] }`,
      which corresponds to the following SQL statement:

      ```sql
      SELECT * FROM inventory WHERE status = "A" OR qty < 30
      ```

  - id: go
    content: |
      The operation uses a query predicate of
      `{ $or: [ { status: 'A' }, { qty: { $lt: 30 } } ] }`,
      which corresponds to the following SQL statement:

      ```sql
      SELECT * FROM inventory WHERE status = "A" OR qty < 30
      ```

**Note:**

Queries with comparison operators are subject to type-bracketing.

## Specify `AND` as well as `OR` Conditions

tabs:
  - id: shell
    content: |
      In the following example, the compound query document
      selects all documents in the
      `sample_mflix.movies` collection where `rated`
      equals `"G"` **and** *either* `runtime` is less
      than (`$lt`) `90` *or* `title` starts
      with the character `T`:

  - id: compass
    content: |
      In the following example, the compound query document
      selects all documents in the collection where
      `status` equals `"A"` **and** *either* `qty`
      is less than (`$lt`) `30` *or* `item`
      starts with the character `p`:

  - id: c
    content: |
      In the following example, the compound query document
      selects all documents in the collection where
      `status` equals `"A"` **and** *either* `qty`
      is less than (`$lt`) `30` *or* `item`
      starts with the character `p`:

  - id: python
    content: |
      In the following example, the compound query document
      selects all documents in the collection where
      `status` equals `"A"` **and** *either* `qty`
      is less than (`$lt`) `30` *or* `item`
      starts with the character `p`:

  - id: motor
    content: |
      In the following example, the compound query document
      selects all documents in the collection where
      `status` equals `"A"` **and** *either* `qty`
      is less than (`$lt`) `30` *or* `item`
      starts with the character `p`:

  - id: java-sync
    content: |
      In the following example, the compound query document
      selects all documents in the collection where
      `status` equals `"A"` **and** *either* `qty`
      is less than (`$lt`) `30` *or* `item`
      starts with the character `p`:

  - id: java-async
    content: |
      In the following example, the compound query document
      selects all documents in the collection where
      `status` equals `"A"` **and** *either* `qty`
      is less than (`$lt`) `30` *or* `item`
      starts with the character `p`:

  - id: kotlin-coroutine
    content: |
      In the following example, the compound query document
      selects all documents in the collection where
      `status` equals `"A"` **and** *either* `qty`
      is less than (`$lt`) `30` *or* `item`
      starts with the character `p`:

  - id: nodejs
    content: |
      In the following example, the compound query document
      selects all documents in the collection where
      `status` equals `"A"` **and** *either* `qty`
      is less than (`$lt`) `30` *or* `item`
      starts with the character `p`:

  - id: php
    content: |
      In the following example, the compound query document
      selects all documents in the collection where
      `status` equals `"A"` **and** *either* `qty`
      is less than (`$lt`) `30` *or* `item`
      starts with the character `p`:

  - id: ruby
    content: |
      In the following example, the compound query document
      selects all documents in the collection where
      `status` equals `"A"` **and** *either* `qty`
      is less than (`$lt`) `30` *or* `item`
      starts with the character `p`:

  - id: scala
    content: |
      In the following example, the compound query document
      selects all documents in the collection where
      `status` equals `"A"` **and** *either* `qty`
      is less than (`$lt`) `30` *or* `item`
      starts with the character `p`:

  - id: csharp
    content: |
      In the following example, the compound query document
      selects all documents in the collection where
      `status` equals `"A"` **and** *either* `qty`
      is less than (`$lt`) `30` *or* `item`
      starts with the character `p`:

  - id: go
    content: |
      In the following example, the compound query document
      selects all documents in the collection where
      `status` equals `"A"` **and** *either* `qty`
      is less than (`$lt`) `30` *or* `item`
      starts with the character `p`:

tabs:
  - id: shell
    content: |

      ```javascript
      db.movies.find( {
           rated: "G",
           $or: [ { runtime: { $lt: 90 } }, { title: /^T/ } ]
      } )
      ```

  - id: compass
    content: |
      Copy the following filter into the Compass query bar and click
      Find:

      ```javascript
      { status: "A", $or: [ { qty: { $lt: 30 } }, { item: /^p/ } ] }
      ```

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

      ```csharp
      var builder = Builders<BsonDocument>.Filter;
      var filter = builder.And(
          builder.Eq("status", "A"),
          builder.Or(builder.Lt("qty", 30), builder.Regex("item", new BsonRegularExpression("^p"))));
      var result = collection.Find(filter).ToList();
      ```

  - id: go
    content: |
      (Code example not available offline: /driver-examples/go_examples.go)

The operation uses a query predicate of:

tabs:
  - id: shell
    content: |

      ```javascript
      {
         rated: 'G',
         $or: [
           { runtime: { $lt: 90 } },
           { title: { $regex: '^T' } }
         ]
      }
      ```

      which corresponds to the following SQL statement:

      ```sql
      SELECT * FROM movies WHERE rated = "G"
      AND ( runtime < 90 OR title LIKE "T%")
      ```

  - id: compass
    content: |

      ```javascript
      {
         status: 'A',
         $or: [
           { qty: { $lt: 30 } },
           { item: { $regex: '^p' } }
         ]
      }
      ```

      which corresponds to the following SQL statement:

      ```sql
      SELECT * FROM inventory WHERE status = "A"
      AND ( qty < 30 OR item LIKE "p%")
      ```

  - id: c
    content: |

      ```javascript
      {
         status: 'A',
         $or: [
           { qty: { $lt: 30 } },
           { item: { $regex: '^p' } }
         ]
      }
      ```

      which corresponds to the following SQL statement:

      ```sql
      SELECT * FROM inventory WHERE status = "A"
      AND ( qty < 30 OR item LIKE "p%")
      ```

  - id: python
    content: |

      ```javascript
      {
         status: 'A',
         $or: [
           { qty: { $lt: 30 } },
           { item: { $regex: '^p' } }
         ]
      }
      ```

      which corresponds to the following SQL statement:

      ```sql
      SELECT * FROM inventory WHERE status = "A"
      AND ( qty < 30 OR item LIKE "p%")
      ```

  - id: motor
    content: |

      ```javascript
      {
         status: 'A',
         $or: [
           { qty: { $lt: 30 } },
           { item: { $regex: '^p' } }
         ]
      }
      ```

      which corresponds to the following SQL statement:

      ```sql
      SELECT * FROM inventory WHERE status = "A"
      AND ( qty < 30 OR item LIKE "p%")
      ```

  - id: java-sync
    content: |

      ```javascript
      {
         status: 'A',
         $or: [
           { qty: { $lt: 30 } },
           { item: { $regex: '^p' } }
         ]
      }
      ```

      which corresponds to the following SQL statement:

      ```sql
      SELECT * FROM inventory WHERE status = "A"
      AND ( qty < 30 OR item LIKE "p%")
      ```

  - id: java-async
    content: |

      ```javascript
      {
         status: 'A',
         $or: [
           { qty: { $lt: 30 } },
           { item: { $regex: '^p' } }
         ]
      }
      ```

      which corresponds to the following SQL statement:

      ```sql
      SELECT * FROM inventory WHERE status = "A"
      AND ( qty < 30 OR item LIKE "p%")
      ```

  - id: kotlin-coroutine
    content: |

      ```javascript
      {
         status: 'A',
         $or: [
           { qty: { $lt: 30 } },
           { item: { $regex: '^p' } }
         ]
      }
      ```

      which corresponds to the following SQL statement:

      ```sql
      SELECT * FROM inventory WHERE status = "A"
      AND ( qty < 30 OR item LIKE "p%")
      ```

  - id: nodejs
    content: |

      ```javascript
      {
         status: 'A',
         $or: [
           { qty: { $lt: 30 } },
           { item: { $regex: '^p' } }
         ]
      }
      ```

      which corresponds to the following SQL statement:

      ```sql
      SELECT * FROM inventory WHERE status = "A"
      AND ( qty < 30 OR item LIKE "p%")
      ```

  - id: php
    content: |

      ```javascript
      {
         status: 'A',
         $or: [
           { qty: { $lt: 30 } },
           { item: { $regex: '^p' } }
         ]
      }
      ```

      which corresponds to the following SQL statement:

      ```sql
      SELECT * FROM inventory WHERE status = "A"
      AND ( qty < 30 OR item LIKE "p%")
      ```

  - id: ruby
    content: |

      ```javascript
      {
         status: 'A',
         $or: [
           { qty: { $lt: 30 } },
           { item: { $regex: '^p' } }
         ]
      }
      ```

      which corresponds to the following SQL statement:

      ```sql
      SELECT * FROM inventory WHERE status = "A"
      AND ( qty < 30 OR item LIKE "p%")
      ```

  - id: scala
    content: |

      ```javascript
      {
         status: 'A',
         $or: [
           { qty: { $lt: 30 } },
           { item: { $regex: '^p' } }
         ]
      }
      ```

      which corresponds to the following SQL statement:

      ```sql
      SELECT * FROM inventory WHERE status = "A"
      AND ( qty < 30 OR item LIKE "p%")
      ```

  - id: csharp
    content: |

      ```javascript
      {
         status: 'A',
         $or: [
           { qty: { $lt: 30 } },
           { item: { $regex: '^p' } }
         ]
      }
      ```

      which corresponds to the following SQL statement:

      ```sql
      SELECT * FROM inventory WHERE status = "A"
      AND ( qty < 30 OR item LIKE "p%")
      ```

  - id: go
    content: |

      ```javascript
      {
         status: 'A',
         $or: [
           { qty: { $lt: 30 } },
           { item: { $regex: '^p' } }
         ]
      }
      ```

      which corresponds to the following SQL statement:

      ```sql
      SELECT * FROM inventory WHERE status = "A"
      AND ( qty < 30 OR item LIKE "p%")
      ```

**Note:**

MongoDB supports regular expression `$regex` queries to
perform string pattern matches. 

Regular expression syntax differs between `mongosh` and drivers. 
`mongosh` uses JavaScript regex literals (for example, `{ title: /^T/ }`).
The drivers use the equivalent `$regex` operator (for example,
`{ title: { $regex: '^T' } }`). 

## Query Documents with MongoDB Atlas

This example uses the sample movies dataset. To load the sample dataset 
into your MongoDB Atlas deployment, see Load Sample Data.

To project fields for a query in MongoDB Atlas, follow these
steps:

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

a. For the cluster that contains the sample data,
   click Browse Collections.
#. In the left navigation pane, select the
   `sample_mflix` database.
#. Select the `movies` collection.

**Step 3: Specify the Filter field**

Specify the query filter document
in the Filter field. A query filter document uses 
query operators to specify
search conditions.

Copy the following query filter document into the 
Filter search bar:

```javascript
{ year: 1924 }
```

**Step 4: Click Apply**

The query returns all documents
in the `sample_mflix.movies` collection where the `year`
field matches `1924`.

## Additional Query Tutorials

For more query examples, see:

- /tutorial/query-embedded-documents
- /tutorial/query-arrays
- /tutorial/query-array-of-documents
- /tutorial/project-fields-from-query-results
- /tutorial/query-for-null-fields

## Behavior

### Cursor

tabs:
  - id: shell
    content: |
      The `db.collection.find()` method
      returns a cursor to the matching
      documents.

  - id: compass
    content: |
      The Find operation opens a
      cursor to the matching
      documents of the collection based on the find query.

      For more information on sampling, see the
      Compass FAQ.

  - id: c
    content: |
      The [mongoc_collection_find_with_opts](https://mongoc.org/libmongoc/current/mongoc_collection_find_with_opts.html) 
      method returns a cursor to the
      matching documents.

  - id: python
    content: |
      The `pymongo.collection.Collection.find` method
      returns a cursor to the
      matching documents. See the PyMongo documentation for
      [iterating over a cursor](https://pymongo.readthedocs.io/en/stable/tutorial.html#querying-for-more-than-one-document).

  - id: motor
    content: |
      The `pymongo.asynchronous.collection.AsyncCollection.find`
      method returns a cursor to the
      matching documents.

  - id: java-sync
    content: |
      The com.mongodb.client.MongoCollection.find_ method returns an
      instance of the com.mongodb.client.FindIterable_ interface.

  - id: java-async
    content: |
      [com.mongodb.reactivestreams.client.MongoCollection.find](http://mongodb.github.io/mongo-java-driver-reactivestreams/1.6/javadoc/com/mongodb/reactivestreams/client/MongoCollection.html#find())
      returns an instance of the [com.mongodb.reactivestreams.client.FindPublisher](http://mongodb.github.io/mongo-java-driver-reactivestreams/1.6/javadoc/com/mongodb/reactivestreams/client/FindPublisher.html)
      interface.

  - id: kotlin-coroutine
    content: |
      The [MongoCollection.find()](https://mongodb.github.io/mongo-java-driver/{+java-driver-version+}/apidocs/driver-kotlin-coroutine/mongodb-driver-kotlin-coroutine/com.mongodb.kotlin.client.coroutine/-mongo-collection/find.html) method returns an
      instance of the
      [FindFlow](https://mongodb.github.io/mongo-java-driver/{+java-driver-version+}/apidocs/driver-kotlin-coroutine/mongodb-driver-kotlin-coroutine/com.mongodb.kotlin.client.coroutine/-find-flow/index.html)
      class.

  - id: nodejs
    content: |
      The `Collection.find()` method
      returns a `cursor`.

  - id: php
    content: |
      The `MongoDBCollection::find()`
      method returns a cursor to
      the matching documents. See the MongoDB PHP Library
      documentation for
      iterating over a cursor.

  - id: ruby
    content: |
      The `Mongo::Collection#find()`
      method returns a `CollectionView`,
      which is an `Enumerable`. A `Cursor` is
      created when the `View` is enumerated; for example, by calling
      `#to_a()` or `#each()`. You can also get an `Enumerator` by calling
      `#to_enum()` on the `View`. See the Ruby driver API documentation
      for [iterating over a cursor](https://www.mongodb.com/docs/ruby-driver/current/api/Mongo/Cursor.html#each-instance_method).

  - id: scala
    content: |
      The `collection.find()`
      method returns the find [Observable](http://mongodb.github.io/mongo-scala-driver/2.1/reference/observables/).

  - id: csharp
    content: |
      The `MongoCollection.Find()`
      method returns a cursor to
      the matching documents. See the MongoDB .NET/C# Driver
      documentation for [iterating over a cursor](https://www.mongodb.com/docs/drivers/csharp/v2.19/fundamentals/crud/read-operations/retrieve/#find-multiple-documents).

  - id: go
    content: |

       The `Collection.Find`
       function returns a `Cursor` to the
       matching documents. See the `Cursor`
       documentation for more information.

### Concurrent Updates While Using a Cursor

As a cursor returns documents, other operations may run in the 
background and affect the results, depending on the read concern level. 
For details, see read-isolation-consistency-recency.

### Read Isolation

For reads to replica sets and replica set
shards, read concern lets clients choose an
isolation level for their reads. For more information, see
/reference/read-concern.

### Query Result Format

When you run a find operation with a MongoDB driver or `mongosh`,
MongoDB returns a cursor that manages query results. Query
results are not returned as an array of documents.

To learn how to iterate through documents in a cursor, see your
`driver's documentation`. If you are using `mongosh`, see
read-operations-cursors.

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
