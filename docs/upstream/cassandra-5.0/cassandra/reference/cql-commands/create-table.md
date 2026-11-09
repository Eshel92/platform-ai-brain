<!-- Converted from modules/cassandra/pages/reference/cql-commands/create-table.adoc (AsciiDoc). Includes are inlined. -->

# CREATE TABLE

Defines the columns of a new table.

{product} supports creating a new [table](https://cassandra.apache.org/_/glossary.html#table) in the selected keyspace.
Use `IF NOT EXISTS` to suppress the error message if the table already exists;
no table is created.
A static column can store the same data in multiple clustered rows of a partition, and then retrieve that data with a single `SELECT` statement.

Tables support a single counter column.

*See also:* ALTER TABLE,
DROP TABLE,
CREATE CUSTOM INDEX for Storage-Attached Indexes (SAI), CREATE INDEX for secondary indexes (2i)

## Syntax

BNF definition:

```bnf
create_table_statement::= CREATE TABLE [ IF NOT EXISTS ] table_name '(' 
	column_definition  ( ',' column_definition )*  
	[ ',' PRIMARY KEY '(' primary_key ')' ] 
	 ')' [ WITH table_options ] 
column_definition::= column_name cql_type [ STATIC ] [ column_mask ] [ PRIMARY KEY]
column_mask::= MASKED WITH ( DEFAULT | function_name '(' term ( ',' term )* ')' )
primary_key::= partition_key [ ',' clustering_columns ] 
partition_key::= column_name  | '(' column_name ( ',' column_name )* ')' 
clustering_columns::= column_name ( ',' column_name )* 
table_options::= COMPACT STORAGE [ AND table_options ]
	| CLUSTERING ORDER BY '(' clustering_order ')' 
	[ AND table_options ]  | options
clustering_order::= column_name (ASC | DESC) ( ',' column_name (ASC | DESC) )*

```

```
CREATE TABLE [ IF NOT EXISTS ] [<keyspace_name>.]<table_name>
  ( <column_definition> [ , ... ] | PRIMARY KEY (column_list) )
  [ WITH [ <table_options> ]
  [ [ AND ] CLUSTERING ORDER BY [ <clustering_column_name> (ASC | DESC) ] ]
  [ [ AND ] ID = '<table_hash_tag>' ] ] ;
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
Name of the table to index.

*column_name*::
Name of the column.

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

## column_definition

Enclosed in parentheses after the table name, use a comma-separated list to define multiple columns.
All tables must have at least one [primary key](https://cassandra.apache.org/_/glossary.html#primary-key) column.
Each column is defined using the following syntax: `column_name cql_type_definition [STATIC | PRIMARY KEY] [, ...]`

*Restriction:*

* A table must have at least one `PRIMARY KEY`.
* When `PRIMARY KEY` is at the end of a column definition, that column is the only primary key for the table, and is defined as the [partition-key](https://cassandra.apache.org/_/glossary.html#)[partition key].
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

### compression = { compression_map }

Configure the `compression_map` by specifying the compression algorithm `class` followed by the subproperties in simple JSON format.

**Tip:**
Implement custom compression classes using the `org.apache.cassandra.io.compress.ICompressor` interface.

```console
compression = {
   ['class' : '<compression_algorithm_name>',
     'chunk_length_in_kb' : '<value>',
     'crc_check_chance' : '<value>',]
   | 'sstable_compression' : '']
}
```

*class* ::
Sets the compressor name.
{product} provides the following built-in classes:
+
|===
|Compression Algorithm |Cassandra Class |Compression |Decompression
|Ratio |C* Version

|[LZ4](https://lz4.github.io/lz4/) |`LZ4Compressor` | A | A | C+ | `>=1.2.2`

|[LZ4HC](https://lz4.github.io/lz4/) |`LZ4Compressor` | C | A | B+ | `>= 3.6`

|[Zstd](https://facebook.github.io/zstd/) |`ZstdCompressor` | A- | A- | A+ | `>= 4.0`

|[Snappy](http://google.github.io/snappy/) |`SnappyCompressor` | A- | A | C | `>= 1.0`

|[Deflate (zlib)](https://zlib.net) |`DeflateCompressor` | C | C | A | `>= 1.0`
|===
+

**Important:**
Use only compression implementations bundled with {product}.
+
Choosing the right compressor depends on your requirements for space savings over read performance.
LZ4 is fastest to decompress, followed by Snappy, then by Deflate.
Compression effectiveness is inversely correlated with decompression speed.
The extra compression from Deflate or Snappy is not enough to make up for the decreased performance for general-purpose workloads, but for archival data they may be worth considering.
+
*Default*: `LZ4Compressor`.
*chunk_length_in_kb* ::
Size (in KB) of the block.
On disk, SSTables are compressed by block to allow random reads.
Values larger than the default value might improve the compression rate, but increases the minimum size of data to be read from disk when a read occurs.
The default value is a good middle ground for compressing tables.
Adjust compression size to account for read/write access patterns (how much data is typically requested at once) and the average size of rows in the table.
+
*Default*: `64`.
*crc_check_chance* ::
When compression is enabled, each compressed block includes a checksum of that block for the purpose of detecting disk bit rot and avoiding the propagation of corruption to other replica.
This option defines the probability with which those checksums are checked during read.
By default they are always checked.
Set to 0 to disable checksum checking and to 0.5, for instance, to check them on every other read.
+
*Default*: `1.0`.
*sstable_compression* ::
Disables compression.
Specify a null value.

### compaction = \{compaction_map}

Defines the strategy for cleaning up data after writes.

Syntax uses a simple JSON format:

```language-cql
compaction = {
     'class' : '<compaction_strategy_name>',
     '<property_name>' : <value> [, ...] }
