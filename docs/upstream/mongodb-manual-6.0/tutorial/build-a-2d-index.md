<!-- Converted from tutorial/build-a-2d-index.txt (reStructuredText). Includes are inlined. -->

# Create a `2d` Index

To build a geospatial `2d` index, use the 
`db.collection.createIndex()` method and specify `2d`. Use the
following syntax:

```javascript
db.<collection>.createIndex( { <location field> : "2d" ,
                               <additional field> : <value> } ,
                             { <index-specification options> } )
```

The `2d` index uses the following optional index-specification
options:

```javascript
{ min : <lower bound> , max : <upper bound> ,
  bits : <bit precision> }
```

## Define Location Range for a `2d` Index

By default, a `2d` index assumes longitude and latitude and has boundaries
of -180 **inclusive** and 180 **non-inclusive**. If
documents contain coordinate data outside of the specified range,
MongoDB returns an error.

**Important:** The default boundaries allow applications to insert

documents with invalid latitudes greater than 90 or less than -90.
The behavior of geospatial queries with such invalid points is not
defined.

On `2d` indexes you can change the location range.

You can build a `2d` geospatial index with a location range other than
the default. Use the `min` and `max` options when creating the
index. Use the following syntax:

```javascript
db.collection.createIndex( { <location field> : "2d" } ,
                           { min : <lower bound> , max : <upper bound> } )
```

## Define Location Precision for a `2d` Index

By default, a `2d` index on legacy coordinate pairs uses 26 bits of
precision, which is roughly equivalent to 2 feet or 60 centimeters of
precision using the default range of -180 to 180. Precision is measured
by the size in bits of the geohash values used to store location
data. You can configure geospatial indexes with up to 32 bits of
precision.

Index precision does not affect query accuracy. The actual grid coordinates
are always used in the final query processing. Advantages to lower
precision are a lower processing overhead for insert operations and use
of less space. An advantage to higher precision is that queries scan
smaller portions of the index to return results.

To configure a location precision other than the default, use the
`bits` option when creating the index. Use following syntax:

```javascript
db.<collection>.createIndex( {<location field> : "<index type>"} ,
                             { bits : <bit precision> } )
```

For information on the internals of geohash values, see
geospatial-indexes-geohash.
