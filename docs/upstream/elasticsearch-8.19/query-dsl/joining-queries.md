<!-- Converted from query-dsl/joining-queries.asciidoc (AsciiDoc). Includes are inlined. -->

## Joining queries

Performing full SQL-style joins in a distributed system like Elasticsearch is
prohibitively expensive. Instead, Elasticsearch offers two forms of join
which are designed to scale horizontally.

`nested` query::
Documents may contain fields of type `nested`. These
fields are used to index arrays of objects, where each object can be queried
(with the `nested` query) as an independent document.

`has_child` and `has_parent` queries::
A `join` field relationship can exist between
documents within a single index. The `has_child` query returns parent
documents whose child documents match the specified query, while the
`has_parent` query returns child documents whose parent document matches the
specified query.

Also see the terms-lookup mechanism in the `terms`
query, which allows you to build a `terms` query from values contained in
another document.

#### Notes

##### Allow expensive queries

Joining queries will not be executed if `search.allow_expensive_queries`
is set to false.

(See `query-dsl/nested-query.md`)
(See `query-dsl/has-child-query.md`)
(See `query-dsl/has-parent-query.md`)
(See `query-dsl/parent-id-query.md`)
