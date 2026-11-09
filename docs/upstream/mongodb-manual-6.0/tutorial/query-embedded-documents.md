<!-- Converted from tutorial/query-embedded-documents.txt (reStructuredText). Includes are inlined. -->

# Query on Embedded/Nested Documents

You can query embedded documents in MongoDB by using the following
methods:

- Your programming language's driver.
- The MongoDB Atlas UI. To learn more, see 
  query-embedded-documents-atlas-ui.
- `MongoDB Compass`.

----------

→ Use the **Select your language** drop-down menu in the
upper-right to set the language of the following examples or select
MongoDB Compass.

----------

tabs:
  - id: shell
    content: |
      This page provides examples of query operations on embedded/nested documents using the
      `db.collection.find()` method in `mongosh`.

      The examples on this page use the `inventory` collection. Connect to a
      test database in your MongoDB instance then create the `inventory`
      collection:

  - id: compass
    content: |
      This page provides examples of query operations on embedded/nested documents using
      MongoDB Compass. 

      The examples on this page use the `inventory` collection. Connect to a
      test database in your MongoDB instance then create the `inventory`
      collection:

  - id: python
    content: |
      This page provides examples of query operations on embedded/nested documents using the
      `pymongo.collection.Collection.find` method in the
      [PyMongo](https://www.mongodb.com/docs/languages/python/pymongo-driver/current/)
      Python driver.

      The examples on this page use the `inventory` collection. Connect to a
      test database in your MongoDB instance then create the `inventory`
      collection:

  - id: motor
    content: |
      This page provides examples of query operations on embedded/nested documents using the
      `motor.motor_asyncio.AsyncIOMotorCollection.find`
      method in the [Motor](https://motor.readthedocs.io/en/stable/)
      driver.

      The examples on this page use the `inventory` collection. Connect to a
      test database in your MongoDB instance then create the `inventory`
      collection:

  - id: java-sync
    content: |
      This page provides examples of query operations on embedded/nested documents using the
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
      This page provides examples of query operations on embedded/nested documents using the
      [com.mongodb.reactivestreams.client.MongoCollection.find](http://mongodb.github.io/mongo-java-driver-reactivestreams/1.6/javadoc/com/mongodb/reactivestreams/client/MongoCollection.html#find())
      method in the MongoDB [Java Reactive Streams Driver](http://mongodb.github.io/mongo-java-driver-reactivestreams/1.6/).

      The examples on this page use the `inventory` collection. Connect to a
      test database in your MongoDB instance then create the `inventory`
      collection:

  - id: nodejs
    content: |
      This page provides examples of query operations on embedded/nested documents using the
      `Collection.find()` method in
      the `MongoDB Node.js Driver`.

      The examples on this page use the `inventory` collection. Connect to a
      test database in your MongoDB instance then create the `inventory`
      collection:

  - id: php
    content: |
      This page provides examples of query operations on embedded/nested documents using the
      `MongoDBCollection::find()`
      method in the
      [MongoDB PHP Library](https://www.mongodb.com/docs/drivers/php-libraries/).

      The examples on this page use the `inventory` collection. Connect to a
      test database in your MongoDB instance then create the `inventory`
      collection:

  - id: ruby
    content: |
      This page provides examples of query operations on embedded/nested documents using the
      `Mongo::Collection#find()`
      method in the
      `MongoDB Ruby Driver`.

      The examples on this page use the `inventory` collection. Connect to a
      test database in your MongoDB instance then create the `inventory`
      collection:

  - id: scala
    content: |
      This page provides examples of query operations on embedded/nested documents using the
      `collection.find()` method
      in the
      [MongoDB Scala Driver](http://mongodb.github.io/mongo-scala-driver/).

      The examples on this page use the `inventory` collection. Connect to a
      test database in your MongoDB instance then create the `inventory`
      collection:

  - id: csharp
    content: |
      This page provides examples of query operations on embedded/nested documents using the
      `MongoCollection.Find()`
      method in the
      [MongoDB C# Driver](https://mongodb.github.io/mongo-csharp-driver/).

      The examples on this page use the `inventory` collection. Connect to a
      test database in your MongoDB instance then create the `inventory`
      collection:

  - id: go
    content: |
      This page provides examples of query operations on embedded/nested documents using the
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
         { item: "journal", qty: 25, size: { h: 14, w: 21, uom: "cm" }, status: "A" },
         { item: "notebook", qty: 50, size: { h: 8.5, w: 11, uom: "in" }, status: "A" },
         { item: "paper", qty: 100, size: { h: 8.5, w: 11, uom: "in" }, status: "D" },
         { item: "planner", qty: 75, size: { h: 22.85, w: 30, uom: "cm" }, status: "D" },
         { item: "postcard", qty: 45, size: { h: 10, w: 15.25, uom: "cm" }, status: "A" }
      ]);
      ```

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
      (Code example not available offline: /driver-examples/node_query_embedded_documents.js)

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

## Query on Nested Field with Dot Notation

To specify a query condition on fields in an embedded/nested document,
use dot notation (`"field.nestedField"`). 

**Note:**

When querying using dot notation, the field and nested field must be
inside quotation marks.

### Specify Equality Match on a Nested Field

The following example selects all documents where the field `uom`
nested in the `size` field equals `"in"`:

tabs:
  - id: shell
    content: |

      ```javascript
      db.inventory.find( { "size.uom": "in" } )
      ```

  - id: compass
    content: |
      Copy the following filter into the Compass query bar and click
      Find:

      ```javascript
      { "size.uom": "in" }
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
      (Code example not available offline: /driver-examples/node_query_embedded_documents.js)

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

### Specify Match using Query Operator

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

The following query uses the less than operator (`$lt`) on
the field `h` embedded in the `size` field:

tabs:
  - id: shell
    content: |

      ```javascript
      db.inventory.find( { "size.h": { $lt: 15 } } )
      ```

  - id: compass
    content: |
      Copy the following filter into the Compass query bar and click
      Find:

      ```javascript
      { "size.h": { $lt: 15 } }
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
      (Code example not available offline: /driver-examples/node_query_embedded_documents.js)

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

### Specify `AND` Condition

The following query selects all documents where the nested field `h`
is less than `15`, the nested field `uom` equals `"in"`, and the
`status` field equals `"D"`:

tabs:
  - id: shell
    content: |

      ```javascript
      db.inventory.find( { "size.h": { $lt: 15 }, "size.uom": "in", status: "D" } )
      ```

  - id: compass
    content: |
      Copy the following filter into the Compass query bar and click
      Find:

      ```javascript
      { "size.h": { $lt: 15 }, "size.uom": "in", status: "D" }
      ```

      (Figure: /images/compass-find-embedded-and.png)

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
      (Code example not available offline: /driver-examples/node_query_embedded_documents.js)

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

## Match an Embedded/Nested Document

tabs:
  - id: shell
    content: |
      To specify an equality condition on a field that is an
      embedded/nested document, use the
      query filter document
      `{ <field>: <value> }` where `<value>` is the document
      to match.

  - id: compass
    content: |
      To specify an equality condition on a field that is an
      embedded/nested document, use the
      query filter document
      `{ <field>: <value> }` where `<value>` is the document
      to match.

  - id: python
    content: |
      To specify an equality condition on a field that is an
      embedded/nested document, use the
      query filter document
      `{ <field>: <value> }` where `<value>` is the document
      to match.

  - id: motor
    content: |
      To specify an equality condition on a field that is an
      embedded/nested document, use the
      query filter document
      `{ <field>: <value> }` where `<value>` is the document
      to match.

  - id: java-sync
    content: |
      To specify an equality condition on a field that is an
      embedded/nested document, use the filter document
      `eq( <field1>, <value>)` where `<value>` is the document
      to match.

  - id: java-async
    content: |
      To specify an equality condition on a field that is an
      embedded/nested document, use the filter document
      `eq( <field1>, <value>)` where `<value>` is the document
      to match.

  - id: nodejs
    content: |
      To specify an equality condition on a field that is an
      embedded/nested document, use the
      query filter document
      `{ <field>: <value> }` where `<value>` is the document
      to match.

  - id: php
    content: |
      To specify an equality condition on a field that is an
      embedded/nested document, use the
      query filter document
      `[ <field> => <value> ]` where `<value>` is the document
      to match.

  - id: ruby
    content: |
      To specify an equality condition on a field that is an
      embedded/nested document, use the
      query filter document
      `{ <field> => <value> }` where `<value>` is the document
      to match.

  - id: scala
    content: |
      To specify an equality condition on a field that is an
      embedded/nested document, use the filter document
      `equal( <field1>, <value> )` where `<value>` is the document
      to match.

  - id: csharp
    content: |
      To specify an equality condition on a field that is an
      embedded/nested document, construct a filter using the
      `Eq`
      method:

      ```csharp
      Builders<BsonDocument>.Filter.Eq(<field>, <value>)
      ```

      `<value>` is the document to match.

For example, the following query selects all documents where the field
`size` equals the document `{ h: 14, w: 21, uom: "cm" }`:

tabs:
  - id: shell
    content: |

      ```javascript
      db.inventory.find( { size: { h: 14, w: 21, uom: "cm" } } )
      ```

  - id: compass
    content: |
      Copy the following filter into the Compass query bar and click
      Find:

      ```javascript
      { size: { h: 14, w: 21, uom: "cm" } }
      ```

      (Figure: /images/compass-match-embedded.png)

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
      (Code example not available offline: /driver-examples/node_query_embedded_documents.js)

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

**Warning:**

MongoDB does not recommend comparisons on embedded 
documents because the operations require an *exact* match of the specified 
`<value>` document, including the field order.

For example, the following query does not match any documents in the
`inventory` collection:

tabs:
  - id: shell
    content: |

      ```javascript
      db.inventory.find(  { size: { w: 21, h: 14, uom: "cm" } }  )
      ```

  - id: compass
    content: |
      (Figure: /images/compass-find-embedded-no-match.png)

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
      (Code example not available offline: /driver-examples/node_query_embedded_documents.js)

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

Queries that use comparisons on embedded documents can result in 
unpredictable behavior when used with a driver that does not use ordered data 
structures for expressing queries. 

## Query Embedded Documents with MongoDB Atlas

The example in this section uses the sample movies dataset. To learn how to load the sample dataset 
into your MongoDB Atlas deployment, see Load Sample Data.

To query an embedded document in MongoDB Atlas, follow these steps:

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

a. For the cluster that contains the sample data,
   click Browse Collections.
#. In the left navigation pane, select the
   `sample_mflix` database.
#. Select the `movies` collection.

**Step 3: Specify the query filter document**

Specify the query filter document
in the Filter field. A query filter document uses 
query operators to specify
search conditions.

Copy the following query filter document into the 
Filter search bar:

```javascript
{ "awards.wins": 1 }
```

**Step 4: Click Apply**

This query filter returns all documents in the 
`sample_mflix.movies` collection where the embedded  document
for the `awards` field contains `{ wins: 1 }`.

## Additional Query Tutorials

For additional query examples, see:

- /tutorial/query-documents

- /tutorial/query-arrays

- /tutorial/query-array-of-documents
