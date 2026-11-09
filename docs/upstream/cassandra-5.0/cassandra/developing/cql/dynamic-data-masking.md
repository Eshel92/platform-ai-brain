<!-- Converted from modules/cassandra/pages/developing/cql/dynamic-data-masking.adoc (AsciiDoc). Includes are inlined. -->

# Dynamic Data Masking (DDM)

Dynamic data masking (DDM) obscures sensitive information while still allowing access to the masked columns.
DDM doesn't alter the stored data. 
Instead, it just presents the data in its obscured form during `SELECT` queries.
This aims to provide some degree of protection against accidental data exposure. However, anyone with direct access to the SSTable files will be able to read the clear data.

## Masking functions

DDM is based on a set of CQL native functions that obscure sensitive information. 
The available functions are:

|===
|Function | Description

| `mask_null(value)` 
| Replaces the first argument with a `null` column. 
The returned value is always a non-existent column, and not a not-null column representing a `null` value.

Examples:

`mask_null('Alice')` -> `null`

`mask_null(123)` -> `null`

| `mask_default(value)` 
| Replaces its argument by an arbitrary, fixed default value of the same type.
This will be `\***\***` for text values, zero for numeric values, `false` for booleans, etc.

Variable-length multi-valued types such as lists, sets and maps are masked as empty collections.

Fixed-length multi-valued types such as tuples, user-defined types (UDTs) and vectors are masked by replacing each of their values by the default masking value of the value type.

Examples:

`mask_default('Alice')` -> `'\****'`

`mask_default(123)` -> `0`

`mask_default((list<int>) [1, 2, 3])` -> `[]`

`mask_default((vector<int, 3>) [1, 2, 3])` -> `[0, 0, 0]`

| `mask_replace(value, replacement])` 
| Replaces the first argument by the replacement value on the second argument. 
The replacement value needs to have the same type as the replaced value.

Examples:

`mask_replace('Alice', 'REDACTED')` -> `'REDACTED'`

`mask_replace(123, -1)` -> `-1`

| `mask_inner(value, begin, end, [padding])` 
| Returns a copy of the first `text`, `varchar` or `ascii` argument, replacing each character except the first and last ones by a padding character. 
The second and third arguments are the size of the exposed prefix and suffix. 
The optional fourth argument is the padding character, `\*` by default.

Examples:

`mask_inner('Alice', 1, 2)` -> `'A**ce'`

`mask_inner('Alice', 1, null)` -> `'A****'`

`mask_inner('Alice', null, 2)` -> `'***ce'`

`mask_inner('Alice', 2, 1, '\#')` -> `'Al##e'`

| `mask_outer(value, begin, end, [padding])` 
| Returns a copy of the first `text`, `varchar` or `ascii` argument, replacing the first and last character by a padding character. 
The second and third arguments are the size of the exposed prefix and suffix. 
The optional fourth argument is the padding character, `\*` by default.

Examples:

`mask_outer('Alice', 1, 2)` -> `'*li**'`

`mask_outer('Alice', 1, null)` -> `'*lice'`

`mask_outer('Alice', null, 2)` -> `'Ali**'`

`mask_outer('Alice', 2, 1, '\#')` -> `'##ic#'`

| `mask_hash(value, [algorithm])` 
| Returns a `blob` containing the hash of the first argument. 
The optional second argument is the hashing algorithm to be used, according the available Java security provider. 
The default hashing algorithm is `SHA-256`.

Examples:

`mask_hash('Alice')`

`mask_hash('Alice', 'SHA-512')`

|===
Those functions can be used on `SELECT` queries to get an obscured view of the data. 
For example:

```cql
CREATE TABLE patients (
   id timeuuid PRIMARY KEY,
   name text,
   birth date
);

INSERT INTO patients(id, name, birth) VALUES (now(), 'alice', '1982-01-02');
INSERT INTO patients(id, name, birth) VALUES (now(), 'bob', '1982-01-02');

SELECT mask_inner(name, 1, null), mask_default(birth) FROM patients;

//   system.mask_inner(name, 1, NULL) | system.mask_default(birth)
// -----------------------------------+----------------------------
//                                b** |                 1970-01-01
//                              a**** |                 1970-01-01

```

## Attaching masking functions to table columns

