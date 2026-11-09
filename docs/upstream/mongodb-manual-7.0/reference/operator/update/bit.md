<!-- Converted from reference/operator/update/bit.txt (reStructuredText). Includes are inlined. -->

# $bit (update operator)

## Definition

**`$bit`**

The `$bit` operator performs a bitwise update of a field.
The operator supports bitwise `and`, bitwise
`or`, and bitwise `xor` (i.e. exclusive or) operations. To
specify a `$bit` operator expression, use the following
prototype:

```javascript
{ $bit: { <field>: { <and|or|xor>: <int> } } }
```

Only use this operator with integer fields (either 32-bit integer or
64-bit integer).

To specify a `<field>` in an embedded document or in an array, use
dot notation.

**Note:**

All numbers in `mongosh` are doubles, not integers. To  
specify integers in `mongosh`, use the `Int32()` or the 
`Long()` constructor. To learn more, see shell-type-int or 
shell-type-long.

To learn how your MongoDB driver handles numeric values, refer to your 
`driver's documentation`.

## Behavior

Starting in MongoDB 5.0, `mongod` no longer raises an
error when you use an update operator like `$bit`
with an empty operand expression ( `{ }` ). An empty update results
in no changes and no oplog entry is created (meaning that the
operation is a no-op).

Starting in MongoDB 5.0, update operators process document fields with
string-based names in lexicographic order. Fields with numeric names are
processed in numeric order. See Update Operators Behavior for details.

## Examples

The following examples use the `switches` collection:

```javascript
db.switches.insertMany( [
   { _id: 1, expdata: Int32(13) },
   { _id: 2, expdata: Int32(3) },
   { _id: 3, expdata: Int32(1) }
] )
```

### Bitwise AND

Use a bitwise `and` in the `updateOne()`
operation to update `expdata`.

```javascript
db.switches.updateOne(
   { _id: 1 },
   { $bit: { expdata: { and: Int32( 10 ) } } }
)
```

The bitwise `and` operation:

- gets the bitwise value of `expdata`
- uses `and` to apply the bitwise value of Int32(10)
- updates `expdata` with the result, 1000

```javascript
1101   // expdata
1010   // Int32(10)
----
1000
```

Binary 1000 is equivalent to Int32(8). The
`db.switches.find( { _id: 1 } )` command returns the following
document:

```javascript
{ "_id" : 1, "expdata" : 8 }
```

### Bitwise OR

Use a bitwise `or` in the `updateOne()`
operation to update `expdata`.

```javascript
db.switches.updateOne(
   { _id: 2 },
   { $bit: { expdata: { or: Int32( 5 ) } } }
)
```

The bitwise `or` operation:

- gets the bitwise value of `expdata`
- uses `or` to apply the bitwise value of Int32(5)
- updates `expdata` with the result, 0111

```javascript
0111   // expdata
0101   // Int32(5)
----
0111
```

Binary 0111 is equivalent to Int32(7). The 
`db.switches.find( { _id: 2 } )` command returns the following
document:

```javascript
{ "_id" : 2, "expdata" : 7 }
```

### Bitwise XOR

Use a bitwise `xor` in the `updateOne()`
operation to update `expdata`.

```javascript
db.switches.updateOne(
   { _id: 3 },
   { $bit: { expdata: { xor: Int32( 5 ) } } }
)
```

The bitwise `and` operation:

- gets the bitwise value of `expdata`
- uses `and` to apply the bitwise value of Int32(5)
- updates `expdata` with the result, 0100

```javascript
0001   // expdata
0101   // Int32(5)
----
0100
```

Binary 0100 is equivalent to `Int32(4)`. The
`db.switches.find( { _id: 3 } )` command returns the following
document:

```javascript
{ "_id" : 1, "expdata" : 4 }
```

**See also:**

- `db.collection.updateOne()`
- `db.collection.findAndModify()`
