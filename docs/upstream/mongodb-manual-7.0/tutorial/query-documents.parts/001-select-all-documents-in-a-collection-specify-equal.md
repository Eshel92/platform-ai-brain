<!-- Part 1 of 5 of tutorial/query-documents.md (split because the page is big). -->

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
