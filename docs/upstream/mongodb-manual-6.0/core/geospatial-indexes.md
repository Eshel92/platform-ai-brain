<!-- Converted from core/geospatial-indexes.txt (reStructuredText). Includes are inlined. -->

# `2d` Index Internals

This document provides a more in-depth explanation of the internals of MongoDB's
`2d` geospatial indexes. This material is not necessary for normal operations
or application development but may be useful for troubleshooting and for
further understanding.

## Calculation of Geohash Values for `2d` Indexes

When you create a geospatial index on legacy coordinate pairs, MongoDB computes geohash values
for the coordinate pairs within the specified location range and then indexes the geohash values.

To calculate a geohash value, recursively divide a two-dimensional map into
quadrants. Then assign each quadrant a two-bit value. For example, a
two-bit representation of four quadrants would be:

```javascript
01  11

00  10
```

These two-bit values (`00`, `01`, `10`, and `11`) represent each
of the quadrants and all points within each quadrant. For a geohash with
two bits of resolution, all points in the bottom left quadrant would
have a geohash of `00`. The top left quadrant would have the geohash
of `01`. The bottom right and top right would have a geohash of `10`
and `11`, respectively.

To provide additional precision, continue dividing each quadrant into
sub-quadrants. Each sub-quadrant would have the geohash value of the
containing quadrant concatenated with the value of the sub-quadrant. The
geohash for the upper-right quadrant is `11`, and the geohash for the
sub-quadrants would be (clockwise from the top left): `1101`,
`1111`, `1110`, and `1100`, respectively.

## Multi-location Documents for `2d` Indexes

**Note:**

in a document, and can express lists of points using
geojson-multipoint embedded documents.

While `2d` geospatial indexes do not support more than one geospatial field
in a document, you can use a multi-key index to index multiple coordinate pairs in
a single document. In the simplest example you may have a field (e.g.
`locs`) that holds an array of coordinates, as in the following
example:

```javascript
db.places.save( {
  locs : [ [ 55.5 , 42.3 ] ,
           [ -74 , 44.74 ] ,
           { lng : 55.5 , lat : 42.3 } ]
} )
```

The values of the array may be either arrays, as in `[ 55.5, 42.3 ]`,
or embedded documents, as in `{ lng : 55.5 , lat : 42.3 }`.

You could then create a geospatial index on the `locs` field, as in
the following:

```javascript
db.places.createIndex( { "locs": "2d" } )
```

You may also model the location data as a field inside of an
embedded document. In this case, the document would contain a field
(e.g. `addresses`) that holds an array of documents where each
document has a field (e.g. `loc:`) that holds location
coordinates. For example:

```javascript
db.records.save( {
  name : "John Smith",
  addresses : [ {
                 context : "home" ,
                 loc : [ 55.5, 42.3 ]
                } ,
                {
                 context : "work",
                 loc : [ -74 , 44.74 ]
                }
              ]
} )
```

You could then create the geospatial index on the `addresses.loc` field as
in the following example:

```javascript
db.records.createIndex( { "addresses.loc": "2d" } )
```
