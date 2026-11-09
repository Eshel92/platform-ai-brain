<!-- Converted from reference/method/db.collection.remove.txt (reStructuredText). Includes are inlined. -->

# db.collection.remove()

**Important:** Deprecated `mongosh` Method

This method is deprecated in `mongosh`. For alternative
methods, see compatibility.

## Definition

**`db.collection.remove()`**

Removes documents from a collection.

:returns: A writeresults-remove object that contains the
   status of the operation.

## Syntax

The `db.collection.remove()` method can have one of two
syntaxes. The `remove()` method can take a
query document and an optional `justOne` boolean:

```javascript
db.collection.remove(
    <query>,
    <justOne>
)
```

Or the method can take a query document and an optional remove
options document:

**Changed in version:** 5.0

```javascript
db.collection.remove(
    <query>,
    {
      justOne: <boolean>,
      writeConcern: <document>,
      collation: <document>,
      let: <document> // Added in MongoDB 5.0
    }
)
```

The `remove()` method takes the following
parameters:

* - Parameter
  - Type
  - Description

* - `query`
  - document
  - Specifies deletion criteria using query operators. To delete all documents in a collection,
    pass an empty document (`{}`).

* - `justOne`
  - boolean 
  - Optional. To limit the deletion to just one document, set to `true`. Omit to
    use the default value of `false` and delete all documents matching
    the deletion criteria.

* - `writeConcern`
  - document
  - Optional. A document expressing the write concern. Omit to use the default write concern.
    See remove-wc.

    Do not explicitly set the write concern for the operation if run in
    a transaction. To use write concern with transactions, see
    transactions-write-concern.

* - `collation`
  - document
  - Optional. 

    Specifies the collation  to use for the operation.

    Collation allows users to specify
    language-specific rules for string comparison, such as rules for
    lettercase and accent marks.

    The collation option has the following syntax:

    ```none
    collation: {
       locale: <string>,
       caseLevel: <boolean>,
       caseFirst: <string>,
       strength: <int>,
       numericOrdering: <boolean>,
       alternate: <string>,
       maxVariable: <string>,
       backwards: <boolean>
    }
    ```

    When specifying collation, the `locale` field is mandatory; all
    other collation fields are optional. For descriptions of the fields,
    see collation-document-fields.

    If the collation is unspecified but the collection has a
    default collation (see `db.createCollection()`), the
    operation uses the collation specified for the collection.

    If no collation is specified for the collection or for the
    operations, MongoDB uses the simple binary comparison used in prior
    versions for string comparisons.

    You cannot specify multiple collations for an operation. For
    example, you cannot specify different collations per field, or if
    performing a find with a sort, you cannot use one collation for the
    find and another for the sort.

* - let
  - document
  - .. _db.collection.remove-let-syntax:

    Optional. 

    Specifies a document with a list of variables. This allows you to
    improve command readability by separating the variables from the query
    text.

    The document syntax is:

    ```javascript
    { 
      <variable_name_1>: <expression_1>,
      ...,
      <variable_name_n>: <expression_n>
    }
    ```

    The variable is set to the value returned by the expression, and cannot
    be changed afterwards.

    To access the value of a variable in the command, use the double
    dollar sign prefix (`$$`) together with your variable name in the form
    `$$<variable_name>`. For example: `$$targetTotal`.

    To use a variable to filter results, you must access the variable
    within the `$expr` operator.

    For a complete example using `let` and variables, see
    db.collection.remove-let-example.

    **New in version:** 5.0

## Behavior

### Write Concern

The `remove()` method uses the
`delete` command, which uses the default write concern. To specify a different write concern,
include the write concern in the options parameter.

### Query Considerations

By default, `remove()` removes all documents
that match the `query` expression. Specify the `justOne` option to
limit the operation to removing a single document. To delete a single
document sorted by a specified order, use the findAndModify() method.

When removing multiple documents, the remove operation may interleave
with other read and/or write operations to the collection.

### Time Series Collections

You cannot use the `remove()` method on a
time series collection.

### Sharded Collections

To use `remove()` operations for a sharded
collection that specify the `justOne: true` option: 

- If you only target one shard, you can use a partial shard key in the query specification or,

- You can provide the shard key or the `_id` field in the query
  specification.

### Transactions

`db.collection.remove()` can be used inside distributed transactions.

Do not explicitly set the write concern for the operation if run in
a transaction. To use write concern with transactions, see
transactions-write-concern.

**Important:**

