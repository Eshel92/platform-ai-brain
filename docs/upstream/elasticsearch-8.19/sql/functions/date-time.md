<!-- Converted from sql/functions/date-time.asciidoc (AsciiDoc). Includes are inlined. -->

### Date/Time and Interval Functions and Operators

{es-sql} offers a wide range of facilities for performing date/time manipulations.

#### Intervals

A common requirement when dealing with date/time in general revolves around
the notion of `interval`, a topic that is worth exploring in the context of Elasticsearch and {es-sql}.

Elasticsearch has comprehensive support for date math both inside index names and queries.
Inside {es-sql} the former is supported as is by passing the expression in the table name, while the latter is supported through the standard SQL `INTERVAL`.

The table below shows the mapping between Elasticsearch and {es-sql}:

|==========================
s|Elasticsearch
s|{es-sql}
2+h| Index/Table datetime math
2+|<index-{now/M{YYYY.MM}}>
2+h| Query date/time math
| 1y  | INTERVAL 1 YEAR
| 2M  | INTERVAL 2 MONTH
| 3w  | INTERVAL 21 DAY
| 4d  | INTERVAL 4 DAY
| 5h  | INTERVAL 5 HOUR
| 6m  | INTERVAL 6 MINUTE
| 7s  | INTERVAL 7 SECOND
|==========================

`INTERVAL` allows either `YEAR` and `MONTH` to be mixed together _or_ `DAY`, `HOUR`, `MINUTE` and `SECOND`.

**Tip:** {es-sql} accepts also the plural for each time unit (e.g. both `YEAR` and `YEARS` are valid).

Example of the possible combinations below:

|===
s|Interval
s|Description
| `INTERVAL '1-2' YEAR TO MONTH`                | 1 year and 2 months
| `INTERVAL '3 4' DAYS TO HOURS`                | 3 days and 4 hours
| `INTERVAL '5 6:12' DAYS TO MINUTES`           | 5 days, 6 hours and 12 minutes
| `INTERVAL '3 4:56:01' DAY TO SECOND`          | 3 days, 4 hours, 56 minutes and 1 second
| `INTERVAL '2 3:45:01.23456789' DAY TO SECOND` | 2 days, 3 hours, 45 minutes, 1 second and 234567890 nanoseconds
| `INTERVAL '123:45' HOUR TO MINUTES`           | 123 hours and 45 minutes
| `INTERVAL '65:43:21.0123' HOUR TO SECONDS`    | 65 hours, 43 minutes, 21 seconds and 12300000 nanoseconds
| `INTERVAL '45:01.23' MINUTES TO SECONDS`      | 45 minutes, 1 second and 230000000 nanoseconds
|===

#### Comparison

Date/time fields can be compared to date math expressions with the equality (`=`) and `IN` operators:

```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[dtDateMathEquals]
```

```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[dtDateMathIn]
```

#### Operators

Basic arithmetic operators (`+`, `-`, `*`) support date/time parameters as indicated below:

```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[dtIntervalPlusInterval]
```

```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[dtDateTimePlusInterval]
```

```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[dtMinusInterval]
```

```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[dtIntervalMinusInterval]
```

```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[dtDateTimeMinusInterval]
```

```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[dtIntervalMul]
```

#### Functions

Functions that target date/time.

#### `CURRENT_DATE/CURDATE`

**Synopsis:**
```sql
CURRENT_DATE
CURRENT_DATE()
CURDATE()
```

*Input*: _none_

*Output*: date

*Description*: Returns the date (no time part) when the current query reached the server.
It can be used both as a keyword: `CURRENT_DATE` or as a function with no arguments: `CURRENT_DATE()`.

Unlike CURRENT_DATE, `CURDATE()` can only be used as a function with no arguments and not as a keyword.

This method always returns the same value for its every occurrence within the same query.

```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[currentDate]
```

```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[currentDateFunction]
```

```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[curDateFunction]
```

Typically, this function (as well as its twin TODAY()) function
is used for relative date filtering:

