<!-- Converted from modules/cassandra/pages/reference/cql-commands/drop-table.adoc (AsciiDoc). Includes are inlined. -->

# DROP TABLE

Immediate, irreversible removal of a table, including all data contained in the table.

*Restriction:* Drop all materialized views associated with the table before dropping the table.
An error message lists any materialized views that are based on the table: `InvalidRequest: Error from server: code=2200 [Invalid query] message="Cannot drop table when materialized views still depend on it (cycling.{cyclist_by_age})"`

*See also:* CREATE TABLE,
ALTER TABLE,
CREATE CUSTOM INDEX for Storage-Attached Indexes (SAI), CREATE INDEX for secondary indexes (2i)

## Syntax

BNF definition:

```bnf
drop_table_statement::= DROP TABLE [ IF EXISTS ] table_name

```

```
DROP TABLE [ IF EXISTS ] [<keyspace_name>.]<table_name> ;
```

.Syntax legend
.Legend
|===
| Syntax conventions | Description

| UPPERCASE
| Literal keyword.

| Lowercase
| Not literal.

| `< >`
| Variable value.
Replace with a user-defined value.

| `[]`
| Optional.
Square brackets (`[]`) surround optional command arguments.
Do not type the square brackets.

| `( )`
| Group.
Parentheses ( `( )` ) identify a group to choose from.
Do not type the parentheses.

| `\|`
| Or.
A vertical bar (`\|`) separates alternative elements.
Type any one of the elements.
Do not type the vertical bar.

| `...`
| Repeatable.
An ellipsis ( `...` ) indicates that you can repeat the syntax element as often as required.

| `'<Literal string>'`
| Single quotation (`'`) marks must surround literal strings in CQL statements.
Use single quotation marks to preserve upper case.

| `{ <key> : <value> }`
| Map collection.
Braces (`{ }`) enclose map collections or key value pairs.
A colon separates the key and the value.

| `< <datatype1>,<datatype2> >`
| Set, list, map, or tuple.
Angle brackets ( `< >` ) enclose data types in a set, list, map, or tuple.
Separate the data types with a comma.

| `<cql_statement>;`
| End CQL statement.
A semicolon (`;`) terminates all CQL statements.

| `[--]`
| Separate the command line options from the command arguments with two hyphens ( `--` ).
This syntax is useful when arguments might be mistaken for command line options.

| `+' <<schema\> ...
</schema\>> '+`
| Search CQL only: Single quotation marks (`'`) surround an entire XML schema declaration.

| `@<xml_entity>='<xml_entity_type>'`
| Search CQL only: Identify the entity and literal value to overwrite the XML element in the schema and solrConfig files.
|===

## Required parameters

*table_name*::
Name of the table to drop.

## Optional parameters

*keyspace_name*::
Name of the keyspace that contains the table to drop.
If no name is specified, the current keyspace is used.

## Examples

Drop the `cyclist_name` table:

```language-cql
DROP TABLE IF EXISTS cycling.cyclist_name;
```
