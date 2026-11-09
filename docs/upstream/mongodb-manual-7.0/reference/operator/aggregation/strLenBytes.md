<!-- Converted from reference/operator/aggregation/strLenBytes.txt (reStructuredText). Includes are inlined. -->

# $strLenBytes (expression operator)

   

## Definition

**`$strLenBytes`**

Returns the number of UTF-8 encoded bytes in the specified string.

`$strLenBytes` has the following operator
expression syntax:

```javascript
{ $strLenBytes: <string expression> }
```

The argument can be any valid expression as long as it resolves to a string. For
more information on expressions, see aggregation-expressions.

If the argument resolves to a value of `null` or refers to a
missing field, `$strLenBytes` returns an error.

## Behavior

The `$strLenBytes` operator counts the number of UTF-8
encoded bytes in a string where each character may use between one
and four bytes.

For example, US-ASCII characters are encoded using one byte. Characters
with diacritic markings and additional Latin alphabetical characters
(Latin characters outside of the English alphabet) are encoded
using two bytes. Chinese, Japanese and Korean characters typically
require three bytes, and other planes of unicode (emoji, mathematical
symbols, etc.) require four bytes. 

The `$strLenBytes` operator differs from 
`$strLenCP` operator which counts the 
[code points](http://www.unicode.org/glossary/#code_point)
in the specified string regardless of how many bytes each character
uses.

| Example | Results | Notes |
|---|---|---|
| .. code-block:: javascript :copyable: false { $strLenBytes: "abcde" } | `5` | Each character is encoded using one byte. |
| .. code-block:: javascript :copyable: false { $strLenBytes: "Hello World!" } | `12` | Each character is encoded using one byte. |
| .. code-block:: javascript :copyable: false { $strLenBytes: "cafeteria" } | `9` | Each character is encoded using one byte. |
| .. code-block:: javascript :copyable: false { $strLenBytes: "cafétéria" } | `11` | `é` is encoded using two bytes. |
| .. code-block:: javascript :copyable: false { $strLenBytes: "" } | `0` | Empty strings return 0. |
| .. code-block:: javascript :copyable: false { $strLenBytes: "$€λG" } | `7` | `€` is encoded using three bytes. `λ` is encoded using two bytes. |
| .. code-block:: javascript :copyable: false { $strLenBytes: "寿司" } | `6` | Each character is encoded using three bytes. |

## Example

### Single-Byte and Multibyte Character Set

Create a `food` collection with the following documents:

```javascript
db.food.insertMany(
 [
    { "_id" : 1, "name" : "apple" },
    { "_id" : 2, "name" : "banana" },
    { "_id" : 3, "name" : "éclair" },
    { "_id" : 4, "name" : "hamburger" },
    { "_id" : 5, "name" : "jalapeño" },
    { "_id" : 6, "name" : "pizza" },
    { "_id" : 7, "name" : "tacos" },
    { "_id" : 8, "name" : "寿司" }
 ]
)
```

The following operation uses the `$strLenBytes` operator to calculate
the `length` of each `name` value:

```javascript
db.food.aggregate(
  [
    {
      $project: {
        "name": 1,
        "length": { $strLenBytes: "$name" }
      }
    }
  ]
)
```

The operation returns the following results:

```javascript
{ "_id" : 1, "name" : "apple", "length" : 5 }
{ "_id" : 2, "name" : "banana", "length" : 6 }
{ "_id" : 3, "name" : "éclair", "length" : 7 }
{ "_id" : 4, "name" : "hamburger", "length" : 9 }
{ "_id" : 5, "name" : "jalapeño", "length" : 9 }
{ "_id" : 6, "name" : "pizza", "length" : 5 }
{ "_id" : 7, "name" : "tacos", "length" : 5 }
{ "_id" : 8, "name" : "寿司", "length" : 6 }
```

The documents with `_id: 3` and `_id: 5` each contain a diacritic
character (`é` and `ñ` respectively) that requires two bytes to
encode. The document with `_id: 8` contains two Japanese characters
that are encoded using three bytes each.  This makes the `length`
greater than the number of characters in `name` for the documents
with `_id: 3`, `_id: 5` and `_id: 8`.

**See also:**

- `$strLenCP`
- `$binarySize`
