<!-- Part 5 of 8 of cassandra/developing/cql/cql_singlefile.md (split because the page is big). -->

### Data Control

#### Permissions

Permissions on resources are granted to roles; there are several
different types of resources in Cassandra and each type is modelled
hierarchically:

* The hierarchy of Data resources, Keyspaces and Tables has the
structure `ALL KEYSPACES` -> `KEYSPACE` -> `TABLE`
* Function resources have the structure `ALL FUNCTIONS` -> `KEYSPACE` ->
`FUNCTION`
* Resources representing roles have the structure `ALL ROLES` -> `ROLE`
* Resources representing JMX ObjectNames, which map to sets of
MBeans/MXBeans, have the structure `ALL MBEANS` -> `MBEAN`

Permissions can be granted at any level of these hierarchies and they
flow downwards. So granting a permission on a resource higher up the
chain automatically grants that same permission on all resources lower
down. For example, granting `SELECT` on a `KEYSPACE` automatically
grants it on all `TABLES` in that `KEYSPACE`. Likewise, granting a
permission on `ALL FUNCTIONS` grants it on every defined function,
regardless of which keyspace it is scoped in. It is also possible to
grant permissions on all functions scoped to a particular keyspace.

Modifications to permissions are visible to existing client sessions;
that is, connections need not be re-established following permissions
changes.

The full set of available permissions is:

* `CREATE`
* `ALTER`
* `DROP`
* `SELECT`
* `MODIFY`
* `AUTHORIZE`
* `DESCRIBE`
* `EXECUTE`
* `UNMASK`
* `SELECT_MASKED`

Not all permissions are applicable to every type of resource. For
instance, `EXECUTE` is only relevant in the context of functions or
mbeans; granting `EXECUTE` on a resource representing a table is
nonsensical. Attempting to `GRANT` a permission on resource to which it
cannot be applied results in an error response. The following
illustrates which permissions can be granted on which types of resource,
and which statements are enabled by that permission.

|===
|permission |resource |operations | | |
|`CREATE` |`ALL KEYSPACES` |`CREATE KEYSPACE` <br> `CREATE TABLE` in any
keyspace | | |

|`CREATE` |`KEYSPACE` |`CREATE TABLE` in specified keyspace | | |

|`CREATE` |`ALL FUNCTIONS` |`CREATE FUNCTION` in any keyspace <br>
`CREATE AGGREGATE` in any keyspace | | |

|`CREATE` |`ALL FUNCTIONS IN KEYSPACE` |`CREATE FUNCTION` in keyspace
<br> `CREATE AGGREGATE` in keyspace | | |

|`CREATE` |`ALL ROLES` |`CREATE ROLE` | | |

|`ALTER` |`ALL KEYSPACES` |`ALTER KEYSPACE` <br> `ALTER TABLE` in any
keyspace | | |

|`ALTER` |`KEYSPACE` |`ALTER KEYSPACE` <br> `ALTER TABLE` in keyspace |
| |

|`ALTER` |`TABLE` |`ALTER TABLE` | | |

|`ALTER` |`ALL FUNCTIONS` |`CREATE FUNCTION` replacing any existing <br>
`CREATE AGGREGATE` replacing any existing | | |

|`ALTER` |`ALL FUNCTIONS IN KEYSPACE` |`CREATE FUNCTION` replacing
existing in keyspace <br> `CREATE AGGREGATE` replacing any existing in
keyspace | | |

|`ALTER` |`FUNCTION` |`CREATE FUNCTION` replacing existing <br>
`CREATE AGGREGATE` replacing existing | | |

|`ALTER` |`ALL ROLES` |`ALTER ROLE` on any role | | |

|`ALTER` |`ROLE` |`ALTER ROLE` | | |

|`DROP` |`ALL KEYSPACES` |`DROP KEYSPACE` <br> `DROP TABLE` in any
keyspace | | |

|`DROP` |`KEYSPACE` |`DROP TABLE` in specified keyspace | | |

|`DROP` |`TABLE` |`DROP TABLE` | | |

|`DROP` |`ALL FUNCTIONS` |`DROP FUNCTION` in any keyspace <br>
`DROP AGGREGATE` in any existing | | |

|`DROP` |`ALL FUNCTIONS IN KEYSPACE` |`DROP FUNCTION` in keyspace <br>
`DROP AGGREGATE` in existing | | |

|`DROP` |`FUNCTION` |`DROP FUNCTION` | | |

|`DROP` |`ALL ROLES` |`DROP ROLE` on any role | | |

|`DROP` |`ROLE` |`DROP ROLE` | | |

|`SELECT` |`ALL KEYSPACES` |`SELECT` on any table | | |

|`SELECT` |`KEYSPACE` |`SELECT` on any table in keyspace | | |

|`SELECT` |`TABLE` |`SELECT` on specified table | | |

