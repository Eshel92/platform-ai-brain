<!-- Converted from reference/operator/aggregation/and.txt (reStructuredText). Includes are inlined. -->

# $and (aggregation)

## Definition

**`$and`**

Evaluates one or more expressions and returns `true` if *all* of
the expressions are `true` or if run with no argument
expressions. Otherwise, `$and` returns `false`.

`$and` syntax:

```javascript
{ $and: [ <expression1>, <expression2>, ... ] }
```

For more information on expressions, see
aggregation-expressions.

## Behavior

In addition to the `false` boolean value, `$and` evaluates
as `false` the following: `null`, `0`, and `undefined`
values. The `$and` evaluates all other values as `true`,
including non-zero numeric values and arrays.

| Example | Result |
|---|---|
| `{ $and: [ 1, "green" ] }` | `true` |
| `{ $and: [ ] }` | `true` |
| `{ $and: [ [ null ], [ false ], [ 0 ] ] }` | `true` |
| `{ $and: [ null, true ] }` | `false` |
| `{ $and: [ 0, true ] }` | `false` |

## Error Handling

To allow the query engine to optimize queries, `$and` handles
errors as follows:

- If any expression supplied to `$and` would cause an error when
  evaluated alone, the `$and` containing the expression may cause an
  error but an error is not guaranteed.

- An expression supplied after the first expression supplied to `$and`
  may cause an error even if the first expression evaluates to
  `false`.

For example, the following query *always* produces an error if `$x` is
`0`:

```javascript
db.example.find( {
   $expr: { $eq: [ { $divide: [ 1, "$x" ] }, 3 ] }
} )
```

The following query, which contains multiple expressions supplied to
`$and`, *may* produce an error if there is any document where `$x`
is `0`:

```javascript
db.example.find( {
   $and: [
      { x: { $ne: 0 } },
      { $expr: { $eq: [ { $divide: [ 1, "$x" ] }, 3 ] } }
   ]
} )
```

## Example

Create an example `inventory` collection with these documents:

```javascript
db.inventory.insertMany([
   { "_id" : 1, "item" : "abc1", description: "product 1", qty: 300 },
   { "_id" : 2, "item" : "abc2", description: "product 2", qty: 200 },
   { "_id" : 3, "item" : "xyz1", description: "product 3", qty: 250 },
   { "_id" : 4, "item" : "VWZ1", description: "product 4", qty: 300 },
   { "_id" : 5, "item" : "VWZ2", description: "product 5", qty: 180 }
])
```

This operation uses the `$and` operator to
determine if `qty` is greater than 100 *and* less than `250`:

```javascript
db.inventory.aggregate(
   [
     {
       $project:
          {
            item: 1,
            qty: 1,
            result: { $and: [ { $gt: [ "$qty", 100 ] }, { $lt: [ "$qty", 250 ] } ] }
          }
     }
   ]
)
```

The operation returns these results:

```javascript
{ "_id" : 1, "item" : "abc1", "qty" : 300, "result" : false }
{ "_id" : 2, "item" : "abc2", "qty" : 200, "result" : true }
{ "_id" : 3, "item" : "xyz1", "qty" : 250, "result" : false }
{ "_id" : 4, "item" : "VWZ1", "qty" : 300, "result" : false }
{ "_id" : 5, "item" : "VWZ2", "qty" : 180, "result" : true }
```
