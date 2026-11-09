<!-- Converted from reference/operator/update/slice.txt (reStructuredText). Includes are inlined. -->

# $slice (update operator)

**`$slice`**

The `$slice` modifier limits the number of array
elements during a `$push` operation. To project, or return,
a specified number of array elements from a read operation, see the
`$slice` projection operator instead.

To use the `$slice` modifier, it **must** appear with the
`$each` modifier. You can pass an empty array `[]` to the
`$each` modifier such that only the `$slice`
modifier has an effect.

```javascript
{
  $push: {
     <field>: {
       $each: [ <value1>, <value2>, ... ],
       $slice: <num>
     }
  }
}
```

The `<num>` can be:

| Value | Description |
|---|---|
| Zero | To update the array `<field>` to an empty array. |
| Negative | To update the array `<field>` to contain only the last `<num>` elements. |
| Positive | To update the array `<field>` contain only the first `<num>` elements. |

## Behavior

Starting in MongoDB 5.0, update operators process document fields with
string-based names in lexicographic order. Fields with numeric names are
processed in numeric order. See Update Operators Behavior for details.

The order in which the modifiers appear is immaterial. Previous
versions required the `$each` modifier to appear as the first
modifier if used in conjunction with `$slice`. For a list of
modifiers available for `$push`, see push-modifiers.

Trying to use the `$slice` modifier without the `$each`
modifier results in an error.

## Examples

### Slice from the End of the Array

A collection `students` contains the following document:

```javascript
{ "_id" : 1, "scores" : [ 40, 50, 60 ] }
```

The following operation adds new elements to the `scores` array, and
then uses the `$slice` modifier to trim the array to the
last five elements:

```javascript
db.students.updateOne(
   { _id: 1 },
   {
     $push: {
       scores: {
         $each: [ 80, 78, 86 ],
         $slice: -5
       }
     }
   }
)
```

The result of the operation is slice the elements of the updated
`scores` array to the last five elements:

```javascript
{ "_id" : 1, "scores" : [  50,  60,  80,  78,  86 ] }
```

### Slice from the Front of the Array

A collection `students` contains the following document:

```javascript
{ "_id" : 2, "scores" : [ 89, 90 ] }
```

The following operation adds new elements to the `scores` array, and
then uses the `$slice` modifier to trim the array to the
first three elements.

```javascript
db.students.updateOne(
   { _id: 2 },
   {
     $push: {
       scores: {
         $each: [ 100, 20 ],
         $slice: 3
       }
     }
   }
)
```

The result of the operation is to slice the elements of the updated
`scores` array to the first three elements:

```javascript
{ "_id" : 2, "scores" : [  89,  90,  100 ] }
```

### Update Array Using Slice Only

A collection `students` contains the following document:

```javascript
{ "_id" : 3, "scores" : [  89,  70,  100,  20 ] }
```

To update the `scores` field with just the effects of the
`$slice` modifier, specify the number of elements to slice
(e.g. `-3`) for the `$slice` modifier and an empty
array `[]` for the `$each` modifier, as in the following:

```javascript
db.students.updateOne(
  { _id: 3 },
  {
    $push: {
      scores: {
         $each: [ ],
         $slice: -3
      }
    }
  }
)
```

The result of the operation is to slice the elements of the `scores`
array to the last three elements:

```javascript
{ "_id" : 3, "scores" : [  70,  100,  20 ] }
```

### Use `$slice` with Other `$push` Modifiers

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

The order of the modifiers is immaterial to the order in which the
modifiers are processed. See push-modifiers for details.
