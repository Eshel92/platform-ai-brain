<!-- Converted from reference/operator/aggregation/isoWeek.txt (reStructuredText). Includes are inlined. -->

# $isoWeek (aggregation)

## Definition

**`$isoWeek`**

Returns the week number in ISO 8601 format, ranging from `1` to
`53`. Week numbers start at `1` with the week (Monday through
Sunday) that contains the year's first Thursday.

The `$isoWeek` expression has the following
operator expression syntax:

```javascript
{ $isoWeek: <dateExpression> }
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
| .. code-block:: javascript :copyable: false { $isoWeek: { date: new Date("Jan 4, 2016") } } | 1 |
| .. code-block:: javascript :copyable: false { $isoWeek: new Date("2016-01-01") } | 53 |
| .. code-block:: javascript :copyable: false { $isoWeek: { date: new Date("August 14, 2011"), timezone: "America/Chicago" } } | 32 |
| .. code-block:: javascript :copyable: false { $isoWeek: ISODate("1998-11-02T00:00:00Z") } | 45 |
| .. code-block:: javascript :copyable: false { $isoWeek: { date: ISODate("1998-11-02T00:00:00Z"), timezone: "-0500" } } | 44 |
| .. code-block:: javascript :copyable: false { $isoWeek: "March 28, 1976" } | `error` |
| .. code-block:: javascript :copyable: false { $isoWeek: Date("2016-01-01") } | `error` |
| .. code-block:: javascript :copyable: false { $isoWeek: "2009-04-09" } | `error` |

**Note:** `$isoWeek` cannot take a string as an argument.

## Example

A collection called `deliveries` contains the following documents:

```javascript
db.deliveries.insertMany( [
   { _id: 1, date: ISODate("2006-10-24T00:00:00Z"), city: "Boston" },
   { _id: 2, date: ISODate("2011-08-18T00:00:00Z"), city: "Detroit" }
] )
```

The following operation returns the week number for each `date` field.

```javascript
db.deliveries.aggregate( [
  {
    $project: {
      _id: 0,
      city: "$city",
      weekNumber: { $isoWeek: "$date" }
    }
  }
] )
```

The operation returns the following results:

```javascript
[
   { city: "Boston", weekNumber: 43 },
   { city: "Detroit", weekNumber: 33 }
]
```

**See also:**

- /reference/operator/aggregation/isoDayOfWeek
- /reference/operator/aggregation/isoWeekYear
