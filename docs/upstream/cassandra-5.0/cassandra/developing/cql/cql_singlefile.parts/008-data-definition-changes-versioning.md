<!-- Part 8 of 8 of cassandra/developing/cql/cql_singlefile.md (split because the page is big). -->

### Changes

The following describes the changes in each version of CQL.

#### 3.4.3

* Support for `GROUP BY`. See link:#selectGroupBy[`<group-by>`] (see
[CASSANDRA-10707](https://issues.apache.org/jira/browse/CASSANDRA-10707)).

#### 3.4.2

* Support for selecting elements and slices of a collection
([CASSANDRA-7396](https://issues.apache.org/jira/browse/CASSANDRA-7396)).

#### 3.4.2

* link:#updateOptions[`INSERT/UPDATE options`] for tables having a
default_time_to_live specifying a TTL of 0 will remove the TTL from the
inserted or updated values
* link:#alterTableStmt[`ALTER TABLE`] `ADD` and `DROP` now allow mutiple
columns to be added/removed
* New link:#selectLimit[`PER PARTITION LIMIT`] option (see
[CASSANDRA-7017](https://issues.apache.org/jira/browse/CASSANDRA-7017)).
* link:#udfs[User-defined functions] can now instantiate `UDTValue` and
`TupleValue` instances via the new `UDFContext` interface (see
[CASSANDRA-10818](https://issues.apache.org/jira/browse/CASSANDRA-10818)).
* ``User-defined types''#createTypeStmt may now be stored in a
non-frozen form, allowing individual fields to be updated and deleted in
link:#updateStmt[`UPDATE` statements] and link:#deleteStmt[`DELETE`
statements], respectively.
([CASSANDRA-7423](https://issues.apache.org/jira/browse/CASSANDRA-7423))

#### 3.4.1

* Adds `CAST` functions. See link:#castFun[`Cast`].

#### 3.4.0

* Support for link:#createMVStmt[materialized views]
* link:#deleteStmt[`DELETE`] support for inequality expressions and `IN`
restrictions on any primary key columns
* link:#updateStmt[`UPDATE`] support for `IN` restrictions on any
primary key columns

#### 3.3.1

* The syntax `TRUNCATE TABLE X` is now accepted as an alias for
`TRUNCATE X`

#### 3.3.0

* Adds new link:#aggregates[aggregates]
* User-defined functions are now supported through
link:#createFunctionStmt[`CREATE FUNCTION`] and
link:#dropFunctionStmt[`DROP FUNCTION`].
* User-defined aggregates are now supported through
link:#createAggregateStmt[`CREATE AGGREGATE`] and
link:#dropAggregateStmt[`DROP AGGREGATE`].
* Allows double-dollar enclosed strings literals as an alternative to
single-quote enclosed strings.
* Introduces Roles to supercede user based authentication and access
control
* link:#usingdates[`Date`] and link:usingtime[`Time`] data types have
been added
* link:#json[`JSON`] support has been added
* `Tinyint` and `Smallint` data types have been added
* Adds new time conversion functions and deprecate `dateOf` and
`unixTimestampOf`. See link:#timeFun[`Time conversion functions`]

#### 3.2.0

* User-defined types are now supported through
link:#createTypeStmt[`CREATE TYPE`], link:#alterTypeStmt[`ALTER TYPE`],
and link:#dropTypeStmt[`DROP TYPE`]
* link:#createIndexStmt[`CREATE INDEX`] now supports indexing collection
columns, including indexing the keys of map collections through the
`keys()` function
* Indexes on collections may be queried using the new `CONTAINS` and
`CONTAINS KEY` operators
* Tuple types were added to hold fixed-length sets of typed positional
fields (see the section on link:#types[types] )
* link:#dropIndexStmt[`DROP INDEX`] now supports optionally specifying a
keyspace

#### 3.1.7

* `SELECT` statements now support selecting multiple rows in a single
partition using an `IN` clause on combinations of clustering columns.
See link:#selectWhere[SELECT WHERE] clauses.
* `IF NOT EXISTS` and `IF EXISTS` syntax is now supported by
`CREATE USER` and `DROP USER` statmenets, respectively.

#### 3.1.6

* A new link:#uuidFun[`uuid` method] has been added.
* Support for `DELETE ... IF EXISTS` syntax.

#### 3.1.5

* It is now possible to group clustering columns in a relatiion, see
link:#selectWhere[SELECT WHERE] clauses.
* Added support for `STATIC` columns, see link:#createTableStatic[static
in CREATE TABLE].

#### 3.1.4

* `CREATE INDEX` now allows specifying options when creating CUSTOM
indexes (see link:#createIndexStmt[CREATE INDEX reference] ).

#### 3.1.3

* Millisecond precision formats have been added to the timestamp parser
(see link:#usingtimestamps[working with dates] ).

#### 3.1.2

* `NaN` and `Infinity` has been added as valid float contants. They are
now reserved keywords. In the unlikely case you we using them as a
column identifier (or keyspace/table one), you will noew need to double
quote them (see link:#identifiers[quote identifiers] ).

#### 3.1.1

* `SELECT` statement now allows listing the partition keys (using the
`DISTINCT` modifier). See
[CASSANDRA-4536](https://issues.apache.org/jira/browse/CASSANDRA-4536).
* The syntax `c IN ?` is now supported in `WHERE` clauses. In that case,
the value expected for the bind variable will be a list of whatever type
`c` is.
* It is now possible to use named bind variables (using `:name` instead
of `?`).

#### 3.1.0

* link:#alterTableStmt[ALTER TABLE] `DROP` option has been reenabled for
CQL3 tables and has new semantics now: the space formerly used by
dropped columns will now be eventually reclaimed (post-compaction). You
should not readd previously dropped columns unless you use timestamps
with microsecond precision (see
[CASSANDRA-3919](https://issues.apache.org/jira/browse/CASSANDRA-3919) for
more details).
* `SELECT` statement now supports aliases in select clause. Aliases in
WHERE and ORDER BY clauses are not supported. See the
link:#selectStmt[section on select] for details.
* `CREATE` statements for `KEYSPACE`, `TABLE` and `INDEX` now supports
an `IF NOT EXISTS` condition. Similarly, `DROP` statements support a
`IF EXISTS` condition.
* `INSERT` statements optionally supports a `IF NOT EXISTS` condition
and `UPDATE` supports `IF` conditions.

#### 3.0.5

* `SELECT`, `UPDATE`, and `DELETE` statements now allow empty `IN`
relations (see
[CASSANDRA-5626](https://issues.apache.org/jira/browse/CASSANDRA-5626)).

#### 3.0.4

* Updated the syntax for custom link:#createIndexStmt[secondary
indexes].
* Non-equal condition on the partition key are now never supported, even
for ordering partitioner as this was not correct (the order was *not*
the one of the type of the partition key). Instead, the `token` method
should always be used for range queries on the partition key (see
link:#selectWhere[WHERE clauses] ).

#### 3.0.3

* Support for custom link:#createIndexStmt[secondary indexes] has been
added.

#### 3.0.2

* Type validation for the link:#constants[constants] has been fixed. For
instance, the implementation used to allow `'2'` as a valid value for an
`int` column (interpreting it has the equivalent of `2`), or `42` as a
valid `blob` value (in which case `42` was interpreted as an hexadecimal
representation of the blob). This is no longer the case, type validation
of constants is now more strict. See the link:#types[data types] section
for details on which constant is allowed for which type.
* The type validation fixed of the previous point has lead to the
introduction of link:#constants[blobs constants] to allow inputing
blobs. Do note that while inputing blobs as strings constant is still
supported by this version (to allow smoother transition to blob
constant), it is now deprecated (in particular the link:#types[data
types] section does not list strings constants as valid blobs) and will
be removed by a future version. If you were using strings as blobs, you
should thus update your client code ASAP to switch blob constants.
* A number of functions to convert native types to blobs have also been
introduced. Furthermore the token function is now also allowed in select
clauses. See the link:#functions[section on functions] for details.

#### 3.0.1

* link:#usingtimestamps[Date strings] (and timestamps) are no longer
accepted as valid `timeuuid` values. Doing so was a bug in the sense
that date string are not valid `timeuuid`, and it was thus resulting in
https://issues.apache.org/jira/browse/CASSANDRA-4936[confusing
behaviors]. However, the following new methods have been added to help
working with `timeuuid`: `now`, `minTimeuuid`, `maxTimeuuid` , `dateOf`
and `unixTimestampOf`. See the link:#timeuuidFun[section dedicated to
these methods] for more detail.
* ``Float constants''#constants now support the exponent notation. In
other words, `4.2E10` is now a valid floating point value.


### Versioning

Versioning of the CQL language adheres to the http://semver.org[Semantic
Versioning] guidelines. Versions take the form X.Y.Z where X, Y, and Z
are integer values representing major, minor, and patch level
respectively. There is no correlation between Cassandra release versions
and the CQL language version.

|===
|version |description
|Major |The major version _must_ be bumped when backward incompatible
changes are introduced. This should rarely occur.

|Minor |Minor version increments occur when new, but backward
compatible, functionality is introduced.

|Patch |The patch version is incremented when bugs are fixed.
|===
