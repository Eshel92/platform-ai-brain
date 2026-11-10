<!-- Converted from query-dsl/special-queries.asciidoc (AsciiDoc). Includes are inlined. -->

## Specialized queries

This group contains queries which do not fit into the other groups:

`distance_feature` query::
A query that computes scores based on the dynamically computed distances
between the origin and documents' `date`, `date_nanos`, and `geo_point` fields.
It is able to efficiently skip non-competitive hits.

`more_like_this` query::
This query finds documents which are similar to the specified text, document,
or collection of documents.

`percolate` query::
This query finds queries that are stored as documents that match with
the specified document.

`rank_feature` query::
A query that computes scores based on the values of numeric features and is
able to efficiently skip non-competitive hits.

`script` query::
This query allows a script to act as a filter. Also see the
`function_score` query.

`script_score` query::
A query that allows to modify the score of a sub-query with a script.

`wrapper` query::
A query that accepts other queries as json or yaml string.

`pinned` query::
A query that promotes selected documents over others matching a given query.

`rule` query::
A query that supports applying query-based contextual rules, defined using the Query Rules API, to a given query.

(See `query-dsl/distance-feature-query.md`)
(See `query-dsl/mlt-query.md`)
(See `query-dsl/percolate-query.md`)
(See `query-dsl/rank-feature-query.md`)
(See `query-dsl/script-query.md`)
(See `query-dsl/script-score-query.md`)
(See `query-dsl/wrapper-query.md`)
(See `query-dsl/pinned-query.md`)
(See `query-dsl/rule-query.md`)
