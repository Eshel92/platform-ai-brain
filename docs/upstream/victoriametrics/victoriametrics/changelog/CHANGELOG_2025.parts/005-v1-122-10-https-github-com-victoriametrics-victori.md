<!-- Part 5 of 19 of victoriametrics/changelog/CHANGELOG_2025.md (split because the page is big). -->

## [v1.122.10](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.122.10)

Released at 2025-11-28

**v1.122.x is a line of [LTS releases](https://docs.victoriametrics.com/victoriametrics/lts-releases/). It contains important up-to-date bugfixes for [VictoriaMetrics enterprise](https://docs.victoriametrics.com/victoriametrics/enterprise/).
All these fixes are also included in [the latest community release](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/latest).
The v1.122.x line will be supported for at least 12 months since [v1.122.0](https://docs.victoriametrics.com/victoriametrics/changelog/#v11220) release**

* FEATURE: [vmui](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#vmui): add option to always show all points on the chart.
* FEATURE: [vmui](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#vmui): improve overall chart rendering performance. See [#9699](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/9699).

* BUGFIX: [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/) and [vmsingle](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/): prevent early exit when one of multiple service discovery configs (under the same service discovery type) fails. see this issue [#9949](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/9949) for details.
* BUGFIX: [vmalert](https://docs.victoriametrics.com/victoriametrics/vmalert/): don't increase `vmalert_alerts_send_errors_total` for request context cancellation, which may occur during graceful shutdown or group configuration update. See [#10027](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/10027).
* BUGFIX: [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/), [vmsingle](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/) and `vminsert` in [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): Prevent `accept()` from blocking when a client connects to `-opentsdbListenAddr` but sends no data or sends it too slowly. Previously, such connections could stall acceptance of new clients. See [#9987](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/9987) for details.
* BUGFIX: `vmselect` in [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): respect `replicationFactor` and `globalReplicationFactor` settings when some of vmstorage nodes are overloaded. See [#10030](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/10030) for details. Thanks to @tIGO for the contribution.
* BUGFIX: [vmui](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#vmui): fix display of isolated points on the chart. See [#9666](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/9666).
* BUGFIX: [vmui](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#vmui): remove the “step” control from the Raw Query page, since it didn't affect the chart rendering. See [#9667](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/9667).
* BUGFIX: [vmui](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#vmui): fix display of multiple points at the same timestamp on the Raw Query page. See [#9666](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/9666).
* BUGFIX: [vmui](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#vmui): fix ability to select multiple metrics in `Explore Metrics` tab. See [#9995](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/9995).
* BUGFIX: Account for excess white spaces in influx write string. See [#10049](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/10049).


## [v1.122.9](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.122.9)

Released at 2025-11-14

**v1.122.x is a line of [LTS releases](https://docs.victoriametrics.com/victoriametrics/lts-releases/). It contains important up-to-date bugfixes for [VictoriaMetrics enterprise](https://docs.victoriametrics.com/victoriametrics/enterprise/).
All these fixes are also included in [the latest community release](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/latest).
The v1.122.x line will be supported for at least 12 months since [v1.122.0](https://docs.victoriametrics.com/victoriametrics/changelog/#v11220) release**

**Update Note 1:** VictoriaMetrics [enterprise](https://docs.victoriametrics.com/enterprise/) [vmsingle](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/) and `vmstorage` in [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): Make sure that, if `-retentionFilter` is used, its duration is lower than `-retentionPeriod` before upgrading; otherwise, the deployment will fail. Read more in [retention filters](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#retention-filters) documentation.

* SECURITY: upgrade Go builder from Go1.24.9 to Go1.24.10. See [the list of issues addressed in Go1.24.10](https://github.com/golang/go/issues?q=milestone%3AGo1.24.10%20label%3ACherryPickApproved).
* SECURITY: upgrade golang.org/x/crypto to v0.43.0 to address CVE-2025-47913.

* BUGFIX: [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/) and [vmsingle](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/): properly access service discovery servers with HTTP/2 protocol enabled. See this issue [#9981](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/9981) for details. Thanks to the @JayiceZ
* BUGFIX: [vmalert](https://docs.victoriametrics.com/victoriametrics/vmalert/): drop labels with empty values in generated alerts and time series. See [#9984](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/9984).
* BUGFIX: `vminsert`, [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/) and [vmsingle](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/): properly apply `maxDataSize` memory limits to the `zstd` encoded requests. It protects ingest endpoints from malicious requests.
* BUGFIX: [vmui](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#vmui): fix median value calculation displayed below series graph. See [#9926](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/9926).
* BUGFIX: VictoriaMetrics [enterprise](https://docs.victoriametrics.com/enterprise/) [vmsingle](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/) and `vmstorage` in [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): disallow having a duration in `-retentionFilter` bigger than `-retentionPeriod`. Previously, it was allowed but had no effect, the data retention period remains limited to `-retentionPeriod`.


## [v1.122.8](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.122.8)

Released at 2025-11-04

**v1.122.x is a line of [LTS releases](https://docs.victoriametrics.com/victoriametrics/lts-releases/). It contains important up-to-date bugfixes for [VictoriaMetrics enterprise](https://docs.victoriametrics.com/victoriametrics/enterprise/).
All these fixes are also included in [the latest community release](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/latest).
The v1.122.x line will be supported for at least 12 months since [v1.122.0](https://docs.victoriametrics.com/victoriametrics/changelog/#v11220) release**


* BUGFIX: `vminsert`, [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/) and [vmsingle](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/): properly apply `maxDataSize` memory limits to the `snappy` encoded requests. It protects ingest endpoints from malicious requests.


## [v1.122.7](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.122.7)

Released at 2025-10-31

**v1.122.x is a line of [LTS releases](https://docs.victoriametrics.com/victoriametrics/lts-releases/). It contains important up-to-date bugfixes for [VictoriaMetrics enterprise](https://docs.victoriametrics.com/victoriametrics/enterprise/).
All these fixes are also included in [the latest community release](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/latest).
The v1.122.x line will be supported for at least 12 months since [v1.122.0](https://docs.victoriametrics.com/victoriametrics/changelog/#v11220) release**

* BUGFIX: [vmbackup](https://docs.victoriametrics.com/victoriametrics/vmbackup/), [vmrestore](https://docs.victoriametrics.com/victoriametrics/vmrestore/), [vmbackupmanager](https://docs.victoriametrics.com/victoriametrics/vmbackupmanager/): complete a fix of environment variables configuration parsing for connection to AWS S3. Previously, such settings were ignored starting from [v1.115.0](https://docs.victoriametrics.com/victoriametrics/changelog/#v11150) and releases [v1.128.0](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.128.0), [v1.122.6](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.122.6) and [v1.110.21](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.110.21) did not fix an issue completely. See this issue [#9858](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/9858) for details.
* BUGFIX: [vmalert](https://docs.victoriametrics.com/victoriametrics/vmalert/): fix search over group names and other attributes in vmalert's WEB UI. See [#9886](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/9886) for details.
* BUGFIX: [vmalert](https://docs.victoriametrics.com/victoriametrics/vmalert/): preserve HTML formatting in rule's annotations in vmalert's [WEB UI](https://docs.victoriametrics.com/vmalert.html#web). See [#9892](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/9892) for details.
* BUGFIX [vmbackupmanager](https://docs.victoriametrics.com/victoriametrics/vmbackupmanager/): consistently set `vm_backup_last_created_at{type="latest"}` to the latest backup start time.
* BUGFIX: [vmbackupmanager](https://docs.victoriametrics.com/victoriametrics/vmbackupmanager/): prevent breaking shell formatting when using `vmbackupmanager` CLI mode by adding a newline after the command output. Previously, using CLI mode would not always include newline at the end of output, which could break shell formatting.


## [v1.122.6](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.122.6)

Released at 2025-10-17

**v1.122.x is a line of [LTS releases](https://docs.victoriametrics.com/victoriametrics/lts-releases/). It contains important up-to-date bugfixes for [VictoriaMetrics enterprise](https://docs.victoriametrics.com/victoriametrics/enterprise/).
All these fixes are also included in [the latest community release](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/latest).
The v1.122.x line will be supported for at least 12 months since [v1.122.0](https://docs.victoriametrics.com/victoriametrics/changelog/#v11220) release**

* SECURITY: upgrade base docker image (Alpine) from 3.22.1 to 3.22.2. See [Alpine 3.22.2 release notes](https://www.alpinelinux.org/posts/Alpine-3.19.9-3.20.8-3.21.5-3.22.2-released.html).
* SECURITY: upgrade Go builder from Go1.24.7 to Go1.24.9. See [the list of issues addressed in Go1.24.9](https://github.com/golang/go/issues?q=milestone%3AGo1.24.9%20label%3ACherryPickApproved).

* BUGFIX: [vmbackup](https://docs.victoriametrics.com/victoriametrics/vmbackup/), [vmrestore](https://docs.victoriametrics.com/victoriametrics/vmrestore/), [vmbackupmanager](https://docs.victoriametrics.com/victoriametrics/vmbackupmanager/): properly apply additional configuration of connection provided via environment variables (such as `AWS_CA_BUNDLE`). Previously, such settings were ignored starting from [v1.115.0](https://docs.victoriametrics.com/victoriametrics/changelog/#v11150). See this issue [#9858](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/9858) for details.
* BUGFIX: [stream aggregation](https://docs.victoriametrics.com/victoriametrics/stream-aggregation/): remove impact of `flush_on_shutdown` on timestamps of flushed samples. See [#9642](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/9642).


## [v1.122.5](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.122.5)

Released at 2025-10-03

**v1.122.x is a line of [LTS releases](https://docs.victoriametrics.com/victoriametrics/lts-releases/). It contains important up-to-date bugfixes for [VictoriaMetrics enterprise](https://docs.victoriametrics.com/victoriametrics/enterprise/).
All these fixes are also included in [the latest community release](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/latest).
The v1.122.x line will be supported for at least 12 months since [v1.122.0](https://docs.victoriametrics.com/victoriametrics/changelog/#v11220) release**

* SECURITY: upgrade Go builder from Go1.24.6 to Go1.24.7. See [the list of issues addressed in Go1.24.7](https://github.com/golang/go/issues?q=milestone%3AGo1.24.7+label%3ACherryPickApproved).

* BUGFIX: [vmsingle](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/) and `vmstorage` in [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): prevent unexpected performance degradation caused by cache misses (exposed via `vm_cache_misses_total` metric) during rotation. See this PR [#9769](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/9769) for details.
* BUGFIX: all components: restore sorting order of summary and quantile metrics exposed by VictoriaMetrics components on `/metrics` page. See [metrics#105](https://github.com/VictoriaMetrics/metrics/pull/105) for details.
* BUGFIX: [vmsingle](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/) and `vmselect` in [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): avoid applying offset modifier twice to the request time when an instant query uses rollup functions `rate()` or `avg_over_time()` with cache enabled. See [#9762](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/9762).
* BUGFIX: [vmalert](https://docs.victoriametrics.com/victoriametrics/vmalert/): restore support for `query` templates in alert rule labels after the regression introduced in [#9543](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/9543). See [#9783](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/9783) for details.


## [v1.122.4](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.122.4)

Released at 2025-09-12

**v1.122.x is a line of [LTS releases](https://docs.victoriametrics.com/victoriametrics/lts-releases/). It contains important up-to-date bugfixes for [VictoriaMetrics enterprise](https://docs.victoriametrics.com/victoriametrics/enterprise/).
All these fixes are also included in [the latest community release](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/latest).
The v1.122.x line will be supported for at least 12 months since [v1.122.0](https://docs.victoriametrics.com/victoriametrics/changelog/#v11220) release**

**Known issues: [vmalert](https://docs.victoriametrics.com/victoriametrics/vmalert/): `query` [template function](https://docs.victoriametrics.com/vmalert.html#template-functions) was accidentally disallowed from using in rule `labels` field. The previous behavior will be restored in upcoming releases.**

* BUGFIX: [vmui](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#vmui): properly apply rollup functions to metrics based on their name in vmui's [metrics explorer](https://docs.victoriametrics.com/victoriametrics/#metrics-explorer). See [#9655](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/9655) for details. Thanks to @wbwren-eric for the fix.
* BUGFIX: all VictoriaMetrics [enterprise](https://docs.victoriametrics.com/enterprise/) components: fix support for automatic issuing of TLS certificates for HTTPS server via [Let's Encrypt service](https://letsencrypt.org/) using [TLS-ALPN-01 challenge](https://letsencrypt.org/docs/challenge-types/#tls-alpn-01). See [Automatic issuing of TLS certificates](https://docs.victoriametrics.com/victoriametrics/#automatic-issuing-of-tls-certificates) for more info.
* BUGFIX: [vmui](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#vmui): fix VMUI backend URL, while using multitenant API. See more in [#9703](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/9703).
* BUGFIX: all components: properly expose metadata for summaries and histograms in VictoriaMetrics components with enabled `-metrics.exposeMetadata` cmd-line flag. See [metrics#98](https://github.com/VictoriaMetrics/metrics/issues/98) for details.
* BUGFIX: all components: lower severity of the log message for unavailable [Pressure Stall Information (PSI)](https://docs.kernel.org/accounting/psi.html) metrics from `ERROR` to `INFO` level. See [#9161](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/9161) for details.
* BUGFIX: [vmbackupmanager](https://docs.victoriametrics.com/victoriametrics/vmbackupmanager/): properly prepare restore mark contents when using a backup shortname (e.g. `vmbackupmanager restore create daily/2025-09-12`). Previously, restore would fail with `failed to restore backup: cannot initialize remote fs: missing scheme in path` error.


## [v1.122.3](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.122.3)

Released at 2025-08-29

**v1.122.x is a line of [LTS releases](https://docs.victoriametrics.com/victoriametrics/lts-releases/). It contains important up-to-date bugfixes for [VictoriaMetrics enterprise](https://docs.victoriametrics.com/victoriametrics/enterprise/).
All these fixes are also included in [the latest community release](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/latest).
The v1.122.x line will be supported for at least 12 months since [v1.122.0](https://docs.victoriametrics.com/changelog/#v11220) release**

**Known issues: [vmalert](https://docs.victoriametrics.com/victoriametrics/vmalert/): `query` [template function](https://docs.victoriametrics.com/vmalert.html#template-functions) was accidentally disallowed from using in rule `labels` field. The previous behavior will be restored in upcoming releases.**

* BUGFIX: [MetricsQL](https://docs.victoriametrics.com/victoriametrics/metricsql/): fix `timestamp` function compatibility with Prometheus when used with sub-expressions such as `timestamp(sum(foo))`. The fix applies only when `-search.disableImplicitConversion` flag is set. See more in [#9527-comment](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/9527#issuecomment-3200646020) and [metricsql#55](https://github.com/VictoriaMetrics/metricsql/pull/55).
* BUGFIX: [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/): prevent remote write ingestion stop on push error for [Google Pub/Sub](https://docs.victoriametrics.com/victoriametrics/integrations/pubsub/#writing-metrics) integration.
* BUGFIX: [vmauth](https://docs.victoriametrics.com/victoriametrics/vmauth/): properly handle [mTLS authorization and routing](https://docs.victoriametrics.com/victoriametrics/vmauth/#mtls-based-request-routing). Previously it didn't work. See [#29](https://github.com/VictoriaMetrics/VictoriaLogs/issues/29).
* BUGFIX: all VictoriaMetrics [enterprise](https://docs.victoriametrics.com/victoriametrics/enterprise/) components: fix support for automatic issuing of TLS certificates for HTTPS server at `-httpListenAddr` via [Let's Encrypt service](https://letsencrypt.org/). See [these docs](https://docs.victoriametrics.com/victoriametrics/#automatic-issuing-of-tls-certificates).
