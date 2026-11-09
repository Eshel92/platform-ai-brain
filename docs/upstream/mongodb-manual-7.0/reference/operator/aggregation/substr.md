<!-- Converted from reference/operator/aggregation/substr.txt (reStructuredText). Includes are inlined. -->

# $substr (expression operator)

## Definition

**`$substr`**

**Deprecated since version:** 3.4

`$substr` is now an alias for
`$substrBytes`.

Returns a substring of a string, starting at a specified index
position and including the specified number of characters. The index
is zero-based.

`$substr` has the following syntax:

```javascript
{ $substr: [ <string>, <start>, <length> ] }
```

The arguments can be any valid expression as long as the first argument
resolves to a string, and the second and third arguments resolve to
integers. For more information on expressions, see
aggregation-expressions.

## Behavior

If `<start>` is a negative number, `$substr` returns an
empty string `""`.

If `<length>` is a negative number, `$substr` returns a
substring that starts at the specified index and includes the rest of
the string.

`$substr` only has a well-defined behavior for strings of ASCII characters.

## Example

The following example uses the `movies` collection from the sample_mflix
sample dataset.  For details on how to load this dataset into
your deployment, see Load the sample dataset.

This aggregation operation uses the `$substr`
operator to separate the `title` value into a `titleStart` and a
`titleRest`. The second expression uses a negative `<length>` to
return the characters from index `3` to the end of the string:

```javascript
```

Output:

```javascript
```
