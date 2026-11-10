<!-- Converted from search/knn-search.asciidoc (AsciiDoc). Includes are inlined. -->

### kNN search API

deprecated::[8.4.0,"The kNN search API has been replaced by the `knn` option in the search API."]

Performs a k-nearest neighbor (kNN) search and returns the matching documents.

```console
GET my-index/_knn_search
{
  "knn": {
    "field": "image_vector",
    "query_vector": [0.3, 0.1, 1.2],
    "k": 10,
    "num_candidates": 100
  },
  "_source": ["name", "file_type"]
}
```

#### Request

`GET <target>/_knn_search`

`POST <target>/_knn_search`

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the `read`
index privilege for the target data stream, index,
or alias.

#### Description

The kNN search API performs a k-nearest neighbor (kNN) search on a
`dense_vector` field. Given a query vector, it finds the _k_
closest vectors and returns those documents as search hits.

Elasticsearch uses the [HNSW algorithm](https://arxiv.org/abs/1603.09320) to support
efficient kNN search. Like most kNN algorithms, HNSW is an approximate method
that sacrifices result accuracy for improved search speed. This means the
results returned are not always the true _k_ closest neighbors.

The kNN search API supports restricting the search using a filter. The search
will return the top `k` documents that also match the filter query.

#### Path parameters

`<target>`::
(Optional, string) Comma-separated list of data streams, indices, and aliases
to search. Supports wildcards (`*`). To search all data streams and indices,
use `*` or `_all`.

#### Query parameters

`routing`::
(Optional, string)
Custom value used to route operations to a specific shard.

#### Request body

`filter`::
(Optional, Query DSL object)
Query to filter the documents that can match. The kNN search will return the top
`k` documents that also match this filter. The value can be a single query or a
list of queries. If `filter` is not provided, all documents are allowed to
match.
`knn`::
(Required, object)
Defines the kNN query to run.
**Properties of `knn` object**
`field`::
(Required, string)
The name of the vector field to search against. Must be a
`dense_vector` field with indexing enabled.
`k`::
(Optional, integer)
Number of nearest neighbors to return as top hits. This value must be less than
or equal to `num_candidates`. Defaults to `size`.
`num_candidates`::
(Optional, integer)
The number of nearest neighbor candidates to consider per shard.
Needs to be greater than `k`, or `size` if `k` is omitted, and cannot exceed 10,000.
Elasticsearch collects `num_candidates` results from each shard, then merges them
to find the top `k` results. Increasing `num_candidates` tends to improve the
accuracy of the final `k` results. Defaults to `Math.min(1.5 * k, 10_000)`.
`query_vector`::
(Required, array of floats or string)
Query vector. Must have the same number of dimensions as the vector field you
are searching against. Must be either an array of floats or a hex-encoded byte vector.

`docvalue_fields`::
(Optional, array of strings and objects)
Array of field patterns. The request returns values for field names matching
these patterns in the `hits.fields` property of the response.
You can specify items in the array as a string or object. See
docvalue-fields.
**Properties of `docvalue_fields` objects**
`field`::
(Required, string)
Wildcard pattern. The request returns doc values for field names matching this
pattern.

`format`::
(Optional, string)
Format in which the doc values are returned.
For date fields, you can specify a date <<mapping-date-format,date
`format`>>. For numeric fields fields, you can specify a
https://docs.oracle.com/javase/8/docs/api/java/text/DecimalFormat.html[DecimalFormat
pattern].
For other field data types, this parameter is not supported.
`fields`::
(Optional, array of strings and objects)
Array of field patterns. The request returns values for field names matching
these patterns in the `hits.fields` property of the response.
You can specify items in the array as a string or object. See
the `fields` option.
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
`_source`::
(Optional)
Indicates which source fields are returned for matching
documents. These fields are returned in the `hits._source` property of
the search response. Defaults to `true`. See source filtering.
**Valid values for `_source`**
`true`::
(Boolean)
The entire document source is returned.

`false`::
(Boolean)
The document source is not returned.

`<wildcard_pattern>`::
(string or array of strings)
Wildcard (`*`) pattern or array of patterns containing source fields to return.

`<object>`::
(object)
Object containing a list of source fields to include or exclude.
**Properties for `<object>`**
=====
`excludes`::
(string or array of strings)
Wildcard (`*`) pattern or array of patterns containing source fields to exclude
from the response.
You can also use this property to exclude fields from the subset specified in
`includes` property.

`includes`::
(string or array of strings)
Wildcard (`*`) pattern or array of patterns containing source fields to return.
If this property is specified, only these source fields are returned. You can
exclude fields from this subset using the `excludes` property.
=====
`stored_fields`::
(Optional, string) A comma-separated list of stored fields to return as part
of a hit. If no fields are specified, no stored fields are included in the
response. See stored-fields.
If this option is specified, the `_source` parameter defaults to `false`. You
can pass `_source: true` to return both source fields and stored fields in the
search response.

#### Response body

A kNN search response has the exact same structure as a
search API response. However, certain sections
have a meaning specific to kNN search:

* The document `_score` is determined by
the similarity between the query and document vector. See
`similarity`.
* The `hits.total` object contains the total number of nearest neighbor
candidates considered, which is `num_candidates * num_shards`. The
`hits.total.relation` will always be `eq`, indicating an exact value.
