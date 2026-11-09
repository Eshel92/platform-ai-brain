<!-- Converted from core/indexes/index-types/index-geospatial.txt (reStructuredText). Includes are inlined. -->

# Geospatial Indexes

Geospatial indexes support queries on data stored as GeoJSON objects or legacy coordinate pairs. You can use geospatial indexes to improve
performance for queries on geospatial data or to run certain 
geospatial queries.

MongoDB provides two types of geospatial indexes:

- 2dsphere-index, which support queries that interpret 
  geometry on a sphere.

- 2d-index, which support queries that interpret geometry 
  on a flat surface.

To learn more about geospatial data and query operations, 
see /geospatial-queries.

## Use Cases

If your application frequently queries a field that contains 
geospatial data, you can create a geospatial index to improve 
performance for those queries.

Certain query operations require a geospatial index.
If you want to query with the `$near` or `$nearSphere` 
operators or the `$geoNear` aggregation stage, you must create 
a geospatial index. For details, see geospatial-operators and 
geospatial-aggregation.

For example, consider a `subway` collection with documents containing
a `location` field, which specifies the coordinates of subway stations 
in a city. You often run queries with the `$geoWithin` operator 
to return a list of stations within a specific area. To improve 
performance for this query, you can create a geospatial index 
on the `location` field. After creating the index, you can query 
using the `$near` operator to return a list of nearby stations, 
sorted from nearest to farthest.

## Get Started

To create a geospatial index and run geospatial queries, see:

- 2dsphere-index-create
- 2dsphere-index-query
- 2d-index-create
- 2d-index-query

## Details

This section describes details about geospatial indexes.

### Sharded Collections

You can't use a geospatial index as a shard key when sharding a
collection. However, you can create a geospatial index
on a sharded collection using a different field as the shard key.

You can use geospatial query operators 
and aggregation stages to query for 
geospatial data on sharded collections.

### Covered Queries

Geospatial indexes can't cover a query.

### Spherical Queries

Using a `2d` index for queries on spherical data
can return incorrect results or an error. For example, 
`2d` indexes don't support spherical queries that wrap 
around the poles.

However, you can use the `2dsphere` index for both spherical queries 
*and* two-dimensional queries. For two-dimensional queries, the 
`2dsphere` index converts data stored as legacy coordinate pairs to 
the GeoJSON Point type.

## Learn More

For sample geospatial query operations, see 
Geospatial Query Examples.
