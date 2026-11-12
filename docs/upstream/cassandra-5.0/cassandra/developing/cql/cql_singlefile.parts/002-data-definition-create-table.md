<!-- Part 2 of 8 of cassandra/developing/cql/cql_singlefile.md (split because the page is big). -->

### CREATE TABLE

_Syntax:_

```bnf
::= CREATE ( TABLE | COLUMNFAMILY ) ( IF NOT EXISTS )?
`(' ( `,' )* `)'
( WITH ( AND )* )?

::= ( STATIC )? ( PRIMARY KEY )?
| PRIMARY KEY `(' ( `,' )* `)'

::=
| `(' (`,' )* `)'

::=
| COMPACT STORAGE
| CLUSTERING ORDER
```

_Sample:_

```sql
CREATE TABLE monkeySpecies (
species text PRIMARY KEY,
common_name text,
population varint,
average_size int
) WITH comment='Important biological records';

CREATE TABLE timeline (
userid uuid,
posted_month int,
posted_time uuid,
body text,
posted_by text,
PRIMARY KEY (userid, posted_month, posted_time)
) WITH compaction = { 'class' : 'LeveledCompactionStrategy' };
```
The `CREATE TABLE` statement creates a new table. Each such table is a
set of _rows_ (usually representing related entities) for which it
defines a number of properties. A table is defined by a
link:#createTableName[name], it defines the columns composing rows of
the table and have a number of link:#createTableOptions[options]. Note
that the `CREATE COLUMNFAMILY` syntax is supported as an alias for
`CREATE TABLE` (for historical reasons).

Attempting to create an already existing table will return an error
unless the `IF NOT EXISTS` option is used. If it is used, the statement
will be a no-op if the table already exists.

[[createTableName]]

#### `<tablename>`

