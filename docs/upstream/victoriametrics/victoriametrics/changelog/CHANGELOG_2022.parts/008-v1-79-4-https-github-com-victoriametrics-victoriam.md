<!-- Part 8 of 13 of victoriametrics/changelog/CHANGELOG_2022.md (split because the page is big). -->

## [v1.79.4](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.79.4)

Released at 2022-10-07

**v1.79.x is a line of [LTS releases](https://docs.victoriametrics.com/victoriametrics/lts-releases/). It contains important up-to-date bugfixes.
The v1.79.x line will be supported for at least 12 months since [v1.79.0](https://docs.victoriametrics.com/victoriametrics/changelog/#v1790) release**

**Update note 1:** [vmalert](https://docs.victoriametrics.com/victoriametrics/vmalert/) changes default value for command-line flag `-datasource.queryStep` from `0s` to `5m`. The change supposed to improve reliability of the rules evaluation when evaluation interval is lower than scraping interval.

* FEATURE: expose `vmagent_remotewrite_queues` metric and use it in alerting rules in order to improve the detection of remote storage connection saturation. See [this pull request](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/2871).

* BUGFIX: do not export stale metrics via [/federate api](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#federation) after the staleness markers. Previously such metrics were exported with `NaN` values. this could break some setups. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/3185).
* BUGFIX: [vmauth](https://docs.victoriametrics.com/victoriametrics/vmauth/): properly handle request paths ending with `/` such as `/vmui/`. Previously `vmui` was dropping the trailing `/`, which could prevent from using `vmui` via `vmauth`. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/1752).
* BUGFIX: [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/): properly encode query params for aws signed requests, use `%20` instead of `+` as api requires. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/3171).
* BUGFIX: [MetricsQL](https://docs.victoriametrics.com/victoriametrics/metricsql/): properly calculate `rate_over_sum(m[d])` as `sum_over_time(m[d])/d`. Previously the `sum_over_time(m[d])` could be improperly divided by smaller than `d` time range. See [rate_over_sum() docs](https://docs.victoriametrics.com/victoriametrics/metricsql/#rate_over_sum) and [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/3045).
* BUGFIX: [MetricsQL](https://docs.victoriametrics.com/victoriametrics/metricsql/): properly calculate `increase(m[d])` over slow-changing counters with values smaller than 100. Previously [increase](https://docs.victoriametrics.com/victoriametrics/metricsql/#increase) could return unexpectedly big results in this case. See [the related issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/962) and [this pull request](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/3163).
* BUGFIX: [MetricsQL](https://docs.victoriametrics.com/victoriametrics/metricsql/): ignore empty series when applying [limit_offset](https://docs.victoriametrics.com/victoriametrics/metricsql/#limit_offset). It should improve queries with additional filters by value in expressions like `limit_offset(1,1, foo > 1)`.
* BUGFIX: [MetricsQL](https://docs.victoriametrics.com/victoriametrics/metricsql/): properly calculate [quantiles_over_time](https://docs.victoriametrics.com/victoriametrics/metricsql/#quantiles_over_time) when the lookbehind window contains only a single sample. Previously an empty result was incorrectly returned in this case.
* BUGFIX: [vmui](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#vmui): fix `RangeError: Maximum call stack size exceeded` error when the query returns too many data points at `Table` view. See [this pull request](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/3092/files).
* BUGFIX: [vmalert](https://docs.victoriametrics.com/victoriametrics/vmalert/): re-evaluate annotations per each alert evaluation. Previously, annotations were evaluated only on alert's value change. This could result in stale annotations in some cases described in [this pull request](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/3119).
* BUGFIX: prevent from excessive CPU usage when the storage enters [read-only mode](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/#readonly-mode). The previous fix in [v1.79.3](https://docs.victoriametrics.com/victoriametrics/changelog/#v1793) wasn't complete.
* BUGFIX: [vmalert](https://docs.victoriametrics.com/victoriametrics/vmalert/): change default value for command-line flag `-datasource.queryStep` from `0s` to `5m`. Param `step` is added by vmalert to every rule evaluation request sent to datasource. Before this change, `step` was equal to group's evaluation interval by default. Param `step` for instant queries defines how far VM can look back for the last written data point. The change supposed to improve reliability of the rules evaluation when evaluation interval is lower than scraping interval.
* BUGFIX: properly calculate `vm_rows_scanned_per_query` histogram exported at `/metrics` page of `vmselect` and single-node VictoriaMetrics. Previously it could return misleadingly high numbers for [rollup functions](https://docs.victoriametrics.com/victoriametrics/metricsql/#rollup-functions), which scan only a few samples on the provided lookbehind window in square brackets. For example, `increase(m[1d])` always scans only 2 rows (aka `raw samples`) per each returned time series.


## [v1.79.3](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.79.3)

Released at 2022-08-30

**v1.79.x is a line of [LTS releases](https://docs.victoriametrics.com/victoriametrics/lts-releases/). It contains important up-to-date bugfixes.
The v1.79.x line will be supported for at least 12 months since [v1.79.0](https://docs.victoriametrics.com/victoriametrics/changelog/#v1790) release**

* SECURITY: [vmalert](https://docs.victoriametrics.com/victoriametrics/vmalert/): do not expose `-remoteWrite.url`, `-remoteRead.url` and `-datasource.url` command-line flag values in logs and at `http://vmalert:8880/flags` page by default, since they may contain sensitive data such as auth keys. This aligns `vmalert` behaviour with [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/), which doesn't expose `-remoteWrite.url` command-line flag value in logs and at `http://vmagent:8429/flags` page by default. Specify `-remoteWrite.showURL`, `-remoteRead.showURL` and `-datasource.showURL` command-line flags for showing values for the corresponding `-*.url` flags in logs. Thanks to @mble for [the pull request](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/2965).
* SECURITY: upgrade base docker image (alpine) from 3.16.1 to 3.16.2. See [alpine 3.16.2 release notes](https://alpinelinux.org/posts/Alpine-3.13.12-3.14.8-3.15.6-3.16.2-released.html).

* BUGFIX: prevent from excess CPU usage when the storage enters [read-only mode](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/#readonly-mode).
* BUGFIX: improve performance for requests to [/api/v1/labels](https://docs.victoriametrics.com/victoriametrics/url-examples/#apiv1labels) and [/api/v1/label/.../values](https://docs.victoriametrics.com/victoriametrics/url-examples/#apiv1labelvalues) when the filter in the `match[]` query arg matches small number of time series. The performance for this case has been reduced in [v1.78.0](https://docs.victoriametrics.com/victoriametrics/changelog/#v1780). See [this](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/2978) and [this](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/1533) issues.
* BUGFIX: increase the default limit on the number of concurrent merges for small parts from 8 to 16. This should help resolving potential issues with heavy data ingestion. See [this comment](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/2673#issuecomment-1218185978) from @lukepalmer .
* BUGFIX: [MetricsQL](https://docs.victoriametrics.com/victoriametrics/metricsql/): fix panic when incorrect arg is passed as `phi` into [histogram_quantiles](https://docs.victoriametrics.com/victoriametrics/metricsql/#histogram_quantiles) function. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/3026).


## [v1.79.2](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.79.2)

Released at 2022-08-08

**v1.79.x is a line of [LTS releases](https://docs.victoriametrics.com/victoriametrics/lts-releases/). It contains important up-to-date bugfixes.
The v1.79.x line will be supported for at least 12 months since [v1.79.0](https://docs.victoriametrics.com/victoriametrics/changelog/#v1790) release**

* BUGFIX: [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): fix potential panic in [multi-level cluster setup](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/#multi-level-cluster-setup) when top-level `vmselect` is configured with `-replicationFactor` bigger than 1. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/2961).
* BUGFIX: [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/): properly handle custom `endpoint` value in [ec2_sd_configs](https://docs.victoriametrics.com/victoriametrics/sd_configs/#ec2_sd_configs). It was ignored since [v1.77.0](https://docs.victoriametrics.com/victoriametrics/changelog/#v1770) because of a bug in the implementation of [this feature request](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/1287).
* BUGFIX: [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/): add missing `__meta_kubernetes_ingress_class_name` meta-label for `role: ingress` service discovery in Kubernetes. See [this commit from Prometheus](https://github.com/prometheus/prometheus/commit/7e65ad3e432bd2837c17e3e63e85dcbcc30f4a8a).
* BUGFIX: [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/): allow stale responses from Consul service discovery (aka [consul_sd_configs](https://docs.victoriametrics.com/victoriametrics/sd_configs/#consul_sd_configs)) by default in the same way as Prometheus does. This should reduce load on Consul when discovering big number of targets. Stale responses can be disabled by specifying `allow_stale: false` option in `consul_sd_config`. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/2940).
* BUGFIX: [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/): [dockerswarm_sd_configs](https://docs.victoriametrics.com/victoriametrics/sd_configs/#dockerswarm_sd_configs): properly set `__meta_dockerswarm_container_label_*` labels instead of `__meta_dockerswarm_task_label_*` labels as Prometheus does. See [this issue](https://github.com/prometheus/prometheus/issues/9187).
* BUGFIX: [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/): set `up` metric to `0` for partial scrapes in [stream parsing mode](https://docs.victoriametrics.com/victoriametrics/vmagent/#stream-parsing-mode). Previously the `up` metric was set to `1` when at least a single metric has been scraped before the error. This aligns the behaviour of `vmselect` with Prometheus.
* BUGFIX: [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/): restart all the scrape jobs during [config reload](https://docs.victoriametrics.com/victoriametrics/vmagent/#configuration-update) after `global` section is changed inside `-promscrape.config`. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/2884).
* BUGFIX: [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/): properly assume role with AWS ECS credentials. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/2875). Thanks to @transacid for [the fix](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/2876).
* BUGFIX: [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/): do not split regex in [relabeling rules](https://docs.victoriametrics.com/victoriametrics/relabeling/) into multiple lines if it contains groups. This fixes [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/2928).
* BUGFIX: [MetricsQL](https://docs.victoriametrics.com/victoriametrics/metricsql/): return series from `q1` if `q2` doesn't return matching time series in the query `q1 ifnot q2`. Previously series from `q1` weren't returned in this case.
* BUGFIX: [vmui](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#vmui): properly show date picker at `Table` tab. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/2874).
* BUGFIX: properly generate http redirects if `-http.pathPrefix` command-line flag is set. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/2918).



## [v1.79.1](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.79.1)

Released at 2022-08-02

**v1.79.x is a line of [LTS releases](https://docs.victoriametrics.com/victoriametrics/lts-releases/). It contains important up-to-date bugfixes.
The v1.79.x line will be supported for at least 12 months since [v1.79.0](https://docs.victoriametrics.com/victoriametrics/changelog/#v1790) release**

* SECURITY: upgrade base docker image (alpine) from 3.16.0 to 3.16.1 . See [alpine 3.16.1 release notes](https://alpinelinux.org/posts/Alpine-3.16.1-released.html).
