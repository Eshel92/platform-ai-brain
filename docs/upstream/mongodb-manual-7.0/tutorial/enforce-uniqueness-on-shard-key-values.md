<!-- Converted from tutorial/enforce-uniqueness-on-shard-key-values.txt (reStructuredText). Includes are inlined. -->

# Enforce Uniqueness on the Shard Key Values

To enforce uniqueness on the shard key values themselves, pass the
`unique` parameter as `true` to the
`sh.shardCollection()` method.

## About this Task

A unique index on the shard key enforces uniqueness on the entire key
combination, not on the individual components of the shard key.

You cannot specify `unique` as `true` when you use a
hashed shard key.

The following restrictions apply when you specify `unique: true`:

- If the collection is empty, `sh.shardCollection()` creates the unique index on the
  shard key if such an index does not already exist.

- If the collection is not empty, you must create the index first
  before using `sh.shardCollection()`.

Although you can have a unique compound index where the shard
key is a prefix, if using `unique`
parameter, the collection must have a unique index that is on the shard
key.

If you omit `unique` or specify `unique: false`, `sh.shardCollection()` doesn't
change the collection's existing indexes. If a unique index on the
shard key already exists, that index remains unique and the sharded
cluster continues to enforce the uniqueness constraint on the shard
key values across shards.

For the full set of constraints that apply to unique indexes on
sharded collections, see
manual-maintain-uniqueness-sharded.

## Before You Begin

- Confirm that no existing documents violate the uniqueness constraint
  for the shard key values.

- Connect `mongosh` to a `mongos` instance.

## Steps

The following example shards the `accounts.names` collection on
`region_id` and enforces a unique constraint on the shard key
values. 

**Step 1: Create the index.**

```javascript
use accounts
db.names.createIndex( { "region_id": 1 }, { unique: true } )
```

**Step 2: Shard the collection.**

To shard the collection on the unique `region_id` index. The `unique`
parameter is the third argument to `sh.shardCollection()`:

```javascript
sh.shardCollection( "accounts.names", { region_id: 1 }, true )
```

## Learn More

- manual-maintain-uniqueness-sharded

- sharding-shard-key-unique

- index-type-unique

- `shardCollection`

- `sh.shardCollection`
