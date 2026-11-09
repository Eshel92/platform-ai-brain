<!-- Converted from reference/operator/query/maxDistance.txt (reStructuredText). Includes are inlined. -->

# $maxDistance (query predicate operator)

## Definition

**`$maxDistance`**

The `$maxDistance` operator constrains the results of a
geospatial `$near` or `$nearSphere` query to the
specified distance. The measuring units for the maximum distance are
determined by the coordinate system in use. For GeoJSON point
objects, specify the distance in meters, not radians. You must
specify a non-negative number for `$maxDistance`.

The 2dsphere and 2d
geospatial indexes both support `$maxDistance`: .

## Example

The following example query returns documents with location values that
are `10` or fewer units from the point `[ -74 , 40 ]`.

```javascript
db.places.find( {
   loc: { $near: [ -74 , 40 ],  $maxDistance: 10 }
} )
```

MongoDB orders the results by their distance from `[ -74 , 40 ]`.
The operation returns the first 100 results, unless you modify the
query with the `cursor.limit()` method.
