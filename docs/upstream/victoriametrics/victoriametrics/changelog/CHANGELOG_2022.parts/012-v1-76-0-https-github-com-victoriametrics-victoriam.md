<!-- Part 12 of 13 of victoriametrics/changelog/CHANGELOG_2022.md (split because the page is big). -->

## [v1.76.0](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.76.0)

Released at 2022-04-07

**Update notes:** this release introduces backwards-incompatible changes to communication protocol between `vmselect` and `vmstorage` nodes in cluster version of VictoriaMetrics, so read requests to `vmselect` will fail until the upgrade is complete. These errors will stop after all the `vmselect` and `vmstorage` nodes are updated to the new release. It is safe to downgrade to previous releases.

* FEATURE: [vmctl](https://docs.victoriametrics.com/victoriametrics/vmctl/): add ability to verify files obtained via [native export](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#how-to-export-data-in-native-format). See [these docs](https://docs.victoriametrics.com/victoriametrics/vmctl/#verifying-exported-blocks-from-victoriametrics) and [this feature request](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/2362).
* FEATURE: [vmui](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#vmui): add pre-defined dashboards for per-job CPU usage, memory usage and disk IO usage. See [this pull request](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/2243) for details.
* FEATURE: [vmalert](https://docs.victoriametrics.com/victoriametrics/vmalert/): improve compatibility with [Prometheus Alert Generator specification](https://github.com/prometheus/compliance/blob/main/alert_generator/specification.md). See [this pull request](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/2340).
* FEATURE: [vmalert](https://docs.victoriametrics.com/victoriametrics/vmalert/): add `-datasource.disableKeepAlive` command-line flag, which can be used for disabling [HTTP keep-alive connections](https://en.wikipedia.org/wiki/HTTP_persistent_connection) to datasources. This option can be useful for distributing load among multiple datasources behind TCP proxy such as [HAProxy](http://www.haproxy.org/).
* FEATURE: [Cluster version of VictoriaMetrics](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): reduce memory usage by up to 50% for `vminsert` and `vmstorage` under high ingestion rate.
* FEATURE: [vmgateway](https://docs.victoriametrics.com/victoriametrics/vmgateway/): Allow to read `-ratelimit.config` file from URL. Also add `-ratelimit.configCheckInterval` command-line option. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/2241).
* FEATURE: add the following command-line flags, which can be used for fine-grained limiting of CPU and memory usage during various API calls:

  * `-search.maxFederateSeries` for limiting the number of time series, which can be returned from [/federate](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#federation).
  * `-search.maxExportSeries` for limiting the number of time series, which can be returned from [/api/v1/export](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#how-to-export-time-series).
  * `-search.maxSeries` for limiting the number of time series, which can be returned from [/api/v1/series](https://docs.victoriametrics.com/victoriametrics/url-examples/#apiv1series).
  * `-search.maxTSDBStatusSeries` for limiting the number of time series, which can be scanned during the request to [/api/v1/status/tsdb](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#tsdb-stats).
  * `-search.maxGraphiteSeries` for limiting the number of time series, which can be scanned during the request to [Graphite Render API](https://docs.victoriametrics.com/victoriametrics/integrations/graphite/#render-api).

Previously the `-search.maxUniqueTimeseries` command-line flag was used as a global limit for all these APIs. Now the `-search.maxUniqueTimeseries` is used only for limiting the number of time series, which can be scanned during requests to [/api/v1/query](https://docs.victoriametrics.com/victoriametrics/url-examples/#apiv1query) and [/api/v1/query_range](https://docs.victoriametrics.com/victoriametrics/url-examples/#apiv1query_range).

When using [cluster version of VictoriaMetrics](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/), these command-line flags (including `-search.maxUniqueTimeseries`) must be passed to `vmselect` instead of `vmstorage`.

* BUGFIX: [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/) and [vmauth](https://docs.victoriametrics.com/victoriametrics/vmauth/): reduce the probability of `TLS handshake error from XX.XX.XX.XX: EOF` errors when `-remoteWrite.url` points to HTTPS url at `vmauth`. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/1699).
* BUGFIX: return `Content-Type: text/html` response header when requesting `/` HTTP path at VictoriaMetrics components. Previously `text/plain` response header was returned, which could lead to broken page formatting. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/2323).
* BUGFIX: [Graphite Render API](https://docs.victoriametrics.com/victoriametrics/integrations/graphite/#render-api): accept floating-point values for [maxDataPoints](https://graphite.readthedocs.io/en/stable/render_api.html#maxdatapoints) query arg, since some clients send floating-point values instead of integer values for this arg.


## [v1.75.1](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.75.1)

Released at 2022-03-28

* BUGFIX: update base image for VictoriaMetrics from `alpine-3.15.0` to `alpine-3.15.2`. This fixes [CVE-2022-0778](https://nvd.nist.gov/vuln/detail/CVE-2022-0778). See [alpine 3.15.2 release docs](https://alpinelinux.org/posts/Alpine-3.15.2-released.html).


## [v1.75.0](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.75.0)

Released at 2022-03-18

**Update notes:** release contains breaking change to vmalert's API introduced in [ee396b5](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/2320/commits/ee396b5750d0bcb98233d624f88fa6cf92a8253b).
It replaces the `api/v1/groups` API handler with `api/v1/rules` handler in order to become compatible
with [alerts generator specification](https://github.com/prometheus/compliance/blob/main/alert_generator/specification.md).
See other changes introduced to vmalert [here](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/2320).

* FEATURE: [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): add support for mTLS communications between cluster components. See [these docs](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/#mtls-protection) and [this feature request](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/550).
* FEATURE: [vmalert](https://docs.victoriametrics.com/victoriametrics/vmalert/): add ability to use OAuth2 for `-datasource.url`, `-notifier.url` and `-remoteRead.url`. See the corresponding command-line flags containing `oauth2` in their names [here](https://docs.victoriametrics.com/victoriametrics/vmalert/#flags).
* FEATURE: [vmalert](https://docs.victoriametrics.com/victoriametrics/vmalert/): add ability to use Bearer Token for `-notifier.url` via `-notifier.bearerToken` and `-notifier.bearerTokenFile` command-line flags. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/1824).
* FEATURE: [vmalert](https://docs.victoriametrics.com/victoriametrics/vmalert/): add `sortByLabel` template function in order to be consistent with Prometheus. See [these docs](https://prometheus.io/docs/prometheus/latest/configuration/template_reference/#functions) for more details.
* FEATURE: [vmalert](https://docs.victoriametrics.com/victoriametrics/vmalert/): improve compliance with [Prometheus Alert Generator Specification](https://github.com/prometheus/compliance/blob/main/alert_generator/specification.md).
* FEATURE: [vmalert](https://docs.victoriametrics.com/victoriametrics/vmalert/): add `-rule.resendDelay` command-line flag, which specifies the minimum amount of time to wait before resending an alert to Alertmanager (e.g. this is equivalent to `-rules.alert.resend-delay` option from Prometheus. See [this feature request](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/1665).
* FEATURE: [vmauth](https://docs.victoriametrics.com/victoriametrics/vmauth/): transparently treat `Authorization: Token ...` request headers as `Authorization: Bearer ...` request headers. This allows sending requests to `vmauth` from InfluxDB clients. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/1897). Thanks to @dcircelli for the pull request.
* FEATURE: do not log trivial network errors such as `broken pipe` and `connection reset by peer`. This error could occur when writing data to the client, which closes the connection to VictoriaMetrics due to request timeout or similar reason. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/2334).

* BUGFIX: [Graphite Render API](https://docs.victoriametrics.com/victoriametrics/integrations/graphite/#render-api): return an additional point after `until` timestamp in the same way as Graphite does. Previously VictoriaMetrics didn't return this point, which could result in missing last point on the graph.
* BUGFIX: properly locate series with the given `name` and without the given `label` when using the `name{label=~"foo|"}` series selector. Previously such series could be skipped. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/2255). Thanks to @jduncan0000 for discovering and fixing the issue.
* BUGFIX: properly free up memory occupied by deleted cache entries for the following caches: `indexdb/dataBlocks`, `indexdb/indexBlocks`, `storage/indexBlocks`. This should reduce the increased memory usage starting from v1.73.0. See [this](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/2242) and [this](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/2007) issue.
* BUGFIX: reduce the interval for checking for free disk space from 30 seconds to 1 second. This should reduce the probability of `no space left on device` panics when `-storage.minFreeDiskSpaceBytes` is set to too low values. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/2305).
* BUGFIX: [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/): prevent from panic at vmagent when importing a time series with big number of samples. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/2335). Thanks to @bleedfish for discovering and fixing the issue.


## [v1.74.0](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.74.0)

Released at 2022-03-03

**Update notes:** In this release VictoriaMetrics may use some extra memory due to issues [#2242](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/2242) and [#2007](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/2007). These issues were addressed in [v1.75.0](#v1750), so we recommend updating straight to it.

* FEATURE: add support for conditional relabeling via `if` filter. The `if` filter can contain arbitrary [series selector](https://prometheus.io/docs/prometheus/latest/querying/basics/#time-series-selectors). For example, the following rule drops targets matching `foo{bar="baz"}` series selector:

```yaml
- action: drop
  if: 'foo{bar="baz"}'
```

This rule is equivalent to less clear traditional one:

```yaml
- action: drop
  source_labels: [__name__, bar]
  regex: 'foo;baz'
```

  See [relabeling docs](https://docs.victoriametrics.com/victoriametrics/relabeling/) and [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/1998) for more details.

* FEATURE: reduce memory usage for various caches under [high churn rate](https://docs.victoriametrics.com/victoriametrics/faq/#what-is-high-churn-rate).
* FEATURE: [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/): reuse Kafka client when pushing data from [many tenants](https://docs.victoriametrics.com/victoriametrics/vmagent/#multitenancy) to Kafka. Previously a separate Kafka client was created per each tenant. This could lead to increased load on Kafka. See [how to push data from vmagent to Kafka](https://docs.victoriametrics.com/victoriametrics/integrations/kafka/#writing-metrics).
* FEATURE: improve performance when registering new time series. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/2247). Thanks to @ahfuzhang .

* BUGFIX: return the proper number of datapoints from `moving*()` functions such as `movingAverage()` in [Graphite Render API](https://docs.victoriametrics.com/victoriametrics/integrations/graphite/#render-api). Previously these functions could return too big number of samples if [maxDataPoints query arg](https://graphite.readthedocs.io/en/stable/render_api.html#maxdatapoints) is explicitly passed to `/render` API.
* BUGFIX: properly handle [series selector](https://prometheus.io/docs/prometheus/latest/querying/basics/#time-series-selectors) containing a filter for multiple metric names plus a negative filter. For example, `{__name__=~"foo|bar",job!="baz"}` . Previously VictoriaMetrics could return series with `foo` or `bar` names and with `job="baz"`. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/2238).
* BUGFIX: [vmgateway](https://docs.victoriametrics.com/victoriametrics/vmgateway/): properly parse JWT tokens if they are encoded with [URL-safe base64 encoding](https://datatracker.ietf.org/doc/html/rfc4648#section-5).


## [v1.73.1](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.73.1)

Released at 2022-02-22

**Update notes:** In this release VictoriaMetrics may use some extra memory due to issues [#2242](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/2242) and [#2007](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/2007). These issues were addressed in [v1.75.0](#v1750), so we recommend updating straight to it.

* FEATURE: allow overriding default limits for the following in-memory caches, which usually occupy the most memory:
  * `storage/tsid` - the cache speeds up lookups of internal metric ids by `metric_name{labels...}` during data ingestion. The size for this cache can be tuned with `-storage.cacheSizeStorageTSID` command-line flag.
  * `indexdb/dataBlocks` - the cache speeds up data lookups in `<-storageDataPath>/indexdb` files. The size for this cache can be tuned with `-storage.cacheSizeIndexDBDataBlocks` command-line flag.
  * `indexdb/indexBlocks` - the cache speeds up index lookups in `<-storageDataPath>/indexdb` files. The size for this cache can be tuned with `-storage.cacheSizeIndexDBIndexBlocks` command-line flag.
  See also [cache tuning docs](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#cache-tuning). See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/1940).
* FEATURE: add `-influxDBLabel` command-line flag for overriding `db` label name for the data [imported into VictoriaMetrics via InfluxDB line protocol](https://docs.victoriametrics.com/victoriametrics/integrations/influxdb/#influxdb-compatible-agents-such-as-telegraf). Thanks to @johnatannvmd for [the pull request](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/2203).
* FEATURE: return `X-Influxdb-Version` HTTP header in responses to [InfluxDB write requests](https://docs.victoriametrics.com/victoriametrics/integrations/influxdb/#influxdb-compatible-agents-such-as-telegraf). This is needed for some InfluxDB clients. See [this comment](https://github.com/ntop/ntopng/issues/5449#issuecomment-1005347597) and [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/2209).

* BUGFIX: reduce memory usage during the first three hours after the upgrade from versions older than v1.73.0. The memory usage spike was related to the need of in-memory caches' re-population after the upgrade because of the fix for [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/1401). Now cache size limits are reduced in order to occupy less memory during the upgrade.
* BUGFIX: fix a bug, which could significantly slow down requests to `/api/v1/labels` and `/api/v1/label/<label_name>/values`. These APIs are used by Grafana for auto-completion of label names and label values. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/2200).
* BUGFIX: vmalert: add support for `$externalLabels` and `$externalURL` template vars in the same way as Prometheus does. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/2193).
* BUGFIX: vmalert: make sure notifiers are discovered during initialization if they are configured via `consul_sd_configs`. Previously they could be discovered in 30 seconds (the default value for `-promscrape.consulSDCheckInterval` command-line flag) after the initialization. See [this pull request](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/2202).
* BUGFIX: update default value for `-promscrape.fileSDCheckInterval`, so it matches default duration used by Prometheus for checking for updates in `file_sd_configs`. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/2187). Thanks to @corporate-gadfly for the fix.
* BUGFIX: [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): do not return partial responses from `vmselect` if at least a single `vmstorage` node was reachable and returned an app-level error. Such errors are usually related to cluster mis-configuration, so they must be returned to the caller instead of being masked by [partial responses](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/#cluster-availability). Partial responses can be returned only if some of `vmstorage` nodes are unreachable during the query. This may help the following issues: [one](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/1941), [two](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/678).
