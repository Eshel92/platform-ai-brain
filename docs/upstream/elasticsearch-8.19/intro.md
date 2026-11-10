<!-- Converted from intro.asciidoc (AsciiDoc). Includes are inlined. -->

## Elasticsearch basics

This guide covers the core concepts you need to understand to get started with Elasticsearch.
If you'd prefer to start working with Elasticsearch right away, set up a local development environment and jump to hands-on code examples.

This guide covers the following topics:

* elasticsearch-intro-what-is-es: Learn about Elasticsearch and some of its main use cases.
* elasticsearch-intro-deploy: Understand your options for deploying Elasticsearch in different environments, including a fast local development setup.
* documents-indices: Understand Elasticsearch's most important primitives and how it stores data.
* es-ingestion-overview: Understand your options for ingesting data into Elasticsearch.
* search-analyze: Understand your options for searching and analyzing data in Elasticsearch.
* scalability: Understand the basic concepts required for moving your Elasticsearch deployment to production.

### What is Elasticsearch?

{es-repo}[Elasticsearch] is a distributed search and analytics engine, scalable data store, and vector database built on Apache Lucene.
It's optimized for speed and relevance on production-scale workloads.
Use Elasticsearch to search, index, store, and analyze data of all shapes and sizes in near real time.

Elasticsearch is the heart of the {estc-welcome-current}/stack-components.html[Elastic Stack]. 
Combined with [Kibana](https://www.elastic.co/kibana), it powers the following Elastic solutions:

* [Observability](https://www.elastic.co/observability)
* [Search](https://www.elastic.co/enterprise-search)
* [Security](https://www.elastic.co/security)

**Tip:**
Elasticsearch has a lot of features. Explore the full list on the [product webpage^](https://www.elastic.co/elasticsearch/features).

**What is the Elastic Stack?**
*******************************
Elasticsearch is the core component of the Elastic Stack, a suite of products for collecting, storing, searching, and visualizing data.
{estc-welcome-current}/stack-components.html[Learn more about the Elastic Stack].
*******************************

#### Use cases

Elasticsearch is used for a wide and growing range of use cases. Here are a few examples:

**Observability**

* *Logs, metrics, and traces*: Collect, store, and analyze logs, metrics, and traces from applications, systems, and services.
* *Application performance monitoring (APM)*: Monitor and analyze the performance of business-critical software applications.
* *Real user monitoring (RUM)*: Monitor, quantify, and analyze user interactions with web applications.
* *OpenTelemetry*: Reuse your existing instrumentation to send telemetry data to the Elastic Stack using the OpenTelemetry standard.

**Search**

* *Full-text search*: Build a fast, relevant full-text search solution using inverted indexes, tokenization, and text analysis.
* *Vector database*: Store and search vectorized data, and create vector embeddings with built-in and third-party natural language processing (NLP) models.
* *Semantic search*: Understand the intent and contextual meaning behind search queries using tools like synonyms, dense vector embeddings, and learned sparse query-document expansion.
* *Hybrid search*: Combine full-text search with vector search using state-of-the-art ranking algorithms.
* *Build search experiences*: Add hybrid search capabilities to apps or websites, or build enterprise search engines over your organization's internal data sources.
* *Retrieval augmented generation (RAG)*: Use Elasticsearch as a retrieval engine to supplement generative AI models with more relevant, up-to-date, or proprietary data for a range of use cases.
* *Geospatial search*: Search for locations and calculate spatial relationships using geospatial queries.

**Security**

* *Security information and event management (SIEM)*: Collect, store, and analyze security data from applications, systems, and services.
* *Endpoint security*: Monitor and analyze endpoint security data.
* *Threat hunting*: Search and analyze data to detect and respond to security threats.

This is just a sample of search, observability, and security use cases enabled by Elasticsearch.
Refer to Elastic [customer success stories](https://www.elastic.co/customers/success-stories) for concrete examples across a range of industries.

### Run Elasticsearch

To use Elasticsearch, you need a running instance of the Elasticsearch service.
You can deploy Elasticsearch in various ways.

**Quick start option**

* *Local development*: Get started quickly with a minimal local Docker setup for development and testing.

**Hosted options**

* {cloud}/ec-getting-started-trial.html[*Elastic Cloud Hosted*]: Elasticsearch is available as part of the hosted Elastic Stack offering, deployed in the cloud with your provider of choice. Sign up for a [14-day free trial](https://cloud.elastic.co/registration).
* {serverless-docs}/general/sign-up-trial[*Elastic Cloud Serverless*]: Create serverless projects for autoscaled and fully managed Elasticsearch deployments. Sign up for a [14-day free trial](https://cloud.elastic.co/serverless-registration).

**Advanced options**

* *Self-managed*: Install, configure, and run Elasticsearch on your own premises.
* {ece-ref}/Elastic-Cloud-Enterprise-overview.html[*Elastic Cloud Enterprise*]: Deploy Elastic Cloud on public or private clouds, virtual machines, or your own premises.
* {eck-ref}/k8s-overview.html[*Elastic Cloud on Kubernetes*]: Deploy Elastic Cloud on Kubernetes.

### Indices, documents, and fields

The index is the fundamental unit of storage in Elasticsearch, a logical namespace for storing data that share similar characteristics.
After you have Elasticsearch deployed, you'll get started by creating an index to store your data.

An index is a collection of documents uniquely identified by a name or an alias.
This unique name is important because it's used to target the index in search queries and other operations.

**Tip:**
A closely related concept is a data stream.
This index abstraction is optimized for append-only timestamped data, and is made up of hidden, auto-generated backing indices.
If you're working with timestamped data, we recommend the {observability-guide}[Elastic Observability] solution for additional tools and optimized content.

#### Documents and fields

Elasticsearch serializes and stores data in the form of JSON documents.
A document is a set of fields, which are key-value pairs that contain your data.
Each document has a unique ID, which you can create or have Elasticsearch auto-generate.

A simple Elasticsearch document might look like this:

```js
{
  "_index": "my-first-elasticsearch-index",
  "_id": "DyFpo5EBxE8fzbb95DOa",
  "_version": 1,
  "_seq_no": 0,
  "_primary_term": 1,
  "found": true,
  "_source": {
    "email": "john@smith.com",
    "first_name": "John",
    "last_name": "Smith",
    "info": {
      "bio": "Eco-warrior and defender of the weak",
      "age": 25,
      "interests": [
        "dolphins",
        "whales"
      ]
    },
    "join_date": "2024/05/01"
  }
}
```

#### Metadata fields

An indexed document contains data and metadata. Metadata fields are system fields that store information about the documents.
In Elasticsearch, metadata fields are prefixed with an underscore.
For example, the following fields are metadata fields:

* `_index`: The name of the index where the document is stored.
* `_id`: The document's ID. IDs must be unique per index.

#### Mappings and data types

Each index has a mapping or schema for how the fields in your documents are indexed.
A mapping defines the data type for each field, how the field should be indexed,
and how it should be stored.
When adding documents to Elasticsearch, you have two options for mappings:

* Dynamic mapping: Let Elasticsearch automatically detect the data types and create the mappings for you. Dynamic mapping helps you get started quickly, but might yield suboptimal results for your specific use case due to automatic field type inference.
* Explicit mapping: Define the mappings up front by specifying data types for each field. Recommended for production use cases, because you have full control over how your data is indexed to suit your specific use case.

**Tip:**
You can use a combination of dynamic and explicit mapping on the same index.
This is useful when you have a mix of known and unknown fields in your data.

### Add data to Elasticsearch

There are multiple ways to ingest data into Elasticsearch.
The option that you choose depends on whether you're working with timestamped data or non-timestamped data, where the data is coming from, its complexity, and more.

**Tip:**
You can load [sample data](https://www.elastic.co/guide/en/kibana/8.19/connect-to-elasticsearch.html#_add_sample_data) into your Elasticsearch cluster using Kibana, to get started quickly.

#### General content

General content is data that does not have a timestamp.
This could be data like vector embeddings, website content, product catalogs, and more.
For general content, you have the following options for adding data to Elasticsearch indices:

* API: Use the Elasticsearch Document APIs to index documents directly, using the Dev Tools [Console](https://www.elastic.co/guide/en/kibana/8.19/console-kibana.html), or cURL.
If you're building a website or app, then you can call Elasticsearch APIs using an [Elasticsearch client](https://www.elastic.co/guide/en/elasticsearch/client/index.html) in the programming language of your choice. If you use the Python client, then check out the `elasticsearch-labs` repo for various [example notebooks](https://github.com/elastic/elasticsearch-labs/tree/main/notebooks/search/python-examples). 
* [File upload](https://www.elastic.co/guide/en/kibana/8.19/connect-to-elasticsearch.html#upload-data-kibana): Use the Kibana file uploader to index single files for one-off testing and exploration. The GUI guides you through setting up your index and field mappings.
* [Web crawler](https://github.com/elastic/crawler): Extract and index web page content into Elasticsearch documents.
* Connectors: Sync data from various third-party data sources to create searchable, read-only replicas in Elasticsearch.

#### Timestamped data

Timestamped data in Elasticsearch refers to datasets that include a timestamp field. If you use the {ecs-ref}/ecs-reference.html[Elastic Common Schema (ECS)], this field is named `@timestamp`.
This could be data like logs, metrics, and traces.

For timestamped data, you have the following options for adding data to Elasticsearch data streams:

* {fleet-guide}/fleet-overview.html[Elastic Agent and Fleet]: The preferred way to index timestamped data. Each Elastic Agent based integration includes default ingestion rules, dashboards, and visualizations to start analyzing your data right away.
You can use the Fleet UI in Kibana to centrally manage Elastic Agents and their policies.
* {beats-ref}/beats-reference.html[Beats]: If your data source isn't supported by Elastic Agent, use Beats to collect and ship data to Elasticsearch. You install a separate Beat for each type of data to collect.
* {logstash-ref}/introduction.html[Logstash]: Logstash is an open source data collection engine with real-time pipelining capabilities that supports a wide variety of data sources. You might use this option because neither Elastic Agent nor Beats supports your data source. You can also use Logstash to persist incoming data, or if you need to send the data to multiple destinations. 
* {cloud}/ec-ingest-guides.html[Language clients]: The linked tutorials demonstrate how to use Elasticsearch programming language clients to ingest data from an application. In these examples, Elasticsearch is running on Elastic Cloud, but the same principles apply to any Elasticsearch deployment.

**Tip:**
If you're interested in data ingestion pipelines for timestamped data, use the decision tree in the {cloud}/ec-cloud-ingest-data.html#ec-data-ingest-pipeline[Elastic Cloud docs] to understand your options.

### Search and analyze data

You can use Elasticsearch as a basic document store to retrieve documents and their
metadata.
However, the real power of Elasticsearch comes from its advanced search and analytics capabilities.

You'll use a combination of an API endpoint and a query language to interact with your data.

#### REST API

Use REST APIs to manage your Elasticsearch cluster, and to index
and search your data.
For testing purposes, you can submit requests
directly from the command line or through the Dev Tools [Console](https://www.elastic.co/guide/en/kibana/8.19/console-kibana.html) in Kibana.
From your applications, you can use a
[client](https://www.elastic.co/guide/en/elasticsearch/client/index.html)
in your programming language of choice.

Refer to first steps with Elasticsearch for a hands-on example of using the `_search` endpoint, adding data to Elasticsearch, and running basic searches in Query DSL syntax.

#### Query languages

Elasticsearch provides a number of query languages for interacting with your data. 

*Query DSL* is the primary query language for Elasticsearch today.

*ES|QL* is a new piped query language and compute engine which was first added in version *8.11*.

ES|QL does not yet support all the features of Query DSL.
Look forward to new ES|QL features and functionalities in each release.

Refer to search-analyze-query-languages for a full overview of the query languages available in Elasticsearch.

##### Query DSL

Query DSL is a full-featured JSON-style query language that enables complex searching, filtering, and aggregations.
It is the original and most powerful query language for Elasticsearch today.

The `_search` endpoint accepts queries written in Query DSL syntax.

###### Search and filter with Query DSL

Query DSL support a wide range of search techniques, including the following:

* *Full-text search*: Search text that has been analyzed and indexed to support phrase or proximity queries, fuzzy matches, and more.
* *Keyword search*: Search for exact matches using `keyword` fields.
* *Semantic search*: Search `semantic_text` fields using dense or sparse vector search on embeddings generated in your Elasticsearch cluster.
* *Vector search*: Search for similar dense vectors using the kNN algorithm for embeddings generated outside of Elasticsearch.
* *Geospatial search*: Search for locations and calculate spatial relationships using geospatial queries.

Learn about the full range of queries supported by Query DSL. 

You can also filter data using Query DSL.
Filters enable you to include or exclude documents by retrieving documents that match specific field-level criteria.
A query that uses the `filter` parameter indicates filter context.

###### Analyze with Query DSL

Aggregations are the primary tool for analyzing Elasticsearch data using Query DSL.
Aggregrations enable you to build complex summaries of your data and gain
insight into key metrics, patterns, and trends.

Because aggregations leverage the same data structures used for search, they are
also very fast. This enables you to analyze and visualize your data in real time.
You can search documents, filter results, and perform analytics at the same time, on the same
data, in a single request.
That means aggregations are calculated in the context of the search query.

The folowing aggregation types are available:

* Metric: Calculate metrics,
such as a sum or average, from field values.
* Bucket: Group documents into buckets based on field values, ranges,
or other criteria.
* Pipeline: Run aggregations on the results of other aggregations.

Run aggregations by specifying the search API's `aggs` parameter.
Learn more in Run an aggregation.

##### ES|QL

Elasticsearch Query Language (ES|QL) is a piped query language for filtering, transforming, and analyzing data.
ES|QL is built on top of a new compute engine, where search, aggregation, and transformation functions are
directly executed within Elasticsearch itself.
ES|QL syntax can also be used within various Kibana tools.

The `_query` endpoint accepts queries written in ES|QL syntax.

Today, it supports a subset of the features available in Query DSL, but it is rapidly evolving.

It comes with a comprehensive set of functions and operators for working with data and has robust integration with Kibana's Discover, dashboards and visualizations.

Learn more in Getting started with ES|QL, or try [our training course](https://www.elastic.co/training/introduction-to-esql).

#### List of available query languages

The following table summarizes all available Elasticsearch query languages, to help you choose the right one for your use case.

|===
| Name | Description | Use cases | API endpoint

| Query DSL
| The primary query language for Elasticsearch. A powerful and flexible JSON-style language that enables complex queries.
| Full-text search, semantic search, keyword search, filtering, aggregations, and more.
| `_search`

| ES|QL
| Introduced in *8.11*, the Elasticsearch Query Language (ES|QL) is a piped query language language for filtering, transforming, and analyzing data.
| Initially tailored towards working with time series data like logs and metrics. 
Robust integration with Kibana for querying, visualizing, and analyzing data.
Does not yet support full-text search.
| `_query`

| EQL
| Event Query Language (EQL) is a query language for event-based time series data. Data must contain the `@timestamp` field to use EQL.
| Designed for the threat hunting security use case.
| `_eql`

| Elasticsearch SQL
| Allows native, real-time SQL-like querying against Elasticsearch data. JDBC and ODBC drivers are available for integration with business intelligence (BI) tools.
| Enables users familiar with SQL to query Elasticsearch data using familiar syntax for BI and reporting.
| `_sql`

| [Kibana Query Language (KQL)](https://www.elastic.co/guide/en/kibana/8.19/kuery-query.html)
| Kibana Query Language (KQL) is a text-based query language for filtering data when you access it through the Kibana UI.
| Use KQL to filter documents where a value for a field exists, matches a given value, or is within a given range.
| N/A

|===

### Get ready for production

Many teams rely on Elasticsearch to run their key services. To keep these services running, you can design your Elasticsearch deployment
to keep Elasticsearch available, even in case of large-scale outages. To keep it running fast, you also can design your
deployment to be responsive to production workloads.

Elasticsearch is built to be always available and to scale with your needs. It does this using a distributed architecture.
By distributing your cluster, you can keep Elastic online and responsive to requests.

In case of failure, Elasticsearch offers tools for cross-cluster replication and cluster snapshots that can
help you fall back or recover quickly. You can also use cross-cluster replication to serve requests based on the
geographic location of your users and your resources.

Elasticsearch also offers security and monitoring tools to help you keep your cluster highly available.

#### Use multiple nodes and shards

When you move to production, you need to introduce multiple nodes and shards to your cluster. Nodes and shards are what make Elasticsearch distributed and scalable. The size and number of these nodes and shards depends on your data, your use case, and your budget.

These concepts aren't essential if you're just getting started. How you deploy Elasticsearch in production determines what you need to know:

* *Self-managed Elasticsearch*: You are responsible for setting up and managing nodes, clusters, shards, and replicas. This includes
managing the underlying infrastructure, scaling, and ensuring high availability through failover and backup strategies.
* *Elastic Cloud*: Elastic can autoscale resources in response to workload changes. Choose from different deployment types
to apply sensible defaults for your use case. A basic understanding of nodes, shards, and replicas is still important.
* *Elastic Cloud Serverless*: You don't need to worry about nodes, shards, or replicas. These resources are 100% automated
on the serverless platform, which is designed to scale with your workload.

Learn more about nodes and shards.

#### CCR for disaster recovery and geo-proximity

To effectively distribute read and write operations across nodes, the nodes in a cluster need good, reliable connections
to each other. To provide better connections, you typically co-locate the nodes in the same data center or nearby data centers.

Co-locating nodes in a single location exposes you to the risk of a single outage taking your entire cluster offline. To
maintain high availability, you can prepare a second cluster that can take over in case of disaster by implementing
cross-cluster replication (CCR).

CCR provides a way to automatically synchronize indices from your primary cluster to a secondary remote cluster that
can serve as a hot backup. If the primary cluster fails, the secondary cluster can take over.

You can also use CCR to create secondary clusters to serve read requests in geo-proximity to your users.

Learn more about cross-cluster replication and about designing for resilience.

**Tip:**
You can also take snapshots of your cluster that can be restored in case of failure.

#### Security and monitoring

As with any enterprise system, you need tools to secure, manage, and monitor your Elasticsearch clusters. Security,
monitoring, and administrative features that are integrated into Elasticsearch enable you to use [Kibana](https://www.elastic.co/guide/en/kibana/8.19/introduction.html) as a
control center for managing a cluster.

Learn about securing an Elasticsearch cluster.

Learn about monitoring your cluster.

#### Cluster design

Elasticsearch offers many options that allow you to configure your cluster to meet your organization’s goals, requirements,
and restrictions. You can review the following guides to learn how to tune your cluster to meet your needs:

* Designing for resilience
* Tune for indexing speed
* Tune for search speed
* Tune for disk usage
* Tune for time series data

Many Elasticsearch options come with different performance considerations and trade-offs. The best way to determine the
optimal configuration for your use case is through [testing with your own data and queries](https://www.elastic.co/elasticon/conf/2016/sf/quantitative-cluster-sizing).
