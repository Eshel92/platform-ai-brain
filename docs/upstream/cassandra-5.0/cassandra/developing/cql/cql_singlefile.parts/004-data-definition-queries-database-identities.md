<!-- Part 4 of 8 of cassandra/developing/cql/cql_singlefile.md (split because the page is big). -->

### Queries

[[selectStmt]]

#### SELECT

_Syntax:_

```bnf
::= SELECT ( JSON )?
FROM
( WHERE )?
( GROUP BY )?
( ORDER BY )?
( PER PARTITION LIMIT )?
( LIMIT )?
( ALLOW FILTERING )?

::= DISTINCT?

::= (AS )? ( `,' (AS )? )*
| `*'

::=
|
| WRITETIME `(' `)'
| MAXWRITETIME `(' `)'
| COUNT `(' `*' `)'
| TTL `(' `)'
| CAST `(' AS `)'
| `(' ( (`,' )*)? `)'
| `.'
| `[' `]'
| `[' ? .. ? `]'

::= ( AND )*

::=
| `(' (`,' )* `)'
| IN `(' ( ( `,' )* )? `)'
| `(' (`,' )* `)' IN `(' ( ( `,' )* )? `)'
| TOKEN `(' ( `,' )* `)'

::= `=' | `<' | `>' | `<=' | `>=' | CONTAINS | CONTAINS KEY
::= (`,' )*
::= ( `,' )*
::= ( ASC | DESC )?
::= `(' (`,' )* `)'
```

_Sample:_

```sql
SELECT name, occupation FROM users WHERE userid IN (199, 200, 207);

SELECT JSON name, occupation FROM users WHERE userid = 199;

SELECT name AS user_name, occupation AS user_occupation FROM users;

SELECT time, value
FROM events
WHERE event_type = 'myEvent'
AND time > '2011-02-03'
AND time <= '2012-01-01'

SELECT COUNT (*) FROM users;

SELECT COUNT (*) AS user_count FROM users;
```

The `SELECT` statements reads one or more columns for one or more rows
in a table. It returns a result-set of rows, where each row contains the
collection of columns corresponding to the query. If the `JSON` keyword
is used, the results for each row will contain only a single column
named ``json''. See the section on link:#selectJson[`SELECT JSON`] for
more details.

[[selectSelection]]

##### `<select-clause>`

The `<select-clause>` determines which columns needs to be queried and
returned in the result-set. It consists of either the comma-separated
list of or the wildcard character (`*`) to select all the columns
defined for the table. Please note that for wildcard `SELECT` queries
the order of columns returned is not specified and is not guaranteed to
be stable between Cassandra versions.

A `<selector>` is either a column name to retrieve or a `<function>` of
one or more `<term>`s. The function allowed are the same as for `<term>`
and are described in the link:#functions[function section]. In addition
to these generic functions, the `WRITETIME` and `MAXWRITETIME` (resp. `TTL`)
function allows to select the timestamp of when the column was inserted (resp.
the time to live (in seconds) for the column (or null if the column has
no expiration set)) and the link:#castFun[`CAST`] function can be used
to convert one data type to another. The `WRITETIME` and `TTL` functions
can't be used on multi-cell columns such as non-frozen collections or
non-frozen user-defined types.

Additionally, individual values of maps and sets can be selected using
`[ <term> ]`. For maps, this will return the value corresponding to the
key, if such entry exists. For sets, this will return the key that is
selected if it exists and is thus mainly a way to check element
existence. It is also possible to select a slice of a set or map with
`[ <term> ... <term> `], where both bound can be omitted.

Any `<selector>` can be aliased using `AS` keyword (see examples).
Please note that `<where-clause>` and `<order-by>` clause should refer
to the columns by their original names and not by their aliases.

The `COUNT` keyword can be used with parenthesis enclosing `*`. If so,
the query will return a single result: the number of rows matching the
query. Note that `COUNT(1)` is supported as an alias.

[[selectWhere]]

##### `<where-clause>`

The `<where-clause>` specifies which rows must be queried. It is
composed of relations on the columns that are part of the `PRIMARY KEY`
and/or have a link:#createIndexStmt[secondary index] defined on them.

Not all relations are allowed in a query. For instance, non-equal
relations (where `IN` is considered as an equal relation) on a partition
key are not supported (but see the use of the `TOKEN` method below to do
non-equal queries on the partition key). Moreover, for a given partition
key, the clustering columns induce an ordering of rows and relations on
them is restricted to the relations that allow to select a *contiguous*
(for the ordering) set of rows. For instance, given

```sql
CREATE TABLE posts (
userid text,
blog_title text,
posted_at timestamp,
entry_title text,
content text,
category int,
PRIMARY KEY (userid, blog_title, posted_at)
)
```

The following query is allowed:

```sql
SELECT entry_title, content FROM posts WHERE userid='john doe' AND
blog_title='John''s Blog' AND posted_at >= '2012-01-01' AND posted_at <
'2012-01-31'
```

But the following one is not, as it does not select a contiguous set of
rows (and we suppose no secondary indexes are set):

```sql
// Needs a blog_title to be set to select ranges of posted_at
SELECT entry_title, content FROM posts WHERE userid='john doe' AND
posted_at >= '2012-01-01' AND posted_at < '2012-01-31'
```

When specifying relations, the `TOKEN` function can be used on the
`PARTITION KEY` column to query. In that case, rows will be selected
based on the token of their `PARTITION_KEY` rather than on the value.
Note that the token of a key depends on the partitioner in use, and that
in particular the RandomPartitioner won’t yield a meaningful order. Also
note that ordering partitioners always order token values by bytes (so
even if the partition key is of type int, `token(-1) > token(0)` in
particular). Example:

SELECT * FROM posts WHERE token(userid) > token('tom') AND token(userid)
< token('bob')

Moreover, the `IN` relation is only allowed on the last column of the
partition key and on the last column of the full primary key.

It is also possible to ``group'' `CLUSTERING COLUMNS` together in a
relation using the tuple notation. For instance:

SELECT * FROM posts WHERE userid='john doe' AND (blog_title, posted_at)
> ('John''s Blog', '2012-01-01')

will request all rows that sorts after the one having ``John’s Blog'' as
`blog_tile` and `2012-01-01' for `posted_at` in the clustering order. In
particular, rows having a `post_at <= '2012-01-01'` will be returned as
long as their `blog_title > 'John''s Blog'`, which wouldn’t be the case
for:

SELECT * FROM posts WHERE userid='john doe' AND blog_title > 'John''s
Blog' AND posted_at > '2012-01-01'

The tuple notation may also be used for `IN` clauses on
`CLUSTERING COLUMNS`:

SELECT * FROM posts WHERE userid='john doe' AND (blog_title, posted_at)
IN (('John''s Blog', '2012-01-01'), ('Extreme Chess', '2014-06-01'))

The `CONTAINS` operator may only be used on collection columns (lists,
sets, and maps). In the case of maps, `CONTAINS` applies to the map
values. The `CONTAINS KEY` operator may only be used on map columns and
applies to the map keys.

[[selectOrderBy]]

##### `<order-by>`

The `ORDER BY` option allows to select the order of the returned
results. It takes as argument a list of column names along with the
order for the column (`ASC` for ascendant and `DESC` for descendant,
omitting the order being equivalent to `ASC`). Currently the possible
orderings are limited (which depends on the table
link:#createTableOptions[`CLUSTERING ORDER`] ):

* if the table has been defined without any specific `CLUSTERING ORDER`,
then then allowed orderings are the order induced by the clustering
columns and the reverse of that one.
* otherwise, the orderings allowed are the order of the
`CLUSTERING ORDER` option and the reversed one.

[[selectGroupBy]]

##### `<group-by>`

The `GROUP BY` option allows to condense into a single row all selected
rows that share the same values for a set of columns.

Using the `GROUP BY` option, it is only possible to group rows at the
partition key level or at a clustering column level. By consequence, the
`GROUP BY` option only accept as arguments primary key column names in
the primary key order. If a primary key column is restricted by an
equality restriction it is not required to be present in the `GROUP BY`
clause.

Aggregate functions will produce a separate value for each group. If no
`GROUP BY` clause is specified, aggregates functions will produce a
single value for all the rows.

If a column is selected without an aggregate function, in a statement
with a `GROUP BY`, the first value encounter in each group will be
returned.

[[selectLimit]]

##### `LIMIT` and `PER PARTITION LIMIT`

The `LIMIT` option to a `SELECT` statement limits the number of rows
returned by a query, while the `PER PARTITION LIMIT` option limits the
number of rows returned for a given partition by the query. Note that
both type of limit can used in the same statement.

[[selectAllowFiltering]]

##### `ALLOW FILTERING`

By default, CQL only allows select queries that don’t involve
``filtering'' server side, i.e. queries where we know that all (live)
record read will be returned (maybe partly) in the result set. The
reasoning is that those ``non filtering'' queries have predictable
performance in the sense that they will execute in a time that is
proportional to the amount of data *returned* by the query (which can be
controlled through `LIMIT`).

The `ALLOW FILTERING` option allows to explicitly allow (some) queries
that require filtering. Please note that a query using `ALLOW FILTERING`
may thus have unpredictable performance (for the definition above), i.e.
even a query that selects a handful of records *may* exhibit performance
that depends on the total amount of data stored in the cluster.

For instance, considering the following table holding user profiles with
their year of birth (with a secondary index on it) and country of
residence:

```sql
CREATE TABLE users (
username text PRIMARY KEY,
firstname text,
lastname text,
birth_year int,
country text
)

CREATE INDEX ON users(birth_year);
```

Then the following queries are valid:

```sql
SELECT * FROM users;
SELECT firstname, lastname FROM users WHERE birth_year = 1981;
```

because in both case, Cassandra guarantees that these queries
performance will be proportional to the amount of data returned. In
particular, if no users are born in 1981, then the second query
performance will not depend of the number of user profile stored in the
database (not directly at least: due to secondary index implementation
consideration, this query may still depend on the number of node in the
cluster, which indirectly depends on the amount of data stored.
Nevertheless, the number of nodes will always be multiple number of
magnitude lower than the number of user profile stored). Of course, both
query may return very large result set in practice, but the amount of
data returned can always be controlled by adding a `LIMIT`.

However, the following query will be rejected:

SELECT firstname, lastname FROM users WHERE birth_year = 1981 AND
country = 'FR';

because Cassandra cannot guarantee that it won’t have to scan large
amount of data even if the result to those query is small. Typically, it
will scan all the index entries for users born in 1981 even if only a
handful are actually from France. However, if you ``know what you are
doing'', you can force the execution of this query by using
`ALLOW FILTERING` and so the following query is valid:

SELECT firstname, lastname FROM users WHERE birth_year = 1981 AND
country = 'FR' ALLOW FILTERING;

[[databaseRoles]]


### Database Roles

[[createRoleStmt]]

#### CREATE ROLE

_Syntax:_

```bnf
::= CREATE ROLE ( IF NOT EXISTS )? ( WITH ( AND )* )?

::= PASSWORD =
| LOGIN =
| SUPERUSER =
| OPTIONS =
```

_Sample:_

```sql
CREATE ROLE new_role;
CREATE ROLE alice WITH PASSWORD = 'password_a' AND LOGIN = true;
CREATE ROLE bob WITH PASSWORD = 'password_b' AND LOGIN = true AND
SUPERUSER = true;
CREATE ROLE carlos WITH OPTIONS = { 'custom_option1' : 'option1_value',
'custom_option2' : 99 };
```

By default roles do not possess `LOGIN` privileges or `SUPERUSER`
status.

link:#permissions[Permissions] on database resources are granted to
roles; types of resources include keyspaces, tables, functions and roles
themselves. Roles may be granted to other roles to create hierarchical
permissions structures; in these hierarchies, permissions and
`SUPERUSER` status are inherited, but the `LOGIN` privilege is not.

If a role has the `LOGIN` privilege, clients may identify as that role
when connecting. For the duration of that connection, the client will
acquire any roles and privileges granted to that role.

Only a client with with the `CREATE` permission on the database roles
resource may issue `CREATE ROLE` requests (see the
link:#permissions[relevant section] below), unless the client is a
`SUPERUSER`. Role management in Cassandra is pluggable and custom
implementations may support only a subset of the listed options.

Role names should be quoted if they contain non-alphanumeric characters.

[[createRolePwd]]

##### Setting credentials for internal authentication

Use the `WITH PASSWORD` clause to set a password for internal
authentication, enclosing the password in single quotation marks. +
If internal authentication has not been set up or the role does not have
`LOGIN` privileges, the `WITH PASSWORD` clause is not necessary.

[[createRoleConditional]]

##### Creating a role conditionally

Attempting to create an existing role results in an invalid query
condition unless the `IF NOT EXISTS` option is used. If the option is
used and the role exists, the statement is a no-op.

```sql
CREATE ROLE other_role;
CREATE ROLE IF NOT EXISTS other_role;
```

[[alterRoleStmt]]

#### ALTER ROLE

_Syntax:_

```bnf
::= ALTER ROLE (IF EXISTS)? ( WITH ( AND )* )?

::= PASSWORD =
| LOGIN =
| SUPERUSER =
| OPTIONS =
```

_Sample:_

ALTER ROLE bob WITH PASSWORD = 'PASSWORD_B' AND SUPERUSER = false;

If the role does not exist, the statement will return an error, unless `IF EXISTS` is used in which case the operation is a no-op.

Conditions on executing `ALTER ROLE` statements:

* A client must have `SUPERUSER` status to alter the `SUPERUSER` status
of another role
* A client cannot alter the `SUPERUSER` status of any role it currently
holds
* A client can only modify certain properties of the role with which it
identified at login (e.g. `PASSWORD`)
* To modify properties of a role, the client must be granted `ALTER`
link:#permissions[permission] on that role

[[dropRoleStmt]]

#### DROP ROLE

_Syntax:_

::= DROP ROLE ( IF EXISTS )?

_Sample:_

```sql
DROP ROLE alice;
DROP ROLE IF EXISTS bob;
```

`DROP ROLE` requires the client to have `DROP`
link:#permissions[permission] on the role in question. In addition,
client may not `DROP` the role with which it identified at login.
Finaly, only a client with `SUPERUSER` status may `DROP` another
`SUPERUSER` role. +
Attempting to drop a role which does not exist results in an invalid
query condition unless the `IF EXISTS` option is used. If the option is
used and the role does not exist the statement is a no-op.

[[grantRoleStmt]]

#### GRANT ROLE

_Syntax:_

::= GRANT TO

_Sample:_

GRANT report_writer TO alice;

This statement grants the `report_writer` role to `alice`. Any
permissions granted to `report_writer` are also acquired by `alice`. +
Roles are modelled as a directed acyclic graph, so circular grants are
not permitted. The following examples result in error conditions:

```sql
GRANT role_a TO role_b;
GRANT role_b TO role_a;
```

```sql
GRANT role_a TO role_b;
GRANT role_b TO role_c;
GRANT role_c TO role_a;
```

[[revokeRoleStmt]]

#### REVOKE ROLE

_Syntax:_

::= REVOKE FROM

_Sample:_

REVOKE report_writer FROM alice;

This statement revokes the `report_writer` role from `alice`. Any
permissions that `alice` has acquired via the `report_writer` role are
also revoked.

[[listRolesStmt]]

##### LIST ROLES

_Syntax:_

::= LIST ROLES ( OF )? ( NORECURSIVE )?

_Sample:_

LIST ROLES;

Return all known roles in the system, this requires `DESCRIBE`
permission on the database roles resource.

LIST ROLES OF 'alice';

Enumerate all roles granted to `alice`, including those transitively
aquired.

LIST ROLES OF 'bob' NORECURSIVE

List all roles directly granted to `bob`.

[[createUserStmt]]

#### CREATE USER

Prior to the introduction of roles in Cassandra 2.2, authentication and
authorization were based around the concept of a `USER`. For backward
compatibility, the legacy syntax has been preserved with `USER` centric
statments becoming synonyms for the `ROLE` based equivalents.

_Syntax:_

```bnf
::= CREATE USER ( IF NOT EXISTS )? ( WITH PASSWORD )? ()?

::= SUPERUSER | NOSUPERUSER
```

_Sample:_

```sql
CREATE USER alice WITH PASSWORD 'password_a' SUPERUSER;
CREATE USER bob WITH PASSWORD 'password_b' NOSUPERUSER;
```

`CREATE USER` is equivalent to `CREATE ROLE` where the `LOGIN` option is
`true`. So, the following pairs of statements are equivalent:

```sql
CREATE USER alice WITH PASSWORD 'password_a' SUPERUSER;
CREATE ROLE alice WITH PASSWORD = 'password_a' AND LOGIN = true AND
SUPERUSER = true;

CREATE USER IF NOT EXISTS alice WITH PASSWORD 'password_a' SUPERUSER;
CREATE ROLE IF NOT EXISTS alice WITH PASSWORD = 'password_a' AND LOGIN =
true AND SUPERUSER = true;

CREATE USER alice WITH PASSWORD 'password_a' NOSUPERUSER;
CREATE ROLE alice WITH PASSWORD = 'password_a' AND LOGIN = true AND
SUPERUSER = false;

CREATE USER alice WITH PASSWORD 'password_a' NOSUPERUSER;
CREATE ROLE alice WITH PASSWORD = 'password_a' AND LOGIN = true;

CREATE USER alice WITH PASSWORD 'password_a';
CREATE ROLE alice WITH PASSWORD = 'password_a' AND LOGIN = true;
```

[[alterUserStmt]]

#### ALTER USER

_Syntax:_

```bnf
::= ALTER USER (IF EXISTS)? ( WITH PASSWORD )? ( )?

::= SUPERUSER | NOSUPERUSER
```

_Sample:_

```sql
ALTER USER alice WITH PASSWORD 'PASSWORD_A';
ALTER USER bob SUPERUSER;
```

If the user does not exist, the statement will return an error, unless `IF EXISTS` is used in which case the operation is a no-op.

[[dropUserStmt]]

#### DROP USER

_Syntax:_

::= DROP USER ( IF EXISTS )?

_Sample:_

```sql
DROP USER alice;
DROP USER IF EXISTS bob;
```

[[listUsersStmt]]

#### LIST USERS

_Syntax:_

::= LIST USERS;

_Sample:_

LIST USERS;

This statement is equivalent to

LIST ROLES;

but only roles with the `LOGIN` privilege are included in the output.

[[databaseIdentity]]


### Database Identities

[[AddIdentityStmt]]

#### ADD IDENTITY

_Syntax:_

::= ADD IDENTITY ( IF NOT EXISTS )? TO ROLE ?

_Sample:_

ADD IDENTITY 'id1' TO ROLE 'role1';

Only a user with privileges to add roles can add identities

Role names & Identity names should be quoted if they contain non-alphanumeric characters.

[[addIdentityConditional]]

##### Adding an identity conditionally

Attempting to add an existing identity results in an invalid query
condition unless the `IF NOT EXISTS` option is used. If the option is
used and the identity exists, the statement is a no-op.

ADD IDENTITY IF NOT EXISTS 'id1' TO ROLE 'role1';

[[dropIdentityStmt]]

#### DROP IDENTITY

_Syntax:_

::= DROP IDENTITY ( IF EXISTS )?

_Sample:_

```sql
DROP IDENTITY 'testIdentity';
DROP IDENTITY IF EXISTS 'testIdentity';
```

Only a user with privileges to drop roles can remove identities

Attempting to drop an Identity which does not exist results in an invalid
query condition unless the `IF EXISTS` option is used. If the option is
used and the identity does not exist the statement is a no-op.

[[dataControl]]
