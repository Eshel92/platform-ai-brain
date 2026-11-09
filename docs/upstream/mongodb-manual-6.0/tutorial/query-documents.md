<!-- Converted from tutorial/query-documents.txt (reStructuredText). Includes are inlined. -->

# Query Documents

You can query documents in MongoDB by using the following
methods:

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
      `motor.motor_asyncio.AsyncIOMotorCollection.find`
      method in the [Motor](https://motor.readthedocs.io/en/stable/)
      driver.

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
      [MongoDB C# Driver](https://mongodb.github.io/mongo-csharp-driver/).

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

      ```javascript
      db.inventory.insertMany([
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
      query bar. The query filter 
      parameter determines the select criteria:

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

This operation uses a filter predicate of `{}`, which corresponds to
the following SQL statement:

```sql
SELECT * FROM inventory
```

tabs:
  - id: shell
    content: |
      For more information on the syntax of the method, see
      `find()`.

  - id: compass
    content: |
      For more information on the MongoDB Compass query bar, see
      Query Bar.

  - id: python
    content: |
      For more information on the syntax of the method, see
      `find`.

  - id: java-sync
    content: |
      For more information on the syntax of the method, see
      com.mongodb.client.MongoCollection.find_.

  - id: java-async
    content: |
      For more information on the syntax of the method, see
      [com.mongodb.reactivestreams.client.MongoCollection.find](http://mongodb.github.io/mongo-java-driver-reactivestreams/1.6/javadoc/com/mongodb/reactivestreams/client/MongoCollection.html#find()).

  - id: nodejs
    content: |

      To see supported options for the `find()` method, see
      `find()`.

  - id: php
    content: |
      For more information on the syntax of the method, see
      `find()`.

  - id: ruby
    content: |
      For more information on the syntax of the method, see
      `find()`.

  - id: scala
    content: |
      For more information on the syntax of the method, see
      `collection.find()`.

  - id: csharp
    content: |
      For more information on the syntax of the method, see
      `Find()`.

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

The following example selects from the `inventory` collection all
documents where the `status` equals `"D"`:

tabs:
  - id: shell
    content: |

      ```javascript
      db.inventory.find( { status: "D" } )
      ```

  - id: compass
    content: |
      Copy the following filter into the Compass query bar and click
      Find:

      ```javascript
      { status: "D" }
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

This operation uses a filter predicate of `{ status: "D" }`, which
corresponds to the following SQL statement:

```sql
SELECT * FROM inventory WHERE status = "D"
```

tabs:
  - id: compass
    content: |

      **Note:**

      The MongoDB Compass query bar autocompletes the current query
      based on the keys in your collection's documents, including
      keys in embedded sub-documents.

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

The following example retrieves all documents from the `inventory`
collection where `status` equals either `"A"` or `"D"`:

tabs:
  - id: shell
    content: |

      ```javascript
      db.inventory.find( { status: { $in: [ "A", "D" ] } } )
      ```

  - id: compass
    content: |
      Copy the following filter into the Compass query bar and click
      Find:

      ```javascript
      { status: { $in: [ "A", "D" ] } }
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

**Note:**

Although you can express this query using the `$or` operator,
use the `$in` operator rather than the `$or`
operator when performing equality checks on the same field.

The operation uses a filter predicate of
`{ status: { $in: [ "A", "D" ] } }`, which corresponds to the
following SQL statement:

```sql
SELECT * FROM inventory WHERE status in ("A", "D")
```

Refer to the /reference/operator/query document for the complete
list of MongoDB query operators.

## Specify `AND` Conditions

A compound query can specify conditions for more than one field in the
collection's documents. Implicitly, a logical `AND` conjunction
connects the clauses of a compound query so that the query selects the
documents in the collection that match all the conditions.

The following example retrieves all documents in the `inventory`
collection where the `status` equals `"A"` **and** `qty` is less
than (`$lt`) `30`:

tabs:
  - id: shell
    content: |

      ```javascript
      db.inventory.find( { status: "A", qty: { $lt: 30 } } )
      ```

  - id: compass
    content: |
      Copy the following filter into the Compass query bar and click
      Find:

      ```javascript
      { status: "A", qty: { $lt: 30 } }
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

The operation uses a filter predicate of
`{ status: "A", qty: { $lt: 30 } }`, which corresponds to the
following SQL statement:

```sql
SELECT * FROM inventory WHERE status = "A" AND qty < 30
```

See comparison operators for other
MongoDB comparison operators.

## Specify `OR` Conditions

Using the `$or` operator, you can specify a compound query
that joins each clause with a logical `OR` conjunction so that the
query selects the documents in the collection that match at least one
condition.

The following example retrieves all documents in the collection where
the `status` equals `"A"` **or** `qty` is less than
(`$lt`) `30`:

tabs:
  - id: shell
    content: |

      ```javascript
      db.inventory.find( { $or: [ { status: "A" }, { qty: { $lt: 30 } } ] } )
      ```

  - id: compass
    content: |
      Copy the following filter into the Compass query bar and click
      Find:

      ```javascript
      { $or: [ { status: "A" }, { qty: { $lt: 30 } } ] }
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

The operation uses a filter predicate of
`{ $or: [ { status: 'A' }, { qty: { $lt: 30 } } ] }`, which
corresponds to the following SQL statement:

```sql
SELECT * FROM inventory WHERE status = "A" OR qty < 30
```

**Note:**

Queries that use comparison operators are subject to type-bracketing.

## Specify `AND` as well as `OR` Conditions

In the following example, the compound query document selects all
documents in the collection where the `status` equals `"A"`
**and** *either* `qty` is less than (`$lt`) `30` *or*
`item` starts with the character `p`:

tabs:
  - id: shell
    content: |

      ```javascript
      db.inventory.find( {
           status: "A",
           $or: [ { qty: { $lt: 30 } }, { item: /^p/ } ]
      } )
      ```

  - id: compass
    content: |
      Copy the following filter into the Compass query bar and click
      Find:

      ```javascript
      { status: "A", $or: [ { qty: { $lt: 30 } }, { item: /^p/ } ] }
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

The operation uses a filter predicate of:

```javascript
{
   status: 'A',
   $or: [
     { qty: { $lt: 30 } }, { item: { $regex: '^p' } }
   ]
}
```

   
which corresponds to the following SQL statement:

```sql
SELECT * FROM inventory WHERE status = "A" AND ( qty < 30 OR item LIKE "p%")
```

**Note:**

MongoDB supports regular expressions `$regex` queries to
perform string pattern matches.

## Query Documents with MongoDB Atlas

The example in this section uses the sample movies dataset. To learn how to load the sample dataset 
into your MongoDB Atlas deployment, see Load Sample Data.

To project fields to return from a query in MongoDB Atlas, follow these
steps:

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

This query filter returns all documents
in the `sample_mflix.movies` collection where the `year`
field matches `1924`.

## Additional Query Tutorials

For additional query examples, see:

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
      The MongoDB Compass Find operation opens a
      cursor to the matching
      documents of the collection based on the find query.

      For more information on sampling in MongoDB Compass, see the
      Compass FAQ.

  - id: python
    content: |
      The `pymongo.collection.Collection.find` method
      returns a cursor to the
      matching documents. See the PyMongo documentation for
      [iterating over a cursor](https://pymongo.readthedocs.io/en/stable/tutorial.html#querying-for-more-than-one-document).

  - id: java-sync
    content: |
      The com.mongodb.client.MongoCollection.find_ method returns an
      instance of the com.mongodb.client.FindIterable_ interface.

  - id: java-async
    content: |
      [com.mongodb.reactivestreams.client.MongoCollection.find](http://mongodb.github.io/mongo-java-driver-reactivestreams/1.6/javadoc/com/mongodb/reactivestreams/client/MongoCollection.html#find())
      returns an instance of the [com.mongodb.reactivestreams.client.FindPublisher](http://mongodb.github.io/mongo-java-driver-reactivestreams/1.6/javadoc/com/mongodb/reactivestreams/client/FindPublisher.html)
      interface.

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
      for [iterating over a cursor](http://api.mongodb.com/ruby/current/Mongo/Cursor.html#each-instance_method).

  - id: scala
    content: |
      The `collection.find()`
      method returns the find [Observable](http://mongodb.github.io/mongo-scala-driver/2.1/reference/observables/).

  - id: csharp
    content: |
      The `MongoCollection.Find()`
      method returns a cursor to
      the matching documents. See the MongoDB C# driver
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
shards, read concern allows clients to choose a
level of isolation for their reads. For more information, see
/reference/read-concern.

### Query Result Format

When you run a find operation with a MongoDB driver or `mongosh`, the
command returns a cursor that manages query results. The query
results are not returned as an array of documents.

To learn how to iterate through documents in a cursor, refer to your
`driver's documentation`. If you are using `mongosh`, see
read-operations-cursors.

## Additional Methods and Options

tabs:
  - id: shell
    content: |

      The following methods can also read documents from a collection:

      - `db.collection.findOne`

      - In aggregation pipeline, the
        `$match` pipeline stage provides access to MongoDB
        queries.

      **Note:**

      The `db.collection.findOne()` method also performs a read
      operation to return a single document. Internally, the
      `db.collection.findOne()` method is the
      `db.collection.find()` method with a limit of 1.

  - id: compass
    content: |

      In addition to `filter`, MongoDB Compass also allows the
      following options to be passed to the query bar:

      |  |  |
      |---|---|
      | `Project` | Specify which fields to return in the resulting data. |
      | `Sort` | Specify the sort order of the returned documents. |
      | `Skip` | Specify the first n-number of document to skip before returning the result set. |
      | `Limit` | Specify the maximum number of documents to return. |

  - id: python
    content: |

      The following methods can also read documents from a collection:

      - `pymongo.collection.Collection.find_one`

      - In aggregation pipeline, the
        `$match` pipeline stage provides access to MongoDB
        queries. See the [PyMongo Aggregation Examples](https://pymongo.readthedocs.io/en/stable/examples/aggregation.html).

      **Note:**

      The `pymongo.collection.Collection.find_one`
      method also performs a read operation to return a single
      document. Internally, the
      `pymongo.collection.Collection.find_one` method is
      the `pymongo.collection.Collection.find` method
      with a limit of 1.

  - id: java-sync
    content: |

      The following methods can also read documents from a collection:

      - In the aggregation pipeline,
        the `$match` pipeline stage provides access to
        MongoDB queries. See the `Java Synchronous Driver Aggregation
        Examples`_.

  - id: java-async
    content: |

      The following methods can also read documents from a collection:

      - In aggregation pipeline,
        the `$match` pipeline stage provides access to
        MongoDB queries. See [com.mongodb.reactivestreams.client.MongoCollection.aggregate](http://mongodb.github.io/mongo-java-driver-reactivestreams/1.6/javadoc/com/mongodb/reactivestreams/client/MongoCollection.html#aggregate(java.util.List))
        for more information.

  - id: nodejs
    content: |

      The following methods can also read documents from a collection:

      - `Collection.findOne()`

      - In aggregation pipeline, the
        `$match` pipeline stage provides access to MongoDB
        queries. See the MongoDB Node.js Driver's
        `aggregation tutorial`.

      **Note:**

      The `Collection.findOne()`
      method also performs a read operation to return a single
      document. Internally, the
      `Collection.findOne()`
      method is the
      `Collection.find()` method
      with a limit of 1.

  - id: php
    content: |

      The following methods can also read documents from a collection:

      - `MongoDBCollection::findOne()`

      - In aggregation pipeline, the
        `$match` pipeline stage provides access to MongoDB
        queries. See the MongoDB PHP Library's
        aggregation example.

      **Note:**

      The `MongoDBCollection::findOne()`
      method also performs a read operation to return a single
      document. Internally, the
      `MongoDBCollection::findOne()`
      method is the
      `MongoDBCollection::find()`
      method with a limit of 1.

  - id: ruby
    content: |

      The following methods can also read documents from a collection:

      - In aggregation pipeline, the
        `$match` pipeline stage provides access to MongoDB
        queries. See the MongoDB Ruby driver's
        `aggregation examples`.

  - id: scala
    content: |

      The following methods can also read documents from a collection:

      - In aggregation pipeline, the
        `$match` pipeline stage provides access to MongoDB
        queries. See the MongoDB Scala driver's `aggregate method`.

  - id: csharp
    content: |

      The following methods can also read documents from a collection:

      - `MongoCollection.FindOne()`

      - In aggregation pipeline, the
        `$match` pipeline stage provides access to MongoDB
        queries. See the MongoDB C# driver's
        [LINQ documentation](https://www.mongodb.com/docs/drivers/csharp/current/fundamentals/linq/).

      **Note:**

      The `MongoCollection.FindOne()`
      method also performs a read operation to return a single
      document. Internally, the
      `MongoCollection.FindOne()`
      method is the
      `MongoCollection.Find()`
      method with a limit of 1.

  - id: go
    content: |

      The following methods can also read documents from a collection:

      - `Collection.FindOne`

      - In aggregation pipeline,
        the `$match` pipeline stage provides access to
        MongoDB queries. See
        `Collection.Aggregate`.
