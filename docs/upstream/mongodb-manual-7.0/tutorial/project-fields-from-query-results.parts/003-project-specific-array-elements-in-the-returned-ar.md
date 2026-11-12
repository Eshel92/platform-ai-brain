<!-- Part 3 of 4 of tutorial/project-fields-from-query-results.md (split because the page is big). -->

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
            var projection = Builders<BsonDocument>.Projection.Include("item").Include("status").Slice("instock", -1);
            var result = collection.Find<BsonDocument>(filter).Project(projection).ToList();
            ```

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
            var projection = Builders<BsonDocument>.Projection.Include("item").Include("status").Slice("instock", -1);
            var result = collection.Find<BsonDocument>(filter).Project(projection).ToList();
            ```

        - id: go
          content: |
            (Code example not available offline: /driver-examples/go_examples.go)

  - id: c 
    content: | 
      For fields that contain arrays, MongoDB provides the following
      projection operators for manipulating arrays: `$elemMatch`,
      `$slice`, and `$`.

      The following example uses the `$slice` projection operator
      to return the last element in the `instock` array:

      (Code example not available offline: /driver-examples/test-mongoc-sample-commands.c)

      `$elemMatch`, `$slice`, and
      `$` are the only operators that you can use to project specific elements
      to include in the returned array. For instance, you cannot
      project specific array elements using the array index; e.g.
      `{ "instock.0": 1 }` projection does not project the array
      with the first element.

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
            var projection = Builders<BsonDocument>.Projection.Include("item").Include("status").Slice("instock", -1);
            var result = collection.Find<BsonDocument>(filter).Project(projection).ToList();
            ```

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
            var projection = Builders<BsonDocument>.Projection.Include("item").Include("status").Slice("instock", -1);
            var result = collection.Find<BsonDocument>(filter).Project(projection).ToList();
            ```

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
            var projection = Builders<BsonDocument>.Projection.Include("item").Include("status").Slice("instock", -1);
            var result = collection.Find<BsonDocument>(filter).Project(projection).ToList();
            ```

        - id: go
          content: |
            (Code example not available offline: /driver-examples/go_examples.go)

      `$elemMatch`, `$slice`, and
      `$` are the *only* way to project specific elements
      to include in the returned array. For instance, you *cannot*
      project specific array elements using the array index; e.g.
      `include("instock.0")` projection will *not* project the array
      with the first element.

  - id: kotlin-coroutine
    content: | 
      For fields that contain arrays, MongoDB provides the following
      projection operators for manipulating arrays: `$elemMatch`,
      `$slice`, and `$`.

      The following example uses the `$slice` projection operator
      to return the last element in the `instock` array:

      (Code example not available offline: /driver-examples/kotlin_examples.kt)

      `$elemMatch`, `$slice`, and
      `$` are the *only* operators that you can use to project specific elements
      to include in the returned array. For instance, you *cannot*
      project specific array elements using the array index; e.g.
      `{ "instock.0": 1 }` projection does *not* project the array
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
            var projection = Builders<BsonDocument>.Projection.Include("item").Include("status").Slice("instock", -1);
            var result = collection.Find<BsonDocument>(filter).Project(projection).ToList();
            ```

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
            var projection = Builders<BsonDocument>.Projection.Include("item").Include("status").Slice("instock", -1);
            var result = collection.Find<BsonDocument>(filter).Project(projection).ToList();
            ```

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
            var projection = Builders<BsonDocument>.Projection.Include("item").Include("status").Slice("instock", -1);
            var result = collection.Find<BsonDocument>(filter).Project(projection).ToList();
            ```

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
            var projection = Builders<BsonDocument>.Projection.Include("item").Include("status").Slice("instock", -1);
            var result = collection.Find<BsonDocument>(filter).Project(projection).ToList();
            ```

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
            var projection = Builders<BsonDocument>.Projection.Include("item").Include("status").Slice("instock", -1);
            var result = collection.Find<BsonDocument>(filter).Project(projection).ToList();
            ```

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
            var projection = Builders<BsonDocument>.Projection.Include("item").Include("status").Slice("instock", -1);
            var result = collection.Find<BsonDocument>(filter).Project(projection).ToList();
            ```

        - id: go
          content: |
            (Code example not available offline: /driver-examples/go_examples.go)

      `$elemMatch`, `$slice`, and
      `$` are the only operators that you can use to project specific elements
      to include in the returned array. For instance, you cannot
      project specific array elements using the array index; e.g.
      `{ "instock.0": 1 }` projection does not project the array
      with the first element.

  - id: motor
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
            var projection = Builders<BsonDocument>.Projection.Include("item").Include("status").Slice("instock", -1);
            var result = collection.Find<BsonDocument>(filter).Project(projection).ToList();
            ```

        - id: go
          content: |
            (Code example not available offline: /driver-examples/go_examples.go)

      `$elemMatch`, `$slice`, and
      `$` are the only operators that you can use to project specific elements
      to include in the returned array. For instance, you cannot
      project specific array elements using the array index; e.g.
      `{ "instock.0": 1 }` projection does not project the array
      with the first element.
