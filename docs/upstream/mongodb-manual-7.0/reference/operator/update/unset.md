<!-- Converted from reference/operator/update/unset.txt (reStructuredText). Includes are inlined. -->

# $unset (update operator)

## Definition

**Note:** Disambiguation

The following page refers to the update operator `$unset`.
For the aggregation stage, see `$unset`.

**`$unset`**

The `$unset` operator deletes a particular field.

## Compatibility

You can use `$unset` for deployments hosted in the following
environments:

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas): The fully
  managed service for MongoDB deployments in the cloud
- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Syntax

The `$unset` operator has the following form:

```javascript
{ $unset: { <field1>: "", ... } }
```

The specified value in the `$unset` expression (that is,
`""`) does not impact the operation.

To specify a `<field>` in an embedded document or in an array, use
dot notation.

## Behavior

Starting in MongoDB 5.0, update operators process document fields with
string-based names in lexicographic order. Fields with numeric names are
processed in numeric order. See Update Operators Behavior for details.

If the field does not exist, then `$unset` does nothing (that
is, no operation).

When used with `$` to match an array element, `$unset`
replaces the matching element with `null` rather than removing the
matching element from the array. This behavior keeps consistent the
array size and element positions.

Starting in MongoDB 5.0, `mongod` no longer raises an
error when you use an update operator like `$unset`
with an empty operand expression ( `{ }` ). An empty update results
in no changes and no oplog entry is created (meaning that the
operation is a no-op).

## Example

The examples on this page use data from the sample_mflix dataset. For details on how to load this dataset into your self-managed
MongoDB deployment, see Load the Sample Dataset.
If you made any modifications to the sample databases, you may need to drop and
recreate the databases to run the examples on this page. 

The following example uses the `$unset` operator to remove
the `label` and `status` fields from the matching movie document:

```javascript
db.movies.updateOne(
   { title: "The Dark Knight" },
   { $unset: { label: "", status: "" } }
)
```

The operation returns the following result:

```javascript
{
  acknowledged: true,
  insertedId: null,
  matchedCount: 1,
  modifiedCount: 1,
  upsertedCount: 0
}
```

**See also:**

`db.collection.updateMany()`
`db.collection.findAndModify()`
