<!-- Converted from core/indexes/index-types/geospatial/2dsphere/create.txt (reStructuredText). Includes are inlined. -->

# Create a 2dsphere Index

2dsphere indexes support geospatial queries on an earth-like sphere. For
example, 2dsphere indexes can:

- Determine points within a specified area.

- Calculate proximity to a specified point.

- Return exact matches on coordinate queries.

To create a 2dsphere index, use the
`db.collection.createIndex()` method and specify the string
`"2dsphere"` as the index type:

```javascript
db.<collection>.createIndex( { <location field> : "2dsphere" } )
```

The values in the `<location field>` must be either:

- GeoJSON objects

- Legacy coordinate pairs

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

The values in the `loc` field are GeoJSON points.

## Procedure

The following operation creates a 2dsphere index on the location field
`loc`:

```javascript
db.places.createIndex( { loc : "2dsphere" } )
```

## Next Steps

After you create a 2dsphere index, you can use the index for geospatial
queries. To learn more, see 2dsphere-index-query.

## Learn More

- 2dsphere-index

- geospatial-queries

- geospatial-restrictions
