<!-- Converted from reference/operator/aggregation/setIntersection.txt (reStructuredText). Includes are inlined. -->

# $setIntersection (aggregation)

## Definition

**`$setIntersection`**

Takes two or more arrays and returns an array that contains the
elements that appear in every input array.

`$setIntersection` has the following syntax:

```javascript
{ $setIntersection: [ <array1>, <array2>, ... ] }
```

The arguments can be any valid expression as long as they each resolve to an array.
For more information on expressions, see
aggregation-expressions.

## Behavior

`$setIntersection` performs set operation on arrays, treating arrays
as sets. If an array contains duplicate entries, `$setIntersection`
ignores the duplicate entries. `$setIntersection` ignores the order of
the elements.

`$setIntersection` filters out duplicates in its result to output an
array that contain only unique entries. The order of the elements in
the output array is unspecified.

If no intersections are found (i.e. the input arrays contain no common
elements), `$setIntersection` returns an empty array.

If a set contains a nested array element, `$setIntersection` does *not* descend
into the nested array but evaluates the array at top-level.

| Example | Result |
|---|---|
| .. code-block:: javascript :copyable: false { $setIntersection: [ [ "a", "b", "a" ], [ "b", "a" ] ] } | .. code-block:: javascript :copyable: false [ "b", "a" ] |
| .. code-block:: javascript :copyable: false { $setIntersection: [ [ "a", "b" ], [ [ "a", "b" ] ] ] } | .. code-block:: javascript :copyable: false [ ] |

## Example

This section contains examples that show the use of `$setIntersection`
with collections.

### Elements Array Example

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

   

The following operation uses the `$setIntersection`
operator to return an array of elements common to both the `flowerFieldA`
array and the `flowerFieldB` array:

```javascript
db.flowers.aggregate(
   [
     { $project: { flowerFieldA: 1, flowerFieldB: 1, commonToBoth: { $setIntersection: [ "$flowerFieldA", "$flowerFieldB" ] }, _id: 0 } }
   ]
)
```

The operation returns the following results:

```javascript
{ "flowerFieldA" : [ "rose", "orchid" ], "flowerFieldB" : [ "rose", "orchid" ], "commonToBoth" : [ "orchid", "rose" ] }
{ "flowerFieldA" : [ "rose", "orchid" ], "flowerFieldB" : [ "orchid", "rose", "orchid" ], "commonToBoth" : [ "orchid", "rose" ] }
{ "flowerFieldA" : [ "rose", "orchid" ], "flowerFieldB" : [ "rose", "orchid", "jasmine" ], "commonToBoth" : [ "orchid", "rose" ] }
{ "flowerFieldA" : [ "rose", "orchid" ], "flowerFieldB" : [ "jasmine", "rose" ], "commonToBoth" : [ "rose" ] }
{ "flowerFieldA" : [ "rose", "orchid" ], "flowerFieldB" : [ ], "commonToBoth" : [ ] }
{ "flowerFieldA" : [ "rose", "orchid" ], "flowerFieldB" : [ [ "rose" ], [ "orchid" ] ], "commonToBoth" : [ ] }
{ "flowerFieldA" : [ "rose", "orchid" ], "flowerFieldB" : [ [ "rose", "orchid" ] ], "commonToBoth" : [ ] }
{ "flowerFieldA" : [ ], "flowerFieldB" : [ ], "commonToBoth" : [ ] }
{ "flowerFieldA" : [ ], "flowerFieldB" : [ "rose" ], "commonToBoth" : [ ] }
```
