<!-- Converted from reference/operator/aggregation/sum.txt (reStructuredText). Includes are inlined. -->

# $sum (aggregation)

## Definition

**`$sum`**

**Changed in version:** 5.0

Calculates and returns the collective sum of numeric values.
`$sum` ignores non-numeric values.

`$sum` is available in these stages:

- `$addFields`

- `$bucket`

- `$bucketAuto`

- `$group`

- `$match` stage that includes an `$expr`
  expression

- `$project`

- `$replaceRoot` 

- `$replaceWith` 

- `$set`

- `$setWindowFields` (Available starting in MongoDB 5.0)

## Compatibility

You can use `$sum` for deployments hosted in the following
environments:

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas?tck=docs_server): The fully
  managed service for MongoDB deployments in the cloud
- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Syntax

When used as an accumulator,  
`$sum` has this syntax:

```none
{ $sum: <expression> }
```

   
When not used as an accumulator, `$sum` has this syntax:

```none
{ $sum: [ <expression1>, <expression2> ... ]  }
```

For more information on expressions, see
aggregation-expressions.

## Behavior

### Result Data Type

The result will have the same type as the input except when it cannot be
represented accurately in that type. In these cases:

- A 32-bit integer will be converted to a 64-bit integer if the
  result is representable as a 64-bit integer.

- A 32-bit integer will be converted to a double if the result is
  not representable as a 64-bit integer.

- A 64-bit integer will be converted to double if the result is not
  representable as a 64-bit integer.

### Non-Numeric or Non-Existent Fields

If used on a field that contains both numeric and non-numeric values,
`$sum` ignores the non-numeric values and returns the sum of the
numeric values.

If used on a field that does not exist in any document in the collection,
`$sum` returns `0` for that field.

If all operands are non-numeric, non-arrays, or contain `null` values,
`$sum` returns `0`. For details on how `$sum` handles arrays,
see sum-array-operand.

### Array Operand

In the `$group` stage, if the expression resolves to an array,
`$sum` treats the operand as a non-numeric value.

In the other supported stages:

- With a single expression as its operand, if the expression resolves
  to an array, `$sum` traverses into the array to operate on the
  numeric elements of the array to return a single value.

- With a list of expressions as its operand, if any of the expressions
  resolves to an array, `$sum` does **not** traverse into the
  array but instead treats the array as a non-numeric value.

For example, when not used in a `$group` stage:

- If the `$sum` operand is `[ 2, 2 ]`, `$sum` adds the array
  elements and returns 4.

- If the `$sum` operand is `[ 2, [ 3, 4 ] ]`, `$sum` returns 2
  because it treats the nested array `[ 3, 4 ]` as a non-numeric
  value.

## Examples

### Use in `$group` Stage

Consider a `sales` collection with the following documents:

```javascript
{ "_id" : 1, "item" : "abc", "price" : 10, "quantity" : 2, "date" : ISODate("2014-01-01T08:00:00Z") }
{ "_id" : 2, "item" : "jkl", "price" : 20, "quantity" : 1, "date" : ISODate("2014-02-03T09:00:00Z") }
{ "_id" : 3, "item" : "xyz", "price" : 5, "quantity" : 5, "date" : ISODate("2014-02-03T09:05:00Z") }
{ "_id" : 4, "item" : "abc", "price" : 10, "quantity" : 10, "date" : ISODate("2014-02-15T08:00:00Z") }
{ "_id" : 5, "item" : "xyz", "price" : 5, "quantity" : 10, "date" : ISODate("2014-02-15T09:05:00Z") }
```

Grouping the documents by the day and the year of the `date` field,
the following operation uses the `$sum` accumulator to compute the
total amount and the count for each group of documents.

```javascript
db.sales.aggregate(
   [
     {
       $group:
         {
           _id: { day: { $dayOfYear: "$date"}, year: { $year: "$date" } },
           totalAmount: { $sum: { $multiply: [ "$price", "$quantity" ] } },
           count: { $sum: 1 }
         }
     }
   ]
)
```

The operation returns the following results:

```javascript
{ "_id" : { "day" : 46, "year" : 2014 }, "totalAmount" : 150, "count" : 2 }
{ "_id" : { "day" : 34, "year" : 2014 }, "totalAmount" : 45, "count" : 2 }
{ "_id" : { "day" : 1, "year" : 2014 }, "totalAmount" : 20, "count" : 1 }
```

Using `$sum` on a non-existent field returns a value of `0`.
The following operation attempts to `$sum` on `qty`:

```javascript
db.sales.aggregate(
   [
     {
       $group:
         {
           _id: { day: { $dayOfYear: "$date"}, year: { $year: "$date" } },
           totalAmount: { $sum: "$qty" },
           count: { $sum: 1 }
         }
     }
   ]
)
```

The operation returns:

```javascript
{ "_id" : { "day" : 46, "year" : 2014 }, "totalAmount" : 0, "count" : 2 }
{ "_id" : { "day" : 34, "year" : 2014 }, "totalAmount" : 0, "count" : 2 }
{ "_id" : { "day" : 1, "year" : 2014 }, "totalAmount" : 0, "count" : 1 }
```

