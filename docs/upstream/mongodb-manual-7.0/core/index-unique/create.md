<!-- Converted from core/index-unique/create.txt (reStructuredText). Includes are inlined. -->

# Create a Single-Field Unique Index

Unique indexes ensure that a value appears at most once for a given
field.

To create a unique index in the MongoDB Shell, use the
`db.collection.createIndex()` method with the `unique` option
set to `true`. 

```javascript
db.collection.createIndex(
   { <field>: <sortOrder> },
   { unique: true }
 )
```

## About this Task

This example adds a unique index on the `user_id` field of a
`members` collection to ensure that there are no duplicate values in
the `user_id` field.

## Steps

To create a unique index on the `user_id` field of the `members`
collection, run the following command in `mongosh`:

```javascript
db.members.createIndex( { "user_id": 1 }, { unique: true } )
```

## Learn More

- index-unique-compound-index

- index-convert-to-unique
