<!-- Part 15 of 19 of victoriametrics/changelog/CHANGELOG_2025.md (split because the page is big). -->

## [v1.110.0](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.110.0)

Released at 2025-01-24

* SECURITY: upgrade Go builder from Go1.23.4 to Go1.23.5. See the list of issues addressed in [Go1.23.5](https://github.com/golang/go/issues?q=milestone%3AGo1.23.5+label%3ACherryPickApproved).

* FEATURE: [MetricsQL](https://docs.victoriametrics.com/victoriametrics/metricsql/): allow executing queries with `$__interval` and `$__rate_interval` - these placeholders are automatically replaced with `1i` (e.g. `step` arg value at [`/api/v1/query_range`](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#range-query)) during query execution. This simplifies copying queries from Grafana dashboards.
* FEATURE: [MetricsQL](https://docs.victoriametrics.com/victoriametrics/metricsql/): allow specifying metric names in quotes inside `{}` braces: `{"metric_name", job="foo"}` is equal to `metric_name{job="foo"}`. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/7703) for details.
* FEATURE: [vmsingle](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/) and `vmselect` in [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): add command-line flag `-search.maxDeleteDuration(default 5m)` to limit the duration of the `/api/v1/admin/tsdb/delete_series` call. Previously, the call is limited by `-search.maxQueryDuration`.
* FEATURE: [dashboards](https://github.com/VictoriaMetrics/VictoriaMetrics/blob/master/dashboards): all dashboards that use [VictoriaMetrics Grafana datasource](https://github.com/VictoriaMetrics/victoriametrics-datasource) were updated to use a [new datasource ID](https://github.com/VictoriaMetrics/victoriametrics-datasource/releases/tag/v0.12.0).
* FEATURE: [vmui](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#vmui): reflect column settings for the table view in URL, so the table view can be shared via link. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/7662).

* BUGFIX: [vmauth](https://docs.victoriametrics.com/victoriametrics/vmauth/): fix possible runtime panic during requests processing under heavy load. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/8051) for details.
* BUGFIX: [vmselect](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): fix panic when trying to delete series by using [multitenant read](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/#multitenancy-via-labels) endpoint. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/8126) for the details.
* BUGFIX: [vmselect](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): prevent panic when `vmselect` receives an error response from `vmstorage` during the query execution and request processing for other `vmstorage` nodes is still in progress. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/8114) for the details.
* BUGFIX: all VictoriaMetrics [enterprise](https://docs.victoriametrics.com/victoriametrics/enterprise/) components: properly trim whitespaces at the end of license provided via `-license` and `-licenseFile` command-line flags. Previously, the trailing whitespaces could cause the license verification to fail.
* BUGFIX: [Single-node VictoriaMetrics](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/) and [vmselect](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): respect staleness detection in increase, increase_pure and delta functions when time series has gaps and `-search.maxStalenessInterval` is set. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/8072) for details.
* BUGFIX: [vmsingle](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/), `vminsert` in [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/) and [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/): allow ingesting histograms with missing `_sum` metric via [OpenTelemetry ingestion protocol](https://docs.victoriametrics.com/victoriametrics/integrations/opentelemetry/) in the same way as Prometheus does.
* BUGFIX: [vmui](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#vmui): fix an issue where pressing the "Enter" key in the query editor did not execute the query. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/8058).
* BUGFIX: [export API](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#how-to-export-time-series): cancel export process on client connection close. Previously client connection close was ignored and VictoriaMetrics started to hog CPU by exporting metrics to nowhere until it export all of them.


## [v1.109.1](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.109.1)

Released at 2025-01-17

* SECURITY: upgrade base docker image (Alpine) from 3.21.0 to 3.21.2. See [Alpine 3.21.1 release notes](https://alpinelinux.org/posts/Alpine-3.21.1-released.html) and [Alpine 3.21.2 release notes](https://alpinelinux.org/posts/Alpine-3.18.11-3.19.6-3.20.5-3.21.2-released.html).

* BUGFIX: [vmsingle](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/), `vminsert` in [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/) and [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/): log metric names for signals with unsupported delta temporality on ingestion via [OpenTelemetry protocol for metrics](https://docs.victoriametrics.com/victoriametrics/integrations/opentelemetry/). Thanks to @chenlujjj for [the pull request](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/8018).
* BUGFIX: [Single-node VictoriaMetrics](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/) and [vmselect](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): fix incorrect behavior of increase, increase_pure, delta caused by [this pull request](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/8002). This fix reverts to the previous behavior before [v1.109.0](https://docs.victoriametrics.com/victoriametrics/changelog/#v11090). But allows controlling staleness detection for these functions explicitly via `-search.maxStalenessInterval`.
* BUGFIX: all VictoriaMetrics [enterprise](https://docs.victoriametrics.com/victoriametrics/enterprise/) components: remove unnecessary delay before failing if all online verification attempts have failed. This should reduce the time required for the component to proceed if all online verification attempts have failed.
* BUGFIX: [vmselect](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): prevent panic when sending `multitenant` [read request](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/#multitenancy-via-labels) to `/api/v1/series/count`. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/8126) for the details.


## [v1.109.0](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.109.0)

Released at 2025-01-14

**Update note: This release contains [issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/8045) that might affect correctness of increase, increase_pure and delta functions. It affects only vmselect or VictoriaMetrics single-node on query time. Please, rollback vmselects to the closest previous version or update to [v1.109.1](https://docs.victoriametrics.com/victoriametrics/changelog/#v11091).**

* FEATURE: all the VictoriaMetrics components: increase the default value for [`GOGC`](https://tip.golang.org/doc/gc-guide#GOGC) from `30` to `100`. This should reduce CPU usage at the cost of slightly higher memory usage. [Single-node VictoriaMetrics](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/), [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/) and [vmstorage](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/#architecture-overview) components continue using `GOGC=30`, since they are optimized for low memory allocations and low memory usage, so they do not benefit from the increased GOGC value too much. It is possible to override the default `GOGC` value in any VictoriaMetrics component by setting `GOGC` environment variable to the desired value. For example, `GOGC=200 ./path/to/vmagent` starts `vmagent` with `GOGC=200`. See [these docs](https://tip.golang.org/doc/gc-guide#GOGC) about `GOGC` tuning. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/7902).
* FEATURE: [vmui](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#vmui): add export data functionality for the `Raw Query` page and the ability to import exported data into the `Query Analyzer` page. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/7628).
* FEATURE: [vmui](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#vmui): add `markdown` support for comments during data export. See [this pull request](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/7828).
* FEATURE: [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/) and [Single-node VictoriaMetrics](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/): added `min` and `max` metrics for Datadog Sketches API metrics, changed `_` metric name separator to `.` if metrics are not sanitized for consistency.
* FEATURE: [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/) and [Single-node VictoriaMetrics](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/): add service discovery support for Marathon. See [these docs](https://docs.victoriametrics.com/victoriametrics/sd_configs/#marathon_sd_configs) and [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/6642).
* FEATURE: [Single-node VictoriaMetrics](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/): support `-maxIngestionRate` cmd-line flag to ratelimit samples/sec ingested. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/7377) for details.
* FEATURE: [vmsingle](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/) and `vmselect` in [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): improve query performance on systems with high number of CPU cores. See [this PR](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/7416) for details.
* FEATURE: [vmsingle](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/) and `vmselect` in [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): add command-line flag `-search.maxBinaryOpPushdownLabelValues` to allow using labels with more candidate values as push down filter in binary operation. See [this pull request](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/7243). Thanks to @tydhot for implementation.
* FEATURE: [vmsingle](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/) and `vmstorage` in [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): add command-line flag `storage.finalDedupScheduleCheckInterval` to control the final deduplication process interval. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/7880) for details.
* FEATURE: [Single-node VictoriaMetrics](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/) and `vmstorage` in [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): add a separate cache type for storing sparse entries when performing large index scans. This significantly reduces memory usage when applying [downsampling filters](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#downsampling) and [retention filters](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#retention-filters) during background merge. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/7182) for the details.

* BUGFIX: [dashboards](https://github.com/VictoriaMetrics/VictoriaMetrics/blob/master/dashboards): consistently use `vmagent_remotewrite_pending_data_bytes` on vmagent dashboard to represent persistent queue size.
* BUGFIX: [vmalert](https://docs.victoriametrics.com/victoriametrics/vmalert/): fix the auto-generated metrics `ALERTS` and `ALERTS_FOR_STATE` for alerting rules. Previously, metrics might have incorrect labels and affect the restore process. See this [issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/7796).
* BUGFIX: [vmalert](https://docs.victoriametrics.com/victorialogs/vmalert/): do not append tenant info to VictoriaLogs datasource request path in [clusterMode](https://docs.victoriametrics.com/victoriametrics/vmalert/#multitenancy). See [this doc](https://docs.victoriametrics.com/victorialogs/vmalert/#how-to-use-multitenancy-in-rules) for how to use multitenancy in VictoriaLogs.
* BUGFIX: [vmauth](https://docs.victoriametrics.com/victoriametrics/vmauth/): properly set `host` field at debug information formatted with `dump_request_on_errors: true` setting.
* BUGFIX: [vmauth](https://docs.victoriametrics.com/victoriametrics/vmauth/): properly handle discovery for ipv6 addresses. Thanks to @badie for the [pull request](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/7955).
* BUGFIX: [vmctl](https://docs.victoriametrics.com/victoriametrics/vmctl/): fix support for migrating influx series without any tag. See [this pull request](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/7935). Thanks to @bitbidu for reporting.
* BUGFIX: `vminsert` in [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): storage nodes defined in `-storageNode` are now sorted, ensuring that varying node orders across different vminsert instances do not result in inconsistent replication.
* BUGFIX: [vmsingle](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/) and `vminsert` in [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): properly ingest `influx` line protocol metrics with empty tags. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/7933) for details.
* BUGFIX: [vmselect](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): allow to override the default unique time series limit in vmstorage with command-line flags like `-search.maxUniqueTimeseries`, `-search.maxLabelsAPISeries`. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/7852).
* BUGFIX: [vmselect](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): properly set tenancy information when evaluating numbers in a query. Previously, the tenancy information could lead to mismatch between query result and a number. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/7987) for the details.
* BUGFIX: [vmalert](https://docs.victoriametrics.com/victoriametrics/vmalert/): fix marshaling of request body for Alertmanager notification. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/7985) for the details.
* BUGFIX: [Single-node VictoriaMetrics](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/) and [vmselect](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): don't take into account the last raw sample before the lookbehind window is sample exceeds the staleness interval. This affects correctness of increase, increase_pure, delta functions when performing calculations on time series with gaps. See [this pull request](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/8002) for details.


## [v1.108.1](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.108.1)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2024/#v11081)


## [v1.108.0](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.108.0)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2024/#v11080)


## [v1.107.0](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.107.0)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2024/#v11070)


## [v1.106.1](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.106.1)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2024/#v11061)


## [v1.106.0](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.106.0)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2024/#v11060)


## [v1.105.0](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.105.0)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2024/#v11050)


## [v1.104.0](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.104.0)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2024/#v11040)


## [v1.103.0](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.103.0)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2024/#v11030)


## [v1.102.25](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.102.25)

Released at 2025-07-04

**v1.102.x is a line of [LTS releases](https://docs.victoriametrics.com/victoriametrics/lts-releases/). It contains important up-to-date bugfixes for [VictoriaMetrics enterprise](https://docs.victoriametrics.com/victoriametrics/enterprise/).
All these fixes are also included in [the latest community release](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/latest).
The v1.102.x line will be supported for at least 12 months since [v1.102.0](https://docs.victoriametrics.com/changelog/#v11020) release**

* BUGFIX: [vmbackup](https://docs.victoriametrics.com/victoriametrics/vmbackup/), [vmbackupmanager](https://docs.victoriametrics.com/victoriametrics/vmbackupmanager/): automatically retry requests failing with `Expired Token` errors. This helps to avoid failed backups when using [EKS Pod Identity](https://docs.aws.amazon.com/eks/latest/userguide/pod-id-how-it-works.html) for authentication. See [#9280](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/9280).
* BUGFIX: [vmalert](https://docs.victoriametrics.com/victoriametrics/vmalert/): fix alerts state restoration for alerting rules that are using [templating](https://docs.victoriametrics.com/victoriametrics/vmalert/#templating) in the labels. See [#9305](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/9305).
* BUGFIX: [vmsingle](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/) and `vmstorage` in [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): properly return results for search requests with `.+|^$` regex filter expression. See [9290](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/9290) issue for details.
