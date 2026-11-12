<!-- Part 13 of 19 of victoriametrics/changelog/CHANGELOG_2025.md (split because the page is big). -->

## [v1.110.15](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.110.15)

Released at 2025-08-01

**v1.110.x is a line of [LTS releases](https://docs.victoriametrics.com/victoriametrics/lts-releases/). It contains important up-to-date bugfixes for [VictoriaMetrics enterprise](https://docs.victoriametrics.com/victoriametrics/enterprise/).
All these fixes are also included in [the latest community release](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/latest).
The v1.110.x line will be supported for at least 12 months since [v1.110.0](https://docs.victoriametrics.com/changelog/#v11100) release**

* BUGFIX: [vmui](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#vmui): always display the tenant selector if the list of tenants is not empty. See [#9396](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/9396).


## [v1.110.14](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.110.14)

Released at 2025-07-18

**v1.110.x is a line of [LTS releases](https://docs.victoriametrics.com/victoriametrics/lts-releases/). It contains important up-to-date bugfixes for [VictoriaMetrics enterprise](https://docs.victoriametrics.com/victoriametrics/enterprise/).
All these fixes are also included in [the latest community release](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/latest).
The v1.110.x line will be supported for at least 12 months since [v1.110.0](https://docs.victoriametrics.com/changelog/#v11100) release**

* SECURITY: upgrade Go builder from Go1.24.4 to Go1.24.5. See [the list of issues addressed in Go1.24.5](https://github.com/golang/go/issues?q=milestone%3AGo1.24.5+label%3ACherryPickApproved).
* SECURITY: upgrade base docker image (Alpine) from 3.22.0 to 3.22.1. See [Alpine 3.22.1 release notes](https://www.alpinelinux.org/posts/Alpine-3.19.8-3.20.7-3.21.4-3.22.1-released.html).

* BUGFIX: all VictoriaMetrics components: fix `process_cpu_cores_available` metric to respect both logical CPU cores and cgroup CPU quota. Previously, it could report incorrect values in containerized environments with no cgroup limits. See [#9449](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/9449).


## [v1.110.13](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.110.13)

Released at 2025-07-04

**v1.110.x is a line of [LTS releases](https://docs.victoriametrics.com/victoriametrics/lts-releases/). It contains important up-to-date bugfixes for [VictoriaMetrics enterprise](https://docs.victoriametrics.com/victoriametrics/enterprise/).
All these fixes are also included in [the latest community release](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/latest).
The v1.110.x line will be supported for at least 12 months since [v1.110.0](https://docs.victoriametrics.com/changelog/#v11100) release**

* BUGFIX: [vmbackup](https://docs.victoriametrics.com/victoriametrics/vmbackup/), [vmbackupmanager](https://docs.victoriametrics.com/victoriametrics/vmbackupmanager/): automatically retry requests failing with `Expired Token` errors. This helps to avoid failed backups when using [EKS Pod Identity](https://docs.aws.amazon.com/eks/latest/userguide/pod-id-how-it-works.html) for authentication. See [#9280](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/9280).
* BUGFIX: [vmui](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#vmui): fix errors in console about loading of `manifest.json` when accessing UI through vmauth with Basic Auth enabled.
* BUGFIX: [vmalert](https://docs.victoriametrics.com/victoriametrics/vmalert/): fix alerts state restoration for alerting rules that are using [templating](https://docs.victoriametrics.com/victoriametrics/vmalert/#templating) in the labels. See [#9305](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/9305).
* BUGFIX: [vmsingle](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/) and `vmstorage` in [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): properly return results for search requests with `.+|^$` regex filter expression. See [9290](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/9290) issue for details.


## [v1.110.12](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.110.12)

Released at 2025-06-20

**v1.110.x is a line of [LTS releases](https://docs.victoriametrics.com/victoriametrics/lts-releases/). It contains important up-to-date bugfixes for [VictoriaMetrics enterprise](https://docs.victoriametrics.com/victoriametrics/enterprise/).
All these fixes are also included in [the latest community release](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/latest).
The v1.110.x line will be supported for at least 12 months since [v1.110.0](https://docs.victoriametrics.com/changelog/#v11100) release**

* SECURITY: upgrade Go builder from Go1.24.3 to Go1.24.4. See [the list of issues addressed in Go1.24.4](https://github.com/golang/go/issues?q=milestone%3AGo1.24.4+label%3ACherryPickApproved).
* SECURITY: upgrade base docker image (Alpine) from 3.21.3 to 3.22.0. See [Alpine 3.22.0 release notes](https://alpinelinux.org/posts/Alpine-3.22.0-released.html).

* BUGFIX: [vmsingle](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/), `vminsert` in [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/) and [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/): fixed duplication in Datadog sketches aggregation metrics. See [#8836](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/8836) for details.
* BUGFIX: [vmsingle](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/) and `vmstorage` in [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): fix incorrect sorting of tag filters, which led to suboptimal tag filter evaluation order and potentially degraded query performance in rare cases. See [#9127](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/9127) for details.
* BUGFIX: [vmselect](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/) in [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): expose `/-/healthy` and `/-/ready` endpoints as Prometheus does on vmselect endpoints, thus achieving full Prometheus compatibility for external dependencies.
* BUGFIX: [vmbackup](https://docs.victoriametrics.com/victoriametrics/vmbackup/), [vmbackupmanager](https://docs.victoriametrics.com/victoriametrics/vmbackupmanager/): fix server-side copying of objects for Azure Blob Storage when using managed identity for authentication. Previously, it wasn't possible to use [smart backups](https://docs.victoriametrics.com/victoriametrics/vmbackup/#smart-backups) strategy for `vmbackup` as server-side copy would fail. See [#9131](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/9131).
* BUGFIX: [vmbackupmanager](https://docs.victoriametrics.com/victoriametrics/vmbackupmanager/): increase startup healthcheck delay for storage reachability from 30 seconds to 3 minutes. This is required to avoid vmbackupmanager restarts when storage node startup take more than 30 seconds (e.g. when storage nodes stores more than 5Tb of data).


## [v1.110.11](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.110.11)

Released at 2025-06-09

**v1.110.x is a line of [LTS releases](https://docs.victoriametrics.com/victoriametrics/lts-releases/). It contains important up-to-date bugfixes for [VictoriaMetrics enterprise](https://docs.victoriametrics.com/victoriametrics/enterprise/).
All these fixes are also included in [the latest community release](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/latest).
The v1.110.x line will be supported for at least 12 months since [v1.110.0](https://docs.victoriametrics.com/changelog/#v11100) release**

* BUGFIX: `vmselect` in [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): remove tenant labels `vm_account_id` and `vm_project_id` from [exported data](https://docs.victoriametrics.com/victoriametrics/#how-to-export-time-series) if tenant info was [specified in URL](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/#url-format). These labels will be present only if export is done via [/multitenant/ endpoint](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/#multitenancy-via-labels), as such response could contain series belonging to different tenants. This change also fixes inconsistency in vmctl's [cluster-to-cluster migration mode](https://docs.victoriametrics.com/victoriametrics/vmctl/victoriametrics/#cluster-to-cluster)  - see [#9016](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/9016) for details. Thank @fxrlv for the bug report.


## [v1.110.10](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.110.10)

Released at 2025-06-06

**v1.110.x is a line of [LTS releases](https://docs.victoriametrics.com/victoriametrics/lts-releases/). It contains important up-to-date bugfixes for [VictoriaMetrics enterprise](https://docs.victoriametrics.com/victoriametrics/enterprise/).
All these fixes are also included in [the latest community release](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/latest).
The v1.110.x line will be supported for at least 12 months since [v1.110.0](https://docs.victoriametrics.com/changelog/#v11100) release**

* BUGFIX: [vmgateway](https://docs.victoriametrics.com/victoriametrics/vmgateway/): add missing vmselect `vmui` related routes to the authorized requests routing. See [9003](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/9003) issue for details.
* BUGFIX: [vmsingle](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/) and `vmstorage` in [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): fixed a regression in downsampling logic introduced in [#7440](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/7440) and released in [v1.106.0](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.106.0), where downsampling rules with filters `filter:offset:interval` could be incorrectly skipped in favor of unfiltered rules `offset:interval`. See [#8969](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/8969).
* BUGFIX: [vmsingle](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/) and `vmstorage` in [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): properly apply `rententionFilter` on flag value changes. Previously, it ignored any `filter` value changes for historical data. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/8885) for details.
* BUGFIX: [vmsingle](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/) and `vmstorage` in [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): schedule a single background merge thread for merging historical data. See [4592](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/4592) issue for details.
* BUGFIX: [vmsingle](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/) and `vmselect` in [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): prevent panic caused by invalid label name in metric relabeling debugging interface. Error is now properly propagated and displayed in the interface. See [#8661](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/8661).
* BUGFIX: [vmctl](https://docs.victoriametrics.com/victoriametrics/vmctl/): enable dual-stack network mode for `vmctl`connections by default. This allows connecting to IPv6 endpoints as it was not possible previously. See [#9116](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/9116).
* BUGFIX: [vmbackup](https://docs.victoriametrics.com/victoriametrics/vmbackup/), [vmrestore](https://docs.victoriametrics.com/victoriametrics/vmrestore/), [vmbackupmanager](https://docs.victoriametrics.com/victoriametrics/vmbackupmanager/): improve resilience to network issues by retrying requests failing due to `IncompleteBody`. Previously, such requests were not retried and leaded to restore/backup process failure. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/8639) and [this PR](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/8547) for details.
* BUGFIX: [vmselect](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/) in [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): include full list of query filters to build a cache key for [multitenant read](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/#multitenancy-via-labels) queries. Previously, cache key did not include tenancy related labels so cache entries could be shared between tenants breaking tenant isolation. See [#9002](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/9002) for details.


## [v1.110.9](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.110.9)

Released at 2025-05-23

**v1.110.x is a line of [LTS releases](https://docs.victoriametrics.com/victoriametrics/lts-releases/). It contains important up-to-date bugfixes for [VictoriaMetrics enterprise](https://docs.victoriametrics.com/victoriametrics/enterprise/).
All these fixes are also included in [the latest community release](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/latest).
The v1.110.x line will be supported for at least 12 months since [v1.110.0](https://docs.victoriametrics.com/changelog/#v11100) release**

* BUGFIX: [vmalert](https://docs.victoriametrics.com/victoriametrics/vmalert/): drop duplicate labels when they appear in both the recording rule label spec and the expression result. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/8954) for details.
* BUGFIX: [vmsingle](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/) and [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/): fix inconsistency with Prometheus in labels discovered by using [Kubernetes service-discovery](https://docs.victoriametrics.com/victoriametrics/sd_configs/#kubernetes_sd_configs) with `role: endpointslice`. See [#8959](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/8959).


## [v1.110.8](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.110.8)

Released at 2025-05-15

**v1.110.x is a line of [LTS releases](https://docs.victoriametrics.com/victoriametrics/lts-releases/). It contains important up-to-date bugfixes for [VictoriaMetrics Enterprise](https://docs.victoriametrics.com/victoriametrics/enterprise/).
All these fixes are also included in [the latest community release](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/latest).
The v1.110.x line will be supported for at least 12 months since [v1.110.0](https://docs.victoriametrics.com/changelog/#v11100) release**

* BUGFIX: [vmsingle](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/), `vminsert` in [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/) and [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/): fixed duplication in Datadog sketches aggregation metrics. See [#8836](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/8836) for details.
* BUGFIX: [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/): properly initialize relabel config reloading metrics for `-remoteWrite.relabelConfig` and `-remoteWrite.urlRelabelConfig` flags. The bug was introduced in versions [v1.117.0](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.117.0), [v1.110.7](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.110.7), [v1.102.20](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.102.20). The fix was released in [v1.117.1](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.117.1) and backported to [v1.110.8](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.110.8) and [v1.102.21](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.102.21).
* BUGFIX: [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/): properly reload authorization configuration on headers changes. See [This issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/8931) for details. Thanks to @smallpath for the [PR](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/8938).


## [v1.110.7](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.110.7)

Released at 2025-05-09

**Known issues: `vmagent` in this release is affected by [#8941](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/8941). The `-remoteWrite.relabelConfig` and `-remoteWrite.urlRelabelConfig` flags are not applied properly, causing the relabeling logic to be skipped.
Update to [v1.110.8](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.110.8) or rollback to [v1.110.6](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.110.6) instead.**

**v1.110.x is a line of [LTS releases](https://docs.victoriametrics.com/victoriametrics/lts-releases/). It contains important up-to-date bugfixes for [VictoriaMetrics Enterprise](https://docs.victoriametrics.com/victoriametrics/enterprise/).
All these fixes are also included in [the latest community release](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/latest).
The v1.110.x line will be supported for at least 12 months since [v1.110.0](https://docs.victoriametrics.com/changelog/#v11100) release**

* BUGFIX: [MetricsQL](https://docs.victoriametrics.com/victoriametrics/metricsql/): properly parse quoted utf-8 label names in parentheses. See [#8826](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/8826) for details.
* BUGFIX: [MetricsQL](https://docs.victoriametrics.com/victoriametrics/metricsql/): properly parse metric name series selectors with `or` expressions. See [metricsql#50](https://github.com/VictoriaMetrics/metricsql/issues/50) for details.
* BUGFIX: [vmalert-tool](https://docs.victoriametrics.com/victoriametrics/vmalert-tool/): fix parsing for (+/-)Inf values and scientific notation in `values` field. Thanks to @evkuzin for [#8847](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/8847).
* BUGFIX: [vmsingle](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/) and [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/): create relabel config reload and stream aggregation config reload related metrics only if config is present. See [helm-charts#2119](https://github.com/VictoriaMetrics/helm-charts/issues/2119) for details.
