<!-- Part 3 of 8 of victoriametrics/MetricsQL.md (split because the page is big). -->

#### mad_over_time

`mad_over_time(series_selector[d])` is a [rollup function](#rollup-functions), which calculates [median absolute deviation](https://en.wikipedia.org/wiki/Median_absolute_deviation)
over [raw samples](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#raw-samples) on the given lookbehind window `d` per each time series returned
from the given [series_selector](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#filtering).

This function is usually applied to [gauges](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#gauge).

See also [mad](#mad), [range_mad](#range_mad) and [outlier_iqr_over_time](#outlier_iqr_over_time).


#### max_over_time

`max_over_time(series_selector[d])` is a [rollup function](#rollup-functions), which calculates the maximum value over [raw samples](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#raw-samples)
on the given lookbehind window `d` per each time series returned from the given [series_selector](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#filtering).

This function is usually applied to [gauges](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#gauge).

This function is supported by PromQL.

See also [tmax_over_time](#tmax_over_time) and [min_over_time](#min_over_time).


#### median_over_time

`median_over_time(series_selector[d])` is a [rollup function](#rollup-functions), which calculates median value over [raw samples](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#raw-samples)
on the given lookbehind window `d` per each time series returned
from the given [series_selector](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#filtering).

This function is usually applied to [gauges](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#gauge).

See also [avg_over_time](#avg_over_time).


#### min_over_time

`min_over_time(series_selector[d])` is a [rollup function](#rollup-functions), which calculates the minimum value over [raw samples](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#raw-samples)
on the given lookbehind window `d` per each time series returned from the given [series_selector](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#filtering).

This function is usually applied to [gauges](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#gauge).

This function is supported by PromQL.

See also [tmin_over_time](#tmin_over_time) and [max_over_time](#max_over_time).


#### mode_over_time

`mode_over_time(series_selector[d])` is a [rollup function](#rollup-functions), which calculates [mode](https://en.wikipedia.org/wiki/Mode_(statistics))
for [raw samples](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#raw-samples) on the given lookbehind window `d`. It is calculated individually per each time series returned
from the given [series_selector](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#filtering). It is expected that [raw sample](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#raw-samples)
values are discrete.

This function is usually applied to [gauges](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#gauge).


#### outlier_iqr_over_time

`outlier_iqr_over_time(series_selector[d])` is a [rollup function](#rollup-functions), which returns the last sample on the given lookbehind window `d`
if its value is either smaller than the `q25-1.5*iqr` or bigger than `q75+1.5*iqr` where:

* `iqr` is an [Interquartile range](https://en.wikipedia.org/wiki/Interquartile_range) over [raw samples](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#raw-samples) on the lookbehind window `d`
* `q25` and `q75` are 25th and 75th [percentiles](https://en.wikipedia.org/wiki/Percentile) over [raw samples](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#raw-samples) on the lookbehind window `d`.

The `outlier_iqr_over_time()` is useful for detecting anomalies in gauge values based on the previous history of values.
For example, `outlier_iqr_over_time(memory_usage_bytes[1h])` triggers when `memory_usage_bytes` suddenly goes outside the usual value range for the last hour.

This function is usually applied to [gauges](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#gauge).

See also [outliers_iqr](#outliers_iqr).


#### predict_linear

`predict_linear(series_selector[d], t)` is a [rollup function](#rollup-functions), which calculates the value `t` seconds in the future using
linear interpolation over [raw samples](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#raw-samples) on the given lookbehind window `d`.
The predicted value is calculated individually per each time series returned from the given [series_selector](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#filtering).

This function is supported by PromQL.

See also [range_linear_regression](#range_linear_regression).


#### present_over_time

`present_over_time(series_selector[d])` is a [rollup function](#rollup-functions), which returns 1 if there is at least a single [raw sample](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#raw-samples)
on the given lookbehind window `d`. Otherwise, an empty result is returned.

Metric names are stripped from the resulting rollups. Add [keep_metric_names](#keep_metric_names) modifier in order to keep metric names.

This function is supported by PromQL.


#### quantile_over_time

`quantile_over_time(phi, series_selector[d])` is a [rollup function](#rollup-functions), which calculates `phi`-quantile over [raw samples](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#raw-samples)
on the given lookbehind window `d` per each time series returned from the given [series_selector](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#filtering).
The `phi` value must be in the range `[0...1]`.

This function is usually applied to [gauges](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#gauge).

This function is supported by PromQL.

See also [quantiles_over_time](#quantiles_over_time).


#### quantiles_over_time

`quantiles_over_time("phiLabel", phi1, ..., phiN, series_selector[d])` is a [rollup function](#rollup-functions), which calculates `phi*`-quantiles
over [raw samples](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#raw-samples) on the given lookbehind window `d` per each time series returned
from the given [series_selector](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#filtering).
The function returns individual series per each `phi*` with `{phiLabel="phi*"}` label. `phi*` values must be in the range `[0...1]`.

This function is usually applied to [gauges](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#gauge).

See also [quantile_over_time](#quantile_over_time).


#### range_over_time

`range_over_time(series_selector[d])` is a [rollup function](#rollup-functions), which calculates value range over [raw samples](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#raw-samples)
on the given lookbehind window `d` per each time series returned from the given [series_selector](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#filtering).
E.g. it calculates `max_over_time(series_selector[d]) - min_over_time(series_selector[d])`.

Metric names are stripped from the resulting rollups. Add [keep_metric_names](#keep_metric_names) modifier in order to keep metric names.

This function is usually applied to [gauges](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#gauge).


#### rate

`rate(series_selector[d])` is a [rollup function](#rollup-functions), which calculates the average per-second increase rate
over the given lookbehind window `d` per each time series returned from the given [series_selector](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#filtering).

If the lookbehind window is skipped in square brackets, then it is automatically calculated as `max(step, scrape_interval)`, where `step` is the query arg value
passed to [/api/v1/query_range](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#range-query) or [/api/v1/query](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#instant-query),
while `scrape_interval` is the interval between [raw samples](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#raw-samples) for the selected time series.
This allows avoiding unexpected gaps on the graph when `step` is smaller than the `scrape_interval`.

Metric names are stripped from the resulting rollups. Add [keep_metric_names](#keep_metric_names) modifier in order to keep metric names.

This function is supported by PromQL.

See also [irate](#irate), [rollup_rate](#rollup_rate) and [rate_prometheus](#rate_prometheus).


#### rate_prometheus

`rate_prometheus(series_selector[d])` {{% available_from "v1.120.0" %}} is a [rollup function](#rollup-functions), which calculates the average per-second
increase rate over the given lookbehind window `d` per each time series returned from the given [series_selector](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#filtering).
The resulting calculation is equivalent to `increase_prometheus(series_selector[d]) / d`.

It doesn't take into account the last sample before the given lookbehind window `d` when calculating the result in the same way as Prometheus does.
See [this article](https://medium.com/@romanhavronenko/victoriametrics-promql-compliance-d4318203f51e) for details.

Metric names are stripped from the resulting rollups. Add [keep_metric_names](#keep_metric_names) modifier in order to keep metric names.

This function is usually applied to [counters](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#counter).

See also [increase_prometheus](#increase_prometheus) and [rate](#rate).


#### rate_over_sum

`rate_over_sum(series_selector[d])` is a [rollup function](#rollup-functions), which calculates per-second rate over the sum of [raw samples](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#raw-samples)
on the given lookbehind window `d`. The calculations are performed individually per each time series returned
from the given [series_selector](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#filtering).

This function is usually applied to [gauges](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#gauge).

Metric names are stripped from the resulting rollups. Add [keep_metric_names](#keep_metric_names) modifier in order to keep metric names.


#### resets

`resets(series_selector[d])` is a [rollup function](#rollup-functions), which returns the number
of [counter](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#counter) resets over the given lookbehind window `d`
per each time series returned from the given [series_selector](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#filtering).

Metric names are stripped from the resulting rollups. Add [keep_metric_names](#keep_metric_names) modifier in order to keep metric names.

This function is usually applied to [counters](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#counter).

This function is supported by PromQL.


#### rollup

`rollup(series_selector[d])` is a [rollup function](#rollup-functions), which calculates `min`, `max` and `avg` values for [raw samples](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#raw-samples)
on the given lookbehind window `d` and returns them in time series with `rollup="min"`, `rollup="max"` and `rollup="avg"` additional labels.
These values are calculated individually per each time series returned from the given [series_selector](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#filtering).

Optional 2nd argument `"min"`, `"max"` or `"avg"` can be passed to keep only one calculation result and without adding a label.
See also [label_match](#label_match).

This function is usually applied to [gauges](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#gauge).

See also [rollup_rate](#rollup_rate).


#### rollup_candlestick

`rollup_candlestick(series_selector[d])` is a [rollup function](#rollup-functions), which calculates `open`, `high`, `low` and `close` values (aka OHLC)
over [raw samples](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#raw-samples) on the given lookbehind window `d` and returns them in time series
with `rollup="open"`, `rollup="high"`, `rollup="low"` and `rollup="close"` additional labels.
The calculations are performed individually per each time series returned
from the given [series_selector](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#filtering). This function is useful for financial applications.

Optional 2nd argument `"open"`, `"high"` or `"low"` or `"close"` can be passed to keep only one calculation result and without adding a label.
See also [label_match](#label_match).

This function is usually applied to [gauges](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#gauge).


#### rollup_delta

`rollup_delta(series_selector[d])` is a [rollup function](#rollup-functions), which calculates differences between adjacent [raw samples](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#raw-samples)
on the given lookbehind window `d` and returns `min`, `max` and `avg` values for the calculated differences
and returns them in time series with `rollup="min"`, `rollup="max"` and `rollup="avg"` additional labels.
The calculations are performed individually per each time series returned from the given [series_selector](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#filtering).

Optional 2nd argument `"min"`, `"max"` or `"avg"` can be passed to keep only one calculation result and without adding a label.
See also [label_match](#label_match).

Metric names are stripped from the resulting rollups. Add [keep_metric_names](#keep_metric_names) modifier in order to keep metric names.

See also [rollup_increase](#rollup_increase).


#### rollup_deriv

`rollup_deriv(series_selector[d])` is a [rollup function](#rollup-functions), which calculates per-second derivatives
for adjacent [raw samples](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#raw-samples) on the given lookbehind window `d` and returns `min`, `max` and `avg` values
for the calculated per-second derivatives and returns them in time series with `rollup="min"`, `rollup="max"` and `rollup="avg"` additional labels.
The calculations are performed individually per each time series returned from the given [series_selector](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#filtering).

Optional 2nd argument `"min"`, `"max"` or `"avg"` can be passed to keep only one calculation result and without adding a label.
See also [label_match](#label_match).

Metric names are stripped from the resulting rollups. Add [keep_metric_names](#keep_metric_names) modifier in order to keep metric names.

See also [rollup](#rollup) and [rollup_rate](#rollup_rate).


#### rollup_increase

`rollup_increase(series_selector[d])` is a [rollup function](#rollup-functions), which calculates increases for adjacent [raw samples](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#raw-samples)
on the given lookbehind window `d` and returns `min`, `max` and `avg` values for the calculated increases
and returns them in time series with `rollup="min"`, `rollup="max"` and `rollup="avg"` additional labels.
The calculations are performed individually per each time series returned from the given [series_selector](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#filtering).

Optional 2nd argument `"min"`, `"max"` or `"avg"` can be passed to keep only one calculation result and without adding a label.
See also [label_match](#label_match).

Metric names are stripped from the resulting rollups. Add [keep_metric_names](#keep_metric_names) modifier in order to keep metric names. See also [rollup_delta](#rollup_delta).

This function is usually applied to [counters](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#counter).

See also [rollup](#rollup) and [rollup_rate](#rollup_rate).


#### rollup_rate

`rollup_rate(series_selector[d])` is a [rollup function](#rollup-functions), which calculates per-second change rates
for adjacent [raw samples](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#raw-samples)
on the given lookbehind window `d` and returns `min`, `max` and `avg` values for the calculated per-second change rates
and returns them in time series with `rollup="min"`, `rollup="max"` and `rollup="avg"` additional labels.
The calculations are performed individually per each time series returned from the given [series_selector](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#filtering).

See [this article](https://valyala.medium.com/why-irate-from-prometheus-doesnt-capture-spikes-45f9896d7832) in order to understand better
when to use `rollup_rate()`.

Optional 2nd argument `"min"`, `"max"` or `"avg"` can be passed to keep only one calculation result and without adding a label.
See also [label_match](#label_match).

Metric names are stripped from the resulting rollups. Add [keep_metric_names](#keep_metric_names) modifier in order to keep metric names.

This function is usually applied to [counters](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#counter).

See also [rollup](#rollup) and [rollup_increase](#rollup_increase).


#### rollup_scrape_interval

`rollup_scrape_interval(series_selector[d])` is a [rollup function](#rollup-functions), which calculates the interval in seconds between
adjacent [raw samples](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#raw-samples) on the given lookbehind window `d` and returns `min`, `max` and `avg` values for the calculated interval
and returns them in time series with `rollup="min"`, `rollup="max"` and `rollup="avg"` additional labels.
The calculations are performed individually per each time series returned from the given [series_selector](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#filtering).

Optional 2nd argument `"min"`, `"max"` or `"avg"` can be passed to keep only one calculation result and without adding a label.
See also [label_match](#label_match).

Metric names are stripped from the resulting rollups. Add [keep_metric_names](#keep_metric_names) modifier in order to keep metric names. See also [scrape_interval](#scrape_interval).


#### scrape_interval

`scrape_interval(series_selector[d])` is a [rollup function](#rollup-functions), which calculates the average interval in seconds
between [raw samples](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#raw-samples)
on the given lookbehind window `d` per each time series returned from the given [series_selector](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#filtering).

Metric names are stripped from the resulting rollups. Add [keep_metric_names](#keep_metric_names) modifier in order to keep metric names.

See also [rollup_scrape_interval](#rollup_scrape_interval).
