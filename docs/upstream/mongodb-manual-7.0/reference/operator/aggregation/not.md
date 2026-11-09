<!-- Converted from reference/operator/aggregation/not.txt (reStructuredText). Includes are inlined. -->

# $not (expression operator)

## Definition

**`$not`**

Evaluates a boolean and returns the opposite boolean value; i.e.
when passed an expression that evaluates to `true`,
`$not` returns `false`; when passed an expression that
evaluates to `false`, `$not` returns `true`.

`$not` has the following syntax:

```javascript
{ $not: [ <expression> ] }
```

For more information on expressions, see
aggregation-expressions.

## Behavior

In addition to the `false` boolean value, `$not` evaluates
as `false` the following: `null`, `0`, and `undefined`
values. The `$not` evaluates all other values as `true`,
including non-zero numeric values and arrays.

| Example | Result |
|---|---|
| `{ $not: [ true ] }` | `false` |
| `{ $not: [ [ false ] ] }` | `false` |
| `{ $not: [ false ] }` | `true` |
| `{ $not: [ null ] }` | `true` |
| `{ $not: [ 0 ] }` | `true` |

## Example

Consider an `inventory` collection with the following documents:

```javascript
db.inventory.insertMany( [ 
   { _id: 1, item: "abc1", description: "product 1", qty: 300 },
   { _id: 2, item: "abc2", description: "product 2", qty: 200 },
   { _id: 3, item: "xyz1", description: "product 3", qty: 250 },
   { _id: 4, item: "VWZ1", description: "product 4", qty: 300 },
   { _id: 5, item: "VWZ2", description: "product 5", qty: 180 }
] )
```

The following operation uses the `$not` operator to
determine if `qty` is not greater than `250`:

```javascript
db.inventory.aggregate(
   [
     {
       $project:
          {
            item: 1,
            result: { $not: [ { $gt: [ "$qty", 250 ] } ] }
          }
     }
   ]
)
```

The operation returns the following results:

```javascript
{ _id: 1, item: "abc1", result: false }
{ _id: 2, item: "abc2", result: true }
{ _id: 3, item: "xyz1", result: true }
{ _id: 4, item: "VWZ1", result: false }
{ _id: 5, item: "VWZ2", result: true }
```
