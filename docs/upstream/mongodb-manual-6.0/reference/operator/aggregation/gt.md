<!-- Converted from reference/operator/aggregation/gt.txt (reStructuredText). Includes are inlined. -->

# $gt (aggregation)

## Definition

**`$gt`**

Compares two values and returns:

- `true` when the first value is *greater than* the second value.

- `false` when the first value is *less than or equal to* the
  second value.

The `$gt` compares both value and type, using the
specified BSON comparison order
for values of different types.

`$gt` has the following syntax:

```javascript
{ $gt: [ <expression1>, <expression2> ] }
```

For more information on expressions, see aggregation-expressions.

## Example

Create an `inventory` collection with these documents:

```javascript
db.inventory.insertMany( [
   { _id : 1, item : "abc1", description: "product 1", qty: 300 },
   { _id : 2, item : "abc2", description: "product 2", qty: 200 },
   { _id : 3, item : "xyz1", description: "product 3", qty: 250 },
   { _id : 4, item : "VWZ1", description: "product 4", qty: 300 },
   { _id : 5, item : "VWZ2", description: "product 5", qty: 180 }
] )
```

Use the `$gt` operator to determine if `qty` is greater than
`250`:

```javascript
db.inventory.aggregate(
   [
     {
       $project:
          {
            item: 1,
            qty: 1,
            qtyGt250: { $gt: [ "$qty", 250 ] },
            _id: 0
          }
     }
   ]
)
```

The operation returns the following results:

```javascript
{ item : "abc1", qty : 300, qtyGt250 : true }
{ item : "abc2", qty : 200, qtyGt250 : false }
{ item : "xyz1", qty : 250, qtyGt250 : false }
{ item : "VWZ1", qty : 300, qtyGt250 : true }
{ item : "VWZ2", qty : 180, qtyGt250 : false }
```
