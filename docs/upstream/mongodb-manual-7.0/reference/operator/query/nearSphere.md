<!-- Converted from reference/operator/query/nearSphere.txt (reStructuredText). Includes are inlined. -->

# $nearSphere (query predicate operator)

## Definition

**`$nearSphere`**

Specifies a point for which a geospatial query returns the
documents from nearest to farthest. MongoDB calculates distances for
`$nearSphere` using spherical geometry.

`$nearSphere` *requires* a geospatial index:

- 2dsphere index for location data defined
  as GeoJSON points.

- 2d index for location data defined as legacy
  coordinate pairs. To use a `2d` index on
  GeoJSON points, create the index on the
  `coordinates` field of the GeoJSON object.

The `$nearSphere` operator can specify either a
GeoJSON point or legacy coordinate point.

To specify a GeoJSON Point, use the following
syntax:

```javascript
{
  $nearSphere: {
     $geometry: {
        type : "Point",
        coordinates : [ <longitude>, <latitude> ]
     },
     $minDistance: <distance in meters>,
     $maxDistance: <distance in meters>
  }
}
```

- The *optional* `$minDistance` limits the results to those
  documents that are *at least* the specified distance from the
  center point.

- The *optional* `$maxDistance` is available for either index.

To specify a point using legacy coordinates, use the following
syntax:

```javascript
{
  $nearSphere: [ <x>, <y> ],
  $minDistance: <distance in radians>,
  $maxDistance: <distance in radians>
}
```

- The *optional* `$minDistance` is available only if the
  query uses the 2dsphere index.
  `$minDistance` limits the results to those documents that
  are *at least* the specified distance from the center point.

- The *optional* `$maxDistance` is available for either index.

If you use longitude and latitude for legacy coordinates, specify
the longitude first, then latitude.

## Behavior

### Special Indexes Restriction

You cannot combine the `$nearSphere` operator, which requires a
special geospatial index, with a
query operator or command that requires another special index. For
example you cannot combine `$nearSphere` with the `$text`
query.

### Sort Operation

The `$nearSphere` operator sorts documents by distance.

- If you use the `sort` method in your query,
  MongoDB performs a second sort operation, re-ordering the matching
  documents.  When querying large collections, this can negatively 
  affect query performance.

- If the order of the documents is not important to you, consider
  using the `$geoWithin` operator instead, as it returns 
  unsorted results.

- `$nearSphere` is a Match Execution operator and is not
  permitted in aggregation pipelines.

## Examples

### Specify Center Point Using GeoJSON

Consider a collection `places` that contains documents with a
`location` field and has a 2dsphere index.

Then, the following example returns whose `location` is at least
`1000` meters from and at most `5000` meters from the specified
point, ordered from nearest to farthest:

```javascript
db.places.find(
   {
     location: {
        $nearSphere: {
           $geometry: {
              type : "Point",
              coordinates : [ -73.9667, 40.78 ]
           },
           $minDistance: 1000,
           $maxDistance: 5000
        }
     }
   }
)
```

### Specify Center Point Using Legacy Coordinates

#### `2d` Index

Consider a collection `legacyPlaces` that contains documents with
legacy coordinates pairs in the `location` field and has a 2d index.

Then, the following example returns those documents whose `location`
is at most `0.10` radians from the specified point, ordered from
nearest to farthest:

```javascript
db.legacyPlaces.find(
   { location : { $nearSphere : [ -73.9667, 40.78 ], $maxDistance: 0.10 } }
)
```

#### `2dsphere` Index

If the collection has a `2dsphere` index instead, you can also
specify the optional `$minDistance` specification. For example,
the following example returns the documents whose `location` is at
least `0.0004` radians from the specified point, ordered from nearest
to farthest:

```javascript
db.legacyPlaces.find(
   { location : { $nearSphere : [ -73.9667, 40.78 ], $minDistance: 0.0004 } }
)
```