```

where the <compaction_strategy_name> is SizeTieredCompactionStrategy, TimeWindowCompactionStrategy, or LeveledCompactionStrategy.

**Important:**
Use only compaction implementations bundled with {product}.
See Compaction for more details.

#### Common properties

The following properties apply to all compaction strategies.

```language-cql
compaction = {
     'class' : 'compaction_strategy_name',
     'enabled' : (true | false),
     'log_all' : (true | false),
     'only_purge_repaired_tombstone' : (true | false),
     'tombstone_threshold' : <ratio>,
     'tombstone_compaction_interval' : <sec>,
     'unchecked_tombstone_compaction' : (true | false),
     'min_threshold' : <num_sstables>,
     'max_threshold' : <num_sstables> }
```

*enabled* ::
Enable background compaction.

* `true` runs minor compactions.
* `false` disables minor compactions.

+

**Tip:**
Use `nodetool enableautocompaction` to start running compactions.

{empty}::
Default: `true`

*log_all* ::
Activates advanced logging for the entire cluster.
+
Default: `false`

*only_purge_repaired_tombstone* ::
Enabling this property prevents data from resurrecting when repair is not run within the `gc_grace_seconds`.
When its been a long time between repairs, the database keeps all tombstones.
+

* `true` - Only allow tombstone purges on repaired SSTables.
* `false` - Purge tombstones on SSTables during compaction even if the table has not been repaired.

+
Default: `false`

*tombstone_threshold* ::
The ratio of garbage-collectable tombstones to all contained columns.
If the ratio exceeds this limit, compactions starts only on that table to purge the tombstones.
+
Default: `0.2`

*tombstone_compaction_interval* ::
Number of seconds before compaction can run on an SSTable after it is created.
An SSTable is eligible for compaction when it exceeds the `tombstone_threshold`.
Because it might not be possible to drop tombstones when doing a single SSTable compaction, and since the compaction is triggered base on an estimated tombstone ratio, this setting makes the minimum interval between two single SSTable compactions tunable to prevent an SSTable from being constantly re-compacted.
+
Default: `86400` (1 day)

*unchecked_tombstone_compaction* ::
Setting to `true` allows tombstone compaction to run without pre-checking which tables are eligible for the operation.
Even without this pre-check, {product} checks an SSTable to make sure it is safe to drop tombstones.
+
Default: `false`

*min_threshold* ::
The minimum number of SSTables to trigger a minor compaction.
+
*Restriction:* Not used in `LeveledCompactionStrategy`.
+
Default: `4`

*max_threshold* ::
The maximum number of SSTables before a minor compaction is triggered.
+
*Restriction:* Not used in `LeveledCompactionStrategy`.
+
Default: `32`

[[STCS]]

#### SizeTieredCompactionStrategy

The compaction class `SizeTieredCompactionStrategy` (STCS) triggers a minor compaction when table meets the `min_threshold`.
Minor compactions do not involve all the tables in a keyspace.
See
SizeTieredCompactionStrategy (STCS).

**Note:**
Default compaction strategy.

The following properties only apply to SizeTieredCompactionStrategy:

```language-cql
compaction = {
     'class' : 'SizeTieredCompactionStrategy',
     'bucket_high' : <factor>,
     'bucket_low' : <factor>,
     'min_sstable_size' : <int> }
