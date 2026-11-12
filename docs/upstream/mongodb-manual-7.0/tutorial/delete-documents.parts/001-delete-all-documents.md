<!-- Part 1 of 6 of tutorial/delete-documents.md (split because the page is big). -->

## Delete All Documents

tabs:
  - id: shell
    content: |

      To delete all documents from a collection, pass an empty
      filter document `{}` to the
      `db.collection.deleteMany()` method.

      The following example deletes *all* documents from the `inventory`
      collection:

  - id: c
    content: |

      To delete all documents from a collection, pass the 
      [mongoc_collection_t](https://mongoc.org/libmongoc/current/mongoc_collection_t.html)
      and a [bson_t](https://mongoc.org/libbson/current/bson_t.html) 
      that matches all documents to the  
      [mongoc_collection_delete_many](https://mongoc.org/libmongoc/current/mongoc_collection_delete_many.html) 
      method.

      The following example deletes *all* documents from the `inventory`
      collection:

  - id: compass
    content: |

      To delete all documents from a collection, click the DELETE button under the 
      Documents tab. 

      The following example deletes *all* documents from the `inventory`
      collection:

  - id: python
    content: |

      To delete all documents from a collection, pass an empty
      filter document `{}` to the
      `pymongo.collection.Collection.delete_many` method.

      The following example deletes *all* documents from the `inventory`
      collection:

  - id: motor
    content: |

      To delete all documents from a collection, pass an empty
      filter document `{}` to the
      `motor.motor_asyncio.AsyncIOMotorCollection.delete_many`
      method.

      The following example deletes *all* documents from the `inventory`
      collection:

  - id: java-sync
    content: |

      To delete all documents from a collection, pass an empty
      org.bson.Document_ object as the
      filter to the
      com.mongodb.client.MongoCollection.deleteMany_ method.

      The following example deletes *all* documents from the `inventory`
      collection:

  - id: java-async
    content: |

      To delete all documents from a collection, pass an empty
      org.bson.Document_ object as the
      filter to the
      [com.mongodb.reactivestreams.client.MongoCollection.deleteMany](http://mongodb.github.io/mongo-java-driver-reactivestreams/1.6/javadoc/com/mongodb/reactivestreams/client/MongoCollection.html#deleteMany(org.bson.conversions.Bson))
      method.

      The following example deletes *all* documents from the `inventory`
      collection:

  - id: kotlin-coroutine
    content: |

      To delete all documents from a collection, pass an empty
      `Bson` object as the filter to the
      [MongoCollection.deleteMany()](https://mongodb.github.io/mongo-java-driver/{+java-driver-version+}/apidocs/driver-kotlin-coroutine/mongodb-driver-kotlin-coroutine/com.mongodb.kotlin.client.coroutine/-mongo-collection/delete-many.html) method.

      The following example deletes *all* documents from the `inventory`
      collection:

  - id: nodejs
    content: |

      To delete all documents from a collection, pass an empty
      filter document `{}` to the
      `Collection.deleteMany()`
      method.

      The following example deletes *all* documents from the `inventory`
      collection:

  - id: php
    content: |

      To delete all documents from a collection, pass an empty
      filter document `[]` to the
      `MongoDBCollection::deleteMany()`
      method.

      The following example deletes *all* documents from the `inventory`
      collection:

  - id: ruby
    content: |

      To delete all documents from a collection, pass an empty
      filter document `{}` to the
      `Mongo::Collection#delete_many()`
      method.

      The following example deletes *all* documents from the `inventory`
      collection:

  - id: scala
    content: |

      To delete all documents from a collection, pass an empty
      filter `Document()` to the
      `collection.deleteMany()`
      method.

      The following example deletes *all* documents from the `inventory`
      collection:

  - id: csharp
    content: |

      To delete all documents from a collection, pass an empty
      filter
      `Builders<BsonDocument>.Filter.Empty` to the
      `IMongoCollection.DeleteMany()` method.

      The following example deletes *all* documents from the `inventory`
      collection:

  - id: go
    content: |

      To delete all documents from a collection, pass an empty
      filter document to the
      `Collection.DeleteMany` function.

      The following example deletes *all* documents from the `inventory`
      collection:

tabs:
  - id: shell
    content: |

      ```javascript
      db.inventory.deleteMany({})
      ```

  - id: c
    content: |

      (Code example not available offline: /driver-examples/test-mongoc-sample-commands.c)

  - id: compass
    content: |

      (Figure: /images/compass-delete-all.png)

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

      (Code example not available offline: /driver-examples/node_remove.js)

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
      var result = collection.DeleteMany(filter);
      ```

  - id: go
    content: |
      (Code example not available offline: /driver-examples/go_examples.go)

tabs:
  - id: shell
    content: |
      The method returns a document with the status of the operation. For
      more information and examples, see
      `deleteMany()`.

  - id: c
    content: |
      The [mongoc_collection_delete_many](https://mongoc.org/libmongoc/current/mongoc_collection_delete_many.html) 
      method returns `true` if successful, or returns `false` and sets 
      an error if there are invalid arguments or a server or network error 
      occurs.

  - id: compass
    content: |
      When you confirm the deletion in the pop-up window that appears when you click DELETE,
      MongoDB Compass deletes all documents and displays a message 
      indicating how many documents were deleted.

  - id: python
    content: |
      The `delete_many`
      method returns an instance of
      `pymongo.results.DeleteResult` with the status of the
      operation.

  - id: motor
    content: |
      The `delete_many`
      coroutine asynchronously returns an instance of
      `pymongo.results.DeleteResult` with the status of the
      operation.

  - id: java-sync
    content: |
      The com.mongodb.client.MongoCollection.deleteMany_
      method returns an instance of
      com.mongodb.client.result.DeleteResult_
      with the status of the
      operation.

  - id: java-async
    content: |
      [com.mongodb.reactivestreams.client.MongoCollection.deleteMany](http://mongodb.github.io/mongo-java-driver-reactivestreams/1.6/javadoc/com/mongodb/reactivestreams/client/MongoCollection.html#deleteMany(org.bson.conversions.Bson))
      returns a [Publisher](http://www.reactive-streams.org/reactive-streams-1.0.1-javadoc/org/reactivestreams/Publisher.html)
      object of type com.mongodb.client.result.DeleteResult_ if
      successful. Returns an instance of `com.mongodb.MongoException` if unsuccessful.

  - id: kotlin-coroutine
    content: |
      The [MongoCollection.deleteMany()](https://mongodb.github.io/mongo-java-driver/{+java-driver-version+}/apidocs/driver-kotlin-coroutine/mongodb-driver-kotlin-coroutine/com.mongodb.kotlin.client.coroutine/-mongo-collection/delete-many.html)
      method returns an instance of
      [com.mongodb.client.result.DeleteResult](https://mongodb.github.io/mongo-java-driver/{+java-driver-version+}/apidocs/driver-core/com/mongodb/client/result/DeleteResult.html)
      that describes the status of the
      operation and count of deleted documents.

  - id: nodejs
    content: |
      `Collection.deleteMany()` 
      returns a promise that provides a `result`. The `result.deletedCount`
      property contains the number of documents that matched the
      filter.

  - id: php
    content: |
      Upon successful execution, the
      `deleteMany()`
      method returns an instance of
      `MongoDBDeleteResult`
      whose `getDeletedCount()`
      method returns the number of documents that matched the filter.

  - id: ruby
    content: |
      Upon successful execution, the
      `delete_many()` method
      returns an instance of
      `Mongo::Operation::Result`, whose
      `deleted_count` attribute contains the number of documents
      that matched the filter.

  - id: scala
    content: |
      Upon successful execution, the
      `collection.deleteMany()` method
      returns an
      [Observable](http://mongodb.github.io/mongo-scala-driver/2.1/reference/observables/)
      with a single element with a `DeleteResult` type parameter or with
      an `com.mongodb.MongoException`.

  - id: csharp
    content: |
      Upon successful execution, the
      `IMongoCollection.DeleteMany()`
      method returns an instance of
      `DeleteResult` whose
      `DeletedCount` property contains the number of documents
      that matched the filter.

  - id: go
    content: |
      Upon successful execution, the
      `Collection.DeleteMany`
      function returns an instance of
      `DeleteResult` whose
      `DeletedCount` property contains the number of documents
      that matched the filter.
