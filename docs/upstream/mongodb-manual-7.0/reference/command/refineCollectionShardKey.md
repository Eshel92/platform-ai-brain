<!-- Converted from reference/command/refineCollectionShardKey.txt (reStructuredText). Includes are inlined. -->

# refineCollectionShardKey (database command)

## Definition

**`refineCollectionShardKey`**

Modifies the collection's shard key by adding new
field(s) as a suffix to the existing key. Refining a collection's
shard key can address situations
where the existing key has led to jumbo (i.e. indivisible)
chunks due to insufficient cardinality.

**Note:** Data Distribution

As part of refining the shard key, the
`refineCollectionShardKey` command updates the
chunk ranges and
zone ranges to incorporate the new
fields without modifying the range values of the existing key
fields. That is, the refinement of the shard key does not
immediately affect the distribution of chunks across shards or
zones. Any future chunk splits or migration occur as part of the
routine sharding operations.

## Compatibility

This command is available in deployments hosted in the following environments: 

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas): The fully
  managed service for MongoDB deployments in the cloud

**Important:**

This command is not supported in M10+ clusters.
For more information, see Unsupported Commands.

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Syntax

**Note:**

To use the `refineCollectionShardKey` command, the sharded
cluster must have feature compatibility version (fcv)
of `4.4`.

The command has the following syntax:

```javascript
db.adminCommand( 
   { 
     refineCollectionShardKey: "<database>.<collection>", 
     key: { <existing key specification>, <suffix1>: <1|"hashed">, ... }
   } 
)
```

## Command Fields

The command takes the following fields:

* - Field
  - Type
  - Description

* - refineCollectionShardKey
  - string
  - .. _refineCollectionShardKey-namespace:

    The namespace of the sharded collection in the
    form `"<database>.<collection>"`.

* - key
  - document
  - .. _refineCollectionShardKey-key:

    The document that specifies the field or fields to use as the
    new shard key for the
    collection.

    `{ <existing key specification>, <suffix1>: <1|"hashed">, ... }`

    - The new key must start with the existing shard key.

    - The new key must be supported by an index that must exist
      before you run the
      `refineCollectionShardKey` command. See
      refineCollectionShardKey-index-considerations for
      more information.

    For the suffix fields, set the field values to either:

    - `1` for ranged based sharding

    - `"hashed"` to specify a hashed shard key *if* no other field in the shard key has
      a `"hashed"` specification and the current shard key is not
      supported by a unique index since hashed indexes do not
      support uniqueness constraint.

**See also:**

/core/sharding-shard-key

## Access Control

When running with access control, the user must have the
`refineCollectionShardKey` privilege actions on database
and/or collection to run the
command. That is, a user must have a role that grants
the following privilege:

```javascript
{ resource: { db: <database>, collection: <collection> }, actions: [ "refineCollectionShardKey" ] }
```

The built-in `clusterManager` role provides the appropriate
privileges.

## Considerations

### Index Considerations

- Index Existence
      An index that supports the command's specified key must exist prior to
      running the command.

      A supporting index is an index that starts with the new shard key
      specification; i.e. the index prefix matches the new shard key specification.
      That is, to change the shard key to `{ x: 1, y: 1 }` from ``{ x:
      1 }`, and index that starts with `{ x: 1, y: 1 }`` must exist; e.g.

      - `{ x: 1, y: 1 }`

      - `{ x: 1, y: 1, a: 1, b: 1}`

      **Note:**

      - The supporting index cannot be a partial index.

      - The supporting index cannot be a sparse index.

      - If the collection uses a non-`simple` collation, the supporting
        index must specify `{ locale: "simple" }` collation.

- Unique Index
      If the current shard index has a uniqueness constraint, the new shard key index must also have a
      unique constraint.

      | After creating the unique index to support the new shard key,
        **drop** the old shard key index before running
        `refineCollectionShardKey`.

      | Also, if the current shard index has a unique constraint, then the new shard key cannot specify
        `"hashed"` for any of its fields.
      
      | See also Sharded Collection and Unique Indexes.
   
