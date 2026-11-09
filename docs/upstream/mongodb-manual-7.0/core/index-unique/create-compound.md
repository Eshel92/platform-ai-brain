<!-- Converted from core/index-unique/create-compound.txt (reStructuredText). Includes are inlined. -->

# Create a Compound Unique Index

You enforce a unique constraint on compound indexes. A unique compound index enforces uniqueness on
the *combination* of the index key values.

To create a unique index in the MongoDB Shell, use the
`db.collection.createIndex()` method with the `unique` option
set to `true`. 

```javascript
db.collection.createIndex(
   {
      <field1>: <sortOrder>,
      <field2>: <sortOrder>,
      ...
      <fieldN>: <sortOrder>
   },
   { unique: true }
 )
```

## About this Task

This example adds a unique compound index on the
`groupNumber`, `lastname`, and `firstname` fields of a
`members` collection. The index ensures that the combination of these
field values is unique for each document in the collection.

## Steps

To create a unique index on `groupNumber`, `lastname`, and
`firstname` fields of the `members` collection, run the following
command in `mongosh`:

```javascript
db.members.createIndex(
   { groupNumber: 1, lastname: 1, firstname: 1 },
   { unique: true }
)
```

The created index enforces uniqueness for the *combination* of
`groupNumber`, `lastname`, and `firstname` values.

## Compound Unique Indexes on Fields with Embedded Arrays

Consider a collection with the following document:

```javascript
db.myColl.insertOne(
   { _id: 1, a: [ { loc: "A", qty: 5 }, { qty: 10 } ] }
)
```

Create a unique compound multikey index
on `a.loc` and `a.qty`:

```javascript
db.myColl.createIndex( { "a.loc": 1, "a.qty": 1 }, { unique: true } )
```

The unique index permits the insertion of the following documents into
the collection since the index enforces uniqueness for the
*combination* of `a.loc` and `a.qty` values:

```javascript
db.myColl.insertMany( [
   { _id: 2, a: [ { loc: "A" }, { qty: 5 } ] },
   { _id: 3, a: [ { loc: "A", qty: 10 } ] }
] )
```

## Learn More

- unique-separate-documents
- unique-index-and-missing-field
