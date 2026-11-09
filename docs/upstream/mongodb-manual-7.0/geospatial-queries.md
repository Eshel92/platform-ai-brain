<!-- Converted from geospatial-queries.txt (reStructuredText). Includes are inlined. -->

# Geospatial Queries

     

MongoDB supports query operations on geospatial data. This section
introduces MongoDB geospatial features.

## Geospatial Data

In MongoDB, you can store geospatial data as GeoJSON
objects or as legacy coordinate pairs.

### GeoJSON Objects

To calculate geometry over an Earth-like sphere, store your location
data as GeoJSON objects.

To specify GeoJSON data, use an embedded document with:

- a field named `type` that specifies the GeoJSON object
  type, and

- a field named `coordinates` that specifies the object's
  coordinates. 

```javascript
<field>: { type: <GeoJSON type> , coordinates: <coordinates> }
```

**Important:**

If specifying latitude and longitude coordinates, list the
**longitude** first, and then **latitude**.

- Valid longitude values are between `-180` and `180`, both
  inclusive.

- Valid latitude values are between `-90` and `90`, both
  inclusive.

For example, to specify a GeoJSON Point:

```javascript
location: {
      type: "Point",
      coordinates: [-73.856077, 40.848447]
}
```

For a list of the GeoJSON objects supported in MongoDB as well as
examples, see GeoJSON objects.

MongoDB geospatial queries on GeoJSON objects calculate on a sphere;
MongoDB uses the WGS84 reference system for geospatial
queries on GeoJSON objects.

### Legacy Coordinate Pairs

Use legacy coordinate pairs for flat (Euclidean) calculations with a
geo-2d index. To perform spherical calculations, convert legacy
pairs to a GeoJSON `Point` and use a geo-2dsphere index.

To specify data as legacy coordinate pairs, you can use either an
array (*preferred*) or an embedded document.

Array:

  ```javascript
  <field>: [ <x>, <y> ]
  ```

  When you use longitude and latitude, list longitude first, then latitude:

  ```javascript
  <field>: [ <longitude>, <latitude> ]
  ```

  - Valid longitude values are between `-180` and `180`, both
    inclusive.

  - Valid latitude values are between `-90` and `90`, both
    inclusive.

Embedded document:

  ```javascript
  <field>: { <field1>: <x>, <field2>: <y> }
  ```

  If you use longitude and latitude, the first field must be longitude and
  the second must be latitude:

  ```javascript
  <field>: { <field1>: <longitude>, <field2>: <latitude> }
  ```

  - Valid longitude values are between `-180` and `180`, both
    inclusive.

  - Valid latitude values are between `-90` and `90`, both
    inclusive.

Use arrays for legacy coordinate pairs because some languages 
do not preserve object field ordering.

## Geospatial Indexes

Geospatial indexes support queries on data stored as GeoJSON objects or legacy coordinate pairs. You can use geospatial indexes to improve
performance for queries on geospatial data or to run certain 
geospatial queries.

MongoDB provides two types of geospatial indexes:

- 2dsphere-index, which support queries that interpret 
  geometry on a sphere.

- 2d-index, which support queries that interpret geometry 
  on a flat surface.

For more information on geospatial indexes, see
geospatial-index.

## Geospatial Queries

**Note:**

Using a `2d` index for queries on spherical data
can return incorrect results or an error. For example, 
`2d` indexes don't support spherical queries that wrap 
around the poles.

### Geospatial Query Operators

MongoDB provides the following geospatial query operators:

| Name | Description |
|---|---|
| `$geoIntersects` | Selects geometries that intersect with a GeoJSON geometry. The 2dsphere index supports `$geoIntersects`. |
| `$geoWithin` | Selects geometries within a bounding GeoJSON geometry. The 2dsphere and 2d indexes support `$geoWithin`. |
| `$near` | Returns geospatial objects in proximity to a point. Requires a geospatial index. The `2dsphere` and `2d` indexes support `$near`. |
| `$nearSphere` | Returns geospatial objects in proximity to a point on a sphere. Requires a geospatial index. The `2dsphere` and `2d` indexes support `$nearSphere`. |

For more details, including examples, see the individual reference page.

### Geospatial Aggregation Stage

MongoDB provides the following geospatial aggregation pipeline
stage:

| Stage | Description |
|---|---|
| `$geoNear` | .. include:: /includes/extracts/geoNear-stage-toc-description.rst `$geoNear` requires a geospatial index. |

For more details, including examples, see `$geoNear`
reference page.

## Geospatial Models

MongoDB geospatial queries can interpret geometry on a flat surface or
a sphere.

`2dsphere` indexes support only spherical queries (that is, queries
that interpret geometries on a spherical surface).

`2d` indexes support flat queries (that is, queries that interpret
geometries on a flat surface) and some spherical queries. While `2d`
indexes support some spherical queries, the use of `2d` indexes for
these spherical queries can result in error. If possible, use
`2dsphere` indexes for spherical queries.

The following table lists the geospatial query operators, supported
query, used by each geospatial operations:

