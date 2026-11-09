<!-- Converted from reference/operator/aggregation/mod.txt (reStructuredText). Includes are inlined. -->

# $mod (expression operator)

## Definition

**`$mod`**

Divides one number by another and returns the *remainder*.

## Syntax

The `$mod` expression has the following syntax:

```javascript
{ $mod: [ <expression1>, <expression2> ] }
```

The first argument is the dividend, and the second argument is the
divisor. That is, the first argument is divided by the second 
argument.

## Behavior

The arguments can be any valid expression as long as they resolve to numbers. For
more information on expressions, see aggregation-expressions.

Starting in version 7.2, the output data type of the `$mod` operator is
the larger of the two input data types.

**Note:**

Prior to version 7.2, the value and field type of inputs determine
the `$mod` output type if:

- The divisor is type `double` but has an integer value. 
- The dividend is type `int` or `long`.

In this case, MongoDB converts the divisor to the dividend data
type before it performs the `$mod` operation. The output data type
is the dividend data type.

### Negative Dividend

When the dividend is negative, the remainder is also negative. For
more details on this behavior, see the [official JavaScript documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Remainder#description).

For an example, see mod-negative-dividend-example.
      

## Example

Consider a `conferencePlanning` collection with the following documents:

```javascript
db.conferencePlanning.insertMany( [
   { "_id" : 1, "city" : "New York", "hours" : 80, "tasks" : 7 },
   { "_id" : 2, "city" : "Singapore", "hours" : 40, "tasks" : 4 }
] )
```

The following aggregation uses the `$mod` expression to
return the remainder of the `hours` field divided by the `tasks`
field:

```javascript
db.conferencePlanning.aggregate( [
  { $project: { remainder: { $mod: [ "$hours", "$tasks" ] } } }
] )
```

The operation returns the following results:

```json
[
  { '_id' : 1, 'remainder' : 3 },
  { '_id' : 2, 'remainder' : 0 }
]
```

### Negative Dividend

Consider a `modExample` collection that contains the following 
document:

```javascript
db.modExample.insertOne( [
   { "_id" : 1, "dividend": -13, "divisor": 9 }
] )
```

This aggregation uses the `$mod` expression to return the remainder of
`dividend` divided by the `divisor` field:

```javascript
db.modExample.aggregate( [
  { $project: { remainder: { $mod: [ "$dividend", "$divisor" ] } } }
] )
```

The operation returns the following results:

```json
[ { '_id' : 1, 'remainder' : -4 } ]
```
