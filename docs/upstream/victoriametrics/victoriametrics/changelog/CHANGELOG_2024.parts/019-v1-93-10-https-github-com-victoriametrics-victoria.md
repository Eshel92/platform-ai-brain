<!-- Part 19 of 19 of victoriametrics/changelog/CHANGELOG_2024.md (split because the page is big). -->

## [v1.93.10](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.93.10)

Released at 2024-01-17

**v1.93.x is a line of [LTS releases](https://docs.victoriametrics.com/victoriametrics/lts-releases/). It contains important up-to-date bugfixes.
The v1.93.x line will be supported for at least 12 months since [v1.93.0](https://docs.victoriametrics.com/victoriametrics/changelog/#v1930) release**

* SECURITY: upgrade Go builder from Go1.21.5 to Go1.21.6. See [the list of issues addressed in Go1.21.6](https://github.com/golang/go/issues?q=milestone%3AGo1.21.6+label%3ACherryPickApproved).

* BUGFIX: `vminsert`: properly accept samples via [OpenTelemetry data ingestion protocol](https://docs.victoriametrics.com/victoriametrics/integrations/opentelemetry/) when these samples have no [resource attributes](https://opentelemetry.io/docs/instrumentation/go/resources/). Previously such samples were silently skipped.
* BUGFIX: `vmstorage`: added missing `-inmemoryDataFlushInterval` command-line flag, which was missing in [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/) after implementing [this feature](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/3337) in [v1.85.0](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.85.0).
* BUGFIX: `vmstorage`: properly expire `storage/prefetchedMetricIDs` cache. Previously this cache was never expired, so it could grow big under [high churn rate](https://docs.victoriametrics.com/victoriametrics/faq/#what-is-high-churn-rate). This could result in increasing CPU load over time.
* BUGFIX: [vmalert](https://docs.victoriametrics.com/victoriametrics/vmalert/): check `-external.url` schema when starting vmalert, must be `http` or `https`. Before, alertmanager could reject alert notifications if `-external.url` contained no or wrong schema.
* BUGFIX: [MetricsQL](https://docs.victoriametrics.com/victoriametrics/metricsql/): properly return results from [bottomk](https://docs.victoriametrics.com/victoriametrics/metricsql/#bottomk) and `bottomk_*()` functions when some of these results contain NaN values. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/5506). Thanks to @xiaozongyang for [the fix](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/5509).
* BUGFIX: [MetricsQL](https://docs.victoriametrics.com/victoriametrics/metricsql/): properly handle queries, which wrap [rollup functions](https://docs.victoriametrics.com/victoriametrics/metricsql/#rollup-functions) with multiple arguments without explicitly specified lookbehind window in square brackets into [aggregate functions](https://docs.victoriametrics.com/victoriametrics/metricsql/#aggregate-functions). For example, `sum(quantile_over_time(0.5, process_resident_memory_bytes))` was resulting to `expecting at least 2 args to ...; got 1 args` error. Thanks to @atykhyy for [the pull request](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/5414).
* BUGFIX: [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/): properly assume role with [AWS IRSA authorization](https://docs.aws.amazon.com/eks/latest/userguide/iam-roles-for-service-accounts.html). Previously role chaining was not supported. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/3822) for details.
* BUGFIX: all: fix potential panic during components shutdown when [metrics push](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#push-metrics) is configured. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/5548). Thanks to @zhdd99 for the [pull request](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/5549).
* BUGFIX: [vmctl](https://docs.victoriametrics.com/victoriametrics/vmctl/): check for Error field in response from influx client during migration. Before, only network errors were checked. Thanks to @wozz for the [pull request](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/5446).
* BUGFIX: [vmctl](https://docs.victoriametrics.com/victoriametrics/vmctl/): retry on import errors in `vm-native` mode. Before, retries happened only on writes into a network connection between source and destination. But errors returned by server after all the data was transmitted were logged, but not retried.


## [v1.93.9](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.93.9)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2023/#v1939)


## [v1.93.8](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.93.8)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2023/#v1938)


## [v1.93.7](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.93.7)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2023/#v1937)


## [v1.93.6](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.93.6)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2023/#v1936)


## [v1.93.5](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.93.5)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2023/#v1935)


## [v1.93.4](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.93.4)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2023/#v1934)


## [v1.93.3](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.93.3)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2023/#v1933)


## [v1.93.2](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.93.2)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2023/#v1932)


## [v1.93.1](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.93.1)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2023/#v1931)


## [v1.93.0](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.93.0)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2023/#v1930)


## [v1.92.1](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.92.1)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2023/#v1921)


## [v1.92.0](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.92.0)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2023/#v1920)


## [v1.91.3](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.91.3)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2023/#v1913)


## [v1.91.2](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.91.2)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2023/#v1912)


## [v1.91.1](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.91.1)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2023/#v1911)


## [v1.91.0](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.91.0)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2023/#v1910)


## [v1.90.0](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.90.0)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2023/#v1900)


## [v1.89.1](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.89.1)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2023/#v1891)


## [v1.89.0](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.89.0)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2023/#v1890)


## [v1.88.1](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.88.1)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2023/#v1881)


## [v1.88.0](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.88.0)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2023/#v1880)


## [v1.87.14](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.87.14)

Released at 2024-02-01

**v1.87.x is a line of [LTS releases](https://docs.victoriametrics.com/victoriametrics/lts-releases/). It contains important up-to-date bugfixes.
The v1.87.x line will be supported for at least 12 months since [v1.87.0](https://docs.victoriametrics.com/victoriametrics/changelog/#v1870) release**

* SECURITY: upgrade base docker image (Alpine) from 3.19.0 to 3.19.1. See [alpine 3.19.1 release notes](https://www.alpinelinux.org/posts/Alpine-3.19.1-released.html).

* BUGFIX: properly return errors from [export APIs](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#how-to-export-time-series). Previously these errors were silently suppressed. See [this pull request](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/5649).
* BUGFIX: [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/): respect explicitly set `series_limit: 0` in [scrape_config](https://docs.victoriametrics.com/victoriametrics/sd_configs/#scrape_configs). This allows removing [`series_limit` restriction](https://docs.victoriametrics.com/victoriametrics/vmagent/#cardinality-limiter) on a per-`scrape_config` basis when global limit is set via `-promscrape.seriesLimitPerTarget`. Previously, `0` value was ignored in favor of `-promscrape.seriesLimitPerTarget`.
* BUGFIX: [MetricsQL](https://docs.victoriametrics.com/victoriametrics/metricsql/): properly process queries with too big lookbehind window such as `foo[100y]`. Previously, such queries could return empty responses even if `foo` is present in database. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/5553).
* BUGFIX: [MetricsQL](https://docs.victoriametrics.com/victoriametrics/metricsql/): properly handle possible negative results caused by float operations precision error in rollup functions like rate() or increase(). See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/5571).


## [v1.87.13](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.87.13)

Released at 2024-01-17

**v1.87.x is a line of [LTS releases](https://docs.victoriametrics.com/victoriametrics/lts-releases/). It contains important up-to-date bugfixes.
The v1.87.x line will be supported for at least 12 months since [v1.87.0](https://docs.victoriametrics.com/victoriametrics/changelog/#v1870) release**

* SECURITY: upgrade Go builder from Go1.21.5 to Go1.21.6. See [the list of issues addressed in Go1.21.6](https://github.com/golang/go/issues?q=milestone%3AGo1.21.6+label%3ACherryPickApproved).

* BUGFIX: `vmstorage`: added missing `-inmemoryDataFlushInterval` command-line flag, which was missing in [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/) after implementing [this feature](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/3337) in [v1.85.0](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.85.0).
* BUGFIX: [MetricsQL](https://docs.victoriametrics.com/victoriametrics/metricsql/): properly handle queries, which wrap [rollup functions](https://docs.victoriametrics.com/victoriametrics/metricsql/#rollup-functions) with multiple arguments without explicitly specified lookbehind window in square brackets into [aggregate functions](https://docs.victoriametrics.com/victoriametrics/metricsql/#aggregate-functions). For example, `sum(quantile_over_time(0.5, process_resident_memory_bytes))` was resulting to `expecting at least 2 args to ...; got 1 args` error. Thanks to @atykhyy for [the pull request](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/5414).
* BUGFIX: `vmstorage`: properly expire `storage/prefetchedMetricIDs` cache. Previously this cache was never expired, so it could grow big under [high churn rate](https://docs.victoriametrics.com/victoriametrics/faq/#what-is-high-churn-rate). This could result in increasing CPU load over time.
* BUGFIX: [MetricsQL](https://docs.victoriametrics.com/victoriametrics/metricsql/): properly return results from [bottomk](https://docs.victoriametrics.com/victoriametrics/metricsql/#bottomk) and `bottomk_...` functions when some of these results contain NaN values. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/5506). Thanks to @xiaozongyang for [the fix](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/5509).
* BUGFIX: all: fix potential panic during components shutdown when [metrics push](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#push-metrics) is configured. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/5548). Thanks to @zhdd99 for the [pull request](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/5549).


## Previous releases

See changes for older releases [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2023/).
