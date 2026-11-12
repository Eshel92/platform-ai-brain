<!-- Part 7 of 7 of victoriametrics/changelog/CHANGELOG_2021.md (split because the page is big). -->

## [v1.53.0](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.53.0)

Released at 2021-02-03

* FEATURE: added [vmctl tool](https://docs.victoriametrics.com/victoriametrics/vmctl/) to VictoriaMetrics release process. Now it is packaged in `vmutils-*.tar.gz` archive on [the releases page](https://github.com/VictoriaMetrics/VictoriaMetrics/releases). Source code for `vmctl` tool has been moved from [github.com/VictoriaMetrics/vmctl](https://github.com/VictoriaMetrics/vmctl) to [github.com/VictoriaMetrics/VictoriaMetrics/app/vmctl](https://github.com/VictoriaMetrics/VictoriaMetrics/tree/master/app/vmctl).
* FEATURE: added `-loggerTimezone` command-line flag for adjusting time zone for timestamps in log messages. By default UTC is used.
* FEATURE: added `-search.maxStepForPointsAdjustment` command-line flag, which can be used for disabling adjustment for points returned by `/api/v1/query_range` handler if such points have timestamps closer than `-search.latencyOffset` to the current time. Such points may contain incomplete data, so they are substituted by the previous values for `step` query args smaller than one minute by default.
* FEATURE: vmselect: added ability to use Graphite-compatible filters in MetricsQL via `{__graphite__="foo.*.bar"}` syntax. This expression is equivalent to `{__name__=~"foo[.][^.]*[.]bar"}`, but it works faster and it is easier to use when migrating from Graphite to VictoriaMetrics. This feature deprecates the usage of `-search.treatDotsAsIsInRegexps` command-line flag.
* FEATURE: vmselect: added ability to set additional label filters, which must be applied during queries. Such label filters can be set via optional `extra_label` query arg, which is accepted by [querying API](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#prometheus-querying-api-usage) handlers. For example, the request to `/api/v1/query_range?extra_label=tenant_id=123&query=<query>` adds `{tenant_id="123"}` label filter to the given `<query>`. It is expected that the `extra_label` query arg is automatically set by auth proxy sitting
in front of VictoriaMetrics. [Contact us](mailto:sales@victoriametrics.com) if you need assistance with such a proxy. See <https://github.com/VictoriaMetrics/VictoriaMetrics/issues/1021> .
* FEATURE: vmalert: added `-datasource.queryStep` command-line flag for passing optional `step` query arg to `/api/v1/query` endpoint. See <https://github.com/VictoriaMetrics/VictoriaMetrics/issues/1025>
* FEATURE: vmalert: added ability to query Graphite datasource when evaluating alerting and recording rules. See [these docs](https://docs.victoriametrics.com/victoriametrics/vmalert/#graphite) for details.
* FEATURE: vmagent: added `-remoteWrite.roundDigits` command-line option for rounding metric values to the given number of decimal digits after the point before sending the metric to the corresponding `-remoteWrite.url`. This option can be used for improving data compression on the remote storage, because values with lower number of decimal digits can be compressed better than values with bigger number of decimal digits.
* FEATURE: vmagent: added `-remoteWrite.rateLimit` command-line flag for limiting data transfer rate to `-remoteWrite.url`. This may be useful when big amounts of buffered data is sent after temporarily unavailability of the remote storage. See <https://github.com/VictoriaMetrics/VictoriaMetrics/issues/1035>
* FEATURE: vmagent: export the following additional metrics, which may be useful during troubleshooting:
  * `vm_promscrape_scrapes_failed_per_url_total`
  * `vm_promscrape_scrapes_skipped_by_sample_limit_per_url_total`
  * `vm_promscrape_discovery_requests_total`
  * `vm_promscrape_discovery_retries_total`
  * `vm_promscrape_scrape_retries_total`
  * `vm_promscrape_service_discovery_duration_seconds`
* FEATURE: vmselect: initial implementation for [Graphite Render API](https://docs.victoriametrics.com/victoriametrics/integrations/graphite/#render-api).

* BUGFIX: vmagent: reduce HTTP reconnection rate for scrape targets. Previously vmagent could erroneously close HTTP keep-alive connections more frequently than needed.
* BUGFIX: vmagent: retry scrape and service discovery requests when the remote server closes HTTP keep-alive connection. Previously `disable_keepalive: true` option could be used under `scrape_configs` section when working with such servers.


## [v1.52.0](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.52.0)

Released at 2021-01-13

* FEATURE: provide a sample list of alerting rules for VictoriaMetrics components. It is available [here](https://github.com/VictoriaMetrics/VictoriaMetrics/tree/master/deployment/docker#alerts).
* FEATURE: disable final merge for data for the previous month at the beginning of new month, since it may result in high disk IO and CPU usage. Final merge can be enabled by setting `-finalMergeDelay` command-line flag to positive duration.
* FEATURE: add `tfirst_over_time(m[d])` and `tlast_over_time(m[d])` functions to [MetricsQL](https://docs.victoriametrics.com/victoriametrics/metricsql/) for returning timestamps for the first and the last data point in `m` over `d` duration.
* FEATURE: add ability to pass multiple labels to `sort_by_label()` and `sort_by_label_desc()` functions. See <https://github.com/VictoriaMetrics/VictoriaMetrics/issues/992> .
* FEATURE: enforce at least TLS v1.2 when accepting HTTPS requests if `-tls`, `-tlsCertFile` and `-tlsKeyFile` command-line flags are set, because older TLS protocols such as v1.0 and v1.1 have been deprecated due to security vulnerabilities.
* FEATURE: support `extra_label` query arg for all HTTP-based [data ingestion protocols](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#how-to-import-time-series-data). This query arg can be used for specifying extra labels which should be added for the ingested data.
* FEATURE: vmbackup: increase backup chunk size from 128MB to 1GB. This should reduce the number of Object storage API calls during backups by 8x. This may also reduce costs, since object storage API calls usually have non-zero costs. See <https://aws.amazon.com/s3/pricing/> and <https://cloud.google.com/storage/pricing#operation-charges> .

* BUGFIX: properly parse escaped unicode chars in MetricsQL metric names, label names and function names. See <https://github.com/VictoriaMetrics/VictoriaMetrics/issues/990>
* BUGFIX: override user-provided labels with labels set in `extra_label` query args during data ingestion over HTTP-based protocols.
* BUGFIX: vmagent: prevent from `dialing to the given TCP address time out` error when scraping big number of unavailable targets. See <https://github.com/VictoriaMetrics/VictoriaMetrics/issues/987>
* BUGFIX: vmagent: properly show scrape duration on `/targets` page. Previously it was incorrectly shown as 0.000s.
* BUGFIX: vmagent: properly log errors when `-promscrape.streamParse` command-line flag is set. See <https://github.com/VictoriaMetrics/VictoriaMetrics/pull/1009>
* BUGFIX: vmagent: properly suppress errors when both `-promscrape.suppressScrapeErrors` and `-promscrape.streamParse` command-line flags are set. See <https://github.com/VictoriaMetrics/VictoriaMetrics/pull/1009> .
* BUGFIX: vmalert: return non-empty result in template func `query` stub to pass validation. See <https://github.com/VictoriaMetrics/VictoriaMetrics/issues/989> .
* BUGFIX: upgrade base image for Docker packages from Alpine 3.12.1 to Alpine 3.12.3 in order to fix potential security issues. See <https://github.com/VictoriaMetrics/VictoriaMetrics/issues/1010>


## Previous releases

See changes for older releases [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2020/).
