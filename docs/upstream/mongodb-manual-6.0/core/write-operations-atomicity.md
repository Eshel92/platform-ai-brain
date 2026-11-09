<!-- Converted from core/write-operations-atomicity.txt (reStructuredText). Includes are inlined. -->

# Atomicity and Transactions

In MongoDB, a write operation is atomic on
the level of a single document, even if the operation modifies multiple
values. When multiple update commands happen in parallel, each
individual command ensures that the query condition still matches.

To guarantee that concurrent update commands do not conflict with each
other, you can specify the expected current value of a field in the
update filter.

## Example

Consider a collection with this document:

```javascript
db.games.insertOne( { _id: 1, score: 80 } )
```

These update operations occur concurrently:

```javascript
// Update A
db.games.updateOne(
   { score: 80 },
   {
      $set: { score: 90 }
   }
)

// Update B
db.games.updateOne(
   { score: 80 },
   {
      $set: { score: 100 }
   }
)
```

One update operation sets the document's `score` field to either
`90` or `100`. After this update completes, the second update
operation no longer matches the query predicate `{ score: 80 }`, and
is not performed.

**Warning:**

In the case of concurrent update operations, specifying a filter on a
field that is not being updated can lead to unexpected results. For
example, consider if these update operations occur concurrently:

```javascript
// Update A
db.games.updateOne(
   { _id: 1 },
   {
      $set: { score: 90 }
   }
)

// Update B
db.games.updateOne(
   { _id: 1 },
   {
      $set: { score: 100 }
   }
)
```

After one update operation completes, the remaining operation still
matches the query predicate `{ _id: 1 }`. As a result, both update
operations occur and the stored `score` value reflects the second
update operation. This is problematic because the client that issued the
first update does not receive any indication that the update was
overwritten and the `score` value is different than expected.

To prevent conflicting write operations when your update filter is on a
different field than the one being updated, use the `$inc`
operator.

For example, consider if these update operations occur concurrently:

```javascript
// Update A
db.games.updateOne(
   { _id: 1 },
   {
      $inc: { score: 10 }
   }
)

// Update B
db.games.updateOne(
   { _id: 1 },
   {
      $inc: { score: 20 }
   }
)
```

After one update operation completes, the remaining operation still
matches the query predicate `{ _id: 1 }`. However, because the
operations modify the current value of `score`, they don't overwrite
each other. Both updates are reflected and the resulting `score` is
`110`.

**Tip:** Store Unique Values

To ensure that a field only has unique values, you can create a
unique index. Unique indexes prevent inserts
and updates from creating duplicate data. You can create a unique index
on multiple fields to ensure the combination of field values is unique.
For examples, see index-unique-create.

### Multi-Document Transactions

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

For more information, see transactions

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

### Learn More

/core/read-isolation-consistency-recency
