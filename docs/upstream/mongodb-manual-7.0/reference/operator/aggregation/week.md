<!-- Converted from reference/operator/aggregation/week.txt (reStructuredText). Includes are inlined. -->

# $week  (expression operator)

## Definition

**`$week`**

Returns the week of the year for a date as a number between 0 and 53.

Weeks begin on Sundays, and week 1 begins with the first Sunday
of the year. Days preceding the first Sunday of the year are in
week 0. This behavior is the same as the "`%U`" operator to the
`strftime` standard library function.

The `$week` expression has the following
operator expression syntax:

```javascript
{ $week: <dateExpression> }
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
| .. code-block:: javascript :copyable: false { $week: new Date("Jan 1, 2016") } | 0 |
| .. code-block:: javascript :copyable: false { $week: { date: new Date("2016-01-04") } } | 1 |
| .. code-block:: javascript :copyable: false { $week: { date: new Date("August 14, 2011"), timezone: "America/Chicago" } } | 33 |
| .. code-block:: javascript :copyable: false { $week: ISODate("1998-11-01T00:00:00Z") } | 44 |
| .. code-block:: javascript :copyable: false { $week: { date: ISODate("1998-11-01T00:00:00Z"), timezone: "-0500" } } | 43 |
| .. code-block:: javascript :copyable: false { $week: "March 28, 1976" } | `error` |
| .. code-block:: javascript :copyable: false { $week: Date("2016-01-01") } | `error` |
| .. code-block:: javascript :copyable: false { $week: "2009-04-09" } | `error` |

**Note:** `$week` cannot take a string as an argument.

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

The following aggregation uses the `$week` and other
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