```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[filterToday]
```

#### `CURRENT_TIME/CURTIME`

**Synopsis:**
```sql
CURRENT_TIME
CURRENT_TIME([precision]) <1>
CURTIME
```

*Input*:

<1> fractional digits; optional

*Output*: time

*Description*: Returns the time when the current query reached the server.
As a function, `CURRENT_TIME()` accepts _precision_ as an optional
parameter for rounding the second fractional digits (nanoseconds). The default _precision_ is 3,
meaning a milliseconds precision current time will be returned.

This method always returns the same value for its every occurrence within the same query.

```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[currentTime]
```

```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[currentTimeFunction]
```

```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[curTimeFunction]
```

```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[currentTimeFunctionPrecision]
```

Typically, this function is used for relative date/time filtering:

```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[filterCurrentTime]
```

Currently, using a _precision_ greater than 6 doesn't make any difference to the output of the
function as the maximum number of second fractional digits returned is 6.

#### `CURRENT_TIMESTAMP`

**Synopsis:**
```sql
CURRENT_TIMESTAMP
CURRENT_TIMESTAMP([precision]) <1>
```

*Input*:

<1> fractional digits; optional

*Output*: date/time

*Description*: Returns the date/time when the current query reached the server.
As a function, `CURRENT_TIMESTAMP()` accepts _precision_ as an optional
parameter for rounding the second fractional digits (nanoseconds). The default _precision_ is 3,
meaning a milliseconds precision current date/time will be returned.

This method always returns the same value for its every occurrence within the same query.

```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[curTs]
```

```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[curTsFunction]
```

```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[curTsFunctionPrecision]
```

Typically, this function (as well as its twin NOW()) function is used for
relative date/time filtering:

```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[filterNow]
```

Currently, using a _precision_ greater than 6 doesn't make any difference to the output of the
function as the maximum number of second fractional digits returned is 6.

#### `DATE_ADD/DATEADD/TIMESTAMP_ADD/TIMESTAMPADD`

**Synopsis:**
```sql
DATE_ADD(
    string_exp, <1>
    integer_exp, <2>
    datetime_exp) <3>
```

*Input*:

<1> string expression denoting the date/time unit to add to the date/datetime.
If `null`, the function returns `null`.
<2> integer expression denoting how many times the above unit should be added
to/from the date/datetime, if a negative value is used it results to a
subtraction from the date/datetime. If `null`, the function returns `null`.
<3> date/datetime expression. If `null`, the function returns `null`.

*Output*: datetime

*Description*: Add the given number of date/time units to a date/datetime. If the number of units is negative then it's subtracted from
the date/datetime.

If the second argument is a long there is possibility of truncation since an integer value will be extracted and
used from that long.

|===
2+h|Datetime units to add/subtract

s|unit
s|abbreviations

| year        | years, yy, yyyy
| quarter     | quarters, qq, q
| month       | months, mm, m
| dayofyear   | dy, y
| day         | days, dd, d
| week        | weeks, wk, ww
| weekday     | weekdays, dw
| hour        | hours, hh
| minute      | minutes, mi, n
| second      | seconds, ss, s
| millisecond | milliseconds, ms
| microsecond | microseconds, mcs
| nanosecond  | nanoseconds, ns
|===

```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[dateAddDateTimeYears]
```

```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[dateAddDateTimeWeeks]
```

```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[dateAddDateTimeSeconds]
```

```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[dateAddDateQuarters]
```

```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[dateAddDateMinutes]
```

#### `DATE_DIFF/DATEDIFF/TIMESTAMP_DIFF/TIMESTAMPDIFF`

**Synopsis:**
```sql
DATE_DIFF(
    string_exp, <1>
    datetime_exp, <2>
    datetime_exp) <3>
```

*Input*:

<1> string expression denoting the date/time unit difference between the
following two date/datetime expressions. If `null`, the function returns `null`.
<2> start date/datetime expression. If `null`, the function returns `null`.
<3> end date/datetime expression. If `null`, the function returns `null`.

