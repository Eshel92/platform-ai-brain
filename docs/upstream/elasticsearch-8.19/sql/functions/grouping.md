<!-- Converted from sql/functions/grouping.asciidoc (AsciiDoc). Includes are inlined. -->

### Grouping Functions

Functions for creating special __grouping__s (also known as _bucketing_); as such these need to be used
as part of the grouping.

#### `HISTOGRAM`

**Synopsis:**
```sql
HISTOGRAM(
    numeric_exp,        <1>
    numeric_interval)   <2>

HISTOGRAM(
    date_exp,           <3>
    date_time_interval) <4>
```

*Input*:

<1> numeric expression (typically a field). If this field contains only `null`
values, the function returns `null`. Otherwise, the function ignores `null`
values in this field.
<2> numeric interval. If `null`, the function returns `null`.
<3> date/time expression (typically a field). If this field contains only `null`
values, the function returns `null`. Otherwise, the function ignores `null`
values in this field.
<4> date/time interval. If `null`, the
function returns `null`.

*Output*: non-empty buckets or groups of the given expression divided according to the given interval

*Description*: The histogram function takes all matching values and divides them into buckets with fixed size matching the given interval, using (roughly) the following formula:

```sql
bucket_key = Math.floor(value / interval) * interval
```

The histogram in SQL does *NOT* return empty buckets for missing intervals as the traditional histogram and  date histogram. Such behavior does not fit conceptually in SQL which treats all missing values as `null`; as such the histogram places all missing values in the `null` group.

`Histogram` can be applied on either numeric fields:

```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[histogramNumeric]
```

or date/time fields:

```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[histogramDateTime]
```

Expressions inside the histogram are also supported as long as the
return type is numeric:

```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[histogramNumericExpression]
```

Do note that histograms (and grouping functions in general) allow custom expressions but cannot have any functions applied to them in the `GROUP BY`. In other words, the following statement is *NOT* allowed:

```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[expressionOnHistogramNotAllowed]
```

as it requires two groupings (one for histogram followed by a second for applying the function on top of the histogram groups).

Instead one can rewrite the query to move the expression on the histogram _inside_ of it:

```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[histogramDateTimeExpression]
```

When the histogram in SQL is applied on **DATE** type instead of **DATETIME**, the interval specified is truncated to
the multiple of a day. E.g.: for `HISTOGRAM(CAST(birth_date AS DATE), INTERVAL '2 3:04' DAY TO MINUTE)` the interval
actually used will be `INTERVAL '2' DAY`. If the interval specified is less than 1 day, e.g.:
`HISTOGRAM(CAST(birth_date AS DATE), INTERVAL '20' HOUR)` then the interval used will be `INTERVAL '1' DAY`.

All intervals specified for a date/time HISTOGRAM will use a fixed interval
in their `date_histogram` aggregation definition, with the notable exceptions of `INTERVAL '1' YEAR`, `INTERVAL '1' MONTH` and `INTERVAL '1' DAY`  where a calendar interval is used.
The choice for a calendar interval was made for having a more intuitive result for YEAR, MONTH and DAY groupings. In the case of YEAR, for example, the calendar intervals consider a one year
bucket as the one starting on January 1st that specific year, whereas a fixed interval one-year-bucket considers one year as a number
of milliseconds (for example, `31536000000ms` corresponding to 365 days, 24 hours per day, 60 minutes per hour etc.). With fixed intervals,
the day of February 5th, 2019 for example, belongs to a bucket that starts on December 20th, 2018 and Elasticsearch (and implicitly {es-sql}) would
have returned the year 2018 for a date that's actually in 2019. With calendar interval this behavior is more intuitive, having the day of
February 5th, 2019 actually belonging to the 2019 year bucket. 

Histogram in SQL cannot be applied on **TIME** type.
E.g.: `HISTOGRAM(CAST(birth_date AS TIME), INTERVAL '10' MINUTES)` is currently not supported.
