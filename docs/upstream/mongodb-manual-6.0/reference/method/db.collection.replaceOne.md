<!-- Converted from reference/method/db.collection.replaceOne.txt (reStructuredText). Includes are inlined. -->

# db.collection.replaceOne()

(Include not available offline: includes/wayfinding/mongosh-method-replaceOne.rst)

## Definition

**`db.collection.replaceOne(filter, replacement, options)`**

Replaces a single document within the collection based on the filter.

:returns:

  A document containing:

  - A boolean `acknowledged` as `true` if the operation ran with
    write concern or `false` if write concern was disabled
  - `matchedCount` containing the number of matched documents
  - `modifiedCount` containing the number of modified documents
  - `upsertedId` containing the `_id` for the upserted document

## Compatibility

This method is available in deployments hosted in the following environments:

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas?tck=docs_server): The fully
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

The `replaceOne()` method has the following form:

```javascript
db.collection.replaceOne(
   <filter>,
   <replacement>,
   {
      upsert: <boolean>,
      writeConcern: <document>,
      collation: <document>,
      hint: <document|string> 
   }
)
```

The `replaceOne()` method takes the following
parameters:

* - Parameter
  - Type   
  - Description

* - filter
  - document
  - .. _replace-one-filter:

    The selection criteria for the update. The same query
    selectors as in the `find()` method are available.

    Specify an empty document `{ }` to replace the first document returned in 
    the collection.

* - `replacement`
  - document   
  - The replacement document.

    Cannot contain update operators.

* - `upsert`
  - boolean
  - .. include:: /includes/extracts/replaceOne-behavior-method.rst

* - `writeConcern`
  - document
  - Optional. A document expressing the write concern. Omit to use the default write concern.

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

* - hint
  - document
  - .. _replace-one-hint:

    Optional. A document or string that specifies the index to use to support the filter.

    The option can take an index specification document or the index
    name string.

    If you specify an index that does not exist, the operation
    errors.

    For an example, see ex-replace-one-hint.
 

## Behavior

`replaceOne()` replaces the first matching document in
the collection that matches the `filter`, using the `replacement`
document.

### `upsert`

If `upsert: true` and no documents match the `filter`,
`db.collection.replaceOne()` creates a new document based on
the `replacement` document.

If you specify `upsert: true` on a sharded collection, you must
include the full shard key in the `filter`. For additional
`db.collection.replaceOne()` behavior on a sharded collection,
see replaceOne-sharded-collection.

See replaceOne-example-replace-with-upsert.

### Capped Collections

If a replacement operation changes the document size, the operation will fail.

### Time Series Collections

You cannot use the `replaceOne()` method on a
time series collection.

### Sharded Collections

`db.collection.replaceOne()` attempts to target a single shard, first by 
using the query filter. If the operation cannot target a single shard by the 
query filter, it then attempts to target by the replacement document. 

In earlier versions, the operation attempts to target using the
replacement document.

#### Shard Key Requirements In Replacement Document

The replacement document does not need to include the shard key. 

**Warning:**

Documents in sharded collections can be missing the shard key fields. 
Take precaution to avoid accidentally removing the shard key when changing 
a document's shard key value.

      

#### `upsert` on a Sharded Collection

A `db.collection.replaceOne()` operation that includes `upsert: true` 
on a sharded collection must include the full shard key in the `filter`.

However, documents in a sharded collection can be
missing the shard key fields. To target a
document that is missing the shard key, you can use the `null`
equality match in conjunction with another filter condition
(such as on the `_id` field). For example:

```javascript
{ _id: <value>, <shardkeyfield>: null } // _id of the document missing shard key
```

#### Shard Key Modification

You can update a document's shard key value unless the shard key field is the 
immutable `_id` field. 

**Warning:**

Documents in sharded collections can be missing the shard key fields. 
Take precaution to avoid accidentally removing the shard key when changing 
a document's shard key value.

