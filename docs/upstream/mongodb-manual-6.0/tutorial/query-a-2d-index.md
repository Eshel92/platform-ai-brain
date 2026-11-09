<!-- Converted from tutorial/query-a-2d-index.txt (reStructuredText). Includes are inlined. -->

# Query a `2d` Index

The following sections describe queries supported by the `2d` index.

## Points within a Shape Defined on a Flat Surface

To select all legacy coordinate pairs found within a given shape on a flat
surface, use the `$geoWithin` operator along with a shape
operator. Use the following syntax:

```javascript
db.<collection>.find( { <location field> :
                         { $geoWithin :
                            { $box|$polygon|$center : <coordinates>
                      } } } )
```

The following queries for documents within a rectangle defined by ``[ 0
, 0 ]` at the bottom left corner and by `[ 100 , 100 ]`` at the top
right corner.

```javascript
db.places.find( { loc :
                  { $geoWithin :
                     { $box : [ [ 0 , 0 ] ,
                                [ 100 , 100 ] ]
                 } } } )
```

The following queries for documents that are within the circle centered
on `[ -74 , 40.74 ]` and with a radius of `10`:

```javascript
db.places.find( { loc: { $geoWithin :
                          { $center : [ [-74, 40.74 ] , 10 ]
                } } } )
```

For syntax and examples for each shape, see the following:

- `$box`

- `$polygon`

- `$center` (defines a circle)

## Points within a Circle Defined on a Sphere

MongoDB supports rudimentary spherical queries on flat `2d` indexes for
legacy reasons. In general, spherical calculations should use a `2dsphere`
index, as described in /core/2dsphere.

To query for legacy coordinate pairs in a "spherical cap" on a sphere,
use `$geoWithin` with the `$centerSphere` operator.
Specify an array that contains:

- The grid coordinates of the circle's center point

- The circle's radius measured in radians. To calculate radians, see
  /tutorial/calculate-distances-using-spherical-geometry-with-2d-geospatial-indexes.

Use the following syntax:

```javascript
db.<collection>.find( { <location field> :
                         { $geoWithin :
                            { $centerSphere : [ [ <x>, <y> ] , <radius> ] }
                      } } )
```

The following example query returns all documents within a 10-mile
radius of longitude `88 W` and latitude `30 N`. The example
converts distance to radians by dividing distance by the approximate
equatorial radius of the earth, 3963.2 miles:

```javascript
db.<collection>.find( { loc : { $geoWithin :
                                 { $centerSphere :
                                    [ [ 88 , 30 ] , 10 / 3963.2 ]
                      } } } )
```

## Proximity to a Point on a Flat Surface

Proximity queries return the legacy coordinate pairs closest to the
defined point and sort the results by distance. Use either the
`$near` operator. The operator requires a `2d` index.

The `$near` operator uses the following syntax:

```javascript
db.<collection>.find( { <location field> :
                         { $near : [ <x> , <y> ]
                      } } )
```

For examples, see `$near`.

## Exact Matches on a Flat Surface

You cannot use a `2d` index to return an exact match for a
coordinate pair. Use a scalar, ascending or descending, index on a
field that stores coordinates to return exact matches. 

In the following example, the `find()`
operation will return an exact match on a location if you have a ``{
'loc': 1}`` index:

```javascript
db.<collection>.find( { loc: [ <x> , <y> ] } )
```

This query will return any documents with the value of `[ <x> , <y> ]`.
