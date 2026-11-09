<!-- Converted from reference/method/convertShardKeyToHashed.txt (reStructuredText). Includes are inlined. -->

# convertShardKeyToHashed (mongosh method)

## Description

**`convertShardKeyToHashed(<Object>)`**

Returns the hashed value for the input. The
`convertShardKeyToHashed()` method uses the same hashing
function as the hashed index and can be used to see what the
hashed value would be for a key.

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

## Example

Consider a sharded collection that uses a hashed shard key [#populated]_

```javascript
use test

db.orders.createIndex( { _id: "hashed" } )

sh.shardCollection( "test.orders", { _id : "hashed" } )
```

If the following document exists in the collection, the hashed value of
the `_id` field is used to distribute the document:

```javascript
{
  _id: ObjectId("5b2be413c06d924ab26ff9ca"),
  "item" : "Chocolates",
  "qty" : 25
}
```

   

To determine the hashed value of `_id` field used to distribute the
document across the shards, you can use the
`convertShardKeyToHashed` method:

```javascript
convertShardKeyToHashed( ObjectId("5b2be413c06d924ab26ff9ca") )
```
