<!-- Part 3 of 18 of release-notes/index.md (split because the page is big). -->

### Highlights [elasticsearch-9.4.0-highlights]

::::{dropdown} ES|QL Views support
ES|QL now supports Views: virtual indices whose fields are produced by an ES|QL query.
A view is referenced inside a `FROM` clause exactly like a regular index, alongside other indices, views, and wildcards.
Complex processing pipelines can be hidden behind a view, exposing a stable set of columns without requiring callers to know the underlying source structure.
A single query can combine multiple pre-processed data sources by listing several views in one `FROM` clause, with each view's pipeline running independently.
Common transformations such as renames, type conversions, derived fields, and aggregations can be defined once in a view and reused across many queries, dashboards, and alerts.
::::

::::{dropdown} Enable PromQL command in ES|QL
PromQL is now supported as a source command in ES|QL (Tech Preview). Users can now leverage their existing knowledge of PromQL
while benefiting from the powerful features and scalability of Elasticsearch. This enhancement expands the
versatility of ES|QL and makes it easier for users to integrate with Prometheus data sources.

The syntax is illustrated in the following example:

```esql
PROMQL index=k8s-downsampled start="2026-02-17T08:00:00Z" end="2026-02-17T09:00:00Z" step=30m avg_bytes=(avg(rate(network.total_bytes_in[30m])))
| SORT avg_bytes DESC, step;
```
::::

::::{dropdown} Discover time series metrics with ES|QL `METRICS_INFO`
ES|QL adds the `METRICS_INFO` command for queries that start with a time series (`TS`) source. It returns one row per
distinct metric, with columns such as `metric_name`, `data_stream`, `unit`, `metric_type`, `field_type`, and
`dimension_fields`, derived from time series metadata in the index. It unlocks inspecting which metrics exist and how they
are typed before you aggregate with `STATS`.

For example, list metrics sorted by name:

```esql
TS my_data_stream
| METRICS_INFO
| SORT metric_name
```

Or filter to counters only:

```esql
TS my_data_stream
| METRICS_INFO
| WHERE metric_type == "counter"
| SORT metric_name
```
::::

::::{dropdown} Implement Prometheus remote write indexing support
We're introducing a Prometheus-compatible `POST /_prometheus/api/v1/write` REST entrypoint that allows receiving data via
Prometheus remote write protocol (Tech Preview). Elasticsearch can now be used as a Prometheus storage backend, consuming data
sent in Prometheus native format.
::::

::::{dropdown} Inspect each time series with ES|QL `TS_INFO`
ES|QL adds the `TS_INFO` command for time series (`TS`) queries. It returns one row per metric and time series combination.
You get the same metadata columns as `METRICS_INFO`, plus a `dimensions` column with a JSON object of dimension keys and values for
that series. That unlocks inferring which labels apply to each series when exploring or validating
time series data.

For example:

```esql
TS my_data_stream
| TS_INFO
| SORT metric_name, dimensions
```
::::

::::{dropdown} Downsampling preserves the resets of counters when the `aggregate` sampling method is used.
Until Elasticsearch `9.3`, both downsampling methods (`aggregate` and `last_value`) used to store only the last value of a counter
in the downsampled document. This works great for the `last_value` method where we optimise for storage efficiency, but
it is not ideal for the `aggregate` method where we optimise for accuracy.

In Elasticsearch `9.4`, we change the way the (default) `aggregate` sampling method is working. We store the first encountered
value for a counter in the downsampled document and then we add auxiliary documents when we detect counter resets.
This enables the rate calculation to take the counter resets into account and produce more accurate results. This change
is backwards compatible.
::::

::::{dropdown} Time series aggregations support windows that are smaller than the time bucket
Time series aggregations in ES|QL are enhanced to support windows smaller than the time bucket.

```esql
TS metrics | STATS AVG(RATE(requests, 5m)) BY TBUCKET(10m), host
```

Previously, only window values that were equal or exact multiples of the time bucket were supported.
::::

::::{dropdown} Time series aggregations support windows that are not an exact multiple of the bucket
Time series aggregations in ES|QL are enhanced to support windows that are not an exact multiple of the time bucket.

