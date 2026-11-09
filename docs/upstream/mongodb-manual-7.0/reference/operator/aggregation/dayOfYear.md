<!-- Converted from reference/operator/aggregation/dayOfYear.txt (reStructuredText). Includes are inlined. -->

# $dayOfYear (expression operator)

## Definition

**`$dayOfYear`**

Returns the day of the year for a date as a number between 1 and 366.

The `$dayOfYear` expression has the following
operator expression syntax:

```javascript
{ $dayOfYear: <dateExpression> }
```

The argument can be:

- An expression that resolves to a
  Date, a Timestamp, or an ObjectID.

- A document with this format:

  ```javascript
  { date: <dateExpression>, timezone: <tzExpression> }
  ```

  | Field | Description |
  |---|---|
  | `date` | The date to which the operator is applied. `<dateExpression>` must be a valid expression that resolves to a Date, a Timestamp, or an ObjectID. |
  | `timezone` | .. include:: /includes/fact-timezone-description.rst |

## Behavior

| Example | Result |
|---|---|
| .. code-block:: javascript :copyable: false { $dayOfYear: new Date("2016-01-01") } | 1 |
| .. code-block:: javascript :copyable: false { $dayOfYear: { date: new Date("Jan 7, 2003") } } | 7 |
| .. code-block:: javascript :copyable: false { $dayOfYear: { date: new Date("August 14, 2011"), timezone: "America/Chicago" } } | 226 |
| .. code-block:: javascript :copyable: false { $dayOfYear: ISODate("1998-11-07T00:00:00Z") } | 311 |
| .. code-block:: javascript :copyable: false { $dayOfYear: { date: ISODate("1998-11-07T00:00:00Z"), timezone: "-0400" } } | 310 |
| .. code-block:: javascript :copyable: false { $dayOfYear: "March 28, 1976" } | `error` |
| .. code-block:: javascript :copyable: false { $dayOfYear: Date("2016-01-01") } | `error` |
| .. code-block:: javascript :copyable: false { $dayOfYear: "2009-04-09" } | `error` |

**Note:** `$dayOfYear` cannot take a string as an argument.

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

The following aggregation uses the `$dayOfYear` and other date
expressions to break down the `date` field:

```javascript
db.sales.aggregate(
   [
     {
       $project:
         {
           year: { $year: "$date" },
           month: { $month: "$date" },
           day: { $dayOfMonth: "$date" },
           hour: { $hour: "$date" },
           minutes: { $minute: "$date" },
           seconds: { $second: "$date" },
           milliseconds: { $millisecond: "$date" },
           dayOfYear: { $dayOfYear: "$date" },
           dayOfWeek: { $dayOfWeek: "$date" },
           week: { $week: "$date" }
         }
     }
   ]
)
```

The operation returns the following result:

```javascript
{
  "_id" : 1,
  "year" : 2014,
  "month" : 1,
  "day" : 1,
  "hour" : 8,
  "minutes" : 15,
  "seconds" : 39,
  "milliseconds" : 736,
  "dayOfYear" : 1,
  "dayOfWeek" : 4,
  "week" : 0
}
```