The `$count` aggregation accumulator can be used in place of
`{ $sum : 1 }` in the `$group` stage. 

**See also:**

`$count (aggregation accumulator)`

### Use in `$project` Stage

A collection `students` contains the following documents:

```javascript
{ "_id": 1, "quizzes": [ 10, 6, 7 ], "labs": [ 5, 8 ], "final": 80, "midterm": 75 }
{ "_id": 2, "quizzes": [ 9, 10 ], "labs": [ 8, 8 ], "final": 95, "midterm": 80 }
{ "_id": 3, "quizzes": [ 4, 5, 5 ], "labs": [ 6, 5 ], "final": 78, "midterm": 70 }
```

The following example uses the `$sum` in the
`$project` stage to calculate the total quiz scores, the
total lab scores, and the total of the final and the midterm:

```javascript
db.students.aggregate([
   {
     $project: {
       quizTotal: { $sum: "$quizzes"},
       labTotal: { $sum: "$labs" },
       examTotal: { $sum: [ "$final", "$midterm" ] }
     }
   }
])
```

The operation results in the following documents:

```javascript
{ "_id" : 1, "quizTotal" : 23, "labTotal" : 13, "examTotal" : 155 }
{ "_id" : 2, "quizTotal" : 19, "labTotal" : 16, "examTotal" : 175 }
{ "_id" : 3, "quizTotal" : 14, "labTotal" : 11, "examTotal" : 148 }
```

### Use in `$setWindowFields` Stage

**New in version:** 5.0

Create a `cakeSales` collection that contains cake sales in the states
of California (`CA`) and Washington (`WA`):

```javascript
db.cakeSales.insertMany( [
   { _id: 0, type: "chocolate", orderDate: new Date("2020-05-18T14:10:30Z"),
     state: "CA", price: 13, quantity: 120 },
   { _id: 1, type: "chocolate", orderDate: new Date("2021-03-20T11:30:05Z"),
     state: "WA", price: 14, quantity: 140 },
   { _id: 2, type: "vanilla", orderDate: new Date("2021-01-11T06:31:15Z"),
     state: "CA", price: 12, quantity: 145 },
   { _id: 3, type: "vanilla", orderDate: new Date("2020-02-08T13:13:23Z"),
     state: "WA", price: 13, quantity: 104 },
   { _id: 4, type: "strawberry", orderDate: new Date("2019-05-18T16:09:01Z"),
     state: "CA", price: 41, quantity: 162 },
   { _id: 5, type: "strawberry", orderDate: new Date("2019-01-08T06:12:03Z"),
     state: "WA", price: 43, quantity: 134 }
] )
```

This example uses `$sum` in the `$setWindowFields`
stage to output the sum of the `quantity` of cakes sold in each
`state`:

```javascript
db.cakeSales.aggregate( [
   {
      $setWindowFields: {
         partitionBy: "$state",
         sortBy: { orderDate: 1 },
         output: {
            sumQuantityForState: {
               $sum: "$quantity",
               window: {
                  documents: [ "unbounded", "current" ]
               }         
            }
         }
      }
   }
] )
```

In the example:

- `partitionBy: "$state"` partitions the documents in the collection by
  `state`. There are partitions for `CA` and `WA`.

- `sortBy: { orderDate: 1 }` sorts the documents in each partition by
  `orderDate` in ascending order (`1`), so the earliest
  `orderDate` is first.

- `output` sets the `sumQuantityForState` field to the sum of the
  `quantity` values using `$sum` that is run in a
  documents window.
  
  The window contains documents between
  an `unbounded` lower limit and the `current` document in the
  output. This means `$sum` returns the sum of the `quantity`
  values for the documents between the beginning of the partition and
  the current document.

In this output, the sum of the `quantity` values for `CA` and `WA`
is shown in the `sumQuantityForState` field:

```javascript
{ "_id" : 4, "type" : "strawberry", "orderDate" : ISODate("2019-05-18T16:09:01Z"),
  "state" : "CA", "price" : 41, "quantity" : 162, "sumQuantityForState" : 162 }
{ "_id" : 0, "type" : "chocolate", "orderDate" : ISODate("2020-05-18T14:10:30Z"),
  "state" : "CA", "price" : 13, "quantity" : 120, "sumQuantityForState" : 282 }
{ "_id" : 2, "type" : "vanilla", "orderDate" : ISODate("2021-01-11T06:31:15Z"),
  "state" : "CA", "price" : 12, "quantity" : 145, "sumQuantityForState" : 427 }
{ "_id" : 5, "type" : "strawberry", "orderDate" : ISODate("2019-01-08T06:12:03Z"),
  "state" : "WA", "price" : 43, "quantity" : 134, "sumQuantityForState" : 134 }
{ "_id" : 3, "type" : "vanilla", "orderDate" : ISODate("2020-02-08T13:13:23Z"),
  "state" : "WA", "price" : 13, "quantity" : 104, "sumQuantityForState" : 238 }
{ "_id" : 1, "type" : "chocolate", "orderDate" : ISODate("2021-03-20T11:30:05Z"),
  "state" : "WA", "price" : 14, "quantity" : 140, "sumQuantityForState" : 378 }
```
