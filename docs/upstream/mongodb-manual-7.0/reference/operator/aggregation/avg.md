<!-- Converted from reference/operator/aggregation/avg.txt (reStructuredText). Includes are inlined. -->

# $avg (accumulator operator)

## Definition

**`$avg`**

Returns the average of numeric values across a group of documents.

The `$avg` accumulator is available in these stages:

- `$bucket`

- `$bucketAuto`

- `$group`

**Note:** Disambiguation

This page describes `$avg` when used as an **accumulator**.
Accumulators return a single aggregated value like sum, maximum, or
minimum across a group of input documents.

You can also use `$avg` in these other contexts:

- `$avg (expression)`, which returns the average
  of numeric elements in an array.  

- `$avg (window function)`, which is used in the
  `$setWindowFields` stage to return the average of values
  from documents in a particular window.

## Syntax

```none
{ $avg: <expression> }
```

## Behavior

### Result Type

The default return type is a double. If at least one input value is a
decimal, then the return type is a decimal.

### Non-numeric or Missing Values

`$avg` ignores non-numeric values, including missing values. If all
input values are non-numeric, `$avg` returns `null`.

### Array Operand

If the operand resolves to an array, `$avg` treats the operand as a
non-numerical value.

## Example

Create a `sales` collection with the following documents:

```javascript
db.sales.insertMany( [
   { _id: 1, item: "abc", price: 10, quantity: 2, date: ISODate("2014-01-01T08:00:00Z") },
   { _id: 2, item: "jkl", price: 20, quantity: 1, date: ISODate("2014-02-03T09:00:00Z") },
   { _id: 3, item: "xyz", price: 5, quantity: 5, date: ISODate("2014-02-03T09:05:00Z") },
   { _id: 4, item: "abc", price: 10, quantity: 10, date: ISODate("2014-02-15T08:00:00Z") },
   { _id: 5, item: "xyz", price: 5, quantity: 10, date: ISODate("2014-02-15T09:12:00Z") }
] )
```

The following operation:

1. Groups the documents by the `item` field.

#. Uses the `$avg` accumulator to compute the average amount and
   average quantity for each group.

```javascript
db.sales.aggregate(
   [
     {
       $group:
         {
           _id: "$item",
           avgAmount: { $avg: { $multiply: [ "$price", "$quantity" ] } },
           avgQuantity: { $avg: "$quantity" }
         }
     }
   ]
)
```

Output:

```javascript
[
   { _id: 'xyz', avgAmount: 37.5, avgQuantity: 7.5 },
   { _id: 'abc', avgAmount: 60, avgQuantity: 6 },
   { _id: 'jkl', avgAmount: 20, avgQuantity: 1 }
]
```
