<!-- Converted from reference/expression/percentile.txt (reStructuredText). Includes are inlined. -->

# $percentile (expression)

## Definition

**`$percentile`**

Returns one or more percentile values computed over an array of numbers.

**Note:** Disambiguation

This page describes `$percentile` when used as an **expression**,
which calculates percentile values over an array of input values.

You can also use `$percentile` in these other contexts:

- `$percentile (accumulator)`, which returns
  percentile values by aggregating across a group of input documents.

- `$percentile (window function)`, which is
  used in the `$setWindowFields` stage to return an array
  of percentile values for documents in a particular window.

## Syntax

```javascript
{
   $percentile: {
      input: <expression>,
      p: [ <expression1>, <expression2>, ... ],
      method: <string>
   }
}
```

### Options

* - Field
  - Type
  - Description

* - `input`
  - Array
  - Can be either:

    - An expression that resolves to an array. For example,
      `$scores`, where the document field `$scores` contains
      an array of numeric values.
    - An array of expressions, each of which evaluates to a
      numeric value. For example,
      `[ "$field1", "$field2", "$field3" ]`.

    `$percentile` calculates percentile values across all numeric
    values in the array. Non-numeric values are ignored.

* - `p`
  - Expression
  - .. include:: /includes/aggregation/percentile/opt-p.rst

* - `method`
  - String
  - .. include:: /includes/aggregation/percentile/opt-method.rst

## Behavior

When used as an expression, `$percentile` always uses an accurate
percentile calculation algorithm rather than an approximate one, even
when `method: 'approximate'` is specified. This is because
expressions operate over arrays of bounded size where it is
acceptable to keep all of the input values in memory.

## Example

Create a `testScores` collection:

```javascript
db.testScores.insertMany( [
   { studentId: "2345", scores: [ 62, 81, 80, 75, 68 ] },
   { studentId: "2356", scores: [ 60, 83, 79, 72, 65 ] },
   { studentId: "2358", scores: [ 67, 82, 78, 70, 84 ] },
   { studentId: "2367", scores: [ 64, 72, 77, 58, 91 ] },
   { studentId: "2369", scores: [ 60, 53, 72, 85, 63 ] }
] )
```

The following pipeline uses `$percentile` to calculate the 25th,
50th, and 75th percentile test scores for each student:

```javascript
```

Output:

```javascript
```

In the preceding pipeline, `$project` with `$percentile`
computes the 25th, 50th, and 75th percentile of each student's
`scores` array and returns them as `testPercentiles`.
