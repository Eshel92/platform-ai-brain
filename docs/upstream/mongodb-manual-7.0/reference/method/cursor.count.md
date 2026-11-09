<!-- Converted from reference/method/cursor.count.txt (reStructuredText). Includes are inlined. -->

# cursor.count() (mongosh method)

## Definition

**`cursor.count()`**

**Important:** `mongosh` Method

This page documents a `mongosh` method. This is *not*
the documentation for a language-specific driver, such as Node.js.

For MongoDB API drivers, refer to the language-specific
`MongoDB driver documentation`.

**Note:**

MongoDB drivers deprecate their respective cursor and collection 
`count()` APIs in favor of new APIs that corresponds to 
`countDocuments()` and `estimatedDocumentCount()`. For the 
specific API names for a given driver, see the driver API 
documentation.

Counts the number of documents referenced by a cursor. Append the
`count()` method to a
`find()` query to return the number of
matching documents. The operation does not perform the query but
instead counts the results that would be returned by the query.

The `count()` method has the following
prototype form:

```javascript
db.collection.find(<query>).count()
```

The `count()` method has the following
parameter:

| Parameter | Type | Description |
|---|---|---|
| `applySkipLimit` | boolean | Optional. Specifies whether to consider the effects of the `cursor.skip()` and `cursor.limit()` methods in the count. By default, the `count()` method ignores the effects of the `cursor.skip()` and `cursor.limit()`. Set `applySkipLimit` to `true` to consider the effect of these methods. |

MongoDB also provides an equivalent `db.collection.count()`
as an alternative to the `db.collection.find(<query>).count()`
construct.

MongoDB supports the use of `hint()` with
`count()`. See count-method-hint for an
example.

**See also:**

`cursor.size()`

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

## Behavior

### Inaccurate Counts Without Query Predicate

When you call `count()` on a
`find()` operation which does not specify a query
predicate, the `count()` method can return inaccurate
document counts. These `count()` methods return results
based on the collection's metadata, which may result in an approximate
count. In particular,

- On a sharded cluster, the resulting count will not correctly
  filter out orphaned documents.

- After an unclean shutdown or file copy based initial sync, the count may be
  incorrect.

For counts based on collection metadata, see also
collStats pipeline stage with the count
option.

### Count and Transactions

You cannot use `count` and shell helpers
`count()` and `db.collection.count()` in
transactions.

For details, see Transactions and Count Operations.

### Sharded Clusters

On a sharded cluster, `count()` without a query predicate in the `find` can result in an *inaccurate* count if
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

## Examples

The following are examples of the `count()` method.

### Count All Documents

The following operation counts the number of all documents in the
`orders` collection:

```javascript
db.orders.find().count()
```

### Count Documents That Match a Query

The following operation counts the number of the documents in the
`orders` collection with the field `ord_dt` greater than ``new
Date('01/01/2012')``:

```javascript
db.orders.find( { ord_dt: { $gt: new Date('01/01/2012') } } ).count()
```

### Limit Documents in Count

The following operation counts the number of the documents in the
`orders` collection with the field `ord_dt` greater than ``new
Date('01/01/2012')`` *taking into account* the effect of the
`limit(5)`:

```javascript
db.orders.find( { ord_dt: { $gt: new Date('01/01/2012') } } ).limit(5).count(true)
```

### Specify the Index to Use

The following operation uses the index named `"status_1"`, which has
the index key specification of `{ status: 1 }`, to return a count of
the documents in the `orders` collection with the field `ord_dt`
greater than `new Date('01/01/2012')` and the `status` field is
equal to `"D"`:

```javascript
db.orders.find(
   { ord_dt: { $gt: new Date('01/01/2012') }, status: "D" }
).hint( "status_1" ).count()
```
