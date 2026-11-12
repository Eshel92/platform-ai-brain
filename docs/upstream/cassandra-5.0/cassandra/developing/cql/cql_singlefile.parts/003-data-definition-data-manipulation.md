<!-- Part 3 of 8 of cassandra/developing/cql/cql_singlefile.md (split because the page is big). -->

### Data Manipulation

[[insertStmt]]

#### INSERT

_Syntax:_

```bnf
::= INSERT INTO
( ( VALUES )
| ( JSON ))
( IF NOT EXISTS )?
( USING ( AND )* )?

::= `(' ( `,' )* `)'

::= `(' ( `,' )* `)'

::= TIMESTAMP
| TTL
```

_Sample:_

```sql
INSERT INTO NerdMovies (movie, director, main_actor, year)
VALUES ('Serenity', 'Joss Whedon', 'Nathan Fillion', 2005)
USING TTL 86400;

INSERT INTO NerdMovies JSON '{"movie": "Serenity", "director":
"Joss Whedon", "year": 2005}'
```

The `INSERT` statement writes one or more columns for a given row in a
table. Note that since a row is identified by its `PRIMARY KEY`, at
least the columns composing it must be specified. The list of columns to
insert to must be supplied when using the `VALUES` syntax. When using
the `JSON` syntax, they are optional. See the section on
link:#insertJson[`INSERT JSON`] for more details.

Note that unlike in SQL, `INSERT` does not check the prior existence of
the row by default: the row is created if none existed before, and
updated otherwise. Furthermore, there is no mean to know which of
creation or update happened.

It is however possible to use the `IF NOT EXISTS` condition to only
insert if the row does not exist prior to the insertion. But please note
that using `IF NOT EXISTS` will incur a non negligible performance cost
(internally, Paxos will be used) so this should be used sparingly.

All updates for an `INSERT` are applied atomically and in isolation.

Please refer to the link:#updateOptions[`UPDATE`] section for
information on the `<option>` available and to the
link:#collections[collections] section for use of
`<collection-literal>`. Also note that `INSERT` does not support
counters, while `UPDATE` does.

[[updateStmt]]

#### UPDATE

_Syntax:_

```bnf
::= UPDATE
( USING ( AND )* )?
SET ( `,' )*
WHERE
( IF ( AND condition )* )?

::= `='
| `=' (`+' | `-') ( | | )
| `=' `+'
| `[' `]' `='
| `.' `='

::=
| CONTAINS (KEY)?
| IN
| `[' `]'
| `[' `]' IN
| `.'
| `.' IN

::= `<' | `<=' | `=' | `!=' | `>=' | `>'
::= ( | `(' ( ( `,' )* )? `)')

::= ( AND )*

::= `='
| `(' (`,' )* `)' `='
| IN `(' ( ( `,' )* )? `)'
| IN
| `(' (`,' )* `)' IN `(' ( ( `,' )* )? `)'
| `(' (`,' )* `)' IN

::= TIMESTAMP
| TTL
```

_Sample:_

```sql
UPDATE NerdMovies USING TTL 400
SET director = 'Joss Whedon',
main_actor = 'Nathan Fillion',
year = 2005
WHERE movie = 'Serenity';

