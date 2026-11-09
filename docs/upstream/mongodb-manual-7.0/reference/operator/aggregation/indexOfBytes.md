<!-- Converted from reference/operator/aggregation/indexOfBytes.txt (reStructuredText). Includes are inlined. -->

# $indexOfBytes (expression operator)

## Definition

**`$indexOfBytes`**

Searches a string for an occurrence of a substring and returns the
UTF-8 byte index (zero-based) of the first occurrence. If the
substring is not found, returns `-1`.

`$indexOfBytes` has the following operator
expression syntax:

```javascript
{ $indexOfBytes: [ <string expression>, <substring expression>, <start>, <end> ] }
```

| Operand | Description |
|---|---|
| `<string expression>` | Can be any valid expression as long as it resolves to a string. For more information on expressions, see aggregation-expressions. If the string expression resolves to a value of `null` or refers to a field that is missing, `$indexOfBytes` returns `null`. If the string expression does not resolve to a string or `null` nor refers to a missing field, `$indexOfBytes` returns an error. |
| `<substring expression>` | Can be any valid expression as long as it resolves to a string. For more information on expressions, see aggregation-expressions. |
| `<start>` | *Optional* An integral number that specifies the starting index position for the search. Can be any valid expression that resolves to a non-negative integral number. |
| `<end>` | *Optional* An integral number that specifies the ending index position for the search. Can be any valid expression that resolves to a non-negative integral number. If you specify a `<end>` index value, you should also specify a `<start>` index value; otherwise, `$indexOfBytes` uses the `<end>` value as the `<start>` index value instead of the `<end>` value. |

## Behavior

- If `<string expression>` is null, `$indexOfBytes` returns `null`.

- If `$indexOfBytes` is called on a field that doesn't exist in the document, `$indexOfBytes` returns `null`.

- If `<string expression>` is not a string and not null, `$indexOfBytes` returns an error.

- If `<substring expression>` is null, `$indexOfBytes` returns an error.

- If `<start>` or `<end>` is a negative number, `$indexOfBytes` returns an error.

- If `<start>` is a number greater than `<end>`, `$indexOfBytes` returns `-1`.

- If `<start>` is a number greater than the byte length of the string, `$indexOfBytes` returns `-1`.

- If `<start>` or `<end>` is given a value that is not an integer, `$indexOfBytes` returns an error.

- If the `<substring expression>` is found multiple times within the `<string expression>`, then `$indexOfBytes` returns the index of the first `<substring expression>` found.

Some short examples to highlight different behavior:

| Example | Results |
|---|---|
| `{ $indexOfBytes: [ "cafeteria", "e" ] }` | `3` |
| `{ $indexOfBytes: [ "cafétéria", "é" ] }` | `3` |
| `{ $indexOfBytes: [ "cafétéria", "e" ] }` | `-1` |
| `{ $indexOfBytes: [ "cafétéria", "t" ] }` | `5` |
| `{ $indexOfBytes: [ "foo.bar.fi", ".", 5 ] }` | `7` |
| `{ $indexOfBytes: [ "vanilla", "ll", 0, 2 ] }` | `-1` |
| `{ $indexOfBytes: [ "vanilla", "ll", -1 ] }` | `-1` |
| `{ $indexOfBytes: [ "vanilla", "ll", 12 ] }` | `-1` |
| `{ $indexOfBytes: [ "vanilla", "ll", 5, 2 ] }` | `-1` |
| `{ $indexOfBytes: [ "vanilla", "nilla", 3 ] }` | `-1` |
| `{ $indexOfBytes: [ null, "foo" ] }` | `null` |

## Examples

Consider an `inventory` collection with the following documents:

```javascript
db.inventory.insertMany( [
   { _id: 1, item: "foo" },
   { _id: 2, item: "fóofoo" },
   { _id: 3, item: "the foo bar" },
   { _id: 4, item: "hello world fóo" },
   { _id: 5, item: null },
   { _id: 6, amount: 3 }
] )
```

The following operation uses the `$indexOfBytes` operator to
retrieve the indexes at which the string `foo` is located in each item:

```javascript
db.inventory.aggregate(
   [
     {
       $project:
          {
            byteLocation: { $indexOfBytes: [ "$item", "foo" ] },
          }
      }
   ]
)
```

The operation returns the following results:

```javascript
{ _id: 1, byteLocation: "0" }
{ _id: 2, byteLocation: "4" }
{ _id: 3, byteLocation: "4" }
{ _id: 4, byteLocation: "-1" }
{ _id: 5, byteLocation: null }
{ _id: 6, byteLocation: null }
```

**See also:**

- `$indexOfCP`
- `$indexOfArray`
