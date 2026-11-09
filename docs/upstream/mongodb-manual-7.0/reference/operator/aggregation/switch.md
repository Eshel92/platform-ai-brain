<!-- Converted from reference/operator/aggregation/switch.txt (reStructuredText). Includes are inlined. -->

# $switch (aggregation expression operator)

## Definition

**`$switch`**

Evaluates a series of case expressions. When it finds an expression
which evaluates to `true`, `$switch` executes a specified
expression and breaks out of the control flow.

`$switch` has the following syntax:

```javascript
$switch: {
   branches: [
      { case: <expression>, then: <expression> },
      { case: <expression>, then: <expression> },
      ...
   ],
   default: <expression>
}
```

The objects in the `branches` array must contain only a `case`
field and a `then` field.

* - Operand
  - Description

* - `branches`

  - An array of control branch documents. Each branch is a
    document with the following fields:

    - `case`
         Can be any valid expression that resolves to a
         `boolean`. If the result is not a `boolean`, it is
         coerced to a boolean value. More information about how
         MongoDB evaluates expressions as either true or false
         can be found here.

    - `then`
         Can be any valid expression.

    The `branches` array must contain at least one branch
    document.

* - `default`

  - Optional. The path to take if no branch `case` expression
    evaluates to `true`.

    Although optional, if `default` is unspecified and no
    branch `case` evaluates to true, `$switch`
    returns an error.

## Behavior

The various case statements do not need to be mutually exclusive.
`$switch` executes the first branch it finds which
evaluates to `true`. If none of the branches evaluates to true,
`$switch` executes the `default` option.

The following conditions cause `$switch` to fail with an
error:

- The `branches` field is missing or is not an array with at least
  one entry.

- An object in the `branches` array does not contain a `case`
  field.

- An object in the `branches` array does not contain a `then`
  field.

- An object in the `branches` array contains a field other than
  `case` or `then`.

- No `default` is specified and no `case` evaluates to `true`.

| Example | Results |
|---|---|
| .. code-block:: javascript :copyable: false { $switch: { branches: [ { case: { $eq: [ 0, 5 ] }, then: "equals" }, { case: { $gt: [ 0, 5 ] }, then: "greater than" }, { case: { $lt: [ 0, 5 ] }, then: "less than" } ] } } | `"less than"` |
| .. code-block:: javascript :copyable: false { $switch: { branches: [ { case: { $eq: [ 0, 5 ] }, then: "equals" }, { case: { $gt: [ 0, 5 ] }, then: "greater than" } ], default: "Did not match" } } | `"Did not match"` |
| .. code-block:: javascript :copyable: false { $switch: { branches: [ { case: "this is true", then: "first case" }, { case: false, then: "second case" } ], default: "Did not match" } } | `"First case"` |

## Example

The following example uses the `movies` collection from the sample_mflix
sample dataset.  For details on how to load this dataset into
your deployment, see Load the sample dataset.

This aggregation operation uses `$switch` to
display a particular message based on each movie's rating. The
`$match` stage limits the results to the three longest
movies in the sample dataset:

```javascript
```

Output:

```javascript
```

**See also:**

`$cond`
