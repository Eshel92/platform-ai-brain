<!-- Converted from migration/migrate_8_0/rest-api-changes.asciidoc (AsciiDoc). Includes are inlined. -->

#### REST API changes

**REST API endpoints containing `_xpack` have been removed.**
*Details* +
In 7.0, we deprecated REST endpoints that contain `_xpack` in their path. These
endpoints are now removed in 8.0. Each endpoint that was deprecated and removed
is replaced with a new endpoint that does not contain `_xpack`. As an example,
`/{index}/_xpack/graph/_explore` is replaced by `/{index}/_graph/explore`.

*Impact* +
Use the replacement REST API endpoints. Requests submitted to the `_xpack`
API endpoints will return an error.

*Compatibility* +
When [rest-api-compatibility](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/rest-api-compatibility.html) is
[requested](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/rest-api-compatibility.html), any requests that include
the`_xpack` prefix are rerouted to the corresponding URL without the `_xpack`
prefix.

**REST API endpoints containing mapping types have been removed.**
*Details* +
Mapping types have been removed. API endpoints that contain a mapping type have
also been removed. Use a typeless endpoint instead.

|====
| API   | Typed API endpoint  | Typeless API endpoint

| [Bulk](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/docs-bulk.html)
| `<target>/<type>/_bulk`
| `<target>/_bulk`

| [Count](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/search-count.html)
| `<target>/<type>/_count`
| `<target>/_count`

| [Delete](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/docs-delete.html)
| `<index>/<type>/<_id>`
| `<index>/_doc/<_id>`

| [Delete by query](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/docs-delete-by-query.html)
| `<target>/<type>/_delete_by_query`
| `<target>/_delete_by_query`

| [Explain](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/search-explain.html)
| `<index>/<type>/<_id>/_explain`
| `<index>/_explain/<_id>`

| [Get](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/docs-get.html)
| `<index>/<type>/<_id>`
| `<index>/_doc/<_id>`

|
| `<index>/<type>/<_id>/_source`
| `<index>/_source/<_id>`

| [Get field mapping](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/indices-get-field-mapping.html)
| `_mapping/<type>/field/<field>`
| `_mapping/field/<field>`

|
| `<target>/_mapping/<type>/field/<field>`
| `<target>/_mapping/field/<field>`

| [Get mapping](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/indices-get-mapping.html)
| `_mapping/<type>`
| `_mapping` or `<target>/_mapping`

|
| `<target>/<type>/_mapping`
| `<target>/_mapping`

|
| `<target>/_mapping/<type>`
| `<target>/_mapping`

| [Graph explore](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/graph-explore-api.html)
| `<index>/<type>/_graph/explore`
| `<index>/_graph/explore`

| [Index](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/docs-index_.html)
| `<target>/<type>/<_id>/_create`
| `<target>/_create/<_id>`

|
| `<target>/<type>`
| `<target>/_doc`

|
| `<target>/<type>/<_id>`
| `<target>/_doc/<_id>`

| [Multi get](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/docs-multi-get.html)
| `<index>/<type>/_mget`
| `<index>/_mget`

| [Multi search](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/search-multi-search.html)
| `<target>/<type>/_msearch`
| `<target>/_msearch`

| [Multi search template](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/multi-search-template.html)
| `<target>/<type>/_msearch/template`
| `<target>/_msearch/template`

| [Multi term vectors](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/docs-multi-termvectors.html)
| `<index>/<type>/_mtermvectors`
| `<index>/_mtermvectors`

| [Rollup search](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/rollup-search.html)
| `<target>/<type>/_rollup_search`
| `<target>/_rollup_search`

| [Search](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/search-search.html)
| `<target>/<type>/_search`
| `<target>/_search`

| [Search template](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/search-template-api.html)
| `<target>/<type>/_search/template`
| `<target>/_search/template`

| [Term vectors](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/docs-termvectors.html)
| `<index>/<mapping_type>/<_id>/_termvectors`
| `<index>/_termvectors<_id>`

|
| `<index>/<mapping_type>/_termvectors`
| `<index>/_termvectors`

| [Update](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/docs-update.html)
| `<index>/<type>/<_id>/_update`
| `<index>/_update/<_id>`

| [Update by query](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/docs-update-by-query.html)
| `<target>/<type>/_update_by_query`
| `<target>/_update_by_query`

| [Update mapping](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/indices-put-mapping.html)
| `<target>/<type>/_mapping`
| `<target>/_mapping`

|
| `<target>/_mapping/<type>`
| `<target>/_mapping`

|
| `_mapping/<type>`
| `<target>/_mapping`

| [Validate](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/search-validate.html)
| `<target>/<type>/_validate/query`
| `<target>/_validate/query`

|====

*Impact* +
Update your application to use typeless REST API endpoints. Requests to
endpoints that contain a mapping type will return an error.

*Compatibility* +
When [rest-api-compatibility](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/rest-api-compatibility.html) is
[requested](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/rest-api-compatibility.html), if a request includes a custom
mapping type it is ignored. The request is rerouted to the corresponding
typeless URL. Custom mapping types in request bodies and type related HTTP
parameters are ignored, and responses, where warranted, include `_type` :
`_doc`.

.Cross-cluster search (CCS) is now only backward-compatible with the previous minor version.
*Details* +
In 8.0+, Elastic supports searches from a local cluster to a remote cluster
running:

