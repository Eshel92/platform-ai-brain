<!-- Converted from reference/method/HexData.txt (reStructuredText). Includes are inlined. -->

# HexData() (mongosh method)

## Definition

Creates a binary data object from hexadecimal data.

## Syntax

`HexData()` has the following syntax:

**`HexData( <subType>, <buffer> )`**

:returns: Binary data object.

## Command Fields

The command takes these fields:

* - Field
  - Type
  - Necessity
  - Description

* - `subType`
  - integer
  - Required
  - Specify a data subtype:

    - `0`: Generic binary subtype

    - `1`: Function

    - `2`: Byte Array

    - `3`: OLD UUID

    - `4`: UUID

    - `5`: MD5

    - `128`: User defined

* - `buffer`
  - string
  - Required
  - Hexadecimal data. The string is decoded up to the first character
    that is not a valid hexadecimal digit. You can use upper or lower
    case letters in the hexadecimal string.

**Note:**

`mongosh` silently stops parsing at the first non-hex character, unlike the 
legacy shell which rejects invalid hex characters. To determine if your 
`HexData()` output is valid, you can use the `.toString('hex')` method on the 
`HexData()` output and compare that string against the original input string
using a case-insensitive comparison.

## Examples

**Step 1: Create the example collection**

Use `HexData()` to insert a document with binary data created
from a hexadecimal string into a test collection:

```javascript
db.hexCollection.insertOne( {
   _id: 0, hexField: HexData( 0, "123456abcdef" )
} )
```

**Step 2: Retrieve the document**

To return the document, run the following `find` command:

```javascript
db.hexCollection.find()
```

Output shows the `hexField` value as a base 64 number using
`Binary.createFromBase64`:

```javascript
[ { _id: 0, hexField: Binary.createFromBase64('EjRWq83v', 0) } ]
```

## Learn More

- `BinData()`
- `Binary.createFromBase64()`
