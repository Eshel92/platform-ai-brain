<!-- Part 4 of 5 of tutorial/query-documents.md (split because the page is big). -->

## Specify `AND` as well as `OR` Conditions

tabs:
  - id: shell
    content: |
      In the following example, the compound query document
      selects all documents in the
      `sample_mflix.movies` collection where `rated`
      equals `"G"` **and** *either* `runtime` is less
      than (`$lt`) `90` *or* `title` starts
      with the character `T`:

  - id: compass
    content: |
      In the following example, the compound query document
      selects all documents in the collection where
      `status` equals `"A"` **and** *either* `qty`
      is less than (`$lt`) `30` *or* `item`
      starts with the character `p`:

  - id: c
    content: |
      In the following example, the compound query document
      selects all documents in the collection where
      `status` equals `"A"` **and** *either* `qty`
      is less than (`$lt`) `30` *or* `item`
      starts with the character `p`:

  - id: python
    content: |
      In the following example, the compound query document
      selects all documents in the collection where
      `status` equals `"A"` **and** *either* `qty`
      is less than (`$lt`) `30` *or* `item`
      starts with the character `p`:

  - id: motor
    content: |
      In the following example, the compound query document
      selects all documents in the collection where
      `status` equals `"A"` **and** *either* `qty`
      is less than (`$lt`) `30` *or* `item`
      starts with the character `p`:

  - id: java-sync
    content: |
      In the following example, the compound query document
      selects all documents in the collection where
      `status` equals `"A"` **and** *either* `qty`
      is less than (`$lt`) `30` *or* `item`
      starts with the character `p`:

  - id: java-async
    content: |
      In the following example, the compound query document
      selects all documents in the collection where
      `status` equals `"A"` **and** *either* `qty`
      is less than (`$lt`) `30` *or* `item`
      starts with the character `p`:

  - id: kotlin-coroutine
    content: |
      In the following example, the compound query document
      selects all documents in the collection where
      `status` equals `"A"` **and** *either* `qty`
      is less than (`$lt`) `30` *or* `item`
      starts with the character `p`:

  - id: nodejs
    content: |
      In the following example, the compound query document
      selects all documents in the collection where
      `status` equals `"A"` **and** *either* `qty`
      is less than (`$lt`) `30` *or* `item`
      starts with the character `p`:

  - id: php
    content: |
      In the following example, the compound query document
      selects all documents in the collection where
      `status` equals `"A"` **and** *either* `qty`
      is less than (`$lt`) `30` *or* `item`
      starts with the character `p`:

  - id: ruby
    content: |
      In the following example, the compound query document
      selects all documents in the collection where
      `status` equals `"A"` **and** *either* `qty`
      is less than (`$lt`) `30` *or* `item`
      starts with the character `p`:

  - id: scala
    content: |
      In the following example, the compound query document
      selects all documents in the collection where
      `status` equals `"A"` **and** *either* `qty`
      is less than (`$lt`) `30` *or* `item`
      starts with the character `p`:

  - id: csharp
    content: |
      In the following example, the compound query document
      selects all documents in the collection where
      `status` equals `"A"` **and** *either* `qty`
      is less than (`$lt`) `30` *or* `item`
      starts with the character `p`:

  - id: go
    content: |
      In the following example, the compound query document
      selects all documents in the collection where
      `status` equals `"A"` **and** *either* `qty`
      is less than (`$lt`) `30` *or* `item`
      starts with the character `p`:

tabs:
  - id: shell
    content: |

      ```javascript
      db.movies.find( {
           rated: "G",
           $or: [ { runtime: { $lt: 90 } }, { title: /^T/ } ]
      } )
      ```

  - id: compass
    content: |
      Copy the following filter into the Compass query bar and click
      Find:

      ```javascript
      { status: "A", $or: [ { qty: { $lt: 30 } }, { item: /^p/ } ] }
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
      var filter = builder.And(
          builder.Eq("status", "A"),
          builder.Or(builder.Lt("qty", 30), builder.Regex("item", new BsonRegularExpression("^p"))));
      var result = collection.Find(filter).ToList();
      ```

  - id: go
    content: |
      (Code example not available offline: /driver-examples/go_examples.go)

The operation uses a query predicate of:

