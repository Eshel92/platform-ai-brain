<!-- Converted from reference/operator/aggregation/year.txt (reStructuredText). Includes are inlined. -->

# $year  (expression operator)

## Definition

**`$year`**

Returns the year portion of a date.

The `$year` expression has the following
operator expression syntax:

```javascript
{ $year: <dateExpression> }
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
| .. code-block:: javascript :copyable: false { $year: new Date("2016-01-01") } | 2016 |
| .. code-block:: javascript :copyable: false { $year: { date: new Date("Jan 7, 2003") } } | 2003 |
| .. code-block:: javascript :copyable: false { $year: { date: new Date("August 14, 2011"), timezone: "America/Chicago" } } | 2011 |
| .. code-block:: javascript :copyable: false { $year: ISODate("1998-11-07T00:00:00Z") } | 1998 |
| .. code-block:: javascript :copyable: false { $year: { date: ISODate("1998-11-07T00:00:00Z"), timezone: "-0400" } } | 1998 |
| .. code-block:: javascript :copyable: false { $year: "March 28, 1976" } | `error` |
| .. code-block:: javascript :copyable: false { $year: Date("2016-01-01") } | `error` |
| .. code-block:: javascript :copyable: false { $year: "2009-04-09" } | `error` |

**Note:** `$year` cannot take a string as an argument.

## Example

Consider a `sales` collection with the following documents:

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

The following aggregation uses the `$year` and other
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
