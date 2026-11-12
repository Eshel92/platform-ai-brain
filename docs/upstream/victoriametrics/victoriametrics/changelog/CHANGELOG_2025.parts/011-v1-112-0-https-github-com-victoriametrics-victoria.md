<!-- Part 11 of 19 of victoriametrics/changelog/CHANGELOG_2025.md (split because the page is big). -->

## [v1.112.0](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.112.0)

Released at 2025-02-21

**Known issues: this release contains change that could increase CPU usage for vminsert, vmagent, vmsingle for certain type of workloads. See [#8501](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/8501) for details.
If you are impacted by this, please upgrade to [v1.114.0](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.114.0) or rollback to [v1.111.0](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.111.0).**

* SECURITY: upgrade Go builder from Go1.23.5 to Go1.23.6. See the list of issues addressed in [Go1.23.6](https://github.com/golang/go/issues?q=milestone%3AGo1.23.6+label%3ACherryPickApproved).
* SECURITY: upgrade base docker image (Alpine) from 3.21.2 to 3.21.3. See [Alpine 3.21.3 release notes](https://alpinelinux.org/posts/Alpine-3.18.12-3.19.7-3.20.6-3.21.3-released.html).

* FEATURE: [Single-node VictoriaMetrics](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/) and [vmstorage](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): allow [disabling per-day indexes](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#index-tuning-for-low-churn-rate) for workloads with low or zero churn rates via `-disablePerDayIndex` cmd-line flag. This option works the best for IoT cases and significantly loads resource and disk usage. See [this PR](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/6976).
* FEATURE: [vmalert](https://docs.victoriametrics.com/victoriametrics/vmalert/): add command-line flag `-notifier.sendTimeout(default 10s)` to allow configuring request timeout when sending alerts to the corresponding `-notifier.url`. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/8287) for details. Thanks to @gjkim42 for the [pull request](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/8297).
* FEATURE: [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/) and [vmsingle](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/): add support of [aggregation windows](https://docs.victoriametrics.com/victoriametrics/stream-aggregation/#aggregation-windows) to improve accuracy of stream aggregation. This feature is especially important for aggregation of [histograms](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#histogram), but enabling this feature requires additional memory. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/4580).
* FEATURE: [vmsingle](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/), `vminsert` in [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/) and [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/): add `-influx.forceStreamMode` cmd-line flag to force stream processing for data ingested via [InfluxDB protocol](https://docs.victoriametrics.com/victoriametrics/integrations/influxdb/#influxdb-compatible-agents-such-as-telegraf). See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/8269).
* FEATURE: [vmselect](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): support overriding vmstorage `-maxUniqueTimeseries` with specific resource limits: `-search.maxLabelsAPISeries`, `-search. maxSeries`, `-search.maxTSDBStatusSeries` and `-search.maxDeleteSeries`. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/7857).
* FEATURE: [vmui](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#vmui): add legend customization options - table view, hiding common values, grouping by label, and custom label format. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/8031) and [this pull request](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/8263).
* FEATURE: [vmui](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#vmui): look back for recent data for longer time intervals when switching to Table or JSON view. The look back window depends on the `step` setting, which is now set as `end - start` (30m) by default. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/8240).
* FEATURE: [vmui](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#vmui): preserve user-defined `step` setting when changing the time interval of displayed query. See [this comment](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/8240#issuecomment-2647674065).
* FEATURE: [vmui](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#vmui): improve numbers formatting for better readability on the `Explore Cardinality` page. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/8318).
* FEATURE: [vmui](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#vmui): print full error messages for failed queries on the `Explore Cardinality` page. Before, only response status code was printed.
* FEATURE: [vmui](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#vmui): move values representing changes relative to the previous day to a separate column for easier sorting on the `Explore Cardinality` page.
* FEATURE: [MetricsQL](https://docs.victoriametrics.com/victoriametrics/metricsql/): parse `$__interval` and `$__rate_interval` inside square brackets as missing square brackets. For example, `rate(m[$__interval])` is parsed as `rate(m)` instead of `rate(m[1i])`. This enables automatic detection of the lookbehind window for [rollup functions](https://docs.victoriametrics.com/victoriametrics/metricsql/#rollup-functions) by VictoriaMetrics, which usually returns the most expected result.
* FEATURE: [MetricsQL](https://docs.victoriametrics.com/victoriametrics/metricsql/): support auto-format (prettify) for expressions that use quoted metric or label names. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/7703) for details.

* BUGFIX: all the VictoriaMetrics components: properly override basic authorization for API endpoints protected with `authKey`. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/7345#issuecomment-2662595807) for details.
* BUGFIX: [vmalert](https://docs.victoriametrics.com/victoriametrics/vmalert/): fix polluted alert messages when multiple Alertmanager instances are configured with `alert_relabel_configs`. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/8040), and thanks to @evkuzin for [the pull request](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/8258).
* BUGFIX: [vmalert](https://docs.victoriametrics.com/victoriametrics/vmalert/): fix the auto-generated metrics for alerts and groups. Previously, metrics might be missing after reload. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/8229) for the details.
* BUGFIX: `vminsert` in [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/) and `vmstorage` in [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): properly return parsing errors during data ingestion in [multi-level cluster setup](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/#multi-level-cluster-setup). Before, some of the errors could have been silently ignored.
* BUGFIX: [vmsingle](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/),  `vmselect` in [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): fix negative rate result when the lookbehind window is longer than `-search.maxLookback` or `-search.maxStalenessInterval` and data contains gap. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/8342).
* BUGFIX: [Single-node VictoriaMetrics](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/) and [vmselect](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): properly enforce presence of default `-retentionPeriod` configuration for [retention filters](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#retention-filters) debug interface. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/8343).


## [v1.111.0](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.111.0)

Released at 2025-02-10

**Update note 1: [Single-node VictoriaMetrics](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/) and [vmstorage](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/) stop exposing `vm_index_search_duration_seconds` histogram metric. This metric records time spent on search operations in the index. It was introduced in [v1.56.0](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.56.0). However, this metric was used neither in dashboards nor in alerting rules. It also has high cardinality because index search operations latency can differ by 3 orders of magnitude. Hence, dropping it as unused.**

* FEATURE: [Single-node VictoriaMetrics](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/) and [vmstorage](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): improve startup times when opening a storage with the [retention](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#retention) exceeding a few months.
* FEATURE: [vmui](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#vmui): add the ability to switch the heatmap to a line chart. Now, vmui would suggest to switch to line graph display if heatmap can't be properly rendered. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/8057).
* FEATURE: [vmauth](https://docs.victoriametrics.com/victoriametrics/vmauth/): add `-httpInternalListenAddr` cmd-line flag to serve internal HTTP routes `/metrics`, `/flags`, etc. It allows properly route requests to backends with the same service routes as vmauth. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/6468) and [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/7345) for details.
* FEATURE: expose `/-/healthy` and `/-/ready` endpoints as Prometheus does on vmselect endpoints, thus achieving full Prometheus compatibility for external dependencies.

* BUGFIX: [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/): properly perform graceful shutdown for kafka client.
* BUGFIX: [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/): properly add message metadata headers for kafka remoteWrite target.
* BUGFIX: [vmui](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#vmui): improve clipboard error handling in tables and code snippets by showing detailed messages with possible reasons. See [this pull request](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/7778).
* BUGFIX: [vmui](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#vmui) for [VictoriaMetrics Enterprise](https://docs.victoriametrics.com/victoriametrics/enterprise/) components: properly display enterprise features when the enterprise version is used.
* BUGFIX: [Single-node VictoriaMetrics](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/) and [vmselect](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): fix discrepancies when using `or` binary operator. See [this](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/7759) and [this](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/7640) issues for details.
* BUGFIX: [vmsingle](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/) and `vmstorage` in [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): properly update number of unique series for [cardinality limiter](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#cardinality-limiter) on ingestion. Previously, limit could undercount the real number of the ingested unique series.


## [v1.110.27](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.110.27)

Released at 2026-01-02

**v1.110.x is a line of [LTS releases](https://docs.victoriametrics.com/victoriametrics/lts-releases/). It contains important up-to-date bugfixes for [VictoriaMetrics enterprise](https://docs.victoriametrics.com/victoriametrics/enterprise/).
All these fixes are also included in [the latest community release](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/latest).
The v1.110.x line will be supported for at least 12 months since [v1.110.0](https://docs.victoriametrics.com/victoriametrics/changelog/#v11100) release**

* SECURITY: upgrade base docker image (Alpine) from 3.22.2 to 3.23.2. See [Alpine 3.23.2 release notes](https://www.alpinelinux.org/posts/Alpine-3.23.2-released.html).
* SECURITY: upgrade Go builder from Go1.24.10 to Go1.24.11. It addresses [CVE-2025-61729](http://scout.docker.com/v/CVE-2025-61729). See [the list of issues addressed in Go1.24.11](https://github.com/golang/go/issues?q=milestone%3AGo1.24.11+label%3ACherryPickApproved).

* BUGFIX: [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/): fix `vmagent_rows_inserted_total{type="newrelic"}` metric to correctly count samples. See [#10191](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/10191). Thanks to @fxrlv for the contribution.
* BUGFIX: [vmauth](https://docs.victoriametrics.com/victoriametrics/vmauth/): fix `vmauth_user_request_backend_errors_total` and `vmauth_unauthorized_user_request_backend_errors_total` to only reflect backend request errors. Previously, these counters could be overcounted with user request error. See [#10177](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/10177).


## [v1.110.26](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.110.26)

Released at 2025-12-12

**v1.110.x is a line of [LTS releases](https://docs.victoriametrics.com/victoriametrics/lts-releases/). It contains important up-to-date bugfixes for [VictoriaMetrics enterprise](https://docs.victoriametrics.com/victoriametrics/enterprise/).
All these fixes are also included in [the latest community release](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/latest).
The v1.110.x line will be supported for at least 12 months since [v1.110.0](https://docs.victoriametrics.com/victoriametrics/changelog/#v11100) release**

* BUGFIX: all VictoriaMetrics components: properly validate remaining system memory limit. Previously it could have negative values. See this issue [#10083](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/10083) for details.
* BUGFIX: [vmalert](https://docs.victoriametrics.com/victoriametrics/vmalert/): don't increase `vmalert_alerting_rules_errors_total`/`vmalert_recording_rules_errors_total` for request context cancellation, which may occur during graceful shutdown or group configuration update. See [#10128](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/10128). Thanks to @tIGO for the contribution.
* BUGFIX: [vmctl](https://docs.victoriametrics.com/victoriametrics/vmctl/): properly handle process termination during prompt confirmation. Previously, termination signal was ignored and process was still waiting for user input. See[#10104](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/10104).
* BUGFIX: [vmgateway](https://docs.victoriametrics.com/victoriametrics/vmgateway/): properly recover from proxy requests errors. Previously, vmgateway may return empty response.
* BUGFIX: [vmauth](https://docs.victoriametrics.com/victoriametrics/vmauth/): verify backend network reachability with a TCP dial before marking it healthy. Previously, backends were auto-restored after `-failTimeout` even if the network was still unreachable, causing requests to hang repeatedly. `vmauth` now performs a 1s TCP dial check before returning a backend to the healthy pool. See [#9997](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/9997).


## [v1.110.25](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.110.25)

Released at 2025-11-28

**v1.110.x is a line of [LTS releases](https://docs.victoriametrics.com/victoriametrics/lts-releases/). It contains important up-to-date bugfixes for [VictoriaMetrics enterprise](https://docs.victoriametrics.com/victoriametrics/enterprise/).
All these fixes are also included in [the latest community release](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/latest).
The v1.110.x line will be supported for at least 12 months since [v1.110.0](https://docs.victoriametrics.com/victoriametrics/changelog/#v11100) release**

* BUGFIX: [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/) and [vmsingle](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/): prevent early exit when one of multiple service discovery configs (under the same service discovery type) fails. see this issue [#9949](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/9949) for details.
* BUGFIX: [vmalert](https://docs.victoriametrics.com/victoriametrics/vmalert/): don't increase `vmalert_alerts_send_errors_total` for request context cancellation, which may occur during graceful shutdown or group configuration update. See [#10027](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/10027).
* BUGFIX: [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/), [vmsingle](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/) and `vminsert` in [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): Prevent `accept()` from blocking when a client connects to `-opentsdbListenAddr` but sends no data or sends it too slowly. Previously, such connections could stall acceptance of new clients. See [#9987](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/9987) for details.
* BUGFIX: `vmselect` in [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): respect `replicationFactor` and `globalReplicationFactor` settings when some of vmstorage nodes are overloaded. See [#10030](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/10030) for details. Thanks to @tIGO for the contribution.
* BUGFIX: Account for excess white spaces in influx write string. See [#10049](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/10049).
