<!-- Converted from modules/cassandra/pages/developing/cql/indexing/sai/_composite-partition-key-index.adoc (AsciiDoc). Includes are inlined. -->

# Index match on a composite partition key column

This example uses the following table and indexes:

```sql
CREATE TABLE IF NOT EXISTS cycling.rank_by_year_and_name (
CREATE INDEX race_name_idx 
    ON cycling.rank_by_year_and_name (race_name) 
    USING 'sai';
CREATE INDEX race_year_idx 
    ON cycling.rank_by_year_and_name (race_year) 
    USING 'sai';
```

Composite partition keys have a partition defined by multiple columns in a table.
Normally, you would need to specify all the columns in the partition key to query the table with a `WHERE` clause.
However, an SAI index makes it possible to define an index using a single column in the table's composite partition key.
You can create an SAI index on each column in the composite partition key, if you need to query based on just one column.

SAI indexes also allow you to query tables without using the inefficient `ALLOW FILTERING` directive. 
The `ALLOW FILTERING` directive requires scanning all the partitions in a table, leading to poor performance.

The `race_year` and `race_name` columns comprise the composite partition key for the `cycling.rank_by_year_and_name` table.

Query for a match on the column `race_name`:

Query::
+
--
```console
    SELECT * FROM cycling.rank_by_year_and_name 
        WHERE race_name = 'Tour of Japan - Stage 4 - Minami > Shinshu';
```
--

Result::
+
--
```results
 race_year | race_name                                  | rank | cyclist_name
-----------+--------------------------------------------+------+----------------------
      2014 | Tour of Japan - Stage 4 - Minami > Shinshu |    1 |        Daniel MARTIN
      2014 | Tour of Japan - Stage 4 - Minami > Shinshu |    2 | Johan Esteban CHAVES
      2014 | Tour of Japan - Stage 4 - Minami > Shinshu |    3 |      Benjamin PRADES
      2015 | Tour of Japan - Stage 4 - Minami > Shinshu |    1 |      Benjamin PRADES
      2015 | Tour of Japan - Stage 4 - Minami > Shinshu |    2 |          Adam PHELAN
      2015 | Tour of Japan - Stage 4 - Minami > Shinshu |    3 |         Thomas LEBAS
```
--

Query for a match on the column `race_year`:

Query::
+
--
```console
    SELECT * FROM cycling.rank_by_year_and_name 
        WHERE race_year = 2014;
```
--

Result::
+
--
```results

 race_year | race_name                                  | rank | cyclist_name
-----------+--------------------------------------------+------+----------------------
      2014 |                        4th Tour of Beijing |    1 |    Phillippe GILBERT
      2014 |                        4th Tour of Beijing |    2 |        Daniel MARTIN
      2014 |                        4th Tour of Beijing |    3 | Johan Esteban CHAVES
      2014 | Tour of Japan - Stage 4 - Minami > Shinshu |    1 |        Daniel MARTIN
      2014 | Tour of Japan - Stage 4 - Minami > Shinshu |    2 | Johan Esteban CHAVES
      2014 | Tour of Japan - Stage 4 - Minami > Shinshu |    3 |      Benjamin PRADES
```
--
