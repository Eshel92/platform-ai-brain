<!-- Converted from tutorial/query-array-of-documents.txt (reStructuredText). Includes are inlined. -->

# Query an Array of Embedded Documents

   
   

You can query documents in MongoDB by using the following
methods:

- Your programming language's driver.
- The MongoDB Atlas UI. To learn more, see 
  query-array-documents-atlas-ui.
- `MongoDB Compass`.

This page provides examples of query operations on an array of nested documents using the
`db.collection.find()` method in `mongosh`.

```javascript
db.inventory.insertMany( [
   { item: "journal", instock: [ { warehouse: "A", qty: 5 }, { warehouse: "C", qty: 15 } ] },
   { item: "notebook", instock: [ { warehouse: "C", qty: 5 } ] },
   { item: "paper", instock: [ { warehouse: "A", qty: 60 }, { warehouse: "B", qty: 15 } ] },
   { item: "planner", instock: [ { warehouse: "A", qty: 40 }, { warehouse: "B", qty: 5 } ] },
   { item: "postcard", instock: [ { warehouse: "B", qty: 15 }, { warehouse: "C", qty: 35 } ] }
]);
```

## Query for a Document Nested in an Array

The following example selects all documents where an element in the
`instock` array matches the specified document:

```javascript
db.inventory.find( { "instock": { warehouse: "A", qty: 5 } } )
```

Equality matches on the whole embedded/nested document require an
*exact* match of the specified document, including the field order. For
example, the following query does not match any documents in the
`inventory` collection:

```javascript
db.inventory.find( { "instock": { qty: 5, warehouse: "A" } } )
```

## Specify a Query Condition on a Field in an Array of Documents

### Specify a Query Condition on a Field Embedded in an Array of Documents

If you do not know the index position of the document nested in the
array, concatenate the name of the array field, with a dot (`.`) and
the name of the field in the nested document.

The following example selects all documents where the `instock` array
has at least one embedded document that contains the field `qty`
whose value is less than or equal to `20`:

```javascript
db.inventory.find( { 'instock.qty': { $lte: 20 } } )
```

### Use the Array Index to Query for a Field in the Embedded Document

Using dot notation, you can specify query conditions for a
field in a document at a particular index or position of the array.
The array uses zero-based indexing.

**Note:**

When querying using dot notation, the field and index must be
inside quotation marks.

The following example selects all documents where the `instock` array
has as its first element a document that contains the field `qty`
whose value is less than or equal to `20`:

```javascript
db.inventory.find( { 'instock.0.qty': { $lte: 20 } } )
```

## Specify Multiple Conditions for Array of Documents

When you specify conditions on more than one field nested in an array
of documents, you can specify the query such that either a single
document meets these conditions or any combination of documents in the
array meets the conditions.

### A Single Nested Document Meets Multiple Query Conditions on Nested Fields

Use the `$elemMatch` operator to specify multiple criteria on
an array of embedded documents such that at least one embedded
document satisfies all the specified criteria.

The following example queries for documents where the `instock` array
has at least one embedded document that contains both the field
`qty` equal to `5` and the field `warehouse` equal
to `A`:

```javascript
db.inventory.find( { "instock": { $elemMatch: { qty: 5, warehouse: "A" } } } )
```

The following example queries for documents where the `instock` array
has at least one embedded document that contains the field `qty` that
is greater than `10` and less than or equal to `20`:

```javascript
db.inventory.find( { "instock": { $elemMatch: { qty: { $gt: 10, $lte: 20 } } } } )
```

### Combination of Elements Satisfies the Criteria

If the compound query conditions on an array field do not use the
`$elemMatch` operator, the query selects those documents whose
array contains any combination of elements that satisfies the
conditions.

For example, the following query matches documents where any document
nested in the `instock` array has the `qty` field greater than
`10` and any document (but not necessarily the same embedded
document) in the array has the `qty` field less than or equal to
`20`:

```javascript
db.inventory.find( { "instock.qty": { $gt: 10,  $lte: 20 } } )
```

The following example queries for documents where the `instock` array
has at least one embedded document that contains the field `qty`
equal to `5` and at least one embedded document (but not necessarily
the same embedded document) that contains the field `warehouse` equal
to `A`:

```javascript
db.inventory.find( { "instock.qty": 5, "instock.warehouse": "A" } )
```

