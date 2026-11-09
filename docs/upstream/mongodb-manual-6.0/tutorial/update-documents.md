<!-- Converted from tutorial/update-documents.txt (reStructuredText). Includes are inlined. -->

# Update Documents

You can update documents in MongoDB using the following methods:

- Your programming language's driver.
- The MongoDB Atlas UI. To learn more, see 
  update-documents-atlas-ui.
- `MongoDB Compass`.

----------

→ Use the **Select your language** drop-down menu in the
upper-right to set the language of the following examples.

----------

   `inventory` collection. Connect to a test database in your MongoDB
   instance then create the `inventory` collection:

**shell:**

This page uses the following `mongosh` methods:

- `db.collection.updateOne(<filter>, <update>, <options>)`

- `db.collection.updateMany(<filter>, <update>, <options>)`

- `db.collection.replaceOne(<filter>, <update>, <options>)`

The examples on this page use the

**compass:**

This page uses MongoDB Compass to
update the documents.

The examples on this page use the `inventory` collection.
Populate the `inventory` collection with the following
documents:

**python:**

This page uses the following
[PyMongo](https://pymongo.readthedocs.io/en/stable/index.html)
Python driver methods:

- `pymongo.collection.Collection.update_one`

- `pymongo.collection.Collection.update_many`

- `pymongo.collection.Collection.replace_one`

The examples on this page use the

**motor:**

This page uses the
following [Motor](https://motor.readthedocs.io/en/stable/)
driver methods:

- `motor.motor_asyncio.AsyncIOMotorCollection.update_one`

- `motor.motor_asyncio.AsyncIOMotorCollection.update_many`

- `motor.motor_asyncio.AsyncIOMotorCollection.replace_one`

The examples on this page use the

**java-sync:**

This page uses the
following Java Synchronous Driver methods:

- com.mongodb.client.MongoCollection.updateOne_

- com.mongodb.client.MongoCollection.updateMany_

- com.mongodb.client.MongoCollection.replaceOne_

The examples on this page use the

**java-async:**

This page uses the
following [Java Reactive Streams Driver](http://mongodb.github.io/mongo-java-driver-reactivestreams/1.6/) methods:

- [com.mongodb.reactivestreams.client.MongoCollection.updateOne](http://mongodb.github.io/mongo-java-driver-reactivestreams/1.6/javadoc/com/mongodb/reactivestreams/client/MongoCollection.html#updateOne(org.bson.conversions.Bson,%20org.bson.conversions.Bson))

- [com.mongodb.reactivestreams.client.MongoCollection.updateMany](http://mongodb.github.io/mongo-java-driver-reactivestreams/1.6/javadoc/com/mongodb/reactivestreams/client/MongoCollection.html#updateMany(org.bson.conversions.Bson,%20org.bson.conversions.Bson))

- [com.mongodb.reactivestreams.client.MongoCollection.replaceOne](http://mongodb.github.io/mongo-java-driver-reactivestreams/1.6/javadoc/com/mongodb/reactivestreams/client/MongoCollection.html#replaceOne(org.bson.conversions.Bson,%20TDocument))

The examples on this page use the

**nodejs:**

This page uses the
following `MongoDB Node.js Driver` methods:

- `Collection.updateOne()`

- `Collection.updateMany()`

- `Collection.replaceOne()`

The examples on this page use the

**php:**

This page uses the following  [MongoDB PHP Library](https://www.mongodb.com/docs/php-library/current/) methods:

- `MongoDBCollection::updateOne()`

- `MongoDBCollection::updateMany()`

- `MongoDBCollection::replaceOne()`

The examples on this page use the

**ruby:**

This page uses the following `MongoDB Ruby Driver` methods:

- `Mongo::Collection#update_one()`

- `Mongo::Collection#update_many()`

- `Mongo::Collection#replace_one()`

The examples on this page use the

**scala:**

This page uses the following  [MongoDB Scala Driver](http://mongodb.github.io/mongo-scala-driver/) methods:

- `collection.updateOne()`

- `collection.updateMany()`

- `collection.replaceOne()`

The examples on this page use the

**csharp:**

This page uses the following `MongoDB C# Driver` methods:

- `IMongoCollection.UpdateOne()`

- `IMongoCollection.UpdateMany()`

- `IMongoCollection.ReplaceOne()`

The examples on this page use the

**go:**

This page uses the following `MongoDB Go Driver` functions:

- `Collection.UpdateOne`

- `Collection.UpdateMany`

- `Collection.ReplaceOne`

The examples on this page use the

tabs:
  - id: shell
    content: |

      ```javascript
      db.inventory.insertMany( [
         { item: "canvas", qty: 100, size: { h: 28, w: 35.5, uom: "cm" }, status: "A" },
         { item: "journal", qty: 25, size: { h: 14, w: 21, uom: "cm" }, status: "A" },
         { item: "mat", qty: 85, size: { h: 27.9, w: 35.5, uom: "cm" }, status: "A" },
         { item: "mousepad", qty: 25, size: { h: 19, w: 22.85, uom: "cm" }, status: "P" },
         { item: "notebook", qty: 50, size: { h: 8.5, w: 11, uom: "in" }, status: "P" },
         { item: "paper", qty: 100, size: { h: 8.5, w: 11, uom: "in" }, status: "D" },
         { item: "planner", qty: 75, size: { h: 22.85, w: 30, uom: "cm" }, status: "D" },
         { item: "postcard", qty: 45, size: { h: 10, w: 15.25, uom: "cm" }, status: "A" },
         { item: "sketchbook", qty: 80, size: { h: 14, w: 21, uom: "cm" }, status: "A" },
         { item: "sketch pad", qty: 95, size: { h: 22.85, w: 30.5, uom: "cm" }, status: "A" }
      ] );
      ```

  - id: compass
    content: |

      ```javascript
      [
          { "item": "canvas", "qty": 100, "size": { "h": 28, "w": 35.5, "uom": "cm" }, "status": "A" },
          { "item": "journal", "qty": 25, "size": { "h": 14, "w": 21, "uom": "cm" }, "status": "A" },
          { "item": "mat", "qty": 85, "size": { "h": 27.9, "w": 35.5, "uom": "cm" }, "status": "A" },
          { "item": "mousepad", "qty": 25, "size": { "h": 19, "w": 22.85, "uom": "cm" }, "status": "P" },
          { "item": "notebook", "qty": 50, "size": { "h": 8.5, "w": 11, "uom": "in" }, "status": "P" },
          { "item": "paper", "qty": 100, "size": { "h": 8.5, "w": 11, "uom": "in" }, "status": "D" },
          { "item": "planner", "qty": 75, "size": { "h": 22.85, "w": 30, "uom": "cm" }, "status": "D" },
          { "item": "postcard", "qty": 45, "size": { "h": 10, "w": 15.25, "uom": "cm" }, "status": "A" },
          { "item": "sketchbook", "qty": 80, "size": { "h": 14, "w": 21, "uom": "cm" }, "status": "A" },
          { "item": "sketch pad", "qty": 95, "size": { "h": 22.85, "w": 30.5, "uom": "cm" }, "status": "A" }
      ]
      ```

      For instructions on inserting documents using MongoDB Compass, see
      Insert Documents.

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

      (Code example not available offline: /driver-examples/DocumentationExamples.cs)

  - id: go
    content: |
      (Code example not available offline: /driver-examples/go_examples.go)

## Update Documents in a Collection

**shell:**

To update a document, MongoDB provides
update operators, such
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

**python:**

To update a document, MongoDB provides
update operators such
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
update operators such
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
update operators such
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
update operators such
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

**nodejs:**

To update a document, MongoDB provides
update operators such
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
update operators such
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
update operators such
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
update operators such
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
update operators such
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
update operators such
as `$set` to modify field values.

Some update operators, such as `$set`, will create the field if
the field does not exist. See the individual update operator reference for details.

**Note:**

MongoDB can accept an aggregation pipeline to specify the modifications to 
make instead of an update document. For details, see the method reference 
page.

   

### Update a Single Document

**shell:**

The following example uses the
`db.collection.updateOne()` method on the
`inventory` collection to update the *first* document where
`item` equals `"paper"`:

**compass:**

The following example demonstrates using MongoDB Compass to modify
a single document where `item: paper` in the `inventory`
collection:

**Note:**

This example uses the Compass Table View to modify the 
document. The editing process using the Compass List View 
follows a very similar approach.

For more information on the differences between Table View
and List View in Compass, refer to the
Compass documentation.

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
      db.inventory.updateOne(
         { item: "paper" },
         {
           $set: { "size.uom": "cm", status: "P" },
           $currentDate: { lastModified: true }
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

      (Code example not available offline: /driver-examples/DocumentationExamples.cs)

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
To update multiple documents, connect to your 
MongoDB deployment from `mongosh` or a MongoDB driver
and follow the examples in this section for your preferred method.

**shell:**

The following example uses the
`db.collection.updateMany()` method on the `inventory`
collection to update all documents where `qty` is less than
`50`:

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
      db.inventory.updateMany(
         { "qty": { $lt: 50 } },
         {
           $set: { "size.uom": "in", status: "P" },
           $currentDate: { lastModified: true }
         }
      )
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

      (Code example not available offline: /driver-examples/DocumentationExamples.cs)

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
To replace a document, connect to your 
MongoDB deployment from `mongosh` or a MongoDB driver
and follow the examples in this section for your preferred method.

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
      db.inventory.replaceOne(
         { item: "paper" },
         { item: "paper", instock: [ { warehouse: "A", qty: 60 }, { warehouse: "B", qty: 40 } ] }
      )
      ```

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

      (Code example not available offline: /driver-examples/DocumentationExamples.cs)

  - id: go
    content: |
      (Code example not available offline: /driver-examples/go_examples.go)

## Update a Document with MongoDB Atlas

**Note:**

You can update only one document at a time in the MongoDB Atlas UI.
To update multiple documents or replace an entire document, 
connect to your Atlas deployment from `mongosh` 
or a MongoDB driver and follow the examples on this page 
for your preferred method.

The example in this section uses the sample supplies dataset. To learn how to load the sample dataset 
into your MongoDB Atlas deployment, see Load Sample Data.

To update a document in MongoDB Atlas, follow these steps:

**Step 1: In the MongoDB Atlas UI, go to the Clusters page for your project.**

**Warning:** Navigation Improvements In Progress

We're currently rolling out a new and improved navigation 
experience. If the following steps don't match your view in the 
Atlas UI, see `the preview Atlas documentation`.

a. If it's not already displayed, select the organization that
   contains your desired project from the `office` Organizations menu in the
   navigation bar.

#. If it's not already displayed, select your project
   from the Projects menu in the navigation bar.

#. If it's not already displayed, click Clusters in the 
   sidebar.

   The [Clusters](https://cloud.mongodb.com/go?l=https%3A%2F%2Fcloud.mongodb.com%2Fv2%2F%3Cproject%3E%23%2Fclusters) page displays.

**Step 2: Navigate to the collection.**

a. For the cluster that contains the sample data, click Browse Collections.
#. In the left navigation pane, select the `sample_supplies` database.
#. Select the `sales` collection.

**Step 3: Specify a query filter document.**

You can specify a query filter document
in the Filter field. A query filter document uses 
query operators to specify search conditions.

Copy the following query filter document into the 
Filter search bar and click Apply:

```javascript
{ saleDate: { $gte: { $date: "2016-01-01T00:00-00:00" }, $lte: { $date: "2016-01-02T00:00-00:00" } } }
```

This query filter returns all documents in the `sample_supplies.sales` 
collection where `saleDate` is on or between January 1 and 2, 2016 
UTC time.

**Step 4: Edit a document.**

To edit a document displayed in the query results, hover over the
document and click on the pencil icon. In the document editor, you can:

- Add a new field. 
- Delete an existing field.
- Edit a field's name, value, or type.
- Revert a specific change.

For detailed instructions, see Create, View, Update, and Delete Documents.

**Step 5: Save your changes.**

To confirm and save your changes, click the Update button.

## Behavior

### Atomicity

All write operations in MongoDB are atomic on the level of a single
document. For more information on MongoDB and atomicity, see
/core/write-operations-atomicity.

### `_id` Field

Once set, you cannot update the value of the `_id` field nor can you
replace an existing document with a replacement document that has a
different `_id` field value.

### Idempotent Operations

Use the `updateMany()` method only for idempotent operations.

### Field Order

For write operations, MongoDB preserves the order of the document fields
*except* for the following cases:

- The `_id` field is always the first field in the document.

- Updates that include `renaming` of field names may
  result in the reordering of fields in the document.

### Upsert Option

**compass:**

The upsert option is not available through MongoDB Compass.

**shell:**

If `updateOne()`,
`updateMany()`, or
`replaceOne()` includes `upsert : true`
**and** no documents match the specified filter, then the
operation creates a new document and inserts it. If there are
matching documents, then the operation modifies or replaces the
matching document or documents.

For details on the new document created, see the individual
reference pages for the methods.

**python:**

If `update_one`,
`update_many`, or
`replace_one` includes
`upsert : true` **and** no documents match the specified
filter, then the operation creates a new document and inserts
it. If there are matching documents, then the operation
modifies or replaces the matching document or documents.

For details on the new document created, see the individual reference
pages for the methods.

**motor:**

If
`update_one`,
`update_many`,
or
`replace_one`
includes `upsert : true` **and** no documents match the
specified filter, then the operation creates a new document and
inserts it. If there are matching documents, then the operation
modifies or replaces the matching document or documents.

For details on the new document created, see the individual
reference pages for the methods.

**java-sync:**

If the update and replace methods include the
com.mongodb.client.model.UpdateOptions_ parameter that
specifies com.mongodb.client.model.UpdateOptions.upsert(true)
**and** no documents match the specified filter, then the
operation creates a new document and inserts it. If there are
matching documents, then the operation modifies or replaces
the matching document or documents.

For details on the new document created, see the individual
reference pages for the methods.

**java-async:**

If the update and replace methods include the [UpdateOptions](https://mongodb.github.io/mongo-java-driver/3.4/javadoc/com/mongodb/client/model/UpdateOptions.html)
parameter that specifies [UpdateOptions.upsert(true)](http://mongodb.github.io/mongo-java-driver/3.4/javadoc/com/mongodb/client/model/UpdateOptions.html?_ga=2.189375400.2069485991.1506612687-1453986945.1494866912&_gac=1.246606128.1506106401.EAIaIQobChMI3tmcxbu51gIVUrnACh12qwkREAAYASABEgLH4PD_BwE#upsert-boolean-)
**and** no documents match the specified filter, then the
operation creates a new document and inserts it. If there are
matching documents, then the operation modifies or replaces the
matching document or documents.

For details on the new document created, see the individual
reference pages for the methods.

**nodejs:**

If `updateOne()`,
`updateMany()`, or
`replaceOne()` include
`upsert : true` in the `options` parameter document **and**
no documents match the specified filter, then the operation
creates a new document and inserts it. If there are matching
documents, then the operation modifies or replaces the matching
document or documents.

For details on the new document created, see the individual
reference pages for the methods.

**php:**

If `updateOne()`,
`updateMany()`, or
`replaceOne()` includes ``upsert =>
true`` **and** no documents match the specified filter, then the
operation creates a new document and inserts it. If there are
matching documents, then the operation modifies or replaces the
matching document or documents.

For details on the new document created, see the individual
reference pages for the methods.

**ruby:**

If
`update_one()`,
`update_many()`,
or
`replace_one()`
includes `upsert => true` **and** no documents match the
specified filter, then the operation creates a new document and
inserts it. If there are matching documents, then the operation
modifies or replaces the matching document or documents.

For details on the new document created, see the individual
reference pages for the methods.

**scala:**

If
`updateOne()`,
`updateMany()`,
or
`replaceOne()`
includes `upsert => true` **and** no documents match the
specified filter, then the operation creates a new document and
inserts it. If there are matching documents, then the operation
modifies or replaces the matching document or documents.

For details on the new document created, see the individual
reference pages for the methods.

**csharp:**

If `UpdateOne()`,
`UpdateMany()`, or
`ReplaceOne()` includes an
`UpdateOptions`
argument instance with the `IsUpsert` option set to `true`
**and** no documents match the specified filter, then the
operation creates a new document and inserts it. If there are
matching documents, then the operation modifies or replaces the
matching document or documents.

For details on the new document created, see the individual
reference pages for the methods.

**go:**

If `Collection.UpdateOne`
includes the `Upsert option set to true` **and** no documents match the
specified filter, then the operation creates a new document and
inserts it. If there are matching documents, then the operation
modifies or replaces the matching document or documents.

For details on the new document created, see the individual
reference pages for the methods.

### Write Acknowledgement

With write concerns, you can specify the level of acknowledgment
requested from MongoDB for write operations. For details, see
/reference/write-concern.

**shell:**

**See also:**

- /tutorial/update-documents-with-aggregation-pipeline

- `db.collection.updateOne()`

- `db.collection.updateMany()`

- `db.collection.replaceOne()`

- additional-updates

**compass:**

**See also:**

- `Compass Documents`

- Compass Query Bar

**python:**

**See also:**

- `pymongo.collection.Collection.update_one`

- `pymongo.collection.Collection.update_many`

- `pymongo.collection.Collection.replace_one`

- additional-updates

**motor:**

**See also:**

- `motor.motor_asyncio.AsyncIOMotorCollection.update_one`

- `motor.motor_asyncio.AsyncIOMotorCollection.update_many`

- `motor.motor_asyncio.AsyncIOMotorCollection.replace_one`

- additional-updates

**java-sync:**

**See also:**

- com.mongodb.client.MongoCollection.updateOne_

- com.mongodb.client.MongoCollection.updateMany_

- com.mongodb.client.MongoCollection.replaceOne_

- Additional Java Synchronous Driver Write Examples

**java-async:**

**See also:**

- [com.mongodb.reactivestreams.client.MongoCollection.updateOne](http://mongodb.github.io/mongo-java-driver-reactivestreams/1.6/javadoc/com/mongodb/reactivestreams/client/MongoCollection.html#updateOne(org.bson.conversions.Bson,%20org.bson.conversions.Bson))

- [com.mongodb.reactivestreams.client.MongoCollection.updateMany](http://mongodb.github.io/mongo-java-driver-reactivestreams/1.6/javadoc/com/mongodb/reactivestreams/client/MongoCollection.html#updateMany(org.bson.conversions.Bson,%20org.bson.conversions.Bson))

- [com.mongodb.reactivestreams.client.MongoCollection.replaceOne](http://mongodb.github.io/mongo-java-driver-reactivestreams/1.6/javadoc/com/mongodb/reactivestreams/client/MongoCollection.html#replaceOne(org.bson.conversions.Bson,%20TDocument))

- [Java Reactive Streams Driver Quick Tour](http://mongodb.github.io/mongo-java-driver-reactivestreams/1.6/getting-started/quick-tour/)

**nodejs:**

**See also:**

- `Collection.updateOne()`

- `Collection.updateMany()`

- `Collection.replaceOne()`

- additional-updates

**php:**

**See also:**

- `MongoDBCollection::updateOne()`

- `MongoDBCollection::updateMany()`

- `MongoDBCollection::replaceOne()`

- additional-updates

**ruby:**

**See also:**

- `Mongo::Collection#update_one()`

- `Mongo::Collection#update_many()`

- `Mongo::Collection#replace_one()`

**scala:**

**See also:**

- `collection.updateOne()`

- `collection.updateMany()`

- `collection.replaceOne()`

- additional-updates

**csharp:**

**See also:**

- `IMongoCollection.UpdateOne()`

- `IMongoCollection.UpdateMany()`

- `IMongoCollection.ReplaceOne()`

- additional-updates

**go:**

**See also:**

- `Collection.UpdateOne`

- `Collection.UpdateMany`

- `Collection.ReplaceOne`

- additional-updates