| Operation | Spherical/Flat Query | Notes |
|---|---|---|
| `$near` (GeoJSON centroid point in this line and the following line, 2dsphere index) | Spherical | See also the `$nearSphere` operator, which provides the same functionality when used with GeoJSON and a 2dsphere index. |
| `$near` (legacy coordinates, 2d index) | Flat |  |
| `$nearSphere` (GeoJSON point, 2dsphere index) | Spherical | Provides the same functionality as `$near` operation that uses GeoJSON point and a 2dsphere index. For spherical queries, it may be preferable to use `$nearSphere` which explicitly specifies the spherical queries in the name rather than `$near` operator. |
| `$nearSphere` (legacy coordinates, 2d index) | Spherical | Use GeoJSON points instead. |
| `$geoWithin` : { `$geometry`: ... } | Spherical |  |
| `$geoWithin` : { `$box`: ... } | Flat |  |
| `$geoWithin` : { `$polygon`: ... } | Flat |  |
| `$geoWithin` : { `$center`: ... } | Flat |  |
| `$geoWithin` : { `$centerSphere`: ... } | Spherical |  |
| `$geoIntersects` | Spherical |  |
| `$geoNear` aggregation stage (2dsphere index) | Spherical |  |
| `$geoNear` aggregation stage (2d index) | Flat |  |

## Perform Geospatial Queries in Atlas

**filter-bar:**

You can use the MongoDB Atlas UI
to perform geospatial queries in Atlas. 

**Step 1: Create an index**

If your geospatial collection does not already have a geospatial
index, you must create one.

1. Select the database for the collection.

   The main panel and Namespaces on the left side 
   list the collections in the database.

#. Select the collection.

   Select the collection that contains your geospatial data on 
   the left-hand side or in the main panel. The main panel displays 
   the Find, Indexes, and 
   Aggregation views.

#. Select the Index view.

   When you open the Index view, Atlas
   displays any indexes that exist on the collection.

#. Define the Index for the geo Type

   Press the Create Index button. 

   Define a geo Type index. Refer to 
   How to Index GeoJSON Objects.

**Step 2: Query the geospatial data**

1. Select the Find view.

   From the collection that contains your geospatial
   data, select the Find tab to view your geospatial 
   collection.

#. Enter a query.

   Enter a query in the Filter text box. Use
   any of the geospatial query operators to perform the relevant query
   on your geospatial data. A geospatial query might resemble:

   ```javascript
   { 
     "coordinates": { 
       $geoWithin: { 
         $geometry: { 
           type: "Polygon", 
           coordinates: [ 
             [ 
               [-80.0, 10.00], [ -80.0, 9.00], [ -79.0, 9.0], [ -79.0, 10.00 ], [ -80.0, 10.0 ] 
             ] 
           ] 
         } 
       } 
     } 
   }
   ```

#. Press the Apply button.

   Press the Apply button to apply your query.
   Atlas filters the geospatial data to show only documents
   that match your geospatial query.

**aggregation:**

You can create and execute aggregation pipelines to perform geospatial
queries in the MongoDB Atlas UI.

**Step 1: Access the aggregation pipeline builder**

1. Select the database for the collection.

   The main panel and Namespaces on the left side list the
   collections in the database.

#. Select the collection.

   Select the collection that contains your geospatial data on 
   the left-hand side or in the main panel. The main panel displays 
   the Find, Indexes, and 
   Aggregation views.

#. Select the Aggregation view.

   When you first open the Aggregation view, Atlas
   displays an empty aggregation pipeline.

**Step 2: Create your geospatial query aggregation pipeline**

1. Select an aggregation stage.

   Select an aggregation stage from the Select dropdown in
   the bottom-left panel.

   The toggle to the right of the dropdown dictates whether the
   stage is enabled.

   Use the `$geoNear` stage to perform geospatial
   queries in your aggregation pipeline.

#. Fill in your aggregation stage.

   Fill in your stage with the appropriate values. 
   If Comment Mode is 
   enabled, the pipeline builder provides syntactic guidelines for 
   your selected stage. 

   As you modify your stage, Atlas updates the preview documents on
   the right based on the results of the current stage.

   Your `$geoNear` stage may resemble:

   ```javascript
   {
     near: { type: "Point", coordinates: [ -73.9667, 40.78 ] },
     spherical: true,
     query: { category: "Parks" },
     distanceField: "calcDistance"
   }
   ```

#. Run other pipeline stages as needed.

   Add stages as needed to complete your aggregation pipeline. 
   You might add `$out` or 
   `$merge` to write the results to a 
   view or the current collection.

## Examples

The examples on this page use data from the sample_mflix dataset. For details on how to load this dataset into your self-managed
MongoDB deployment, see Load the Sample Dataset.
If you made any modifications to the sample databases, you may need to drop and
recreate the databases to run the examples on this page. 

The `sample_mflix.theaters` collection has a `2dsphere` index.
The following query uses the `$near` operator to return
documents sorted from nearest to farthest. The query returns
documents at least 1000 meters and at most 100000 meters from
the specified GeoJSON point:

```javascript
```

Output:

```javascript
```

The following operation uses the `$geoNear` aggregation
operation to return documents that match the query filter
`{ "location.address.state": "NY" }`, sorted in order of nearest
to farthest to the specified GeoJSON point:

```javascript
```

Output:

```javascript
```
