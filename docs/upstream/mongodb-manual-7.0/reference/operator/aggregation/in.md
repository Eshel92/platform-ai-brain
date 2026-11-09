<!-- Converted from reference/operator/aggregation/in.txt (reStructuredText). Includes are inlined. -->

# $in (expression operator)

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

The following example uses the `movies` collection from the sample_mflix
sample dataset.  For details on how to load this dataset into
your deployment, see Load the sample dataset.

This aggregation operation looks at the `genres` array in
each movie and determines whether the string `"Drama"` is present:

```javascript
```

Output:

```javascript
```
