<!-- Part 6 of 8 of cassandra/developing/cql/cql_singlefile.md (split because the page is big). -->

### Data Types

CQL supports a rich set of data types for columns defined in a table,
including collection types. On top of those native +
and collection types, users can also provide custom types (through a
JAVA class extending `AbstractType` loadable by +
Cassandra). The syntax of types is thus:

```bnf
::=
|
|
| // Used for custom types. The fully-qualified name of a JAVA class

::= ascii
| bigint
| blob
| boolean
| counter
| date
| decimal
| double
| float
| inet
| int
| smallint
| text
| time
| timestamp
| timeuuid
| tinyint
| uuid
| varchar
| varint

::= list `<' `>'
| set `<' `>'
| map `<' `,' `>'
::= tuple `<' (`,' )* `>'
```

Note that the native types are keywords and as such are
case-insensitive. They are however not reserved ones.

The following table gives additional informations on the native data
types, and on which kind of link:#constants[constants] each type
supports:

|===
|type |constants supported |description
|`ascii` |strings |ASCII character string

|`bigint` |integers |64-bit signed long

|`blob` |blobs |Arbitrary bytes (no validation)

|`boolean` |booleans |true or false

|`counter` |integers |Counter column (64-bit signed value). See
link:#counters[Counters] for details

|`date` |integers, strings |A date (with no corresponding time value).
See link:#usingdates[Working with dates] below for more information.

|`decimal` |integers, floats |Variable-precision decimal

|`double` |integers |64-bit IEEE-754 floating point

|`float` |integers, floats |32-bit IEEE-754 floating point

|`inet` |strings |An IP address. It can be either 4 bytes long (IPv4) or
16 bytes long (IPv6). There is no `inet` constant, IP address should be
inputed as strings

|`int` |integers |32-bit signed int

|`smallint` |integers |16-bit signed int

|`text` |strings |UTF8 encoded string

|`time` |integers, strings |A time with nanosecond precision. See
link:#usingtime[Working with time] below for more information.

|`timestamp` |integers, strings |A timestamp. Strings constant are allow
to input timestamps as dates, see link:#usingtimestamps[Working with
timestamps] below for more information.

|`timeuuid` |uuids |Type 1 UUID. This is generally used as a
``conflict-free'' timestamp. Also see the link:#timeuuidFun[functions on
Timeuuid]

|`tinyint` |integers |8-bit signed int

|`uuid` |uuids |Type 1 or type 4 UUID

|`varchar` |strings |UTF8 encoded string

|`varint` |integers |Arbitrary-precision integer
|===

For more information on how to use the collection types, see the
link:#collections[Working with collections] section below.

[[usingtimestamps]]

#### Working with timestamps

Values of the `timestamp` type are encoded as 64-bit signed integers
representing a number of milliseconds since the standard base time known
as ``the epoch'': January 1 1970 at 00:00:00 GMT.

Timestamp can be input in CQL as simple long integers, giving the number
of milliseconds since the epoch, as defined above.

They can also be input as string literals in any of the following ISO
8601 formats, each representing the time and date Mar 2, 2011, at
04:05:00 AM, GMT.:

* `2011-02-03 04:05+0000`
* `2011-02-03 04:05:00+0000`
* `2011-02-03 04:05:00.000+0000`
* `2011-02-03T04:05+0000`
* `2011-02-03T04:05:00+0000`
* `2011-02-03T04:05:00.000+0000`

The `0000` above is an RFC 822 4-digit time zone specification; `0000`
refers to GMT. US Pacific Standard Time is `-0800`. The time zone may be
omitted if desired— the date will be interpreted as being in the time
zone under which the coordinating Cassandra node is configured.

* `2011-02-03 04:05`
* `2011-02-03 04:05:00`
* `2011-02-03 04:05:00.000`
* `2011-02-03T04:05`
* `2011-02-03T04:05:00`
* `2011-02-03T04:05:00.000`

There are clear difficulties inherent in relying on the time zone
configuration being as expected, though, so it is recommended that the
time zone always be specified for timestamps when feasible.

The time of day may also be omitted, if the date is the only piece that
matters:

* `2011-02-03`
* `2011-02-03+0000`

In that case, the time of day will default to 00:00:00, in the specified
or default time zone.

[[usingdates]]

#### Working with dates

Values of the `date` type are encoded as 32-bit unsigned integers
representing a number of days with ``the epoch'' at the center of the
range (2^31). Epoch is January 1st, 1970

A date can be input in CQL as an unsigned integer as defined above.

They can also be input as string literals in the following format:

* `2014-01-01`

[[usingtime]]

#### Working with time

Values of the `time` type are encoded as 64-bit signed integers
representing the number of nanoseconds since midnight.

A time can be input in CQL as simple long integers, giving the number of
nanoseconds since midnight.

They can also be input as string literals in any of the following
formats:

* `08:12:54`
* `08:12:54.123`
* `08:12:54.123456`
* `08:12:54.123456789`

#### Counters

The `counter` type is used to define _counter columns_. A counter column
is a column whose value is a 64-bit signed integer and on which 2
operations are supported: incrementation and decrementation (see
link:#updateStmt[`UPDATE`] for syntax). Note the value of a counter
cannot be set. A counter doesn’t exist until first
incremented/decremented, and the first incrementation/decrementation is
made as if the previous value was 0. Deletion of counter columns is
supported but have some limitations (see the
[Cassandra Wiki](http://wiki.apache.org/cassandra/Counters) for more
information).

The use of the counter type is limited in the following way:

* It cannot be used for column that is part of the `PRIMARY KEY` of a
table.
* A table that contains a counter can only contain counters. In other
words, either all the columns of a table outside the `PRIMARY KEY` have
the counter type, or none of them have it.

[[collections]]

#### Working with collections

##### Noteworthy characteristics

Collections are meant for storing/denormalizing relatively small amount
of data. They work well for things like ``the phone numbers of a given
user'', ``labels applied to an email'', etc. But when items are expected
to grow unbounded (``all the messages sent by a given user'', ``events
registered by a sensor'', …), then collections are not appropriate
anymore and a specific table (with clustering columns) should be used.
Concretely, collections have the following limitations:

* Collections are always read in their entirety (and reading one is not
paged internally).
* Collections cannot have more than 65535 elements. More precisely,
while it may be possible to insert more than 65535 elements, it is not
possible to read more than the 65535 first elements (see
[CASSANDRA-5428](https://issues.apache.org/jira/browse/CASSANDRA-5428) for
details).
* While insertion operations on sets and maps never incur a
read-before-write internally, some operations on lists do (see the
section on lists below for details). It is thus advised to prefer sets
over lists when possible.

Please note that while some of those limitations may or may not be
loosen in the future, the general rule that collections are for
denormalizing small amount of data is meant to stay.

[[map]]

##### Maps

A `map` is a link:#types[typed] set of key-value pairs, where keys are
unique. Furthermore, note that the map are internally sorted by their
keys and will thus always be returned in that order. To create a column
of type `map`, use the `map` keyword suffixed with comma-separated key
and value types, enclosed in angle brackets. For example:

```sql
CREATE TABLE users (
id text PRIMARY KEY,
given text,
surname text,
favs map<text, text>  -- A map of text keys, and text values
)
```

Writing `map` data is accomplished with a JSON-inspired syntax. To write
a record using `INSERT`, specify the entire map as a JSON-style
associative array. _Note: This form will always replace the entire map._

```sql
// Inserting (or Updating)
INSERT INTO users (id, given, surname, favs)
VALUES ('jsmith', 'John', 'Smith', { 'fruit' : 'apple', 'band' :
'Beatles' })
```

Adding or updating key-values of a (potentially) existing map can be
accomplished either by subscripting the map column in an `UPDATE`
statement or by adding a new map literal:

```sql
// Updating (or inserting)
UPDATE users SET favs['author'] = 'Ed Poe' WHERE id = 'jsmith'
UPDATE users SET favs = favs + {'`movie' : 'Cassablanca' } WHERE id =
'jsmith'
```

Note that TTLs are allowed for both `INSERT` and `UPDATE`, but in both
case the TTL set only apply to the newly inserted/updated _values_. In
other words,

UPDATE users USING TTL 10 SET favs['color'] = 'green' WHERE id =
'jsmith'

will only apply the TTL to the `{ 'color' : 'green' }` record, the rest
of the map remaining unaffected.

Deleting a map record is done with:

DELETE favs['author'] FROM users WHERE id = 'jsmith'

[[set]]

##### Sets

A `set` is a link:#types[typed] collection of unique values. Sets are
ordered by their values. To create a column of type `set`, use the `set`
keyword suffixed with the value type enclosed in angle brackets. For
example:

```sql
CREATE TABLE images (
name text PRIMARY KEY,
owner text,
date timestamp,
tags set
);
```

Writing a `set` is accomplished by comma separating the set values, and
enclosing them in curly braces. _Note: An `INSERT` will always replace
the entire set._

INSERT INTO images (name, owner, date, tags)
VALUES ('cat.jpg', 'jsmith', 'now', { 'kitten', 'cat', 'pet' });

Adding and removing values of a set can be accomplished with an `UPDATE`
by adding/removing new set values to an existing `set` column.

UPDATE images SET tags = tags + { 'cute', 'cuddly' } WHERE name =
'cat.jpg';
UPDATE images SET tags = tags - { 'lame' } WHERE name = 'cat.jpg';

As with link:#map[maps], TTLs if used only apply to the newly
inserted/updated _values_.

[[list]]

##### Lists

A `list` is a link:#types[typed] collection of non-unique values where
elements are ordered by there position in the list. To create a column
of type `list`, use the `list` keyword suffixed with the value type
enclosed in angle brackets. For example:

```sql
CREATE TABLE plays (
id text PRIMARY KEY,
game text,
players int,
scores list
)
```

Do note that as explained below, lists have some limitations and
performance considerations to take into account, and it is advised to
prefer link:#set[sets] over lists when this is possible.

Writing `list` data is accomplished with a JSON-style syntax. To write a
record using `INSERT`, specify the entire list as a JSON array. _Note:
An `INSERT` will always replace the entire list._

INSERT INTO plays (id, game, players, scores)
VALUES ('123-afde', 'quake', 3, [17, 4, 2]);

Adding (appending or prepending) values to a list can be accomplished by
adding a new JSON-style array to an existing `list` column.

```sql
UPDATE plays SET players = 5, scores = scores + [ 14, 21 ] WHERE id =
'123-afde';
UPDATE plays SET players = 5, scores = [ 12 ] + scores WHERE id =
'123-afde';
```

It should be noted that append and prepend are not idempotent
operations. This means that if during an append or a prepend the
operation timeout, it is not always safe to retry the operation (as this
could result in the record appended or prepended twice).

Lists also provides the following operation: setting an element by its
position in the list, removing an element by its position in the list
and remove all the occurrence of a given value in the list. _However,
and contrarily to all the other collection operations, these three
operations induce an internal read before the update, and will thus
typically have slower performance characteristics_. Those operations
have the following syntax:

```sql
UPDATE plays SET scores[1] = 7 WHERE id = '123-afde'; // sets the 2nd
element of scores to 7 (raises an error is scores has less than 2
elements)

