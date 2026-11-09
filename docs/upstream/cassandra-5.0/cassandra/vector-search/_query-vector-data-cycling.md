<!-- Converted from modules/cassandra/pages/vector-search/_query-vector-data-cycling.adoc (AsciiDoc). Includes are inlined. -->

# Query vector data with CQL

To query data using Vector Search, use a `SELECT` query:

```cql
SELECT * FROM cycling.comments_vs 
```

To obtain the similarity calculation of the best scoring node closest to the query data as part of the results, use a `SELECT` query:

```cql
SELECT comment, similarity_cosine(comment_vector, [0.2, 0.15, 0.3, 0.2, 0.05])
```

The supported functions for this type of query are:

* similarity_dot_product
* similarity_cosine
* similarity_euclidean

with the parameters of (<vector_column>, <embedding_value>).
Both parameters represent vectors.

**Note:**
* The limit must be 1,000 or fewer.
* Vector Search utilizes Approximate Nearest Neighbor (ANN) that in most cases yields results almost as good as the exact match. The scaling is superior to Exact Nearest Neighbor (KNN).

* Least-similar searches are not supported.
* Vector Search works optimally on tables with no overwrites or deletions of the `item_vector` column. For an `item_vector` column with changes, expect slower search results.
