<!-- Converted from reference/expression/stdDevSamp.txt (reStructuredText). Includes are inlined. -->

# $stdDevSamp (expression)

## Definition

**`$stdDevSamp`**

Returns the sample standard deviation of numeric values in an array.

**Note:** Disambiguation

This page describes `$stdDevSamp` when used as an
**expression**, which returns the sample standard deviation of
numeric values in an array.

You can also use `$stdDevSamp` in these other contexts:

- `$stdDevSamp (accumulator)`, which calculates
  the sample standard deviation of values across a group of
  documents.

- `$stdDevSamp (window function)`, which
  is used in the `$setWindowFields` stage to calculate
  the sample standard deviation of values in a window.

## Syntax

When used as an expression, `$stdDevSamp` has one of these syntaxes:

```javascript
{ $stdDevSamp: <expression> }
```

In the preceding syntax, the operand is a single expression that
evaluates to an array. `$stdDevSamp` traverses the array and
returns the sample standard deviation of the array's numeric values.

```javascript
{ $stdDevSamp: [ <expression1>, <expression2>, ... ] }
```

In the preceding syntax, each expression should evaluate to a single
numeric value. `$stdDevSamp` returns the sample standard deviation of
those values. Non-numeric values are ignored.

## Behavior

### Result Type

`$stdDevSamp` returns the sample standard deviation of the input
values as a `double`.

### Non-Numeric Values

`$stdDevSamp` ignores non-numeric values, null values, and missing
fields. If all input values are non-numeric or missing, `$stdDevSamp`
returns `null`.

### Single Value

If there is only one numeric input value, `$stdDevSamp` returns
`null`.

## Example

Create a `testScores` collection:

```javascript
db.testScores.insertMany( [
   { studentId: "2345", scores: [ 62, 81, 80, 75, 68, 72, 74, 78, 69, 77 ] },
   { studentId: "2356", scores: [ 60, 83, 79, 72, 65, 71, 68, 74, 64, 76 ] },
   { studentId: "2358", scores: [ 67, 82, 78, 70, 84, 73, 79, 71, 88, 75 ] },
   { studentId: "2367", scores: [ 64, 72, 77, 58, 91, 66, 83, 55, 94, 61 ] },
   { studentId: "2369", scores: [ 60, 53, 72, 85, 63, 88, 57, 79, 66, 74 ] }
] )
```

The following pipeline uses `$stdDevSamp` to calculate the
sample standard deviation of each student's test scores:

```javascript
```

Output:

```javascript
```

In the preceding pipeline, `$project` with `$stdDevSamp`
computes the sample standard deviation of each student's
`scores` array and returns it as `scoreStdDev`.

## Learn More

- aggregation-expressions
- `$stdDevPop`
- read-operations-arrays
