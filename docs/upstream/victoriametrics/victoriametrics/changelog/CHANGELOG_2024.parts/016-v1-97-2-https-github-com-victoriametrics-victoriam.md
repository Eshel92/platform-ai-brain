<!-- Part 16 of 19 of victoriametrics/changelog/CHANGELOG_2024.md (split because the page is big). -->

## [v1.97.2](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.97.2)

Released at 2024-02-14

**v1.97.x is a line of [LTS releases](https://docs.victoriametrics.com/victoriametrics/lts-releases/). It contains important up-to-date bugfixes for [VictoriaMetrics Enterprise](https://docs.victoriametrics.com/victoriametrics/enterprise/).
All these fixes are also included in [the latest community release](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/latest).
The v1.97.x line will be supported for at least 12 months since [v1.97.0](https://docs.victoriametrics.com/victoriametrics/changelog/#v1970) release**

* SECURITY: upgrade Go builder from Go1.21.6 to Go1.22.0. See [the list of issues addressed in Go1.21.7](https://github.com/golang/go/issues?q=milestone%3AGo1.21.7+label%3ACherryPickApproved),
  plus [the changelog for Go1.22.0](https://go.dev/doc/go1.22).

* BUGFIX: all VictoriaMetrics components: do not close connections to `-httpListenAddr` every 2 minutes. This behavior didn't help spreading load among multiple backend servers behind load-balancing TCP proxy. Instead, it could lead to hard-to-debug issues like [this one](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/1304#issuecomment-1636997037). If you still need periodically closing client connections because of some reason, then pass the desired timeout to `-http.connTimeout` command-line flag.
* BUGFIX: [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/): reduce CPU usage when `-promscrape.dropOriginalLabels` command-line flag is set. This issue has been introduced in [v1.96.0](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.96.0) when addressing [this feature request](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/5389).
* BUGFIX: [vmauth](https://docs.victoriametrics.com/victoriametrics/vmauth/): properly release memory during config reload. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/4690).
* BUGFIX: [vmauth](https://docs.victoriametrics.com/victoriametrics/vmauth/): properly expose `vmauth_unauthorized_user_concurrent_requests_capacity`, `vmauth_unauthorized_user_concurrent_requests_current`, `vmauth_user_concurrent_requests_capacity` and `vmauth_user_concurrent_requests_current` [metrics](https://docs.victoriametrics.com/victoriametrics/vmauth/#monitoring) after [config reload](https://docs.victoriametrics.com/victoriametrics/vmauth/#config-reload). Previously these metrics didn't work after config reload.
* BUGFIX: [MetricsQL](https://docs.victoriametrics.com/victoriametrics/metricsql/): properly propagate [label filters](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#filtering) from multiple arguments passed to [aggregate functions](https://docs.victoriametrics.com/victoriametrics/metricsql/#aggregate-functions). For example, `sum({job="foo"}, {job="bar"}) by (job) + a` was improperly optimized to `sum({job="foo"}, {job="bar"}) by (job) + a{job="foo"}` before being executed. This could lead to unexpected results. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/5604).
* BUGFIX: [MetricsQL](https://docs.victoriametrics.com/victoriametrics/metricsql/): properly handle precision errors when calculating [changes](https://docs.victoriametrics.com/victoriametrics/metricsql/#changes), [changes_prometheus](https://docs.victoriametrics.com/victoriametrics/metricsql/#changes_prometheus), [increases_over_time](https://docs.victoriametrics.com/victoriametrics/metricsql/#increases_over_time) and [resets](https://docs.victoriametrics.com/victoriametrics/metricsql/#resets) functions. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/767).
* BUGFIX: properly store [staleness markers](https://docs.victoriametrics.com/victoriametrics/vmagent/#prometheus-staleness-markers) for [self-scraped metrics](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#monitoring) on single-node VictoriaMetrics shutdown. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/943).
* BUGFIX: prevent from possible `too big indexBlockSize` panic when samples with too long label values (~64Kb) are ingested into VictoriaMetrics.


## [v1.97.1](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.97.1)

Released at 2024-02-01

**v1.97.x is a line of [LTS releases](https://docs.victoriametrics.com/victoriametrics/lts-releases/). It contains important up-to-date bugfixes for [VictoriaMetrics Enterprise](https://docs.victoriametrics.com/victoriametrics/enterprise/).
All these fixes are also included in [the latest community release](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/latest).
The v1.97.x line will be supported for at least 12 months since [v1.97.0](https://docs.victoriametrics.com/victoriametrics/changelog/#v1970) release**

* FEATURE: [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/): add support for `username_file` option at `basic_auth` section in [`scrape_configs`](https://docs.victoriametrics.com/victoriametrics/sd_configs/#http-api-client-options). See [this feature request](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/5511). Thanks to @wasim-nihal for [the initial implementation](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/5720).

* BUGFIX: [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/): fix the increased CPU usage when sending the data to remote storage. The issue has been introduced in [v1.97.0](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.97.0).
* BUGFIX: fix `runtime error: slice bounds out of range` panic, which can occur during query execution. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/5733). The bug has been introduced in `v1.97.0`.
* BUGFIX: [MetricsQL](https://docs.victoriametrics.com/victoriametrics/metricsql/): properly handle `avg_over_time({some_filter}[d]) keep_metric_names` queries, where [`some_filter`](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#filtering) matches multiple time series with multiple names, while `d` is bigger or equal to `3h`. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/5556).
* BUGFIX: [dashboards/single](https://grafana.com/grafana/dashboards/10229): fix typo in query for `version` annotation which falsely produced many version change events.
