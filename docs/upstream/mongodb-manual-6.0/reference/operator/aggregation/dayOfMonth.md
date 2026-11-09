<!-- Converted from reference/operator/aggregation/dayOfMonth.txt (reStructuredText). Includes are inlined. -->

# $dayOfMonth (aggregation)

## Definition

**`$dayOfMonth`**

Returns the day of the month for a date as a number between 1 and 31.

The `$dayOfMonth` expression has the following
operator expression syntax:

```javascript
{ $dayOfMonth: <dateExpression> }
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
| .. code-block:: javascript :copyable: false { $dayOfMonth: new Date("2016-01-01") } | 1 |
| .. code-block:: javascript :copyable: false { $dayOfMonth: { date: new Date("Jan 7, 2003") } } | 7 |
| .. code-block:: javascript :copyable: false { $dayOfMonth: { date: new Date("August 14, 2011"), timezone: "America/Chicago" } } | 14 |
| .. code-block:: javascript :copyable: false { $dayOfMonth: ISODate("1998-11-07T00:00:00Z") } | 7 |
| .. code-block:: javascript :copyable: false { $dayOfMonth: { date: ISODate("1998-11-07T00:00:00Z"), timezone: "-0400" } } | 6 |
| .. code-block:: javascript :copyable: false { $dayOfMonth: "March 28, 1976" } | `error` |
| .. code-block:: javascript :copyable: false { $dayOfMonth: Date("2016-01-01") } | `error` |
| .. code-block:: javascript :copyable: false { $dayOfMonth: "2009-04-09" } | `error` |

**Note:** `$dayOfMonth` cannot take a string as an argument.

## Example

Consider a `sales` collection with the following document:

```javascript
{
  "_id" : 1,
  "item" : "abc",
  "price" : 10,
  "quantity" : 2,
  "date" : ISODate("2014-01-01T08:15:39.736Z")
}
```

The following aggregation uses the `$dayOfMonth` and other
date operators to break down the `date` field:

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
