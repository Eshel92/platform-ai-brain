<!-- Converted from reference/operator/aggregation/abs.txt (reStructuredText). Includes are inlined. -->

# $abs (aggregation)

## Definition

**`$abs`**

Returns the absolute value of a number.

`$abs` has the following syntax:

```javascript
{ $abs: <number> }
```

The `<number>` expression can be any valid expression as long as it resolves to a number. For
more information on expressions, see aggregation-expressions.

## Behavior

If the argument resolves to a value of `null` or refers to a field that is
missing, `$abs` returns `null`. If the argument resolves to
`NaN`, `$abs` returns `NaN`.

| Example | Results |
|---|---|
| `{ $abs: -1 }` | `1` |
| `{ $abs: 1 }` | `1` |
| `{ $abs: null }` | `null` |

## Example

A collection `temperatureChange` contains the following documents:

```javascript
db.temperatureChange.insertMany( [
   { _id: 1, startTemp: 50, endTemp: 80 },
   { _id: 2, startTemp: 40, endTemp: 40 },
   { _id: 3, startTemp: 90, endTemp: 70 },
   { _id: 4, startTemp: 60, endTemp: 70 }
] )
```

The following example calculates the magnitude of difference between
the `startTemp` and `endTemp` ratings:

```javascript
db.temperatureChange.aggregate([
   {
      $project: { delta: { $abs: { $subtract: [ "$startTemp", "$endTemp" ] } } }
   }
])
```

The operation returns the following results:

```javascript
{ "_id" : 1, "delta" : 30 }
{ "_id" : 2, "delta" : 0 }
{ "_id" : 3, "delta" : 20 }
{ "_id" : 4, "delta" : 10 }
```
