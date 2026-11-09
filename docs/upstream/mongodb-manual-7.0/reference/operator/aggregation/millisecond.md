<!-- Converted from reference/operator/aggregation/millisecond.txt (reStructuredText). Includes are inlined. -->

# $millisecond (expression operator)

## Definition

**`$millisecond`**

Returns the millisecond portion of a date as an integer between 0
and 999.

The `$millisecond` expression has the following
operator expression syntax:

```javascript
{ $millisecond: <dateExpression> }
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
| .. code-block:: javascript :copyable: false { $millisecond: new Date("2016-01-01") } | 0 |
| .. code-block:: javascript :copyable: false { $millisecond: { date: new Date("Jan 7, 2003") } } | 0 |
| .. code-block:: javascript :copyable: false { $millisecond: { date: new Date("August 14, 2011"), timezone: "America/Chicago" } } | 0 |
| .. code-block:: javascript :copyable: false { $millisecond: ISODate("1998-11-07T00:00:00Z") } | 0 |
| .. code-block:: javascript :copyable: false { $millisecond: { date: ISODate("1998-11-07T00:00:00Z"), timezone: "-0400" } } | 0 |
| .. code-block:: javascript :copyable: false { $millisecond: "March 28, 1976" } | `error` |
| .. code-block:: javascript :copyable: false { $millisecond: Date("2016-01-01") } | `error` |
| .. code-block:: javascript :copyable: false { $millisecond: "2009-04-09" } | `error` |

**Note:** `$millisecond` cannot take a string as an argument.

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

The following aggregation uses the `$millisecond` and other
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
