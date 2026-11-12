<!-- Part 4 of 13 of victoriametrics/changelog/CHANGELOG_2022.md (split because the page is big). -->

## [v1.83.0](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.83.0)

Released at 2022-10-29

**It is recommended upgrading to [VictoriaMetrics v1.85.2](https://docs.victoriametrics.com/victoriametrics/changelog/#v1852) because of [the bug](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/3502), which may result in incomplete query results for historical time series.**

**Update note 1:** the `indexdb/tagFilters` cache type at [/metrics](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#monitoring) has been renamed to `indexdb/tagFiltersToMetricIDs` in order to make its purpose more clear.

**Update note 2:** [vmalert](https://docs.victoriametrics.com/victoriametrics/vmalert/): the `crlfEscape` [template function](https://docs.victoriametrics.com/victoriametrics/vmalert/#template-functions) becomes obsolete starting from this release. It can be safely removed from alerting templates, since `\n` chars are properly escaped with other `*Escape` functions now. See [this](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/3139) and [this](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/890) issue for details.


* FEATURE: [VictoriaMetrics Enterprise](https://docs.victoriametrics.com/victoriametrics/enterprise/): add support for automatic `vmstorage` nodes discovering and updating at `vmselect` and `vminsert`. See [these docs](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/#automatic-vmstorage-discovery).
* FEATURE: [VictoriaMetrics Enterprise](https://docs.victoriametrics.com/victoriametrics/enterprise/): allow configuring multiple retentions for distinct sets of time series. See [these docs](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#retention-filters), [this](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/143) and [this](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/289) feature request.
* FEATURE: [VictoriaMetric cluster enterprise](https://docs.victoriametrics.com/victoriametrics/enterprise/): add support for multiple retentions for distinct tenants - see [these docs](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/#retention-filters) and [this](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/143) and [this](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/289) feature request.
* FEATURE: allow limiting memory usage on a per-query basis with `-search.maxMemoryPerQuery` command-line flag. See [this feature request](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/3203).
* FEATURE: allow referring environment variables inside command-line flags via `%{ENV_VAR}` syntax. For example, if `AUTH_KEY=top-secret` environment variable is set, then `-metricsAuthKey=%{AUTH_KEY}` command-line flag is automatically expanded to `-storageDataPath=top-secret` at VictoriaMetrics startup. See [these docs](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#environment-variables) for details.
* FEATURE: allow referring environment variables inside other environment variables via `%{ENV_VAR}` syntax. For example, if `A=a-%{B}`, `B=b-%{C}` and `C=c` env vars are set, then VictoriaMetrics components automatically expand them to `A=a-b-c`, `B=b-c` and `C=c` on startup.
* FEATURE: [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/): drop all the labels with `__` prefix from discovered targets in the same way as Prometheus does according to [this article](https://www.robustperception.io/life-of-a-label/). Previously the following labels were available during [metric-level relabeling](https://prometheus.io/docs/prometheus/latest/configuration/configuration/#metric_relabel_configs): `__address__`, `__scheme__`, `__metrics_path__`, `__scrape_interval__`, `__scrape_timeout__`, `__param_*`. Now these labels are available only during [target-level relabeling](https://prometheus.io/docs/prometheus/latest/configuration/configuration/#relabel_config). This should reduce CPU usage and memory usage for `vmagent` setups, which scrape big number of targets.
* FEATURE: [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/): improve the performance for metric-level [relabeling](https://docs.victoriametrics.com/victoriametrics/relabeling/), which can be applied via `metric_relabel_configs` section at [scrape_configs](https://docs.victoriametrics.com/victoriametrics/sd_configs/#scrape_configs), via `-remoteWrite.relabelConfig` or via `-remoteWrite.urlRelabelConfig` command-line options.
* FEATURE: [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/): allow specifying full url in scrape target addresses (aka `__address__` label). This makes valid the following `-promscrape.config`:

  ```yaml
  scrape_configs:
  - job_name: abc
    metrics_path: /foo/bar
    scheme: https
    static_configs:
    - targets:
      # the following targets are scraped by the provided full urls
      - 'http://host1/metric/path1'
      - 'https://host2/metric/path2'
      - 'http://host3:1234/metric/path3?arg1=value1'
      # the following target is scraped by <scheme>://host4:1234<metrics_path>
      - host4:1234
  ```

  See [the corresponding issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/3208).

* FEATURE: [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/): allow controlling [staleness tracking](https://docs.victoriametrics.com/victoriametrics/vmagent/#prometheus-staleness-markers) on a per-[scrape_config](https://docs.victoriametrics.com/victoriametrics/sd_configs/#scrape_configs) basis by specifying `no_stale_markers: true` or `no_stale_markers: false` option in the corresponding [scrape_config](https://docs.victoriametrics.com/victoriametrics/sd_configs/#scrape_configs).
* FEATURE: [vmalert](https://docs.victoriametrics.com/victoriametrics/vmalert/): add `strvalue` and `stripDomain` [template functions](https://docs.victoriametrics.com/victoriametrics/vmalert/#template-functions) in order to improve compatibility with Prometheus.
* FEATURE: [vmalert](https://docs.victoriametrics.com/victoriametrics/vmalert/): add `jsonEscape` and `htmlEscape` [template functions](https://docs.victoriametrics.com/victoriametrics/vmalert/#template-functions).
* FEATURE: [vmui](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#vmui): limit the number of plotted series. This should prevent from browser crashes or hangs when the query returns big number of time series. See [this feature request](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/3155).
* FEATURE: [vmui](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#vmui): reduce memory usage when querying big number of time series. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/3240).
* FEATURE: [vmui](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#vmui): add responsive styles for small screens. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/3239) and [this pull request](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/3256).
* FEATURE: log error if some environment variables referred at `-promscrape.config` via `%{ENV_VAR}` aren't found. This should prevent from silent using incorrect config files.
* FEATURE: immediately shut down VictoriaMetrics apps on the second SIGINT or SIGTERM signal if they couldn't be finished gracefully for some reason after receiving the first signal.
* FEATURE: improve the performance of [/api/v1/series](https://docs.victoriametrics.com/victoriametrics/url-examples/#apiv1series) endpoint by eliminating loading of unused `TSID` data during the API call.
* FEATURE: [vmbackupmanager](https://docs.victoriametrics.com/victoriametrics/vmbackupmanager/): add functionality for automated restore from backup. See [these docs](https://docs.victoriametrics.com/victoriametrics/vmbackupmanager/#how-to-restore-backup-via-cli).

* BUGFIX: [MetricsQL](https://docs.victoriametrics.com/victoriametrics/metricsql/): properly merge buckets with identical `le` values, but with different string representation of these values when calculating [histogram_quantile](https://docs.victoriametrics.com/victoriametrics/metricsql/#histogram_quantile) and [histogram_share](https://docs.victoriametrics.com/victoriametrics/metricsql/#histogram_share). For example, `http_request_duration_seconds_bucket{le="5"}` and `http_requests_duration_seconds_bucket{le="5.0"}`. Such buckets may be returned from distinct targets. Thanks to @647-coder for the [pull request](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/3225).
* BUGFIX: [vmalert](https://docs.victoriametrics.com/victoriametrics/vmalert/): change severity level for log messages about failed attempts for sending data to remote storage from `error` to `warn`. The message for about all failed send attempts remains at `error` severity level.
* BUGFIX: [vmalert](https://docs.victoriametrics.com/victoriametrics/vmalert/): fix panic if `vmalert` runs with `-clusterMode` command-line flag in [multitenant mode](https://docs.victoriametrics.com/victoriametrics/vmalert/#multitenancy). The issue has been introduced in [v1.82.0](https://docs.victoriametrics.com/victoriametrics/changelog/#v1820).
* BUGFIX: [vmalert](https://docs.victoriametrics.com/victoriametrics/vmalert/): properly escape string passed to `quotesEscape` [template function](https://docs.victoriametrics.com/victoriametrics/vmalert/#template-functions), so it can be safely embedded into JSON string. This makes obsolete the `crlfEscape` function. See [this](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/3139) and [this](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/890) issue.
* BUGFIX: [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/): do not show invalid error message in Kubernetes service discovery: `cannot parse WatchEvent json response: EOF`. The invalid error message has been appeared in [v1.82.0](https://docs.victoriametrics.com/victoriametrics/changelog/#v1820).
* BUGFIX: [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/): properly add `exported_` prefix to metric labels, which clashing with scrape target labels if `honor_labels: true` option isn't set in [scrape_config](https://docs.victoriametrics.com/victoriametrics/sd_configs/#scrape_configs). Previously some `exported_` prefixes were missing in the resulting metric labels. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/3278). The issue has been introduced in [v1.82.0](https://docs.victoriametrics.com/victoriametrics/changelog/#v1820).
* BUGFIX: `vmselect`: expose missing metric `vm_cache_size_max_bytes{type="promql/rollupResult"}` . This metric is used for monitoring rollup cache usage with the query `vm_cache_size_bytes{type="promql/rollupResult"} / vm_cache_size_max_bytes{type="promql/rollupResult"}` in the same way as this is done for other cache types.


## [v1.82.1](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.82.1)

Released at 2022-10-14

* BUGFIX: [vmui](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#vmui): automatically update graph, legend and url after the removal of query field. See [this feature request](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/3169) and [this comment](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/3196#issuecomment-1269765205).
* BUGFIX: [vmalert](https://docs.victoriametrics.com/victoriametrics/vmalert/): remove duplicate `alertname` JSON entry from generated alerts. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/3053). Thanks to @Howie59 for [the fix](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/3182)!
* BUGFIX: [vmalert](https://docs.victoriametrics.com/victoriametrics/vmalert/): fix integration with Grafana via `-vmalert.proxyURL`, which has been broken in [v1.82.0](https://docs.victoriametrics.com/victoriametrics/changelog/#v1820). See [this issue](https://github.com/VictoriaMetrics/helm-charts/issues/391).
* BUGFIX: [vmbackup](https://docs.victoriametrics.com/victoriametrics/vmbackup/): set default region to `us-east-1` if `AWS_REGION` environment variable isn't set. The issue was introduced in [vmbackup v1.82.0](https://docs.victoriametrics.com/victoriametrics/changelog/#v1820). See [this pull request](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/3224).
* BUGFIX: [vmbackupmanager](https://docs.victoriametrics.com/victoriametrics/vmbackupmanager/): fix deletion of old backups at [Azure blob storage](https://azure.microsoft.com/en-us/products/storage/blobs/).
* BUGFIX: [MetricsQL](https://docs.victoriametrics.com/victoriametrics/metricsql/): properly apply regex filters when searching for time series. Previously unexpected time series could be returned from regex filter. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/3227). The issue was introduced in [v1.82.0](https://docs.victoriametrics.com/victoriametrics/changelog/#v1820).
* BUGFIX: [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/): properly apply `if` section with regex filters. Previously unexpected metrics could be returned from `if` section. The issue was introduced in [v1.82.0](https://docs.victoriametrics.com/victoriametrics/changelog/#v1820).
