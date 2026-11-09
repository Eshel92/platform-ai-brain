<!-- Converted from reference/operator/aggregation/eq.txt (reStructuredText). Includes are inlined. -->

# $eq (expression operator)

## Definition

**`$eq`**

Compares two values and returns:

- `true` when the values are equivalent.

- `false` when the values are not equivalent.

The `$eq` compares both value and type, using the
specified BSON comparison order
for values of different types.

`$eq` has this syntax:

```javascript
{ $eq: [ <expression1>, <expression2> ] }
```

The arguments can be any valid expression. For more information on expressions, see
aggregation-expressions.

## Example

The following example uses the `movies` collection from the sample_mflix
sample dataset.  For details on how to load this dataset into
your deployment, see Load the sample dataset.

This aggregation operation uses the `$eq` operator
to determine if the `year` field equals `1978`:

```javascript
```

Output:

```javascript
```
