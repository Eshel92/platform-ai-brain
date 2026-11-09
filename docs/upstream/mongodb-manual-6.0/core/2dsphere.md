<!-- Converted from core/2dsphere.txt (reStructuredText). Includes are inlined. -->

# `2dsphere` Indexes

## Overview

A `2dsphere` index supports queries that calculate geometries on an
earth-like sphere. `2dsphere` index supports all MongoDB geospatial
queries: queries for inclusion, intersection and proximity.
For more information on geospatial queries, see
/geospatial-queries.

The `2dsphere` index supports data stored as GeoJSON objects *and* legacy coordinate pairs (See also 2dsphere-data-restrictions).
For legacy coordinate pairs, the index converts the data to GeoJSON
geojson-point.

## Versions

| `2dsphere` Index Version | Description |
|---|---|
| Version 3 | MongoDB 3.2 introduces a version 3 of `2dsphere` indexes. Version 3 is the default version of `2dsphere` indexes created in MongoDB 3.2 and later. |
| Version 2 | MongoDB 2.6 introduces a version 2 of `2dsphere` indexes. Version 2 is the default version of `2dsphere` indexes created in MongoDB 2.6 and 3.0 series. |

To override the default version and specify a different version,
include the option `{ "2dsphereIndexVersion": <version> }` when
creating the index.

### `sparse` Property

Version 2 and later `2dsphere` indexes are always sparse and ignore the sparse option. If a document lacks a `2dsphere` index
field (or the field is `null` or an empty array), MongoDB does not
add an entry for the document to the index. For inserts, MongoDB
inserts the document but does not add to the `2dsphere` index.

For a compound index that includes a `2dsphere` index key along with
keys of other types, only the `2dsphere` index field determines
whether the index references a document.

Earlier versions of MongoDB only support `2dsphere (Version 1)`
indexes. `2dsphere (Version 1)` indexes are *not* sparse by default
and will reject documents with `null` location fields.

### Additional GeoJSON Objects

Version 2 and later `2dsphere` indexes includes support for additional GeoJSON
object: geojson-multipoint, geojson-multilinestring,
geojson-multipolygon, and geojson-geometrycollection. For
details on all supported GeoJSON objects, see /reference/geojson.

## Considerations

### `geoNear` and `$geoNear` Restrictions

You can specify a `key` option to the `$geoNear` pipeline stage to 
indicate the indexed field path to use. This allows the `$geoNear` 
stage to be used on a collection that has multiple `2dsphere` index and/or 
multiple 2d index:

- If your collection has multiple `2dsphere` index and/or multiple
  2d index, you must use the `key` option to specify the
  indexed field path to use.

- If you do not specify the `key`, you cannot have multiple
  `2dsphere` index and/or multiple 2d index since without
  the `key`, index selection among multiple `2d` indexes or
  `2dsphere` indexes is ambiguous.

**Note:**

If you do not specify the `key`, and you have at most only one
`2dsphere` index and/or only one 2d index,
MongoDB looks first for a `2d` index to use. If a `2d` index
does not exists, then MongoDB looks for a `2dsphere` index to use.

### Shard Key Restrictions

You cannot use a `2dsphere` index as a shard key when sharding a
collection. However, you can create a geospatial index
on a sharded collection by using a different field as the shard key.

### `2dsphere` Indexed Field Restrictions

Fields with 2dsphere indexes must hold geometry
data in the form of coordinate pairs
or GeoJSON data. If you attempt to insert a document with
non-geometry data in a `2dsphere` indexed field, or build a
`2dsphere` index on a collection where the indexed field has
non-geometry data, the operation will fail.

### Limited Number of Index Keys

To generate keys for a 2dsphere index, `mongod` maps
GeoJSON shapes to an internal
representation. The resulting internal representation may be a large
array of values.

When `mongod` generates index keys on a field that holds an
array, `mongod` generates an index key for each array element.
For compound indexes, `mongod` calculates the cartesian
product of the sets of keys that are generated for each field. If both
sets are large, then calculating the cartesian product could cause the
operation to exceed memory limits.

`indexMaxNumGeneratedKeysPerDocument` limits the maximum
number of keys generated for a single document to prevent out of
memory errors. The default is 100000 index keys per document. It is
possible to raise the limit, but if an operation requires more keys
than the `indexMaxNumGeneratedKeysPerDocument` parameter
specifies, the operation will fail.

## Create a `2dsphere` Index

To create a `2dsphere` index, use the
`db.collection.createIndex()` method and specify the string
literal `"2dsphere"` as the index type:

```javascript
db.collection.createIndex( { <location field> : "2dsphere" } )
```

where the `<location field>` is a field whose value is either a
GeoJSON object or a legacy
coordinates pair.

**Note:**

If you try to create an index on a field that contains an array of 
geoJSON points, the index build fails and returns the following error: 

`MongoServerError: Index build failed`

Unlike a compound 2d index which can reference one
location field and one other field, a compound `2dsphere` index can reference multiple
location and non-location fields.

For the following examples, consider a collection `places` with
documents that store location data as GeoJSON Point in a field named `loc`:

```javascript
db.places.insertMany( [
   {
      loc : { type: "Point", coordinates: [ -73.97, 40.77 ] },
      name: "Central Park",
      category : "Parks"
   },
   {
      loc : { type: "Point", coordinates: [ -73.88, 40.78 ] },
      name: "La Guardia Airport",
      category : "Airport"
   }
] )
```

### Create a `2dsphere` Index

The following operation creates a 2dsphere
index on the location field `loc`:

```javascript
db.places.createIndex( { loc : "2dsphere" } )
```

### Create a Compound Index with `2dsphere` Index Key

A compound index can include a
`2dsphere` index key in combination with non-geospatial index keys.
For example, the following operation creates a compound index where
the first key `loc` is a `2dsphere` index key, and the remaining
keys `category` and `names` are non-geospatial index keys,
specifically descending (`-1`) and ascending (`1`) keys
respectively.

```javascript
db.places.createIndex( { loc : "2dsphere" , category : -1, name: 1 } )
```

Unlike the 2d index, a compound `2dsphere` index
does not require the location field to be the first field indexed. For
example:

```javascript
db.places.createIndex( { category : 1 , loc : "2dsphere" } )
```
