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

## Delete All Documents

tabs:
  - id: shell
    content: |

      To delete all documents from a collection, pass an empty
      filter document `{}` to the
      `db.collection.deleteMany()` method.

      The following example deletes *all* documents from the `inventory`
      collection:

  - id: python
    content: |

      To delete all documents from a collection, pass an empty
      filter document `{}` to the
      `pymongo.collection.Collection.delete_many` method.

      The following example deletes *all* documents from the `inventory`
      collection:

  - id: motor
    content: |

      To delete all documents from a collection, pass an empty
      filter document `{}` to the
      `motor.motor_asyncio.AsyncIOMotorCollection.delete_many`
      method.

      The following example deletes *all* documents from the `inventory`
      collection:

  - id: java-sync
    content: |

      To delete all documents from a collection, pass an empty
      org.bson.Document_ object as the
      filter to the
      com.mongodb.client.MongoCollection.deleteMany_ method.

      The following example deletes *all* documents from the `inventory`
      collection:

  - id: java-async
    content: |

      To delete all documents from a collection, pass an empty
      org.bson.Document_ object as the
      filter to the
      [com.mongodb.reactivestreams.client.MongoCollection.deleteMany](http://mongodb.github.io/mongo-java-driver-reactivestreams/1.6/javadoc/com/mongodb/reactivestreams/client/MongoCollection.html#deleteMany(org.bson.conversions.Bson))
      method.

      The following example deletes *all* documents from the `inventory`
      collection:

  - id: nodejs
    content: |

      To delete all documents from a collection, pass an empty
      filter document `{}` to the
      `Collection.deleteMany()`
      method.

      The following example deletes *all* documents from the `inventory`
      collection:

  - id: php
    content: |

      To delete all documents from a collection, pass an empty
      filter document `[]` to the
      `MongoDBCollection::deleteMany()`
      method.

      The following example deletes *all* documents from the `inventory`
      collection:

  - id: ruby
    content: |

      To delete all documents from a collection, pass an empty
      filter document `{}` to the
      `Mongo::Collection#delete_many()`
      method.

      The following example deletes *all* documents from the `inventory`
      collection:

  - id: scala
    content: |

      To delete all documents from a collection, pass an empty
      filter `Document()` to the
      `collection.deleteMany()`
      method.

      The following example deletes *all* documents from the `inventory`
      collection:

  - id: csharp
    content: |

      To delete all documents from a collection, pass an empty
      filter
      `Builders<BsonDocument>.Filter.Empty` to the
      `IMongoCollection.DeleteMany()` method.

      The following example deletes *all* documents from the `inventory`
      collection:

  - id: go
    content: |

      To delete all documents from a collection, pass an empty
      filter document to the
      `Collection.DeleteMany` function.

      The following example deletes *all* documents from the `inventory`
      collection:

tabs:
  - id: shell
    content: |

      ```javascript
      db.inventory.deleteMany({})
      ```

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

tabs:
  - id: shell
    content: |
      The method returns a document with the status of the operation. For
      more information and examples, see
      `deleteMany()`.

  - id: python
    content: |
      The `delete_many`
      method returns an instance of
      `pymongo.results.DeleteResult` with the status of the
      operation.

  - id: motor
    content: |
      The `delete_many`
      coroutine asynchronously returns an instance of
      `pymongo.results.DeleteResult` with the status of the
      operation.

  - id: java-sync
    content: |
      The com.mongodb.client.MongoCollection.deleteMany_
      method returns an instance of
      com.mongodb.client.result.DeleteResult_
      with the status of the
      operation.

  - id: java-async
    content: |
      [com.mongodb.reactivestreams.client.MongoCollection.deleteMany](http://mongodb.github.io/mongo-java-driver-reactivestreams/1.6/javadoc/com/mongodb/reactivestreams/client/MongoCollection.html#deleteMany(org.bson.conversions.Bson))
      returns a [Publisher](http://www.reactive-streams.org/reactive-streams-1.0.1-javadoc/org/reactivestreams/Publisher.html)
      object of type com.mongodb.client.result.DeleteResult_ if
      successful. Returns an instance of `com.mongodb.MongoException` if unsuccessful.

  - id: nodejs
    content: |
      `Collection.deleteMany()` 
      returns a promise that provides a `result`. The `result.deletedCount`
      property contains the number of documents that matched the
      filter.

  - id: php
    content: |
      Upon successful execution, the
      `deleteMany()`
      method returns an instance of
      `MongoDBDeleteResult`
      whose `getDeletedCount()`
      method returns the number of documents that matched the filter.

  - id: ruby
    content: |
      Upon successful execution, the
      `delete_many()` method
      returns an instance of
      `Mongo::Operation::Result`, whose
      `deleted_count` attribute contains the number of documents
      that matched the filter.

  - id: scala
    content: |
      Upon successful execution, the
      `collection.deleteMany()` method
      returns an
      [Observable](http://mongodb.github.io/mongo-scala-driver/2.1/reference/observables/)
      with a single element with a `DeleteResult` type parameter or with
      an `com.mongodb.MongoException`.

  - id: csharp
    content: |
      Upon successful execution, the
      `IMongoCollection.DeleteMany()`
      method returns an instance of
      `DeleteResult` whose
      `DeletedCount` property contains the number of documents
      that matched the filter.

  - id: go
    content: |
      Upon successful execution, the
      `Collection.DeleteMany`
      function returns an instance of
      `DeleteResult` whose
      `DeletedCount` property contains the number of documents
      that matched the filter.

## Delete All Documents that Match a Condition

tabs:
  - id: shell
    content: |

      You can specify criteria, or filters, that identify the documents to
      delete. The filters use the same syntax
      as read operations.

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

      tabs:
        - id: shell
          content: |
            A query filter document can
            use the query operators to specify
            conditions in the following form:

            ```javascript
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

        - id: perl
          content: |
            A query filter document can
            use the query operators to specify
            conditions in the following form:

            ```perl
            { <field1> => { <operator1> => <value1> }, ... }
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

      To delete all documents that match a deletion criteria, pass a
      filter parameter to the
      `deleteMany()` method.

      The following example removes all documents from the `inventory`
      collection where the `status` field equals `"A"`:

  - id: python
    content: |

      You can specify criteria, or filters, that identify the documents to
      delete. The filters use the same syntax
      as read operations.

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

      tabs:
        - id: shell
          content: |
            A query filter document can
            use the query operators to specify
            conditions in the following form:

            ```javascript
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

        - id: perl
          content: |
            A query filter document can
            use the query operators to specify
            conditions in the following form:

            ```perl
            { <field1> => { <operator1> => <value1> }, ... }
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

      To delete all documents that match a deletion criteria, pass a
      filter parameter to the
      `delete_many` method.

      The following example removes all documents from the `inventory`
      collection where the `status` field equals `"A"`:

  - id: motor
    content: |

      You can specify criteria, or filters, that identify the documents to
      delete. The filters use the same syntax
      as read operations.

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

      tabs:
        - id: shell
          content: |
            A query filter document can
            use the query operators to specify
            conditions in the following form:

            ```javascript
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

        - id: perl
          content: |
            A query filter document can
            use the query operators to specify
            conditions in the following form:

            ```perl
            { <field1> => { <operator1> => <value1> }, ... }
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

      To delete all documents that match a deletion criteria, pass a
      filter parameter to the
      `delete_many`
      method.

      The following example removes all documents from the `inventory`
      collection where the `status` field equals `"A"`:

  - id: java-sync
    content: |

      You can specify criteria, or filters, that identify the documents to
      delete. The filters use the same syntax
      as read operations.

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

      tabs:
        - id: shell
          content: |
            A query filter document can
            use the query operators to specify
            conditions in the following form:

            ```javascript
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

        - id: perl
          content: |
            A query filter document can
            use the query operators to specify
            conditions in the following form:

            ```perl
            { <field1> => { <operator1> => <value1> }, ... }
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

      To delete all documents that match a deletion criteria, pass a
      filter parameter to the
      com.mongodb.client.MongoCollection.deleteMany_ method.

      The following example removes all documents from the `inventory`
      collection where the `status` field equals `"A"`:

  - id: java-async
    content: |

      You can specify criteria, or filters, that identify the documents to
      delete. The filters use the same syntax
      as read operations.

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

      tabs:
        - id: shell
          content: |
            A query filter document can
            use the query operators to specify
            conditions in the following form:

            ```javascript
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

        - id: perl
          content: |
            A query filter document can
            use the query operators to specify
            conditions in the following form:

            ```perl
            { <field1> => { <operator1> => <value1> }, ... }
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

      To delete all documents that match a deletion criteria, pass a
      filter parameter to the
      [com.mongodb.reactivestreams.client.MongoCollection.deleteMany](http://mongodb.github.io/mongo-java-driver-reactivestreams/1.6/javadoc/com/mongodb/reactivestreams/client/MongoCollection.html#deleteMany(org.bson.conversions.Bson))
      method.

      The following example removes all documents from the `inventory`
      collection where the `status` field equals `"A"`:

  - id: nodejs
    content: |

      You can specify criteria, or filters, that identify the documents to
      delete. The filters use the same syntax
      as read operations.

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

      tabs:
        - id: shell
          content: |
            A query filter document can
            use the query operators to specify
            conditions in the following form:

            ```javascript
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

        - id: perl
          content: |
            A query filter document can
            use the query operators to specify
            conditions in the following form:

            ```perl
            { <field1> => { <operator1> => <value1> }, ... }
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

      To delete all documents that match a deletion criteria, pass a
      filter parameter to the
      `deleteMany()`
      method.

      The following example removes all documents from the `inventory`
      collection where the `status` field equals `"A"`:

  - id: php
    content: |

      You can specify criteria, or filters, that identify the documents to
      delete. The filters use the same syntax
      as read operations.

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

      tabs:
        - id: shell
          content: |
            A query filter document can
            use the query operators to specify
            conditions in the following form:

            ```javascript
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

        - id: perl
          content: |
            A query filter document can
            use the query operators to specify
            conditions in the following form:

            ```perl
            { <field1> => { <operator1> => <value1> }, ... }
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

      To delete all documents that match a deletion criteria, pass a
      filter parameter to the
      `deleteMany()`
      method.

      The following example removes all documents from the `inventory`
      collection where the `status` field equals `"A"`:

  - id: ruby
    content: |

      You can specify criteria, or filters, that identify the documents to
      delete. The filters use the same syntax
      as read operations.

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

      tabs:
        - id: shell
          content: |
            A query filter document can
            use the query operators to specify
            conditions in the following form:

            ```javascript
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

        - id: perl
          content: |
            A query filter document can
            use the query operators to specify
            conditions in the following form:

            ```perl
            { <field1> => { <operator1> => <value1> }, ... }
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

      To delete all documents that match a deletion criteria, pass a
      filter parameter to the
      `delete_many()`
      method.

      The following example removes all documents from the `inventory`
      collection where the `status` field equals `"A"`:

  - id: scala
    content: |

      You can specify criteria, or filters, that identify the documents to
      delete. The filters use the same syntax
      as read operations.

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

      tabs:
        - id: shell
          content: |
            A query filter document can
            use the query operators to specify
            conditions in the following form:

            ```javascript
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

        - id: perl
          content: |
            A query filter document can
            use the query operators to specify
            conditions in the following form:

            ```perl
            { <field1> => { <operator1> => <value1> }, ... }
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

      To delete all documents that match a deletion criteria, pass a
      filter parameter to the
      `deleteMany()`
      method.

      The following example removes all documents from the `inventory`
      collection where the `status` field equals `"A"`:

  - id: csharp
    content: |

      You can specify criteria, or filters, that identify the documents to
      delete. The filters use the same syntax
      as read operations.

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

      tabs:
        - id: shell
          content: |
            A query filter document can
            use the query operators to specify
            conditions in the following form:

            ```javascript
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

        - id: perl
          content: |
            A query filter document can
            use the query operators to specify
            conditions in the following form:

            ```perl
            { <field1> => { <operator1> => <value1> }, ... }
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

      To delete all documents that match a deletion criteria, pass a
      filter parameter to the
      `IMongoCollection.DeleteMany()`
      method.

      The following example removes all documents from the `inventory`
      collection where the `status` field equals `"A"`:

  - id: go
    content: |

      You can specify criteria, or filters, that identify the documents to
      delete. The filters use the same syntax
      as read operations.

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

      tabs:
        - id: shell
          content: |
            A query filter document can
            use the query operators to specify
            conditions in the following form:

            ```javascript
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

        - id: perl
          content: |
            A query filter document can
            use the query operators to specify
            conditions in the following form:

            ```perl
            { <field1> => { <operator1> => <value1> }, ... }
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

      To delete all documents that match a deletion criteria, pass a
      filter parameter to the
      `Collection.DeleteMany` function.

      The following example removes all documents from the `inventory`
      collection where the `status` field equals `"A"`:

tabs:
  - id: shell
    content: |

      ```javascript
      db.inventory.deleteMany({ status : "A" })
      ```

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

tabs:
  - id: shell
    content: |
      The method returns a document with the status of the operation. For
      more information and examples, see
      `deleteMany()`.

  - id: python
    content: |
      The `delete_many`
      method returns an instance of
      `pymongo.results.DeleteResult` with the status of the
      operation.

  - id: motor
    content: |
      The `delete_many`
      coroutine asynchronously returns an instance of
      `pymongo.results.DeleteResult` with the status of the
      operation.

  - id: java-sync
    content: |
      The com.mongodb.client.MongoCollection.deleteMany_
      method returns an instance of
      com.mongodb.client.result.DeleteResult_
      with the status of the
      operation.

  - id: java-async
    content: |
      [com.mongodb.reactivestreams.client.MongoCollection.deleteMany](http://mongodb.github.io/mongo-java-driver-reactivestreams/1.6/javadoc/com/mongodb/reactivestreams/client/MongoCollection.html#deleteMany(org.bson.conversions.Bson))
      returns a [Publisher](http://www.reactive-streams.org/reactive-streams-1.0.1-javadoc/org/reactivestreams/Publisher.html)
      object of type com.mongodb.client.result.DeleteResult_ if
      successful. Returns an instance of `com.mongodb.MongoException` if unsuccessful.

  - id: nodejs
    content: |
      `Collection.deleteMany()` 
      returns a promise that provides a `result`. The `result.deletedCount`
      property contains the number of documents that matched the
      filter.

  - id: php
    content: |
      Upon successful execution, the
      `deleteMany()`
      method returns an instance of
      `MongoDBDeleteResult`
      whose `getDeletedCount()`
      method returns the number of documents that matched the filter.

  - id: ruby
    content: |
      Upon successful execution, the
      `delete_many()` method
      returns an instance of
      `Mongo::Operation::Result`, whose
      `deleted_count` attribute contains the number of documents
      that matched the filter.

  - id: scala
    content: |
      Upon successful execution, the
      `collection.deleteMany()` method
      returns an
      [Observable](http://mongodb.github.io/mongo-scala-driver/2.1/reference/observables/)
      with a single element with a `DeleteResult` type parameter or with
      an `com.mongodb.MongoException`.

  - id: csharp
    content: |
      Upon successful execution, the
      `IMongoCollection.DeleteMany()`
      method returns an instance of
      `DeleteResult` whose
      `DeletedCount` property contains the number of documents
      that matched the filter.

  - id: go
    content: |
      Upon successful execution, the
      `Collection.DeleteMany`
      function returns an instance of
      `DeleteResult` whose
      `DeletedCount` property contains the number of documents
      that matched the filter.

## Delete Only One Document that Matches a Condition

tabs:
  - id: shell
    content: |

      To delete at most a single document that matches a specified
      filter (even though multiple documents may match the specified
      filter) use the `db.collection.deleteOne()` method.

      The following example deletes the *first* document where `status` is
      `"D"`:

  - id: compass
    content: |

      MongoDB Compass provides a simple way to delete a document
      from a collection. The following example shows how to delete
      the document with `item` equal to `paper` from the
      `inventory` collection:

      **Note:**

      In this example we are using the Compass Table View to 
      delete the document. The deletion process using the Compass
      List View follows a very similar approach.

      For more information on the differences between Table View
      and List View in Compass, refer to the
      Compass documentation.

  - id: python
    content: |

      To delete at most a single document that matches a specified
      filter (even though multiple documents may match the specified
      filter) use the
      `pymongo.collection.Collection.delete_one` method.

      The following example deletes the *first* document where `status` is
      `"D"`:

  - id: motor
    content: |

      To delete at most a single document that matches a specified
      filter (even though multiple documents may match the specified
      filter) use the
      `motor.motor_asyncio.AsyncIOMotorCollection.delete_one`
      method.

      The following example deletes the *first* document where `status` is
      `"D"`:

  - id: java-sync
    content: |

      To delete at most a single document that matches a specified
      filter (even though multiple documents may match the specified
      filter) use the com.mongodb.client.MongoCollection.deleteOne_
      method.

      The following example deletes the *first* document where `status` is
      `"D"`:

  - id: java-async
    content: |

      To delete at most a single document that matches a specified
      filter (even though multiple documents may match the specified
      filter) use the [com.mongodb.reactivestreams.client.MongoCollection.deleteMany](http://mongodb.github.io/mongo-java-driver-reactivestreams/1.6/javadoc/com/mongodb/reactivestreams/client/MongoCollection.html#deleteMany(org.bson.conversions.Bson))
      method.

      The following example deletes the *first* document where `status` is
      `"D"`:

  - id: nodejs
    content: |

      To delete at most a single document that matches a specified
      filter (even though multiple documents may match the specified
      filter) use the
      `Collection.deleteOne()`
      method.

      The following example deletes the *first* document where `status` is
      `"D"`:

  - id: php
    content: |

      To delete at most a single document that matches a specified
      filter (even though multiple documents may match the specified
      filter) use the
      `MongoDBCollection::deleteOne()`
      method.

      The following example deletes the *first* document where `status` is
      `"D"`:

  - id: ruby
    content: |

      To delete at most a single document that matches a specified
      filter (even though multiple documents may match the specified
      filter) use the
      `Mongo::Collection#delete_one()`
      method.

      The following example deletes the *first* document where `status` is
      `"D"`:

  - id: csharp
    content: |

      To delete at most a single document that matches a specified
      filter (even though multiple documents may match the specified
      filter) use the
      `IMongoCollection.DeleteOne()`
      method.

      The following example deletes the *first* document where `status` is
      `"D"`:

  - id: scala
    content: |

      To delete at most a single document that matches a specified
      filter (even though multiple documents may match the specified
      filter) use the
      `collection.deleteOne()`
      method.

      The following example deletes the *first* document where `status` is
      `"D"`:

  - id: go
    content: |

      To delete at most a single document that matches a specified
      filter (even though multiple documents may match the specified
      filter) use the
      `Collection.DeleteOne` function.

      The following example deletes the *first* document where `status` is
      `"D"`:

tabs:
  - id: shell
    content: |

      ```javascript
      db.inventory.deleteOne( { status: "D" } )
      ```

  - id: compass
    content: |

      1. Click the Table button in the top navigation
         to access the Table View:

         (Figure: /images/compass-table-btn-click-2.png)

      #. Use the Compass query bar to
         locate the target document.

         Copy the following filter document into the query bar and click
         Find:

         ```javascript
         { item: "paper" }
         ```

         (Figure: /images/compass-delete-paper-find.png)

      #. Hover over the document and click the trash icon which
         appears on the right-hand side:

         (Figure: /images/compass-delete-button-click.png)

         After clicking the delete button, the document is flagged
         for deletion and Compass asks for confirmation that you
         want to remove the document:

         (Figure: /images/compass-delete-confirm.png)

      #. Click Delete to confirm. Compass deletes the
         document from the collection.

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

## Delete a Document with MongoDB Atlas

**Note:**

You can delete only one document at a time in the MongoDB Atlas UI.
To delete multiple documents, connect to your 
Atlas deployment from `mongosh` or a MongoDB driver
and follow the examples on this page for your preferred method.

The example in this section uses the sample movies dataset. To learn how to load the sample dataset 
into your MongoDB Atlas deployment, see Load Sample Data.

To delete a document in MongoDB Atlas, follow these steps:

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

**Step 2: Navigate to the collection.**

a. For the cluster that contains the sample data,
   click Browse Collections.
#. In the left navigation pane, select the
   `sample_mflix` database.
#. Select the `movies` collection.

**Step 3: Specify a query filter document.**

Optionally, you can specify a query filter document
in the Filter field. A query filter document uses 
query operators to specify search conditions.

Copy the following query filter document into the 
Filter search bar and click Apply:

```javascript
{ genres: "Action", rated: { $in: [ "PG", "PG-13" ] } }
```

This query filter returns all documents in the `sample_mflix.movies` 
collection where `genres` equals `Action` and `rated` equals either 
`PG` or `PG-13`.

**Step 4: Delete a document.**

a. For the document that you want to delete, hover over
   the document and click the trash icon that 
   appears on the right-hand side.

   After clicking the delete button, MongoDB Atlas flags
   the document for deletion and asks for your confirmation.

#. Click Delete to confirm your selection.

To learn more, see Create, View, Update, and Delete Documents.

## Delete Behavior

### Indexes

Delete operations do not drop indexes, even if deleting all documents
from a collection.

### Atomicity

All write operations in MongoDB are atomic on the level of a single
document. For more information on MongoDB and atomicity, see
/core/write-operations-atomicity.

### Write Acknowledgement

With write concerns, you can specify the level of acknowledgment
requested from MongoDB for write operations. For details, see
/reference/write-concern.

tabs:
  - id: shell
    content: |

      **See also:**

      - `db.collection.deleteMany()`

      - `db.collection.deleteOne()`

      - additional-deletes

  - id: compass
    content: |

      **See also:**

      - `Compass Documents`

      - Compass Query Bar

  - id: python
    content: |

      **See also:**

      - `pymongo.collection.Collection.delete_many`

      - `pymongo.collection.Collection.delete_one`

      - additional-deletes

  - id: motor
    content: |

      **See also:**

      - `motor.motor_asyncio.AsyncIOMotorCollection.delete_many`

      - `motor.motor_asyncio.AsyncIOMotorCollection.delete_one`

      - additional-deletes

  - id: java-sync
    content: |

       **See also:**

       - com.mongodb.client.MongoCollection.deleteMany_

       - com.mongodb.client.MongoCollection.deleteOne_

       - Additional Java Synchronous Driver Write Examples

  - id: java-async
    content: |

       **See also:**

       - [com.mongodb.reactivestreams.client.MongoCollection.deleteMany](http://mongodb.github.io/mongo-java-driver-reactivestreams/1.6/javadoc/com/mongodb/reactivestreams/client/MongoCollection.html#deleteMany(org.bson.conversions.Bson))

       - [com.mongodb.reactivestreams.client.MongoCollection.deleteOne](http://mongodb.github.io/mongo-java-driver-reactivestreams/1.6/javadoc/com/mongodb/reactivestreams/client/MongoCollection.html#deleteOne(org.bson.conversions.Bson))

       - [Java Reactive Streams Driver Quick Tour](http://mongodb.github.io/mongo-java-driver-reactivestreams/1.6/getting-started/quick-tour/)

  - id: nodejs
    content: |

      **See also:**

      - `Collection.deleteMany()`

      - `Collection.deleteOne()`

      - additional-deletes

  - id: php
    content: |

      **See also:**

      - `MongoDBCollection::deleteMany()`

      - `MongoDBCollection::deleteOne()`

      - additional-deletes

  - id: ruby
    content: |

      **See also:**

      - `Mongo::Collection#delete_many()`

      - `Mongo::Collection#delete_one()`

  - id: scala
    content: |

      **See also:**

      - `collection.deleteMany()`

      - `collection.deleteOne()`

      - additional-deletes

  - id: csharp
    content: |

      **See also:**

      - `IMongoCollection.DeleteMany()`

      - `IMongoCollection.DeleteOne()`

      - additional-deletes

  - id: go
    content: |

      **See also:**

      - `Collection.DeleteMany`

      - `Collection.DeleteOne`

      - additional-deletes
