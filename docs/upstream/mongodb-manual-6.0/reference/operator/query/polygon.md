<!-- Converted from reference/operator/query/polygon.txt (reStructuredText). Includes are inlined. -->

# $polygon

## Definition

**`$polygon`**

Specifies a polygon for a
geospatial `$geoWithin` query on legacy coordinate
pairs. The query returns pairs that are within the bounds of the
polygon. The operator does *not* query for GeoJSON objects.

To define the polygon, specify an array of coordinate points:

```javascript
{
   <location field>: {
      $geoWithin: {
         $polygon: [ [ <x1> , <y1> ], [ <x2> , <y2> ], [ <x3> , <y3> ], ... ]
      }
   }
}
```

The last point is always implicitly connected to the first. You can
specify as many points, i.e. sides, as you like.

**Important:**

If you use longitude and latitude, specify **longitude first**.

## Behavior

The `$polygon` operator calculates distances using flat (planar)
geometry.

Applications can use `$polygon` *without* having a geospatial index.
However, geospatial indexes support much faster queries than the
unindexed equivalents.

Only the 2d geospatial index supports the
`$polygon` operator.

## Example

The following query returns all documents that have coordinates that
exist within the polygon defined by `[ 0 , 0 ]`, `[ 3 , 6 ]`, and
`[ 6 , 0 ]`:

```javascript
db.places.find(
  {
     loc: {
       $geoWithin: { $polygon: [ [ 0 , 0 ], [ 3 , 6 ], [ 6 , 0 ] ] }
     }
  }
)
```
