<!-- Converted from reference/operator/query/box.txt (reStructuredText). Includes are inlined. -->

# $box

## Definition

**`$box`**

Specifies a rectangle for a geospatial `$geoWithin`
query to return documents that are within the bounds of the
rectangle, according to their point-based location data. When used
with the `$box` operator, `$geoWithin` returns
documents based on grid coordinates and does *not* query
for GeoJSON shapes.

To use the `$box` operator, you must specify the bottom
left and top right corners of the rectangle in an array object:

```javascript
{
  <location field>: {
     $geoWithin: {
        $box: [
          [ <bottom left coordinates> ],
          [ <upper right coordinates> ]
        ]
     }
  }
}
```

**Important:**

If you use longitude and latitude, specify **longitude first**.

## Behavior

The query calculates distances using flat (planar) geometry.

Applications can use `$box` *without* having a geospatial index.
However, geospatial indexes support much faster queries than the
unindexed equivalents.

Only the 2d geospatial index supports `$box`.

## Example

The following example query returns all documents that are within the
box having points at: `[ 0 , 0 ]`, `[ 0 , 100 ]`, `[ 100 , 0 ]`,
and `[ 100 , 100 ]`.

```javascript
db.places.find( {
   loc: { $geoWithin: { $box:  [ [ 0, 0 ], [ 100, 100 ] ] } }
} )
```
