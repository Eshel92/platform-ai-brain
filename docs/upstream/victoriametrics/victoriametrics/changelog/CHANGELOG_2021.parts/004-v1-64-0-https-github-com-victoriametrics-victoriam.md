<!-- Part 4 of 7 of victoriametrics/changelog/CHANGELOG_2021.md (split because the page is big). -->

## [v1.64.0](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.64.0)

Released at 2021-08-15

* FEATURE: add support for Prometheus staleness markers. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/1526).
* FEATURE: vmagent: automatically generate Prometheus staleness markers for the scraped metrics when scrape targets disappear in the same way as Prometheus does. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/1526).
* FEATURE: add `present_over_time(m[d])` function, which returns 1 if `m` has a least a single sample over the previous duration `d`. This function has been added also to [Prometheus 2.29](https://github.com/prometheus/prometheus/releases/tag/v2.29.0).
* FEATURE: vmagent: support multitenant writes according to [these docs](https://docs.victoriametrics.com/victoriametrics/vmagent/#multitenancy). This allows using a single `vmagent` instance in front of VictoriaMetrics cluster for all the tenants. Thanks to @omarghader for [the pull request](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/1505). See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/1491).
* FEATURE: vmagent: add `__meta_ec2_availability_zone_id` label to discovered Amazon EC2 targets. This label is available in Prometheus [starting from v2.29](https://github.com/prometheus/prometheus/releases/tag/v2.29.0).
* FEATURE: vmagent: add `__meta_gce_interface_ipv4_<name>` labels to discovered GCE targets. These labels are available in Prometheus [starting from v2.29](https://github.com/prometheus/prometheus/releases/tag/v2.29.0).
* FEATURE: add `-search.maxSamplesPerSeries` command-line flag for limiting the number of raw samples a single query can process per each time series. This option can protect from out of memory errors when a query processes tens of millions of raw samples per series. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/1067).
* FEATURE: add `-search.maxSamplesPerQuery` command-line flag for limiting the number of raw samples a single query can process across all the time series. This option can protect from heavy queries, which select too big number of raw samples. Thanks to @jiangxinlingdu for [the initial pull request](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/1478).
* FEATURE: improve performance for queries that process big number of time series and/or samples on systems with big number of CPU cores.
* FEATURE: vmalert: expose `vmalert_alerting_rules_last_evaluation_samples` and `vmalert_recording_rules_last_evaluation_samples` metrics. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/1494).
* FEATURE: vminsert: expose `vm_rpc_send_duration_seconds_total` counter, which can be used for determining high saturation of every `vminsert -> vmstorage` link with an alerting query `rate(vm_rpc_send_duration_seconds_total) > 0.9s`. This query triggers when the link is saturated by more than 90%. This usually means that more `vminsert` or `vmstorage` nodes must be added to the cluster in order to increase the total number of `vminsert -> vmstorage` links.
* FEATURE: vmagent: expose `vmagent_remotewrite_send_duration_seconds_total` counter, which can be used for determining high saturation of every connection to remote storage with an alerting query `rate(vmagent_remotewrite_send_duration_seconds_total) > 0.9s`. This query triggers when a connection is saturated by more than 90%. This usually means that `-remoteWrite.queues` command-line flag must be increased in order to increase the number of connections per each remote storage.
* FEATURE: vmui: automatically fill Server URL field. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/1506).

* BUGFIX: fix corner cases for queries on time ranges exceeding 40 days. Previously some series can be missing in query results. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/1486).
* BUGFIX: vmselect: return dummy response at `/rules` page in the same way as for `/api/v1/rules` page. The `/rules` page is requested by Grafana 8. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/1493) for details.
* BUGFIX: vmbackup: automatically set default `us-east-1` S3 region if it is missing. This should simplify using S3-compatible services such as MinIO for backups. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/1449).
* BUGFIX: vmselect: prevent from possible deadlock when multiple `target` query args are passed to [Graphite Render API](https://docs.victoriametrics.com/victoriametrics/integrations/graphite/#render-api).
* BUGFIX: return series with `a op b` labels and `N` values for `(a op b) default N` if `(a op b)` returns series with all NaN values. Previously such series were removed.
* BUGFIX: vmui: fix layout when the query selects more than 27 time series. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/1497).
* BUGFIX: vmagent: restore highlighting in red for DOWN targets at `/targets` page. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/1461).


## [v1.63.0](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.63.0)

Released at 2021-07-15

