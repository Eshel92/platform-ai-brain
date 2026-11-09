<!-- Converted from reference/operator/query/center.txt (reStructuredText). Includes are inlined. -->

# $center

## Definition

**`$center`**

The `$center` operator specifies a circle for a
`$geoWithin` query. The query returns legacy coordinate pairs
that are within the bounds of the circle. The operator does *not*
return GeoJSON objects.

To use the `$center` operator, specify an array that
contains:

- The grid coordinates of the circle's center point, and

- The circle's radius, as measured in the units used by the
  coordinate system.

```javascript
{
   <location field>: {
      $geoWithin: { $center: [ [ <x>, <y> ] , <radius> ] }
   }
}
```

**Important:**

If you use longitude and latitude, specify **longitude first**.

## Behavior

The query calculates distances using flat (planar) geometry.

Applications can use `$center` *without* having a geospatial index.
However, geospatial indexes support much faster queries than the
unindexed equivalents.

Only the 2d geospatial index supports
`$center`.

## Example

The following example query returns all documents that have coordinates
that exist within the circle centered on `[ -74, 40.74 ]` and with a
radius of `10`:

```javascript
db.places.find(
   { loc: { $geoWithin: { $center: [ [-74, 40.74], 10 ] } } }
)
```
