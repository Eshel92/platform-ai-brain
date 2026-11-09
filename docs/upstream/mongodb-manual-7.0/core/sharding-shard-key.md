<!-- Converted from core/sharding-shard-key.txt (reStructuredText). Includes are inlined. -->

# Shard Keys

The shard key is either a single indexed field or multiple
fields covered by a compound index that determines the
distribution of the collection's documents among the
cluster's shards. For details, see
sharding-shard-key-indexes.

MongoDB divides the span of shard key values (or hashed shard key
values) into non-overlapping ranges. Each range is associated with a
chunk, and MongoDB attempts to distribute chunks evenly among
the shards in the cluster.

(Figure: /images/sharding-range-based.bakedsvg.svg)

## Shard a Collection

You can use the `mongosh` method `sh.shardCollection()` to
shard a collection. To shard a collection, you must specify the full namespace
of the collection that you want to shard and the shard key.

```javascript
sh.shardCollection(<namespace>, <key>) // Optional parameters omitted
```

* - `namespace`

  - Specify the full namespace of the collection that you want to
    shard (`"<database>.<collection>"`).

* - `key`

  - Specify a document `{ <shard key field1>: <1|"hashed">, ... }`
    where

    - `1` indicates range-based sharding

    - `"hashed"` indicates hashed sharding.

For more information on the sharding method, see
`sh.shardCollection()`.

## Choose a Shard Key

The choice of shard key affects the creation and distribution of
data across the available shards. The ideal shard key allows MongoDB to distribute documents
evenly throughout the cluster while also facilitating common query
patterns.

For details, see the Choose a Shard Key page.

## Change a Shard Key

You can change a shard key in two ways:

- You can refine a shard key by adding fields to your existing key.
- You can change a shard key entirely and reshard a collection
  with the new key.

For details, see the Change a Shard Key page.

## Change Shard Key Field Value for a Document

You can change the value for the shard key field in any
document in your collection unless the shard key field is
the `_id` field. This can affect which shard the document
lives on.

For details, see update-shard-key.

## Set Missing Shard Key Fields

Documents in your collection can be missing fields that your shard
key specifies. By default, documents that are missing fields specified
by your shard key live in the same chunk range as shard keys with
null values.

For details, see shard-key-missing-set.

## Display a Shard Key

Use `db.printShardingStatus()` to display the shard key used
for your collection.

For details, see sharding-display-shard-key.

## Troubleshoot

Common issues caused by a suboptimal shard key are:

- Jumbo chunks
- Uneven load distribution
- Decreased query performance

For details, see Troubleshoot Shard Keys.