To modify the **existing** shard key value with
`db.collection.replaceOne()`:

- You must run on a `mongos`. Do not
  issue the operation directly on the shard.

- You must run either in a transaction or as a retryable write. 

- You must include an equality filter on the full shard key.

#### Missing Shard Key

Documents in a sharded collection can be
missing the shard key fields. To use
`db.collection.replaceOne()` to set the document's
**missing** shard key, you must run on a
`mongos`. Do not issue the operation directly on
the shard.

In addition, the following requirements also apply:

* - Task

  - Requirements

* - To set to `null`

  - - Requires equality filter on the full shard key if ``upsert:
      true`` is specified.

* - To set to a non-`null` value

  - - Must be performed either inside a transaction or as a retryable write.

    - Requires equality filter on the full shard key if either:

      - `upsert: true`, or

      - the new shard key value belongs to a different shard.

**Tip:**

Since a missing key value is returned as part of a null equality
match, to avoid updating a null-valued key, include additional
query conditions (such as on the `_id` field) as appropriate.

See also:

- replaceOne-sharded-upsert

- shard-key-missing

### Transactions

`db.collection.replaceOne()` can be used inside distributed transactions.

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

#### Upsert within Transactions

You can create collections and indexes inside a distributed 
transaction if the
transaction is not a cross-shard write transaction.

`db.collection.replaceOne()` with `upsert: true` can be run on an existing
collection or a non-existing collection. If run on a non-existing
collection, the operation creates the collection.

**See also:**

transactions-create-collections-indexes

#### Write Concerns and Transactions

Do not explicitly set the write concern for the operation if run in
a transaction. To use write concern with transactions, see
transactions-write-concern.

## Examples

### Replace

The `restaurant` collection contains the  following documents:

```javascript
{ "_id" : 1, "name" : "Central Perk Cafe", "Borough" : "Manhattan" },
{ "_id" : 2, "name" : "Rock A Feller Bar and Grill", "Borough" : "Queens", "violations" : 2 },
{ "_id" : 3, "name" : "Empire State Pub", "Borough" : "Brooklyn", "violations" : 0 }
```

The following operation replaces a single document where
`name: "Central Perk Cafe"`:

```javascript
try {
   db.restaurant.replaceOne(
      { "name" : "Central Perk Cafe" },
      { "name" : "Central Pork Cafe", "Borough" : "Manhattan" }
   );
} catch (e){
   print(e);
}
```

The operation returns:

```javascript
{ "acknowledged" : true, "matchedCount" : 1, "modifiedCount" : 1 }
```

If no matches were found, the operation instead returns:

```javascript
{ "acknowledged" : true, "matchedCount" : 0, "modifiedCount" : 0 }
```

Setting `upsert: true` would insert the document if no match was found. See
replaceOne-example-replace-with-upsert

### Replace with Upsert

The `restaurant` collection contains the following documents:

```javascript
{ "_id" : 1, "name" : "Central Perk Cafe", "Borough" : "Manhattan",  "violations" : 3 },
{ "_id" : 2, "name" : "Rock A Feller Bar and Grill", "Borough" : "Queens", "violations" : 2 },
{ "_id" : 3, "name" : "Empire State Pub", "Borough" : "Brooklyn", "violations" : 0 }
```

The following operation attempts to replace the document with
`name : "Pizza Rat's Pizzaria"`, with `upsert : true`:

```javascript
try {
   db.restaurant.replaceOne(
      { "name" : "Pizza Rat's Pizzaria" },
      { "_id": 4, "name" : "Pizza Rat's Pizzaria", "Borough" : "Manhattan", "violations" : 8 },
      { upsert: true }
   );
} catch (e){
   print(e);
}
```

Since `upsert : true` the document is inserted based on the
`replacement` document. The operation returns:

```javascript
{
   "acknowledged" : true,
   "matchedCount" : 0,
   "modifiedCount" : 0,
   "upsertedId" : 4
}
```