```

*bucket_high* ::
Size-tiered compaction merges sets of SSTables that are approximately the same size.
The database compares each SSTable size to the average of all SSTable sizes for this table on the node.
It merges SSTables whose size in KB are within [average-size * bucket_low] and [average-size * bucket_high].
+
Default: `1.5`

*bucket_low* ::
Size-tiered compaction merges sets of SSTables that are approximately the same size.
The database compares each SSTable size to the average of all SSTable sizes for this table on the node.
It merges SSTables whose size in KB are within [average-size * bucket_low] and [average-size * bucket_high].
+
Default: `0.5`

*min_sstable_size* ::
STCS groups SSTables into buckets.
The bucketing process groups SSTables that differ in size by less than 50%.
This bucketing process is too fine-grained for small SSTables.
If your SSTables are small, use this option to define a size threshold in MB below which all SSTables belong to one unique bucket.
+
Default: `50` (MB)

**Note:**
The `cold_reads_to_omit` property for
SizeTieredCompactionStrategy (STCS) is no longer supported.

[[TWCS]]

#### TimeWindowCompactionStrategy

The compaction class `TimeWindowCompactionStrategy` (TWCS) compacts SSTables using a series of _time windows_ or _buckets_.
TWCS creates a new time window within each successive time period.
During the active time window, TWCS compacts all SSTables flushed from memory into larger SSTables using STCS.
At the end of the time period, all of these SSTables are compacted into a single SSTable.
Then the next time window starts and the process repeats.
See TimeWindowCompactionStrategy (TWCS).

**Note:**
All of the properties for STCS are also valid for TWCS.

The following properties apply only to TimeWindowCompactionStrategy:

```language-cql
compaction = {
     'class' : 'TimeWindowCompactionStrategy,
     'compaction_window_unit' : <days>,
     'compaction_window_size' : <int>,
     'split_during_flush' : (true | false) }
```

*compaction_window_unit* ::
Time unit used to define the bucket size.
The value is based on the Java `TimeUnit`.
For the list of valid values, see the Java API `TimeUnit` page located at https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/TimeUnit.html.
+
Default: `days`

*compaction_window_size* ::
Units per bucket.
+
Default: `1`

[[LCS]]

#### LeveledCompactionStrategy

The compaction class `LeveledCompactionStrategy` (LCS) creates SSTables of a fixed, relatively small size (160 MB by default) that are grouped into levels.
Within each level, SSTables are guaranteed to be non-overlapping.
Each level (L0, L1, L2 and so on) is 10 times as large as the previous.
Disk I/O is more uniform and predictable on higher than on lower levels as SSTables are continuously being compacted into progressively larger levels.
At each level, row keys are merged into non-overlapping SSTables in the next level.
See [LeveledCompactionStrategy (LCS)](https://docs.datastax.com/en/dse/6.8/dse-arch/datastax_enterprise/dbInternals/dbIntHowDataMaintain.html#dbIntHowDataMaintain__lcs-compaction).

**Note:**
For more guidance, see [When to Use Leveled Compaction](https://www.datastax.com/dev/blog/when-to-use-leveled-compaction) and [Leveled Compaction](https://www.datastax.com/dev/blog/leveled-compaction-in-apache-cassandra) blog.

The following properties only apply to LeveledCompactionStrategy:

```language-cql
compaction = {
     'class' : 'LeveledCompactionStrategy,
     'sstable_size_in_mb' : <int> }
