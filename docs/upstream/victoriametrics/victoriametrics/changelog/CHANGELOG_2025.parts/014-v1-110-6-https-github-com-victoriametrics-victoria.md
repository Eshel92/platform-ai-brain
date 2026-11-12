<!-- Part 14 of 19 of victoriametrics/changelog/CHANGELOG_2025.md (split because the page is big). -->

## [v1.110.6](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.110.6)

Released at 2025-04-25

**v1.110.x is a line of [LTS releases](https://docs.victoriametrics.com/victoriametrics/lts-releases/). It contains important up-to-date bugfixes for [VictoriaMetrics Enterprise](https://docs.victoriametrics.com/victoriametrics/enterprise/).
All these fixes are also included in [the latest community release](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/latest).
The v1.110.x line will be supported for at least 12 months since [v1.110.0](https://docs.victoriametrics.com/victoriametrics/changelog/#v11100) release**

* BUGFIX: all the VictoriaMetrics components: properly detect `cgroupv2` [CPU limits](https://www.kernel.org/doc/html/latest/admin-guide/cgroup-v2.html#cpu). See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/8808) for details.
* BUGFIX: [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/): properly init [enterprise](https://docs.victoriametrics.com/victoriametrics/enterprise/) version for `linux/arm` and non-CGO builds. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/6019) for details.
* BUGFIX: [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/): remote write client sets correct content encoding header based on actual body content, rather than relying on configuration. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/8650).
* BUGFIX: [vmbackup](https://docs.victoriametrics.com/victoriametrics/vmbackup/) and [vmbackupmanager](https://docs.victoriametrics.com/victoriametrics/vmbackupmanager/): properly configure s3 client with if `configFilePath` is set. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/8668) for details.
* BUGFIX: [vmsingle](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/), `vmstorage` and `vmselect` in [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): allow using `-downsampling.period=filter:0s:0s` to skip downsampling for time series that match the specified `filter`. See [this doc](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#downsampling).
* BUGFIX: [vmalert](https://docs.victoriametrics.com/victoriametrics/vmalert/): properly set the rule group id in `/rules` and `/alerts` APIs. Previously, the group id was not set, preventing rules from being toggled by group in the vmalert UI. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/8773).


## [v1.110.5](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.110.5)

Released at 2025-04-04

**v1.110.x is a line of [LTS releases](https://docs.victoriametrics.com/victoriametrics/lts-releases/). It contains important up-to-date bugfixes for [VictoriaMetrics Enterprise](https://docs.victoriametrics.com/victoriametrics/enterprise/).
All these fixes are also included in [the latest community release](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/latest).
The v1.110.x line will be supported for at least 12 months since [v1.110.0](https://docs.victoriametrics.com/victoriametrics/changelog/#v11100) release**

* SECURITY: upgrade Go builder from Go1.23.6 to Go1.23.8. See the list of issues addressed in [Go1.23.8](https://github.com/golang/go/issues?q=milestone%3AGo1.23.8+label%3ACherryPickApproved).

* BUGFIX: [vmgateway](https://docs.victoriametrics.com/victoriametrics/vmgateway/): properly set the `Host` header when routing requests to `-write.url` and `-read.url`, which is needed for reverse proxies like Traefik.
* BUGFIX: [vmauth](https://docs.victoriametrics.com/victoriametrics/vmauth/): return `502 Bad Gateway` status code in case request failed due to a network timeout. Previously, vmauth would incorrectly return `200 OK`. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/8621).
* BUGFIX: [vmbackup](https://docs.victoriametrics.com/victoriametrics/vmbackup/), [vmrestore](https://docs.victoriametrics.com/victoriametrics/vmrestore/), [vmbackupmanager](https://docs.victoriametrics.com/victoriametrics/vmbackupmanager/): fix compatibility with S3-compatible storages which do not support data integrity checks. See [this issue](https://github.com/victoriaMetrics/victoriaMetrics/issues/8622).


## [v1.110.4](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.110.4)

Released at 2025-03-21

**v1.110.x is a line of [LTS releases](https://docs.victoriametrics.com/victoriametrics/lts-releases/). It contains important up-to-date bugfixes for [VictoriaMetrics Enterprise](https://docs.victoriametrics.com/victoriametrics/enterprise/).
All these fixes are also included in [the latest community release](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/latest).
The v1.110.x line will be supported for at least 12 months since [v1.110.0](https://docs.victoriametrics.com/victoriametrics/changelog/#v11100) release**

* SECURITY: upgrade golang.org/x/net from v0.33.0 to v0.36.0 to address [CVE-2025-22870](https://github.com/advisories/GHSA-qxp5-gwg8-xv66).

* BUGFIX: [vmbackupmanager](https://docs.victoriametrics.com/victoriametrics/vmbackupmanager/): do not set `vm_backup_last_run_failed` metric to `1` when running vmbackupmanager with an empty storage. Previously, the metrics was set to `1` even though backup was not created yet. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/8490).
* BUGFIX: [vmalert](https://docs.victoriametrics.com/victoriametrics/vmalert/), [vmctl](https://docs.victoriametrics.com/victoriametrics/vmctl/), [vmbackup](https://docs.victoriametrics.com/victoriametrics/vmbackup/), [vmrestore](https://docs.victoriametrics.com/victoriametrics/vmrestore/), [vmbackupmanager](https://docs.victoriametrics.com/victoriametrics/vmbackupmanager/): properly apply TLS settings for URLs with scheme other than `https`. Previously, TLS settings were ignored for such URLs. That could lead to unexpected behavior when a request was receiving a redirect response to a URL with `https` scheme. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/8494) for details.
* BUGFIX: [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/): prevent dropping persistent queue data when changes happened for `-remoteWrite.showURL` flag, query params or fragment in remote write URL. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/8477).
* BUGFIX: [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/): properly send staleness markers if scrape error occurs. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/8528) for details.
* BUGFIX: `vmselect` in [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): properly handle `multitenant` query request on storage communication error. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/8461) for details.
* BUGFIX: [vmalert](https://docs.victoriametrics.com/victoriametrics/vmalert/): fix memory leak when sending alerts with `-notifier.blackhole` enabled. Bug was introduced in [v1.112.0](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.112.0).
* BUGFIX: [vmalert](https://docs.victoriametrics.com/victoriametrics/vmalert/): properly compare rules `group.checksum` and statically define `group.id` at creation time. See [this PR](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/8540) for details.
* BUGFIX: [vmalert](https://docs.victoriametrics.com/victoriametrics/vmalert/): fix memory leak during rule group updates on reload. Bug was introduced in [v1.112.0](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.112.0). See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/8532).
* BUGFIX: [vmgateway](https://docs.victoriametrics.com/victoriametrics/vmgateway/): fix the `vmgateway_ratelimit_refresh_duration_seconds` value, before it did not account for the actual time spent refreshing limits.


## [v1.110.3](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.110.3)

Released at 2025-03-07

**v1.110.x is a line of [LTS releases](https://docs.victoriametrics.com/victoriametrics/lts-releases/). It contains important up-to-date bugfixes for [VictoriaMetrics Enterprise](https://docs.victoriametrics.com/victoriametrics/enterprise/).
All these fixes are also included in [the latest community release](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/latest).
The v1.110.x line will be supported for at least 12 months since [v1.110.0](https://docs.victoriametrics.com/victoriametrics/changelog/#v11100) release**

**Update note 1: [vmsingle](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/) and [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/) include a fix which enforces IPv6 addresses escaping for containers discovered with [Kubernetes service-discovery](https://docs.victoriametrics.com/victoriametrics/sd_configs/#kubernetes_sd_configs) and `role: pod` which do not have exposed ports defined. This means that `address` for these containers will always be wrapped in square brackets, this might affect some relabeling rules which were relying on previous behaviour.**

* BUGFIX: [Single-node VictoriaMetrics](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/) and [vmstorage](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): fix the incorrect caching of extMetricsIDs when a query timeout error occurs. This can lead to incorrect query results. Thanks to @changshun-shi for [the bug report issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/8345).
* BUGFIX: [vmctl](https://docs.victoriametrics.com/victoriametrics/vmctl/): respect time filter when exploring time series for [influxdb mode](https://docs.victoriametrics.com/victoriametrics/vmctl/influxdb/). See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/8259) for details.
* BUGFIX: [vmsingle](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/): properly apply global relabeling configuration, defined with  `-relabelConfig` flag, for metrics scrapped with `-promscrape.config`. Bug was introduces in [v1.108.0](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.108.0). See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/8389).
* BUGFIX: [vmbackupmanager](https://docs.victoriametrics.com/victoriametrics/vmbackupmanager/): properly propagate an error message when applying retention policy fails. Previously, an actual error messages was discarded.
* BUGFIX: [vmgateway](https://docs.victoriametrics.com/victoriametrics/vmgateway/): fix data query in [rate limiter](https://docs.victoriametrics.com/victoriametrics/vmgateway/#rate-limiter). The bug was introduced in [this commit](https://github.com/VictoriaMetrics/VictoriaMetrics/commit/68bad22fd26d1436ad0236b1f3ced8604c5d851c) starting from [v1.106.0](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.106.0).
* BUGFIX: [vmgateway](https://docs.victoriametrics.com/victoriametrics/vmgateway/): properly apply the [rate limiter](https://docs.victoriametrics.com/victoriametrics/vmgateway/#rate-limiter) for the `rows_inserted` limit type. Previously, the rate limit for this type was ignored.
* BUGFIX: [vmgateway](https://docs.victoriametrics.com/victoriametrics/vmgateway/): properly handle HTTP requests with path ending with a trailing `/` when using the [rate limiter](https://docs.victoriametrics.com/victoriametrics/vmgateway/#rate-limiter). Previously, the trailing slash was removed and caused an incorrect redirect path when visiting VMUI. Thanks to @jindov for [the bug report issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/8439).
* BUGFIX: [vmsingle](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/) and [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/): properly escape IPv6 address in [Kubernetes service-discovery](https://docs.victoriametrics.com/victoriametrics/sd_configs/#kubernetes_sd_configs) with `role: pod` for containers without exposed ports. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/8374).
* BUGFIX: [vmui](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#vmui): fix an infinite loader on the [Downsampling filters debug page](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#vmui) when provided configuration matches no series. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/8339).
* BUGFIX: [MetricsQL](https://docs.victoriametrics.com/victoriametrics/metricsql/): fix filters pushdown logic for expression like `foo{a="a"} ifnot bar{a="b"}`. Previously, filters from right operand were incorrectly propagated to the left operand and could result in empty query results even if `foo{a="a"}` matches time series. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/8435).
* BUGFIX: [vmsingle](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/), `vmselect` in [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): prevent possible panic for `foo @ bar` expression when first sample in `bar` starts with `NaN` or starts long after first sample in `foo`. Now, VM will try to find first non-NaN value in `bar` and could yield an error `@ modifier must return a non-NaN value` if it won't find it. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/8444).
* BUGFIX: [Single-node VictoriaMetrics](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/) and [vmstorage](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): prevent panic when using with rules that have zero interval: `-downsampling.period=5m:5m,0s:0s`. Such rule configuration shouldn't be rejected and cause an error when used. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/8454).


## [v1.110.2](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.110.2)

Released at 2025-02-21

**v1.110.x is a line of [LTS releases](https://docs.victoriametrics.com/victoriametrics/lts-releases/). It contains important up-to-date bugfixes for [VictoriaMetrics Enterprise](https://docs.victoriametrics.com/victoriametrics/enterprise/).
All these fixes are also included in [the latest community release](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/latest).
The v1.110.x line will be supported for at least 12 months since [v1.110.0](https://docs.victoriametrics.com/victoriametrics/changelog/#v11100) release**

* SECURITY: upgrade Go builder from Go1.23.5 to Go1.23.6. See the list of issues addressed in [Go1.23.6](https://github.com/golang/go/issues?q=milestone%3AGo1.23.6+label%3ACherryPickApproved).
* SECURITY: upgrade base docker image (Alpine) from 3.21.2 to 3.21.3. See [Alpine 3.21.3 release notes](https://alpinelinux.org/posts/Alpine-3.18.12-3.19.7-3.20.6-3.21.3-released.html).

* BUGFIX: [vmalert](https://docs.victoriametrics.com/victoriametrics/vmalert/): fix polluted alert messages when multiple Alertmanager instances are configured with `alert_relabel_configs`. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/8040), and thanks to @evkuzin for [the pull request](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/8258).
* BUGFIX: [vmalert](https://docs.victoriametrics.com/victoriametrics/vmalert/): fix the auto-generated metrics for alerts and groups. Previously, metrics might be missing after reload. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/8229) for the details.
* BUGFIX: `vminsert` in [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/) and `vmstorage` in [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): properly return parsing errors during data ingestion in [multi-level cluster setup](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/#multi-level-cluster-setup). Before, some of the errors could have been silently ignored.
* BUGFIX: [Single-node VictoriaMetrics](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/) and [vmselect](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): properly enforce presence of default `-retentionPeriod` configuration for [retention filters](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#retention-filters) debug interface. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/8343).


## [v1.110.1](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.110.1)

Released at 2025-02-10

**v1.110.x is a line of [LTS releases](https://docs.victoriametrics.com/victoriametrics/lts-releases/). It contains important up-to-date bugfixes for [VictoriaMetrics Enterprise](https://docs.victoriametrics.com/victoriametrics/enterprise/).
All these fixes are also included in [the latest community release](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/latest).
The v1.110.x line will be supported for at least 12 months since [v1.110.0](https://docs.victoriametrics.com/victoriametrics/changelog/#v11100) release**

* BUGFIX: [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/): properly perform graceful shutdown for kafka client.
* BUGFIX: [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/): properly add message metadata headers for kafka remoteWrite target.
* BUGFIX: [vmui](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#vmui): improve clipboard error handling in tables and code snippets by showing detailed messages with possible reasons. See [this pull request](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/7778).
* BUGFIX: [vmsingle](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/) and `vmstorage` in [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): properly update number of unique series for [cardinality limiter](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#cardinality-limiter) on ingestion. Previously, limit could undercount the real number of the ingested unique series.
* BUGFIX: [Single-node VictoriaMetrics](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/) and [vmselect](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): fix discrepancies when using `or` binary operator. See [this](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/7759) and [this](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/7640) issues for details.
* BUGFIX: [vmui](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#vmui) for [VictoriaMetrics Enterprise](https://docs.victoriametrics.com/victoriametrics/enterprise/) components: properly display enterprise features when the enterprise version is used.
