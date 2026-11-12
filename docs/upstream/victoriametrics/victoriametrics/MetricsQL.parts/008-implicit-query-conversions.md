<!-- Part 8 of 8 of victoriametrics/MetricsQL.md (split because the page is big). -->

## Implicit query conversions

VictoriaMetrics performs the following implicit conversions for incoming queries before starting the calculations:

* If lookbehind window in square brackets is missing inside [rollup function](#rollup-functions), then it is automatically set to the following value:
  * To `step` value passed to [/api/v1/query_range](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#range-query) or [/api/v1/query](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#instant-query)
    for all the [rollup functions](#rollup-functions) except of [default_rollup](#default_rollup) and [rate](#rate). This value is known as `$__interval` in Grafana or `1i` in MetricsQL.
    For example, `avg_over_time(temperature)` is automatically transformed to `avg_over_time(temperature[1i])`.
  * To the `max(step, scrape_interval)`, where `scrape_interval` is the interval between [raw samples](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#raw-samples)
    for [default_rollup](#default_rollup) and [rate](#rate) functions. This allows avoiding unexpected gaps on the graph when `step` is smaller than `scrape_interval`.
* All the [series selectors](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#filtering),
  which aren't wrapped into [rollup functions](#rollup-functions), are automatically wrapped into [default_rollup](#default_rollup) function.
  Examples:
  * `foo` is transformed to `default_rollup(foo)`
  * `foo + bar` is transformed to `default_rollup(foo) + default_rollup(bar)`
  * `count(up)` is transformed to `count(default_rollup(up))`, because [count](#count) isn't a [rollup function](#rollup-functions) -
    it is [aggregate function](#aggregate-functions)
  * `abs(temperature)` is transformed to `abs(default_rollup(temperature))`, because [abs](#abs) isn't a [rollup function](#rollup-functions) -
    it is [transform function](#transform-functions)
* If `step` in square brackets is missing inside [subquery](#subqueries), then `1i` step is automatically added there.
  For example, `avg_over_time(rate(http_requests_total[5m])[1h])` is automatically converted to `avg_over_time(rate(http_requests_total[5m])[1h:1i])`.
* If something other than [series selector](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#filtering)
  is passed to [rollup function](#rollup-functions), then a [subquery](#subqueries) with `1i` lookbehind window and `1i` step is automatically formed.
  For example, `rate(sum(up))` is automatically converted to `rate((sum(default_rollup(up)))[1i:1i])`.
  This behavior can be disabled or logged via `-search.disableImplicitConversion` and `-search.logImplicitConversion` command-line flags
  starting from [`v1.102.0-rc2` release](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2024/#v11020-rc2).
