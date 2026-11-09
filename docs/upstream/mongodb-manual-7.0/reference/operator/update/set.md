<!-- Converted from reference/operator/update/set.txt (reStructuredText). Includes are inlined. -->

# $set (update operator)

## Definition

**Note:** Disambiguation

The following page refers to the update operator `$set`.
For the aggregation stage, see `$set`.

**`$set`**

The `$set` operator replaces the value of a field with the
specified value.

## Compatibility

You can use `$set` for deployments hosted in the following
environments:

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas): The fully
  managed service for MongoDB deployments in the cloud
- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Syntax

The `$set` operator expression has the following form:

```javascript
{ $set: { <field1>: <value1>, ... } }
```

To specify a `<field>` in an embedded document or in an array, use
dot notation.

## Behavior

Starting in MongoDB 5.0, update operators process document fields with
string-based names in lexicographic order. Fields with numeric names are
processed in numeric order. See Update Operators Behavior for details.

If the field does not exist, `$set` adds a new field with the
specified value if the new field does not violate a type constraint.
If you specify a dotted path for a non-existent field,
`$set` creates the embedded documents *as needed* to
fulfill the dotted path to the field.

If you specify multiple field-value pairs, `$set` updates
or creates each field.

Starting in MongoDB 5.0, `mongod` no longer raises an
error when you use an update operator like `$set`
with an empty operand expression ( `{ }` ). An empty update results
in no changes and no oplog entry is created (meaning that the
operation is a no-op).

### Advantages of $set

The `$set` operator provides the following advantages compared to full
document replacement:

- **Targeted Updates**: `$set` modifies only the specified fields,
  ensuring efficient updates by avoiding unnecessary writes and
  overhead when you work with large documents.

- **Efficient Oplog Entries**: `$set` optimizes replication by writing only the
  updated fields to the oplog instead of the entire document. This
  process reduces the size of oplog entries and allows nodes to
  replicate changes more efficiently.

- **Simplified Logic**: Applications using `$set` do not need to compute
  changed fields before they send an update. MongoDB reduces complexity
  by handling the delta computation internally.

## Examples

The examples on this page use data from the sample_mflix dataset. For details on how to load this dataset into your self-managed
MongoDB deployment, see Load the Sample Dataset.
If you made any modifications to the sample databases, you may need to drop and
recreate the databases to run the examples on this page. 

### Set Top-Level Fields

The following example uses the `$set` operator to add the
`label` and `status` fields to the matching movie document:

```javascript
db.movies.updateOne(
   { title: "The Dark Knight" },
   {
      $set: {
         label: "Award Winner",
         status: "classic"
      }
   }
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

### Set Fields in Embedded Documents

The following example uses dot notation to update the `highlight`
field of the `imdb` embedded document in the matching movie:

```javascript
db.movies.updateOne(
   { title: "The Dark Knight" },
   { $set: { "imdb.highlight": "Critics' Choice" } }
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

**Important:**

The preceding example uses dot notation to update the `highlight`
field of the embedded `imdb` document. The following format
instead *replaces the entire embedded document*, removing all
other fields from `imdb`:

```javascript
db.movies.updateOne(
   { title: "The Dark Knight" },
   { $set: { imdb: { highlight: "Critics' Choice" } } }
)
```

### Set Elements in Arrays

The following example uses the `$set` operator to update the
first element (array index `0`) of the `genres` array in the
matching movie document:

```javascript
db.movies.updateOne(
   { title: "The Dark Knight" },
   { $set: { "genres.0": "Thriller" } }
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

For additional update operators for arrays, see
/reference/operator/update-array.

**See also:**

- `db.collection.updateMany()`
- `db.collection.findAndModify()`
