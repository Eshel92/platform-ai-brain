<!-- Converted from reference/operator/query-geospatial.txt (reStructuredText). Includes are inlined. -->

# Geospatial Query Operators

Geospatial operators return data based on geospatial expression 
conditions.

**Note:**

For details on a specific operator, including syntax and examples,
click on the link to the operator's reference page.

## Operators

### Query Selectors

| Name | Description |
|---|---|
| `$geoIntersects` | Selects geometries that intersect with a GeoJSON geometry. The 2dsphere index supports `$geoIntersects`. |
| `$geoWithin` | Selects geometries within a bounding GeoJSON geometry. The 2dsphere and 2d indexes support `$geoWithin`. |
| `$near` | Returns geospatial objects in proximity to a point. Requires a geospatial index.  The 2dsphere and 2d indexes support `$near`. |
| `$nearSphere` | Returns geospatial objects in proximity to a point on a sphere. Requires a geospatial index.  The 2dsphere and 2d indexes support `$nearSphere`. |

   

### Geometry Specifiers

| Name | Description |
|---|---|
| `$box` | Specifies a rectangular box using legacy coordinate pairs for `$geoWithin` queries. The 2d index supports `$box`. |
| `$center` | Specifies a circle using legacy coordinate pairs to `$geoWithin` queries when using planar geometry. The 2d index supports `$center`. |
| `$centerSphere` | Specifies a circle using either legacy coordinate pairs or GeoJSON format for `$geoWithin` queries when using spherical geometry. The 2dsphere and 2d indexes support `$centerSphere`. |
| `$geometry` | Specifies a geometry in GeoJSON format to geospatial query operators. |
| `$maxDistance` | Specifies a maximum distance to limit the results of `$near` and `$nearSphere` queries. The 2dsphere and 2d indexes support `$maxDistance`. |
| `$minDistance` | Specifies a minimum distance to limit the results of `$near` and `$nearSphere` queries. For use with `2dsphere` index only. |
| `$polygon` | Specifies a polygon to using legacy coordinate pairs for `$geoWithin` queries. The `2d` index supports `$polygon`. |
