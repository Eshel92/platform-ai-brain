<!-- Converted from core/dot-dollar-considerations.txt (reStructuredText). Includes are inlined. -->

# Field Names with Periods (`.`) and Dollar Signs (`$`)

## Overview

MongoDB 5.0 adds improved support for field names that are dollar
(`$`) prefixed or that contain periods (`.`). The validation rules
for storing data have been updated to make it easier to work with data
sources that use these characters. 

In most cases data that has been stored using field names like these
is not directly accessible. You need to use helper methods like
`$getField`, `$setField`, and
`$literal` in queries that access those fields. 

The field name validation rules are not the same for all types of
storage operations. This page summarizes how different insert and
update operations handle dollar (`$`) prefixed field names.

## Insert operations

Dollar (`$`) prefixed fields are permitted as top level and nested
field names for inserts.

```javascript
db.sales.insertOne( {
   "$price": 50.00,
   "quantity": 30
} )
```

Dollar (`$`) prefixed fields are permitted on inserts using otherwise
reserved words. Operator names like `$inc` can be used as
field names as well as words like `id`, `db`, and `ref`.

```javascript
db.books.insertOne( {
   "$id": "h1961-01",
   "location": {
      "$db": "novels",
      "$ref": "2007042768",
      "$inc": true
} } )
```

An update which creates a new document during an upsert is
treated as an `insert` rather than an `update` for field name
validation. Upserts can accept dollar (`$`) prefixed
fields. However, upserts are a special case and
similar update operations may cause an error if the `match` portion
of the update selects an existing document.

This code sample has `upsert: true` so it will insert a new document
if the collection doesn't already contain a document that matches the
query term, `{ "date": "2021-07-07" }`. If this sample code matches
an existing document, the update will fail since `$hotel` is dollar
(`$`) prefixed.

```javascript
db.expenses.updateOne(
   { "date": "2021-07-07" },
   { $set: {
      "phone": 25.17,
      "$hotel": 320.10
   } },
   { upsert: true }
)
```

## Document Replacing Updates

Update operators either replace existing fields with new documents
or else modify those fields. In cases where the update performs a
replacement, dollar (`$`) prefixed fields are not permitted as top
level field names. 

Consider a document like

```javascript::
{
   "_id": "E123",
   "address": {
      "$number": 123,
      "$street": "Elm Road"
   },
   "$rooms": {
      "br": 2,
      "bath": 1
   }
}
```

You could use an update operator that replaces an existing document to
modify the `address.$street` field but you could not update the
`$rooms` field that way. 

```
db.housing.updateOne(
   { "_id": "E123" },
   { $set: { "address.$street": "Elm Ave" } }
)
```

Use `$setField` as part of an aggregation pipeline to
update top level dollar (`$`)
prefixed fields like `$rooms`.

## Document Modifying Updates

When an update modifies, rather than replaces, existing document
fields, dollar (`$`) prefixed fields can be top level field names.
Subfields can be accessed directly, but you need a helper method to
access the top level fields. 

**See also:**

`$getField`, `$setField`,
`$literal`, `$replaceWith`

Consider a collection with documents like this inventory record:

```
{
   _id: ObjectId("610023ad7d58ecda39b8d161"),
   "part": "AB305",
   "$bin": 200,
   "quantity": 100,
   "pricing": { sale: true, "$discount": 60 }
}
```

The `pricing.$discount` subfield can be queried directly.

```
db.inventory.findAndModify( {
    query: { "part": { $eq: "AB305" } },
    update: { $inc: { "pricing.$discount": 10 } }
} )
```

Use `$getField` and `$literal` to access the
value of the top level `$bin` field.

```
db.inventory.findAndModify( {
   query: { $expr: {
      $eq: [ { $getField: { $literal: "$bin" } }, 200 ]
   } }, 
   update: { $inc: { "quantity": 10 } }
} )
```

## Updates Using Aggregation Pipelines

Use `$setField`, `$getField`, and
`$literal` in the `$replaceWith` stage to modify
dollar (`$`) prefixed fields in an aggregation pipeline.

Consider a collection of school records like:

```javascript
{
   "_id": 100001,
   "$term": "fall",
   "registered": true,
   "grade": 4
}
```

Create a new collection for the spring semester using a 
pipeline to update the dollar (`$`) prefixed `$term` field.

```javascript
db.school.aggregate( [
   { $match: { "registered": true } }, 
   { $replaceWith: {
      $setField: {
         field: { $literal: "$term" }, 
         input: "$$ROOT",
         value: "spring"
   } } },
   { $out: "spring2022" }
] )
```

## General Restrictions

In addition to the storage validation rules above, there are some
general restrictions on using dollar (`$`) prefixed field names.
These fields cannot: 

- Be indexed
- Be used as part of a shard key
- Be validated using `$jsonSchema`
- Be be modified with an escape sequence
- Be used with
  `Field Level Encryption`
- Be used as a subfield in an `_id` document

**Warning:** Possible Data Loss With Dollar Signs (`$`) and Periods (`.`)

There is a small chance of data loss when using dollar (`$`) prefixed
field names or field names that contain periods (`.`) if these
field names are used in conjunction with unacknowledged writes
(write concern `w=0`) on servers
that are older than MongoDB 5.0.

When running insert,
update, and
findAndModify
commands, drivers that are 5.0 compatible remove restrictions on
using documents with field names that are dollar (`$`) prefixed or
that contain periods (`.`). These field names generated a client-side
error in earlier driver versions.

The restrictions are removed regardless of the server version the
driver is connected to. If a 5.0 driver sends a document to an older
server, the document will be rejected without sending an error.

**Warning:** Import and Export Concerns With Dollar Signs (`$`) and Periods (`.`)

Starting in MongoDB 5.0, document field names can be dollar (`$`)
prefixed and can contain periods (`.`). However,
`mongoimport` and `mongoexport` may not work
as expected in some situations with field names that make use of these
characters.

MongoDB Extended JSON v2
cannot differentiate between type wrappers and fields that happen to
have the same name as type wrappers. Do not use Extended JSON
formats in contexts where the corresponding BSON representations
might include dollar (`$`) prefixed keys. The
DBRef mechanism is an exception to this
general rule. 

There are also restrictions on using `mongoimport` and
`mongoexport` with periods (`.`) in field names. Since
CSV files use the period (`.`) to represent data hierarchies, a
period (`.`) in a field name will be misinterpreted as a level of
nesting.
