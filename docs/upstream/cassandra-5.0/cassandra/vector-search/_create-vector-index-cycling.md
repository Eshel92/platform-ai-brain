<!-- Converted from modules/cassandra/pages/vector-search/_create-vector-index-cycling.adoc (AsciiDoc). Includes are inlined. -->

# Create vector index

Create the custom index with Storage Attached Indexing (SAI):

```cql
CREATE INDEX IF NOT EXISTS ann_index 
```

For more about SAI, see the Storage Attached Indexing documentation.

**Important:**
The index can be created with options that define the similarity function:

```
CREATE INDEX IF NOT EXISTS ann_index
```

Valid values for the `similarity_function` are `DOT_PRODUCT`, `COSINE`, or `EUCLIDEAN`.
