<!-- Converted from mapping/types/geo-shape.asciidoc (AsciiDoc). Includes are inlined. -->

### Geoshape field type

The `geo_shape` data type facilitates the indexing of and searching
with arbitrary geoshapes such as rectangles, lines and polygons. If the data being
indexed contains shapes other than just points, it is necessary to use this mapping.
If the data contains only points, it can be indexed as either
`geo_point` or `geo_shape`.

Documents using this type can be used:

* to find geoshapes within:
** a bounding box
** a certain distance of a central point
** a `geo_shape` query (for example, intersecting polygons).
* to aggregate documents by geographic grids:
** either `geo_hash`
** or `geo_tile`
** or `geo_hex`

#### Mapping Options

The `geo_shape` mapping maps GeoJSON or WKT geometry objects to the `geo_shape`
type. To enable it, users must explicitly map fields to the `geo_shape`
type.

=============================================
In [GeoJSON](https://datatracker.ietf.org/doc/html/rfc7946)
and [WKT](https://www.ogc.org/standard/sfa/), and therefore Elasticsearch,
the correct *coordinate order is longitude, latitude (X, Y)* within coordinate
arrays. This differs from many Geospatial APIs (e.g., Google Maps) that generally
use the colloquial latitude, longitude (Y, X).
=============================================

|=======================================================================
|Option |Description| Default

|`orientation`
a|Optional. Default orientation for the field's
WKT polygons.

This parameter sets and returns only a `RIGHT` (counterclockwise) or `LEFT`
(clockwise) value. However, you can specify either value in multiple ways.

To set `RIGHT`, use one of the following arguments or its uppercase
variant:

* `right`
* `counterclockwise`
* `ccw`

To set `LEFT`, use one of the following arguments or its uppercase
variant:

* `left`
* `clockwise`
* `cw`
| `RIGHT`

|`ignore_malformed` |If true, malformed GeoJSON or WKT shapes are ignored. If
false (default), malformed GeoJSON and WKT shapes throw an exception and reject the
entire document.
| `false`

|`ignore_z_value` |If `true` (default) three dimension points will be accepted (stored in source)
but only latitude and longitude values will be indexed; the third dimension is ignored. If `false`,
geopoints containing any more than latitude and longitude (two dimensions) values throw an exception
and reject the whole document.
| `true`

|`coerce` |If `true` unclosed linear rings in polygons will be automatically closed.
| `false`

|`index` |Should the field be quickly searchable? Accepts `true` (default) and `false`.
Fields that only have `doc_values` enabled can still be queried, albeit slower.
| `true`

|`doc_values` |Should the field be stored on disk in a column-stride fashion,
so that it can later be used for aggregations or scripting?
| `true`

|=======================================================================

#### Indexing approach

Geoshape types are indexed by decomposing the shape into a triangular mesh and
indexing each triangle as a 7 dimension point in a BKD tree. This provides
near perfect spatial resolution (down to 1e-7 decimal degree precision) since all
spatial relations are computed using an encoded vector representation of the
original shape. Performance of the tessellator primarily
depends on the number of vertices that define the polygon/multi-polygon.

##### Example

```console
PUT /example
{
  "mappings": {
    "properties": {
      "location": {
        "type": "geo_shape"
      }
    }
  }
}
```

#### Input Structure

Shapes can be represented using either the [GeoJSON](http://geojson.org)
or [Well-Known Text](https://docs.opengeospatial.org/is/12-063r5/12-063r5.html)
(WKT) format. The following table provides a mapping of GeoJSON and WKT
to Elasticsearch types:

|=======================================================================
|GeoJSON Type |WKT Type |Elasticsearch Type |Description

|`Point` |`POINT` |`point` |A single geographic coordinate. Note: Elasticsearch uses WGS-84 coordinates only.
|`LineString` |`LINESTRING` |`linestring` |An arbitrary line given two or more points.
|`Polygon` |`POLYGON` |`polygon` |A _closed_ polygon whose first and last point
must match, thus requiring `n + 1` vertices to create an `n`-sided
polygon and a minimum of `4` vertices.
|`MultiPoint` |`MULTIPOINT` |`multipoint` |An array of unconnected, but likely related
points.
|`MultiLineString` |`MULTILINESTRING` |`multilinestring` |An array of separate linestrings.
|`MultiPolygon` |`MULTIPOLYGON` |`multipolygon` |An array of separate polygons.
|`GeometryCollection` |`GEOMETRYCOLLECTION` |`geometrycollection` | A GeoJSON shape similar to the
`multi*` shapes except that multiple types can coexist (e.g., a Point
and a LineString).
|`N/A` |`BBOX` |`envelope` |A bounding rectangle, or envelope, specified by
specifying only the top left and bottom right points.
|=======================================================================

=============================================
For all types, both the inner `type` and `coordinates` fields are
required.
=============================================

##### [Point](http://geojson.org/geojson-spec.html#id2)

A point is a single geographic coordinate, such as the location of a
building or the current position given by a smartphone's Geolocation
API. The following is an example of a point in GeoJSON.

```console
POST /example/_doc
{
  "location" : {
    "type" : "Point",
    "coordinates" : [-77.03653, 38.897676]
  }
}
```

The following is an example of a point in WKT:

```console
POST /example/_doc
{
  "location" : "POINT (-77.03653 38.897676)"
}
```

##### [LineString](http://geojson.org/geojson-spec.html#id3)

A linestring defined by an array of two or more positions. By
specifying only two points, the linestring will represent a straight
line. Specifying more than two points creates an arbitrary path. The
following is an example of a linestring in GeoJSON.

```console
POST /example/_doc
{
  "location" : {
    "type" : "LineString",
    "coordinates" : [[-77.03653, 38.897676], [-77.009051, 38.889939]]
  }
}
```

The following is an example of a linestring in WKT:

```console
POST /example/_doc
{
  "location" : "LINESTRING (-77.03653 38.897676, -77.009051 38.889939)"
}
```

The above linestring would draw a straight line starting at the White
House to the US Capitol Building.

##### [Polygon](http://geojson.org/geojson-spec.html#id4)

A polygon is defined by a list of a list of points. The first and last
points in each (outer) list must be the same (the polygon must be
closed). The following is an example of a polygon in GeoJSON.

```console
POST /example/_doc
{
  "location" : {
    "type" : "Polygon",
    "coordinates" : [
      [ [100.0, 0.0], [101.0, 0.0], [101.0, 1.0], [100.0, 1.0], [100.0, 0.0] ]
    ]
  }
}
```

The following is an example of a polygon in WKT:

```console
POST /example/_doc
{
  "location" : "POLYGON ((100.0 0.0, 101.0 0.0, 101.0 1.0, 100.0 1.0, 100.0 0.0))"
}
```

The first array represents the outer boundary of the polygon, the other
arrays represent the interior shapes ("holes"). The following is a GeoJSON example
of a polygon with a hole:

```console
POST /example/_doc
{
  "location" : {
    "type" : "Polygon",
    "coordinates" : [
      [ [100.0, 0.0], [101.0, 0.0], [101.0, 1.0], [100.0, 1.0], [100.0, 0.0] ],
      [ [100.2, 0.2], [100.8, 0.2], [100.8, 0.8], [100.2, 0.8], [100.2, 0.2] ]
    ]
  }
}
```

The following is an example of a polygon with a hole in WKT:

```console
POST /example/_doc
{
  "location" : "POLYGON ((100.0 0.0, 101.0 0.0, 101.0 1.0, 100.0 1.0, 100.0 0.0), (100.2 0.2, 100.8 0.2, 100.8 0.8, 100.2 0.8, 100.2 0.2))"
}
```

##### Polygon orientation

A polygon's orientation indicates the order of its vertices: `RIGHT`
(counterclockwise) or `LEFT` (clockwise). Elasticsearch uses a polygon’s orientation to
determine if it crosses the international dateline (+/-180° longitude).

You can set a default orientation for WKT polygons using the
`orientation` mapping parameter. This is because
the WKT specification doesn't specify or enforce a default orientation.

GeoJSON polygons use a default orientation of `RIGHT`, regardless of
`orientation` mapping parameter's value. This is because the
[GeoJSON specification](https://tools.ietf.org/html/rfc7946#section-3.1.6)
mandates that an outer polygon use a counterclockwise orientation and interior
shapes use a clockwise orientation.

You can override the default orientation for GeoJSON polygons using the
document-level `orientation` parameter. For example, the following indexing
request specifies a document-level `orientation` of `LEFT`.

```console
POST /example/_doc
{
  "location" : {
    "type" : "Polygon",
    "orientation" : "LEFT",
    "coordinates" : [
      [ [-177.0, 10.0], [176.0, 15.0], [172.0, 0.0], [176.0, -15.0], [-177.0, -10.0], [-177.0, 10.0] ]
    ]
  }
}
```

Elasticsearch only uses a polygon’s orientation to determine if it crosses the
international dateline. If the difference between a polygon’s minimum longitude
and the maximum longitude is less than 180°, the polygon doesn't cross the
dateline and its orientation has no effect.

If the difference between a polygon’s minimum longitude and the maximum
longitude is 180° or greater, Elasticsearch checks whether the polygon's document-level
`orientation` differs from the default orientation. If the orientation differs,
Elasticsearch considers the polygon to cross the international dateline and splits the
polygon at the dateline.

##### [MultiPoint](http://geojson.org/geojson-spec.html#id5)

The following is an example of a list of GeoJSON points:

```console
POST /example/_doc
{
  "location" : {
    "type" : "MultiPoint",
    "coordinates" : [
      [102.0, 2.0], [103.0, 2.0]
    ]
  }
}
```

The following is an example of a list of WKT points:

```console
POST /example/_doc
{
  "location" : "MULTIPOINT (102.0 2.0, 103.0 2.0)"
}
```

##### [MultiLineString](http://geojson.org/geojson-spec.html#id6)

The following is an example of a list of GeoJSON linestrings:

```console
POST /example/_doc
{
  "location" : {
    "type" : "MultiLineString",
    "coordinates" : [
      [ [102.0, 2.0], [103.0, 2.0], [103.0, 3.0], [102.0, 3.0] ],
      [ [100.0, 0.0], [101.0, 0.0], [101.0, 1.0], [100.0, 1.0] ],
      [ [100.2, 0.2], [100.8, 0.2], [100.8, 0.8], [100.2, 0.8] ]
    ]
  }
}
```

The following is an example of a list of WKT linestrings:

```console
POST /example/_doc
{
  "location" : "MULTILINESTRING ((102.0 2.0, 103.0 2.0, 103.0 3.0, 102.0 3.0), (100.0 0.0, 101.0 0.0, 101.0 1.0, 100.0 1.0), (100.2 0.2, 100.8 0.2, 100.8 0.8, 100.2 0.8))"
}
```

##### [MultiPolygon](http://geojson.org/geojson-spec.html#id7)

The following is an example of a list of GeoJSON polygons (second polygon contains a hole):

```console
POST /example/_doc
{
  "location" : {
    "type" : "MultiPolygon",
    "coordinates" : [
      [ [[102.0, 2.0], [103.0, 2.0], [103.0, 3.0], [102.0, 3.0], [102.0, 2.0]] ],
      [ [[100.0, 0.0], [101.0, 0.0], [101.0, 1.0], [100.0, 1.0], [100.0, 0.0]],
        [[100.2, 0.2], [100.8, 0.2], [100.8, 0.8], [100.2, 0.8], [100.2, 0.2]] ]
    ]
  }
}
```

The following is an example of a list of WKT polygons (second polygon contains a hole):

```console
POST /example/_doc
{
  "location" : "MULTIPOLYGON (((102.0 2.0, 103.0 2.0, 103.0 3.0, 102.0 3.0, 102.0 2.0)), ((100.0 0.0, 101.0 0.0, 101.0 1.0, 100.0 1.0, 100.0 0.0), (100.2 0.2, 100.8 0.2, 100.8 0.8, 100.2 0.8, 100.2 0.2)))"
}
```

##### [Geometry Collection](http://geojson.org/geojson-spec.html#geometrycollection)

The following is an example of a collection of GeoJSON geometry objects:

```console
POST /example/_doc
{
  "location" : {
    "type": "GeometryCollection",
    "geometries": [
      {
        "type": "Point",
        "coordinates": [100.0, 0.0]
      },
      {
        "type": "LineString",
        "coordinates": [ [101.0, 0.0], [102.0, 1.0] ]
      }
    ]
  }
}
```

The following is an example of a collection of WKT geometry objects:

```console
POST /example/_doc
{
  "location" : "GEOMETRYCOLLECTION (POINT (100.0 0.0), LINESTRING (101.0 0.0, 102.0 1.0))"
}
```

##### Envelope

Elasticsearch supports an `envelope` type, which consists of coordinates
for upper left and lower right points of the shape to represent a
bounding rectangle in the format `[[minLon, maxLat], [maxLon, minLat]]`:

```console
POST /example/_doc
{
  "location" : {
    "type" : "envelope",
    "coordinates" : [ [100.0, 1.0], [101.0, 0.0] ]
  }
}
```

The following is an example of an envelope using the WKT BBOX format:

*NOTE:* WKT specification expects the following order: minLon, maxLon, maxLat, minLat.

```console
POST /example/_doc
{
  "location" : "BBOX (100.0, 102.0, 2.0, 0.0)"
}
```

##### Circle

Neither GeoJSON nor WKT supports a point-radius circle type. Instead, use a
circle ingest processor to approximate the circle as
a `polygon`.

#### Sorting and Retrieving index Shapes

Due to the complex input structure and index representation of shapes,
it is not currently possible to sort shapes or retrieve their fields
directly. The `geo_shape` value is only retrievable through the `_source`
field.
