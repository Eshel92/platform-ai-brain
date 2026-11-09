<!-- Converted from reference/command/distinct.txt (reStructuredText). Includes are inlined. -->

# distinct

## Definition

**`distinct`**

Finds the distinct values for a specified field across a single
collection. `distinct` returns a document that contains
an array of the distinct values. The return document also contains
an embedded document with query statistics and the query plan.

**Tip:**

In `mongosh`, this command can also be run through the `db.collection.distinct()` helper method.

Helper methods are convenient for `mongosh` users, but they may not
return the same level of information as database commands.  In cases where
the convenience is not needed or the additional return fields are required,
use the database command.

## Compatibility

This command is available in deployments hosted in the following environments: 

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas?tck=docs_server): The fully
  managed service for MongoDB deployments in the cloud

**Important:**

This command has limited support in M0, M2, M5, and Flex clusters.
For more information, see Unsupported Commands.

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Syntax

The command has the following syntax:

```javascript
db.runCommand(
   {
     distinct: "<collection>",
     key: "<field>",
     query: <query>,
     readConcern: <read concern document>,
     collation: <collation document>,
     comment: <any>
   }
)
```

## Command Fields

The command takes the following fields:

* - Field
  - Type
  - Description

* - `distinct`
  - string
  - The name of the collection to query for distinct values.

* - `key`
  - string
  - The field for which to return distinct values.

* - `query`
  - document
  - Optional. A query that specifies the documents from which to retrieve the
    distinct values.

* - `readConcern`
  - document
  - Optional. Specifies the read concern.

    The `readConcern` option has the following syntax: 
    `readConcern: { level: <value> }`

    Possible read concern levels are:

    - `"local"`. This is the default read concern level for
      read operations against the primary and secondaries.

    - `"available"`. Available for read operations against
      the primary and secondaries. `"available"` behaves the 
      same as `"local"` against the primary and non-sharded
      secondaries. The query returns the instance's most recent data.

    - `"majority"`. Available for replica sets that use
      WiredTiger storage engine.

    - `"linearizable"`. Available for read operations on the
      `primary` only.

    - `"snapshot"`. Available for multi-document
      transactions, and starting in MongoDB 5.0, certain
      read operations outside of multi-document transactions.

    For more formation on the read concern levels, see
    read-concern-levels.

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

* - `comment`
  - any
  - .. include:: /includes/extracts/comment-content.rst

**Note:**

Results must not be larger than the maximum BSON size. If your results exceed the maximum
BSON size, use the aggregation pipeline to retrieve distinct
values using the `$group` operator, as described in
Retrieve Distinct Values with the Aggregation Pipeline.

MongoDB also provides the shell wrapper method
`db.collection.distinct()` for the `distinct`
command. Additionally, many MongoDB drivers
provide a wrapper method. Refer to the specific driver documentation.

## Behavior

In a sharded cluster, the `distinct` command may return
orphaned documents.

For time series collections, the
`distinct` command can't make efficient use of indexes. Instead, use a
`$group` aggregation to group documents by distinct values. For 
details, see Time Series Limitations.

### Array Fields

If the value of the specified `field` is an array,
`distinct` considers each element of the array
as a separate value.

For instance, if a field has as its value `[ 1, [1], 1 ]`, then
`distinct` considers `1`, `[1]`, and `1` as separate values.

Starting in MongoDB 6.0, the `distinct` command returns the
same results for collections and views when
using arrays.

For examples, see:

- distinct-command-array
- distinct-arrays-in-collections-and-views

### Index Use

When possible, `distinct` operations can use indexes.

Indexes can also cover
`distinct` operations. See covered-queries for more information
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
/core/transactions-production-consideration.

### Client Disconnection

Starting in MongoDB 4.2, if the client that issued `distinct`
disconnects before the operation completes, MongoDB marks `distinct` 
for termination using `killOp`.

### Replica Set Member State Restriction

To run on a replica set member, `distinct` operations require the member 
to be in `PRIMARY` or `SECONDARY` state. If the member
is in another state, such as `STARTUP2`, the
operation errors.

### Index Filters and Collations

Starting in MongoDB 6.0, an index filter uses the collation previously set using the `planCacheSetFilter`
command.

## Examples

The examples use the `inventory` collection that contains the
following documents:

```javascript
{ "_id": 1, "dept": "A", "item": { "sku": "111", "color": "red" }, "sizes": [ "S", "M" ] }
{ "_id": 2, "dept": "A", "item": { "sku": "111", "color": "blue" }, "sizes": [ "M", "L" ] }
{ "_id": 3, "dept": "B", "item": { "sku": "222", "color": "blue" }, "sizes": "S" }
{ "_id": 4, "dept": "A", "item": { "sku": "333", "color": "black" }, "sizes": [ "S" ] }
```

