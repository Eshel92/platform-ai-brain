<!-- Converted from reference/operator/update/pullAll.txt (reStructuredText). Includes are inlined. -->

# $pullAll

## Definition

**`$pullAll`**

The `$pullAll` operator removes all instances of the
specified values from an existing array. Unlike the `$pull`
operator that removes elements by specifying a query,
`$pullAll` removes elements that match the listed values.

The `$pullAll` operator has the form:

```javascript
{ $pullAll: { <field1>: [ <value1>, <value2> ... ], ... } }
```

To specify a `<field>` in an embedded document or in an array, use
dot notation.

## Behavior

Starting in MongoDB 5.0, update operators process document fields with
string-based names in lexicographic order. Fields with numeric names are
processed in numeric order. See Update Operators Behavior for details.

If a `<value>` to remove is a document or an array,
`$pullAll` removes only the elements in the array that match
the specified `<value>` exactly, including order.

Starting in MongoDB 5.0, `mongod` no longer raises an
error when you use an update operator like `$pullAll`
with an empty operand expression ( `{ }` ). An empty update results
in no changes and no oplog entry is created (meaning that the
operation is a no-op).

## Examples

Create the `survey` collection:

```javascript
db.survey.insertOne( { _id: 1, scores: [ 0, 2, 5, 5, 1, 0 ] } )
```

The following operation removes all instances of the values "0" and "5"
from the `scores` array:

```javascript
db.survey.updateOne( { _id: 1 }, { $pullAll: { scores: [ 0, 5 ] } } )
```

After the update, the `scores` field no longer has any instances of
"0" or "5".

```javascript
{ "_id" : 1, "scores" : [ 2, 1 ] }
```

**See also:**

- `db.collection.updateMany()`
- `db.collection.findAndModify()`
