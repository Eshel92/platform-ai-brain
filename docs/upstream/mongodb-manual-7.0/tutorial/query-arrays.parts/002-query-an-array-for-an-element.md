<!-- Part 2 of 4 of tutorial/query-arrays.md (split because the page is big). -->

## Query an Array for an Element

tabs:
  - id: shell
    content: |
      To query if the array field contains at least *one* element
      with the specified value, use the filter
      `{ <field>: <value> }` where `<value>` is the element value.

  - id: compass
    content: |
      To query if the array field contains at least *one* element
      with the specified value, use the filter
      `{ <field>: <value> }` where `<value>` is the element value.

  - id: c
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

  - id: kotlin-coroutine
    content: |

      To query if the array field contains at least *one* element
      with the specified value, use the filter
      `eq( <field>, <value>)` where `<value>` is the element value.

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

  - id: go
    content: |

      To query if the array field contains at least *one* element
      with the specified value, use the filter
      `eq( <field>, <value>)` where `<value>` is the element value.

tabs:
  - id: shell
    content: |
      The following example queries for all documents where
      the `genres` array contains the string `"Short"`
      as one of its elements:

  - id: compass
    content: |
      The following example queries for all documents where
      the `tags` array contains the string `"red"`
      as one of its elements:

  - id: c
    content: |
      The following example queries for all documents where
      the `tags` array contains the string `"red"`
      as one of its elements:

  - id: python
    content: |
      The following example queries for all documents where
      the `tags` array contains the string `"red"`
      as one of its elements:

  - id: motor
    content: |
      The following example queries for all documents where
      the `tags` array contains the string `"red"`
      as one of its elements:

  - id: java-sync
    content: |
      The following example queries for all documents where
      the `tags` array contains the string `"red"`
      as one of its elements:

  - id: java-async
    content: |
      The following example queries for all documents where
      the `tags` array contains the string `"red"`
      as one of its elements:

  - id: kotlin-coroutine
    content: |
      The following example queries for all documents where
      the `tags` array contains the string `"red"`
      as one of its elements:

  - id: nodejs
    content: |
      The following example queries for all documents where
      the `tags` array contains the string `"red"`
      as one of its elements:

  - id: php
    content: |
      The following example queries for all documents where
      the `tags` array contains the string `"red"`
      as one of its elements:

  - id: ruby
    content: |
      The following example queries for all documents where
      the `tags` array contains the string `"red"`
      as one of its elements:

  - id: scala
    content: |
      The following example queries for all documents where
      the `tags` array contains the string `"red"`
      as one of its elements:

  - id: csharp
    content: |
      The following example queries for all documents where
      the `tags` array contains the string `"red"`
      as one of its elements:

  - id: go
    content: |
      The following example queries for all documents where
      the `tags` array contains the string `"red"`
      as one of its elements:

tabs:
  - id: shell
    content: |

      ```javascript
      db.movies.find( { genres: "Short" } )
      ```

  - id: compass
    content: |
      Copy the following filter into the Compass query bar and click
      Find:

      ```javascript
      { tags: "red" }
      ```

      (Figure: /images/compass-array-elem-match.png)

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
      var filter = Builders<BsonDocument>.Filter.Eq("tags", "red");
      var result = collection.Find(filter).ToList();
      ```

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

  - id: c
    content: |
      To specify conditions on the elements in the array field,
      use query operators in the
      query filter document:

      ```c
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

  - id: kotlin-coroutine
    content: |
      To specify conditions on the elements in the array field,
      use query operators in the
      query filter document. For example:

      ```kotlin
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

  - id: go
    content: |
      To specify conditions on the elements in the array field,
      use query operators in the
      query filter document. For example:

      ```go
      filter := bson.D{
          {"$and", bson.A{
              bson.D{{<array field>, bson.D{{"$eq", <value1>}}}},
              bson.D{{<array field>, bson.D{{"$lt", <value2>}}}},
          }},
      }
      ```

tabs:
  - id: shell
    content: |
      The following example queries for all documents where
      the `cast` array contains at least one element that
      matches the regular expression `^A`:

  - id: compass
    content: |
      The following example queries for all documents where
      the array `dim_cm` contains at least one element
      whose value is greater than `25`:

  - id: c
    content: |
      The following example queries for all documents where
      the array `dim_cm` contains at least one element
      whose value is greater than `25`:

  - id: python
    content: |
      The following example queries for all documents where
      the array `dim_cm` contains at least one element
      whose value is greater than `25`:

  - id: motor
    content: |
      The following example queries for all documents where
      the array `dim_cm` contains at least one element
      whose value is greater than `25`:

  - id: java-sync
    content: |
      The following example queries for all documents where
      the array `dim_cm` contains at least one element
      whose value is greater than `25`:

  - id: java-async
    content: |
      The following example queries for all documents where
      the array `dim_cm` contains at least one element
      whose value is greater than `25`:

  - id: kotlin-coroutine
    content: |
      The following example queries for all documents where
      the array `dim_cm` contains at least one element
      whose value is greater than `25`:

  - id: nodejs
    content: |
      The following example queries for all documents where
      the array `dim_cm` contains at least one element
      whose value is greater than `25`:

  - id: php
    content: |
      The following example queries for all documents where
      the array `dim_cm` contains at least one element
      whose value is greater than `25`:

  - id: ruby
    content: |
      The following example queries for all documents where
      the array `dim_cm` contains at least one element
      whose value is greater than `25`:

  - id: scala
    content: |
      The following example queries for all documents where
      the array `dim_cm` contains at least one element
      whose value is greater than `25`:

  - id: csharp
    content: |
      The following example queries for all documents where
      the array `dim_cm` contains at least one element
      whose value is greater than `25`:

  - id: go
    content: |
      The following example queries for all documents where
      the array `dim_cm` contains at least one element
      whose value is greater than `25`:

tabs:
  - id: shell
    content: |

      ```javascript
      db.movies.find( { cast: { $regex: "^A" } } )
      ```

  - id: compass
    content: |
      Copy the following filter into the Compass query bar and click
      Find:

      ```javascript
      { dim_cm: { $gt: 25 } }
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
      var filter = Builders<BsonDocument>.Filter.Gt("dim_cm", 25);
      var result = collection.Find(filter).ToList();
      ```

  - id: go
    content: |
      (Code example not available offline: /driver-examples/go_examples.go)