A masking function can be permanently attached to any column of a table.
If a masking column is defined, `SELECT` queries will always return the column values in their masked form.
The masking will be transparent to the users running `SELECT` queries.
The only way to know that a column is masked is to consult the table definition.

This is an optional feature that is disabled by default.
To use the feature, enable the `dynamic_data_masking_enabled` property in `cassandra.yaml`.

The masks of the columns of a table can be defined in the `CREATE TABLE` to create the table schema. This example uses the `mask_inner` function with two arguments:

```cql
CREATE TABLE patients (
```

When using a `SELECT` query on this data, three arguments are required for the `mask_inner` function, but the first argument is always omitted when attaching the function to the table schema.
The value of that first argument is always interpreted as the value of the masked column, in this case a `text` column.

For the same reason, using the masking function `mask_default` doesn't have any argument when creating the table schema, but it requires one argument when used on `SELECT` queries.

Data can be normally inserted into the masked table without alteration. 
For example:

```cql
INSERT INTO patients(id, name, birth) VALUES (now(), 'alice', '1984-01-02');
```

The `SELECT` query will return the masked data.
The masking function will be automatically applied to the column values.

```cql
SELECT name, birth FROM patients;
```

An `ALTER TABLE` query can be used to make changes to a masking function on a table column.

```cql
ALTER TABLE patients ALTER name 
```

In a similar way, a masking function can be detached from a column with an `ALTER TABLE` query:

```cql
ALTER TABLE patients ALTER name 
```

## Permissions

Ordinary users are created without the `UNMASK` permission and will see masked values.
Giving a user the `UNMASK` permission allows them to retrieve the unmasked values of masked columns.
Superusers are automatically created with the `UNMASK` permission,
and will see the unmasked values in a `SELECT` query results.

For example, suppose that we have a table with masked columns:

```cql
CREATE TABLE patients (
```

And we insert some data into the table:

```cql
INSERT INTO patients(id, name, birth) VALUES (now(), 'alice', '1984-01-02');
```

```cql
LOGIN unprivileged
```

Then we create two users with `SELECT` permission for the table, but we only grant the `UNMASK` permission to one of the users:

```cql
CREATE USER privileged WITH PASSWORD 'xyz';
```

The user with the `UNMASK` permission can see the clear, unmasked data:

```cql
LOGIN privileged
```

The user without the `UNMASK` permission can only see the masked data:

```cql
LOGIN unprivileged
```

The `UNMASK` permission works like any other permission, and can be revoked at will:

```cql
REVOKE UNMASK ON TABLE patients 
```

Please note that, when authentication is disabled, the anonymous default user has all the permissions, including the `UNMASK` permission, and can see the unmasked data.
In other words, attaching data masking functions to columns only makes sense if authentication is enabled.

Only users with the `UNMASK` permission are allowed to use masked columns in the `WHERE` clause of a `SELECT` query.
Users without the `UNMASK` permission cannot use this feature.
This feature prevents malicious users seeing clear data by running exhaustive, brute force queries. 
The user without the `UNMASK` permission will see the following:

```cql
CREATE USER untrusted_user WITH PASSWORD 'xyz';
```

There are some use cases where a trusted database user needs to produce masked data that untrusted external users will query.
For instance, a trusted app can connect to the database and with a query extract masked data that will be displayed to its end users.
In that case, the trusted user (the app) can be given the `SELECT_MASKED` permission.
This permission lets the user query masked columns in the `WHERE` clause of a `SELECT` query,
while still only seeing the masked data in the query results:

```cql
CREATE USER trusted_user WITH PASSWORD 'xyz';
```

## Custom functions

User-defined functions (UDFs) can be attached to a table column.
The UDFs used for masking should belong to the same keyspace as the masked table.
The column value to mask will be passed as the first argument of the attached UDF.
Thus, the UDFs attached to a column should have at least one argument,
and that argument should have the same type as the masked column.
Also, the attached UDF should return values of the same type as the masked column:

```cql
CREATE FUNCTION redact(input text)
```

This creates a dependency between the table schema and the functions.
Any attempt to drop the function will be rejected while this dependency exists.
Consequently, you must drop the mask column in the table before dropping the function:

```cql
ALTER TABLE patients ALTER name 
```

Dropping the column, or its containing table, or its containing keyspace will also remove the dependency.

Aggregate functions cannot be used as masking functions.
