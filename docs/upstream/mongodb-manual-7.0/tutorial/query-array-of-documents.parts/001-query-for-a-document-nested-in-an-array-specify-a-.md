<!-- Part 1 of 4 of tutorial/query-array-of-documents.md (split because the page is big). -->

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