* The previous minor version.
* The same version.
* A newer minor version in the same major version.

Elastic also supports searches from a local cluster running the last minor
version of a major version to a remote cluster running any minor version in the
following major version. For example, a local 7.17 cluster can search any
remote 8.x cluster.

|====
| 24+^h| Remote cluster version
h| Local cluster version
            |  6.8        | 7.1–7.16   | 7.17       | 8.0        | 8.1        | 8.2        | 8.3       | 8.4       | 8.5       | 8.6        | 8.7        | 8.8        | 8.9        | 8.10       | 8.11       | 8.12       | 8.13       | 8.14       | 8.15       | 8.16        | 8.17        | 8.18        | 8.19        |      
| 6.8       |  ✓ | ✓ | ✓ | ✗  | ✗  | ✗  | ✗ | ✗ | ✗ | ✗  | ✗  | ✗  | ✗  | ✗  | ✗  | ✗  | ✗  | ✗  | ✗  | ✗   | ✗   | ✗   | ✗   |
| 7.1–7.16  |  ✓ | ✓ | ✓ | ✗  | ✗  | ✗  | ✗ | ✗ | ✗ | ✗  | ✗  | ✗  | ✗  | ✗  | ✗  | ✗  | ✗  | ✗  | ✗  | ✗   | ✗   | ✗   | ✗   |
| 7.17      |  ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓| ✓| ✓| ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓  | ✓  | ✓  | ✓  |
| 8.0       |  ✗  | ✗  | ✓ | ✓ | ✓ | ✓ | ✓| ✓| ✓| ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓  | ✓  | ✓  | ✓  |
| 8.1       |  ✗  | ✗  | ✗  | ✓ | ✓ | ✓ | ✓| ✓| ✓| ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓  | ✓  | ✓  | ✓  |
| 8.2       |  ✗  | ✗  | ✗  | ✗  | ✓ | ✓ | ✓| ✓| ✓| ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓  | ✓  | ✓  | ✓  |
| 8.3       |  ✗  | ✗  | ✗  | ✗  | ✗  | ✓ | ✓| ✓| ✓| ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓  | ✓  | ✓  | ✓  |
| 8.4       |  ✗  | ✗  | ✗  | ✗  | ✗  | ✗  | ✓| ✓| ✓| ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓  | ✓  | ✓  | ✓  |
| 8.5       |  ✗  | ✗  | ✗  | ✗  | ✗  | ✗  | ✗ | ✓| ✓| ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓  | ✓  | ✓  | ✓  |
| 8.6       |  ✗  | ✗  | ✗  | ✗  | ✗  | ✗  | ✗ | ✗ | ✓| ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓  | ✓  | ✓  | ✓  |
| 8.7       |  ✗  | ✗  | ✗  | ✗  | ✗  | ✗  | ✗ | ✗ | ✗ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓  | ✓  | ✓  | ✓  |
| 8.8       |  ✗  | ✗  | ✗  | ✗  | ✗  | ✗  | ✗ | ✗ | ✗ | ✗  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓  | ✓  | ✓  | ✓  |
| 8.9       |  ✗  | ✗  | ✗  | ✗  | ✗  | ✗  | ✗ | ✗ | ✗ | ✗  | ✗  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓  | ✓  | ✓  | ✓  |
| 8.10      |  ✗  | ✗  | ✗  | ✗  | ✗  | ✗  | ✗ | ✗ | ✗ | ✗  | ✗  | ✗  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓  | ✓  | ✓  | ✓  |
| 8.11      |  ✗  | ✗  | ✗  | ✗  | ✗  | ✗  | ✗ | ✗ | ✗ | ✗  | ✗  | ✗  | ✗  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓  | ✓  | ✓  | ✓  |
| 8.12      |  ✗  | ✗  | ✗  | ✗  | ✗  | ✗  | ✗ | ✗ | ✗ | ✗  | ✗  | ✗  | ✗  | ✗  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓  | ✓  | ✓  | ✓  |
| 8.13      |  ✗  | ✗  | ✗  | ✗  | ✗  | ✗  | ✗ | ✗ | ✗ | ✗  | ✗  | ✗  | ✗  | ✗  | ✗  | ✓ | ✓ | ✓ | ✓ | ✓  | ✓  | ✓  | ✓  |
| 8.14      |  ✗  | ✗  | ✗  | ✗  | ✗  | ✗  | ✗ | ✗ | ✗ | ✗  | ✗  | ✗  | ✗  | ✗  | ✗  | ✗  | ✓ | ✓ | ✓ | ✓  | ✓  | ✓  | ✓  |
| 8.15      |  ✗  | ✗  | ✗  | ✗  | ✗  | ✗  | ✗ | ✗ | ✗ | ✗  | ✗  | ✗  | ✗  | ✗  | ✗  | ✗  | ✗  | ✓ | ✓ | ✓  | ✓  | ✓  | ✓  |
| 8.16      |  ✗  | ✗  | ✗  | ✗  | ✗  | ✗  | ✗ | ✗ | ✗ | ✗  | ✗  | ✗  | ✗  | ✗  | ✗  | ✗  | ✗  | ✗  | ✓ | ✓  | ✓  | ✓  | ✓  |
| 8.17      |  ✗  | ✗  | ✗  | ✗  | ✗  | ✗  | ✗ | ✗ | ✗ | ✗  | ✗  | ✗  | ✗  | ✗  | ✗  | ✗  | ✗  | ✗  | ✗  | ✓  | ✓  | ✓  | ✓  |
| 8.18      |  ✗  | ✗  | ✗  | ✗  | ✗  | ✗  | ✗ | ✗ | ✗ | ✗  | ✗  | ✗  | ✗  | ✗  | ✗  | ✗  | ✗  | ✗  | ✗  | ✗   | ✓  | ✓  | ✓  |
| 8.19      |  ✗  | ✗  | ✗  | ✗  | ✗  | ✗  | ✗ | ✗ | ✗ | ✗  | ✗  | ✗  | ✗  | ✗  | ✗  | ✗  | ✗  | ✗  | ✗  | ✗   | ✗  | ✓  | ✓  |
|====

