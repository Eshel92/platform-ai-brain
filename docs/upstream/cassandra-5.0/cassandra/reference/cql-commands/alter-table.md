<!-- Converted from modules/cassandra/pages/reference/cql-commands/alter-table.adoc (AsciiDoc). Includes are inlined. -->

# ALTER TABLE

Modifies the columns and properties of a table.

Add new columns, drop existing columns, renames columns, and modify table properties.
The command returns no results.

**Note:**
`ALTER COLUMNFAMILY` is deprecated.

*See also:* CREATE TABLE,
DROP TABLE,
CREATE CUSTOM INDEX for Storage-Attached Indexes (SAI), CREATE INDEX for secondary indexes (2i)

## Syntax

BNF definition:

```bnf
alter_table_statement::= ALTER TABLE [ IF EXISTS ] table_name alter_table_instruction
alter_table_instruction::= ADD [ IF NOT EXISTS ] column_definition ( ',' column_definition)*
	| DROP [ IF EXISTS ] column_name ( ',' column_name )*
	| RENAME [ IF EXISTS ] column_name to column_name (AND column_name to column_name)*
	| ALTER [ IF EXISTS ] column_name ( column_mask | DROP MASKED )
	| WITH options
column_definition::= column_name cql_type [ column_mask]
column_mask::= MASKED WITH ( DEFAULT | function_name '(' term ( ',' term )* ')' )

```

