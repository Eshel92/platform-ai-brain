<!-- Converted from core/write-operations-atomicity.txt (reStructuredText). Includes are inlined. -->

# Atomicity and Transactions

In MongoDB, write operations are atomic on
the single-document level, even if modifying multiple values. For
parallel updates, each command ensures the query condition still
matches.

To prevent conflicts during concurrent updates, include the expected
current value in the update filter.

## Use Cases

The examples on this page use data from the sample_mflix dataset. For details on how to load this dataset into your self-managed
MongoDB deployment, see Load the Sample Dataset.
If you made any modifications to the sample databases, you may need to drop and
recreate the databases to run the examples on this page. 

Consider a collection with this document:

```javascript
db.movies.insertOne( { _id: 1, num_mflix_comments: 80 } )
```

These update operations occur concurrently:

```javascript
(
   // Update A
   db.movies.updateOne(
      { _id: 1, num_mflix_comments: 80 },
      {
         $set: { num_mflix_comments: 90 }
      }
   ),

   // Update B
   db.movies.updateOne(
      { _id: 1, num_mflix_comments: 80 },
      {
         $set: { num_mflix_comments: 100 }
      }
   )
)
```

One update sets `num_mflix_comments` to `90` or `100`. The
second update then fails to match `{ num_mflix_comments: 80 }` and
does not run.

**Warning:**

Filtering on a field you do not update can cause unexpected results
during concurrent updates. Consider these operations:

```javascript
(
   // Update A
   db.movies.updateOne(
      { _id: 1 },
      {
         $set: { num_mflix_comments: 90 }
      }
   ),

   // Update B
   db.movies.updateOne(
      { _id: 1 },
      {
         $set: { num_mflix_comments: 100 }
      }
   )
)
```

Both updates match `{ _id: 1 }`, so both run. The second update
overwrites the first. The first client receives no warning that its
update was lost.

To avoid conflicts when filtering on non-updated fields, use
`$inc`.

For example, consider the following concurrent update operations:

```javascript
(
   // Update A
   db.movies.updateOne(
      { _id: 1 },
      {
         $inc: { num_mflix_comments: 10 }
      }
   ),

   // Update B
   db.movies.updateOne(
      { _id: 1 },
      {
         $inc: { num_mflix_comments: 20 }
      }
   )
)
```

Both updates match `{ _id: 1 }`. Because they increment rather than
set the value, they do not overwrite each other. The final
`num_mflix_comments` is `110`.

**Tip:** Store Unique Values

To enforce uniqueness, create a unique index. This prevents duplicate data in inserts and
updates. You can also create unique indexes on multiple fields. See
index-unique-create.

## Details

This section describes additional details for multi-document
transactions.

When a single write operation (e.g.
`db.collection.updateMany()`) modifies multiple documents,
the modification of each document is atomic, but the operation as a
whole is not atomic.

When performing multi-document write operations, whether through a
single write operation or multiple write operations, other
operations may interleave.

For situations that require atomicity of reads and writes to multiple
documents (in a single or multiple collections), MongoDB supports
distributed transactions, including transactions on replica sets and 
sharded clusters.

For more information, see Transactions.

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

## Learn More

/core/read-isolation-consistency-recency
