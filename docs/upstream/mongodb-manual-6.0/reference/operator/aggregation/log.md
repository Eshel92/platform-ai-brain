<!-- Converted from reference/operator/aggregation/log.txt (reStructuredText). Includes are inlined. -->

# $log (aggregation)

## Definition

**`$log`**

Calculates the log of a number in the specified base and returns the
result as a double.

`$log` has the following syntax:

```javascript
{ $log: [ <number>, <base> ] }
```

The `<number>` expression can be any valid expression as long as it resolves to a non-negative number.

The `<base>` expression can be any valid expression as long as it resolves to a positive
number greater than `1`.

For more information on expressions, see aggregation-expressions.

## Behavior

If either argument resolves to a value of `null` or refers to a field that is
missing, `$log` returns `null`. If either argument resolves to
`NaN`, `$log` returns `NaN`.

| Example | Results |
|---|---|
| `{ $log: [ 100, 10 ] }` | `2` |
| `{ $log: [ 100, Math.E ] }` where `Math.E` is a JavaScript representation for *e*. | `4.605170185988092` |

## Example

A collection `integers` contains the following documents:

```javascript
db.integers.insertMany( [
   { _id: 1, int: 5 },
   { _id: 2, int: 2 },
   { _id: 3, int: 23 },
   { _id: 4, int: 10 }
] )
```

The following example uses log`2` in its calculation to
determine the number of bits required to represent the value of
`int`.

```javascript
db.integers.aggregate([
   { $project: { bitsNeeded:
      {
         $floor: { $add: [ 1, { $log: [ "$int", 2 ] } ] } } }
      }
])
```

The operation returns the following results:

```javascript
{ "_id" : 1, "bitsNeeded" : 3 }
{ "_id" : 2, "bitsNeeded" : 2 }
{ "_id" : 3, "bitsNeeded" : 5 }
{ "_id" : 4, "bitsNeeded" : 4 }
```

**See also:**

- `$log10`
- `$ln`
