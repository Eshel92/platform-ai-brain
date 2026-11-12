<!-- Part 1 of 8 of cassandra/developing/cql/cql_singlefile.md (split because the page is big). -->

## CQL Syntax

### Preamble

This document describes the Cassandra Query Language (CQL) version 3.
CQL v3 is not backward compatible with CQL v2 and differs from it in
numerous ways. Note that this document describes the last version of the
languages. However, the link:#changes[changes] section provides the diff
between the different versions of CQL v3.

CQL v3 offers a model very close to SQL in the sense that data is put in
_tables_ containing _rows_ of _columns_. For that reason, when used in
this document, these terms (tables, rows and columns) have the same
definition than they have in SQL. But please note that as such, they do
*not* refer to the concept of rows and columns found in the internal
implementation of Cassandra and in the thrift and CQL v2 API.

### Conventions

To aid in specifying the CQL syntax, we will use the following
conventions in this document:

* Language rules will be given in a
[BNF](http://en.wikipedia.org/wiki/Backus%E2%80%93Naur_Form) -like
notation:

::= TERMINAL

* Nonterminal symbols will have `<angle brackets>`.
* As additional shortcut notations to BNF, we’ll use traditional regular
expression’s symbols (`?`, `+` and `*`) to signify that a given symbol
is optional and/or can be repeated. We’ll also allow parentheses to
group symbols and the `[<characters>]` notation to represent any one of
`<characters>`.
* The grammar is provided for documentation purposes and leave some
minor details out. For instance, the last column definition in a
`CREATE TABLE` statement is optional but supported if present even
though the provided grammar in this document suggest it is not
supported.
* Sample code will be provided in a code block:

SELECT sample_usage FROM cql;

* References to keywords or pieces of CQL code in running text will be
shown in a `fixed-width font`.

[[identifiers]]

### Identifiers and keywords

The CQL language uses _identifiers_ (or _names_) to identify tables,
columns and other objects. An identifier is a token matching the regular
expression `[a-zA-Z]``[a-zA-Z0-9_]``*`.

A number of such identifiers, like `SELECT` or `WITH`, are _keywords_.
They have a fixed meaning for the language and most are reserved. The
list of those keywords can be found in link:#appendixA[Appendix A].

Identifiers and (unquoted) keywords are case insensitive. Thus `SELECT`
is the same than `select` or `sElEcT`, and `myId` is the same than
`myid` or `MYID` for instance. A convention often used (in particular by
the samples of this documentation) is to use upper case for keywords and
lower case for other identifiers.

There is a second kind of identifiers called _quoted identifiers_
defined by enclosing an arbitrary sequence of characters in
double-quotes(`"`). Quoted identifiers are never keywords. Thus
`"select"` is not a reserved keyword and can be used to refer to a
column, while `select` would raise a parse error. Also, contrarily to
unquoted identifiers and keywords, quoted identifiers are case sensitive
(`"My Quoted Id"` is _different_ from `"my quoted id"`). A fully
lowercase quoted identifier that matches `[a-zA-Z]``[a-zA-Z0-9_]``*` is
equivalent to the unquoted identifier obtained by removing the
double-quote (so `"myid"` is equivalent to `myid` and to `myId` but
different from `"myId"`). Inside a quoted identifier, the double-quote
character can be repeated to escape it, so `"foo "" bar"` is a valid
identifier.

*Warning*: _quoted identifiers_ allows to declare columns with arbitrary
names, and those can sometime clash with specific names used by the
server. For instance, when using conditional update, the server will
respond with a result-set containing a special result named
`"[applied]"`. If you’ve declared a column with such a name, this could
potentially confuse some tools and should be avoided. In general,
unquoted identifiers should be preferred but if you use quoted
identifiers, it is strongly advised to avoid any name enclosed by
squared brackets (like `"[applied]"`) and any name that looks like a
function call (like `"f(x)"`).

### Constants

CQL defines the following kind of _constants_: strings, integers,
floats, booleans, uuids and blobs:

* A string constant is an arbitrary sequence of characters characters
enclosed by single-quote(`'`). One can include a single-quote in a
string by repeating it, e.g. `'It''s raining today'`. Those are not to
be confused with quoted identifiers that use double-quotes.
* An integer constant is defined by `'-'?[0-9]+`.
* A float constant is defined by
`'-'?[0-9]('.'[0-9]*)?([eE][-]?[0-9+])?`. On top of that, `NaN` and
`Infinity` are also float constants.
* A boolean constant is either `true` or `false` up to
case-insensitivity (i.e. `True` is a valid boolean constant).
* A [UUID](http://en.wikipedia.org/wiki/Universally_unique_identifier)
constant is defined by `hex{8}-hex{4}-hex{4}-hex{4}-hex{12}` where `hex`
is an hexadecimal character, e.g. `[0-9a-fA-F]` and `{4}` is the number
of such characters.
* A blob constant is an hexadecimal number defined by `0[xX](hex)+`
where `hex` is an hexadecimal character, e.g. `[0-9a-fA-F]`.

For how these constants are typed, see the link:#types[data types
section].


## Terms

CQL has the notion of a _term_, which denotes the kind of values that
CQL support. Terms are defined by:

```bnf
term::= constant | literal | function_call | arithmetic_operation | type_hint | bind_marker
literal::= collection_literal | vector_literal | udt_literal | tuple_literal
function_call::= identifier '(' [ term (',' term)* ] ')'
arithmetic_operation::= '-' term | term ('+' | '-' | '*' | '/' | '%') term
type_hint::= '(' cql_type ')' term
bind_marker::= '?' | ':' identifier

```

A term is thus one of:

* A constant
* A literal for either a collection, a vector,
a user-defined type or a tuple
* A function call, either a native function
or a user-defined function
* An arithmetic operation between terms
* A type hint
* A bind marker, which denotes a variable to be bound at execution time.
See the section on `prepared-statements` for details. A bind marker can
be either anonymous (`?`) or named (`:some_name`). The latter form
provides a more convenient way to refer to the variable for binding it
and should generally be preferred.

### Comments

A comment in CQL is a line beginning by either double dashes (`--`) or
double slash (`//`).

Multi-line comments are also supported through enclosure within `/*` and
`*/` (but nesting is not supported).

```sql
-- This is a comment
// This is a comment too
/* This is
a multi-line comment */
```

### Statements

CQL consists of statements. As in SQL, these statements can be divided
in 3 categories:

* Data definition statements, that allow to set and change the way data
is stored.
* Data manipulation statements, that allow to change data
* Queries, to look up data

All statements end with a semicolon (`;`) but that semicolon can be
omitted when dealing with a single statement. The supported statements
are described in the following sections. When describing the grammar of
said statements, we will reuse the non-terminal symbols defined below:

```bnf
::= any quoted or unquoted identifier, excluding reserved keywords
::= ( `.')?

::= a string constant
::= an integer constant
::= a float constant
::= |
::= a uuid constant
::= a boolean constant
::= a blob constant

::=
|
|
|
|
::= `?'
| `:'
::=
|
|
| `(' ( (`,' )*)? `)'

::=
|
|
::= `\{' ( `:' ( `,' `:' )* )? `}'
::= `\{' ( ( `,' )* )? `}'
::= `[' ( ( `,' )* )? `]'

