<!-- Converted from tutorial/query-for-null-fields.txt (reStructuredText). Includes are inlined. -->

# Query for Null or Missing Fields

  

You can query for `null` or missing fields in MongoDB 
using the following methods:

- Your programming language's driver.
- The MongoDB Atlas UI. To learn more, see 
  query-null-documents-atlas-ui.
- `MongoDB Compass`.

----------

→ Use the **Select your language** drop-down menu in the
upper-right to set the language of the following examples or select
MongoDB Compass.

----------

Different query operators in MongoDB treat `null` values differently.

tabs:
  - id: shell
    content: |

      This page provides examples of operations that query for `null` values using the
      `db.collection.find()` method in `mongosh`.

      The examples on this page use the `inventory` collection. Connect to a
      test database in your MongoDB instance then create the `inventory`
      collection:

  - id: compass
    content: |

      This page provides examples of operations that query for `null` values using
      MongoDB Compass. 

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
      [MongoDB C# Driver](https://mongodb.github.io/mongo-csharp-driver/).

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

  - id: ruby
    content: |

      **Important:**

      Use `nil` with the MongoDB Ruby driver to
      query for `null` or missing fields in MongoDB.

  - id: scala
    content: |

      **Important:**

      Use `BsonNull()` with the MongoDB Scala driver to query
      for `null` or missing fields in MongoDB.

  - id: csharp
    content: |

      **Important:**

      Use `BsonNull.Value` with the MongoDB C# driver to
      query for `null` or missing fields in MongoDB.

  - id: go
    content: |

      **Important:**

      Use `nil` with the MongoDB Go driver to
      query for `null` or missing fields in MongoDB.

tabs:
  - id: shell
    content: |

      ```javascript
      db.inventory.insertMany([
         { _id: 1, item: null },
         { _id: 2 }
      ])
      ```

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

      (Code example not available offline: /driver-examples/DocumentationExamples.cs)

  - id: go
    content: |
      (Code example not available offline: /driver-examples/go_examples.go)

## Equality Filter

tabs:
  - id: shell
    content: |
      The `{ item : null }` query matches documents that either
      contain the `item` field whose value is `null` **or** that
      do not contain the `item` field.

  - id: compass
    content: |
      The `{ item : null }` query matches documents that either
      contain the `item` field whose value is `null` **or** that
      do not contain the `item` field.

  - id: python
    content: |
      The `{ item : None }` query matches documents that either
      contain the `item` field whose value is `null` **or** that
      do not contain the `item` field.

  - id: motor
    content: |
      The `{ item : None }` query matches documents that either
      contain the `item` field whose value is `null` **or** that
      do not contain the `item` field.

  - id: java-sync
    content: |
      The `eq("item", null)` query matches documents that either
      contain the `item` field whose value is `null` **or** that
      do not contain the `item` field.

  - id: java-async
    content: |
      The `eq("item", null)` query matches documents that either
      contain the `item` field whose value is `null` **or** that
      do not contain the `item` field.

  - id: nodejs
    content: |
      The `{ item : null }` query matches documents that either
      contain the `item` field whose value is `null` **or** that
      do not contain the `item` field.

  - id: php
    content: |
      The `[ item => undef ]` query matches documents that either
      contain the `item` field whose value is `null` **or** that
      do not contain the `item` field.

  - id: ruby
    content: |
      The `{ item => nil }` query matches documents that either
      contain the `item` field whose value is `nil` **or** that
      do not contain the `item` field.

  - id: scala
    content: |
      The `equal("item", BsonNull)` query matches documents that
      either contain the `item` field whose value is `null` **or**
      that do not contain the `item` field.

  - id: csharp
    content: |
      The `Eq("item", BsonNull.Value)` query using the `FilterDefinitionBuilder.Eq()` method
      matches documents that either contain the `item` field whose
      value is `null` **or** that do not contain the `item` field.

  - id: go
    content: |
      The `item => nil` query matches documents that either
      contain the `item` field whose value is `nil` **or** that
      do not contain the `item` field.

tabs:
  - id: shell
    content: |

      ```javascript
      db.inventory.find( { item: null } )
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

      (Code example not available offline: /driver-examples/DocumentationExamples.cs)

  - id: go
    content: |
      (Code example not available offline: /driver-examples/go_examples.go)

The query returns both documents in the collection.

## Non-Equality Filter

To query for fields that **exist** and are **not null**, use the ``{ $ne
: null }` filter. The `{ item : { $ne : null } }`` query matches
documents where the `item` field exists **and** has a non-null value.

tabs:
  - id: shell
    content: |

      ```sh
      db.inventory.find( { item: { $ne : null } } )
      ```

  - id: compass
    content: |

      ```javascript
      { item: { $ne : null } }
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
      The `{ item : { $type: 10 } }` query matches *only*
      documents that contain the `item` field whose value is
      `null`; i.e. the value of the `item` field is of
      BSON Type `Null`
      (type number `10`) :

  - id: compass
    content: |
      The `{ item : { $type: 10 } }` query matches *only*
      documents that contain the `item` field whose value is
      `null`; i.e. the value of the `item` field is of
      BSON Type `Null`
      (type number `10`) :

  - id: python
    content: |
      The `{ item : { $type: 10 } }` query matches *only*
      documents that contain the `item` field whose value is
      `null`; i.e. the value of the `item` field is of
      BSON Type `Null`
      (type number `10`) :

  - id: motor
    content: |
      The `{ item : { $type: 10 } }` query matches *only*
      documents that contain the `item` field whose value is
      `null`; i.e. the value of the `item` field is of
      BSON Type `Null`
      (type number `10`) :

  - id: java-sync
    content: |
      The `type("item", BsonType.NULL)` query matches *only*
      documents that contain the `item` field whose value is
      `null`; i.e. the value of the `item` field is of
      BSON Type `Null`
      (type number `10`) :

  - id: java-async
    content: |
      The `type("item", BsonType.NULL)` query matches *only*
      documents that contain the `item` field whose value is
      `null`; i.e. the value of the `item` field is of
      BSON Type `Null`
      (type number `10`) :

  - id: nodejs
    content: |
      The `{ item : { $type: 10 } }` query matches *only*
      documents that contain the `item` field whose value is
      `null`; i.e. the value of the `item` field is of
      BSON Type `Null`
      (type number `10`) :

  - id: php
    content: |
      The `[ item => [ $type => 10 ] ]` query matches *only*
      documents that contain the `item` field whose value is
      `null`; i.e. the value of the `item` field is of
      BSON Type `Null`
      (type number `10`) :

  - id: ruby
    content: |
      The `{ item => { $type => 10 } }` query matches *only*
      documents that contain the `item` field whose value is
      `null`; i.e. the value of the `item` field is of
      BSON Type `Null`
      (type number `10`) :

  - id: java-sync
    content: |
      The `type("item", BsonType.NULL)` query matches *only*
      documents that contain the `item` field whose value is
      `null`; i.e. the value of the `item` field is of
      BSON Type `Null`
      (type number `10`) :

  - id: csharp
    content: |
      The `Type("item", BsonType.Null)` query using the
      `FilterDefinitionBuilder.Type()`
      method matches *only* documents that contain the `item`
      field whose value is `null`; i.e. the value of the `item`
      field is of BSON Type `Null`
      (type number `10`) :

  - id: go
    content: |
      The following query matches *only*
      documents that contain the `item` field whose value is of
      BSON Type `Null`
      (type number `10`) :

tabs:
  - id: shell
    content: |

      ```javascript
      db.inventory.find( { item : { $type: 10 } } )
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

      (Code example not available offline: /driver-examples/DocumentationExamples.cs)

  - id: go
    content: |
      (Code example not available offline: /driver-examples/go_examples.go)

The query returns only the document where the `item` field has a
value of `null`.

## Existence Check

The following example queries for documents that do not contain a
field. [#type0]_

tabs:
  - id: shell
    content: |
      The `{ item : { $exists: false } }` query matches documents
      that do not contain the `item` field:

  - id: compass
    content: |
      The `{ item : { $exists: false } }` query matches documents
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

tabs:
  - id: shell
    content: |

      ```javascript
      db.inventory.find( { item : { $exists: false } } )
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

      (Code example not available offline: /driver-examples/DocumentationExamples.cs)

  - id: go
    content: |
      (Code example not available offline: /driver-examples/go_examples.go)

The query only returns the document that does *not* contain the
`item` field.

**See also:**

Reference documentation for the `$type` and
`$exists` operators.

## Query for Null or Missing Fields with MongoDB Atlas

The example in this section uses the sample training dataset. To learn how to load the sample dataset 
into your MongoDB Atlas deployment, see Load Sample Data.

To query for a `null` or missing field in MongoDB Atlas, follow these steps:

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

Different query operators in MongoDB treat `null` values differently.
To apply a query filter, copying each of the following documents into the 
Filter search bar and click Apply.

Use the following query filter to match documents that either contain a
`description` field with a `null` value or do not contain the 
`description` field:

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
