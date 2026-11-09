<!-- Converted from reference/operator/aggregation/toUpper.txt (reStructuredText). Includes are inlined. -->

# $toUpper (aggregation)

## Definition

**`$toUpper`**

Converts a string to uppercase, returning the result.

`$toUpper` has the following syntax:

```javascript
{ $toUpper: <expression> }
```

The argument can be any expression
as long as it resolves to a string. For more information on
expressions, see aggregation-expressions.

If the argument resolves to null, `$toUpper` returns an
empty string `""`.

## Behavior

`$toUpper` only has a well-defined behavior for strings of ASCII characters.

## Example

Consider a `inventory` collection with the following documents:

```javascript
db.inventory.insertMany( [
   { "_id" : 1, "item" : "ABC1", quarter: "13Q1", "description" : "PRODUCT 1" },
   { "_id" : 2, "item" : "abc2", quarter: "13Q4", "description" : "Product 2" },
   { "_id" : 3, "item" : "xyz1", quarter: "14Q2", "description" : null }
] )
```

The following operation uses the `$toUpper` operator return
uppercase `item` and uppercase `description` values:

```javascript
db.inventory.aggregate(
   [
     {
       $project:
         {
           item: { $toUpper: "$item" },
           description: { $toUpper: "$description" }
         }
     }
   ]
)
```

The operation returns the following results:

```javascript
{ "_id" : 1, "item" : "ABC1", "description" : "PRODUCT 1" }
{ "_id" : 2, "item" : "ABC2", "description" : "PRODUCT 2" }
{ "_id" : 3, "item" : "XYZ1", "description" : "" }
```
