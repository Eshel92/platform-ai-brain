<!-- Converted from core/geohaystack.txt (reStructuredText). Includes are inlined. -->

# `geoHaystack` Indexes

**Important:** Removed in MongoDB 5.0

MongoDB 5.0 removes the deprecated geoHaystack index and `geoSearch` command. Use a
2d index with `$geoNear` or one of the
supported geospatial query operators
instead.

Upgrading your MongoDB instance to 5.0 and setting
featureCompatibilityVersion to `5.0` will delete any
pre-existing geoHaystack indexes.

A `geoHaystack` index is a special index that is optimized to return
results over small areas. `geoHaystack` indexes improve performance
on queries that use flat geometry.

For queries that use spherical geometry, a **2dsphere index is a better
option** than a haystack index. 2dsphere indexes allow field reordering; `geoHaystack` indexes
require the first field to be the location field. Also, `geoHaystack`
indexes are only usable via commands and so always return all results
at once.

## Behavior

`geoHaystack` indexes create "buckets" of documents from the same
geographic area in order to improve performance for queries limited to
that area. Each bucket in a `geoHaystack` index contains all the
documents within a specified proximity to a given longitude and
latitude.

## `sparse` Property

`geoHaystack` indexes are sparse by
default and ignore the sparse: true
option. If a document lacks a `geoHaystack` index field (or the field
is `null` or an empty array), MongoDB does not add an entry for the
document to the `geoHaystack` index. For inserts, MongoDB inserts the
document but does not add to the `geoHaystack` index.

`geoHaystack` indexes include one `geoHaystack` index key and one
non-geospatial index key; however, only the `geoHaystack` index field
determines whether the index references a document.

### Collation Option

`geoHaystack` indexes only support simple binary comparison and do not support
the collation.

To create a `geoHaystack` index on a collection that has a non-simple
collation, you must explicitly specify ``{collation: {locale: "simple"}
}`` when creating the index.

## Create `geoHaystack` Index

To create a `geoHaystack` index, see
/tutorial/build-a-geohaystack-index. For information and example
on querying a haystack index, see
/tutorial/query-a-geohaystack-index.
