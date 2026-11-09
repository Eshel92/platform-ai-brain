<!-- Converted from reference/operator/aggregation/bitAnd.txt (reStructuredText). Includes are inlined. -->

# $bitAnd (expression operator)

## Definition

**New in version:** 6.3

**`$bitAnd`**

Returns the result of a bitwise `and` operation on an array of `int` or 
`long` values. 

## Syntax

The `$bitAnd` operator has the following syntax: 

```javascript
{ $bitAnd: [ <expression1>, <expression2>, ... ] }
```

## Behavior

If the operands include both integers and long values, MongoDB sign-extends the 
calculated integer result and returns a long value. Otherwise, if the operands 
include only integers or only longs, MongoDB returns results with the 
corresponding value type.

**Note:**

All numbers in `mongosh` are doubles, not integers. To  
specify integers in `mongosh`, use the `Int32()` or the 
`Long()` constructor. To learn more, see shell-type-int or 
shell-type-long.

To learn how your MongoDB driver handles numeric values, refer to your 
`driver's documentation`.

If any arguments in the array are of a different data type such as a string, 
double, or decimal, MongoDB returns an error.

If the argument is an empty array, the operation returns `Int32(-1)`.

If any of the operands equate to `null`, the operation returns `null`. 

## Examples

The examples on this page use the `switches` collection, which contains the 
following documents: 

```javascript
db.switches.insertMany( [
    { _id: 0, a: Int32(0), b: Int32(127) },
    { _id: 1, a: Int32(2), b: Int32(3) },
    { _id: 2, a: Int32(3), b: Int32(5) }
] )
```

### Bitwise `AND` with Two Integers

The following aggregation uses the `$bitAnd` operator in the 
`$project` stage:

```javascript
db.switches.aggregate( [
  { 
    $project: { 
      result: { 
        $bitAnd: [ "$a", "$b" ]
      }
    }
  }
])
```

The operation returns the following results:

```javascript
  [
    { _id: 0, result: 0 }
    { _id: 1, result: 2 }
    { _id: 2, result: 1 }
  ]
```

### Bitwise `AND` with a Long and Integer

The following aggregation uses the `$bitAnd` operator in the 
`$project` stage:

```javascript
db.switches.aggregate( [
  { 
    $project: { 
      result: { 
        $bitAnd: [ "$a", Long("63") ]
      }
    }
  }
])
```

The operation returns the following results:

```javascript
  [
    { _id: 0, result: Long("0") }
    { _id: 1, result: Long("2") }
    { _id: 2, result: Long("3") }
  ]
```

## Learn More

- aggregation-pipeline-operators

- update-bit
