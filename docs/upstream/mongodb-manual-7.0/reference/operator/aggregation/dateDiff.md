<!-- Converted from reference/operator/aggregation/dateDiff.txt (reStructuredText). Includes are inlined. -->

# $dateDiff (expression operator)

## Definition

**`$dateDiff`**

**New in version:** 5.0

Returns the difference between two dates. 

The `$dateDiff` expression has this syntax:

```javascript
{ 
   $dateDiff: { 
      startDate: <Expression>, 
      endDate: <Expression>, 
      unit: <Expression>, 
      timezone: <tzExpression>,
      startOfWeek: <String> 
   }
} 
```

`$dateDiff` calculates the difference by counting the
upper boundaries of time intervals crossed from `startDate` to
`endDate` within the `timezone`. The time intervals length is
equal to one `unit` and are aligned so that their boundaries occur
at integer multiples of `unit` along the time axis. It excludes
partial units that do not cross a boundary. This expression returns
an integer in the specified `unit`. If `endDate` precedes
`startDate`, it returns a negative integer.

* - Field
  - Required/Optional
  - Description

* - `startDate`
  - Required
  - The start of the time period. The `startDate` can be any
    expression that resolves to
    a Date, a
    Timestamp,
    or an ObjectID.

* - `endDate`
  - Required
  - The end of the time period. The `endDate` can be any
    expression that resolves to
    a Date, a
    Timestamp,
    or an ObjectID.

* - `unit`
  - Required
  - The time measurement `unit` between the `startDate` and
    `endDate`. It is an 
    expression that resolves to
    a string:

    - `year` 
    - `quarter`
    - `week`
    - `month`
    - `day`
    - `hour`
    - `minute`
    - `second`
    - `millisecond`

* - `timezone`
  - Optional
  - .. include:: /includes/fact-timezone-description-no-option.rst

* - `startOfWeek`
  - Optional
  - Used when the unit is equal to `week`. Defaults to
    `Sunday`. The `startOfWeek` parameter is an
    expression that resolves
    to a case insensitive string:

    - `monday` (or `mon`)
    - `tuesday` (or `tue`)
    - `wednesday` (or `wed`)
    - `thursday` (or `thu`)
    - `friday` (or `fri`)
    - `saturday` (or `sat`)
    - `sunday` (or `sun`)

**See also:**

aggregation-expressions, bson-types.

## Behavior

### No Fractional Units

The `$dateDiff` expression returns an integer by comparing a
specific part of each date. For the `year` unit, it compares
the year values: any date in 2022 is one `year` apart from any
date in 2023. For the `week` unit, it compares week numbers:
any date in week 5 is one `week` apart from any date in week 6.

`$dateDiff` counts the unit boundaries crossed between
`startDate` and `endDate`. It does not measure elapsed
duration. For example, `$dateDiff` reports a difference of one
`year` between December 31, 2022 and January 1, 2023. A year
boundary was crossed, even though a few hours passed between the
two dates. See dateDiff-year-boundary-example for a full
example.

### Start Of Week

The start of the `week` is `Sunday` unless modified by the
`startOfWeek` parameter. `$dateDiff` counts any week that begins
between the `startDate` and `endDate` on the specified day. The
week count is not bounded by calendar `month` or calendar `year`.

### Time Zone

When using an Olson Timezone Identifier in the `<timezone>`
field, MongoDB applies the DST (Daylight Savings Time) offset
if applicable for the specified timezone.

For example, consider a `sales` collection with the following document:

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

The following aggregation illustrates how MongoDB handles the DST
offset for the Olson Timezone Identifier. The example uses the
`$hour` and `$minute` operators to return the
corresponding portions of the `date` field:

```javascript
db.sales.aggregate([
{
   $project: { 
      "nycHour": { 
         $hour: { date: "$date", timezone: "-05:00" }
       }, 
       "nycMinute": { 
          $minute: { date: "$date", timezone: "-05:00" }
       },
       "gmtHour": {
          $hour: { date: "$date", timezone: "GMT" }
       },
       "gmtMinute": {
          $minute: { date: "$date", timezone: "GMT" } },
       "nycOlsonHour": {
          $hour: { date: "$date", timezone: "America/New_York" }
       },
       "nycOlsonMinute": {
          $minute: { date: "$date", timezone: "America/New_York" }
       }
   }
}])
```

The operation returns the following result:

```javascript
{
   "_id": 1,
   "nycHour" : 5,
   "nycMinute" : 24,
   "gmtHour" : 10,
   "gmtMinute" : 24,
   "nycOlsonHour" : 6,
   "nycOlsonMinute" : 24
}
```

### Additional Details

The algorithm calculates the date difference using the Gregorian
calendar. 

Leap years and daylight savings time are accounted for but not leap
seconds.

The difference returned can be negative.   

## Examples

### Elapsed Time

Create a collection of customer orders:

```javascript
db.orders.insertMany(
   [
      { 
         custId: 456, 
         purchased: ISODate("2020-12-31"), 
         delivered: ISODate("2021-01-05")
      },
      { 
         custId: 457, 
         purchased: ISODate("2021-02-28"), 
         delivered: ISODate("2021-03-07")
      },
      { 
         custId: 458, 
         purchased: ISODate("2021-02-16"), 
         delivered: ISODate("2021-02-18")
      }
   ]
)
```

 

The following example:

- Returns the average number of days for a delivery.
- Uses `dateDiff` to calculate the difference between the
  `purchased` date and the `delivered` date.

