<!-- Converted from query-dsl/span-queries.asciidoc (AsciiDoc). Includes are inlined. -->

## Span queries

Span queries are low-level positional queries which provide expert control
over the order and proximity of the specified terms. These are typically used
to implement very specific queries on legal documents or patents.

It is only allowed to set boost on an outer span query. Compound span queries,
like span_near, only use the list of matching spans of inner span queries in
order to find their own spans, which they then use to produce a score. Scores
are never computed on inner span queries, which is the reason why boosts are not
allowed: they only influence the way scores are computed, not spans.

Span queries cannot be mixed with non-span queries (with the exception of the `span_multi` query).

The queries in this group are:

`span_containing` query::
Accepts a list of span queries, but only returns those spans which also match a second span query.

`span_field_masking` query::
Allows queries like `span-near` or `span-or` across different fields.

`span_first` query::
Accepts another span query whose matches must appear within the first N
positions of the field.

`span_multi` query::
Wraps a `term`, `range`,
`prefix`, `wildcard`,
`regexp`, or `fuzzy` query.

`span_near` query::
Accepts multiple span queries whose matches must be within the specified distance of each other, and possibly in the same order.

`span_not` query::
Wraps another span query, and excludes any documents which match that query.

`span_or` query::
Combines multiple span queries -- returns documents which match any of the
specified queries.

`span_term` query::

The equivalent of the `term` query but for use with
other span queries.

`span_within` query::
The result from a single span query is returned as long is its span falls
within the spans returned by a list of other span queries.

(See `query-dsl/span-containing-query.md`)
(See `query-dsl/span-field-masking-query.md`)
(See `query-dsl/span-first-query.md`)
(See `query-dsl/span-multi-term-query.md`)
(See `query-dsl/span-near-query.md`)
(See `query-dsl/span-not-query.md`)
(See `query-dsl/span-or-query.md`)
(See `query-dsl/span-term-query.md`)
(See `query-dsl/span-within-query.md`)
