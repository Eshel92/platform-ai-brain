<!-- Converted from reference/operator/update/pop.txt (reStructuredText). Includes are inlined. -->

# $pop

## Definition

**`$pop`**

The `$pop` operator removes the first or last element of an
array. Pass `$pop` a value of `-1` to remove the first
element of an array and `1` to remove the last element in an
array.

The `$pop` operator has the form:

```javascript
{ $pop: { <field>: <-1 | 1>, ... } }
```

To specify a `<field>` in an embedded document or in an array, use
dot notation.

## Behavior

Starting in MongoDB 5.0, update operators process document fields with
string-based names in lexicographic order. Fields with numeric names are
processed in numeric order. See Update Operators Behavior for details.

The `$pop` operation fails if the `<field>` is not an array.

If the `$pop` operator removes the last item in the
`<field>`, the `<field>` will then hold an empty array.

Starting in MongoDB 5.0, `mongod` no longer raises an
error when you use an update operator like `$pop`
with an empty operand expression ( `{ }` ). An empty update results
in no changes and no oplog entry is created (meaning that the
operation is a no-op).

## Examples

### Remove the First Item of an Array

Create the `students` collection:

```javascript
db.students.insertOne( { _id: 1, scores: [ 8, 9, 10 ] } )
```

The following example removes the *first* element, 8, from the
`scores` array:

```javascript
db.students.updateOne( { _id: 1 }, { $pop: { scores: -1 } } )
```

The first element, 8, has been removed from the `scores` array:

```javascript
{ _id: 1, scores: [ 9, 10 ] }
```

### Remove the Last Item of an Array

Add the following document to the `students` collection:

```javascript
db.students.insertOne( { _id: 10, scores: [ 9, 10 ] } )
```

The following example removes the *last* element, 10, from the
`scores` array by specifying `1` in the `$pop` expression:

```javascript
db.students.updateOne( { _id: 10 }, { $pop: { scores: 1 } } )
```

The last element, 10, has been removed from the `scores` array:

```javascript
{ _id: 10, scores: [ 9 ] }
```

**See also:**

- `db.collection.updateMany()`
- `db.collection.findAndModify()`
