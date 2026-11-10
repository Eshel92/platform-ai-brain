<!-- Converted from query-dsl/geo-queries.asciidoc (AsciiDoc). Includes are inlined. -->

## Geo queries

Elasticsearch supports two types of geo data:
`geo_point` fields which support lat/lon pairs, and
`geo_shape` fields, which support points,
lines, circles, polygons, multi-polygons, etc.

The queries in this group are:

`geo_bounding_box` query::
Finds documents with geoshapes or geopoints which intersect the specified rectangle.

`geo_distance` query::
Finds documents with geoshapes or geopoints within the specified distance of a central point.

`geo_grid` query::
Finds documents with:
* Geoshapes or geopoints which intersect the specified geohash
* Geoshapes or geopoints which intersect the specified map tile
* Geopoints which intersect the specified H3 bin

`geo_polygon` query::
Find documents with geoshapes or geopoints which intersect the specified polygon.

`geo_shape` query::
Finds documents with geoshapes or geopoints which are related to the specified geoshape.
Possible spatial relationships to specify are: intersects, contained, within and disjoint.

(See `query-dsl/geo-bounding-box-query.md`)
(See `query-dsl/geo-distance-query.md`)
(See `query-dsl/geo-grid-query.md`)
(See `query-dsl/geo-polygon-query.md`)
(See `query-dsl/geo-shape-query.md`)
