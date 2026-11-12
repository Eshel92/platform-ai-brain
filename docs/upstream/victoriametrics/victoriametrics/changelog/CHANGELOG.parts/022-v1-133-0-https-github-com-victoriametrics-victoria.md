<!-- Part 22 of 27 of victoriametrics/changelog/CHANGELOG.md (split because the page is big). -->

## [v1.133.0](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.133.0)

Released at 2026-01-02

**Update Note 1:** [vmsingle](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/) and `vmstorage` in [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): Upgrading to per-partition index requires registering all active time series. Expect slow down of data ingestion and queries during upgrade roll-out. This is a one-time operation. Additionally, for users with retention periods shorter than 1 month the disk usage may increase.

**Update Note 2:** [vmsingle](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/) and `vmstorage` in [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): Certain data and query patterns may cause high CPU utilization due to [10154](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/10154). See [10297](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/10297).

**Update Note 3:** [vmsingle](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/) and `vmstorage` in [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): lock contention in the ingestion path may cause frequent context switches and storage connection saturation spikes. See [10367](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/10367). Addressed in `v1.135.0`.

**Update Note 4:** [vmsingle](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/) and `vmstorage` in [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): TSDB status may be empty if the partition index does not have records for the requested date. See [10315](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/10315). Addressed in `v1.135.0`.

**Update Note 5:** [vmsingle](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/) and `vmstorage` in [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): `indexdb/tagFiltersToMetricIDs`, `indexdb/metricID` and `indexdb/date_metricID` cache metrics are not reported properly. See [10275](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/10275). Addressed in `v1.135.0`.

