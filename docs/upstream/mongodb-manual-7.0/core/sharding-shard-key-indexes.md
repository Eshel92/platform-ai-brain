<!-- Converted from core/sharding-shard-key-indexes.txt (reStructuredText). Includes are inlined. -->

# Shard Key Indexes

Sharded collections require an index that supports the shard key.
The index can be an index on the shard key or a compound index
where the shard key is a prefix of the index.

- If the collection is empty, `sh.shardCollection()` creates
  the index on the shard key if such an index does not already exists.

- If the collection is not empty, you must create the index first
  before using `sh.shardCollection()`.

- If you reshard a collection using
  `sh.reshardCollection()`, you do not need to create the
  index on the new shard key beforehand. The resharding operation
  builds the required indexes automatically. To learn more, see the
  Reshard a Collection procedure.

You cannot drop or
hide an index if it is the only
non-hidden index that supports the shard key.

Starting in MongoDB 7.0.3, 6.0.12, and 5.0.22, you can drop the index
for a hashed shard key. For details,
see drop-a-hashed-shard-key-index.

## Unique Indexes

MongoDB can enforce a uniqueness constraint on a ranged shard key index.
Using a unique index on the shard key enforces uniqueness on the entire
key combination and not individual components of the shard key.

For a ranged sharded collection, only an index on the shard key, a
compound index where the shard key is a prefix, or the default `_id` index can be
unique. You cannot specify a unique
constraint on a hashed index.

To learn about the restrictions that apply to unique indexes on
sharded collections, how to enforce uniqueness on the shard key
values, and how to maintain uniqueness on a field that is not your
shard key, see manual-maintain-uniqueness-sharded.