DELETE scores[1] FROM plays WHERE id = '123-afde'; // deletes the 2nd
element of scores (raises an error is scores has less than 2 elements)

UPDATE plays SET scores = scores - [ 12, 21 ] WHERE id = '123-afde'; // removes all occurrences of 12 and 21 from scores
```

As with link:#map[maps], TTLs if used only apply to the newly
inserted/updated _values_.

[[vectors]]

#### Working with vectors

Vectors are fixed-size sequences of non-null values of a certain data type. They use the same literals as lists.

You can define, insert and update a vector with:

```sql
CREATE TABLE plays (
    id text PRIMARY KEY,
    game text,
    players int,
    scores vector<int, 3> // A vector of 3 integers
)

INSERT INTO plays (id, game, players, scores)
           VALUES ('123-afde', 'quake', 3, [17, 4, 2]);

// Replace the existing vector entirely
UPDATE plays SET scores = [ 3, 9, 4] WHERE id = '123-afde';

```

Note that it isn't possible to change the individual values of a vector, and it isn't possible to select individual
elements of a vector.


### Functions

CQL3 distinguishes between built-in functions (so called `native
functions') and link:#udfs[user-defined functions]. CQL3 includes
several native functions, described below:

[[castFun]]

#### Cast

The `cast` function can be used to converts one native datatype to
another.

