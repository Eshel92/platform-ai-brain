<!-- Converted from tutorial/calculate-distances-using-spherical-geometry-with-2d-geospatial-indexes.txt (reStructuredText). Includes are inlined. -->

# Calculate Distance Using Spherical Geometry

**Warning:**

For spherical queries, use the `2dsphere` index result.

The use of `2d` index for spherical queries may lead to incorrect
results, such as the use of the `2d` index for spherical queries
that wrap around the poles.

The `2d` index supports queries that calculate distances on a
Euclidean plane (flat surface). The index also supports the following
query operators and command that calculate distances using spherical
geometry:

**Note:** While basic queries using spherical distance are supported by

the `2d` index, consider moving to a `2dsphere` index if your
data is primarily longitude and latitude.

- `$nearSphere`

- `$centerSphere`

- `$near`

- `$geoNear` pipeline stage with the `spherical: true` option

**Important:** The aforementioned operations use radians for distance. Other

spherical query operators do not, such as `$geoWithin`.

For spherical query operators to function properly, you must convert
distances to radians, and convert from radians to the distances units
used by your application.

To convert:

- *distance to radians*: divide the distance by the radius of the
  sphere (e.g. the Earth) in the same units as the distance
  measurement.

- *radians to distance*: multiply the radian measure by the radius
  of the sphere (e.g. the Earth) in the units system that you want to
  convert the distance to.

The equatorial radius of the Earth is approximately `3,963.2`
miles or `6,378.1` kilometers.

The following query would return documents from the `places`
collection within the circle described by the center `[ -74, 40.74 ]`
with a radius of `100` miles:

```javascript
db.places.find( { loc: { $geoWithin: { $centerSphere: [ [ -74, 40.74 ] ,
                                                     100 / 3963.2 ] } } } )
```

**Note:**

**Important:**

If specifying latitude and longitude coordinates, list the
**longitude** first, and then **latitude**.

- Valid longitude values are between `-180` and `180`, both
  inclusive.

- Valid latitude values are between `-90` and `90`, both
  inclusive.
