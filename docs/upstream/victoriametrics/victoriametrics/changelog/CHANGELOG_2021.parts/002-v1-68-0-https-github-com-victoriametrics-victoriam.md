<!-- Part 2 of 7 of victoriametrics/changelog/CHANGELOG_2021.md (split because the page is big). -->

## [v1.68.0](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.68.0)

Released at 2021-10-22

* FEATURE: vmagent: expose `-promscrape.config` contents at `/config` page as Prometheus does. See [this feature request](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/1695).
* FEATURE: vmagent: add `show original labels` button per each scrape target displayed at `http://vmagent:8429/targets` page. This should improve debuggability for service discovery and relabeling issues similar to [this one](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/1664). See [this feature request](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/1698).
* FEATURE: vmagent: shard targets among cluster nodes after the relabeling is applied. This should guarantee that targets with the same set of labels go to the same `vmagent` node in the cluster. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/1687).
* FEATURE: vmagent: automatically switch to [stream parsing mode](https://docs.victoriametrics.com/victoriametrics/vmagent/#stream-parsing-mode) if the response from the given target exceeds the command-line flag value `-promscrape.minResponseSizeForStreamParse`. This should reduce memory usage when `vmagent` scrapes targets with non-uniform response sizes (this is the case in Kubernetes monitoring).
* FEATURE: vmagent: send Prometheus-like staleness marks in [stream parsing mode](https://docs.victoriametrics.com/victoriametrics/vmagent/#stream-parsing-mode). Previously staleness marks weren't sent in stream parsing mode. See [these docs](https://docs.victoriametrics.com/victoriametrics/vmagent/#prometheus-staleness-markers) for details.
* FEATURE: vmagent: properly calculate `scrape_series_added` metric for targets in [stream parsing mode](https://docs.victoriametrics.com/victoriametrics/vmagent/#stream-parsing-mode). Previously it was set to 0 in stream parsing mode. See [more details about this metric](https://prometheus.io/docs/concepts/jobs_instances/#automatically-generated-labels-and-time-series).
* FEATURE: vmagent: expose `promscrape_series_limit_max_series` and `promscrape_series_limit_current_series` metrics at `http://vmagent:8429/metrics` for scrape targets with the [enabled series limiter](https://docs.victoriametrics.com/victoriametrics/vmagent/#cardinality-limiter).
* FEATURE: vmagent: return error if `sample_limit` or `series_limit` options are set when [stream parsing mode](https://docs.victoriametrics.com/victoriametrics/vmagent/#stream-parsing-mode) is enabled, since these limits cannot be applied in stream parsing mode.
* FEATURE: vmalert: add `-remoteRead.disablePathAppend` command-line flag, which allows specifying the full `-remoteRead.url`. If `-remoteRead.disablePathAppend` is set, then `vmalert` doesn't add `/api/v1/query` suffix to `-remoteRead.url`.
* FEATURE: add trigonometric functions, which are going to be added in [Prometheus 2.31](https://github.com/prometheus/prometheus/pull/9239): [acosh](https://docs.victoriametrics.com/victoriametrics/metricsql/#acosh), [asinh](https://docs.victoriametrics.com/victoriametrics/metricsql/#asinh), [atan](https://docs.victoriametrics.com/victoriametrics/metricsql/#atan), [atanh](https://docs.victoriametrics.com/victoriametrics/metricsql/#atanh), [cosh](https://docs.victoriametrics.com/victoriametrics/metricsql/#cosh), [deg](https://docs.victoriametrics.com/victoriametrics/metricsql/#deg), [rad](https://docs.victoriametrics.com/victoriametrics/metricsql/#rad), [sinh](https://docs.victoriametrics.com/victoriametrics/metricsql/#sinh), [tan](https://docs.victoriametrics.com/victoriametrics/metricsql/#tan), [tanh](https://docs.victoriametrics.com/victoriametrics/metricsql/#tanh). Also add `atan2` binary operator. See [this pull request](https://github.com/prometheus/prometheus/pull/9248).
* FEATURE: consistently return the same set of time series from [limitk](https://docs.victoriametrics.com/victoriametrics/metricsql/#limitk) function. This improves the usability of periodically refreshed graphs.
* FEATURE: [vmui](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#vmui): various UX improvements. See [this pull request](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/1711) and [these docs](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#vmui).
* FEATURE: [vmauth](https://docs.victoriametrics.com/victoriametrics/vmauth/): add ability to specify HTTP headers, which will be sent in requests to backends. See [this feature request](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/1736).
* FEATURE: add `/flags` page to all the VictoriaMetrics components. This page contains command-line flags passed to the component.
* FEATURE: allow using tab separators additionally to whitespace separators when [ingesting data in Graphite plaintext protocol](https://docs.victoriametrics.com/victoriametrics/integrations/graphite/#ingesting). Such separators are [supported by Carbon-c-relay](https://github.com/grobian/carbon-c-relay/commit/f3ffe6cc2b52b07d14acbda649ad3fd6babdd528).

* BUGFIX: vmstorage: fix `unaligned 64-bit atomic operation` panic on 32-bit architectures (arm and 386). The panic has been introduced in v1.67.0.
* BUGFIX: vmalert, vmauth: prevent from frequent closing of TCP connections established to backends under high load. This should reduce the number of TCP sockets in `TIME_WAIT` state at `vmalert` and `vmauth` under high load. See [this pull request](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/1704).
* BUGFIX: vmalert: correctly calculate alert ID including extra labels. Previously, ID for alert entity was generated without alertname or groupname. This led to collision, when multiple alerting rules within the same group producing same labelsets. E.g. expr: `sum(metric1) by (job) > 0` and expr: `sum(metric2) by (job) > 0` could result into same labelset `job: "job"`. The bugfix adds all extra labels right after receiving response from the datasource. See [this pull request](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/1734).
* BUGFIX: vmalert: fix links in [Web UI](https://docs.victoriametrics.com/victoriametrics/vmalert/#web). See [this pull request](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/1717).
* BUGFIX: vmagent: set `honor_timestamps: true` by default in [scrape configs](https://docs.victoriametrics.com/victoriametrics/sd_configs/#scrape_configs) if this options isn't set explicitly. This aligns the behaviour with Prometheus.
* BUGFIX: vmagent: group scrape targets by the original job names at `http://vmagent:8429/targets` page like Prometheus does. Previously they were grouped by the job name after relabeling, which may result in unexpected empty target groups. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/1707).
* BUGFIX: [vmctl](https://docs.victoriametrics.com/victoriametrics/vmctl/): fix importing boolean fields from InfluxDB line protocol. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/1709).


## [v1.67.0](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.67.0)

Released at 2021-10-08

* FEATURE: add ability to accept metrics from [DataDog agent](https://docs.datadoghq.com/agent/) and [DogStatsD](https://docs.datadoghq.com/developers/dogstatsd/). See [these docs](https://docs.victoriametrics.com/victoriametrics/integrations/datadog/). This option simplifies the migration path from DataDog to VictoriaMetrics. See also [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/206).
* FEATURE: vmagent [enterprise](https://docs.victoriametrics.com/victoriametrics/enterprise/): add support for data reading and writing from/to [Apache Kafka](https://kafka.apache.org/). See [these docs](https://docs.victoriametrics.com/victoriametrics/integrations/kafka/).
* FEATURE: vmui: switch to [μPlot](https://github.com/leeoniya/uPlot) and add ability to naturally scroll and zoom graphs. See [these docs](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#vmui). Thanks to @Loori-R.
* FEATURE: vmstorage: stop accepting new data if `-storageDataPath` directory contains less than `-storage.minFreeDiskSpaceBytes` of free space. This should prevent from `out of disk space` crashes. See [this feature request](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/269).
* FEATURE: calculate quantiles in the same way as Prometheus does in such functions as [quantile_over_time](https://docs.victoriametrics.com/victoriametrics/metricsql/#quantile_over_time) and [quantile](https://docs.victoriametrics.com/victoriametrics/metricsql/#quantile). Previously results from VictoriaMetrics could be slightly different than results from Prometheus. See [this](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/1625) and [this](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/1612) issues.
* FEATURE: add `rollup_scrape_interval(m[d])` function to [MetricsQL](https://docs.victoriametrics.com/victoriametrics/metricsql/), which returns `min`, `max` and `avg` values for the interval between samples for `m` on the given lookbehind window `d`.
* FEATURE: add `topk_last(k, q)` and `bottomk_last(k, q)` functions to [MetricsQL](https://docs.victoriametrics.com/victoriametrics/metricsql/), which return up to `k` time series from `q` with the maximum / minimum last value on the graph.

* BUGFIX: align behavior of the queries `a or on (labels) b`, `a and on (labels) b` and `a unless on (labels) b` where `b` has multiple time series with the given `labels` to Prometheus behavior. See [this pull request](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/1643).
* BUGFIX: vmagent: fix `openstack_sd_config` service discovery when both `domain_name` and `project_id` config options are set. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/1655).
* BUGFIX: return proper values (zeroes) from [stddev_over_time](https://docs.victoriametrics.com/victoriametrics/metricsql/#stddev_over_time) and [stdvar_over_time](https://docs.victoriametrics.com/victoriametrics/metricsql/#stdvar_over_time) functions when the lookbehind window in square brackets contains only a single sample. Previously the sample value was incorrectly returned in this case.
* BUGFIX: vminsert: fix uneven distribution of time series among storage nodes in [multi-level cluster setup](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/#multi-level-cluster-setup). See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/1672).


## [v1.66.2](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.66.2)

Released at 2021-09-23

* FEATURE: vmagent: add `vm_promscrape_max_scrape_size_exceeded_errors_total` metric for counting of the failed scrapes due to the exceeded response size (the response size limit can be configured via `-promscrape.maxScrapeSize` command-line flag). See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/1639).

* BUGFIX: vmalert: properly reload rule groups if only the `interval` config option is changed. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/1641).
* BUGFIX: properly handle `{__name__=~"prefix(suffix1|suffix2)",other_label="..."}` queries. They may return unexpected empty responses since v1.66.0. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/1644).


## [v1.66.1](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.66.1)

Released at 2021-09-22

* FEATURE: add `-cluster` and/or `-enterprise` suffixes to `short_version` label at `vm_app_version` metric exposed at `/metrics` page of every VictoriaMetrics component. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/1635).

* BUGFIX: vmselect: fix accessing [Graphite APIs](https://docs.victoriametrics.com/victoriametrics/integrations/graphite/#graphite-api-usage). The access has been broken in v1.66.0, because `/graphite/*` path prefix accidentally clashed with `/graph*` path prefix used for VictoriaMetrics UI (aka `vmui`).
* BUGFIX: fix parsing `regex: <bool_or_number>` in relabeling rules (for example, `regex: true` or `regex: 123`). The bug has been introduced in v1.66.0.
