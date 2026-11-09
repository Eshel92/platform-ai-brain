<!-- Converted from reference/operator/aggregation/hour.txt (reStructuredText). Includes are inlined. -->

# $hour (expression operator)

## Definition

**`$hour`**

Returns the hour portion of a date as a number between 0 and 23.

The `$hour` expression has the following
operator expression syntax:

```javascript
{ $hour: <dateExpression> }
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
| .. code-block:: javascript :copyable: false { $hour: new Date("2016-01-01T12:00:00Z") } | 12 |
| .. code-block:: javascript :copyable: false { $hour: { date: new Date("Jan 7, 2003Z") } } | 0 |
| .. code-block:: javascript :copyable: false { $hour: { date: new Date("August 14, 2011Z"), timezone: "America/Chicago" } } | 19 |
| .. code-block:: javascript :copyable: false { $hour: ISODate("2017-10-19T00:00:00Z") } | 0 |
| .. code-block:: javascript :copyable: false { $hour: { date: ISODate("2017-10-19T00:00:00Z"), timezone: "+0530" } } | 5 |
| .. code-block:: javascript :copyable: false { $hour: "March 28, 1976" } | `error` |
| .. code-block:: javascript :copyable: false { $hour: Date("2016-01-01") } | `error` |
| .. code-block:: javascript :copyable: false { $hour: "2009-04-09" } | `error` |

**Note:** `$hour` cannot take a string as an argument.

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

The following aggregation uses the `$hour` and other date
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
           dayOfWeek: { $dayOfWeek: "$date" }
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
