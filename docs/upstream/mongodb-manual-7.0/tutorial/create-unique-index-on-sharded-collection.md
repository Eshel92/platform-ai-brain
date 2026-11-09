<!-- Converted from tutorial/create-unique-index-on-sharded-collection.txt (reStructuredText). Includes are inlined. -->

# Create a Unique Index on Existing Sharded Collection

You can create a new unique index on a collection that is already
sharded, but only if the index includes the shard key as a prefix.

## About this Task

The uniqueness constraint on an index ensures that documents in the
collection have a unique value for the indexed field. For a sharded
collection, MongoDB enforces uniqueness only when the index is the
shard key or includes the shard key as a prefix.

For an already-sharded collection, you cannot create a unique index on
other fields unless the shard key is included as the prefix. If the
index doesn't include the shard key as a prefix, MongoDB returns an
error when you run the `createIndexes` command.

For the constraints that apply to unique indexes on sharded
collections, and for how to maintain uniqueness on a field that is not
part of the shard key, see
manual-maintain-uniqueness-sharded.

## Before You Begin

- Identify the shard key for the collection. To view the shard key,
  run the `sh.status()` method and locate the collection in the
  output.

- Confirm that no existing documents violate the uniqueness constraint
  for the field. If a shard contains documents with duplicate values,
  the create index operation may succeed on the shards without
  duplicates but fail on the shard with duplicates, leaving
  inconsistent indexes across shards.

- Connect `mongosh` to a `mongos` instance.

## Steps

The following example creates a unique compund index on the `region_id` and 
`email` fields of the `accounts.names` collection, which is sharded on the
`region_id` field.

**Step 1: Verify the shard key.**

Run the `sh.status()` method and locate the
`accounts.names` collection in the output to confirm that the
shard key is `region_id`:

```javascript
sh.status()
```

**Step 2: Create the unique index.**

Create the unique index and include the shard key `region_id`
as a prefix of the compound index:

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

## Learn More

- manual-maintain-uniqueness-sharded

- index-type-unique

- sharding-shard-key-unique

- `createIndexes`

- `db.collection.createIndex`
