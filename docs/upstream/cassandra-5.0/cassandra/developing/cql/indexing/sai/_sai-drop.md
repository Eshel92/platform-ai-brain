<!-- Converted from modules/cassandra/pages/developing/cql/indexing/sai/_sai-drop.adoc (AsciiDoc). Includes are inlined. -->

# Drop SAI index

SAI indexes can be dropped (deleted). 

To drop an SAI index:

```language-cql
DROP INDEX IF EXISTS cycling.lastname_sai_idx;
```

This command does not return a result.
