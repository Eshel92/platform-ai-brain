<!-- Converted from reference/operator/aggregation/strcasecmp.txt (reStructuredText). Includes are inlined. -->

# $strcasecmp (expression operator)

## Definition

**`$strcasecmp`**

Performs case-insensitive comparison of two strings. Returns

- 1 if first string is "greater than" the second string.

- 0 if the two strings are equal.

- -1 if the first string is "less than" the second string.

`$strcasecmp` has the following syntax:

```javascript
{ $strcasecmp: [ <expression1>, <expression2> ] }
```

The arguments can be any valid expression as long as they resolve to strings. For
more information on expressions, see aggregation-expressions.

## Behavior

`$strcasecmp` only has a well-defined behavior for strings of ASCII characters.

For a case sensitive comparison, see `$cmp`.

## Example

Consider a `inventory` collection with the following documents:

```javascript
db.inventory.insertMany( [
   { _id: 1, item: "ABC1", quarter: "13Q1", description: "product 1" },
   { _id: 2, item: "ABC2", quarter: "13Q4", description: "product 2" },
   { _id: 3, item: "XYZ1", quarter: "14Q2", description: null } 
] )
```

The following operation uses the `$strcasecmp` operator to
perform case-insensitive comparison of the `quarter` field value to
the string `"13q4"`:

```javascript
db.inventory.aggregate(
   [
     {
       $project:
          {
            item: 1,
            comparisonResult: { $strcasecmp: [ "$quarter", "13q4" ] }
          }
      }
   ]
)
```

The operation returns the following results:

```javascript
{ _id: 1, item: "ABC1", comparisonResult: -1 }
{ _id: 2, item: "ABC2", comparisonResult: 0 }
{ _id: 3, item: "XYZ1", comparisonResult: 1 }
```
