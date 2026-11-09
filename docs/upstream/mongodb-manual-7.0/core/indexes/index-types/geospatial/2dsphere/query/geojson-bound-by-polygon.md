<!-- Converted from core/indexes/index-types/geospatial/2dsphere/query/geojson-bound-by-polygon.txt (reStructuredText). Includes are inlined. -->

# Query for Locations Bound by a Polygon

You can query for location data within the perimeter of a specified
polygon.

To query for location data within a perimeter, use the
`$geoWithin` operator and specify the coordinates of the
polygon's vertices:

```javascript
db.<collection>.find( {
   <location field> : {
      $geoWithin : {
         $geometry : {
            type : "Polygon",
            coordinates : [ <coordinates> ]
         }
       }
    }
 } )
```

## About this Task

- The values in the field you query with the `$geoWithin` operator
  must be in GeoJSON format.

- .. include:: /includes/indexes/geojson-lat-long.rst

- When you specify Polygon `coordinates`, the first and last
  coordinates in the array must be the same. This closes the bounds of
  the polygon.

- .. include:: /includes/indexes/geospatial-index-not-required.rst

## Before You Begin

Create a `places` collection that contains these documents:

```javascript
db.places.insertMany( [
   {
      loc: { type: "Point", coordinates: [ -73.97, 40.77 ] },
      name: "Central Park",
      category : "Park"
   },
   {
      loc: { type: "Point", coordinates: [ -73.88, 40.78 ] },
      name: "La Guardia Airport",
      category: "Airport"
   },
   {
      loc: { type: "Point", coordinates: [ -1.83, 51.18 ] },
      name: "Stonehenge",
      category : "Monument"
   }
] )
```

## Procedure

Use `$geoWithin` to query the collection. The following `$geoWithin`
query specifies a polygon with four vertices (a rectangle) and returns
points within that polygon:

```javascript
db.places.find( {
   loc: {
      $geoWithin: {
         $geometry: {
            type: "Polygon",
            coordinates: [ [
               [ -73.95, 40.80 ],
               [ -73.94, 40.79 ],
               [ -73.97, 40.76 ],
               [ -73.98, 40.76 ],
               [ -73.95, 40.80 ]
            ] ]
          }
      }
   }
} )
```

Output:

```javascript
[
  {
    _id: ObjectId("63a4a8d67348ebdcd0a061f0"),
    loc: { type: 'Point', coordinates: [ -73.97, 40.77 ] },
    name: 'Central Park',
    category: 'Park'
  }
]
```

## Learn More

- `$geoWithin`

- geojson-polygon

- geospatial-restrictions