Valid table names are the same as valid
link:#createKeyspaceStmt[keyspace names] (up to 32 characters long
alphanumerical identifiers). If the table name is provided alone, the
table is created within the current keyspace (see `USE`), but if it is
prefixed by an existing keyspace name (see
link:#statements[`<tablename>`] grammar), it is created in the specified
keyspace (but does *not* change the current keyspace).

[[createTableColumn]]

#### `<column-definition>`

A `CREATE TABLE` statement defines the columns that rows of the table
can have. A _column_ is defined by its name (an identifier) and its type
(see the link:#types[data types] section for more details on allowed
types and their properties).

Within a table, a row is uniquely identified by its `PRIMARY KEY` (or
more simply the key), and hence all table definitions *must* define a
PRIMARY KEY (and only one). A `PRIMARY KEY` is composed of one or more
of the columns defined in the table. If the `PRIMARY KEY` is only one
column, this can be specified directly after the column definition.
Otherwise, it must be specified by following `PRIMARY KEY` by the
comma-separated list of column names composing the key within
parenthesis. Note that:

```sql
CREATE TABLE t (
k int PRIMARY KEY,
other text
)
```

is equivalent to

```sql
CREATE TABLE t (
k int,
other text,
PRIMARY KEY (k)
)
```

[[createTablepartitionClustering]]

#### Partition key and clustering columns

In CQL, the order in which columns are defined for the `PRIMARY KEY`
matters. The first column of the key is called the _partition key_. It
has the property that all the rows sharing the same partition key (even
across table in fact) are stored on the same physical node. Also,
insertion/update/deletion on rows sharing the same partition key for a
given table are performed _atomically_ and in _isolation_. Note that it
is possible to have a composite partition key, i.e. a partition key
formed of multiple columns, using an extra set of parentheses to define
which columns forms the partition key.

The remaining columns of the `PRIMARY KEY` definition, if any, are
called __clustering columns. On a given physical node, rows for a given
partition key are stored in the order induced by the clustering columns,
making the retrieval of rows in that clustering order particularly
efficient (see `SELECT`).

[[createTableStatic]]

#### `STATIC` columns

Some columns can be declared as `STATIC` in a table definition. A column
that is static will be ``shared'' by all the rows belonging to the same
partition (having the same partition key). For instance, in:

```sql
CREATE TABLE test (
pk int,
t int,
v text,
s text static,
PRIMARY KEY (pk, t)
);
INSERT INTO test(pk, t, v, s) VALUES (0, 0, 'val0', 'static0');
INSERT INTO test(pk, t, v, s) VALUES (0, 1, 'val1', 'static1');
SELECT * FROM test WHERE pk=0 AND t=0;
```

the last query will return `'static1'` as value for `s`, since `s` is
static and thus the 2nd insertion modified this ``shared'' value. Note
however that static columns are only static within a given partition,
and if in the example above both rows where from different partitions
(i.e. if they had different value for `pk`), then the 2nd insertion
would not have modified the value of `s` for the first row.

A few restrictions applies to when static columns are allowed:

* tables with the `COMPACT STORAGE` option (see below) cannot have them
* a table without clustering columns cannot have static columns (in a
table without clustering columns, every partition has only one row, and
so every column is inherently static).
* only non `PRIMARY KEY` columns can be static

[[createTableOptions]]

#### `<option>`

The `CREATE TABLE` statement supports a number of options that controls
the configuration of a new table. These options can be specified after
the `WITH` keyword.

The first of these option is `COMPACT STORAGE`. This option is mainly
targeted towards backward compatibility for definitions created before
CQL3 (see
[www.datastax.com/dev/blog/thrift-to-cql3](http://www.datastax.com/dev/blog/thrift-to-cql3)
for more details). The option also provides a slightly more compact
layout of data on disk but at the price of diminished flexibility and
extensibility for the table. Most notably, `COMPACT STORAGE` tables
cannot have collections nor static columns and a `COMPACT STORAGE` table
with at least one clustering column supports exactly one (as in not 0
nor more than 1) column not part of the `PRIMARY KEY` definition (which
imply in particular that you cannot add nor remove columns after
creation). For those reasons, `COMPACT STORAGE` is not recommended
outside of the backward compatibility reason evoked above.

Another option is `CLUSTERING ORDER`. It allows to define the ordering
of rows on disk. It takes the list of the clustering column names with,
for each of them, the on-disk order (Ascending or descending). Note that
this option affects link:#selectOrderBy[what `ORDER BY` are allowed
during `SELECT`].

Table creation supports the following other `<property>`:

|===
|option |kind |default |description
|`comment` |_simple_ |none |A free-form, human-readable comment.

|`gc_grace_seconds` |_simple_ |864000 |Time to wait before garbage
collecting tombstones (deletion markers).

|`bloom_filter_fp_chance` |_simple_ |0.00075 |The target probability of
false positive of the sstable bloom filters. Said bloom filters will be
sized to provide the provided probability (thus lowering this value
impact the size of bloom filters in-memory and on-disk)

|`default_time_to_live` |_simple_ |0 |The default expiration time
(``TTL'') in seconds for a table.

|`compaction` |_map_ |_see below_ |Compaction options, see
link:#compactionOptions[below].

|`compression` |_map_ |_see below_ |Compression options, see
link:#compressionOptions[below].

|`caching` |_map_ |_see below_ |Caching options, see
link:#cachingOptions[below].

|`crc_check_chance` |simple|1.0|This option defines the probability with which checksums
should be checked during reads to detect bit rot and prevent the propagation of corruption
to other replicas. The default value is 1 to apply a checksum every time a data chunk is read.
Set to 0 to disable checksum checking and to 0.5 for instance to check every other read.

Due to technical limitations we only currently apply this for compressed files.
If compression is not enabled on the table, no checksums will be verified.
|===

[[compactionOptions]]

#### Compaction options

The `compaction` property must at least define the `'class'` sub-option,
that defines the compaction strategy class to use. The default supported
class are `'SizeTieredCompactionStrategy'`,
`'LeveledCompactionStrategy'` and
`'TimeWindowCompactionStrategy'`. Custom strategy can be provided by
specifying the full class name as a link:#constants[string constant].
The rest of the sub-options depends on the chosen class. The sub-options
supported by the default classes are:

|===
|option |supported compaction strategy |default |description
|`enabled` |_all_ |true |A boolean denoting whether compaction should be
enabled or not.

|`tombstone_threshold` |_all_ |0.2 |A ratio such that if a sstable has
more than this ratio of gcable tombstones over all contained columns,
the sstable will be compacted (with no other sstables) for the purpose
of purging those tombstones.

|`tombstone_compaction_interval` |_all_ |1 day |The minimum time to wait
after an sstable creation time before considering it for ``tombstone
compaction'', where ``tombstone compaction'' is the compaction triggered
if the sstable has more gcable tombstones than `tombstone_threshold`.

|`unchecked_tombstone_compaction` |_all_ |false |Setting this to true
enables more aggressive tombstone compactions - single sstable tombstone
compactions will run without checking how likely it is that they will be
successful.

|`min_sstable_size` |SizeTieredCompactionStrategy |50MB |The size tiered
strategy groups SSTables to compact in buckets. A bucket groups SSTables
that differs from less than 50% in size. However, for small sizes, this
would result in a bucketing that is too fine grained. `min_sstable_size`
defines a size threshold (in bytes) below which all SSTables belong to
one unique bucket

|`min_threshold` |SizeTieredCompactionStrategy |4 |Minimum number of
SSTables needed to start a minor compaction.

|`max_threshold` |SizeTieredCompactionStrategy |32 |Maximum number of
SSTables processed by one minor compaction.

|`bucket_low` |SizeTieredCompactionStrategy |0.5 |Size tiered consider
sstables to be within the same bucket if their size is within
[average_size * `bucket_low`, average_size * `bucket_high` ] (i.e the
default groups sstable whose sizes diverges by at most 50%)

|`bucket_high` |SizeTieredCompactionStrategy |1.5 |Size tiered consider
sstables to be within the same bucket if their size is within
[average_size * `bucket_low`, average_size * `bucket_high` ] (i.e the
default groups sstable whose sizes diverges by at most 50%).

|`sstable_size_in_mb` |LeveledCompactionStrategy |5MB |The target size
(in MB) for sstables in the leveled strategy. Note that while sstable
sizes should stay less or equal to `sstable_size_in_mb`, it is possible
to exceptionally have a larger sstable as during compaction, data for a
given partition key are never split into 2 sstables

|`timestamp_resolution` |TimeWindowCompactionStrategy |MICROSECONDS |The
timestamp resolution used when inserting data, could be MILLISECONDS,
MICROSECONDS etc (should be understandable by Java TimeUnit) - don’t
change this unless you do mutations with USING TIMESTAMP (or equivalent
directly in the client)

|`compaction_window_unit` |TimeWindowCompactionStrategy |DAYS |The Java
TimeUnit used for the window size, set in conjunction with
`compaction_window_size`. Must be one of DAYS, HOURS, MINUTES

|`compaction_window_size` |TimeWindowCompactionStrategy |1 |The number
of `compaction_window_unit` units that make up a time window.

|`unsafe_aggressive_sstable_expiration` |TimeWindowCompactionStrategy
|false |Expired sstables will be dropped without checking its data is
shadowing other sstables. This is a potentially risky option that can
lead to data loss or deleted data re-appearing, going beyond what
`unchecked_tombstone_compaction` does for single sstable compaction. Due
to the risk the jvm must also be started with
`-Dcassandra.unsafe_aggressive_sstable_expiration=true`.
|===

[[compressionOptions]]

##### Compression options

For the `compression` property, the following sub-options are available:

|===
|option |default |description | | |
|`class` |LZ4Compressor |The compression algorithm to use. Default
compressor are: LZ4Compressor, SnappyCompressor and DeflateCompressor.
Use `'enabled' : false` to disable compression. Custom compressor can be
provided by specifying the full class name as a link:#constants[string
constant]. | | |

