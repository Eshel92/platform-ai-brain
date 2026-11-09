<!-- Converted from reference/method/Date.txt (reStructuredText). Includes are inlined. -->

# Date() and Datetime

**`Date()`**

Returns a date either as a string or as a
document-bson-type-date object. The date can contain a date
and a time, known as a *datetime*.

The [BSON specification](http://bsonspec.org/#/specification)
states a `Date` object contains the *UTC datetime*. UTC is
*Coordinated Universal Time*. The UTC datetime stores an unsigned
64-bit integer value, indicating the number of milliseconds after the
Unix epoch (January 1st, 1970 at 00:00:00 UTC).

## Compatibility

You can use `Date()` for deployments hosted in the following
environments:

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas?tck=docs_server): The fully
  managed service for MongoDB deployments in the cloud
- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Syntax

You can specify either of the following formats:

- `Date()` returns the current date as a string in
  `mongosh`.

- `new Date()` returns the current date as a
  document-bson-type-date object. `mongosh`
  wraps the document-bson-type-date object with the
  `ISODate` helper. The `ISODate` is in [UTC](https://en.wikipedia.org/wiki/Coordinated_Universal_Time).

You can specify a particular date by passing an ISO-8601 date string
with a year within the inclusive range `0` through `9999` to the
`new Date()` constructor or the `ISODate()` function. These
functions accept the following formats:

- `new Date("<YYYY-mm-dd>")` returns the `ISODate` with the
  specified date.

- `new Date("<YYYY-mm-ddTHH:MM:ss.sss>")` specifies the datetime in
  the client's local timezone and returns the `ISODate` with the
  specified datetime in UTC. `ss.sss` specifies seconds (`ss`) and
  milliseconds (`.sss`). Milliseconds are set to `0` if omitted.

- `new Date("<YYYY-mm-ddTHH:MM:ss.sssZ>")` specifies the datetime in
  UTC and returns the `ISODate` with the specified datetime in UTC.
  `ss.sss` specifies seconds (`ss`) and milliseconds (`.sss`).
  Milliseconds are set to `0` if omitted.

- `new Date(<integer>)` specifies the datetime as milliseconds
  since the UNIX epoch (Jan 1, 1970), and
  returns the resulting `ISODate` instance.

## Behavior

Internally, document-bson-type-date objects are stored as a signed
64-bit integer representing the number of milliseconds since the Unix
epoch (Jan 1, 1970).

Not all database operations and drivers support the full 64-bit range.
You may safely work with dates with years within the inclusive range
`0` through `9999`.

## Examples

### Use Date in a Query

If no document with `_id` equal to `1` exists in the `products`
collection, the following operation inserts a document with the field
`dateAdded` set to the current date:

```javascript
db.products.updateOne(
   { _id: 1 },
   {
     $set: { item: "apple" },
     $setOnInsert: { dateAdded: new Date() }
   },
   { upsert: true }
)
```

**See also:**

- `$currentDate`
- NOW aggregation variable usage to
  update with aggregation pipeline 

### Return Date as a String

To return the date as a string, use the `Date()` method. For example:

```javascript
var myDateString = Date();
```

### Return Date as `Date` Object

`mongosh` wraps objects of
document-bson-type-date type with the `ISODate` helper.
However, the objects are document-bson-type-date types.

The following example uses `new Date()` to return
a document-bson-type-date object with the specified UTC datetime:

```javascript
var myDate = new Date("2016-05-18T16:00:00Z");
```

**See also:**

- BSON Date
- mongo Shell Date

### Insert and Return `ISODate` Objects

You can specify dates as `ISODate` objects.

The following example creates a `cakeSales` collection with
`ISODate` objects in the `orderDate` field:

```javascript
db.cakeSales.insertMany( [
   { _id: 0, type: "chocolate", orderDate: new ISODate("2020-05-18T14:10:30.123Z") },
   { _id: 1, type: "strawberry", orderDate: new ISODate("2021-03-20T11:30:05Z") },
   { _id: 2, type: "vanilla", orderDate: new ISODate("2021-01-15T06:31:15.456Z") }
] )
```

The following example returns documents where the `orderDate` is less
than the `ISODate` specified in the `$lt` operator:

```javascript
db.cakeSales.find( { orderDate: { $lt: ISODate("2021-02-25T10:03:46.234Z") } } )
```

Example output:

```javascript
[
   {
      _id: 0,
      type: 'chocolate',
      orderDate: ISODate("2020-05-18T14:10:30.123Z")
   },
   {
      _id: 2,
      type: 'vanilla',
      orderDate: ISODate("2021-01-15T06:31:15.456Z")
   }
]
```