tabs:
  - id: shell
    content: |

      ```javascript
      {
         rated: 'G',
         $or: [
           { runtime: { $lt: 90 } },
           { title: { $regex: '^T' } }
         ]
      }
      ```

      which corresponds to the following SQL statement:

      ```sql
      SELECT * FROM movies WHERE rated = "G"
      AND ( runtime < 90 OR title LIKE "T%")
      ```

  - id: compass
    content: |

      ```javascript
      {
         status: 'A',
         $or: [
           { qty: { $lt: 30 } },
           { item: { $regex: '^p' } }
         ]
      }
      ```

      which corresponds to the following SQL statement:

      ```sql
      SELECT * FROM inventory WHERE status = "A"
      AND ( qty < 30 OR item LIKE "p%")
      ```

  - id: c
    content: |

      ```javascript
      {
         status: 'A',
         $or: [
           { qty: { $lt: 30 } },
           { item: { $regex: '^p' } }
         ]
      }
      ```

      which corresponds to the following SQL statement:

      ```sql
      SELECT * FROM inventory WHERE status = "A"
      AND ( qty < 30 OR item LIKE "p%")
      ```

  - id: python
    content: |

      ```javascript
      {
         status: 'A',
         $or: [
           { qty: { $lt: 30 } },
           { item: { $regex: '^p' } }
         ]
      }
      ```

      which corresponds to the following SQL statement:

      ```sql
      SELECT * FROM inventory WHERE status = "A"
      AND ( qty < 30 OR item LIKE "p%")
      ```

  - id: motor
    content: |

      ```javascript
      {
         status: 'A',
         $or: [
           { qty: { $lt: 30 } },
           { item: { $regex: '^p' } }
         ]
      }
      ```

      which corresponds to the following SQL statement:

      ```sql
      SELECT * FROM inventory WHERE status = "A"
      AND ( qty < 30 OR item LIKE "p%")
      ```

  - id: java-sync
    content: |

      ```javascript
      {
         status: 'A',
         $or: [
           { qty: { $lt: 30 } },
           { item: { $regex: '^p' } }
         ]
      }
      ```

      which corresponds to the following SQL statement:

      ```sql
      SELECT * FROM inventory WHERE status = "A"
      AND ( qty < 30 OR item LIKE "p%")
      ```

  - id: java-async
    content: |

      ```javascript
      {
         status: 'A',
         $or: [
           { qty: { $lt: 30 } },
           { item: { $regex: '^p' } }
         ]
      }
      ```

      which corresponds to the following SQL statement:

      ```sql
      SELECT * FROM inventory WHERE status = "A"
      AND ( qty < 30 OR item LIKE "p%")
      ```

  - id: kotlin-coroutine
    content: |

      ```javascript
      {
         status: 'A',
         $or: [
           { qty: { $lt: 30 } },
           { item: { $regex: '^p' } }
         ]
      }
      ```

      which corresponds to the following SQL statement:

      ```sql
      SELECT * FROM inventory WHERE status = "A"
      AND ( qty < 30 OR item LIKE "p%")
      ```

  - id: nodejs
    content: |

      ```javascript
      {
         status: 'A',
         $or: [
           { qty: { $lt: 30 } },
           { item: { $regex: '^p' } }
         ]
      }
      ```

      which corresponds to the following SQL statement:

      ```sql
      SELECT * FROM inventory WHERE status = "A"
      AND ( qty < 30 OR item LIKE "p%")
      ```

  - id: php
    content: |

      ```javascript
      {
         status: 'A',
         $or: [
           { qty: { $lt: 30 } },
           { item: { $regex: '^p' } }
         ]
      }
      ```

      which corresponds to the following SQL statement:

      ```sql
      SELECT * FROM inventory WHERE status = "A"
      AND ( qty < 30 OR item LIKE "p%")
      ```

  - id: ruby
    content: |

      ```javascript
      {
         status: 'A',
         $or: [
           { qty: { $lt: 30 } },
           { item: { $regex: '^p' } }
         ]
      }
      ```

      which corresponds to the following SQL statement:

      ```sql
      SELECT * FROM inventory WHERE status = "A"
      AND ( qty < 30 OR item LIKE "p%")
      ```

  - id: scala
    content: |

      ```javascript
      {
         status: 'A',
         $or: [
           { qty: { $lt: 30 } },
           { item: { $regex: '^p' } }
         ]
      }
      ```

      which corresponds to the following SQL statement:

      ```sql
      SELECT * FROM inventory WHERE status = "A"
      AND ( qty < 30 OR item LIKE "p%")
      ```

  - id: csharp
    content: |

      ```javascript
      {
         status: 'A',
         $or: [
           { qty: { $lt: 30 } },
           { item: { $regex: '^p' } }
         ]
      }
      ```

      which corresponds to the following SQL statement:

      ```sql
      SELECT * FROM inventory WHERE status = "A"
      AND ( qty < 30 OR item LIKE "p%")
      ```

  - id: go
    content: |

      ```javascript
      {
         status: 'A',
         $or: [
           { qty: { $lt: 30 } },
           { item: { $regex: '^p' } }
         ]
      }
      ```

      which corresponds to the following SQL statement:

      ```sql
      SELECT * FROM inventory WHERE status = "A"
      AND ( qty < 30 OR item LIKE "p%")
      ```

