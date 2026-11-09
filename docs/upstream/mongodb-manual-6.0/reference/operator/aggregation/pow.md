<!-- Converted from reference/operator/aggregation/pow.txt (reStructuredText). Includes are inlined. -->

# $pow (aggregation)

## Definition

**`$pow`**

Raises a number to the specified exponent and returns the result.
`$pow` has the following syntax:

```javascript
{ $pow: [ <number>, <exponent> ] }
```

The `<number>` expression can be any valid expression as long as it resolves to a number.

The `<exponent>` expression can be any valid expression as long as it resolves to a number.

You cannot raise `0` to a negative exponent.

## Behavior

The result will have the same type as the input except when it
cannot be represented accurately in that type. In these cases:

- A 32-bit integer will be converted to a 64-bit integer if the
  result is representable as a 64-bit integer.

- A 32-bit integer will be converted to a double if the result is
  not representable as a 64-bit integer.

- A 64-bit integer will be converted to double if the result is not
  representable as a 64-bit integer.

If either argument resolves to a value of `null` or refers to a field that is
missing, `$pow` returns `null`. If either argument resolves to
`NaN`, `$pow` returns `NaN`.

| Example | Results |
|---|---|
| `{ $pow: [ 5, 0 ] }` | `1` |
| `{ $pow: [ 5, 2 ] }` | `25` |
| `{ $pow: [ 5, -2 ] }` | `0.04` |
| `{ $pow: [ -5, 0.5 ] }` | `NaN` |

## Example

Create a collection called `quizzes` with the following documents:

```javascript
db.quizzes.insertMany( [
   { 
      _id : 1, 
      scores : [
         { name : "dave123", score : 85 },
         { name : "dave2", score : 90 },
         { name : "ahn", score : 71 }
      ]
   },
   {
      _id : 2,
      scores : [
         { name : "li", quiz : 2, score : 96 },
         { name : "annT", score : 77 },
         { name : "ty", score : 82 }
      ]
   }
] )
```

The following example calculates the variance for each quiz:

```javascript
db.quizzes.aggregate( [
   { $project: { variance: { $pow: [ { $stdDevPop: "$scores.score" }, 2 ] } } }
] )
```

The operation returns the following results:

```javascript
{ _id : 1, variance : 64.66666666666667 }
{ _id : 2, variance : 64.66666666666667 }
```
