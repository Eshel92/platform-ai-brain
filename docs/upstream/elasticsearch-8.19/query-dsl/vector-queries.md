<!-- Converted from query-dsl/vector-queries.asciidoc (AsciiDoc). Includes are inlined. -->

## Vector queries

Vector queries are specialized queries that work on vector fields to efficiently perform semantic search.

`knn` query::
A query that finds the _k_ nearest vectors to a query vector for `dense_vector` fields, as measured by a similarity metric.

`sparse_vector` query::
A query used to search `sparse_vector` field types.

`semantic` query::
A query that allows you to perform semantic search on `semantic_text` fields.

### Deprecated vector queries

The following queries have been deprecated and will be removed in the near future.
Use the `sparse_vector` query query instead.

`text_expansion` query::
A query that allows you to perform sparse vector search on `sparse_vector` or `rank_features` fields.

`weighted_tokens` query::
Allows to perform text expansion queries optimizing for performance.

(See `query-dsl/knn-query.md`)
(See `query-dsl/sparse-vector-query.md`)
(See `query-dsl/semantic-query.md`)
(See `query-dsl/text-expansion-query.md`)
(See `query-dsl/weighted-tokens-query.md`)
