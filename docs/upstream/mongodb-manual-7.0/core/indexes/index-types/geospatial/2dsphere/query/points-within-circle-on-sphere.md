<!-- Converted from core/indexes/index-types/geospatial/2dsphere/query/points-within-circle-on-sphere.txt (reStructuredText). Includes are inlined. -->

# Query for Locations within a Circle on a Sphere

You can query for location data within a circle on the surface of a
sphere. Use these queries to return data within a [spherical cap](https://en.wikipedia.org/w/index.php?title=Spherical_cap&oldid=1107980309).

To query for location data within a circle on a sphere, use
`$geoWithin` with the `$centerSphere` operator. In the
`$centerSphere` operator, specify the coordinates and radius of the
circle to query within:

```javascript
db.<collection>.find( {
   <location field> : {
      $geoWithin : {
         $centerSphere: [
            [ <longitude>, <latitude> ],
            <radius>
         ]
       }
    }
 } )
```

## About this Task

- .. include:: /includes/indexes/geojson-lat-long.rst

- In the `$centerSphere` operator, specify the circle's radius in
  **radians**. To convert other units to and from radians,
  see calculate-distance-spherical-geometry.

  - This example calculates distance in kilometers. To convert
    kilometers to radians, divide the kilometer value by `6378.1`.

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

To query the collection, use `$geoWithin` with the `$centerSphere`
operator:

```javascript
db.places.find( {
   loc: {
      $geoWithin: {
         $centerSphere: [
            [ -1.76, 51.16 ],
            10 / 6378.1
         ]
      }
   }
} )
```

The query returns documents where the `loc` field is within a
10 kilometer radius of a point at longitude `-1.76`, latitude
`51.16`.

Output:

```javascript
[
   {
     _id: ObjectId("63fd205e4a08b5e248c03e32"),
     loc: { type: 'Point', coordinates: [ -1.83, 51.18 ] },
     name: 'Stonehenge',
     category: 'Monument'
   }
]
```

## Learn More

- `$geoWithin`

- `$centerSphere`

- 2dsphere-query-geojson-objects-polygon

- 2dsphere-query-intersection

- 2dsphere-query-geojson-proximity

- geospatial-restrictions
