<!-- Converted from reference/operator/aggregation/bitNot.txt (reStructuredText). Includes are inlined. -->

# $bitNot (expression operator)

## Definition

**New in version:** 6.3

**`$bitNot`**

Returns the result of a bitwise `not` operation on a single `int` or 
`long` value. 

## Syntax

The `$bitNot` operator has the following syntax: 

```javascript
{ $bitNot: <expression> }
```

The expression can be a single argument or an array with one `int` or `long` 
element.

## Behavior

**Note:**

All numbers in `mongosh` are doubles, not integers. To  
specify integers in `mongosh`, use the `Int32()` or the 
`Long()` constructor. To learn more, see shell-type-int or 
shell-type-long.

To learn how your MongoDB driver handles numeric values, refer to your 
`driver's documentation`.

If any arguments in the array are of a different data type such as a string, 
double, or decimal, MongoDB returns an error.

If the expression evalutates to `null`, the operation returns `null`. 

## Example

The example on this page uses the `switches` collection: 

```javascript
db.switches.insertMany( [
    { _id: 0, a: Int32(0), b: Int32(127) },
    { _id: 1, a: Int32(2), b: Int32(3) },
    { _id: 2, a: Int32(3), b: Int32(5) }
] )
```

The following aggregation uses the `$bitNot` operator in the 
`$project` stage:

```javascript
db.switches.aggregate( [
  { 
    $project: { 
      result: { 
        $bitNot: "$a"
      }
    }
  }
])
```

The operation returns the following results:

```javascript
  [
    { _id: 0, result: -1 },
    { _id: 1, result: -3 },
    { _id: 2, result: -4 }
  ]
```

## Learn More

- aggregation-pipeline-operators

- update-bit
