<!-- Converted from tutorial/maintain-uniqueness-in-sharded-clusters.txt (reStructuredText). Includes are inlined. -->

# Maintain Uniqueness in Sharded Clusters

A sharded cluster enforces a unique constraint across shards only when
the unique index is on the shard key or includes the shard key as a
prefix. This page describes how to
maintain uniqueness when you shard a collection.

To create a unique index on a collection
that is already sharded, see manual-create-unique-index-sharded. To
enforce uniqueness on the shard key values, see 
manual-uniqueness-shard-key-values. To enforce uniqueness on a field that
cannot be part of the shard key, see manual-uniqueness-proxy-collection.

To reshard a collection that has a uniqueness 
constraint, the new shard key must satisfy the unique index requirements for any existing unique indexes. For details, see
sharding-resharding.

## About this Task

A unique index ensures that the indexed fields do not store duplicate
values. On a sharded collection, each shard can only check its own
data for duplicates, so MongoDB can enforce the constraint across the
cluster only when every document with a given index key value is
guaranteed to live on the same shard. Including the shard key as a
prefix of the index provides that guarantee.

For a ranged sharded collection, only the following indexes can be
unique:

- The index on the shard key

- A compound index where the shard key is a prefix

- The default `_id` index; however, the `_id` index only
  enforces the uniqueness constraint **per shard** if the `_id` field
  is not the shard key.

The unique index constraints mean that:

- For a to-be-sharded collection, you cannot shard the collection if
  the collection has multiple unique indexes unless the shard key is the prefix
  for all the unique indexes. 

- For an already-sharded collection, you cannot create unique indexes
  on other fields unless the shard key is included as the prefix.

- A unique index stores a null value for a document missing the
  indexed field. A missing index field is treated as another
  instance of a `null` index key value. For details, see
  unique-index-and-missing-field.

The following constraints also apply:

- You cannot specify a unique constraint on a hashed index.

- If there is a collation on the index key, MongoDB
  can only ensure uniqueness if the collation is simple.

- A unique index on the shard key enforces uniqueness on the entire
  key combination, not on the individual components of the shard key.

**Important:**

Sharded clusters do not enforce the uniqueness constraint on `_id` fields 
across the cluster when the `_id` field is not the shard key.

If the `_id` field is not the shard key, the uniqueness constraint only 
applies to the shard that stores the document. This means that two or more
documents can have the same `_id` value, provided they occur on different
shards.

For example, consider a sharded collection with shard key ``{x:
1}` that spans two shards A and B. Because the `_id`` key is
not the shard key, the collection could have a document
with `_id` value `1` in shard A and another document with
`_id` value `1` in shard B.

In cases where the `_id` field is not the shard key, MongoDB expects
applications to ensure the uniqueness of `_id` values across the shards,
for example, by using a unique identifier to populate the `_id` field.

## Before You Begin

- Identify the shard key for the collection. To view the shard key of
  a sharded collection, run the `sh.status()` method and
  locate the collection in the output.

- Confirm that no existing documents violate the uniqueness constraint
  for the field. If a shard contains documents with duplicate values,
  the create index operation may succeed on the shards without
  duplicates but fail on the shard with duplicates, leaving
  inconsistent indexes across shards.

- Connect `mongosh` to a `mongos` instance.

## Steps

The following example shards the `accounts.names` collection on
`region_id` and enforces a unique constraint on the combination of
`region_id` and `email`. 

**Step 1: Create the shard key index.**

Create the index you plan to use as the shard key:

```javascript
db.names.createIndex( { region_id: 1 } )
```

Output:

```javascript
region_id_1
```

**Step 2: Create the unique index.**

Create the unique index for the collection. Include the shard
key as a prefix of the index:

```javascript
db.names.createIndex(
   { region_id: 1, email: 1 },
   { unique: true }
)
```

Output:

```javascript
region_id_1_email_1
```

**Step 3: Shard the collection.**

To shard the collection, run the `sh.shardCollection` method:

```javascript
sh.shardCollection( "accounts.names", { region_id: 1 } )
```

Output:

```javascript
{
   collectionsharded: 'accounts.names',
   ok: 1,
   '$clusterTime': {
      clusterTime: Timestamp( { t: 1759260515, i: 58 } ),
      signature: {
         hash: Binary.createFromBase64( 'AAAAAAAAAAAAAAAAAAAAAAAAAAA=', 0 ),
         keyId: Long( '0' )
      }
   },
   operationTime: Timestamp( { t: 1759260515, i: 57 } )
}
```

If you shard a collection that contains a unique index that doesn't
include the shard key as a prefix, MongoDB returns an error when you
run the `shardCollection` command.

## Learn More

- index-type-unique

- sharding-shard-key-unique

- sharding-introduction

- `createIndexes`

- `db.collection.createIndex`
