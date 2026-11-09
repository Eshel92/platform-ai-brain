<!-- Converted from reference/operator/aggregation/in.txt (reStructuredText). Includes are inlined. -->

# $in (aggregation)

## Definition

**`$in`**

Returns a boolean indicating whether a specified value is in an
array.

**Note:**

This document describes the `$in` aggregation
operator. For the `$in` query operator, see
/reference/operator/query/in.

`$in` has the following operator expression syntax:

```javascript
{ $in: [ <expression>, <array expression> ] }
```

| Operand | Description |
|---|---|
| `<expression>` | Any valid expression expression. |
| `<array expression>` | Any valid expression that resolves to an array. |

Unlike the `$in` query operator, the aggregation
`$in` operator does not support matching by
regular expressions.

| Example | Results |
|---|---|
| `{ $in: [ 2, [ 1, 2, 3 ] ] }` | `true` |
| `{ $in: [ "abc", [ "xyz", "abc" ] ] }` | `true` |
| `{ $in: [ "xy", [ "xyz", "abc" ] ] }` | `false` |
| `{ $in: [ [ "a" ], [ "a" ] ] }` | `false` |
| `{ $in: [ [ "a" ], [ [ "a" ] ] ] }` | `true` |
| `{ $in: [ /^a/, [ "a" ] ] }` | `false` |
| `{ $in: [ /^a/, [ /^a/ ] ] }` | `true` |

## Behavior

`$in` fails with an error in either of the
following cases: if the $in expression is not given exactly two
arguments, or if the second argument does not resolve to an array.

## Example

A collection named `fruit` has the following documents:

```javascript
{ "_id" : 1, "location" : "24th Street",
  "in_stock" : [ "apples", "oranges", "bananas" ] }
{ "_id" : 2, "location" : "36th Street",
  "in_stock" : [ "bananas", "pears", "grapes" ] }
{ "_id" : 3, "location" : "82nd Street",
  "in_stock" : [ "cantaloupes", "watermelons", "apples" ] }
```

The following aggregation operation looks at the `in_stock` array in
each document and determines whether the string `bananas` is present.

```javascript
db.fruit.aggregate([
  {
    $project: {
      "store location" : "$location",
      "has bananas" : {
        $in: [ "bananas", "$in_stock" ]
      }
    }
  }
])
```

The operation returns the following results:

```javascript
{ "_id" : 1, "store location" : "24th Street", "has bananas" : true }
{ "_id" : 2, "store location" : "36th Street", "has bananas" : true }
{ "_id" : 3, "store location" : "82nd Street", "has bananas" : false }
```
