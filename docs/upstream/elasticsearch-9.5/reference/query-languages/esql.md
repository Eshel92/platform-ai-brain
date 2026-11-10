---
applies_to:
  stack:
  serverless:
navigation_title: "ES|QL"
mapped_pages:
  - https://www.elastic.co/guide/en/elasticsearch/reference/current/esql-language.html
  - https://www.elastic.co/guide/en/elasticsearch/reference/current/esql.html
  - https://www.elastic.co/guide/en/elasticsearch/reference/current/esql-getting-started.html
  - https://www.elastic.co/guide/en/elasticsearch/reference/current/esql-using.html
  - https://www.elastic.co/guide/en/elasticsearch/reference/current/esql-examples.html
products:
  - id: elasticsearch
---

# ES|QL reference [esql-language]

**Elasticsearch Query Language (ES|QL)** is a piped query language for filtering, transforming, and analyzing data.

## What's ES|QL? [_the_esql_compute_engine]

You can author ES|QL queries to find specific events, perform statistical analysis, and create visualizations. It supports a wide range of commands, functions, and operators to perform various data operations, such as filter, aggregation, time-series analysis, and more. It initially supported a subset of the features available in Query DSL, but it is rapidly evolving with every Elastic Cloud Serverless and Stack release.

ES|QL is designed to be easy to read and write, making it accessible for users with varying levels of technical expertise. It is particularly useful for data analysts, security professionals, and developers who need to work with large datasets in Elasticsearch.

::::{include} esql/_snippets/common/query-performance-tip.md
::::

## How does it work? [search-analyze-data-esql]

ES|QL uses pipes (`|`) to manipulate and transform data in a step-by-step fashion. This approach allows you to compose a series of operations, where the output of one operation becomes the input for the next, enabling complex data transformations and analysis.

Here's a simple example of an ES|QL query:

```esql
FROM sample_data
| SORT @timestamp DESC
| LIMIT 3
```

Note that each line in the query represents a step in the data processing pipeline:
- The `FROM` clause specifies the index or data stream to query
- The `SORT` clause sorts the data by the `@timestamp` field in descending order
- The `LIMIT` clause restricts the output to the top 3 results

### User interfaces

You can interact with ES|QL in two ways:

- **Programmatic access**: Use ES|QL syntax with the Elasticsearch `_query` endpoint.
  - Refer to [](esql/esql-rest.md)

- **Interactive interfaces**: Work with ES|QL through Elastic user interfaces including Kibana Discover, Dashboards, Dev Tools, and analysis tools in Elastic Security and Observability.
  - Refer to [Using ES|QL in Kibana](docs-content://explore-analyze/query-filter/languages/esql-kibana.md).


## ES|QL circuit breaker settings [esql-circuit-breaker]

The relevant circuit breaker settings can be found in the [Circuit Breakers page](/reference/elasticsearch/configuration-reference/circuit-breaker-settings.md#circuit-breakers-page-esql).

