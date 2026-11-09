<!-- Converted from tutorial/project-fields-from-query-results.txt (reStructuredText). Includes are inlined. -->

# Project Fields to Return from Query

----------

→ Use the **Select your language** drop-down menu in the
upper-right to set the language of the following examples.

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
      `motor.motor_asyncio.AsyncIOMotorCollection.find`
      method in the [Motor](https://motor.readthedocs.io/en/stable/)
      driver.

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
      [MongoDB C# Driver](https://mongodb.github.io/mongo-csharp-driver/).

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

      (Code example not available offline: /driver-examples/DocumentationExamples.cs)

  - id: go
    content: |
      (Code example not available offline: /driver-examples/go_examples.go)

## Return All Fields in Matching Documents

tabs:
  - id: shell
    content: |
      If you do not specify a projection document, the
      `db.collection.find()` method returns all fields in the
      matching documents.

  - id: compass
    content: |
      If you do not specify a projection document, Compass
      returns all fields in the matching documents.

  - id: python
    content: |
      If you do not specify a projection document, the
      `find` method returns
      all fields in the matching documents.

  - id: java-sync
    content: |
      If you do not specify a projection, the
      com.mongodb.client.MongoCollection.find_ method returns all
      fields in the matching documents.

  - id: java-async
    content: |
      If you do not specify a projection, the [com.mongodb.reactivestreams.client.MongoCollection.find](http://mongodb.github.io/mongo-java-driver-reactivestreams/1.6/javadoc/com/mongodb/reactivestreams/client/MongoCollection.html#find(org.bson.conversions.Bson))
      method returns all fields in the matching documents.

  - id: nodejs
    content: |
      If you do not specify a projection document, the
      `find()` method yields all
      fields in the matching documents.

  - id: php
    content: |
      If you do not specify a projection document, the
      `find()`
      method returns all fields in the matching documents

  - id: ruby
    content: |
      If you do not specify a projection document, the
      `find()`
      method returns all fields in the matching documents.

  - id: scala
    content: |
      If you do not specify a projection, the
      `collection.find()`
      method returns all fields in the matching documents.

  - id: csharp
    content: |
      If you do not specify a projection filter, the
      `MongoCollection.Find()`
      method returns all fields in the matching documents.

The following example returns all fields from all documents in the
`inventory` collection where the `status` equals `"A"`:

tabs:
  - id: shell
    content: |

      ```javascript
      db.inventory.find( { status: "A" } )
      ```

  - id: compass
    content: |
      1. Copy the following expression into the Filter
         field:

         ```javascript
         { status: "A" }
         ```

      #. Click Find.

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

      (Code example not available offline: /driver-examples/DocumentationExamples.cs)

  - id: go
    content: |
      (Code example not available offline: /driver-examples/go_examples.go)

The operation corresponds to the following SQL statement:

```sql
SELECT * from inventory WHERE status = "A"
```

## Return the Specified Fields and the `_id` Field Only

A projection can explicitly include several fields by setting the
`<field>` to `1` in the projection document. The following
operation returns all documents that match the query. In the result
set, only the `item`, `status` and, by default, the `_id` fields
return in the matching documents.

tabs:
  - id: shell
    content: |

      ```javascript
      db.inventory.find( { status: "A" }, { item: 1, status: 1 } )
      ```

  - id: compass
    content: |

      1. Copy the following expression into the Filter
         field:

         ```javascript
         { status: "A" }
         ```

      #. Click Options to open the additional query
         options.

      #. Copy the following expression into the Project
         field:

         ```javascript
         { item: 1, status: 1 }
         ```

      #. Click Find.

  - id: python
    content: |

      (Code example not available offline: /driver-examples/test_examples.py)

  - id: motor
    content: |

      (Code example not available offline: /driver-examples/test_examples_motor.py)

  - id: java-sync
    content: |
      To specify a projection document, chain the
      com.mongodb.client.FindIterable.projection_ method to the
      `find` method. The example uses the
      com.mongodb.client.model.Projections_ class to create the
      projection documents.

      (Code example not available offline: /driver-examples/DocumentationSamples.java)

  - id: java-async
    content: |

      (Code example not available offline: /driver-examples/AsyncDocumentationSamples.java)

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

      (Code example not available offline: /driver-examples/DocumentationExamples.cs)

  - id: go
    content: |
      (Code example not available offline: /driver-examples/go_examples.go)

The operation corresponds to the following SQL statement:

```sql
SELECT _id, item, status from inventory WHERE status = "A"
```

## Suppress `_id` Field

You can remove the `_id` field from the results by setting it to
`0` in the projection, as in the following example:

tabs:
  - id: shell
    content: |

      ```javascript
      db.inventory.find( { status: "A" }, { item: 1, status: 1, _id: 0 } )
      ```

  - id: compass
    content: |
      1. Copy the following expression into the Filter
         field:

         ```javascript
         { status: "A" }
         ```

      #. Click Options to open the additional query
         options.

      #. Copy the following expression into the Project
         field:

         ```javascript
         { item: 1, status: 1, _id: 0 }
         ```

      #. Click Find.

  - id: python
    content: |

      (Code example not available offline: /driver-examples/test_examples.py)

  - id: motor
    content: |

      (Code example not available offline: /driver-examples/test_examples_motor.py)

  - id: java-sync
    content: |
      To specify a projection document, chain the
      com.mongodb.client.FindIterable.projection_ method to the
      `find` method. The example uses the
      com.mongodb.client.model.Projections_ class to create the
      projection documents.

      (Code example not available offline: /driver-examples/DocumentationSamples.java)

  - id: java-async
    content: |

      (Code example not available offline: /driver-examples/AsyncDocumentationSamples.java)

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

      (Code example not available offline: /driver-examples/DocumentationExamples.cs)

  - id: go
    content: |
      (Code example not available offline: /driver-examples/go_examples.go)

The operation corresponds to the following SQL statement:

```sql
SELECT item, status from inventory WHERE status = "A"
```

**Note:**

With the exception of the `_id` field, you cannot combine inclusion
and exclusion statements in projection documents.

## Return All But the Excluded Fields

Instead of listing the fields to return in the matching document, you
can use a projection to exclude specific fields. The following example
which returns all fields except for the `status` and the `instock`
fields in the matching documents:

tabs:
  - id: shell
    content: |

      ```javascript
      db.inventory.find( { status: "A" }, { status: 0, instock: 0 } )
      ```

  - id: compass
    content: |
      1. Copy the following expression into the Filter
         field:

         ```javascript
         { status: "A" }
         ```

      #. Click Options to open the additional query
         options.

      #. Copy the following expression into the Project
         field:

         ```javascript
         { status: 0, instock: 0 }
         ```

      #. Click Find.

  - id: python
    content: |

      (Code example not available offline: /driver-examples/test_examples.py)

  - id: motor
    content: |

      (Code example not available offline: /driver-examples/test_examples_motor.py)

  - id: java-sync
    content: |
      To specify a projection document, chain the
      com.mongodb.client.FindIterable.projection_ method to the
      `find` method. The example uses the
      com.mongodb.client.model.Projections_ class to create the
      projection documents.

      (Code example not available offline: /driver-examples/DocumentationSamples.java)

  - id: java-async
    content: |

      (Code example not available offline: /driver-examples/AsyncDocumentationSamples.java)

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

      (Code example not available offline: /driver-examples/DocumentationExamples.cs)

  - id: go
    content: |
      (Code example not available offline: /driver-examples/go_examples.go)

**Note:**

With the exception of the `_id` field, you cannot combine inclusion
and exclusion statements in projection documents.

## Return Specific Fields in Embedded Documents

You can return specific fields in an embedded document. Use the
dot notation to refer to the embedded
field and set to `1` in the projection document.

The following example returns:

- The `_id` field (returned by default),
- The `item` field,
- The `status` field,
- The `uom` field in the `size` document.

The `uom` field remains embedded in the `size` document.

tabs:
  - id: shell
    content: |

      ```javascript
      db.inventory.find(
         { status: "A" },
         { item: 1, status: 1, "size.uom": 1 }
      )
      ```

  - id: compass
    content: |
      1. Copy the following expression into the Filter
         field:

         ```javascript
         { status: "A" }
         ```

      #. Click Options to open the additional query
         options.

      #. Copy the following expression into the Project
         field:

         ```javascript
         { item: 1, status: 1, "size.uom": 1 }
         ```

      #. Click Find.

  - id: python
    content: |

      (Code example not available offline: /driver-examples/test_examples.py)

  - id: motor
    content: |

      (Code example not available offline: /driver-examples/test_examples_motor.py)

  - id: java-sync
    content: |
      To specify a projection document, chain the
      com.mongodb.client.FindIterable.projection_ method to the
      `find` method. The example uses the
      com.mongodb.client.model.Projections_ class to create the
      projection documents.

      (Code example not available offline: /driver-examples/DocumentationSamples.java)

  - id: java-async
    content: |

      (Code example not available offline: /driver-examples/AsyncDocumentationSamples.java)

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

      (Code example not available offline: /driver-examples/DocumentationExamples.cs)

  - id: go
    content: |
      (Code example not available offline: /driver-examples/go_examples.go)

You can also specify embedded fields using the nested form. For example, 
`{ item: 1, status: 1, size: { uom: 1 } }`.

## Suppress Specific Fields in Embedded Documents

You can suppress specific fields in an embedded document. Use the
dot notation to refer to the embedded
field in the projection document and set to `0`.

The following example specifies a projection to exclude the `uom`
field inside the `size` document. All other fields are returned in
the matching documents:

tabs:
  - id: shell
    content: |

      ```javascript
      db.inventory.find(
         { status: "A" },
         { "size.uom": 0 }
      )
      ```

  - id: compass
    content: |
      1. Copy the following expression into the Filter
         field:

         ```javascript
         { status: "A" }
         ```

      #. Click Options to open the additional query
         options.

      #. Copy the following expression into the Project
         field:

         ```javascript
         { "size.uom": 0 }
         ```

      #. Click Find.

  - id: python
    content: |

      (Code example not available offline: /driver-examples/test_examples.py)

  - id: motor
    content: |

      (Code example not available offline: /driver-examples/test_examples_motor.py)

  - id: java-sync
    content: |
      To specify a projection document, chain the
      com.mongodb.client.FindIterable.projection_ method to the
      `find` method. The example uses the
      com.mongodb.client.model.Projections_ class to create the
      projection documents.

      (Code example not available offline: /driver-examples/DocumentationSamples.java)

  - id: java-async
    content: |

      (Code example not available offline: /driver-examples/AsyncDocumentationSamples.java)

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

      (Code example not available offline: /driver-examples/DocumentationExamples.cs)

  - id: go
    content: |
      (Code example not available offline: /driver-examples/go_examples.go)

You can also specify embedded fields using the nested form. For example, 
`{ size: { uom: 0 } }`.

## Projection on Embedded Documents in an Array

Use dot notation to project specific
fields inside documents embedded in an array.

The following example specifies a projection to return:

- The `_id` field (returned by default),
- The `item` field,
- The `status` field,
- The `qty` field in the documents embedded in the `instock` array.

tabs:
  - id: shell
    content: |

      ```javascript
      db.inventory.find( { status: "A" }, { item: 1, status: 1, "instock.qty": 1 } )
      ```

  - id: compass
    content: |
      1. Copy the following expression into the Filter
         field:

         ```javascript
         { status: "A" }
         ```

      #. Click Options to open the additional query
         options.

      #. Copy the following expression into the Project
         field:

         ```javascript
         { item: 1, status: 1, "instock.qty": 1 }
         ```

      #. Click Find.

  - id: python
    content: |

      (Code example not available offline: /driver-examples/test_examples.py)

  - id: motor
    content: |

      (Code example not available offline: /driver-examples/test_examples_motor.py)

  - id: java-sync
    content: |
      To specify a projection document, chain the
      com.mongodb.client.FindIterable.projection_ method to the
      `find` method. The example uses the
      com.mongodb.client.model.Projections_ class to create the
      projection documents.

      (Code example not available offline: /driver-examples/DocumentationSamples.java)

  - id: java-async
    content: |

      (Code example not available offline: /driver-examples/AsyncDocumentationSamples.java)

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

      (Code example not available offline: /driver-examples/DocumentationExamples.cs)

  - id: go
    content: |
      (Code example not available offline: /driver-examples/go_examples.go)

## Project Specific Array Elements in the Returned Array

tabs:
  - id: shell
    content: |
      For fields that contain arrays, MongoDB provides the following
      projection operators for manipulating arrays: `$elemMatch`,
      `$slice`, and `$`.

      The following example uses the `$slice` projection operator
      to return the last element in the `instock` array:

      tabs:
        - id: shell
          content: |

            ```javascript
            db.inventory.find( { status: "A" }, { item: 1, status: 1, instock: { $slice: -1 } } )
            ```

        - id: compass
          content: |

            1. Copy the following expression into the Filter
               field:

               ```javascript
               { status: "A" }
               ```

            #. Click Options to open the additional query
               options.

            #. Copy the following expression into the Project
               field:

               ```javascript
               { item: 1, status: 1, instock: { $slice: -1 } }
               ```

            #. Click Find.

        - id: python
          content: |

            (Code example not available offline: /driver-examples/test_examples.py)

        - id: motor
          content: |

            (Code example not available offline: /driver-examples/test_examples_motor.py)

        - id: java-sync
          content: |
            To specify a projection document, chain the
            com.mongodb.client.FindIterable.projection_ method to the
            `find` method. The example uses the
            com.mongodb.client.model.Projections_ class to create the
            projection documents.

            (Code example not available offline: /driver-examples/DocumentationSamples.java)

        - id: java-async
          content: |

            (Code example not available offline: /driver-examples/AsyncDocumentationSamples.java)

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

            (Code example not available offline: /driver-examples/DocumentationExamples.cs)

        - id: go
          content: |
            (Code example not available offline: /driver-examples/go_examples.go)

      `$elemMatch`, `$slice`, and
      `$` are the *only* way to project specific elements
      to include in the returned array. For instance, you *cannot*
      project specific array elements using the array index; e.g.
      `{ "instock.0": 1 }` projection will *not* project the array
      with the first element.

  - id: compass
    content: |
      For fields that contain arrays, MongoDB provides the following
      projection operators for manipulating arrays: `$elemMatch`,
      `$slice`, and `$`.

      The following example uses the `$slice` projection operator
      to return the last element in the `instock` array:

      tabs:
        - id: shell
          content: |

            ```javascript
            db.inventory.find( { status: "A" }, { item: 1, status: 1, instock: { $slice: -1 } } )
            ```

        - id: compass
          content: |

            1. Copy the following expression into the Filter
               field:

               ```javascript
               { status: "A" }
               ```

            #. Click Options to open the additional query
               options.

            #. Copy the following expression into the Project
               field:

               ```javascript
               { item: 1, status: 1, instock: { $slice: -1 } }
               ```

            #. Click Find.

        - id: python
          content: |

            (Code example not available offline: /driver-examples/test_examples.py)

        - id: motor
          content: |

            (Code example not available offline: /driver-examples/test_examples_motor.py)

        - id: java-sync
          content: |
            To specify a projection document, chain the
            com.mongodb.client.FindIterable.projection_ method to the
            `find` method. The example uses the
            com.mongodb.client.model.Projections_ class to create the
            projection documents.

            (Code example not available offline: /driver-examples/DocumentationSamples.java)

        - id: java-async
          content: |

            (Code example not available offline: /driver-examples/AsyncDocumentationSamples.java)

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

            (Code example not available offline: /driver-examples/DocumentationExamples.cs)

        - id: go
          content: |
            (Code example not available offline: /driver-examples/go_examples.go)

  - id: python
    content: |
      For fields that contain arrays, MongoDB provides the following
      projection operators for manipulating arrays: `$elemMatch`,
      `$slice`, and `$`.

      The following example uses the `$slice` projection operator
      to return the last element in the `instock` array:

      tabs:
        - id: shell
          content: |

            ```javascript
            db.inventory.find( { status: "A" }, { item: 1, status: 1, instock: { $slice: -1 } } )
            ```

        - id: compass
          content: |

            1. Copy the following expression into the Filter
               field:

               ```javascript
               { status: "A" }
               ```

            #. Click Options to open the additional query
               options.

            #. Copy the following expression into the Project
               field:

               ```javascript
               { item: 1, status: 1, instock: { $slice: -1 } }
               ```

            #. Click Find.

        - id: python
          content: |

            (Code example not available offline: /driver-examples/test_examples.py)

        - id: motor
          content: |

            (Code example not available offline: /driver-examples/test_examples_motor.py)

        - id: java-sync
          content: |
            To specify a projection document, chain the
            com.mongodb.client.FindIterable.projection_ method to the
            `find` method. The example uses the
            com.mongodb.client.model.Projections_ class to create the
            projection documents.

            (Code example not available offline: /driver-examples/DocumentationSamples.java)

        - id: java-async
          content: |

            (Code example not available offline: /driver-examples/AsyncDocumentationSamples.java)

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

            (Code example not available offline: /driver-examples/DocumentationExamples.cs)

        - id: go
          content: |
            (Code example not available offline: /driver-examples/go_examples.go)

      `$elemMatch`, `$slice`, and
      `$` are the *only* way to project specific elements
      to include in the returned array. For instance, you *cannot*
      project specific array elements using the array index; e.g.
      `{ "instock.0": 1 }` projection will *not* project the array
      with the first element.

  - id: java-sync
    content: |
      For fields that contain arrays, MongoDB provides the following
      projection operators for manipulating arrays: `$elemMatch`,
      `$slice`, and `$`.

      The following example uses the `$slice` projection operator
      to return the last element in the `instock` array:

      tabs:
        - id: shell
          content: |

            ```javascript
            db.inventory.find( { status: "A" }, { item: 1, status: 1, instock: { $slice: -1 } } )
            ```

        - id: compass
          content: |

            1. Copy the following expression into the Filter
               field:

               ```javascript
               { status: "A" }
               ```

            #. Click Options to open the additional query
               options.

            #. Copy the following expression into the Project
               field:

               ```javascript
               { item: 1, status: 1, instock: { $slice: -1 } }
               ```

            #. Click Find.

        - id: python
          content: |

            (Code example not available offline: /driver-examples/test_examples.py)

        - id: motor
          content: |

            (Code example not available offline: /driver-examples/test_examples_motor.py)

        - id: java-sync
          content: |
            To specify a projection document, chain the
            com.mongodb.client.FindIterable.projection_ method to the
            `find` method. The example uses the
            com.mongodb.client.model.Projections_ class to create the
            projection documents.

            (Code example not available offline: /driver-examples/DocumentationSamples.java)

        - id: java-async
          content: |

            (Code example not available offline: /driver-examples/AsyncDocumentationSamples.java)

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

            (Code example not available offline: /driver-examples/DocumentationExamples.cs)

        - id: go
          content: |
            (Code example not available offline: /driver-examples/go_examples.go)

      `$elemMatch`, `$slice`, and
      `$` are the *only* way to project specific elements
      to include in the returned array. For instance, you *cannot*
      project specific array elements using the array index; e.g.
      `include("instock.0")` projection will *not* project the array
      with the first element.

  - id: java-async
    content: |
      For fields that contain arrays, MongoDB provides the following
      projection operators for manipulating arrays: `$elemMatch`,
      `$slice`, and `$`.

      The following example uses the `$slice` projection operator
      to return the last element in the `instock` array:

      tabs:
        - id: shell
          content: |

            ```javascript
            db.inventory.find( { status: "A" }, { item: 1, status: 1, instock: { $slice: -1 } } )
            ```

        - id: compass
          content: |

            1. Copy the following expression into the Filter
               field:

               ```javascript
               { status: "A" }
               ```

            #. Click Options to open the additional query
               options.

            #. Copy the following expression into the Project
               field:

               ```javascript
               { item: 1, status: 1, instock: { $slice: -1 } }
               ```

            #. Click Find.

        - id: python
          content: |

            (Code example not available offline: /driver-examples/test_examples.py)

        - id: motor
          content: |

            (Code example not available offline: /driver-examples/test_examples_motor.py)

        - id: java-sync
          content: |
            To specify a projection document, chain the
            com.mongodb.client.FindIterable.projection_ method to the
            `find` method. The example uses the
            com.mongodb.client.model.Projections_ class to create the
            projection documents.

            (Code example not available offline: /driver-examples/DocumentationSamples.java)

        - id: java-async
          content: |

            (Code example not available offline: /driver-examples/AsyncDocumentationSamples.java)

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

            (Code example not available offline: /driver-examples/DocumentationExamples.cs)

        - id: go
          content: |
            (Code example not available offline: /driver-examples/go_examples.go)

      `$elemMatch`, `$slice`, and
      `$` are the *only* way to project specific elements
      to include in the returned array. For instance, you *cannot*
      project specific array elements using the array index; e.g.
      `include("instock.0")` projection will *not* project the array
      with the first element.

  - id: nodejs
    content: |
      For fields that contain arrays, MongoDB provides the following
      projection operators for manipulating arrays: `$elemMatch`,
      `$slice`, and `$`.

      The following example uses the `$slice` projection operator
      to return the last element in the `instock` array:

      tabs:
        - id: shell
          content: |

            ```javascript
            db.inventory.find( { status: "A" }, { item: 1, status: 1, instock: { $slice: -1 } } )
            ```

        - id: compass
          content: |

            1. Copy the following expression into the Filter
               field:

               ```javascript
               { status: "A" }
               ```

            #. Click Options to open the additional query
               options.

            #. Copy the following expression into the Project
               field:

               ```javascript
               { item: 1, status: 1, instock: { $slice: -1 } }
               ```

            #. Click Find.

        - id: python
          content: |

            (Code example not available offline: /driver-examples/test_examples.py)

        - id: motor
          content: |

            (Code example not available offline: /driver-examples/test_examples_motor.py)

        - id: java-sync
          content: |
            To specify a projection document, chain the
            com.mongodb.client.FindIterable.projection_ method to the
            `find` method. The example uses the
            com.mongodb.client.model.Projections_ class to create the
            projection documents.

            (Code example not available offline: /driver-examples/DocumentationSamples.java)

        - id: java-async
          content: |

            (Code example not available offline: /driver-examples/AsyncDocumentationSamples.java)

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

            (Code example not available offline: /driver-examples/DocumentationExamples.cs)

        - id: go
          content: |
            (Code example not available offline: /driver-examples/go_examples.go)

      `$elemMatch`, `$slice`, and
      `$` are the *only* way to project specific elements
      to include in the returned array. For instance, you *cannot*
      project specific array elements using the array index; e.g.
      `{ "instock.0": 1 }` projection will *not* project the array
      with the first element.

  - id: php
    content: |
      For fields that contain arrays, MongoDB provides the following
      projection operators for manipulating arrays: `$elemMatch`,
      `$slice`, and `$`.

      The following example uses the `$slice` projection operator
      to return the last element in the `instock` array:

      tabs:
        - id: shell
          content: |

            ```javascript
            db.inventory.find( { status: "A" }, { item: 1, status: 1, instock: { $slice: -1 } } )
            ```

        - id: compass
          content: |

            1. Copy the following expression into the Filter
               field:

               ```javascript
               { status: "A" }
               ```

            #. Click Options to open the additional query
               options.

            #. Copy the following expression into the Project
               field:

               ```javascript
               { item: 1, status: 1, instock: { $slice: -1 } }
               ```

            #. Click Find.

        - id: python
          content: |

            (Code example not available offline: /driver-examples/test_examples.py)

        - id: motor
          content: |

            (Code example not available offline: /driver-examples/test_examples_motor.py)

        - id: java-sync
          content: |
            To specify a projection document, chain the
            com.mongodb.client.FindIterable.projection_ method to the
            `find` method. The example uses the
            com.mongodb.client.model.Projections_ class to create the
            projection documents.

            (Code example not available offline: /driver-examples/DocumentationSamples.java)

        - id: java-async
          content: |

            (Code example not available offline: /driver-examples/AsyncDocumentationSamples.java)

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

            (Code example not available offline: /driver-examples/DocumentationExamples.cs)

        - id: go
          content: |
            (Code example not available offline: /driver-examples/go_examples.go)

      `$elemMatch`, `$slice`, and
      `$` are the *only* way to project specific elements
      to include in the returned array. For instance, you *cannot*
      project specific array elements using the array index; e.g.
      `[ "instock.0" => 1 ]` projection will *not* project the array
      with the first element.

  - id: ruby
    content: |
      For fields that contain arrays, MongoDB provides the following
      projection operators for manipulating arrays: `$elemMatch`,
      `$slice`, and `$`.

      The following example uses the `$slice` projection operator
      to return the last element in the `instock` array:

      tabs:
        - id: shell
          content: |

            ```javascript
            db.inventory.find( { status: "A" }, { item: 1, status: 1, instock: { $slice: -1 } } )
            ```

        - id: compass
          content: |

            1. Copy the following expression into the Filter
               field:

               ```javascript
               { status: "A" }
               ```

            #. Click Options to open the additional query
               options.

            #. Copy the following expression into the Project
               field:

               ```javascript
               { item: 1, status: 1, instock: { $slice: -1 } }
               ```

            #. Click Find.

        - id: python
          content: |

            (Code example not available offline: /driver-examples/test_examples.py)

        - id: motor
          content: |

            (Code example not available offline: /driver-examples/test_examples_motor.py)

        - id: java-sync
          content: |
            To specify a projection document, chain the
            com.mongodb.client.FindIterable.projection_ method to the
            `find` method. The example uses the
            com.mongodb.client.model.Projections_ class to create the
            projection documents.

            (Code example not available offline: /driver-examples/DocumentationSamples.java)

        - id: java-async
          content: |

            (Code example not available offline: /driver-examples/AsyncDocumentationSamples.java)

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

            (Code example not available offline: /driver-examples/DocumentationExamples.cs)

        - id: go
          content: |
            (Code example not available offline: /driver-examples/go_examples.go)

      `$elemMatch`, `$slice`, and
      `$` are the *only* way to project specific elements
      to include in the returned array. For instance, you *cannot*
      project specific array elements using the array index; e.g.
      `{ "instock.0" => 1 }` projection will *not* project the array
      with the first element.

  - id: scala
    content: |
      For fields that contain arrays, MongoDB provides the following
      projection operators for manipulating arrays: `$elemMatch`,
      `$slice`, and `$`.

      The following example uses the `$slice` projection operator
      to return the last element in the `instock` array:

      tabs:
        - id: shell
          content: |

            ```javascript
            db.inventory.find( { status: "A" }, { item: 1, status: 1, instock: { $slice: -1 } } )
            ```

        - id: compass
          content: |

            1. Copy the following expression into the Filter
               field:

               ```javascript
               { status: "A" }
               ```

            #. Click Options to open the additional query
               options.

            #. Copy the following expression into the Project
               field:

               ```javascript
               { item: 1, status: 1, instock: { $slice: -1 } }
               ```

            #. Click Find.

        - id: python
          content: |

            (Code example not available offline: /driver-examples/test_examples.py)

        - id: motor
          content: |

            (Code example not available offline: /driver-examples/test_examples_motor.py)

        - id: java-sync
          content: |
            To specify a projection document, chain the
            com.mongodb.client.FindIterable.projection_ method to the
            `find` method. The example uses the
            com.mongodb.client.model.Projections_ class to create the
            projection documents.

            (Code example not available offline: /driver-examples/DocumentationSamples.java)

        - id: java-async
          content: |

            (Code example not available offline: /driver-examples/AsyncDocumentationSamples.java)

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

            (Code example not available offline: /driver-examples/DocumentationExamples.cs)

        - id: go
          content: |
            (Code example not available offline: /driver-examples/go_examples.go)

      `$elemMatch`, `$slice`, and
      `$` are the *only* way to project specific elements
      to include in the returned array. For instance, you *cannot*
      project specific array elements using the array index; e.g.
      `include("instock.0")` projection will *not* project the array
      with the first element.

  - id: csharp
    content: |
      For fields that contain arrays, MongoDB provides the following
      projection operators for manipulating arrays: `$elemMatch`,
      `$slice`, and `$`.

      The following example uses the `$slice` projection operator
      to return the last element in the `instock` array:

      tabs:
        - id: shell
          content: |

            ```javascript
            db.inventory.find( { status: "A" }, { item: 1, status: 1, instock: { $slice: -1 } } )
            ```

        - id: compass
          content: |

            1. Copy the following expression into the Filter
               field:

               ```javascript
               { status: "A" }
               ```

            #. Click Options to open the additional query
               options.

            #. Copy the following expression into the Project
               field:

               ```javascript
               { item: 1, status: 1, instock: { $slice: -1 } }
               ```

            #. Click Find.

        - id: python
          content: |

            (Code example not available offline: /driver-examples/test_examples.py)

        - id: motor
          content: |

            (Code example not available offline: /driver-examples/test_examples_motor.py)

        - id: java-sync
          content: |
            To specify a projection document, chain the
            com.mongodb.client.FindIterable.projection_ method to the
            `find` method. The example uses the
            com.mongodb.client.model.Projections_ class to create the
            projection documents.

            (Code example not available offline: /driver-examples/DocumentationSamples.java)

        - id: java-async
          content: |

            (Code example not available offline: /driver-examples/AsyncDocumentationSamples.java)

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

            (Code example not available offline: /driver-examples/DocumentationExamples.cs)

        - id: go
          content: |
            (Code example not available offline: /driver-examples/go_examples.go)

      `$elemMatch`, `$slice`, and
      `$` are the *only* way to project specific elements
      to include in the returned array.

      For example, the following operation will not project the array
      with the first element:

      ```c#
      Builders<BsonDocument>.Projection.Include("instock.0")
      ```

  - id: go
    content: |
      For fields that contain arrays, MongoDB provides the following
      projection operators for manipulating arrays: `$elemMatch`,
      `$slice`, and `$`.

      The following example uses the `$slice` projection operator
      to return the last element in the `instock` array:

      tabs:
        - id: shell
          content: |

            ```javascript
            db.inventory.find( { status: "A" }, { item: 1, status: 1, instock: { $slice: -1 } } )
            ```

        - id: compass
          content: |

            1. Copy the following expression into the Filter
               field:

               ```javascript
               { status: "A" }
               ```

            #. Click Options to open the additional query
               options.

            #. Copy the following expression into the Project
               field:

               ```javascript
               { item: 1, status: 1, instock: { $slice: -1 } }
               ```

            #. Click Find.

        - id: python
          content: |

            (Code example not available offline: /driver-examples/test_examples.py)

        - id: motor
          content: |

            (Code example not available offline: /driver-examples/test_examples_motor.py)

        - id: java-sync
          content: |
            To specify a projection document, chain the
            com.mongodb.client.FindIterable.projection_ method to the
            `find` method. The example uses the
            com.mongodb.client.model.Projections_ class to create the
            projection documents.

            (Code example not available offline: /driver-examples/DocumentationSamples.java)

        - id: java-async
          content: |

            (Code example not available offline: /driver-examples/AsyncDocumentationSamples.java)

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

            (Code example not available offline: /driver-examples/DocumentationExamples.cs)

        - id: go
          content: |
            (Code example not available offline: /driver-examples/go_examples.go)

      `$elemMatch`, `$slice`, and
      `$` are the *only* way to project specific elements
      to include in the returned array. For instance, you *cannot*
      project specific array elements using the array index; e.g.
      `include("instock.0")` projection will *not* project the array
      with the first element.

## Project Fields with Aggregation Expressions

You can specify aggregation expressions
in a query projection. Aggregation expressions let you project new
fields and modify the values of existing fields.

For example, the following operation uses aggregation expressions to
override the value of the `status` field, and project new fields
`area` and `reportNumber`.

**Note:**

The following example uses MongoDB Shell syntax. For driver examples
of projection with aggregation, see your `driver
documentation`.

```javascript
db.inventory.find(
   { },
   {
      _id: 0,
      item: 1,
      status: {
         $switch: {
            branches: [
               {
                  case: { $eq: [ "$status", "A" ] },
                  then: "Available"
               },
               {
                  case: { $eq: [ "$status", "D" ] },
                  then: "Discontinued"
               },
            ],
            default: "No status found"
         }
      },
      area: {
         $concat: [
            { $toString: { $multiply: [ "$size.h", "$size.w" ] } },
            " ",
            "$size.uom"
         ]
      },
      reportNumber: { $literal: 1 }
   }
)
```

Output:

```javascript
[
   {
      item: 'journal',
      status: 'Available',
      area: '294 cm',
      reportNumber: 1
   },
   {
      item: 'planner',
      status: 'Discontinued',
      area: '685.5 cm',
      reportNumber: 1
   },
   {
      item: 'notebook',
      status: 'Available',
      area: '93.5 in',
      reportNumber: 1
   },
   {
      item: 'paper',
      status: 'Discontinued',
      area: '93.5 in',
      reportNumber: 1
   },
   {
      item: 'postcard',
      status: 'Available',
      area: '152.5 cm',
      reportNumber: 1
   }
]
```

## Additional Considerations

MongoDB enforces additional restrictions with regards to projections. 
See `Projection Restrictions` for details.

**See also:**

- find-projection

- /tutorial/query-documents
