<!-- Converted from reference/operator/query/geoWithin.txt (reStructuredText). Includes are inlined. -->

# $geoWithin (query predicate operator)

## Definition

**`$geoWithin`**

Selects documents with geospatial data that exists entirely
within a specified shape.

The specified shape can be either a GeoJSON geojson-polygon
(either single-ringed or multi-ringed), a GeoJSON
geojson-multipolygon, or a shape defined by legacy coordinate
pairs. The `$geoWithin` operator uses the `$geometry`
operator to specify the GeoJSON object.

To specify a GeoJSON polygons or multipolygons using the default
coordinate reference system (CRS), use the following syntax:

```javascript
{
   <location field>: {
      $geoWithin: {
         $geometry: {
            type: <"Polygon" or "MultiPolygon"> ,
            coordinates: [ <coordinates> ]
         }
      }
   }
}
```

For `$geoWithin` queries that specify GeoJSON geometries with
areas greater than a single hemisphere, the use of the default CRS
results in queries for the complementary geometries.

To specify a single-ringed GeoJSON polygon with a custom MongoDB CRS, use the following
prototype that specifies the custom MongoDB CRS in the
`$geometry` expression:

```javascript
{
   <location field>: {
      $geoWithin: {
         $geometry: {
           type: "Polygon" ,
           coordinates: [ <coordinates> ],
           crs: {
              type: "name",
              properties: { name: "urn:x-mongodb:crs:strictwinding:EPSG:4326" }
           }
         }
      }
   }
}
```

The custom MongoDB CRS uses a counter-clockwise winding order and
allows `$geoWithin` to support queries with a single-ringed
GeoJSON polygon whose area is greater than
or equal to a single hemisphere. If the specified polygon is smaller
than a single hemisphere, the behavior of `$geoWithin` with
the MongoDB CRS is the same as with the default CRS. See also
geowithin-big-poly.

If querying for inclusion in a shape defined by legacy coordinate
pairs on a plane, use the following syntax:

```javascript
{
   <location field>: {
      $geoWithin: { <shape operator>: <coordinates> }
   }
}
```

The available shape operators are:

- `$box`,
- `$polygon`,
- `$center` (defines a circle), and
- `$centerSphere` (defines a circle on a sphere).

**Important:**

If you use longitude and latitude, specify coordinates in order
of `longitude, latitude`.

## Behavior

### Geospatial Indexes

`$geoWithin` does not require a geospatial index. However, a
geospatial index will improve query performance. Both 2dsphere and 2d geospatial indexes support
`$geoWithin`.

### Unsorted Results

The `$geoWithin` operator does not return sorted results. As
such, MongoDB can return `$geoWithin` queries more quickly than
geospatial `$near` or `$nearSphere` queries, which sort
results.

### Degenerate Geometry

`$geoWithin` does not guarantee that it will consider a piece of
geometry to contain its component geometry, or another polygon sharing
its component geometry.

### "Big" Polygons

For `$geoWithin`, if you specify a single-ringed polygon that
has an area greater than a single hemisphere, include the custom MongoDB
coordinate reference system in the `$geometry`
expression. Otherwise, `$geoWithin` queries for the
complementary geometry. For all other GeoJSON polygons with areas
greater than a hemisphere, `$geoWithin` queries for the
complementary geometry.

## Examples

### Within a Polygon

The following example selects all `loc` data that exist entirely
within a GeoJSON geojson-polygon. The area of the polygon is
less than the area of a single hemisphere:

```javascript
db.places.find(
   {
     loc: {
       $geoWithin: {
          $geometry: {
             type : "Polygon" ,
             coordinates: [ [ [ 0, 0 ], [ 3, 6 ], [ 6, 1 ], [ 0, 0 ] ] ]
          }
       }
     }
   }
)
```

For single-ringed polygons with areas greater than a single hemisphere,
see geowithin-big-polygon.

### Within a "Big" Polygon

To query with a single-ringed GeoJSON polygon whose area is greater
than a single hemisphere, the `$geometry` expression must
specify the custom MongoDB coordinate reference system. For example:

```javascript
db.places.find(
   {
     loc: {
       $geoWithin: {
          $geometry: {
             type : "Polygon" ,
             coordinates: [
               [
                 [ -100, 60 ], [ -100, 0 ], [ -100, -60 ], [ 100, -60 ], [ 100, 60 ], [ -100, 60 ]
               ]
             ],
             crs: {
                type: "name",
                properties: { name: "urn:x-mongodb:crs:strictwinding:EPSG:4326" }
             }
          }
       }
     }
   }
)
```
