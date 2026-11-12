<!-- Part 7 of 8 of victoriametrics/MetricsQL.md (split because the page is big). -->

### Aggregate functions

**Aggregate functions** calculate aggregates over groups of [rollup results](#rollup-functions).

Additional details:

* By default, a single group is used for aggregation. Multiple independent groups can be set up by specifying grouping labels
  in `by` and `without` modifiers. For example, `count(up) by (job)` would group [rollup results](#rollup-functions) by `job` label value
  and calculate the [count](#count) aggregate function independently per each group, while `count(up) without (instance)`
  would group [rollup results](#rollup-functions) by all the labels except `instance` before calculating [count](#count) aggregate function independently per each group.
  Multiple labels can be put in `by` and `without` modifiers.
* If the aggregate function is applied directly to a [series_selector](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#filtering),
  then the [default_rollup()](#default_rollup) function is automatically applied before calculating the aggregate.
  For example, `count(up)` is implicitly transformed to `count(default_rollup(up))`.
* Aggregate functions accept arbitrary number of args. For example, `avg(q1, q2, q3)` would return the average values for every point
  across time series returned by `q1`, `q2` and `q3`.
* Aggregate functions support optional `limit N` suffix, which can be used for limiting the number of output groups.
  For example, `sum(x) by (y) limit 3` limits the number of groups for the aggregation to 3. All the other groups are ignored.

See also [implicit query conversions](#implicit-query-conversions).

The list of supported aggregate functions:

#### any

`any(q) by (group_labels)` is [aggregate function](#aggregate-functions), which returns a single series per `group_labels` out of time series returned by `q`.

See also [group](#group).

#### avg

`avg(q) by (group_labels)` is [aggregate function](#aggregate-functions), which returns the average value per `group_labels` for time series returned by `q`.
The aggregate is calculated individually per each group of points with the same timestamp.

This function is supported by PromQL.

#### bottomk

`bottomk(k, q)` is [aggregate function](#aggregate-functions), which returns up to `k` points with the smallest values across all the time series returned by `q`.
The aggregate is calculated individually per each group of points with the same timestamp.

This function is supported by PromQL.

See also [topk](#topk), [bottomk_min](#bottomk_min) and [#bottomk_last](#bottomk_last).

#### bottomk_avg

`bottomk_avg(k, q, "other_label=other_value")` is [aggregate function](#aggregate-functions), which returns up to `k` time series from `q` with the smallest averages.
If an optional `other_label=other_value` arg is set, then the sum of the remaining time series is returned with the given label.
For example, `bottomk_avg(3, sum(process_resident_memory_bytes) by (job), "job=other")` would return up to 3 time series
with the smallest averages plus a time series with `{job="other"}` label with the sum of the remaining series if any.

See also [topk_avg](#topk_avg).

#### bottomk_last

`bottomk_last(k, q, "other_label=other_value")` is [aggregate function](#aggregate-functions), which returns up to `k` time series from `q` with the smallest last values.
If an optional `other_label=other_value` arg is set, then the sum of the remaining time series is returned with the given label.
For example, `bottomk_max(3, sum(process_resident_memory_bytes) by (job), "job=other")` would return up to 3 time series
with the smallest maximums plus a time series with `{job="other"}` label with the sum of the remaining series if any.

See also [topk_last](#topk_last).

#### bottomk_max

`bottomk_max(k, q, "other_label=other_value")` is [aggregate function](#aggregate-functions), which returns up to `k` time series from `q` with the smallest maximums.
If an optional `other_label=other_value` arg is set, then the sum of the remaining time series is returned with the given label.
For example, `bottomk_max(3, sum(process_resident_memory_bytes) by (job), "job=other")` would return up to 3 time series
with the smallest maximums plus a time series with `{job="other"}` label with the sum of the remaining series if any.

See also [topk_max](#topk_max).

#### bottomk_median

`bottomk_median(k, q, "other_label=other_value")` is [aggregate function](#aggregate-functions), which returns up to `k` time series from `q` with the smallest medians.
If an optional`other_label=other_value` arg is set, then the sum of the remaining time series is returned with the given label.
For example, `bottomk_median(3, sum(process_resident_memory_bytes) by (job), "job=other")` would return up to 3 time series
with the smallest medians plus a time series with `{job="other"}` label with the sum of the remaining series if any.

See also [topk_median](#topk_median).

#### bottomk_min

`bottomk_min(k, q, "other_label=other_value")` is [aggregate function](#aggregate-functions), which returns up to `k` time series from `q` with the smallest minimums.
If an optional `other_label=other_value` arg is set, then the sum of the remaining time series is returned with the given label.
For example, `bottomk_min(3, sum(process_resident_memory_bytes) by (job), "job=other")` would return up to 3 time series
with the smallest minimums plus a time series with `{job="other"}` label with the sum of the remaining series if any.

See also [topk_min](#topk_min).

#### count

`count(q) by (group_labels)` is [aggregate function](#aggregate-functions), which returns the number of non-empty points per `group_labels`
for time series returned by `q`. The aggregate is calculated individually per each group of points with the same timestamp.

This function is supported by PromQL.

#### count_values

`count_values("label", q)` is [aggregate function](#aggregate-functions), which counts the number of points with the same value
and stores the counts in a time series with an additional `label`, which contains each initial value.
The aggregate is calculated individually per each group of points with the same timestamp.

This function is supported by PromQL.

See also [count_values_over_time](#count_values_over_time) and [label_match](#label_match).

#### distinct

`distinct(q)` is [aggregate function](#aggregate-functions), which calculates the number of unique values per each group of points with the same timestamp.

See also [distinct_over_time](#distinct_over_time).

#### geomean

`geomean(q)` is [aggregate function](#aggregate-functions), which calculates geometric mean per each group of points with the same timestamp.

#### group

`group(q) by (group_labels)` is [aggregate function](#aggregate-functions), which returns `1` per each `group_labels` for time series returned by `q`.

This function is supported by PromQL. See also [any](#any).

#### histogram

`histogram(q)` is [aggregate function](#aggregate-functions), which calculates
[VictoriaMetrics histogram](https://valyala.medium.com/improving-histogram-usability-for-prometheus-and-grafana-bc7e5df0e350)
per each group of points with the same timestamp. Useful for visualizing big number of time series via a heatmap.
See [this article](https://medium.com/@valyala/improving-histogram-usability-for-prometheus-and-grafana-bc7e5df0e350) for more details.

See also [histogram_over_time](#histogram_over_time) and [histogram_quantile](#histogram_quantile).

#### limitk

`limitk(k, q) by (group_labels)` is [aggregate function](#aggregate-functions), which returns up to `k` time series per each `group_labels`
out of time series returned by `q`. The returned set of time series remain the same across calls.

See also [limit_offset](#limit_offset).

#### mad

`mad(q) by (group_labels)` is [aggregate function](#aggregate-functions), which returns the [Median absolute deviation](https://en.wikipedia.org/wiki/Median_absolute_deviation)
per each `group_labels` for all the time series returned by `q`. The aggregate is calculated individually per each group of points with the same timestamp.

See also [range_mad](#range_mad), [mad_over_time](#mad_over_time), [outliers_mad](#outliers_mad) and [stddev](#stddev).

#### max

`max(q) by (group_labels)` is [aggregate function](#aggregate-functions), which returns the maximum value per each `group_labels`
for all the time series returned by `q`. The aggregate is calculated individually per each group of points with the same timestamp.

This function is supported by PromQL.

#### median

`median(q) by (group_labels)` is [aggregate function](#aggregate-functions), which returns the median value per each `group_labels`
for all the time series returned by `q`. The aggregate is calculated individually per each group of points with the same timestamp.

#### min

`min(q) by (group_labels)` is [aggregate function](#aggregate-functions), which returns the minimum value per each `group_labels`
for all the time series returned by `q`. The aggregate is calculated individually per each group of points with the same timestamp.

This function is supported by PromQL.

#### mode

`mode(q) by (group_labels)` is [aggregate function](#aggregate-functions), which returns [mode](https://en.wikipedia.org/wiki/Mode_(statistics))
per each `group_labels` for all the time series returned by `q`. The aggregate is calculated individually per each group of points with the same timestamp.

#### outliers_iqr

`outliers_iqr(q)` is [aggregate function](#aggregate-functions), which returns time series from `q` with at least a single point
outside e.g. [Interquartile range outlier bounds](https://en.wikipedia.org/wiki/Interquartile_range) `[q25-1.5*iqr .. q75+1.5*iqr]`
comparing to other time series at the given point, where:

* `iqr` is an [Interquartile range](https://en.wikipedia.org/wiki/Interquartile_range) calculated independently per each point on the graph across `q` series.
* `q25` and `q75` are 25th and 75th [percentiles](https://en.wikipedia.org/wiki/Percentile) calculated independently per each point on the graph across `q` series.

The `outliers_iqr()` is useful for detecting anomalous series in the group of series. For example, `outliers_iqr(temperature) by (country)` returns
per-country series with anomalous outlier values comparing to the rest of per-country series.

See also [outliers_mad](#outliers_mad), [outliersk](#outliersk) and [outlier_iqr_over_time](#outlier_iqr_over_time).

#### outliers_mad

`outliers_mad(tolerance, q)` is [aggregate function](#aggregate-functions), which returns time series from `q` with at least
a single point outside [Median absolute deviation](https://en.wikipedia.org/wiki/Median_absolute_deviation) (aka MAD) multiplied by `tolerance`.
E.g. it returns time series with at least a single point below `median(q) - mad(q)` or a single point above `median(q) + mad(q)`.

See also [outliers_iqr](#outliers_iqr), [outliersk](#outliersk) and [mad](#mad).

#### outliersk

`outliersk(k, q)` is [aggregate function](#aggregate-functions), which returns up to `k` time series with the biggest standard deviation (aka outliers)
out of time series returned by `q`.

See also [outliers_iqr](#outliers_iqr) and [outliers_mad](#outliers_mad).

#### quantile

`quantile(phi, q) by (group_labels)` is [aggregate function](#aggregate-functions), which calculates `phi`-quantile per each `group_labels`
for all the time series returned by `q`. `phi` must be in the range `[0...1]`.
The aggregate is calculated individually per each group of points with the same timestamp.

This function is supported by PromQL.

See also [quantiles](#quantiles) and [histogram_quantile](#histogram_quantile).

#### quantiles

`quantiles("phiLabel", phi1, ..., phiN, q)` is [aggregate function](#aggregate-functions), which calculates `phi*`-quantiles for all the time series
returned by `q` and return them in time series with `{phiLabel="phi*"}` label. `phi*` must be in the range `[0...1]`.
The aggregate is calculated individually per each group of points with the same timestamp.

See also [quantile](#quantile).

#### share

`share(q) by (group_labels)` is [aggregate function](#aggregate-functions), which returns shares in the range `[0..1]`
for every non-negative points returned by `q` per each timestamp, so the sum of shares per each `group_labels` equals 1.

This function is useful for normalizing [histogram bucket](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#histogram) shares
into `[0..1]` range:

```metricsql
share(
  sum(
    rate(http_request_duration_seconds_bucket[5m])
  ) by (le, vmrange)
)
```

See also [range_normalize](#range_normalize).

#### stddev

`stddev(q) by (group_labels)` is [aggregate function](#aggregate-functions), which calculates standard deviation per each `group_labels`
for all the time series returned by `q`. The aggregate is calculated individually per each group of points with the same timestamp.

This function is supported by PromQL.

#### stdvar

`stdvar(q) by (group_labels)` is [aggregate function](#aggregate-functions), which calculates standard variance per each `group_labels`
for all the time series returned by `q`. The aggregate is calculated individually per each group of points with the same timestamp.

This function is supported by PromQL.

#### sum

`sum(q) by (group_labels)` is [aggregate function](#aggregate-functions), which returns the sum per each `group_labels`
for all the time series returned by `q`. The aggregate is calculated individually per each group of points with the same timestamp.

This function is supported by PromQL.

#### sum2

`sum2(q) by (group_labels)` is [aggregate function](#aggregate-functions), which calculates the sum of squares per each `group_labels`
for all the time series returned by `q`. The aggregate is calculated individually per each group of points with the same timestamp.

#### topk

`topk(k, q)` is [aggregate function](#aggregate-functions), which returns up to `k` points with the biggest values across all the time series returned by `q`.
The aggregate is calculated individually per each group of points with the same timestamp.

This function is supported by PromQL.

See also [bottomk](#bottomk), [topk_max](#topk_max) and [topk_last](#topk_last).

#### topk_avg

`topk_avg(k, q, "other_label=other_value")` is [aggregate function](#aggregate-functions), which returns up to `k` time series from `q` with the biggest averages.
If an optional `other_label=other_value` arg is set, then the sum of the remaining time series is returned with the given label.
For example, `topk_avg(3, sum(process_resident_memory_bytes) by (job), "job=other")` would return up to 3 time series with the biggest averages
plus a time series with `{job="other"}` label with the sum of the remaining series if any.

See also [bottomk_avg](#bottomk_avg).

#### topk_last

`topk_last(k, q, "other_label=other_value")` is [aggregate function](#aggregate-functions), which returns up to `k` time series from `q` with the biggest last values.
If an optional `other_label=other_value` arg is set, then the sum of the remaining time series is returned with the given label.
For example, `topk_max(3, sum(process_resident_memory_bytes) by (job), "job=other")` would return up to 3 time series with the biggest maximums
plus a time series with `{job="other"}` label with the sum of the remaining series if any.

See also [bottomk_last](#bottomk_last).

#### topk_max

`topk_max(k, q, "other_label=other_value")` is [aggregate function](#aggregate-functions), which returns up to `k` time series from `q` with the biggest maximums.
If an optional `other_label=other_value` arg is set, then the sum of the remaining time series is returned with the given label.
For example, `topk_max(3, sum(process_resident_memory_bytes) by (job), "job=other")` would return up to 3 time series with the biggest maximums
plus a time series with `{job="other"}` label with the sum of the remaining series if any.

See also [bottomk_max](#bottomk_max).

#### topk_median

`topk_median(k, q, "other_label=other_value")` is [aggregate function](#aggregate-functions), which returns up to `k` time series from `q` with the biggest medians.
If an optional `other_label=other_value` arg is set, then the sum of the remaining time series is returned with the given label.
For example, `topk_median(3, sum(process_resident_memory_bytes) by (job), "job=other")` would return up to 3 time series with the biggest medians
plus a time series with `{job="other"}` label with the sum of the remaining series if any.

See also [bottomk_median](#bottomk_median).

#### topk_min

`topk_min(k, q, "other_label=other_value")` is [aggregate function](#aggregate-functions), which returns up to `k` time series from `q` with the biggest minimums.
If an optional `other_label=other_value` arg is set, then the sum of the remaining time series is returned with the given label.
For example, `topk_min(3, sum(process_resident_memory_bytes) by (job), "job=other")` would return up to 3 time series with the biggest minimums
plus a time series with `{job="other"}` label with the sum of the remaining series if any.

See also [bottomk_min](#bottomk_min).

#### zscore

`zscore(q) by (group_labels)` is [aggregate function](#aggregate-functions), which returns [z-score](https://en.wikipedia.org/wiki/Standard_score) values
per each `group_labels` for all the time series returned by `q`. The aggregate is calculated individually per each group of points with the same timestamp.
This function is useful for detecting anomalies in the group of related time series.

See also [zscore_over_time](#zscore_over_time), [range_trim_zscore](#range_trim_zscore) and [outliers_iqr](#outliers_iqr).


## Subqueries

MetricsQL supports and extends PromQL subqueries. See [this article](https://valyala.medium.com/prometheus-subqueries-in-victoriametrics-9b1492b720b3) for details.
Any [rollup function](#rollup-functions) for something other than [series selector](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#filtering) form a subquery.
Nested rollup functions can be implicit thanks to the [implicit query conversions](#implicit-query-conversions).
For example, `delta(sum(m))` is implicitly converted to `delta(sum(default_rollup(m))[1i:1i])`, so it becomes a subquery,
since it contains [default_rollup](#default_rollup) nested into [delta](#delta).
This behavior can be disabled or logged via `-search.disableImplicitConversion` and `-search.logImplicitConversion` command-line flags
starting from [`v1.101.0` release](https://docs.victoriametrics.com/victoriametrics/changelog/).

VictoriaMetrics performs subqueries in the following way:

* It calculates the inner rollup function using the `step` value from the outer rollup function.
  For example, for expression `max_over_time(rate(http_requests_total[5m])[1h:30s])` the inner function `rate(http_requests_total[5m])`
  is calculated with `step=30s`. The resulting data points are aligned by the `step`.
* It calculates the outer rollup function over the results of the inner rollup function using the `step` value
  passed by Grafana to [/api/v1/query_range](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#range-query).
