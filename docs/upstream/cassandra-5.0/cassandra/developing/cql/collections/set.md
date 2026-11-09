<!-- Converted from modules/cassandra/pages/developing/cql/collections/set.adoc (AsciiDoc). Includes are inlined. -->

# `set` column

A `set` consists of a unordered group of elements with unique values.
Duplicate values will not be stored distinctly.
The values of a `set` are stored unordered, but will return the elements in sorted order when queried.
Use the `set` data type to store data that has a many-to-one relationship with another column.

## Prerequisite

* Keyspace must exist

In the following example, a `set` called `teams` stores all the teams that a cyclist has been a member of during their career.
The table is `cyclist_career_teams`.
Each team listed in the `set` will have a `text` data type.

The following example shows the table and the initial rows.

CQL::
+
--
```language-cql
CREATE TABLE IF NOT EXISTS cycling.cyclist_career_teams (
```
--

Result::
+
--
```results
 id                                   | lastname        | teams
--------------------------------------+-----------------+--------------------------------------------------------------------------------
----------------------
 cb07baad-eac8-4f65-b28a-bddc06a0de23 |      ARMITSTEAD |                    {'AA Drink - Leontien.nl', 'Boels-Dolmans Cycling Team', 'Te
am Garmin - Cervelo'}
 5b6962dd-3f90-4c93-8f61-eabfa4a803e2 |             VOS | {'Nederland bloeit', 'Rabobank Women Team', 'Rabobank-Liv Giant', 'Rabobank-Liv
 Woman Cycling Team'}
 1c9ebc13-1eab-4ad5-be87-dce433216d40 |           BRAND |   {'AA Drink - Leontien.nl', 'Leontien.nl', 'Rabobank-Liv Giant', 'Rabobank-Liv
 Woman Cycling Team'}
 e7cd5752-bc0d-4157-a80f-7523add8dbcd | VAN DER BREGGEN |                 {'Rabobank-Liv Woman Cycling Team', 'Sengers Ladies Cycling Tea
m', 'Team Flexpoint'}

(4 rows)

```
--