**Note:**

MongoDB supports regular expression `$regex` queries to
perform string pattern matches. 

Regular expression syntax differs between `mongosh` and drivers. 
`mongosh` uses JavaScript regex literals (for example, `{ title: /^T/ }`).
The drivers use the equivalent `$regex` operator (for example,
`{ title: { $regex: '^T' } }`). 


## Query Documents with MongoDB Atlas

This example uses the sample movies dataset. To load the sample dataset 
into your MongoDB Atlas deployment, see Load Sample Data.

To project fields for a query in MongoDB Atlas, follow these
steps:

**Step 1: In the MongoDB Atlas UI, go to the Clusters page for your project.**

a. If it's not already displayed, select the organization that
   contains your desired project from the `office` Organizations menu in the
   navigation bar.

#. If it's not already displayed, select your project
   from the Projects menu in the navigation bar.

#. In the sidebar, click Clusters under 
   the Database heading.

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

The query returns all documents
in the `sample_mflix.movies` collection where the `year`
field matches `1924`.


## Additional Query Tutorials

For more query examples, see:

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
      The Find operation opens a
      cursor to the matching
      documents of the collection based on the find query.

      For more information on sampling, see the
      Compass FAQ.

  - id: c
    content: |
      The [mongoc_collection_find_with_opts](https://mongoc.org/libmongoc/current/mongoc_collection_find_with_opts.html) 
      method returns a cursor to the
      matching documents.

  - id: python
    content: |
      The `pymongo.collection.Collection.find` method
      returns a cursor to the
      matching documents. See the PyMongo documentation for
      [iterating over a cursor](https://pymongo.readthedocs.io/en/stable/tutorial.html#querying-for-more-than-one-document).

  - id: motor
    content: |
      The `pymongo.asynchronous.collection.AsyncCollection.find`
      method returns a cursor to the
      matching documents.

  - id: java-sync
    content: |
      The com.mongodb.client.MongoCollection.find_ method returns an
      instance of the com.mongodb.client.FindIterable_ interface.

  - id: java-async
    content: |
      [com.mongodb.reactivestreams.client.MongoCollection.find](http://mongodb.github.io/mongo-java-driver-reactivestreams/1.6/javadoc/com/mongodb/reactivestreams/client/MongoCollection.html#find())
      returns an instance of the [com.mongodb.reactivestreams.client.FindPublisher](http://mongodb.github.io/mongo-java-driver-reactivestreams/1.6/javadoc/com/mongodb/reactivestreams/client/FindPublisher.html)
      interface.

  - id: kotlin-coroutine
    content: |
      The [MongoCollection.find()](https://mongodb.github.io/mongo-java-driver/{+java-driver-version+}/apidocs/driver-kotlin-coroutine/mongodb-driver-kotlin-coroutine/com.mongodb.kotlin.client.coroutine/-mongo-collection/find.html) method returns an
      instance of the
      [FindFlow](https://mongodb.github.io/mongo-java-driver/{+java-driver-version+}/apidocs/driver-kotlin-coroutine/mongodb-driver-kotlin-coroutine/com.mongodb.kotlin.client.coroutine/-find-flow/index.html)
      class.

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
      for [iterating over a cursor](https://www.mongodb.com/docs/ruby-driver/current/api/Mongo/Cursor.html#each-instance_method).

  - id: scala
    content: |
      The `collection.find()`
      method returns the find [Observable](http://mongodb.github.io/mongo-scala-driver/2.1/reference/observables/).

  - id: csharp
    content: |
      The `MongoCollection.Find()`
      method returns a cursor to
      the matching documents. See the MongoDB .NET/C# Driver
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
shards, read concern lets clients choose an
isolation level for their reads. For more information, see
/reference/read-concern.

### Query Result Format

When you run a find operation with a MongoDB driver or `mongosh`,
MongoDB returns a cursor that manages query results. Query
results are not returned as an array of documents.

To learn how to iterate through documents in a cursor, see your
`driver's documentation`. If you are using `mongosh`, see
read-operations-cursors.
