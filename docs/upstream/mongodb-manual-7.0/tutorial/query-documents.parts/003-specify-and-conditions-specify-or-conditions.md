<!-- Part 3 of 5 of tutorial/query-documents.md (split because the page is big). -->

## Specify `AND` Conditions

A compound query can specify conditions for more than one field in the
collection's documents. Implicitly, a logical `AND` conjunction
connects the clauses of a compound query so that the query selects the
documents in the collection that match all the conditions.

tabs:
  - id: shell
    content: |
      The following example retrieves all documents in the
      `sample_mflix.movies` collection where `rated`
      equals `"G"` **and** `runtime` is less than
      (`$lt`) `90`:

  - id: compass
    content: |
      The following example retrieves all documents in the
      `inventory` collection where `status` equals
      `"A"` **and** `qty` is less than
      (`$lt`) `30`:

  - id: c
    content: |
      The following example retrieves all documents in the
      `inventory` collection where `status` equals
      `"A"` **and** `qty` is less than
      (`$lt`) `30`:

  - id: python
    content: |
      The following example retrieves all documents in the
      `inventory` collection where `status` equals
      `"A"` **and** `qty` is less than
      (`$lt`) `30`:

  - id: motor
    content: |
      The following example retrieves all documents in the
      `inventory` collection where `status` equals
      `"A"` **and** `qty` is less than
      (`$lt`) `30`:

  - id: java-sync
    content: |
      The following example retrieves all documents in the
      `inventory` collection where `status` equals
      `"A"` **and** `qty` is less than
      (`$lt`) `30`:

  - id: java-async
    content: |
      The following example retrieves all documents in the
      `inventory` collection where `status` equals
      `"A"` **and** `qty` is less than
      (`$lt`) `30`:

  - id: kotlin-coroutine
    content: |
      The following example retrieves all documents in the
      `inventory` collection where `status` equals
      `"A"` **and** `qty` is less than
      (`$lt`) `30`:

  - id: nodejs
    content: |
      The following example retrieves all documents in the
      `inventory` collection where `status` equals
      `"A"` **and** `qty` is less than
      (`$lt`) `30`:

  - id: php
    content: |
      The following example retrieves all documents in the
      `inventory` collection where `status` equals
      `"A"` **and** `qty` is less than
      (`$lt`) `30`:

  - id: ruby
    content: |
      The following example retrieves all documents in the
      `inventory` collection where `status` equals
      `"A"` **and** `qty` is less than
      (`$lt`) `30`:

  - id: scala
    content: |
      The following example retrieves all documents in the
      `inventory` collection where `status` equals
      `"A"` **and** `qty` is less than
      (`$lt`) `30`:

  - id: csharp
    content: |
      The following example retrieves all documents in the
      `inventory` collection where `status` equals
      `"A"` **and** `qty` is less than
      (`$lt`) `30`:

  - id: go
    content: |
      The following example retrieves all documents in the
      `inventory` collection where `status` equals
      `"A"` **and** `qty` is less than
      (`$lt`) `30`:

tabs:
  - id: shell
    content: |

      ```javascript
      db.movies.find( { rated: "G", runtime: { $lt: 90 } } )
      ```

  - id: compass
    content: |
      Copy the following filter into the Compass query bar and click
      Find:

      ```javascript
      { status: "A", qty: { $lt: 30 } }
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
      var builder = Builders<BsonDocument>.Filter;
      var filter = builder.And(builder.Eq("status", "A"), builder.Lt("qty", 30));
      var result = collection.Find(filter).ToList();
      ```

  - id: go
    content: |
      (Code example not available offline: /driver-examples/go_examples.go)