|`enabled` |true |By default compression is enabled. To disable it, set
`enabled` to `false` |`chunk_length_in_kb` |64KB |On disk SSTables are
compressed by block (to allow random reads). This defines the size (in
KB) of said block. Bigger values may improve the compression rate, but
increases the minimum size of data to be read from disk for a read
|===

[[cachingOptions]]

##### Caching options

For the `caching` property, the following sub-options are available:

|===
|option |default |description
|`keys` |ALL |Whether to cache keys (``key cache'') for this table.
Valid values are: `ALL` and `NONE`.

|`rows_per_partition` |NONE |The amount of rows to cache per partition
(``row cache''). If an integer `n` is specified, the first `n` queried
rows of a partition will be cached. Other possible options are `ALL`, to
cache all rows of a queried partition, or `NONE` to disable row caching.
|===

##### Other considerations:

* When link:#insertStmt[inserting] / link:#updateStmt[updating] a given
row, not all columns needs to be defined (except for those part of the
key), and missing columns occupy no space on disk. Furthermore, adding
new columns (see `ALTER TABLE`) is a constant time operation. There is
thus no need to try to anticipate future usage (or to cry when you
haven’t) when creating a table.

[[alterTableStmt]]

#### ALTER TABLE

_Syntax:_

```bnf
::= ALTER (TABLE | COLUMNFAMILY) (IF EXISTS)?

::= ADD (IF NOT EXISTS)?
| ADD  (IF NOT EXISTS)? ( ( , )* )
| DROP (IF EXISTS)?
| DROP (IF EXISTS)? ( ( , )* )
| RENAME (IF EXISTS)? TO (AND TO)*
| WITH ( AND )*
```

