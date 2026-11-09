<!-- Converted from reference/operator/aggregation/floor.txt (reStructuredText). Includes are inlined. -->

# $floor (expression operator)

## Definition

**`$floor`**

Returns the largest integer less than or equal to the specified
number.

`$floor` has the following syntax:

```javascript
{ $floor: <number> }
```

The `<number>` expression can be any valid expression as long as it resolves to a number. For
more information on expressions, see aggregation-expressions.

## Behavior

If the argument resolves to a value of `null` or refers to a field that is
missing, `$floor` returns `null`. If the argument resolves to
`NaN`, `$floor` returns `NaN`.

| Example | Results |
|---|---|
| `{ $floor: 1 }` | `1` |
| `{ $floor: 7.80 }` | `7` |
| `{ $floor: -2.8 }` | `-3` |

## Example

Create a collection named `samples` with the following documents:

```javascript
db.samples.insertMany(
   [
      { _id: 1, value: 9.25 },
      { _id: 2, value: 8.73 },
      { _id: 3, value: 4.32 },
      { _id: 4, value: -5.34 }
   ]
)
```

The following example returns both the original value and the floor
value:

```javascript
db.samples.aggregate([
   { $project: { value: 1, floorValue: { $floor: "$value" } } }
])
```

The operation returns the following results:

```javascript
{ "_id" : 1, "value" : 9.25, "floorValue" : 9 }
{ "_id" : 2, "value" : 8.73, "floorValue" : 8 }
{ "_id" : 3, "value" : 4.32, "floorValue" : 4 }
{ "_id" : 4, "value" : -5.34, "floorValue" : -6 }
```
