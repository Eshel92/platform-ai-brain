<!-- Converted from reference/operator/aggregation/type.txt (reStructuredText). Includes are inlined. -->

# $type  (expression operator)

## Definition

**`$type`**

Returns a string that specifies the BSON type of the argument.

`$type` has the following operator expression
syntax:

```javascript
{ $type: <expression> }
```

The argument can be any valid expression.

**See also:**

- `$isNumber` - checks if the argument is a number.
- `$type (Query)` - filters fields based on BSON type.

## Behavior

### `$type`

Unlike the `$type` query operator, which matches array
elements based on their BSON type, the `$type`
aggregation operator does not examine array elements. Instead,
when passed an array as its argument, the `$type` aggregation
operator returns the type of the argument, i.e. `"array"`.

If the argument is a field that is missing in the input document,
`$type` returns the string `"missing"`.

The following table shows the `$type` output for several
common types of expressions:

| Example | Results |
|---|---|
| `{ $type: "a" }` | `"string"` |
| `{ $type: /a/ }` | `"regex"` |
| `{ $type: 1 }` | `"double"` |
| `{ $type: Long(627) }` | `"long"` |
| `{ $type: { x: 1 } }` | `"object"` |
| `{ $type: [ [ 1, 2, 3 ] ] }` | `"array"` |

**Note:**

In the case of a literal array such as `[ 1, 2, 3 ]`,
enclose the expression in an outer set
of array brackets to prevent MongoDB from parsing
`[ 1, 2, 3 ]` as an
argument list
with three arguments (`1, 2, 3`). Wrapping the array
`[ 1, 2, 3 ]` in a `$literal` expression
achieves the same result.

See operator expression syntax forms for more information.

### Available Types

| Type | Number | Alias | Notes |
|---|---|---|---|
| Double | 1 | "double" |  |
| String | 2 | "string" |  |
| Object | 3 | "object" |  |
| Array | 4 | "array" |  |
| Binary data | 5 | "binData" |  |
| Undefined | 6 | "undefined" | Deprecated. |
| ObjectId | 7 | "objectId" |  |
| Boolean | 8 | "bool" |  |
| Date | 9 | "date" |  |
| Null | 10 | "null" |  |
| Regular Expression | 11 | "regex" |  |
| DBPointer | 12 | "dbPointer" | Deprecated. |
| JavaScript | 13 | "javascript" |  |
| Symbol | 14 | "symbol" | Deprecated. |
| JavaScript with scope | 15 | "javascriptWithScope" | Deprecated. |
| 32-bit integer | 16 | "int" |  |
| Timestamp | 17 | "timestamp" |  |
| 64-bit integer | 18 | "long" |  |
| Decimal128 | 19 | "decimal" |  |
| Min key | -1 | "minKey" |  |
| Max key | 127 | "maxKey" |  |

If the argument is a field that is missing in the input document,
`$type` returns the string `"missing"`.

## Example

This example uses a collection named `coll` with
the following documents:

```shell
db.coll.insertMany( [
   { _id: 0, a : 8 },
   { _id: 1, a : [ 41.63, 88.19 ] },
   { _id: 2, a : { a : "apple", b : "banana", c: "carrot" } },
   { _id: 3, a :  "caribou" },
   { _id: 4, a : Long(71) },
   { _id: 5, a : null },
   { _id: 6 }
] )
```

The following aggregation operation uses the `$type`
operator to display the type of field `a` for all documents
as part of the `$project` stage.

```shell
```

Output:

```shell
```

### Existence Check

Expressions do not support the `$exists`
operator. To evaluate whether or not a field exists in an expression, you can
use the `missing` type.

The following aggregation operation uses the `missing` type to add an `a`
field to documents from the `coll` collection above that are missing the
`a` field. Notice that a document where `a: null` is not the same as a
document where the `a` field is missing.

```shell
```

Output:

```shell
```