**Important:** For the [EQL search API](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/eql-search-api.html), the local and
remote clusters must use the same Elasticsearch version if they have versions prior to 7.17.7 (included) or prior to 8.5.1 (included).

For example, a local 8.0 cluster can search a remote 7.17 or any remote 8.x
cluster. However, a search from a local 8.0 cluster to a remote 7.16 or 6.8
cluster is not supported.

Previously, we also supported searches on remote clusters running:

* Any minor version of the local cluster's major version.
* The last minor release of the previous major version.

However, such searches can result in undefined behavior.

*Impact* +
If you only run cross-cluster searches on remote clusters using the same or a
newer version, no changes are needed.

If you previously searched remote clusters running an earlier version of Elasticsearch,
see https://www.elastic.co/guide/en/elasticsearch/reference/8.19/modules-cross-cluster-search.html#ensure-ccs-support[Ensure cross-cluster search
support] for recommended solutions.

A cross-cluster search using an unsupported configuration may still work. However, such
searches aren't tested by Elastic, and their behavior isn't guaranteed.

**The `terms` aggregation no longer supports the `_term` order key.**
*Details* +
The `terms` aggregation no longer supports the `_term` key in `order` values. To
sort buckets by their term, use `_key` instead.

*Impact* +
Discontinue use of the `_term` order key. Requests that include a `_term` order
key will return an error.

*Compatibility* +
When [rest-api-compatibility](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/rest-api-compatibility.html) is
[requested](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/rest-api-compatibility.html), the `_term` order is ignored and
`key` is used instead.

**The `date_histogram` aggregation no longer supports the `_time` order key.**
*Details* +
The `date_histogram` aggregation no longer supports the `_time` key in `order`
values. To sort buckets by their key, use `_key` instead.

*Impact* +
Discontinue use of the `_time` order key. Requests that include a `_time` order
key will return an error.

*Compatibility* +
When [rest-api-compatibility](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/rest-api-compatibility.html) is
[requested](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/rest-api-compatibility.html), the `_time` order is ignored and
`_key` is used instead.

**The `moving_avg` aggregation has been removed.**
*Details* +
The `moving_avg` aggregation was deprecated in 6.4 and has been removed. To
calculate moving averages, use the
https://www.elastic.co/guide/en/elasticsearch/reference/8.19/search-aggregations-pipeline-movfn-aggregation.html[`moving_fn`
aggregation] instead.

*Impact* +
Discontinue use of the `moving_avg` aggregation. Requests that include the
`moving_avg` aggregation will return an error.

**The `percentiles` aggregation's `percents` parameter no longer supports duplicate values.**
*Details* +
If you specify the `percents` parameter with the
[`percentiles` aggregation](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/search-aggregations-metrics-percentile-aggregation.html),
its values must be unique. Otherwise, an exception occurs.

*Impact* +
Use unique values in the `percents` parameter of the `percentiles` aggregation.
Requests containing duplicate values in the `percents` parameter will return
an error.

