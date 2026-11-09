<!-- Converted from reference/operator/query/type.txt (reStructuredText). Includes are inlined. -->

# $type

## Definition

**`$type`**

`$type` selects documents where the *value* of the
`field` is an instance of the specified BSON type(s).
Querying by data type is useful when dealing with highly
unstructured data where data types are not predictable.

## Compatibility

You can use `$type` for deployments hosted in the following
environments:

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas?tck=docs_server): The fully
  managed service for MongoDB deployments in the cloud
- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Syntax

A `$type` expression for a single BSON type has
the following syntax:

```javascript
{ field: { $type: <BSON type> } }
```

You can specify either the number or alias for the BSON
type.

The `$type` expression can also accept an array of BSON
types and has the following syntax:

```javascript
{ field: { $type: [ <BSON type1> , <BSON type2>, ... ] } }
```

The above query matches documents where the `field` value is
any of the listed types. The types specified in the array can be
either numeric or string aliases.

See document-querying-by-multiple-data-types for an example.

document-type-available-types describes the BSON types and
their corresponding numeric and string aliases.

**See also:**

- `$isNumber` - checks if the argument is a number.

- `$type (Aggregation)` - returns the BSON type
  of the argument.

## Behavior

`$type` returns documents where the BSON type of the `field`
matches the BSON type passed to `$type`. 

### Arrays

For documents where `field` is an array, `$type` returns
documents in which at least one array element matches a type passed to
`$type`.

Queries for `$type: "array"` return documents where the field itself is 
an array.

### Available Types

