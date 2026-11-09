<!-- Converted from reference/operator/update/sort.txt (reStructuredText). Includes are inlined. -->

# $sort

**`$sort`**

The `$sort` modifier orders the elements of an array
during a `$push` operation.

To use the `$sort` modifier, it **must** appear with the
`$each` modifier. You can pass an empty array `[]` to the
`$each` modifier such that only the `$sort` modifier
has an effect.

```javascript
{
  $push: {
     <field>: {
       $each: [ <value1>, <value2>, ... ],
       $sort: <sort specification>
     }
  }
}
```

For `<sort specification>`:

- To sort array elements that are not documents, or if the array
  elements are documents, to sort by the whole documents, specify
  `1` for ascending or `-1` for descending.

- If the array elements are documents, to sort by a field in the
  documents, specify a sort document with the field and the
  direction, i.e. `{ field: 1 }` or `{ field: -1 }`. Do **not**
  reference the containing array field in the sort specification
  (e.g. `{ "arrayField.field": 1 }` is incorrect).

## Behavior

Starting in MongoDB 5.0, update operators process document fields with
string-based names in lexicographic order. Fields with numeric names are
processed in numeric order. See Update Operators Behavior for details.

The `$sort` modifier can sort array elements that are not
documents. In previous versions, the `$sort` modifier required
the array elements be documents.

If the array elements are documents, the modifier can sort by either
the whole document or by a specific field in the documents. In previous
versions, the `$sort` modifier can only sort by a specific
field in the documents.

Trying to use the `$sort` modifier without the `$each`
modifier results in an error. The `$sort` no longer requires
the `$slice` modifier. For a list of modifiers available for
`$push`, see push-modifiers.

## Examples

### Sort Array of Documents by a Field in the Documents

Create the `students` collection:

```javascript
db.students.insertOne(
   {
     "_id": 1,
     "quizzes": [
       { "id" : 1, "score" : 6 },
       { "id" : 2, "score" : 9 }
     ]
   }
)
```

The following update appends additional documents to the `quizzes`
array and then sorts all the elements of the array by the ascending
`score` field:

```javascript
db.students.updateOne(
   { _id: 1 },
   {
     $push: {
       quizzes: {
         $each: [ { id: 3, score: 8 }, { id: 4, score: 7 }, { id: 5, score: 6 } ],
         $sort: { score: 1 }
       }
     }
   }
)
```

**Important:** The sort document refers directly to the field in the

documents and does not reference the containing array field
`quizzes`; i.e. `{ score: 1 }` and **not** `{ "quizzes.score": 1}`

After the update, the array elements are in order of ascending
`score` field:

```javascript
{
  "_id" : 1,
  "quizzes" : [
     { "id" : 1, "score" : 6 },
     { "id" : 5, "score" : 6 },
     { "id" : 4, "score" : 7 },
     { "id" : 3, "score" : 8 },
     { "id" : 2, "score" : 9 }
  ]
}
```

### Sort Array Elements That Are Not Documents

Add the following document to the `students` collection:

```javascript
db.students.insertOne( { "_id" : 2, "tests" : [  89,  70,  89,  50 ] } )
```

The following operation adds two more elements to the `tests` array
and sorts the elements:

```javascript
db.students.updateOne(
   { _id: 2 },
   { $push: { tests: { $each: [ 40, 60 ], $sort: 1 } } }
)
```

The updated document has the elements of the `tests` array in
ascending order:

```javascript
{ "_id" : 2, "tests" : [  40,  50,  60,  70,  89,  89 ] }
```

### Update Array Using Sort Only

Add the following document to the `students` collection:

```javascript
db.students.insertOne( { "_id" : 3, "tests" : [  89,  70,  100,  20 ] } )
```

To update the `tests` field to sort its elements in descending
order, specify the `{ $sort: -1 }` and specify an empty array `[]`
for the `$each` modifier. For example:

```javascript
db.students.updateOne(
   { _id: 3 },
   { $push: { tests: { $each: [ ], $sort: -1 } } }
)
```

The example sorts the `tests` field values in descending order:

```javascript
{ "_id" : 3, "tests" : [ 100,  89,  70,  20 ] }
```

### Use `$sort` with Other `$push` Modifiers

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

The order of the modifiers in the query does not change the order that
the modifiers are applied. For details, see push-modifiers.
