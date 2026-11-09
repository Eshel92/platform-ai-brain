<!-- Converted from modules/cassandra/pages/developing/cql/indexing/sai/_sai-create.adoc (AsciiDoc). Includes are inlined. -->

# Create SAI index

To create an SAI index, you must define the index name, table name, and column name for the column to be indexed. 
 
To create a simple SAI index:

```language-cql
CREATE INDEX lastname_sai_idx ON cycling.cyclist_semi_pro (lastname) 
```

For most SAI indexes, the column name is defined in the `CREATE INDEX` statement that also uses `USING 'sai'`.
The SAI index options are defined in the `WITH OPTIONS` clause.
The `case_sensitive` option is set to `false` to allow case-insensitive searches.
The `normalize` option is set to `true` to allow searches to be normalized for Unicode characters.
The `ascii_only` option is set to `true` to allow searches to be limited to ASCII characters.

The `map` collection data type is the one exception, as shown in the example below.

## Partition key SAI error

SAI indexes cannot be created on the partition key, as a primary index already exists and is used for queries.
If you attempt to create an SAI on the partition key column, an error will be returned:

CQL::
+
--
```language-cql
CREATE INDEX ON demo2.person_id_name_primarykey (id)
  USING 'sai';
```
--

Result::
+
--
```console
InvalidRequest: Error from server: code=2200 [Invalid query] message="Cannot create secondary index on the only partition key column id"
```
--

## `map` collection in SAI index

Map collections do have a different format than other SAI indexes:

```sql
// Create an index on a map key to find all cyclist/team combos for a year 
CREATE INDEX IF NOT EXISTS team_year_keys_idx
ON cycling.cyclist_teams ( KEYS (teams) );

// Create an index on a map key to find all cyclist/team combos for a year 
CREATE INDEX IF NOT EXISTS team_year_values_idx
ON cycling.cyclist_teams ( VALUES (teams) );

// Create an index on a map key to find all cyclist/team combos for a year 
CREATE INDEX IF NOT EXISTS team_year_entries_idx
ON cycling.cyclist_teams ( ENTRIES (teams) );
```

## similarity-function for vector search

This example uses the following table:

```sql
CREATE TABLE IF NOT EXISTS cycling.comments_vs (
```

To check if `comment_vector` has a particular similarity function set, use the `similarity-function` option set to one of the supported similarity functions: DOT_PRODUCT, COSINE, or EUCLIDEAN. The default similarity function is COSINE.

This index creates an index on the `comment_vector` column with the similarity function set to DOT_PRODUCT:

```console
CREATE INDEX sim_comments_idx 
    ON cycling.comments_vs (comment_vector) 
    USING 'sai'  
    WITH OPTIONS = { 'similarity_function': 'DOT_PRODUCT'};
```

'''
Other resources

See CREATE CUSTOM INDEX for more information about creating SAI indexes.