```
ALTER TABLE [<keyspace_name>.]<table_name>
  [ ADD ( <column_definition> | <column_definition_list> ) [ , ... ] ]
  [ DROP <column_name> [ , ... ] ]
  [ [ RENAME <column_name> TO <column_name> ] ]
  [ WITH <table_properties> [ , ... ] ];
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
Name of the table to alter.

*column_name*::
Name of the column to alter, drop, or add.

## column_definition

Enclosed in parentheses after the table name, use a comma-separated list to define multiple columns.
All tables must have at least one [primary key](https://cassandra.apache.org/_/glossary.html#primary-key) column.
Each column is defined using the following syntax: `column_name cql_type_definition [STATIC | PRIMARY KEY] [, ...]`

*Restriction:*

* A table must have at least one `PRIMARY KEY`.
* When `PRIMARY KEY` is at the end of a column definition, that column is the only primary key for the table, and is defined as the [partition key](https://cassandra.apache.org/_/glossary.html#partition-key).
* A static column cannot be a primary key.
* Primary keys can include frozen collections.

*column_name* ::
Use a unique name for each column in a table.
To preserve case or use special characters, enclose the name in double-quotes.
cql_type_definition ::
Defines the type of data allowed in the column.
See CQL data type or a user-defined type.
*STATIC* ::
Optional, the column has a single value.
*PRIMARY KEY* ::
When the `PRIMARY KEY` is one column, append PRIMARY KEY to the end of the column definition.
This is only schema information required to create a table.
When there is one primary key, it is the partition key;
the data is divided and stored by the unique values in this column: ``column_name cql_type_definition PRIMARY KEY``.
+
Alternatively, you can declare the primary key consisting of only one column in the same way as you declare a compound primary key.

## Optional parameters

*keyspace_name*::
Name of the keyspace that contains the table to alter. 
If no name is specified, the current keyspace is used.

*ADD ( <column_definition> | <column_definition_list> )* ::
Add one or more columns and set the column data types.
Specify the column names followed by the data types.
The column value is automatically set to null.
To add multiple columns, use a comma separated list of columns placed inside parentheses.
+
```
<column_name> <cql_type> [ , ] 
[ <column_name> <cql_type> [ , ... ]
```
*Restriction:* Adding columns to a primary key is not supported after a table has been created.

*DROP ( <column> | <column_list> )* ::
Drop one or more columns.
The values contained in the row are also dropped and not recoverable.
To drop multiple columns, use a comma separated list of columns placed inside parentheses.

*RENAME <column_name> TO <column_name>* ::
Changes the name of a primary key column and preserves the existing values.
+
*Restriction:* Not supported on materialized view base-tables, or tables with secondary indexes.

[[table_options]]

## table_options

Tunes data handling, including I/O operations, compression, and compaction.
Table property options use the following syntax:

* Single values: `<option_name> = '<value>'`
* Multiple values: `<option_name> = { '<subproperty>' : '<value>' [, ...] } [AND ...]`
+
Simple JSON format, key-value pairs in a comma-separated list enclosed by curly brackets.

**Note:**
When no value is specified, the default is used.

In a CREATE TABLE (or ALTER TABLE) CQL statement, use a `WITH` clause to define table property options.
Separate multiple values with `AND`.

```language-cql
CREATE TABLE [<keyspace_name>.]<table_name>
WITH option_name = '<value>'
AND option_name = {<option_map>};
```

*bloom_filter_fp_chance = <N>* ::
False-positive probability for SSTable [bloom filter](https://en.wikipedia.org/wiki/Bloom_filter).
When a client requests data, the bloom filter checks if the row exists before executing disk I/O.
Values range from 0 to 1.0, where: `0` is the minimum value use to enable the largest possible bloom filter (uses the most memory) and `1.0` is the maximum value disabling the bloom filter.

**Tip:**
Recommended setting: `0.1`.
A higher value yields diminishing returns.

*Default*: `bloom_filter_fp_chance = '0.01'`

*caching = { 'keys' : 'value', 'rows_per_partition' : 'value'}* ::
Optimizes the use of cache memory without manual tuning.
Weighs the cached data by size and access frequency.
Coordinate this setting with the global caching properties in the cassandra.yaml file.
Valid values:

* `ALL`-- all primary keys or rows
* `NONE`-- no primary keys or rows
* `<N>`: (rows per partition only) -- specify a whole number *Default*: `{ 'keys': 'ALL', 'rows_per_partition': 'NONE' }`

*cdc* ::
Creates a Change Data Capture (CDC) log on the table.
+
Valid values:

* `TRUE`- create CDC log
* `FALSE`- do not create CDC log
*comment = 'some text that describes the table'* ::
Provide documentation on the table.

**Tip:**
Enter a description of the types of queries the table was designed to satisfy.

[[DefaultTTL]]*default_time_to_live* ::
TTL (Time To Live) in seconds, where zero is disabled.
The maximum configurable value is `630720000` (20 years).
Beginning in 2018, the expiration timestamp can exceed the maximum value supported by the storage engine;
see the warning below.
If the value is greater than zero, TTL is enabled for the entire table and an expiration timestamp is added to each column.
A new TTL timestamp is calculated each time the data is updated and the row is removed after all the data expires.
+
Default value: `0` (disabled).
+

**Warning:**
The database storage engine can only encode TTL timestamps through `January 19 2038 03:14:07 UTC` due to the [Year 2038 problem](https://en.wikipedia.org/wiki/Year_2038_problem).
The TTL date overflow policy determines whether requests with expiration timestamps later than the maximum date are rejected or inserted.

[[gc_grace_seconds]]*gc_grace_seconds* ::
Seconds after data is marked with a tombstone (deletion marker) before it is eligible for garbage-collection.
Default value: 864000 (10 days).
The default value allows time for the database to maximize consistency prior to deletion.
+

**Note:**
Tombstoned records within the grace period are excluded from hints or batched mutations.
+
In a single-node cluster, this property can safely be set to zero.
You can also reduce this value for tables whose data is not explicitly deleted -- for example, tables containing only data with [TTL](https://cassandra.apache.org/_/glossary.html#ttl) set, or tables with `default_time_to_live` set.
However, if you lower the `gc_grace_seconds` value, consider its interaction with these operations:
+

* *hint replays*: When a node goes down and then comes back up, other nodes replay the write operations (called hints) that are queued for that node while it was unresponsive.
The database does not replay hints older than gc_grace_seconds after creation.
The max_hint_window setting in the
cassandra.yaml file sets the time limit (3 hours by default) for collecting hints for the unresponsive node.

* *batch replays*: Like hint queues, batch operations store database mutations that are replayed in sequence.
As with hints, the database does not replay a batched mutation older than gc_grace_seconds after creation.
If your application uses batch operations, consider the possibility that decreasing gc_grace_seconds increases the chance that a batched write operation may restore deleted data.
The configuration/cass_yaml_file.html#batchlog_replay_throttle[batchlog_replay_throttle] property in the cassandra.yaml file give some control of the batch replay process.
The most important factors, however, are the size and scope of the batches you use.

*memtable_flush_period_in_ms* ::
Milliseconds before `memtables` associated with the table are flushed.
When memtable_flush_period_in_ms=0, the memtable will flush when:

* the flush threshold is met
* on shutdown
* on nodetool flush
* when commitlogs get full *Default*: `0`

*min_index_interval* ::
Minimum gap between index entries in the index summary.
A lower min_index_interval means the index summary contains more entries from the index, which allows the database to search fewer index entries to execute a read.
A larger index summary may also use more memory.
The value for min_index_interval is the densest possible sampling of the index.

*max_index_interval* ::
If the total memory usage of all index summaries reaches this value,
{product} decreases the index summaries for the coldest SSTables to the maximum set by max_index_interval.
The max_index_interval is the sparsest possible sampling in relation to memory pressure.

*speculative_retry* ::
Configures [rapid read protection](https://www.datastax.com/dev/blog/rapid-read-protection-in-cassandra-2-0-2).
Normal read requests are sent to just enough replica nodes to satisfy the [consistency level](https://cassandra.apache.org/_/glossary.html#consistency-level).
In rapid read protection, extra read requests are sent to other replicas, even after the consistency level has been met.
The speculative retry property specifies the trigger for these extra read requests.
+

* ALWAYS: The coordinator node sends extra read requests to all other replicas after every read of that table.
* <X>percentile: Track each table's typical read latency (in milliseconds).
Coordinator node retrieves the typical latency time of the table being read and calculates X percent of that figure.
The coordinator sends redundant read requests if the number of milliseconds it waits without responses exceeds that calculated figure.
+
For example, if the speculative_retry property for Table_A is set to `80percentile`, and that table's typical latency is 60 milliseconds, the coordinator node handling a read of Table_A would send a normal read request first, and send out redundant read requests if it received no responses within 48ms, which is 80% of 60ms.
+
* <N>ms: The coordinator node sends extra read requests to all other replicas if the coordinator node has not received any responses within `N` milliseconds.
* NONE: The coordinator node does not send extra read requests after any read of that table.

|===
| Compaction Strategy |  |  |

| UCS
| LCS
| STCS
| TWCS

|===

*table_properties* ::
You can modify an existing table's properties.
Some properties are single options that are set to a value:
+
```no-highlight
<option_name> = <value> [ AND ... ]
```
+
For example, `speculative_retry = '10ms'`.
Enclose the value for a string property in single quotation marks.
+
Other table properties are set using a JSON map: `option_name = { <subproperty_name> : <value> [ , ... ] }`
+
See table_options for more details.

## Usage notes

*Restrictions:*

* Can only rename clustering columns in the primary key.
* Cannot change the data type of a column.
* For a table that has a materialized view, cannot drop a column from the table even if the column is not used in the materialized view.
* Cannot rename or drop columns that have dependent secondary indexes.
* Do not add a column with the same name as an existing column but with a different data type.
It will prevent commit log replays and corrupt existing SSTables with old data.

## Examples

This section uses the cyclist_races table.

### Adding a column

To add a column, use the ADD instruction:

```language-cql
ALTER TABLE cycling.cyclist_races
```

To add a column of a collection type:

```language-cql
ALTER TABLE cycling.cyclist_races
```

This operation does not validate the existing data.

*Restriction:* You cannot use the `ADD` instruction to add:

* A column with the same name as an existing column
* A static column if the table has no clustering columns.

### Dropping a column

To remove a column from the table, use the DROP instruction:

```language-cql
ALTER TABLE cycling.cyclist_races
```

`DROP` removes the column from the table definition.
The column becomes unavailable for queries immediately after it is dropped.
The database drops the column data during the next compaction.

*Restriction:*

* If you drop a column then re-add it, {product}
does not restore the values written before the column was dropped.
* Do not re-add a dropped column that contained timestamps generated by a client;
you can re-add columns with timestamps generated by the write time facility.

### Renaming a column

To rename a column in the race_times table:

```language-cql
ALTER TABLE cycling.race_times
```

*Restriction:* The following restrictions apply to `RENAME`:

* You can only rename clustering columns, which are part of the primary key.
* You cannot rename the partition key because the partition key determines the data storage location on a node.
If a different partition name is required, the table must be recreated and the data migrated.
+

**Note:**
There are many restrictions when using `RENAME` because SSTables are immutable.
To change the state of the data on disk, everything must be rewritten.

* You can index a renamed column.
* You cannot rename a column if an index has been created on it.
* You cannot rename a static column.

### Modifying table properties

To change an existing table's properties, use `ALTER TABLE` and `WITH`.
You can specify a:

* Single property name and value.
* Property map to set the names and values, as shown in the next section on compression and compaction.

For example, to add a comment to the cyclist_base table using WITH:

```language-cql
ALTER TABLE cycling.cyclist_base
```

Enclose a text property value in single quotation marks.

[[alter-compression]]

### Modifying compression and compaction

Use a property map to alter the comments table's compression or compaction setting:

```language-cql
ALTER TABLE cycling.cyclist_base
```

Enclose the name of each key in single quotes.
If the value is a string, enclose the string in quotes as well.

**Caution:**
If you change the compaction strategy of a table with existing data, the database rewrites all existing SSTables using the new strategy.
This can take hours, which can be a major problem for a production system.
For strategies to minimize this disruption, see [How to change the compaction strategy on a production cluster](http://blog.alteroot.org/articles/2015-04-20/change-cassandra-compaction-strategy-on-production-cluster.html) and [Impact of Changing Compaction Strategy](https://groups.google.com/forum/#!topic/nosql-databases/iYPoy-06Qvs).

### Changing caching

Set the number of rows per partition to store in the row cache for the comments table to 10 rows:

```language-cql
ALTER TABLE cycling.comments
```

### Change the speculative retries

Modify the `cyclist_base` table to 95th percentile for speculative retry:

```language-cql
ALTER TABLE cycling.cyclist_base
```

Modify the `cyclist_base` table to use 10 milliseconds for speculative retry:

```language-cql
ALTER TABLE cycling.cyclist_base
```

### Enabling and disabling background compaction

The following example sets the `enabled` property to `false` to disable background compaction:

```language-cql
ALTER TABLE cycling.comments
```

**Warning:**
Disabling background compaction can be harmful: without it, the database does not regain disk space, and could allow [zombies](https://docs.datastax.com/en/glossary/doc/glossary/gloss_zombie.html) to propagate.
Although compaction uses I/O, it is better to leave it enabled in most cases.

### Reading extended compaction logs

Set the `log_all` subproperty to `true` to collect in-depth information about compaction activity on a node in a dedicated log file.

**Important:**
If you enable extended compaction logging for any table on any node, it is enabled for all tables on all nodes in the cluster.

When extended compaction is enabled, the database creates a file named compaction-%d.log (where `%d` is a sequential number) in home/logs.

The compaction logging service logs detailed information about the following types of compaction events:

* `type:enable`
+
Lists SSTables that have been flushed previously.
+
```no-highlight
{"type":"enable","keyspace":"test","table":"t","time":1470071098866,"strategies":
  [    {"strategyId":"0","type":"LeveledCompactionStrategy","tables":[],"repaired":true,"folders":
      ["/home/carl/oss/cassandra/bin/../data/data"]},
    {"strategyId":"1","type":"LeveledCompactionStrategy","tables":[],"repaired":false,"folders":
      ["/home/carl/oss/cassandra/bin/../data/data"]
    }
 ]
}
```

* `type: flush`
+
Logs a flush event from a memtable to an SSTable on disk, including the CompactionStrategy for each table.
+
```
{"type":"flush","keyspace":"test","table":"t","time":1470083335639,"tables":
  [    {"strategyId":"1","table":
      {"generation":1,"version":"mb","size":106846362,"details":
        {"level":0,"min_token":"-9221834874718566760","max_token":"9221396997139245178"}
      }
    }
 ]
}
```

* `type: compaction`
+
Logs a compaction event.
+
```
{"type":"compaction","keyspace":"test","table":"t","time":1470083660267,
 "start":"1470083660188","end":"1470083660267","input":
  [    {"strategyId":"1","table":
      {"generation":1372,"version":"mb","size":1064979,"details":
        {"level":1,"min_token":"7199305267944662291","max_token":"7323434447996777057"}
      }
    }
 ],"output":
  [    {"strategyId":"1","table":
      {"generation":1404,"version":"mb","size":1064306,"details":
        {"level":2,"min_token":"7199305267944662291","max_token":"7323434447996777057"}
      }
    }
 ]
}
```

* `type: pending`
+
Lists the number of pending tasks for a compaction strategy.
+
```
{"type":"pending","keyspace":"test","table":"t",
 "time":1470083447967,"strategyId":"1","pending":200}
```

### Reviewing the table definition

Use `DESCRIBE` or `DESC` to view the table definition.

```language-cql
DESC cycling.comments;

```

The table details including the column names are returned.

```results
CREATE TABLE cycling.comments (
    id uuid,
    created_at timestamp,
    comment text,
    commenter text,
    record_id timeuuid,
    PRIMARY KEY (id, created_at)
) WITH CLUSTERING ORDER BY (created_at DESC)
    AND bloom_filter_fp_chance = 0.01
    AND caching = {'keys': 'NONE', 'rows_per_partition': '10'}
    AND comment = ''
    AND compaction = {'class': 'org.apache.cassandra.db.compaction.SizeTieredCompactionStrategy', 'enabled': 'true', 'max_threshold': '32', 'min_threshold': '4'}
    AND compression = {'chunk_length_in_kb': '64', 'class': 'org.apache.cassandra.io.compress.DeflateCompressor'}
    AND crc_check_chance = 1.0
    AND default_time_to_live = 0
    AND gc_grace_seconds = 864000
    AND max_index_interval = 2048
    AND memtable_flush_period_in_ms = 0
    AND min_index_interval = 128
    AND speculative_retry = '99PERCENTILE';

```
