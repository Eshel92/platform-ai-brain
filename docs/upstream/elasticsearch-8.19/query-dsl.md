<!-- Converted from query-dsl.asciidoc (AsciiDoc). Includes are inlined. -->

# Query DSL

Elasticsearch provides a full Query DSL (Domain Specific Language) based on JSON to define queries.
Think of the Query DSL as an AST (Abstract Syntax Tree) of queries, consisting of two types of clauses:

Leaf query clauses::

Leaf query clauses look for a particular value in a particular field, such as the
`match`, `term` or
`range` queries.
These queries can be used by themselves.

Compound query clauses::

Compound query clauses wrap other leaf *or* compound queries and are used to combine multiple queries in a logical fashion (such as the
`bool` or `dis_max` query), or to alter their behaviour (such as the
`constant_score` query).

Query clauses behave differently depending on whether they are used in
query context or filter context.

Allow expensive queries::
Certain types of queries will generally execute slowly due to the way they are implemented, which can affect the stability of the cluster.
Those queries can be categorised as follows:

* Queries that need to do linear scans to identify matches:
** `script` queries
** queries on numeric, date, boolean, ip,
geo_point or keyword fields that are not indexed but have doc values enabled

* Queries that have a high up-front cost:
** `fuzzy` queries (except on
`wildcard` fields)
** `regexp` queries (except on
`wildcard` fields)
** `prefix` queries  (except on
`wildcard` fields or those without
`index_prefixes`)
** `wildcard` queries (except on
`wildcard` fields)
** `range` queries on `text` and
`keyword` fields

* Joining queries

* Queries that may have a high per-document cost:
** `script_score` queries
** `percolate` queries

The execution of such queries can be prevented by setting the value of the `search.allow_expensive_queries`
setting to `false` (defaults to `true`).

(See `query-dsl/query_filter_context.md`)
(See `query-dsl/compound-queries.md`)
(See `query-dsl/full-text-queries.md`)
(See `query-dsl/geo-queries.md`)
(See `query-dsl/shape-queries.md`)
(See `query-dsl/joining-queries.md`)
(See `query-dsl/match-all-query.md`)
(See `query-dsl/span-queries.md`)
(See `query-dsl/vector-queries.md`)
(See `query-dsl/special-queries.md`)
(See `query-dsl/term-level-queries.md`)
(See `query-dsl/minimum-should-match.md`)
(See `query-dsl/multi-term-rewrite.md`)
(See `query-dsl/regexp-syntax.md`)
