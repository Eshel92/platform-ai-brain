<!-- Converted from reference/expression/stdDevPop.txt (reStructuredText). Includes are inlined. -->

# $stdDevPop (expression)

## Definition

**`$stdDevPop`**

Returns the population standard deviation of numeric values in an
array.

**Note:** Disambiguation

This page describes `$stdDevPop` when used as an **expression**.

You can also use `$stdDevPop` in these other contexts:

- `$stdDevPop (accumulator)`, which returns the
  population standard deviation of values across a group of
  documents.

- `$stdDevPop (window function)`, which is
  used in the `$setWindowFields` stage to calculate the
  population standard deviation of values from documents in a
  particular window.

## Syntax

When used as an expression, `$stdDevPop` has one of the following
two syntaxes:

```javascript
{ $stdDevPop: <expression> }
```

In the preceding syntax, the operand is a single expression that
evaluates to an array. `$stdDevPop` traverses the array and returns
the population standard deviation of the array's numeric values.

```javascript
{ $stdDevPop: [ <expression1>, <expression2>, ... ] }
```

In the preceding syntax, each expression should evaluate to a single
numeric value. `$stdDevPop` returns the population standard deviation
of those values. Non-numeric values are ignored.

## Behavior

### Result Type

`$stdDevPop` returns the population standard deviation of the
input values as a `double`.

### Non-numeric or Missing Values

`$stdDevPop` ignores non-numeric values, including missing values.
If all input values are non-numeric, `$stdDevPop` returns `null`.

### Single Value

If the input consists of a single numeric value, `$stdDevPop`
returns `0`.

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

The following pipeline uses `$stdDevPop` to calculate the
population standard deviation of each student's test scores:

```javascript
```

Output:

```javascript
```

In the preceding pipeline, `$project` with `$stdDevPop`
computes the population standard deviation of each student's
`scores` array and returns it as `scoreStdDev`.
