<!-- Converted from modules/cassandra/pages/reference/cql-commands/drop-index.adoc (AsciiDoc). Includes are inlined. -->

# DROP INDEX

Removes an existing index.
The default index name is `table_name_column_name_idx`.

## Syntax

BNF definition:

```bnf
drop_index_statement::= DROP INDEX [ IF EXISTS ] index_name

```

```
DROP INDEX [ IF EXISTS ] [<keyspace_name>.]<index_name> ;
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

## Example

Drop the index `rank_idx` from the `cycling.rank_by_year_and_name` table.

```language-cql
DROP INDEX IF EXISTS cycling.rank_idx;
```