The `$type` operator accepts string aliases
for the BSON types in addition to the numbers corresponding to the BSON
types. [#type0]_

| Type | Number | Alias | Notes |
|---|---|---|---|
| Double | 1 | "double" |  |
| String | 2 | "string" |  |
| Object | 3 | "object" |  |
| Array | 4 | "array" |  |
| Binary data | 5 | "binData" |  |
| Undefined | 6 | "undefined" | Deprecated. |
| ObjectId | 7 | "objectId" |  |
| Boolean | 8 | "bool" |  |
| Date | 9 | "date" |  |
| Null | 10 | "null" |  |
| Regular Expression | 11 | "regex" |  |
| DBPointer | 12 | "dbPointer" | Deprecated. |
| JavaScript | 13 | "javascript" |  |
| Symbol | 14 | "symbol" | Deprecated. |
| 32-bit integer | 16 | "int" |  |
| Timestamp | 17 | "timestamp" |  |
| 64-bit integer | 18 | "long" |  |
| Decimal128 | 19 | "decimal" |  |
| Min key | -1 | "minKey" |  |
| Max key | 127 | "maxKey" |  |

`$type` supports the `number` alias, which matches against
the following BSON types:

- `double`

- `32-bit integer`

- `64-bit integer`

- `decimal`

For examples, see query-type-examples.

**See also:**

`$isNumber`

### MinKey and MaxKey

MinKey and MaxKey
are used in comparison operations and exist primarily for internal use.
For all possible BSON element values, `MinKey` is always the
smallest value while `MaxKey` is always the greatest value.

Querying for  `minKey` or `maxKey` with `$type` only returns fields 
that match the special `MinKey` or `MaxKey` values.

Suppose that the `data` collection has two documents
with `MinKey` and `MaxKey`:

```javascript
db.data.insertMany( [
   { _id : 1, x : { "$minKey" : 1 } },
   { _id : 2, y : { "$maxKey" : 1 } }
] )
```

The following query returns the document with `_id: 1`:

```javascript
db.data.find( { x: { $type: "minKey" } } )
```

The following query returns the document with `_id: 2`:

```javascript
db.data.find( { y: { $type: "maxKey" } } )
```

## Examples

### Querying by Data Type

The `addressBook` contains addresses and zipcodes, where
`zipCode` has `string`, `int`, `double`, and `long`
values:

```javascript
db.addressBook.insertMany( [
      { _id : 1, address : "2030 Martian Way", zipCode : "90698345" },
      { _id : 2, address : "156 Lunar Place", zipCode : 43339374 },
      { _id : 3, address : "2324 Pluto Place", zipCode : NumberLong(3921412) },
      { _id : 4, address : "55 Saturn Ring" , zipCode : NumberInt(88602117) },
      { _id : 5, address : "104 Venus Drive", zipCode : ["834847278", "1893289032"] }
] )
```

The following queries return all documents where `zipCode` is the
BSON type `string` *or* is an array containing an element of
the specified type:

```javascript
db.addressBook.find( { zipCode : { $type : 2 } } );
db.addressBook.find( { zipCode : { $type : "string" } } );
```

These queries return:

```javascript
{ _id : 1, address : "2030 Martian Way", zipCode : "90698345" }
{ _id : 5, address : "104 Venus Drive", zipCode : [ "834847278", "1893289032" ] }
```

The following queries return all documents where `zipCode` is the
BSON type `double` *or* is an array containing an element of
the specified type:

```javascript
db.addressBook.find( { zipCode : { $type : 1 } } );
db.addressBook.find( { zipCode : { $type : "double" } } );
```

These queries return:

```javascript
{ _id : 2, address : "156 Lunar Place", zipCode : 43339374 }
```

The following query uses the `number` alias to return documents where
`zipCode` is the BSON type `double`, `int`, or `long`
*or* is an array containing an element of the specified types:

```javascript
db.addressBook.find( { zipCode : { $type : "number" } } )
```

These queries return:

```javascript
{ _id : 2, address : "156 Lunar Place", zipCode : 43339374 }
{ _id : 3, address : "2324 Pluto Place", zipCode : NumberLong(3921412) }
{ _id : 4, address : "55 Saturn Ring", zipCode : 88602117 }
```

### Querying by Multiple Data Types

The `grades` collection contains names and averages, where
`classAverage` has `string`, `int`, and `double` values:

```javascript
db.grades.insertMany( [
      { _id : 1, name : "Alice King" , classAverage : 87.333333333333333 },
      { _id : 2, name : "Bob Jenkins", classAverage : "83.52" },
      { _id : 3, name : "Cathy Hart", classAverage: "94.06" },
      { _id : 4, name : "Drew Williams" , classAverage : NumberInt("93") }
] )
```

The following queries return all documents where `classAverage` is the
BSON type `string` or `double` *or* is an array containing
an element of the  specified types. The first query uses numeric aliases
while the second query uses string aliases.

```javascript
db.grades.find( { classAverage : { $type : [ 2 , 1 ] } } );
db.grades.find( { classAverage : { $type : [ "string" , "double" ] } } );
```

These queries return the following documents:

```javascript
{ _id : 1, name : "Alice King", classAverage : 87.33333333333333 }
{ _id : 2, name : "Bob Jenkins", classAverage : "83.52" }
{ _id : 3, name : "Cathy Hart", classAverage : "94.06" } 
```

### Querying by MinKey and MaxKey

The `restaurants` collection uses `minKey` for any grade that is a
failing grade:

```javascript
db.restaurants.insertOne( [ 
   {
      _id: 1,
      address: {
         building: "230",
         coord: [ -73.996089, 40.675018 ],
         street: "Huntington St",
         zipcode: "11231"
      },
      borough: "Brooklyn",
      cuisine: "Bakery",
      grades: [
         { date : new Date(1393804800000), grade : "C", score : 15 },
         { date : new Date(1378857600000), grade : "C", score : 16 },
         { date : new Date(1358985600000), grade : MinKey(), score : 30 },
         { date : new Date(1322006400000), grade : "C", score : 15 }
      ],
      name : "Dirty Dan's Donuts",
      restaurant_id : "30075445"
   }
] )
```

And `maxKey` for any grade that is the highest passing grade:

```javascript
db.restaurants.insertOne( [
   {
      _id : 2,
      address : {
         building : "1166",
         coord : [ -73.955184, 40.738589 ],
         street : "Manhattan Ave",
         zipcode : "11222"
      },
      borough: "Brooklyn",
      cuisine: "Bakery",
      grades: [
         { date : new Date(1393804800000), grade : MaxKey(), score : 2 },
         { date : new Date(1378857600000), grade : "B", score : 6 },
         { date : new Date(1358985600000), grade : MaxKey(), score : 3 },
         { date : new Date(1322006400000), grade : "B", score : 5 }
      ],
      name : "Dainty Daisey's Donuts",
      restaurant_id : "30075449"
   }
] )
```

The following query returns any restaurant whose `grades.grade` field
contains `minKey` *or* is an array containing an element of
the specified type:

```javascript
db.restaurants.find(
   { "grades.grade" : { $type : "minKey" } }
)
```

This returns the following results: 

```javascript
{
   _id : 1,
   address : {
      building : "230",
      coord : [ -73.996089, 40.675018 ],
      street : "Huntington St",
      zipcode : "11231"
   },
   borough : "Brooklyn",
   cuisine : "Bakery",
   grades : [
      { date : ISODate("2014-03-03T00:00:00Z"), grade : "C", score : 15 },
      { date : ISODate("2013-09-11T00:00:00Z"), grade : "C", score : 16 },
      { date : ISODate("2013-01-24T00:00:00Z"), grade : { "$minKey" : 1 }, score : 30 },
      { date : ISODate("2011-11-23T00:00:00Z"), grade : "C", score : 15 }
   ],
   name : "Dirty Dan's Donuts",
   restaurant_id : "30075445"
}
```

The following query returns any restaurant whose `grades.grade` field
contains `maxKey` *or* is an array containing an element of
the specified type:

```javascript
db.restaurants.find(
   { "grades.grade" : { $type : "maxKey" } }
)
```

This returns the following results:

```javascript
{
   _id : 2,
   address : {
      building : "1166",
      coord : [ -73.955184, 40.738589 ],
      street : "Manhattan Ave",
      zipcode : "11222"
   },
   borough : "Brooklyn",
   cuisine : "Bakery",
   grades : [
      { date : ISODate("2014-03-03T00:00:00Z"), grade : { "$maxKey" : 1 }, score : 2 },
      { date : ISODate("2013-09-11T00:00:00Z"), grade : "B", score : 6 },
      { date : ISODate("2013-01-24T00:00:00Z"), grade : { "$maxKey" : 1 }, score : 3 },
      { date : ISODate("2011-11-23T00:00:00Z"), grade : "B", score : 5 }
   ],
   name : "Dainty Daisey's Donuts",
   restaurant_id : "30075449"
}
```

   

## Querying by Array Type

A collection named `sensorReading` contains the following documents:

```javascript
db.sensorReading.insertMany( [
   { _id : 1, readings : [ 25, 23, [ "Warn: High Temp!", 55 ], [ "ERROR: SYSTEM SHUTDOWN!", 66 ] ] },
   { _id : 2, readings : [ 25, 25, 24, 23 ] },
   { _id : 3, readings : [ 22, 24, [] ] },
   { _id : 4, readings : [] },
   { _id : 5, readings : 24 }
] )
```

The following query returns any document in which the `readings`
field is an array, empty or non-empty.

```javascript
db.SensorReading.find( { readings : { $type: "array" } } )
```

The above query returns the following documents:

```javascript
{
   _id : 1,
   readings : [
      25,
      23,
      [ "Warn: High Temp!", 55 ],
      [ "ERROR: SYSTEM SHUTDOWN!", 66 ]
   ]
},
{
   _id : 2,
   readings : [ 25, 25, 24, 23 ]
},
{
   _id : 3,
   readings : [ 22, 24, [] ]
},
{
   _id : 4,
   readings : []
}
```

In the documents with `_id : 1`, `_id : 2`, `_id : 3`, and
`_id : 4`, the `readings` field is an array. 

## Additional Information

- /tutorial/query-for-null-fields

- `db.collection.find()`

- BSON Types.
