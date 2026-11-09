<!-- Converted from tutorial/query-a-geohaystack-index.txt (reStructuredText). Includes are inlined. -->

# Query a Haystack Index

**Important:** Removed in MongoDB 5.0

MongoDB 5.0 removes the deprecated geoHaystack index and `geoSearch` command. Use a
2d index with `$geoNear` or one of the
supported geospatial query operators
instead.

Upgrading your MongoDB instance to 5.0 and setting
featureCompatibilityVersion to `5.0` will delete any
pre-existing geoHaystack indexes.

   
A haystack index is a special `2d` geospatial index that is optimized
to return results over small areas. To create a haystack index see
geospatial-indexes-haystack-index.

To query a haystack index, use the `geoSearch` command. You
must specify both the coordinates and the additional
field to `geoSearch`. For example, to return all documents
with the value `restaurant` in the `type` field near the example
point, the command would resemble:

```javascript
db.runCommand( { geoSearch : "places" ,
                 search : { type: "restaurant" } ,
                 near : [-74, 40.74] ,
                 maxDistance : 10 } )
```

**Note:**

Haystack indexes are not suited to queries for the complete list of
documents closest to a particular location. The closest documents
could be more distant compared to the bucket size.

**Note:**

Spherical query operations
are not currently supported by haystack indexes.

The `find()` method cannot access the
haystack index.
