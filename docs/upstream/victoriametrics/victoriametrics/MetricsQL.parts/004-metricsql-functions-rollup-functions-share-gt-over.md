<!-- Part 4 of 8 of victoriametrics/MetricsQL.md (split because the page is big). -->

#### share_gt_over_time

`share_gt_over_time(series_selector[d], gt)` is a [rollup function](#rollup-functions), which returns share (in the range `[0...1]`)
of [raw samples](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#raw-samples)
on the given lookbehind window `d`, which are bigger than `gt`. It is calculated independently per each time series returned
from the given [series_selector](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#filtering).

This function is useful for calculating SLI and SLO. Example: `share_gt_over_time(up[24h], 0)` - returns service availability for the last 24 hours.

Metric names are stripped from the resulting rollups. Add [keep_metric_names](#keep_metric_names) modifier in order to keep metric names.

This function is usually applied to [gauges](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#gauge).

See also [share_le_over_time](#share_le_over_time) and [count_gt_over_time](#count_gt_over_time).


#### share_le_over_time

`share_le_over_time(series_selector[d], le)` is a [rollup function](#rollup-functions), which returns share (in the range `[0...1]`)
of [raw samples](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#raw-samples)
on the given lookbehind window `d`, which are smaller or equal to `le`. It is calculated independently per each time series returned
from the given [series_selector](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#filtering).

This function is useful for calculating SLI and SLO. Example: `share_le_over_time(memory_usage_bytes[24h], 100*1024*1024)` returns
the share of time series values for the last 24 hours when memory usage was below or equal to 100MB.

Metric names are stripped from the resulting rollups. Add [keep_metric_names](#keep_metric_names) modifier in order to keep metric names.

This function is usually applied to [gauges](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#gauge).

See also [share_gt_over_time](#share_gt_over_time) and [count_le_over_time](#count_le_over_time).


#### share_eq_over_time

`share_eq_over_time(series_selector[d], eq)` is a [rollup function](#rollup-functions), which returns share (in the range `[0...1]`)
of [raw samples](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#raw-samples)
on the given lookbehind window `d`, which are equal to `eq`. It is calculated independently per each time series returned
from the given [series_selector](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#filtering).

Metric names are stripped from the resulting rollups. Add [keep_metric_names](#keep_metric_names) modifier in order to keep metric names.

This function is usually applied to [gauges](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#gauge).

See also [count_eq_over_time](#count_eq_over_time).


#### stale_samples_over_time

`stale_samples_over_time(series_selector[d])` is a [rollup function](#rollup-functions), which calculates the number
of [staleness markers](https://docs.victoriametrics.com/victoriametrics/vmagent/#prometheus-staleness-markers) on the given lookbehind window `d`
per each time series matching the given [series_selector](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#filtering).

Metric names are stripped from the resulting rollups. Add [keep_metric_names](#keep_metric_names) modifier in order to keep metric names.


#### stddev_over_time

`stddev_over_time(series_selector[d])` is a [rollup function](#rollup-functions), which calculates standard deviation over [raw samples](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#raw-samples)
on the given lookbehind window `d` per each time series returned from the given [series_selector](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#filtering).

Metric names are stripped from the resulting rollups. Add [keep_metric_names](#keep_metric_names) modifier in order to keep metric names.

This function is usually applied to [gauges](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#gauge).

This function is supported by PromQL.

See also [stdvar_over_time](#stdvar_over_time).


#### stdvar_over_time

`stdvar_over_time(series_selector[d])` is a [rollup function](#rollup-functions), which calculates standard variance over [raw samples](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#raw-samples)
on the given lookbehind window `d` per each time series returned from the given [series_selector](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#filtering).

Metric names are stripped from the resulting rollups. Add [keep_metric_names](#keep_metric_names) modifier in order to keep metric names.

This function is usually applied to [gauges](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#gauge).

This function is supported by PromQL.

See also [stddev_over_time](#stddev_over_time).


#### sum_eq_over_time

`sum_eq_over_time(series_selector[d], eq)` is a [rollup function](#rollup-functions), which calculates the sum of [raw sample](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#raw-samples)
values equal to `eq` on the given lookbehind window `d` per each time series returned from the given [series_selector](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#filtering).

Metric names are stripped from the resulting rollups. Add [keep_metric_names](#keep_metric_names) modifier in order to keep metric names.

This function is usually applied to [gauges](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#gauge).

See also [sum_over_time](#sum_over_time) and [count_eq_over_time](#count_eq_over_time).


#### sum_gt_over_time

`sum_gt_over_time(series_selector[d], gt)` is a [rollup function](#rollup-functions), which calculates the sum of [raw sample](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#raw-samples)
values bigger than `gt` on the given lookbehind window `d` per each time series returned from the given [series_selector](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#filtering).

Metric names are stripped from the resulting rollups. Add [keep_metric_names](#keep_metric_names) modifier in order to keep metric names.

This function is usually applied to [gauges](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#gauge).

See also [sum_over_time](#sum_over_time) and [count_gt_over_time](#count_gt_over_time).


#### sum_le_over_time

`sum_le_over_time(series_selector[d], le)` is a [rollup function](#rollup-functions), which calculates the sum of [raw sample](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#raw-samples)
values smaller or equal to `le` on the given lookbehind window `d` per each time series returned from the given [series_selector](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#filtering).

Metric names are stripped from the resulting rollups. Add [keep_metric_names](#keep_metric_names) modifier in order to keep metric names.

This function is usually applied to [gauges](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#gauge).

See also [sum_over_time](#sum_over_time) and [count_le_over_time](#count_le_over_time).


#### sum_over_time

`sum_over_time(series_selector[d])` is a [rollup function](#rollup-functions), which calculates the sum of [raw sample](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#raw-samples) values
on the given lookbehind window `d` per each time series returned from the given [series_selector](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#filtering).

Metric names are stripped from the resulting rollups. Add [keep_metric_names](#keep_metric_names) modifier in order to keep metric names.

This function is usually applied to [gauges](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#gauge).

This function is supported by PromQL.


#### sum2_over_time

`sum2_over_time(series_selector[d])` is a [rollup function](#rollup-functions), which calculates the sum of squares for [raw sample](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#raw-samples)
values on the given lookbehind window `d` per each time series returned from the given [series_selector](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#filtering).

Metric names are stripped from the resulting rollups. Add [keep_metric_names](#keep_metric_names) modifier in order to keep metric names.

This function is usually applied to [gauges](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#gauge).


#### timestamp

`timestamp(series_selector[d])` is a [rollup function](#rollup-functions), which returns the timestamp in seconds with millisecond precision
for the last [raw sample](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#raw-samples)
on the given lookbehind window `d` per each time series returned from the given [series_selector](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#filtering).

Metric names are stripped from the resulting rollups. Add [keep_metric_names](#keep_metric_names) modifier in order to keep metric names.

This function is supported by PromQL.

See also [time](#time) and [now](#now).


#### timestamp_with_name

`timestamp_with_name(series_selector[d])` is a [rollup function](#rollup-functions), which returns the timestamp in seconds with millisecond precision
for the last [raw sample](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#raw-samples)
on the given lookbehind window `d` per each time series returned from the given [series_selector](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#filtering).

Metric names are preserved in the resulting rollups.

See also [timestamp](#timestamp) and [keep_metric_names](#keep_metric_names) modifier.


#### tfirst_over_time

`tfirst_over_time(series_selector[d])` is a [rollup function](#rollup-functions), which returns the timestamp in seconds with millisecond precision
for the first [raw sample](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#raw-samples)
on the given lookbehind window `d` per each time series returned from the given [series_selector](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#filtering).

Metric names are stripped from the resulting rollups. Add [keep_metric_names](#keep_metric_names) modifier in order to keep metric names.

See also [first_over_time](#first_over_time).


#### tlast_change_over_time

`tlast_change_over_time(series_selector[d])` is a [rollup function](#rollup-functions), which returns the timestamp in seconds with millisecond precision for the last change
per each time series returned from the given [series_selector](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#filtering) on the given lookbehind window `d`.

Metric names are stripped from the resulting rollups. Add [keep_metric_names](#keep_metric_names) modifier in order to keep metric names.

See also [last_over_time](#last_over_time).


#### tlast_over_time

`tlast_over_time(series_selector[d])` is a [rollup function](#rollup-functions), which is an alias for [timestamp](#timestamp).

See also [tlast_change_over_time](#tlast_change_over_time).


#### tmax_over_time

`tmax_over_time(series_selector[d])` is a [rollup function](#rollup-functions), which returns the timestamp in seconds with millisecond precision
for the [raw sample](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#raw-samples)
with the maximum value on the given lookbehind window `d`. It is calculated independently per each time series returned
from the given [series_selector](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#filtering).

Metric names are stripped from the resulting rollups. Add [keep_metric_names](#keep_metric_names) modifier in order to keep metric names.

See also [max_over_time](#max_over_time).


#### tmin_over_time

`tmin_over_time(series_selector[d])` is a [rollup function](#rollup-functions), which returns the timestamp in seconds with millisecond precision
for the [raw sample](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#raw-samples)
with the minimum value on the given lookbehind window `d`. It is calculated independently per each time series returned
from the given [series_selector](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#filtering).

Metric names are stripped from the resulting rollups. Add [keep_metric_names](#keep_metric_names) modifier in order to keep metric names.

See also [min_over_time](#min_over_time).


#### zscore_over_time

`zscore_over_time(series_selector[d])` is a [rollup function](#rollup-functions), which returns [z-score](https://en.wikipedia.org/wiki/Standard_score)
for [raw samples](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#raw-samples) on the given lookbehind window `d`. It is calculated independently per each time series returned
from the given [series_selector](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#filtering).

Metric names are stripped from the resulting rollups. Add [keep_metric_names](#keep_metric_names) modifier in order to keep metric names.

This function is usually applied to [gauges](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#gauge).

See also [zscore](#zscore), [range_trim_zscore](#range_trim_zscore) and [outlier_iqr_over_time](#outlier_iqr_over_time).