::=

::= (AND )*
::= `=' ( | | )
```

Please note that not every possible productions of the grammar above
will be valid in practice. Most notably, `<variable>` and nested
`<collection-literal>` are currently not allowed inside
`<collection-literal>`.

A `<variable>` can be either anonymous (a question mark (`?`)) or named
(an identifier preceded by `:`). Both declare a bind variables for
link:#preparedStatement[prepared statements]. The only difference
between an anymous and a named variable is that a named one will be
easier to refer to (how exactly depends on the client driver used).

The `<properties>` production is use by statement that create and alter
keyspaces and tables. Each `<property>` is either a _simple_ one, in
which case it just has a value, or a _map_ one, in which case it’s value
is a map grouping sub-options. The following will refer to one or the
other as the _kind_ (_simple_ or _map_) of the property.

A `<tablename>` will be used to identify a table. This is an identifier
representing the table name that can be preceded by a keyspace name. The
keyspace name, if provided, allow to identify a table in another
keyspace than the currently active one (the currently active keyspace is
set through the `USE` statement).

For supported `<function>`, see the section on
link:#functions[functions].

Strings can be either enclosed with single quotes or two dollar
characters. The second syntax has been introduced to allow strings that
contain single quotes. Typical candidates for such strings are source
code fragments for user-defined functions.

_Sample:_

```text
'some string value'
$$A King's ransom$$
```

$$double-dollar string can contain single ’ quotes$$

[[preparedStatement]]

### Prepared Statement

CQL supports _prepared statements_. Prepared statement is an
optimization that allows to parse a query only once but execute it
multiple times with different concrete values.

In a statement, each time a column value is expected (in the data
manipulation and query statements), a `<variable>` (see above) can be
used instead. A statement with bind variables must then be _prepared_.
Once it has been prepared, it can executed by providing concrete values
for the bind variables. The exact procedure to prepare a statement and
execute a prepared statement depends on the CQL driver used and is
beyond the scope of this document.

