<!-- Converted from reference/operator/aggregation/month.txt (reStructuredText). Includes are inlined. -->

# $month (aggregation)

## Definition

**`$month`**

Returns the month of a date as a number between 1 and 12.

The `$month` expression has the following
operator expression syntax:

```javascript
{ $month: <dateExpression> }
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
| .. code-block:: javascript :copyable: false { $month: new Date("2016-01-01") } | 1 |
| .. code-block:: javascript :copyable: false { $month: { date: new Date("Nov 7, 2003") } } | 11 |
| .. code-block:: javascript :copyable: false { $month: ISODate("2000-01-01T00:00:00Z") } | 1 |
| .. code-block:: javascript :copyable: false { $month: { date: new Date("August 14, 2011"), timezone: "America/Chicago" } } | 8 |
| .. code-block:: javascript :copyable: false { $month: { date: ISODate("2000-01-01T00:00:00Z"), timezone: "-0500" } } | 12 |
| .. code-block:: javascript :copyable: false { $month: "March 28, 1976" } | `error` |
| .. code-block:: javascript :copyable: false { $month: { date: Date("2016-01-01"), timezone: "-0500" } } | `error` |
| .. code-block:: javascript :copyable: false { $month: "2009-04-09" } | `error` |

**Note:** `$month` cannot take a string as an argument.

## Example

Consider a `sales` collection with the following document:

```javascript
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

The following aggregation uses the `$month` and other
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
