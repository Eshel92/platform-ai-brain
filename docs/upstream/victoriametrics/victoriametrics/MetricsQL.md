---
weight: 23
title: MetricsQL
description: "Query language reference. Enhanced PromQL with additional functions, histogram helpers, and subquery support."
menu:
  docs:
    parent: 'victoriametrics'
    weight: 23
tags:
  - metrics
aliases:
- /ExtendedPromQL.html
- /MetricsQL.html
- /metricsql/index.html
- /metricsql/
- /MetricsQL/
---
[VictoriaMetrics](https://github.com/VictoriaMetrics/VictoriaMetrics) implements MetricsQL -
query language inspired by [PromQL](https://prometheus.io/docs/prometheus/latest/querying/basics/).
MetricsQL is backwards-compatible with PromQL, so Grafana dashboards backed by Prometheus datasource should work
the same after switching from Prometheus to VictoriaMetrics.
However, there are some [intentional differences](https://medium.com/@romanhavronenko/victoriametrics-promql-compliance-d4318203f51e) between these two languages.

[Standalone MetricsQL package](https://godoc.org/github.com/VictoriaMetrics/metricsql) can be used for parsing MetricsQL in external apps.

If you are unfamiliar with PromQL, we suggest reading [this tutorial for beginners](https://medium.com/@valyala/promql-tutorial-for-beginners-9ab455142085)
and introduction into [basic querying via MetricsQL](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#metricsql).

The following functionality is implemented differently in MetricsQL compared to PromQL. This improves user experience:

* MetricsQL takes into account the last [raw sample](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#raw-samples) before the lookbehind window
  in square brackets for [increase](#increase) and [rate](#rate) functions. This allows returning the exact results users expect for `increase(metric[$__interval])` queries
  instead of incomplete results Prometheus returns for such queries. Prometheus misses the increase between the last sample before the lookbehind window
  and the first sample inside the lookbehind window.
* MetricsQL doesn't extrapolate [rate](#rate) and [increase](#increase) function results, so it always returns the expected results. For example, it returns
  integer results from `increase()` over slow-changing integer counter. Prometheus in this case returns unexpected fractional results,
  which may significantly differ from the expected results. This addresses [this issue from Prometheus](https://github.com/prometheus/prometheus/issues/3746).
  See technical details about VictoriaMetrics and Prometheus calculations for [rate](#rate)
  and [increase](#increase) [in this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/1215#issuecomment-850305711).
* MetricsQL returns the expected non-empty responses for [rate](#rate) function when Grafana or [vmui](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#vmui)
  passes `step` values smaller than the interval between [raw samples](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#raw-samples)
  to [/api/v1/query_range](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#range-query).
  This addresses [this issue from Grafana](https://github.com/grafana/grafana/issues/11451).
  See also [this blog post](https://www.percona.com/blog/2020/02/28/better-prometheus-rate-function-with-victoriametrics/).
* MetricsQL treats `scalar` type the same as `instant vector` without labels, since subtle differences between these types usually confuse users.
  See [the corresponding Prometheus docs](https://prometheus.io/docs/prometheus/latest/querying/basics/#expression-language-data-types) for details.
* MetricsQL removes all the `NaN` values from the output, so some queries like `(-1)^0.5` return empty results in VictoriaMetrics,
  while returning a series of `NaN` values in Prometheus. Note that Grafana doesn't draw any lines or dots for `NaN` values,
  so the end result looks the same for both VictoriaMetrics and Prometheus.
* MetricsQL keeps metric names after applying functions, which don't change the meaning of the original time series.
  For example, [min_over_time(foo)](#min_over_time) or [round(foo)](#round) leaves `foo` metric name in the result.
  See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/674) for details.

Read more about the differences between PromQL and MetricsQL in [this article](https://medium.com/@romanhavronenko/victoriametrics-promql-compliance-d4318203f51e).

Other PromQL functionality should work the same in MetricsQL.
[File an issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues) if you notice discrepancies between PromQL and MetricsQL results other than mentioned above.

<!-- This page was over 60 KB, so its sections are separate files. -->

## Sections (in `MetricsQL.parts/`)

- `001-metricsql-features-count-ne-over-time.md`: MetricsQL features … count_ne_over_time
- `002-metricsql-functions-rollup-functions-count-over-ti.md`: MetricsQL functions › Rollup functions › count_over_time … lifetime
- `003-metricsql-functions-rollup-functions-mad-over-time.md`: MetricsQL functions › Rollup functions › mad_over_time … scrape_interval
- `004-metricsql-functions-rollup-functions-share-gt-over.md`: MetricsQL functions › Rollup functions › share_gt_over_time … zscore_over_time
- `005-metricsql-functions-transform-functions.md`: MetricsQL functions › Transform functions
- `006-metricsql-functions-label-manipulation-functions.md`: MetricsQL functions › Label manipulation functions
- `007-metricsql-functions-aggregate-functions-subqueries.md`: MetricsQL functions › Aggregate functions … Subqueries
- `008-implicit-query-conversions.md`: Implicit query conversions
