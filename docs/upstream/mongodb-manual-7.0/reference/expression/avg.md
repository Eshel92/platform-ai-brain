<!-- Converted from reference/expression/avg.txt (reStructuredText). Includes are inlined. -->

# $avg (expression)

## Definition

**`$avg`**

Returns the average of numeric array elements.

**Note:** Disambiguation

This page describes `$avg` when used as an **expression**, which
returns the average of numeric elements in an array.

You can also use `$avg` in these other contexts:

- `$avg (accumulator)`, which returns a single
  aggregated value based on a variable number of input documents.

- `$avg (window function)`, which is used in the
  `$setWindowFields` stage to return the average of values
  from documents in a particular window.

## Syntax

When used as an expression, `$avg` has one of these syntaxes:

```none
{ $avg: <expression> }
```

In this syntax, the operand is a single expression that resolves to an
array. `$avg` traverses the array and returns the average of the
array's numeric values. For example, `{ $avg: "$testScores" }` returns
the average of numeric values in the `testScores` array field.

```none
{ $avg: [ <expression1>, <expression2> ... ]  }
```

In this syntax, each expression in the input array is a single numeric
value. `$avg` returns the average of the individual input values. If
any of the input expressions resolve to an array, `$avg` does **not**
traverse the array and instead treats the array as a non-numeric value.

## Behavior

### Result Type

The default return type is a double. If at least one input value is a
decimal, then the return type is a decimal.

### Non-numeric or Missing Values

`$avg` ignores non-numeric values, including missing values. If all
input values are non-numeric, `$avg` returns `null`.

## Example

Create a `students` collection with the following documents:

```javascript
db.students.insertMany( [
   { _id: 1, quizzes: [ 10, 6, 7 ], labs: [ 5, 8 ], final: 80, midterm: 75 },
   { _id: 2, quizzes: [ 9, 10 ], labs: [ 8, 8 ], final: 95, midterm: 80 },
   { _id: 3, quizzes: [ 4, 5, 5 ], labs: [ 6, 5 ], final: 78, midterm: 70 }
] )
```

The following operation uses `$avg` in the `$project` stage
to calculate averages for the following fields:

- `quizzes`
- `labs`
- Combined average of `final` and `midterm`

```javascript
db.students.aggregate( [
   {
      $project: {
         quizAvg: { $avg: "$quizzes"},
         labAvg: { $avg: "$labs" },
         examAvg: { $avg: [ "$final", "$midterm" ] }
      }
   }
] )
```

Output

```javascript
[
   { _id: 1, quizAvg: 7.666666666666667, labAvg: 6.5, examAvg: 77.5 },
   { _id: 2, quizAvg: 9.5, labAvg: 8, examAvg: 87.5 },
   { _id: 3, quizAvg: 4.666666666666667, labAvg: 5.5, examAvg: 74 }
]
```
