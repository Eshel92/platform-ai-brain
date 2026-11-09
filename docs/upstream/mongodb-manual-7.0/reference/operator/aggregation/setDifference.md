<!-- Converted from reference/operator/aggregation/setDifference.txt (reStructuredText). Includes are inlined. -->

# $setDifference  (expression operator)

## Definition

**`$setDifference`**

Takes two sets and returns an array containing the elements that
only exist in the first set; i.e. performs a [relative complement](http://en.wikipedia.org/wiki/Complement_(set_theory)) of the
second set relative to the first.

`$setDifference` has the following syntax:

```javascript
{ $setDifference: [ <expression1>, <expression2> ] }
```

The arguments can be any valid expression as long as they each resolve to an array.
For more information on expressions, see
aggregation-expressions.

## Behavior

`$setDifference` performs set operation on arrays, treating arrays
as sets. If an array contains duplicate entries, `$setDifference`
ignores the duplicate entries. `$setDifference` ignores the order of
the elements.

`$setDifference` filters out duplicates in its result to output an
array that contain only unique entries. The order of the elements in
the output array is unspecified.

If a set contains a nested array element, `$setDifference` does *not* descend
into the nested array but evaluates the array at top-level.

| Example | Result |
|---|---|
| .. code-block:: javascript :copyable: false { $setDifference: [ [ "a", "b", "a" ], [ "b", "a" ] ] } | .. code-block:: javascript :copyable: false [ ] |
| .. code-block:: javascript :copyable: false { $setDifference: [ [ "a", "b" ], [ [ "a", "b" ] ] ] } | .. code-block:: javascript :copyable: false [ "a", "b" ] |

## Example

Consider an `flowers` collection with the following documents:

```javascript
db.flowers.insertMany( [
   { "_id" : 1, "flowerFieldA" : [ "rose", "orchid" ], "flowerFieldB" : [ "rose", "orchid" ] },
   { "_id" : 2, "flowerFieldA" : [ "rose", "orchid" ], "flowerFieldB" : [ "orchid", "rose", "orchid" ] },
   { "_id" : 3, "flowerFieldA" : [ "rose", "orchid" ], "flowerFieldB" : [ "rose", "orchid", "jasmine" ] },
   { "_id" : 4, "flowerFieldA" : [ "rose", "orchid" ], "flowerFieldB" : [ "jasmine", "rose" ] },
   { "_id" : 5, "flowerFieldA" : [ "rose", "orchid" ], "flowerFieldB" : [ ] },
   { "_id" : 6, "flowerFieldA" : [ "rose", "orchid" ], "flowerFieldB" : [ [ "rose" ], [ "orchid" ] ] },
   { "_id" : 7, "flowerFieldA" : [ "rose", "orchid" ], "flowerFieldB" : [ [ "rose", "orchid" ] ] },
   { "_id" : 8, "flowerFieldA" : [ ], "flowerFieldB" : [ ] },
   { "_id" : 9, "flowerFieldA" : [ ], "flowerFieldB" : [ "rose" ] }
] ) 
```

The following operation uses the `$setDifference` operator
to return an array of elements found in the `flowerFieldB` array but *not*
in the `flowerFieldA` array:

```javascript
db.flowers.aggregate(
   [
     { $project: { flowerFieldA: 1, flowerFieldB: 1, inBOnly: { $setDifference: [ "$flowerFieldB", "$flowerFieldA" ] }, _id: 0 } }
   ]
)
```

The operation returns the following results:

```javascript
{ "flowerFieldA" : [ "rose", "orchid" ], "flowerFieldB" : [ "rose", "orchid" ], "inBOnly" : [ ] }
{ "flowerFieldA" : [ "rose", "orchid" ], "flowerFieldB" : [ "orchid", "rose", "orchid" ], "inBOnly" : [ ] }
{ "flowerFieldA" : [ "rose", "orchid" ], "flowerFieldB" : [ "rose", "orchid", "jasmine" ], "inBOnly" : [ "jasmine" ] }
{ "flowerFieldA" : [ "rose", "orchid" ], "flowerFieldB" : [ "jasmine", "rose" ], "inBOnly" : [ "jasmine" ] }
{ "flowerFieldA" : [ "rose", "orchid" ], "flowerFieldB" : [ ], "inBOnly" : [ ] }
{ "flowerFieldA" : [ "rose", "orchid" ], "flowerFieldB" : [ [ "rose" ], [ "orchid" ] ], "inBOnly" : [ [ "rose" ], [ "orchid" ] ] }
{ "flowerFieldA" : [ "rose", "orchid" ], "flowerFieldB" : [ [ "rose", "orchid" ] ], "inBOnly" : [ [ "rose", "orchid" ] ] }
{ "flowerFieldA" : [ ], "flowerFieldB" : [ ], "inBOnly" : [ ] }
{ "flowerFieldA" : [ ], "flowerFieldB" : [ "rose" ], "inBOnly" : [ "rose" ] }
```
