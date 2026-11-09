<!-- Converted from reference/expression/median.txt (reStructuredText). Includes are inlined. -->

# $median (expression)

## Definition

**`$median`**

**New in version:** 7.0

Returns the median (50th percentile) of an array of numeric values.

**Note:** Disambiguation

This page describes `$median` when used as an **expression**,
which calculates the median of an array of values.

You can also use `$median` in these other contexts:

- `$median (accumulator)`, used in grouping to
  return the median value across a group of input documents.
- `$median (window function)`, used in the
  `$setWindowFields` stage to return the median value from
  documents in a window.

## Syntax

```javascript
{
   $median: {
      input: <expression>,
      method: <string>
   }
}
```

### Command Fields

* - Field
  - Type
  - Necessity
  - Description

* - `input`
  - Array
  - Required
  - Can be either:

    - An expression that resolves to an array. For example, `$grades`, where
      the document field `$grades` contains an array of numeric values.
    - An array of expressions, each of which evaluates to a numeric
      value. For example, `[ "$field1", "$field2", "$field3" ]`.

    `$median` calculates the median across all values in
    the array. Non-numeric values are ignored.

* - `method`
  - String
  - Required
  - The method that MongoDB uses to calculate the median value.
    The method must be `'approximate'`.

## Behavior

When `$median` is used as an expression, it always uses an accurate
percentile calculation algorithm rather than an approximate one, even
when `method: "approximate"` is specified.

This is because expressions operate over arrays of bounded size where
it is acceptable to keep all of the input values in memory.

## Example

The following example uses a `testScores` collection to demonstrate
the array input form of `$median`.

Create the `testScores` collection:

```javascript
db.testScores.insertMany( [
   { studentId: "2345", scores: [ 62, 81, 80, 75, 68 ] },
   { studentId: "2356", scores: [ 60, 83, 79, 72, 65 ] },
   { studentId: "2358", scores: [ 67, 82, 78, 70, 84 ] },
   { studentId: "2367", scores: [ 64, 72, 77, 58, 91 ] },
   { studentId: "2369", scores: [ 60, 53, 72, 85, 63 ] }
] )
```

The following pipeline uses `$median` to calculate the median test
score for each student:

```javascript
```

Output:

```javascript
```

In the preceding pipeline:

- `$project` with `$median` finds the median value in the
  `scores` array for each document and returns it as `testMedians`.
- Each result reflects the median score across that student's
  recorded test scores.

## Learn More

- `$median (accumulator)`
- `$median (window function)`
- `$percentile`
