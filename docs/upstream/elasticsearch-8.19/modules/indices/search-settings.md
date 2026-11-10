<!-- Converted from modules/indices/search-settings.asciidoc (AsciiDoc). Includes are inlined. -->

### Search settings

The following expert settings can be set to manage global search and aggregation
limits.

`indices.query.bool.max_clause_count`::
deprecated:[8.0.0]
(Static, integer)
This deprecated setting has no effect.
Elasticsearch will now dynamically set the maximum number of allowed clauses in a query, using
a heuristic based on the size of the search thread pool and the size of the heap allocated to
the JVM. This limit has a minimum value of 1024 and will in most cases be larger (for example,
a node with 30Gb RAM and 48 CPUs will have a maximum clause count of around 27,000). Larger
heaps lead to higher values, and larger thread pools result in lower values.
Queries with many clauses should be avoided whenever possible. If you previously bumped this
setting to accommodate heavy queries, you might need to increase the amount of memory available
to Elasticsearch, or to reduce the size of your search thread pool so that more memory is
available to each concurrent search.
In previous versions of Lucene you could get around this limit by nesting boolean queries
within each other, but the limit is now based on the total number of leaf queries within the
query as a whole and this workaround will no longer help.

`search.max_buckets`::
(Dynamic, integer)
Maximum number of aggregation buckets allowed in
a single response. Defaults to 65,536.
Requests that attempt to return more than this limit will return an error.

`search.aggs.only_allowed_metric_scripts`::
(Dynamic, boolean)
Configures whether only explicitly allowed scripts can be used in
scripted metrics aggregations.
Defaults to `false`.
Requests using scripts not contained in either
`search.aggs.allowed_inline_metric_scripts`
or
`search.aggs.allowed_stored_metric_scripts`
will return an error.

`search.aggs.allowed_inline_metric_scripts`::
(Dynamic, list of strings)
List of inline scripts that can be used in scripted metrics aggregations when
`search.aggs.only_allowed_metric_scripts`
is set to `true`.
Defaults to an empty list.
Requests using other inline scripts will return an error.

`search.aggs.allowed_stored_metric_scripts`::
(Dynamic, list of strings)
List of ids of stored scripts that can be used in scripted metrics aggregations when
`search.aggs.only_allowed_metric_scripts`
is set to `true`.
Defaults to an empty list.
Requests using other stored scripts will return an error.

`indices.query.bool.max_nested_depth`::
(Static, integer) Maximum nested depth of queries. Defaults to `30`.
This setting limits the nesting depth of queries. Deep nesting of queries may lead to
stack overflow errors.
