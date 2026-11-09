<!-- Converted from reference/operator/aggregation/setUnion.txt (reStructuredText). Includes are inlined. -->

# $setUnion (aggregation)

## Definition

**`$setUnion`**

Takes two or more arrays and returns an array containing the
elements that appear in any input array.

`$setUnion` has the following syntax:

```javascript
{ $setUnion: [ <expression1>, <expression2>, ... ] }
```

The arguments can be any valid expression as long as they each resolve to an array.
For more information on expressions, see
aggregation-expressions.

## Behavior

`$setUnion` performs set operation on arrays, treating arrays
as sets. If an array contains duplicate entries, `$setUnion`
ignores the duplicate entries. `$setUnion` ignores the order of
the elements.

`$setUnion` filters out duplicates in its result to output an
array that contain only unique entries. The order of the elements in
the output array is unspecified.

If a set contains a nested array element, `$setUnion` does *not* descend
into the nested array but evaluates the array at top-level.

| Example | Result |
|---|---|
| .. code-block:: javascript :copyable: false { $setUnion: [ [ "a", "b", "a" ], [ "b", "a" ] ] } | .. code-block:: javascript :copyable: false [ "b", "a" ] |
| .. code-block:: javascript :copyable: false { $setUnion: [ [ "a", "b" ], [ [ "a", "b" ] ] ] } | .. code-block:: javascript :copyable: false [ [ "a", "b" ], "b", "a" ] |

**Note:**

Starting in MongoDB 5.2, the sort order for `$setUnion`
is undefined. To sort an array, refer to `$sortArray`.

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

The following operation uses the `$setUnion` operator to
return an array of elements found in the `flowerFieldA` array or the
`flowerFieldB` array or both:

```javascript
db.flowers.aggregate(
   [
     { $project: { flowerFieldA:1, flowerFieldB: 1, allValues: { $setUnion: [ "$flowerFieldA", "$flowerFieldB" ] }, _id: 0 } }
   ]
)
```

The operation returns the following results:

```javascript
{ "flowerFieldA": [ "rose", "orchid" ], "flowerFieldB": [ "rose", "orchid" ], "allValues": [ "orchid", "rose" ] }
{ "flowerFieldA": [ "rose", "orchid" ], "flowerFieldB": [ "orchid", "rose", "orchid" ], "allValues": [ "orchid", "rose" ] }
{ "flowerFieldA": [ "rose", "orchid" ], "flowerFieldB": [ "rose", "orchid", "jasmine" ], "allValues": [ "orchid", "rose", "jasmine" ] }
{ "flowerFieldA": [ "rose", "orchid" ], "flowerFieldB": [ "jasmine", "rose" ], "allValues": [ "orchid", "rose", "jasmine" ] }
{ "flowerFieldA": [ "rose", "orchid" ], "flowerFieldB": [ ], "allValues": [ "orchid", "rose" ] }
{ "flowerFieldA": [ "rose", "orchid" ], "flowerFieldB": [ [ "rose" ], [ "orchid" ] ], "allValues": [ "orchid", "rose", [ "rose" ], [ "orchid" ] ] }
{ "flowerFieldA": [ "rose", "orchid" ], "flowerFieldB": [ [ "rose", "orchid" ] ], "allValues": [ "orchid", "rose", [ "rose", "orchid" ] ] }
{ "flowerFieldA": [ ], "flowerFieldB": [ ], "allValues": [ ] }
{ "flowerFieldA": [ ], "flowerFieldB": [ "rose" ], "allValues": [ "rose" ] }
```
