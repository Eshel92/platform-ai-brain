<!-- Part 23 of 27 of victoriametrics/changelog/CHANGELOG.md (split because the page is big). -->

## [v1.122.24](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.122.24)

Released at 2026-06-05

**v1.122.x is a line of [LTS releases](https://docs.victoriametrics.com/victoriametrics/lts-releases/). It contains important up-to-date bugfixes for [VictoriaMetrics enterprise](https://docs.victoriametrics.com/victoriametrics/enterprise/).
All these fixes are also included in [the latest community release](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/latest).
The v1.122.x line will be supported for at least 12 months since [v1.122.0](https://docs.victoriametrics.com/victoriametrics/changelog/#v11220) release**

* SECURITY: upgrade Go builder from Go1.26.3 to Go1.26.4. See [the list of issues addressed in Go1.26.4](https://github.com/golang/go/issues?q=milestone%3AGo1.26.4%20label%3ACherryPickApproved).

* BUGFIX: [MetricsQL](https://docs.victoriametrics.com/victoriametrics/metricsql/): `integrate()` no longer extrapolates the last sample's value past the end of the time series. Previously, querying `integrate(metric[1h])` at a timestamp where the series had already ended would keep accruing area as if the last value continued indefinitely, producing values much larger than the true integral. See [#9474](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/9474). Thanks to @wtfashwin for contribution.
* BUGFIX: [vmalert](https://docs.victoriametrics.com/victoriametrics/vmalert/): reset the group evaluation timestamp if it exceeds the current host time. Previously, vmalert could use future timestamps for evaluations if the system clock was shifted backward. See [#10985](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/10985).
* BUGFIX: `vmselect` in [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): avoid returning HTTP 503 for queries with partial results when a storage group is unavailable and `-search.denyPartialResponse` is disabled. See [#11009](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/11009). Thanks to @fxrlv for the contribution.
* BUGFIX: [vmsingle](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/) and `vmselect` in [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): properly escape `utf-8` label names for [/federate](https://docs.victoriametrics.com/victoriametrics/#federation) API requests. See [#10968](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/10968).
* BUGFIX: `vmselect` in [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): fix intermittent `write: connection timed out` errors caused by silently dropped TCP connections being reused from the connection pool. See [#10735](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/10735#issuecomment-4535832301).


## [v1.122.23](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.122.23)

Released at 2026-05-22

**v1.122.x is a line of [LTS releases](https://docs.victoriametrics.com/victoriametrics/lts-releases/). It contains important up-to-date bugfixes for [VictoriaMetrics enterprise](https://docs.victoriametrics.com/victoriametrics/enterprise/).
All these fixes are also included in [the latest community release](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/latest).
The v1.122.x line will be supported for at least 12 months since [v1.122.0](https://docs.victoriametrics.com/victoriametrics/changelog/#v11220) release**

* BUGFIX: [stream aggregation](https://docs.victoriametrics.com/victoriametrics/stream-aggregation/): stop emitting stale values for `quantiles(...)` outputs when a time series has no samples during the current aggregation interval. See [#10918](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/10918). Thanks to @alexei38 for the contribution.
* BUGFIX: [stream aggregation](https://docs.victoriametrics.com/victoriametrics/stream-aggregation/): extend delay on aggregation windows flush by the biggest lag among pushed samples. Before, the delay was calculated as 95th percentile across samples, which could underrepresent outliers and reject them from aggregation as "too old". See [#10402](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/10402).
* BUGFIX: [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/): fix a bug in [cardinality limiters](https://docs.victoriametrics.com/victoriametrics/vmagent/#cardinality-limiter) where series with different labels, like `{a="bc"}` and `{ab="c"}`, could be incorrectly treated as identical and dropped. See [#10937](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/10937).
* BUGFIX: [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/): hide values passed to `-remoteWrite.headers` in startup logs, `/metrics`, and `/flags`, since they can contain sensitive HTTP headers such as `Authorization` and API keys.
* BUGFIX: [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/): hide values passed to `-remoteWrite.proxyURL` in startup logs, `/metrics`, and `/flags`, since they can contain sensitive credentials.
* BUGFIX: [vmalert](https://docs.victoriametrics.com/victoriametrics/vmalert/): hide values passed to `-remoteWrite.headers`,`remoteRead.headers`, `datasource.headers` and `notifier.headers` in startup logs, `/metrics`, and `/flags`, since they can contain sensitive HTTP headers such as `Authorization` and API keys.
* BUGFIX: [vmrestore](https://docs.victoriametrics.com/victoriametrics/vmrestore/): fix a bug where specifying `-storageDataPath` with a trailing slash could cause `vmrestore` to panic. See [#10823](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/10823). Thanks to @utafrali for the contribution.
* BUGFIX: [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/): prevent unintentional rerouting of samples to other sharding targets when one of the `-remoteWrite.url` targets with `-remoteWrite.disableOnDiskQueue` becomes blocked. Previously this could break the sharding guarantee by sending samples to wrong targets instead of dropping or retrying them. See [#10507](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/10507).
* BUGFIX: [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/): return error on startup if `-remoteWrite.disableOnDiskQueue` is not configured uniformly across all `-remoteWrite.url` targets when `-remoteWrite.shardByURL` is enabled. Either all targets must have it enabled or all must have it disabled. See [#10507](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/10507).
* BUGFIX: [vmsingle](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/) and `vmselect` in [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): hide values passed to `vmalert.proxyURL` in startup logs, `/metrics`, and `/flags`, since they can contain sensitive HTTP headers such as `Authorization` and API keys.
* BUGFIX: [vmui](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#vmui): preserve exact series values in graph tooltips instead of rounding them by significant digits. See [#10952](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/10952).


## [v1.122.22](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.122.22)

Released at 2026-05-08

**v1.122.x is a line of [LTS releases](https://docs.victoriametrics.com/victoriametrics/lts-releases/). It contains important up-to-date bugfixes for [VictoriaMetrics enterprise](https://docs.victoriametrics.com/victoriametrics/enterprise/).
All these fixes are also included in [the latest community release](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/latest).
The v1.122.x line will be supported for at least 12 months since [v1.122.0](https://docs.victoriametrics.com/victoriametrics/changelog/#v11220) release**

* SECURITY: upgrade Go builder from Go1.26.2 to Go1.26.3. See [the list of issues addressed in Go1.26.3](https://github.com/golang/go/issues?q=milestone%3AGo1.26.3%20label%3ACherryPickApproved).

* BUGFIX: [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/) and [vmsingle](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/): properly obtain `__meta_hetzner_hcloud_location` and `__meta_hetzner_hcloud_location_network_zone` labels for [hetzner_sd_configs](https://docs.victoriametrics.com/victoriametrics/sd_configs/#hetzner_sd_configs). Hetzner changed discovery [API response](https://docs.hetzner.cloud/changelog#2025-12-16-phasing-out-datacenters) and returns `location` information from different field. See [#10909](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/10909). Thanks to @juliusrickert for contribution.
* BUGFIX: [vmsingle](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/): and `vmselect` in [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): give priority to `extra_label` and `extra_filters[]` params defined in URL query string over those defined in request body form, to properly respect constraints imposed by `vmauth`. See [#10908](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/10908).
* BUGFIX: [vmsingle](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/) and `vmselect` in [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): set CORS headers on `/api/v1/export`, `/api/v1/export/csv` and `/api/v1/export/native`. See [#10899](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/10899). Thanks to @andriibeee for the contribution.


## [v1.122.21](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.122.21)

Released at 2026-04-24

**v1.122.x is a line of [LTS releases](https://docs.victoriametrics.com/victoriametrics/lts-releases/). It contains important up-to-date bugfixes for [VictoriaMetrics enterprise](https://docs.victoriametrics.com/victoriametrics/enterprise/).
All these fixes are also included in [the latest community release](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/latest).
The v1.122.x line will be supported for at least 12 months since [v1.122.0](https://docs.victoriametrics.com/victoriametrics/changelog/#v11220) release**

* SECURITY: upgrade Go builder from Go1.25.9 to Go1.26.2. See [the list of issues addressed in Go1.26.2](https://github.com/golang/go/issues?q=milestone%3AGo1.26.2%20label%3ACherryPickApproved).
* SECURITY: upgrade base docker image (Alpine) from 3.23.2 to 3.23.3. See [Alpine 3.23.4 release notes](https://www.alpinelinux.org/posts/Alpine-3.20.10-3.21.7-3.22.4-3.23.4-released.html).

* BUGFIX: all VictoriaMetrics components: properly parse IPv6 source address when accepting connections with proxy protocol v2 enabled. See [#10839](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/10839). Thanks to @andriibeee for the contribution.
* BUGFIX: [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/) and [vmsingle](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/): `-maxScrapeSize` is now correctly applied when reading response bodies, including non-OK scrape error responses. See [#10804](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/10804).
* BUGFIX: `vminsert` in [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): properly allocate vminsert buffer size per vmstorage node based on available CPU, memory and storage node count to reduce OOM risk. See [#10725](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/10725).
* BUGFIX: [vmrestore](https://docs.victoriametrics.com/victoriametrics/vmrestore/): fix an issue where vmrestore could hang indefinitely when interrupted during backup download. See [#10794](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/10794).
* BUGFIX: [vmsingle](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/): properly execute graceful shutdown for vmsingle if `-maxIngestionRate` is configured. See [#10795](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/10795).
* BUGFIX: [vmalert](https://docs.victoriametrics.com/victoriametrics/vmalert/): delete labels from rule results if they are specified with an empty string value in rule or group labels. See [#10766](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/10766).
* BUGFIX: [vmui](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#vmui): use contrasting colors when displaying time series to improve visibility on light and dark themes. See [#10869](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/10869).


## [v1.122.20](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.122.20)

Released at 2026-04-23

**v1.122.x is a line of [LTS releases](https://docs.victoriametrics.com/victoriametrics/lts-releases/). It contains important up-to-date bugfixes for [VictoriaMetrics enterprise](https://docs.victoriametrics.com/victoriametrics/enterprise/).
All these fixes are also included in [the latest community release](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/latest).
The v1.122.x line will be supported for at least 12 months since [v1.122.0](https://docs.victoriametrics.com/victoriametrics/changelog/#v11220) release**

* BUGFIX: [vmsingle](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/) and `vmselect` in [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): fix incorrect evaluation of binary operations caused by an ordering bug (e.g. `10 - (3 + 3 + 4)` being evaluated as `10 - 3 + 3 + 4`). The issue was introduced in v1.140.0, v1.136.4, and v1.122.19. See [#10856](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/10856).


## [v1.122.19](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.122.19)

**Update Note 1:** [MetricsQL](https://docs.victoriametrics.com/victoriametrics/metricsql/): Due to an ordering bug in binary operations, some queries may produce incorrect results. For example, `10 - (3 + 3 + 4)` is evaluated as `10 - 3 + 3 + 4`. The issue was introduced in versions v1.140.0, v1.136.4, v1.122.19, and is addressed in upcoming releases. It is strongly recommended to avoid these versions entirely. See [#10856](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/10856).

Released at 2026-04-10

**v1.122.x is a line of [LTS releases](https://docs.victoriametrics.com/victoriametrics/lts-releases/). It contains important up-to-date bugfixes for [VictoriaMetrics enterprise](https://docs.victoriametrics.com/victoriametrics/enterprise/).
All these fixes are also included in [the latest community release](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/latest).
The v1.122.x line will be supported for at least 12 months since [v1.122.0](https://docs.victoriametrics.com/victoriametrics/changelog/#v11220) release**

* SECURITY: upgrade Go builder from Go1.25.8 to Go1.25.9. See [the list of issues addressed in Go1.25.9](https://github.com/golang/go/issues?q=milestone%3AGo1.25.9+label%3ACherryPickApproved).

* BUGFIX: [vmbackup](https://docs.victoriametrics.com/vmbackup/), [vmbackupmanager](https://docs.victoriametrics.com/victoriametrics/vmbackupmanager/): retry the requests that failed with unexpected EOF due to unstable network to S3 service. See [#10699](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/10699).
* BUGFIX: [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/): fix `scrape_series_added` metric to update only on successful scrapes, aligning its behavior with Prometheus. See [#10653](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/10653).
* BUGFIX: `vmselect` in [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): prevent partial responses from second-level vmselect nodes in [multi-level cluster setups](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/#multi-level-cluster-setup). Ensures response completeness and correctness, and avoids cache pollution in top-level vmselect. See [#10678](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/10678)
* BUGFIX: [vmsingle](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/) and `vmstorage` in [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): prevent rare panic during storage start-up at 100% disk usage. See [#10747](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/10747) Thanks to @nmn3m for the contribution.


## [v1.122.18](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.122.18)

Released at 2026-03-27

**v1.122.x is a line of [LTS releases](https://docs.victoriametrics.com/victoriametrics/lts-releases/). It contains important up-to-date bugfixes for [VictoriaMetrics enterprise](https://docs.victoriametrics.com/victoriametrics/enterprise/).
All these fixes are also included in [the latest community release](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/latest).
The v1.122.x line will be supported for at least 12 months since [v1.122.0](https://docs.victoriametrics.com/victoriametrics/changelog/#v11220) release**

* BUGFIX: `vmselect` in [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): retry RPC by dialing a new connection instead of reusing a pooled one when the previous attempt fails with `io.EOF`, `broken pipe` or `reset by peer`. This reduces query failures caused by stale connections to restarted vmstorage nodes. See [#10314](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/10314)
* BUGFIX: [vmsingle](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/) and `vmselect` in [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): enforce `datasource_type=prometheus` when [proxying](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/#vmalert) Grafana requests to [vmalert](https://docs.victoriametrics.com/victoriametrics/vmalert/). Grafana supports only `prometheus` and `loki` alerts. Without this fix, Grafana shows `Error loading alerts` when non-Prometheus alert types are returned. See [victoriametrics-datasource#329](https://github.com/VictoriaMetrics/victoriametrics-datasource/issues/329).