### Return Distinct Values for a Field

The following example returns the distinct values for the field
`dept` from all documents in the `inventory` collection:

```javascript
db.runCommand ( { distinct: "inventory", key: "dept" } )
```

The command returns a document with a field named `values` that
contains the distinct `dept` values:

```javascript
{
   "values" : [ "A", "B" ],
   "ok" : 1
}
```

### Return Distinct Values for an Embedded Field

The following example returns the distinct values for the field
`sku`, embedded in the `item` field, from all documents in the
`inventory` collection:

```javascript
db.runCommand ( { distinct: "inventory", key: "item.sku" } )
```

The command returns a document with a field named `values` that
contains the distinct `sku` values:

```javascript
{
  "values" : [ "111", "222", "333" ],
  "ok" : 1
}
```

**See also:**

document-dot-notation for information on accessing fields
within embedded documents

### Return Distinct Values for an Array Field

The following example returns the distinct values for the field
`sizes` from all documents in the `inventory` collection:

```javascript
db.runCommand ( { distinct: "inventory", key: "sizes" } )
```

The command returns a document with a field named `values` that
contains the distinct `sizes` values:

```javascript
{
  "values" : [ "M", "S", "L" ],
  "ok" : 1
}
```

For information on `distinct` and array fields, see the
Behavior section.

### Arrays in Collections and Views

Starting in MongoDB 6.0, the `distinct` command returns the
same results for collections and views when
using arrays.

The following example creates a collection named `sensor` with
an array of temperature values for each document:

```javascript
db.sensor.insertMany( [
   { _id: 0, temperatures: [ { value: 1 }, { value: 4 } ] },
   { _id: 1, temperatures: [ { value: 2 }, { value: 8 } ] },
   { _id: 2, temperatures: [ { value: 3 }, { value: 12 } ] },
   { _id: 3, temperatures: [ { value: 1 }, { value: 4 } ] }
] )
```

The following example creates a view named `sensorView` from the
`sensor` collection:

```javascript
db.createView( "sensorView", "sensor", [] )
```

The following example uses `distinct` to return the unique
values from the `temperatures` array in the `sensor` collection:

```javascript
db.sensor.distinct( "temperatures.1.value" )
```

The `1` in `temperatures.1.value` specifies the `temperatures`
array index.

Example output:

```javascript
[ 4, 8, 12 ]
```

Example for `sensorView`:

```javascript
db.sensorView.distinct( "temperatures.1.value" )
```

Example output:

- `[ 4, 8, 12 ]` starting in MongoDB 6.0 (identical to result
  returned from the `sensor` collection).
- `[]` in MongoDB versions earlier than 6.0.

### Specify Query with `distinct`

The following example returns the distinct values for the field
`sku`, embedded in the `item` field, from the documents whose
`dept` is equal to `"A"`:

```javascript
db.runCommand ( { distinct: "inventory", key: "item.sku", query: { dept: "A"} } )
```

The command returns a document with a field named `values` that
contains the distinct `sku` values:

```javascript
{
  "values" : [ "111", "333" ],
  "ok" : 1
}
```

### Specify a Collation

Collation allows users to specify
language-specific rules for string comparison, such as rules for
lettercase and accent marks.

A collection `myColl` has the following documents:

```javascript
{ _id: 1, category: "café", status: "A" }
{ _id: 2, category: "cafe", status: "a" }
{ _id: 3, category: "cafE", status: "a" }
```

The following aggregation operation includes the collation
option:

```javascript
db.runCommand( 
   { 
      distinct: "myColl",
      key: "category",
      collation: { locale: "fr", strength: 1 } 
   }
)
```

For descriptions on the collation fields, see
collation-document-fields.

### Override Default Read Concern

To override the default read concern level of `"local"`,
use the `readConcern` option.

The following operation on a replica set specifies a
/reference/read-concern of `"majority"` to read the
most recent copy of the data confirmed as having been written to a
majority of the nodes.

**Note:**

Regardless of the read concern level, the most recent data on a
node may not reflect the most recent version of the data in the system.

```javascript
db.runCommand(
   {
     distinct: "restaurants",
     key: "rating",
     query: { cuisine: "italian" },
     readConcern: { level: "majority" }
   }
)
```

To ensure that a single thread can read its own writes, use
`"majority"` read concern and `"majority"`
write concern against the primary of the replica set.
