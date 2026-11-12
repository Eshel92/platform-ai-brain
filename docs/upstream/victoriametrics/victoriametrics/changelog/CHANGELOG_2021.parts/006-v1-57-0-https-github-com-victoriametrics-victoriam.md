<!-- Part 6 of 7 of victoriametrics/changelog/CHANGELOG_2021.md (split because the page is big). -->

## [v1.57.0](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.57.0)

Released at 2021-03-29

* FEATURE: optimize query performance by up to 10x on systems with many CPU cores. See [this tweet](https://twitter.com/MetricsVictoria/status/1375064484860067840).
* FEATURE: add the following metrics at `/metrics` page for every VictoriaMetrics app:
  * `process_resident_memory_anon_bytes` - RSS share for memory allocated by the process itself.  This share cannot be freed by the OS, so it must be taken into account by OOM killer.
  * `process_resident_memory_file_bytes` - RSS share for page cache memory (aka memory-mapped files). This share can be freed by the OS at any time, so it must be ignored by OOM killer.
  * `process_resident_memory_shared_bytes` - RSS share for memory shared with other processes (aka shared memory). This share can be freed by the OS at any time, so it must be ignored by OOM killer.
  * `process_resident_memory_peak_bytes` - peak RSS usage for the process.
  * `process_virtual_memory_peak_bytes` - peak virtual memory usage for the process.
* FEATURE: accept and enforce `extra_label=<label_name>=<label_value>` query arg at [Graphite APIs](https://docs.victoriametrics.com/victoriametrics/integrations/graphite/#graphite-api-usage).
* FEATURE: use InfluxDB field as metric name if measurement is empty and `-influxSkipSingleField` command-line is set. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/1139).
* FEATURE: vmagent: add `-promscrape.consul.waitTime` command-line flag for tuning the maximum wait time for Consul service discovery. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/1144).
* FEATURE: vmagent: add `vm_promscrape_discovery_kubernetes_stale_resource_versions_total` metric for monitoring the frequency of `too old resource version` errors during Kubernetes service discovery.
* FEATURE: single-node VictoriaMetrics: log metrics with timestamps older than `-search.cacheTimestampOffset` compared to the current time. See [these docs](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#backfilling) for details.

* BUGFIX: prevent from infinite loop on `{__graphite__="..."}` filters when a metric name contains `*`, `{` or `[` chars.
* BUGFIX: prevent from infinite loop in `/metrics/find` and `/metrics/expand` [Graphite Metrics API handlers](https://docs.victoriametrics.com/victoriametrics/integrations/graphite/#metrics-api) when they match metric names or labels with `*`, `{` or `[` chars.
* BUGFIX: do not merge duplicate time series during requests to `/api/v1/query`. See <https://github.com/VictoriaMetrics/VictoriaMetrics/issues/1141>
* BUGFIX: vmagent: properly handle `too old resource version` error messages from Kubernetes watch API. See <https://github.com/VictoriaMetrics/VictoriaMetrics/issues/1150>
* BUGFIX: vmagent: do not retry sending data blocks if remote storage returns `400 Bad Request` error. The number of dropped blocks due to such errors can be monitored with `vmagent_remotewrite_packets_dropped_total` metrics. See <https://github.com/VictoriaMetrics/VictoriaMetrics/issues/1149>
* BUGFIX: properly calculate `summarize` and `*Series` functions in [Graphite Render API](https://docs.victoriametrics.com/victoriametrics/integrations/graphite/#render-api).


## [v1.56.0](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.56.0)

Released at 2021-03-17

* FEATURE: add the following functions to [MetricsQL](https://docs.victoriametrics.com/victoriametrics/metricsql/):
  * `histogram_avg(buckets)` - returns the average value for the given buckets.
  * `histogram_stdvar(buckets)` - returns standard variance for the given buckets.
  * `histogram_stddev(buckets)` - returns standard deviation for the given buckets.
* FEATURE: export `vm_available_memory_bytes` and `vm_available_cpu_cores` metrics, which show the number of available RAM and available CPU cores for VictoriaMetrics apps.
* FEATURE: export `vm_index_search_duration_seconds` histogram, which can be used for troubleshooting time series search performance.
* FEATURE: vmagent: add ability to replicate scrape targets among `vmagent` instances in the cluster with `-promscrape.cluster.replicationFactor` command-line flag. See [these docs](https://docs.victoriametrics.com/victoriametrics/vmagent/#scraping-big-number-of-targets).
* FEATURE: vmagent: accept `scrape_offset` option at `scrape_config`. This option may be useful when scrapes must start at the specified offset of every scrape interval. See [these docs](https://docs.victoriametrics.com/victoriametrics/vmagent/#troubleshooting) for details.
* FEATURE: vmagent: support `proxy_tls_config`, `proxy_basic_auth`, `proxy_bearer_token` and `proxy_bearer_token_file` options at `scrape_config` section for configuring proxies specified via `proxy_url`. See [these docs](https://docs.victoriametrics.com/victoriametrics/vmagent/#scraping-targets-via-a-proxy).
* FEATURE: vmauth: allow using regexp paths in `url_map`. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/1112) for details.
* FEATURE: accept `round_digits` query arg at `/api/v1/query` and `/api/v1/query_range` handlers. This option can be set at Prometheus datasource in Grafana for limiting the number of digits after the decimal point in response values.
* FEATURE: add `-influx.databaseNames` command-line flag, which can be used for accepting data from some Telegraf plugins such as [fluentd plugin](https://github.com/fangli/fluent-plugin-influxdb). See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/1124).
* FEATURE: add `-logNewSeries` command-line flag, which can be used for debugging the source of time series churn rate.
* FEATURE: publish Windows builds for [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/), [vmalert](https://docs.victoriametrics.com/victoriametrics/vmalert/), [vmauth](https://docs.victoriametrics.com/victoriametrics/vmauth/) and [vmctl](https://docs.victoriametrics.com/victoriametrics/vmctl/) at `vmutils-windows-*.zip` archives at [releases page](https://github.com/VictoriaMetrics/VictoriaMetrics/releases).
* FEATURE: listen for IPv6 UDP if `-enableTCP6` command-line flag is passed to VictoriaMetrics. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/1131).

* BUGFIX: vmagent: prevent from high CPU usage bug during failing scrapes with small `scrape_timeout` (less than a few seconds).
* BUGFIX: vmagent: reduce memory usage when Kubernetes service discovery is used in big number of distinct scrape config jobs by sharing Kubernetes object cache. See <https://github.com/VictoriaMetrics/VictoriaMetrics/issues/1113>
* BUGFIX: vmagent: apply `sample_limit` only after `metric_relabel_configs` are applied as Prometheus does. Previously the `sample_limit` was applied before metrics relabeling.
* BUGFIX: vmagent: properly apply `tls_config`, `basic_auth` and `bearer_token` to proxy connections if `proxy_url` option is set. See <https://github.com/VictoriaMetrics/VictoriaMetrics/issues/1116>
* BUGFIX: vmagent: properly scrape targets via https proxy specified in `proxy_url` if `insecure_skip_verify` flag isn't set in `tls_config` section. See <https://github.com/VictoriaMetrics/VictoriaMetrics/issues/1116>
* BUGFIX: avoid `duplicate time series` error if `prometheus_buckets()` covers a time range with distinct set of buckets.
* BUGFIX: prevent exponent overflow when processing extremely small values close to zero such as `2.964393875E-314`. See <https://github.com/VictoriaMetrics/VictoriaMetrics/issues/1114>
* BUGFIX: do not include datapoints with a timestamp `t-d` when returning results from `/api/v1/query?query=m[d]&time=t` as Prometheus does.
* BUGFIX: do not crash if a query contains `histogram_over_time()` function name with uppercase chars. For example, `Histogram_Over_Time(m[5m])`.


## [v1.55.1](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.55.1)

Released at 2021-03-03

* BUGFIX: vmagent: fix a panic in Kubernetes service discovery when a target is filtered out with relabeling. See <https://github.com/VictoriaMetrics/VictoriaMetrics/issues/1107>
* BUGFIX: vmagent: fix Kubernetes service discovery for `role: ingress`. See <https://github.com/VictoriaMetrics/VictoriaMetrics/pull/1110>


## [v1.55.0](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.55.0)

Released at 2021-03-02

* FEATURE: add `sign(q)` and `clamp(q, min, max)` functions, which are planned to be added in [the upcoming Prometheus release](https://twitter.com/roidelapluie/status/1363428376162295811) . The `last_over_time(m[d])` function is already supported in [MetricsQL](https://docs.victoriametrics.com/victoriametrics/metricsql/).
* FEATURE: vmagent: add `scrape_align_interval` config option, which can be used for aligning scrapes to the beginning of the configured interval. See [these docs](https://docs.victoriametrics.com/victoriametrics/vmagent/#troubleshooting) for details.
* FEATURE: expose io-related metrics at `/metrics` page for every VictoriaMetrics component:
  * `process_io_read_bytes_total` - the number of bytes read via io syscalls such as read and pread
  * `process_io_written_bytes_total` - the number of bytes written via io syscalls such as write and pwrite
  * `process_io_read_syscalls_total` - the number of read syscalls such as read and pread
  * `process_io_write_syscalls_total` - the number of write syscalls such as write and pwrite
  * `process_io_storage_read_bytes_total` - the number of bytes read from storage layer
  * `process_io_storage_written_bytes_total` - the number of bytes written to storage layer
* FEATURE: vmagent: add ability to spread scrape targets among multiple `vmagent` instances. See [these docs](https://docs.victoriametrics.com/victoriametrics/vmagent/#scraping-big-number-of-targets) and [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/1084) for details.
* FEATURE: vmagent: use watch API for Kubernetes service discovery. This should reduce load on Kubernetes API server when it tracks big number of objects (for example, 10K pods). This should also reduce the time needed for k8s targets discovery. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/1057) for details.
* FEATURE: vmagent: export `vm_promscrape_target_relabel_duration_seconds` metric, which can be used for monitoring the time spend on relabeling for discovered targets.
* FEATURE: vmagent: optimize [relabeling](https://docs.victoriametrics.com/victoriametrics/relabeling/) performance for common cases.
* FEATURE: add `increase_pure(m[d])` function to MetricsQL. It works the same as `increase(m[d])` except of various edge cases. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/962) for details.
* FEATURE: increase accuracy for `buckets_limit(limit, buckets)` results for small `limit` values. See [MetricsQL docs](https://docs.victoriametrics.com/victoriametrics/metricsql/) for details.
* FEATURE: vmagent: initial support for Windows build with `CGO_ENABLED=0 GOOS=windows go build ./app/vmagent`. See [this](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/70) and [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/1036).
* FEATURE: vmagent: support WebIdentityToken auth in EC2 service discovery. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/1080) for details.
* FEATURE: vmalert: properly process query params in `-datasource.url` and `-remoteRead.url` command-line flags. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/1087) for details.

* BUGFIX: vmagent: properly apply `-remoteWrite.rateLimit` when `-remoteWrite.queues` is greater than 1. Previously there was a data race, which could prevent from proper rate limiting.
* BUGFIX: vmagent: properly perform graceful shutdown on `SIGINT` and `SIGTERM` signals. The graceful shutdown has been broken in `v1.54.0`. See <https://github.com/VictoriaMetrics/VictoriaMetrics/issues/1065>
* BUGFIX: reduce the probability of `duplicate time series` errors when querying Kubernetes metrics.
* BUGFIX: properly calculate `histogram_quantile()` over time series with only a single non-zero bucket with `{le="+Inf"}`. Previously `NaN` was returned, now the value for the last bucket before `{le="+Inf"}` is returned like Prometheus does.
* BUGFIX: vmselect: do not cache partial query results on timeout when receiving data from `vmstorage` nodes. See <https://github.com/VictoriaMetrics/VictoriaMetrics/pull/1085>
* BUGFIX: properly handle `stale NFS file handle` error.
* BUGFIX: properly cache query results when `extra_label` query arg is used. Previously the cached results could clash for different `extra_label` values. See <https://github.com/VictoriaMetrics/VictoriaMetrics/pull/1095>
* BUGFIX: fix `http: superfluous response.WriteHeader call` issue. See <https://github.com/VictoriaMetrics/VictoriaMetrics/issues/1078>
* BUGFIX: fix arm64 builds due to the issue in `github.com/golang/snappy`. See <https://github.com/VictoriaMetrics/VictoriaMetrics/issues/1074>
* BUGFIX: fix `index out of range [1024819115206086200] with length 27` panic, which could occur when `1e-9` value is passed to VictoriaMetrics histogram. See <https://github.com/VictoriaMetrics/VictoriaMetrics/issues/1096>
* BUGFIX: fix parsing for Graphite line with empty tags such as `foo; 123 456`. See <https://github.com/VictoriaMetrics/VictoriaMetrics/issues/1100>
* BUGFIX: unescape only `\\`, `\n` and `\"` in label names when parsing Prometheus text exposition format as Prometheus does. Previously other escape sequences could be improperly unescaped.


## [v1.54.1](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.54.1)

Released at 2021-08-18

* BUGFIX: properly handle queries containing a filter on metric name plus any number of negative filters and zero non-negative filters. For example, `node_cpu_seconds_total{mode!="idle"}`. The bug was introduced in [v1.54.0](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.54.0).


## [v1.54.0](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.54.0)

Released at 2021-02-18

* FEATURE: optimize searching for matching metrics for `metric{<label_filters>}` queries if `<label_filters>` contains at least a single filter. For example, the query `up{job="foobar"}` should find the matching time series much faster than previously.
* FEATURE: reduce execution times for `q1 <binary_op> q2` queries by executing `q1` and `q2` in parallel.
* FEATURE: switch from Go1.15 to [Go1.16](https://golang.org/doc/go1.16) for building prod binaries.
* FEATURE: single-node VictoriaMetrics now accepts requests to handlers with `/prometheus` and `/graphite` prefixes such as `/prometheus/api/v1/query`. This improves compatibility with [handlers from VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/#url-format).
* FEATURE: expose `process_open_fds` and `process_max_fds` metrics. These metrics can be used for alerting when `process_open_fds` reaches `process_max_fds`. See <https://github.com/VictoriaMetrics/VictoriaMetrics/issues/402> and <https://github.com/VictoriaMetrics/VictoriaMetrics/issues/1037>
* FEATURE: vmalert: add `-datasource.appendTypePrefix` command-line option for querying both Prometheus and Graphite datasource in cluster version of VictoriaMetrics. See [these docs](https://docs.victoriametrics.com/victoriametrics/vmalert/#graphite) for details.
* FEATURE: vmauth: add ability to route requests from a single user to multiple destinations depending on the requested paths. See <https://github.com/VictoriaMetrics/VictoriaMetrics/issues/1064>
* FEATURE: remove dependency on external programs such as `cat`, `grep` and `cut` when detecting cpu and memory limits inside Docker or LXC container.
* FEATURE: vmagent: add `__meta_kubernetes_endpoints_label_*`, `__meta_kubernetes_endpoints_labelpresent_*`, `__meta_kubernetes_endpoints_annotation_*` and `__meta_kubernetes_endpoints_annotationpresent_*` labels for `role: endpoints` in Kubernetes service discovery. These labels where added in Prometheus 2.25.
* FEATURE: reduce the minimum supported retention period for inverted index (aka `indexdb`) from one month to one day. This should reduce disk space usage for `<-storageDataPath>/indexdb` folder if `-retentionPeriod` is set to values smaller than one month.
* FEATURE: vmselect: export per-tenant metrics `vm_vmselect_http_requests_total` and `vm_vmselect_http_requests_duration_ms_total` . Other per-tenant metrics are available as a part of [enterprise package](https://docs.victoriametrics.com/victoriametrics/enterprise/). See <https://github.com/VictoriaMetrics/VictoriaMetrics/issues/932> for details.

* BUGFIX: properly convert regexp tag filters containing escaped dots to non-regexp tag filters. For example, `{foo=~"bar\.baz"}` should be converted to `{foo="bar.baz"}`. Previously it was incorrectly converted to `{foo="bar\.baz"}`, which could result in missing time series for this tag filter.
* BUGFIX: do not spam error logs when discovering Docker Swarm targets without dedicated IP. See <https://github.com/VictoriaMetrics/VictoriaMetrics/issues/1028> .
* BUGFIX: properly embed timezone data into VictoriaMetrics apps. This should fix `-loggerTimezone` usage inside Docker containers.
* BUGFIX: properly build Docker images for non-amd64 architectures (arm, arm64, ppc64le, 386) on [Docker hub](https://hub.docker.com/u/victoriametrics/). Previously these images were incorrectly based on amd64 base image, so they didn't work.
* BUGFIX: vmagent: return back unsent block to the queue during graceful shutdown. Previously this block could be dropped if remote storage is unavailable during vmagent shutdown. See <https://github.com/VictoriaMetrics/VictoriaMetrics/issues/1065> .


## [v1.53.1](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.53.1)

Released at 2021-02-03

* BUGFIX: vmselect: fix the bug preventing from proper searching by Graphite filter with wildcards such as `{__graphite__="foo.*.bar"}`.
