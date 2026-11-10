<!-- Converted from query-dsl/shape-queries.asciidoc (AsciiDoc). Includes are inlined. -->

## Shape queries

Like `geo_shape` Elasticsearch supports the ability to index
arbitrary two dimension (non Geospatial) geometries making it possible to
map out virtual worlds, sporting venues, theme parks, and CAD diagrams.

Elasticsearch supports two types of cartesian data:
`point` fields which support x/y pairs, and
`shape` fields, which support points, lines, circles, polygons, multi-polygons, etc.

The queries in this group are:

`shape` query::
Finds documents with:
* `shapes` which either intersect, are contained by, are within or do not intersect
with the specified shape
* `points` which intersect the specified shape

(See `query-dsl/shape-query.md`)
