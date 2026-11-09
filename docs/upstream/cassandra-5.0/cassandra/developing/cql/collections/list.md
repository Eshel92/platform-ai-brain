<!-- Converted from modules/cassandra/pages/developing/cql/collections/list.adoc (AsciiDoc). Includes are inlined. -->

# Using list type

A `list` is similar to a `set`; it groups and stores values.
Unlike a `set`, the values stored in a `list` do not need to be unique and can be duplicated.
In addition, a `list` stores the elements in a particular order and may be inserted or retrieved according to an index value.

Use the `list` data type to store data that has a possible many-to-many relationship with another column.

## Prerequisite

* Keyspace must exist

In the following example, a `list` called `events` stores all the race events on an upcoming calendar.
The table is called `upcoming_calendar`. Each event listed in the `list` will have a `text` data type.
Events can have several events occurring in a particular month and year, so duplicates can occur.
The `list` can be ordered so that the races appear in the order that they will take place, rather than alphabetical order.

CQL::
+
--
```language-cql
CREATE TABLE IF NOT EXISTS cycling.upcoming_calendar (
```
--

Result::
+
--
```results
 year | month | events
------+-------+---------------------------------------------
 2015 |     6 | ['Criterium du Dauphine', 'Tour de Suisse']
 2015 |     7 |                          ['Tour de France']

(2 rows)

```
--
