<!-- Converted from tutorial/split-chunks-in-sharded-cluster.txt (reStructuredText). Includes are inlined. -->

# Split Chunks in a Sharded Cluster

MongoDB automatically splits chunks to ensure a
fair distribution of data across the cluster and the
AutoMerger automatically merges
adjacent chunks residing on the same shard.

To split chunks manually, use the `split` command with either
fields `middle` or `find`. `mongosh` provides the
helper methods `sh.splitFind()` and `sh.splitAt()`.

`splitFind()` splits the chunk that contains the *first*
document returned that matches this query into two equally sized chunks.
You must specify the full namespace (i.e. "`<database>.<collection>`")
of the sharded collection to `splitFind()`. The query in
`splitFind()` does not need to use the shard key, though it
nearly always makes sense to do so.

**Example:**

The following command splits the chunk that contains the value of
`63109` for the `zipcode` field in the `people` collection of
the `records` database:

```javascript
sh.splitFind( "records.people", { "zipcode": "63109" } )
```

Use `splitAt()` to split a chunk in two, using the queried
document as the lower bound in the new chunk:

**Example:**

The following command splits the chunk that contains the value of
`63109` for the `zipcode` field in the `people` collection of
the `records` database.

```javascript
sh.splitAt( "records.people", { "zipcode": "63109" } )
```

**Note:**

`splitAt()` does not necessarily split the chunk
into two equally sized chunks. The split occurs at the location of
the document matching the query, regardless of where that document is
in the chunk.

**See also:**

initial-chunks-empty-collection