This page provides examples of query operations on an array of nested documents using the
`pymongo.collection.Collection.find` method in the
[PyMongo](https://www.mongodb.com/docs/languages/python/pymongo-driver/current/)
Python driver.

The examples on this page use the `inventory` collection. Connect to a
test database in your MongoDB instance then create the `inventory`
collection:

(Code example not available offline: /driver-examples/test_examples.py)

## Query for a Document Nested in an Array

The following example selects all documents where an element in the
`instock` array matches the specified document:

(Code example not available offline: /driver-examples/test_examples.py)

Equality matches on the whole embedded/nested document require an
*exact* match of the specified document, including the field order. For
example, the following query does not match any documents in the
`inventory` collection:

(Code example not available offline: /driver-examples/test_examples.py)

## Specify a Query Condition on a Field in an Array of Documents

### Specify a Query Condition on a Field Embedded in an Array of Documents

If you do not know the index position of the document nested in the
array, concatenate the name of the array field, with a dot (`.`) and
the name of the field in the nested document.

The following example selects all documents where the `instock` array
has at least one embedded document that contains the field `qty`
whose value is less than or equal to `20`:

(Code example not available offline: /driver-examples/test_examples.py)

### Use the Array Index to Query for a Field in the Embedded Document

Using dot notation, you can specify query conditions for a
field in a document at a particular index or position of the array.
The array uses zero-based indexing.

**Note:**

When querying using dot notation, the field and index must be
inside quotation marks.

The following example selects all documents where the `instock` array
has as its first element a document that contains the field `qty`
whose value is less than or equal to `20`:

(Code example not available offline: /driver-examples/test_examples.py)

## Specify Multiple Conditions for Array of Documents

When you specify conditions on more than one field nested in an array
of documents, you can specify the query such that either a single
document meets these conditions or any combination of documents in the
array meets the conditions.

### A Single Nested Document Meets Multiple Query Conditions on Nested Fields

Use the `$elemMatch` operator to specify multiple criteria on
an array of embedded documents such that at least one embedded
document satisfies all the specified criteria.

The following example queries for documents where the `instock` array
has at least one embedded document that contains both the field
`qty` equal to `5` and the field `warehouse` equal
to `A`:

(Code example not available offline: /driver-examples/test_examples.py)

The following example queries for documents where the `instock` array
has at least one embedded document that contains the field `qty` that
is greater than `10` and less than or equal to `20`:

(Code example not available offline: /driver-examples/test_examples.py)

### Combination of Elements Satisfies the Criteria

If the compound query conditions on an array field do not use the
`$elemMatch` operator, the query selects those documents whose
array contains any combination of elements that satisfies the
conditions.

For example, the following query matches documents where any document
nested in the `instock` array has the `qty` field greater than
`10` and any document (but not necessarily the same embedded
document) in the array has the `qty` field less than or equal to
`20`:

(Code example not available offline: /driver-examples/test_examples.py)

The following example queries for documents where the `instock` array
has at least one embedded document that contains the field `qty`
equal to `5` and at least one embedded document (but not necessarily
the same embedded document) that contains the field `warehouse` equal
to `A`:

(Code example not available offline: /driver-examples/test_examples.py)

This page provides examples of query operations on an array of nested documents using the
`pymongo.asynchronous.collection.AsyncCollection.find`
method in the [PyMongo Async API](https://pymongo.readthedocs.io/en/stable/api/pymongo/asynchronous/index.html).

The examples on this page use the `inventory` collection. Connect to a
test database in your MongoDB instance then create the `inventory`
collection:

(Code example not available offline: /driver-examples/test_examples_motor.py)

## Query for a Document Nested in an Array

The following example selects all documents where an element in the
`instock` array matches the specified document:

(Code example not available offline: /driver-examples/test_examples_motor.py)

Equality matches on the whole embedded/nested document require an
*exact* match of the specified document, including the field order. For
example, the following query does not match any documents in the
`inventory` collection:

(Code example not available offline: /driver-examples/test_examples_motor.py)

## Specify a Query Condition on a Field in an Array of Documents

### Specify a Query Condition on a Field Embedded in an Array of Documents

If you do not know the index position of the document nested in the
array, concatenate the name of the array field, with a dot (`.`) and
the name of the field in the nested document.

The following example selects all documents where the `instock` array
has at least one embedded document that contains the field `qty`
whose value is less than or equal to `20`:

(Code example not available offline: /driver-examples/test_examples_motor.py)

### Use the Array Index to Query for a Field in the Embedded Document

Using dot notation, you can specify query conditions for a
field in a document at a particular index or position of the array.
The array uses zero-based indexing.

**Note:**

When querying using dot notation, the field and index must be
inside quotation marks.

The following example selects all documents where the `instock` array
has as its first element a document that contains the field `qty`
whose value is less than or equal to `20`:

(Code example not available offline: /driver-examples/test_examples_motor.py)

## Specify Multiple Conditions for Array of Documents

When you specify conditions on more than one field nested in an array
of documents, you can specify the query such that either a single
document meets these conditions or any combination of documents in the
array meets the conditions.

### A Single Nested Document Meets Multiple Query Conditions on Nested Fields

Use the `$elemMatch` operator to specify multiple criteria on
an array of embedded documents such that at least one embedded
document satisfies all the specified criteria.

The following example queries for documents where the `instock` array
has at least one embedded document that contains both the field
`qty` equal to `5` and the field `warehouse` equal
to `A`:

(Code example not available offline: /driver-examples/test_examples_motor.py)

The following example queries for documents where the `instock` array
has at least one embedded document that contains the field `qty` that
is greater than `10` and less than or equal to `20`:

(Code example not available offline: /driver-examples/test_examples_motor.py)

### Combination of Elements Satisfies the Criteria

If the compound query conditions on an array field do not use the
`$elemMatch` operator, the query selects those documents whose
array contains any combination of elements that satisfies the
conditions.

For example, the following query matches documents where any document
nested in the `instock` array has the `qty` field greater than
`10` and any document (but not necessarily the same embedded
document) in the array has the `qty` field less than or equal to
`20`:

(Code example not available offline: /driver-examples/test_examples_motor.py)

The following example queries for documents where the `instock` array
has at least one embedded document that contains the field `qty`
equal to `5` and at least one embedded document (but not necessarily
the same embedded document) that contains the field `warehouse` equal
to `A`:

(Code example not available offline: /driver-examples/test_examples_motor.py)

This page provides examples of query operations on an array of nested documents using the
com.mongodb.client.MongoCollection.find_ method in the MongoDB
Java Synchronous Driver.

**Tip:**

The driver provides com.mongodb.client.model.Filters_
helper methods to facilitate the creation of filter
documents. The examples on this page use these methods to
create the filter documents.

The examples on this page use the `inventory` collection. Connect to a
test database in your MongoDB instance then create the `inventory`
collection:

(Code example not available offline: /driver-examples/DocumentationSamples.java)

## Query for a Document Nested in an Array

The following example selects all documents where an element in the
`instock` array matches the specified document:

(Code example not available offline: /driver-examples/DocumentationSamples.java)

Equality matches on the whole embedded/nested document require an
*exact* match of the specified document, including the field order. For
example, the following query does not match any documents in the
`inventory` collection:

(Code example not available offline: /driver-examples/DocumentationSamples.java)

## Specify a Query Condition on a Field in an Array of Documents

### Specify a Query Condition on a Field Embedded in an Array of Documents

If you do not know the index position of the document nested in the
array, concatenate the name of the array field, with a dot (`.`) and
the name of the field in the nested document.

The following example selects all documents where the `instock` array
has at least one embedded document that contains the field `qty`
whose value is less than or equal to `20`:

(Code example not available offline: /driver-examples/DocumentationSamples.java)

### Use the Array Index to Query for a Field in the Embedded Document

Using dot notation, you can specify query conditions for a
field in a document at a particular index or position of the array.
The array uses zero-based indexing.

**Note:**

When querying using dot notation, the field and index must be
inside quotation marks.

The following example selects all documents where the `instock` array
has as its first element a document that contains the field `qty`
whose value is less than or equal to `20`:

(Code example not available offline: /driver-examples/DocumentationSamples.java)

## Specify Multiple Conditions for Array of Documents

When you specify conditions on more than one field nested in an array
of documents, you can specify the query such that either a single
document meets these conditions or any combination of documents in the
array meets the conditions.

### A Single Nested Document Meets Multiple Query Conditions on Nested Fields

Use the `$elemMatch` operator to specify multiple criteria on
an array of embedded documents such that at least one embedded
document satisfies all the specified criteria.

The following example queries for documents where the `instock` array
has at least one embedded document that contains both the field
`qty` equal to `5` and the field `warehouse` equal
to `A`:

(Code example not available offline: /driver-examples/DocumentationSamples.java)

The following example queries for documents where the `instock` array
has at least one embedded document that contains the field `qty` that
is greater than `10` and less than or equal to `20`:

(Code example not available offline: /driver-examples/DocumentationSamples.java)

### Combination of Elements Satisfies the Criteria

If the compound query conditions on an array field do not use the
`$elemMatch` operator, the query selects those documents whose
array contains any combination of elements that satisfies the
conditions.

For example, the following query matches documents where any document
nested in the `instock` array has the `qty` field greater than
`10` and any document (but not necessarily the same embedded
document) in the array has the `qty` field less than or equal to
`20`:

(Code example not available offline: /driver-examples/DocumentationSamples.java)

The following example queries for documents where the `instock` array
has at least one embedded document that contains the field `qty`
equal to `5` and at least one embedded document (but not necessarily
the same embedded document) that contains the field `warehouse` equal
to `A`:

(Code example not available offline: /driver-examples/DocumentationSamples.java)

This page provides examples of query operations on an array of nested documents using the
[com.mongodb.reactivestreams.client.MongoCollection.find](http://mongodb.github.io/mongo-java-driver-reactivestreams/1.6/javadoc/com/mongodb/reactivestreams/client/MongoCollection.html#find())
method in the MongoDB [Java Reactive Streams Driver](http://mongodb.github.io/mongo-java-driver-reactivestreams/1.6/).

The examples on this page use the `inventory` collection. Connect to a
test database in your MongoDB instance then create the `inventory`
collection:

(Code example not available offline: /driver-examples/AsyncDocumentationSamples.java)

## Query for a Document Nested in an Array

The following example selects all documents where an element in the
`instock` array matches the specified document:

(Code example not available offline: /driver-examples/AsyncDocumentationSamples.java)

Equality matches on the whole embedded/nested document require an
*exact* match of the specified document, including the field order. For
example, the following query does not match any documents in the
`inventory` collection:

(Code example not available offline: /driver-examples/AsyncDocumentationSamples.java)

## Specify a Query Condition on a Field in an Array of Documents

### Specify a Query Condition on a Field Embedded in an Array of Documents

If you do not know the index position of the document nested in the
array, concatenate the name of the array field, with a dot (`.`) and
the name of the field in the nested document.

The following example selects all documents where the `instock` array
has at least one embedded document that contains the field `qty`
whose value is less than or equal to `20`:

(Code example not available offline: /driver-examples/AsyncDocumentationSamples.java)

### Use the Array Index to Query for a Field in the Embedded Document

Using dot notation, you can specify query conditions for a
field in a document at a particular index or position of the array.
The array uses zero-based indexing.

**Note:**

When querying using dot notation, the field and index must be
inside quotation marks.

The following example selects all documents where the `instock` array
has as its first element a document that contains the field `qty`
whose value is less than or equal to `20`:

(Code example not available offline: /driver-examples/AsyncDocumentationSamples.java)

## Specify Multiple Conditions for Array of Documents

When you specify conditions on more than one field nested in an array
of documents, you can specify the query such that either a single
document meets these conditions or any combination of documents in the
array meets the conditions.

### A Single Nested Document Meets Multiple Query Conditions on Nested Fields

Use the `$elemMatch` operator to specify multiple criteria on
an array of embedded documents such that at least one embedded
document satisfies all the specified criteria.

The following example queries for documents where the `instock` array
has at least one embedded document that contains both the field
`qty` equal to `5` and the field `warehouse` equal
to `A`:

(Code example not available offline: /driver-examples/AsyncDocumentationSamples.java)

The following example queries for documents where the `instock` array
has at least one embedded document that contains the field `qty` that
is greater than `10` and less than or equal to `20`:

(Code example not available offline: /driver-examples/AsyncDocumentationSamples.java)

### Combination of Elements Satisfies the Criteria

If the compound query conditions on an array field do not use the
`$elemMatch` operator, the query selects those documents whose
array contains any combination of elements that satisfies the
conditions.

For example, the following query matches documents where any document
nested in the `instock` array has the `qty` field greater than
`10` and any document (but not necessarily the same embedded
document) in the array has the `qty` field less than or equal to
`20`:

(Code example not available offline: /driver-examples/AsyncDocumentationSamples.java)

The following example queries for documents where the `instock` array
has at least one embedded document that contains the field `qty`
equal to `5` and at least one embedded document (but not necessarily
the same embedded document) that contains the field `warehouse` equal
to `A`:

(Code example not available offline: /driver-examples/AsyncDocumentationSamples.java)

This page provides examples of query operations on an array of nested documents by using the
[MongoCollection.find()](https://mongodb.github.io/mongo-java-driver/{+java-driver-version+}/apidocs/driver-kotlin-coroutine/mongodb-driver-kotlin-coroutine/com.mongodb.kotlin.client.coroutine/-mongo-collection/find.html) method in the MongoDB
`Kotlin Coroutine Driver`.

**Tip:**

The driver provides [com.mongodb.client.model.Filters](https://mongodb.github.io/mongo-java-driver/{+java-driver-version+}/apidocs/driver-core/com/mongodb/client/model/Filters.html)
helper methods to facilitate the creation of filter
documents. The examples on this page use these methods to
create the filter documents.

The examples on this page use the `inventory` collection. Connect to a
test database in your MongoDB instance then create the `inventory`
collection:

(Code example not available offline: /driver-examples/kotlin_examples.kt)

## Query for a Document Nested in an Array

The following example selects all documents where an element in the
`instock` array matches the specified document:

(Code example not available offline: /driver-examples/kotlin_examples.kt)

Equality matches on the whole embedded/nested document require an
*exact* match of the specified document, including the field order. For
example, the following query does not match any documents in the
`inventory` collection:

(Code example not available offline: /driver-examples/kotlin_examples.kt)

## Specify a Query Condition on a Field in an Array of Documents

### Specify a Query Condition on a Field Embedded in an Array of Documents

If you do not know the index position of the document nested in the
array, concatenate the name of the array field, with a dot (`.`) and
the name of the field in the nested document.

The following example selects all documents where the `instock` array
has at least one embedded document that contains the field `qty`
whose value is less than or equal to `20`:

(Code example not available offline: /driver-examples/kotlin_examples.kt)

### Use the Array Index to Query for a Field in the Embedded Document

Using dot notation, you can specify query conditions for a
field in a document at a particular index or position of the array.
The array uses zero-based indexing.

**Note:**

When querying using dot notation, the field and index must be
inside quotation marks.

The following example selects all documents where the `instock` array
has as its first element a document that contains the field `qty`
whose value is less than or equal to `20`:

(Code example not available offline: /driver-examples/kotlin_examples.kt)

## Specify Multiple Conditions for Array of Documents

When you specify conditions on more than one field nested in an array
of documents, you can specify the query such that either a single
document meets these conditions or any combination of documents in the
array meets the conditions.

### A Single Nested Document Meets Multiple Query Conditions on Nested Fields

Use the `$elemMatch` operator to specify multiple criteria on
an array of embedded documents such that at least one embedded
document satisfies all the specified criteria.

The following example queries for documents where the `instock` array
has at least one embedded document that contains both the field
`qty` equal to `5` and the field `warehouse` equal
to `A`:

(Code example not available offline: /driver-examples/kotlin_examples.kt)

The following example queries for documents where the `instock` array
has at least one embedded document that contains the field `qty` that
is greater than `10` and less than or equal to `20`:

(Code example not available offline: /driver-examples/kotlin_examples.kt)

### Combination of Elements Satisfies the Criteria

If the compound query conditions on an array field do not use the
`$elemMatch` operator, the query selects those documents whose
array contains any combination of elements that satisfies the
conditions.

For example, the following query matches documents where any document
nested in the `instock` array has the `qty` field greater than
`10` and any document (but not necessarily the same embedded
document) in the array has the `qty` field less than or equal to
`20`:

(Code example not available offline: /driver-examples/kotlin_examples.kt)

The following example queries for documents where the `instock` array
has at least one embedded document that contains the field `qty`
equal to `5` and at least one embedded document (but not necessarily
the same embedded document) that contains the field `warehouse` equal
to `A`:

(Code example not available offline: /driver-examples/kotlin_examples.kt)

This page provides examples of query operations on an array of nested documents using the
`Collection.find()` method in
the `MongoDB Node.js Driver`.

The examples on this page use the `inventory` collection. Connect to a
test database in your MongoDB instance then create the `inventory`
collection:

(Code example not available offline: /driver-examples/node_query_array_of_documents.js)

## Query for a Document Nested in an Array

The following example selects all documents where an element in the
`instock` array matches the specified document:

(Code example not available offline: /driver-examples/node_query_array_of_documents.js)

Equality matches on the whole embedded/nested document require an
*exact* match of the specified document, including the field order. For
example, the following query does not match any documents in the
`inventory` collection:

(Code example not available offline: /driver-examples/node_query_array_of_documents.js)

## Specify a Query Condition on a Field in an Array of Documents

### Specify a Query Condition on a Field Embedded in an Array of Documents

If you do not know the index position of the document nested in the
array, concatenate the name of the array field, with a dot (`.`) and
the name of the field in the nested document.

The following example selects all documents where the `instock` array
has at least one embedded document that contains the field `qty`
whose value is less than or equal to `20`:

(Code example not available offline: /driver-examples/node_query_array_of_documents.js)

### Use the Array Index to Query for a Field in the Embedded Document

Using dot notation, you can specify query conditions for a
field in a document at a particular index or position of the array.
The array uses zero-based indexing.

**Note:**

When querying using dot notation, the field and index must be
inside quotation marks.

The following example selects all documents where the `instock` array
has as its first element a document that contains the field `qty`
whose value is less than or equal to `20`:

(Code example not available offline: /driver-examples/node_query_array_of_documents.js)

## Specify Multiple Conditions for Array of Documents

When you specify conditions on more than one field nested in an array
of documents, you can specify the query such that either a single
document meets these conditions or any combination of documents in the
array meets the conditions.

### A Single Nested Document Meets Multiple Query Conditions on Nested Fields

Use the `$elemMatch` operator to specify multiple criteria on
an array of embedded documents such that at least one embedded
document satisfies all the specified criteria.

The following example queries for documents where the `instock` array
has at least one embedded document that contains both the field
`qty` equal to `5` and the field `warehouse` equal
to `A`:

(Code example not available offline: /driver-examples/node_query_array_of_documents.js)

The following example queries for documents where the `instock` array
has at least one embedded document that contains the field `qty` that
is greater than `10` and less than or equal to `20`:

(Code example not available offline: /driver-examples/node_query_array_of_documents.js)

### Combination of Elements Satisfies the Criteria

If the compound query conditions on an array field do not use the
`$elemMatch` operator, the query selects those documents whose
array contains any combination of elements that satisfies the
conditions.

For example, the following query matches documents where any document
nested in the `instock` array has the `qty` field greater than
`10` and any document (but not necessarily the same embedded
document) in the array has the `qty` field less than or equal to
`20`:

(Code example not available offline: /driver-examples/node_query_array_of_documents.js)

The following example queries for documents where the `instock` array
has at least one embedded document that contains the field `qty`
equal to `5` and at least one embedded document (but not necessarily
the same embedded document) that contains the field `warehouse` equal
to `A`:

(Code example not available offline: /driver-examples/node_query_array_of_documents.js)

This page provides examples of query operations on an array of nested documents using the
`MongoDBCollection::find()`
method in the
[MongoDB PHP Library](https://www.mongodb.com/docs/drivers/php-libraries/).

The examples on this page use the `inventory` collection. Connect to a
test database in your MongoDB instance then create the `inventory`
collection:

(Code example not available offline: /driver-examples/DocumentationExamplesTest.php)

## Query for a Document Nested in an Array

The following example selects all documents where an element in the
`instock` array matches the specified document:

(Code example not available offline: /driver-examples/DocumentationExamplesTest.php)

Equality matches on the whole embedded/nested document require an
*exact* match of the specified document, including the field order. For
example, the following query does not match any documents in the
`inventory` collection:

(Code example not available offline: /driver-examples/DocumentationExamplesTest.php)

## Specify a Query Condition on a Field in an Array of Documents

### Specify a Query Condition on a Field Embedded in an Array of Documents

If you do not know the index position of the document nested in the
array, concatenate the name of the array field, with a dot (`.`) and
the name of the field in the nested document.

The following example selects all documents where the `instock` array
has at least one embedded document that contains the field `qty`
whose value is less than or equal to `20`:

(Code example not available offline: /driver-examples/DocumentationExamplesTest.php)

### Use the Array Index to Query for a Field in the Embedded Document

Using dot notation, you can specify query conditions for a
field in a document at a particular index or position of the array.
The array uses zero-based indexing.

**Note:**

When querying using dot notation, the field and index must be
inside quotation marks.

The following example selects all documents where the `instock` array
has as its first element a document that contains the field `qty`
whose value is less than or equal to `20`:

(Code example not available offline: /driver-examples/DocumentationExamplesTest.php)

## Specify Multiple Conditions for Array of Documents

When you specify conditions on more than one field nested in an array
of documents, you can specify the query such that either a single
document meets these conditions or any combination of documents in the
array meets the conditions.

### A Single Nested Document Meets Multiple Query Conditions on Nested Fields

Use the `$elemMatch` operator to specify multiple criteria on
an array of embedded documents such that at least one embedded
document satisfies all the specified criteria.

The following example queries for documents where the `instock` array
has at least one embedded document that contains both the field
`qty` equal to `5` and the field `warehouse` equal
to `A`:

(Code example not available offline: /driver-examples/DocumentationExamplesTest.php)

The following example queries for documents where the `instock` array
has at least one embedded document that contains the field `qty` that
is greater than `10` and less than or equal to `20`:

(Code example not available offline: /driver-examples/DocumentationExamplesTest.php)

### Combination of Elements Satisfies the Criteria

If the compound query conditions on an array field do not use the
`$elemMatch` operator, the query selects those documents whose
array contains any combination of elements that satisfies the
conditions.

For example, the following query matches documents where any document
nested in the `instock` array has the `qty` field greater than
`10` and any document (but not necessarily the same embedded
document) in the array has the `qty` field less than or equal to
`20`:

(Code example not available offline: /driver-examples/DocumentationExamplesTest.php)

The following example queries for documents where the `instock` array
has at least one embedded document that contains the field `qty`
equal to `5` and at least one embedded document (but not necessarily
the same embedded document) that contains the field `warehouse` equal
to `A`:

(Code example not available offline: /driver-examples/DocumentationExamplesTest.php)

This page provides examples of query operations on an array of nested documents using the
`Mongo::Collection#find()`
method in the
`MongoDB Ruby Driver`.

The examples on this page use the `inventory` collection. Connect to a
test database in your MongoDB instance then create the `inventory`
collection:

(Code example not available offline: /driver-examples/shell_examples_spec.rb)

## Query for a Document Nested in an Array

The following example selects all documents where an element in the
`instock` array matches the specified document:

(Code example not available offline: /driver-examples/shell_examples_spec.rb)

Equality matches on the whole embedded/nested document require an
*exact* match of the specified document, including the field order. For
example, the following query does not match any documents in the
`inventory` collection:

(Code example not available offline: /driver-examples/shell_examples_spec.rb)

## Specify a Query Condition on a Field in an Array of Documents

### Specify a Query Condition on a Field Embedded in an Array of Documents

If you do not know the index position of the document nested in the
array, concatenate the name of the array field, with a dot (`.`) and
the name of the field in the nested document.

The following example selects all documents where the `instock` array
has at least one embedded document that contains the field `qty`
whose value is less than or equal to `20`:

(Code example not available offline: /driver-examples/shell_examples_spec.rb)

### Use the Array Index to Query for a Field in the Embedded Document

Using dot notation, you can specify query conditions for a
field in a document at a particular index or position of the array.
The array uses zero-based indexing.

**Note:**

When querying using dot notation, the field and index must be
inside quotation marks.

The following example selects all documents where the `instock` array
has as its first element a document that contains the field `qty`
whose value is less than or equal to `20`:

(Code example not available offline: /driver-examples/shell_examples_spec.rb)

## Specify Multiple Conditions for Array of Documents

When you specify conditions on more than one field nested in an array
of documents, you can specify the query such that either a single
document meets these conditions or any combination of documents in the
array meets the conditions.

### A Single Nested Document Meets Multiple Query Conditions on Nested Fields

Use the `$elemMatch` operator to specify multiple criteria on
an array of embedded documents such that at least one embedded
document satisfies all the specified criteria.

The following example queries for documents where the `instock` array
has at least one embedded document that contains both the field
`qty` equal to `5` and the field `warehouse` equal
to `A`:

(Code example not available offline: /driver-examples/shell_examples_spec.rb)

The following example queries for documents where the `instock` array
has at least one embedded document that contains the field `qty` that
is greater than `10` and less than or equal to `20`:

(Code example not available offline: /driver-examples/shell_examples_spec.rb)

### Combination of Elements Satisfies the Criteria

If the compound query conditions on an array field do not use the
`$elemMatch` operator, the query selects those documents whose
array contains any combination of elements that satisfies the
conditions.

For example, the following query matches documents where any document
nested in the `instock` array has the `qty` field greater than
`10` and any document (but not necessarily the same embedded
document) in the array has the `qty` field less than or equal to
`20`:

(Code example not available offline: /driver-examples/shell_examples_spec.rb)

The following example queries for documents where the `instock` array
has at least one embedded document that contains the field `qty`
equal to `5` and at least one embedded document (but not necessarily
the same embedded document) that contains the field `warehouse` equal
to `A`:

(Code example not available offline: /driver-examples/shell_examples_spec.rb)

This page provides examples of query operations on an array of nested documents using the
`collection.find()` method
in the
[MongoDB Scala Driver](http://mongodb.github.io/mongo-scala-driver/).

The examples on this page use the `inventory` collection. Connect to a
test database in your MongoDB instance then create the `inventory`
collection:

(Code example not available offline: /driver-examples/DocumentationExampleSpec.scala)

## Query for a Document Nested in an Array

The following example selects all documents where an element in the
`instock` array matches the specified document:

(Code example not available offline: /driver-examples/DocumentationExampleSpec.scala)

Equality matches on the whole embedded/nested document require an
*exact* match of the specified document, including the field order. For
example, the following query does not match any documents in the
`inventory` collection:

(Code example not available offline: /driver-examples/DocumentationExampleSpec.scala)

## Specify a Query Condition on a Field in an Array of Documents

### Specify a Query Condition on a Field Embedded in an Array of Documents

If you do not know the index position of the document nested in the
array, concatenate the name of the array field, with a dot (`.`) and
the name of the field in the nested document.

The following example selects all documents where the `instock` array
has at least one embedded document that contains the field `qty`
whose value is less than or equal to `20`:

(Code example not available offline: /driver-examples/DocumentationExampleSpec.scala)

### Use the Array Index to Query for a Field in the Embedded Document

Using dot notation, you can specify query conditions for a
field in a document at a particular index or position of the array.
The array uses zero-based indexing.

**Note:**

When querying using dot notation, the field and index must be
inside quotation marks.

The following example selects all documents where the `instock` array
has as its first element a document that contains the field `qty`
whose value is less than or equal to `20`:

(Code example not available offline: /driver-examples/DocumentationExampleSpec.scala)

## Specify Multiple Conditions for Array of Documents

When you specify conditions on more than one field nested in an array
of documents, you can specify the query such that either a single
document meets these conditions or any combination of documents in the
array meets the conditions.

### A Single Nested Document Meets Multiple Query Conditions on Nested Fields

Use the `$elemMatch` operator to specify multiple criteria on
an array of embedded documents such that at least one embedded
document satisfies all the specified criteria.

The following example queries for documents where the `instock` array
has at least one embedded document that contains both the field
`qty` equal to `5` and the field `warehouse` equal
to `A`:

(Code example not available offline: /driver-examples/DocumentationExampleSpec.scala)

The following example queries for documents where the `instock` array
has at least one embedded document that contains the field `qty` that
is greater than `10` and less than or equal to `20`:

(Code example not available offline: /driver-examples/DocumentationExampleSpec.scala)

### Combination of Elements Satisfies the Criteria

If the compound query conditions on an array field do not use the
`$elemMatch` operator, the query selects those documents whose
array contains any combination of elements that satisfies the
conditions.

For example, the following query matches documents where any document
nested in the `instock` array has the `qty` field greater than
`10` and any document (but not necessarily the same embedded
document) in the array has the `qty` field less than or equal to
`20`:

(Code example not available offline: /driver-examples/DocumentationExampleSpec.scala)

The following example queries for documents where the `instock` array
has at least one embedded document that contains the field `qty`
equal to `5` and at least one embedded document (but not necessarily
the same embedded document) that contains the field `warehouse` equal
to `A`:

(Code example not available offline: /driver-examples/DocumentationExampleSpec.scala)

This page provides examples of query operations on an array of nested documents using the
`MongoCollection.Find()`
method in the
[MongoDB .NET/C# Driver](https://mongodb.github.io/mongo-csharp-driver/).

The examples on this page use the `inventory` collection. Connect to a
test database in your MongoDB instance then create the `inventory`
collection:

```csharp
var documents = new[]
{
    new BsonDocument
    {
        { "item", "journal" },
        { "instock", new BsonArray
            {
                new BsonDocument { { "warehouse", "A" }, { "qty", 5 } },
                new BsonDocument { { "warehouse", "C" }, { "qty", 15 } } }
            }
    },
    new BsonDocument
    {
        { "item", "notebook" },
        { "instock", new BsonArray
            {
                new BsonDocument { { "warehouse", "C" }, { "qty", 5 } } }
            }
    },
    new BsonDocument
    {
        { "item", "paper" },
        { "instock", new BsonArray
            {
                new BsonDocument { { "warehouse", "A" }, { "qty", 60 } },
                new BsonDocument { { "warehouse", "B" }, { "qty", 15 } } }
            }
    },
    new BsonDocument
    {
        { "item", "planner" },
        { "instock", new BsonArray
            {
                new BsonDocument { { "warehouse", "A" }, { "qty", 40 } },
                new BsonDocument { { "warehouse", "B" }, { "qty", 5 } } }
            }
    },
    new BsonDocument
    {
        { "item", "postcard" },
        { "instock", new BsonArray
            {
                new BsonDocument { { "warehouse", "B" }, { "qty", 15 } },
                new BsonDocument { { "warehouse", "C" }, { "qty", 35 } } }
            }
    }
};
collection.InsertMany(documents);
```

## Query for a Document Nested in an Array

The following example selects all documents where an element in the
`instock` array matches the specified document:

```csharp
var filter = Builders<BsonDocument>.Filter.AnyEq("instock", new BsonDocument { { "warehouse", "A" }, { "qty", 5 } });
var result = collection.Find(filter).ToList();
```

Equality matches on the whole embedded/nested document require an
*exact* match of the specified document, including the field order. For
example, the following query does not match any documents in the
`inventory` collection:

```csharp
var filter = Builders<BsonDocument>.Filter.AnyEq("instock", new BsonDocument { { "qty", 5 }, { "warehouse", "A" } });
var result = collection.Find(filter).ToList();
```

## Specify a Query Condition on a Field in an Array of Documents

### Specify a Query Condition on a Field Embedded in an Array of Documents

If you do not know the index position of the document nested in the
array, concatenate the name of the array field, with a dot (`.`) and
the name of the field in the nested document.

The following example selects all documents where the `instock` array
has at least one embedded document that contains the field `qty`
whose value is less than or equal to `20`:

```csharp
var filter = Builders<BsonDocument>.Filter.Lte("instock.qty", 20);
var result = collection.Find(filter).ToList();
```

### Use the Array Index to Query for a Field in the Embedded Document

Using dot notation, you can specify query conditions for a
field in a document at a particular index or position of the array.
The array uses zero-based indexing.

**Note:**

When querying using dot notation, the field and index must be
inside quotation marks.

The following example selects all documents where the `instock` array
has as its first element a document that contains the field `qty`
whose value is less than or equal to `20`:

```csharp
var filter = Builders<BsonDocument>.Filter.Lte("instock.0.qty", 20);
var result = collection.Find(filter).ToList();
```

## Specify Multiple Conditions for Array of Documents

When you specify conditions on more than one field nested in an array
of documents, you can specify the query such that either a single
document meets these conditions or any combination of documents in the
array meets the conditions.

### A Single Nested Document Meets Multiple Query Conditions on Nested Fields

Use the `$elemMatch` operator to specify multiple criteria on
an array of embedded documents such that at least one embedded
document satisfies all the specified criteria.

The following example queries for documents where the `instock` array
has at least one embedded document that contains both the field
`qty` equal to `5` and the field `warehouse` equal
to `A`:

```csharp
var filter = Builders<BsonDocument>.Filter.ElemMatch<BsonValue>("instock", new BsonDocument { { "qty", 5 }, { "warehouse", "A" } });
var result = collection.Find(filter).ToList();
```

The following example queries for documents where the `instock` array
has at least one embedded document that contains the field `qty` that
is greater than `10` and less than or equal to `20`:

```csharp
var filter = Builders<BsonDocument>.Filter.ElemMatch<BsonValue>("instock", new BsonDocument { { "qty", new BsonDocument { { "$gt", 10 }, { "$lte", 20 } } } });
var result = collection.Find(filter).ToList();
```

### Combination of Elements Satisfies the Criteria

If the compound query conditions on an array field do not use the
`$elemMatch` operator, the query selects those documents whose
array contains any combination of elements that satisfies the
conditions.

For example, the following query matches documents where any document
nested in the `instock` array has the `qty` field greater than
`10` and any document (but not necessarily the same embedded
document) in the array has the `qty` field less than or equal to
`20`:

```csharp
var builder = Builders<BsonDocument>.Filter;
var filter = builder.And(builder.Gt("instock.qty", 10), builder.Lte("instock.qty", 20));
var result = collection.Find(filter).ToList();
```

The following example queries for documents where the `instock` array
has at least one embedded document that contains the field `qty`
equal to `5` and at least one embedded document (but not necessarily
the same embedded document) that contains the field `warehouse` equal
to `A`:

```csharp
var builder = Builders<BsonDocument>.Filter;
var filter = builder.And(builder.Eq("instock.qty", 5), builder.Eq("instock.warehouse", "A"));
var result = collection.Find(filter).ToList();
```

This page provides examples of query operations on an array of nested documents using
[mongoc_collection_find_with_opts](https://mongoc.org/libmongoc/current/mongoc_collection_find_with_opts.html).

The examples on this page use the `inventory` collection. Connect to a
test database in your MongoDB instance then create the `inventory`
collection:

(Code example not available offline: /driver-examples/test-mongoc-sample-commands.c)

## Query for a Document Nested in an Array

The following example selects all documents where an element in the
`instock` array matches the specified document:

(Code example not available offline: /driver-examples/test-mongoc-sample-commands.c)

Equality matches on the whole embedded/nested document require an
*exact* match of the specified document, including the field order. For
example, the following query does not match any documents in the
`inventory` collection:

(Code example not available offline: /driver-examples/test-mongoc-sample-commands.c)

## Specify a Query Condition on a Field in an Array of Documents

### Specify a Query Condition on a Field Embedded in an Array of Documents

If you do not know the index position of the document nested in the
array, concatenate the name of the array field, with a dot (`.`) and
the name of the field in the nested document.

The following example selects all documents where the `instock` array
has at least one embedded document that contains the field `qty`
whose value is less than or equal to `20`:

(Code example not available offline: /driver-examples/test-mongoc-sample-commands.c)

### Use the Array Index to Query for a Field in the Embedded Document

Using dot notation, you can specify query conditions for a
field in a document at a particular index or position of the array.
The array uses zero-based indexing.

**Note:**

When querying using dot notation, the field and index must be
inside quotation marks.

The following example selects all documents where the `instock` array
has as its first element a document that contains the field `qty`
whose value is less than or equal to `20`:

(Code example not available offline: /driver-examples/test-mongoc-sample-commands.c)

## Specify Multiple Conditions for Array of Documents

When you specify conditions on more than one field nested in an array
of documents, you can specify the query such that either a single
document meets these conditions or any combination of documents in the
array meets the conditions.

### A Single Nested Document Meets Multiple Query Conditions on Nested Fields

Use the `$elemMatch` operator to specify multiple criteria on
an array of embedded documents such that at least one embedded
document satisfies all the specified criteria.

The following example queries for documents where the `instock` array
has at least one embedded document that contains both the field
`qty` equal to `5` and the field `warehouse` equal
to `A`:

(Code example not available offline: /driver-examples/test-mongoc-sample-commands.c)

The following example queries for documents where the `instock` array
has at least one embedded document that contains the field `qty` that
is greater than `10` and less than or equal to `20`:

(Code example not available offline: /driver-examples/test-mongoc-sample-commands.c)

### Combination of Elements Satisfies the Criteria

If the compound query conditions on an array field do not use the
`$elemMatch` operator, the query selects those documents whose
array contains any combination of elements that satisfies the
conditions.

For example, the following query matches documents where any document
nested in the `instock` array has the `qty` field greater than
`10` and any document (but not necessarily the same embedded
document) in the array has the `qty` field less than or equal to
`20`:

(Code example not available offline: /driver-examples/test-mongoc-sample-commands.c)

The following example queries for documents where the `instock` array
has at least one embedded document that contains the field `qty`
equal to `5` and at least one embedded document (but not necessarily
the same embedded document) that contains the field `warehouse` equal
to `A`:

(Code example not available offline: /driver-examples/test-mongoc-sample-commands.c)

This page provides examples of query operations on an array of nested documents using the
`Collection.Find`
function in the
[MongoDB Go Driver](https://github.com/mongodb/mongo-go-driver/).

The examples on this page use the `inventory` collection. Connect to a
test database in your MongoDB instance then create the `inventory`
collection:

(Code example not available offline: /driver-examples/go_examples.go)

## Query for a Document Nested in an Array

The following example selects all documents where an element in the
`instock` array matches the specified document:

(Code example not available offline: /driver-examples/go_examples.go)

Equality matches on the whole embedded/nested document require an
*exact* match of the specified document, including the field order. For
example, the following query does not match any documents in the
`inventory` collection:

(Code example not available offline: /driver-examples/go_examples.go)

## Specify a Query Condition on a Field in an Array of Documents

### Specify a Query Condition on a Field Embedded in an Array of Documents

If you do not know the index position of the document nested in the
array, concatenate the name of the array field, with a dot (`.`) and
the name of the field in the nested document.

The following example selects all documents where the `instock` array
has at least one embedded document that contains the field `qty`
whose value is less than or equal to `20`:

(Code example not available offline: /driver-examples/go_examples.go)

### Use the Array Index to Query for a Field in the Embedded Document

Using dot notation, you can specify query conditions for a
field in a document at a particular index or position of the array.
The array uses zero-based indexing.

**Note:**

When querying using dot notation, the field and index must be
inside quotation marks.

The following example selects all documents where the `instock` array
has as its first element a document that contains the field `qty`
whose value is less than or equal to `20`:

(Code example not available offline: /driver-examples/go_examples.go)

## Specify Multiple Conditions for Array of Documents

When you specify conditions on more than one field nested in an array
of documents, you can specify the query such that either a single
document meets these conditions or any combination of documents in the
array meets the conditions.

### A Single Nested Document Meets Multiple Query Conditions on Nested Fields

Use the `$elemMatch` operator to specify multiple criteria on
an array of embedded documents such that at least one embedded
document satisfies all the specified criteria.

The following example queries for documents where the `instock` array
has at least one embedded document that contains both the field
`qty` equal to `5` and the field `warehouse` equal
to `A`:

(Code example not available offline: /driver-examples/go_examples.go)

The following example queries for documents where the `instock` array
has at least one embedded document that contains the field `qty` that
is greater than `10` and less than or equal to `20`:

(Code example not available offline: /driver-examples/go_examples.go)

### Combination of Elements Satisfies the Criteria

If the compound query conditions on an array field do not use the
`$elemMatch` operator, the query selects those documents whose
array contains any combination of elements that satisfies the
conditions.

For example, the following query matches documents where any document
nested in the `instock` array has the `qty` field greater than
`10` and any document (but not necessarily the same embedded
document) in the array has the `qty` field less than or equal to
`20`:

(Code example not available offline: /driver-examples/go_examples.go)

The following example queries for documents where the `instock` array
has at least one embedded document that contains the field `qty`
equal to `5` and at least one embedded document (but not necessarily
the same embedded document) that contains the field `warehouse` equal
to `A`:

(Code example not available offline: /driver-examples/go_examples.go)

This page provides examples of query operations on an array of nested documents using
MongoDB Compass. 

The examples on this page use the `inventory` collection. Connect to a
test database in your MongoDB instance then create the `inventory`
collection:

```javascript
[
    { "item": "journal", "instock": [ { "warehouse": "A", "qty": 5 }, { "warehouse": "C", "qty": 15 } ] },
    { "item": "notebook", "instock": [ { "warehouse": "C", "qty": 5 } ] },
    { "item": "paper", "instock": [ { "warehouse": "A", "qty": 60 }, { "warehouse": "B", "qty": 15 } ] },
    { "item": "planner", "instock": [ { "warehouse": "A", "qty": 40 }, { "warehouse": "B", "qty": 5 } ] },
    { "item": "postcard", "instock": [ { "warehouse": "B","qty": 15 }, { "warehouse": "C", "qty": 35 } ] }
]
```

For instructions on inserting documents in MongoDB Compass, see
Insert Documents.

## Query for a Document Nested in an Array

The following example selects all documents where an element in the
`instock` array matches the specified document:

Copy the following filter into the Compass query bar and click
Find:

```javascript
{ "instock": { warehouse: "A", qty: 5 } }
```

Equality matches on the whole embedded/nested document require an
*exact* match of the specified document, including the field order. For
example, the following query does not match any documents in the
`inventory` collection:

```javascript
instock: { qty: 5, warehouse: 'A' }
```

## Specify a Query Condition on a Field in an Array of Documents

### Specify a Query Condition on a Field Embedded in an Array of Documents

If you do not know the index position of the document nested in the
array, concatenate the name of the array field, with a dot (`.`) and
the name of the field in the nested document.

The following example selects all documents where the `instock` array
has at least one embedded document that contains the field `qty`
whose value is less than or equal to `20`:

Copy the following filter into the Compass query bar and click
Find:

```javascript
{ 'instock.qty': { $lte: 20 } }
```

(Figure: /images/compass-find-arr-embedded-field.png)

### Use the Array Index to Query for a Field in the Embedded Document

Using dot notation, you can specify query conditions for a
field in a document at a particular index or position of the array.
The array uses zero-based indexing.

**Note:**

When querying using dot notation, the field and index must be
inside quotation marks.

The following example selects all documents where the `instock` array
has as its first element a document that contains the field `qty`
whose value is less than or equal to `20`:

Copy the following filter into the Compass query bar and click
Find:

```javascript
{ 'instock.0.qty': { $lte: 20 } }
```

(Figure: /images/compass-find-embedded-field-arr-index.png)

## Specify Multiple Conditions for Array of Documents

When you specify conditions on more than one field nested in an array
of documents, you can specify the query such that either a single
document meets these conditions or any combination of documents in the
array meets the conditions.

### A Single Nested Document Meets Multiple Query Conditions on Nested Fields

Use the `$elemMatch` operator to specify multiple criteria on
an array of embedded documents such that at least one embedded
document satisfies all the specified criteria.

The following example queries for documents where the `instock` array
has at least one embedded document that contains both the field
`qty` equal to `5` and the field `warehouse` equal
to `A`:

Copy the following filter into the Compass query bar and click
Find:

```javascript
{ "instock": { $elemMatch: { qty: 5, warehouse: "A" } } }
```

(Figure: /images/compass-multiple-query-conditions-nested-fields.png)

The following example queries for documents where the `instock` array
has at least one embedded document that contains the field `qty` that
is greater than `10` and less than or equal to `20`:

Copy the following filter into the Compass query bar and click
Find:

```javascript
{ "instock": { $elemMatch: { qty: { $gt: 10, $lte: 20 } } } }
```

(Figure: /images/compass-multiple-query-conditions-nested-fields-2.png)

### Combination of Elements Satisfies the Criteria

If the compound query conditions on an array field do not use the
`$elemMatch` operator, the query selects those documents whose
array contains any combination of elements that satisfies the
conditions.

For example, the following query matches documents where any document
nested in the `instock` array has the `qty` field greater than
`10` and any document (but not necessarily the same embedded
document) in the array has the `qty` field less than or equal to
`20`:

Copy the following filter into the Compass query bar and click
Find:

```javascript
{ "instock.qty": { $gt: 10,  $lte: 20 } }
```

(Figure: /images/compass-arr-match-combo-of-elements.png)

The following example queries for documents where the `instock` array
has at least one embedded document that contains the field `qty`
equal to `5` and at least one embedded document (but not necessarily
the same embedded document) that contains the field `warehouse` equal
to `A`:

Copy the following filter into the Compass query bar and click
Find:

```javascript
{ "instock.qty": 5, "instock.warehouse": "A" }
```

(Figure: /images/compass-arr-match-combo-of-elements-2.png)

## Query an Array of Documents with MongoDB Atlas

This example uses the sample training dataset. To load the sample dataset into your
MongoDB Atlas deployment, see Load Sample Data.

To query an array of documents in MongoDB Atlas, follow these steps:

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
   sample_training database.
#. Select the grades collection.

**Step 3: Specify the Filter field**

Specify the query filter document
in the Filter field. A query filter document uses 
query operators to specify
search conditions.

Copy the following query filter document into the 
Filter search bar:

```javascript
{"scores.type": "exam"}
```

**Step 4: Click Apply**

This query filter returns all documents in the
`sample_training.grades` collection that contain a subdocument
in the `scores` array where `type` is set to `exam`. The
full document, including the entire `scores` array, is
returned. For more information on modifying the returned array,
see project-array-elements-in-returned-array.

## Additional Query Tutorials

For additional query examples, see:

- /tutorial/query-arrays

- /tutorial/query-documents

- /tutorial/query-embedded-documents
