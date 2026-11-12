<!-- Part 7 of 13 of victoriametrics/changelog/CHANGELOG_2022.md (split because the page is big). -->

## [v1.79.14](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.79.14)

Released at 2023-08-12

**v1.79.x is a line of [LTS releases](https://docs.victoriametrics.com/victoriametrics/lts-releases/). It contains important up-to-date bugfixes.
The v1.79.x line will be supported for at least 12 months since [v1.79.0](https://docs.victoriametrics.com/victoriametrics/changelog/#v1790) release**

* SECURITY: upgrade Go builder from Go1.20.4 to Go1.21.0.
* SECURITY: upgrade base docker image (Alpine) from 3.18.2 to 3.18.3. See [alpine 3.18.3 release notes](https://alpinelinux.org/posts/Alpine-3.15.10-3.16.7-3.17.5-3.18.3-released.html).

* BUGFIX: [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/): properly apply `if` filters during [relabeling](https://docs.victoriametrics.com/victoriametrics/relabeling/#relabeling-enhancements). Previously the `if` filter could improperly work. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/4806) and [this pull request](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/4816).
* BUGFIX: [vmalert](https://docs.victoriametrics.com/victoriametrics/vmalert/): Properly form path to static assets in WEB UI if `http.pathPrefix` set. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/4349).
* BUGFIX: [vmalert](https://docs.victoriametrics.com/victoriametrics/vmalert/): Properly set datasource query params. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/4340). Thanks to @gsakun for [the pull request](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/4341).
* BUGFIX: [vmalert](https://docs.victoriametrics.com/victoriametrics/vmalert/): properly return empty slices instead of nil for `/api/v1/rules` and `/api/v1/alerts` API handlers. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/4221).
* BUGFIX: [vmalert](https://docs.victoriametrics.com/victoriametrics/vmalert/): properly return empty slices instead of nil for `/api/v1/rules` for groups with present name but absent `rules`. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/4221).


## [v1.79.13](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.79.13)

Released at 2023-05-18

**v1.79.x is a line of [LTS releases](https://docs.victoriametrics.com/victoriametrics/lts-releases/). It contains important up-to-date bugfixes.
The v1.79.x line will be supported for at least 12 months since [v1.79.0](https://docs.victoriametrics.com/victoriametrics/changelog/#v1790) release**

* SECURITY: upgrade Go builder from Go1.20.3 to Go1.20.4. See [the list of issues addressed in Go1.20.4](https://github.com/golang/go/issues?q=milestone%3AGo1.20.4+label%3ACherryPickApproved).
* SECURITY: upgrade base docker image (alpine) from 3.17.3 to 3.18.0. See [alpine 3.18.0 release notes](https://www.alpinelinux.org/posts/Alpine-3.18.0-released.html).
* SECURITY: serve `/robots.txt` content to disallow indexing of the exposed instances by search engines. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/4128) for details.


## [v1.79.12](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.79.12)

Released at 2023-04-06

**v1.79.x is a line of [LTS releases](https://docs.victoriametrics.com/victoriametrics/lts-releases/). It contains important up-to-date bugfixes.
The v1.79.x line will be supported for at least 12 months since [v1.79.0](https://docs.victoriametrics.com/victoriametrics/changelog/#v1790) release**

* SECURITY: upgrade base docker image (alpine) from 3.17.2 to 3.17.3. See [alpine 3.17.3 release notes](https://alpinelinux.org/posts/Alpine-3.17.3-released.html).
* SECURITY: upgrade Go builder from Go1.20.2 to Go1.20.3. See [the list of issues addressed in Go1.20.3](https://github.com/golang/go/issues?q=milestone%3AGo1.20.3+label%3ACherryPickApproved).

* BUGFIX: [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/): fix CPU and memory usage spikes when files pointed by [file_sd_config](https://docs.victoriametrics.com/victoriametrics/sd_configs/#file_sd_configs) cannot be re-read. See [this_issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/3989).
* BUGFIX: prevent unexpected merges on start-up when `-storage.minFreeDiskSpaceBytes` is set. See [the issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/4023).
* BUGFIX: verify response code when fetching configuration files via HTTP. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/4034).


## [v1.79.11](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.79.11)

Released at 2023-03-12

**v1.79.x is a line of [LTS releases](https://docs.victoriametrics.com/victoriametrics/lts-releases/). It contains important up-to-date bugfixes.
The v1.79.x line will be supported for at least 12 months since [v1.79.0](https://docs.victoriametrics.com/victoriametrics/changelog/#v1790) release**

* SECURITY: upgrade Go builder from Go1.20.1 to Go1.20.2. See [the list of issues addressed in Go1.20.2](https://github.com/golang/go/issues?q=milestone%3AGo1.20.2+label%3ACherryPickApproved).

* BUGFIX: fix a bug, which could lead to incomplete or empty results for heavy queries selecting tens of thousands of time series. See [this pull request](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/3946).
* BUGFIX: [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): properly take into account `-rpc.disableCompression` command-line flag at `vmstorage`. It was ignored since [v1.78.0](https://docs.victoriametrics.com/victoriametrics/changelog/#v1780). See [this pull request](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/3932).
* BUGFIX: prevent from possible `SIGBUS` crash on ARM architectures (Raspberry Pi), which deny unaligned access to 8-byte words. Thanks to @oliverpool for narrowing down the issue and for [the initial attempt to fix it](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/3927).


## [v1.79.10](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.79.10)

Released at 2023-02-27

**v1.79.x is a line of [LTS releases](https://docs.victoriametrics.com/victoriametrics/lts-releases/). It contains important up-to-date bugfixes.
The v1.79.x line will be supported for at least 12 months since [v1.79.0](https://docs.victoriametrics.com/victoriametrics/changelog/#v1790) release**

* BUGFIX: prevent from high CPU usage on the first UTC hour of the data. The issue has been introduced in [v1.79.5](https://docs.victoriametrics.com/victoriametrics/changelog/#v1795) when fixing [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/3309).


## [v1.79.9](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.79.9)

Released at 2023-02-24

**v1.79.x is a line of [LTS releases](https://docs.victoriametrics.com/victoriametrics/lts-releases/). It contains important up-to-date bugfixes.
The v1.79.x line will be supported for at least 12 months since [v1.79.0](https://docs.victoriametrics.com/victoriametrics/changelog/#v1790) release**

* SECURITY: upgrade base docker image (alpine) from 3.17.1 to 3.17.2. See [alpine 3.17.2 release notes](https://alpinelinux.org/posts/Alpine-3.17.2-released.html).
* SECURITY: upgrade Go builder from Go1.20.0 to Go1.20.1. See [the list of issues addressed in Go1.20.1](https://github.com/golang/go/issues?q=milestone%3AGo1.20.1+label%3ACherryPickApproved).

* BUGFIX: properly parse timestamps in milliseconds when [ingesting data via OpenTSDB telnet put protocol](https://docs.victoriametrics.com/victoriametrics/integrations/opentsdb/#sending-data-via-telnet). Previously timestamps in milliseconds were mistakenly multiplied by 1000. Thanks to @Droxenator for the [pull request](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/3810).


## [v1.79.8](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.79.8)

Released at 2023-02-03

**v1.79.x is a line of [LTS releases](https://docs.victoriametrics.com/victoriametrics/lts-releases/). It contains important up-to-date bugfixes.
The v1.79.x line will be supported for at least 12 months since [v1.79.0](https://docs.victoriametrics.com/victoriametrics/changelog/#v1790) release**

* BUGFIX: fix a bug, which could prevent background merges for the previous partitions until restart if the storage didn't have enough disk space for final deduplication and down-sampling.
* BUGFIX: [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/): update API version for [ec2_sd_configs](https://docs.victoriametrics.com/victoriametrics/sd_configs/#ec2_sd_configs) to fix [the issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/3700) with missing `__meta_ec2_availability_zone_id` attribute.
* BUGFIX: [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): fix panic on top-level vmselect nodes of [multi-level setup](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/#multi-level-cluster-setup) when the `-replicationFactor` flag is set and request contains `trace` query parameter. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/3734).
* BUGFIX: [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/): [dockerswarm_sd_configs](https://docs.victoriametrics.com/victoriametrics/sd_configs/#dockerswarm_sd_configs): apply `filters` only to objects of the specified `role`. Previously filters were applied to all the objects, which could cause errors when different types of objects were used with filters that were not compatible with them. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/3579).
* BUGFIX: [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/): suppress all the scrape errors when `-promscrape.suppressScrapeErrors` is enabled. Previously some scrape errors were logged even if `-promscrape.suppressScrapeErrors` flag was set.
* BUGFIX: [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/): consistently put the scrape url with scrape target labels to all error logs for failed scrapes. Previously some failed scrapes were logged without this information.
* BUGFIX: [MetricsQL](https://docs.victoriametrics.com/victoriametrics/metricsql/): properly parse `M` and `Mi` suffixes as `1e6` multipliers in `1M` and `1Mi` numeric constants. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/3664). The issue has been introduced in [v1.79.7](https://docs.victoriametrics.com/victoriametrics/changelog/#v1797).


## [v1.79.7](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.79.7)

Released at 2023-01-10

**v1.79.x is a line of [LTS releases](https://docs.victoriametrics.com/victoriametrics/lts-releases/). It contains important up-to-date bugfixes.
The v1.79.x line will be supported for at least 12 months since [v1.79.0](https://docs.victoriametrics.com/victoriametrics/changelog/#v1790) release**

* BUGFIX: properly parse floating-point numbers without integer or fractional parts such as `.123` and `20.` during [data import](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#how-to-import-time-series-data). See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/3544).
* BUGFIX: [MetricsQL](https://docs.victoriametrics.com/victoriametrics/metricsql/): properly parse durations with uppercase suffixes such as `10S`, `5MS`, `1W`, etc. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/3589).
* BUGFIX: [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/): [dockerswarm_sd_configs](https://docs.victoriametrics.com/victoriametrics/sd_configs/#dockerswarm_sd_configs): properly encode `filters` field. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/3579)
* BUGFIX: allow specifying values bigger than 2GiB to the following command-line flag values on 32-bit architectures (`386` and `arm`): `-storage.minFreeDiskSpaceBytes` and `-remoteWrite.maxDiskUsagePerURL`. Previously values bigger than 2GiB were incorrectly truncated on these architectures.
* BUGFIX: [VictoriaMetrics Enterprise](https://docs.victoriametrics.com/victoriametrics/enterprise/): expose proper values for `vm_downsampling_partitions_scheduled` and `vm_downsampling_partitions_scheduled_size_bytes` metrics, which were added at [v1.78.0](https://docs.victoriametrics.com/victoriametrics/changelog/#v1780). See [this feature request](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/2612).
* BUGFIX: [DataDog protocol parser](https://docs.victoriametrics.com/victoriametrics/integrations/datadog/): do not reuse `host` and `device` fields from the previously parsed messages if these fields are missing in the currently parsed message. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/3432).


## [v1.79.6](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.79.6)

Released at 2022-12-11

**v1.79.x is a line of [LTS releases](https://docs.victoriametrics.com/victoriametrics/lts-releases/). It contains important up-to-date bugfixes.
The v1.79.x line will be supported for at least 12 months since [v1.79.0](https://docs.victoriametrics.com/victoriametrics/changelog/#v1790) release**

* SECURITY: update Go builder from v1.19.3 to v1.19.4. See [the changelog](https://github.com/golang/go/issues?q=milestone%3AGo1.19.4+label%3ACherryPickApproved).
* SECURITY: update base Docker image for VictoriaMetrics components from Alpine 3.16.2 to Alpine v3.17.0. See [the changelog](https://alpinelinux.org/releases/).

* BUGFIX: [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/): fix the `The request did not have a subscription or a valid tenant level resource provider` error when discovering Azure targets with [azure_sd_configs](https://docs.victoriametrics.com/victoriametrics/sd_configs/#azure_sd_configs). See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/3247).
* BUGFIX: [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/): properly discover GCE zones when `filter` option is set at [gce_sd_configs](https://docs.victoriametrics.com/victoriametrics/sd_configs/#gce_sd_configs). See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/3202).
* BUGFIX: [vmalert](https://docs.victoriametrics.com/victoriametrics/vmalert/): properly specify rule evaluation step during the [replay mode](https://docs.victoriametrics.com/victoriametrics/vmalert/#rules-backfilling). The `step` value was previously overridden by `-datasource.queryStep` command-line flag.
* BUGFIX: [vmalert](https://docs.victoriametrics.com/victoriametrics/vmalert/): properly return the error message from remote-write failures. Before, error was ignored and only `vmalert_remotewrite_errors_total` was incremented.
* BUGFIX: [MetricsQL](https://docs.victoriametrics.com/victoriametrics/metricsql/): properly return an empty result from [limit_offset](https://docs.victoriametrics.com/victoriametrics/metricsql/#limit_offset) if the `offset` arg exceeds the number of inner time series. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/3312).


## [v1.79.5](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.79.5)

Released at 2022-11-10

**v1.79.x is a line of [LTS releases](https://docs.victoriametrics.com/victoriametrics/lts-releases/). It contains important up-to-date bugfixes.
The v1.79.x line will be supported for at least 12 months since [v1.79.0](https://docs.victoriametrics.com/victoriametrics/changelog/#v1790) release**

**Update note 1:** [vmalert](https://docs.victoriametrics.com/victoriametrics/vmalert/): the `crlfEscape` [template function](https://docs.victoriametrics.com/victoriametrics/vmalert/#template-functions) becomes obsolete starting from this release. It can be safely removed from alerting templates, since `\n` chars are properly escaped with other `*Escape` functions now. See [this](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/3139) and [this](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/890) issue for details.

* SECURITY: update Go builder to v1.19.3. This fixes [CVE-2022 security issue](https://github.com/golang/go/issues/56328). See [the changelog](https://github.com/golang/go/issues?q=milestone%3AGo1.19.3+label%3ACherryPickApproved).

* BUGFIX: properly register new time series in per-day inverted index if they were ingested during the last 10 seconds of the day. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/3309). Thanks to @lmarszal for the bugreport and for the [initial fix](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/3320).
* BUGFIX: properly accept [OpenTSDB telnet put lines](https://docs.victoriametrics.com/victoriametrics/integrations/opentsdb/#sending-data-via-telnet) without tags without the need to specify the trailing whitespace. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/3290).
* BUGFIX: [MetricsQL](https://docs.victoriametrics.com/victoriametrics/metricsql/): properly merge buckets with identical `le` values, but with different string representation of these values when calculating [histogram_quantile](https://docs.victoriametrics.com/victoriametrics/metricsql/#histogram_quantile) and [histogram_share](https://docs.victoriametrics.com/victoriametrics/metricsql/#histogram_share). For example, `http_request_duration_seconds_bucket{le="5"}` and `http_requests_duration_seconds_bucket{le="5.0"}`. Such buckets may be returned from distinct targets. Thanks to @647-coder for the [pull request](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/3225).
* BUGFIX: [vmalert](https://docs.victoriametrics.com/victoriametrics/vmalert/): change severity level for log messages about failed attempts for sending data to remote storage from `error` to `warn`. The message for about all failed send attempts remains at `error` severity level.
* BUGFIX: [vmalert](https://docs.victoriametrics.com/victoriametrics/vmalert/): properly escape string passed to `quotesEscape` [template function](https://docs.victoriametrics.com/victoriametrics/vmalert/#template-functions), so it can be safely embedded into JSON string. This makes obsolete the `crlfEscape` function. See [this](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/3139) and [this](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/890) issue.
* BUGFIX: `vmselect`: expose missing metric `vm_cache_size_max_bytes{type="promql/rollupResult"}` . This metric is used for monitoring rollup cache usage with the query `vm_cache_size_bytes{type="promql/rollupResult"} / vm_cache_size_max_bytes{type="promql/rollupResult"}` in the same way as this is done for other cache types.
