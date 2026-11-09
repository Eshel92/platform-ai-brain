<!-- Converted from reference/operator/query/bitsAllSet.txt (reStructuredText). Includes are inlined. -->

# $bitsAllSet (query predicate operator)

**`$bitsAllSet`**

`$bitsAllSet` matches documents where *all* of the bit positions
given by the query are set (i.e. `1`) in `field`.

|  |
|---|
| `{ <field>: { $bitsAllSet: <numeric bitmask> } }` |
| `{ <field>: { $bitsAllSet: <` `BinData` `bitmask> } }` |
| `{ <field>: { $bitsAllSet: [ <position1>, <position2>, ... ] } }` |

The `field` value must be either numeric or a
`BinData` instance. Otherwise, `$bitsAllSet`
will not match the current document.

Numeric Bitmask
  You can provide a numeric bitmask to be matched against the operand field.
  The bitmask must be a non-negative 64-bit signed integer.
  Otherwise, `$bitsAllSet` returns an error.

BinData Bitmask
  You can also use an arbitrarily large `BinData` 
  instance as a bitmask.

Position List
  If querying a list of bit positions, each `<position>` must be a non-negative
  integer. Bit positions start at `0` from the least significant bit. For
  example, the decimal number `254` would have the following bit positions:

| Bit Value | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 |
|---|---|---|---|---|---|---|---|---|
| Position | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |

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

### Indexes

Queries cannot use indexes for the `$bitsAllSet` portion of a
query, although the other portions of a query can use indexes, if
applicable.

### Floating Point Values

`$bitsAllSet` will not match numerical values that cannot be represented as
a signed 64-bit integer. This can be the case if a value is either too large
or too small to fit in a signed 64-bit integer, or if it has a fractional
component.

### Sign Extension

Numbers are sign extended. For example, `$bitsAllSet` considers bit position `200`
to be set for the negative number `-5`, but bit position `200` to be clear
for the positive number `+5`.

In contrast, `BinData` instances are zero-extended.
For example, given the following document:

```javascript
db.collection.insertOne({ x: BinData(0, "ww=="), binaryValueofA: "11000011" })
```

`$bitsAllSet` will consider all bits outside of `x` to be clear.

## Examples

The following examples will use a collection with the following documents:

```javascript
db.collection.insertMany([
  { _id: 1, a: 54, binaryValueofA: "00110110" },
  { _id: 2, a: 20, binaryValueofA: "00010100" },
  { _id: 3, a: 20.0, binaryValueofA: "00010100" },
  { _id: 4, a: BinData(0, "Zg=="), binaryValueofA: "01100110" }
])
```

### Bit Position Array

The following query uses the `$bitsAllSet` operator to test
whether field `a` has bits set at position `1` and position
`5`, where the least significant bit is position `0`.

```javascript
db.collection.find( { a: { $bitsAllSet: [ 1, 5 ] } } )
```

The query matches the following documents:

```javascript
{ "_id" : 1, "a" : 54, "binaryValueofA" : "00110110" }
{ "_id" : 4, "a" : BinData(0,"Zg=="), "binaryValueofA" : "01100110" }
```

### Integer Bitmask

The following query uses the `$bitsAllSet` operator to test
whether field `a` has bits set at positions `1`, `4`, and `5`
(the binary representation of the bitmask `50` is `00110010`).

```javascript
db.collection.find( { a: { $bitsAllSet: 50 } } )
```

The query matches the following document:

```javascript
{ "_id" : 1, "a" : 54, "binaryValueofA" : "00110110" }
```

### BinData Bitmask

The following query uses the `$bitsAllSet` operator to test
whether field `a` has bits set at positions `4` and `5`
(the binary representation of `BinData(0, "MA==")` is `00110000`).

```javascript
db.collection.find( { a: { $bitsAllSet: BinData(0, "MA==") } } )
```

The query matches the following document:

```javascript
{ _id: 1, a: 54, binaryValueofA: "00110110" }
```
