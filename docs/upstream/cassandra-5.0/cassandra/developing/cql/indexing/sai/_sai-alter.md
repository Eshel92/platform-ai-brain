<!-- Converted from modules/cassandra/pages/developing/cql/indexing/sai/_sai-alter.adoc (AsciiDoc). Includes are inlined. -->

# Alter SAI index

SAI indexes cannot be altered. 
If you need to modify an SAI index, you will need to drop the current index, create a new index, and rebuild the cycling.

. Drop index
+
```language-cql
DROP INDEX IF EXISTS cycling.lastname_sai_idx;
```

. Create new index  
+ 
```language-cql
CREATE INDEX lastname_sai_idx ON cycling.cyclist_semi_pro (lastname) 
```