- Index Collation
      If the sharded collection has a non-`simple` default
      collation, then the index *must* include a
      collation document with `{ locale : "simple" }`. At least one
      of the indexes whose fields support the shard key pattern must
      have the simple collation.

**Warning:**

Do not modify the range or hashed type for any of the current shard
key fields. It causes data inconsistencies. For example, do not
modify a shard key from `{ customer_id: 1 }` to ``{ customer_id:
"hashed", order_id: 1 }``.

## Examples

To set up the example in the `test` database:

#. Use following `shardCollection` operation to shard the
   `orders` collection in the `test` database. The operation
   uses the `customer_id` field as the initial shard key:

   ```javascript
   db.adminCommand( { shardCollection: "test.orders", key: { customer_id: 1 } } )
   ```

To modify the shard key to be the `customer_id` field and the
`order_id` field `{ customer_id: 1, order_id: 1 }`,

#. `Create the index` to
   support the new shard key if the index does not already exist.

   ```javascript
   db.getSiblingDB("test").orders.createIndex( { customer_id: 1, order_id: 1 } )
   ```

#. Run `refineCollectionShardKey` command to add the `order_id`
   field as a suffix:

   ```javascript
   db.adminCommand( { 
      refineCollectionShardKey: "test.orders", 
      key: { customer_id: 1, order_id: 1 }
   } )
   ```

Upon successful completion of the command, the shard key for the
collection has changed to `{ customer_id: 1, order_id: 1 }`. To verify,
you can run `sh.status()`.

**Tip:**

After you refine the shard key, it may be that not all documents in
the collection have the suffix field(s). To populate the missing
shard key field(s), see shard-key-missing.

Before refining the shard key, ensure that all or most documents in
the collection have the suffix fields, if possible, to avoid having
to populate the field afterwards.

### Collection with non-`simple` Collation

To set up the example in the `test` database:

#. Create the `cafés` collection in the `test` database,
   specifying French `fr` as the default collation.

   ```javascript
   db.getSiblingDB("test").createCollection( "cafés", { collation: { locale: "fr" } } );
   ```

#. Shard the collection using `customer_id` field as the initial
   shard key. Because the collection has a default `fr`
   collation and not a `simple` collation, the
   `shardCollection` command must include a ``collation:
   { locale: "simple" }`` option:

   ```javascript
   db.adminCommand( { 
      shardCollection: "test.cafés", 
      key: { customer_id: 1 },
      collation: { locale: "simple" } 
   } )
   ```

To modify the shard key to be both the `customer_id` field and the
`order_id` field `{ customer_id: 1, order_id: 1 }`,

#. `Create the index` to
   support the new shard key if the index does not already exist.
   Because the collection uses a non-simple collation, the index
   must include the `collation: { locale: "simple" }` option.

   ```javascript
   db.getSiblingDB("test").cafés.createIndex( 
      { customer_id: 1, order_id: 1 }, 
      { collation: { locale: "simple" } } 
   )
   ```

#. Run `refineCollectionShardKey` command to add the `order_id`
   field as a suffix:

   ```javascript
   db.adminCommand( { 
      refineCollectionShardKey: "test.cafés",
      key: { customer_id: 1, order_id: 1 } 
   } )
   ```

Upon successful completion of the command, the shard key for the
collection has changed to `{ customer_id: 1, order_id: 1 }`. To verify,
you can run `sh.status()`.

**Tip:**

After you refine the shard key, it may be that not all documents in
the collection have the suffix field(s). To populate the missing
shard key field(s), see shard-key-missing.

Before refining the shard key, ensure that all or most documents in
the collection have the suffix fields, if possible, to avoid having
to populate the field afterwards.

**See also:**

/core/sharding-shard-key/
