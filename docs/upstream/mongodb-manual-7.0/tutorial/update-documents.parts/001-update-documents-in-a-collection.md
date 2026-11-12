<!-- Part 1 of 2 of tutorial/update-documents.md (split because the page is big). -->

## Update Documents in a Collection

**shell:**

To update a document, MongoDB provides
field-update-operators, such
as `$set`, to modify field values.

To use the update operators, pass to the update methods an
update document of the form:

```javascript
{
  <update operator>: { <field1>: <value1>, ... },
  <update operator>: { <field2>: <value2>, ... },
  ...
}
```

Some update operators, such as `$set`, will create the field if
the field does not exist. See the individual update operator reference for details.

**compass:**

To update a document in Compass, hover over the target
document and click the pencil icon:

(Figure: /images/compass-update-doc-button.png)

After clicking the pencil icon, the document enters edit mode:

(Figure: /images/compass-update-edit-mode.png)

You can now change the this document by clicking the item you wish
to change and modifying the value.

For detailed instructions on updating documents in Compass,
refer to the
Compass documentation
or follow the example below.

Once you are satisfied with your changes, click
Update to save the updated document.

Click Cancel to revert any modifications made to
the document and exit edit mode.

**c:**

To update a document, MongoDB provides
update operators such as `$set` to modify field values.

To use the update operators, pass an update document
with the following form to the update methods:

```c
{
  <update operator>: { <field1>: <value1>, ... },
  <update operator>: { <field2>: <value2>, ... },
  ...
}
```

Some update operators, such as `$set`, will create the field if
the field does not exist. See the individual update operator reference for details.

**python:**

To update a document, MongoDB provides
field-update-operators such
as `$set` to modify field values.

To use the update operators, pass to the update methods an
update document of the form:

```python
{
  <update operator>: { <field1>: <value1>, ... },
  <update operator>: { <field2>: <value2>, ... },
  ...
}
```

Some update operators, such as `$set`, will create the field if
the field does not exist. See the individual update operator reference for details.

**motor:**

To update a document, MongoDB provides
field-update-operators such
as `$set` to modify field values.

To use the update operators, pass to the update methods an
update document of the form:

```python
{
  <update operator>: { <field1>: <value1>, ... },
  <update operator>: { <field2>: <value2>, ... },
  ...
}
```

Some update operators, such as `$set`, will create the field if
the field does not exist. See the individual update operator reference for details.

**java-sync:**

To update a document, MongoDB provides
field-update-operators such
as `$set` to modify field values.