tabs:
  - id: shell
    content: |
      The operation uses a query predicate of
      `{ rated: "G", runtime: { $lt: 90 } }`, which
      corresponds to the following SQL statement:

      ```sql
      SELECT * FROM movies WHERE rated = "G" AND runtime < 90
      ```

  - id: compass
    content: |
      The operation uses a query predicate of
      `{ status: "A", qty: { $lt: 30 } }`, which
      corresponds to the following SQL statement:

      ```sql
      SELECT * FROM inventory WHERE status = "A" AND qty < 30
      ```

  - id: c
    content: |
      The operation uses a query predicate of
      `{ status: "A", qty: { $lt: 30 } }`, which
      corresponds to the following SQL statement:

      ```sql
      SELECT * FROM inventory WHERE status = "A" AND qty < 30
      ```

  - id: python
    content: |
      The operation uses a query predicate of
      `{ status: "A", qty: { $lt: 30 } }`, which
      corresponds to the following SQL statement:

      ```sql
      SELECT * FROM inventory WHERE status = "A" AND qty < 30
      ```

  - id: motor
    content: |
      The operation uses a query predicate of
      `{ status: "A", qty: { $lt: 30 } }`, which
      corresponds to the following SQL statement:

      ```sql
      SELECT * FROM inventory WHERE status = "A" AND qty < 30
      ```

  - id: java-sync
    content: |
      The operation uses a query predicate of
      `{ status: "A", qty: { $lt: 30 } }`, which
      corresponds to the following SQL statement:

      ```sql
      SELECT * FROM inventory WHERE status = "A" AND qty < 30
      ```

  - id: java-async
    content: |
      The operation uses a query predicate of
      `{ status: "A", qty: { $lt: 30 } }`, which
      corresponds to the following SQL statement:

      ```sql
      SELECT * FROM inventory WHERE status = "A" AND qty < 30
      ```

  - id: kotlin-coroutine
    content: |
      The operation uses a query predicate of
      `{ status: "A", qty: { $lt: 30 } }`, which
      corresponds to the following SQL statement:

      ```sql
      SELECT * FROM inventory WHERE status = "A" AND qty < 30
      ```

  - id: nodejs
    content: |
      The operation uses a query predicate of
      `{ status: "A", qty: { $lt: 30 } }`, which
      corresponds to the following SQL statement:

      ```sql
      SELECT * FROM inventory WHERE status = "A" AND qty < 30
      ```

  - id: php
    content: |
      The operation uses a query predicate of
      `{ status: "A", qty: { $lt: 30 } }`, which
      corresponds to the following SQL statement:

      ```sql
      SELECT * FROM inventory WHERE status = "A" AND qty < 30
      ```

  - id: ruby
    content: |
      The operation uses a query predicate of
      `{ status: "A", qty: { $lt: 30 } }`, which
      corresponds to the following SQL statement:

      ```sql
      SELECT * FROM inventory WHERE status = "A" AND qty < 30
      ```

  - id: scala
    content: |
      The operation uses a query predicate of
      `{ status: "A", qty: { $lt: 30 } }`, which
      corresponds to the following SQL statement:

      ```sql
      SELECT * FROM inventory WHERE status = "A" AND qty < 30
      ```

  - id: csharp
    content: |
      The operation uses a query predicate of
      `{ status: "A", qty: { $lt: 30 } }`, which
      corresponds to the following SQL statement:

      ```sql
      SELECT * FROM inventory WHERE status = "A" AND qty < 30
      ```

  - id: go
    content: |
      The operation uses a query predicate of
      `{ status: "A", qty: { $lt: 30 } }`, which
      corresponds to the following SQL statement:

      ```sql
      SELECT * FROM inventory WHERE status = "A" AND qty < 30
      ```

See comparison operators for other
MongoDB comparison operators.


## Specify `OR` Conditions

Use the `$or` operator to specify a compound query
that joins each clause with a logical `OR` conjunction. The
query selects documents that match at least one
condition.

tabs:
  - id: shell
    content: |
      The following example retrieves all documents in the
      `sample_mflix.movies` collection where `rated`
      equals `"G"` **or** `runtime` is less than
      (`$lt`) `90`:

  - id: compass
    content: |
      The following example retrieves all documents in the
      collection where `status` equals `"A"` **or**
      `qty` is less than (`$lt`) `30`:

  - id: c
    content: |
      The following example retrieves all documents in the
      collection where `status` equals `"A"` **or**
      `qty` is less than (`$lt`) `30`:

  - id: python
    content: |
      The following example retrieves all documents in the
      collection where `status` equals `"A"` **or**
      `qty` is less than (`$lt`) `30`:

  - id: motor
    content: |
      The following example retrieves all documents in the
      collection where `status` equals `"A"` **or**
      `qty` is less than (`$lt`) `30`:

  - id: java-sync
    content: |
      The following example retrieves all documents in the
      collection where `status` equals `"A"` **or**
      `qty` is less than (`$lt`) `30`:

  - id: java-async
    content: |
      The following example retrieves all documents in the
      collection where `status` equals `"A"` **or**
      `qty` is less than (`$lt`) `30`:

  - id: kotlin-coroutine
    content: |
      The following example retrieves all documents in the
      collection where `status` equals `"A"` **or**
      `qty` is less than (`$lt`) `30`:

  - id: nodejs
    content: |
      The following example retrieves all documents in the
      collection where `status` equals `"A"` **or**
      `qty` is less than (`$lt`) `30`:

  - id: php
    content: |
      The following example retrieves all documents in the
      collection where `status` equals `"A"` **or**
      `qty` is less than (`$lt`) `30`:

  - id: ruby
    content: |
      The following example retrieves all documents in the
      collection where `status` equals `"A"` **or**
      `qty` is less than (`$lt`) `30`:

  - id: scala
    content: |
      The following example retrieves all documents in the
      collection where `status` equals `"A"` **or**
      `qty` is less than (`$lt`) `30`:

  - id: csharp
    content: |
      The following example retrieves all documents in the
      collection where `status` equals `"A"` **or**
      `qty` is less than (`$lt`) `30`:

  - id: go
    content: |
      The following example retrieves all documents in the
      collection where `status` equals `"A"` **or**
      `qty` is less than (`$lt`) `30`:

