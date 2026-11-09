<!-- Converted from reference/operator/query/centerSphere.txt (reStructuredText). Includes are inlined. -->

# $centerSphere (query predicate operator)

## Definition

**`$centerSphere`**

Defines a circle for a geospatial query that uses spherical
geometry. The query returns documents that are within the bounds of
the circle. You can use the `$centerSphere` operator on both
GeoJSON objects and legacy coordinate pairs.

To use `$centerSphere`, specify an array that contains:

- The grid coordinates of the circle's center point, and

- The circle's radius measured in radians. To calculate radians, see
  calculate-distance-spherical-geometry.

```javascript
{
   <location field>: {
      $geoWithin: { $centerSphere: [ [ <x>, <y> ], <radius> ] }
   }
}
```

**Important:**

If you use longitude and latitude, specify **longitude first**.

## Behavior

Applications can use `$centerSphere` *without* having a geospatial index.
However, geospatial indexes support much faster queries than the
unindexed equivalents.

Both 2dsphere and 2d
geospatial indexes support `$centerSphere`.

## Example

The following example queries grid coordinates and returns all
documents within a 10 mile radius of longitude `88 W` and latitude
`30 N`. The query converts the distance to radians by dividing by the
approximate equatorial radius of the earth, 3963.2 miles:

```javascript
db.places.find( {
  loc: { $geoWithin: { $centerSphere: [ [ -88, 30 ], 10/3963.2 ] } }
} )
```