In addition to providing column values, bind markers may be used to
provide values for `LIMIT`, `TIMESTAMP`, and `TTL` clauses. If anonymous
bind markers are used, the names for the query parameters will be
`[limit]`, `[timestamp]`, and `[ttl]`, respectively.

##### Prepared Statement Caching

Prepared Statements are cached by cassandra in-memory using a
[Caffeine](https://github.com/ben-manes/caffeine)-managed cache which
can be configured using
`prepared_statements_cache_size`.
The cache is also persisted to the `system.prepared_statements` table
so it can be preloaded into memory on startup.

To ensure optimal performance, it's important to use a bind `<variable>`
for *all non-constant values* in your CQL statements. If you include
literal values directly in the query instead, each variation will be
treated as a unique statement that must be prepared and cached
separately. This will soon overflow the prepared statement cache,
which is small by design.

When the cache reaches its maximum size, older or less frequently
used statements are
[evicted](https://github.com/ben-manes/caffeine/wiki/Eviction),
leading to additional overhead as previously prepared statements must
be re-prepared.

[[dataDefinition]]


## Data Definition

[[createKeyspaceStmt]]


### CREATE KEYSPACE

_Syntax:_

::= CREATE KEYSPACE (IF NOT EXISTS)? WITH

_Sample:_

```sql
CREATE KEYSPACE Excelsior
WITH replication = {'class': 'SimpleStrategy', 'replication_factor' :
3};

CREATE KEYSPACE Excalibur
WITH replication = {'class': 'NetworkTopologyStrategy', 'DC1' : 1,
'DC2' : 3}
AND durable_writes = false;
```

The `CREATE KEYSPACE` statement creates a new top-level _keyspace_. A
keyspace is a namespace that defines a replication strategy and some
options for a set of tables. Valid keyspaces names are identifiers
composed exclusively of alphanumerical characters and whose length is
lesser or equal to 32. Note that as identifiers, keyspace names are case
insensitive: use a quoted identifier for case sensitive keyspace names.

The supported `<properties>` for `CREATE KEYSPACE` are:

|===
|name |kind |mandatory |default |description
|`replication` |_map_ |yes | |The replication strategy and options to
use for the keyspace.

|`durable_writes` |_simple_ |no |true |Whether to use the commit log for
updates on this keyspace (disable this option at your own risk!).
|===

The `replication` `<property>` is mandatory. It must at least contains
the `'class'` sub-option which defines the replication strategy class to
use. The rest of the sub-options depends on that replication strategy
class. By default, Cassandra support the following `'class'`:

* `'SimpleStrategy'`: A simple strategy that defines a simple
replication factor for the whole cluster. The only sub-options supported
is `'replication_factor'` to define that replication factor and is
mandatory.
* `'NetworkTopologyStrategy'`: A replication strategy that allows to set
the replication factor independently for each data-center. The rest of
the sub-options are key-value pairs where each time the key is the name
of a datacenter and the value the replication factor for that
data-center.

Attempting to create an already existing keyspace will return an error
unless the `IF NOT EXISTS` option is used. If it is used, the statement
will be a no-op if the keyspace already exists.

[[useStmt]]


### USE

_Syntax:_

::= USE

_Sample:_

USE myApp;

The `USE` statement takes an existing keyspace name as argument and set
it as the per-connection current working keyspace. All subsequent
keyspace-specific actions will be performed in the context of the
selected keyspace, unless link:#statements[otherwise specified], until
another USE statement is issued or the connection terminates.

[[alterKeyspaceStmt]]


### ALTER KEYSPACE

_Syntax:_

::= ALTER KEYSPACE (IF EXISTS)? WITH

_Sample:_

ALTER KEYSPACE Excelsior
WITH replication = {'class': 'SimpleStrategy', 'replication_factor' :
4};

The `ALTER KEYSPACE` statement alters the properties of an existing
keyspace. The supported `<properties>` are the same as for the
link:#createKeyspaceStmt[`CREATE KEYSPACE`] statement.

[[dropKeyspaceStmt]]


### DROP KEYSPACE

_Syntax:_

::= DROP KEYSPACE ( IF EXISTS )?

_Sample:_

 DROP KEYSPACE myApp;

A `DROP KEYSPACE` statement results in the immediate, irreversible
removal of an existing keyspace, including all column families in it,
and all data contained in those column families.

If the keyspace does not exists, the statement will return an error,
unless `IF EXISTS` is used in which case the operation is a no-op.

[[createTableStmt]]
