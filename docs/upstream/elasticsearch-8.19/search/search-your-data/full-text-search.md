<!-- Converted from search/search-your-data/full-text-search.asciidoc (AsciiDoc). Includes are inlined. -->

## Full-text search

**Hands-on introduction to full-text search**

**Tip:**
Would you prefer to jump straight into a hands-on tutorial?
Refer to our quick start full-text search tutorial.

Full-text search, also known as lexical search, is a technique for fast, efficient searching through text fields in documents.
Documents and search queries are transformed to enable returning [relevant](https://www.elastic.co/what-is/search-relevance) results instead of simply exact term matches.
Fields of type `text` are analyzed and indexed for full-text search.

Built on decades of information retrieval research, full-text search delivers reliable results that scale predictably as your data grows. Because it runs efficiently on CPUs, Elasticsearch's full-text search requires minimal computational resources compared to GPU-intensive vector operations.

You can combine full-text search with semantic search using vectors to build modern hybrid search applications. While vector search may require additional GPU resources, the full-text component remains cost-effective by leveraging existing CPU infrastructure.

### How full-text search works

The following diagram illustrates the components of full-text search.

(Figure: images/search/full-text-search-overview.svg)

At a high level, full-text search involves the following:

* *Text analysis*: Analysis consists of a pipeline of sequential transformations. Text is transformed into a format optimized for searching using techniques such as stemming, lowercasing, and stop word elimination. Elasticsearch contains a number of built-in analyzers and tokenizers, including options to analyze specific language text. You can also create custom analyzers.

**Tip:**
Refer to Test an analyzer to learn how to test an analyzer and inspect the tokens and metadata it generates.
* *Inverted index creation*: After analysis is complete, Elasticsearch builds an inverted index from the resulting tokens.
An inverted index is a data structure that maps each token to the documents that contain it.
It's made up of two key components:
** *Dictionary*: A sorted list of all unique terms in the collection of documents in your index.
** *Posting list*: For each term, a list of document IDs where the term appears, along with optional metadata like term frequency and position.
* *Relevance scoring*: Results are ranked by how relevant they are to the given query. The relevance score of each document is represented by a positive floating-point number called the `_score`. The higher the `_score`, the more relevant the document.
The default similarity algorithm Elasticsearch uses for calculating relevance scores is [Okapi BM25](https://en.wikipedia.org/wiki/Okapi_BM25), a variation of the [TF-IDF algorithm](https://en.wikipedia.org/wiki/Tf–idf). BM25 calculates relevance scores based on term frequency, document frequency, and document length.
Refer to this [technical blog post](https://www.elastic.co/blog/practical-bm25-part-2-the-bm25-algorithm-and-its-variables) for a deep dive into BM25.
* *Full-text search query*: Query text is analyzed the same way as the indexed text, and the resulting tokens are used to search the inverted index.
Query DSL supports a number of full-text queries.
As of 8.17, ES|QL also supports full-text search functions.

### Getting started

For a hands-on introduction to full-text search, refer to the full-text search tutorial.

### Learn more

Here are some resources to help you learn more about full-text search with Elasticsearch.

*Core concepts*

Learn about the core components of full-text search:

* Text fields
* Text analysis
** Tokenizers
** Analyzers

*Elasticsearch query languages*

Learn how to build full-text search queries using Elasticsearch's query languages:

* Full-text queries using Query DSL 
* Full-text search functions in ES|QL

*Advanced topics*

For a technical deep dive into Elasticsearch's BM25 implementation read this blog post: [The BM25 Algorithm and its Variables](https://www.elastic.co/blog/practical-bm25-part-2-the-bm25-algorithm-and-its-variables).

To learn how to optimize the relevance of your search results, refer to Search relevance optimizations.
