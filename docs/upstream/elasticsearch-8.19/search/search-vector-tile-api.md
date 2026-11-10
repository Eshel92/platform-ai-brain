<!-- Converted from search/search-vector-tile-api.asciidoc (AsciiDoc). Includes are inlined. -->

### Vector tile search API

**New API reference**
For the most up-to-date API details, refer to [Search APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-search).

Searches a vector tile for geospatial values. Returns results as a binary
[Mapbox vector tile](https://docs.mapbox.com/vector-tiles/specification).

```console
GET my-index/_mvt/my-geo-field/15/5271/12710
```

#### Request

`GET <target>/_mvt/<field>/<zoom>/<x>/<y>`

`POST <target>/_mvt/<field>/<zoom>/<x>/<y>`

#### Prerequisites

* Before using this API, you should be familiar with the
[Mapbox vector tile specification](https://github.com/mapbox/vector-tile-spec).

* If the Elasticsearch security features are enabled, you must have the `read`
index privilege for the target data stream, index,
or alias. For cross-cluster search, see remote-clusters.

#### Path parameters

`<target>`::
(Required, string) Comma-separated list of data streams, indices, or aliases to
search. Supports wildcards (`*`). To search all data streams and indices, omit
this parameter or use `*` or `_all`.
To search a remote cluster, use the `<cluster>:<target>` syntax. See
modules-cross-cluster-search.

`<field>`::
(Required, string) Field containing geospatial values to return. Must be a
`geo_point` or `geo_shape` field. The field must
have doc values enabled. Cannot be a nested field.
**Note:** Vector tiles do not natively support geometry collections. For
`geometrycollection` values in a `geo_shape` field, the API returns a `hits`
layer feature for each element of the collection.
This behavior may change in a future release.

`<zoom>`::
(Required, integer) Zoom level for the vector tile to search. Accepts `0`-`29`.

`<x>`::
(Required, integer) X coordinate for the vector tile to search.

`<y>`::
(Required, integer) Y coordinate for the vector tile to search.

#### Description

Internally, Elasticsearch translates a vector tile search API request into a
search containing:

* A `geo_bounding_box` query on the
`<field>`. The query uses the `<zoom>/<x>/<y>` tile as a bounding box.

* A `geotile_grid` or
`geohex_grid` aggregation
on the `<field>`. The `grid_agg` parameter determines the aggregation type. The
aggregation uses the `<zoom>/<x>/<y>` tile as a bounding box.

* Optionally, a
`geo_bounds` aggregation
on the `<field>`. The search only includes this aggregation if the
`exact_bounds` parameter is `true`.

* If the optional parameter `with_labels` is true, the internal search will include
a dynamic runtime field that calls the `getLabelPosition` function of the geometry doc value.
This enables the generation of new point features containing suggested geometry labels,
so that, for example, multi-polygons will have only one label.

For example, Elasticsearch may translate a vector tile search API request with a
`grid_agg` argument of `geotile` and an `exact_bounds` argument of `true`
into the following search:

```console
GET my-index/_search
{
  "size": 10000,
  "query": {
    "geo_bounding_box": {
      "my-geo-field": {
        "top_left": {
          "lat": -40.979898069620134,
          "lon": -45
        },
        "bottom_right": {
          "lat": -66.51326044311186,
          "lon": 0
        }
      }
    }
  },
  "aggregations": {
    "grid": {
      "geotile_grid": {
        "field": "my-geo-field",
        "precision": 11,
        "size": 65536,
        "bounds": {
          "top_left": {
            "lat": -40.979898069620134,
            "lon": -45
          },
          "bottom_right": {
            "lat": -66.51326044311186,
            "lon": 0
          }
        }
      }
    },
    "bounds": {
      "geo_bounds": {
        "field": "my-geo-field",
        "wrap_longitude": false
      }
    }
  }
}
```

The API returns results as a binary
[Mapbox vector tile](https://github.com/mapbox/vector-tile-spec). Mapbox vector
tiles are encoded as https://github.com/protocolbuffers/protobuf[Google
Protobufs (PBF)]. By default, the tile contains three layers:

* A `hits` layer containing a feature for each `<field>` value matching the
`geo_bounding_box` query.

*  An `aggs` layer containing a feature for each cell of the `geotile_grid` or
`geohex_grid`. The layer only contains features for cells with matching data.

* A `meta` layer containing:
** A feature containing a bounding box. By default, this is the bounding box of
the tile.
** Value ranges for any sub-aggregations on the `geotile_grid` or `geohex_grid`.
** Metadata for the search.

The API only returns features that can display at its zoom level. For example,
if a polygon feature has no area at its zoom level, the API omits it.

The API returns errors as UTF-8 encoded JSON.

#### Query parameters

**Important:** You can specify several options for this API as either a query
parameter or request body parameter. If you specify both parameters, the query
parameter takes precedence.

`exact_bounds`::
(Optional, Boolean)
If `false`, the `meta` layer's feature is the bounding box of the tile. Defaults
to `false`.
If `true`, the `meta` layer's feature is a bounding box resulting from a
`geo_bounds` aggregation.
The aggregation runs on `<field>` values that intersect the `<zoom>/<x>/<y>`
tile with `wrap_longitude` set to `false`. The resulting bounding box may be
larger than the vector tile.

`extent`::
(Optional, integer) Size, in pixels, of a side of the tile. Vector tiles are
square with equal sides. Defaults to `4096`.

`buffer`::
(Optional, integer) Size, in pixels, of a clipping buffer outside the tile.
This allows renderers to avoid outline artifacts from geometries that extend past the extent of the tile.
Defaults to `5`.

`grid_agg`::
(Optional, string) Aggregation used to create a grid for the `<field>`.
**Valid values for `grid_agg`**
`geotile` (Default)::
`geotile_grid` aggregation.

`geohex`::
`geohex_grid` aggregation.

`grid_precision`::
(Optional, integer) Precision level for cells in the `grid_agg`. Accepts
`0`-`8`. Defaults to `8`. If `0`, results don't include the `aggs` layer.
**Grid precision for `geotile`**
For a `grid_agg` of `geotile`, you can use cells in the `aggs` layer as tiles
for lower zoom levels. `grid_precision` represents the additional zoom levels
available through these cells. The final precision is computed by as
follows:

`<zoom> + grid_precision`

For example, if `<zoom>` is `7` and `grid_precision` is `8`, then the
`geotile_grid` aggregation will use a precision of `15`. The maximum final
precision is `29`.

The `grid_precision` also determines the number of cells for the grid as
follows:

`(2^grid_precision) x (2^grid_precision)`

For example, a value of `8` divides the tile into a grid of 256 x 256 cells. The
`aggs` layer only contains features for cells with matching data.
**Grid precision for `geohex`**
For a `grid_agg` of `geohex`, Elasticsearch uses `<zoom>` and `grid_precision` to
calculate a final precision as follows:

`<zoom> + grid_precision`

This precision determines the https://h3geo.org/docs/core-library/restable[H3
resolution of the hexagonal cells] produced by the `geohex` aggregation. The
following table maps the H3 resolution for each precision.

For example, if `<zoom>` is `3` and `grid_precision` is `3`, the precision is
`6`. At a precision of `6`, hexagonal cells have an H3 resolution of `2`. If
`<zoom>` is `3` and `grid_precision` is `4`, the precision is `7`. At a
precision of `7`, hexagonal cells have an H3 resolution of `3`.

|====
|Precision | Unique tile bins| H3 resolution| Unique hex bins | Ratio
|1	|4	                 |0	|122	            |30.5
|2	|16	                 |0	|122	            |7.625
|3	|64	                 |1	|842	            |13.15625
|4	|256	               |1	|842	            |3.2890625
|5	|1024	               |2	|5882	            |5.744140625
|6	|4096	               |2	|5882	            |1.436035156
|7	|16384	             |3	|41162	          |2.512329102
|8	|65536	             |3	|41162	          |0.6280822754
|9	|262144	             |4	|288122	          |1.099098206
|10	|1048576	           |4	|288122	          |0.2747745514
|11	|4194304	           |5	|2016842	        |0.4808526039
|12	|16777216	           |6	|14117882	        |0.8414913416
|13	|67108864	           |6	|14117882	        |0.2103728354
|14	|268435456	         |7	|98825162	        |0.3681524172
|15	|1073741824	         |8	|691776122	      |0.644266719
|16	|4294967296	         |8	|691776122	      |0.1610666797
|17	|17179869184	       |9	|4842432842	      |0.2818666889
|18	|68719476736	       |10 |33897029882	    |0.4932667053
|19	|274877906944	       |11 |237279209162	  |0.8632167343
|20	|1099511627776	     |11 |237279209162	  |0.2158041836
|21	|4398046511104	     |12 |1660954464122	  |0.3776573213
|22	|17592186044416	     |13 |11626681248842	|0.6609003122
|23	|70368744177664	     |13 |11626681248842	|0.165225078
|24	|281474976710656	   |14 |81386768741882	|0.2891438866
|25	|1125899906842620	   |15 |569707381193162	|0.5060018015
|26	|4503599627370500	   |15 |569707381193162	|0.1265004504
|27	|18014398509482000	 |15 |569707381193162	|0.03162511259
|28	|72057594037927900	 |15 |569707381193162	|0.007906278149
|29	|288230376151712000	 |15 |569707381193162	|0.001976569537
|====

Hexagonal cells don't align perfectly on a vector tile. Some cells may intersect
more than one vector tile. To compute the H3 resolution for each precision, Elasticsearch
compares the average density of hexagonal bins at each resolution with the
average density of tile bins at each zoom level. Elasticsearch uses the H3 resolution
that is closest to the corresponding `geotile` density.

`grid_type`::
(Optional, string) Determines the geometry type for features in the `aggs`
layer. In the `aggs` layer, each feature represents a cell in the grid.
**Valid values for `grid_type`**
`grid` (Default)::
Each feature is a `Polygon` of the cell's geometry. For a `grid_agg` of
`geotile`, the feature is the cell's bounding box. For a `grid_agg` of
`geohex`, the feature is the hexagonal cell's boundaries.

`point`::
Each feature is a `Point` that's the centroid of the cell.

`centroid`::
Each feature is a `Point` that's the centroid of the data within the cell. For
complex geometries, the actual centroid may be outside the cell. In these cases,
the feature is set to the closest point to the centroid inside the cell.

`size`::
(Optional, integer) Maximum number of features to return in the `hits` layer.
Accepts `0`-`10000`. Defaults to `10000`. If `0`, results don't include the
`hits` layer.

`track_total_hits`::
(Optional, integer or Boolean)
Number of hits matching the query to count accurately. Defaults to `10000`.
If `true`, the exact number of hits is returned at the cost of some performance.
If `false`, the response does not include the total number of hits matching the query.

`with_labels`::
(Optional, Boolean)
If true, the hits and aggs layers will contain additional point features representing
suggested label positions for the original features.
* `Point` and `MultiPoint` features will have one of the points selected.
* `Polygon` and `MultiPolygon` features will have a single point generated,
either the centroid, if it is within the polygon, or another point within the
polygon selected from the sorted triangle-tree.
* `LineString` features will likewise provide a roughly central point selected
from the triangle-tree.
* The aggregation results will provide one central point for each aggregation bucket.

All attributes from the original features will also be copied to the new label features.
In addition, the new features will be distinguishable using the tag `_mvt_label_position`.

#### Request body

`aggs`::
(Optional, aggregation object)
Sub-aggregations for the `grid_agg`. Supports the following
aggregation types:
* `avg`
* `boxplot`
* `cardinality`
* `extended stats`
* `max`
* `median absolute deviation`
* `min`
* `percentile`
* `percentile-rank`
* `stats`
* `sum`
* `value count`
The aggregation names can't start with `_mvt_`. The `_mvt_` prefix is reserved
for internal aggregations.

`exact_bounds`::
(Optional, Boolean)
If `false`, the `meta` layer's feature is the bounding box of the tile. Defaults
to `false`.
If `true`, the `meta` layer's feature is a bounding box resulting from a
`geo_bounds` aggregation.
The aggregation runs on `<field>` values that intersect the `<zoom>/<x>/<y>`
tile with `wrap_longitude` set to `false`. The resulting bounding box may be
larger than the vector tile.
`extent`::
(Optional, integer) Size, in pixels, of a side of the tile. Vector tiles are
square with equal sides. Defaults to `4096`.
`buffer`::
(Optional, integer) Size, in pixels, of a clipping buffer outside the tile.
This allows renderers to avoid outline artifacts from geometries that extend past the extent of the tile.
Defaults to `5`.
`fields`::
(Optional, array of strings and objects) Fields to return in the `hits` layer.
Supports wildcards (`*`).
This parameter does not support fields with array values. Fields with
array values may return inconsistent results.
You can specify fields in the array as a string or object.
**Properties of `fields` objects**
`field`::
(Required, string) Field to return. Supports wildcards (`*`).

`format`::
(Optional, string)
Format for date and geospatial fields. Other field data types do not support
this parameter.
`date` and `date_nanos` fields accept a
date format. `geo_point` and
`geo_shape` fields accept:

`geojson` (default):::
[GeoJSON](http://www.geojson.org)

`wkt`:::
[Well Known Text](https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry)

`mvt(<spec>)`:::
Binary
[Mapbox vector tile](https://docs.mapbox.com/vector-tiles/specification). The API
returns the tile as a base64-encoded string.
The `<spec>` has the format `<zoom>/<x>/<y>` with two optional suffixes: `@<extent>` and/or `:<buffer>`. For example, `2/0/1` or `2/0/1@4096:5`.
.`mvt` parameters
========
`<zoom>`::
(Required, integer) Zoom level for the tile. Accepts `0`-`29`.

`<x>`::
(Required, integer) X coordinate for the tile.

`<y>`::
(Required, integer) Y coordinate for the tile.

`<extent>`::
(Optional, integer) Size, in pixels, of a side of the tile. Vector tiles are
square with equal sides. Defaults to `4096`.

`<buffer>`::
(Optional, integer) Size, in pixels, of a clipping buffer outside the tile.
This allows renderers to avoid outline artifacts from geometries that extend past the extent of the tile. Defaults to `5`.
========

`grid_agg`::
(Optional, string) Aggregation used to create a grid for the `<field>`.
**Valid values for `grid_agg`**
`geotile` (Default)::
`geotile_grid` aggregation.

`geohex`::
`geohex_grid` aggregation.
`grid_precision`::
(Optional, integer) Precision level for cells in the `grid_agg`. Accepts
`0`-`8`. Defaults to `8`. If `0`, results don't include the `aggs` layer.
**Grid precision for `geotile`**
For a `grid_agg` of `geotile`, you can use cells in the `aggs` layer as tiles
for lower zoom levels. `grid_precision` represents the additional zoom levels
available through these cells. The final precision is computed by as
follows:

`<zoom> + grid_precision`

For example, if `<zoom>` is `7` and `grid_precision` is `8`, then the
`geotile_grid` aggregation will use a precision of `15`. The maximum final
precision is `29`.

The `grid_precision` also determines the number of cells for the grid as
follows:

`(2^grid_precision) x (2^grid_precision)`

For example, a value of `8` divides the tile into a grid of 256 x 256 cells. The
`aggs` layer only contains features for cells with matching data.
**Grid precision for `geohex`**
For a `grid_agg` of `geohex`, Elasticsearch uses `<zoom>` and `grid_precision` to
calculate a final precision as follows:

`<zoom> + grid_precision`

This precision determines the https://h3geo.org/docs/core-library/restable[H3
resolution of the hexagonal cells] produced by the `geohex` aggregation. The
following table maps the H3 resolution for each precision.

For example, if `<zoom>` is `3` and `grid_precision` is `3`, the precision is
`6`. At a precision of `6`, hexagonal cells have an H3 resolution of `2`. If
`<zoom>` is `3` and `grid_precision` is `4`, the precision is `7`. At a
precision of `7`, hexagonal cells have an H3 resolution of `3`.

|====
|Precision | Unique tile bins| H3 resolution| Unique hex bins | Ratio
|1	|4	                 |0	|122	            |30.5
|2	|16	                 |0	|122	            |7.625
|3	|64	                 |1	|842	            |13.15625
|4	|256	               |1	|842	            |3.2890625
|5	|1024	               |2	|5882	            |5.744140625
|6	|4096	               |2	|5882	            |1.436035156
|7	|16384	             |3	|41162	          |2.512329102
|8	|65536	             |3	|41162	          |0.6280822754
|9	|262144	             |4	|288122	          |1.099098206
|10	|1048576	           |4	|288122	          |0.2747745514
|11	|4194304	           |5	|2016842	        |0.4808526039
|12	|16777216	           |6	|14117882	        |0.8414913416
|13	|67108864	           |6	|14117882	        |0.2103728354
|14	|268435456	         |7	|98825162	        |0.3681524172
|15	|1073741824	         |8	|691776122	      |0.644266719
|16	|4294967296	         |8	|691776122	      |0.1610666797
|17	|17179869184	       |9	|4842432842	      |0.2818666889
|18	|68719476736	       |10 |33897029882	    |0.4932667053
|19	|274877906944	       |11 |237279209162	  |0.8632167343
|20	|1099511627776	     |11 |237279209162	  |0.2158041836
|21	|4398046511104	     |12 |1660954464122	  |0.3776573213
|22	|17592186044416	     |13 |11626681248842	|0.6609003122
|23	|70368744177664	     |13 |11626681248842	|0.165225078
|24	|281474976710656	   |14 |81386768741882	|0.2891438866
|25	|1125899906842620	   |15 |569707381193162	|0.5060018015
|26	|4503599627370500	   |15 |569707381193162	|0.1265004504
|27	|18014398509482000	 |15 |569707381193162	|0.03162511259
|28	|72057594037927900	 |15 |569707381193162	|0.007906278149
|29	|288230376151712000	 |15 |569707381193162	|0.001976569537
|====

Hexagonal cells don't align perfectly on a vector tile. Some cells may intersect
more than one vector tile. To compute the H3 resolution for each precision, Elasticsearch
compares the average density of hexagonal bins at each resolution with the
average density of tile bins at each zoom level. Elasticsearch uses the H3 resolution
that is closest to the corresponding `geotile` density.
`grid_type`::
(Optional, string) Determines the geometry type for features in the `aggs`
layer. In the `aggs` layer, each feature represents a cell in the grid.
**Valid values for `grid_type`**
`grid` (Default)::
Each feature is a `Polygon` of the cell's geometry. For a `grid_agg` of
`geotile`, the feature is the cell's bounding box. For a `grid_agg` of
`geohex`, the feature is the hexagonal cell's boundaries.

`point`::
Each feature is a `Point` that's the centroid of the cell.

`centroid`::
Each feature is a `Point` that's the centroid of the data within the cell. For
complex geometries, the actual centroid may be outside the cell. In these cases,
the feature is set to the closest point to the centroid inside the cell.
`query`::
(Optional, object) Query DSL used to filter documents for the
search.

`runtime_mappings`::
(Optional, object of objects)
Defines one or more runtime fields in the search
request. These fields take precedence over mapped fields with the same name.
**Properties of `runtime_mappings` objects**

`<field-name>`::
(Required, object)
Configuration for the runtime field. The key is the field name.
**Properties of `<field-name>`**
=====

`type`::
(Required, string)
Field type, which can be any of the following:
* `boolean`
* `composite`
* `date`
* `double`
* `geo_point`
* `ip`
* `keyword`
* `long`
* `lookup`
`script`::
(Optional, string)
Painless script executed at query time. The
script has access to the entire context of a document, including the original
`_source` and any mapped fields plus their values.
This script must include `emit` to return calculated values. For example:
```js
      "script": "emit(doc['@timestamp'].value.dayOfWeekEnum.toString())"
```

=====
`size`::
(Optional, integer) Maximum number of features to return in the `hits` layer.
Accepts `0`-`10000`. Defaults to `10000`. If `0`, results don't include the
`hits` layer.
`sort`::
(Optional, array of sort objects) Sorts features in the
`hits` layer.
By default, the API calculates a bounding box for each feature. It sorts
features based on this box's diagonal length, from longest to shortest.

`track_total_hits`::
(Optional, integer or Boolean)
Number of hits matching the query to count accurately. Defaults to `10000`.
If `true`, the exact number of hits is returned at the cost of some performance.
If `false`, the response does not include the total number of hits matching the query.
`with_labels`::
(Optional, Boolean)
If true, the hits and aggs layers will contain additional point features representing
suggested label positions for the original features.
* `Point` and `MultiPoint` features will have one of the points selected.
* `Polygon` and `MultiPolygon` features will have a single point generated,
either the centroid, if it is within the polygon, or another point within the
polygon selected from the sorted triangle-tree.
* `LineString` features will likewise provide a roughly central point selected
from the triangle-tree.
* The aggregation results will provide one central point for each aggregation bucket.

All attributes from the original features will also be copied to the new label features.
In addition, the new features will be distinguishable using the tag `_mvt_label_position`.

#### Response

Returned vector tiles contain the following data:

`hits`::
(object) Layer containing results for the `geo_bounding_box` query.
**Properties of `hits`**
`extent`::
(integer) Size, in pixels, of a side of the tile. Vector tiles are square with
equal sides.

`version`::
(integer) Major version number of the
[Mapbox vector tile specification](https://github.com/mapbox/vector-tile-spec).

`features`::
(array of objects) Array of features. Contains a feature for each `<field>`
value that matches the `geo_bounding_box` query.
**Properties of `features` objects**
=====
`geometry`::
(object) Geometry for the feature.
**Properties of `geometry`**
======
`type`::
(string) Geometry type for the feature. Valid values are:

* `UNKNOWN`
* `POINT`
* `LINESTRING`
* `POLYGON`

`coordinates`::
(array of integers or array of arrays) Tile coordinates for the feature.
======

`properties`::
(object) Properties for the feature.
**Properties of `properties`**
======
`_id`::
(string) Document `_id` for the feature's document.

`_index`::
(string) Name of the index for the feature's document.

`<field>`::
Field value. Only returned for fields in the `fields` parameter.
======
`type`::
(integer) Identifier for the feature's geometry type. Values are:
* `1` (`POINT`)
* `2` (`LINESTRING`)
* `3` (`POLYGON`)
=====

`aggs`::
(object) Layer containing results for the `grid_agg` aggregation and its
sub-aggregations.
**Properties of `aggs`**
`extent`::
(integer) Size, in pixels, of a side of the tile. Vector tiles are square with
equal sides.
`version`::
(integer) Major version number of the
[Mapbox vector tile specification](https://github.com/mapbox/vector-tile-spec).
`features`::
(array of objects) Array of features. Contains a feature for each cell of the grid.
**Properties of `features` objects**
=====
`geometry`::
(object) Geometry for the feature.
**Properties of `geometry`**
======
`type`::
(string) Geometry type for the feature. Valid values are:

* `UNKNOWN`
* `POINT`
* `LINESTRING`
* `POLYGON`

`coordinates`::
(array of integers or array of arrays) Tile coordinates for the feature.
======
`properties`::
(object) Properties for the feature.
**Properties of `properties`**
======
`_count`::
(long) Count of the cell's documents.

`_key`::
(string) Bucket key of the cell in the format `<zoom>/<x>/<y>`.

`<sub-aggregation>.value`::
Sub-aggregation results for the cell. Only returned for sub-aggregations in the
`aggs` parameter.
======
`type`::
(integer) Identifier for the feature's geometry type. Values are:
* `1` (`POINT`)
* `2` (`LINESTRING`)
* `3` (`POLYGON`)
=====

`meta`::
(object) Layer containing metadata for the request.
**Properties of `meta`**
`extent`::
(integer) Size, in pixels, of a side of the tile. Vector tiles are square with
equal sides.
`version`::
(integer) Major version number of the
[Mapbox vector tile specification](https://github.com/mapbox/vector-tile-spec).
`features`::
(array of objects) Contains a feature for a bounding box.
**Properties of `features` objects**
=====
`geometry`::
(object) Geometry for the feature.
**Properties of `geometry`**
======
`type`::
(string) Geometry type for the feature. Valid values are:

* `UNKNOWN`
* `POINT`
* `LINESTRING`
* `POLYGON`

`coordinates`::
(array of integers or array of arrays) Tile coordinates for the feature.
======
`properties`::
(object) Properties for the feature.
**Properties of `properties`**
======
`_shards.failed`::
(integer) Number of shards that failed to execute the search. See the search
API's `shards` response property.

`_shards.skipped`::
(integer) Number of shards that skipped the search. See the search
API's `shards` response property.

`_shards.successful`::
(integer)  Number of shards that executed the search successfully. See the
search API's `shards` response property.

`_shards.total`::
(integer) Total number of shards that required querying, including unallocated
shards. See the search API's `shards` response property.

`aggregations._count.avg`::
(float) Average `_count` value for features in the `aggs` layer.

`aggregations._count.count`::
(integer) Number of unique `_count` values for features in the `aggs` layer.

`aggregations._count.max`::
(float) Largest `_count` value for features in the `aggs` layer.

`aggregations._count.min`::
(float) Smallest `_count` value for features in the `aggs` layer.

`aggregations._count.sum`::
(float) Sum of `_count` values for features in the `aggs` layer.

`aggregations.<sub-aggregation>.avg`::
(float) Average value for the sub-aggregation's results.

`aggregations.<agg_name>.count`::
(integer) Number of unique values from the sub-aggregation's results.

`aggregations.<agg_name>.max`::
(float) Largest value from the sub-aggregation's results.

`aggregations.<agg_name>.min`::
(float) Smallest value from the sub-aggregation's results.

`aggregations.<agg_name>.sum`::
(float) Sum of values for the sub-aggregation's results.

`hits.max_score`::
(float) Highest document `_score` for the search's hits.

`hits.total.relation`::
(string) Indicates whether `hits.total.value` is accurate or a lower bound.
Possible values are:

`eq`::: Accurate

`gte`::: Lower bound

`hits.total.value`::
(integer) Total number of hits for the search.

`timed_out`::
(Boolean) If `true`, the search timed out before completion. Results may be
partial or empty.

`took`::
(integer) Milliseconds it took Elasticsearch to run the search. See the search API's
`took` response property.
======
`type`::
(integer) Identifier for the feature's geometry type. Values are:
* `1` (`POINT`)
* `2` (`LINESTRING`)
* `3` (`POLYGON`)
=====

#### Examples

The following requests create the `museum` index and add several geospatial
`location` values.

```console
PUT museums
{
  "mappings": {
    "properties": {
      "location": {
        "type": "geo_point"
      },
      "name": {
        "type": "keyword"
      },
      "price": {
        "type": "long"
      },
      "included": {
        "type": "boolean"
      }
    }
  }
}

POST museums/_bulk?refresh
{ "index": { "_id": "1" } }
{ "location": "POINT (4.912350 52.374081)", "name": "NEMO Science Museum",  "price": 1750, "included": true }
{ "index": { "_id": "2" } }
{ "location": "POINT (4.901618 52.369219)", "name": "Museum Het Rembrandthuis", "price": 1500, "included": false }
{ "index": { "_id": "3" } }
{ "location": "POINT (4.914722 52.371667)", "name": "Nederlands Scheepvaartmuseum", "price":1650, "included": true }
{ "index": { "_id": "4" } }
{ "location": "POINT (4.914722 52.371667)", "name": "Amsterdam Centre for Architecture", "price":0, "included": true }
```

The following request searches the index for `location` values that intersect
the `13/4207/2692` vector tile.

```console
GET museums/_mvt/location/13/4207/2692
{
  "grid_agg": "geotile",
  "grid_precision": 2,
  "fields": [
    "name",
    "price"
  ],
  "query": {
    "term": {
      "included": true
    }
  },
  "aggs": {
    "min_price": {
      "min": {
        "field": "price"
      }
    },
    "max_price": {
      "max": {
        "field": "price"
      }
    },
    "avg_price": {
      "avg": {
        "field": "price"
      }
    }
  }
}
```

The API returns results as a binary vector tile. When decoded into JSON, the
tile contains the following data:

```js
{
  "hits": {
    "extent": 4096,
    "version": 2,
    "features": [
      {
        "geometry": {
          "type": "Point",
          "coordinates": [
            3208,
            3864
          ]
        },
        "properties": {
          "_id": "1",
          "_index": "museums",
          "name": "NEMO Science Museum",
          "price": 1750
        },
        "type": 1
      },
      {
        "geometry": {
          "type": "Point",
          "coordinates": [
            3429,
            3496
          ]
        },
        "properties": {
          "_id": "3",
          "_index": "museums",
          "name": "Nederlands Scheepvaartmuseum",
          "price": 1650
        },
        "type": 1
      },
      {
        "geometry": {
          "type": "Point",
          "coordinates": [
            3429,
            3496
          ]
        },
        "properties": {
          "_id": "4",
          "_index": "museums",
          "name": "Amsterdam Centre for Architecture",
          "price": 0
        },
        "type": 1
      }
    ]
  },
  "aggs": {
    "extent": 4096,
    "version": 2,
    "features": [
      {
        "geometry": {
          "type": "Polygon",
          "coordinates": [
            [
              [
                3072,
                3072
              ],
              [
                4096,
                3072
              ],
              [
                4096,
                4096
              ],
              [
                3072,
                4096
              ],
              [
                3072,
                3072
              ]
            ]
          ]
        },
        "properties": {
          "_count": 3,
          "max_price.value": 1750.0,
          "min_price.value": 0.0,
          "avg_price.value": 1133.3333333333333
        },
        "type": 3
      }
    ]
  },
  "meta": {
    "extent": 4096,
    "version": 2,
    "features": [
      {
        "geometry": {
          "type": "Polygon",
          "coordinates": [
            [
              [
                0,
                0
              ],
              [
                4096,
                0
              ],
              [
                4096,
                4096
              ],
              [
                0,
                4096
              ],
              [
                0,
                0
              ]
            ]
          ]
        },
        "properties": {
          "_shards.failed": 0,
          "_shards.skipped": 0,
          "_shards.successful": 1,
          "_shards.total": 1,
          "aggregations._count.avg": 3.0,
          "aggregations._count.count": 1,
          "aggregations._count.max": 3.0,
          "aggregations._count.min": 3.0,
          "aggregations._count.sum": 3.0,
          "aggregations.avg_price.avg": 1133.3333333333333,
          "aggregations.avg_price.count": 1,
          "aggregations.avg_price.max": 1133.3333333333333,
          "aggregations.avg_price.min": 1133.3333333333333,
          "aggregations.avg_price.sum": 1133.3333333333333,
          "aggregations.max_price.avg": 1750.0,
          "aggregations.max_price.count": 1,
          "aggregations.max_price.max": 1750.0,
          "aggregations.max_price.min": 1750.0,
          "aggregations.max_price.sum": 1750.0,
          "aggregations.min_price.avg": 0.0,
          "aggregations.min_price.count": 1,
          "aggregations.min_price.max": 0.0,
          "aggregations.min_price.min": 0.0,
          "aggregations.min_price.sum": 0.0,
          "hits.max_score": 0.0,
          "hits.total.relation": "eq",
          "hits.total.value": 3,
          "timed_out": false,
          "took": 2
        },
        "type": 3
      }
    ]
  }
}
```
