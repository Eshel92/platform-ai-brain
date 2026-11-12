<!-- Part 5 of 7 of victoriametrics/changelog/CHANGELOG_2021.md (split because the page is big). -->

## [v1.60.0](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.60.0)

Released at 2021-05-24

* FEATURE: add ability to limit the number of unique time series, which can be added to storage per hour and per day. This can help dealing with high cardinality and high churn rate issues. See [these docs](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#cardinality-limiter).
* FEATURE: vmagent: add ability to limit the number of unique time series, which can be sent to remote storage systems per hour and per day. This can help dealing with high cardinality and high churn rate issues. See [these docs](https://docs.victoriametrics.com/victoriametrics/vmagent/#cardinality-limiter).
* FEATURE: vmalert: add ability to run alerting and recording rules for multiple tenants. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/740) and [these docs](https://docs.victoriametrics.com/victoriametrics/vmalert/#multitenancy).
* FEATURE: vminsert: add support for data ingestion via other `vminsert` nodes. This allows building multi-level data ingestion paths in VictoriaMetrics cluster by writing data from one level of `vminsert` nodes to another level of `vminsert` nodes. See [these docs](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/#multi-level-cluster-setup) and [this comment](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/541#issuecomment-835487858) for details.
* FEATURE: vmagent: reload `bearer_token_file`, `credentials_file` and `password_file` contents every second. This allows dynamically changing the contents of these files during target scraping and service discovery without the need to restart `vmagent`. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/1297).
* FEATURE: vmalert: add a flag to control behaviour on startup for state restore errors. Such errors were returned and logged before as well. Now user can specify whether to just log these errors (`-remoteRead.ignoreRestoreErrors=true`) or to stop the process (`-remoteRead.ignoreRestoreErrors=false`). The latter is important when VM isn't ready yet to serve queries from vmalert and it needs to wait. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/1252).
* FEATURE: vmalert: add ability to pass `round_digits` query arg to datasource via `-datasource.roundDigits` command-line flag. This can be used for limiting the number of decimal digits after the point in recording rule results. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/525).
* FEATURE: return `X-Server-Hostname` header in http responses of all the VictoriaMetrics components. This should simplify tracing the origin server behind a load balancer or behind auth proxy during troubleshooting.
* FEATURE: vmselect: allow to use 2x more memory for query processing at `vmselect` nodes in [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/). This should allow processing heavy queries without the need to increase RAM size at `vmselect` nodes.
* FEATURE: add ability to filter `/api/v1/status/tsdb` output with arbitrary [time series selectors](https://prometheus.io/docs/prometheus/latest/querying/basics/#time-series-selectors) passed via `match[]` query args. See [these docs](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#tsdb-stats) and [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/1168) for details.
* FEATURE: automatically detect memory and cpu limits for VictoriaMetrics components running under [cgroup v2](https://www.kernel.org/doc/html/latest/admin-guide/cgroup-v2.html) environments such as [HashiCorp Nomad](https://www.nomadproject.io/). See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/1269).
* FEATURE: vmauth: allow `-auth.config` reloading via `/-/reload` http endpoint. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/1194).
* FEATURE: add `timezone_offset(tz)` function. It returns offset in seconds for the given timezone `tz` relative to UTC. This can be useful when combining with datetime-related functions. For example, `day_of_week(time()+timezone_offset("America/Los_Angeles"))` would return weekdays for `America/Los_Angeles` time zone. Special `Local` time zone can be used for returning an offset for the time zone set on the host where VictoriaMetrics runs. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/1306) and [MetricsQL docs](https://docs.victoriametrics.com/victoriametrics/metricsql/) for more details.
* FEATURE: vmagent: add support for OAuth2 authorization for scrape targets and service discovery in the same way as Prometheus does. See [these docs](https://prometheus.io/docs/prometheus/latest/configuration/configuration/#oauth2).
* FEATURE: vmagent: add support for OAuth2 authorization when writing data to `-remoteWrite.url`. See `-remoteWrite.oauth2.*` config params in `/path/to/vmagent -help` output.
* FEATURE: vmalert: add ability to set `extra_filter_labels` at alerting and recording group configs. See [these docs](https://docs.victoriametrics.com/victoriametrics/vmalert/#groups).
* FEATURE: vmstorage: reduce memory usage by up to 30% when ingesting big number of active time series.

* BUGFIX: vmagent: do not retry scraping targets, which don't support HTTP. This should reduce CPU load and network usage at `vmagent` and at scrape target. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/1289).
* BUGFIX: vmagent: fix possible race when refreshing `role: endpoints` and `role: endpointslices` scrape targets in `kubernetes_sd_config`. Previously `pod` objects could be updated after the related `endpoints` object update. This could lead to missing scrape targets. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/1240).
* BUGFIX: vmagent: properly spread scrape targets among `vmagent` replicas if `-promscrape.cluster.replicationFactor` exceeds 1. See [this pull request](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/1292).
* BUGFIX: vmagent: limit `scrape_timeout` by `scrape_interval`. This guarantees that only a single sample is lost during the configured `scrape_interval` when scrape target responds slowly. See [this comment](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/1281#issuecomment-840538907) for details.
* BUGFIX: properly remove stale parts outside the configured retention if `-retentionPeriod` is smaller than one month. Previously stale parts could remain active for up to a month after they go outside the retention.
* BUGFIX: stop the process on panic errors, since such errors may leave the process in inconsistent state. Previously panics could be recovered, which could result in unexpected hard-to-debug further behavior of running process.
* BUGFIX: vminsert, vmagent: make sure data ingestion connections are closed before completing graceful shutdown. Previously the connection may remain open, which could result in trailing samples loss.
* BUGFIX: vmauth, vmalert: properly reuse HTTP keep-alive connections to backends and datasources. Previously only 2 keep-alive connections per backend could be reused. Other connections were closed after the first request. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/1300) for details.
* BUGFIX: vmalert: fix false positive error `result contains metrics with the same labelset after applying rule labels`, which could be triggered when recording rules generate unique metrics. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/1293).
* BUGFIX: vmctl: properly import InfluxDB rows if they have a field and a tag with identical names. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/1299).
* BUGFIX: properly reload configs if `SIGHUP` signal arrives during service initialization. Previously such `SIGHUP` signal could be ignored and configs weren't reloaded.
* BUGFIX: vmalert: properly import default rules from OpenShift. See [this issue](https://github.com/VictoriaMetrics/operator/issues/243).
* BUGFIX: reduce the probability of `the removal queue is full` panic when highly loaded VictoriaMetrics stores data on NFS. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/1313).


## [v1.59.0](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.59.0)

Released at 2021-05-01

* FEATURE: improved new time series registration speed on systems with many CPU cores. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/1244). Thanks to @waldoweng for the idea and [draft implementation](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/1243).
* FEATURE: vmalert: use the same technique as Grafana for determining evaluation timestamps for recording rules. This should make consistent graphs for series generated by recording rules compared to graphs generated for queries from recording rules in Grafana. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/1232).
* FEATURE: vmauth: add ability to set mandatory query args in `url_prefix`. For example, `url_prefix: http://vm:8428/?extra_label=team=dev` would add `extra_label=team=dev` query arg to all the incoming requests. See [the example](https://docs.victoriametrics.com/victoriametrics/vmauth/#auth-config) for more details.
* FEATURE: vmctl: add OpenTSDB migration option. See more details [here](https://docs.victoriametrics.com/victoriametrics/vmctl/opentsdb/).
Thanks to @johnseekins!
* FEATURE: log metrics with dropped labels if the number of labels in the ingested metric exceeds `-maxLabelsPerTimeseries`. This should simplify debugging for this case.
* FEATURE: vmagent: list user-visible endpoints at `http://vmagent:8429/`. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/1251).

* BUGFIX: vmagent: properly update `role: endpoints` and `role: endpointslices` scrape targets if the underlying service objects are updated in `kubernetes_sd_config`. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/1240).
* BUGFIX: vmagent: apply `scrape_timeout` on receiving the first response byte from `stream_parse: true` scrape targets. Previously it was applied to receiving and *processing* the full response stream. This could result in false timeout errors when scrape target exposes millions of metrics as described [here](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/1017#issuecomment-767235047).
* BUGFIX: vmagent: eliminate possible data race when obtaining value for the metric `vm_persistentqueue_bytes_pending`. The data race could result in incorrect value for this metric.
* BUGFIX: vmstorage: remove empty directories on startup. Such directories can be left after unclean shutdown on NFS storage. Previously such directories could lead to crashloop until manually removed. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/1142).


