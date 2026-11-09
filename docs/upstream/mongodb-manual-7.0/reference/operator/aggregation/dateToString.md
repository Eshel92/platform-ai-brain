<!-- Converted from reference/operator/aggregation/dateToString.txt (reStructuredText). Includes are inlined. -->

# $dateToString (expression operator)

## Definition

**`$dateToString`**

Converts a date object to a string according to a user-specified
format.

## Compatibility

You can use `$dateToString` for deployments hosted in the following
environments:

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas): The fully
  managed service for MongoDB deployments in the cloud
- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Syntax

The `$dateToString` expression has the following
operator expression syntax:

```javascript
{ $dateToString: {
    date: <dateExpression>,
    format: <formatString>,
    timezone: <tzExpression>,
    onNull: <expression>
} }
```

The `$dateToString` takes a document with the following fields:

| Field | Description |
|---|---|
| `date` | .. versionchanged:: 3.6 The date to convert to string. `<dateExpression>` must be a valid expression that resolves to a Date, a Timestamp, or an ObjectID. |
| `format` | Optional. The date format specification. `<formatString>` can be any string literal, containing 0 or more format specifiers. For a list of specifiers available, see format-specifiers. If unspecified, `$dateToString` uses `"%Y-%m-%dT%H:%M:%S.%LZ"` as the default format. |
| `timezone` | .. include:: /includes/fact-timezone-description.rst |
| `onNull` | Optional. The value to return if the `date` is null or missing. The arguments can be any valid expression. If unspecified, `$dateToString` returns null if the `date` is null or missing. |

**See also:**

- `$toString`
- `$convert`

## Format Specifiers

The following format specifiers are available for use in the
`<formatString>`:

* - Specifiers
  - Description
  - Possible Values

* - `%b`
  - Abbreviated month name (3 letters)

    **New in version:** 7.0

  - `jan`-`dec`

* - `%B`
  - Full month name

    **New in version:** 7.0

  - `january`-`december`

* - `%d`
  - Day of month (2 digits, zero padded)
  - `01`-`31`

* - `%G`

  - Year in ISO 8601 format
  - `0000`-`9999`

* - `%H`
  - Hour (2 digits, zero padded, 24-hour clock)
  - `00`-`23`

* - `%j`
  - Day of year (3 digits, zero padded)
  - `001`-`366`

* - `%L`
  - Millisecond (3 digits, zero padded)
  - `000`-`999`

* - `%m`
  - Month (2 digits, zero padded)
  - `01`-`12`

* - `%M`
  - Minute (2 digits, zero padded)
  - `00`-`59`

* - `%S`
  - Second (2 digits, zero padded)
  - `00`-`60`

* - `%u`
  - Day of week number in ISO 8601 format (1-Monday, 7-Sunday)
  - `1`-`7`

* - `%U`
  - Week of year (2 digits, zero padded)
  - `00`-`53`

* - `%V`

  - Week of Year in ISO 8601 format
  - `01`-`53`

* - `%w`
  - Day of week (1-Sunday, 7-Saturday)
  - `1`-`7`

* - `%Y`
  - Year (4 digits, zero padded)
  - `0000`-`9999`

* - `%z`

  - The timezone offset from UTC.
  - `+/-[hh][mm]`

* - `%Z`

  - The minutes offset from UTC as a number. For example, if the
    timezone offset (`+/-[hhmm]`) was `+0445`, the minutes
    offset is `+285`.
  - `+/-mmm`

* - `%%`
  - Percent Character as a Literal
  - `%`

## Example

Consider a `sales` collection with the following document:

```javascript
 :copyable: true

 db.sales.insertOne(
  {
   "_id" : 1,
   "item" : "abc",
   "price" : 10,
   "quantity" : 2,
   "date" : ISODate("2014-01-01T08:15:39.736Z")
  } 
)
```

The following aggregation uses `$dateToString` to
return the `date` field as formatted strings:

```javascript
db.sales.aggregate(
   [
     {
       $project: {
          yearMonthDayUTC: { $dateToString: { format: "%Y-%m-%d", date: "$date" } },
          timewithOffsetNY: { $dateToString: { format: "%H:%M:%S:%L%z", date: "$date", timezone: "America/New_York"} },
          timewithOffset430: { $dateToString: { format: "%H:%M:%S:%L%z", date: "$date", timezone: "+04:30" } },
          minutesOffsetNY: { $dateToString: { format: "%Z", date: "$date", timezone: "America/New_York" } },
          minutesOffset430: { $dateToString: { format: "%Z", date: "$date", timezone: "+04:30" } },
          abbreviated_month: { $dateToString: {format: "%b", date: "$date", timezone: "+04:30" } },
          full_month: { $dateToString: { format: "%B", date: "$date", timezone: "+04:30" } }
       }
     }
   ]
)
```

The operation returns the following result:

```javascript
{
   "_id" : 1,
   "yearMonthDayUTC" : "2014-01-01",
   "timewithOffsetNY" : "03:15:39:736-0500",
   "timewithOffset430" : "12:45:39:736+0430",
   "minutesOffsetNY" : "-300",
   "minutesOffset430" : "270",
   "abbreviated_month": "Jan",
   "full_month": "January"
}
```
