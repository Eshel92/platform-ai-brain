<!-- Converted from tutorial/enforce-uniqueness-on-non-shard-key-field.txt (reStructuredText). Includes are inlined. -->

# Enforce Uniqueness on a Field That Is Not the Shard Key

If you cannot use a unique field as the shard key, or if you need to
enforce uniqueness over multiple fields, create another
collection to act as a proxy collection.

## About this Task

A sharded cluster enforces a unique constraint across shards only when
the unique index is on the shard key or includes the shard key as a
prefix. A proxy collection works around
that constraint: the proxy collection contains both a reference to the
original document and the unique key, and your application writes to
the proxy collection first.

When you use a proxy collection, consider the following:

- Your application must catch errors when inserting documents into the
  proxy collection. Write to both collections in a transaction so that the collections cannot diverge if either
  insert fails.

- If the proxy collection requires sharding, you must shard on the
  single field on which you want to enforce uniqueness.

- Each field requires its own proxy collection. To enforce uniqueness
  on more than one field using sharded proxy collections, you must
  have one proxy collection for every field. If you create multiple
  unique indexes on a single proxy collection, you cannot shard the
  proxy collection.

- This approach requires generating the `_id` value in your
  application rather than letting MongoDB create it automatically on
  document insertion, so that both documents share the same `_id`.

For the full set of constraints that apply to unique indexes on
sharded collections, see manual-maintain-uniqueness-sharded.

## Before You Begin

- Identify the field that requires a unique constraint but cannot be
  part of the shard key.

- Confirm that no existing documents violate the uniqueness constraint
  for the field.

- Connect `mongosh` to a `mongos` instance.

## Steps

Consider a collection `records` that stores user information. The
field `email` is not the shard key, but needs to be unique. The
`proxy` collection contains the following fields:

```javascript
{
  "_id" : ObjectId("..."),
  "email" : "<string>"
}
```

**Step 1: Create the unique index on the proxy collection.**

Create a unique index on the `email` field of the `proxy`
collection:

```javascript
db.proxy.createIndex( { "email" : 1 }, { unique : true } )
```

Output:

```javascript
email_1
```

**Step 2: Write to both collections in a transaction.**

Insert a document containing the target field and a generated
unique ID into the `proxy` collection, then insert the full
document into the `records` collection. Run both inserts in a
transaction so that MongoDB either applies both writes or
neither:

```javascript
// Start a session
session = db.getMongo().startSession( { readPreference: { mode: "primary" } } );
proxy = session.getDatabase( db.getName() ).proxy;
records = session.getDatabase( db.getName() ).records;

var primary_id = ObjectId();

// Start a transaction
session.startTransaction( { readConcern: { level: "local" }, writeConcern: { w: "majority" } } );

// Operations inside the transaction
try {
   proxy.insertOne( {
      "_id" : primary_id,
      "email" : "example@example.net"
   } );

   records.insertOne( {
      "_id" : primary_id,
      "email" : "example@example.net",
      // additional information...
   } );
} catch (error) {
   // A duplicate email value fails the proxy insert and
   // cancels the transaction
   session.abortTransaction();
   throw error;
}
// Commit the transaction using write concern set at transaction start
session.commitTransaction();
session.endSession();
```

If the `email` value already exists in the `proxy`
collection, the unique index rejects the insert and the
transaction aborts, so no document is added to `records`.

## Learn More

- manual-maintain-uniqueness-sharded

- manual-create-unique-index-sharded

- manual-uniqueness-shard-key-values

- index-type-unique

- sharding-shard-key-unique

- `db.collection.createIndex`
