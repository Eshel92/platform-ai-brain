<!-- Part 16 of 19 of victoriametrics/changelog/CHANGELOG_2025.md (split because the page is big). -->

## [v1.102.24](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.102.24)

Released at 2025-06-20

**v1.102.x is a line of [LTS releases](https://docs.victoriametrics.com/victoriametrics/lts-releases/). It contains important up-to-date bugfixes for [VictoriaMetrics enterprise](https://docs.victoriametrics.com/victoriametrics/enterprise/).
All these fixes are also included in [the latest community release](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/latest).
The v1.102.x line will be supported for at least 12 months since [v1.102.0](https://docs.victoriametrics.com/changelog/#v11020) release**

* SECURITY: upgrade base docker image (Alpine) from 3.21.3 to 3.22.0. See [Alpine 3.22.0 release notes](https://alpinelinux.org/posts/Alpine-3.22.0-released.html).
* SECURITY: upgrade Go builder from Go1.23.9 to Go1.23.10. See [the list of issues addressed in Go1.23.10](https://github.com/golang/go/issues?q=milestone%3AGo1.23.10+label%3ACherryPickApproved).

* BUGFIX: [vmsingle](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/) and `vmstorage` in [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): fix incorrect sorting of tag filters, which led to suboptimal tag filter evaluation order and potentially degraded query performance in rare cases. See [#9127](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/9127) for details.
* BUGFIX: [vmselect](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/) in [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): expose `/-/healthy` and `/-/ready` endpoints as Prometheus does on vmselect endpoints, thus achieving full Prometheus compatibility for external dependencies.
* BUGFIX: [vmbackup](https://docs.victoriametrics.com/victoriametrics/vmbackup/), [vmbackupmanager](https://docs.victoriametrics.com/victoriametrics/vmbackupmanager/): fix server-side copying of objects for Azure Blob Storage when using managed identity for authentication. Previously, it wasn't possible to use [smart backups](https://docs.victoriametrics.com/victoriametrics/vmbackup/#smart-backups) strategy for `vmbackup` as server-side copy would fail. See [#9131](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/9131).
* BUGFIX: [vmbackupmanager](https://docs.victoriametrics.com/victoriametrics/vmbackupmanager/): increase startup healthcheck delay for storage reachability from 30 seconds to 3 minutes. This is required to avoid vmbackupmanager restarts when storage node startup take more than 30 seconds (e.g. when storage nodes stores more than 5Tb of data).


## [v1.102.23](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.102.23)

Released at 2025-06-06

**v1.102.x is a line of [LTS releases](https://docs.victoriametrics.com/victoriametrics/lts-releases/). It contains important up-to-date bugfixes for [VictoriaMetrics enterprise](https://docs.victoriametrics.com/victoriametrics/enterprise/).
All these fixes are also included in [the latest community release](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/latest).
The v1.102.x line will be supported for at least 12 months since [v1.102.0](https://docs.victoriametrics.com/changelog/#v11020) release**

* BUGFIX: [vmgateway](https://docs.victoriametrics.com/victoriametrics/vmgateway/): add missing vmselect `vmui` related routes to the authorized requests routing. See [9003](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/9003) issue for details.
* BUGFIX: [vmsingle](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/) and `vmselect` in [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): prevent panic caused by invalid label name in metric relabeling debugging interface. Error is now properly propagated and displayed in the interface. See [#8661](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/8661).
* BUGFIX: [vmctl](https://docs.victoriametrics.com/victoriametrics/vmctl/): enable dual-stack network mode for `vmctl`connections by default. This allows connecting to IPv6 endpoints as it was not possible previously. See [#9116](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/9116).
* BUGFIX: [vmbackup](https://docs.victoriametrics.com/victoriametrics/vmbackup/), [vmrestore](https://docs.victoriametrics.com/victoriametrics/vmrestore/), [vmbackupmanager](https://docs.victoriametrics.com/victoriametrics/vmbackupmanager/): use exponential backoff for retries when uploading or downloading data from S3. This should reduce the number of failed uploads and downloads when S3 is temporarily unavailable. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/8639).
* BUGFIX: [vmbackup](https://docs.victoriametrics.com/victoriametrics/vmbackup/), [vmrestore](https://docs.victoriametrics.com/victoriametrics/vmrestore/), [vmbackupmanager](https://docs.victoriametrics.com/victoriametrics/vmbackupmanager/): improve resilience to network issues by retrying requests failing due to `IncompleteBody`. Previously, such requests were not retried and leaded to restore/backup process failure. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/8639) and [this PR](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/8547) for details.


## [v1.102.22](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.102.22)

Released at 2025-05-23

**v1.102.x is a line of [LTS releases](https://docs.victoriametrics.com/victoriametrics/lts-releases/). It contains important up-to-date bugfixes for [VictoriaMetrics enterprise](https://docs.victoriametrics.com/victoriametrics/enterprise/).
All these fixes are also included in [the latest community release](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/latest).
The v1.102.x line will be supported for at least 12 months since [v1.102.0](https://docs.victoriametrics.com/changelog/#v11020) release**

* BUGFIX: [vmsingle](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/) and [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/): fix inconsistency with Prometheus in labels discovered by using [Kubernetes service-discovery](https://docs.victoriametrics.com/victoriametrics/sd_configs/#kubernetes_sd_configs) with `role: endpointslice`. See [#8959](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/8959).


## [v1.102.21](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.102.21)

Released at 2025-05-15

**v1.102.x is a line of [LTS releases](https://docs.victoriametrics.com/victoriametrics/lts-releases/). It contains important up-to-date bugfixes for [VictoriaMetrics Enterprise](https://docs.victoriametrics.com/victoriametrics/enterprise/).
All these fixes are also included in [the latest community release](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/latest).
The v1.102.x line will be supported for at least 12 months since [v1.102.0](https://docs.victoriametrics.com/changelog/#v11020) release**

* BUGFIX: [vmsingle](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/), `vminsert` in [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/) and [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/): fixed duplication in Datadog sketches aggregation metrics. See [#8836](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/8836) for details.
* BUGFIX: [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/): properly initialize relabel config reloading metrics for `-remoteWrite.relabelConfig` and `-remoteWrite.urlRelabelConfig` flags. The bug was introduced in versions [v1.117.0](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.117.0), [v1.110.7](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.110.7), [v1.102.20](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.102.20). The fix was released in [v1.117.1](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.117.1) and backported to [v1.110.8](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.110.8) and [v1.102.21](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.102.21).
* BUGFIX: [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/): properly reload authorization configuration on headers changes. See [This issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/8931) for details. Thanks to @smallpath for the [PR](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/8938).


## [v1.102.20](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.102.20)

Released at 2025-05-09

**Known issues: `vmagent` in this release is affected by [#8941](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/8941). The `-remoteWrite.relabelConfig` and `-remoteWrite.urlRelabelConfig` flags are not applied properly, causing the relabeling logic to be skipped.
Update to [v1.102.21](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.102.21) or rollback to [v1.102.19](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.102.19) instead.**

**v1.102.x is a line of [LTS releases](https://docs.victoriametrics.com/victoriametrics/lts-releases/). It contains important up-to-date bugfixes for [VictoriaMetrics Enterprise](https://docs.victoriametrics.com/victoriametrics/enterprise/).
All these fixes are also included in [the latest community release](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/latest).
The v1.102.x line will be supported for at least 12 months since [v1.102.0](https://docs.victoriametrics.com/changelog/#v11020) release**

* SECURITY: upgrade Go builder from Go1.23.8 to Go1.23.9. See the list of issues addressed in [Go1.23.9](https://github.com/golang/go/issues?q=milestone%3AGo1.23.9+label%3ACherryPickApproved)

* BUGFIX: [vmalert-tool](https://docs.victoriametrics.com/victoriametrics/vmalert-tool/): fix parsing for (+/-)Inf values and scientific notation in `values` field. Thanks to @evkuzin for [#8847](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/8847).
* BUGFIX: [vmsingle](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/) and [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/): create relabel config reload and stream aggregation config reload related metrics only if config is present. See [helm-charts#2119](https://github.com/VictoriaMetrics/helm-charts/issues/2119) for details.


## [v1.102.19](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.102.19)

Released at 2025-04-25

**v1.102.x is a line of [LTS releases](https://docs.victoriametrics.com/victoriametrics/lts-releases/). It contains important up-to-date bugfixes for [VictoriaMetrics Enterprise](https://docs.victoriametrics.com/victoriametrics/enterprise/).
All these fixes are also included in [the latest community release](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/latest).
The v1.102.x line will be supported for at least 12 months since [v1.102.0](https://docs.victoriametrics.com/victoriametrics/changelog/#v11020) release**

* BUGFIX: all the VictoriaMetrics components: properly detect `cgroupv2` [CPU limits](https://www.kernel.org/doc/html/latest/admin-guide/cgroup-v2.html#cpu). See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/8808) for details.
* BUGFIX: [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/): properly init [enterprise](https://docs.victoriametrics.com/victoriametrics/enterprise/) version for `linux/arm` and non-CGO builds. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/6019) for details.
* BUGFIX: [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/): remote write client sets correct content encoding header based on actual body content, rather than relying on configuration. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/8650).
* BUGFIX: [vmbackup](https://docs.victoriametrics.com/victoriametrics/vmbackup/) and [vmbackupmanager](https://docs.victoriametrics.com/victoriametrics/vmbackupmanager/): properly configure s3 client with if `configFilePath` is set. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/8668) for details.
* BUGFIX: [vmsingle](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/), `vmstorage` and `vmselect` in [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): allow using `-downsampling.period=filter:0s:0s` to skip downsampling for time series that match the specified `filter`. See [this doc](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#downsampling).
* BUGFIX: [vmalert](https://docs.victoriametrics.com/victoriametrics/vmalert/): properly set the rule group id in `/rules` and `/alerts` APIs. Previously, the group id was not set, preventing rules from being toggled by group in the vmalert UI. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/8773).


## [v1.102.18](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.102.18)

Released at 2025-04-04

**v1.102.x is a line of [LTS releases](https://docs.victoriametrics.com/victoriametrics/lts-releases/). It contains important up-to-date bugfixes for [VictoriaMetrics Enterprise](https://docs.victoriametrics.com/victoriametrics/enterprise/).
All these fixes are also included in [the latest community release](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/latest).
The v1.102.x line will be supported for at least 12 months since [v1.102.0](https://docs.victoriametrics.com/victoriametrics/changelog/#v11020) release**

* SECURITY: upgrade Go builder from Go1.23.6 to Go1.23.8. See the list of issues addressed in [Go1.23.8](https://github.com/golang/go/issues?q=milestone%3AGo1.23.8+label%3ACherryPickApproved).

* BUGFIX: [vmgateway](https://docs.victoriametrics.com/victoriametrics/vmgateway/): properly set the `Host` header when routing requests to `-write.url` and `-read.url`, which is needed for reverse proxies like Traefik.
* BUGFIX: [vmauth](https://docs.victoriametrics.com/victoriametrics/vmauth/): return `502 Bad Gateway` status code in case request failed due to a network timeout. Previously, vmauth would incorrectly return `200 OK`. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/8621).


## [v1.102.17](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.102.17)

Released at 2025-03-21

**v1.102.x is a line of [LTS releases](https://docs.victoriametrics.com/victoriametrics/lts-releases/). It contains important up-to-date bugfixes for [VictoriaMetrics Enterprise](https://docs.victoriametrics.com/victoriametrics/enterprise/).
All these fixes are also included in [the latest community release](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/latest).
The v1.102.x line will be supported for at least 12 months since [v1.102.0](https://docs.victoriametrics.com/victoriametrics/changelog/#v11020) release**

* SECURITY: upgrade golang.org/x/net from v0.33.0 to v0.36.0 to address [CVE-2025-22870](https://github.com/advisories/GHSA-qxp5-gwg8-xv66).

* BUGFIX: [vmbackupmanager](https://docs.victoriametrics.com/victoriametrics/vmbackupmanager/): do not set `vm_backup_last_run_failed` metric to `1` when running vmbackupmanager with an empty storage. Previously, the metrics was set to `1` even though backup was not created yet. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/8490).
* BUGFIX: [vmalert](https://docs.victoriametrics.com/victoriametrics/vmalert/), [vmctl](https://docs.victoriametrics.com/victoriametrics/vmctl/), [vmbackup](https://docs.victoriametrics.com/victoriametrics/vmbackup/), [vmrestore](https://docs.victoriametrics.com/victoriametrics/vmrestore/), [vmbackupmanager](https://docs.victoriametrics.com/victoriametrics/vmbackupmanager/): properly apply TLS settings for URLs with scheme other than `https`. Previously, TLS settings were ignored for such URLs. That could lead to unexpected behavior when a request was receiving a redirect response to a URL with `https` scheme. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/8494) for details.
* BUGFIX: [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/): prevent dropping persistent queue data when changes happened for `-remoteWrite.showURL` flag, query params or fragment in remote write URL. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/8477).
* BUGFIX: [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/): properly send staleness markers if scrape error occurs. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/8528) for details.
* BUGFIX: [vmalert](https://docs.victoriametrics.com/victoriametrics/vmalert/): fix memory leak when sending alerts with `-notifier.blackhole` enabled. Bug was introduced in [v1.112.0](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.112.0).
* BUGFIX: [vmalert](https://docs.victoriametrics.com/victoriametrics/vmalert/): properly compare rules `group.checksum` and statically define `group.id` at creation time. See [this PR](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/8540) for details.
* BUGFIX: [vmalert](https://docs.victoriametrics.com/victoriametrics/vmalert/): fix memory leak during rule group updates on reload. Bug was introduced in [v1.112.0](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.112.0). See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/8532).
* BUGFIX: [vmgateway](https://docs.victoriametrics.com/victoriametrics/vmgateway/): fix the `vmgateway_ratelimit_refresh_duration_seconds` value, before it did not account for the actual time spent refreshing limits.
