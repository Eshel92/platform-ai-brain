<!-- Part 3 of 4 of tutorial/query-arrays.md (split because the page is big). -->

## Specify Multiple Conditions for Array Elements

When you specify compound conditions on array elements, you can query for
documents where either:

- A single array element meets all the specified conditions
- Different array elements collectively meet all the conditions, with each
  element satisfying one or more conditions

### Query an Array with Compound Filter Conditions on the Array Elements

tabs:
  - id: shell
    content: |
      The following example queries for documents where the
      `cast` array contains elements that in some
      combination satisfy the query conditions. One element
      can satisfy the `$regex: "^A"` condition and another
      element can satisfy the `$ne: "Adam Sandler"`
      condition, or a single element can satisfy both:

  - id: compass
    content: |
      The following example queries for documents where the
      `dim_cm` array contains elements that in some
      combination satisfy the query conditions. One element
      can satisfy the greater than `15` condition and
      another element can satisfy the less than `20`
      condition, or a single element can satisfy both:

  - id: c
    content: |
      The following example queries for documents where the
      `dim_cm` array contains elements that in some
      combination satisfy the query conditions. One element
      can satisfy the greater than `15` condition and
      another element can satisfy the less than `20`
      condition, or a single element can satisfy both:

  - id: python
    content: |
      The following example queries for documents where the
      `dim_cm` array contains elements that in some
      combination satisfy the query conditions. One element
      can satisfy the greater than `15` condition and
      another element can satisfy the less than `20`
      condition, or a single element can satisfy both:

  - id: motor
    content: |
      The following example queries for documents where the
      `dim_cm` array contains elements that in some
      combination satisfy the query conditions. One element
      can satisfy the greater than `15` condition and
      another element can satisfy the less than `20`
      condition, or a single element can satisfy both:

  - id: java-sync
    content: |
      The following example queries for documents where the
      `dim_cm` array contains elements that in some
      combination satisfy the query conditions. One element
      can satisfy the greater than `15` condition and
      another element can satisfy the less than `20`
      condition, or a single element can satisfy both:

  - id: java-async
    content: |
      The following example queries for documents where the
      `dim_cm` array contains elements that in some
      combination satisfy the query conditions. One element
      can satisfy the greater than `15` condition and
      another element can satisfy the less than `20`
      condition, or a single element can satisfy both:

  - id: kotlin-coroutine
    content: |
      The following example queries for documents where the
      `dim_cm` array contains elements that in some
      combination satisfy the query conditions. One element
      can satisfy the greater than `15` condition and
      another element can satisfy the less than `20`
      condition, or a single element can satisfy both:

  - id: nodejs
    content: |
      The following example queries for documents where the
      `dim_cm` array contains elements that in some
      combination satisfy the query conditions. One element
      can satisfy the greater than `15` condition and
      another element can satisfy the less than `20`
      condition, or a single element can satisfy both:

  - id: php
    content: |
      The following example queries for documents where the
      `dim_cm` array contains elements that in some
      combination satisfy the query conditions. One element
      can satisfy the greater than `15` condition and
      another element can satisfy the less than `20`
      condition, or a single element can satisfy both:

  - id: ruby
    content: |
      The following example queries for documents where the
      `dim_cm` array contains elements that in some
      combination satisfy the query conditions. One element
      can satisfy the greater than `15` condition and
      another element can satisfy the less than `20`
      condition, or a single element can satisfy both:

  - id: scala
    content: |
      The following example queries for documents where the
      `dim_cm` array contains elements that in some
      combination satisfy the query conditions. One element
      can satisfy the greater than `15` condition and
      another element can satisfy the less than `20`
      condition, or a single element can satisfy both:

  - id: csharp
    content: |
      The following example queries for documents where the
      `dim_cm` array contains elements that in some
      combination satisfy the query conditions. One element
      can satisfy the greater than `15` condition and
      another element can satisfy the less than `20`
      condition, or a single element can satisfy both:

  - id: go
    content: |
      The following example queries for documents where the
      `dim_cm` array contains elements that in some
      combination satisfy the query conditions. One element
      can satisfy the greater than `15` condition and
      another element can satisfy the less than `20`
      condition, or a single element can satisfy both:

