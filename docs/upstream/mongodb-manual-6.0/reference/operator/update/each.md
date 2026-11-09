<!-- Converted from reference/operator/update/each.txt (reStructuredText). Includes are inlined. -->

# $each

## Definition

**`$each`**

The `$each` modifier is available for use with the
`$addToSet` operator and the `$push`
operator.

Use with the `$addToSet` operator to add multiple values to
an array `<field>` if the values do not exist in the `<field>`.

```javascript
{ $addToSet: { <field>: { $each: [ <value1>, <value2> ... ] } } }
```

Use with the `$push` operator to append multiple values to
an array `<field>`.

```javascript
{ $push: { <field>: { $each: [ <value1>, <value2> ... ] } } }
```

The `$push` operator can use `$each` modifier with
other modifiers. For a list of modifiers available for
`$push`, see push-modifiers.

## Behavior

Starting in MongoDB 5.0, update operators process document fields with
string-based names in lexicographic order. Fields with numeric names are
processed in numeric order. See Update Operators Behavior for details.

## Examples

### Use `$each`  with `$push` Operator

The following example appends each element of `[ 90, 92, 85 ]` to
the `scores` array for the document where the `name` field
equals `joe`:

```javascript
db.students.updateOne(
   { name: "joe" },
   { $push: { scores: { $each: [ 90, 92, 85 ] } } }
)
```

### Use `$each`  with `$addToSet` Operator

A collection `inventory` has the following document:

```javascript
db.inventory.insertOne (
   { _id: 2, item: "cable", tags: [ "electronics", "supplies" ] }
)
```

Then the following operation uses the `$addToSet` operator
with the `$each` modifier to add multiple elements to the
`tags` array:

```javascript
db.inventory.updateOne(
   { _id: 2 },
   { $addToSet: { tags: { $each: [ "camera", "electronics", "accessories" ] } } }
 )
```

The operation only adds `"camera"` and `"accessories"` to the
`tags` array. `"electronics"` was already in the array:

```javascript
{
  _id: 2,
  item: "cable",
  tags: [ "electronics", "supplies", "camera", "accessories" ]
}
```
