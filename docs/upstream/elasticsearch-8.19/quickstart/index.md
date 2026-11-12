<!-- Converted from quickstart/index.asciidoc (AsciiDoc). Includes are inlined. -->

# Quick starts

Use these quick starts to get hands-on experience with the Elasticsearch APIs.
Unless otherwise noted, these examples will use queries written in Query DSL syntax.

## Requirements

You'll need a running Elasticsearch cluster, together with Kibana to use the Dev Tools API Console.
Run the following command in your terminal to set up a single-node local cluster in Docker:

```sh
curl -fsSL https://elastic.co/start-local | sh
```

Alternatively, refer to our other deployment options.

## Hands-on quick starts

* Basics: Index and search data using Elasticsearch APIs. Learn about indices, documents, and mappings, and perform a basic search using the Query DSL.
* Basics: Full-text search and filtering. Learn about different options for querying data, including full-text search and filtering, using the Query DSL.
* ES|QL basics: Learn how to query and aggregate your data using ES|QL.
* ES|QL for search: Learn how to use ES|QL for search use cases, including full-text search, semantic search, and hybrid search.
* Basics: Analyze ecommerce data with aggregations. Learn how to analyze data using different types of aggregations, including metrics, buckets, and pipelines.
* Semantic search: Learn how to create embeddings for your data with `semantic_text` and query using the `semantic` query.
** Hybrid search with `semantic_text`: Learn how to combine semantic search with full-text search.
* Bring your own dense vector embeddings: Learn how to ingest dense vector embeddings into Elasticsearch.

**Working in Python**
******************

If you're interested in using Elasticsearch with Python, check out Elastic Search Labs:

* [`elasticsearch-labs` repository](https://github.com/elastic/elasticsearch-labs): Contains a range of Python [notebooks](https://github.com/elastic/elasticsearch-labs/tree/main/notebooks) and [example apps](https://github.com/elastic/elasticsearch-labs/tree/main/example-apps).
* [Tutorial](https://www.elastic.co/search-labs/tutorials/search-tutorial/welcome): This walks you through building a complete search solution with Elasticsearch from the ground up using Flask.
******************

(See `quickstart/getting-started.md`)
(See `quickstart/full-text-filtering-tutorial.md`)
(See `quickstart/esql-search-tutorial.md`)
(See `quickstart/aggs-tutorial.md`)
