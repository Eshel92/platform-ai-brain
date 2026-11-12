<!-- Part 17 of 27 of victoriametrics/changelog/CHANGELOG.md (split because the page is big). -->

## [v1.136.14](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.136.14)

Released at 2026-07-17

**v1.136.x is a line of [LTS releases](https://docs.victoriametrics.com/victoriametrics/lts-releases/). It contains important up-to-date bugfixes for [VictoriaMetrics enterprise](https://docs.victoriametrics.com/victoriametrics/enterprise/).
All these fixes are also included in [the latest community release](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/latest).
The v1.136.x line will be supported for at least 12 months since [v1.136.0](https://docs.victoriametrics.com/victoriametrics/changelog/#v11360) release**

* SECURITY: upgrade Go builder from Go1.26.4 to Go1.26.5. See [the list of issues addressed in Go1.26.5](https://github.com/golang/go/issues?q=milestone%3AGo1.26.5%20label%3ACherryPickApproved).

* BUGFIX: [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/): flush pending persistent queue data to chunk file before updating the metadata. This prevents the metadata writer offset from getting ahead of the chunk file size and avoids losing the persistent queue after an unclean shutdown. See [#11192](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/11192).
* BUGFIX: [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/): fix a possible data race when processing OpenTelemetry metadata. See [#11238](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/11238). Thanks to @nevgeny for contribution.
* BUGFIX: [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/): atomically write persistent queue metainfo to prevent possible file corruption on ungraceful shutdown. See [#11192](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/11192).
* BUGFIX: [vmbackup](https://docs.victoriametrics.com/victoriametrics/vmbackup/) and [vmbackupmanager](https://docs.victoriametrics.com/victoriametrics/vmbackupmanager/): retry S3 requests failing with `HTTP 429` status code or `TooManyRequests` error code. Previously such requests were not retried, so a short burst of rate limiting would fail the whole backup. See [#11218](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/11218). Thanks to @gautamrizwani for contribution.
* BUGFIX: `vmselect` in [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): properly apply limit to metrics metadata response. See [#11139](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/11139).
* BUGFIX: `vminsert` in [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): Now drops metadata blocks when communicating with vmstorage nodes over the legacy RPC protocol. To avoid this limitation, upgrade `vmstorage` to a version that supports the new RPC protocol (>= [v1.137.0](https://github.com/VictoriaMetrics/VictoriaMetrics/blob/master/docs/victoriametrics/changelog/CHANGELOG.md#v11370)). See [#11146](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/11146).
* BUGFIX: [vmui](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#vmui): keep only one header navigation dropdown (`Explore`, `Tools`) open at a time. Previously, hovering across two dropdowns could briefly leave both open due to the close delay. See [#11224](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/11224). Thanks to @antedotee for contribution.
* BUGFIX: [vmui](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#vmui): preserve newline formatting in alert and rule annotations on the Alerting page. See [#11171](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/11171).
* BUGFIX: [vmui](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#vmui): hide `Total metric names` stats on [Cardinality Explorer](https://docs.victoriametrics.com/victoriametrics/#cardinality-explorer) page when user selects a specific metric or label to focus. See [#11154](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/11154) for details. Thanks to @lghuy05 for the contribution.
* BUGFIX: [vmauth](https://docs.victoriametrics.com/victoriametrics/vmauth/): return `408 Request Timeout` instead of `400 Bad Request` when the request body isn't received within `-maxQueueDuration`. This prevents `vmagent` from incorrectly downgrading the remote write protocol and dropping data when `vmauth` is used as a proxy for a remote write endpoint. See [#11272](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/11272).


## [v1.136.13](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.136.13)

Released at 2026-07-03

**v1.136.x is a line of [LTS releases](https://docs.victoriametrics.com/victoriametrics/lts-releases/). It contains important up-to-date bugfixes for [VictoriaMetrics enterprise](https://docs.victoriametrics.com/victoriametrics/enterprise/).
All these fixes are also included in [the latest community release](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/latest).
The v1.136.x line will be supported for at least 12 months since [v1.136.0](https://docs.victoriametrics.com/victoriametrics/changelog/#v11360) release**

* SECURITY: upgrade base docker image (Alpine) from 3.23.4 to 3.24.1. See [Alpine 3.24.1 release notes](https://www.alpinelinux.org/posts/Alpine-3.24.1-released.html).

* BUGFIX: `vminsert` in [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/) and [vmsingle](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/): properly check values range for the limits configured with flags `-maxLabelsPerTimeseries`, `-maxLabelNameLen` and `-maxLabelValueLen`. It must be in range `1..65535`. See [#11128](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/11128).
* BUGFIX: `vminsert` in [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): fixes unexpected rare rerouting. See [#11162](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/11162).
* BUGFIX: `vmselect` in [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): propagate cache reset operation to `selectNode` when `/internal/resetRollupResultCache` is called. Previously, the propagation only happened when the `delete_series` API was called. See [#11112](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/11112).
* BUGFIX: [stream aggregation](https://docs.victoriametrics.com/victoriametrics/stream-aggregation/): fix possible unexpected increases in `rate_avg` and `rate_sum` if an out-of-order sample is ingested after the previous flush. See [#11140](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/11140).
* BUGFIX: [vmctl](https://docs.victoriametrics.com/victoriametrics/vmctl/): properly URL-encode `-vm-extra-label` values when building import requests, so special characters such as `&` don't get split into broken query parameters. See [#11144](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/11144). Thanks to @immanuwell for contribution.
* BUGFIX: [enterprise](https://docs.victoriametrics.com/enterprise/) [vmagent](https://docs.victoriametrics.com/vmagent/): ignore `enable.auto.offset.store` option in `kafka.consumer.topic.options`, since `vmagent` manages offset storage internally. Previously, setting this option could cause `vmagent` to stop committing Kafka messages. See [#11208](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/11208).
* BUGFIX: all VictoriaMetrics components: cancel in-flight HTTP requests shortly before `-http.maxGracefulShutdownDuration` elapses during graceful shutdown, so they can drain and the shutdown completes cleanly within that window instead of timing out and exiting via `logger.Fatalf` -> `os.Exit`. This prevents skipping the storage flush and losing in-memory data when long-lived requests are in flight (such as VictoriaLogs live tailing). See [#1502](https://github.com/VictoriaMetrics/VictoriaLogs/issues/1502).


## [v1.136.12](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.136.12)

Released at 2026-06-19

**v1.136.x is a line of [LTS releases](https://docs.victoriametrics.com/victoriametrics/lts-releases/). It contains important up-to-date bugfixes for [VictoriaMetrics enterprise](https://docs.victoriametrics.com/victoriametrics/enterprise/).
All these fixes are also included in [the latest community release](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/latest).
The v1.136.x line will be supported for at least 12 months since [v1.136.0](https://docs.victoriametrics.com/victoriametrics/changelog/#v11360) release**

* BUGFIX: [stream aggregation](https://docs.victoriametrics.com/victoriametrics/stream-aggregation/): fix issue with producing aggregated samples with identical timestamps between flushes. See [#10808](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/10808).
* BUGFIX: [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/): fix potential corruption of remote-write metadata `Unit` values. See [#11120](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/11120). Thanks for @fxrlv for the contribution.
* BUGFIX: [vmalert](https://docs.victoriametrics.com/victoriametrics/vmalert/),[vmauth](https://docs.victoriametrics.com/victoriametrics/vmauth/),[vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/) and [vmsingle](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/): fix rare unbounded shutdown delay when config reload takes longer than `-configCheckInterval`. See [#11107](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/11107). Thanks to @PleasingFungus for contribution.
* BUGFIX: [vmbackup](https://docs.victoriametrics.com/vmbackup/), [vmbackupmanager](https://docs.victoriametrics.com/victoriametrics/vmbackupmanager/): do not fail backup list if directory is absent while using `fs://` destination to align with other protocols. See [6c3c548d](https://github.com/VictoriaMetrics/VictoriaMetrics/commit/6c3c548ddb0385b749e731f52276f130e2a4e4a8)
* BUGFIX: [vmctl](https://docs.victoriametrics.com/victoriametrics/vmctl/): push metrics to configured `-pushmetrics.url` on shutdown when migration fails. Previously, metrics were not pushed if vmctl exited with an error. See [#11081](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/11081). Thanks to @zasdaym for contribution.
* BUGFIX: [vmrestore](https://docs.victoriametrics.com/victoriametrics/vmrestore/): disallow restoring parts outside the configured `-storageDataPath` directory. See [710c920d](https://github.com/VictoriaMetrics/VictoriaMetrics/commit/710c920d6083327042a309e449fae4383617d817).
* BUGFIX: `vmselect` in [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): fix corrupted metrics metadata when a response contains multiple rows. See [#11115](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/11115). Thanks for @fxrlv for the contribution.
* BUGFIX: [vmsingle](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/) and `vmselect` in [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): properly escape `metricFamilyName` at metrics metadata response. See [#11129](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/11129). Thanks for @fxrlv for the contribution.
* BUGFIX: `vmselect` in [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): correctly apply long tenant filters. Previously, such filters could be truncated, causing tenants to be matched incorrectly. See [#11096](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/11096). Thanks for @fxrlv for the contribution.
* BUGFIX: [vmsingle](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/) and `vmstorage` in [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): prevent more cases of panic during directory deletion on `NFS`-based mounts. See [#11060](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/11060).


## [v1.136.11](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.136.11)

Released at 2026-06-05

**v1.136.x is a line of [LTS releases](https://docs.victoriametrics.com/victoriametrics/lts-releases/). It contains important up-to-date bugfixes for [VictoriaMetrics enterprise](https://docs.victoriametrics.com/victoriametrics/enterprise/).
All these fixes are also included in [the latest community release](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/latest).
The v1.136.x line will be supported for at least 12 months since [v1.136.0](https://docs.victoriametrics.com/victoriametrics/changelog/#v11360) release**

* SECURITY: upgrade Go builder from Go1.26.3 to Go1.26.4. See [the list of issues addressed in Go1.26.4](https://github.com/golang/go/issues?q=milestone%3AGo1.26.4%20label%3ACherryPickApproved).

* BUGFIX: [MetricsQL](https://docs.victoriametrics.com/victoriametrics/metricsql/): `integrate()` no longer extrapolates the last sample's value past the end of the time series. Previously, querying `integrate(metric[1h])` at a timestamp where the series had already ended would keep accruing area as if the last value continued indefinitely, producing values much larger than the true integral. See [#9474](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/9474). Thanks to @wtfashwin for contribution.
* BUGFIX: [vmui](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#vmui): persist the `Disable deduplication` toggle under its own local storage key. Before this fix, the toggle state was lost after reload and could overwrite the `Compact view` table setting. See [#11004](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/11004). Thanks to @immanuwell for the contribution.
* BUGFIX: [vmalert](https://docs.victoriametrics.com/victoriametrics/vmalert/): fix the `Notifiers` page in web UI appearing blank despite the API returning notifier data correctly. See [#11035](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/11035).
* BUGFIX: [vmalert](https://docs.victoriametrics.com/victoriametrics/vmalert/): reset the group evaluation timestamp if it exceeds the current host time. Previously, vmalert could use future timestamps for evaluations if the system clock was shifted backward. See [#10985](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/10985).
* BUGFIX: `vmselect` in [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): avoid returning HTTP 503 for queries with partial results when a storage group is unavailable and `-search.denyPartialResponse` is disabled. See [#11009](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/11009). Thanks to @fxrlv for the contribution.
* BUGFIX: [vmsingle](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/) and `vmselect` in [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): properly escape `utf-8` label names for [/federate](https://docs.victoriametrics.com/victoriametrics/#federation) API requests. See [#10968](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/10968).
* BUGFIX: `vmselect` in [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): fix intermittent `write: connection timed out` errors caused by silently dropped TCP connections being reused from the connection pool. See [#10735](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/10735#issuecomment-4535832301).
