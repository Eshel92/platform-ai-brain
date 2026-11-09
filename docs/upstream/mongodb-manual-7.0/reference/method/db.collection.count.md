<!-- Converted from reference/method/db.collection.count.txt (reStructuredText). Includes are inlined. -->

# db.collection.count() (mongosh method)

**Important:** `mongosh` Method

This page documents a `mongosh` method. This is *not*
the documentation for database commands or language-specific drivers,
such as Node.js. 

For the database command, see the `count` command.

For MongoDB API drivers, refer to the language-specific
`MongoDB driver documentation`.

## Definition

**`db.collection.count(query, options)`**

Returns the count of documents that would match a
`find()` query for the collection or view,
without performing the find operation.

**Note:**

MongoDB drivers deprecate their respective cursor and collection 
`count()` APIs in favor of new APIs for `countDocuments()` 
and `estimatedDocumentCount()`. For the specific API names 
for a given driver, see the driver documentation.

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

The `db.collection.count()` method has the following form:

```javascript
db.collection.count(query, options)
```

### Parameters

This method takes the following parameters:

| Parameter | Type | Description |
|---|---|---|
| `query` | document | The query selection criteria. |
| `options` | document | Optional. Extra options for modifying the count. |

## Fields

The `options` document contains the following fields:

* - Field

  - Type

  - Description

* - `limit`

  - integer

  - Optional. The maximum number of documents to count.

* - `skip`

  - integer

  - Optional. The number of documents to skip before counting.

* - `hint`

  - string or document

  - Optional. An index name hint or specification for the query.

* - `maxTimeMS`

  - integer

  - Optional. The maximum amount of time to allow the query to run.

* - `readConcern`

  - string

  - Optional. Specifies the read concern. The default level is
    `"local"`.

    To ensure that a single thread can read its own writes, use
    `"majority"` read concern and `"majority"`
    write concern against the primary of the replica set.

    To use a read concern level of `"majority"`, you must
    specify a nonempty `query` condition.

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

          
          
   

`count()` is equivalent to the
`db.collection.find(query).count()` construct.

**See also:**

- `cursor.count()`
- `db.collection.estimatedDocumentCount()`
- `db.collection.countDocuments()`

## Behavior

### Inaccurate Counts Without Query Predicate

Without a query predicate, `count()` returns
results based on the collection's metadata, which may result in an
incorrect count. In particular,

- On a sharded cluster, the resulting count will not correctly
  filter out orphaned documents.

- After an unclean shutdown or file copy based initial sync, the count may be
  incorrect.

For counts based on collection metadata, see also
collStats pipeline stage with the count
option.

### Count and Transactions

You cannot use `count` and shell helpers
`cursor.count()` and `count()` in
transactions.

For details, see Transactions and Count Operations.

### Sharded Clusters

On a sharded cluster, `db.collection.count()` without a query predicate can result in an *inaccurate* count if
orphaned documents exist or if a
chunk migration is in progress.

To avoid these situations, on a sharded cluster, use the
`db.collection.aggregate()` method:

You can use the `$count` stage to count the documents. For
example, the following operation counts the documents in a collection:

```javascript
db.collection.aggregate( [
   { $count: "myCount" }
])
```

The `$count` stage is equivalent to the following
`$group` + `$project` sequence:

```javascript
db.collection.aggregate( [
   { $group: { _id: null, count: { $sum: 1 } } },
   { $project: { _id: 0 } }
] )
```

**See also:**

`$collStats` to return an approximate count based on the
collection's metadata.

### Index Use

Consider a collection with the following index:

```javascript
{ a: 1, b: 1 }
```

When performing a count, MongoDB can return the count using only the
index if:

- the query can use an index,

- the query only contains conditions on the keys of the index, *and*

- the query predicates access a single contiguous range of index keys.

For example, the following operations can return the count using only
the index:

```javascript
db.collection.find( { a: 5, b: 5 } ).count()
db.collection.find( { a: { $gt: 5 } } ).count()
db.collection.find( { a: 5, b: { $gt: 10 } } ).count()
```

If, however, the query can use an index but the query predicates do not
access a single contiguous range of index keys or the query also
contains conditions on fields outside the index, then in addition to
using the index, MongoDB must also read the documents to return the
count.

```javascript
db.collection.find( { a: 5, b: { $in: [ 1, 2, 3 ] } } ).count()
db.collection.find( { a: { $gt: 5 }, b: 5 } ).count()
db.collection.find( { a: 5, b: 5, c: 5 } ).count()
```

In such cases, during the initial read of the documents, MongoDB pages
the documents into memory such that subsequent calls of the same count
operation will have better performance.

### Accuracy after Unexpected Shutdown

After an unclean shutdown of a `mongod` using the Wired Tiger storage engine, count statistics reported by
`count()` may be inaccurate.

The amount of drift depends on the number of insert, update, or delete
operations performed between the last checkpoint and the unclean shutdown. Checkpoints
usually occur every 60 seconds. However, `mongod` instances running
with non-default `--syncdelay` settings may have more or less frequent
checkpoints.

Run `validate` on each collection on the `mongod`
to restore statistics after an unclean shutdown.

After an unclean shutdown:

- `validate` updates the count statistic in the `collStats` output with the latest value.

- Other statistics like the number of documents inserted or removed in
  the `collStats` output are
  estimates.

**Note:**

This loss of accuracy only applies to `count()`
operations that do *not* include a query predicate.

### Client Disconnection

If the client that issued `count()` disconnects before the operation 
completes, MongoDB marks `count()` for termination using 
`killOp`.

## Examples

### Count all Documents in a Collection

To count all documents in the `orders` collection:

```javascript
db.orders.count()
```

The equivalent operation is:

```javascript
db.orders.find().count()
```

### Count all Documents that Match a Query

Count documents in the `orders` collection where `ord_dt`
is greater than `new Date('01/01/2012')`:

```javascript
db.orders.count( { ord_dt: { $gt: new Date('01/01/2012') } } )
```

The equivalent operation is:

```javascript
db.orders.find( { ord_dt: { $gt: new Date('01/01/2012') } } ).count()
```