## [v1.58.0](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.58.0)

Released at 2021-04-08

* FEATURE: vminsert and vmagent: add `-sortLabels` command-line flag for sorting metric labels before pushing them to `vmstorage`. This should reduce the size of `MetricName -> internal_series_id` cache (aka `vm_cache_size_bytes{type="storage/tsid"}`) when ingesting samples for the same time series with distinct order of labels. For example, `foo{k1="v1",k2="v2"}` and `foo{k2="v2",k1="v1"}` represent a single time series. Labels sorting is disabled by default, since the majority of established exporters preserve the order of labels for the exported metrics.
* FEATURE: allow specifying label value alongside label name for the `others sum` time series returned from `topk_*` and `bottomk_*` functions from [MetricsQL](https://docs.victoriametrics.com/victoriametrics/metricsql/). For example, `topk_avg(3, max(process_resident_memory_bytes) by (instance), "instance=other_sum")` would return top 3 series from `max(process_resident_memory_bytes) by (instance)` plus a series containing the sum of other series. The `others sum` series will have `{instance="other_sum"}` label.
* FEATURE: do not delete `dst_label` when applying `label_copy(q, "src_label", "dst_label")` and `label_move(q, "src_label", "dst_label")` to series without `src_label` and with non-empty `dst_label`. See more details at [MetricsQL docs](https://docs.victoriametrics.com/victoriametrics/metricsql/).
* FEATURE: update Go builder from `v1.16.2` to `v1.16.3`. This should fix [these issues](https://github.com/golang/go/issues?q=milestone%3AGo1.16.3+label%3ACherryPickApproved).
* FEATURE: vmagent: add support for `follow_redirects` option to `scrape_configs` section in the same way as [Prometheus 2.26 does](https://github.com/prometheus/prometheus/pull/8546).
* FEATURE: vmagent: add support for `authorization` section in `-promscrape.config` in the same way as [Prometheus 2.26 does](https://github.com/prometheus/prometheus/pull/8512).
* FEATURE: vmagent: add support for socks5 proxy in `proxy_url` config option. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/1177).
* FEATURE: vmagent: add support for `socks5 over tls` proxy in `proxy_url` config option. It can be set up with the following config: `proxy_url: "tls+socks5://proxy-addr:port"`.
* FEATURE: vmagent: reduce memory usage when `-remoteWrite.queues` is set to a big value. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/1167).
* FEATURE: vmagent: add AWS IAM roles for tasks support for EC2 service discovery according to [these docs](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-iam-roles.html).
* FEATURE: vmagent: add support for `proxy_tls_config`, `proxy_authorization`, `proxy_basic_auth`, `proxy_bearer_token` and `proxy_bearer_token_file` options in `consul_sd_config`, `dockerswarm_sd_config` and `eureka_sd_config` sections.
* FEATURE: vmagent: pass `X-Prometheus-Scrape-Timeout-Seconds` header to scrape targets as Prometheus does. In this case scrape targets can limit the time needed for performing the scrape. See [this comment](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/1179#issuecomment-813118733) for details.
* FEATURE: vmagent: drop corrupted persistent queue files at `-remoteWrite.tmpDataPath` instead of throwing a fatal error. Corrupted files can appear after unclean shutdown of `vmagent` such as OOM kill or hardware reset. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/1030).
* FEATURE: vmauth: add support for authorization via [bearer token](https://swagger.io/docs/specification/authentication/bearer-authentication/). See [the docs](https://docs.victoriametrics.com/victoriametrics/vmauth/#auth-config) for details.
* FEATURE: publish `arm64` and `amd64` binaries for cluster version of VictoriaMetrics at [releases page](https://github.com/VictoriaMetrics/VictoriaMetrics/releases).

* BUGFIX: properly handle `/api/v1/labels` and `/api/v1/label/<label_name>/values` queries on big `start ... end` time range. This should fix big resource usage when VictoriaMetrics is queried with [Promxy](https://github.com/jacksontj/promxy) v0.0.62 or newer versions.
* BUGFIX: do not break sort order for series returned from `topk*`, `bottomk*` and `outliersk` [MetricsQL](https://docs.victoriametrics.com/victoriametrics/metricsql/) functions. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/1189).
* BUGFIX: vmagent: properly work with simple HTTP proxies which don't support `CONNECT` method. For example, [PushProx](https://github.com/prometheus-community/PushProx). See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/1179).
* BUGFIX: vmagent: properly discover targets if multiple namespace selectors are put inside `kubernetes_sd_config`. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/1170).
* BUGFIX: vmagent: properly discover `role: endpoints` and `role: endpointslices` targets in `kubernetes_sd_config`. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/1182).
* BUGFIX: properly generate filename for `*.tar.gz` archive inside `_checksums.txt` file posted at [releases page](https://github.com/VictoriaMetrics/VictoriaMetrics/releases). See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/1171).


## [v1.57.1](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.57.1)

Released at 2021-03-30

* FEATURE: publish vmutils for `GOOS=arm` on [releases page](https://github.com/VictoriaMetrics/VictoriaMetrics/releases).

* BUGFIX: prevent from possible incomplete query results after timed out query.
* BUGFIX: vmselect: remove `-search.storageTimeout` command-line flag, since it has the same meaning as `-search.maxQueryDuration`. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/711#issuecomment-808884995).
* BUGFIX: vminsert: return back `type` label to per-tenant metric `vm_tenant_inserted_rows_total`. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/932).
