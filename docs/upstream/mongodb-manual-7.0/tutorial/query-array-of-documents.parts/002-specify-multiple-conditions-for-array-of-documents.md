<!-- Part 2 of 4 of tutorial/query-array-of-documents.md (split because the page is big). -->

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
