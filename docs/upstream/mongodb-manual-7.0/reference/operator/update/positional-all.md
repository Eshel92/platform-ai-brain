<!-- Converted from reference/operator/update/positional-all.txt (reStructuredText). Includes are inlined. -->

# \$[] (update operator)

## Definition

**`$[]`**

The all positional operator `$[]` indicates that the update
operator should modify all elements in the specified array field.

The `$[]` operator has the following form:

```javascript
{ <update operator>: { "<array>.$[]" : value } }
```

Use in update operations, e.g. `db.collection.updateOne()`
and `db.collection.findAndModify()`, to modify all array
elements for the document or documents that match the query
condition. For example:

```javascript
db.collection.updateOne(
   { <query conditions> },
   { <update operator>: { "<array>.$[]" : value } }
)
```

For an example, see positional-update-all.

## Behavior

Starting in MongoDB 5.0, update operators process document fields with
string-based names in lexicographic order. Fields with numeric names are
processed in numeric order. See Update Operators Behavior for details.

### `upsert`

If an upsert operation results in an insert, the `query` must
include an exact equality match on the array
field in order to use the `$[]` positional operator in the update
statement.

For example, the following upsert operation, which uses `$[]` in the
update document, specifies an exact equality match condition on the
array field:

```javascript
db.collection.updateOne(
   { myArray: [ 5, 8 ] },
   { $set: { "myArray.$[]": 10 } },
   { upsert: true }
)
```

If no such document exists, the operation would result in an insertion
of the following document:

```javascript
{ "_id" : ObjectId(...), "myArray" : [ 10, 10 ] }
```

If the upsert operation did not include an exact equality match and no
matching documents were found to update, the upsert operation would
error. 

For example, the following operations would error if no matching
documents were found to update:

```javascript
db.emptyCollection.updateOne(
   { },
   { $set: { "myArray.$[]": 10 } },
   { upsert: true }
)

db.emptyCollection.updateOne(
   { myArray: 5 },
   { $set: { "myArray.$[]": 10 } },
   { upsert: true }
)
```

### Nested Arrays

The `$[]` operator can be used for queries that traverse more than
one array and nested arrays.

For an example, see position-nested-arrays.

## Examples

### Update All Elements in an Array

Create the `students` collection:

```javascript
db.students.insertMany( [
   { "_id" : 1, "grades" : [ 85, 82, 80 ] },
   { "_id" : 2, "grades" : [ 88, 90, 92 ] },
   { "_id" : 3, "grades" : [ 85, 100, 90 ] }
] )
```

To increment all elements in the `grades` array by `10` for all
documents in the collection, use the all positional `$[]`
operator:

```javascript
db.students.updateMany(
   { },
   { $inc: { "grades.$[]": 10 } },
)
```

The all positional `$[]` operator acts as a placeholder for all
elements in the array field.

After the operation, the `students` collection contains the following
documents:

```javascript
{ "_id" : 1, "grades" : [ 95, 92, 90 ] }
{ "_id" : 2, "grades" : [ 98, 100, 102 ] }
{ "_id" : 3, "grades" : [ 95, 110, 100 ] }
```

### Update All Documents in an Array

The `$[]` positional operator facilitates updates to arrays
that contain embedded documents. To access the fields in the embedded
documents, use the dot notation with the
`$[]` operator.

```javascript
db.collection.updateOne(
   { <query selector> },
   { <update operator>: { "array.$[].field" : value } }
)
```

Create the `students2` collection:

```javascript
db.students2.insertMany( [
   {
      "_id" : 1,
      "grades" : [
         { "grade" : 80, "mean" : 75, "std" : 8 },
         { "grade" : 85, "mean" : 90, "std" : 6 },
         { "grade" : 85, "mean" : 85, "std" : 8 }
      ]
   },
   {
      "_id" : 2,
      "grades" : [
         { "grade" : 90, "mean" : 75, "std" : 8 },
         { "grade" : 87, "mean" : 90, "std" : 5 },
         { "grade" : 85, "mean" : 85, "std" : 6 }
      ]
   }
] )
```

To modify the value of the `std` field for all elements in the
`grades` array, use the positional `$[]` operator:

```javascript
db.students2.updateMany(
   { },
   { $inc: { "grades.$[].std" : -2 } },
)
```

After the operation, the collection has the following documents:

```javascript
{
   "_id" : 1,
   "grades" : [
      { "grade" : 80, "mean" : 75, "std" : 6 },
      { "grade" : 85, "mean" : 90, "std" : 4 },
      { "grade" : 85, "mean" : 85, "std" : 6 }
   ]
}
{
   "_id" : 2,
   "grades" : [
      { "grade" : 90, "mean" : 75, "std" : 6 },
      { "grade" : 87, "mean" : 90, "std" : 3 },
      { "grade" : 85, "mean" : 85, "std" : 4 }
   ]
}
```

### Update Arrays Specified Using a Negation Query Operator

Create the `results` collection:

```javascript
db.results.insertMany( [
   { "_id" : 1, "grades" : [ 85, 82, 80 ] },
   { "_id" : 2, "grades" : [ 88, 90, 92 ] },
   { "_id" : 3, "grades" : [ 85, 100, 90 ] }
] )
```

To increment all elements in the `grades` array by `10` for all
documents **except** those with the value `100` in the `grades`
array, use the all positional `$[]` operator:

```javascript
db.results.updateMany(
   { "grades" : { $ne: 100 } },
   { $inc: { "grades.$[]": 10 } },
)
```

The all positional `$[]` operator acts as a
placeholder for all elements in the array field.

After the operation, the `students` collection contains the following
documents:

```javascript
{ "_id" : 1, "grades" : [ 95, 92, 90 ] }
{ "_id" : 2, "grades" : [ 98, 100, 102 ] }
{ "_id" : 3, "grades" : [ 85, 100, 90 ] }
```

### Update Nested Arrays in Conjunction with `$[<identifier>]`

The `$[]` positional operator, in conjunction with filter
`$[<identifier>]` positional operator can be used to update nested
arrays.

Create a collection `students3` with the following documents:

```javascript
db.students3.insertMany( [
   { "_id" : 1,
      "grades" : [
        { type: "quiz", questions: [ 10, 8, 5 ] },
        { type: "quiz", questions: [ 8, 9, 6 ] },
        { type: "hw", questions: [ 5, 4, 3 ] },
        { type: "exam", questions: [ 25, 10, 23, 0 ] },
      ]
   }
] )
```

To update all values that are greater than or equal to `8` in the
nested `grades.questions` array, regardless of `type`:

```javascript
db.students3.updateMany(
   {},
   { $inc: { "grades.$[].questions.$[score]": 2 } },
   { arrayFilters: [  { "score": { $gte: 8 } } ] } 
)
```

The updated documents look like this: 

```javascript
{
  _id: 1,
  grades: [
    { type: 'quiz', questions: [ 12, 10, 5 ] },
    { type: 'quiz', questions: [ 10, 11, 6 ] },
    { type: 'hw', questions: [ 5, 4, 3 ] },
    { type: 'exam', questions: [ 27, 12, 25, 0 ] }
  ]
}
```

**See also:**

- `$[<identifier>]`
- `db.collection.updateMany()`
- `db.collection.findAndModify()`
- `$elemMatch`

## Learn More

For examples that use the `$[]` operator to update arrays, see
array-updates-mql.