|`SELECT` |`ALL MBEANS` |Call getter methods on any mbean | | |

|`SELECT` |`MBEANS` |Call getter methods on any mbean matching a
wildcard pattern | | |

|`SELECT` |`MBEAN` |Call getter methods on named mbean | | |

|`MODIFY` |`ALL KEYSPACES` |`INSERT` on any table <br> `UPDATE` on any
table <br> `DELETE` on any table <br> `TRUNCATE` on any table | | |

|`MODIFY` |`KEYSPACE` |`INSERT` on any table in keyspace <br> `UPDATE`
on any table in keyspace <br>   `DELETE` on any table in keyspace <br>
`TRUNCATE` on any table in keyspace |`MODIFY` |`TABLE` |`INSERT` <br>
`UPDATE` <br> `DELETE` <br> `TRUNCATE`

|`MODIFY` |`ALL MBEANS` |Call setter methods on any mbean | | |

|`MODIFY` |`MBEANS` |Call setter methods on any mbean matching a
wildcard pattern | | |

|`MODIFY` |`MBEAN` |Call setter methods on named mbean | | |

|`AUTHORIZE` |`ALL KEYSPACES` |`GRANT PERMISSION` on any table <br>
`REVOKE PERMISSION` on any table | | |

|`AUTHORIZE` |`KEYSPACE` |`GRANT PERMISSION` on table in keyspace <br>
`REVOKE PERMISSION` on table in keyspace | | |

|`AUTHORIZE` |`TABLE` |`GRANT PERMISSION` <br> `REVOKE PERMISSION` | | |

|`AUTHORIZE` |`ALL FUNCTIONS` |`GRANT PERMISSION` on any function <br>
`REVOKE PERMISSION` on any function | | |

|`AUTHORIZE` |`ALL FUNCTIONS IN KEYSPACE` |`GRANT PERMISSION` in
keyspace <br> `REVOKE PERMISSION` in keyspace | | |

|`AUTHORIZE` |`ALL FUNCTIONS IN KEYSPACE` |`GRANT PERMISSION` in
keyspace <br> `REVOKE PERMISSION` in keyspace | | |

|`AUTHORIZE` |`FUNCTION` |`GRANT PERMISSION` <br> `REVOKE PERMISSION` |
| |

|`AUTHORIZE` |`ALL MBEANS` |`GRANT PERMISSION` on any mbean <br>
`REVOKE PERMISSION` on any mbean | | |

|`AUTHORIZE` |`MBEANS` |`GRANT PERMISSION` on any mbean matching a
wildcard pattern <br> `REVOKE PERMISSION` on any mbean matching a
wildcard pattern | | |

|`AUTHORIZE` |`MBEAN` |`GRANT PERMISSION` on named mbean <br>
`REVOKE PERMISSION` on named mbean | | |

|`AUTHORIZE` |`ALL ROLES` |`GRANT ROLE` grant any role <br>
`REVOKE ROLE` revoke any role | | |

|`AUTHORIZE` |`ROLES` |`GRANT ROLE` grant role <br> `REVOKE ROLE` revoke
role | | |

|`DESCRIBE` |`ALL ROLES` |`LIST ROLES` all roles or only roles granted
to another, specified role | | |

|`DESCRIBE` |@ALL MBEANS |Retrieve metadata about any mbean from the
platform’s MBeanServer | | |

|`DESCRIBE` |@MBEANS |Retrieve metadata about any mbean matching a
wildcard patter from the platform’s MBeanServer | | |

|`DESCRIBE` |@MBEAN |Retrieve metadata about a named mbean from the
platform’s MBeanServer | | |

|`EXECUTE` |`ALL FUNCTIONS` |`SELECT`, `INSERT`, `UPDATE` using any
function <br> use of any function in `CREATE AGGREGATE` | | |

|`EXECUTE` |`ALL FUNCTIONS IN KEYSPACE` |`SELECT`, `INSERT`, `UPDATE`
using any function in keyspace <br> use of any function in keyspace in
`CREATE AGGREGATE` | | |

|`EXECUTE` |`FUNCTION` |`SELECT`, `INSERT`, `UPDATE` using function <br>
use of function in `CREATE AGGREGATE` | | |

|`EXECUTE` |`ALL MBEANS` |Execute operations on any mbean | | |

|`EXECUTE` |`MBEANS` |Execute operations on any mbean matching a
wildcard pattern | | |

|`EXECUTE` |`MBEAN` |Execute operations on named mbean | | |

|`UNMASK` |`ALL KEYSPACES` |See the clear contents of masked columns on any table | | |

|`UNMASK` |`KEYSPACE` |See the clear contents of masked columns on any table in keyspace | | |

|`UNMASK` |`TABLE` |See the clear contents of masked columns on the specified table | | |

|`SELECT_MASKED` | `ALL KEYSPACES` | `SELECT` restricting masked columns on any table | | |

