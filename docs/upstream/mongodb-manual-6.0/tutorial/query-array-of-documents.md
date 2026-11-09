<!-- Converted from tutorial/query-array-of-documents.txt (reStructuredText). Includes are inlined. -->

# Query an Array of Embedded Documents

   

You can query documents in MongoDB by using the following
methods:

- Your programming language's driver.
- The MongoDB Atlas UI. To learn more, see 
  query-array-documents-atlas-ui.
- `MongoDB Compass`.

----------

→ Use the **Select your language** drop-down menu in the
upper-right to set the language of the following examples or select
MongoDB Compass.

----------

tabs:
  - id: shell
    content: |
      This page provides examples of query operations on an array of nested documents using the
      `db.collection.find()` method in `mongosh`.

      The examples on this page use the `inventory` collection. Connect to a
      test database in your MongoDB instance then create the `inventory`
      collection:

  - id: compass
    content: |
      This page provides examples of query operations on an array of nested documents using
      MongoDB Compass. 

      The examples on this page use the `inventory` collection. Connect to a
      test database in your MongoDB instance then create the `inventory`
      collection:

  - id: python
    content: |
      This page provides examples of query operations on an array of nested documents using the
      `pymongo.collection.Collection.find` method in the
      [PyMongo](https://www.mongodb.com/docs/languages/python/pymongo-driver/current/)
      Python driver.

      The examples on this page use the `inventory` collection. Connect to a
      test database in your MongoDB instance then create the `inventory`
      collection:

  - id: motor
    content: |
      This page provides examples of query operations on an array of nested documents using the
      `motor.motor_asyncio.AsyncIOMotorCollection.find`
      method in the [Motor](https://motor.readthedocs.io/en/stable/)
      driver.

      The examples on this page use the `inventory` collection. Connect to a
      test database in your MongoDB instance then create the `inventory`
      collection:

  - id: java-sync
    content: |
      This page provides examples of query operations on an array of nested documents using the
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
      This page provides examples of query operations on an array of nested documents using the
      [com.mongodb.reactivestreams.client.MongoCollection.find](http://mongodb.github.io/mongo-java-driver-reactivestreams/1.6/javadoc/com/mongodb/reactivestreams/client/MongoCollection.html#find())
      method in the MongoDB [Java Reactive Streams Driver](http://mongodb.github.io/mongo-java-driver-reactivestreams/1.6/).

      The examples on this page use the `inventory` collection. Connect to a
      test database in your MongoDB instance then create the `inventory`
      collection:

  - id: nodejs
    content: |
      This page provides examples of query operations on an array of nested documents using the
      `Collection.find()` method in
      the `MongoDB Node.js Driver`.

      The examples on this page use the `inventory` collection. Connect to a
      test database in your MongoDB instance then create the `inventory`
      collection:

  - id: php
    content: |
      This page provides examples of query operations on an array of nested documents using the
      `MongoDBCollection::find()`
      method in the
      [MongoDB PHP Library](https://www.mongodb.com/docs/drivers/php-libraries/).

      The examples on this page use the `inventory` collection. Connect to a
      test database in your MongoDB instance then create the `inventory`
      collection:

  - id: ruby
    content: |
      This page provides examples of query operations on an array of nested documents using the
      `Mongo::Collection#find()`
      method in the
      `MongoDB Ruby Driver`.

      The examples on this page use the `inventory` collection. Connect to a
      test database in your MongoDB instance then create the `inventory`
      collection:

  - id: scala
    content: |
      This page provides examples of query operations on an array of nested documents using the
      `collection.find()` method
      in the
      [MongoDB Scala Driver](http://mongodb.github.io/mongo-scala-driver/).

      The examples on this page use the `inventory` collection. Connect to a
      test database in your MongoDB instance then create the `inventory`
      collection:

  - id: csharp
    content: |
      This page provides examples of query operations on an array of nested documents using the
      `MongoCollection.Find()`
      method in the
      [MongoDB C# Driver](https://mongodb.github.io/mongo-csharp-driver/).

      The examples on this page use the `inventory` collection. Connect to a
      test database in your MongoDB instance then create the `inventory`
      collection:

  - id: go
    content: |
      This page provides examples of query operations on an array of nested documents using the
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
         { item: "journal", instock: [ { warehouse: "A", qty: 5 }, { warehouse: "C", qty: 15 } ] },
         { item: "notebook", instock: [ { warehouse: "C", qty: 5 } ] },
         { item: "paper", instock: [ { warehouse: "A", qty: 60 }, { warehouse: "B", qty: 15 } ] },
         { item: "planner", instock: [ { warehouse: "A", qty: 40 }, { warehouse: "B", qty: 5 } ] },
         { item: "postcard", instock: [ { warehouse: "B", qty: 15 }, { warehouse: "C", qty: 35 } ] }
      ]);
      ```

  - id: compass
    content: |

      ```javascript
      [
          { "item": "journal", "instock": [ { "warehouse": "A", "qty": 5 }, { "warehouse": "C", "qty": 15 } ] },
          { "item": "notebook", "instock": [ { "warehouse": "C", "qty": 5 } ] },
          { "item": "paper", "instock": [ { "warehouse": "A", "qty": 60 }, { "warehouse": "B", "qty": 15 } ] },
          { "item": "planner", "instock": [ { "warehouse": "A", "qty": 40 }, { "warehouse": "B", "qty": 5 } ] },
          { "item": "postcard", "instock": [ { "warehouse": "B","qty": 15 }, { "warehouse": "C", "qty": 35 } ] }
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
      (Code example not available offline: /driver-examples/node_query_array_of_documents.js)

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

## Query for a Document Nested in an Array

The following example selects all documents where an element in the
`instock` array matches the specified document:

tabs:
  - id: shell
    content: |

      ```javascript
      db.inventory.find( { "instock": { warehouse: "A", qty: 5 } } )
      ```

  - id: compass
    content: |
      Copy the following filter into the Compass query bar and click
      Find:

      ```javascript
      { "instock": { warehouse: "A", qty: 5 } }
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
      (Code example not available offline: /driver-examples/node_query_array_of_documents.js)

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

Equality matches on the whole embedded/nested document require an
*exact* match of the specified document, including the field order. For
example, the following query does not match any documents in the
`inventory` collection:

tabs:
  - id: shell
    content: |

      ```javascript
      db.inventory.find( { "instock": { qty: 5, warehouse: "A" } } )
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
      (Code example not available offline: /driver-examples/node_query_array_of_documents.js)

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

## Specify a Query Condition on a Field in an Array of Documents

### Specify a Query Condition on a Field Embedded in an Array of Documents

If you do not know the index position of the document nested in the
array, concatenate the name of the array field, with a dot (`.`) and
the name of the field in the nested document.

The following example selects all documents where the `instock` array
has at least one embedded document that contains the field `qty`
whose value is less than or equal to `20`:

tabs:
  - id: shell
    content: |

      ```javascript
      db.inventory.find( { 'instock.qty': { $lte: 20 } } )
      ```

  - id: compass
    content: |
      Copy the following filter into the Compass query bar and click
      Find:

      ```javascript
      { 'instock.qty': { $lte: 20 } }
      ```

      (Figure: /images/compass-find-array-embedded-field-condition.png)

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
      (Code example not available offline: /driver-examples/node_query_array_of_documents.js)

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

### Use the Array Index to Query for a Field in the Embedded Document

Using dot notation, you can specify query conditions for
field in a document at a particular index or position of the array. The
array uses zero-based indexing.

**Note:**

When querying using dot notation, the field and index must be
inside quotation marks.

The following example selects all documents where the `instock` array
has as its first element a document that contains the field `qty`
whose value is less than or equal to `20`:

tabs:
  - id: shell
    content: |

      ```javascript
      db.inventory.find( { 'instock.0.qty': { $lte: 20 } } )
      ```

  - id: compass
    content: |
      Copy the following filter into the Compass query bar and click
      Find:

      ```javascript
      { 'instock.0.qty': { $lte: 20 } }
      ```

      (Figure: /images/compass-find-array-index-embedded-doc.png)

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
      (Code example not available offline: /driver-examples/node_query_array_of_documents.js)

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

## Specify Multiple Conditions for Array of Documents

When specifying conditions on more than one field nested in an array of
documents, you can specify the query such that either a single document
meets these condition or any combination of documents (including a
single document) in the array meets the conditions.

### A Single Nested Document Meets Multiple Query Conditions on Nested Fields

Use `$elemMatch` operator to specify multiple criteria on an
array of embedded documents such that at least one embedded document
satisfies all the specified criteria.

The following example queries for documents where the `instock` array
has at least one embedded document that contains both the field
`qty` equal to `5` and the field `warehouse` equal
to `A`:

tabs:
  - id: shell
    content: |

      ```javascript
      db.inventory.find( { "instock": { $elemMatch: { qty: 5, warehouse: "A" } } } )
      ```

  - id: compass
    content: |
      Copy the following filter into the Compass query bar and click
      Find:

      ```javascript
      { "instock": { $elemMatch: { qty: 5, warehouse: "A" } } }
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
      (Code example not available offline: /driver-examples/node_query_array_of_documents.js)

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

The following example queries for documents where the `instock` array
has at least one embedded document that contains the field `qty` that
is greater than `10` and less than or equal to `20`:

tabs:
  - id: shell
    content: |

      ```javascript
      db.inventory.find( { "instock": { $elemMatch: { qty: { $gt: 10, $lte: 20 } } } } )
      ```

  - id: compass
    content: |
      Copy the following filter into the Compass query bar and click
      Find:

      ```javascript
      { "instock": { $elemMatch: { qty: { $gt: 10, $lte: 20 } } } }
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
      (Code example not available offline: /driver-examples/node_query_array_of_documents.js)

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

### Combination of Elements Satisfies the Criteria

If the compound query conditions on an array field do not use the
`$elemMatch` operator, the query selects those documents whose
array contains any combination of elements that satisfies the
conditions.

For example, the following query matches documents where any document
nested in the `instock` array has the `qty` field greater than
`10` and any document (but not necessarily the same embedded
document) in the array has the `qty` field less than or equal to
`20`:

tabs:
  - id: shell
    content: |

      ```javascript
      db.inventory.find( { "instock.qty": { $gt: 10,  $lte: 20 } } )
      ```

  - id: compass
    content: |
      Copy the following filter into the Compass query bar and click
      Find:

      ```javascript
      { "instock.qty": { $gt: 10,  $lte: 20 } }
      ```

      (Figure: /images/compass-array-match-combination-of-elements.png)

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
      (Code example not available offline: /driver-examples/node_query_array_of_documents.js)

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

The following example queries for documents where the `instock` array
has at least one embedded document that contains the field `qty`
equal to `5` and at least one embedded document (but not necessarily
the same embedded document) that contains the field `warehouse` equal
to `A`:

tabs:
  - id: shell
    content: |

      ```javascript
      db.inventory.find( { "instock.qty": 5, "instock.warehouse": "A" } )
      ```

  - id: compass
    content: |
      Copy the following filter into the Compass query bar and click
      Find:

      ```javascript
      { "instock.qty": 5, "instock.warehouse": "A" }
      ```

      (Figure: /images/compass-array-match-combination-of-elements-2.png)

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
      (Code example not available offline: /driver-examples/node_query_array_of_documents.js)

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

## Query an Array of Documents with MongoDB Atlas

The example in this section uses the sample training dataset. To learn how to load the sample
dataset into your MongoDB Atlas deployment, see Load Sample Data.

To query an array of documents in MongoDB Atlas, follow these steps:

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
   sample_training database.
#. Select the grades collection.

**Step 3: Specify the Filter field**

Specify the query filter document
in the Filter field. A query filter document uses 
query operators to specify
search conditions.

Copy the following query filter document into the 
Filter search bar:

```javascript
{"scores.type": "exam"}
```

**Step 4: Click Apply**

This query filter returns all documents in the `sample_training.grades` 
collection that contain a subdocument in the `scores` array where 
`type` is set to `exam`. The full document, including the entire 
`scores` array, is returned. For more information on modifying the 
returned array, see project-array-elements-in-returned-array. 

## Additional Query Tutorials

For additional query examples, see:

- /tutorial/query-arrays

- /tutorial/query-documents

- /tutorial/query-embedded-documents