tabs:
  - id: shell
    content: |

      ```javascript
      db.movies.find(
         { cast: { $regex: "^A", $ne: "Adam Sandler" } }
      )
      ```

  - id: compass
    content: |
      Copy the following filter into the Compass query bar and click
      Find:

      ```javascript
      { dim_cm: { $gt: 15, $lt: 20 } }
      ```

      (Figure: /images/compass-array-compound-filter.png)

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

      ```csharp
      var builder = Builders<BsonDocument>.Filter;
      var filter = builder.And(builder.Gt("dim_cm", 15), builder.Lt("dim_cm", 20));
      var result = collection.Find(filter).ToList();
      ```

  - id: go
    content: |
      (Code example not available offline: /driver-examples/go_examples.go)

### Query for an Array Element that Meets Multiple Criteria

Use the `$elemMatch` operator to specify multiple criteria on
array elements so that at least one array element satisfies all the
specified criteria.

tabs:
  - id: shell
    content: |
      The following example queries for documents where the
      `cast` array contains at least one element that both
      matches the regular expression `^A` and is not equal
      to `"Adam Sandler"`:

  - id: compass
    content: |
      The following example queries for documents where the
      `dim_cm` array contains at least one element that
      is both greater than (`$gt`) `22` and less
      than (`$lt`) `30`:

  - id: c
    content: |
      The following example queries for documents where the
      `dim_cm` array contains at least one element that
      is both greater than (`$gt`) `22` and less
      than (`$lt`) `30`:

  - id: python
    content: |
      The following example queries for documents where the
      `dim_cm` array contains at least one element that
      is both greater than (`$gt`) `22` and less
      than (`$lt`) `30`:

  - id: motor
    content: |
      The following example queries for documents where the
      `dim_cm` array contains at least one element that
      is both greater than (`$gt`) `22` and less
      than (`$lt`) `30`:

  - id: java-sync
    content: |
      The following example queries for documents where the
      `dim_cm` array contains at least one element that
      is both greater than (`$gt`) `22` and less
      than (`$lt`) `30`:

  - id: java-async
    content: |
      The following example queries for documents where the
      `dim_cm` array contains at least one element that
      is both greater than (`$gt`) `22` and less
      than (`$lt`) `30`:

  - id: kotlin-coroutine
    content: |
      The following example queries for documents where the
      `dim_cm` array contains at least one element that
      is both greater than (`$gt`) `22` and less
      than (`$lt`) `30`:

  - id: nodejs
    content: |
      The following example queries for documents where the
      `dim_cm` array contains at least one element that
      is both greater than (`$gt`) `22` and less
      than (`$lt`) `30`:

  - id: php
    content: |
      The following example queries for documents where the
      `dim_cm` array contains at least one element that
      is both greater than (`$gt`) `22` and less
      than (`$lt`) `30`:

  - id: ruby
    content: |
      The following example queries for documents where the
      `dim_cm` array contains at least one element that
      is both greater than (`$gt`) `22` and less
      than (`$lt`) `30`:

  - id: scala
    content: |
      The following example queries for documents where the
      `dim_cm` array contains at least one element that
      is both greater than (`$gt`) `22` and less
      than (`$lt`) `30`:

  - id: csharp
    content: |
      The following example queries for documents where the
      `dim_cm` array contains at least one element that
      is both greater than (`$gt`) `22` and less
      than (`$lt`) `30`:

  - id: go
    content: |
      The following example queries for documents where the
      `dim_cm` array contains at least one element that
      is both greater than (`$gt`) `22` and less
      than (`$lt`) `30`:

tabs:
  - id: shell
    content: |

      ```javascript
      db.movies.find(
         { cast: { $elemMatch: { $regex: "^A", $ne: "Adam Sandler" } } }
      )
      ```

  - id: compass
    content: |
      Copy the following filter into the Compass query bar and click
      Find:

      ```javascript
      { dim_cm: { $elemMatch: { $gt: 22, $lt: 30 } } }
      ```

      (Figure: /images/compass-array-compound-multiple-criteria.png)

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

      ```csharp
      var filter = Builders<BsonDocument>.Filter.ElemMatch<BsonValue>("dim_cm", new BsonDocument { { "$gt", 22 }, { "$lt", 30 } });
      var result = collection.Find(filter).ToList();
      ```

  - id: go
    content: |
      (Code example not available offline: /driver-examples/go_examples.go)

### Query for an Element by the Array Index Position

Use dot notation to specify query conditions for an element at
a particular index or position of the array. The array uses zero-based
indexing.