**The `date_histogram` aggregation's `interval` parameter is no longer valid.**
*Details* +
It is now an error to specify the `interval` parameter to the
https://www.elastic.co/guide/en/elasticsearch/reference/8.19/search-aggregations-bucket-datehistogram-aggregation.html[`date_histogram`
aggregation] or the
https://www.elastic.co/guide/en/elasticsearch/reference/8.19/search-aggregations-bucket-composite-aggregation.html#_date_histogram[`composite
date_histogram` source.  Instead, please use either `calendar_interval` or
`fixed_interval` as appropriate.

*Impact* +
Uses of the `interval` parameter in either the `date_histogram` aggregation or
the `date_histogram` composite source will now generate an error.  Instead
please use the more specific `fixed_interval` or `calendar_interval`
parameters.

*Compatibility* +
When [rest-api-compatibility](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/rest-api-compatibility.html) is
[requested](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/rest-api-compatibility.html), the `interval` parameter is
adapted to either a fixed or calendar interval.

**The `nGram` and `edgeNGram` token filter names have been removed.**
*Details* +
The `nGram` and `edgeNGram` token filter names that have been deprecated since
version 6.4 have been removed. Both token filters can only be used by their
alternative names `ngram` and `edge_ngram` since version 7.0.

*Impact* +
Use the equivalent `ngram` and `edge_ngram` token filters. Requests containing
the `nGram` and `edgeNGram` token filter names will return an error.

**The `nGram` and `edgeNGram` tokenizer names have been removed.**
*Details* +
The `nGram` and `edgeNGram` tokenizer names haven been deprecated with 7.6 and are no longer
supported on new indices. Mappings for indices created after 7.6 will continue to work but
emit a deprecation warning. The tokenizer name should be changed to the fully equivalent
`ngram` or `edge_ngram` names for new indices and in index templates.

*Impact* +
Use the `ngram` and `edge_ngram` tokenizers. Requests to create new indices
using the `nGram` and `edgeNGram` tokenizer names will return an error.

**The `in_flight_requests` stat has been renamed `inflight_requests` in logs and diagnostic APIs.**
*Details* +
The name of the in flight requests circuit breaker in log output and diagnostic APIs (such as the node stats API) changes from `in_flight_requests` to `inflight_requests` to align it with the name of the corresponding settings.

*Impact* +
Update your workflow and applications to use the `inflight_requests` stat in
place of `in_flight_requests`.

**The voting configuration exclusions API endpoint has changed.**
*Details* +
The `POST /_cluster/voting_config_exclusions/{node_filter}` API has been
removed in favour of `POST /_cluster/voting_config_exclusions?node_names=...`
and `POST /_cluster/voting_config_exclusions?node_ids=...` which allow you to
specify the names or IDs of the nodes to exclude.

*Impact* +
Use `POST /_cluster/voting_config_exclusions?node_ids=...` and specify the nodes
to exclude instead of using a node filter. Requests submitted to the
`/_cluster/voting_config_exclusions/{node_filter}` endpoint will return an
error.

**Remote system indices are not followed automatically if they match an auto-follow pattern.**
*Details* +
Remote system indices matching an https://www.elastic.co/guide/en/elasticsearch/reference/8.19/ccr-auto-follow.html[auto-follow
pattern] won't be configured as a follower index automatically.

*Impact* +
Explicitly [create a follower index](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/ccr-put-follow.html) to follow a remote
system index if that's the wanted behaviour.

**The EQL `wildcard` function has been removed.**
*Details* +
The `wildcard` function was deprecated in Elasticsearch 7.13.0 and has been removed.

*Impact* +
Use the `like` or `regex` [keywords](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/eql-syntax.html#eql-syntax-pattern-comparison-keywords) instead.

**The ILM `freeze` action is now a no-op.**
*Details* +
The ILM freeze action is now a no-op and performs no action on the index, as the freeze API endpoint
has been removed in 8.0.

*Impact* +
Update your ILM policies to remove the `freeze` action from the `cold` phase.

**Additional validation for ILM policies.**
*Details* +
Creating or updating an ILM policy now requires that any referenced snapshot repositories and SLM
policies exist.

*Impact* +
Update your code or configuration management to ensure that repositories and SLM policies are created
before any policies that reference them.

**The deprecated `_upgrade` API has been removed.**
*Details* +
Previously, the `_upgrade` API upgraded indices from the previous major
version to the current version. The `_reindex` API should be used
instead for that purpose.

*Impact* +
Requests made to the old `_upgrade` API will return an error.

**The deprecated freeze index API has been removed.**
*Details* +
The freeze index API (`POST /<index>/_freeze`) has been removed.
https://www.elastic.co/blog/significantly-decrease-your-elasticsearch-heap-memory-usage[Improvements
in heap memory usage] have eliminated the reason to freeze indices.
You can still unfreeze existing frozen indices using the
[unfreeze index API](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/unfreeze-index-api.html). For some use cases, the
frozen tier may be a suitable replacement for frozen indices. See
[data tiers](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/data-tiers.html) for more information.

*Impact* +
Requests made to the old freeze index API will return an error.

**The force merge API's `max_num_segments` and `only_expunge_deletes` parameters cannot both be specified in the same request.**
*Details* +
Previously, the force merge API allowed the parameters `only_expunge_deletes`
and `max_num_segments` to be set to a non default value at the same time. But
the `max_num_segments` was silently ignored when `only_expunge_deletes` is set
to `true`, leaving the false impression that it has been applied.

*Impact* +
When using the [force merge API](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/indices-forcemerge.html), do not specify
values for both the `max_num_segments` and `only_expunge_deletes` parameters.
Requests that include values for both parameters will return an error.

**The create or update index template API's `template` parameter has been removed.**
*Details* +
In 6.0, we deprecated the `template` parameter in create or update index
template requests in favor of using `index_patterns`. Support for the `template`
parameter is now removed in 8.0.

*Impact* +
Use the [create or update index template API](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/indices-templates-v1.html)'s
`index_patterns` parameter. Requests that include the `template` parameter will
return an error.

*Compatibility* +
When [rest-api-compatibility](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/rest-api-compatibility.html) is
[requested](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/rest-api-compatibility.html), the `template` parameter is mapped
to `index_patterns`.

**Synced flush has been removed.**
*Details* +
Synced flush was deprecated in 7.6 and is removed in 8.0. Use a regular flush
instead as it has the same effect as a synced flush in 7.6 and later.

*Impact* +
Use the [flush API](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/indices-flush.html). Requests to the
`/<index>/flush/synced` or `/flush/synced` endpoints will return an error.

*Compatibility* +
When [rest-api-compatibility](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/rest-api-compatibility.html) is
[requested](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/rest-api-compatibility.html), the request to synced flush is
routed to the equivalent non-synced flush URL.

**The default for the `?wait_for_active_shards` parameter on the close index API has changed.**
*Details* +
When closing an index in earlier versions, by default Elasticsearch would not wait for
the shards of the closed index to be properly assigned before returning. From
version 8.0 onwards the default behaviour is to wait for shards to be assigned
according to the
https://www.elastic.co/guide/en/elasticsearch/reference/8.19/docs-index_.html#index-wait-for-active-shards[`index.write.wait_for_active_shards`
index setting].

*Impact* +
Accept the new behaviour, or specify `?wait_for_active_shards=0` to preserve
the old behaviour if needed.

**The index stats API's `types` query parameter has been removed.**
*Details* +
The index stats API's `types` query parameter has been removed. Previously, you
could combine `types` with the `indexing` query parameter to return indexing
stats for specific mapping types. Mapping types have been removed in 8.0.

*Impact* +
Discontinue use of the `types` query parameter. Requests that include the
parameter will return an error.

*Compatibility* +
When [rest-api-compatibility](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/rest-api-compatibility.html) is
[requested](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/rest-api-compatibility.html), the `types` query parameter is
ignored and stats are returned for the entire index.

**The `user_agent` ingest processor's `ecs` parameter has no effect.**
*Details* +
In 7.2, we deprecated the `ecs` parameter for the `user_agent` ingest processor.
In 8.x, the `user_agent` ingest processor will only return {ecs-ref}[Elastic
Common Schema (ECS)] fields, regardless of the `ecs` value.

*Impact* +
To avoid deprecation warnings, remove the parameter from your ingest pipelines.
If a pipeline specifies an `ecs` value, the value is ignored.

**The `include_type_name` query parameter has been removed.**
*Details* +
The `include_type_name` query parameter has been removed from the index
creation, index template, and mapping APIs. Previously, you could set
`include_type_name` to `true` to indicate that requests and responses should
include a mapping type name. Mapping types have been removed in 8.x.

*Impact* +
Discontinue use of the `include_type_name` query parameter. Requests that
include the parameter will return an error.

*Compatibility* +
When [rest-api-compatibility](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/rest-api-compatibility.html) is
[requested](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/rest-api-compatibility.html), the `include_type_name` query
parameter is ignored and any custom mapping types in the request are removed.

**Reindex from remote now re-encodes URL-encoded index names.**
*Details* +
Reindex from remote would previously allow URL-encoded index names and not
re-encode them when generating the search request for the remote host. This
leniency has been removed such that all index names are correctly encoded when
reindex generates remote search requests.

*Impact* +
Specify unencoded index names for reindex from remote requests.

**In the reindex, delete by query, and update by query APIs, the `size` parameter has been renamed.**
*Details* +
Previously, a `_reindex` request had two different size specifications in the body:

- Outer level, determining the maximum number of documents to process
- Inside the `source` element, determining the scroll/batch size.

The outer level `size` parameter has now been renamed to `max_docs` to
avoid confusion and clarify its semantics.

Similarly, the `size` parameter has been renamed to `max_docs` for
`_delete_by_query` and `_update_by_query` to keep the 3 interfaces consistent.

*Impact* +
Use the replacement parameters. Requests containing the `size` parameter will
return an error.

*Compatibility* +
When [rest-api-compatibility](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/rest-api-compatibility.html) is
[requested](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/rest-api-compatibility.html), the `size` parameter is mapped to
the `max_docs` parameter.

**The update by query API now rejects unsupported `script` fields.**
*Details* +
An update by query API request that includes an unsupported field in the
`script` object now returns an error. Previously, the API would silently ignore
these unsupported fields.

*Impact* +
To avoid errors, remove unsupported fields from the `script` object.

**The cat node API's `local` query parameter has been removed.**
*Details* +
The `?local` parameter to the `GET _cat/nodes` API was deprecated in 7.x and is
rejected in 8.0. This parameter caused the API to use the local cluster state
to determine the nodes returned by the API rather than the cluster state from
the master, but this API requests information from each selected node
regardless of the `?local` parameter which means this API does not run in a
fully node-local fashion.

*Impact* +
Discontinue use of the `?local` query parameter. https://www.elastic.co/guide/en/elasticsearch/reference/8.19/cat-nodes.html[cat node
API] requests that include this parameter will return an error.

**The cat shard API's `local` query parameter has been removed.**
*Details* +
The `?local` parameter to the `GET _cat/shards` API was deprecated in 7.x and is
rejected in 8.0. This parameter caused the API to use the local cluster state
to determine the nodes returned by the API rather than the cluster state from
the master, but this API requests information from each selected node
regardless of the `?local` parameter which means this API does not run in a
fully node-local fashion.

*Impact* +
Discontinue use of the `?local` query parameter. https://www.elastic.co/guide/en/elasticsearch/reference/8.19/cat-shards.html[cat shards
API] requests that include this parameter will return an error.

**The cat indices API's `local` query parameter has been removed.**
*Details* +
The `?local` parameter to the `GET _cat/indices` API was deprecated in 7.x and is
rejected in 8.0. This parameter caused the API to use the local cluster state
to determine the nodes returned by the API rather than the cluster state from
the master, but this API requests information from each selected node
regardless of the `?local` parameter which means this API does not run in a
fully node-local fashion.

*Impact* +
Discontinue use of the `?local` query parameter. https://www.elastic.co/guide/en/elasticsearch/reference/8.19/cat-indices.html[cat indices
API] requests that include this parameter will return an error.

**The get field mapping API's `local` query parameter has been removed.**
*Details* +
The `local` parameter for get field mapping API was deprecated in 7.8 and is
removed in 8.0. This parameter is a no-op and field mappings are always retrieved
locally.

*Impact* +
Discontinue use of the `local` query parameter.
[get field mapping API](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/indices-get-field-mapping.html) requests that
include this parameter will return an error.

**Post data to jobs API is deprecated.**
*Details* +
The machine learning [post data to jobs API](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/ml-post-data.html) is deprecated starting in 7.11.0
and will be removed in a future major version.

*Impact* +
Use [datafeeds](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/ml-ad-apis.html#ml-api-datafeed-endpoint) instead.

**The `job_id` property of the Update datafeeds API has been removed.**
*Details* +
The ability to update a `job_id` in a datafeed was deprecated in 7.3.0. and is
removed in 8.0.

*Impact* +
It is not possible to move datafeeds between anomaly detection jobs.

**Create repository and delete repository API's return `409` status code when a repository is in use instead of `500`.**
*Details* +
The [Create or update snapshot repository API](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/put-snapshot-repo-api.html) and
[Delete snapshot repository API](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/delete-snapshot-repo-api.html) return `409`
status code when the request is attempting to modify an existing repository that's in use instead of status code `500`.

*Impact* +
Update client code that handles creation and deletion of repositories to reflect this change.

**The `allow_no_datafeeds` property has been removed from machine learning APIs.**
*Details* +
The `allow_no_datafeeds` property was deprecated in the
[cat datafeeds](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/cat-datafeeds.html),
[get datafeeds](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/ml-get-datafeed.html),
[get datafeed statistics](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/ml-get-datafeed-stats.html), and
[stop datafeeds](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/ml-stop-datafeed.html) APIs in 7.10.0.

*Impact* +
Use `allow_no_match` instead.

**The `allow_no_jobs` property has been removed from machine learning APIs.**
*Details* +
The `allow_no_jobs` property was deprecated in the
[cat anomaly detectors](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/cat-anomaly-detectors.html),
[close anomaly detection jobs](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/ml-close-job.html),
[get anomaly detection jobs](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/ml-get-job.html),
[get anomaly detection job statistics](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/ml-get-job-stats.html), and
[get overall buckets](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/ml-get-overall-buckets.html) APIs in 7.10.0.

*Impact* +
Use `allow_no_match` instead.

**The StartRollupJob endpoint now returns a success status if a job has already started.**
*Details* +
Previously, attempting to start an already-started rollup job would
result in a `500 InternalServerError: Cannot start task for Rollup Job
[job] because state was [STARTED]` exception.

Now, attempting to start a job that is already started will just
return a successful `200 OK: started` response.

*Impact* +
Update your workflow and applications to assume that a 200 status in response to
attempting to start a rollup job means the job is in an actively started state.
The request itself may have started the job, or it was previously running and so
the request had no effect.

**Stored scripts no longer support empty scripts or search templates.**
*Details* +
The [create or update stored script API](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/create-stored-script-api.html)'s
`source` parameter cannot be empty.

*Impact* +
Before upgrading, use the https://www.elastic.co/guide/en/elasticsearch/reference/8.19/delete-stored-script-api.html[delete stored
script API] to delete any empty stored scripts or search templates.
In 8.0, Elasticsearch will drop any empty stored scripts or empty search templates from
the cluster state. Requests to create a stored script or search template with
an empty `source` will return an error.

**The create or update stored script API's `code` parameter has been removed.**
*Details* +
The [create or update stored script API](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/create-stored-script-api.html)'s
`code` parameter has been removed. Use the `source` parameter instead.

*Impact* +
Discontinue use of the `code` parameter. Requests that include the parameter
will return an error.

**Searches on the `_type` field are no longer supported.**
*Details* +
In 8.x, the `_type` metadata field has been removed. Elasticsearch now handles a search
on the `_type` field as a search on a non-existent field. A search on a
non-existent field matches no documents, regardless of the query string.

In 7.x, a search for `_doc` in the `_type` field would match the same documents
as a `match_all` query.

*Impact* +
Remove queries on the `_type` field from your search requests and search
templates. Searches that include these queries may return no results.

**The multi search API now parses an empty first line as action metadata in text files.**
*Details* +
The multi search API now parses an empty first line as empty action metadata
when you provide a text file as the request body, such as when using curl's
`--data-binary` flag.

The API no longer supports text files that contain:

* An empty first line followed by a line containing only `{}`.
* An empty first line followed by another empty line.

*Impact* +
Don't provide an unsupported text file to the multi search API. Requests that
include an unsupported file will return an error.

**The `unmapped_type: string` sort option has been removed.**
*Details* +
Search requests no longer support the `unmapped_type: string` sort option.
Instead, use `unmapped_type: keyword` to handle an unmapped field as if it had
the `keyword` field type but ignore its values for sorting.

*Impact* +
Discontinue use of `unmapped_type: string`. Search requests that include the
`unmapped_type: string` sort option will return shard failures.

**Aggregating and sorting on `_id` is disallowed by default.**
*Details* +
Previously, it was possible to aggregate and sort on the built-in `_id` field
by loading an expensive data structure called fielddata. This was deprecated
in 7.6 and is now disallowed by default in 8.0.

*Impact* +
Aggregating and sorting on `_id` should be avoided. As an alternative, the
`_id` field's contents can be duplicated into another field with docvalues
enabled (note that this does not apply to auto-generated IDs).

**The `common` query has been removed.**
*Details* +
The `common` query, deprecated in 7.x, has been removed in 8.0.
The same functionality can be achieved by the `match` query if the total number of hits is not tracked.

*Impact* +
Discontinue use of the `common` query. Search requests containing a `common`
query will return an error.

**The `cutoff_frequency` parameter has been removed from the `match` and `multi_match` query.**
*Details* +
The `cutoff_frequency` parameter, deprecated in 7.x, has been removed in 8.0 from `match` and `multi_match` queries.
The same functionality can be achieved without any configuration provided that the total number of hits is not tracked.

*Impact* +
Discontinue use of the `cutoff_frequency` parameter. Search requests containing
this parameter in a `match` or `multi_match` query will return an error.

**The `nested_filter` and `nested_path` properties have been removed from the search API's `sort` request body parameter.**
*Details* +
The `nested_filter` and `nested_path` options, deprecated in 6.x, have been removed in favor of the `nested` context.

*Impact* +
Discontinue use of the `sort` request body parameter's `nested_filter` and
`nested_path` properties. Requests containing these properties will return an
error.

**Search and get requests are now routed to shards using adaptive replica selection by default.**
*Details* +
Elasticsearch will no longer prefer using shards in the same location (with the same awareness attribute values) to process
`_search` and `_get` requests. Adaptive replica selection (activated by default in this version) will route requests
more efficiently using the service time of prior inter-node communications.

*Impact* +
No action needed.

**Vector functions using `(query, doc['field'])` are no longer supported.**
*Details* +
The vector functions of the form `function(query, doc['field'])` were
deprecated in 7.6, and are now removed in 8.x. The form
`function(query, 'field')` should be used instead. For example,
`cosineSimilarity(query, doc['field'])` is replaced by
`cosineSimilarity(query, 'field')`.

*Impact* +
Use the `function(query, 'field')` form. Discontinue use of the `function(query,
doc['field'])` form. Requests containing the `function(query,
doc['field'])` form will return an error.

**The search API's `indices_boost` request body parameter no longer accepts object values.**
*Details* +
The `indices_boost` option in the search request used to accept the boosts
both as an object and as an array. The object format has been deprecated since
5.2 and is now removed in 8.0.

*Impact* +
Use only array values in the `indices_boost` parameter. Requests containing an
object value in the `indices_boost` parameter will return an error.

**The search API's `use_field_mapping` request body parameter has been removed.**
*Details* +
In 7.0, we began formatting `docvalue_fields` by default using each field's
mapping definition. To ease the transition from 6.x, we added the format
option `use_field_mapping`. This parameter was deprecated in 7.0, and is now
removed in 8.0.

*Impact* +
Discontinue use of the `use_field_mapping` request body parameter. Requests
containing this parameter will return an error.

*Compatibility* +
When [rest-api-compatibility](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/rest-api-compatibility.html) is
[requested](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/rest-api-compatibility.html), the `use_field_mapping` parameter
is ignored.

**The search API's `from` request body and url parameter cannot be negative.**
*Details* +
Search request used to accept `-1` as a `from` in the search body and the url,
treating it as the default value of 0. Other negative values got rejected with
an error already. We now also reject `-1` as an invalid value.

*Impact* +
Change any use of `-1` as `from` parameter in request body or url parameters by either
setting it to `0` or omitting it entirely. Requests containing negative values will
return an error.

**Range queries on date fields treat numeric values alwas as milliseconds-since-epoch.**
*Details* +
Range queries on date fields used to misinterpret small numbers (e.g. four digits like 1000)
as a year when no additional format was set, but would interpret other numeric values as
milliseconds since epoch. We now treat all numeric values in absence of a specific `format`
parameter as milliseconds since epoch. If you want to query for years instead, with a missing
`format` you now need to quote the input value (e.g. "1984").

*Impact* +
If you query date fields without a specified `format`, check if the values in your queries are
actually meant to be milliseconds-since-epoch and use a numeric value in this case. If not, use
a string value which gets parsed by either the date format set on the field in the mappings or
by `strict_date_optional_time` by default.

**The `geo_bounding_box` query's `type` parameter has been removed.**
*Details* +
The `geo_bounding_box` query's `type` parameter was deprecated in 7.14.0 and has
been removed in 8.0.0. This parameter is a no-op and has no effect on the query.

*Impact* +
Discontinue use of the `type` parameter. `geo_bounding_box` queries that include
this parameter will return an error.

**The `type` query has been removed.**
*Details* +
The `type` query has been removed. Mapping types have been removed in 8.0.

*Impact* +
Discontinue use of the `type` query. Requests that include the `type` query
will return an error.

**The `kibana_user` role has been renamed `kibana_admin`.**
*Details* +
Users who were previously assigned the `kibana_user` role should instead be assigned
the `kibana_admin` role. This role grants the same set of privileges as `kibana_user`, but has been
renamed to better reflect its intended use.

*Impact* +
Assign users with the `kibana_user` role to the `kibana_admin` role.
Discontinue use of the `kibana_user` role.

**For snapshot and SLM APIs, the `indices` parameter no longer resolves to system indices or system data streams.**
*Details* +
For snapshot and SLM APIs, the `indices` parameter no longer resolves to
system indices or system data streams.
[Feature states](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/snapshot-restore.html#feature-state) are now the only way
to back up and restore system indices or system data streams from a snapshot.

You can no longer use the `indices` parameter for the
[create SLM policy API](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/slm-api-put-policy.html) or the
[create snapshot API](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/create-snapshot-api.html) to include a system index in
a snapshot. To back up a system index, use the `include_global_state` and
`feature_states` parameters to include the corresponding feature state instead.
By default, the `include_global_state` and `feature_states` parameters include
all system indices.

Similarly, you can no longer use the https://www.elastic.co/guide/en/elasticsearch/reference/8.19/restore-snapshot-api.html[restore snapshot
API]'s `indices` parameter to restore a system index from a snapshot. To restore
a system index, use the `include_global_state` and `feature_states` parameters
to restore the corresponding feature state instead. By default, the
`include_global_state` and `feature_states` parameters don't restore any system
indices.

*Impact* +
If you previously used the `indices` parameter to back up or restore system
indices, update your SLM policies and application to use the
`include_global_state` and `feature_states` parameters instead.

An SLM policy that explicitly specifies a system index in the `indices`
parameter will fail to create snapshots. Similarly, a create snapshot API or
restore snapshot API request that explicitly specifies a system index in the
`indices` parameter will fail and return an error. If the `indices` value
includes a wildcard (`*`) pattern, the pattern will no longer match system
indices.

**Snapshots compress metadata files by default.**
*Details* +
Previously, the default value for `compress` was `false`. The default has been changed to `true`.

This change will affect both newly created repositories and existing repositories where `compress=false` has not been
explicitly specified.

*Impact* +
Update your workflow and applications to assume a default value of `true` for
the `compress` parameter.

**S3 snapshot repositories now use a DNS-style access pattern by default.**
*Details* +
Starting in version 7.4, `s3` snapshot repositories no longer use the
now-deprecated path-style access pattern by default. In versions 7.0, 7.1, 7.2
and 7.3 `s3` snapshot repositories always used the path-style access pattern.
This is a breaking change for deployments that only support path-style access
but which are recognized as supporting DNS-style access by the AWS SDK. This
breaking change was made necessary by
https://aws.amazon.com/blogs/aws/amazon-s3-path-deprecation-plan-the-rest-of-the-story/[AWS's
announcement] that the path-style access pattern is deprecated and will be
unsupported on buckets created after September 30th 2020.

*Impact* +
If your deployment only supports path-style access and is affected by this
change then you must configure the S3 client setting `path_style_access` to
`true`.

**Restore requests no longer accept settings.**
*Details* +
In earlier versions, you could pass both `settings` and `index_settings` in the
body of a restore snapshot request, but the `settings` value was ignored. The
restore snapshot API now rejects requests that include a `settings` value.

*Impact* +
Discontinue use of the `settings` parameter in restore
snapshot request. Requests that include these parameters will return an error.

**The repository stats API has been removed.**
*Details* +
The repository stats API has been removed. We deprecated this experimental API
in 7.10.0.

*Impact* +
Use the [repositories metering APIs](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/repositories-metering-apis.html)
instead.

**Watcher history now writes to a hidden data stream.**
*Details* +
In 8.x, Elasticsearch writes Watcher history to a hidden
`.watcher-history-<index-template-version>` data stream. Previously, Elasticsearch wrote
Watcher history to hidden
`.watcher-history-<index-template-version>-<yyyy-MM-dd>` indices.

*Impact* +
Update your requests to target the Watcher history data stream. For example, use
the `.watcher-history-*` wildcard expression. Requests that specifically target
non-existent Watcher history indices may return an error.

**HTTP Status code has changed for the Cluster Health API in case of a server timeout.**
*Details* +
The [cluster health API](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/cluster-health.html) includes options for waiting
for certain health conditions to be satisfied. If the requested conditions are
not satisfied within a timeout then Elasticsearch will send back a normal response
including the field `"timed_out": true`. In earlier versions it would also use
the HTTP response code `408 Request timeout` if the request timed out, and `200
OK` otherwise. The `408 Request timeout` response code is not appropriate for
this situation, so from version 8.0.0 Elasticsearch will use the response code `200 OK`
for both cases.

*Impact* +
To detect a server timeout, check the `timed_out` field of the JSON response.

**The `Content-Type` response header no longer specifies the charset.**
*Details* +
The `Content-Type` response header no longer specifies the charset. This information is not required when transferring JSON data, because JSON text will always be encoded in Unicode, with UTF-8 being the default encoding.

*Impact* +
Some applications and utilities, such as PowerShell's [Invoke-RestMethod](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/invoke-restmethod), must receive charset information to display data correctly. If your application or utility relies on charset information in the `Content-Type` response header, UTF-8 encoded characters will be rendered incorrectly in the response body.

As a workaround, to render non-ASCII characters, include an HTTP `Accept` header in your requests, specifying the charset: 

```sh
Accept: application/json; charset=utf-8
```
