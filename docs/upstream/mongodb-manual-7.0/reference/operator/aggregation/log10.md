<!-- Converted from reference/operator/aggregation/log10.txt (reStructuredText). Includes are inlined. -->

# $log10 (expression operator)

## Definition

**`$log10`**

Calculates the log base 10 of a number and returns the result as a
double.

`$log10` has the following syntax:

```javascript
{ $log10: <number> }
```

The `<number>` expression can be any valid expression as long as it resolves to a non-negative
number. For more information on expressions, see
aggregation-expressions.

`$log10` is equivalent to `$log: [ <number>, 10 ]` expression.

## Behavior

If the argument resolves to a value of `null` or refers to a field that is
missing, `$log10` returns `null`. If the argument resolves to
`NaN`, `$log10` returns `NaN`.

| Example | Results |
|---|---|
| `{ $log10: 1 }` | `0` |
| `{ $log10: 10 }` | `1` |
| `{ $log10: 100 }` | `2` |
| `{ $log10: 1000 }` | `3` |

## Example

Create a collection named `samples` with the following documents:

```javascript
db.samples.insertMany(
   [
      { _id: 1, H3O: 0.0025 },
      { _id: 2, H3O: 0.001 },
      { _id: 3, H3O: 0.02 }
   ]
)
```

The following example calculates the pH value of the samples:

```javascript
db.samples.aggregate( [ 
   { $project: { pH: { $multiply: [ -1, { $log10: "$H3O" } ] } } }
] )
```

The operation returns the following results:

```javascript
{ "_id" : 1, "pH" : 2.6020599913279625 }
{ "_id" : 2, "pH" : 3 }
{ "_id" : 3, "pH" : 1.6989700043360187 }
```

**See also:**

`$log`
