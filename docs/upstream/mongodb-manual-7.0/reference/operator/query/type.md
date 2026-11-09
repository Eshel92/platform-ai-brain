<!-- Converted from reference/operator/query/type.txt (reStructuredText). Includes are inlined. -->

# $type (query predicate operator)

## Definition

**`$type`**

`$type` selects documents where the *value* of the
`field` is an instance of the specified BSON type(s).
Querying by data type is useful for
unstructured data where data types aren't predictable.

## Compatibility

You can use `$type` for deployments hosted in the following
environments:

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas): The fully
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

For an example, see document-querying-by-multiple-data-types.

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
types.

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

`MinKey` and `MaxKey`
are used in comparison operations and exist primarily for internal use.
For all possible BSON element values, `MinKey` is always the
smallest value, and `MaxKey` is always the greatest value.

Querying for `minKey` or `maxKey` with `$type` only returns
fields that match the special `MinKey` or `MaxKey` values.

For example, the following `data` collection has these documents
with `MinKey` and `MaxKey`:

```javascript
db.data.insertMany( [
   { _id: 1, x: MinKey() },
   { _id: 2, y: MaxKey() }
] )
```

The following query returns the document with `_id: 1`:

```javascript
```

Output:

```javascript
```

The following query returns the document with `_id: 2`:

```javascript
```

Output:

```javascript
```

## Examples

### Querying by Data Type

The examples on this page use data from the sample_mflix dataset. For details on how to load this dataset into your self-managed
MongoDB deployment, see Load the Sample Dataset.
If you made any modifications to the sample databases, you may need to drop and
recreate the databases to run the examples on this page. 

The `movies` collection stores IMDb ratings in the
`imdb.rating` field. Most documents store `imdb.rating` as a
`double`, but some documents store it as an empty `string`
(`""`).

The following queries return documents from 2013 where
`imdb.rating` is the BSON type `string`.

This query specifies the type with the number of the BSON type. 

```javascript
```

Output:

```javascript
```

This query specifies the type with the alias of the BSON type:

```javascript
```

Output:

```javascript
```

The following query uses the `number` alias to return documents
where `imdb.rating` is the BSON type `double`, `int`,
or `long`:

```javascript
```

Output:

```javascript
```

### Querying by Multiple Data Types

The following queries return documents where `imdb.rating` is the BSON
type `string` or `double`. The first query uses numeric aliases and the
second query uses string aliases.

```javascript
```

Output:

```javascript
```

```javascript
```

Output:

```javascript
```

### Querying by Array Type

The `movies` collection stores film genres in the `genres`
field as an array. The following query returns documents where
the `genres` field is an array:

```javascript
```

Output:

```javascript
```

### Querying by MinKey and MaxKey

The folllowing examples use the `restaurants` collection that uses `minKey`
for any grade that is a failing grade:

```javascript
db.restaurants.insertOne( {
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
   name : "Dan's Donuts",
   restaurant_id : "30075445"
} )
```

And `maxKey` for any grade that is the highest passing grade:

```javascript
db.restaurants.insertOne( {
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
} )
```

The following query returns any restaurant whose `grades.grade` field
contains `minKey` *or* is an array containing an element of
the specified type:

```javascript
```

Output:

```javascript
```

The following query returns any restaurant whose `grades.grade` field
contains `maxKey` *or* is an array containing an element of
the specified type:

```javascript
```

Output:

```javascript
```

## Learn More

- faq-developers-query-for-nulls
- `db.collection.find()`
- bson-types
