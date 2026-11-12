<!-- Part 14 of 19 of victoriametrics/changelog/CHANGELOG_2024.md (split because the page is big). -->

## [v1.97.12](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.97.12)

Released at 2024-11-15

**v1.97.x is a line of [LTS releases](https://docs.victoriametrics.com/victoriametrics/lts-releases/). It contains important up-to-date bugfixes for [VictoriaMetrics Enterprise](https://docs.victoriametrics.com/victoriametrics/enterprise/).
All these fixes are also included in [the latest community release](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/latest).
The v1.97.x line will be supported for at least 12 months since [v1.97.0](https://docs.victoriametrics.com/victoriametrics/changelog/#v1970) release**

* BUGFIX: [vmctl](https://docs.victoriametrics.com/victoriametrics/vmctl/): drop rows that do not belong to the current series during import. The dropped rows should belong to another series whose tags are a superset of the current series. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/7301) and [this pull request](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/7330). Thanks to @dpedu for reporting and cooperating with the test.
* BUGFIX: [vmsingle](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/), `vmselect` in [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): keep the order of resulting time series when `limit_offset` is applied. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/7068).
* BUGFIX: [graphite](https://docs.victoriametrics.com/victoriametrics/integrations/graphite/#render-api): properly handle xFilesFactor=0 for `transformRemoveEmptySeries` function. See [this PR](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/7337) for details.
* BUGFIX: [vmauth](https://docs.victoriametrics.com/victoriametrics/vmauth/): properly check availability of all the backends before giving up when proxying requests. Previously, vmauth could return an error even if there were healthy backends available. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/3061) for details.
* BUGFIX: [vmauth](https://docs.victoriametrics.com/victoriametrics/vmauth/): fixed unauthorized routing behavior inconsistency. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/7543) for details.


## [v1.97.11](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.97.11)

Released at 2024-11-04

**v1.97.x is a line of [LTS releases](https://docs.victoriametrics.com/victoriametrics/lts-releases/). It contains important up-to-date bugfixes for [VictoriaMetrics Enterprise](https://docs.victoriametrics.com/victoriametrics/enterprise/).
All these fixes are also included in [the latest community release](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/latest).
The v1.97.x line will be supported for at least 12 months since [v1.97.0](https://docs.victoriametrics.com/victoriametrics/changelog/#v1970) release**

* BUGFIX: [vmalert](https://docs.victoriametrics.com/victoriametrics/vmalert/): properly set `group_name` and `file` fields for recording rules in `/api/v1/rules`.
* BUGFIX: [Single-node VictoriaMetrics](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/) and `vmstorage` in [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): prevent panic when ingesting samples which are outside of configured [retention filters](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#retention-filters). This could happen when backfilling data with retention filters which exclude samples from the backfill range.


## [v1.97.10](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.97.10)

Released at 2024-10-21

**v1.97.x is a line of [LTS releases](https://docs.victoriametrics.com/victoriametrics/lts-releases/). It contains important up-to-date bugfixes for [VictoriaMetrics Enterprise](https://docs.victoriametrics.com/victoriametrics/enterprise/).
All these fixes are also included in [the latest community release](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/latest).
The v1.97.x line will be supported for at least 12 months since [v1.97.0](https://docs.victoriametrics.com/victoriametrics/changelog/#v1970) release**

* BUGFIX: [vmui](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#vmui): fix error messages rendering from overflowing the screen with long messages. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/7207).
* BUGFIX: [vmctl](https://docs.victoriametrics.com/victoriametrics/vmctl/): properly add metrics tags for `opentsdb` migration source. Previously it could have empty values. See [this PR](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/7161).
* BUGFIX: [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): properly apply replication factor when storage node groups are used and replication factor is configured via global value such as `-replicationFactor=2`. Previously, global replication factor was ignored for storage node groups. See [these docs](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/#vmstorage-groups-at-vmselect) for more information about storage groups configuration.
* BUGFIX: [vmalert](https://docs.victoriametrics.com/victoriametrics/vmalert/): properly apply configuration changes during hot-reload to rule groups that haven't started yet. Previously, configuration updates to such groups could have resulted into blocking all evaluations within the group, until vmalert restart.


## [v1.97.9](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.97.9)

Released at 2024-10-02

**v1.97.x is a line of [LTS releases](https://docs.victoriametrics.com/victoriametrics/lts-releases/). It contains important up-to-date bugfixes for [VictoriaMetrics Enterprise](https://docs.victoriametrics.com/victoriametrics/enterprise/).
All these fixes are also included in [the latest community release](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/latest).
The v1.97.x line will be supported for at least 12 months since [v1.97.0](https://docs.victoriametrics.com/victoriametrics/changelog/#v1970) release**

* BUGFIX: [MetricsQL](https://docs.victoriametrics.com/victoriametrics/metricsql/): consistently return the first non-`NaN` value from [`range_first`](https://docs.victoriametrics.com/victoriametrics/metricsql/#range_first) function across all the returned data points. Previously `NaN` data points weren't replaced with the first non-`NaN` value.


## [v1.97.8](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.97.8)

Released at 2024-09-23

* SECURITY: upgrade Go builder from Go1.22.5 to Go1.23.1. See the list of issues addressed in [Go1.23.1](https://github.com/golang/go/issues?q=milestone%3AGo1.23.1+label%3ACherryPickApproved).
* SECURITY: upgrade base docker image (Alpine) from 3.20.2 to 3.20.3. See [alpine 3.20.3 release notes](https://alpinelinux.org/posts/Alpine-3.17.10-3.18.9-3.19.4-3.20.3-released.html).

* BUGFIX: [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/) fix service discovery of Azure Virtual Machines for response contains `nextLink` in `Host:Port` format. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/6912).
* BUGFIX: [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/): properly consume messages [from kafka](https://docs.victoriametrics.com/victoriametrics/integrations/kafka/). Previously vmagent could skip some messages during start-up.
* BUGFIX: [vmgateway](https://docs.victoriametrics.com/victoriametrics/vmgateway/): add missing `datadog`, `newrelic`, `opentelemetry` and `pushgateway` routes to the `JWT` authorization routes. Allows prefixed (`prometheus/graphite`) routes for query requests.
* BUGFIX: [Single-node VictoriaMetrics](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/) and `vmstorage` in [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): properly cache empty list of matching time series for the given [labels filter](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#filtering). This type of caching was broken since [v1.97.0](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.97.0), which could result in the increased CPU usage when performing queries, which match zero time series. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/7009).
* BUGFIX: [Single-node VictoriaMetrics](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/) and `vmstorage` in [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): Fixes start-up crash on Windows OS. See this [issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/6973) for details.
* BUGFIX: [Single-node VictoriaMetrics](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/) and `vmstorage` in [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): fix metric `vm_object_references{type="indexdb"}`. Previously, it was overcounted.
* BUGFIX: [Single-node VictoriaMetrics](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/) and `vmstorage` in [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): properly ingest stale NaN samples. Previously it could be dropped if series didn't exist at storage node. See this issue [https://github.com/VictoriaMetrics/VictoriaMetrics/issues/5069] for details.
* BUGFIX: [Single-node VictoriaMetrics](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/) and `vmstorage` in [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): properly track `vm_missing_tsids_for_metric_id_total` metric. See this [issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/6931) for details.
* BUGFIX: [vmalert](https://docs.victoriametrics.com/victoriametrics/vmalert/): do not send notifications without labels to Alertmanager. Such notifications are rejected by Alertmanager anyway. Before, vmalert could send alert notifications even if no label-value pairs left after applying `alert_relabel_configs` from [notifier config](https://docs.victoriametrics.com/victoriametrics/vmalert/#notifier-configuration-file).
* BUGFIX: [vmalert](https://docs.victoriametrics.com/victoriametrics/vmalert/): properly update value of variable `$activeAt` in rules annotation during replay mode. Before, `$activeAt` could have provided incorrect values during replay.
* BUGFIX: [MetricsQL](https://docs.victoriametrics.com/victoriametrics/metricsql/): properly handle `c1 AND c2` and `c1 OR c1` queries for constants `c1` and `c2`. Previously such queries could return unexpected results. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/6637).
* BUGFIX: all VictoriaMetrics components: increase default value of `-loggerMaxArgLen` cmd-line flag from 1000 to 5000. This should improve visibility on errors produced by very long queries.


## [v1.97.7](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.97.7)

Released at 2024-08-28

**v1.97.x is a line of [LTS releases](https://docs.victoriametrics.com/victoriametrics/lts-releases/). It contains important up-to-date bugfixes for [VictoriaMetrics Enterprise](https://docs.victoriametrics.com/victoriametrics/enterprise/).
All these fixes are also included in [the latest community release](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/latest).
The v1.97.x line will be supported for at least 12 months since [v1.97.0](https://docs.victoriametrics.com/victoriametrics/changelog/#v1970) release**

* BUGFIX: [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/): fixes `proxy_url` authorization for scrape targets. Previously proxy authorization configuration was ignored for `https` targets. See [this](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/6771) issue for details.
* BUGFIX: [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/) fix service discovery of Azure Virtual Machines for response contains `nextLink`. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/6784).
* BUGFIX: [vmalert](https://docs.victoriametrics.com/victoriametrics/vmalert/): respect HTTP headers defined in [notifier configuration file](https://docs.victoriametrics.com/victoriametrics/vmalert/#notifier-configuration-file) for each request to notifiers. Previously, this param was ignored by mistake.
* BUGFIX: [graphite](https://docs.victoriametrics.com/victoriametrics/integrations/graphite/#render-api): respect `-search.denyPartialResponse` cmd-line flag and `deny_partial_response` query GET param when serving requests via Graphite API. Before, partial responses were always denied. Thanks to @penguinlav for the [pull request](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/6748).
* BUGFIX: [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/): account for `-usePromCompatibleNaming` cmd-line flag during when pushing data to remote storages. Thanks to @12345XXX  for the [pull request](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/6776).
* BUGFIX: [MetricsQL](https://docs.victoriametrics.com/victoriametrics/metricsql/): fix calculation [histogram_quantile](https://docs.victoriametrics.com/victoriametrics/metricsql/#histogram_quantile) over Prometheus buckets with inconsistent values. It was producing incorrect results in case lower buckets. The issue was introduced in [v1.102.0](https://docs.victoriametrics.com/victoriametrics/changelog/#v11020) release, see [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/6714) for the details.
* BUGFIX: [vmalert](https://docs.victoriametrics.com/victoriametrics/vmalert/), [vmctl](https://docs.victoriametrics.com/victoriametrics/vmctl/) and snapshot API: verify correctness of URLs provided via cmd-line flags before executing HTTP requests. See [this](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/6740) issue for details.
* BUGFIX: all VictoriaMetrics components: forcefully set owner/group for release tars to 1000:1000. This helps to avoid unpacking [issues](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/6788) on systems with limitations around UID:GID configuration. See [this pull request](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/6846).
* BUGFIX: [Single-node VictoriaMetrics](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/) and `vmstorage` in [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): properly register index metrics for previous index part. See this [issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/6868) for details.
* BUGFIX: [Single-node VictoriaMetrics](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/) and `vmstorage` in [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): fix metric names registering in the per-day index for new dates for existing time series when making calls to `/tags/tagSeries` and `/tags/tagMultiSeries` handlers of [Graphite API](https://docs.victoriametrics.com/victoriametrics/integrations/graphite/#graphite-api-usage). See [this](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/6872/) for details.
