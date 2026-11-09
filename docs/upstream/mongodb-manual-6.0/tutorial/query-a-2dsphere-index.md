<!-- Converted from tutorial/query-a-2dsphere-index.txt (reStructuredText). Includes are inlined. -->

# Query a `2dsphere` Index

The following sections describe queries supported by the `2dsphere` index.

## GeoJSON Objects Bounded by a Polygon

The `$geoWithin` operator queries for location data found
within a GeoJSON polygon. Your location
data must be stored in GeoJSON format. Use the following syntax:

```javascript
db.<collection>.find( { <location field> :
                         { $geoWithin :
                           { $geometry :
                             { type : "Polygon" ,
                               coordinates : [ <coordinates> ]
                      } } } } )
```

The following example selects all points and shapes that
exist entirely within a GeoJSON polygon:

```javascript
db.places.find( { loc :
                  { $geoWithin :
                    { $geometry :
                      { type : "Polygon" ,
                        coordinates : [ [
                                          [ 0 , 0 ] ,
                                          [ 3 , 6 ] ,
                                          [ 6 , 1 ] ,
                                          [ 0 , 0 ]
                                        ] ]
                } } } } )
```

## Intersections of GeoJSON Objects

The `$geoIntersects` operator queries for locations that
intersect a specified GeoJSON object. A location intersects the object
if the intersection is non-empty. This includes documents that have a
shared edge.

The `$geoIntersects` operator uses the following syntax:

```javascript
db.<collection>.find( { <location field> :
                         { $geoIntersects :
                           { $geometry :
                             { type : "<GeoJSON object type>" ,
                               coordinates : [ <coordinates> ]
                      } } } } )
```

The following example uses `$geoIntersects` to select all
indexed points and shapes that intersect with the polygon defined by the
`coordinates` array.

```javascript
db.places.find( { loc :
                  { $geoIntersects :
                    { $geometry :
                      { type : "Polygon" ,
                        coordinates: [ [
                                         [ 0 , 0 ] ,
                                         [ 3 , 6 ] ,
                                         [ 6 , 1 ] ,
                                         [ 0 , 0 ]
                                       ] ]
                } } } } )
```

## Proximity to a GeoJSON Point

Proximity queries return the points closest to the defined point and
sorts the results by distance. A proximity query on GeoJSON data
requires a `2dsphere` index.

To query for proximity to a GeoJSON point, use either the
`$near` operator. Distance is in meters.

The `$near` uses the following syntax:

```javascript
db.<collection>.find( { <location field> :
                         { $near :
                           { $geometry :
                              { type : "Point" ,
                                coordinates : [ <longitude> , <latitude> ] } ,
                             $maxDistance : <distance in meters>
                      } } } )
```

For examples, see `$near`.

See also the `$nearSphere` operator and the `$geoNear`
aggregation pipeline stage.

## Points within a Circle Defined on a Sphere

To select all grid coordinates in a "spherical cap" on a sphere, use
`$geoWithin` with the `$centerSphere` operator.
Specify an array that contains:

- The grid coordinates of the circle's center point

- The circle's radius measured in radians. To calculate radians, see
  /tutorial/calculate-distances-using-spherical-geometry-with-2d-geospatial-indexes.

Use the following syntax:

```javascript
db.<collection>.find( { <location field> :
                         { $geoWithin :
                           { $centerSphere :
                              [ [ <x>, <y> ] , <radius> ] }
                      } } )
```

The following example queries grid coordinates and returns all
documents within a 10 mile radius of longitude `88 W` and latitude
`30 N`. The example converts the distance, 10 miles, to radians by
dividing by the approximate equatorial radius of the earth, 3963.2 miles:

```javascript
db.places.find( { loc :
                  { $geoWithin :
                    { $centerSphere :
                       [ [ -88 , 30 ] , 10 / 3963.2 ]
                } } } )
```
