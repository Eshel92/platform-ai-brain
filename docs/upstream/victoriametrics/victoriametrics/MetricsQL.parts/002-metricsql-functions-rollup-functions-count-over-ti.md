<!-- Part 2 of 8 of victoriametrics/MetricsQL.md (split because the page is big). -->

#### count_over_time

`count_over_time(series_selector[d])` is a [rollup function](#rollup-functions), which calculates the number of [raw samples](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#raw-samples)
on the given lookbehind window `d` per each time series returned from the given [series_selector](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#filtering).

Metric names are stripped from the resulting rollups. Add [keep_metric_names](#keep_metric_names) modifier in order to keep metric names.

This function is supported by PromQL.

See also [count_le_over_time](#count_le_over_time), [count_gt_over_time](#count_gt_over_time), [count_eq_over_time](#count_eq_over_time) and [count_ne_over_time](#count_ne_over_time).


#### count_values_over_time

`count_values_over_time("label", series_selector[d])` is a [rollup function](#rollup-functions), which counts the number of [raw samples](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#raw-samples)
with the same value over the given lookbehind window and stores the counts in a time series with an additional `label`, which contains each initial value.
The results are calculated independently per each time series returned from the given [series_selector](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#filtering).

Metric names are stripped from the resulting rollups. Add [keep_metric_names](#keep_metric_names) modifier in order to keep metric names.

This function is usually applied to [gauges](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#gauge).

See also [count_eq_over_time](#count_eq_over_time), [count_values](#count_values) and [distinct_over_time](#distinct_over_time) and [label_match](#label_match).


#### decreases_over_time

`decreases_over_time(series_selector[d])` is a [rollup function](#rollup-functions), which calculates the number of [raw sample](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#raw-samples)
value decreases over the given lookbehind window `d` per each time series returned from the given [series_selector](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#filtering).

Metric names are stripped from the resulting rollups. Add [keep_metric_names](#keep_metric_names) modifier in order to keep metric names.

See also [increases_over_time](#increases_over_time).


#### default_rollup

`default_rollup(series_selector[d])` is a [rollup function](#rollup-functions), which returns the last [raw sample](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#raw-samples)
value on the given lookbehind window `d` per each time series returned from the given [series_selector](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#filtering).
Compared to [last_over_time](#last_over_time) it accounts for [staleness markers](https://docs.victoriametrics.com/victoriametrics/vmagent/#prometheus-staleness-markers) to detect stale series.

If the lookbehind window is skipped in square brackets, then it is automatically calculated as `max(step, scrape_interval)`, where `step` is the query arg value
passed to [/api/v1/query_range](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#range-query) or [/api/v1/query](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#instant-query),
while `scrape_interval` is the interval between [raw samples](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#raw-samples) for the selected time series.
This allows avoiding unexpected gaps on the graph when `step` is smaller than the `scrape_interval`.


#### delta

`delta(series_selector[d])` is a [rollup function](#rollup-functions), which calculates the difference between
the last sample before the given lookbehind window `d` and the last sample at the given lookbehind window `d`
per each time series returned from the given [series_selector](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#filtering).

The behaviour of `delta()` function in MetricsQL is slightly different to the behaviour of `delta()` function in Prometheus.
See [this article](https://medium.com/@romanhavronenko/victoriametrics-promql-compliance-d4318203f51e) for details.

Metric names are stripped from the resulting rollups. Add [keep_metric_names](#keep_metric_names) modifier in order to keep metric names.

This function is supported by PromQL.

See also [increase](#increase) and [delta_prometheus](#delta_prometheus).


#### delta_prometheus

`delta_prometheus(series_selector[d])` is a [rollup function](#rollup-functions), which calculates the difference between
the first and the last samples at the given lookbehind window `d` per each time series returned
from the given [series_selector](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#filtering).

The behaviour of `delta_prometheus()` is close to the behaviour of `delta()` function in Prometheus.
See [this article](https://medium.com/@romanhavronenko/victoriametrics-promql-compliance-d4318203f51e) for details.

Metric names are stripped from the resulting rollups. Add [keep_metric_names](#keep_metric_names) modifier in order to keep metric names.

See also [delta](#delta).


#### deriv

`deriv(series_selector[d])` is a [rollup function](#rollup-functions), which calculates per-second derivative over the given lookbehind window `d`
per each time series returned from the given [series_selector](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#filtering).
The derivative is calculated using linear regression.

Metric names are stripped from the resulting rollups. Add [keep_metric_names](#keep_metric_names) modifier in order to keep metric names.

This function is supported by PromQL.

See also [deriv_fast](#deriv_fast) and [ideriv](#ideriv).


#### deriv_fast

`deriv_fast(series_selector[d])` is a [rollup function](#rollup-functions), which calculates per-second derivative
using the first and the last [raw samples](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#raw-samples) on the given lookbehind window `d` per each time series returned
from the given [series_selector](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#filtering).

Metric names are stripped from the resulting rollups. Add [keep_metric_names](#keep_metric_names) modifier in order to keep metric names.

See also [deriv](#deriv) and [ideriv](#ideriv).


#### descent_over_time

`descent_over_time(series_selector[d])` is a [rollup function](#rollup-functions), which calculates descent of [raw sample](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#raw-samples)
values on the given lookbehind window `d`. The calculations are performed individually per each time series returned
from the given [series_selector](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#filtering).

This function is useful for tracking height loss in GPS tracking.

Metric names are stripped from the resulting rollups. Add [keep_metric_names](#keep_metric_names) modifier in order to keep metric names.

See also [ascent_over_time](#ascent_over_time).


#### distinct_over_time

`distinct_over_time(series_selector[d])` is a [rollup function](#rollup-functions), which returns the number of unique [raw sample](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#raw-samples)
values on the given lookbehind window `d` per each time series returned from the given [series_selector](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#filtering).

Metric names are stripped from the resulting rollups. Add [keep_metric_names](#keep_metric_names) modifier in order to keep metric names.

See also [count_values_over_time](#count_values_over_time).


#### duration_over_time

`duration_over_time(series_selector[d], max_interval)` is a [rollup function](#rollup-functions), which returns the duration in seconds
when time series returned from the given [series_selector](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#filtering) were present
over the given lookbehind window `d`. It is expected that intervals between adjacent samples per each series don't exceed the `max_interval`.
Otherwise, such intervals are considered as gaps and aren't counted.

Metric names are stripped from the resulting rollups. Add [keep_metric_names](#keep_metric_names) modifier in order to keep metric names.

See also [lifetime](#lifetime) and [lag](#lag).


#### first_over_time

`first_over_time(series_selector[d])` is a [rollup function](#rollup-functions), which returns the first [raw sample](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#raw-samples)
value on the given lookbehind window `d` per each time series returned from the given [series_selector](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#filtering).

See also [last_over_time](#last_over_time) and [tfirst_over_time](#tfirst_over_time).


#### geomean_over_time

`geomean_over_time(series_selector[d])` is a [rollup function](#rollup-functions), which calculates [geometric mean](https://en.wikipedia.org/wiki/Geometric_mean)
over [raw samples](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#raw-samples) on the given lookbehind window `d` per each time series returned
from the given [series_selector](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#filtering).

Metric names are stripped from the resulting rollups. Add [keep_metric_names](#keep_metric_names) modifier in order to keep metric names.

This function is usually applied to [gauges](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#gauge).


#### histogram_over_time

`histogram_over_time(series_selector[d])` is a [rollup function](#rollup-functions), which calculates
[VictoriaMetrics histogram](https://godoc.org/github.com/VictoriaMetrics/metrics#Histogram) over [raw samples](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#raw-samples)
on the given lookbehind window `d`. It is calculated individually per each time series returned from the given [series_selector](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#filtering).
The resulting histograms are useful to pass to [histogram_quantile](#histogram_quantile) for calculating quantiles
over multiple [gauges](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#gauge).
For example, the following query calculates median temperature by country over the last 24 hours:

`histogram_quantile(0.5, sum(histogram_over_time(temperature[24h])) by (vmrange,country))`.

This function is usually applied to [gauges](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#gauge).


#### hoeffding_bound_lower

`hoeffding_bound_lower(phi, series_selector[d])` is a [rollup function](#rollup-functions), which calculates
lower [Hoeffding bound](https://en.wikipedia.org/wiki/Hoeffding%27s_inequality) for the given `phi` in the range `[0...1]`.

This function is usually applied to [gauges](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#gauge).

See also [hoeffding_bound_upper](#hoeffding_bound_upper).


#### hoeffding_bound_upper

`hoeffding_bound_upper(phi, series_selector[d])` is a [rollup function](#rollup-functions), which calculates
upper [Hoeffding bound](https://en.wikipedia.org/wiki/Hoeffding%27s_inequality) for the given `phi` in the range `[0...1]`.

This function is usually applied to [gauges](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#gauge).

See also [hoeffding_bound_lower](#hoeffding_bound_lower).


#### holt_winters

`holt_winters(series_selector[d], sf, tf)` is a [rollup function](#rollup-functions), which calculates Holt-Winters value
(aka [double exponential smoothing](https://en.wikipedia.org/wiki/Exponential_smoothing#Double_exponential_smoothing_%28Holt_linear%29)) for [raw samples](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#raw-samples)
over the given lookbehind window `d` using the given smoothing factor `sf` and the given trend factor `tf`.
Both `sf` and `tf` must be in the range `[0...1]`.

This function is usually applied to [gauges](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#gauge).

This function is supported by PromQL.

See also [range_linear_regression](#range_linear_regression).


#### idelta

`idelta(series_selector[d])` is a [rollup function](#rollup-functions), which calculates the difference between the last two [raw samples](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#raw-samples)
on the given lookbehind window `d` per each time series returned from the given [series_selector](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#filtering).

Metric names are stripped from the resulting rollups. Add [keep_metric_names](#keep_metric_names) modifier in order to keep metric names.

This function is supported by PromQL.

See also [delta](#delta).


#### ideriv

`ideriv(series_selector[d])` is a [rollup function](#rollup-functions), which calculates the per-second derivative based
on the last two [raw samples](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#raw-samples)
over the given lookbehind window `d`. The derivative is calculated independently per each time series returned
from the given [series_selector](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#filtering).

Metric names are stripped from the resulting rollups. Add [keep_metric_names](#keep_metric_names) modifier in order to keep metric names.

See also [deriv](#deriv).


#### increase

`increase(series_selector[d])` is a [rollup function](#rollup-functions), which calculates the increase over the given lookbehind window `d`
per each time series returned from the given [series_selector](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#filtering).

Unlike Prometheus, it takes into account the last sample before the given lookbehind window `d` when calculating the result.
See [this article](https://medium.com/@romanhavronenko/victoriametrics-promql-compliance-d4318203f51e) for details.

Metric names are stripped from the resulting rollups. Add [keep_metric_names](#keep_metric_names) modifier in order to keep metric names.

This function is usually applied to [counters](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#counter).

This function is supported by PromQL.

See also [increase_pure](#increase_pure), [increase_prometheus](#increase_prometheus) and [delta](#delta).


#### increase_prometheus

`increase_prometheus(series_selector[d])` is a [rollup function](#rollup-functions), which calculates the increase
over the given lookbehind window `d` per each time series returned from the given [series_selector](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#filtering).
It doesn't take into account the last sample before the given lookbehind window `d` when calculating the result in the same way as Prometheus does.
See [this article](https://medium.com/@romanhavronenko/victoriametrics-promql-compliance-d4318203f51e) for details.

Metric names are stripped from the resulting rollups. Add [keep_metric_names](#keep_metric_names) modifier in order to keep metric names.

This function is usually applied to [counters](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#counter).

See also [increase_pure](#increase_pure) and [increase](#increase).


#### increase_pure

`increase_pure(series_selector[d])` is a [rollup function](#rollup-functions), which works the same as [increase](#increase) except
of the following corner case - it assumes that [counters](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#counter) always start from 0,
while [increase](#increase) ignores the first value in a series if it is too big.

This function is usually applied to [counters](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#counter).

See also [increase](#increase) and [increase_prometheus](#increase_prometheus).


#### increases_over_time

`increases_over_time(series_selector[d])` is a [rollup function](#rollup-functions), which calculates the number of [raw sample](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#raw-samples)
value increases over the given lookbehind window `d` per each time series returned from the given [series_selector](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#filtering).

Metric names are stripped from the resulting rollups. Add [keep_metric_names](#keep_metric_names) modifier in order to keep metric names.

See also [decreases_over_time](#decreases_over_time).


#### integrate

`integrate(series_selector[d])` is a [rollup function](#rollup-functions), which calculates the integral over [raw samples](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#raw-samples)
on the given lookbehind window `d` per each time series returned from the given [series_selector](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#filtering).

Metric names are stripped from the resulting rollups. Add [keep_metric_names](#keep_metric_names) modifier in order to keep metric names.

This function is usually applied to [gauges](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#gauge).


#### irate

`irate(series_selector[d])` is a [rollup function](#rollup-functions), which calculates the "instant" per-second increase rate over
the last two [raw samples](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#raw-samples)
on the given lookbehind window `d` per each time series returned from the given [series_selector](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#filtering).

Metric names are stripped from the resulting rollups. Add [keep_metric_names](#keep_metric_names) modifier in order to keep metric names.

This function is usually applied to [counters](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#counter).

This function is supported by PromQL.

See also [rate](#rate) and [rollup_rate](#rollup_rate).


#### lag

`lag(series_selector[d])` is a [rollup function](#rollup-functions), which returns the duration in seconds between the last sample
on the given lookbehind window `d` and the timestamp of the current point. It is calculated independently per each time series returned
from the given [series_selector](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#filtering).

Metric names are stripped from the resulting rollups. Add [keep_metric_names](#keep_metric_names) modifier in order to keep metric names.

See also [lifetime](#lifetime) and [duration_over_time](#duration_over_time).


#### last_over_time

`last_over_time(series_selector[d])` is a [rollup function](#rollup-functions), which returns the last [raw sample](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#raw-samples)
value on the given lookbehind window `d` per each time series returned from the given [series_selector](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#filtering).

This function is supported by PromQL.

See also [first_over_time](#first_over_time) and [tlast_over_time](#tlast_over_time).


#### lifetime

`lifetime(series_selector[d])` is a [rollup function](#rollup-functions), which returns the duration in seconds between the last and the first sample
on the given lookbehind window `d` per each time series returned from the given [series_selector](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#filtering).

Metric names are stripped from the resulting rollups. Add [keep_metric_names](#keep_metric_names) modifier in order to keep metric names.

See also [duration_over_time](#duration_over_time) and [lag](#lag).
