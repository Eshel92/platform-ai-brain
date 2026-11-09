<!-- Converted from reference/operator/aggregation/multiply.txt (reStructuredText). Includes are inlined. -->

# $multiply (aggregation)

## Definition

**`$multiply`**

Multiplies numbers together and returns the result. Pass the
arguments to `$multiply` in an array.

The `$multiply` expression has the following syntax:

```javascript
{ $multiply: [ <expression1>, <expression2>, ... ] }
```

The arguments can be any valid expression as long as they resolve to numbers. For
more information on expressions, see aggregation-expressions.

## Example

Consider a `sales` collection with the following documents:

```javascript
{ "_id" : 1, "item" : "abc", "price" : 10, "quantity": 2, date: ISODate("2014-03-01T08:00:00Z") }
{ "_id" : 2, "item" : "jkl", "price" : 20, "quantity": 1, date: ISODate("2014-03-01T09:00:00Z") }
{ "_id" : 3, "item" : "xyz", "price" : 5, "quantity": 10, date: ISODate("2014-03-15T09:00:00Z") }
```

The following aggregation uses the `$multiply` expression
in the `$project` pipeline to multiply the `price` and the
`quantity` fields:

```javascript
db.sales.aggregate(
   [
     { $project: { date: 1, item: 1, total: { $multiply: [ "$price", "$quantity" ] } } }
   ]
)
```

The operation returns the following results:

```javascript
{ "_id" : 1, "item" : "abc", "date" : ISODate("2014-03-01T08:00:00Z"), "total" : 20 }
{ "_id" : 2, "item" : "jkl", "date" : ISODate("2014-03-01T09:00:00Z"), "total" : 20 }
{ "_id" : 3, "item" : "xyz", "date" : ISODate("2014-03-15T09:00:00Z"), "total" : 50 }
```
