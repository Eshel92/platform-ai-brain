<!-- Converted from core/sharding-shard-key.txt (reStructuredText). Includes are inlined. -->

# Shard Keys

The shard key is either a single indexed field or multiple
fields covered by a compound index that determines the
distribution of the collection's documents among the
cluster's shards.

MongoDB divides the span of shard key values (or hashed
shard key values) into non-overlapping ranges of shard key values (or
hashed shard key values). Each range is associated with a
chunk, and MongoDB attempts to distribute chunks evenly among
the shards in the cluster.

(Figure: /images/sharding-range-based.bakedsvg.svg)

The shard key has a direct relationship to the effectiveness of chunk
distribution. See sharding-shard-key-selection.

## Shard Key Indexes

Sharded collections typically require an index that supports the
shard key. The index can be an index on the shard key or a
compound index where the shard key is a prefix of the index.

- If the collection is empty, `sh.shardCollection()` creates
  the index on the shard key if such an index does not already exists.

- If the collection is not empty, you must create the index first
  before using `sh.shardCollection()`.

You cannot drop or 
hide an index if it is the only 
non-hidden index that supports the shard key.

Starting in MongoDB 6.0.12 and 5.0.22, you can drop the index
for a hashed shard key. For details,
see /tutorial/drop-a-hashed-shard-key-index.
 

### Unique Indexes

MongoDB can enforce a uniqueness constraint on a ranged shard key index.
Through the use of a unique index on the shard key, MongoDB enforces
uniqueness on the entire key combination and not individual components
of the shard key.

For a ranged sharded collection, only the following indexes can be
unique:

- The index on the shard key

- A compound index where the shard key is a prefix

- The default `_id` index; however, the `_id` index only
  enforces the uniqueness constraint **per shard** if the `_id` field
  is not the shard key.

**Important:**

Sharded clusters only enforce the uniqueness constraint on `_id` fields 
across the cluster when the `_id` field is also the shard key.

If the `_id` field is not the shard key or if it is only the prefix to the
shard key, the uniqueness constraint only applies to the shard that 
stores the document. This means that two or more documents can have
the same `_id` value, provided they occur on different shards.

For example, consider a sharded collection with shard key ``{x:
1}` that spans two shards A and B. Because the `_id`` key is
not the shard key, the collection could have a document
with `_id` value `1` in shard A and another document with
`_id` value `1` in shard B.

In cases where the `_id` field is not the shard key, MongoDB expects
applications to enforce the uniqueness of `_id` values across the shards.

The unique index constraints mean that:

- For a to-be-sharded collection, you cannot shard the collection if
  the collection has multiple unique indexes unless the shard key is the prefix for all the unique indexes. 

- For an already-sharded collection, you cannot create unique indexes
  on other fields unless the shard key is included as the prefix.

- A unique index stores a null value for a document missing the
  indexed field; that is a missing index field is treated as another
  instance of a `null` index key value. For more information, see
  unique-index-and-missing-field.

To enforce uniqueness on the shard key values, pass the `unique`
parameter as `true` to the `sh.shardCollection()` method:

- If the collection is empty, `sh.shardCollection()` creates the unique index on the
  shard key if such an index does not already exist.

- If the collection is not empty, you must create the index first
  before using `sh.shardCollection()`.

Although you can have a unique compound index where the shard
key is a prefix, if using `unique`
parameter, the collection must have a unique index that is on the shard
key.

You cannot specify a unique constraint on a hashed index.

To maintain uniqueness on a field that is not your shard key, 
see shard-key-arbitrary-uniqueness. 

## Missing Shard Key Fields

Documents in sharded collections can be missing the shard key fields. 
To set missing shard key fields, see shard-key-missing-set.

### Chunk Range and Missing Shard Key Fields

Missing shard key fields fall within the same chunk range as shard keys
with null values. For example, if the shard key is on the fields ``{ x:
1, y: 1 }``, then:

| Document Missing Shard Key | Falls into Same Range As |
|---|---|
| `{ x: "hello" }` | `{ x: "hello", y: null }` |
| `{ y: "goodbye" }` | `{ x: null, y: "goodbye" }` |
| `{ z: "oops" }` | `{ x: null, y: null }` |

### Read/Write Operations and Missing Shard Key Fields

To target documents with missing shard key fields, you can use the
`{ $exists: false }` filter condition on the shard key
fields. For example, if the shard key is on the fields ``{ x: 1, y: 1
}``, you can find the documents with missing shard key fields by running
this query:

```javascript
db.shardedcollection.find( { $or: [ { x: { $exists: false } }, { y: { $exists: false } } ] } )
```

If you specify a null equality match filter condition (e.g. ``{ x: null
}``), the filter matches both those documents with missing shard
key fields and those with shard key fields set to `null`.

Some write operations, such as a write with an `upsert`
specification, require an equality match on the shard key. In those
cases, to target a document that is missing the shard key, include
another filter condition in addition to the `null` equality match.
For example:

```javascript
{ _id: <value>, <shardkeyfield>: null } // _id of the document missing shard key
```
