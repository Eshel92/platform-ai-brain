<!-- Part 17 of 19 of victoriametrics/changelog/CHANGELOG_2025.md (split because the page is big). -->

## [v1.102.16](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.102.16)

Released at 2025-03-07

**v1.102.x is a line of [LTS releases](https://docs.victoriametrics.com/victoriametrics/lts-releases/). It contains important up-to-date bugfixes for [VictoriaMetrics Enterprise](https://docs.victoriametrics.com/victoriametrics/enterprise/).
All these fixes are also included in [the latest community release](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/latest).
The v1.102.x line will be supported for at least 12 months since [v1.102.0](https://docs.victoriametrics.com/victoriametrics/changelog/#v11020) release**

* BUGFIX: [vmgateway](https://docs.victoriametrics.com/victoriametrics/vmgateway/): properly apply the [rate limiter](https://docs.victoriametrics.com/victoriametrics/vmgateway/#rate-limiter) for the `rows_inserted` limit type. Previously, the rate limit for this type was ignored.
* BUGFIX: [vmgateway](https://docs.victoriametrics.com/victoriametrics/vmgateway/): properly handle HTTP requests with path ending with a trailing `/` when using the [rate limiter](https://docs.victoriametrics.com/victoriametrics/vmgateway/#rate-limiter). Previously, the trailing slash was removed and caused an incorrect redirect path when visiting VMUI. Thanks to @jindov for [the bug report issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/8439).
* BUGFIX: [vmsingle](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/), `vmselect` in [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): prevent possible panic for `foo @ bar` expression when first sample in `bar` starts with `NaN` or starts long after first sample in `foo`. Now, VM will try to find first non-NaN value in `bar` and could yield an error `@ modifier must return a non-NaN value` if it won't find it. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/8444).
* BUGFIX: [Single-node VictoriaMetrics](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/) and [vmstorage](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): prevent panic when using with rules that have zero interval: `-downsampling.period=5m:5m,0s:0s`. Such rule configuration shouldn't be rejected and cause an error when used. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/8454).


## [v1.102.15](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.102.15)

Released at 2025-02-28

**v1.102.x is a line of [LTS releases](https://docs.victoriametrics.com/victoriametrics/lts-releases/). It contains important up-to-date bugfixes for [VictoriaMetrics Enterprise](https://docs.victoriametrics.com/victoriametrics/enterprise/).
All these fixes are also included in [the latest community release](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/latest).
The v1.102.x line will be supported for at least 12 months since [v1.102.0](https://docs.victoriametrics.com/victoriametrics/changelog/#v11020) release**

**Update note 1: [vmsingle](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/) and [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/) include a fix which enforces IPv6 addresses escaping for containers discovered with [Kubernetes service-discovery](https://docs.victoriametrics.com/victoriametrics/sd_configs/#kubernetes_sd_configs) and `role: pod` which do not have exposed ports defined. This means that `address` for these containers will always be wrapped in square brackets, this might affect some relabeling rules which were relying on previous behaviour.**

* SECURITY: upgrade golang.org/x/net from v0.31.0 to v0.33.0 to address [GHSA-w32m-9786-jp63](https://github.com/advisories/GHSA-w32m-9786-jp63).

* BUGFIX: [Single-node VictoriaMetrics](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/) and [vmstorage](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): fix the incorrect caching of extMetricsIDs when a query timeout error occurs. This can lead to incorrect query results. Thanks to @changshun-shi for [the bug report issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/8345).
* BUGFIX: [vmctl](https://docs.victoriametrics.com/victoriametrics/vmctl/): respect time filter when exploring time series for [influxdb mode](https://docs.victoriametrics.com/victoriametrics/vmctl/influxdb/). See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/8259) for details.
* BUGFIX: [vmsingle](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/) and [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/): properly escape IPv6 address in [Kubernetes service-discovery](https://docs.victoriametrics.com/victoriametrics/sd_configs/#kubernetes_sd_configs) with `role: pod` for containers without exposed ports. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/8374).


## [v1.102.14](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.102.14)

Released at 2025-02-21

**v1.102.x is a line of [LTS releases](https://docs.victoriametrics.com/victoriametrics/lts-releases/). It contains important up-to-date bugfixes for [VictoriaMetrics Enterprise](https://docs.victoriametrics.com/victoriametrics/enterprise/).
All these fixes are also included in [the latest community release](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/latest).
The v1.102.x line will be supported for at least 12 months since [v1.102.0](https://docs.victoriametrics.com/victoriametrics/changelog/#v11020) release**

* SECURITY: upgrade Go builder from Go1.23.5 to Go1.23.6. See the list of issues addressed in [Go1.23.6](https://github.com/golang/go/issues?q=milestone%3AGo1.23.6+label%3ACherryPickApproved).
* SECURITY: upgrade base docker image (Alpine) from 3.21.2 to 3.21.3. See [Alpine 3.21.3 release notes](https://alpinelinux.org/posts/Alpine-3.18.12-3.19.7-3.20.6-3.21.3-released.html).

* BUGFIX: `vminsert` in [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/) and `vmstorage` in [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): properly return parsing error for data ingestion.
* BUGFIX: [vmalert](https://docs.victoriametrics.com/victoriametrics/vmalert/): fix the auto-generated metrics for alerts and groups. Previously, metrics might be missing after reload. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/8229) for the details.


## [v1.102.13](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.102.13)

Released at 2025-02-10

**v1.102.x is a line of [LTS releases](https://docs.victoriametrics.com/victoriametrics/lts-releases/). It contains important up-to-date bugfixes for [VictoriaMetrics Enterprise](https://docs.victoriametrics.com/victoriametrics/enterprise/).
All these fixes are also included in [the latest community release](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/latest).
The v1.102.x line will be supported for at least 12 months since [v1.102.0](https://docs.victoriametrics.com/victoriametrics/changelog/#v11020) release**

* BUGFIX: [export API](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#how-to-export-time-series): cancel export process on client connection close. Previously client connection close was ignored and VictoriaMetrics started to hog CPU by exporting metrics to nowhere until it export all of them.
* BUGFIX: [Single-node VictoriaMetrics](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/) and [vmselect](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): fix discrepancies when using `or` binary operator. See [this](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/7759) and [this](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/7640) issues for details.
* BUGFIX: [vmsingle](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/) and `vmstorage` in [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): properly update number of unique series for [cardinality limiter](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#cardinality-limiter) on ingestion. Previously, limit could undercount the real number of the ingested unique series.


## [v1.102.12](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.102.12)

Released at 2025-01-28

**v1.102.x is a line of [LTS releases](https://docs.victoriametrics.com/victoriametrics/lts-releases/). It contains important up-to-date bugfixes for [VictoriaMetrics Enterprise](https://docs.victoriametrics.com/victoriametrics/enterprise/).
All these fixes are also included in [the latest community release](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/latest).
The v1.102.x line will be supported for at least 12 months since [v1.102.0](https://docs.victoriametrics.com/victoriametrics/changelog/#v11020) release**

* BUGFIX: [vmsingle](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/), `vminsert` in [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/) and [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/): log metric names for signals with unsupported delta temporality on ingestion via [OpenTelemetry protocol for metrics](https://docs.victoriametrics.com/victoriametrics/integrations/opentelemetry/). Thanks to @chenlujjj for [the pull request](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/8018).
* BUGFIX: [Single-node VictoriaMetrics](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/) and [vmselect](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): respect staleness detection in increase, increase_pure and delta functions when time series has gaps and `-search.maxStalenessInterval` is set. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/8072) for details.


## [v1.102.11](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.102.11)

Released at 2025-01-24

It is recommended upgrading to [v1.102.12](https://docs.victoriametrics.com/victoriametrics/changelog/#v110212) because [v1.102.11](https://docs.victoriametrics.com/victoriametrics/changelog/#v110211) contains a bug with staleness detection.

**v1.102.x is a line of [LTS releases](https://docs.victoriametrics.com/victoriametrics/lts-releases/). It contains important up-to-date bugfixes for [VictoriaMetrics Enterprise](https://docs.victoriametrics.com/victoriametrics/enterprise/).
All these fixes are also included in [the latest community release](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/latest).
The v1.102.x line will be supported for at least 12 months since [v1.102.0](https://docs.victoriametrics.com/victoriametrics/changelog/#v11020) release**

* SECURITY: upgrade Go builder from Go1.23.4 to Go1.23.5. See the list of issues addressed in [Go1.23.5](https://github.com/golang/go/issues?q=milestone%3AGo1.23.5+label%3ACherryPickApproved).

* BUGFIX: [vmauth](https://docs.victoriametrics.com/victoriametrics/vmauth/): fix possible runtime panic during requests processing under heavy load. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/8051) for details.
* BUGFIX: all VictoriaMetrics [enterprise](https://docs.victoriametrics.com/victoriametrics/enterprise/) components: properly trim whitespaces at the end of license provided via `-license` and `-licenseFile` command-line flags. Previously, the trailing whitespaces could cause the license verification to fail.
* BUGFIX: all VictoriaMetrics [enterprise](https://docs.victoriametrics.com/victoriametrics/enterprise/) components: remove unnecessary delay before failing if all online verification attempts have failed. This should reduce the time required for the component to proceed if all online verification attempts have failed.
* BUGFIX: [Single-node VictoriaMetrics](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/) and [vmselect](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): don't take into account the last raw sample before the lookbehind window is sample exceeds the staleness interval. This affects correctness of increase, increase_pure, delta functions when performing calculations on time series with gaps. See [this pull request](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/8002) for details.
* BUGFIX: [vmsingle](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/), `vminsert` in [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/) and [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/): allow ingesting histograms with missing `_sum` metric via [OpenTelemetry ingestion protocol](https://docs.victoriametrics.com/victoriametrics/integrations/opentelemetry/) in the same way as Prometheus does.


## [v1.102.10](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.102.10)

Released at 2025-01-14

**v1.102.x is a line of [LTS releases](https://docs.victoriametrics.com/victoriametrics/lts-releases/). It contains important up-to-date bugfixes for [VictoriaMetrics Enterprise](https://docs.victoriametrics.com/victoriametrics/enterprise/).
All these fixes are also included in [the latest community release](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/latest).
The v1.102.x line will be supported for at least 12 months since [v1.102.0](https://docs.victoriametrics.com/victoriametrics/changelog/#v11020) release**

* FEATURE: all VictoriaMetrics [enterprise](https://docs.victoriametrics.com/victoriametrics/enterprise/) components: add support of hot-reload for license key supplied by `-licenseFile` command-line flag.

* BUGFIX: [vmsingle](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/), `vmselect` in [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): make instant query results consistent. VictoriaMetrics detects and adjusts scrape interval and while this is very useful for range queries (i.e. this eliminates gaps on the graph), it may cause instant queries to return a non-empty result when no result is expected. The fix is to disable scrape interval detection and always use the step as the scrape interval in instant queries. This will guarantee that the samples are searched within the (time-step, time] interval. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/5796) for details.
* BUGFIX: [vmui](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#vmui): fix cursor reset in query input field. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/7288).
* BUGFIX: [vmauth](https://docs.victoriametrics.com/victoriametrics/vmauth/): properly handle discovery for ipv6 addresses. Thanks to @badie for the [pull request](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/7955).
* BUGFIX: [vmctl](https://docs.victoriametrics.com/victoriametrics/vmctl/): fix support for migrating influx series without any tag. See [this pull request](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/7935). Thanks to @bitbidu for reporting.
* BUGFIX: `vminsert` in [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): storage nodes defined in `-storageNode` are now sorted, ensuring that varying node orders across different vminsert instances do not result in inconsistent replication.


## [v1.102.9](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.102.9)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2024/#v11029)


## [v1.102.8](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.102.8)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2024/#v11028)


## [v1.102.7](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.102.7)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2024/#v11027)


## [v1.102.6](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.102.6)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2024/#v11026)


## [v1.102.5](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.102.5)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2024/#v11025)


## [v1.102.4](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.102.4)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2024/#v11024)


## [v1.102.3](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.102.3)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2024/#v11023)


## [v1.102.2](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.102.2)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2024/#v11022)


## [v1.102.1](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.102.1)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2024/#v11021)


## [v1.102.0](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.102.0)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2024/#v11020)


## [v1.102.0-rc2](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.102.0-rc2)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2024/#v11020-rc2)


## [v1.102.0-rc1](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.102.0-rc1)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2024/#v11020-rc1)


## [v1.101.0](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.101.0)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2024/#v11010)


## [v1.100.1](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.100.1)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2024/#v11001)


## [v1.100.0](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.100.0)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2024/#v11000)


## [v1.99.0](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.99.0)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2024/#v1990)


## [v1.98.0](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.98.0)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2024/#v1980)