|`SELECT_MASKED` | `KEYSPACE` | `SELECT` restricting masked columns on any table in specified keyspace | | |

|`SELECT_MASKED` | `TABLE` | `SELECT` restricting masked columns on the specified table | | |
|===

[[grantPermissionsStmt]]

#### GRANT PERMISSION

_Syntax:_

```bnf
::= GRANT ( ALL ( PERMISSIONS )? | ( PERMISSION )? ) ON TO

::= CREATE | ALTER | DROP | SELECT | MODIFY | AUTHORIZE | DESCRIBE | UNMASK | SELECT_MASKED
EXECUTE

::= ALL KEYSPACES
| KEYSPACE
| ( TABLE )?
| ALL ROLES
| ROLE
| ALL FUNCTIONS ( IN KEYSPACE )?
| FUNCTION
| ALL MBEANS
| ( MBEAN | MBEANS )
```

_Sample:_

GRANT SELECT ON ALL KEYSPACES TO data_reader;

This gives any user with the role `data_reader` permission to execute
`SELECT` statements on any table across all keyspaces

GRANT MODIFY ON KEYSPACE keyspace1 TO data_writer;

This give any user with the role `data_writer` permission to perform
`UPDATE`, `INSERT`, `UPDATE`, `DELETE` and `TRUNCATE` queries on all
tables in the `keyspace1` keyspace

GRANT DROP ON keyspace1.table1 TO schema_owner;

This gives any user with the `schema_owner` role permissions to `DROP`
`keyspace1.table1`.

GRANT EXECUTE ON FUNCTION keyspace1.user_function( int ) TO
report_writer;

This grants any user with the `report_writer` role permission to execute
`SELECT`, `INSERT` and `UPDATE` queries which use the function
`keyspace1.user_function( int )`

GRANT DESCRIBE ON ALL ROLES TO role_admin;

This grants any user with the `role_admin` role permission to view any
and all roles in the system with a `LIST ROLES` statement

[[grantAll]]

##### GRANT ALL

When the `GRANT ALL` form is used, the appropriate set of permissions is
determined automatically based on the target resource.

[[autoGrantPermissions]]

##### Automatic Granting

When a resource is created, via a `CREATE KEYSPACE`, `CREATE TABLE`,
`CREATE FUNCTION`, `CREATE AGGREGATE` or `CREATE ROLE` statement, the
creator (the role the database user who issues the statement is
identified as), is automatically granted all applicable permissions on
the new resource.

[[revokePermissionsStmt]]

#### REVOKE PERMISSION

_Syntax:_

```bnf
::= REVOKE ( ALL ( PERMISSIONS )? | ( PERMISSION )? ) ON FROM

::= CREATE | ALTER | DROP | SELECT | MODIFY | AUTHORIZE | DESCRIBE | UNMASK | SELECT_MASKED
EXECUTE

::= ALL KEYSPACES
| KEYSPACE
| ( TABLE )?
| ALL ROLES
| ROLE
| ALL FUNCTIONS ( IN KEYSPACE )?
| FUNCTION
| ALL MBEANS
| ( MBEAN | MBEANS )
```

_Sample:_

```sql
REVOKE SELECT ON ALL KEYSPACES FROM data_reader;
REVOKE MODIFY ON KEYSPACE keyspace1 FROM data_writer;
REVOKE DROP ON keyspace1.table1 FROM schema_owner;
REVOKE EXECUTE ON FUNCTION keyspace1.user_function( int ) FROM
report_writer;
REVOKE DESCRIBE ON ALL ROLES FROM role_admin;
```

[[listPermissionsStmt]]

##### LIST PERMISSIONS

_Syntax:_

```bnf
::= LIST ( ALL ( PERMISSIONS )? | )
( ON )?
( OF ( NORECURSIVE )? )?

::= ALL KEYSPACES
| KEYSPACE
| ( TABLE )?
| ALL ROLES
| ROLE
| ALL FUNCTIONS ( IN KEYSPACE )?
| FUNCTION
| ALL MBEANS
| ( MBEAN | MBEANS )
```

_Sample:_

LIST ALL PERMISSIONS OF alice;

Show all permissions granted to `alice`, including those acquired
transitively from any other roles.

LIST ALL PERMISSIONS ON keyspace1.table1 OF bob;

Show all permissions on `keyspace1.table1` granted to `bob`, including
those acquired transitively from any other roles. This also includes any
permissions higher up the resource hierarchy which can be applied to
`keyspace1.table1`. For example, should `bob` have `ALTER` permission on
`keyspace1`, that would be included in the results of this query. Adding
the `NORECURSIVE` switch restricts the results to only those permissions
which were directly granted to `bob` or one of `bob`’s roles.

LIST SELECT PERMISSIONS OF carlos;

Show any permissions granted to `carlos` or any of `carlos`’s roles,
limited to `SELECT` permissions on any resource.

[[types]]
