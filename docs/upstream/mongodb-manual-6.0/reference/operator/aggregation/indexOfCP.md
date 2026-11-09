<!-- Converted from reference/operator/aggregation/indexOfCP.txt (reStructuredText). Includes are inlined. -->

# $indexOfCP (aggregation)

## Definition

**`$indexOfCP`**

Searches a string for an occurrence of a substring and returns the
UTF-8 [code point](http://www.unicode.org/glossary/#code_point)
index (zero-based) of the first occurrence. If the
substring is not found, returns `-1`.

`$indexOfCP` has the following operator
expression syntax:

```javascript
{ $indexOfCP: [ <string expression>, <substring expression>, <start>, <end> ] }
```

| Field | Type | Description |
|---|---|---|
| `<string>` | string | Can be any valid expression as long as it resolves to a string. For more information on expressions, see aggregation-expressions. If the string expression resolves to a value of `null` or refers to a field that is missing, `$indexOfCP` returns `null`. If the string expression does not resolve to a string or `null` nor refers to a missing field, `$indexOfCP` returns an error. |
| `<substring>` | string | Can be any valid expression as long as it resolves to a string. For more information on expressions, see aggregation-expressions. |
| `<start>` | integer | Optional. An integer, or a number that can be represented as integers (such as 2.0), that specifies the starting index position for the search. Can be any valid expression that resolves to a non-negative integral number. If unspecified, the starting index position for the search is the beginning of the string. |
| `<end>` | integer | Optional. An integer, or a number that can be represented as integers (such as 2.0), that specifies the ending index position for the search. Can be any valid expression that resolves to a non-negative integral number. If you specify a `<end>` index value, you should also specify a `<start>` index value; otherwise, `$indexOfCP` uses the `<end>` value as the `<start>` index value instead of the `<end>` value. If unspecified, the ending index position for the search is the end of the string. |

          
          
   

## Behavior

If the `<substring expression>` is found multiple times within the
`<string expression>`, then `$indexOfCP` returns the
index of the first `<substring expression>` found from the starting
index position.

`$indexOfCP` returns `null`:

- If `<string expression>` is null, or

- If `<string expression>` refers to a non-existing field in the
  input document.

`$indexOfCP` returns an error:

- If `<string expression>` is not a string and not null, or

- If `<substring expression>` is null or is not a string or refers to
  a nonexistent field in the input document, or

- If `<start>` or `<end>` is a negative integer (or a value that
  can be represented as a negative integer, like -5.0).

`$indexOfCP` returns `-1`:

- If the substring is not found in the `<string expression>`, or

- If `<start>` is a number greater than `<end>`, or

- If `<start>` is a number greater than the byte length of the string.

| Example | Results |
|---|---|
| `{ $indexOfCP: [ "cafeteria", "e" ] }` | `3` |
| `{ $indexOfCP: [ "cafétéria", "é" ] }` | `3` |
| `{ $indexOfCP: [ "cafétéria", "e" ] }` | `-1` |
| `{ $indexOfCP: [ "cafétéria", "t" ] }` | `4` |
| `{ $indexOfCP: [ "foo.bar.fi", ".", 5 ] }` | `7` |
| `{ $indexOfCP: [ "vanilla", "ll", 0, 2 ] }` | `-1` |
| `{ $indexOfCP: [ "vanilla", "ll", -1 ] }` | Error |
| `{ $indexOfCP: [ "vanilla", "ll", 12 ] }` | `-1` |
| `{ $indexOfCP: [ "vanilla", "ll", 5, 2 ] }` | `-1` |
| `{ $indexOfCP: [ "vanilla", "nilla", 3 ] }` | `-1` |
| `{ $indexOfCP: [ null, "foo" ] }` | `null` |

## Examples

Consider an `inventory` collection with the following documents:

```javascript
{ "_id" : 1, "item" : "foo" }
{ "_id" : 2, "item" : "fóofoo" }
{ "_id" : 3, "item" : "the foo bar" }
{ "_id" : 4, "item" : "hello world fóo" }
{ "_id" : 5, "item" : null }
{ "_id" : 6, "amount" : 3 }
```

The following operation uses the `$indexOfCP` operator to
return the code point index at which the string `foo` is located in
each `item` string:

```javascript
db.inventory.aggregate(
   [
     {
       $project:
          {
            cpLocation: { $indexOfCP: [ "$item", "foo" ] },
          }
      }
   ]
)
```

The operation returns the following results:

```javascript
{ "_id" : 1, "cpLocation" : "0" }
{ "_id" : 2, "cpLocation" : "3" }
{ "_id" : 3, "cpLocation" : "4" }
{ "_id" : 4, "cpLocation" : "-1" }
{ "_id" : 5, "cpLocation" : null }
{ "_id" : 6, "cpLocation" : null }
```

**See also:**

- `$indexOfBytes`
- `$indexOfArray`
