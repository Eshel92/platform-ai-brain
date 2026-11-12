<!-- Part 2 of 4 of tutorial/project-fields-from-query-results.md (split because the page is big). -->

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
      var projection = Builders<BsonDocument>.Projection.Include("item").Include("status").Include("instock.qty");
      var result = collection.Find<BsonDocument>(filter).Project(projection).ToList();
      ```

  - id: go
    content: |
      (Code example not available offline: /driver-examples/go_examples.go)