*Output*: integer

*Description*: Subtract the second argument from the third argument and return their difference in multiples of the unit
specified in the first argument. If the second argument (start) is greater than the third argument (end),
then negative values are returned.

|===
2+h|Datetime difference units

s|unit
s|abbreviations

| year        | years, yy, yyyy
| quarter     | quarters, qq, q
| month       | months, mm, m
| dayofyear   | dy, y
| day         | days, dd, d
| week        | weeks, wk, ww
| weekday     | weekdays, dw
| hour        | hours, hh
| minute      | minutes, mi, n
| second      | seconds, ss, s
| millisecond | milliseconds, ms
| microsecond | microseconds, mcs
| nanosecond  | nanoseconds, ns
|===

```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[dateDiffDateTimeYears]
```

```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[dateDiffDateTimeWeeks]
```

```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[dateDiffDateTimeSeconds]
```

```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[dateDiffDateQuarters]
```

For `hour` and `minute`, `DATEDIFF` doesn't do any rounding, but instead first truncates
the more detailed time fields on the 2 dates to zero and then calculates the subtraction.

```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[dateDiffDateTimeHours]
```

```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[dateDiffDateTimeMinutes]
```

```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[dateDiffDateMinutes]
```

#### `DATE_FORMAT`

**Synopsis:**
```sql
DATE_FORMAT(
    date_exp/datetime_exp/time_exp, <1>
    string_exp) <2>
```

*Input*:

<1> date/datetime/time expression. If `null`, the function returns `null`.
<2> format pattern. If `null` or an empty string, the function returns `null`.

*Output*: string

