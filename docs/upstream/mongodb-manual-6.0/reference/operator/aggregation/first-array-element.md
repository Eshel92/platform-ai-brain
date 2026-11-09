<!-- Converted from reference/operator/aggregation/first-array-element.txt (reStructuredText). Includes are inlined. -->

# $first (array operator)

## Definition

**`$first`**

**New in version:** 4.4

Returns the first element in an array.

**Note:** Disambiguation

This page describes the `$first` array operator. For
the `$first` aggregation accumulator, see `$first
(aggregation accumulator)`.

**See also:**

`$last`

## Syntax

`$first` has the following syntax:

```javascript
{ $first: <expression> }
```

The `<expression>` can be any valid expression as long as it resolves to an array, 
null or missing. For more information on expressions, see
aggregation-expressions.

The `$first` operator is an alias for the following
`$arrayElemAt` expression:

```javascript
{ $arrayElemAt: [ <array expression>, 0 ] }
```

## Behavior

### Valid Operands

Valid operand for `$first` must resolve to an array, 
null, or missing

- If the operand resolves to a non-empty array, `$first`
  returns the first element in the array:

- If the operand resolves to an empty array `[]`,
  `$first` does not return a value.

- If the operand is null or missing, `$first` returns null.

For example, create a test collection `example1` with the following
documents:

```javascript
db.example1.insertMany([
     { "_id" : 1, "x" : [ 1, 2, 3 ] },      // Non-empty array
     { "_id" : 2, "x" : [ [ ] ] },          // Non-empty array
     { "_id" : 3, "x" : [ null ] },         // Non-empty array
     { "_id" : 4, "x" : [ ] },              // Empty array
     { "_id" : 5, "x" : null },             // Is null
     { "_id" : 6 }                          // Is Missing
])
```

Then, the following adds a new field `firstElem` whose value is
derived from applying the `$first` operator to the `x`
field:

```javascript
db.example1.aggregate([
   { $addFields: { firstElem: { $first: "$x" } } }
])
```

The operator returns the following documents:

```javascript
{ "_id" : 1, "x" : [ 1, 2, 3 ], "firstElem" : 1 }
{ "_id" : 2, "x" : [ [ ] ], "firstElem" : [ ] }
{ "_id" : 3, "x" : [ null ], "firstElem" : null }
{ "_id" : 4, "x" : [ ] }                          // No output
{ "_id" : 5, "x" : null, "firstElem" : null }
{ "_id" : 6, "firstElem" : null }
```

### Invalid Operands

If the operand does not resolve to an array, null, or missing, the
aggregation operation as a whole errors.

For example, create a test collection `example2` with the following
documents:

```javascript
db.example2.insertMany([
   { "_id" : 1, "x" : [ 1, 2, 3 ] },
   { "_id" : 2, "x" : 2 },             // x is not an array/null or missing
])
```

Then, the following aggregation operation returns an error because of
the `{ "_id" : 2, "x" : 2 }` document:

```javascript
db.example2.aggregate( { $addFields: { firstElem: { $first: "$x" } } } )
```

That is, the operation returns the following:

```javascript
2020-01-20T18:31:13.431-05:00 E  QUERY    [js] uncaught exception: Error: command failed: {
   "ok" : 0,
   "errmsg" : "$first's argument must be an array, but is double",
   "code" : 28689,
   "codeName" : "Location28689"
} : aggregate failed :
```

## Example

Create a sample collection `runninglog` with the following documents:

```javascript
db.runninglog.insertMany([
   { "_id" : 1, "team" : "Anteater", log: [ { run: 1, distance: 8 }, { run2: 2, distance: 7.5 }, { run: 3, distance: 9.2 } ] },
   { "_id" : 2, "team" : "Bears", log: [ { run: 1, distance: 18 }, { run2: 2, distance: 17 }, { run: 3, distance: 16 } ] },
   { "_id" : 3, "team" : "Cobras", log: [ { run: 1, distance: 2 } ] }
])
```

The following aggregation uses the `$first` and
`$last` operator on the `log` array to retrieve the
information for the first run and the last run:

```javascript
db.runninglog.aggregate([
   { $addFields: { firstrun: { $first: "$log" }, lastrun: { $last: "$log" } } }
])
```

The operation returns the following results:

```javascript
{ "_id" : 1, "team" : "Anteater", "log" : [ { "run" : 1, "distance" : 8 }, { "run2" : 2, "distance" : 7.5 }, { "run" : 3, "distance" : 9.2 } ],
      "firstrun" : { "run" : 1, "distance" : 8 }, "lastrun" : { "run" : 3, "distance" : 9.2 } }
{ "_id" : 2, "team" : "Bears", "log" : [ { "run" : 1, "distance" : 18 }, { "run2" : 2, "distance" : 17 }, { "run" : 3, "distance" : 16 } ],
      "firstrun" : { "run" : 1, "distance" : 18 }, "lastrun" : { "run" : 3, "distance" : 16 } }
{ "_id" : 3, "team" : "Cobras", "log" : [ { "run" : 1, "distance" : 2 } ],
      "firstrun" : { "run" : 1, "distance" : 2 }, "lastrun" : { "run" : 1, "distance" : 2 } }
```

   
To calculate the change between the first and the last distances, the
following operation uses `$cond` and `$size`
operators to calculate the difference (i.e. `$subtract`)
the two distances if there are two or more elements in the `log`
array:

```javascript
db.runninglog.aggregate([
  { $addFields: { firstrun: { $first: "$log" }, lastrun: { $last: "$log" } } },
  { $project: { team: 1, progress: 
      {
        $cond: { 
           if: { $gt: [ { $size:"$log" }, 1 ] } , 
           then: { $subtract: [ "$lastrun.distance", "$firstrun.distance"] }, 
           else: "Not enough data." }
      }

  }}
])
```

The operation returns the following documents:

```javascript
{ "_id" : 1, "team" : "Anteater", "progress" : 1.1999999999999993 }
{ "_id" : 2, "team" : "Bears", "progress" : -2 }
{ "_id" : 3, "team" : "Cobras", "progress" : "Not enough data." }
```

By default, `mongosh` uses the 64-bit floating-point
double for numbers. To improve precision, you can use shell-type-decimal
instead.

## See Also

- `$last`

- `$arrayElemAt`

- `$slice`

- agg-quick-ref-operator-array
