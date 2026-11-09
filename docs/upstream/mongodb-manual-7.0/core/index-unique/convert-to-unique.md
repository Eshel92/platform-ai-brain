<!-- Converted from core/index-unique/convert-to-unique.txt (reStructuredText). Includes are inlined. -->

# Convert an Existing Index to a Unique Index

To convert a non-unique index to a unique index, use the `collMod` command. The
`collMod` command provides options to verify that your indexed field
contains unique values before you complete the conversion.

## About this Task

The `collMod` command converts the existing index. MongoDB scans the
index for duplicate keys and then marks the index as unique.

Keep the following behavior in mind when you convert an index:

- Set `prepareUnique` to `true` before you convert the index. If
  `prepareUnique` is `false`, `collMod` with `unique: true`
  returns an error.

- Run the `prepareUnique` modification in a separate `collMod`
  command. You cannot combine `prepareUnique` with other index
  modifications.

- You cannot set `prepareUnique` on an index in a time series
  collection. MongoDB returns an error.

- If another operation modifies or drops the index while `collMod`
  converts it, the command fails. Rerun the command after the other
  operation completes.

For sharded collections, the following behavior also applies:

- If any shard contains duplicate keys, `collMod` returns
  `CannotConvertIndexToUnique`. MongoDB does not convert the index on
  any shard.

- If the index key conflicts with the shard key, setting
  `prepareUnique` fails. To learn which indexes can be unique on a
  sharded collection, see sharded-clusters-unique-indexes.

## Before you Begin

**Step 1: Populate sample data**

Create the `apples` collection:

```javascript
db.apples.insertMany( [
   { type: "Delicious", quantity: 12 },
   { type: "Macintosh", quantity: 13 },
   { type: "Delicious", quantity: 13 },
   { type: "Fuji", quantity: 15 },
   { type: "Washington", quantity: 10 }
] )
```

**Step 2: Create a single field index**

Add a single field index on the `type` field:

```javascript
db.apples.createIndex( { type: 1 } )
```

## Steps

**Step 1: Prepare the index to be converted to a unique index**

Run `collMod` on the `type` field index and set
`prepareUnique` to `true`:

```javascript
db.runCommand( {
   collMod: "apples",
   index: {
      keyPattern: { type: 1 },
      prepareUnique: true
   }
} )
```

After `prepareUnique` is set, you cannot insert new documents
that duplicate an index key entry. For example, the following
insert operation results in an error:

```javascript
db.apples.insertOne( { type: "Delicious", quantity: 20 } )
```

Output:

```javascript
MongoServerError: E11000 duplicate key error collection:
test.apples index: type_1 dup key: { type: "Delicious" }
```

**Step 2: Check for unique key violations**

To see if there are any documents that violate the unique constraint on
the `type` field, run `collMod` with `unique: true` and ``dryRun:
true``:

```javascript
db.runCommand( {
   collMod: "apples",
   index: {
      keyPattern: { type: 1 },
      unique: true
   },
   dryRun: true
} )
```

Output:

```javascript
MongoServerError: Cannot convert the index to unique. Please resolve conflicting documents before running collMod again.

Violations: [
   {
      ids: [
         ObjectId("660489d24cabd75abebadbd0"),
         ObjectId("660489d24cabd75abebadbd2")
      ]
   }
]
```

**Note:**

If the response containing all conflicting document `_id` values
exceeds 8MB, MongoDB returns the following error message instead of
listing the specific violations:

```none
Cannot convert the index to unique. Too many conflicting documents
were detected. Please resolve them and rerun collMod.
```

In this case, resolve duplicate entries until the response
is under 8MB, then run `collMod` again to see the remaining
violations.

**Step 3: Resolve duplicate key conflicts**

To complete the conversion, modify the duplicate entries to remove any
conflicts. For example:

```javascript
db.apples.deleteOne(
   { _id: ObjectId("660489d24cabd75abebadbd2") }
)
```

**Step 4: Confirm that all conflicts are resolved**

To confirm that the index can be converted, re-run the `collMod()`
command with `dryRun: true`:

```javascript
db.runCommand( {
   collMod: "apples",
   index: {
      keyPattern: { type: 1 },
      unique: true
   },
   dryRun: true
} )
```

Output:

```javascript
{ ok: 1 }
```

**Step 5: Finalize the index conversion**

To finalize the conversion to a unique index, run the `collMod`
command with `unique: true` and remove the `dryRun` flag:

```javascript
db.runCommand( {
   collMod: "apples",
   index: {
      keyPattern: { type: 1 },
      unique: true
   }
} )
```

Output:

```javascript
{ unique_new: true, ok: 1 }
```

## Learn More

- manage-indexes

- index-properties

- indexing-strategies
