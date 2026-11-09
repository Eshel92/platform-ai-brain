<!-- Converted from reference/operator/query/near.txt (reStructuredText). Includes are inlined. -->

# $near

## Definition

**`$near`**

Specifies a point for which a geospatial query returns the
documents from nearest to farthest. The `$near` operator can
specify either a GeoJSON point or legacy coordinate point.

`$near` requires a geospatial index:

- 2dsphere index if specifying a
  GeoJSON point,

- 2d index if specifying a point using legacy
  coordinates.

To specify a GeoJSON point, `$near` operator requires
a 2dsphere index and has the following
syntax:

```javascript
{
   <location field>: {
     $near: {
       $geometry: {
          type: "Point" ,
          coordinates: [ <longitude> , <latitude> ]
       },
       $maxDistance: <distance in meters>,
       $minDistance: <distance in meters>
     }
   }
}
```

**Important:**

If specifying latitude and longitude coordinates, list the
**longitude** first, and then **latitude**.

- Valid longitude values are between `-180` and `180`, both
  inclusive.

- Valid latitude values are between `-90` and `90`, both
  inclusive.

When specifying a GeoJSON point, you can use the *optional*
`$minDistance` and `$maxDistance` specifications to
limit the `$near` results by distance in *meters*:

- `$minDistance` limits the results to those documents that
  are *at least* the specified distance from the center point.

- `$maxDistance` limits the results to those documents that
  are *at most* the specified distance from the center point.

To specify a point using legacy coordinates, `$near` requires
a 2d index and has the following syntax:

```javascript
{
  $near: [ <x>, <y> ],
  $maxDistance: <distance in radians>
}
```

When specifying a legacy coordinate, you can use the *optional*
`$maxDistance` specification to limit the `$near`
results by distance in *radians*. `$maxDistance` limits the
results to those documents that are *at most* the specified distance
from the center point.

## Behavior

### Special Indexes Restriction

You cannot combine the `$near` operator, which requires a
special geospatial index, with a
query operator or command that requires another special index. For
example you cannot combine `$near` with the `$text`
query.

### Sort Operation

The `$near` operator sorts documents by distance.

- If you use the `sort` method in your query,
  MongoDB performs a second sort operation, re-ordering the matching
  documents.  When querying large collections, this can negatively 
  affect query performance.

- If the order of the documents is not important to you, consider
  using the `$geoWithin` operator instead, as it returns 
  unsorted results.

- `$near` is a Match Execution operator and is not
  permitted in aggregation pipelines.

## Examples

### Query on GeoJSON Data

**Important:**

If specifying latitude and longitude coordinates, list the
**longitude** first, and then **latitude**.

- Valid longitude values are between `-180` and `180`, both
  inclusive.

- Valid latitude values are between `-90` and `90`, both
  inclusive.

Consider a collection `places` that has a `2dsphere` index.

The following example returns documents that are at least `1000`
meters from and at most `5000` meters from the specified GeoJSON
point, sorted from nearest to farthest:

```javascript
db.places.find(
   {
     location:
       { $near :
          {
            $geometry: { type: "Point",  coordinates: [ -73.9667, 40.78 ] },
            $minDistance: 1000,
            $maxDistance: 5000
          }
       }
   }
)
```

### Query on Legacy Coordinates

**Important:**

If specifying latitude and longitude coordinates, list the
**longitude** first, and then **latitude**.

- Valid longitude values are between `-180` and `180`, both
  inclusive.

- Valid latitude values are between `-90` and `90`, both
  inclusive.

Consider a collection `legacy2d` that has a `2d` index.

The following example returns documents that are at most `0.10`
radians from the specified legacy coordinate pair, sorted from nearest
to farthest:

```javascript
db.legacy2d.find(
   { location : { $near : [ -73.9667, 40.78 ], $maxDistance: 0.10 } }
)
```
