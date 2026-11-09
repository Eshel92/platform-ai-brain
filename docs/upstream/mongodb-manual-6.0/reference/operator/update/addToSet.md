<!-- Converted from reference/operator/update/addToSet.txt (reStructuredText). Includes are inlined. -->

# $addToSet

## Definition

**`$addToSet`**

The `$addToSet` operator adds a value to an array unless the value
is already present, in which case `$addToSet` does nothing to that
array.

## Compatibility

You can use `$addToSet` for deployments hosted in the following
environments:

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas?tck=docs_server): The fully
  managed service for MongoDB deployments in the cloud
- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Syntax

The `$addToSet` operator has the form:

```javascript
{ $addToSet: { <field1>: <value1>, ... } }
```

To specify a `<field>` in an embedded document or in an array, use
dot notation.

## Behavior

Starting in MongoDB 5.0, update operators process document fields with
string-based names in lexicographic order. Fields with numeric names are
processed in numeric order. See Update Operators Behavior for details.

`$addToSet` only ensures that there are no duplicate items
*added* to the set and does not affect existing duplicate elements.
`$addToSet` does not guarantee a particular ordering of
elements in the modified set.

Starting in MongoDB 5.0, `mongod` no longer raises an
error when you use an update operator like `$addToSet`
with an empty operand expression ( `{ }` ). An empty update results
in no changes and no oplog entry is created (meaning that the
operation is a no-op).

### Missing Field

If you use `$addToSet` on a field that is absent from the
document to update, `$addToSet` creates the array field with
the specified value as its element.

### Field is Not an Array

If you use `$addToSet` on a field that is **not** an array, the
operation will fail. 

For example, create the `pigments` collection:

```javascript
db.pigments.insertOne( { _id: 1, colors: "blue, green, red" } )
```

The `colors` field is not an array. The following `$addToSet`
operation fails:

```javascript
db.pigments.updateOne(
   { _id: 1 },
   { $addToSet: { colors: "mauve" } }
)
```

### Value to Add is An Array

If the value is an array, `$addToSet` appends the whole array
as a *single* element.

Create the `alphabet` collection:

```javascript
db.alphabet.insertOne( { _id: 1, letters: ["a", "b"] } )
```

The following operation appends the array `[ "c", "d" ]` to the
`letters` field:

```javascript
db.alphabet.updateOne(
   { _id: 1 },
   { $addToSet: { letters: [ "c", "d" ] } }
)
```

The array `[ "c", "d" ]` is added as a single element:

```javascript
{ _id: 1, letters: [ 'a', 'b', [ 'c', 'd' ] ] }
```

**Tip:**

To add each element of the value **separately**, use the
`$each` modifier with `$addToSet`. See
addToSet-modifiers for details.

### Value to Add is a Document

If the value is a document, MongoDB determines that the document is a
duplicate if an existing document in the array matches the to-be-added
document exactly; i.e. the existing document has the exact same fields
and values *and* the fields are in the same order. As such, field order
matters and you cannot specify that MongoDB compare only a subset of
the fields in the document to determine whether the document is a
duplicate of an existing array element.

## Examples

Create the `inventory` collection:

```javascript
db.inventory.insertOne( 
   { _id: 1, item: "polarizing_filter", tags: [ "electronics", "camera" ] }
)
```

### Add to Array

The following operation adds the element `"accessories"` to the
`tags` array since `"accessories"` does not exist in the array:

```javascript
db.inventory.updateOne(
   { _id: 1 },
   { $addToSet: { tags: "accessories" } }
)
```

### Value Already Exists

The following `$addToSet` operation has no effect because
`"camera"` is already an element of the `tags` array:

```javascript
db.inventory.updateOne(
   { _id: 1 },
   { $addToSet: { tags: "camera"  } }
)
```

### `$each` Modifier

You can use the `$addToSet` operator with the
`$each` modifier. The `$each` modifier allows the
`$addToSet` operator to add multiple values to the array
field.

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

**See also:**

- `db.collection.updateMany()`
- `db.collection.findAndModify()`
- `$push`
- `$pull`