```esql
TS metrics | STATS AVG(RATE(requests, 15m)) BY TBUCKET(10m), host
```

Previously, only window values that were exact multiples of the time bucket were supported.
::::

::::{dropdown} Upgrade DiskBBQ algorithm
This updates our diskbbq algorithm and format.

 - It now provides 3x or more better search performance on very restrictive filters (prefilters on centroids)
 - Provides a way to condition non iid vectors (expert API for now)
 - Gives more bit options (1, 2, 4, and 7 bits!)
 - More native code improvements for overall performance
::::

::::{dropdown} Synthetic IDs for indices in time-series mode
The `_id` field has a significant storage footprint in metrics applications, as it requires both storing and indexing
unique document identifiers that are rarely used for direct lookups. To alleviate this, we are introducing synthetic
IDs for indices in time-series mode. Instead of indexing the `_id` field, a Bloom filter is used for fast, lightweight
duplicate detection at ingest time. Lookups and operations that previously relied on `_id` are delegated to other
indexed fields on the document, such as timestamps, or dimension fields, preserving the same query and
retrieval functionality.

This offers up to 40% storage improvement for OTLP metrics and reduces the cpu overhead for segment merging due to the
lack of an inverted index for `_id` fields.
::::

::::{dropdown} Add Prometheus query_range endpoint
We're introducing a Prometheus-compatible /_prometheus/api/v1/query_range REST endpoint (Tech Preview) that:

 - Accepts the standard Prometheus range query parameters (query, start, end, step, optional index)
 - Translates the PromQL expression into an ES|QL PROMQL command and executes it via EsqlQueryAction
 - Converts the columnar ES|QL response into the Prometheus matrix JSON format and returns it to the caller
::::

::::{dropdown} Add Prometheus series REST endpoint
We're introducing a Prometheus-compatible `GET /_prometheus/api/v1/series` REST entrypoint that accepts Prometheus
series selectors and returns matching label sets (Tech Preview). This is typically used for auto-completion in web UIs.
::::

::::{dropdown} Counter rate aggregations use tsid prefixes to parallelize execution
The first bytes of a time series id (tsid) include a hash of the metric name(s) for each doc of a time-series index.
Counter rate evaluation leverages these bytes to assign tsids to workers inside the ES|QL compute engine. This
(a) improves parallelism by dividing work in a granular and uniform fashion, and (b) leads to dense, sequential
access patterns per time series that have been optimized to avoid copies between counter value decoding and rate calculations.

Rate execution performance thus improves substantially, with up to 5x faster query responses.
::::

::::{dropdown} Add Prometheus labels REST endpoint
We're introducing a Prometheus-compatible `GET /_prometheus/api/v1/labels` REST entrypoint for time series discovery and
label enumeration and introspection (Tech Preview). Web UIs can use this for label auto-completion.
::::

::::{dropdown} Add Prometheus instant query REST endpoint
We're introducing a Prometheus-compatible `GET /_prometheus/api/v1/query` REST endpoint that evaluates a PromQL
expression at a single point in time and returns vector results (Tech Preview). The instant query endpoint currently runs a
short range query under the hood and returns the last sample.
::::

::::{dropdown} Improve the supportability of `aggregate_metric_double` by ES|QL.
In Elasticsearch `9.4` we expand the supportability of `aggregate_metric_double` to include non-native operations in ES|QL,
such as `std_dev`, using the average. The average is calculated using the `sum` and `value_count` sub-fields.
The average was selected because in most cases it is a more representative signal compared to a single sub-field. Native
operations such as `max`, `min`, `sum`, `avg`, and `count` will be supported natively by the respective sub-fields.

For example, the following query is now supported where `network.eth0.tx` is a an `aggregate_metric_double`:
```esql
FROM k8s-downsampled
| STATS max = max(network.eth0.tx), std_dev = STD_DEV(network.eth0.tx) by pod
| sort pod
```
Response:

```
max:double | std_dev:double | pod:keyword
1060.0     | 275.6970067    | one
824.0      | 184.1213952    | three
1419.0     | 356.9865993    | two
```
::::
