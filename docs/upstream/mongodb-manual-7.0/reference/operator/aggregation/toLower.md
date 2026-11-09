<!-- Converted from reference/operator/aggregation/toLower.txt (reStructuredText). Includes are inlined. -->

# $toLower  (expression operator)

## Definition

**`$toLower`**

Converts a string to lowercase, returning the result.

`$toLower` has the following syntax:

```javascript
{ $toLower: <expression> }
```

The argument can be any expression
as long as it resolves to a string. For more information on
expressions, see aggregation-expressions.

If the argument resolves to null, `$toLower` returns an
empty string `""`.

## Behavior

`$toLower` only has a well-defined behavior for strings of ASCII characters.

## Example

Consider a `inventory` collection with the following documents:

```javascript
db.inventory.insertMany( [
   { _id: 1, item: "ABC1", quarter: "13Q1", description: "PRODUCT 1" },
   { _id: 2, item: "abc2", quarter: "13Q4", description: "Product 2" },
   { _id: 3, item: "xyz1", quarter: "14Q2", description: null }
] )
```

The following operation uses the `$toLower` operator return
lowercase `item` and lowercase `description` value:

```javascript
db.inventory.aggregate(
   [
     {
       $project:
         {
           item: { $toLower: "$item" },
           description: { $toLower: "$description" }
         }
     }
   ]
)
```

The operation returns the following results:

```javascript
{ _id: 1, item: "abc1", description: "product 1" }
{ _id: 2, item: "abc2", description: "product 2" }
{ _id: 3, item: "xyz1", description: "" }
```
