<!-- Converted from reference/method/db.collection.distinct.txt (reStructuredText). Includes are inlined. -->

# db.collection.distinct() (mongosh method)

## Definition

**`db.collection.distinct(field, query, options)`**

(Include not available offline: includes/wayfinding/mongosh-method-distinct.rst)

Finds the distinct values for a specified field across a
single collection or view and returns the unique results
in an array.

## Compatibility

This method is available in deployments hosted in the following environments:

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas): The fully
  managed service for MongoDB deployments in the cloud

**Note:**

This command is supported in all MongoDB Atlas clusters.
For information on Atlas support for all commands, see 
Unsupported Commands.

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Syntax

This method takes the following parameters:

| Parameter | Type | Description |
|---|---|---|
| `field` | string | The field for which to return distinct values. |
| `query` | document | A query that specifies the documents from which to retrieve the distinct values. |
| `options` | document | Optional. A document that specifies the options.  See distinct-method-options. |

          
          

**Note:**

Results must not be larger than the maximum BSON size. If your results exceed the maximum
BSON size, use the aggregation pipeline to retrieve distinct
values using the `$group` operator, as described in
Retrieve Distinct Values with the Aggregation Pipeline.

The following diagram shows an example
`distinct()` call.

(Figure: /images/distinct.bakedsvg.svg)

## Options

```javascript
{ collation: <document> }
```

* - Field

  - Type

  - Description

* - `collation`

  - document

  - Optional. 

    Optional. Specifies the collation  to use for the operation.

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

       
       

## Behavior

In a sharded cluster, the `distinct` command may return
orphaned documents.

For time series collections, the
`distinct` command can't make efficient use of indexes. Instead, use a
`$group` aggregation to group documents by distinct values. For 
details, see Time Series Limitations.

### Array Fields

If the value of the specified `field` is an array,
`db.collection.distinct()` considers each element of the array
as a separate value.

For instance, if a field has as its value `[ 1, [1], 1 ]`, then
`db.collection.distinct()` considers `1`, `[1]`, and `1` as separate values.

For an example, see distinct-method-array.

### Index Use

When possible, `db.collection.distinct()` operations can use indexes.

Indexes can also cover
`db.collection.distinct()` operations. See covered-queries for more information
on queries covered by indexes.

### Transactions

To perform a distinct operation within a transaction:

- For unsharded collections, you can use the
  `db.collection.distinct()` method/the
  `distinct` command as well as the aggregation pipeline
  with the `$group` stage.

- For sharded collections, you cannot use the
  `db.collection.distinct()` method or the
  `distinct` command.

  To find the distinct values for a sharded collection, use the
  aggregation pipeline with the `$group` stage instead.
  See transactions-operations-distinct for details.

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
production-considerations.

### Client Disconnection

If the client that issued `distinct()` disconnects before the operation 
completes, MongoDB marks `distinct()` for termination using 
`killOp`.

### Replica Set Member State Restriction

To run on a replica set member, `distinct` operations require the member 
to be in `PRIMARY` or `SECONDARY` state. If the member
is in another state, such as `STARTUP2`, the
operation errors.

## Examples

The examples use the `inventory` collection that contains the
following documents:

```javascript
db.inventory.insertMany( [
   { _id: 1, dept: "A", item: { sku: "111", color: "red" }, sizes: [ "S", "M" ] },
   { _id: 2, dept: "A", item: { sku: "111", color: "blue" }, sizes: [ "M", "L" ] },
   { _id: 3, dept: "B", item: { sku: "222", color: "blue" }, sizes: "S" },
   { _id: 4, dept: "A", item: { sku: "333", color: "black" }, sizes: [ "S" ] }
] )
```

### Return Distinct Values for a Field

The following example returns distinct values for the `dept` field:

```javascript
db.inventory.distinct( "dept" )
```

The operation returns:

```javascript
[ "A", "B" ]
```

### Return Distinct Values for an Embedded Field

The following example returns distinct values for the embedded
`item.sku` field:

```javascript
db.inventory.distinct( "item.sku" )
```

The operation returns:

```javascript
[ "111", "222", "333" ]
```

**See also:**

document-dot-notation for information on accessing fields
within embedded documents

### Return Distinct Values for an Array Field

The following example returns distinct values for the `sizes`
array field:

```javascript
db.inventory.distinct( "sizes" )
```

The operation returns:

```javascript
[ "M", "S", "L" ]
```

For information on `distinct()` and array
fields, see the Behavior section.

### Specify Query with `distinct`

The following example returns distinct values for the embedded
`item.sku` field where `dept` equals `"A"`:

```javascript
db.inventory.distinct( "item.sku", { dept: "A" } )
```

The operation returns:

```javascript
[ "111", "333" ]
```

### Specify a Collation

Collation allows users to specify
language-specific rules for string comparison, such as rules for
lettercase and accent marks.

A collection `myColl` has the following documents:

```javascript
db.myColl.insertMany( [
   { _id: 1, category: "café", status: "A" },
   { _id: 2, category: "cafe", status: "a" },
   { _id: 3, category: "cafE", status: "a" }
] )
```

The following aggregation operation includes the collation
option:

```javascript
db.myColl.distinct( "category", {}, { collation: { locale: "fr", strength: 1 } } )
```

For descriptions on the collation fields, see
collation-document-fields.
