<!-- Part 6 of 6 of tutorial/delete-documents.md (split because the page is big). -->

## Delete Only One Document that Matches a Condition

tabs:
  - id: shell
    content: |

      To delete at most a single document that matches a specified
      filter (even though multiple documents may match the specified
      filter) use the `db.collection.deleteOne()` method.

      The following example deletes the *first* document where `status` is
      `"D"`:

  - id: compass
    content: |

      To delete a single document that matches a specified filter:

      1. Write your query filter in ther Compass query bar and click Find.
      #. Hover your mouse over the document you want to delete.
      #. Click the `Trash` button on the right side of your document.

      The following example deletes a document with `{ status: "A" }` 
      from the `inventory` collection:

  - id: c
    content: |

      To delete a single document from a collection, pass the 
      [mongoc_collection_t](https://mongoc.org/libmongoc/current/mongoc_collection_t.html)
      and a [bson_t](https://mongoc.org/libbson/current/bson_t.html) 
      that matches the document you want to delete to the 
      [mongoc_collection_delete_one](https://mongoc.org/libmongoc/current/mongoc_collection_delete_one.html) 
      method.

      The following example deletes the *first* document where `status` is
      `"D"`:

  - id: python
    content: |

      To delete at most a single document that matches a specified
      filter (even though multiple documents may match the specified
      filter) use the
      `pymongo.collection.Collection.delete_one` method.

      The following example deletes the *first* document where `status` is
      `"D"`:

  - id: motor
    content: |

      To delete at most a single document that matches a specified
      filter (even though multiple documents may match the specified
      filter) use the
      `motor.motor_asyncio.AsyncIOMotorCollection.delete_one`
      method.

      The following example deletes the *first* document where `status` is
      `"D"`:

  - id: java-sync
    content: |

      To delete at most a single document that matches a specified
      filter (even though multiple documents may match the specified
      filter) use the com.mongodb.client.MongoCollection.deleteOne_
      method.

      The following example deletes the *first* document where `status` is
      `"D"`:

  - id: java-async
    content: |

      To delete at most a single document that matches a specified
      filter (even though multiple documents may match the specified
      filter) use the [com.mongodb.reactivestreams.client.MongoCollection.deleteMany](http://mongodb.github.io/mongo-java-driver-reactivestreams/1.6/javadoc/com/mongodb/reactivestreams/client/MongoCollection.html#deleteMany(org.bson.conversions.Bson))
      method.

      The following example deletes the *first* document where `status` is
      `"D"`:

  - id: kotlin-coroutine
    content: |

      To delete at most a single document that matches a specified
      filter, even if multiple documents match the specified
      filter, you can use the [MongoCollection.deleteOne()](https://mongodb.github.io/mongo-java-driver/{+java-driver-version+}/apidocs/driver-kotlin-coroutine/mongodb-driver-kotlin-coroutine/com.mongodb.kotlin.client.coroutine/-mongo-collection/delete-one.html)
      method.

  - id: nodejs
    content: |

      To delete at most a single document that matches a specified
      filter (even though multiple documents may match the specified
      filter) use the
      `Collection.deleteOne()`
      method.

      The following example deletes the *first* document where `status` is
      `"D"`:

  - id: php
    content: |

      To delete at most a single document that matches a specified
      filter (even though multiple documents may match the specified
      filter) use the
      `MongoDBCollection::deleteOne()`
      method.

      The following example deletes the *first* document where `status` is
      `"D"`:

  - id: ruby
    content: |

      To delete at most a single document that matches a specified
      filter (even though multiple documents may match the specified
      filter) use the
      `Mongo::Collection#delete_one()`
      method.

      The following example deletes the *first* document where `status` is
      `"D"`:

  - id: csharp
    content: |

      To delete at most a single document that matches a specified
      filter (even though multiple documents may match the specified
      filter) use the
      `IMongoCollection.DeleteOne()`
      method.

      The following example deletes the *first* document where `status` is
      `"D"`:

  - id: scala
    content: |

      To delete at most a single document that matches a specified
      filter (even though multiple documents may match the specified
      filter) use the
      `collection.deleteOne()`
      method.

      The following example deletes the *first* document where `status` is
      `"D"`:

  - id: go
    content: |

      To delete at most a single document that matches a specified
      filter (even though multiple documents may match the specified
      filter) use the
      `Collection.DeleteOne` function.

      The following example deletes the *first* document where `status` is
      `"D"`:

tabs:
  - id: shell
    content: |

      ```javascript
      db.inventory.deleteOne( { status: "D" } )
      ```

  - id: compass
    content: |

      (Figure: /images/compass-delete-one.png)

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

  - id: kotlin-coroutine
    content: |

      The following example deletes the *first* document where `status` is
      `"D"`:

  - id: motor
    content: |

      (Code example not available offline: /driver-examples/test_examples_motor.py)

  - id: java-sync
    content: |

      (Code example not available offline: /driver-examples/DocumentationSamples.java)

  - id: java-async
    content: |

      (Code example not available offline: /driver-examples/AsyncDocumentationSamples.java)

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
      var filter = Builders<BsonDocument>.Filter.Eq("status", "D");
      var result = collection.DeleteOne(filter);
      ```

  - id: go
    content: |
      (Code example not available offline: /driver-examples/go_examples.go)


## Delete a Document with MongoDB Atlas

**Note:**

You can delete only one document at a time in the MongoDB Atlas UI.
To delete multiple documents, connect to your 
Atlas deployment from `mongosh` or a MongoDB driver
and follow the examples on this page for your preferred method.

The example in this section uses the sample movies dataset. To learn how to load the sample dataset 
into your MongoDB Atlas deployment, see Load Sample Data.

To delete a document in MongoDB Atlas, follow these steps:

**Step 1: In the MongoDB Atlas UI, go to the Clusters page for your project.**

a. If it's not already displayed, select the organization that
   contains your desired project from the `office` Organizations menu in the
   navigation bar.

#. If it's not already displayed, select your project
   from the Projects menu in the navigation bar.

#. In the sidebar, click Clusters under 
   the Database heading.

   The [Clusters](https://cloud.mongodb.com/go?l=https%3A%2F%2Fcloud.mongodb.com%2Fv2%2F%3Cproject%3E%23%2Fclusters) page displays.

**Step 2: Navigate to the collection.**

a. For the cluster that contains the sample data,
   click Browse Collections.
#. In the left navigation pane, select the
   `sample_mflix` database.
#. Select the `movies` collection.

**Step 3: Specify a query filter document.**

Optionally, you can specify a query filter document
in the Filter field. A query filter document uses 
query operators to specify search conditions.

Copy the following query filter document into the 
Filter search bar and click Apply:

```javascript
{ genres: "Action", rated: { $in: [ "PG", "PG-13" ] } }
```

This query filter returns all documents in the `sample_mflix.movies` 
collection where `genres` equals `Action` and `rated` equals either 
`PG` or `PG-13`.

**Step 4: Delete a document.**

a. For the document that you want to delete, hover over
   the document and click the trash icon that 
   appears on the right-hand side.

   After clicking the delete button, MongoDB Atlas flags
   the document for deletion and asks for your confirmation.

#. Click Delete to confirm your selection.

To learn more, see Create, View, Update, and Delete Documents.


## Delete Behavior

### Indexes

Delete operations do not drop indexes, even if deleting all documents
from a collection.

**Note:** Atomicity and Write Acknowledgement

MongoDB write operations are atomic on the level of a single document. 
For more information, see transactions-write-atomicity. 

You can also use write concerns to specify the level of acknowledgment 
requested from MongoDB for write operations. For more information, 
see write-concern.

tabs:
  - id: shell
    content: |

      **See also:**

      - `db.collection.deleteMany()`

      - `db.collection.deleteOne()`

      - additional-deletes

  - id: compass
    content: |

      **See also:**

      - `Compass Documents`

      - Compass Query Bar

  - id: c
    content: |

      **See also:**

      - [mongoc_collection_delete_one](https://mongoc.org/libmongoc/current/mongoc_collection_delete_one.html)

      - [mongoc_collection_delete_many](https://mongoc.org/libmongoc/current/mongoc_collection_delete_many.html)

      - additional-deletes

  - id: python
    content: |

      **See also:**

      - `pymongo.collection.Collection.delete_many`

      - `pymongo.collection.Collection.delete_one`

      - additional-deletes

  - id: motor
    content: |

      **See also:**

      - `motor.motor_asyncio.AsyncIOMotorCollection.delete_many`

      - `motor.motor_asyncio.AsyncIOMotorCollection.delete_one`

      - additional-deletes

  - id: java-sync
    content: |

       **See also:**

       - com.mongodb.client.MongoCollection.deleteMany_

       - com.mongodb.client.MongoCollection.deleteOne_

       - Additional Java Synchronous Driver Write Examples

  - id: java-async
    content: |

       **See also:**

       - [com.mongodb.reactivestreams.client.MongoCollection.deleteMany](http://mongodb.github.io/mongo-java-driver-reactivestreams/1.6/javadoc/com/mongodb/reactivestreams/client/MongoCollection.html#deleteMany(org.bson.conversions.Bson))

       - [com.mongodb.reactivestreams.client.MongoCollection.deleteOne](http://mongodb.github.io/mongo-java-driver-reactivestreams/1.6/javadoc/com/mongodb/reactivestreams/client/MongoCollection.html#deleteOne(org.bson.conversions.Bson))

       - [Java Reactive Streams Driver Quick Tour](http://mongodb.github.io/mongo-java-driver-reactivestreams/1.6/getting-started/quick-tour/)

  - id: kotlin-coroutine
    content: |

       **See also:**

       - [MongoCollection.deleteOne()](https://mongodb.github.io/mongo-java-driver/{+java-driver-version+}/apidocs/driver-kotlin-coroutine/mongodb-driver-kotlin-coroutine/com.mongodb.kotlin.client.coroutine/-mongo-collection/delete-one.html)

       - [MongoCollection.deleteMany()](https://mongodb.github.io/mongo-java-driver/{+java-driver-version+}/apidocs/driver-kotlin-coroutine/mongodb-driver-kotlin-coroutine/com.mongodb.kotlin.client.coroutine/-mongo-collection/delete-many.html)

       - `Kotlin Coroutine Driver Delete Documents Guide`

  - id: nodejs
    content: |

      **See also:**

      - `Collection.deleteMany()`

      - `Collection.deleteOne()`

      - additional-deletes

  - id: php
    content: |

      **See also:**

      - `MongoDBCollection::deleteMany()`

      - `MongoDBCollection::deleteOne()`

      - additional-deletes

  - id: ruby
    content: |

      **See also:**

      - `Mongo::Collection#delete_many()`

      - `Mongo::Collection#delete_one()`

  - id: scala
    content: |

      **See also:**

      - `collection.deleteMany()`

      - `collection.deleteOne()`

      - additional-deletes

  - id: csharp
    content: |

      **See also:**

      - `IMongoCollection.DeleteMany()`

      - `IMongoCollection.DeleteOne()`

      - additional-deletes

  - id: go
    content: |

      **See also:**

      - `Collection.DeleteMany`

      - `Collection.DeleteOne`

      - additional-deletes