_Sample:_

```sql
ALTER TABLE addamsFamily

ALTER TABLE addamsFamily
ADD gravesite varchar;

ALTER TABLE addamsFamily
WITH comment = 'A most excellent and useful column family';
```

The `ALTER` statement is used to manipulate table definitions. It allows
for adding new columns, dropping existing ones, or updating the table
options. As with table creation, `ALTER COLUMNFAMILY` is allowed as an
alias for `ALTER TABLE`.
If the table does not exist, the statement will return an error, unless `IF EXISTS` is used in which case the operation is a no-op.

The `<tablename>` is the table name optionally preceded by the keyspace
name. The `<instruction>` defines the alteration to perform:

* `ADD`: Adds a new column to the table. The `<identifier>` for the new
column must not conflict with an existing column. Moreover, columns
cannot be added to tables defined with the `COMPACT STORAGE` option.
If the new column already exists, the statement will return an error, unless `IF NOT EXISTS` is used in which case the operation is a no-op.
* `DROP`: Removes a column from the table. Dropped columns will
immediately become unavailable in the queries and will not be included
in compacted sstables in the future. If a column is readded, queries
won’t return values written before the column was last dropped. It is
assumed that timestamps represent actual time, so if this is not your
case, you should NOT read previously dropped columns. Columns can’t be
dropped from tables defined with the `COMPACT STORAGE` option.
If the dropped column does not already exist, the statement will return an error, unless `IF EXISTS` is used in which case the operation is a no-op.
* `RENAME` a primary key column of a table. Non primary key columns cannot be renamed.
Furthermore, renaming a column to another name which already exists isn't allowed.
It's important to keep in mind that renamed columns shouldn't have dependent seconday indexes.
If the renamed column does not already exist, the statement will return an error, unless `IF EXISTS` is used in which case the operation is a no-op.

* `WITH`: Allows to update the options of the table. The
link:#createTableOptions[supported `<option>`] (and syntax) are the same
as for the `CREATE TABLE` statement except that `COMPACT STORAGE` is not
supported. Note that setting any `compaction` sub-options has the effect
of erasing all previous `compaction` options, so you need to re-specify
all the sub-options if you want to keep them. The same note applies to
the set of `compression` sub-options.

