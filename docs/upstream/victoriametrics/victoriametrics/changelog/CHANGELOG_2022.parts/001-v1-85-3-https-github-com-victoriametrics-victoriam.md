<!-- Part 1 of 13 of victoriametrics/changelog/CHANGELOG_2022.md (split because the page is big). -->

## [v1.85.3](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.85.3)

Released at 2022-12-20

**Update note 1:** This and newer releases of VictoriaMetrics may return gaps for `rate(m[d])` queries on short time ranges if `[d]` lookbehind window is set explicitly. For example, `rate(http_requests_total[$__interval])`. This reduces confusion level when the user expects the needed results from the query with explicitly set lookbehind window. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/3483). The previous gap filling behaviour can be restored by removing explicit lookbehind window `[d]` from the query, e.g. by substituting the `rate(m[d])` with `rate(m)`. See [these docs](https://docs.victoriametrics.com/victoriametrics/metricsql/#implicit-query-conversions) for details.

* BUGFIX: fix `error when searching for TSIDs by metricIDs in the previous indexdb: EOF` error, which can occur during queries after unclean shutdown of VictoriaMetrics (e.g. via hardware reset, out of memory crash or `kill -9`). The error has been introduced in [v1.85.2](https://docs.victoriametrics.com/victoriametrics/changelog/#v1852). See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/3515).
* BUGFIX: [VictoriaMetrics Enterprise](https://docs.victoriametrics.com/victoriametrics/enterprise/): expose proper values for `vm_downsampling_partitions_scheduled` and `vm_downsampling_partitions_scheduled_size_bytes` metrics, which were added at [v1.78.0](https://docs.victoriametrics.com/victoriametrics/changelog/#v1780). See [this feature request](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/2612).
* BUGFIX: [MetricsQL](https://docs.victoriametrics.com/victoriametrics/metricsql/): never extend explicitly set lookbehind window for [rate()](https://docs.victoriametrics.com/victoriametrics/metricsql/#rate) function. This reduces the level of confusion when the user expects the needed results after explicitly setting the lookbehind window `[d]` in the query `rate(m[d])`. Previously VictoriaMetrics could silently extend the lookbehind window, so it covers at least two raw samples. Now this behavior works only if the lookbehind window in square brackets isn't set explicitly, e.g. in the case of `rate(m)`. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/3483) for details.
* BUGFIX: [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/): respect `-usePromCompatibleNaming` flag if no relabeling or extra labels were set. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/3511) for details.
* BUGFIX: [vmui](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#vmui): fix the wrong legend when queries are hidden. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/3512).
* BUGFIX: [vmui](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#vmui): fix incorrect time selection after the timezone change. See [this pull request](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/3519).



## [v1.85.2](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.85.2)

Released at 2022-12-19

* FEATURE: support overriding of `-search.latencyOffset` value via URL param `latency_offset` when performing requests to [/api/v1/query](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#instant-query) and [/api/v1/query_range](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#range-query). See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/3481).
* FEATURE: allow changing field names in JSON logs if VictoriaMetrics components are started with `-loggerFormat=json` command-line flags. The field names can be changed with the `-loggerJSONFields` command-line flag. For example `-loggerJSONFields=ts:timestamp,msg:message` would rename `ts` and `msg` fields on the output JSON to `timestamp` and `message` fields. See [this feature request](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/2348). Thanks to @michal-kralik for [the pull request](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/3488).
* FEATURE: [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/): expose `__meta_consul_tag_<tagname>` and `__meta_consul_tagpresent_<tagname>` labels for targets discovered via [consul_sd_configs](https://docs.victoriametrics.com/victoriametrics/sd_configs/#consul_sd_configs). This simplifies converting [Consul service tags](https://developer.hashicorp.com/consul/docs/services/discovery/dns-overview) to target labels with a simple [relabeling rule](https://docs.victoriametrics.com/victoriametrics/relabeling/):

  ```yaml
  - action: labelmap
    regex: __meta_consul_tag_(.+)
  ```

  This resolves [this StackOverflow question](https://stackoverflow.com/questions/44339461/relabeling-in-prometheus).

* BUGFIX: properly return query results for time series, which stop receiving new samples after the rotation of `indexdb`. Previously such time series could be missing in query results. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/3502). The issue has been introduced in [v1.83.0](https://docs.victoriametrics.com/victoriametrics/changelog/#v1830).
* BUGFIX: allow specifying values bigger than 2GiB to the following command-line flag values on 32-bit architectures (`386` and `arm`): `-storage.minFreeDiskSpaceBytes` and `-remoteWrite.maxDiskUsagePerURL`. Previously values bigger than 2GiB were incorrectly truncated on these architectures.
* BUGFIX: [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/): stop dropping metric name by a mistake on the [/metric-relabel-debug](https://docs.victoriametrics.com/victoriametrics/relabeling/#relabel-debugging) page.



## [v1.85.1](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.85.1)

Released at 2022-12-14

**It is recommended upgrading to [VictoriaMetrics v1.85.2](https://docs.victoriametrics.com/victoriametrics/changelog/#v1852) because of [the bug](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/3502), which may result in incomplete query results for historical time series.**

* FEATURE: [vmalert](https://docs.victoriametrics.com/victoriametrics/vmalert/): support `$for` or `.For` template variables in alert's annotations. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/3246).

* BUGFIX: [DataDog protocol parser](https://docs.victoriametrics.com/victoriametrics/integrations/datadog/): do not reuse `host` and `device` fields from the previously parsed messages if these fields are missing in the currently parsed message. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/3432).
* BUGFIX: reduce CPU usage when the regex-based relabeling rules are applied to more than 100K unique Graphite metrics. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/3466). The issue was introduced in [v1.82.0](https://docs.victoriametrics.com/victoriametrics/changelog/#v1820).
* BUGFIX: do not block [merges](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#storage) of small parts by merges of big parts on hosts with small number of CPU cores. This issue could result in the increasing number of `storage/small` parts while big merge is in progress. This, in turn, could result in increased CPU usage and memory usage during querying, since queries need to inspect bigger number of small parts. The issue has been introduced in [v1.85.0](https://docs.victoriametrics.com/victoriametrics/changelog/#v1850).
* BUGFIX: [vmbackup](https://docs.victoriametrics.com/victoriametrics/vmbackup/): fix the `The source request body for synchronous copy is too large and exceeds the maximum permissible limit (256MB)` error when performing backups to Azure blob storage. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/3477).
