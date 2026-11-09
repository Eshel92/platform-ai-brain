<!-- Converted from reference/operator/query/minDistance.txt (reStructuredText). Includes are inlined. -->

# $minDistance (query predicate operator)

## Definition

**`$minDistance`**

Filters the results of a geospatial `$near` or
`$nearSphere` query to those documents that are *at least* the
specified distance from the center point.

If `$near` or `$nearSphere` query specifies the center
point as a GeoJSON point, specify the distance
as a non-negative number in *meters*.

If `$nearSphere` query specifies the center point as
legacy coordinate pair, specify
the distance as a non-negative number in *radians*. `$near`
can only use the 2dsphere index if the query
specifies the center point as a GeoJSON point.

## Examples

### Use with `$near`

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

### Use with `$nearSphere`

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

For an example that specifies the center point as legacy coordinate
pair, see `$nearSphere`