```

*sstable_size_in_mb* ::
The target size for SSTables that use the LeveledCompactionStrategy.
Although SSTable sizes should be less or equal to sstable_size_in_mb, it is possible that compaction could produce a larger SSTable during compaction.
This occurs when data for a given partition key is exceptionally large.
The {product} database does not split the data into two SSTables.
+
Default: `160`
+

**Caution:**
The default value, 160 MB, may be inefficient and negatively impact database indexing and the queries that rely on indexes.
For example, consider the benefit of using higher values for sstable_size_in_mb in tables that use (SAI) indexes.
For related information, see Compaction strategies.

#### DateTieredCompactionStrategy (deprecated)

**Important:**
Use TimeWindowCompactionStrategy instead.

Stores data written within a certain period of time in the same SSTable.

*base_time_seconds* ::
The size of the first time window.
+
Default: `3600`

*max_sstable_age_days (deprecated)* ::
{product} does not compact SSTables if its most recent data is older than this property.
Fractional days can be set.
+
Default: `1000`

*max_window_size_seconds* ::
The maximum window size in seconds.
+
Default: `86400`

*timestamp_resolution* ::
Units, <MICROSECONDS> or <MILLISECONDS>, to match the timestamp of inserted data.
+
Default: `MICROSECONDS`

## Optional parameters

### Table keywords

*CLUSTERING ORDER BY ( column_name ASC | DESC)* ::
Order rows storage to make use of the on-disk sorting of columns.
Specifying order can make query results more efficient.
Options are:
+
`ASC`: ascending (default order)
+
`DESC`: descending, reverse order

*ID* ::
If a table is accidentally dropped with DROP TABLE, use this option to
recreate the table and run a commit log replay to retrieve the data.

*index_name*::
Name of the index.
Enclose in quotes to use special characters or preserve capitalization.
If no name is specified, {product} names the index: `<table_name>_<column_name>_idx`.

*keyspace_name*::
Name of the keyspace that contains the table to index.
If no name is specified, the current keyspace is used.

## Usage notes

If the column already contains data, it is indexed during the execution of this statement.
After an index has been created, it is automatically updated when data in the column changes.

Indexing with the `CREATE INDEX` command can impact performance.
Before creating an index, be aware of when and when not to create an index.

*Restriction:* Indexing counter columns is not supported.

# Examples

## Create a table with UUID as the primary key

Create the `cyclist_name` table with UUID as the primary key:

```language-cql
CREATE TABLE IF NOT EXISTS cycling.cyclist_name (
```

## Create a compound primary key

Create the `cyclist_category` table and store the data in reverse order:

```language-cql
CREATE TABLE IF NOT EXISTS cycling.cyclist_category (
```

## Create a composite partition key

Create a table that is optimized for query by cyclist rank by year:

```language-cql
CREATE TABLE IF NOT EXISTS cycling.rank_by_year_and_name (
```

## Create a table with a vector column

Create a table with a vector column

```language-cql
CREATE TABLE IF NOT EXISTS cycling.comments_vs (
```

## Create a table with a frozen UDT

Create the `race_winners` table that has a frozen user-defined type (UDT):

```language-cql
CREATE TABLE IF NOT EXISTS cycling.race_winners (
```

See Create a user-defined type for information on Create UDTs.
UDTs can be created unfrozen if only non-collection fields are used in the user-defined type creation.
If the table is created with an unfrozen UDT, then individual field values can be updated and deleted.

## Create a table with a CDC log

Create a change data capture log for the `cyclist_id` table:

```language-cql
CREATE TABLE IF NOT EXISTS cycling.cyclist_id (
```

CDC logging must be enabled in cassandra.yaml.

**Caution:**
Before enabling CDC logging, have a plan for moving and consuming the log information.
After the disk space limit is reached, writes to CDC-enabled tables are rejected until more space is freed.
See [Change-data-capture (CDC) space settings](https://docs.datastax.com/en/dse/6.8/dse-admin/datastax_enterprise/config/configCassandra_yaml.html#cdcSpaceSection) for information about available CDC settings.

## Storing data in descending order

The following example shows a table definition that stores the categories with the highest points first.

```language-cql
CREATE TABLE IF NOT EXISTS cycling.cyclist_category (
```

[[restore-commit-log]]

## Restoring from the table ID for commit log replay

Recreate a table with its original ID to facilitate restoring table data by replaying commit logs:

```language-cql
CREATE TABLE IF NOT EXISTS cycling.cyclist_emails (
```

To retrieve a table's ID, query the `id` column of `system_schema.tables`.
For example:

```language-cql
SELECT id
```

To perform a restoration of the table, see Backups for more information.