The driver provides the [com.mongodb.client.model.Updates](http://mongodb.github.io/mongo-java-driver/3.4/javadoc/com/mongodb/client/model/Updates.html)
class to facilitate the creation of update documents. For example:

```java
combine(set( <field1>, <value1>), set(<field2>, <value2> ) )
```

For a list of the update helpers, see
[com.mongodb.client.model.Updates](http://mongodb.github.io/mongo-java-driver/3.4/javadoc/com/mongodb/client/model/Updates.html).

Some update operators, such as `$set`, will create the field if
the field does not exist. See the individual update operator reference for details.

**java-async:**

To update a document, MongoDB provides
field-update-operators such
as `$set` to modify field values.

The driver provides the [com.mongodb.client.model.Updates](http://mongodb.github.io/mongo-java-driver/3.4/javadoc/com/mongodb/client/model/Updates.html)
class to facilitate the creation of update documents. For example:

```java
combine(set( <field1>, <value1>), set(<field2>, <value2> ) )
```

For a list of the update helpers, see
[com.mongodb.client.model.Updates](http://mongodb.github.io/mongo-java-driver/3.4/javadoc/com/mongodb/client/model/Updates.html).

Some update operators, such as `$set`, will create the field if
the field does not exist. See the individual update operator reference for details.

**kotlin-coroutine:**

To update a document, MongoDB provides
update operators such
as `$set` to modify field values.

The driver provides the [com.mongodb.client.model.Updates](https://mongodb.github.io/mongo-java-driver/{+java-driver-version+}/apidocs/driver-core/com/mongodb/client/model/Updates.html)
class to facilitate the creation of update documents. The
following code shows an update document that uses methods
from the `Updates` builder class:

```kotlin
combine(set(<field1>, <value1>), set(<field2>, <value2>))
```

Some update operators, such as `$set`, will create the field if
the field does not exist. See the individual update operator reference for details.

**nodejs:**

To update a document, MongoDB provides
field-update-operators such
as `$set` to modify field values.

To use the update operators, pass to the update methods an
update document of the form:

```javascript
{
  <update operator>: { <field1>: <value1>, ... },
  <update operator>: { <field2>: <value2>, ... },
  ...
}
```

Some update operators, such as `$set`, will create the field if
the field does not exist. See the individual update operator reference for details.

**php:**

To update a document, MongoDB provides
field-update-operators such
as `$set` to modify field values.

To use the update operators, pass to the update methods an
update document of the form:

```php
[
  <update operator> => [ <field1> => <value1>, ... ],
  <update operator> => [ <field2> => <value2>, ... ],
  ...
]
```

Some update operators, such as `$set`, will create the field if
the field does not exist. See the individual update operator reference for details.

**ruby:**

To update a document, MongoDB provides
field-update-operators such
as `$set` to modify field values.

To use the update operators, pass to the update methods an
update document of the form:

```ruby
{
  <update operator> => { <field1> => <value1>, ... },
  <update operator> => { <field2> => <value2>, ... },
  ...
}
```

Some update operators, such as `$set`, will create the field if
the field does not exist. See the individual update operator reference for details.

**csharp:**

To update a document, MongoDB provides
field-update-operators such
as `$set` to modify field values.

To use the update operators, pass to the update methods an
update document of the form:

```csharp
{
  <update operator> => { <field1> => <value1>, ... },
  <update operator> => { <field2> => <value2>, ... },
  ...
}
```

Some update operators, such as `$set`, will create the field if
the field does not exist. See the individual update operator reference for details.

**scala:**

To update a document, MongoDB provides
field-update-operators such
as `$set` to modify field values.

To use the update operators, pass to the update methods an
update document of the form:

```scala
(
  set (<field1>, <value1>),
  set (<field2>, <value2>),
  ...
)
```

Some update operators, such as `$set`, will create the field if
the field does not exist. See the individual update operator reference for details.

**go:**

To update a document, MongoDB provides
field-update-operators such
as `$set` to modify field values.

Some update operators, such as `$set`, will create the field if
the field does not exist. See the individual update operator reference for details.

   

### Update a Single Document

**shell:**

The following example uses the
`db.collection.updateOne()` method on the
`movies` collection to update the *first* document where
`title` equals `"The Godfather"`:

**compass:**

The following example demonstrates using MongoDB Compass to modify
a single document where `item: paper` in the `inventory`
collection:

**Note:**

This example uses the Compass
Table View to modify the
document. The editing process using the Compass
List View follows a similar 
approach.

For more information on the differences between Table View
and List View in Compass, refer to the
Compass documentation.

**c:**

The following example uses the
[mongoc_collection_update_one](https://mongoc.org/libmongoc/current/mongoc_collection_update_one.html)
function on the `inventory` collection to update the *first* document
where `item` equals `"paper"`:

**python:**

The following example uses the
`update_one` method on
the `inventory` collection to update the *first* document
where `item` equals `"paper"`:

**motor:**

The following example uses the
`update_one`
method on the `inventory` collection to update the *first*
document where `item` equals `"paper"`:

**java-sync:**

The following example uses the
com.mongodb.client.MongoCollection.updateOne_ method on the
`inventory` collection to update the *first* document where
`item` equals `"paper"`:

**java-async:**

The following example uses the
[com.mongodb.reactivestreams.client.MongoCollection.updateOne](http://mongodb.github.io/mongo-java-driver-reactivestreams/1.6/javadoc/com/mongodb/reactivestreams/client/MongoCollection.html#updateOne(org.bson.conversions.Bson,%20org.bson.conversions.Bson))
on the `inventory` collection to update the *first* document
where `item` equals `"paper"`:

**kotlin-coroutine:**

The following example uses the
[MongoCollection.updateOne()](https://mongodb.github.io/mongo-java-driver/{+java-driver-version+}/apidocs/driver-kotlin-coroutine/mongodb-driver-kotlin-coroutine/com.mongodb.kotlin.client.coroutine/-mongo-collection/update-one.html)
method on the `inventory` collection to update the *first*
document where `item` equals `"paper"`:

**nodejs:**

The following example uses the
`Collection.updateOne()`
method on the `inventory` collection to update the *first*
document where `item` equals `"paper"`:

**php:**

The following example uses the `updateOne()` method on the
`inventory` collection to update the *first* document where
`item` equals `"paper"`:

**ruby:**

The following example uses the
`update_one()`
method on the `inventory` collection to update the *first*
document where `item` equals `"paper"`:

**scala:**

The following example uses the
`updateOne()`
method on the `inventory` collection to update the *first*
document where `item` equals `"paper"`:

**csharp:**

The following example uses the
`IMongoCollection.UpdateOne()` method on the
`inventory` collection to update the *first* document where
`item` equals `"paper"`:

**go:**

The following example uses the
`Collection.UpdateOne` method
on the `inventory` collection to update the *first* document
where `item` equals `"paper"`:

tabs:
  - id: shell
    content: |

      ```javascript
      db.movies.updateOne(
         { title: "The Godfather" },
         {
           $set: { rated: "PG", "tomatoes.viewer.rating": 4.5 },
           $currentDate: { lastupdated: true }
         }
      )
      ```

      The update operation:

      - uses the `$set` operator to update the value of the
        `size.uom` field to `"cm"` and the value of the `status`
        field to `"P"`,

      - uses the `$currentDate` operator to update the value
        of the `lastModified` field to the current date. If
        `lastModified` field does not exist,
        `$currentDate` will create the field. See
        `$currentDate` for details.

  - id: compass
    content: |
      Modify the target document as follows:

      - Change the `status` field from `D` to `P`.

      - Change the `size.uom` field from `in` to `cm`.

      - Add a new field called `lastModified` whose value will
        be today's date.

      1. Click the Table button in the top navigation
         to access the Table View:

         (Figure: /images/compass-table-btn-click.png)

      #. Use the Compass query bar to
         locate the target document.

         Copy the following filter document into the query bar and click
         Find:

         ```javascript
         { item: "paper" }
         ```

         (Figure: /images/compass-update-paper-filter.png)

      #. Hover over the `status` field and click the pencil icon
         which appears on the right side of the document to enter
         edit mode:

         (Figure: /images/compass-edit-paper-example.png)

      #. Change the value of the field to `"P"`.

      #. Click the Update button below the field to
         save your changes.

      #. Hover over the `size` field and click the
         outward-pointing arrows which appear on the right side of
         the field. This opens a new tab which displays the fields
         within the `size` object:

         (Figure: /images/compass-edit-paper-expand.png)

      #. Using the same process outlined in steps 3-5 for editing the
         `status` field, change the value of the `size.uom` field
         to `"cm"`.

      #. Click the left-most tab above the table labelled
         `inventory` to return to the original table view, which
         displays the top-level document:

         (Figure: /images/compass-edit-inv-tab-click.png)

      #. Hover over the `status` field and click the pencil icon
         which appears on the right side of the document to re-enter
         edit mode.

      #. Click inside of the `status` field and click the
         plus button icon which appears in the edit menu.

         Click the Add Field After status button which
         appears below the plus button:

         (Figure: /images/compass-edit-paper-add-field-after.png)

      #. Add a new field called `lastModified` with a value of
         today's date. Set the field type to `Date`:

         (Figure: /images/compass-edit-paper-add-last-modified.png)

      #. Click the Update button below the field to
         save your changes.

         **Note:**

         Because MongoDB Compass does not support
         `$currentDate` or any other
         Field Update Operators,
         you must manually enter the date value in Compass.

  - id: c
    content: |

      (Code example not available offline: /driver-examples/test-mongoc-sample-commands.c)

  - id: python
    content: |

      (Code example not available offline: /driver-examples/test_examples.py)

  - id: motor
    content: |

      (Code example not available offline: /driver-examples/test_examples_motor.py)

      The update operation:

      - uses the `$set` operator to update the value of the
        `size.uom` field to `"cm"` and the value of the `status`
        field to `"P"`,

      - uses the `$currentDate` operator to update the value
        of the `lastModified` field to the current date. If
        `lastModified` field does not exist,
        `$currentDate` will create the field. See
        `$currentDate` for details.

  - id: java-sync
    content: |

      (Code example not available offline: /driver-examples/DocumentationSamples.java)

      The update operation:

      - uses the `$set` operator to update the value of the
        `size.uom` field to `"cm"` and the value of the `status`
        field to `"P"`,

      - uses the `$currentDate` operator to update the value
        of the `lastModified` field to the current date. If
        `lastModified` field does not exist,
        `$currentDate` will create the field. See
        `$currentDate` for details.

  - id: java-async
    content: |

      (Code example not available offline: /driver-examples/AsyncDocumentationSamples.java)

      The update operation:

      - uses the `$set` operator to update the value of the
        `size.uom` field to `"cm"` and the value of the `status`
        field to `"P"`,

      - uses the `$currentDate` operator to update the value
        of the `lastModified` field to the current date. If
        `lastModified` field does not exist,
        `$currentDate` will create the field. See
        `$currentDate` for details.

  - id: kotlin-coroutine
    content: |

      (Code example not available offline: /driver-examples/kotlin_examples.kt)

      The update operation:

      - uses the `$set` operator to update the value of the
        `size.uom` field to `"cm"` and the value of the `status`
        field to `"P"`,

      - uses the `$currentDate` operator to update the value
        of the `lastModified` field to the current date. If
        `lastModified` field does not exist,
        `$currentDate` will create the field. See
        `$currentDate` for details.

  - id: nodejs
    content: |
      (Code example not available offline: /driver-examples/node_update.js)

      The update operation:

      - uses the `$set` operator to update the value of the
        `size.uom` field to `"cm"` and the value of the `status`
        field to `"P"`,

      - uses the `$currentDate` operator to update the value
        of the `lastModified` field to the current date. If
        `lastModified` field does not exist,
        `$currentDate` will create the field. See
        `$currentDate` for details.

  - id: php
    content: |

      (Code example not available offline: /driver-examples/DocumentationExamplesTest.php)

      The update operation:

      - uses the `$set` operator to update the value of the
        `size.uom` field to `"cm"` and the value of the `status`
        field to `"P"`,

      - uses the `$currentDate` operator to update the value
        of the `lastModified` field to the current date. If
        `lastModified` field does not exist,
        `$currentDate` will create the field. See
        `$currentDate` for details.

  - id: ruby
    content: |

      (Code example not available offline: /driver-examples/shell_examples_spec.rb)

      The update operation:

      - uses the `$set` operator to update the value of the
        `size.uom` field to `"cm"` and the value of the `status`
        field to `"P"`,

      - uses the `$currentDate` operator to update the value
        of the `lastModified` field to the current date. If
        `lastModified` field does not exist,
        `$currentDate` will create the field. See
        `$currentDate` for details.

  - id: scala
    content: |

      (Code example not available offline: /driver-examples/DocumentationExampleSpec.scala)

      The update operation:

      - uses the `$set` operator to update the value of the
        `size.uom` field to `"cm"` and the value of the `status`
        field to `"P"`,

      - uses the `$currentDate` operator to update the value
        of the `lastModified` field to the current date. If
        `lastModified` field does not exist,
        `$currentDate` will create the field. See
        `$currentDate` for details.

  - id: csharp
    content: |

      ```csharp
      var filter = Builders<BsonDocument>.Filter.Eq("item", "paper");
      var update = Builders<BsonDocument>.Update.Set("size.uom", "cm").Set("status", "P").CurrentDate("lastModified");
      var result = collection.UpdateOne(filter, update);
      ```

      The update operation:

      - uses the `$set` operator to update the value of the
        `size.uom` field to `"cm"` and the value of the `status`
        field to `"P"`,

      - uses the `$currentDate` operator to update the value
        of the `lastModified` field to the current date. If
        `lastModified` field does not exist,
        `$currentDate` will create the field. See
        `$currentDate` for details.

  - id: go
    content: |
      (Code example not available offline: /driver-examples/go_examples.go)

      The update operation:

      - uses the `$set` operator to update the value of the
        `size.uom` field to `"cm"` and the value of the `status`
        field to `"P"`,

      - uses the `$currentDate` operator to update the value
        of the `lastModified` field to the current date. If
        `lastModified` field does not exist,
        `$currentDate` will create the field. See
        `$currentDate` for details.

### Update Multiple Documents

**compass:**

You can update only one document at a time in MongoDB Compass.

**shell:**

The following example uses the
`db.collection.updateMany()` method on the `movies`
collection to update all documents where `num_mflix_comments` is greater than
`100`:

**c:**

The following example uses the
[mongoc_collection_update_many](https://mongoc.org/libmongoc/current/mongoc_collection_update_many.html)
function on the `inventory` collection to update all documents where `qty`
is less than `50`:

**python:**

The following example uses the
`update_many` method on
the `inventory` collection to update all documents where `qty`
is less than `50`:

**motor:**

The following example uses the
`update_many`
method on the `inventory` collection to update all documents
where `qty` is less than `50`:

**java-sync:**

The following example uses the
com.mongodb.client.MongoCollection.updateMany_ method on
the `inventory` collection to update all documents where
`qty` is less than `50`:

**java-async:**

The following example uses the
[com.mongodb.reactivestreams.client.MongoCollection.updateMany](http://mongodb.github.io/mongo-java-driver-reactivestreams/1.6/javadoc/com/mongodb/reactivestreams/client/MongoCollection.html#updateMany(org.bson.conversions.Bson,%20org.bson.conversions.Bson))
method on the `inventory` collection to update all documents
where `qty` is less than `50`:

**kotlin-coroutine:**

The following example uses the
[MongoCollection.updateMany()](https://mongodb.github.io/mongo-java-driver/{+java-driver-version+}/apidocs/driver-kotlin-coroutine/mongodb-driver-kotlin-coroutine/com.mongodb.kotlin.client.coroutine/-mongo-collection/update-many.html)
method on the `inventory` collection to update all documents
where `qty` is less than `50`:

**nodejs:**

The following example uses the `Collection.updateMany()` method on the `inventory`
collection to update all documents where `qty` is less than
`50`:

**php:**

The following example uses the `updateMany()` method on the
`inventory` collection to update all documents where `qty` is
less than `50`:

**ruby:**

The following example uses the
`update_many()`
method on the `inventory` collection to update all documents
where `qty` is less than `50`:

**scala:**

The following example uses the
`updateMany()`
method on the `inventory` collection to update all documents
where `qty` is less than `50`:

**csharp:**

The following example uses the
`IMongoCollection.UpdateMany()` method on the
`inventory` collection to update all documents where `qty` is
less than `50`:

**go:**

The following example uses the
`Collection.UpdateMany`
method on the `inventory` collection to update all documents
where `qty` is less than `50`:

tabs:
  - id: shell
    content: |

      ```javascript
      db.movies.updateMany(
         { "num_mflix_comments": { $gt: 100 } },
         {
           $set: { popular: true },
           $currentDate: { lastupdated: true }
         }
      )
      ```

  - id: compass
    content: |

      To update multiple documents, connect to your 
      MongoDB deployment from `mongosh` or a MongoDB driver
      and follow the examples in this section for your preferred method.

  - id: c
    content: |

      (Code example not available offline: /driver-examples/test-mongoc-sample-commands.c)

  - id: python
    content: |

      (Code example not available offline: /driver-examples/test_examples.py)

  - id: motor
    content: |

      (Code example not available offline: /driver-examples/test_examples_motor.py)

      The update operation:

      - uses the `$set` operator to update the value of the
        `size.uom` field to `"in"` and the value of the `status`
        field to `"P"`,

      - uses the `$currentDate` operator to update the value
        of the `lastModified` field to the current date. If
        `lastModified` field does not exist,
        `$currentDate` will create the field. See
        `$currentDate` for details.

  - id: java-sync
    content: |

      (Code example not available offline: /driver-examples/DocumentationSamples.java)

      The update operation:

      - uses the `$set` operator to update the value of the
        `size.uom` field to `"in"` and the value of the `status`
        field to `"P"`,

      - uses the `$currentDate` operator to update the value
        of the `lastModified` field to the current date. If
        `lastModified` field does not exist,
        `$currentDate` will create the field. See
        `$currentDate` for details.

  - id: java-async
    content: |

      (Code example not available offline: /driver-examples/AsyncDocumentationSamples.java)

      The update operation:

      - uses the `$set` operator to update the value of the
        `size.uom` field to `"in"` and the value of the `status`
        field to `"P"`,

      - uses the `$currentDate` operator to update the value
        of the `lastModified` field to the current date. If
        `lastModified` field does not exist,
        `$currentDate` will create the field. See
        `$currentDate` for details.

  - id: kotlin-coroutine
    content: |

      (Code example not available offline: /driver-examples/kotlin_examples.kt)

      The update operation:

      - uses the `$set` operator to update the value of the
        `size.uom` field to `"in"` and the value of the `status`
        field to `"P"`,

      - uses the `$currentDate` operator to update the value
        of the `lastModified` field to the current date. If
        `lastModified` field does not exist,
        `$currentDate` will create the field. See
        `$currentDate` for details.

  - id: nodejs
    content: |
      (Code example not available offline: /driver-examples/node_update.js)

      The update operation:

      - uses the `$set` operator to update the value of the
        `size.uom` field to `"in"` and the value of the `status`
        field to `"P"`,

      - uses the `$currentDate` operator to update the value
        of the `lastModified` field to the current date. If
        `lastModified` field does not exist,
        `$currentDate` will create the field. See
        `$currentDate` for details.

  - id: php
    content: |

      (Code example not available offline: /driver-examples/DocumentationExamplesTest.php)

      The update operation:

      - uses the `$set` operator to update the value of the
        `size.uom` field to `"in"` and the value of the `status`
        field to `"P"`,

      - uses the `$currentDate` operator to update the value
        of the `lastModified` field to the current date. If
        `lastModified` field does not exist,
        `$currentDate` will create the field. See
        `$currentDate` for details.

  - id: ruby
    content: |

      (Code example not available offline: /driver-examples/shell_examples_spec.rb)

      The update operation:

      - uses the `$set` operator to update the value of the
        `size.uom` field to `"in"` and the value of the `status`
        field to `"P"`,

      - uses the `$currentDate` operator to update the value
        of the `lastModified` field to the current date. If
        `lastModified` field does not exist,
        `$currentDate` will create the field. See
        `$currentDate` for details.

  - id: scala
    content: |

      (Code example not available offline: /driver-examples/DocumentationExampleSpec.scala)

      The update operation:

      - uses the `$set` operator to update the value of the
        `size.uom` field to `"in"` and the value of the `status`
        field to `"P"`,

      - uses the `$currentDate` operator to update the value
        of the `lastModified` field to the current date. If
        `lastModified` field does not exist,
        `$currentDate` will create the field. See
        `$currentDate` for details.

  - id: csharp
    content: |

      ```csharp
      var filter = Builders<BsonDocument>.Filter.Lt("qty", 50);
      var update = Builders<BsonDocument>.Update.Set("size.uom", "in").Set("status", "P").CurrentDate("lastModified");
      var result = collection.UpdateMany(filter, update);
      ```

      The update operation:

      - uses the `$set` operator to update the value of the
        `size.uom` field to `"in"` and the value of the `status`
        field to `"P"`,

      - uses the `$currentDate` operator to update the value
        of the `lastModified` field to the current date. If
        `lastModified` field does not exist,
        `$currentDate` will create the field. See
        `$currentDate` for details.

  - id: go
    content: |
      (Code example not available offline: /driver-examples/go_examples.go)

      The update operation:

      - uses the `$set` operator to update the value of the
        `size.uom` field to `"in"` and the value of the `status`
        field to `"P"`,

      - uses the `$currentDate` operator to update the value
        of the `lastModified` field to the current date. If
        `lastModified` field does not exist,
        `$currentDate` will create the field. See
        `$currentDate` for details.

### Replace a Document

**compass:**

You can't replace a document in MongoDB Compass.

**shell:**

To replace the entire content of a document except for the `_id`
field, pass an entirely new document as the second argument to
`db.collection.replaceOne()`.

When replacing a document, the replacement document must consist of only
field/value pairs. The replacement document cannot include 
update operators expressions.

The replacement document can have different fields from the original
document. In the replacement document, you can omit the `_id` field
since the `_id` field is immutable. However, if you do include the
`_id` field, it must have the same value as the current value.

The following example replaces the *first* document from the
`movies` collection where `title: "The Godfather"`:

**c:**

To replace the entire content of a document except for the `_id`
field, pass an entirely new document as the third argument to
[mongoc_collection_replace_one](https://mongoc.org/libmongoc/current/mongoc_collection_replace_one.html).

When replacing a document, the replacement document must consist of only
field/value pairs. The replacement document cannot include 
update operators expressions.

The replacement document can have different fields from the original
document. In the replacement document, you can omit the `_id` field
since the `_id` field is immutable. However, if you do include the
`_id` field, it must have the same value as the current value.

The following example replaces the *first* document from the
`inventory` collection where `item: "paper"`:

**python:**

To replace the entire content of a document except for the `_id`
field, pass an entirely new document as the second argument to
`replace_one`.

When replacing a document, the replacement document must consist of only
field/value pairs. The replacement document cannot include 
update operators expressions.

The replacement document can have different fields from the original
document. In the replacement document, you can omit the `_id` field
since the `_id` field is immutable. However, if you do include the
`_id` field, it must have the same value as the current value.

The following example replaces the *first* document from the
`inventory` collection where `item: "paper"`:

**motor:**

To replace the entire content of a document except for the `_id`
field, pass an entirely new document as the second argument to
`replace_one`.

When replacing a document, the replacement document must consist of only
field/value pairs. The replacement document cannot include 
update operators expressions.

The replacement document can have different fields from the original
document. In the replacement document, you can omit the `_id` field
since the `_id` field is immutable. However, if you do include the
`_id` field, it must have the same value as the current value.

The following example replaces the *first* document from the
`inventory` collection where `item: "paper"`:

**java-sync:**

To replace the entire content of a document except for the `_id`
field, pass an entirely new document as the second argument to
com.mongodb.client.MongoCollection.replaceOne_.

When replacing a document, the replacement document must consist of only
field/value pairs. The replacement document cannot include 
update operators expressions.

The replacement document can have different fields from the original
document. In the replacement document, you can omit the `_id` field
since the `_id` field is immutable. However, if you do include the
`_id` field, it must have the same value as the current value.

The following example replaces the *first* document from the
`inventory` collection where `item: "paper"`:

**java-async:**

To replace the entire content of a document except for the `_id`
field, pass an entirely new document as the second argument to
[com.mongodb.reactivestreams.client.MongoCollection.replaceOne](http://mongodb.github.io/mongo-java-driver-reactivestreams/1.6/javadoc/com/mongodb/reactivestreams/client/MongoCollection.html#replaceOne(org.bson.conversions.Bson,%20TDocument)).

When replacing a document, the replacement document must consist of only
field/value pairs. The replacement document cannot include 
update operators expressions.

The replacement document can have different fields from the original
document. In the replacement document, you can omit the `_id` field
since the `_id` field is immutable. However, if you do include the
`_id` field, it must have the same value as the current value.

The following example replaces the *first* document from the
`inventory` collection where `item: "paper"`:

**kotlin-coroutine:**

To replace the entire content of a document except for the `_id`
field, pass an entirely new document as the second argument to
the [MongoCollection.replaceOne()](https://mongodb.github.io/mongo-java-driver/{+java-driver-version+}/apidocs/driver-kotlin-coroutine/mongodb-driver-kotlin-coroutine/com.mongodb.kotlin.client.coroutine/-mongo-collection/replace-one.html) method.

When replacing a document, the replacement document must consist of only
field/value pairs. The replacement document cannot include 
update operators expressions.

The replacement document can have different fields from the original
document. In the replacement document, you can omit the `_id` field
since the `_id` field is immutable. However, if you do include the
`_id` field, it must have the same value as the current value.

The following example replaces the *first* document from the
`inventory` collection where `item: "paper"`:

**nodejs:**

To replace the entire content of a document except for the
`_id` field, pass an entirely new document as the second
argument to
`Collection.replaceOne()`.

When replacing a document, the replacement document must consist of only
field/value pairs. The replacement document cannot include 
update operators expressions.

The replacement document can have different fields from the original
document. In the replacement document, you can omit the `_id` field
since the `_id` field is immutable. However, if you do include the
`_id` field, it must have the same value as the current value.

The following example replaces the *first* document from the
`inventory` collection where `item: "paper"`:

**php:**

To replace the entire content of a document except for the `_id`
field, pass an entirely new document as the second argument to
`replaceOne()`.

When replacing a document, the replacement document must consist of only
field/value pairs. The replacement document cannot include 
update operators expressions.

The replacement document can have different fields from the original
document. In the replacement document, you can omit the `_id` field
since the `_id` field is immutable. However, if you do include the
`_id` field, it must have the same value as the current value.

The following example replaces the *first* document from the
`inventory` collection where `item: "paper"`:

**ruby:**

To replace the entire content of a document except for the `_id`
field, pass an entirely new document as the second argument to
`replace_one()`.

When replacing a document, the replacement document must consist of only
field/value pairs. The replacement document cannot include 
update operators expressions.

The replacement document can have different fields from the original
document. In the replacement document, you can omit the `_id` field
since the `_id` field is immutable. However, if you do include the
`_id` field, it must have the same value as the current value.

The following example replaces the *first* document from the
`inventory` collection where `item: "paper"`:

**scala:**

To replace the entire content of a document except for the `_id`
field, pass an entirely new document as the second argument to
`replaceOne()`

When replacing a document, the replacement document must consist of only
field/value pairs. The replacement document cannot include 
update operators expressions.

The replacement document can have different fields from the original
document. In the replacement document, you can omit the `_id` field
since the `_id` field is immutable. However, if you do include the
`_id` field, it must have the same value as the current value.

The following example replaces the *first* document from the
`inventory` collection where `item: "paper"`:

**csharp:**

To replace the entire content of a document except for the `_id`
field, pass an entirely new document as the second argument to
`IMongoCollection.ReplaceOne()`.

When replacing a document, the replacement document must consist of only
field/value pairs. The replacement document cannot include 
update operators expressions.

The replacement document can have different fields from the original
document. In the replacement document, you can omit the `_id` field
since the `_id` field is immutable. However, if you do include the
`_id` field, it must have the same value as the current value.

The following example replaces the *first* document from the
`inventory` collection where `item: "paper"`:

**go:**

To replace the entire content of a document except for the `_id`
field, pass an entirely new document as the second argument to
`Collection.ReplaceOne`.

When replacing a document, the replacement document must consist of only
field/value pairs. The replacement document cannot include 
update operators expressions.

The replacement document can have different fields from the original
document. In the replacement document, you can omit the `_id` field
since the `_id` field is immutable. However, if you do include the
`_id` field, it must have the same value as the current value.

The following example replaces the *first* document from the
`inventory` collection where `item: "paper"`:

tabs:
  - id: shell
    content: |

      ```javascript
      db.movies.replaceOne(
         { title: "The Godfather" },
         { title: "The Godfather", plot: "Updated plot summary", year: 1972, rated: "R", runtime: 175 }
      )
      ```

  - id: compass
    content: |

      To replace a document, connect to your 
      MongoDB deployment from `mongosh` or a MongoDB driver
      and follow the examples in this section for your preferred method.

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
      (Code example not available offline: /driver-examples/node_update.js)

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
      var filter = Builders<BsonDocument>.Filter.Eq("item", "paper");
      var replacement = new BsonDocument
      {
          { "item", "paper" },
          { "instock", new BsonArray
              {
                  new BsonDocument { { "warehouse", "A" }, { "qty", 60 } },
                  new BsonDocument { { "warehouse", "B" }, { "qty", 40 } } }
              }
      };
      var result = collection.ReplaceOne(filter, replacement);
      ```

  - id: go
    content: |
      (Code example not available offline: /driver-examples/go_examples.go)
