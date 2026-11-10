<!-- Converted from query-dsl/term-level-queries.asciidoc (AsciiDoc). Includes are inlined. -->

## Term-level queries

You can use **term-level queries** to find documents based on precise values in
structured data. Examples of structured data include date ranges, IP addresses,
prices, or product IDs.

Unlike full-text queries, term-level queries do not
analyze search terms. Instead, term-level queries match the exact terms stored
in a field.

**Note:**
Term-level queries still normalize search terms for `keyword` fields with the
`normalizer` property. For more details, see `normalizer`.

### Types of term-level queries

`exists` query::
Returns documents that contain any indexed value for a field.

`fuzzy` query::
Returns documents that contain terms similar to the search term. Elasticsearch measures
similarity, or fuzziness, using a
[Levenshtein edit distance](https://en.wikipedia.org/wiki/Levenshtein_distance).

`ids` query::
Returns documents based on their document IDs. 

`prefix` query::
Returns documents that contain a specific prefix in a provided field.

`range` query::
Returns documents that contain terms within a provided range.

`regexp` query::
Returns documents that contain terms matching a
[regular expression](https://en.wikipedia.org/wiki/Regular_expression).

`term` query::
Returns documents that contain an exact term in a provided field.

`terms` query::
Returns documents that contain one or more exact terms in a provided field.

`terms_set` query::
Returns documents that contain a minimum number of exact terms in a provided
field. You can define the minimum number of matching terms using a field or
script.

`wildcard` query::
Returns documents that contain terms matching a wildcard pattern.

(See `query-dsl/exists-query.md`)
(See `query-dsl/fuzzy-query.md`)
(See `query-dsl/ids-query.md`)
(See `query-dsl/prefix-query.md`)
(See `query-dsl/range-query.md`)
(See `query-dsl/regexp-query.md`)
(See `query-dsl/term-query.md`)
(See `query-dsl/terms-query.md`)
(See `query-dsl/terms-set-query.md`)
(See `query-dsl/wildcard-query.md`)
