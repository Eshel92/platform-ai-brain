<!-- Converted from modules/cassandra/pages/developing/cql/indexing/sai/_collections-list.adoc (AsciiDoc). Includes are inlined. -->

[[saiUsingCollectionsListExamples]]

# Using the list type

This example uses the following table and index:

```sql
CREATE TABLE IF NOT EXISTS cycling.upcoming_calendar (
CREATE INDEX events_idx 
    ON cycling.upcoming_calendar (events) 
    USING 'sai';
```

An index is created on the list column `events` in the `upcoming_calendar` table.

Query with `CONTAINS` from the list `events` column:

CQL::
+
--
```language-cql
SELECT * FROM cycling.upcoming_calendar 
   WHERE events CONTAINS 'Criterium du Dauphine';
```
--

Result::
+
--
```console
 year | month | events
------+-------+-----------------------------------------------
 2015 |     6 | ['Criterium du Dauphine', 'Tour de Sui\nsse']
```
--

A slightly more complex query selects rows that either contain a particular event or have a particular month date:

CQL::
+
--
```language-cql
SELECT * FROM cycling.upcoming_calendar
    WHERE events CONTAINS 'Criterium du Dauphine' 
          OR month = 7;
```
--

Result::
+
--
```console
 year | month | events
------+-------+-----------------------------------------------
 2015 |     6 | ['Criterium du Dauphine', 'Tour de Sui\nsse']
 2015 |     7 |                            ['Tour de France']
```
--