* FEATURE: reduce memory usage by up to 30% on production workloads.
* FEATURE: vmselect: embed [vmui](https://github.com/VictoriaMetrics/vmui) into a single-node VictoriaMetrics and into `vmselect` component of cluster version. See [this feature request](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/1413). The web interface is available at the following paths:
  * `/vmui/` for a single-node VictoriaMetrics
  * `/select/<accountID>/vmui/` for `vmselect` at cluster version of VictoriaMetrics
* FEATURE: support durations anywhere in [MetricsQL queries](https://docs.victoriametrics.com/victoriametrics/metricsql/). For example, `sum_over_time(m[1h]) / 1h` is a valid query, which is equivalent to `sum_over_time(m[1h]) / 3600`.
* FEATURE: support durations without suffixes in [MetricsQL queries](https://docs.victoriametrics.com/victoriametrics/metricsql/). For example, `rate(m[3600])` is a valid query, which is equivalent to `rate(m[1h])`.
* FEATURE: export `vmselect_request_duration_seconds` and `vminsert_request_duration_seconds` [VictoriaMetrics histograms](https://valyala.medium.com/improving-histogram-usability-for-prometheus-and-grafana-bc7e5df0e350) at `/metrics` page. These histograms can be used for determining latency distribution and SLI/SLO for the served requests. For example, the following query would return the percent of queries that took less than 500ms during the last hour: `histogram_share(500ms, sum(rate(vmselect_request_duration_seconds_bucket[1h])) by (vmrange))`.
* FEATURE: vmagent: dynamically reload client TLS certificates from disk on every [mTLS connection](https://developers.cloudflare.com/cloudflare-one/access-controls/service-credentials/mutual-tls-authentication/). This should allow using `vmagent` with [Istio service mesh](https://istio.io/latest/about/service-mesh/). See [this feature request](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/1420).
* FEATURE: log http request path plus all the query args on errors during request processing. Previously only http request path was logged without query args, so it could be hard debugging such errors.
* FEATURE: add `is_set` label to `flag` metrics. This allows determining explicitly set command-line flags with the query `flag{is_set="true"}`.
* FEATURE: add ability to remove caches stored inside `<-storageDataPath>/cache` on startup if `reset_cache_on_startup` file is present there. See [this feature request](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/1447).

* BUGFIX: vmagent: remove `{ %space %}` typo in `/targets` output. The typo has been introduced in v1.62.0. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/1408).
* BUGFIX: vmagent: fix CSS styles on `/targets` page. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/1422).
* BUGFIX: vmalert: accept Prometheus-like durations in `interval` config option inside `group` section. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/1444).
* BUGFIX: properly update `vm_merge_need_free_disk_space` metric at `/metrics` page when there is no enough free disk space for performing optimal merges. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/1373).


## [v1.62.0](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.62.0)

Released at 2021-06-25

* FEATURE: vmagent: add service discovery for Docker (aka [docker_sd_config](https://docs.victoriametrics.com/victoriametrics/sd_configs/#docker_sd_configs)). See [this pull request](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/1402).
* FEATURE: vmagent: add service discovery for DigitalOcean (aka [digitalocean_sd_config](https://docs.victoriametrics.com/victoriametrics/sd_configs/#digitalocean_sd_configs)). See [this feature request](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/1367).
* FEATURE: vmagent: change the default value for `-remoteWrite.queues` from 4 to `2 * numCPUs`. This should reduce scrape duration for highly loaded vmagent, which scrapes tens of thousands of targets. See [this pull request](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/1385).
* FEATURE: vmagent: show the number of samples the target returns during the last scrape on `/targets` and `/api/v1/targets` pages. This should simplify debugging targets, which may return too big or too low number of samples. See [this feature request](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/1377).
* FEATURE: vmagent: show jobs with zero discovered targets on `/targets` page. This should help debugging improperly configured scrape configs.
* FEATURE: vmagent: support for http-based service discovery (aka [http_sd_config](https://docs.victoriametrics.com/victoriametrics/sd_configs/#http_sd_configs)), which has been added since Prometheus 2.28. See [this feature request](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/1392).
* FEATURE: vmagent: support namespace in Consul service discovery in the same way as Prometheus 2.28 does. See [this issue](https://github.com/prometheus/prometheus/issues/8894) for details.
* FEATURE: vmagent: support generic auth configs in `consul_sd_configs` in the same way as Prometheus 2.28 does. See [this issue](https://github.com/prometheus/prometheus/issues/8924) for details.
* FEATURE: [vmctl](https://docs.victoriametrics.com/victoriametrics/vmctl/): limit the number of samples per each imported JSON line. This should limit the memory usage at VictoriaMetrics side when importing time series with big number of samples.
* FEATURE: vmselect: log slow queries across all the `/api/v1/*` handlers (aka [Prometheus query API](https://prometheus.io/docs/prometheus/latest/querying/api)) if their execution duration exceeds `-search.logSlowQueryDuration`. This should simplify debugging slow requests to such handlers as `/api/v1/labels` or `/api/v1/series` additionally to `/api/v1/query` and `/api/v1/query_range`, which were logged in the previous releases.
* FEATURE: vminsert: sort the `-storageNode` list in order to guarantee the identical `series -> vmstorage` mapping across all the `vminsert` nodes. This should reduce resource usage (RAM, CPU and disk IO) at `vmstorage` nodes if `vmstorage` addresses are passed in random order to `vminsert` nodes.
* FEATURE: vmstorage: reduce memory usage on a system with many CPU cores under high ingestion rate.

* BUGFIX: prevent from adding new samples to deleted time series after the rotation of the inverted index (the rotation is performed once per `-retentionPeriod`). See [this comment](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/1347#issuecomment-861232136) for details.
* BUGFIX: vmstorage: reduce high disk write IO usage on systems with big number of CPU cores. The issue has been introduced in the release [v1.59.0](#v1590). See [this commit](https://github.com/VictoriaMetrics/VictoriaMetrics/commit/aa9b56a046b6ae8083fa659df35dd5e994bf9115) and [this comment](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/1338#issuecomment-863046999) for details.
* BUGFIX: vmstorage: prevent from incorrect stats collection when multiple concurrent queries execute the same tag filter. This may help reducing CPU usage under certain workloads. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/1338).
* BUGFIX: vmselect: return the last timestamp for the max / min value from `tmax_over_time(m[d])` and `tmin_over_time(m[d])` [MetricsQL functions](https://docs.victoriametrics.com/victoriametrics/metricsql/) as most users expect. See also [this issue](https://github.com/prometheus/prometheus/issues/8966).
* BUGFIX: vmselect: return the expected value for `increase_pure()` [MetricsQL function](https://docs.victoriametrics.com/victoriametrics/metricsql/) after a gap in a time series. Previously incorrect too big value could be returned after the gap from `increase_pure()`.


## [v1.61.1](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.61.1)

Released at 2021-06-11

* BUGFIX: vmalert: fix recording rules, which were broken in v1.61.0. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/1369).
* BUGFIX: reset the on-disk cache for mapping from the full metric name to an internal metric id (e.g. `metric_name{labels} -> internal_metric_id`) after deleting metrics via [delete API](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#how-to-delete-time-series). This should prevent from possible inconsistent state after unclean shutdown. This [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/1347).


## [v1.61.0](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.61.0)

Released at 2021-06-09

* FEATURE: vmalert: add support for backfilling (aka replay) of recording and alerting rules. See [these docs](https://docs.victoriametrics.com/victoriametrics/vmalert/#rules-backfilling) and [this feature request](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/836).
* FEATURE: vmalert: add a command-line flag `-rule.configCheckInterval` for automatic re-reading of `-rule` files without the need to send SIGHUP signal. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/512).
* FEATURE: vmagent: respect the `sample_limit` and `-promscrape.maxScrapeSize` values when scraping targets in [stream parsing mode](https://docs.victoriametrics.com/victoriametrics/vmagent/#stream-parsing-mode). See [this pull request](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/1331).
* FEATURE: vmauth: add ability to specify multiple `url_prefix` entries for balancing the load among multiple `vmselect` and/or `vminsert` nodes in a cluster. See [these docs](https://docs.victoriametrics.com/victoriametrics/vmauth/#load-balancing).
* FEATURE: vminsert: add `-disableRerouting` command-line flag for forcibly disabling the rerouting. This should help resolving [this](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/791) and [this](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/1054) issues.
* FEATURE: vminsert: reduce the probability of global re-routing storm if all the vmstorage nodes cannot keep up with the given ingestion rate for some time. This should improve cluster stability in such cases. See [this](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/791) and [this](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/1054) issues.
* FEATURE: allow building VictoriaMetrics components for Solaris / SmartOS. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/1322).
* FEATURE: vmagent: add ability to debug relabeling rules. See [these docs](https://docs.victoriametrics.com/victoriametrics/relabeling/) and [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/1343).

* BUGFIX: reduce CPU usage by up to 2x during querying a database with big number of active daily time series. The issue has been introduced in `v1.59.0`.
* BUGFIX: vmagent: properly apply auth and tls configs in `eureka_sd_configs`. See [this pull request](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/1350).
* BUGFIX: vmauth: do not panic on aborted http requests. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/1353).
* BUGFIX: properly generate `target` property for `*Series(foo.*.bar)` responses returned from [Graphite Render API](https://docs.victoriametrics.com/victoriametrics/integrations/graphite/#render-api). Previously the `target` contained the expanded list of series for `foo.*.bar`, e.g. `sumSeries(foo.a.bar,foo.b.bar,...foo.z.bar)`. Now VictoriaMetrics returns `sumSeries(foo.*.bar)` as a target in the same way as Graphite does.
