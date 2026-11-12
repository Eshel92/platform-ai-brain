<!-- Part 7 of 8 of cassandra/developing/cql/cql_singlefile.md (split because the page is big). -->

### Aggregates

Aggregate functions work on a set of rows. They receive values for each
row and returns one value for the whole set. +
If `normal` columns, `scalar functions`, `UDT` fields, `writetime`, `maxwritetime`
or `ttl` are selected together with aggregate functions, the values
returned for them will be the ones of the first row matching the query.

CQL3 distinguishes between built-in aggregates (so called `native
aggregates') and link:#udas[user-defined aggregates]. CQL3 includes
several native aggregates, described below:

[[countFct]]

#### Count

The `count` function can be used to count the rows returned by a query.
Example:

```sql
SELECT COUNT (*) FROM plays;
SELECT COUNT (1) FROM plays;
```

It also can be used to count the non null value of a given column.
Example:

SELECT COUNT (scores) FROM plays;

[[maxMinFcts]]

#### Max and Min

The `max` and `min` functions can be used to compute the maximum and the
minimum value returned by a query for a given column.

SELECT MIN (players), MAX (players) FROM plays WHERE game = 'quake';

[[sumFct]]

#### Sum

The `sum` function can be used to sum up all the values returned by a
query for a given column.

SELECT SUM (players) FROM plays;

[[avgFct]]

#### Avg

The `avg` function can be used to compute the average of all the values
returned by a query for a given column.

SELECT AVG (players) FROM plays;

[[udfs]]


### User-Defined Functions

User-defined functions allow execution of user-provided code in
Cassandra. By default, Cassandra supports defining functions in _Java_
and _JavaScript_. Support for other JSR 223 compliant scripting
languages (such as Python, Ruby, and Scala) has been removed in 3.0.11.

UDFs are part of the Cassandra schema. As such, they are automatically
propagated to all nodes in the cluster.

UDFs can be _overloaded_ - i.e. multiple UDFs with different argument
types but the same function name. Example:

```sql
CREATE FUNCTION sample ( arg int ) ...;
CREATE FUNCTION sample ( arg text ) ...;
```

User-defined functions are susceptible to all of the normal problems
with the chosen programming language. Accordingly, implementations
should be safe against null pointer exceptions, illegal arguments, or
any other potential source of exceptions. An exception during function
execution will result in the entire statement failing.

It is valid to use _complex_ types like collections, tuple types and
user-defined types as argument and return types. Tuple types and
user-defined types are handled by the conversion functions of the
DataStax Java Driver. Please see the documentation of the Java Driver
for details on handling tuple types and user-defined types.

Arguments for functions can be literals or terms. Prepared statement
placeholders can be used, too.

Note that you can use the double-quoted string syntax to enclose the UDF
source code. For example:

```sql
CREATE FUNCTION some_function ( arg int )
RETURNS NULL ON NULL INPUT
RETURNS int
LANGUAGE java
AS $$ return arg; $$;

SELECT some_function(column) FROM atable ...;
UPDATE atable SET col = some_function(?) ...;
```

```sql
CREATE TYPE custom_type (txt text, i int);
CREATE FUNCTION fct_using_udt ( udtarg frozen )
RETURNS NULL ON NULL INPUT
RETURNS text
LANGUAGE java
AS $$ return udtarg.getString("txt"); $$;
```

User-defined functions can be used in link:#selectStmt[`SELECT`],
link:#insertStmt[`INSERT`] and link:#updateStmt[`UPDATE`] statements.

The implicitly available `udfContext` field (or binding for script UDFs)
provides the neccessary functionality to create new UDT and tuple
values.

```sql
CREATE TYPE custom_type (txt text, i int);
CREATE FUNCTION fct_using_udt ( somearg int )
RETURNS NULL ON NULL INPUT
RETURNS custom_type
LANGUAGE java
AS $$
UDTValue udt = udfContext.newReturnUDTValue();
udt.setString("txt", "some string");
udt.setInt("i", 42);
return udt;
$$;
```

The definition of the `UDFContext` interface can be found in the Apache
Cassandra source code for
`org.apache.cassandra.cql3.functions.UDFContext`.

```java
public interface UDFContext
{
UDTValue newArgUDTValue(String argName);
UDTValue newArgUDTValue(int argNum);
UDTValue newReturnUDTValue();
UDTValue newUDTValue(String udtName);
TupleValue newArgTupleValue(String argName);
TupleValue newArgTupleValue(int argNum);
TupleValue newReturnTupleValue();
TupleValue newTupleValue(String cqlDefinition);
}
```

Java UDFs already have some imports for common interfaces and classes
defined. These imports are: +
Please note, that these convenience imports are not available for script
UDFs.

```java
import java.nio.ByteBuffer;
import java.util.List;
import java.util.Map;
import java.util.Set;
import org.apache.cassandra.cql3.functions.UDFContext;
import com.datastax.driver.core.TypeCodec;
import com.datastax.driver.core.TupleValue;
import com.datastax.driver.core.UDTValue;
```

See link:#createFunctionStmt[`CREATE FUNCTION`] and
link:#dropFunctionStmt[`DROP FUNCTION`].

[[udas]]


### User-Defined Aggregates

User-defined aggregates allow creation of custom aggregate functions
using link:#udfs[UDFs]. Common examples of aggregate functions are
_count_, _min_, and _max_.

Each aggregate requires an _initial state_ (`INITCOND`, which defaults
to `null`) of type `STYPE`. The first argument of the state function
must have type `STYPE`. The remaining arguments of the state function
must match the types of the user-defined aggregate arguments. The state
function is called once for each row, and the value returned by the
state function becomes the new state. After all rows are processed, the
optional `FINALFUNC` is executed with last state value as its argument.

`STYPE` is mandatory in order to be able to distinguish possibly
overloaded versions of the state and/or final function (since the
overload can appear after creation of the aggregate).

User-defined aggregates can be used in link:#selectStmt[`SELECT`]
statement.

A complete working example for user-defined aggregates (assuming that a
keyspace has been selected using the link:#useStmt[`USE`] statement):

```sql
CREATE OR REPLACE FUNCTION averageState ( state tuple<int,bigint>, val
int )
CALLED ON NULL INPUT
RETURNS tuple<int,bigint>
LANGUAGE java
AS ’
if (val != null) {
state.setInt(0, state.getInt(0)+1);
state.setLong(1, state.getLong(1)+val.intValue());
}
return state;
’;

CREATE OR REPLACE FUNCTION averageFinal ( state tuple<int,bigint> )
CALLED ON NULL INPUT
RETURNS double
LANGUAGE java
AS ’
double r = 0;
if (state.getInt(0) == 0) return null;
r = state.getLong(1);
r /= state.getInt(0);
return Double.valueOf(r);
’;

CREATE OR REPLACE AGGREGATE average ( int )
SFUNC averageState
STYPE tuple<int,bigint>
FINALFUNC averageFinal
INITCOND (0, 0);

CREATE TABLE atable (
pk int PRIMARY KEY,
val int);
INSERT INTO atable (pk, val) VALUES (1,1);
INSERT INTO atable (pk, val) VALUES (2,2);
INSERT INTO atable (pk, val) VALUES (3,3);
INSERT INTO atable (pk, val) VALUES (4,4);
SELECT average(val) FROM atable;
```

See link:#createAggregateStmt[`CREATE AGGREGATE`] and
link:#dropAggregateStmt[`DROP AGGREGATE`].

[[json]]


### JSON Support

Cassandra 2.2 introduces JSON support to link:#selectStmt[`SELECT`] and
link:#insertStmt[`INSERT`] statements. This support does not
fundamentally alter the CQL API (for example, the schema is still
enforced), it simply provides a convenient way to work with JSON
documents.

[[selectJson]]

#### SELECT JSON

With `SELECT` statements, the new `JSON` keyword can be used to return
each row as a single `JSON` encoded map. The remainder of the `SELECT`
statment behavior is the same.

The result map keys are the same as the column names in a normal result
set. For example, a statement like
`SELECT JSON a, ttl(b) FROM ...`
would result in a map with keys `"a"` and `"ttl(b)"`. However, this is
one notable exception: for symmetry with `INSERT JSON` behavior,
case-sensitive column names with upper-case letters will be surrounded
with double quotes. For example, `SELECT JSON myColumn FROM ...`
 would result in a map key `"\"myColumn\""` (note the escaped quotes).

The map values will `JSON`-encoded representations (as described below)
of the result set values.

[[insertJson]]

#### INSERT JSON

With `INSERT` statements, the new `JSON` keyword can be used to enable
inserting a `JSON` encoded map as a single row. The format of the `JSON`
map should generally match that returned by a `SELECT JSON` statement on
the same table. In particular, case-sensitive column names should be
surrounded with double quotes. For example, to insert into a table with
two columns named ``myKey'' and ``value'', you would do the following:

INSERT INTO mytable JSON '{"\"myKey\"": 0, "value": 0}'

Any columns which are omitted from the `JSON` map will be defaulted to
a `NULL` value (which will result in a tombstone being created).

[[jsonEncoding]]

#### JSON Encoding of Cassandra Data Types

Where possible, Cassandra will represent and accept data types in their
native `JSON` representation. Cassandra will also accept string
representations matching the CQL literal format for all single-field
types. For example, floats, ints, UUIDs, and dates can be represented by
CQL literal strings. However, compound types, such as collections,
tuples, and user-defined types must be represented by native `JSON`
collections (maps and lists) or a JSON-encoded string representation of
the collection.

The following table describes the encodings that Cassandra will accept
in `INSERT JSON` values (and `from_json()` arguments) as well as the
format Cassandra will use when returning data for `SELECT JSON`
statements (and `from_json()`):

|===
|type |formats accepted |return format |notes
|`ascii` |string |string |Uses JSON’s `\u` character escape

|`bigint` |integer, string |integer |String must be valid 64 bit integer

|`blob` |string |string |String should be 0x followed by an even number
of hex digits

|`boolean` |boolean, string |boolean |String must be ``true'' or
``false''

|`date` |string |string |Date in format `YYYY-MM-DD`, timezone UTC

|`decimal` |integer, float, string |float |May exceed 32 or 64-bit
IEEE-754 floating point precision in client-side decoder

|`double` |integer, float, string |float |String must be valid integer
or float

|`float` |integer, float, string |float |String must be valid integer or
float

|`inet` |string |string |IPv4 or IPv6 address

|`int` |integer, string |integer |String must be valid 32 bit integer

|`list` |list, string |list |Uses JSON’s native list representation

|`map` |map, string |map |Uses JSON’s native map representation

|`smallint` |integer, string |integer |String must be valid 16 bit
integer

|`set` |list, string |list |Uses JSON’s native list representation

|`text` |string |string |Uses JSON’s `\u` character escape

|`time` |string |string |Time of day in format `HH-MM-SS[.fffffffff]`

|`timestamp` |integer, string |string |A timestamp. Strings constant are
allow to input timestamps as dates, see link:#usingdates[Working with
dates] below for more information. Datestamps with format
`YYYY-MM-DD HH:MM:SS.SSS` are returned.

|`timeuuid` |string |string |Type 1 UUID. See link:#constants[Constants]
for the UUID format

|`tinyint` |integer, string |integer |String must be valid 8 bit integer

|`tuple` |list, string |list |Uses JSON’s native list representation

|`UDT` |map, string |map |Uses JSON’s native map representation with
field names as keys

|`uuid` |string |string |See link:#constants[Constants] for the UUID
format

|`varchar` |string |string |Uses JSON’s `\u` character escape

|`varint` |integer, string |integer |Variable length; may overflow 32 or
64 bit integers in client-side decoder
|===

[[from_json]]

#### The from_json() Function

The `from_json()` function may be used similarly to `INSERT JSON`, but
for a single column value. It may only be used in the `VALUES` clause of
an `INSERT` statement or as one of the column values in an `UPDATE`,
`DELETE`, or `SELECT` statement. For example, it cannot be used in the
selection clause of a `SELECT` statement.

[[to_json]]

#### The to_json() Function

The `to_json()` function may be used similarly to `SELECT JSON`, but for
a single column value. It may only be used in the selection clause of a
`SELECT` statement.

[[appendixA]]


### Appendix A: CQL Keywords

CQL distinguishes between _reserved_ and _non-reserved_ keywords.
Reserved keywords cannot be used as identifier, they are truly reserved
for the language (but one can enclose a reserved keyword by
double-quotes to use it as an identifier). Non-reserved keywords however
only have a specific meaning in certain context but can used as
identifer otherwise. The only _raison d’être_ of these non-reserved
keywords is convenience: some keyword are non-reserved when it was
always easy for the parser to decide whether they were used as keywords
or not.

|===
|Keyword |Reserved?
|`ADD` |yes
|`AGGREGATE` |no
|`ALL` |no
|`ALLOW` |yes
|`ALTER` |yes
|`AND` |yes
|`APPLY` |yes
|`AS` |no
|`ASC` |yes
|`ASCII` |no
|`AUTHORIZE` |yes
|`BATCH` |yes
|`BEGIN` |yes
|`BIGINT` |no
|`BLOB` |no
|`BOOLEAN` |no
|`BY` |yes
|`CALLED` |no
|`CAST` |no
|`CLUSTERING` |no
|`COLUMNFAMILY` |yes
|`COMPACT` |no
|`CONTAINS` |no
|`COUNT` |no
|`COUNTER` |no
|`CREATE` |yes
|`CUSTOM` |no
|`DATE` |no
|`DECIMAL` |no
|`DEFAULT` |yes
|`DELETE` |yes
|`DESC` |yes
|`DESCRIBE` |yes
|`DISTINCT` |no
|`DOUBLE` |no
|`DROP` |yes
|`DURATION` |no
|`ENTRIES` |yes
|`EXECUTE` |yes
|`EXISTS` |no
|`FILTERING` |no
|`FINALFUNC` |no
|`FLOAT` |no
|`FROM` |yes
|`FROZEN` |no
|`FULL` |yes
|`FUNCTION` |no
|`FUNCTIONS` |no
|`GRANT` |yes
|`GROUP` |no
|`IF` |yes
|`IN` |yes
|`INDEX` |yes
|`INET` |no
|`INFINITY` |yes
|`INITCOND` |no
|`INPUT` |no
|`INSERT` |yes
|`INT` |no
|`INTO` |yes
|`IS` |yes
|`JSON` |no
|`KEY` |no
|`KEYS` |no
|`KEYSPACE` |yes
|`KEYSPACES` |no
|`LANGUAGE` |no
|`LIKE` |no
|`LIMIT` |yes
|`LIST` |no
|`LOGIN` |no
|`MAP` |no
|`MASKED` |no
|`MATERIALIZED` |yes
|`MBEAN` |yes
|`MBEANS` |yes
|`MODIFY` |yes
|`NAN` |yes
|`NOLOGIN` |no
|`NORECURSIVE` |yes
|`NOSUPERUSER` |no
|`NOT` |yes
|`NULL` |yes
|`OF` |yes
|`ON` |yes
|`OPTIONS` |no
|`OR` |yes
|`ORDER` |yes
|`PARTITION` |no
|`PASSWORD` |no
|`PER` |no
|`PERMISSION` |no
|`PERMISSIONS` |no
|`PRIMARY` |yes
|`RENAME` |yes
|`REPLACE` |yes
|`RETURNS` |no
|`REVOKE` |yes
|`ROLE` |no
|`ROLES` |no
|`SCHEMA` |yes
|`SELECT` |yes
|`SELECT_MASKED` |no
|`SET` |yes
|`SFUNC` |no
|`SMALLINT` |no
|`STATIC` |no
|`STORAGE` |no
|`STYPE` |no
|`SUPERUSER` |no
|`TABLE` |yes
|`TEXT` |no
|`TIME` |no
|`TIMESTAMP` |no
|`TIMEUUID` |no
|`TINYINT` |no
|`TO` |yes
|`TOKEN` |yes
|`TRIGGER` |no
|`TRUNCATE` |yes
|`TTL` |no
|`TUPLE` |no
|`TYPE` |no
|`UNLOGGED` |yes
|`UNMASK` |no
|`UNSET` |yes
|`UPDATE` |yes
|`USE` |yes
|`USER` |no
|`USERS` |no
|`USING` |yes
|`UUID` |no
|`VALUES` |no
|`VARCHAR` |no
|`VARINT` |no
|`VIEW` |yes
|`WHERE` |yes
|`WITH` |yes
|`WRITETIME` |no
|===

[[appendixB]]


### Appendix B: CQL Reserved Types

The following type names are not currently used by CQL, but are reserved
for potential future use. User-defined types may not use reserved type
names as their name.

|===
|type
|`bitstring`
|`byte`
|`complex`
|`date`
|`enum`
|`interval`
|`macaddr`
|===
