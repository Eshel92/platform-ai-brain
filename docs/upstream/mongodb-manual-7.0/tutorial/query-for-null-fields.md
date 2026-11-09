<!-- Converted from tutorial/query-for-null-fields.txt (reStructuredText). Includes are inlined. -->

# Query for Null or Missing Fields

Query for `null` or missing fields in MongoDB using the
following methods:

- Your programming language's driver.
- The MongoDB Atlas UI. To learn more, see 
  query-null-documents-atlas-ui.
- `MongoDB Compass`.

----------

→ Use the **Select your language** drop-down menu in the
upper-right to set the language of the following examples or select
MongoDB Compass.

----------

Query operators in MongoDB treat `null` values differently.

tabs:
  - id: shell
    content: |

      This page provides examples of operations that query for `null` values using the
      `db.collection.find()` method in `mongosh`.

  - id: compass
    content: |

      This page provides examples of operations that query for `null` values using
      MongoDB Compass. 

      The examples on this page use the `inventory` collection. Connect to a
      test database in your MongoDB instance then create the `inventory`
      collection:

  - id: c
    content: |

      This page provides examples of operations that query for `null` values using
      [mongoc_collection_find_with_opts](https://mongoc.org/libmongoc/current/mongoc_collection_find_with_opts.html).

      The examples on this page use the `inventory` collection. Connect to a
      test database in your MongoDB instance then create the `inventory`
      collection:

  - id: python
    content: |

      This page provides examples of operations that query for `null` values using the
      `pymongo.collection.Collection.find` method in the
      [PyMongo](https://pymongo.readthedocs.io/en/stable/api)
      Python driver.

      The examples on this page use the `inventory` collection. Connect to a
      test database in your MongoDB instance then create the `inventory`
      collection:

  - id: motor
    content: |

      This page provides examples of operations that query for `null` values using the
      `motor.motor_asyncio.AsyncIOMotorCollection.find`
      method in the [Motor](https://motor.readthedocs.io/en/stable/)
      driver.

      The examples on this page use the `inventory` collection. Connect to a
      test database in your MongoDB instance then create the `inventory`
      collection:

  - id: java-sync
    content: |

      This page provides examples of operations that query for `null` values using the
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

      This page provides examples of operations that query for `null` values using the
      [com.mongodb.reactivestreams.client.MongoCollection.find](http://mongodb.github.io/mongo-java-driver-reactivestreams/1.6/javadoc/com/mongodb/reactivestreams/client/MongoCollection.html#find())
      method in the MongoDB [Java Reactive Streams Driver](http://mongodb.github.io/mongo-java-driver-reactivestreams/1.6/).

      The examples on this page use the `inventory` collection. Connect to a
      test database in your MongoDB instance then create the `inventory`
      collection:

  - id: kotlin-coroutine
    content: |
      This page provides examples of operations that query for `null` values by using the
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

      This page provides examples of operations that query for `null` values using the
      `Collection.find()` method in
      the `MongoDB Node.js Driver`.

      The examples on this page use the `inventory` collection. Connect to a
      test database in your MongoDB instance then create the `inventory`
      collection:

  - id: php
    content: |

      This page provides examples of operations that query for `null` values using the
      `MongoDBCollection::find()`
      method in the
      [MongoDB PHP Library](https://www.mongodb.com/docs/drivers/php-libraries/).

      The examples on this page use the `inventory` collection. Connect to a
      test database in your MongoDB instance then create the `inventory`
      collection:

  - id: ruby
    content: |

      This page provides examples of operations that query for `null` values using the
      `Mongo::Collection#find()`
      method in the
      `MongoDB Ruby Driver`.

      The examples on this page use the `inventory` collection. Connect to a
      test database in your MongoDB instance then create the `inventory`
      collection:

  - id: scala
    content: |

      This page provides examples of operations that query for `null` values using the
      `collection.find()` method
      in the
      [MongoDB Scala Driver](http://mongodb.github.io/mongo-scala-driver/).

      The examples on this page use the `inventory` collection. Connect to a
      test database in your MongoDB instance then create the `inventory`
      collection:

  - id: csharp
    content: |

      This page provides examples of operations that query for `null` values using the
      `MongoCollection.Find()`
      method in the
      [MongoDB .NET/C# Driver](https://mongodb.github.io/mongo-csharp-driver/).

      The examples on this page use the `inventory` collection. Connect to a
      test database in your MongoDB instance then create the `inventory`
      collection:

  - id: go
    content: |

      This page provides examples of operations that query for `null` values using the
      `Collection.Find`
      function in the
      [MongoDB Go Driver](https://github.com/mongodb/mongo-go-driver/).

      The examples on this page use the `inventory` collection. Connect to a
      test database in your MongoDB instance then create the `inventory`
      collection:

tabs:
  - id: c
    content: |

      **Important:**

      Use `BCON_NULL` with the MongoDB C driver to
      query for `null` or missing fields in MongoDB.

  - id: shell
    content: |

      **Important:**

      Use `null` with the MongoDB Shell to
      query for `null` or missing fields in MongoDB.

  - id: compass
    content: |

      **Important:**

      Use `null` with MongoDB Compass to
      query for `null` or missing fields in MongoDB.

  - id: python
    content: |

      **Important:**

      Use `None` with the PyMongo Python driver to
      query for `null` or missing fields in MongoDB.

  - id: motor
    content: |

      **Important:**

      Use `None` with the Motor driver to
      query for `null` or missing fields in MongoDB.

  - id: java-sync
    content: |

      **Important:**

      Use `null` with the Java driver to
      query for `null` or missing fields in MongoDB.

  - id: java-async
    content: |

      **Important:**

      Use `null` with the Java Reactive Streams driver to
      query for `null` or missing fields in MongoDB.

  - id: kotlin-coroutine
    content: |

      **Important:**

      Use `null` with the Kotlin Coroutine driver to
      query for `null` or missing fields in MongoDB.

  - id: nodejs
    content: |

      **Important:**

      Use `null` with the Node.js driver to
      query for `null` or missing fields in MongoDB.

  - id: ruby
    content: |

      **Important:**

      Use `nil` with the MongoDB Ruby driver to
      query for `null` or missing fields in MongoDB.

  - id: php
    content: |

      **Important:**

      Use `null` with the MongoDB PHP driver to
      query for `null` or missing fields in MongoDB.

  - id: scala
    content: |

      **Important:**

      Use `BsonNull()` with the MongoDB Scala driver to query
      for `null` or missing fields in MongoDB.

  - id: csharp
    content: |

      **Important:**

      Use `BsonNull.Value` with the MongoDB .NET/C# Driver to
      query for `null` or missing fields in MongoDB.

  - id: go
    content: |

      **Important:**

      Use `nil` with the MongoDB Go driver to
      query for `null` or missing fields in MongoDB.

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
         { "_id": 1, "item": null },
         { "_id": 2 }
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
      (Code example not available offline: /driver-examples/node_query_for_null_fields.js)

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
          new BsonDocument { { "_id", 1 }, { "item", BsonNull.Value } },
          new BsonDocument { { "_id", 2 } }
      };
      collection.InsertMany(documents);
      ```

  - id: go
    content: |
      (Code example not available offline: /driver-examples/go_examples.go)

## Equality Filter

tabs:
  - id: shell
    content: |
      The `{ metacritic : null }` query matches documents that
      contain the `metacritic` field with a `null` value **or**
      do not contain the `metacritic` field.

  - id: compass
    content: |
      The `{ item : null }` query matches documents that contain
      the `item` field with a `null` value **or** do not contain
      the `item` field.

  - id: c
    content: |
      The `{ item, BCON_NULL }` query matches documents that
      contain the `item` field with a `null` value **or** do not
      contain the `item` field.

  - id: python
    content: |
      The `{ item : None }` query matches documents that contain
      the `item` field with a `null` value **or** do not contain
      the `item` field.

  - id: motor
    content: |
      The `{ item : None }` query matches documents that contain
      the `item` field with a `null` value **or** do not contain
      the `item` field.

  - id: java-sync
    content: |
      The `eq("item", null)` query matches documents that contain
      the `item` field with a `null` value **or** do not contain
      the `item` field.

  - id: java-async
    content: |
      The `eq("item", null)` query matches documents that contain
      the `item` field with a `null` value **or** do not contain
      the `item` field.

  - id: kotlin-coroutine
    content: |
      The `eq("item", null)` query matches documents that contain
      the `item` field with a `null` value **or** do not contain
      the `item` field.

  - id: nodejs
    content: |
      The `{ item : null }` query matches documents that contain
      the `item` field with a `null` value **or** do not contain
      the `item` field.

  - id: php
    content: |
      The `[ item => undef ]` query matches documents that contain
      the `item` field with a `null` value **or** do not contain
      the `item` field.

  - id: ruby
    content: |
      The `{ item => nil }` query matches documents that contain
      the `item` field with a `nil` value **or** do not contain
      the `item` field.

  - id: scala
    content: |
      The `equal("item", BsonNull)` query matches documents that
      contain the `item` field with a `null` value **or** do not
      contain the `item` field.

  - id: csharp
    content: |
      The `Eq("item", BsonNull.Value)` query using the
      `FilterDefinitionBuilder.Eq()` method
      matches documents that contain the `item` field with a
      `null` value **or** do not contain the `item` field.

  - id: go
    content: |
      The `item => nil` query matches documents that contain
      the `item` field with a `nil` value **or** do not contain
      the `item` field.

tabs:
  - id: shell
    content: |

      ```javascript
      db.movies.find( { metacritic: null } )
      ```

  - id: compass
    content: |
      Copy the following query filter document into the
      query bar and click
      Find:

      ```javascript
      { item: null }
      ```

      (Figure: /images/compass-find-null-field.png)

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
      (Code example not available offline: /driver-examples/node_query_for_null_fields.js)

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
      var filter = Builders<BsonDocument>.Filter.Eq("item", BsonNull.Value);
      var result = collection.Find(filter).ToList();
      ```

  - id: go
    content: |
      (Code example not available offline: /driver-examples/go_examples.go)

tabs:
  - id: shell
    content: |
      The query returns all documents in the `movies`
      collection where the `metacritic` field contains a
      `null` value or does not exist.

  - id: compass
    content: |
      The query returns both documents in the collection.

  - id: c
    content: |
      The query returns both documents in the collection.

  - id: python
    content: |
      The query returns both documents in the collection.

  - id: motor
    content: |
      The query returns both documents in the collection.

  - id: java-sync
    content: |
      The query returns both documents in the collection.

  - id: java-async
    content: |
      The query returns both documents in the collection.

  - id: kotlin-coroutine
    content: |
      The query returns both documents in the collection.

  - id: nodejs
    content: |
      The query returns both documents in the collection.

  - id: php
    content: |
      The query returns both documents in the collection.

  - id: ruby
    content: |
      The query returns both documents in the collection.

  - id: scala
    content: |
      The query returns both documents in the collection.

  - id: csharp
    content: |
      The query returns both documents in the collection.

  - id: go
    content: |
      The query returns both documents in the collection.

## Non-Equality Filter

To query for fields that **exist** and are **not null**, use the
`{ $ne : null }` filter.

tabs:
  - id: shell
    content: |
      The `{ metacritic : { $ne : null } }` query matches
      documents where the `metacritic` field exists **and**
      has a non-null value.

  - id: compass
    content: |
      The `{ item : { $ne : null } }` query matches
      documents where the `item` field exists **and** has a
      non-null value.

  - id: c
    content: |
      The `{ item : { $ne : null } }` query matches
      documents where the `item` field exists **and** has a
      non-null value.

  - id: python
    content: |
      The `{ item : { $ne : null } }` query matches
      documents where the `item` field exists **and** has a
      non-null value.

  - id: motor
    content: |
      The `{ item : { $ne : null } }` query matches
      documents where the `item` field exists **and** has a
      non-null value.

  - id: java-sync
    content: |
      The `{ item : { $ne : null } }` query matches
      documents where the `item` field exists **and** has a
      non-null value.

  - id: java-async
    content: |
      The `{ item : { $ne : null } }` query matches
      documents where the `item` field exists **and** has a
      non-null value.

  - id: kotlin-coroutine
    content: |
      The `{ item : { $ne : null } }` query matches
      documents where the `item` field exists **and** has a
      non-null value.

  - id: nodejs
    content: |
      The `{ item : { $ne : null } }` query matches
      documents where the `item` field exists **and** has a
      non-null value.

  - id: php
    content: |
      The `{ item : { $ne : null } }` query matches
      documents where the `item` field exists **and** has a
      non-null value.

  - id: ruby
    content: |
      The `{ item : { $ne : null } }` query matches
      documents where the `item` field exists **and** has a
      non-null value.

  - id: scala
    content: |
      The `{ item : { $ne : null } }` query matches
      documents where the `item` field exists **and** has a
      non-null value.

  - id: csharp
    content: |
      The `{ item : { $ne : null } }` query matches
      documents where the `item` field exists **and** has a
      non-null value.

  - id: go
    content: |
      The `{ item : { $ne : null } }` query matches
      documents where the `item` field exists **and** has a
      non-null value.

tabs:
  - id: shell
    content: |

      ```javascript
      db.movies.find( { metacritic: { $ne: null } } )
      ```

  - id: compass
    content: |

      ```javascript
      { item: { $ne : null } }
      ```

  - id: c
    content: |

      ```c
      filter = BCON_NEW ("item", BCON_NULL);
      cursor = mongoc_collection_find_with_opts (collection, filter, NULL, NULL);
      ```

  - id: python
    content: |

      ```python
      cursor = db.inventory.find( { "item": { "$ne": None } } )
      ```

  - id: motor
    content: |

      ```python
      cursor = db.inventory.find( { "item": { "$ne": None } } )
      ```

  - id: java-sync
    content: |

      ```java
      collection.find($ne("item", null));
      ```

  - id: java-async
    content: |

      ```java
      db.inventory.find( { item: { $ne : nul l} } )
      ```

  - id: kotlin-coroutine
    content: |

      ```kotlin
      collection.find(ne("item", null))
      ```

  - id: nodejs
    content: |

      ```javascript
      const cursor = db.collection('inventory')
        .find({ item: { $ne : null }
      });
      ```

  - id: php
    content: |

      ```php
      $cursor = $db->inventory->find(['item' => ['$ne' => null ]]);
      ```

  - id: ruby
    content: |

      ```ruby
      client[:inventory].find(item: { '$ne' => nil })
      ```

  - id: scala
    content: |

      ```scala
      collection.find($ne("item", null));
      ```

  - id: csharp
    content: |

      ```csharp
      var filter = Builders<BsonDocument>.Filter.Ne("item", BsonNull.Value);
      var result = collection.Find(filter).ToList();
      ```

  - id: go
    content: |

      ```go
      cursor, err := coll.Find(
        context.TODO(),
        bson.D{
          {"item", bson.D{"$ne": nil}},
        })
      ```

## Type Check

tabs:
  - id: shell
    content: |
      The `{ metacritic : { $type: 10 } }` query matches
      *only* documents that contain the `metacritic` field
      with a `null` value. The value of the `metacritic`
      field is of BSON Type `Null`
      (BSON Type 10):

  - id: compass
    content: |
      The `{ item : { $type: 10 } }` query matches *only*
      documents that contain the `item` field with a `null`
      value. The value of the `item` field is of
      BSON Type `Null` (BSON Type 10):

  - id: c
    content: |
      The `{ item, { $type, BCON_NULL } }` query matches *only*
      documents that contain the `item` field with a `null`
      value. The value of the `item` field is of
      BSON Type `Null` (BSON Type 10):

  - id: python
    content: |
      The `{ item : { $type: 10 } }` query matches *only*
      documents that contain the `item` field with a `null`
      value. The value of the `item` field is of
      BSON Type `Null` (BSON Type 10):

  - id: motor
    content: |
      The `{ item : { $type: 10 } }` query matches *only*
      documents that contain the `item` field with a `null`
      value. The value of the `item` field is of
      BSON Type `Null` (BSON Type 10):

  - id: java-sync
    content: |
      The `type("item", BsonType.NULL)` query matches *only*
      documents that contain the `item` field with a `null`
      value. The value of the `item` field is of
      BSON Type `Null` (BSON Type 10):

  - id: java-async
    content: |
      The `type("item", BsonType.NULL)` query matches *only*
      documents that contain the `item` field with a `null`
      value. The value of the `item` field is of
      BSON Type `Null` (BSON Type 10):

  - id: kotlin-coroutine
    content: |
      The `type("item", BsonType.NULL)` query matches *only*
      documents that contain the `item` field with a `null`
      value. The value of the `item` field is of
      BSON Type `Null` (BSON Type 10):

  - id: scala
    content: |
      The `type("item", BsonType.NULL)` query matches *only*
      documents that contain the `item` field with a `null`
      value. The value of the `item` field is of
      BSON Type `Null` (BSON Type 10):

  - id: nodejs
    content: |
      The `{ item : { $type: 10 } }` query matches *only*
      documents that contain the `item` field with a `null`
      value. The value of the `item` field is of
      BSON Type `Null` (BSON Type 10):

  - id: php
    content: |
      The `[ item => [ $type => 10 ] ]` query matches *only*
      documents that contain the `item` field with a `null`
      value. The value of the `item` field is of
      BSON Type `Null` (BSON Type 10):

  - id: ruby
    content: |
      The `{ item => { $type => 10 } }` query matches *only*
      documents that contain the `item` field with a `null`
      value. The value of the `item` field is of
      BSON Type `Null` (BSON Type 10):

  - id: csharp
    content: |
      The `Type("item", BsonType.Null)` query using the
      `FilterDefinitionBuilder.Type()`
      method matches *only* documents that contain the `item`
      field with a `null` value. The value of the `item` field
      is of BSON Type `Null` (BSON Type 10):

  - id: go
    content: |
      The following query matches *only* documents that contain the
      `item` field with a value of BSON Type
      `Null` (BSON Type 10):

tabs:
  - id: shell
    content: |

      ```javascript
      db.movies.find( { metacritic: { $type: 10 } } )
      ```

  - id: compass
    content: |
      Copy the following query filter document into the
      query bar and click
      Find:

      ```javascript
      { item : { $type: 10 } }
      ```

      (Figure: /images/compass-find-null-type-check.png)

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
      (Code example not available offline: /driver-examples/node_query_for_null_fields.js)

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
      var filter = Builders<BsonDocument>.Filter.Type("item", BsonType.Null);
      var result = collection.Find(filter).ToList();
      ```

  - id: go
    content: |
      (Code example not available offline: /driver-examples/go_examples.go)

tabs:
  - id: shell
    content: |
      The query returns only the documents from the `movies`
      collection where the `metacritic` field has a `null`
      value.

  - id: compass
    content: |
      The query returns only the document where the `item`
      field has a value of `null`.

  - id: c
    content: |
      The query returns only the document where the `item`
      field has a value of `null`.

  - id: python
    content: |
      The query returns only the document where the `item`
      field has a value of `null`.

  - id: motor
    content: |
      The query returns only the document where the `item`
      field has a value of `null`.

  - id: java-sync
    content: |
      The query returns only the document where the `item`
      field has a value of `null`.

  - id: java-async
    content: |
      The query returns only the document where the `item`
      field has a value of `null`.

  - id: kotlin-coroutine
    content: |
      The query returns only the document where the `item`
      field has a value of `null`.

  - id: nodejs
    content: |
      The query returns only the document where the `item`
      field has a value of `null`.

  - id: php
    content: |
      The query returns only the document where the `item`
      field has a value of `null`.

  - id: ruby
    content: |
      The query returns only the document where the `item`
      field has a value of `null`.

  - id: scala
    content: |
      The query returns only the document where the `item`
      field has a value of `null`.

  - id: csharp
    content: |
      The query returns only the document where the `item`
      field has a value of `null`.

  - id: go
    content: |
      The query returns only the document where the `item`
      field has a value of `null`.

## Existence Check

The following example queries for documents that do not contain a
field.

tabs:
  - id: shell
    content: |
      The `{ metacritic : { $exists: false } }` query matches
      documents that do not contain the `metacritic` field:

  - id: compass
    content: |
      The `{ item : { $exists: false } }` query matches documents
      that do not contain the `item` field:

  - id: c
    content: |
      The `{ item, { $exists, BCON_BOOL (false) } }` query matches documents
      that do not contain the `item` field:

  - id: python
    content: |
      The `{ item : { $exists: False } }` query matches documents
      that do not contain the `item` field:

  - id: motor
    content: |
      The `{ item : { $exists: False } }` query matches documents
      that do not contain the `item` field:

  - id: java-sync
    content: |
      The `exists("item", false)` query matches documents that
      do not contain the `item` field:

  - id: java-async
    content: |
      The   `exists("item", false)` query matches documents that do
      not contain the `item` field:

  - id: kotlin-coroutine
    content: |
      The `exists("item", false)` query matches documents that
      do not contain the `item` field:

  - id: nodejs
    content: |
      The `{ item : { $exists: false } }` query matches documents
      that do not contain the `item` field:

  - id: php
    content: |
      The `[ item => [ $exists => false ] ]` query matches documents
      that do not contain the `item` field:

  - id: ruby
    content: |
      The `{ item => { $exists => false } }` query matches documents
      that do not contain the `item` field:

  - id: scala
    content: |
      The `exists("item", exists = false)` query matches documents
      that do not contain the `item` field:

  - id: csharp
    content: |
      The `Exists("item", false)` query using the `FilterDefinitionBuilder.Exists()`
      method matches documents that do not contain the `item` field:

  - id: go
    content: |
      The `bson.D{{"item", bson.D{{"$exists", false}}}}` query matches documents
      that do not contain the `item` field:

tabs:
  - id: shell
    content: |

      ```javascript
      db.movies.find( { metacritic: { $exists: false } } )
      ```

  - id: compass
    content: |
      Copy the following query filter document into the
      query bar and click
      Find:

      ```javascript
      { item : { $exists: false } }
      ```

      (Figure: /images/compass-find-null-existence-check.png)

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
      (Code example not available offline: /driver-examples/node_query_for_null_fields.js)

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
      var filter = Builders<BsonDocument>.Filter.Exists("item", false);
      var result = collection.Find(filter).ToList();
      ```

  - id: go
    content: |
      (Code example not available offline: /driver-examples/go_examples.go)

tabs:
  - id: shell
    content: |
      The query returns only the documents from the `movies`
      collection that do not contain the `metacritic` field.

  - id: compass
    content: |
      The query only returns the document that does *not*
      contain the `item` field.

  - id: c
    content: |
      The query only returns the document that does *not*
      contain the `item` field.

  - id: python
    content: |
      The query only returns the document that does *not*
      contain the `item` field.

  - id: motor
    content: |
      The query only returns the document that does *not*
      contain the `item` field.

  - id: java-sync
    content: |
      The query only returns the document that does *not*
      contain the `item` field.

  - id: java-async
    content: |
      The query only returns the document that does *not*
      contain the `item` field.

  - id: kotlin-coroutine
    content: |
      The query only returns the document that does *not*
      contain the `item` field.

  - id: nodejs
    content: |
      The query only returns the document that does *not*
      contain the `item` field.

  - id: php
    content: |
      The query only returns the document that does *not*
      contain the `item` field.

  - id: ruby
    content: |
      The query only returns the document that does *not*
      contain the `item` field.

  - id: scala
    content: |
      The query only returns the document that does *not*
      contain the `item` field.

  - id: csharp
    content: |
      The query only returns the document that does *not*
      contain the `item` field.

  - id: go
    content: |
      The query only returns the document that does *not*
      contain the `item` field.

**Note:**

Expressions do not support 
the `$exists` operator. To check for the existence of a field in an 
expression, you can use the `$type` aggregation
operator to check if a field has a type of `missing`.

For more information, see $type Existence Check.

**See also:**

Reference documentation for the `$type` and
`$exists` operators.

## Query for Null or Missing Fields with MongoDB Atlas

The example in this section uses the sample training dataset. To learn how to load the sample dataset 
into your MongoDB Atlas deployment, see Load Sample Data.

To query for a `null` or missing field in MongoDB Atlas, follow these steps:

**Step 1: In the MongoDB Atlas UI, go to the Clusters page for your project.**

a. If it's not already displayed, select the organization that
   contains your desired project from the `office` Organizations menu in the
   navigation bar.

#. If it's not already displayed, select your project
   from the Projects menu in the navigation bar.

#. In the sidebar, click Clusters under 
   the Database heading.

   The [Clusters](https://cloud.mongodb.com/go?l=https%3A%2F%2Fcloud.mongodb.com%2Fv2%2F%3Cproject%3E%23%2Fclusters) page displays.

**Step 2: Navigate to the collection.**

a. For the cluster that contains the sample data, click Browse Collections.
#. In the left navigation pane, select the `sample_training` database.
#. Select the `companies` collection.

**Step 3: Insert a blank document.**

Click the Insert Document button to display the 
dialog box, and then click Insert
to insert a document with only the `_id` field.

**Step 4: Specify a query filter document.**

To find a document that contains a `null` or missing value,
specify a query filter document
in the Filter field. A query filter document uses
query operators
to specify search conditions.

Query operators in MongoDB treat `null` values differently. To apply a
query filter, copy each of the following documents into the
Filter search bar and click Apply.

Use the following query filter to match documents that contain a
`description` field with a `null` value or do not contain
the `description` field:

```javascript
{ description : null }
```

Use the following query filter to match only documents that contain 
a `description` field with a `null` value. This filter specifies
that the value of the field must be BSON Type `Null` 
(BSON Type 10):

```javascript
{ description : { $type: 10 } }
```

Use the following query filter to match only documents that
do not contain the `description` field. Only the document
that you inserted earlier should appear:

```javascript
{ description : { $exists: false } }
```
