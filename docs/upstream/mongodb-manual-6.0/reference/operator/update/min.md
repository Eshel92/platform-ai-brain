<!-- Converted from reference/operator/update/min.txt (reStructuredText). Includes are inlined. -->

# $min

## Definition

**`$min`**

The `$min` updates the value of the field to a specified
value *if* the specified value is **less than** the current value of
the field. The `$min` operator can compare values of
different types, using the BSON comparison order.

```javascript
{ $min: { <field1>: <value1>, ... } }
```

To specify a `<field>` in an embedded document or in an array, use
dot notation.

## Behavior

Starting in MongoDB 5.0, update operators process document fields with
string-based names in lexicographic order. Fields with numeric names are
processed in numeric order. See Update Operators Behavior for details.

If the field does not exist, the `$min` operator sets the
field to the specified value.

For comparisons between values of different types, such as a number and
a null, `$min` uses the BSON comparison order.

Starting in MongoDB 5.0, `mongod` no longer raises an
error when you use an update operator like `$min`
with an empty operand expression ( `{ }` ). An empty update results
in no changes and no oplog entry is created (meaning that the
operation is a no-op).

## Examples

### Use `$min` to Compare Numbers

Create the `scores` collection:

```javascript
db.scores.insertOne( { _id: 1, highScore: 800, lowScore: 200 } )
```

The `lowScore` for the document currently has the value
`200`. The following operation uses `$min` to compare
`200` to the specified value `150` and updates the value of
`lowScore` to `150` since `150` is less than `200`:

```javascript
db.scores.updateOne( { _id: 1 }, { $min: { lowScore: 150 } } )
```

The `scores` collection now contains the following modified document:

```javascript
{ _id: 1, highScore: 800, lowScore: 150 }
```

The next operation has no effect since the current value of the
field `lowScore`, i.e `150`, is less than `250`:

```javascript
db.scores.updateOne( { _id: 1 }, { $min: { lowScore: 250 } } )
```

The document remains unchanged in the `scores` collection:

```javascript
{ _id: 1, highScore: 800, lowScore: 150 }
```

### Use `$min` to Compare Dates

Create the `tags` collection:

```javascript
db.tags.insertOne(
   {
     _id: 1,
     desc: "crafts",
     dateEntered: ISODate("2013-10-01T05:00:00Z"),
     dateExpired: ISODate("2013-10-01T16:38:16Z")
   }
)
```

The following operation compares the current value of the
`dateEntered` field, i.e. `ISODate("2013-10-01T05:00:00Z")`,
with the specified date `new Date("2013-09-25")` to determine
whether to update the field:

```javascript
db.tags.updateOne(
   { _id: 1 },
   { $min: { dateEntered: new Date("2013-09-25") } }
)
```

The operation updates the `dateEntered` field:

```javascript
{
  _id: 1,
  desc: "crafts",
  dateEntered: ISODate("2013-09-25T00:00:00Z"),
  dateExpired: ISODate("2013-10-01T16:38:16Z")
}
```

**See also:**

- `db.collection.updateMany()`
- `db.collection.findAndModify()`
