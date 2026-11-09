<!-- Converted from reference/operator/aggregation/concat.txt (reStructuredText). Includes are inlined. -->

# $concat (expression operator)

## Definition

**`$concat`**

Concatenates strings and returns the concatenated string.

`$concat` has this syntax:

```javascript
{ $concat: [ <expression1>, <expression2>, ... ] }
```

The arguments can be any valid expression as long as they resolve to
strings. For more information on expressions, see
aggregation-expressions.

If the argument resolves to a value of `null` or refers to a field
that is missing, `$concat` returns `null`.

## Example

The following example uses the `movies` collection from the sample_mflix
sample dataset.  For details on how to load this dataset into
your deployment, see Load the sample dataset.

Use the `$concat` operator to concatenate the `title` field and
the `rated` field with a " - " delimiter. The `runtime` filter
limits the result to a small, representative set of documents:

```javascript
```

Output:

```javascript
```
