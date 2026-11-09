<!-- Converted from tutorial/clear-jumbo-flag.txt (reStructuredText). Includes are inlined. -->

# Clear `jumbo` Flag

If MongoDB cannot split a chunk that exceeds the specified range
size, MongoDB labels the chunk as 
jumbo.

The following procedures outline the steps to manually clear the 
`jumbo` flag.

## Procedures

### Divisible Chunks

The preferred manual way to clear the `jumbo` flag from a chunk is to
attempt to split the chunk. If the chunk is divisible, MongoDB removes
the flag upon successful split of the chunk.

**Step 1: Connect to `mongos`.**

Connect `mongosh` to a `mongos`.

**Step 2: Find the `jumbo` Chunk.**

Run `sh.status(true)` to find the chunk labeled
`jumbo`.

```bash
sh.status(true)
```

For example, the following output from sh.status(true) shows that
chunk with shard key range `{ "x" : 2 } -->> { "x" : 4 }` is
`jumbo`.

```none
 --- Sharding Status ---
   sharding version: {
      ...
   }
   shards:
      ...
   databases:
      ...
         test.foo
            shard key: { "x" : 1 }
         chunks:
              shard-b  2
              shard-a  2
         { "x" : { "$minKey" : 1 } } -->> { "x" : 1 } on : shard-b Timestamp(2, 0) 
         { "x" : 1 } -->> { "x" : 2 } on : shard-a Timestamp(3, 1) 
         { "x" : 2 } -->> { "x" : 4 } on : shard-a Timestamp(2, 2) jumbo 
         { "x" : 4 } -->> { "x" : { "$maxKey" : 1 } } on : shard-b Timestamp(3, 0)
```

**Step 3: Split the `jumbo` Chunk.**

Use either `sh.splitAt()` or `sh.splitFind()` to
split the `jumbo` chunk.

```javascript
sh.splitAt( "test.foo", { x: 3 })
```

MongoDB removes the `jumbo` flag upon successful split of the
chunk.

### Indivisible Chunks

In some instances, MongoDB cannot split the no-longer `jumbo` chunk,
such as a chunk with a range of single shard key value. As such, you
cannot split the chunk to clear the flag.

In such cases, you can either change the shard key so that the chunk can become divisible or manually
clear the flag.

#### Refine the Shard Key

MongoDB provides the `refineCollectionShardKey` command. Using the
`refineCollectionShardKey` command, you can refine a
collection's shard key by adding a suffix field or fields to the
existing key. By adding new field(s) to the shard key, indivisible
jumbo chunks can become divisible.

**Step 1: Connect to `mongos`.**

Connect `mongosh` to a `mongos`.

**Step 2: Find the `jumbo` Chunk.**

Run `sh.status(true)` to find the chunk labeled
`jumbo`.

```bash
sh.status(true)
```

For example, the following output from `sh.status(true)` shows that for the sharded collection `test.orders`,
both the chunk with shard key range ``{ "status" : "A" } -->> {
"status" : "D" }` and the chunk with range `{ "status" : "D" }
-->> { "status" : "P" }` are `jumbo``.

```none
 --- Sharding Status ---
   sharding version: {
     ...
   }
   shards:
     ...
   databases:
     ...
     test.orders
        shard key: { "status" : 1 }
        unique: false
        balancing: true
        chunks:
                shardA	2
                shardB	2
        { "status" : { "$minKey" : 1 } } -->> { "status" : "A" } on : shardB Timestamp(3, 0) 
        { "status" : "A" } -->> { "status" : "D" } on : shardA Timestamp(5, 1) jumbo 
        { "status" : "D" } -->> { "status" : "P" } on : shardA Timestamp(4, 2) jumbo 
        { "status" : "P" } -->> { "status" : { "$maxKey" : 1 } } on : shardB Timestamp(5, 0)
```

**Step 3: Refine the Shard Key for `test.orders` Collection.**