**Update Note 6:** [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/), [vmsingle](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/) and `vminsert` in [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): a bug in [OpenTelemetry](https://docs.victoriametrics.com/victoriametrics/integrations/opentelemetry/) parsing caused the `Unit` suffix of the previously parsed metric to be incorrectly applied to subsequent metrics that have no `Unit` field, when `-opentelemetry.usePrometheusNaming` is enabled. For example, if `http_requests` has `Unit: seconds` and the next metric `cpu_usage` has no `Unit`, `cpu_usage` would be ingested as `cpu_usage_seconds`. The bug was introduced in [v1.132.0](https://github.com/VictoriaMetrics/VictoriaMetrics/blob/master/docs/victoriametrics/changelog/CHANGELOG_2025.md#v11320). See [#10889](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/10889).

* SECURITY: upgrade base docker image (Alpine) from 3.22.2 to 3.23.2. See [Alpine 3.23.2 release notes](https://www.alpinelinux.org/posts/Alpine-3.23.2-released.html).

* FEATURE: [vmagent](https://docs.victoriametrics.com/vmagent/) and [vmsingle](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/): add support for global `sampleLimit` setting. This allows users to efficiently limit the number of samples accepted per scrape target. This also ensures target-level `sample_limit` can correctly override the global setting. See [#10145](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/10145). Thanks to @kobylyanskiy for the contribution.
* FEATURE: [vmauth](https://docs.victoriametrics.com/victoriametrics/vmauth/): expose `vmauth_user_request_backend_requests_total` and `vmauth_unauthorized_user_request_backend_requests_total` [metrics](https://docs.victoriametrics.com/victoriametrics/vmauth/#monitoring), which track the number of requests sent to backends. These counts may exceed `vmauth_user_requests_total` and `vmauth_unauthorized_user_requests_total` when requests are retried across multiple backends. See [#10171](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/10171).
* FEATURE: [vmauth](https://docs.victoriametrics.com/victoriametrics/vmauth/): expose `vmauth_user_request_errors_total` and `vmauth_unauthorized_user_request_errors_total` [metrics](https://docs.victoriametrics.com/victoriametrics/vmauth/#monitoring), which track the number of user request errors. See [#10188](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/10188).
* FEATURE: [vmauth](https://docs.victoriametrics.com/victoriametrics/vmauth/): add `-maxQueueDuration` command-line flag for waiting until the incoming request could be executed if `-maxConcurrentRequests` are already exceeded. This should help with graceful handling of a short spike in the number of concurrent requests without leading to a retry storm. See [#10078](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/10078).
* FEATURE: [vmsingle](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/) and `vmstorage` in [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): introduce per-partition index. This should reduce disk space occupied by indexDBs as they get deleted along with the corresponding partitions once those partitions become outside the retention window. Read more about the motivation behind this feature at [#7599](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/7599) and what to expect at [#8134](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/8134).

* BUGFIX: [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/) and [vmsingle](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/): properly add `exported_` prefix to scraped metrics that have the same names as [auto-generated metrics](https://docs.victoriametrics.com/victoriametrics/vmagent/#automatically-generated-metrics). Previously, some auto-generated metrics were not recognized, so scraped metrics with the same names could overwrite them. See [#10197](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/10197). Thanks to @fxrlv for the contribution.
* BUGFIX: [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/): fix `vmagent_rows_inserted_total{type="newrelic"}` metric to correctly count samples. See [#10191](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/10191). Thanks to @fxrlv for the contribution.
* BUGFIX: [vmauth](https://docs.victoriametrics.com/victoriametrics/vmauth/): fix `vmauth_user_request_backend_errors_total` and `vmauth_unauthorized_user_request_backend_errors_total` to only reflect backend request errors. Previously, these counters could be overcounted with user request error. See [#10177](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/10177).
* BUGFIX: [vmsingle](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/) and `vmstorage` in [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): rotate `dateMetricIDCache` instead of resetting it. This should make the eviction less aggressive. Since the cache does not have fixed max size anymore the `-storage.cacheSizeIndexDBDateMetricID` flag has been removed. See [#10064](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/10064) and PR [#10169](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/10169).
* BUGFIX: [vmsingle](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/): properly add metrics metadata scraped with `promscrape.config` and `selfScrapeInterval`. See [#10175](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/10175).
* BUGFIX: [vmsingle](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/) and `vmstorage` in [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): fix stats collection for `indexdb/tagFiltersToMetricIDs`, `indexdb/metricID`, and `indexdb/date_metricID` caches. As per PR [#10131](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/10131), the stats is collected for most utilized instance only, but if the size of all instances is 0 then the stats won't be collected at all. This may result in max cache size alternating between the actual value and 0. See [#10204](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/10204) and [#10230](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/10230).
* BUGFIX: [vmsingle](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/) and `vmselect` in [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): properly proxy requests to [vmalert](https://docs.victoriametrics.com/victoriametrics/vmalert/) when `-vmalert.proxyURL` flag is set. See [#10178](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/10178).


## [v1.132.0](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.132.0)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2025/#v11320)


## [v1.131.0](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.131.0)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2025/#v11310)


## [v1.130.0](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.130.0)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2025/#v11300)


## [v1.129.1](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.129.1)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2025/#v11291)


## [v1.129.0](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.129.0)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2025/#v11290)


## [v1.128.0](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.128.0)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2025/#v11280)


## [v1.127.0](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.127.0)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2025/#v11270)


## [v1.126.0](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.126.0)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2025/#v11260)


## [v1.125.1](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.125.1)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2025/#v11251)


## [v1.125.0](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.125.0)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2025/#v11250)


## [v1.124.0](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.124.0)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2025/#v11240)


## [v1.123.0](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.123.0)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2025/#v11230)


## [v1.122.27](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.122.27)

Released at 2026-07-17

**v1.122.x is a line of [LTS releases](https://docs.victoriametrics.com/victoriametrics/lts-releases/). It contains important up-to-date bugfixes for [VictoriaMetrics enterprise](https://docs.victoriametrics.com/victoriametrics/enterprise/).
All these fixes are also included in [the latest community release](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/latest).
The v1.122.x line will be supported for at least 12 months since [v1.122.0](https://docs.victoriametrics.com/victoriametrics/changelog/#v11220) release**

* BUGFIX: [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/): flush pending persistent queue data to chunk file before updating the metadata. This prevents the metadata writer offset from getting ahead of the chunk file size and avoids losing the persistent queue after an unclean shutdown. See [#11192](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/11192).
* BUGFIX: [vmbackup](https://docs.victoriametrics.com/victoriametrics/vmbackup/) and [vmbackupmanager](https://docs.victoriametrics.com/victoriametrics/vmbackupmanager/): retry S3 requests failing with `HTTP 429` status code or `TooManyRequests` error code. Previously such requests were not retried, so a short burst of rate limiting would fail the whole backup. See [#11218](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/11218). Thanks to @gautamrizwani for contribution.
* BUGFIX: [vmui](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#vmui): hide `Total metric names` stats on [Cardinality Explorer](https://docs.victoriametrics.com/victoriametrics/#cardinality-explorer) page when user selects a specific metric or label to focus. See [#11154](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/11154) for details. Thanks to @lghuy05 for the contribution.


## [v1.122.26](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.122.26)

Released at 2026-07-03

**v1.122.x is a line of [LTS releases](https://docs.victoriametrics.com/victoriametrics/lts-releases/). It contains important up-to-date bugfixes for [VictoriaMetrics enterprise](https://docs.victoriametrics.com/victoriametrics/enterprise/).
All these fixes are also included in [the latest community release](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/latest).
The v1.122.x line will be supported for at least 12 months since [v1.122.0](https://docs.victoriametrics.com/victoriametrics/changelog/#v11220) release**

* SECURITY: upgrade base docker image (Alpine) from 3.23.4 to 3.24.1. See [Alpine 3.24.1 release notes](https://www.alpinelinux.org/posts/Alpine-3.24.1-released.html).

* BUGFIX: `vminsert` in [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/) and [vmsingle](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/): properly check values range for the limits configured with flags `-maxLabelsPerTimeseries`, `-maxLabelNameLen` and `-maxLabelValueLen`. It must be in range `1..65535`. See [#11128](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/11128).
* BUGFIX: [stream aggregation](https://docs.victoriametrics.com/victoriametrics/stream-aggregation/): fix possible unexpected increases in `rate_avg` and `rate_sum` if an out-of-order sample is ingested after the previous flush. See [#11140](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/11140).
* BUGFIX: `vmselect` in [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): propagate cache reset operation to `selectNode` when `/internal/resetRollupResultCache` is called. Previously, the propagation only happened when the `delete_series` API was called. See [#11112](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/11112).
* BUGFIX: [vmctl](https://docs.victoriametrics.com/victoriametrics/vmctl/): properly URL-encode `-vm-extra-label` values when building import requests, so special characters such as `&` don't get split into broken query parameters. See [#11144](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/11144). Thanks to @immanuwell for contribution.
* BUGFIX: all VictoriaMetrics components: cancel in-flight HTTP requests shortly before `-http.maxGracefulShutdownDuration` elapses during graceful shutdown, so they can drain and the shutdown completes cleanly within that window instead of timing out and exiting via `logger.Fatalf` -> `os.Exit`. This prevents skipping the storage flush and losing in-memory data when long-lived requests are in flight (such as VictoriaLogs live tailing). See [#1502](https://github.com/VictoriaMetrics/VictoriaLogs/issues/1502).


## [v1.122.25](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.122.25)

Released at 2026-06-19

**v1.122.x is a line of [LTS releases](https://docs.victoriametrics.com/victoriametrics/lts-releases/). It contains important up-to-date bugfixes for [VictoriaMetrics enterprise](https://docs.victoriametrics.com/victoriametrics/enterprise/).
All these fixes are also included in [the latest community release](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/latest).
The v1.122.x line will be supported for at least 12 months since [v1.122.0](https://docs.victoriametrics.com/victoriametrics/changelog/#v11220) release**

* BUGFIX: [stream aggregation](https://docs.victoriametrics.com/victoriametrics/stream-aggregation/): fix issue with producing aggregated samples with identical timestamps between flushes. See [#10808](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/10808).
* BUGFIX: [vmalert](https://docs.victoriametrics.com/victoriametrics/vmalert/),[vmauth](https://docs.victoriametrics.com/victoriametrics/vmauth/),[vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/) and [vmsingle](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/): fix rare unbounded shutdown delay when config reload takes longer than `-configCheckInterval`. See [#11107](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/11107). Thanks to @PleasingFungus for contribution.
* BUGFIX: `vmselect` in [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): fix corrupted metrics metadata when a response contains multiple rows. See [#11115](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/11115). Thanks for @fxrlv for the contribution.
* BUGFIX: [vmbackup](https://docs.victoriametrics.com/vmbackup/), [vmbackupmanager](https://docs.victoriametrics.com/victoriametrics/vmbackupmanager/): do not fail backup list if directory is absent while using `fs://` destination to align with other protocols. See [6c3c548d](https://github.com/VictoriaMetrics/VictoriaMetrics/commit/6c3c548ddb0385b749e731f52276f130e2a4e4a8)
* BUGFIX: [vmrestore](https://docs.victoriametrics.com/victoriametrics/vmrestore/): disallow restoring parts outside the configured `-storageDataPath` directory. See [710c920d](https://github.com/VictoriaMetrics/VictoriaMetrics/commit/710c920d6083327042a309e449fae4383617d817).
