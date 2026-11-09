<!-- Converted from modules/cassandra/pages/reference/cql-commands/create-table-examples.adoc (AsciiDoc). Includes are inlined. -->

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
