<!-- Converted from tutorial/query-arrays.txt (reStructuredText). Includes are inlined. -->

# Query an Array

You can query arrays in MongoDB using the following methods:

- Your programming language's driver.
- The MongoDB Atlas UI. To learn more, see 
  query-array-atlas-ui.
- `MongoDB Compass`.

----------

→ Use the **Select your language** drop-down menu in the
upper-right to set the language of the following examples or select
MongoDB Compass.

----------

tabs:
  - id: shell
    content: |
      This page provides examples of query operations on array fields using the
      `db.collection.find()` method in `mongosh`.

      The examples on this page use the `inventory` collection. Connect to a
      test database in your MongoDB instance then create the `inventory`
      collection:

  - id: compass
    content: |
      This page provides examples of query operations on array fields using
      MongoDB Compass. 

      The examples on this page use the `inventory` collection. Connect to a
      test database in your MongoDB instance then create the `inventory`
      collection:

  - id: python
    content: |
      This page provides examples of query operations on array fields using the
      `pymongo.collection.Collection.find` method in the
      [PyMongo](https://www.mongodb.com/docs/languages/python/pymongo-driver/current/)
      Python driver.

      The examples on this page use the `inventory` collection. Connect to a
      test database in your MongoDB instance then create the `inventory`
      collection:

  - id: motor
    content: |
      This page provides examples of query operations on array fields using the
      `motor.motor_asyncio.AsyncIOMotorCollection.find`
      method in the [Motor](https://motor.readthedocs.io/en/stable/)
      driver.

      The examples on this page use the `inventory` collection. Connect to a
      test database in your MongoDB instance then create the `inventory`
      collection:

  - id: java-sync
    content: |
      This page provides examples of query operations on array fields using the
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
      This page provides examples of query operations on array fields using the
      [com.mongodb.reactivestreams.client.MongoCollection.find](http://mongodb.github.io/mongo-java-driver-reactivestreams/1.6/javadoc/com/mongodb/reactivestreams/client/MongoCollection.html#find())
      method in the MongoDB [Java Reactive Streams Driver](http://mongodb.github.io/mongo-java-driver-reactivestreams/1.6/).

      The examples on this page use the `inventory` collection. Connect to a
      test database in your MongoDB instance then create the `inventory`
      collection:

  - id: nodejs
    content: |
      This page provides examples of query operations on array fields using the
      `Collection.find()` method in
      the `MongoDB Node.js Driver`.

      The examples on this page use the `inventory` collection. Connect to a
      test database in your MongoDB instance then create the `inventory`
      collection:

  - id: php
    content: |
      This page provides examples of query operations on array fields using the
      `MongoDBCollection::find()`
      method in the
      [MongoDB PHP Library](https://www.mongodb.com/docs/drivers/php-libraries/).

      The examples on this page use the `inventory` collection. Connect to a
      test database in your MongoDB instance then create the `inventory`
      collection:

  - id: ruby
    content: |
      This page provides examples of query operations on array fields using the
      `Mongo::Collection#find()`
      method in the
      `MongoDB Ruby Driver`.

      The examples on this page use the `inventory` collection. Connect to a
      test database in your MongoDB instance then create the `inventory`
      collection:

  - id: scala
    content: |
      This page provides examples of query operations on array fields using the
      `collection.find()` method
      in the
      [MongoDB Scala Driver](http://mongodb.github.io/mongo-scala-driver/).

      The examples on this page use the `inventory` collection. Connect to a
      test database in your MongoDB instance then create the `inventory`
      collection:

  - id: csharp
    content: |
      This page provides examples of query operations on array fields using the
      `MongoCollection.Find()`
      method in the
      [MongoDB C# Driver](https://mongodb.github.io/mongo-csharp-driver/).

      The examples on this page use the `inventory` collection. Connect to a
      test database in your MongoDB instance then create the `inventory`
      collection:

  - id: go
    content: |
      This page provides examples of query operations on array fields using the
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
         { item: "journal", qty: 25, tags: ["blank", "red"], dim_cm: [ 14, 21 ] },
         { item: "notebook", qty: 50, tags: ["red", "blank"], dim_cm: [ 14, 21 ] },
         { item: "paper", qty: 100, tags: ["red", "blank", "plain"], dim_cm: [ 14, 21 ] },
         { item: "planner", qty: 75, tags: ["blank", "red"], dim_cm: [ 22.85, 30 ] },
         { item: "postcard", qty: 45, tags: ["blue"], dim_cm: [ 10, 15.25 ] }
      ]);
      ```

  - id: compass
    content: |

      ```javascript
      [
          { "item": "journal", "qty": 25, "tags": ["blank", "red"], "dim_cm": [ 14, 21 ] },
          { "item": "notebook", "qty": 50, "tags": ["red", "blank"], "dim_cm": [ 14, 21 ] },
          { "item": "paper", "qty": 100, "tags": ["red", "blank", "plain"], "dim_cm": [ 14, 21 ] },
          { "item": "planner", "qty": 75, "tags": ["blank", "red"], "dim_cm": [ 22.85, 30 ] },
          { "item": "postcard", "qty": 45, "tags": ["blue"], "dim_cm": [ 10, 15.25 ] }
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
      (Code example not available offline: /driver-examples/node_query_arrays.js)

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

## Match an Array

tabs:
  - id: shell
    content: |
      To specify equality condition on an array, use the query
      document `{ <field>: <value> }` where `<value>` is the
      exact array to match, including the order of the elements.

  - id: compass
    content: |
      To specify equality condition on an array, use the query
      document `{ <field>: <value> }` where `<value>` is the
      exact array to match, including the order of the elements.

  - id: python
    content: |
      To specify equality condition on an array, use the query
      document `{ <field>: <value> }` where `<value>` is the
      exact array to match, including the order of the elements.

  - id: motor
    content: |
      To specify equality condition on an array, use the query
      document `{ <field>: <value> }` where `<value>` is the
      exact array to match, including the order of the elements.

  - id: java-sync
    content: |
      To specify equality condition on an array, use the query
      document `eq( <field>, <value>)` where `<value>` is
      the exact array to match, including the order of the
      elements.

  - id: java-async
    content: |
      To specify equality condition on an array, use the query
      document `eq( <field>, <value>)` where `<value>` is
      the exact array to match, including the order of the
      elements.

  - id: nodejs
    content: |
      To specify equality condition on an array, use the query
      document `{ <field>: <value> }` where `<value>` is the
      exact array to match, including the order of the elements.

  - id: php
    content: |
      To specify equality condition on an array, use the query
      document `[ <field> => <value> ]` where `<value>` is the
      exact array to match, including the order of the elements.

  - id: ruby
    content: |
      To specify equality condition on an array, use the query
      document `{ <field> => <value> }` where `<value>` is the
      exact array to match, including the order of the elements.

  - id: scala
    content: |
      To specify equality condition on an array, use the query
      document `equal( <field>, <value> )` where `<value>` is
      the exact array to match, including the order of the
      elements.

  - id: csharp
    content: |
      To specify equality condition on an array, construct a filter
      using the `Eq` method:

      ```csharp
      Builders<BsonDocument>.Filter.Eq(<field>, <value>)
      ```

      `<value>` is the exact array to match, including the
      order of the elements.

The following example queries for all documents where the field `tags`
value is an array with exactly two elements, `"red"` and `"blank"`,
in the specified order:

tabs:
  - id: shell
    content: |

      ```javascript
      db.inventory.find( { tags: ["red", "blank"] } )
      ```

  - id: compass
    content: |
      Copy the following filter into the Compass query bar and click
      Find:

      ```javascript
      { tags: ["red", "blank"] }
      ```

      (Figure: /images/compass-array-match-exact.png)

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
      (Code example not available offline: /driver-examples/node_query_arrays.js)

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

If, instead, you wish to find an array that contains both the elements
`"red"` and `"blank"`, without regard to order or other elements in
the array, use the `$all` operator:

tabs:
  - id: shell
    content: |

      ```javascript
      db.inventory.find( { tags: { $all: ["red", "blank"] } } )
      ```

  - id: compass
    content: |
      Copy the following filter into the Compass query bar and click
      Find:

      ```javascript
      { tags: { $all: ["red", "blank"] } }
      ```

      (Figure: /images/compass-array-match-all.png)

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
      (Code example not available offline: /driver-examples/node_query_arrays.js)

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

## Query an Array for an Element

tabs:
  - id: shell
    content: |
      To query if the array field contains at least *one* element
      with the specified value, use the filter
      `{ <field>: <value> }` where `<value>` is the element value.

  - id: python
    content: |
      To query if the array field contains at least *one* element
      with the specified value, use the filter
      `{ <field>: <value> }` where `<value>` is the element value.

  - id: motor
    content: |
      To query if the array field contains at least *one* element
      with the specified value, use the filter
      `{ <field>: <value> }` where `<value>` is the element value.

  - id: java-sync
    content: |

      To query if the array field contains at least *one* element
      with the specified value, use the filter
      `eq( <field>, <value>)` where `<value>` is the element value.

  - id: java-async
    content: |

      To query if the array field contains at least *one* element
      with the specified value, use the filter
      `eq( <field>, <value>)` where value is the element value.

  - id: nodejs
    content: |
      To query if the array field contains at least *one* element
      with the specified value, use the filter
      `{ <field>: <value> }` where `<value>` is the element value.

  - id: php
    content: |
      To query if the array field contains at least *one* element
      with the specified value, use the filter
      `[ <field> => <value> ]` where `<value>` is the element value.

  - id: ruby
    content: |
      To query if the array field contains at least *one* element
      with the specified value, use the filter
      `{ <field> => <value> }` where `<value>` is the element value.

  - id: scala
    content: |

      To query if the array field contains at least *one* element
      with the specified value, use the filter
      `equal( <field>, <value> )` where `<value>` is the element value.

  - id: csharp
    content: |
      To query if the array field contains at least *one* element
      with the specified value, construct a filter using the
      `Eq` method:

      ```csharp
      Builders<BsonDocument>.Filter.Eq(<field>, <value>)
      ```

      `<value>` is the element value to match.

The following example queries for all documents where `tags` is an
array that contains the string `"red"` as one of its elements:

tabs:
  - id: shell
    content: |

      ```javascript
      db.inventory.find( { tags: "red" } )
      ```

  - id: compass
    content: |
      Copy the following filter into the Compass query bar and click
      Find:

      ```javascript
      { tags: "red" }
      ```

      (Figure: /images/compass-array-elem-match.png)

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
      (Code example not available offline: /driver-examples/node_query_arrays.js)

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
      To specify conditions on the elements in the array field,
      use query operators in the
      query filter document:

      ```javascript
      { <array field>: { <operator1>: <value1>, ... } }
      ```

  - id: compass
    content: |
      To specify conditions on the elements in the array field,
      use query operators in the
      query filter document:

      ```javascript
      { <array field>: { <operator1>: <value1>, ... } }
      ```

  - id: python
    content: |
      To specify conditions on the elements in the array field,
      use query operators in the
      query filter document:

      ```python
      { <array field>: { <operator1>: <value1>, ... } }
      ```

  - id: motor
    content: |
      To specify conditions on the elements in the array field,
      use query operators in the
      query filter document:

      ```python
      { <array field>: { <operator1>: <value1>, ... } }
      ```

  - id: java-sync
    content: |
      To specify conditions on the elements in the array field,
      use query operators in the
      query filter document. For example:

      ```java
      and(gte(<array field>, <value1>), lt(<array field>, <value2>) ...)
      ```

  - id: java-async
    content: |
      To specify conditions on the elements in the array field,
      use query operators in the
      query filter document. For example:

      ```java
      and(gte(<array field>, <value1>), lt(<array field>, <value2>) ...)
      ```

  - id: nodejs
    content: |
      To specify conditions on the elements in the array field,
      use query operators in the
      query filter document:

      ```javascript
      { <array field>: { <operator1>: <value1>, ... } }
      ```

  - id: php
    content: |
      To specify conditions on the elements in the array field,
      use query operators in the
      query filter document:

      ```php
      [ <array field> => [ <operator1> => <value1>, ... ] ]
      ```

  - id: ruby
    content: |
      To specify conditions on the elements in the array field,
      use query operators in the
      query filter document:

      ```ruby
      { <array field> => { <operator1> => <value1>, ... } }
      ```

  - id: scala
    content: |
      To specify conditions on the elements in the array field,
      use query operators in the
      query filter document:

      ```scala
      and(gte(<array field>, <value1>), lt(<array field>, <value2>) ...)
      ```

  - id: csharp
    content: |
      To specify conditions on the elements in the array field,
      use query operators in the
      query filter document. For example:

      ```csharp
      var builder = Builders<BsonDocument>.Filter;
      builder.And(builder.Eq(<array field>, <value1>), builder.Lt(<array field>, <value2>));
      ```

For example, the following operation queries for all documents where the array
`dim_cm` contains at least one element whose value is greater than
`25`.

tabs:
  - id: shell
    content: |

      ```javascript
      db.inventory.find( { dim_cm: { $gt: 25 } } )
      ```

  - id: compass
    content: |
      Copy the following filter into the Compass query bar and click
      Find:

      ```javascript
      { dim_cm: { $gt: 25 } }
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
      (Code example not available offline: /driver-examples/node_query_arrays.js)

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

## Specify Multiple Conditions for Array Elements

When specifying compound conditions on array elements, you can specify
the query such that either a single array element meets these condition
or any combination of array elements meets the conditions.

### Query an Array with Compound Filter Conditions on the Array Elements

The following example queries for documents where the `dim_cm` array
contains elements that in some combination satisfy the query
conditions; e.g., one element can satisfy the greater than `15`
condition and another element can satisfy the less than `20`
condition, or a single element can satisfy both:

tabs:
  - id: shell
    content: |

      ```javascript
      db.inventory.find( { dim_cm: { $gt: 15, $lt: 20 } } )
      ```

  - id: compass
    content: |
      Copy the following filter into the Compass query bar and click
      Find:

      ```javascript
      { dim_cm: { $gt: 15, $lt: 20 } }
      ```

      (Figure: /images/compass-array-compound-filter.png)

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
      (Code example not available offline: /driver-examples/node_query_arrays.js)

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

### Query for an Array Element that Meets Multiple Criteria

Use `$elemMatch` operator to specify multiple criteria on the
elements of an array such that at least one array element satisfies all
the specified criteria.

The following example queries for documents where the `dim_cm` array
contains at least one element that is both greater than (`$gt`)
`22` and less than (`$lt`) `30`:

tabs:
  - id: shell
    content: |

      ```javascript
      db.inventory.find( { dim_cm: { $elemMatch: { $gt: 22, $lt: 30 } } } )
      ```

  - id: compass
    content: |
      Copy the following filter into the Compass query bar and click
      Find:

      ```javascript
      { dim_cm: { $elemMatch: { $gt: 22, $lt: 30 } } }
      ```

      (Figure: /images/compass-array-compound-multiple-criteria.png)

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
      (Code example not available offline: /driver-examples/node_query_arrays.js)

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

### Query for an Element by the Array Index Position

Using dot notation, you can specify query conditions for an
element at a particular index or position of the array. The array uses
zero-based indexing.

**Note:**

When querying using dot notation, the field and nested field must be
inside quotation marks.

The following example queries for all documents where the second
element in the array `dim_cm` is greater than `25`:

tabs:
  - id: shell
    content: |

      ```javascript
      db.inventory.find( { "dim_cm.1": { $gt: 25 } } )
      ```

  - id: compass
    content: |
      Copy the following filter into the Compass query bar and click
      Find:

      ```javascript
      { "dim_cm.1": { $gt: 25 } }
      ```

      (Figure: /images/compass-array-match-by-index.png)

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
      (Code example not available offline: /driver-examples/node_query_arrays.js)

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

### Query an Array by Array Length

Use the `$size` operator to query for arrays by number of
elements. For example, the following selects documents where the array
`tags` has 3 elements.

tabs:
  - id: shell
    content: |

      ```javascript
      db.inventory.find( { "tags": { $size: 3 } } )
      ```

  - id: compass
    content: |
      Copy the following filter into the Compass query bar and click
      Find:

      ```javascript
      { "tags": { $size: 3 } }
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
      (Code example not available offline: /driver-examples/node_query_arrays.js)

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

## Query an Array with MongoDB Atlas

The example in this section uses the sample movies dataset. To learn how to load the sample dataset 
into your MongoDB Atlas deployment, see Load Sample Data.

To query an array in MongoDB Atlas, follow these steps:

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

To query a document that contains an array, 
specify a query filter document.
A query filter document uses query operators to specify search conditions.
Use the following example documents to query array fields in the 
`sample_mflix.movies` collection.

To apply a query filter, copy an example document into the 
Filter search bar and click Apply.

**match:**

To specify an equality condition on an array, use the query 
document `{ <field>: <value> }` where `<value>` is 
the exact array to match, including the order of the elements.
The following example finds documents that have a `genres`
field that contains the `["Action", "Comedy"]` array in the 
specified order:

```
{ genres: ["Action", "Comedy"] }
```

To find an array that contains both the elements `Action` and
`Comedy`, without regard to order or other elements 
in the array, use the `$all` operator:

```
{ genres: { $all: ["Action", "Comedy"] } }
```

**element:**

To query if the array field contains at least one element with the 
specified value, use the filter `{ <field>: <value> }` where 
`<value>` is the element value.

The following example queries for all documents where the
`genres` field contains the string `Short` as one 
of its elements:

```
{ genres: "Short" }
```

To specify conditions on the elements in the array field,
use query operators in the
query filter document:

```
{ <array field>: { <operator1>: <value1>, ... } }
```

For example, the following operation uses the
`$nin` operator to query for all documents 
where the `genres` field does not contain `Drama`.

```
{ genres: { $nin: ["Drama"] } }
```

**multiple:**

When specifying compound conditions on array elements, you can specify
the query such that either a single array element meets these condition
or any combination of array elements meets the conditions.

### Query an Array with Compound Filter Conditions on the Array Elements

The following example queries for documents where the `cast` 
array contains elements that in some combination satisfy the query
conditions. For example, the following filter uses the `$regex`
and `$eq` operators to return documents where a single array element 
ends in `Olsen` and another element equals `Mary-Kate Olsen` or 
a single element that satisfies both conditions:

```
{ cast: { $regex: "Olsen$", $eq: "Mary-Kate Olsen" } }
```

This query filter returns movies that include `Mary-Kate Olsen` in
their cast, and movies that include both `Mary-Kate Olsen` and 
`Ashley Olsen` in their cast.

### Query for an Array Element that Meets Multiple Criteria

Use `$elemMatch` operator to specify multiple criteria on the
elements of an array such that at least one array element satisfies all
the specified criteria.

The following example uses the `$elemMatch` and `$ne` 
operators to query for documents where the `languages` array contains 
at least one element that is both not `null` and does not equal `English`.

```
{ languages: { $elemMatch: { $ne: null, $ne: "English" } } }
```

### Query for an Element by the Array Index Position

Using dot notation, you can specify query conditions for an
element at a particular index or position of the array. The array uses
zero-based indexing.

**Note:**

When querying using dot notation, the field and nested field must be
inside quotation marks.

The following example uses the `$ne` operator to query 
for all documents where the first element in the `countries` 
array is not equal to `USA`:

```
{ "countries.0": { $ne: "USA" }
```

### Query an Array by Array Length

Use the `$size` operator to query for arrays by number of
elements. For example, the following selects documents where the array
`genres` has 3 elements.

```
{ genres: { $size: 3 } }
```

      

## Additional Query Tutorials

For additional query examples, see:

- /tutorial/query-documents

- /tutorial/query-embedded-documents

- /tutorial/query-array-of-documents
