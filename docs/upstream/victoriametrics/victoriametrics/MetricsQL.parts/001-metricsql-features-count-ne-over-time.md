<!-- Part 1 of 8 of victoriametrics/MetricsQL.md (split because the page is big). -->

## MetricsQL features

MetricsQL implements [PromQL](https://medium.com/@valyala/promql-tutorial-for-beginners-9ab455142085)
and provides additional functionality mentioned below, which is aimed towards solving practical cases.
Feel free [filing a feature request](https://github.com/VictoriaMetrics/VictoriaMetrics/issues) if you think MetricsQL misses certain useful functionality.

This functionality can be evaluated at [VictoriaMetrics demo playground](https://play.victoriametrics.com/select/accounting/1/6a716b0f-38bc-4856-90ce-448fd713e3fe/prometheus/graph/)
or at your own [VictoriaMetrics instance](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#how-to-start-victoriametrics).

The list of MetricsQL features on top of PromQL:

* Graphite-compatible filters can be passed via `{__graphite__="foo.*.bar"}` syntax.
  See [these docs](https://docs.victoriametrics.com/victoriametrics/integrations/graphite/#selecting-graphite-metrics).
  VictoriaMetrics can be used as Graphite datasource in Grafana. See [these docs](https://docs.victoriametrics.com/victoriametrics/integrations/graphite/#graphite-api-usage) for details.
  See also [label_graphite_group](#label_graphite_group) function, which can be used for extracting the given groups from Graphite metric name.
* The lookbehind window in square brackets for [rollup functions](#rollup-functions) may be omitted. VictoriaMetrics automatically selects the lookbehind window
  depending on the `step` query arg passed to [/api/v1/query_range](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#range-query)
  and the real interval between [raw samples](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#raw-samples) (aka `scrape_interval`).
  For instance, the following query is valid in VictoriaMetrics: `rate(node_network_receive_bytes_total)`.
  It is roughly equivalent to `rate(node_network_receive_bytes_total[$__interval])` when used in Grafana.
  The difference is documented in [rate() docs](#rate).
* Numeric values may include underscore delimiters for better readability. For example, `1_234_567_890` can be used in queries instead of `1234567890`.
* [Series selectors](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#filtering) accept multiple `or` filters. For example, `{env="prod",job="a" or env="dev",job="b"}`
  selects series with `{env="prod",job="a"}` or `{env="dev",job="b"}` labels.
  See [these docs](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#filtering-by-multiple-or-filters) for details.
* Support for matching against multiple numeric constants via `q == (C1, ..., CN)` and `q != (C1, ..., CN)` syntax. For example, `status_code == (300, 301, 304)`
  returns `status_code` metrics with one of `300`, `301` or `304` values.
* Support for `group_left(*)` and `group_right(*)` for copying all the labels from time series on the `one` side
  of [many-to-one operations](https://prometheus.io/docs/prometheus/latest/querying/operators/#many-to-one-and-one-to-many-vector-matches).
  The copied label names may clash with the existing label names, so MetricsQL provides an ability to add prefix to the copied metric names
  via `group_left(*) prefix "..."` syntax.
  For example, the following query copies all the `namespace`-related labels from `kube_namespace_labels` to `kube_pod_info` series,
  while adding `ns_` prefix to the copied labels: `kube_pod_info * on(namespace) group_left(*) prefix "ns_" kube_namespace_labels`.
  Labels from the `on()` list aren't copied.
* [Aggregate functions](#aggregate-functions) accept arbitrary number of args.
  For example, `avg(q1, q2, q3)` would return the average values for every point across time series returned by `q1`, `q2` and `q3`.
* [@ modifier](https://prometheus.io/docs/prometheus/latest/querying/basics/#-modifier) can be put anywhere in the query.
  For example, `sum(foo) @ end()` calculates `sum(foo)` at the `end` timestamp of the selected time range `[start ... end]`.
* Arbitrary subexpression can be used as [@ modifier](https://prometheus.io/docs/prometheus/latest/querying/basics/#-modifier).
  For example, `foo @ (end() - 1h)` calculates `foo` at the `end - 1 hour` timestamp on the selected time range `[start ... end]`.
* [offset](https://prometheus.io/docs/prometheus/latest/querying/basics/#offset-modifier), lookbehind window in square brackets
  and `step` value for [subquery](#subqueries) may refer to the current step aka `$__interval` value from Grafana with `[Ni]` syntax.
  For instance, `rate(metric[10i] offset 5i)` would return per-second rate over a range covering 10 previous steps with the offset of 5 steps.
* [offset](https://prometheus.io/docs/prometheus/latest/querying/basics/#offset-modifier) may be put anywhere in the query. For instance, `sum(foo) offset 24h`.
* Lookbehind window in square brackets and [offset](https://prometheus.io/docs/prometheus/latest/querying/basics/#offset-modifier) may be fractional.
  For instance, `rate(node_network_receive_bytes_total[1.5m] offset 0.5d)`.
* The duration suffix is optional. The duration is in seconds if the suffix is missing.
  For example, `rate(m[300] offset 1800)` is equivalent to `rate(m[5m]) offset 30m`.
* The duration can be placed anywhere in the query. For example, `sum_over_time(m[1h]) / 1h` is equivalent to `sum_over_time(m[1h]) / 3600`.
* Numeric values can have `K`, `Ki`, `M`, `Mi`, `G`, `Gi`, `T` and `Ti` suffixes. For example, `8K` is equivalent to `8000`, while `1.2Mi` is equivalent to `1.2*1024*1024`.
* Trailing commas on all the lists are allowed - label filters, function args and with expressions.
  For instance, the following queries are valid: `m{foo="bar",}`, `f(a, b,)`, `WITH (x=y,) x`.
  This simplifies maintenance of multi-line queries.
* Metric names and label names may contain any unicode letter. For example `ტემპერატურა{πόλη="Київ"}` is a valid MetricsQL expression.
* Metric names and labels names may contain escaped chars. For example, `foo\-bar{baz\=aa="b"}` is valid expression.
  It returns time series with name `foo-bar` containing label `baz=aa` with value `b`.
  Additionally, the following escape sequences are supported:
  * `\xXX`, where `XX` is hexadecimal representation of the escaped ascii char.
  * `\uXXXX`, where `XXXX` is a hexadecimal representation of the escaped unicode char.
* Aggregate functions support optional `limit N` suffix in order to limit the number of output series.
  For example, `sum(x) by (y) limit 3` limits the number of output time series after the aggregation to 3.
  All the other time series are dropped.
* [histogram_quantile](#histogram_quantile) accepts optional third arg - `boundsLabel`.
  In this case it returns `lower` and `upper` bounds for the estimated percentile.
  See [this issue for details](https://github.com/prometheus/prometheus/issues/5706).
* `default` binary operator. `q1 default q2` fills gaps in `q1` with the corresponding values from `q2`. See also [drop_empty_series](#drop_empty_series).
* `if` binary operator. `q1 if q2` removes values from `q1` for missing values from `q2`.
* `ifnot` binary operator. `q1 ifnot q2` removes values from `q1` for existing values from `q2`.
* `WITH` templates. This feature simplifies writing and managing complex queries.
  Go to [WITH templates playground](https://play.victoriametrics.com/select/0/prometheus/graph/#/expand-with-exprs) and try it.
* String literals may be concatenated. This is useful with `WITH` templates:
  `WITH (commonPrefix="long_metric_prefix_") {__name__=commonPrefix+"suffix1"} / {__name__=commonPrefix+"suffix2"}`.
* `keep_metric_names` modifier can be applied to all the [rollup functions](#rollup-functions), [transform functions](#transform-functions)
  and [binary operators](https://prometheus.io/docs/prometheus/latest/querying/operators/#binary-operators).
  This modifier prevents from dropping metric names in function results. See [these docs](#keep_metric_names).


## keep_metric_names

By default, metric names are dropped after applying functions or [binary operators](https://prometheus.io/docs/prometheus/latest/querying/operators/#binary-operators),
since they may change the meaning of the original time series.
This may result in `duplicate time series` error when the function is applied to multiple time series with different names.
This error can be fixed by applying `keep_metric_names` modifier to the function or binary operator.

For example:

* `rate({__name__=~"foo|bar"}) keep_metric_names` leaves `foo` and `bar` metric names in the returned time series.
* `({__name__=~"foo|bar"} / 10) keep_metric_names` leaves `foo` and `bar` metric names in the returned time series.


## MetricsQL functions

If you are unfamiliar with PromQL, then please read [this tutorial](https://medium.com/@valyala/promql-tutorial-for-beginners-9ab455142085) at first.

MetricsQL provides the following functions:

* [Rollup functions](#rollup-functions)
* [Transform functions](#transform-functions)
* [Label manipulation functions](#label-manipulation-functions)
* [Aggregate functions](#aggregate-functions)


### Rollup functions

**Rollup functions** (aka range functions or window functions) calculate rollups over [raw samples](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#raw-samples)
on the given lookbehind window for the [selected time series](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#filtering).
For example, `avg_over_time(temperature[24h])` calculates the average temperature over [raw samples](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#raw-samples) for the last 24 hours.

Additional details:

* If rollup functions are used for building graphs in Grafana, then the rollup is calculated independently per each point on the graph.
  For example, every point for `avg_over_time(temperature[24h])` graph shows the average temperature for the last 24 hours ending at this point.
  The interval between points is set as `step` query arg passed by Grafana to [/api/v1/query_range](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#range-query).
* If the given [series selector](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#filtering) returns multiple time series,
  then rollups are calculated individually per each returned series.
* If lookbehind window in square brackets is missing, then it is automatically set to the following value:
  * To `step` value passed to [/api/v1/query_range](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#range-query) or [/api/v1/query](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#instant-query)
    for all the [rollup functions](#rollup-functions) except of [default_rollup](#default_rollup) and [rate](#rate). This value is known as `$__interval` in Grafana or `1i` in MetricsQL.
    For example, `avg_over_time(temperature)` is automatically transformed to `avg_over_time(temperature[1i])`.
  * To the `max(step, scrape_interval)`, where `scrape_interval` is the interval between [raw samples](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#raw-samples)
    for [default_rollup](#default_rollup) and [rate](#rate) functions. This allows avoiding unexpected gaps on the graph when `step` is smaller than `scrape_interval`.
* Every [series selector](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#filtering) in MetricsQL must be wrapped into a rollup function.
  Otherwise, it is automatically wrapped into [default_rollup](#default_rollup). For example, `foo{bar="baz"}`
  is automatically converted to `default_rollup(foo{bar="baz"})` before performing the calculations.
* If something other than [series selector](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#filtering) is passed to rollup function,
  then the inner arg is automatically converted to a [subquery](#subqueries).
* All the rollup functions accept optional `keep_metric_names` modifier. If it is set, then the function keeps metric names in results.
  See [these docs](#keep_metric_names).

See also [implicit query conversions](#implicit-query-conversions).

The list of supported rollup functions:


#### absent_over_time

`absent_over_time(series_selector[d])` is a [rollup function](#rollup-functions), which returns 1
if the given lookbehind window `d` doesn't contain [raw samples](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#raw-samples). Otherwise, it returns an empty result.

This function is supported by PromQL.

See also [present_over_time](#present_over_time).


#### aggr_over_time

`aggr_over_time(("rollup_func1", "rollup_func2", ...), series_selector[d])` is a [rollup function](#rollup-functions),
which calculates all the listed `rollup_func*` for [raw samples](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#raw-samples) on the given lookbehind window `d`.
The calculations are performed individually per each time series returned
from the given [series_selector](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#filtering).

`rollup_func*` can contain any rollup function. For instance, `aggr_over_time(("min_over_time", "max_over_time", "rate"), m[d])`
would calculate [min_over_time](#min_over_time), [max_over_time](#max_over_time) and [rate](#rate) for `m[d]`.


#### ascent_over_time

`ascent_over_time(series_selector[d])` is a [rollup function](#rollup-functions), which calculates
ascent of [raw sample](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#raw-samples) values on the given lookbehind window `d`. The calculations are performed individually
per each time series returned from the given [series_selector](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#filtering).

This function is useful for tracking height gains in GPS tracking.

Metric names are stripped from the resulting rollups. Add [keep_metric_names](#keep_metric_names) modifier in order to keep metric names.

See also [descent_over_time](#descent_over_time).


#### avg_over_time

`avg_over_time(series_selector[d])` is a [rollup function](#rollup-functions), which calculates the average value
over [raw samples](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#raw-samples) on the given lookbehind window `d` per each time series returned
from the given [series_selector](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#filtering).

This function is usually applied to [gauges](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#gauge).

This function is supported by PromQL.

See also [median_over_time](#median_over_time), [min_over_time](#min_over_time) and [max_over_time](#max_over_time).


#### changes

`changes(series_selector[d])` is a [rollup function](#rollup-functions), which calculates the number of times
the [raw samples](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#raw-samples) changed on the given lookbehind window `d` per each time series returned
from the given [series_selector](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#filtering).

Unlike `changes()` in Prometheus it takes into account the change from the last sample before the given lookbehind window `d`.
See [this article](https://medium.com/@romanhavronenko/victoriametrics-promql-compliance-d4318203f51e) for details.

Metric names are stripped from the resulting rollups. Add [keep_metric_names](#keep_metric_names) modifier in order to keep metric names.

This function is supported by PromQL.

See also [changes_prometheus](#changes_prometheus).


#### changes_prometheus

`changes_prometheus(series_selector[d])` is a [rollup function](#rollup-functions), which calculates the number of times
the [raw samples](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#raw-samples) changed on the given lookbehind window `d` per each time series returned
from the given [series_selector](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#filtering).

It doesn't take into account the change from the last sample before the given lookbehind window `d` in the same way as Prometheus does.
See [this article](https://medium.com/@romanhavronenko/victoriametrics-promql-compliance-d4318203f51e) for details.

Metric names are stripped from the resulting rollups. Add [keep_metric_names](#keep_metric_names) modifier in order to keep metric names.

This function is supported by PromQL.

See also [changes](#changes).


#### count_eq_over_time

`count_eq_over_time(series_selector[d], eq)` is a [rollup function](#rollup-functions), which calculates the number of [raw samples](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#raw-samples)
on the given lookbehind window `d`, which are equal to `eq`. It is calculated independently per each time series returned
from the given [series_selector](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#filtering).

Metric names are stripped from the resulting rollups. Add [keep_metric_names](#keep_metric_names) modifier in order to keep metric names.

This function is usually applied to [gauges](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#gauge).

See also [count_over_time](#count_over_time), [share_eq_over_time](#share_eq_over_time) and [count_values_over_time](#count_values_over_time).


#### count_gt_over_time

`count_gt_over_time(series_selector[d], gt)` is a [rollup function](#rollup-functions), which calculates the number of [raw samples](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#raw-samples)
on the given lookbehind window `d`, which are bigger than `gt`. It is calculated independently per each time series returned
from the given [series_selector](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#filtering).

Metric names are stripped from the resulting rollups. Add [keep_metric_names](#keep_metric_names) modifier in order to keep metric names.

This function is usually applied to [gauges](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#gauge).

See also [count_over_time](#count_over_time) and [share_gt_over_time](#share_gt_over_time).


#### count_le_over_time

`count_le_over_time(series_selector[d], le)` is a [rollup function](#rollup-functions), which calculates the number of [raw samples](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#raw-samples)
on the given lookbehind window `d`, which don't exceed `le`. It is calculated independently per each time series returned
from the given [series_selector](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#filtering).

Metric names are stripped from the resulting rollups. Add [keep_metric_names](#keep_metric_names) modifier in order to keep metric names.

This function is usually applied to [gauges](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#gauge).

See also [count_over_time](#count_over_time) and [share_le_over_time](#share_le_over_time).


#### count_ne_over_time

`count_ne_over_time(series_selector[d], ne)` is a [rollup function](#rollup-functions), which calculates the number of [raw samples](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#raw-samples)
on the given lookbehind window `d`, which aren't equal to `ne`. It is calculated independently per each time series returned
from the given [series_selector](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#filtering).

Metric names are stripped from the resulting rollups. Add [keep_metric_names](#keep_metric_names) modifier in order to keep metric names.

This function is usually applied to [gauges](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#gauge).

See also [count_over_time](#count_over_time) and [count_eq_over_time](#count_eq_over_time).