UPDATE UserActions SET total = total + 2 WHERE user =
B70DE1D0-9908-4AE3-BE34-5573E5B09F14 AND action = 'click';
```

The `UPDATE` statement writes one or more columns for a given row in a
table. The `<where-clause>` is used to select the row to update and must
include all columns composing the `PRIMARY KEY`. Other columns values
are specified through `<assignment>` after the `SET` keyword.

Note that unlike in SQL, `UPDATE` does not check the prior existence of
the row by default (except through the use of `<condition>`, see below):
the row is created if none existed before, and updated otherwise.
Furthermore, there are no means to know whether a creation or update
occurred.

It is however possible to use the conditions on some columns through
`IF`, in which case the row will not be updated unless the conditions
are met. But, please note that using `IF` conditions will incur a
non-negligible performance cost (internally, Paxos will be used) so this
should be used sparingly.

In an `UPDATE` statement, all updates within the same partition key are
applied atomically and in isolation.

The `c = c + 3` form of `<assignment>` is used to increment/decrement
counters. The identifier after the `=' sign *must* be the same than the
one before the `=' sign (Only increment/decrement is supported on
counters, not the assignment of a specific value).

The `id = id + <collection-literal>` and `id[value1] = value2` forms of
`<assignment>` are for collections. Please refer to the
link:#collections[relevant section] for more details.

The `id.field = <term>` form of `<assignemt>` is for setting the value
of a single field on a non-frozen user-defined types.

[[updateOptions]]

##### `<options>`

The `UPDATE` and `INSERT` statements support the following options:

* `TIMESTAMP`: sets the timestamp for the operation. If not specified,
the coordinator will use the current time (in microseconds) at the start
of statement execution as the timestamp. This is usually a suitable
default.
* `TTL`: specifies an optional Time To Live (in seconds) for the
inserted values. If set, the inserted values are automatically removed
from the database after the specified time. Note that the TTL concerns
the inserted values, not the columns themselves. This means that any
subsequent update of the column will also reset the TTL (to whatever TTL
is specified in that update). By default, values never expire. A TTL of
0 is equivalent to no TTL. If the table has a default_time_to_live, a
TTL of 0 will remove the TTL for the inserted or updated values.

[[deleteStmt]]

#### DELETE

_Syntax:_

```bnf
::= DELETE ( ( `,' )* )?
FROM
( USING TIMESTAMP )?
WHERE
( IF ( EXISTS | ( ( AND )*) ) )?

::=
| `[' `]'
| `.'

::= ( AND )*

::=
| `(' (`,' )* `)'
| IN `(' ( ( `,' )* )? `)'
| IN
| `(' (`,' )* `)' IN `(' ( ( `,' )* )? `)'
| `(' (`,' )* `)' IN

::= `=' | `<' | `>' | `<=' | `>='
::= ( | `(' ( ( `,' )* )? `)')

::= ( | `!=')
| CONTAINS (KEY)?
| IN
| `[' `]' ( | `!=')
| `[' `]' IN
| `.' ( | `!=')
| `.' IN
```

_Sample:_

```sql
DELETE FROM NerdMovies USING TIMESTAMP 1240003134 WHERE movie =
'Serenity';

DELETE phone FROM Users WHERE userid IN
(C73DE1D3-AF08-40F3-B124-3FF3E5109F22,
B70DE1D0-9908-4AE3-BE34-5573E5B09F14);
```

The `DELETE` statement deletes columns and rows. If column names are
provided directly after the `DELETE` keyword, only those columns are
deleted from the row indicated by the `<where-clause>`. The `id[value]`
syntax in `<selection>` is for non-frozen collections (please refer to
the link:#collections[collection section] for more details). The
`id.field` syntax is for the deletion of non-frozen user-defined types.
Otherwise, whole rows are removed. The `<where-clause>` specifies which
rows are to be deleted. Multiple rows may be deleted with one statement
by using an `IN` clause. A range of rows may be deleted using an
inequality operator (such as `>=`).

`DELETE` supports the `TIMESTAMP` option with the same semantics as the
link:#updateStmt[`UPDATE`] statement.

In a `DELETE` statement, all deletions within the same partition key are
applied atomically and in isolation.

A `DELETE` operation can be conditional through the use of an `IF`
clause, similar to `UPDATE` and `INSERT` statements. However, as with
`INSERT` and `UPDATE` statements, this will incur a non-negligible
performance cost (internally, Paxos will be used) and so should be used
sparingly.

[[batchStmt]]

#### BATCH

_Syntax:_

```bnf
::= BEGIN ( UNLOGGED | COUNTER ) BATCH
( USING ( AND )* )?
( `;' )*
APPLY BATCH

::=
|
|

::= TIMESTAMP
```

_Sample:_

```sql
BEGIN BATCH
INSERT INTO users (userid, password, name) VALUES ('user2', 'ch@ngem3b',
'second user');
UPDATE users SET password = 'ps22dhds' WHERE userid = 'user3';
INSERT INTO users (userid, password) VALUES ('user4', 'ch@ngem3c');
DELETE name FROM users WHERE userid = 'user1';
APPLY BATCH;
```

The `BATCH` statement group multiple modification statements
(insertions/updates and deletions) into a single statement. It serves
several purposes:

. It saves network round-trips between the client and the server (and
sometimes between the server coordinator and the replicas) when batching
multiple updates.
. All updates in a `BATCH` belonging to a given partition key are
performed in isolation.
. By default, all operations in the batch are performed as `LOGGED`, to
ensure all mutations eventually complete (or none will). See the notes
on link:#unloggedBatch[`UNLOGGED`] for more details.

Note that:

* `BATCH` statements may only contain `UPDATE`, `INSERT` and `DELETE`
statements.
* Batches are _not_ a full analogue for SQL transactions.
* If a timestamp is not specified for each operation, then all
operations will be applied with the same timestamp. Due to Cassandra’s
conflict resolution procedure in the case of
[timestamp ties](http://wiki.apache.org/cassandra/FAQ#clocktie),
operations may be applied in an order that is different from the order
they are listed in the `BATCH` statement. To force a particular
operation ordering, you must specify per-operation timestamps.

[[unloggedBatch]]

##### `UNLOGGED`

By default, Cassandra uses a batch log to ensure all operations in a
batch eventually complete or none will (note however that operations are
only isolated within a single partition).

There is a performance penalty for batch atomicity when a batch spans
multiple partitions. If you do not want to incur this penalty, you can
tell Cassandra to skip the batchlog with the `UNLOGGED` option. If the
`UNLOGGED` option is used, a failed batch might leave the patch only
partly applied.

[[counterBatch]]

##### `COUNTER`

Use the `COUNTER` option for batched counter updates. Unlike other
updates in Cassandra, counter updates are not idempotent.

[[batchOptions]]

##### `<option>`

`BATCH` supports both the `TIMESTAMP` option, with similar semantic to
the one described in the link:#updateOptions[`UPDATE`] statement (the
timestamp applies to all the statement inside the batch). However, if
used, `TIMESTAMP` *must not* be used in the statements within the batch.
