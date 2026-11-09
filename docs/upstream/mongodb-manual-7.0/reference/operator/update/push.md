<!-- Converted from reference/operator/update/push.txt (reStructuredText). Includes are inlined. -->

# $push (update operator)

## Definition

**`$push`**

The `$push` operator appends a specified value to an array.

## Compatibility

You can use `$push` for deployments hosted in the following
environments:

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas): The fully
  managed service for MongoDB deployments in the cloud
- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Syntax

The `$push` operator has the form:

```javascript
{ $push: { <field1>: <value1>, ... } }
```

To specify a `<field>` in an embedded document or in an array, use
dot notation.

## Behavior

Starting in MongoDB 5.0, update operators process document fields with
string-based names in lexicographic order. Fields with numeric names are
processed in numeric order. See Update Operators Behavior for details.

If the field is absent in the document to update, `$push` adds
the array field with the value as its element.

If the field is **not** an array, the operation fails.

If the value is an array, `$push` appends the whole array as a
*single* element. To add each element of the value separately, use the
`$each` modifier with `$push`. For an example, see
example-push-each. For a list of modifiers available for
`$push`, see push-modifiers.

Starting in MongoDB 5.0, `mongod` no longer raises an
error when you use an update operator like `$push`
with an empty operand expression ( `{ }` ). An empty update results
in no changes and no oplog entry is created (meaning that the
operation is a no-op).

## Modifiers

You can use the `$push` operator with the following modifiers:

| Modifier | Description |
|---|---|
| `$each` | Appends multiple values to the array field. |
| `$slice` | Limits the number of array elements. Requires the use of the `$each` modifier. |
| `$sort` | Orders elements of the array. Requires the use of the `$each` modifier. |
| `$position` | Specifies the location in the array at which to insert the new elements. Requires the use of the `$each` modifier. Without the `$position` modifier, the `$push` appends the elements to the end of the array. |

When used with modifiers, the `$push` operator has the form:

```javascript
{ $push: { <field1>: { <modifier1>: <value1>, ... }, ... } }
```

The processing of the `$push` operation with modifiers occur
in the following order, regardless of the order in which the modifiers
appear:

#. Update array to add elements in the correct position.

#. Apply sort, if specified.

#. Slice the array, if specified.

#. Store the array.

## Examples

The examples on this page use data from the sample_mflix dataset. For details on how to load this dataset into your self-managed
MongoDB deployment, see Load the Sample Dataset.
If you made any modifications to the sample databases, you may need to drop and
recreate the databases to run the examples on this page. 

### Append a Value to an Array

The following example uses the `$push` operator to append
`"Classic"` to the `genres` array in the matching movie document:

```javascript
db.movies.updateOne(
   { title: "The Dark Knight" },
   { $push: { genres: "Classic" } }
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

### Append a Value to Arrays in Multiple Documents

The following example uses the `$push` operator to append
`"Acclaimed"` to the `genres` array in all matching movie documents:

```javascript
db.movies.updateMany(
   { "imdb.rating": { $gt: 9 } },
   { $push: { genres: "Acclaimed" } }
)
```

The operation returns the following result:

```javascript
{
  acknowledged: true,
  insertedId: null,
  matchedCount: '...',
  modifiedCount: '...',
  upsertedCount: 0
}
```

### Append Multiple Values to an Array

Use `$push` with the `$each` modifier to append
multiple values to the array field.

```javascript
db.movies.updateOne(
   { title: "The Dark Knight" },
   { $push: { genres: { $each: [ "Modern Classic", "Award-Winning" ] } } }
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

### Use `$push` Operator with Multiple Modifiers

Add the following document to the `students` collection:

```javascript
db.students.insertOne(
   {
      "_id" : 5,
      "quizzes" : [
         { "wk": 1, "score" : 10 },
         { "wk": 2, "score" : 8 },
         { "wk": 3, "score" : 5 },
         { "wk": 4, "score" : 6 }
      ]
   }
)
```

The following `$push` operation uses:

- the `$each` modifier to add multiple documents to the
  `quizzes` array,

- the `$sort` modifier to sort all the elements of the
  modified `quizzes` array by the `score` field in descending
  order, and

- the `$slice` modifier to keep only the **first** three
  sorted elements of the `quizzes` array.

```javascript
db.students.updateOne(
   { _id: 5 },
   {
     $push: { 
       quizzes: { 
          $each: [ { wk: 5, score: 8 }, { wk: 6, score: 7 }, { wk: 7, score: 6 } ],
          $sort: { score: -1 },
          $slice: 3
       }
     }
   }
)
```

After the operation only the three highest scoring quizzes are in the array:

```javascript
{
  "_id" : 5,
  "quizzes" : [
     { "wk" : 1, "score" : 10 },
     { "wk" : 2, "score" : 8 },
     { "wk" : 5, "score" : 8 }
  ]
}
```

**See also:**

- `db.collection.updateMany()`
- `db.collection.findAndModify()`