The following table describes the conversions supported by the `cast`
function. Cassandra will silently ignore any cast converting a datatype
into its own datatype.

|===
|from |to
|`ascii` |`text`, `varchar`

|`bigint` |`tinyint`, `smallint`, `int`, `float`, `double`, `decimal`,
`varint`, `text`, `varchar`

|`boolean` |`text`, `varchar`

|`counter` |`tinyint`, `smallint`, `int`, `bigint`, `float`, `double`,
`decimal`, `varint`, `text`, `varchar`

|`date` |`timestamp`

|`decimal` |`tinyint`, `smallint`, `int`, `bigint`, `float`, `double`,
`varint`, `text`, `varchar`

|`double` |`tinyint`, `smallint`, `int`, `bigint`, `float`, `decimal`,
`varint`, `text`, `varchar`

|`float` |`tinyint`, `smallint`, `int`, `bigint`, `double`, `decimal`,
`varint`, `text`, `varchar`

|`inet` |`text`, `varchar`

|`int` |`tinyint`, `smallint`, `bigint`, `float`, `double`, `decimal`,
`varint`, `text`, `varchar`

|`smallint` |`tinyint`, `int`, `bigint`, `float`, `double`, `decimal`,
`varint`, `text`, `varchar`

|`time` |`text`, `varchar`

|`timestamp` |`date`, `text`, `varchar`

|`timeuuid` |`timestamp`, `date`, `text`, `varchar`