The collection now contains the following documents:

```javascript
{ "_id" : 1, "name" : "Central Perk Cafe", "Borough" : "Manhattan", "violations" : 3 },
{ "_id" : 2, "name" : "Rock A Feller Bar and Grill", "Borough" : "Queens", "violations" : 2 },
{ "_id" : 3, "name" : "Empire State Pub", "Borough" : "Brooklyn", "violations" : 0 },
{ "_id" : 4, "name" : "Pizza Rat's Pizzaria", "Borough" : "Manhattan", "violations" : 8 }
```

### Replace with Write Concern

Given a three member replica set, the following operation specifies a
`w` of `majority` and `wtimeout` of `100`:

```javascript
try {
   db.restaurant.replaceOne(
       { "name" : "Pizza Rat's Pizzaria" },
       { "name" : "Pizza Rat's Pub", "Borough" : "Manhattan", "violations" : 3 },
       { w: "majority", wtimeout: 100 }
   );
} catch (e) {
   print(e);
}
```

If the acknowledgment takes longer than the `wtimeout` limit, the following
exception is thrown:

```javascript
WriteConcernError({
   "code" : 64,
   "errmsg" : "waiting for replication timed out",
   "errInfo" : {
     "wtimeout" : true,
     "writeConcern" : {
       "w" : "majority",
       "wtimeout" : 100,
       "provenance" : "getLastErrorDefaults"
     }
   }
})
```

The following table explains the possible values of
`errInfo.writeConcern.provenance`:

| Provenance | Description |
|---|---|
| `clientSupplied` | The write concern was specified in the application. |
| `customDefault` | The write concern originated from a custom defined default value. See `setDefaultRWConcern`. |
| `getLastErrorDefaults` | The write concern originated from the replica set's `settings.getLastErrorDefaults` field. |
| `implicitDefault` | The write concern originated from the server in absence of all other write concern specifications. |

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
db.myColl.replaceOne(
   { category: "cafe", status: "a" },
   { category: "cafÉ", status: "Replaced" },
   { collation: { locale: "fr", strength: 1 } }

);
```

### Specify `hint` for `replaceOne`

Create a sample `members` collection with the following documents:

```javascript
db.members.insertMany([
   { "_id" : 1, "member" : "abc123", "status" : "P", "points" :  0,  "misc1" : null, "misc2" : null },
   { "_id" : 2, "member" : "xyz123", "status" : "A", "points" : 60,  "misc1" : "reminder: ping me at 100pts", "misc2" : "Some random comment" },
   { "_id" : 3, "member" : "lmn123", "status" : "P", "points" :  0,  "misc1" : null, "misc2" : null },
   { "_id" : 4, "member" : "pqr123", "status" : "D", "points" : 20,  "misc1" : "Deactivated", "misc2" : null },
   { "_id" : 5, "member" : "ijk123", "status" : "P", "points" :  0,  "misc1" : null, "misc2" : null },
   { "_id" : 6, "member" : "cde123", "status" : "A", "points" : 86,  "misc1" : "reminder: ping me at 100pts", "misc2" : "Some random comment" }
])
```

Create the following indexes on the collection:

```javascript
db.members.createIndex( { status: 1 } )
db.members.createIndex( { points: 1 } )
```

The following update operation explicitly hints to use the index ``{
status: 1 }``:

**Note:**

If you specify an index that does not exist, the operation errors.

```javascript
db.members.replaceOne(
   { "points": { $lte: 20 }, "status": "P" }, 
   { "misc1": "using index on status", status: "P", member: "replacement", points: "20"},
   { hint: { status: 1 } }
)
```

The operation returns the following:

```javascript
{ "acknowledged" : true, "matchedCount" : 1, "modifiedCount" : 1 }
```

To view the indexes used, you can use the `$indexStats` pipeline:

```javascript
db.members.aggregate( [ { $indexStats: { } }, { $sort: { name: 1 } } ] )
```
