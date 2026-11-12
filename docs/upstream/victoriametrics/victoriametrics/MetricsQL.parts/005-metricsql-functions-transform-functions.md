<!-- Part 5 of 8 of victoriametrics/MetricsQL.md (split because the page is big). -->

### Transform functions

**Transform functions** calculate transformations over [rollup results](#rollup-functions).
For example, `abs(delta(temperature[24h]))` calculates the absolute value for every point of every time series
returned from the rollup `delta(temperature[24h])`.

Additional details:

* If transform function is applied directly to a [series selector](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#filtering),
  then the [default_rollup()](#default_rollup) function is automatically applied before calculating the transformations.
  For example, `abs(temperature)` is implicitly transformed to `abs(default_rollup(temperature))`.
* All the transform functions accept optional `keep_metric_names` modifier. If it is set,
  then the function doesn't drop metric names from the resulting time series. See [these docs](#keep_metric_names).

See also [implicit query conversions](#implicit-query-conversions).

The list of supported transform functions:

#### abs

`abs(q)` is a [transform function](#transform-functions), which calculates the absolute value for every point of every time series returned by `q`.

This function is supported by PromQL.

#### absent

`absent(q)` is a [transform function](#transform-functions), which returns 1 if `q` has no points. Otherwise, returns an empty result.

This function is supported by PromQL.

See also [absent_over_time](#absent_over_time).

#### acos

`acos(q)` is a [transform function](#transform-functions), which returns [inverse cosine](https://en.wikipedia.org/wiki/Inverse_trigonometric_functions)
for every point of every time series returned by `q`.

Metric names are stripped from the resulting series. Add [keep_metric_names](#keep_metric_names) modifier in order to keep metric names.

This function is supported by PromQL.

See also [asin](#asin) and [cos](#cos).

#### acosh

`acosh(q)` is a [transform function](#transform-functions), which returns
[inverse hyperbolic cosine](https://en.wikipedia.org/wiki/Inverse_hyperbolic_functions#Definitions_in_terms_of_logarithms) for every point of every time series returned by `q`.

Metric names are stripped from the resulting series. Add [keep_metric_names](#keep_metric_names) modifier in order to keep metric names.

This function is supported by PromQL.

See also [sinh](#cosh).

#### asin

`asin(q)` is a [transform function](#transform-functions), which returns [inverse sine](https://en.wikipedia.org/wiki/Inverse_trigonometric_functions)
for every point of every time series returned by `q`.

Metric names are stripped from the resulting series. Add [keep_metric_names](#keep_metric_names) modifier in order to keep metric names.

This function is supported by PromQL.

See also [acos](#acos) and [sin](#sin).

#### asinh

`asinh(q)` is a [transform function](#transform-functions), which returns
[inverse hyperbolic sine](https://en.wikipedia.org/wiki/Inverse_hyperbolic_functions#Definitions_in_terms_of_logarithms) for every point of every time series returned by `q`.

Metric names are stripped from the resulting series. Add [keep_metric_names](#keep_metric_names) modifier in order to keep metric names.

This function is supported by PromQL.

See also [sinh](#sinh).

#### atan

`atan(q)` is a [transform function](#transform-functions), which returns [inverse tangent](https://en.wikipedia.org/wiki/Inverse_trigonometric_functions)
for every point of every time series returned by `q`.

Metric names are stripped from the resulting series. Add [keep_metric_names](#keep_metric_names) modifier in order to keep metric names.

This function is supported by PromQL.

See also [tan](#tan).

#### atanh

`atanh(q)` is a [transform function](#transform-functions), which returns
[inverse hyperbolic tangent](https://en.wikipedia.org/wiki/Inverse_hyperbolic_functions#Definitions_in_terms_of_logarithms) for every point of every time series returned by `q`.

Metric names are stripped from the resulting series. Add [keep_metric_names](#keep_metric_names) modifier in order to keep metric names.

This function is supported by PromQL.

See also [tanh](#tanh).

#### bitmap_and

`bitmap_and(q, mask)` is a [transform function](#transform-functions), which calculates bitwise `v & mask` for every `v` point of every time series returned from `q`.

Metric names are stripped from the resulting series. Add [keep_metric_names](#keep_metric_names) modifier in order to keep metric names.

#### bitmap_or

`bitmap_or(q, mask)` is a [transform function](#transform-functions), which calculates bitwise `v | mask` for every `v` point of every time series returned from `q`.

Metric names are stripped from the resulting series. Add [keep_metric_names](#keep_metric_names) modifier in order to keep metric names.

#### bitmap_xor

`bitmap_xor(q, mask)` is a [transform function](#transform-functions), which calculates bitwise `v ^ mask` for every `v` point of every time series returned from `q`.

Metric names are stripped from the resulting series. Add [keep_metric_names](#keep_metric_names) modifier in order to keep metric names.

#### buckets_limit

`buckets_limit(limit, buckets)` is a [transform function](#transform-functions), which limits the number
of [histogram buckets](https://valyala.medium.com/improving-histogram-usability-for-prometheus-and-grafana-bc7e5df0e350) to the given `limit`. 

The given `limit` should be greater than `0`. If it is less than `3`, it will be automatically raised to `3` to preserve the first and last buckets for better accuracy of min and max values.

See also [prometheus_buckets](#prometheus_buckets) and [histogram_quantile](#histogram_quantile).

#### ceil

`ceil(q)` is a [transform function](#transform-functions), which rounds every point for every time series returned by `q` to the upper nearest integer.

This function is supported by PromQL.

See also [floor](#floor) and [round](#round).

#### clamp

`clamp(q, min, max)` is a [transform function](#transform-functions), which clamps every point for every time series returned by `q` with the given `min` and `max` values.

This function is supported by PromQL.

See also [clamp_min](#clamp_min) and [clamp_max](#clamp_max).

#### clamp_max

`clamp_max(q, max)` is a [transform function](#transform-functions), which clamps every point for every time series returned by `q` with the given `max` value.

This function is supported by PromQL.

See also [clamp](#clamp) and [clamp_min](#clamp_min).

#### clamp_min

`clamp_min(q, min)` is a [transform function](#transform-functions), which clamps every point for every time series returned by `q` with the given `min` value.

This function is supported by PromQL.

See also [clamp](#clamp) and [clamp_max](#clamp_max).

#### cos

`cos(q)` is a [transform function](#transform-functions), which returns `cos(v)` for every `v` point of every time series returned by `q`.

Metric names are stripped from the resulting series. Add [keep_metric_names](#keep_metric_names) modifier in order to keep metric names.

This function is supported by PromQL.

See also [sin](#sin).

#### cosh

`cosh(q)` is a [transform function](#transform-functions), which returns [hyperbolic cosine](https://en.wikipedia.org/wiki/Hyperbolic_functions)
for every point of every time series returned by `q`.

Metric names are stripped from the resulting series. Add [keep_metric_names](#keep_metric_names) modifier in order to keep metric names.

This function is supported by PromQL.

See also [acosh](#acosh).

#### day_of_month

`day_of_month(q)` is a [transform function](#transform-functions), which returns the day of month for every point of every time series returned by `q`.
It is expected that `q` returns unix timestamps. The returned values are in the range `[1...31]`.

Metric names are stripped from the resulting series. Add [keep_metric_names](#keep_metric_names) modifier in order to keep metric names.

This function is supported by PromQL.

See also [day_of_week](#day_of_week) and [day_of_year](#day_of_year).

#### day_of_week

`day_of_week(q)` is a [transform function](#transform-functions), which returns the day of week for every point of every time series returned by `q`.
It is expected that `q` returns unix timestamps. The returned values are in the range `[0...6]`, where `0` means Sunday and `6` means Saturday.

Metric names are stripped from the resulting series. Add [keep_metric_names](#keep_metric_names) modifier in order to keep metric names.

This function is supported by PromQL.

See also [day_of_month](#day_of_month) and [day_of_year](#day_of_year).

#### day_of_year

`day_of_year(q)` is a [transform function](#transform-functions), which returns the day of year for every point of every time series returned by `q`.
It is expected that `q` returns unix timestamps. The returned values are in the range `[1...365]` for non-leap years, and `[1 to 366]` in leap years.

Metric names are stripped from the resulting series. Add [keep_metric_names](#keep_metric_names) modifier in order to keep metric names.

This function is supported by PromQL.

See also [day_of_week](#day_of_week) and [day_of_month](#day_of_month).

#### days_in_month

`days_in_month(q)` is a [transform function](#transform-functions), which returns the number of days in the month identified
by every point of every time series returned by `q`. It is expected that `q` returns unix timestamps.
The returned values are in the range `[28...31]`.

Metric names are stripped from the resulting series. Add [keep_metric_names](#keep_metric_names) modifier in order to keep metric names.

This function is supported by PromQL.

#### deg

`deg(q)` is a [transform function](#transform-functions), which converts [Radians to degrees](https://en.wikipedia.org/wiki/Radian#Conversions)
for every point of every time series returned by `q`.

Metric names are stripped from the resulting series. Add [keep_metric_names](#keep_metric_names) modifier in order to keep metric names.

This function is supported by PromQL.

See also [rad](#rad).

#### drop_empty_series

`drop_empty_series(q)` is a [transform function](#transform-functions), which drops empty series from `q`.

This function can be used when `default` operator should be applied only to non-empty series. For example,
`drop_empty_series(temperature < 30) default 42` returns series, which have at least a single sample smaller than 30 on the selected time range,
while filling gaps in the returned series with 42.

On the other hand `(temperature < 30) default 40` returns all the `temperature` series, even if they have no samples smaller than 30,
by replacing all the values bigger or equal to 30 with 40.

#### end

`end()` is a [transform function](#transform-functions), which returns the unix timestamp in seconds for the last point.
It is known as `end` query arg passed to [/api/v1/query_range](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#range-query).

See also [start](#start), [time](#time) and [now](#now).

#### exp

`exp(q)` is a [transform function](#transform-functions), which calculates the `e^v` for every point `v` of every time series returned by `q`.

Metric names are stripped from the resulting series. Add [keep_metric_names](#keep_metric_names) modifier in order to keep metric names.

This function is supported by PromQL.

See also [ln](#ln).

#### floor

`floor(q)` is a [transform function](#transform-functions), which rounds every point for every time series returned by `q` to the lower nearest integer.

This function is supported by PromQL.

See also [ceil](#ceil) and [round](#round).

#### histogram_avg

`histogram_avg(buckets)` is a [transform function](#transform-functions), which calculates the average value for the given `buckets`.
It can be used for calculating the average over the given time range across multiple time series.
For example, `histogram_avg(sum(histogram_over_time(response_time_duration_seconds[5m])) by (vmrange,job))` would return the average response time
per each `job` over the last 5 minutes.

#### histogram_fraction

`histogram_fraction(lowerLe, upperLe, buckets)` is a [transform function](#transform-functions), which calculates the share (in the range `[0...1]`) for `buckets` that fall between `lowerLe` and `upperLe`.
The result of `histogram_fraction(lowerLe, upperLe, buckets)` is equivalent to `histogram_share(upperLe, buckets) - histogram_share(lowerLe, buckets)`.

This function is supported by PromQL.

See also [histogram_share](#histogram_share).

#### histogram_quantile

`histogram_quantile(phi, buckets)` is a [transform function](#transform-functions), which calculates `phi`-[percentile](https://en.wikipedia.org/wiki/Percentile)
over the given [histogram buckets](https://valyala.medium.com/improving-histogram-usability-for-prometheus-and-grafana-bc7e5df0e350).
`phi` must be in the range `[0...1]`. For example, `histogram_quantile(0.5, sum(rate(http_request_duration_seconds_bucket[5m])) by (le))`
would return median request duration for all the requests during the last 5 minutes.

The function accepts optional third arg - `boundsLabel`. In this case it returns `lower` and `upper` bounds for the estimated percentile with the given `boundsLabel` label.
See [this issue for details](https://github.com/prometheus/prometheus/issues/5706).

When the [percentile](https://en.wikipedia.org/wiki/Percentile) is calculated over multiple histograms,
then all the input histograms **must** have buckets with identical boundaries, e.g. they must have the same set of `le` or `vmrange` labels.
Otherwise, the returned result may be invalid. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/3231) for details.

This function is supported by PromQL (except of the `boundLabel` arg).

See also [histogram_quantiles](#histogram_quantiles), [histogram_share](#histogram_share) and [quantile](#quantile).

#### histogram_quantiles

`histogram_quantiles("phiLabel", phi1, ..., phiN, buckets)` is a [transform function](#transform-functions), which calculates the given `phi*`-quantiles
over the given [histogram buckets](https://valyala.medium.com/improving-histogram-usability-for-prometheus-and-grafana-bc7e5df0e350).
Argument `phi*` must be in the range `[0...1]`. For example, `histogram_quantiles('le', 0.3, 0.5, sum(rate(http_request_duration_seconds_bucket[5m]) by (le))`.
Each calculated quantile is returned in a separate time series with the corresponding `{phiLabel="phi*"}` label.

See also [histogram_quantile](#histogram_quantile).

#### histogram_share

`histogram_share(le, buckets)` is a [transform function](#transform-functions), which calculates the share (in the range `[0...1]`)
for `buckets` that fall below `le`. This function is useful for calculating SLI and SLO. This is inverse to [histogram_quantile](#histogram_quantile).

The function accepts optional third arg - `boundsLabel`. In this case it returns `lower` and `upper` bounds for the estimated share with the given `boundsLabel` label.

#### histogram_stddev

`histogram_stddev(buckets)` is a [transform function](#transform-functions), which calculates standard deviation for the given `buckets`.

#### histogram_stdvar

`histogram_stdvar(buckets)` is a [transform function](#transform-functions), which calculates standard variance for the given `buckets`.
It can be used for calculating standard deviation over the given time range across multiple time series.
For example, `histogram_stdvar(sum(histogram_over_time(temperature[24])) by (vmrange,country))` would return standard deviation
for the temperature per each country over the last 24 hours.

#### hour

`hour(q)` is a [transform function](#transform-functions), which returns the hour for every point of every time series returned by `q`.
It is expected that `q` returns unix timestamps. The returned values are in the range `[0...23]`.

Metric names are stripped from the resulting series. Add [keep_metric_names](#keep_metric_names) modifier in order to keep metric names.

This function is supported by PromQL.

#### interpolate

`interpolate(q)` is a [transform function](#transform-functions), which fills gaps with linearly interpolated values calculated
from the last and the next non-empty points per each time series returned by `q`.

See also [keep_last_value](#keep_last_value) and [keep_next_value](#keep_next_value).

#### keep_last_value

`keep_last_value(q)` is a [transform function](#transform-functions), which fills gaps with the value of the last non-empty point
in every time series returned by `q`.

See also [keep_next_value](#keep_next_value) and [interpolate](#interpolate).

#### keep_next_value

`keep_next_value(q)` is a [transform function](#transform-functions), which fills gaps with the value of the next non-empty point
in every time series returned by `q`.

See also [keep_last_value](#keep_last_value) and [interpolate](#interpolate).

#### limit_offset

`limit_offset(limit, offset, q)` is a [transform function](#transform-functions), which skips `offset` time series from series returned by `q`
and then returns up to `limit` of the remaining time series per each group.

This allows implementing simple paging for `q` time series. See also [limitk](#limitk).

#### ln

`ln(q)` is a [transform function](#transform-functions), which calculates `ln(v)` for every point `v` of every time series returned by `q`.

Metric names are stripped from the resulting series. Add [keep_metric_names](#keep_metric_names) modifier in order to keep metric names.

This function is supported by PromQL.

See also [exp](#exp) and [log2](#log2).

#### log2

`log2(q)` is a [transform function](#transform-functions), which calculates `log2(v)` for every point `v` of every time series returned by `q`.

Metric names are stripped from the resulting series. Add [keep_metric_names](#keep_metric_names) modifier in order to keep metric names.

This function is supported by PromQL.

See also [log10](#log10) and [ln](#ln).

#### log10

`log10(q)` is a [transform function](#transform-functions), which calculates `log10(v)` for every point `v` of every time series returned by `q`.

Metric names are stripped from the resulting series. Add [keep_metric_names](#keep_metric_names) modifier in order to keep metric names.

This function is supported by PromQL.

See also [log2](#log2) and [ln](#ln).

#### minute

`minute(q)` is a [transform function](#transform-functions), which returns the minute for every point of every time series returned by `q`.
It is expected that `q` returns unix timestamps. The returned values are in the range `[0...59]`.

Metric names are stripped from the resulting series. Add [keep_metric_names](#keep_metric_names) modifier in order to keep metric names.

This function is supported by PromQL.

#### month

`month(q)` is a [transform function](#transform-functions), which returns the month for every point of every time series returned by `q`.
It is expected that `q` returns unix timestamps. The returned values are in the range `[1...12]`, where `1` means January and `12` means December.

Metric names are stripped from the resulting series. Add [keep_metric_names](#keep_metric_names) modifier in order to keep metric names.

This function is supported by PromQL.

#### now

`now()` is a [transform function](#transform-functions), which returns the current timestamp as a floating-point value in seconds.

See also [time](#time).

#### pi

`pi()` is a [transform function](#transform-functions), which returns [Pi number](https://en.wikipedia.org/wiki/Pi).

This function is supported by PromQL.

#### rad

`rad(q)` is a [transform function](#transform-functions), which converts [degrees to Radians](https://en.wikipedia.org/wiki/Radian#Conversions)
for every point of every time series returned by `q`.

Metric names are stripped from the resulting series. Add [keep_metric_names](#keep_metric_names) modifier in order to keep metric names.

This function is supported by PromQL.

See also [deg](#deg).

#### prometheus_buckets

`prometheus_buckets(buckets)` is a [transform function](#transform-functions), which converts
[VictoriaMetrics histogram buckets](https://valyala.medium.com/improving-histogram-usability-for-prometheus-and-grafana-bc7e5df0e350) with `vmrange` labels
to Prometheus histogram buckets with `le` labels. This may be useful for building heatmaps in Grafana.

See also [histogram_quantile](#histogram_quantile) and [buckets_limit](#buckets_limit).

#### rand

`rand(seed)` is a [transform function](#transform-functions), which returns pseudo-random numbers on the range `[0...1]` with even distribution.
Optional `seed` can be used as a seed for pseudo-random number generator.

See also [rand_normal](#rand_normal) and [rand_exponential](#rand_exponential).

#### rand_exponential

`rand_exponential(seed)` is a [transform function](#transform-functions), which returns pseudo-random numbers
with [exponential distribution](https://en.wikipedia.org/wiki/Exponential_distribution). Optional `seed` can be used as a seed for pseudo-random number generator.

See also [rand](#rand) and [rand_normal](#rand_normal).

#### rand_normal

`rand_normal(seed)` is a [transform function](#transform-functions), which returns pseudo-random numbers
with [normal distribution](https://en.wikipedia.org/wiki/Normal_distribution). Optional `seed` can be used as a seed for pseudo-random number generator.

See also [rand](#rand) and [rand_exponential](#rand_exponential).

#### range_avg

`range_avg(q)` is a [transform function](#transform-functions), which calculates the avg value across points per each time series returned by `q`.

#### range_first

`range_first(q)` is a [transform function](#transform-functions), which returns the value for the first point per each time series returned by `q`.

#### range_last

`range_last(q)` is a [transform function](#transform-functions), which returns the value for the last point per each time series returned by `q`.

#### range_linear_regression

`range_linear_regression(q)` is a [transform function](#transform-functions), which calculates [simple linear regression](https://en.wikipedia.org/wiki/Simple_linear_regression)
over the selected time range per each time series returned by `q`. This function is useful for capacity planning and predictions.

#### range_mad

`range_mad(q)` is a [transform function](#transform-functions), which calculates the [median absolute deviation](https://en.wikipedia.org/wiki/Median_absolute_deviation)
across points per each time series returned by `q`.

See also [mad](#mad) and [mad_over_time](#mad_over_time).

#### range_max

`range_max(q)` is a [transform function](#transform-functions), which calculates the max value across points per each time series returned by `q`.

#### range_median

`range_median(q)` is a [transform function](#transform-functions), which calculates the median value across points per each time series returned by `q`.

#### range_min

`range_min(q)` is a [transform function](#transform-functions), which calculates the min value across points per each time series returned by `q`.

#### range_normalize

`range_normalize(q1, ...)` is a [transform function](#transform-functions), which normalizes values for time series returned by `q1, ...` into `[0 ... 1]` range.
This function is useful for correlating time series with distinct value ranges.

See also [share](#share).

#### range_quantile

`range_quantile(phi, q)` is a [transform function](#transform-functions), which returns `phi`-quantile across points per each time series returned by `q`.
`phi` must be in the range `[0...1]`.

#### range_stddev

`range_stddev(q)` is a [transform function](#transform-functions), which calculates [standard deviation](https://en.wikipedia.org/wiki/Standard_deviation)
per each time series returned by `q` on the selected time range.

#### range_stdvar

`range_stdvar(q)` is a [transform function](#transform-functions), which calculates [standard variance](https://en.wikipedia.org/wiki/Variance)
per each time series returned by `q` on the selected time range.

#### range_sum

`range_sum(q)` is a [transform function](#transform-functions), which calculates the sum of points per each time series returned by `q`.

#### range_trim_outliers

`range_trim_outliers(k, q)` is a [transform function](#transform-functions), which drops points located farther than `k*range_mad(q)`
from the `range_median(q)`. E.g. it is equivalent to the following query: `q ifnot (abs(q - range_median(q)) > k*range_mad(q))`.

See also [range_trim_spikes](#range_trim_spikes) and [range_trim_zscore](#range_trim_zscore).

#### range_trim_spikes

`range_trim_spikes(phi, q)` is a [transform function](#transform-functions), which drops `phi` percent of biggest spikes from time series returned by `q`.
The `phi` must be in the range `[0..1]`, where `0` means `0%` and `1` means `100%`.

See also [range_trim_outliers](#range_trim_outliers) and [range_trim_zscore](#range_trim_zscore).

#### range_trim_zscore

`range_trim_zscore(z, q)` is a [transform function](#transform-functions), which drops points located farther than `z*range_stddev(q)`
from the `range_avg(q)`. E.g. it is equivalent to the following query: `q ifnot (abs(q - range_avg(q)) > z*range_avg(q))`.

See also [range_trim_outliers](#range_trim_outliers) and [range_trim_spikes](#range_trim_spikes).

#### range_zscore

`range_zscore(q)` is a [transform function](#transform-functions), which calculates [z-score](https://en.wikipedia.org/wiki/Standard_score)
for points returned by `q`, e.g. it is equivalent to the following query: `(q - range_avg(q)) / range_stddev(q)`.

#### remove_resets

`remove_resets(q)` is a [transform function](#transform-functions), which removes counter resets from time series returned by `q`.

#### round

`round(q, nearest)` is a [transform function](#transform-functions), which rounds every point of every time series returned by `q` to the `nearest` multiple.
If `nearest` is missing then the rounding is performed to the nearest integer.

This function is supported by PromQL.

See also [floor](#floor) and [ceil](#ceil).

#### ru

`ru(free, max)` is a [transform function](#transform-functions), which calculates resource utilization in the range `[0%...100%]` for the given `free` and `max` resources.
For instance, `ru(node_memory_MemFree_bytes, node_memory_MemTotal_bytes)` returns memory utilization over [node_exporter](https://github.com/prometheus/node_exporter) metrics.

#### running_avg

`running_avg(q)` is a [transform function](#transform-functions), which calculates the running avg per each time series returned by `q`.

#### running_max

`running_max(q)` is a [transform function](#transform-functions), which calculates the running max per each time series returned by `q`.

#### running_min

`running_min(q)` is a [transform function](#transform-functions), which calculates the running min per each time series returned by `q`.

#### running_sum

`running_sum(q)` is a [transform function](#transform-functions), which calculates the running sum per each time series returned by `q`.

#### scalar

`scalar(q)` is a [transform function](#transform-functions), which returns `q` if `q` contains only a single time series. Otherwise, it returns nothing.

This function is supported by PromQL.

#### sgn

`sgn(q)` is a [transform function](#transform-functions), which returns `1` if `v>0`, `-1` if `v<0` and `0` if `v==0` for every point `v`
of every time series returned by `q`.

Metric names are stripped from the resulting series. Add [keep_metric_names](#keep_metric_names) modifier in order to keep metric names.

This function is supported by PromQL.

#### sin

`sin(q)` is a [transform function](#transform-functions), which returns `sin(v)` for every `v` point of every time series returned by `q`.

Metric names are stripped from the resulting series. Add [keep_metric_names](#keep_metric_names) modifier in order to keep metric names.

This function is supported by MetricsQL.

See also [cos](#cos).

#### sinh

`sinh(q)` is a [transform function](#transform-functions), which returns [hyperbolic sine](https://en.wikipedia.org/wiki/Hyperbolic_functions)
for every point of every time series returned by `q`.

Metric names are stripped from the resulting series. Add [keep_metric_names](#keep_metric_names) modifier in order to keep metric names.

This function is supported by MetricsQL.

See also [cosh](#cosh).

#### tan

`tan(q)` is a [transform function](#transform-functions), which returns `tan(v)` for every `v` point of every time series returned by `q`.

Metric names are stripped from the resulting series. Add [keep_metric_names](#keep_metric_names) modifier in order to keep metric names.

This function is supported by MetricsQL.

See also [atan](#atan).

#### tanh

`tanh(q)` is a [transform function](#transform-functions), which returns [hyperbolic tangent](https://en.wikipedia.org/wiki/Hyperbolic_functions)
for every point of every time series returned by `q`.

Metric names are stripped from the resulting series. Add [keep_metric_names](#keep_metric_names) modifier in order to keep metric names.

This function is supported by MetricsQL.

See also [atanh](#atanh).

#### smooth_exponential

`smooth_exponential(q, sf)` is a [transform function](#transform-functions), which smooths points per each time series returned
by `q` using [exponential moving average](https://en.wikipedia.org/wiki/Moving_average#Exponential_moving_average) with the given smooth factor `sf`.

#### sort

`sort(q)` is a [transform function](#transform-functions), which sorts series in ascending order by the last point in every time series returned by `q`.

This function is supported by PromQL.

See also [sort_desc](#sort_desc) and [sort_by_label](#sort_by_label).

#### sort_desc

`sort_desc(q)` is a [transform function](#transform-functions), which sorts series in descending order by the last point in every time series returned by `q`.

This function is supported by PromQL.

See also [sort](#sort) and [sort_by_label](#sort_by_label_desc).

#### sqrt

`sqrt(q)` is a [transform function](#transform-functions), which calculates square root for every point of every time series returned by `q`.

Metric names are stripped from the resulting series. Add [keep_metric_names](#keep_metric_names) modifier in order to keep metric names.

This function is supported by PromQL.

#### start

`start()` is a [transform function](#transform-functions), which returns unix timestamp in seconds for the first point.

It is known as `start` query arg passed to [/api/v1/query_range](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#range-query).

See also [end](#end), [time](#time) and [now](#now).

#### step

`step()` is a [transform function](#transform-functions), which returns the step in seconds (aka interval) between the returned points.
It is known as `step` query arg passed to [/api/v1/query_range](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#range-query).

See also [start](#start) and [end](#end).

#### time

`time()` is a [transform function](#transform-functions), which returns unix timestamp for every returned point.

This function is supported by PromQL.

See also [timestamp](#timestamp), [now](#now), [start](#start) and [end](#end).

#### timezone_offset

`timezone_offset(tz)` is a [transform function](#transform-functions), which returns offset in seconds for the given timezone `tz` relative to UTC.
This can be useful when combining with datetime-related functions. For example, `day_of_week(time()+timezone_offset("America/Los_Angeles"))`
would return weekdays for `America/Los_Angeles` time zone.

Special `Local` time zone can be used for returning an offset for the time zone set on the host where VictoriaMetrics runs.

See [the list of supported timezones](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones).

#### ttf

`ttf(free)` is a [transform function](#transform-functions), which estimates the time in seconds needed to exhaust `free` resources.
For instance, `ttf(node_filesystem_avail_byte)` returns the time to storage space exhaustion. This function may be useful for capacity planning.

#### union

`union(q1, ..., qN)` is a [transform function](#transform-functions), which returns a union of time series returned from `q1`, ..., `qN`.
The `union` function name can be skipped - the following queries are equivalent: `union(q1, q2)` and `(q1, q2)`.

It is expected that each `q*` query returns time series with unique sets of labels.
Otherwise, only the first time series out of series with identical set of labels is returned.
Use [alias](#alias) and [label_set](#label_set) functions for giving unique labelsets per each `q*` query:

#### vector

`vector(q)` is a [transform function](#transform-functions), which returns `q`, e.g. it does nothing in MetricsQL.

This function is supported by PromQL.

#### year

`year(q)` is a [transform function](#transform-functions), which returns the year for every point of every time series returned by `q`.
It is expected that `q` returns unix timestamps.

Metric names are stripped from the resulting series. Add [keep_metric_names](#keep_metric_names) modifier in order to keep metric names.

This function is supported by PromQL.