To address the low cardinality of the key `status`, refine the key
for the `test.orders` collection. For example, add the
`order_id` and `customer_id` fields as a suffix to the current
shard key; i.e. the shard key will be ``{ status: 1, order_id: 1,
customer_id: 1 }`` after refinement.

a. First, `create the index`
   to support the shard key 
   `{ status: 1, order_id: 1, customer_id: 1 }` if the index does
   not already exist.

   ```javascript
   db.orders.createIndex( { status: 1, order_id: 1, customer_id: 1 } )
   ```

   For additional index considerations for refining the shard key,
   see refineCollectionShardKey-index-considerations.

#. In the `admin` database, run the
   `refineCollectionShardKey` command to add the
   `order_id` and `customer_id` fields as a suffix to the existing key:

   ```javascript
   db.adminCommand( { 
      refineCollectionShardKey: "test.orders", 
      key: { status: 1, order_id: 1, customer_id: 1 }
   } )
   ```

The `refineCollectionShardKey` command updates the
chunk ranges and
zone ranges to incorporate the new
fields without modifying the range values of the existing key
fields. That is, the refinement of the shard key does not
immediately affect the distribution of chunks across shards or
zones. Any future chunk splits or migration occur as part of the
routine sharding operations.

**Tip:**

After you refine the shard key, it may be that not all documents in
the collection have the suffix field(s). To populate the missing
shard key field(s), see shard-key-missing.

Before refining the shard key, ensure that all or most documents in
the collection have the suffix fields, if possible, to avoid having
to populate the field afterwards.

#### Manually Clear the `jumbo` Flag for an Indivisible Chunk

To manually clear the `jumbo` flag, you can use the 
`clearJumboFlag` command. If you clear the `jumbo` flag for a chunk 
that still exceeds the chunk size, MongoDB will re-label the chunk as `jumbo` 
when MongoDB tries to move the chunk.

**Important:**

Only use this method if the preferred method is *not* applicable.

To manually clear the flag, use the following steps: 

**Step 1: Connect to `mongos`.**

Connect `mongosh` to a `mongos`.

**Step 2: Find the `jumbo` Chunk.**

Run `sh.status(true)` to find the chunk labeled
`jumbo`.

```bash
sh.status(true)
```

For example, the following output from sh.status(true) shows that
chunk with shard key range `{ "x" : 2 } -->> { "x" : 3 }` is
`jumbo`.

```none
 --- Sharding Status ---
   sharding version: {
      ...
   }
   shards:
      ...
   databases:
      ...
         test.foo
            shard key: { "x" : 1 }
         chunks:
              shard-b  2
              shard-a  2
         { "x" : { "$minKey" : 1 } } -->> { "x" : 1 } on : shard-b Timestamp(2, 0) 
         { "x" : 1 } -->> { "x" : 2 } on : shard-a Timestamp(3, 1) 
         { "x" : 2 } -->> { "x" : 3 } on : shard-a Timestamp(2, 2) jumbo 
         { "x" : 3 } -->> { "x" : { "$maxKey" : 1 } } on : shard-b Timestamp(3, 0)
```

**Step 3: Run the `clearJumboFlag` Command.**

From the `admin` database, run the `clearJumboFlag`,
passing in the namespace of the sharded collection and either:

- the bounds of the `jumbo` chunk:

  ```javascript
  db.adminCommand( { 
     clearJumboFlag: "test.foo",
     bounds: [{ "x" : 2 }, { "x" : 3 }]

  })
  ```

- the find document with a shard key
  and value contained in the `jumbo` chunk:

  ```javascript
  db.adminCommand( { 
     clearJumboFlag: "test.foo",
     find: { "x" : 2 }
  })
  ```

  **Note:**

  If the collection uses a hashed shard key, do not use the
  `find` field with `clearJumboFlag`. For hashed
  shard keys, use the `bounds` field instead.

**See also:**

`refineCollectionShardKey`
