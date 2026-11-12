<!-- Part 3 of 4 of tutorial/query-array-of-documents.md (split because the page is big). -->

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
