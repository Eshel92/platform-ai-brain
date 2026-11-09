<!-- Converted from reference/operator/query/geoIntersects.txt (reStructuredText). Includes are inlined. -->

# $geoIntersects

## Definition

**`$geoIntersects`**

Selects documents whose geospatial data intersects with a specified
GeoJSON object; i.e. where
the intersection of the data and the specified object is non-empty.

The `$geoIntersects` operator uses the `$geometry`
operator to specify the GeoJSON object. To specify a GeoJSON
polygons or multipolygons using the default coordinate reference
system (CRS), use the following syntax:

```javascript
{
  <location field>: {
     $geoIntersects: {
        $geometry: {
           type: "<GeoJSON object type>" ,
           coordinates: [ <coordinates> ]
        }
     }
  }
}
```

For `$geoIntersects` queries that specify GeoJSON geometries
with areas greater than a single hemisphere, the use of the default
CRS results in queries for the complementary geometries.

A complementary geometry is the smaller of two geometries. If a
specified geometry covers more than a hemisphere, the default CRS
query returns documents for the complementary geometry.

For example, if you define a geometry to be an area covering 75% of
Earth's surface, CRS uses the remaining 25% as the complementary
area. The query returns results from that smaller complementary 25%
area instead of the larger 75%.

The geointersects-examples section on this page shows how to
specify smaller and larger areas.

To specify a single-ringed GeoJSON polygon with a custom MongoDB CRS, use the following
prototype that specifies the custom MongoDB CRS in the
`$geometry` expression:

```javascript
{
  <location field>: {
     $geoIntersects: {
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
allows `$geoIntersects` to support queries with a
single-ringed GeoJSON polygon whose area is
greater than or equal to a single hemisphere. If the specified
polygon is smaller than a single hemisphere, the behavior of
`$geoIntersects` with the MongoDB CRS is the same as with the
default CRS. See also geointersects-big-poly.

**Important:**

If specifying latitude and longitude coordinates, list the
**longitude** first, and then **latitude**.

- Valid longitude values are between `-180` and `180`, both
  inclusive.

- Valid latitude values are between `-90` and `90`, both
  inclusive.

## Behavior

### Geospatial Indexes

`$geoIntersects` uses spherical geometry.
`$geoIntersects` does not require a geospatial index. However, a
geospatial index will improve query performance. Only the
2dsphere geospatial index supports
`$geoIntersects`.

### Degenerate Geometry

`$geoIntersects` does not guarantee that it will consider a
polygon to intersect with its own edges; its own vertices; or another
polygon sharing vertices or edges but no interior space.

### "Big" Polygons

For `$geoIntersects`, if you specify a single-ringed polygon that
has an area greater than a single hemisphere, include `the
custom MongoDB coordinate reference system in the $geometry` expression; otherwise, `$geoIntersects` queries for
the complementary geometry. For all other GeoJSON polygons with areas
greater than a hemisphere, `$geoIntersects` queries for the
complementary geometry.

## Examples

### Intersects a Polygon

The following example uses `$geoIntersects` to select all
`loc` data that intersect with the geojson-polygon defined by
the `coordinates` array. The area of the polygon is less than the
area of a single hemisphere:

```javascript
db.places.find(
   {
     loc: {
       $geoIntersects: {
          $geometry: {
             type: "Polygon" ,
             coordinates: [
               [ [ 0, 0 ], [ 3, 6 ], [ 6, 1 ], [ 0, 0 ] ]
             ]
          }
       }
     }
   }
)
```

For single-ringed polygons with areas greater than a single hemisphere,
see geointersects-big-polygon.

### Intersects a "Big" Polygon

To query with a single-ringed GeoJSON polygon whose area is greater
than a single hemisphere, the `$geometry` expression must
specify the custom MongoDB coordinate reference system. For example:

```javascript
db.places.find(
   {
     loc: {
       $geoIntersects: {
          $geometry: {
             type : "Polygon",
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
