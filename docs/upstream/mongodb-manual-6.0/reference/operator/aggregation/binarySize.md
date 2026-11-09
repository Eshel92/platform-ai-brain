<!-- Converted from reference/operator/aggregation/binarySize.txt (reStructuredText). Includes are inlined. -->

# $binarySize (aggregation)

## Definition

**`$binarySize`**

Returns the size of a given string or binary data value's content in
bytes.

`$binarySize` has the following syntax:

```javascript
{ $binarySize: <string or binData> }
```

The argument can be any valid expression as long as it resolves to
either a string or binary data value. For more information on
expressions, see aggregation-expressions.

## Behavior

The argument for `$binarySize` must resolve to either:

- A string,

- A binary data value, or

- null.

If the argument is a string or binary data value, the expression
returns the size of the argument in bytes. 

If the argument is `null`, the expression returns `null`.

If the argument resolves to any other data type,
`$binarySize` errors.

### String Size Calculation

If the argument for `$binarySize` is a string, the operator
counts the number of UTF-8 encoded bytes in a string where each character
may use between one and four bytes.

For example, US-ASCII characters are encoded using one byte. Characters
with diacritic markings and additional Latin alphabetical characters
(Latin characters outside of the English alphabet) are encoded
using two bytes. Chinese, Japanese and Korean characters typically
require three bytes, and other planes of unicode (emoji, mathematical
symbols, etc.) require four bytes. 

Consider the following examples:

| Example | Results | Notes |
|---|---|---|
| .. code-block:: javascript :copyable: false { $binarySize: "abcde" } | `5` | Each character is encoded using one byte. |
| .. code-block:: javascript :copyable: false { $binarySize: "Hello World!" } | `12` | Each character is encoded using one byte. |
| .. code-block:: javascript :copyable: false { $binarySize: "cafeteria" } | `9` | Each character is encoded using one byte. |
| .. code-block:: javascript :copyable: false { $binarySize: "cafétéria" } | `11` | `é` is encoded using two bytes. |
| .. code-block:: javascript :copyable: false { $binarySize: "" } | `0` | Empty strings return 0. |
| .. code-block:: javascript :copyable: false { $binarySize: "$€λG" } | `7` | `€` is encoded using three bytes. `λ` is encoded using two bytes. |
| .. code-block:: javascript :copyable: false { $binarySize: "寿司" } | `6` | Each character is encoded using three bytes. |

## Example

In `mongosh`, create a sample collection named
`images` with the following documents:

```javascript
db.images.insertMany([
  { _id: 1, name: "cat.jpg", binary: new BinData(0, "OEJTfmD8twzaj/LPKLIVkA==")},
  { _id: 2, name: "big_ben.jpg", binary: new BinData(0, "aGVsZmRqYWZqYmxhaGJsYXJnYWZkYXJlcTU1NDE1Z2FmZCBmZGFmZGE=")},
  { _id: 3, name: "tea_set.jpg", binary: new BinData(0, "MyIRAFVEd2aImaq7zN3u/w==")},
  { _id: 4, name: "concert.jpg", binary: new BinData(0, "TWFuIGlzIGRpc3Rpbmd1aXNoZWQsIG5vdCBvbmx5IGJ5IGhpcyByZWFzb24sIGJ1dCBieSB0aGlzIHNpbmd1bGFyIHBhc3Npb24gZnJvbSBvdGhlciBhbmltYWxzLCB3aGljaCBpcyBhIGx1c3Qgb2YgdGhlIG1pbmQsIHRoYXQgYnkgYSBwZXJzZXZlcmFuY2Ugb2YgZGVsaWdodCBpbiB0aGUgY29udGludWVkIGFuZCBpbmRlZmF0aWdhYmxlIGdlbmVyYXRpb24gb2Yga25vd2xlZGdlLCBleGNlZWRzIHRoZSBzaG9ydCB2ZWhlbWVuY2Ugb2YgYW55IGNhcm5hbCBwbGVhc3VyZS4=")},
  { _id: 5, name: "empty.jpg", binary: new BinData(0, "") }
])
```

The following aggregation `projects`:

- The `name` field

- The `imageSize` field, which uses `$binarySize` to
  return the size of the document's `binary` field in bytes.

```javascript
db.images.aggregate([
  {
    $project: {
      "name": "$name",
      "imageSize": { $binarySize: "$binary" }
    }
  }
])
```

The operation returns the following result:

```javascript
{ "_id" : 1, "name" : "cat.jpg", "imageSize" : 16 }
{ "_id" : 2, "name" : "big_ben.jpg", "imageSize" : 41 }
{ "_id" : 3, "name" : "teaset.jpg", "imageSize" : 16 }
{ "_id" : 4, "name" : "concert.jpg", "imageSize" : 269 }
{ "_id" : 5, "name" : "empty.jpg", "imageSize" : 0 }
```

### Find Largest Binary Data

The following pipeline returns the image with the largest 
binary data size:

```javascript
db.images.aggregate([
   // First Stage
   { $project: { name: "$name", imageSize: { $binarySize: "$binary" } }  },
   // Second Stage
   { $sort: { "imageSize" : -1 } },
   // Third Stage
   { $limit: 1 }
])
```

First Stage
  The first stage of the pipeline `projects`:
  
  - The `name` field

  - The `imageSize` field, which uses `$binarySize` to
    return the size of the document's `binary` field in bytes.

  This stage outputs the following documents to the next stage:

  ```javascript
  { "_id" : 1, "name" : "cat.jpg", "imageSize" : 16 }
  { "_id" : 2, "name" : "big_ben.jpg", "imageSize" : 41 }
  { "_id" : 3, "name" : "teaset.jpg", "imageSize" : 16 }
  { "_id" : 4, "name" : "concert.jpg", "imageSize" : 269 }
  { "_id" : 5, "name" : "empty.jpg", "imageSize" : 0 }
  ```

Second Stage
  The second stage `sorts` the documents by
  `imageSize` in descending order.

  This stage outputs the following documents to the next stage:

  ```javascript
  { "_id" : 4, "name" : "concert.jpg", "imageSize" : 269 }
  { "_id" : 2, "name" : "big_ben.jpg", "imageSize" : 41 }
  { "_id" : 1, "name" : "cat.jpg", "imageSize" : 16 }
  { "_id" : 3, "name" : "teaset.jpg", "imageSize" : 16 }
  { "_id" : 5, "name" : "empty.jpg", "imageSize" : 0 }
  ```

Third Stage
  The third stage `limits` the output documents to
  only return the document appearing first in the sort order:

  ```javascript
  { "_id" : 4, "name" : "concert.jpg", "imageSize" : 269 }
  ```

**See also:**

- `$project`
- `$sort`
- `$limit`
- `$strLenBytes`
- `$bsonSize`
