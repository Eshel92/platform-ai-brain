<!-- Converted from reference/mql/query-predicates/type-bracketing.txt (reStructuredText). Includes are inlined. -->

# Type Bracketing in Query Predicates

Type bracketing is an implicit filter that MongoDB applies to query
predicates: a comparison on a given BSON type matches only values of
that type. For example, `{ a: { $gt: 0 } }` means "`a` is a number
*and* `a` is greater than `0`".

## Which Operators Type Bracket

The inequality operators (`$gt`, `$gte`, `$lt`,
and `$lte`) use type bracketing.

Negations (`$ne` and `$nin`) do not use type bracketing.
They match values of any type. For example, `{ a: { $ne: 2 } }` also
matches documents where `a` is a string or an object, in addition to
the numeric type in the comparison.

## Type Bracketing for Comparisons to Numbers

BSON has several numeric types: `int`, `long`, `double`, and
`decimal`. MongoDB treats these as equivalent for comparison, so a
comparison against a number matches values of any numeric type.

For example, `{ a: { $gt: 0 } }` matches `a` values of type `int`,
`long`, `double`, or `decimal`.

## Type Bracketing and Implicit Array Traversal

Type bracketing also applies when a comparison traverses an array
implicitly. If the target field is an array, the comparison matches
documents where at least one element satisfies the comparison and is of
the same type as the operand.

For example, `{ a: { $gt: 3 } }` matches `{ a: [ 1, 2, 3, 4 ] }` and
`{ a: [ "red", 4, "blue" ] }`, but not `{ a: [ "red", "blue" ] }`.

## Example

Consider the following collection:

```javascript
{ "_id": "apples", "qty": 5 }
{ "_id": "bananas", "qty": 7 }
{ "_id": "apricots", "qty": 3 }
{ "_id": "oranges", "qty": { "in stock": 8, "ordered": 12 } }
{ "_id": "avocados", "qty": "fourteen" }
```

The following query uses `$gt` to return documents where the
value of `qty` is greater than `4`:

```javascript
```

Output:

```javascript
```

The document with `_id` equal to `"apricots"` is not returned
because its `qty` value, `3`, is not greater than `4`.

The document with `_id` equal to `"avocados"` is not returned
because its `qty` value is of type `string` while the `$gt`
operand is of type `integer`.

The document with `_id` equal to `"oranges"` is not returned
because its `qty` value is of type `object`.

**Tip:**

To enforce data types in a collection, use
schema validation.
