<!-- Part 1 of 4 of tutorial/query-arrays.md (split because the page is big). -->

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

  - id: c
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

  - id: kotlin-coroutine
    content: |
      To specify equality condition on an array, use the query
      document `{ <field>: <value> }` where `<value>` is the
      exact array to match, including the order of the elements.

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

  - id: go
    content: |
      To specify equality condition on an array, use the query
      document `{ <field>: <value> }` where `<value>` is the
      exact array to match, including the order of the elements.

tabs:
  - id: shell
    content: |
      The following example queries for all documents where
      `genres` is an array with exactly two elements,
      `"Action"` and `"Comedy"`, in the specified order:

  - id: compass
    content: |
      The following example queries for all documents where
      `tags` is an array with exactly two elements,
      `"red"` and `"blank"`, in the specified order:

  - id: c
    content: |
      The following example queries for all documents where
      `tags` is an array with exactly two elements,
      `"red"` and `"blank"`, in the specified order:

  - id: python
    content: |
      The following example queries for all documents where
      `tags` is an array with exactly two elements,
      `"red"` and `"blank"`, in the specified order:

  - id: motor
    content: |
      The following example queries for all documents where
      `tags` is an array with exactly two elements,
      `"red"` and `"blank"`, in the specified order:

  - id: java-sync
    content: |
      The following example queries for all documents where
      `tags` is an array with exactly two elements,
      `"red"` and `"blank"`, in the specified order:

  - id: java-async
    content: |
      The following example queries for all documents where
      `tags` is an array with exactly two elements,
      `"red"` and `"blank"`, in the specified order:

  - id: kotlin-coroutine
    content: |
      The following example queries for all documents where
      `tags` is an array with exactly two elements,
      `"red"` and `"blank"`, in the specified order:

  - id: nodejs
    content: |
      The following example queries for all documents where
      `tags` is an array with exactly two elements,
      `"red"` and `"blank"`, in the specified order:

  - id: php
    content: |
      The following example queries for all documents where
      `tags` is an array with exactly two elements,
      `"red"` and `"blank"`, in the specified order:

  - id: ruby
    content: |
      The following example queries for all documents where
      `tags` is an array with exactly two elements,
      `"red"` and `"blank"`, in the specified order:

  - id: scala
    content: |
      The following example queries for all documents where
      `tags` is an array with exactly two elements,
      `"red"` and `"blank"`, in the specified order:

  - id: csharp
    content: |
      The following example queries for all documents where
      `tags` is an array with exactly two elements,
      `"red"` and `"blank"`, in the specified order:

  - id: go
    content: |
      The following example queries for all documents where
      `tags` is an array with exactly two elements,
      `"red"` and `"blank"`, in the specified order:

tabs:
  - id: shell
    content: |

      ```javascript
      db.movies.find( { genres: ["Action", "Comedy"] } )
      ```

  - id: compass
    content: |
      Copy the following filter into the Compass query bar and click
      Find:

      ```javascript
      { tags: ["red", "blank"] }
      ```

      (Figure: /images/compass-array-match-exact.png)

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
      var filter = Builders<BsonDocument>.Filter.Eq("tags", new[] { "red", "blank" });
      var result = collection.Find(filter).ToList();
      ```

  - id: go
    content: |
      (Code example not available offline: /driver-examples/go_examples.go)

tabs:
  - id: shell
    content: |
      To find an array that contains both `"Action"` and
      `"Comedy"` regardless of order or other elements in
      the array, use the `$all` operator:

  - id: compass
    content: |
      To find an array that contains both `"red"` and
      `"blank"` regardless of order or other elements in
      the array, use the `$all` operator:

  - id: c
    content: |
      To find an array that contains both `"red"` and
      `"blank"` regardless of order or other elements in
      the array, use the `$all` operator:

  - id: python
    content: |
      To find an array that contains both `"red"` and
      `"blank"` regardless of order or other elements in
      the array, use the `$all` operator:

  - id: motor
    content: |
      To find an array that contains both `"red"` and
      `"blank"` regardless of order or other elements in
      the array, use the `$all` operator:

  - id: java-sync
    content: |
      To find an array that contains both `"red"` and
      `"blank"` regardless of order or other elements in
      the array, use the `$all` operator:

  - id: java-async
    content: |
      To find an array that contains both `"red"` and
      `"blank"` regardless of order or other elements in
      the array, use the `$all` operator:

  - id: kotlin-coroutine
    content: |
      To find an array that contains both `"red"` and
      `"blank"` regardless of order or other elements in
      the array, use the `$all` operator:

  - id: nodejs
    content: |
      To find an array that contains both `"red"` and
      `"blank"` regardless of order or other elements in
      the array, use the `$all` operator:

  - id: php
    content: |
      To find an array that contains both `"red"` and
      `"blank"` regardless of order or other elements in
      the array, use the `$all` operator:

  - id: ruby
    content: |
      To find an array that contains both `"red"` and
      `"blank"` regardless of order or other elements in
      the array, use the `$all` operator:

  - id: scala
    content: |
      To find an array that contains both `"red"` and
      `"blank"` regardless of order or other elements in
      the array, use the `$all` operator:

  - id: csharp
    content: |
      To find an array that contains both `"red"` and
      `"blank"` regardless of order or other elements in
      the array, use the `$all` operator:

  - id: go
    content: |
      To find an array that contains both `"red"` and
      `"blank"` regardless of order or other elements in
      the array, use the `$all` operator:

tabs:
  - id: shell
    content: |

      ```javascript
      db.movies.find( { genres: { $all: ["Action", "Comedy"] } } )
      ```

  - id: compass
    content: |
      Copy the following filter into the Compass query bar and click
      Find:

      ```javascript
      { tags: { $all: ["red", "blank"] } }
      ```

      (Figure: /images/compass-array-match-all.png)

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
      var filter = Builders<BsonDocument>.Filter.All("tags", new[] { "red", "blank" });
      var result = collection.Find(filter).ToList();
      ```

  - id: go
    content: |
      (Code example not available offline: /driver-examples/go_examples.go)
