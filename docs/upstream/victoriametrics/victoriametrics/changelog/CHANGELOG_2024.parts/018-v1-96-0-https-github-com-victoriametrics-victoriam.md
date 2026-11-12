<!-- Part 18 of 19 of victoriametrics/changelog/CHANGELOG_2024.md (split because the page is big). -->

## [v1.96.0](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.96.0)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2023/#v1960)


## [v1.95.1](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.95.1)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2023/#v1951)


## [v1.95.0](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.95.0)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2023/#v1950)


## [v1.94.0](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.94.0)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2023/#v1940)


## [v1.93.16](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.93.16)

Released at 2024-07-17

**v1.93.x is a line of [LTS releases](https://docs.victoriametrics.com/victoriametrics/lts-releases/). It contains important up-to-date bugfixes.
The v1.93.x line will be supported for at least 12 months since [v1.93.0](https://docs.victoriametrics.com/victoriametrics/changelog/#v1930) release**

* SECURITY: upgrade Go builder from Go1.22.4 to Go1.22.5. See the list of issues addressed in [Go1.22.5](https://github.com/golang/go/issues?q=milestone%3AGo1.22.5+label%3ACherryPickApproved).
* SECURITY: upgrade base docker image (Alpine) from 3.20.0 to 3.20.1. See [alpine 3.20.1 release notes](https://www.alpinelinux.org/posts/Alpine-3.20.1-released.html).

* BUGFIX: [vmbackup](https://docs.victoriametrics.com/victoriametrics/vmbackup/): properly configure authentication with S3 when `-configFilePath` cmd-line flag is specified.
* BUGFIX: [vmalert](https://docs.victoriametrics.com/victoriametrics/vmalert/): fix path for system links printed on default vmalert's UI page when `-http.pathPrefix` is set.
* BUGFIX: [vmalert](https://docs.victoriametrics.com/victoriametrics/vmalert/): fix incorrect redirection in WebUI of vmalert. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/6603) and [this pull request](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/6620).
* BUGFIX: [vmalert](https://docs.victoriametrics.com/victoriametrics/vmalert/) enterprise: properly configure authentication with S3 when `-s3.configFilePath` cmd-line flag is specified for reading rule configs.
* BUGFIX: [vmalert](https://docs.victoriametrics.com/victoriametrics/vmalert/): properly specify oauth2 `ClientSecret` when configuring authentication for `notifier.url`. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/6471) for details. Thanks to @yincongcyincong for the [pull request](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/6478).
* BUGFIX: [vmui](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#vmui): **copy row** button in Table view produces unexpected result. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/6421) and [pull request](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/6495).
* BUGFIX: [MetricsQL](https://docs.victoriametrics.com/victoriametrics/metricsql/): properly calculate [histogram_quantile](https://docs.victoriametrics.com/victoriametrics/metricsql/#histogram_quantile) over Prometheus buckets with inconsistent values. See [this comment](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/4580#issuecomment-2186659102) and [this pull request](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/6547). Updates [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/2819).


## [v1.93.15](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.93.15)

Released at 2024-06-07

**v1.93.x is a line of [LTS releases](https://docs.victoriametrics.com/victoriametrics/lts-releases/). It contains important up-to-date bugfixes.
The v1.93.x line will be supported for at least 12 months since [v1.93.0](https://docs.victoriametrics.com/victoriametrics/changelog/#v1930) release**

* SECURITY: upgrade Go builder from Go1.22.2 to Go1.22.4. See the list of issues addressed in [Go1.22.3](https://github.com/golang/go/issues?q=milestone%3AGo1.22.3+label%3ACherryPickApproved) and [Go1.22.4](https://github.com/golang/go/issues?q=milestone%3AGo1.22.4+label%3ACherryPickApproved).
* SECURITY: upgrade base docker image (Alpine) from 3.19.1 to 3.20.0. See [alpine 3.20.0 release notes](https://www.alpinelinux.org/posts/Alpine-3.20.0-released.html).

* BUGFIX: [vmui](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#vmui): fix calendar display when `UTC+00:00` timezone is set. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/6239).
* BUGFIX: [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/): skip empty data blocks before sending to the remote write destination. Thanks to @viperstars for [the pull request](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/6241).
* BUGFIX: properly estimate the needed memory for query execution if it has the format [`aggr_func`](https://docs.victoriametrics.com/victoriametrics/metricsql/#aggregate-functions)([`rollup_func[d]`](https://docs.victoriametrics.com/victoriametrics/metricsql/#rollup-functions) (for example, `sum(rate(request_duration_seconds_bucket[5m]))`). This should allow performing aggregations over bigger number of time series when VictoriaMetrics runs in environments with small amounts of available memory. The issue has been introduced in [this commit](https://github.com/VictoriaMetrics/VictoriaMetrics/commit/5138eaeea0791caa34bcfab410e0ca9cd253cd8f) in [v1.83.0](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2022/#v1830).
* BUGFIX: [Single-node VictoriaMetrics](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/) and `vmselect` in [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): filter deleted label names and values from [`/api/v1/labels`](https://docs.victoriametrics.com/victoriametrics/url-examples/#apiv1labels) and [`/api/v1/label/.../values`](https://docs.victoriametrics.com/victoriametrics/url-examples/#apiv1labelvalues) responses when `match[]` filter matches small number of time series. The issue was introduced [v1.81.0](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2022/#v1810).
* BUGFIX: [vmalert](https://docs.victoriametrics.com/victoriametrics/vmalert/): fix misleading error logs in vmalert's stdout when unsupported HTTP path is requested.
* BUGFIX: retry files delete attempts on vXFS file system for `EEXIST` error type. See the [related issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/6396). Thanks to @pludov for the [pull request](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/6398).


## [v1.93.14](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.93.14)

Released at 2024-04-19

**v1.93.x is a line of [LTS releases](https://docs.victoriametrics.com/victoriametrics/lts-releases/). It contains important up-to-date bugfixes.
The v1.93.x line will be supported for at least 12 months since [v1.93.0](https://docs.victoriametrics.com/victoriametrics/changelog/#v1930) release**

* SECURITY: upgrade Go builder from Go1.21.7 to Go1.22.2. See [the list of issues addressed in Go1.22.1](https://github.com/golang/go/issues?q=milestone%3AGo1.22.1+label%3ACherryPickApproved) and [the list of issues addressed in Go1.22.2](https://github.com/golang/go/issues?q=milestone%3AGo1.22.2+label%3ACherryPickApproved).

* BUGFIX: [vmalert](https://docs.victoriametrics.com/victoriametrics/vmalert/): set correct `endsAt` value in notifications sent to the Alertmanager. Previously, a rule with evaluation intervals lower than 10s could never be triggered. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/5995) for details.
* BUGFIX: [vmalert](https://docs.victoriametrics.com/victoriametrics/vmalert/): properly account for `-rule.resendDelay` for alerting rules that are constantly switching state from inactive to firing. Before, notifications for such rules could have been skipped if state change happened more often than `-rule.resendDelay`. See [this pull request](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/6028) for details.
* BUGFIX: [vmalert](https://docs.victoriametrics.com/victoriametrics/vmalert/): respect `-remoteWrite.maxBatchSize` at shutdown period. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/6025). Thanks to @jiekun for [the pull request](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/6039).
* BUGFIX: [vmalert](https://docs.victoriametrics.com/victoriametrics/vmalert/): supported any status codes from the range 200-299 from alertmanager. Previously, only 200 status code considered a successful action. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/6110).


## [v1.93.13](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.93.13)

Released at 2024-03-01

**v1.93.x is a line of [LTS releases](https://docs.victoriametrics.com/victoriametrics/lts-releases/). It contains important up-to-date bugfixes.
The v1.93.x line will be supported for at least 12 months since [v1.93.0](https://docs.victoriametrics.com/victoriametrics/changelog/#v1930) release**

* BUGFIX: downgrade Go builder from `1.22.0` to `1.21.7`, since `1.22.0` contains [the bug](https://github.com/golang/go/issues/65705), which can lead to deadlocked HTTP connections to remote storage systems, scrape targets and service discovery endpoints at [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/). This may result in incorrect service discovery, target scraping and failed sending samples to remote storage.
* BUGFIX: [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/): accept OpenTelemetry data at `/opentelemetry/v1/metrics`, since the `/v1/metrics` suffix is hardcoded at [OpenTelemetry protocol specification](https://opentelemetry.io/docs/specs/otlp/#otlphttp-request).
* BUGFIX: [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/): fix possible deadlock when [sharding among remote storages](https://docs.victoriametrics.com/victoriametrics/vmagent/#sharding-among-remote-storages) is enabled with `-remoteWrite.shardByURL` command-line flag. Thanks to @penguinlav for [the fix](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/5834) for [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/5833).

* BUGFIX: fix the misleading error `0ms is out of allowed range [0 ...` when passing `step=0` to [/api/v1/query](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#instant-query)
  or [/api/v1/query_range](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#range-query). See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/5795).
* BUGFIX: [Single-node VictoriaMetrics](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/) and `vmselect` in [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): fixed floating-point error when parsing time in RFC3339 format. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/5801) for details.
* BUGFIX: [vmalert](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#vmalert): consistently sort groups by name and filename on `/groups` page in UI. This should prevent non-deterministic sorting for groups with identical names.
* BUGFIX: [MetricsQL](https://docs.victoriametrics.com/victoriametrics/metricsql/): properly construct the destination label in [label_join](https://docs.victoriametrics.com/victoriametrics/metricsql/#label_join) if it is used as source label. See this [issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/5881) for details.


## [v1.93.12](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.93.12)

Released at 2024-02-14

**v1.93.x is a line of [LTS releases](https://docs.victoriametrics.com/victoriametrics/lts-releases/). It contains important up-to-date bugfixes.
The v1.93.x line will be supported for at least 12 months since [v1.93.0](https://docs.victoriametrics.com/victoriametrics/changelog/#v1930) release**

* SECURITY: upgrade Go builder from Go1.21.6 to Go1.22.0. See [the list of issues addressed in Go1.21.7](https://github.com/golang/go/issues?q=milestone%3AGo1.21.7+label%3ACherryPickApproved), plus [the changelog for Go1.22.0](https://go.dev/doc/go1.22).

* BUGFIX: [MetricsQL](https://docs.victoriametrics.com/victoriametrics/metricsql/): properly propagate [label filters](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#filtering) from multiple arguments passed to [aggregate functions](https://docs.victoriametrics.com/victoriametrics/metricsql/#aggregate-functions). For example, `sum({job="foo"}, {job="bar"}) by (job) + a` was improperly optimized to `sum({job="foo"}, {job="bar"}) by (job) + a{job="foo"}` before being executed. This could lead to unexpected results. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/5604).
* BUGFIX: [MetricsQL](https://docs.victoriametrics.com/victoriametrics/metricsql/): properly handle precision errors when calculating [changes](https://docs.victoriametrics.com/victoriametrics/metricsql/#changes), [changes_prometheus](https://docs.victoriametrics.com/victoriametrics/metricsql/#changes_prometheus), [increases_over_time](https://docs.victoriametrics.com/victoriametrics/metricsql/#increases_over_time) and [resets](https://docs.victoriametrics.com/victoriametrics/metricsql/#resets) functions. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/767).
* BUGFIX: properly store [staleness markers](https://docs.victoriametrics.com/victoriametrics/vmagent/#prometheus-staleness-markers) for [self-scraped metrics](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#monitoring) on single-node VictoriaMetrics shutdown. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/943).
* BUGFIX: prevent from possible `too big indexBlockSize` panic when samples with too long label values (~64Kb) are ingested into VictoriaMetrics.


## [v1.93.11](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.93.11)

Released at 2024-02-01

**v1.93.x is a line of [LTS releases](https://docs.victoriametrics.com/victoriametrics/lts-releases/). It contains important up-to-date bugfixes.
The v1.93.x line will be supported for at least 12 months since [v1.93.0](https://docs.victoriametrics.com/victoriametrics/changelog/#v1930) release**

* SECURITY: upgrade base docker image (Alpine) from 3.19.0 to 3.19.1. See [alpine 3.19.1 release notes](https://www.alpinelinux.org/posts/Alpine-3.19.1-released.html).

* BUGFIX: properly return errors from [export APIs](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#how-to-export-time-series). Previously these errors were silently suppressed. See [this pull request](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/5649).
* BUGFIX: [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/): properly discover targets for `role: endpoints` and `role: endpointslice` in [kubernetes_sd_configs](https://docs.victoriametrics.com/victoriametrics/sd_configs/#kubernetes_sd_configs). Previously some `endpoints` and `endpointslice` targets could be left undiscovered or some targets could have missing `__meta_*` labels when performing service discovery in busy Kubernetes clusters with large number of pods. See [this pull request](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/5557).
* BUGFIX: [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/): respect explicitly set `series_limit: 0` in [scrape_config](https://docs.victoriametrics.com/victoriametrics/sd_configs/#scrape_configs). This allows removing [`series_limit` restriction](https://docs.victoriametrics.com/victoriametrics/vmagent/#cardinality-limiter) on a per-`scrape_config` basis when global limit is set via `-promscrape.seriesLimitPerTarget`. Previously, `0` value was ignored in favor of `-promscrape.seriesLimitPerTarget`.
* BUGFIX: [MetricsQL](https://docs.victoriametrics.com/victoriametrics/metricsql/): properly process queries with too big lookbehind window such as `foo[100y]`. Previously, such queries could return empty responses even if `foo` is present in database. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/5553).
* BUGFIX: [MetricsQL](https://docs.victoriametrics.com/victoriametrics/metricsql/): properly handle possible negative results caused by float operations precision error in rollup functions like rate() or increase(). See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/5571).
