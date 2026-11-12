<!-- Part 1 of 4 of tutorial/project-fields-from-query-results.md (split because the page is big). -->

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

  - id: c
    content: |
      If you do not specify a projection document, the
      `db.collection.find()` method returns all fields in the
      matching documents.

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

  - id: kotlin-coroutine
    content: |
      If you do not specify a projection document, the
      `db.collection.find()` method returns all fields in the
      matching documents.

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

  - id: go
    content: |
      If you do not specify a projection filter, the
      `Find()` method returns all
      fields in the matching documents.

  - id: motor
    content: |
      If you do not specify a projection filter, the
      `find` method returns
      all fields in the matching documents.

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
      var filter = Builders<BsonDocument>.Filter.Eq("status", "A");
      var result = collection.Find(filter).ToList();
      ```

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
      To specify a projection document, chain the
      com.mongodb.client.FindIterable.projection_ method to the
      `find` method. The example uses the
      com.mongodb.client.model.Projections_ class to create the
      projection documents.

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
      var filter = Builders<BsonDocument>.Filter.Eq("status", "A");
      var projection = Builders<BsonDocument>.Projection.Include("item").Include("status");
      var result = collection.Find<BsonDocument>(filter).Project(projection).ToList();
      ```

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
      To specify a projection document, chain the
      com.mongodb.client.FindIterable.projection_ method to the
      `find` method. The example uses the
      com.mongodb.client.model.Projections_ class to create the
      projection documents.

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
      var filter = Builders<BsonDocument>.Filter.Eq("status", "A");
      var projection = Builders<BsonDocument>.Projection.Include("item").Include("status").Exclude("_id");
      var result = collection.Find<BsonDocument>(filter).Project(projection).ToList();
      ```

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
      To specify a projection document, chain the
      com.mongodb.client.FindIterable.projection_ method to the
      `find` method. The example uses the
      com.mongodb.client.model.Projections_ class to create the
      projection documents.

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
      var filter = Builders<BsonDocument>.Filter.Eq("status", "A");
      var projection = Builders<BsonDocument>.Projection.Exclude("status").Exclude("instock");
      var result = collection.Find<BsonDocument>(filter).Project(projection).ToList();
      ```

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
      To specify a projection document, chain the
      com.mongodb.client.FindIterable.projection_ method to the
      `find` method. The example uses the
      com.mongodb.client.model.Projections_ class to create the
      projection documents.

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
      var filter = Builders<BsonDocument>.Filter.Eq("status", "A");
      var projection = Builders<BsonDocument>.Projection.Include("item").Include("status").Include("size.uom");
      var result = collection.Find<BsonDocument>(filter).Project(projection).ToList();
      ```

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
      To specify a projection document, chain the
      com.mongodb.client.FindIterable.projection_ method to the
      `find` method. The example uses the
      com.mongodb.client.model.Projections_ class to create the
      projection documents.

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
      var filter = Builders<BsonDocument>.Filter.Eq("status", "A");
      var projection = Builders<BsonDocument>.Projection.Exclude("size.uom");
      var result = collection.Find<BsonDocument>(filter).Project(projection).ToList();
      ```

  - id: go
    content: |
      (Code example not available offline: /driver-examples/go_examples.go)

You can also specify embedded fields using the nested form. For example, 
`{ size: { uom: 0 } }`.
