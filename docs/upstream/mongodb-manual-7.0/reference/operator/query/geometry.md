<!-- Converted from reference/operator/query/geometry.txt (reStructuredText). Includes are inlined. -->

# $geometry (query predicate operator)

**`$geometry`**

The `$geometry` operator specifies a GeoJSON geometry
for use with the following geospatial query operators:
`$geoWithin`, `$geoIntersects`, `$near`, and
`$nearSphere`. `$geometry` uses `EPSG:4326` as the
default coordinate reference system (CRS).

To specify GeoJSON objects with the default CRS, use the following
prototype for `$geometry`:

```javascript
$geometry: {
   type: "<GeoJSON object type>",
   coordinates: [ <coordinates> ]
}
```

To specify a single-ringed GeoJSON polygon with a custom MongoDB CRS, use the following
prototype (available only for `$geoWithin` and
`$geoIntersects`):

```javascript
$geometry: {
   type: "Polygon",
   coordinates: [ <coordinates> ],
   crs: {
      type: "name",
      properties: { name: "urn:x-mongodb:crs:strictwinding:EPSG:4326" }
   }
}
```

The custom MongoDB coordinate reference system has a strict
counter-clockwise winding order.

**Important:**

If specifying latitude and longitude coordinates, list the
**longitude** first, and then **latitude**.

- Valid longitude values are between `-180` and `180`, both
  inclusive.

- Valid latitude values are between `-90` and `90`, both
  inclusive.
