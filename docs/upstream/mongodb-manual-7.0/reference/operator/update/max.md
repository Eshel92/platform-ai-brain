<!-- Converted from reference/operator/update/max.txt (reStructuredText). Includes are inlined. -->

# $max (update operator)

## Definition

**`$max`**

The `$max` operator updates the value of the field to a
specified value *if* the specified value is **greater than** the
current value of the field. The `$max` operator can compare
values of different types, using the BSON comparison order.

The `$max` operator expression has the form:

```javascript
{ $max: { <field1>: <value1>, ... } }
```

To specify a `<field>` in an embedded document or in an array, use
dot notation.

## Behavior

Starting in MongoDB 5.0, update operators process document fields with
string-based names in lexicographic order. Fields with numeric names are
processed in numeric order. See Update Operators Behavior for details.

If the field does not exists, the `$max` operator sets the
field to the specified value.

Starting in MongoDB 5.0, `mongod` no longer raises an
error when you use an update operator like `$max`
with an empty operand expression ( `{ }` ). An empty update results
in no changes and no oplog entry is created (meaning that the
operation is a no-op).

## Examples

### Use `$max` to Compare Numbers

Create the `scores` collection:

```javascript
db.scores.insertOne( { _id: 1, highScore: 800, lowScore: 200 } )
```

The `highScore` for the document currently has the value 800. The
following operation:

- Compares the `highscore`, 800, to the specified value, 950
- Updates `highScore` to 950 since 950 is greater than 800

```javascript
db.scores.updateOne( { _id: 1 }, { $max: { highScore: 950 } } )
```

The `scores` collection now contains the following modified document:

```javascript
{ _id: 1, highScore: 950, lowScore: 200 }
```

The next operation has no effect since the value of `highScore`, 950,
is greater than 870:

```javascript
db.scores.updateOne( { _id: 1 }, { $max: { highScore: 870 } } )
```

The document remains unchanged in the `scores` collection:

```javascript
{ _id: 1, highScore: 950, lowScore: 200 }
```

### Use `$max` to Compare Dates

Create the `tags` collection:

```javascript
db.tags.insertOne(
   {
     _id: 1,
     desc: "crafts",
     dateEntered: ISODate("2013-10-01T05:00:00Z"),
     dateExpired: ISODate("2013-10-01T16:38:16.163Z")
   }
)
```

The following operation compares the current value of the
`dateExpired` field, `ISODate("2013-10-01T16:38:16.163Z")`, with
the specified date `new Date("2013-09-30")` to determine whether to
update the field:

```javascript
db.tags.updateOne(
   { _id: 1 },
   { $max: { dateExpired: new Date("2013-09-30") } }
)
```

`new Date("2013-09-30")` is not the newest date, so the operation
does *not* update the `dateExpired` field:

```javascript
{
   _id: 1,
   desc: "decorative arts",
   dateEntered: ISODate("2013-10-01T05:00:00Z"),
   dateExpired: ISODate("2013-10-01T16:38:16.163Z")
}
```

**See also:**

- `db.collection.updateMany()`
- `db.collection.findAndModify()`