**Note:**

When you query using dot notation, the field and nested field must be
inside quotation marks.

tabs:
  - id: shell
    content: |
      The following example queries for all documents where
      the first element in the array `cast` equals
      `"Tom Hanks"`:

  - id: compass
    content: |
      The following example queries for all documents where
      the second element in the array `dim_cm` is greater
      than `25`:

  - id: c
    content: |
      The following example queries for all documents where
      the second element in the array `dim_cm` is greater
      than `25`:

  - id: python
    content: |
      The following example queries for all documents where
      the second element in the array `dim_cm` is greater
      than `25`:

  - id: motor
    content: |
      The following example queries for all documents where
      the second element in the array `dim_cm` is greater
      than `25`:

  - id: java-sync
    content: |
      The following example queries for all documents where
      the second element in the array `dim_cm` is greater
      than `25`:

  - id: java-async
    content: |
      The following example queries for all documents where
      the second element in the array `dim_cm` is greater
      than `25`:

  - id: kotlin-coroutine
    content: |
      The following example queries for all documents where
      the second element in the array `dim_cm` is greater
      than `25`:

  - id: nodejs
    content: |
      The following example queries for all documents where
      the second element in the array `dim_cm` is greater
      than `25`:

  - id: php
    content: |
      The following example queries for all documents where
      the second element in the array `dim_cm` is greater
      than `25`:

  - id: ruby
    content: |
      The following example queries for all documents where
      the second element in the array `dim_cm` is greater
      than `25`:

  - id: scala
    content: |
      The following example queries for all documents where
      the second element in the array `dim_cm` is greater
      than `25`:

  - id: csharp
    content: |
      The following example queries for all documents where
      the second element in the array `dim_cm` is greater
      than `25`:

  - id: go
    content: |
      The following example queries for all documents where
      the second element in the array `dim_cm` is greater
      than `25`:

tabs:
  - id: shell
    content: |

      ```javascript
      db.movies.find( { "cast.0": "Tom Hanks" } )
      ```

  - id: compass
    content: |
      Copy the following filter into the Compass query bar and click
      Find:

      ```javascript
      { "dim_cm.1": { $gt: 25 } }
      ```

      (Figure: /images/compass-array-match-by-index.png)

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

      ```csharp
      var filter = Builders<BsonDocument>.Filter.Gt("dim_cm.1", 25);
      var result = collection.Find(filter).ToList();
      ```

  - id: go
    content: |
      (Code example not available offline: /driver-examples/go_examples.go)

### Query an Array by Array Length

Use the `$size` operator to query for arrays by number of
elements.

tabs:
  - id: shell
    content: |
      The following example selects documents where
      `genres` has 3 elements:

  - id: compass
    content: |
      The following example selects documents where
      `tags` has 3 elements:

  - id: c
    content: |
      The following example selects documents where
      `tags` has 3 elements:

  - id: python
    content: |
      The following example selects documents where
      `tags` has 3 elements:

  - id: motor
    content: |
      The following example selects documents where
      `tags` has 3 elements:

  - id: java-sync
    content: |
      The following example selects documents where
      `tags` has 3 elements:

  - id: java-async
    content: |
      The following example selects documents where
      `tags` has 3 elements:

  - id: kotlin-coroutine
    content: |
      The following example selects documents where
      `tags` has 3 elements:

  - id: nodejs
    content: |
      The following example selects documents where
      `tags` has 3 elements:

  - id: php
    content: |
      The following example selects documents where
      `tags` has 3 elements:

  - id: ruby
    content: |
      The following example selects documents where
      `tags` has 3 elements:

  - id: scala
    content: |
      The following example selects documents where
      `tags` has 3 elements:

  - id: csharp
    content: |
      The following example selects documents where
      `tags` has 3 elements:

  - id: go
    content: |
      The following example selects documents where
      `tags` has 3 elements:

tabs:
  - id: shell
    content: |

      ```javascript
      db.movies.find( { genres: { $size: 3 } } )
      ```

  - id: compass
    content: |
      Copy the following filter into the Compass query bar and click
      Find:

      ```javascript
      { "tags": { $size: 3 } }
      ```

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

      ```csharp
      var filter = Builders<BsonDocument>.Filter.Size("tags", 3);
      var result = collection.Find(filter).ToList();
      ```

  - id: go
    content: |
      (Code example not available offline: /driver-examples/go_examples.go)
