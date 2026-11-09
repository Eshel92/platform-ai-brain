<!-- Converted from reference/operator/aggregation/cmp.txt (reStructuredText). Includes are inlined. -->

# $cmp (aggregation)

## Definition

**`$cmp`**

Compares two values and returns:

- `-1` if the first value is less than the second.

- `1` if the first value is greater than the second.

- `0` if the two values are equivalent.

The `$cmp` compares both value and type, using the
specified BSON comparison order
for values of different types.

`$cmp` has this syntax:

```javascript
{ $cmp: [ <expression1>, <expression2> ] }
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

Use the `$cmp` operator to compare the `qty` value with `250`:

```javascript
db.inventory.aggregate(
   [
     {
       $project:
          {
            item: 1,
            qty: 1,
            cmpTo250: { $cmp: [ "$qty", 250 ] },
            _id: 0
          }
     }
   ]
)
```

Output:

```javascript
{ item : "abc1", qty : 300, cmpTo250 : 1 }
{ item : "abc2", qty : 200, cmpTo250 : -1 }
{ item : "xyz1", qty : 250, cmpTo250 : 0 }
{ item : "VWZ1", qty : 300, cmpTo250 : 1 }
{ item : "VWZ2", qty : 180, cmpTo250 : -1 }
```