##### CQL type compatibility:

CQL data types may be converted only as the following table.

|===
|Data type may be altered to: |Data type
|timestamp |bigint

|ascii, bigint, boolean, date, decimal, double, float, inet, int,
smallint, text, time, timestamp, timeuuid, tinyint, uuid, varchar,
varint |blob

|int |date

|ascii, varchar |text

|bigint |time

|bigint |timestamp

|timeuuid |uuid

|ascii, text |varchar

|bigint, int, timestamp |varint
|===

Clustering columns have stricter requirements, only the below
conversions are allowed.

|===
|Data type may be altered to: |Data type
|ascii, text, varchar |blob
|ascii, varchar |text
|ascii, text |varchar
|===

[[dropTableStmt]]

#### DROP TABLE

_Syntax:_

::= DROP TABLE ( IF EXISTS )?

_Sample:_

 DROP TABLE worldSeriesAttendees;

The `DROP TABLE` statement results in the immediate, irreversible
removal of a table, including all data contained in it. As for table
creation, `DROP COLUMNFAMILY` is allowed as an alias for `DROP TABLE`.

If the table does not exist, the statement will return an error, unless
`IF EXISTS` is used in which case the operation is a no-op.

[[truncateStmt]]

#### TRUNCATE

_Syntax:_

::= TRUNCATE ( TABLE | COLUMNFAMILY )?

_Sample:_

 TRUNCATE superImportantData;

The `TRUNCATE` statement permanently removes all data from a table.

[[createIndexStmt]]

#### CREATE INDEX

The `CREATE INDEX` statement is used to create a new
secondary index for a given (existing) column in a given table. A name
for the index itself can be specified before the `ON` keyword, if
desired.

_Syntax:_

