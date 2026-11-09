<!-- Converted from reference/operator/aggregation/ne.txt (reStructuredText). Includes are inlined. -->

# $ne (expression operator)

## Definition

**`$ne`**

Compares two values and returns:

- `true` when the values are not equivalent.

- `false` when the values are equivalent.

If a field is missing from a document, `$ne` treats the
missing field as a distinct value, separate from `null`.
`$ne` considers two missing fields equivalent to each
other, and considers a missing field different from a `null`
value.

The `$ne` compares both value and type, using the
specified BSON comparison order
for values of different types.

`$ne` has the following syntax:

```javascript
{ $ne: [ <expression1>, <expression2> ] }
```

For more information on expressions, see aggregation-expressions.

## Example

Consider an `inventory` collection with the following documents:

```javascript
db.inventory.insertMany( [ 
   { _id: 1, item: "abc1", description: "product 1", qty: 300 }
   { _id: 2, item: "abc2", description: "product 2", qty: 200 }
   { _id: 3, item: "xyz1", description: "product 3", qty: 250 }
   { _id: 4, item: "VWZ1", description: "product 4", qty: 300 }
   { _id: 5, item: "VWZ2", description: "product 5", qty: 180 }
] )
```

The following operation uses the `$ne` operator to
determine if `qty` does not equal `250`:

```javascript
db.inventory.aggregate(
   [
     {
       $project:
          {
            item: 1,
            qty: 1,
            qtyNe250: { $ne: [ "$qty", 250 ] },
            _id: 0
          }
     }
   ]
)
```

The operation returns the following results:

```javascript
{ item: "abc1", qty: 300, qtyNe250: true }
{ item: "abc2", qty: 200, qtyNe250: true }
{ item: "xyz1", qty: 250, qtyNe250: false }
{ item: "VWZ1", qty: 300, qtyNe250: true }
{ item: "VWZ2", qty: 180, qtyNe250: true }
```
