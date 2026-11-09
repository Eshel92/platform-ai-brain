<!-- Converted from modules/cassandra/pages/developing/cql/triggers.adoc (AsciiDoc). Includes are inlined. -->

# Triggers

Triggers are identified with a name defined by:

```bnf
trigger_name ::= identifier

```

[[create-trigger-statement]]

## CREATE TRIGGER

Creating a new trigger uses the `CREATE TRIGGER` statement:

```bnf
create_trigger_statement ::= CREATE TRIGGER [ IF NOT EXISTS ] trigger_name
	ON table_name
	USING string

```

For instance:

```cql
CREATE TRIGGER myTrigger ON myTable USING 'org.apache.cassandra.triggers.InvertedIndex';

```

The actual logic that makes up the trigger can be written in any Java
(JVM) language and exists outside the database. You place the trigger
code in a `lib/triggers` subdirectory of the Cassandra installation
directory, it loads during cluster startup, and exists on every node
that participates in a cluster. The trigger defined on a table fires
before a requested DML statement occurs, which ensures the atomicity of
the transaction.

[[drop-trigger-statement]]

## DROP TRIGGER

Dropping a trigger uses the `DROP TRIGGER` statement:

```bnf
drop_trigger_statement ::= DROP TRIGGER [ IF EXISTS ] trigger_nameON table_name

```

For instance:

```cql
DROP TRIGGER myTrigger ON myTable;

```
