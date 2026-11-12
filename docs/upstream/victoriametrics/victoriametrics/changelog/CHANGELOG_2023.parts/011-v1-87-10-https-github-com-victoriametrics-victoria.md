<!-- Part 11 of 14 of victoriametrics/changelog/CHANGELOG_2023.md (split because the page is big). -->

## [v1.87.10](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.87.10)

Released at 2023-10-16

**v1.87.x is a line of [LTS releases](https://docs.victoriametrics.com/victoriametrics/lts-releases/). It contains important up-to-date bugfixes.
The v1.87.x line will be supported for at least 12 months since [v1.87.0](https://docs.victoriametrics.com/victoriametrics/changelog/#v1870) release**

* SECURITY: upgrade Go builder from Go1.21.1 to Go1.21.3. See [the list of issues addressed in Go1.21.2](https://github.com/golang/go/issues?q=milestone%3AGo1.21.2+label%3ACherryPickApproved) and [the list of issues addressed in Go1.21.3](https://github.com/golang/go/issues?q=milestone%3AGo1.21.3+label%3ACherryPickApproved).

* BUGFIX: [storage](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/): prevent from livelock when [forced merge](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#forced-merge) is called under high data ingestion. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/4987).
* BUGFIX: [Graphite Render API](https://docs.victoriametrics.com/victoriametrics/integrations/graphite/#render-api): correctly return `null` instead of `Inf` in JSON query responses. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/3783).
* BUGFIX: [vminsert](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): fix ingestion via [multitenant url](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/#multitenancy-via-labels) for opentsdbhttp. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/5061). The bug has been introduced in [v1.87.8](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.87.8).
* BUGFIX: [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/): fix support of legacy DataDog agent, which adds trailing slashes to urls. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/5078). Thanks to @maxb for spotting the issue.


## [v1.87.9](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.87.9)

Released at 2023-09-10

**v1.87.x is a line of [LTS releases](https://docs.victoriametrics.com/victoriametrics/lts-releases/). It contains important up-to-date bugfixes.
The v1.87.x line will be supported for at least 12 months since [v1.87.0](https://docs.victoriametrics.com/victoriametrics/changelog/#v1870) release**

* SECURITY: upgrade Go builder from Go1.21.0 to Go1.21.1. See [the list of issues addressed in Go1.20.6](https://github.com/golang/go/issues?q=milestone%3AGo1.21.1+label%3ACherryPickApproved).

* BUGFIX: [vminsert enterprise](https://docs.victoriametrics.com/victoriametrics/enterprise/): properly parse `/insert/multitenant/*` urls, which have been broken since [v1.93.2](#v1932). See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/4947).
* BUGFIX: properly build production armv5 binaries for `GOARCH=arm`. This has been broken after the upgrading of Go builder to Go1.21.0. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/4965).
* BUGFIX: [vmselect](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): return `503 Service Unavailable` status code when [partial responses](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/#cluster-availability) are denied and some of `vmstorage` nodes are temporarily unavailable. Previously `422 Unprocessable Entity` status code was mistakenly returned in this case, which could prevent from automatic recovery by re-sending the request to healthy cluster replica in another availability zone.
* BUGFIX: [vmalert](https://docs.victoriametrics.com/victoriametrics/vmalert/): fix the bug when Group's `params` fields with multiple values were overriding each other instead of adding up. The bug was introduced in [this commit](https://github.com/VictoriaMetrics/VictoriaMetrics/commit/eccecdf177115297fa1dc4d42d38e23de9a9f2cb) starting from [v1.87.7](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.87.7). See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/4908).


## [v1.87.8](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.87.8)

Released at 2023-09-01

**v1.87.x is a line of [LTS releases](https://docs.victoriametrics.com/victoriametrics/lts-releases/). It contains important up-to-date bugfixes.
The v1.87.x line will be supported for at least 12 months since [v1.87.0](https://docs.victoriametrics.com/victoriametrics/changelog/#v1870) release**

* BUGFIX: [build](https://docs.victoriametrics.com/victoriametrics/): fix Docker builds for old Docker releases. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/4907).
* BUGFIX: vmselect: correctly handle requests with `/select/multitenant` prefix. Such requests must be rejected since vmselect does not support multitenancy endpoint. Previously, such requests were causing panic. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/4910).
* BUGFIX: [vminsert](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): properly check for [read-only state](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/#readonly-mode) at `vmstorage`. Previously it wasn't properly checked, which could lead to increased resource usage and data ingestion slowdown when some of `vmstorage` nodes are in read-only mode. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/4870).
* BUGFIX: [vminsert](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): properly close broken vmstorage connection during [read-only state](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/#readonly-mode) checks at `vmstorage`. Previously it wasn't properly closed, which prevents restoring `vmstorage` node from read-only mode. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/4870).
* BUGFIX: [vmstorage](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/):  prevent from breaking `vmselect` -> `vmstorage` RPC communication when `vmstorage` returns an empty label name at `/api/v1/labels` request. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/4932).
* BUGFIX: do not allow starting VictoriaMetrics components with improperly set boolean command-line flags in the form `-boolFlagName value`, since this leads to silent incomplete flags' parsing. This form should be replaced with `-boolFlagName=value`. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/4845).
* BUGFIX: properly replace `:` chars in label names with `_` when `-usePromCompatibleNaming` command-line flag is passed to `vmagent`, `vminsert` or single-node VictoriaMetrics. This addresses [this comment](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/3113#issuecomment-1275077071).
* BUGFIX: [vmbackup](https://docs.victoriametrics.com/victoriametrics/vmbackup/): correctly check if specified `-dst` belongs to specified `-storageDataPath`. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/4837).


## [v1.87.7](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.87.7)

Released at 2023-08-12

**v1.87.x is a line of [LTS releases](https://docs.victoriametrics.com/victoriametrics/lts-releases/). It contains important up-to-date bugfixes.
The v1.87.x line will be supported for at least 12 months since [v1.87.0](https://docs.victoriametrics.com/victoriametrics/changelog/#v1870) release**

* SECURITY: upgrade Go builder from Go1.20.4 to Go1.21.0.
* SECURITY: upgrade base docker image (Alpine) from 3.18.2 to 3.18.3. See [alpine 3.18.3 release notes](https://alpinelinux.org/posts/Alpine-3.15.10-3.16.7-3.17.5-3.18.3-released.html).

* BUGFIX: vmselect: fix timestamp alignment for Prometheus querying API if time argument is less than 10m from the beginning of Unix epoch.
* BUGFIX: vminsert: fixed decoding of label values with slash when accepting data via [pushgateway protocol](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#how-to-import-data-in-prometheus-exposition-format). This fixes Prometheus golang client compatibility. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/4692).
* BUGFIX: [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/): properly validate scheme for `proxy_url` field at the scrape config. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/4811) for details.
* BUGFIX: [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/): close HTTP connections to [service discovery](https://docs.victoriametrics.com/victoriametrics/sd_configs/) servers when they are no longer needed. This should prevent from possible connection exhaustion in some cases. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/4724).
* BUGFIX: [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/): properly apply `if` filters during [relabeling](https://docs.victoriametrics.com/victoriametrics/relabeling/#relabeling-enhancements). Previously the `if` filter could improperly work. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/4806) and [this pull request](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/4816).
* BUGFIX: [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/): fix possible panic at shutdown when [stream aggregation](https://docs.victoriametrics.com/victoriametrics/stream-aggregation/) is enabled. See [this pull request](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/4407) for details.
* BUGFIX: [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/): use local scrape timestamps for the scraped metrics unless `honor_timestamps: true` option is explicitly set at [scrape_config](https://docs.victoriametrics.com/victoriametrics/sd_configs/#scrape_configs). This fixes gaps for metrics collected from [cadvisor](https://github.com/google/cadvisor) or similar exporters, which export metrics with invalid timestamps. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/4697) and [this comment](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/4697#issuecomment-1654614799) for details.
* BUGFIX: [vmauth](https://docs.victoriametrics.com/victoriametrics/vmauth/): Properly handle LOCAL command for proxy protocol. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/3335#issuecomment-1569864108).
* BUGFIX: [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): properly return error from [/api/v1/query](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#instant-query) and [/api/v1/query_range](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#range-query) at `vmselect` when the `-search.maxSamplesPerQuery` or `-search.maxSamplesPerSeries` [limit](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/#resource-usage-limits) is exceeded. Previously incomplete response could be returned without the error if `vmselect` runs with `-replicationFactor` greater than 1. See [this pull request](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/4472).
* BUGFIX: [vmalert](https://docs.victoriametrics.com/victoriametrics/vmalert/): correctly calculate evaluation time for rules. Before, there was a low probability for discrepancy between actual time and rules evaluation time if evaluation interval was lower than the execution time for rules within the group.
* BUGFIX: [vmalert](https://docs.victoriametrics.com/victoriametrics/vmalert/): reset evaluation timestamp after modifying group interval. Before, there could have latency on rule evaluation time.
* BUGFIX: [vmalert](https://docs.victoriametrics.com/victoriametrics/vmalert/): Properly set datasource query params. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/4340). Thanks to @gsakun for [the pull request](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/4341).
* BUGFIX: [vmalert](https://docs.victoriametrics.com/victoriametrics/vmalert/): Properly form path to static assets in WEB UI if `http.pathPrefix` set. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/4349).
* BUGFIX: [vmalert](https://docs.victoriametrics.com/victoriametrics/vmalert/): properly return empty slices instead of nil for `/api/v1/rules` for groups with present name but absent `rules`. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/4221).
* BUGFIX: [vmctl](https://docs.victoriametrics.com/victoriametrics/vmctl/): interrupt explore procedure in influx mode if vmctl found no numeric fields.
* BUGFIX: [vmctl](https://docs.victoriametrics.com/victoriametrics/vmctl/): fix panic in case `--remote-read-filter-time-start` flag is not set for remote-read mode. This flag is now required to use remote-read mode. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/4553).


## [v1.87.6](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.87.6)

Released at 2023-05-18

**v1.87.x is a line of [LTS releases](https://docs.victoriametrics.com/victoriametrics/lts-releases/). It contains important up-to-date bugfixes.
The v1.87.x line will be supported for at least 12 months since [v1.87.0](https://docs.victoriametrics.com/victoriametrics/changelog/#v1870) release**

* SECURITY: upgrade Go builder from Go1.20.3 to Go1.20.4. See [the list of issues addressed in Go1.20.4](https://github.com/golang/go/issues?q=milestone%3AGo1.20.4+label%3ACherryPickApproved).
* SECURITY: upgrade base docker image (alpine) from 3.17.3 to 3.18.0. See [alpine 3.18.0 release notes](https://www.alpinelinux.org/posts/Alpine-3.18.0-released.html).
* SECURITY: serve `/robots.txt` content to disallow indexing of the exposed instances by search engines. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/4128) for details.

* BUGFIX: reduce the probability of sudden increase in the number of small parts on systems with small number of CPU cores.
* BUGFIX: reduce the possibility of increased CPU usage when data with timestamps older than one hour is ingested into VictoriaMetrics. This reduces spikes for the graph `sum(rate(vm_slow_per_day_index_inserts_total))`. See [this pull request](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/4258).
* BUGFIX: do not ignore trailing empty field in CSV lines when [importing data in CSV format](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#how-to-import-csv-data). See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/4048).
* BUGFIX: disallow `"` chars when parsing Prometheus label names, since they aren't allowed by [Prometheus text exposition format](https://prometheus.io/docs/instrumenting/exposition_formats/#line-format). Previously this could result in silent incorrect parsing of incorrect Prometheus labels such as `foo{"bar"="baz"}` or `{foo:"bar",baz="aaa"}`. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/4284).
* BUGFIX: [MetricsQL](https://docs.victoriametrics.com/victoriametrics/metricsql/): fix a panic when the duration in the query contains uppercase `M` suffix. Such a suffix isn't allowed to use in durations, since it clashes with `a million` suffix, e.g. it isn't clear whether `rate(metric[5M])` means rate over 5 minutes, 5 months or 5 million seconds. See [this](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/3589) and [this](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/4120) issues.
* BUGFIX: [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): prevent from possible panic when the number of vmstorage nodes increases when [automatic vmstorage discovery](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/#automatic-vmstorage-discovery) is enabled.
* BUGFIX: properly limit the number of [OpenTSDB HTTP](https://docs.victoriametrics.com/victoriametrics/integrations/opentsdb/#sending-data-via-http) concurrent requests specified via `-maxConcurrentInserts` command-line flag. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/4204). Thanks to @zouxiang1993 for [the fix](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/4208).
* BUGFIX: [vmalert](https://docs.victoriametrics.com/victoriametrics/vmalert/): properly return empty slices instead of nil for `/api/v1/rules` and `/api/v1/alerts` API handlers. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/4221).
* BUGFIX: [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/): add `__meta_kubernetes_endpoints_name` label for all ports discovered from endpoint. Previously, ports not matched by `Service` did not have this label. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/4154) for details. Thanks to @thunderbird86 for discovering and [fixing](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/4253) the issue.
* BUGFIX: fix possible infinite loop during `indexdb` rotation when `-retentionTimezoneOffset` command-line flag is set and the local timezone is not UTC. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/4207). Thanks to @faceair for [the fix](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/4206).
* BUGFIX: [vmauth](https://docs.victoriametrics.com/victoriametrics/vmauth/): do not return invalid auth credentials in http response by default, since it may be logged by client. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/4188).
* BUGFIX: [alerts-health](https://github.com/VictoriaMetrics/VictoriaMetrics/blob/master/deployment/docker/rules/alerts-health.yml): update threshold for `TooHighMemoryUsage` alert from 90% to 80%, since 90% is too high for production environments.
* BUGFIX: [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/): properly handle the `vm_promscrape_config_last_reload_successful` metric after config reload. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/4260).
* BUGFIX: [stream aggregation](https://docs.victoriametrics.com/victoriametrics/stream-aggregation/): fix bug with duplicated labels during stream aggregation via single-node VictoriaMetrics. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/4277).
* BUGFIX: [stream aggregation](https://docs.victoriametrics.com/victoriametrics/stream-aggregation/): suppress `series after dedup` error message in logs when `-remoteWrite.streamAggr.dedupInterval` command-line flag is set at [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/) or when `-streamAggr.dedupInterval` command-line flag is set at [single-node VictoriaMetrics](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/).