```javascript
 db.orders.aggregate(
    [
       { 
          $group: 
             { 
                 _id: null, 
                 averageTime: 
                    { 
                       $avg:
                          { 
                             $dateDiff: 
                                { 
                                    startDate: "$purchased",
                                    endDate: "$delivered",
                                    unit: "day"
                                } 
                           }
                    }
             }
       },
       {
          $project:
             { 
                _id: 0,
                numDays: 
                   { 
                      $trunc: 
                         [ "$averageTime", 1 ]
                   }
             }
        }
    ]
)
```

The `$avg` accumulator in the `$group` stage uses
`$dateDiff` on each document to get the time between the
`purchased` and `delivered` dates. The resulting value is returned
as `averageTime`.

The decimal portion of the `averageTime` is truncated
(`$trunc`) in the `$project` stage to produce
output like this:

```javascript
{ "numDays" : 4.6 }
```

### Result Precision

Create this collection with starting and ending dates for a
subscription. 

```javascript
db.subscriptions.insertMany(
   [
      { 
         custId: 456,
         start: ISODate("2010-01-01"),
         end: ISODate("2011-01-01")
      },
      {
         custId: 457,
         start: ISODate("2010-01-01"),
         end: ISODate("2011-06-31")
      },
      {
         custId: 458, 
         start: ISODate("2010-03-01"),
         end: ISODate("2010-04-30")
      }
   ]
)
```

The `$dateDiff` expression returns a time difference expressed in
integer `units`. There are no fractional parts of a unit. For
example, when counting in `years` there are no half years. 

In this example, note how changing the `unit` changes the returned
precision: 

```javascript
db.subscriptions.aggregate(
   [
      {
         $project:
            { 
               Start: "$start",
               End: "$end", 
               years:
                  {
                     $dateDiff:
                        {
                           startDate: "$start",
                           endDate: "$end",
                           unit: "year"
                        }
                  }, 
               months:
                  {
                     $dateDiff:
                        {
                           startDate: "$start",
                           endDate: "$end",
                           unit: "month"
                        }
                  },
               days:
                  {
                     $dateDiff:
                        {
                           startDate: "$start",
                           endDate: "$end",
                           unit: "day"
                        }
                  },
               _id: 0 
            }
       }
   ]
 )
```

The results are summarized in this table:

| Start | End | Years | Months | Days |
|---|---|---|---|---|
| 2010-01-01 | 2011-01-01 | 1 | 12 | 365 |
| 2010-01-01 | 2011-07-01 | 1 | 18 | 546 |
| 2010-03-01 | 2010-04-30 | 0 | 1 | 60 |

 
In the second row, 2010-01-01 and 2011-07-01 are in different years
(2010 and 2011), so `$dateDiff` returns 1 `year`. In the third
row, 2010-03-01 (March) and 2010-04-30 (April) differ by one month,
so `$dateDiff` returns 1 `month`.

### Year Boundary Crossing

Create a collection with two dates that are only a few hours apart
but fall on either side of a calendar year boundary:

```javascript
db.events.insertOne(
   {
      start: ISODate("2022-12-31T20:00:00Z"),
      end: ISODate("2023-01-01T02:00:00Z")
   }
)
```

Use `$dateDiff` with the `year` unit to find the difference
between the two dates:

```javascript
db.events.aggregate(
   [
      {
         $project: {
            _id: 0,
            yearsApart: {
               $dateDiff: {
                  startDate: "$start",
                  endDate: "$end",
                  unit: "year"
               }
            }
         }
      }
   ]
)
```

The operation returns the following result:

```javascript
{ "yearsApart" : 1 }
```

Even though only six hours passed between the two dates,
`$dateDiff` returns `1` because the dates fall in different
calendar years. This reflects the fact that `$dateDiff` counts
unit boundaries crossed rather than elapsed duration.

### Weeks Per Month

Create a collection of months:

```javascript
db.months.insertMany(
     [
        { 
           month: "January",
           start: ISODate("2021-01-01"),
           end: ISODate("2021-01-31")
        },
        { 
           month: "February",
           start: ISODate("2021-02-01"),
           end: ISODate("2021-02-28")
        },
        {
           month: "March",
           start: ISODate("2021-03-01"),
           end: ISODate("2021-03-31")
        },
     ]
   )
```

You can change the start of each week, and count the resulting number of
weeks in each month with the following code:

```javascript
db.months.aggregate(
   [
      {
         $project:
            { 
               wks_default:
                  {
                     $dateDiff:
                        { 
                           startDate: "$start",  
                           endDate: "$end", 
                           unit: "week"
                        }
                  }, 
               wks_monday:
                  {
                     $dateDiff:
                        { 
                           startDate: "$start",
                           endDate: "$end", 
                           unit: "week", 
                           startOfWeek: "Monday"
                        }
                  },
               wks_friday:
                  {
                     $dateDiff:
                        { 
                           startDate: "$start",
                           endDate: "$end",
                           unit: "week",
                           startOfWeek: "fri" 
                        }
                  },
               _id: 0 
            }
       }
   ]
 )
```

The results are summarized in this table:

| Month | Sunday | Monday | Friday |
|---|---|---|---|
| January | 5 | 4 | 4 |
| February | 4 | 3 | 4 |
| March | 4 | 4 | 4 |

From the results:

- When the `startOfWeek` is Sunday, the 5th `week` in January, 2021
  begins on the 31st.
- Because the 31st is a Sunday and it is between `startDate` and
  `endDate`, one `week` is added to the count.
- The `week` count is incremented even when a calendar week finishes
  after `endDate` or in the next calendar period.
