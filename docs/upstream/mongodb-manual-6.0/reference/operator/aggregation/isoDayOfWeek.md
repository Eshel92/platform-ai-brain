<!-- Converted from reference/operator/aggregation/isoDayOfWeek.txt (reStructuredText). Includes are inlined. -->

# $isoDayOfWeek (aggregation)

## Definition

**`$isoDayOfWeek`**

Returns the weekday number in ISO 8601 format, ranging from
`1` (for Monday) to `7` (for Sunday).

The `$isoDayOfWeek` expression has the following
operator expression syntax:

```javascript
{ $isoDayOfWeek: <dateExpression> }
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
| .. code-block:: javascript :copyable: false { $isoDayOfWeek: new Date("2016-01-01") } | 5 |
| .. code-block:: javascript :copyable: false { $isoDayOfWeek: { date: new Date("Jan 7, 2003") } } | 2 |
| .. code-block:: javascript :copyable: false { $isoDayOfWeek: { date: new Date("August 14, 2011"), timezone: "America/Chicago" } } | 7 |
| .. code-block:: javascript :copyable: false { $isoDayOfWeek: ISODate("1998-11-07T00:00:00Z") } | 6 |
| .. code-block:: javascript :copyable: false { $isoDayOfWeek: { date: ISODate("1998-11-07T00:00:00Z"), timezone: "-0400" } } | 5 |
| .. code-block:: javascript :copyable: false { $isoDayOfWeek: "March 28, 1976" } | `error` |
| .. code-block:: javascript :copyable: false { $isoDayOfWeek: Date("2016-01-01") } | `error` |
| .. code-block:: javascript :copyable: false { $isoDayOfWeek: "2009-04-09" } | `error` |

**Note:** `$isoDayOfWeek` cannot take a string as an argument.

## Example

A collection called `birthdays` contains the following documents:

```javascript
{ "_id" : 1, "name" : "Betty", "birthday" : ISODate("1993-09-21T00:00:00Z") }
{ "_id" : 2, "name" : "Veronica", "birthday" : ISODate("1981-11-07T00:00:00Z") }
```

The following operation returns the weekday number for each
`birthday` field.

```javascript
db.dates.aggregate( [
  {
    $project: {
      _id: 0,
      name: "$name",
      dayOfWeek: { $isoDayOfWeek: "$birthday" }
    }
  }
] )
```

The operation returns the following results:

```javascript
{ "name" : "Betty", "dayOfWeek" : 2 }
{ "name" : "Veronica", "dayOfWeek" : 6 }
```

**See also:**

- /reference/operator/aggregation/isoWeekYear
- /reference/operator/aggregation/isoWeek
