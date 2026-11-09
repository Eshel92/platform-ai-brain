<!-- Converted from reference/operator/update/positional.txt (reStructuredText). Includes are inlined. -->

# \$ (update)

## Definition

**`$`**

The positional `$` operator identifies an element in
an array to update without explicitly specifying the position of the
element in the array.

**Note:** Disambiguation

- To project, or return, an array element from a read operation,
  see the `$` projection operator instead.

- To update all elements in an array, see the all positional
  operator  `$[]` instead.

- To update all elements that match an array filter condition or
  conditions, see the filtered positional operator instead
  `$[<identifier>]`.

## Compatibility

You can use the positional `$` operator for deployments hosted in the following
environments:

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas?tck=docs_server): The fully
  managed service for MongoDB deployments in the cloud
- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Syntax

The positional `$` operator has the form:

```javascript
{ "<array>.$" : value }
```

When used with update operations, e.g.
`db.collection.updateOne()` and
`db.collection.findAndModify()`,

- the positional `$` operator acts as a placeholder for
  the **first** element that matches the `query document`, and

- the `array` field **must** appear as part of the ``query
  document``.

For example:

```javascript
db.collection.updateOne(
   { <array>: value ... },
   { <update operator>: { "<array>.$" : value } }
)
```

## Behavior

Starting in MongoDB 5.0, update operators process document fields with
string-based names in lexicographic order. Fields with numeric names are
processed in numeric order. See Update Operators Behavior for details.

### `upsert`

Do not use the positional operator `$` with
upsert operations because inserts will use the `$` as
a field name in the inserted document.

### Nested Arrays

The positional `$` operator cannot be used for queries which
traverse more than one array, such as queries that traverse arrays
nested within other arrays, because the replacement for the
`$` placeholder is a single value

### Unsets

When used with the `$unset` operator, the positional
`$` operator does not remove the matching element
from the array but rather sets it to `null`.

### Negations

If the query matches the array using a negation operator, such as
`$ne`, `$not`, or `$nin`, then you cannot use the
positional operator to update values from this array.

However, if the negated portion of the query is inside of an
`$elemMatch` expression, then you *can* use the positional
operator to update this field.

### Multiple Array Matches

The positional `$` update operator behaves ambiguously when filtering
on multiple array fields.

When the server executes an update method, it first runs a query to determine
which documents you want to update. If the update filters documents on multiple
array fields, the subsequent call to the positional `$` update operator
doesn't always update the required position in the array.

For more information, see the example.

## Examples

### Update Values in an Array

Create a collection `students` with the following documents:

```javascript
db.students.insertMany( [
   { "_id" : 1, "grades" : [ 85, 80, 80 ] },
   { "_id" : 2, "grades" : [ 88, 90, 92 ] },
   { "_id" : 3, "grades" : [ 85, 100, 90 ] }
] )
```

To update the first element whose value is `80` to `82` in the in
the `grades` array, use the positional `$` operator if you do
not know the position of the element in the array:

**Important:**

You must include the array field as part of the `query` document.

```javascript
db.students.updateOne(
   { _id: 1, grades: 80 },
   { $set: { "grades.$" : 82 } }
)
```

The positional `$` operator acts as a placeholder for the
**first match** of the update query document.

After the operation, the `students` collection contains the following
documents:

```javascript
{ "_id" : 1, "grades" : [ 85, 82, 80 ] }
{ "_id" : 2, "grades" : [ 88, 90, 92 ] }
{ "_id" : 3, "grades" : [ 85, 100, 90 ] }
```

### Update Documents in an Array

The positional `$` operator facilitates updates to arrays
that contain embedded documents. Use the positional `$`
operator to access the fields in the embedded documents with the
dot notation on the
`$` operator.

```javascript
db.collection.updateOne(
   { <query selector> },
   { <update operator>: { "array.$.field" : value } }
)
```

Consider the following document in the `students` collection whose
`grades` element value is an array of embedded documents:

```javascript
{
  _id: 4,
  grades: [
     { grade: 80, mean: 75, std: 8 },
     { grade: 85, mean: 90, std: 5 },
     { grade: 85, mean: 85, std: 8 }
  ]
}
```

Use the positional `$` operator to update the `std` field of
the first array element that matches the `grade` equal to `85`
condition:

**Important:**

You must include the array field as part of the `query` document.

```javascript
db.students.updateOne(
   { _id: 4, "grades.grade": 85 },
   { $set: { "grades.$.std" : 6 } }
)
```

After the operation, the document has the following updated values:

```javascript
{ 
   "_id" : 4,
   "grades" : [
      { "grade" : 80, "mean" : 75, "std" : 8 },
      { "grade" : 85, "mean" : 90, "std" : 6 },
      { "grade" : 85, "mean" : 85, "std" : 8 }
   ]
}
```

### Update Embedded Documents Using Multiple Field Matches

The `$` operator can update the first array element that matches
multiple query criteria specified with the `$elemMatch` operator.

Consider the following document in the `students` collection whose
`grades` field value is an array of embedded documents:

```javascript
{
  _id: 5,
  grades: [
     { grade: 80, mean: 75, std: 8 },
     { grade: 85, mean: 90, std: 5 },
     { grade: 90, mean: 85, std: 3 }
  ]
}
```

In the example below, the `$` operator updates the value of the
`std` field in the first embedded document that has `grade` field with
a value less than or equal to `90` and a `mean` field with a value
greater than `80`:

```javascript
db.students.updateOne(
   {
     _id: 5,
     grades: { $elemMatch: { grade: { $lte: 90 }, mean: { $gt: 80 } } }
   },
   { $set: { "grades.$.std" : 6 } }
)
```

This operation updates the first embedded document that matches the
criteria, namely the second embedded document in the array:

```javascript
{
  _id: 5,
  grades: [
    { grade: 80, mean: 75, std: 8 },
    { grade: 85, mean: 90, std: 6 },
    { grade: 90, mean: 85, std: 3 }
  ]
}
```

### Update with Multiple Array Matches

The positional `$` update operator behaves ambiguously when the
query has multiple array fields to filter documents in the collection.

Consider a document in the `students_deans_list` collection, which holds
arrays of student information:

```javascript
db.students_deans_list.insertMany( [
   {
      _id: 8,
      activity_ids: [ 1, 2 ],
      grades: [ 90, 95 ],
      deans_list: [ 2021, 2020 ]
   }
] )
```

In the following example, the user attempts to modify the `deans_list` field,
filtering documents using the `activity_ids`, `deans_list`, and `grades`
fields, and updating the 2021 value in the `deans_list` field to 2022:

```javascript
db.students_deans_list.updateOne(
   { activity_ids: 1, grades: 95, deans_list: 2021 },
   { $set: { "deans_list.$": 2022 } }
)
```

When the server executes the `updateOne` method above, it filters
the available documents using values in the supplied array fields.
Although the `deans_list` field is used in the filter, it is not the field
used by the positional `$` update operator to determine which position
in the array to update:

```javascript
db.students_deans_list.find( { _id: 8 } )
```

Example output:

```javascript
{
   _id: 8,
   activity_ids: [ 1, 2 ],
   grades: [ 90, 95 ],
   deans_list: [ 2021, 2022 ]
}
```

The `updateOne` method matched the `deans_list` field on 2021, but the
positional `$` update operator instead changed the 2020 value to 2022.

To avoid unexpected results when matching on multiple arrays, instead
use the filtered positional operator `$[<identifier>]`.

**See also:**

- `db.collection.updateMany()`
- `db.collection.findAndModify()`
- `$elemMatch`
