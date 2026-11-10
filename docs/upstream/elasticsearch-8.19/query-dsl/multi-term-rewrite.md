<!-- Converted from query-dsl/multi-term-rewrite.asciidoc (AsciiDoc). Includes are inlined. -->

## `rewrite` parameter

**Warning:** This parameter is for expert users only. Changing the value of
this parameter can impact search performance and relevance.

Elasticsearch uses [Apache Lucene](https://lucene.apache.org/core/) internally to power
indexing and searching. In their original form, Lucene cannot execute the
following queries:

* `fuzzy`
* `prefix`
* `query_string`
* `regexp`
* `wildcard`

To execute them, Lucene changes these queries to a simpler form, such as a
`bool` query or a
[bit set](https://en.wikipedia.org/wiki/Bit_array).

The `rewrite` parameter determines:

* How Lucene calculates the relevance scores for each matching document
* Whether Lucene changes the original query to a `bool`
query or bit set
* If changed to a `bool` query, which `term` query clauses are included

### Valid values

`constant_score_blended` (Default)::
Assigns each document a relevance score equal to the `boost`
parameter.
This method maintains a <<query-dsl-bool-query, `bool`
query>> like implementation over the most costly terms while pre-processing
the less costly terms into a filter bitset.
This method can cause the generated `bool` query to exceed the clause limit in the
`indices.query.bool.max_clause_count`
setting. If the query exceeds this limit, Elasticsearch returns an error.

`constant_score` ::
Uses the `constant_score_boolean` method for fewer matching terms. Otherwise,
this method finds all matching terms in sequence and returns matching documents
using a bit set.

`constant_score_boolean`::
Assigns each document a relevance score equal to the `boost`
parameter.
This method changes the original query to a <<query-dsl-bool-query, `bool`
query>>. This `bool` query contains a `should` clause and
`term` query for each matching term.
This method can cause the final `bool` query to exceed the clause limit in the
`indices.query.bool.max_clause_count`
setting. If the query exceeds this limit, Elasticsearch returns an error.

`scoring_boolean`::
Calculates a relevance score for each matching document.
This method changes the original query to a <<query-dsl-bool-query, `bool`
query>>. This `bool` query contains a `should` clause and
`term` query for each matching term.
This method can cause the final `bool` query to exceed the clause limit in the
`indices.query.bool.max_clause_count`
setting. If the query exceeds this limit, Elasticsearch returns an error.

`top_terms_blended_freqs_N`::
Calculates a relevance score for each matching document as if all terms had the
same frequency. This frequency is the maximum frequency of all matching terms.
This method changes the original query to a <<query-dsl-bool-query, `bool`
query>>. This `bool` query contains a `should` clause and
`term` query for each matching term.
The final `bool` query only includes `term` queries for the top `N` scoring
terms.
You can use this method to avoid exceeding the clause limit in the
`indices.query.bool.max_clause_count`
setting.

`top_terms_boost_N`::
Assigns each matching document a relevance score equal to the `boost` parameter.
This method changes the original query to a <<query-dsl-bool-query, `bool`
query>>. This `bool` query contains a `should` clause and
`term` query for each matching term.
The final `bool` query only includes `term` queries for the top `N` terms.
You can use this method to avoid exceeding the clause limit in the
`indices.query.bool.max_clause_count`
setting.

`top_terms_N`::
Calculates a relevance score for each matching document.
This method changes the original query to a <<query-dsl-bool-query, `bool`
query>>. This `bool` query contains a `should` clause and
`term` query for each matching term.
The final `bool` query
only includes `term` queries for the top `N` scoring terms.
You can use this method to avoid exceeding the clause limit in the
`indices.query.bool.max_clause_count`
setting.

### Performance considerations for the `rewrite` parameter

For most uses, we recommend using the  `constant_score_blended`, `constant_score`,
`constant_score_boolean`, or `top_terms_boost_N` rewrite methods.

Other methods calculate relevance scores. These score calculations are often
expensive and do not improve query results.