*Description*: Returns the date/datetime/time as a string using the format specified in the 2nd argument. The formatting
pattern is one of the specifiers used in the
[MySQL DATE_FORMAT() function](https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html#function_date-format).

If the 1st argument is of type `time`, then pattern specified by the 2nd argument cannot contain date related units
(e.g. 'dd', 'MM', 'yyyy', etc.). If it contains such units an error is returned.
Ranges for month and day specifiers (%c, %D, %d, %e, %m) start at one, unlike MySQL, where they start at zero, due to
the fact that MySQL permits the storing of incomplete dates such as '2014-00-00'.
Elasticsearch in this case returns an error.
```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[dateFormatDate]
```

```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[dateFormatDateTime]
```

```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[dateFormatTime]
```

#### `DATE_PARSE`

**Synopsis:**
```sql
DATE_PARSE(
    string_exp, <1>
    string_exp) <2>
```

*Input*:

<1> date expression as a string. If `null` or an empty string, the function
returns `null`.
<2> parsing pattern. If `null` or an empty string, the function returns `null`.

*Output*: date

*Description*: Returns a date by parsing the 1st argument using the format specified in the 2nd argument. The parsing
format pattern used is the one from
[`java.time.format.DateTimeFormatter`](https://docs.oracle.com/en/java/javase/14/docs/api/java.base/java/time/format/DateTimeFormatter.html).

If the parsing pattern does not contain all valid date units (e.g. 'HH:mm:ss', 'dd-MM HH:mm:ss', etc.) an error is returned
as the function needs to return a value of `date` type which will contain date part.

```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[dateParse1]
```

**Note:**
The resulting `date` will have the time zone specified by the user through the
`time_zone`/`timezone` REST/driver parameters
with no conversion applied.

```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[dateParse2]
```

#### `DATETIME_FORMAT`

**Synopsis:**
```sql
DATETIME_FORMAT(
    date_exp/datetime_exp/time_exp, <1>
    string_exp) <2>
```

*Input*:

<1> date/datetime/time expression. If `null`, the function returns `null`.
<2> format pattern. If `null` or an empty string, the function returns `null`.

*Output*: string

*Description*: Returns the date/datetime/time as a string using the format specified in the 2nd argument. The formatting
pattern used is the one from
[`java.time.format.DateTimeFormatter`](https://docs.oracle.com/en/java/javase/14/docs/api/java.base/java/time/format/DateTimeFormatter.html).

If the 1st argument is of type `time`, then pattern specified by the 2nd argument cannot contain date related units
(e.g. 'dd', 'MM', 'yyyy', etc.). If it contains such units an error is returned.

```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[dateTimeFormatDate]
```

```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[dateTimeFormatDateTime]
```

```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[dateTimeFormatTime]
```

#### `DATETIME_PARSE`

**Synopsis:**
```sql
DATETIME_PARSE(
    string_exp, <1>
    string_exp) <2>
```

*Input*:

<1> datetime expression as a string. If `null` or an empty string, the function
returns `null`.
<2> parsing pattern. If `null` or an empty string, the function returns `null`.

*Output*: datetime

*Description*: Returns a datetime by parsing the 1st argument using the format specified in the 2nd argument. The parsing
format pattern used is the one from
[`java.time.format.DateTimeFormatter`](https://docs.oracle.com/en/java/javase/14/docs/api/java.base/java/time/format/DateTimeFormatter.html).

If the parsing pattern contains only date or only time units (e.g. 'dd/MM/yyyy', 'HH:mm:ss', etc.) an error is returned
as the function needs to return a value of `datetime` type which must contain both.

```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[dateTimeParse1]
```

```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[dateTimeParse2]
```

**Note:**
If timezone is not specified in the datetime string expression and the parsing pattern, the resulting `datetime` will have the
time zone specified by the user through the `time_zone`/`timezone` REST/driver parameters
with no conversion applied.

```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[dateTimeParse3]
```

#### `TIME_PARSE`

**Synopsis:**
```sql
TIME_PARSE(
    string_exp, <1>
    string_exp) <2>
```

*Input*:

<1> time expression as a string. If `null` or an empty string, the function
returns `null`.
<2> parsing pattern. If `null` or an empty string, the function returns `null`.

*Output*: time

*Description*: Returns a time by parsing the 1st argument using the format specified in the 2nd argument. The parsing
format pattern used is the one from
[`java.time.format.DateTimeFormatter`](https://docs.oracle.com/en/java/javase/14/docs/api/java.base/java/time/format/DateTimeFormatter.html).

If the parsing pattern contains only date units (e.g. 'dd/MM/yyyy') an error is returned
as the function needs to return a value of `time` type which will contain only time.

```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[timeParse1]
```

```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[timeParse2]
```

**Note:**
If timezone is not specified in the time string expression and the parsing pattern,
the resulting `time` will have the offset of the time zone specified by the user through the
 `time_zone`/`timezone` REST/driver
parameters at the Unix epoch date (`1970-01-01`) with no conversion applied.

```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[timeParse3]
```

#### `DATE_PART/DATEPART`

**Synopsis:**
```sql
DATE_PART(
    string_exp, <1>
    datetime_exp) <2>
```

*Input*:

<1> string expression denoting the unit to extract from the date/datetime. If
`null`, the function returns `null`.
<2> date/datetime expression. If `null`, the function returns `null`.

*Output*: integer

*Description*: Extract the specified unit from a date/datetime. It's similar to
sql-functions-datetime-extract but with different names and aliases for the
units and provides more options (e.g.: `TZOFFSET`).

|===
2+h|Datetime units to extract

s|unit
s|abbreviations

| year        | years, yy, yyyy
| quarter     | quarters, qq, q
| month       | months, mm, m
| dayofyear   | dy, y
| day         | days, dd, d
| week        | weeks, wk, ww
| weekday     | weekdays, dw
| hour        | hours, hh
| minute      | minutes, mi, n
| second      | seconds, ss, s
| millisecond | milliseconds, ms
| microsecond | microseconds, mcs
| nanosecond  | nanoseconds, ns
| tzoffset    | tz
|===

```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[datePartDateTimeYears]
```

```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[datePartDateTimeMinutes]
```

```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[datePartDateQuarter]
```

```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[datePartDateMonth]
```

For `week` and `weekday` the unit is extracted using the non-ISO calculation, which means
that a given week is considered to start from Sunday, not Monday.

```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[datePartDateTimeWeek]
```

The `tzoffset` returns the total number of minutes (signed) that represent the time zone's offset.

```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[datePartDateTimeTzOffsetPlus]
```

```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[datePartDateTimeTzOffsetMinus]
```

#### `DATE_TRUNC/DATETRUNC`

**Synopsis:**
```sql
DATE_TRUNC(
    string_exp, <1>
    datetime_exp/interval_exp) <2>
```

*Input*:

<1> string expression denoting the unit to which the date/datetime/interval
should be truncated to. If `null`, the function returns `null`.
<2> date/datetime/interval expression. If `null`, the function returns `null`.

*Output*: datetime/interval

*Description*: Truncate the date/datetime/interval to the specified unit by
setting all fields that are less significant than the specified one to zero (or
one, for day, day of week and month). If the first argument is `week` and the
second argument is of `interval` type, an error is thrown since the `interval`
data type doesn't support a `week` time unit.

|===
2+h|Datetime truncation units

s|unit
s|abbreviations

| millennium  | millennia
| century     | centuries
| decade      | decades
| year        | years, yy, yyyy
| quarter     | quarters, qq, q
| month       | months, mm, m
| week        | weeks, wk, ww
| day         | days, dd, d
| hour        | hours, hh
| minute      | minutes, mi, n
| second      | seconds, ss, s
| millisecond | milliseconds, ms
| microsecond | microseconds, mcs
| nanosecond  | nanoseconds, ns
|===

```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[truncateDateTimeMillennium]
```

```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[truncateDateTimeWeek]
```

```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[truncateDateTimeMinutes]
```

```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[truncateDateDecades]
```

```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[truncateDateQuarter]
```

```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[truncateIntervalCenturies]
```

```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[truncateIntervalHour]
```

```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[truncateIntervalDay]
```

#### `FORMAT`

**Synopsis:**
```sql
FORMAT(
    date_exp/datetime_exp/time_exp, <1>
    string_exp) <2>
```

*Input*:

<1> date/datetime/time expression. If `null`, the function returns `null`.
<2> format pattern. If `null` or an empty string, the function returns `null`.

*Output*: string

*Description*: Returns the date/datetime/time as a string using the
[format](https://docs.microsoft.com/en-us/sql/t-sql/functions/format-transact-sql#arguments)
specified in the 2nd argument. The formatting pattern used is the one from
https://docs.microsoft.com/en-us/dotnet/standard/base-types/custom-date-and-time-format-strings[Microsoft
SQL Server Format Specification].

If the 1st argument is of type `time`, then pattern specified by the 2nd argument cannot contain date related units
(e.g. 'dd', 'MM', 'yyyy', etc.). If it contains such units an error is returned. +
Format specifier `F` will be working similar to format specifier `f`.
It will return the fractional part of seconds, and the number of digits will be same as of the number of `Fs` provided as input (up to 9 digits).
Result will contain `0` appended in the end to match with number of `F` provided.
e.g.: for a time part `10:20:30.1234` and pattern `HH:mm:ss.FFFFFF`, the output string of the function would be: `10:20:30.123400`. +
Format specifier `y` will return year-of-era instead of one/two low-order digits.
eg.: For year `2009`, `y` will be returning `2009` instead of `9`. For year `43`, `y` format specifier will return `43`.
- Special characters like `"` , `\` and `%` will be returned as it is without any change. eg.: formatting date `17-sep-2020` with `%M` will return `%9`

```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[formatDate]
```

```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[formatDateTime]
```

```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[formatTime]
```

#### `TO_CHAR`

**Synopsis:**
```sql
TO_CHAR(
    date_exp/datetime_exp/time_exp, <1>
    string_exp) <2>
```

*Input*:

<1> date/datetime/time expression. If `null`, the function returns `null`.
<2> format pattern. If `null` or an empty string, the function returns `null`.

*Output*: string

*Description*: Returns the date/datetime/time as a string using the format
specified in the 2nd argument. The formatting pattern conforms to
https://www.postgresql.org/docs/13/functions-formatting.html[PostgreSQL Template
Patterns for Date/Time Formatting].

If the 1st argument is of type `time`, then the pattern specified by the 2nd argument cannot contain date related units
(e.g. 'dd', 'MM', 'YYYY', etc.). If it contains such units an error is returned. +
The result of the patterns `TZ` and `tz` (time zone abbreviations) in some cases differ from the results returned by the `TO_CHAR`
in PostgreSQL. The reason is that the time zone abbreviations specified by the JDK are different from the ones specified by PostgreSQL.
This function might show an actual time zone abbreviation instead of the generic `LMT` or empty string or offset returned by the PostgreSQL
implementation. The summer/daylight markers might also differ between the two implementations (e.g. will show `HT` instead of `HST`
for Hawaii). +
The `FX`, `TM`, `SP` pattern modifiers are not supported and will show up as `FX`, `TM`, `SP` literals in the output.

```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[toCharDate]
```

```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[toCharDateTime]
```

```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[toCharTime]
```

#### `DAY_OF_MONTH/DOM/DAY`

**Synopsis:**
```sql
DAY_OF_MONTH(datetime_exp) <1>
```

*Input*:

<1> date/datetime expression. If `null`, the function returns `null`.

*Output*: integer

*Description*: Extract the day of the month from a date/datetime.

```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[dayOfMonth]
```

#### `DAY_OF_WEEK/DAYOFWEEK/DOW`

**Synopsis:**
```sql
DAY_OF_WEEK(datetime_exp) <1>
```

*Input*:

<1> date/datetime expression. If `null`, the function returns `null`.

*Output*: integer

*Description*: Extract the day of the week from a date/datetime. Sunday is `1`, Monday is `2`, etc.

```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[dayOfWeek]
```

#### `DAY_OF_YEAR/DOY`

**Synopsis:**
```sql
DAY_OF_YEAR(datetime_exp) <1>
```

*Input*:

<1> date/datetime expression. If `null`, the function returns `null`.

*Output*: integer

*Description*: Extract the day of the year from a date/datetime.

```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[dayOfYear]
```

#### `DAY_NAME/DAYNAME`

**Synopsis:**
```sql
DAY_NAME(datetime_exp) <1>
```

*Input*:

<1> date/datetime expression. If `null`, the function returns `null`.

*Output*: string

*Description*: Extract the day of the week from a date/datetime in text format (`Monday`, `Tuesday`...).

```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[dayName]
```

#### `HOUR_OF_DAY/HOUR`

**Synopsis:**
```sql
HOUR_OF_DAY(datetime_exp) <1>
```

*Input*:

<1> date/datetime expression. If `null`, the function returns `null`.

*Output*: integer

*Description*: Extract the hour of the day from a date/datetime.

```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[hourOfDay]
```

#### `ISO_DAY_OF_WEEK/ISODAYOFWEEK/ISODOW/IDOW`

**Synopsis:**
```sql
ISO_DAY_OF_WEEK(datetime_exp) <1>
```

*Input*:

<1> date/datetime expression. If `null`, the function returns `null`.

*Output*: integer

*Description*: Extract the day of the week from a date/datetime, following the [ISO 8601 standard](https://en.wikipedia.org/wiki/ISO_week_date).
Monday is `1`, Tuesday is `2`, etc.

```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[isoDayOfWeek]
```

#### `ISO_WEEK_OF_YEAR/ISOWEEKOFYEAR/ISOWEEK/IWOY/IW`

**Synopsis:**
```sql
ISO_WEEK_OF_YEAR(datetime_exp) <1>
```

*Input*:

<1> date/datetime expression. If `null`, the function returns `null`.

*Output*: integer

*Description*: Extract the week of the year from a date/datetime, following [ISO 8601 standard](https://en.wikipedia.org/wiki/ISO_week_date). The first week
of a year is the first week with a majority (4 or more) of its days in January.

```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[isoWeekOfYear]
```

#### `MINUTE_OF_DAY`

**Synopsis:**
```sql
MINUTE_OF_DAY(datetime_exp) <1>
```

*Input*:

<1> date/datetime expression. If `null`, the function returns `null`.

*Output*: integer

*Description*: Extract the minute of the day from a date/datetime.

```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[minuteOfDay]
```

#### `MINUTE_OF_HOUR/MINUTE`

**Synopsis:**
```sql
MINUTE_OF_HOUR(datetime_exp) <1>
```

*Input*:

<1> date/datetime expression. If `null`, the function returns `null`.

*Output*: integer

*Description*: Extract the minute of the hour from a date/datetime.

```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[minuteOfHour]
```

#### `MONTH_OF_YEAR/MONTH`

**Synopsis:**
```sql
MONTH(datetime_exp) <1>
```

*Input*:

<1> date/datetime expression. If `null`, the function returns `null`.

*Output*: integer

*Description*: Extract the month of the year from a date/datetime.

```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[monthOfYear]
```

#### `MONTH_NAME/MONTHNAME`

**Synopsis:**
```sql
MONTH_NAME(datetime_exp) <1>
```

*Input*:

<1> date/datetime expression. If `null`, the function returns `null`.

*Output*: string

*Description*: Extract the month from a date/datetime in text format (`January`, `February`...).

```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[monthName]
```

#### `NOW`

**Synopsis:**
```sql
NOW()
```

*Input*: _none_

*Output*: datetime

*Description*: This function offers the same functionality as CURRENT_TIMESTAMP() function: returns
the datetime when the current query reached the server. This method always returns the same value for its every
occurrence within the same query.

```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[nowFunction]
```

Typically, this function (as well as its twin CURRENT_TIMESTAMP()) function is used
for relative date/time filtering:

```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[filterNow]
```

#### `SECOND_OF_MINUTE/SECOND`

**Synopsis:**
```sql
SECOND_OF_MINUTE(datetime_exp) <1>
```

*Input*:

<1> date/datetime expression. If `null`, the function returns `null`.

*Output*: integer

*Description*: Extract the second of the minute from a date/datetime.

```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[secondOfMinute]
```

#### `QUARTER`

**Synopsis:**
```sql
QUARTER(datetime_exp) <1>
```

*Input*:

<1> date/datetime expression. If `null`, the function returns `null`.

*Output*: integer

*Description*: Extract the year quarter the date/datetime falls in.

```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[quarter]
```

#### `TODAY`

**Synopsis:**
```sql
TODAY()
```

*Input*: _none_

*Output*: date

*Description*: This function offers the same functionality as CURRENT_DATE() function: returns
the date when the current query reached the server. This method always returns the same value for its every occurrence
within the same query.

```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[todayFunction]
```

Typically, this function (as well as its twin CURRENT_TIMESTAMP()) function is used
for relative date filtering:

```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[filterToday]
```

#### `WEEK_OF_YEAR/WEEK`

**Synopsis:**
```sql
WEEK_OF_YEAR(datetime_exp) <1>
```

*Input*:

<1> date/datetime expression. If `null`, the function returns `null`.

*Output*: integer

*Description*: Extract the week of the year from a date/datetime.

```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[weekOfYear]
```

#### `YEAR`

**Synopsis:**
```sql
YEAR(datetime_exp) <1>
```

*Input*:

<1> date/datetime expression. If `null`, the function returns `null`.

*Output*: integer

*Description*: Extract the year from a date/datetime.

```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[year]
```

#### `EXTRACT`

**Synopsis:**
```sql
EXTRACT(
    datetime_function  <1>
    FROM datetime_exp) <2>
```

*Input*:

<1> date/time function name
<2> date/datetime expression

*Output*: integer

*Description*: Extract fields from a date/datetime by specifying the name of a datetime function.
The following

```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[extractDayOfYear]
```

is the equivalent to

```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[dayOfYear]
```
