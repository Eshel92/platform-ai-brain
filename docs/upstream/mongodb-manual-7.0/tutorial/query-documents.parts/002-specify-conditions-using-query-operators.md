<!-- Part 2 of 5 of tutorial/query-documents.md (split because the page is big). -->

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

  - id: c
    content: |
      A query filter document can
      use the query operators to specify
      conditions in the following form:

      ```c
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

  - id: kotlin-coroutine
    content: |

      In addition to the equality condition, MongoDB provides
      various query operators to specify
      filter conditions. Use the [com.mongodb.client.model.Filters](https://mongodb.github.io/mongo-java-driver/{+java-driver-version+}/apidocs/driver-core/com/mongodb/client/model/Filters.html) helper methods to
      facilitate the creation of filter documents. For example:

      ```kotlin
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

  - id: go
    content: |
      In addition to the equality filter, MongoDB provides
      various query operators to specify
      filter conditions. Use the bson package to create query 
      operators for filter documents. For example:

      ```go
      filter := bson.D{
          {"$and", bson.A{
              bson.D{{"field1", bson.D{{"$eq", value1}}}},
              bson.D{{"field2", bson.D{{"$lt", value2}}}},
          }},
      }
      ```

tabs:
  - id: shell
    content: |
      The following example retrieves all documents from the
      `sample_mflix.movies` collection where `rated`
      equals either `"G"` or `"PG-13"`:

  - id: compass
    content: |
      The following example retrieves all documents from the
      `inventory` collection where `status` equals
      either `"A"` or `"D"`:

  - id: c
    content: |
      The following example retrieves all documents from the
      `inventory` collection where `status` equals
      either `"A"` or `"D"`:

  - id: python
    content: |
      The following example retrieves all documents from the
      `inventory` collection where `status` equals
      either `"A"` or `"D"`:

  - id: motor
    content: |
      The following example retrieves all documents from the
      `inventory` collection where `status` equals
      either `"A"` or `"D"`:

  - id: java-sync
    content: |
      The following example retrieves all documents from the
      `inventory` collection where `status` equals
      either `"A"` or `"D"`:

  - id: java-async
    content: |
      The following example retrieves all documents from the
      `inventory` collection where `status` equals
      either `"A"` or `"D"`:

  - id: kotlin-coroutine
    content: |
      The following example retrieves all documents from the
      `inventory` collection where `status` equals
      either `"A"` or `"D"`:

  - id: nodejs
    content: |
      The following example retrieves all documents from the
      `inventory` collection where `status` equals
      either `"A"` or `"D"`:

  - id: php
    content: |
      The following example retrieves all documents from the
      `inventory` collection where `status` equals
      either `"A"` or `"D"`:

  - id: ruby
    content: |
      The following example retrieves all documents from the
      `inventory` collection where `status` equals
      either `"A"` or `"D"`:

  - id: scala
    content: |
      The following example retrieves all documents from the
      `inventory` collection where `status` equals
      either `"A"` or `"D"`:

  - id: csharp
    content: |
      The following example retrieves all documents from the
      `inventory` collection where `status` equals
      either `"A"` or `"D"`:

  - id: go
    content: |
      The following example retrieves all documents from the
      `inventory` collection where `status` equals
      either `"A"` or `"D"`:

tabs:
  - id: shell
    content: |

      ```javascript
      db.movies.find( { rated: { $in: [ "G", "PG-13" ] } } )
      ```

  - id: compass
    content: |
      Copy the following filter into the Compass query bar and click
      Find:

      ```javascript
      { status: { $in: [ "A", "D" ] } }
      ```

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
      var filter = Builders<BsonDocument>.Filter.In("status", new[] { "A", "D" });
      var result = collection.Find(filter).ToList();
      ```

  - id: go
    content: |
      (Code example not available offline: /driver-examples/go_examples.go)

**Note:**

Although you can use the `$or` operator for this query,
use the `$in` operator instead of `$or`
when performing equality checks on the same field.

tabs:
  - id: shell
    content: |
      The operation uses a query predicate of
      `{ rated: { $in: [ "G", "PG-13" ] } }`, which
      corresponds to the following SQL statement:

      ```sql
      SELECT * FROM movies WHERE rated in ("G", "PG-13")
      ```

  - id: compass
    content: |
      The operation uses a query predicate of
      `{ status: { $in: [ "A", "D" ] } }`, which
      corresponds to the following SQL statement:

      ```sql
      SELECT * FROM inventory WHERE status in ("A", "D")
      ```

  - id: c
    content: |
      The operation uses a query predicate of
      `{ status: { $in: [ "A", "D" ] } }`, which
      corresponds to the following SQL statement:

      ```sql
      SELECT * FROM inventory WHERE status in ("A", "D")
      ```

  - id: python
    content: |
      The operation uses a query predicate of
      `{ status: { $in: [ "A", "D" ] } }`, which
      corresponds to the following SQL statement:

      ```sql
      SELECT * FROM inventory WHERE status in ("A", "D")
      ```

  - id: motor
    content: |
      The operation uses a query predicate of
      `{ status: { $in: [ "A", "D" ] } }`, which
      corresponds to the following SQL statement:

      ```sql
      SELECT * FROM inventory WHERE status in ("A", "D")
      ```

  - id: java-sync
    content: |
      The operation uses a query predicate of
      `{ status: { $in: [ "A", "D" ] } }`, which
      corresponds to the following SQL statement:

      ```sql
      SELECT * FROM inventory WHERE status in ("A", "D")
      ```

  - id: java-async
    content: |
      The operation uses a query predicate of
      `{ status: { $in: [ "A", "D" ] } }`, which
      corresponds to the following SQL statement:

      ```sql
      SELECT * FROM inventory WHERE status in ("A", "D")
      ```

  - id: kotlin-coroutine
    content: |
      The operation uses a query predicate of
      `{ status: { $in: [ "A", "D" ] } }`, which
      corresponds to the following SQL statement:

      ```sql
      SELECT * FROM inventory WHERE status in ("A", "D")
      ```

  - id: nodejs
    content: |
      The operation uses a query predicate of
      `{ status: { $in: [ "A", "D" ] } }`, which
      corresponds to the following SQL statement:

      ```sql
      SELECT * FROM inventory WHERE status in ("A", "D")
      ```

  - id: php
    content: |
      The operation uses a query predicate of
      `{ status: { $in: [ "A", "D" ] } }`, which
      corresponds to the following SQL statement:

      ```sql
      SELECT * FROM inventory WHERE status in ("A", "D")
      ```

  - id: ruby
    content: |
      The operation uses a query predicate of
      `{ status: { $in: [ "A", "D" ] } }`, which
      corresponds to the following SQL statement:

      ```sql
      SELECT * FROM inventory WHERE status in ("A", "D")
      ```

  - id: scala
    content: |
      The operation uses a query predicate of
      `{ status: { $in: [ "A", "D" ] } }`, which
      corresponds to the following SQL statement:

      ```sql
      SELECT * FROM inventory WHERE status in ("A", "D")
      ```

  - id: csharp
    content: |
      The operation uses a query predicate of
      `{ status: { $in: [ "A", "D" ] } }`, which
      corresponds to the following SQL statement:

      ```sql
      SELECT * FROM inventory WHERE status in ("A", "D")
      ```

  - id: go
    content: |
      The operation uses a query predicate of
      `{ status: { $in: [ "A", "D" ] } }`, which
      corresponds to the following SQL statement:

      ```sql
      SELECT * FROM inventory WHERE status in ("A", "D")
      ```

For the complete list of MongoDB query operators, see
query-predicates-ref.