In most cases, a distributed transaction incurs a greater
performance cost over single document writes, and the
availability of distributed transactions should not be a
replacement for effective schema design. For many scenarios, the
denormalized data model (embedded documents and arrays) will continue to be optimal for your
data and use cases. That is, for many scenarios, modeling your data
appropriately will minimize the need for distributed
transactions. 

For additional transactions usage considerations
(such as runtime limit and oplog size limit), see also
/core/transactions-production-consideration.

## Examples

The following are examples of the `remove()` method.

### Remove All Documents from a Collection

To remove all documents in a collection, call the `remove` method with an empty query document `{}`.
The following operation deletes all documents from the bios
collection:

```javascript
db.bios.remove( { } )
```

This operation is not equivalent to the
`drop()` method.

To remove all documents from a collection, it may be more efficient
to use the `drop()` method to drop the entire
collection, including the indexes, and then recreate the collection
and rebuild the indexes.

### Remove All Documents that Match a Condition

To remove the documents that match a deletion criteria, call the
`remove()` method with the `<query>`
parameter:

The following operation removes all the documents from the collection
`products` where `qty` is greater than `20`:

```javascript
db.products.remove( { qty: { $gt: 20 } } )
```

### Override Default Write Concern

The following operation to a replica set removes all the documents from
the collection `products` where `qty` is greater than `20` and
specifies a write concern of `w: 2`
with a `wtimeout` of 5000 milliseconds. This operation either returns
after the write propagates to both the primary and one secondary, or
times out after 5 seconds.

```javascript
db.products.remove(
    { qty: { $gt: 20 } },
    { writeConcern: { w: "majority", wtimeout: 5000 } }
)
```

### Remove a Single Document that Matches a Condition

To remove the first document that match a deletion criteria, call the
`remove` method with the `query`
criteria and the `justOne` parameter set to `true` or `1`.

The following operation removes the first document from the collection
`products` where `qty` is greater than `20`:

```javascript
db.products.remove( { qty: { $gt: 20 } }, true )
```

### Specify Collation

Collation allows users to specify
language-specific rules for string comparison, such as rules for
lettercase and accent marks.

A collection `myColl` has the following documents:

```javascript
{ _id: 1, category: "café", status: "A" }
{ _id: 2, category: "cafe", status: "a" }
{ _id: 3, category: "cafE", status: "a" }
```

The following operation includes the collation
option:

```javascript
db.myColl.remove( 
   { category: "cafe", status: "A" }, 
   { collation: { locale: "fr", strength: 1 } }
)
```

### Use Variables in `let`

**New in version:** 5.0

To define variables that you can access elsewhere in the command, use
the let option.

**Note:**

To filter results using a variable, you must access the variable
within the `$expr` operator.

Create a collection `cakeFlavors`:

```javascript
db.cakeFlavors.insertMany( [
   { _id: 1, flavor: "chocolate" },
   { _id: 2, flavor: "strawberry" },
   { _id: 3, flavor: "cherry" }
] )
```

The following example defines a `targetFlavor` variable in `let` and
uses the variable to delete the strawberry cake flavor:

```javascript
db.cakeFlavors.remove(
   { $expr: { $eq: [ "$flavor", "$$targetFlavor" ] } },
   { let : { targetFlavor: "strawberry" } }
)
```

## WriteResult

### Successful Results

The `remove()` returns a `WriteResult`
object that contains the status of the operation. Upon success, the
`WriteResult` object contains information on the number of
documents removed:

```javascript
WriteResult({ "nRemoved" : 4 })
```

**See also:**

`WriteResult.nRemoved`

### Write Concern Errors

If the `remove()` method encounters write
concern errors, the results include the
`WriteResult.writeConcernError` field:

```javascript
WriteResult({
  "nRemoved" : 7,
  "writeConcernError" : {
    "code" : 64,
    "codeName" : "WriteConcernTimeout",
    "errmsg" : "waiting for replication timed out",
    "errInfo" : {
      "wtimeout" : true,
      "writeConcern" : { 
        "w" : "majority",
        "wtimeout" : 1,
        "provenance" : "getLastErrorDefaults"
      }
    }
  }
})
```

**See also:**

- `WriteResult.writeConcernError`

### Errors Unrelated to Write Concern

If the `remove()` method encounters a non-write
concern error, the results include `WriteResult.writeError` field:

```javascript
WriteResult({
   "nRemoved" : 0,
   "writeError" : {
      "code" : 2,
      "errmsg" : "unknown top level operator: $invalidFieldName"
   }
})
```