|`tinyint` |`tinyint`, `smallint`, `int`, `bigint`, `float`, `double`,
`decimal`, `varint`, `text`, `varchar`

|`uuid` |`text`, `varchar`

|`varint` |`tinyint`, `smallint`, `int`, `bigint`, `float`, `double`,
`decimal`, `text`, `varchar`
|===

The conversions rely strictly on Java’s semantics. For example, the
double value 1 will be converted to the text value `1.0'.

SELECT avg(cast(count as double)) FROM myTable

[[tokenFun]]

#### Token

The `token` function allows to compute the token for a given partition
key. The exact signature of the token function depends on the table
concerned and of the partitioner used by the cluster.

The type of the arguments of the `token` depend on the type of the
partition key columns. The return type depend on the partitioner in use:

* For Murmur3Partitioner, the return type is `bigint`.
* For RandomPartitioner, the return type is `varint`.
* For ByteOrderedPartitioner, the return type is `blob`.

For instance, in a cluster using the default Murmur3Partitioner, if a
table is defined by

```sql
CREATE TABLE users (
userid text PRIMARY KEY,
username text,
...
)
```

then the `token` function will take a single argument of type `text` (in
that case, the partition key is `userid` (there is no clustering columns
so the partition key is the same than the primary key)), and the return
type will be `bigint`.

[[uuidFun]]

#### Uuid

The `uuid` function takes no parameters and generates a random type 4
uuid suitable for use in INSERT or SET statements.

[[timeuuidFun]]

#### Timeuuid functions

##### `now`

The `now` function takes no arguments and generates, on the coordinator
node, a new unique timeuuid (at the time where the statement using it is
executed). Note that this method is useful for insertion but is largely
non-sensical in `WHERE` clauses. For instance, a query of the form

SELECT * FROM myTable WHERE t = now()

will never return any result by design, since the value returned by
`now()` is guaranteed to be unique.

##### `min_timeuuid` and `max_timeuuid`

The `min_timeuuid` (resp. `max_timeuuid`) function takes a `timestamp`
value `t` (which can be link:#usingtimestamps[either a timestamp or a
date string] ) and return a _fake_ `timeuuid` corresponding to the
_smallest_ (resp. _biggest_) possible `timeuuid` having for timestamp
`t`. So for instance:

SELECT * FROM myTable WHERE t > max_timeuuid('2013-01-01 00:05+0000') AND
t < min_timeuuid('2013-02-02 10:00+0000')

will select all rows where the `timeuuid` column `t` is strictly older
than `2013-01-01 00:05+0000' but strictly younger than `2013-02-02
10:00+0000'. Please note that
`t >= max_timeuuid('2013-01-01 00:05+0000')` would still _not_ select a
`timeuuid` generated exactly at `2013-01-01 00:05+0000' and is
essentially equivalent to `t > max_timeuuid('2013-01-01 00:05+0000')`.

_Warning_: We called the values generated by `min_timeuuid` and
`max_timeuuid` _fake_ UUID because they do no respect the Time-Based UUID
generation process specified by the
[RFC 4122](http://www.ietf.org/rfc/rfc4122.txt). In particular, the value
returned by these 2 methods will not be unique. This means you should
only use those methods for querying (as in the example above). Inserting
the result of those methods is almost certainly _a bad idea_.

[[timeFun]]

#### Time conversion functions

A number of functions are provided to ``convert'' a `timeuuid`, a
`timestamp` or a `date` into another `native` type.

|===
|function name |input type |description
|`to_date` |`timeuuid` |Converts the `timeuuid` argument into a `date`
type

|`to_date` |`timestamp` |Converts the `timestamp` argument into a `date`
type

|`to_timestamp` |`timeuuid` |Converts the `timeuuid` argument into a
`timestamp` type

|`to_timestamp` |`date` |Converts the `date` argument into a `timestamp`
type

|`to_unix_timestamp` |`timeuuid` |Converts the `timeuuid` argument into a
`bigInt` raw value

|`to_unix_timestamp` |`timestamp` |Converts the `timestamp` argument into
a `bigInt` raw value

|`to_unix_timestamp` |`date` |Converts the `date` argument into a `bigInt`
raw value
|===

[[blobFun]]

#### Blob conversion functions

A number of functions are provided to ``convert'' the native types into
binary data (`blob`). For every `<native-type>` `type` supported by CQL3
(a notable exceptions is `blob`, for obvious reasons), the function
`type_as_blob` takes a argument of type `type` and return it as a `blob`.
Conversely, the function `blob_as_type` takes a 64-bit `blob` argument and
convert it to a `bigint` value. And so for instance, `bigint_as_blob(3)`
is `0x0000000000000003` and `blob_as_bigint(0x0000000000000003)` is `3`.
