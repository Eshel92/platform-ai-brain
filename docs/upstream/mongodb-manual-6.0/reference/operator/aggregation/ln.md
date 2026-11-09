<!-- Converted from reference/operator/aggregation/ln.txt (reStructuredText). Includes are inlined. -->

# $ln (aggregation)

## Definition

**`$ln`**

Calculates the natural logarithm *ln* (i.e log`e`) of a number and
returns the result as a double.

`$ln` has the following syntax:

```javascript
{ $ln: <number> }
```

The `<number>` expression can be any valid expression as long as it resolves to a non-negative
number. For more information on expressions, see
aggregation-expressions.

`$ln` is equivalent to `$log: [ <number>, Math.E ]`
expression, where `Math.E` is a JavaScript representation for
Euler's number *e*.

## Behavior

If the argument resolves to a value of `null` or refers to a field that is
missing, `$ln` returns `null`. If the argument resolves to
`NaN`, `$ln` returns `NaN`.

| Example | Results |
|---|---|
| `{ $ln: 1 }` | `0` |
| `{ $ln: Math.E }` where `Math.E` is a JavaScript representation for *e*. | `1` |
| `{ $ln: 10  }` | `2.302585092994046` |

## Example

A collection `sales` contains the following documents:

```javascript
{ _id: 1, year: "2000", sales: 8700000 }
{ _id: 2, year: "2005", sales: 5000000 }
{ _id: 3, year: "2010", sales: 6250000 }
```

The following example transforms the `sales` data:

```javascript
db.sales.aggregate( [ { $project: { x: "$year", y: { $ln: "$sales"  } } } ] )
```

The operation returns the following results:

```javascript
{ "_id" : 1, "x" : "2000", "y" : 15.978833583624812 }
{ "_id" : 2, "x" : "2005", "y" : 15.424948470398375 }
{ "_id" : 3, "x" : "2010", "y" : 15.648092021712584 }
```

**See also:**

`$log`
