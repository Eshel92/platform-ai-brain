<!-- Converted from reference/operator/aggregation/add.txt (reStructuredText). Includes are inlined. -->

# $add (expression operator)

## Definition

**`$add`**

Adds numbers together or adds numbers and a date. If one of the
arguments is a date, `$add` treats the other arguments
as milliseconds to add to the date.

The `$add` expression has the following syntax:

```javascript
{ $add: [ <expression1>, <expression2>, ... ] }
```

The arguments can be any valid expression as long as they resolve to
either all numbers or to numbers and a date. For more information on
expressions, see aggregation-expressions.

Starting in MongoDB 6.1 you can optimize the `$add` operation. To
improve performance, group references at the end of the argument
list. For example,

```javascript
$add: [ 1, 2, 3, '$a', '$b', '$c' ]
```

## Behavior

When input types are mixed, `$add` promotes the smaller input 
type to the larger of the two. A type is considered larger when it 
represents a wider range of values. The order of numeric types from 
smallest to largest is: integer → long → double → decimal

The larger of the input types also determines the result type unless 
the operation overflows and is beyond the range represented by that 
larger data type. In cases of overflow, `$add` promotes the 
result according to the following order:

- If the larger input type is `integer`, the result type 
  is promoted to `long`.

- If the larger input type is `long`, the result type is 
  promoted to `double`.

- If the larger type is `double` or 
  `decimal`, the overflow result is represented 
  as + or - infinity. There is no type promotion of the result.

When mixing document-bson-type-date and non-integer operands, the `$add` 
operator evaluates the array of expressions from left to right and rounds 
numeric values before adding them to the `Date` value. For more information, see
add-operation-left-associative.

## Examples

The following examples use a `sales` collection with the following
documents:

```javascript
db.sales.insertMany( [
   { _id : 1, "item" : "abc", "price" : 10, "fee" : 2, date: ISODate("2014-03-01T08:00:00Z") },
   { _id : 2, "item" : "jkl", "price" : 20, "fee" : 1, date: ISODate("2014-03-01T09:00:00Z") },
   { _id : 3, "item" : "xyz", "price" : 5,  "fee" : 0, date: ISODate("2014-03-15T09:00:00Z") }
] )
```

### Add Numbers

The following aggregation uses the `$add` expression in the
`$project` pipeline to calculate the total cost:

```javascript
db.sales.aggregate(
   [
     { $project: { item: 1, total: { $add: [ "$price", "$fee" ] } } }
   ]
)
```

The operation returns the following results:

```javascript
{ "_id" : 1, "item" : "abc", "total" : 12 }
{ "_id" : 2, "item" : "jkl", "total" : 21 }
{ "_id" : 3, "item" : "xyz", "total" : 5 }
```

### Perform Addition on a Date

The following aggregation uses the `$add` expression to
compute the `billing_date` by adding `3*24*60*60000` milliseconds
(i.e. 3 days) to the `date` field :

```javascript
db.sales.aggregate(
   [
     { $project: { item: 1, billing_date: { $add: [ "$date", 3*24*60*60000 ] } } }
   ]
)
```

The operation returns the following results:

```javascript
{ "_id" : 1, "item" : "abc", "billing_date" : ISODate("2014-03-04T08:00:00Z") }
{ "_id" : 2, "item" : "jkl", "billing_date" : ISODate("2014-03-04T09:00:00Z") }
{ "_id" : 3, "item" : "xyz", "billing_date" : ISODate("2014-03-18T09:00:00Z") }
```

### Add Non-Integer Values to a Date

The following aggregation uses the `$add` expression to compute the `result` 
field by adding numeric values to the `date` field:

```javascript
db.sales.aggregate(
   [
      { $project: { item: 1, result: { $add: [ 1.5, 1.6, "$date", 1.5, 1.5 ] } } }
   ]
)
```

Output:

```
{ "_id" : 1, "item" : 'abc', "result" : ISODate("2014-03-01T08:00:00.007Z") }
{ "_id" : 2, "item" : 'jkl', "result" : ISODate("2014-03-01T09:00:00.007Z") }
{ "_id" : 3, "item" : 'xyz', "result" : ISODate("2014-03-15T09:00:00.007Z") }
```

Note that, although the sum of non-date expressions is `6.1` milliseconds,
the aggregation results in the initial `$date` field plus `7` milliseconds due 
to the `$add` operation's left associativity.

When `$add` evaluates the array of expressions from left to right, it first adds
the two numeric values `1.5` and `1.6`. The resulting `3.1` is rounded to `3` 
before being added to the `$date` field. Next, it is added to the rounded 
value of `1.5` (which is `2`), and then to the rounded value of the final `1.5` 
(which is also `2`).