```bnf
::= CREATE ( CUSTOM )? INDEX ( IF NOT EXISTS )? ( )?
ON `(' `)'
( USING ( WITH OPTIONS = )? )?

::=
| keys( )
```

_Sample:_

```sql
CREATE INDEX userIndex ON NerdMovies (user);
CREATE INDEX ON Mutants (abilityId);
CREATE INDEX ON users (keys(favs));
CREATE INDEX ON users (age) USING 'sai';
CREATE CUSTOM INDEX ON users (email) USING 'path.to.the.IndexClass';
CREATE CUSTOM INDEX ON users (email) USING 'path.to.the.IndexClass' WITH
OPTIONS = {'storage': '/mnt/ssd/indexes/'};
```

If data already exists for the column, it will be indexed
asynchronously. After the index is created, new data for the column is
indexed automatically at insertion time. Attempting to create an already
existing index will return an error unless the `IF NOT EXISTS` option is used.
If it is used, the statement will be a no-op if the index already exists.

[[indexTypes]]

##### Index Types

The `USING` keyword optionally specifies an index type. There are two built-in types:

- legacy_local_table - (default) legacy secondary index, implemented as a hidden local table
- sai - "storage-attched" index, implemented via optimized SSTable/Memtable-attached indexes

To create a custom index, a fully qualified class name must be specified.

[[keysIndex]]

##### Indexes on Map Keys

When creating an index on a link:#map[map column], you may index either
the keys or the values. If the column identifier is placed within the
`keys()` function, the index will be on the map keys, allowing you to
use `CONTAINS KEY` in `WHERE` clauses. Otherwise, the index will be on
the map values.

[[dropIndexStmt]]

#### DROP INDEX

_Syntax:_

DROP INDEX ( IF EXISTS )? ('.')?

_Sample:_

```sql
DROP INDEX userIndex;
DROP INDEX userkeyspace.address_index;
```

The `DROP INDEX` statement is used to drop an existing secondary index.
The argument of the statement is the index name, which may optionally
specify the keyspace of the index.

If the index does not exists, the statement will return an error, unless
`IF EXISTS` is used in which case the operation is a no-op.

[[createMVStmt]]

#### CREATE MATERIALIZED VIEW

_Syntax:_

```bnf
::= CREATE MATERIALIZED VIEW ( IF NOT EXISTS )? AS
SELECT ( `(' ( `,' ) * `)' | `*' )
FROM
( WHERE )?
PRIMARY KEY `(' ( `,' )* `)'
( WITH ( AND )* )?
```

_Sample:_

```sql
CREATE MATERIALIZED VIEW monkeySpecies_by_population AS
SELECT *
FROM monkeySpecies
WHERE population IS NOT NULL AND species IS NOT NULL
PRIMARY KEY (population, species)
WITH comment='Allow query by population instead of species';
```

The `CREATE MATERIALIZED VIEW` statement creates a new materialized
view. Each such view is a set of _rows_ which corresponds to rows which
are present in the underlying, or base, table specified in the `SELECT`
statement. A materialized view cannot be directly updated, but updates
to the base table will cause corresponding updates in the view.

Attempting to create an already existing materialized view will return
an error unless the `IF NOT EXISTS` option is used. If it is used, the
statement will be a no-op if the materialized view already exists.

[[createMVWhere]]

##### `WHERE` Clause

The `<where-clause>` is similar to the link:#selectWhere[where clause of
a `SELECT` statement], with a few differences. First, the where clause
must contain an expression that disallows `NULL` values in columns in
the view’s primary key. If no other restriction is desired, this can be
accomplished with an `IS NOT NULL` expression. Second, only columns
which are in the base table’s primary key may be restricted with
expressions other than `IS NOT NULL`. (Note that this second restriction
may be lifted in the future.)

[[alterMVStmt]]

#### ALTER MATERIALIZED VIEW

_Syntax:_

::= ALTER MATERIALIZED VIEW WITH ( AND )*

The `ALTER MATERIALIZED VIEW` statement allows options to be update;
these options are the same as `CREATE TABLE`’s options.

[[dropMVStmt]]

#### DROP MATERIALIZED VIEW

_Syntax:_

::= DROP MATERIALIZED VIEW ( IF EXISTS )?

_Sample:_

DROP MATERIALIZED VIEW monkeySpecies_by_population;

The `DROP MATERIALIZED VIEW` statement is used to drop an existing
materialized view.

If the materialized view does not exists, the statement will return an
error, unless `IF EXISTS` is used in which case the operation is a
no-op.

[[createTypeStmt]]

#### CREATE TYPE

_Syntax:_

```bnf
::= CREATE TYPE ( IF NOT EXISTS )?
`(' ( `,' )* `)'

::= ( `.' )?

::=
```

_Sample:_

```sql
CREATE TYPE address (
street_name text,
street_number int,
city text,
state text,
zip int
)

CREATE TYPE work_and_home_addresses (
home_address address,
work_address address
)
```

The `CREATE TYPE` statement creates a new user-defined type. Each type
is a set of named, typed fields. Field types may be any valid type,
including collections and other existing user-defined types.

Attempting to create an already existing type will result in an error
unless the `IF NOT EXISTS` option is used. If it is used, the statement
will be a no-op if the type already exists.

[[createTypeName]]

##### `<typename>`

Valid type names are identifiers. The names of existing CQL types and
link:#appendixB[reserved type names] may not be used.

If the type name is provided alone, the type is created with the current
keyspace (see `USE`). If it is prefixed by an existing keyspace name,
the type is created within the specified keyspace instead of the current
keyspace.

[[alterTypeStmt]]

#### ALTER TYPE

_Syntax:_

```bnf
::= ALTER TYPE (IF EXISTS)?

::= ADD (IF NOT EXISTS)?
| RENAME (IF EXISTS)? TO ( AND TO )*
```

_Sample:_

```sql
ALTER TYPE address ADD country text
ALTER TYPE address RENAME zip TO zipcode AND street_name TO street
```

The `ALTER TYPE` statement is used to manipulate type definitions. It
allows for adding new fields, renaming existing fields, or changing the
type of existing fields. If the type does not exist, the statement will return an error, unless `IF EXISTS` is used in which case the operation is a no-op.

[[dropTypeStmt]]

#### DROP TYPE

_Syntax:_

::= DROP TYPE ( IF EXISTS )?

The `DROP TYPE` statement results in the immediate, irreversible removal
of a type. Attempting to drop a type that is still in use by another
type or a table will result in an error.

If the type does not exist, an error will be returned unless `IF EXISTS`
is used, in which case the operation is a no-op.

[[createTriggerStmt]]

#### CREATE TRIGGER

_Syntax:_

::= CREATE TRIGGER ( IF NOT EXISTS )? ( )? ON USING

_Sample:_

CREATE TRIGGER myTrigger ON myTable USING
'org.apache.cassandra.triggers.InvertedIndex';

The actual logic that makes up the trigger can be written in any Java
(JVM) language and exists outside the database. You place the trigger
code in a `lib/triggers` subdirectory of the Cassandra installation
directory, it loads during cluster startup, and exists on every node
that participates in a cluster. The trigger defined on a table fires
before a requested DML statement occurs, which ensures the atomicity of
the transaction.

[[dropTriggerStmt]]

#### DROP TRIGGER

_Syntax:_

::= DROP TRIGGER ( IF EXISTS )? ( )? ON

_Sample:_

DROP TRIGGER myTrigger ON myTable;

`DROP TRIGGER` statement removes the registration of a trigger created
using `CREATE TRIGGER`.

[[createFunctionStmt]]

#### CREATE FUNCTION

_Syntax:_

```bnf
::= CREATE ( OR REPLACE )?
FUNCTION ( IF NOT EXISTS )?
( `.' )?
`(' ( `,' )* `)'
( CALLED | RETURNS NULL ) ON NULL INPUT
RETURNS
LANGUAGE
AS
```

_Sample:_

CREATE OR REPLACE FUNCTION somefunction
( somearg int, anotherarg text, complexarg frozen, listarg list )
RETURNS NULL ON NULL INPUT
RETURNS text
LANGUAGE java
AS $$
$$;
CREATE FUNCTION akeyspace.fname IF NOT EXISTS
( someArg int )
CALLED ON NULL INPUT
RETURNS text
LANGUAGE java
AS $$
$$;

`CREATE FUNCTION` creates or replaces a user-defined function.

[[functionSignature]]

##### Function Signature

Signatures are used to distinguish individual functions. The signature
consists of:

. The fully qualified function name - i.e _keyspace_ plus
_function-name_
. The concatenated list of all argument types

Note that keyspace names, function names and argument types are subject
to the default naming conventions and case-sensitivity rules.

`CREATE FUNCTION` with the optional `OR REPLACE` keywords either creates
a function or replaces an existing one with the same signature. A
`CREATE FUNCTION` without `OR REPLACE` fails if a function with the same
signature already exists.

Behavior on invocation with `null` values must be defined for each
function. There are two options:

. `RETURNS NULL ON NULL INPUT` declares that the function will always
return `null` if any of the input arguments is `null`.
. `CALLED ON NULL INPUT` declares that the function will always be
executed.

If the optional `IF NOT EXISTS` keywords are used, the function will
only be created if another function with the same signature does not
exist.

`OR REPLACE` and `IF NOT EXIST` cannot be used together.

Functions belong to a keyspace. If no keyspace is specified in
`<function-name>`, the current keyspace is used (i.e. the keyspace
specified using the link:#useStmt[`USE`] statement). It is not possible
to create a user-defined function in one of the system keyspaces.

See the section on link:#udfs[user-defined functions] for more
information.

[[dropFunctionStmt]]

#### DROP FUNCTION

_Syntax:_

::= DROP FUNCTION ( IF EXISTS )?
( `.' )?
( `(' ( `,' )* `)' )?

_Sample:_

```sql
DROP FUNCTION myfunction;
DROP FUNCTION mykeyspace.afunction;
DROP FUNCTION afunction ( int );
DROP FUNCTION afunction ( text );
```

`DROP FUNCTION` statement removes a function created using
`CREATE FUNCTION`. +
You must specify the argument types (link:#functionSignature[signature]
) of the function to drop if there are multiple functions with the same
name but a different signature (overloaded functions).

`DROP FUNCTION` with the optional `IF EXISTS` keywords drops a function
if it exists.

[[createAggregateStmt]]

#### CREATE AGGREGATE

_Syntax:_

```bnf
::= CREATE ( OR REPLACE )?
AGGREGATE ( IF NOT EXISTS )?
( `.' )?
`(' ( `,' )* `)'
SFUNC
STYPE
( FINALFUNC )?
( INITCOND )?
```

_Sample:_

```sql
CREATE AGGREGATE myaggregate ( val text )
SFUNC myaggregate_state
STYPE text
FINALFUNC myaggregate_final
INITCOND 'foo';
```

See the section on link:#udas[user-defined aggregates] for a complete
example.

`CREATE AGGREGATE` creates or replaces a user-defined aggregate.

`CREATE AGGREGATE` with the optional `OR REPLACE` keywords either
creates an aggregate or replaces an existing one with the same
signature. A `CREATE AGGREGATE` without `OR REPLACE` fails if an
aggregate with the same signature already exists.

`CREATE AGGREGATE` with the optional `IF NOT EXISTS` keywords either
creates an aggregate if it does not already exist.

`OR REPLACE` and `IF NOT EXIST` cannot be used together.

Aggregates belong to a keyspace. If no keyspace is specified in
`<aggregate-name>`, the current keyspace is used (i.e. the keyspace
specified using the link:#useStmt[`USE`] statement). It is not possible
to create a user-defined aggregate in one of the system keyspaces.

Signatures for user-defined aggregates follow the
link:#functionSignature[same rules] as for user-defined functions.

`STYPE` defines the type of the state value and must be specified.

The optional `INITCOND` defines the initial state value for the
aggregate. It defaults to `null`. A non-`null` `INITCOND` must be
specified for state functions that are declared with
`RETURNS NULL ON NULL INPUT`.

`SFUNC` references an existing function to be used as the state
modifying function. The type of first argument of the state function
must match `STYPE`. The remaining argument types of the state function
must match the argument types of the aggregate function. State is not
updated for state functions declared with `RETURNS NULL ON NULL INPUT`
and called with `null`.

The optional `FINALFUNC` is called just before the aggregate result is
returned. It must take only one argument with type `STYPE`. The return
type of the `FINALFUNC` may be a different type. A final function
declared with `RETURNS NULL ON NULL INPUT` means that the aggregate’s
return value will be `null`, if the last state is `null`.

If no `FINALFUNC` is defined, the overall return type of the aggregate
function is `STYPE`. If a `FINALFUNC` is defined, it is the return type
of that function.

See the section on link:#udas[user-defined aggregates] for more
information.

[[dropAggregateStmt]]

#### DROP AGGREGATE

_Syntax:_

```bnf
::= DROP AGGREGATE ( IF EXISTS )?
( `.' )?
( `(' ( `,' )* `)' )?
```

_Sample:_

```sql
DROP AGGREGATE myAggregate;
DROP AGGREGATE myKeyspace.anAggregate;
DROP AGGREGATE someAggregate ( int );
DROP AGGREGATE someAggregate ( text );
```

The `DROP AGGREGATE` statement removes an aggregate created using
`CREATE AGGREGATE`. You must specify the argument types of the aggregate
to drop if there are multiple aggregates with the same name but a
different signature (overloaded aggregates).

`DROP AGGREGATE` with the optional `IF EXISTS` keywords drops an
aggregate if it exists, and does nothing if a function with the
signature does not exist.

Signatures for user-defined aggregates follow the
link:#functionSignature[same rules] as for user-defined functions.

[[dataManipulation]]
