<!-- Converted from reference/method/BinData.txt (reStructuredText). Includes are inlined. -->

# BinData() (mongosh method)

## Definition

Creates a binary data object.

`BinData` has the following syntax:

**`BinData(<sub_type>,<buffer>)`**

* - Parameter

  - Type

  - Description

* - `sub_type`

  - integer

  - The binary type.

    | Subtype | Description |
    |---|---|
    | 0 | Generic binary subtype |
    | 1 | Function |
    | 2 | Byte Array |
    | 3 | OLD UUID |
    | 4 | UUID |
    | 5 | MD5 |
    | 128 | User defined |

* - `buffer`

  - string

  - The buffer object containing binary data, must be a base 64 encoded string value.

:returns: A binary data object.

## Compatibility

This method is available in deployments hosted in the following environments: 

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas): The fully
  managed service for MongoDB deployments in the cloud

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Behavior

The endianness of your system depends on the architecture of 
your machine. Numbers in BSON data are always stored as 
little-endian, if your system is big-endian this means 
that numeric data is converted between big and little endian.

In the context of the bit-test match expression operators:

- `$bitsAnySet`
- `$bitsAnyClear`
- `$bitsAllSet` 
- `$bitsAllClear` 

`BinData` values act as 
[bitmasks](https://en.wikipedia.org/wiki/Mask_(computing)) and are 
interpreted as though they are arbitrary-length unsigned little-endian 
numbers. The lowest-addressable byte is always interpreted as the least
significant byte. Similarly, the highest-addressable byte in the `BinData`
is always interpreted as the most significant byte.

## Examples

### Insert a `BinData()` Object

Use the `BinData()` constructor to create the `bdata` variable.

```javascript
var bdata = BinData(0, "gf1UcxdHTJ2HQ/EGQrO7mQ==")
```

Insert the object into the `testbin` collection.

```javascript
db.testbin.insertOne( { _id : 1, bin_data: bdata } )
```

Query the `testbin` collection for the inserted document.

```javascript
db.testbin.find()
```

You can see the binary `buffer` stored in the collection.

```javascript
{
  _id: 1,
  bin_data: Binary(Buffer.from("81fd547317474c9d8743f10642b3bb99", "hex"), 0) 
}
```

### Get the Length of `BinData()` Object

Use the `BinData()` constructor to create the `bdata` variable.

```javascript
var bdata = BinData(0, "gf1UcxdHTJ2HQ/EGQrO7mQ==")
```

Use `.length()` to return the bit length of the object.

```javascript
bdata.length()
```

The returned value is:

```javascript
16
```
