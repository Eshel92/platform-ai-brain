<!-- Converted from core/sharding-shard-a-collection.txt (reStructuredText). Includes are inlined. -->

# Shard a Collection

To shard a collection, you must specify the full namespace of the
collection that you want to shard and the shard key. You can use the
`mongosh` method `sh.shardCollection()` to
shard a collection:

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

## Shard Key Fields and Values

### Missing Shard Key Fields

Documents in sharded collections can be missing the shard key fields. 
A missing shard key falls into the same range as a `null`-valued shard key. 
See shard-key-missing.

### Change a Document's Shard Key Value

You can update a document's shard key value unless the shard key field is the 
immutable `_id` field. 

For details on updating the shard key value, see
update-shard-key.

### Change a Collection's Shard Key

Starting in MongoDB 5.0, you can reshard a collection by changing a document's shard key.

You can refine a shard key by adding a suffix field 
or fields to the existing shard key.