tabs:
  - id: shell
    content: |

      ```javascript
      db.movies.find( { $or: [ { rated: "G" }, { runtime: { $lt: 90 } } ] } )
      ```

  - id: compass
    content: |
      Copy the following filter into the Compass query bar and click
      Find:

      ```javascript
      { $or: [ { status: "A" }, { qty: { $lt: 30 } } ] }
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
      var builder = Builders<BsonDocument>.Filter;
      var filter = builder.Or(builder.Eq("status", "A"), builder.Lt("qty", 30));
      var result = collection.Find(filter).ToList();
      ```

  - id: go
    content: |
      (Code example not available offline: /driver-examples/go_examples.go)

tabs:
  - id: shell
    content: |
      The operation uses a query predicate of
      `{ $or: [ { rated: 'G' }, { runtime: { $lt: 90 } } ] }`,
      which corresponds to the following SQL statement:

      ```sql
      SELECT * FROM movies WHERE rated = "G" OR runtime < 90
      ```

  - id: compass
    content: |
      The operation uses a query predicate of
      `{ $or: [ { status: 'A' }, { qty: { $lt: 30 } } ] }`,
      which corresponds to the following SQL statement:

      ```sql
      SELECT * FROM inventory WHERE status = "A" OR qty < 30
      ```

  - id: c
    content: |
      The operation uses a query predicate of
      `{ $or: [ { status: 'A' }, { qty: { $lt: 30 } } ] }`,
      which corresponds to the following SQL statement:

      ```sql
      SELECT * FROM inventory WHERE status = "A" OR qty < 30
      ```

  - id: python
    content: |
      The operation uses a query predicate of
      `{ $or: [ { status: 'A' }, { qty: { $lt: 30 } } ] }`,
      which corresponds to the following SQL statement:

      ```sql
      SELECT * FROM inventory WHERE status = "A" OR qty < 30
      ```

  - id: motor
    content: |
      The operation uses a query predicate of
      `{ $or: [ { status: 'A' }, { qty: { $lt: 30 } } ] }`,
      which corresponds to the following SQL statement:

      ```sql
      SELECT * FROM inventory WHERE status = "A" OR qty < 30
      ```

  - id: java-sync
    content: |
      The operation uses a query predicate of
      `{ $or: [ { status: 'A' }, { qty: { $lt: 30 } } ] }`,
      which corresponds to the following SQL statement:

      ```sql
      SELECT * FROM inventory WHERE status = "A" OR qty < 30
      ```

  - id: java-async
    content: |
      The operation uses a query predicate of
      `{ $or: [ { status: 'A' }, { qty: { $lt: 30 } } ] }`,
      which corresponds to the following SQL statement:

      ```sql
      SELECT * FROM inventory WHERE status = "A" OR qty < 30
      ```

  - id: kotlin-coroutine
    content: |
      The operation uses a query predicate of
      `{ $or: [ { status: 'A' }, { qty: { $lt: 30 } } ] }`,
      which corresponds to the following SQL statement:

      ```sql
      SELECT * FROM inventory WHERE status = "A" OR qty < 30
      ```

  - id: nodejs
    content: |
      The operation uses a query predicate of
      `{ $or: [ { status: 'A' }, { qty: { $lt: 30 } } ] }`,
      which corresponds to the following SQL statement:

      ```sql
      SELECT * FROM inventory WHERE status = "A" OR qty < 30
      ```

  - id: php
    content: |
      The operation uses a query predicate of
      `{ $or: [ { status: 'A' }, { qty: { $lt: 30 } } ] }`,
      which corresponds to the following SQL statement:

      ```sql
      SELECT * FROM inventory WHERE status = "A" OR qty < 30
      ```

  - id: ruby
    content: |
      The operation uses a query predicate of
      `{ $or: [ { status: 'A' }, { qty: { $lt: 30 } } ] }`,
      which corresponds to the following SQL statement:

      ```sql
      SELECT * FROM inventory WHERE status = "A" OR qty < 30
      ```

  - id: scala
    content: |
      The operation uses a query predicate of
      `{ $or: [ { status: 'A' }, { qty: { $lt: 30 } } ] }`,
      which corresponds to the following SQL statement:

      ```sql
      SELECT * FROM inventory WHERE status = "A" OR qty < 30
      ```

  - id: csharp
    content: |
      The operation uses a query predicate of
      `{ $or: [ { status: 'A' }, { qty: { $lt: 30 } } ] }`,
      which corresponds to the following SQL statement:

      ```sql
      SELECT * FROM inventory WHERE status = "A" OR qty < 30
      ```

  - id: go
    content: |
      The operation uses a query predicate of
      `{ $or: [ { status: 'A' }, { qty: { $lt: 30 } } ] }`,
      which corresponds to the following SQL statement:

      ```sql
      SELECT * FROM inventory WHERE status = "A" OR qty < 30
      ```

**Note:**

Queries with comparison operators are subject to type-bracketing.
