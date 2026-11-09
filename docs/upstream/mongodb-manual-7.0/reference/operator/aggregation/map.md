<!-- Converted from reference/operator/aggregation/map.txt (reStructuredText). Includes are inlined. -->

# $map (expression operator)

## Definition

**`$map`**

Applies an expression to
each item in an array and returns an array with the applied results.

## Compatibility

You can use `$map` for deployments hosted in the following
environments:

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas): The fully
  managed service for MongoDB deployments in the cloud
- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Syntax

The `$map` expression has the following syntax:

```javascript
{ $map: { input: <expression>, as: <string>, in: <expression> } }
```

| Field | Specification |
|---|---|
| `input` | An expression that resolves to an array. If `input` resolves to `null` or refers to a missing field, `$map` returns `null`. If `input` resolves to a non-array, non-null value, the pipeline errors. |
| `as` | Optional. A name for the variable that represents each individual element of the `input` array. If no name is specified, the variable name defaults to `this`. |
| `in` | An expression that is applied to each element of the `input` array. The expression references each element individually with the variable name specified in `as`. |

For more information on expressions, see
aggregation-expressions.

## Examples

### Add to Each Element of an Array

The examples on this page use data from the sample_mflix dataset. For details on how to load this dataset into your self-managed
MongoDB deployment, see Load the Sample Dataset.
If you made any modifications to the sample databases, you may need to drop and
recreate the databases to run the examples on this page. 

The following aggregation operation uses `$map` with
the `$add` expression to add `10` to each element
in the `location.geo.coordinates` array:

```javascript
```

Output:

```javascript
```

### Truncate Each Array Element

The following aggregation operation uses `$map` to
`truncate` each element in the
`location.geo.coordinates` array to its integer:

```javascript
```

Output:

```javascript
```

### Apply Arithmetic Operators to Each Array Element

The following aggregation operation uses the `$addFields`
stage to add a new `genreScores` field. The operation uses
`$map` to apply `$multiply` and
`$add` to each element in the `genres` array,
computing a score based on the character count of each genre name:

```javascript
```

Output:

```javascript
```

## Learn More

To learn more about expressions used in the previous examples, see:

- `$add`
- `$multiply`
- `$trunc`
- `$strLenCP`
