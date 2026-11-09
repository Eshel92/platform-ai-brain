<!-- Converted from reference/operator/aggregation/setEquals.txt (reStructuredText). Includes are inlined. -->

# $setEquals  (expression operator)

## Definition

**`$setEquals`**

Compares two or more arrays and returns `true` if they have the
same distinct elements and `false` otherwise.

`$setEquals` has the following syntax:

```javascript
{ $setEquals: [ <expression1>, <expression2>, ... ] }
```

The arguments can be any valid expression as long as they each resolve to an array.
For more information on expressions, see
aggregation-expressions.

## Behavior

`$setEquals` performs set operation on arrays, treating arrays
as sets. If an array contains duplicate entries, `$setEquals`
ignores the duplicate entries. `$setEquals` ignores the order of
the elements.

`$setEquals` filters out duplicates in its result to output an
array that contain only unique entries. The order of the elements in
the output array is unspecified.

If a set contains a nested array element, `$setEquals` does *not* descend
into the nested array but evaluates the array at top-level.

| Example | Result |
|---|---|
| `{ $setEquals: [ [ "a", "b", "a" ], [ "b", "a" ] ] }` | `true` |
| `{ $setEquals: [ [ "a", "b" ], [ [ "a", "b" ] ] ] }` | `false` |

## Example

Consider a `bakeryOrders` collection with the following documents:

```javascript
db.bakeryOrders.insertMany( [
   { _id: 0, cakes: ["chocolate", "vanilla"], cupcakes: ["chocolate", "vanilla"] },
   { _id: 1, cakes: ["chocolate", "vanilla"], cupcakes: ["vanilla", "chocolate"] },
   { _id: 2, cakes: ["chocolate", "chocolate"], cupcakes: ["chocolate"] },
   { _id: 3, cakes: ["vanilla"], cupcakes: ["chocolate"] },
   { _id: 4, cakes: ["vanilla"], cupcakes: [] }
] )
```

The following operation uses the `$setEquals` operator to
determine if the `cakes` array and the `cupcakes` array in each order
contain the same flavors:

```javascript
db.bakeryOrders.aggregate(
   [
      { 
         $project: { 
            _id: 0, 
            cakes: 1, 
            cupcakes: 1, 
            sameFlavors: { $setEquals: [ "$cakes", "$cupcakes" ] } 
         } 
      }
   ] )
```

**Note:** $project

The `$project` stage specifies which fields are included
in the output documents. In this example, the `$project` 
stage:

- Excludes the `_id` field from the output.
- Includes the `cakes` and `cupcakes` fields in the output.
- Outputs the result of the `$setEquals` operator in a new field 
  called `sameFlavors`.

The operation returns the following results:

```javascript
{
 cakes: [ "chocolate", "vanilla" ],
 cupcakes: [ "chocolate", "vanilla" ],
 sameFlavors: true
},
{
 cakes: [ "chocolate", "vanilla" ],
 cupcakes: [ "vanilla", "chocolate" ],
 sameFlavors: true
},
{ 
 cakes: [ "chocolate", "chocolate" ],
 cupcakes: [ "chocolate" ],
 sameFlavors: true
},
{
 cakes: [ "vanilla" ],
 cupcakes: [ "chocolate" ],
 sameFlavors: false
},
{ 
   cakes: [ "vanilla" ], 
   cupcakes: [], 
   sameFlavors: false 
}
```
