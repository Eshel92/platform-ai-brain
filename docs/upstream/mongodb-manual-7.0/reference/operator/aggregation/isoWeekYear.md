<!-- Converted from reference/operator/aggregation/isoWeekYear.txt (reStructuredText). Includes are inlined. -->

# $isoWeekYear (expression operator)

## Definition

**`$isoWeekYear`**

Returns the year number in ISO 8601 format. The year starts
with the Monday of week 1 and ends with the Sunday of the
last week.

The `$isoWeekYear` expression has the following
operator expression syntax:

```javascript
{ $isoWeekYear: <dateExpression> }
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
| .. code-block:: javascript :copyable: false { $isoWeekYear: new Date("2015-05-26") } | 2015 |
| .. code-block:: javascript :copyable: false { $isoWeekYear: { date: new Date("Jan 7, 2003") } } | 2003 |
| .. code-block:: javascript :copyable: false { $isoWeekYear: ISODate("2017-01-02T00:00:00Z") } | 2017 |
| .. code-block:: javascript :copyable: false { $isoWeekYear: { date: ISODate("2017-01-02T00:00:00Z"), timezone: "-0500" } } | 2016 |
| .. code-block:: javascript :copyable: false { $isoWeekYear: { date: new Date("April 08, 2024"), timezone: "America/Chicago" } } | 2024 |
| .. code-block:: javascript :copyable: false { $isoWeekYear: "March 28, 1976" } | `error` |
| .. code-block:: javascript :copyable: false { $isoWeekYear: Date("2016-01-01") } | `error` |
| .. code-block:: javascript :copyable: false { $isoWeekYear: "2009-04-09" } | `error` |

**Note:** `$isoWeekYear` cannot take a string as an argument.

## Example

A collection called `anniversaries` contains the following documents:

```javascript
{ "_id" : 1, "date" : ISODate("2016-01-01T00:00:00Z") }
{ "_id" : 2, "date" : ISODate("2016-01-04T00:00:00Z") }
{ "_id" : 3, "date" : ISODate("2015-01-01T00:00:00Z") }
{ "_id" : 4, "date" : ISODate("2014-04-21T00:00:00Z") }
```

The following operation returns the year number in ISO 8601
format for each `date` field.

```javascript
db.anniversaries.aggregate( [
  {
    $project: {
      yearNumber: { $isoWeekYear: "$date" }
    }
  }
] )
```

The operation returns the following results:

```javascript
{ "_id" : 1, "yearNumber" : 2015 }
{ "_id" : 2, "yearNumber" : 2016 }
{ "_id" : 3, "yearNumber" : 2015 }
{ "_id" : 4, "yearNumber" : 2014 }
```

**See also:**

- /reference/operator/aggregation/isoDayOfWeek
- /reference/operator/aggregation/isoWeek
