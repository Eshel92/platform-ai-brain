<!-- Part 24 of 27 of victoriametrics/changelog/CHANGELOG.md (split because the page is big). -->

## [v1.122.17](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.122.17)

Released at 2026-03-13

**v1.122.x is a line of [LTS releases](https://docs.victoriametrics.com/victoriametrics/lts-releases/). It contains important up-to-date bugfixes for [VictoriaMetrics enterprise](https://docs.victoriametrics.com/victoriametrics/enterprise/).
All these fixes are also included in [the latest community release](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/latest).
The v1.122.x line will be supported for at least 12 months since [v1.122.0](https://docs.victoriametrics.com/victoriametrics/changelog/#v11220) release**

* SECURITY: upgrade Go builder from Go1.24.13 to Go1.25.8. See [the list of issues addressed in Go1.25.8](https://github.com/golang/go/issues?q=milestone%3AGo1.25.8+label%3ACherryPickApproved).

* FEATURE: [MetricsQL](https://docs.victoriametrics.com/victoriametrics/metricsql/): add [histogram_fraction](https://docs.victoriametrics.com/victoriametrics/metricsql/#histogram_fraction) function to calculate the fraction of buckets falling between lowerLe and upperLe. See [#5346](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/5346).

* BUGFIX: all VictoriaMetrics components: replace `histogram` with `untyped` metric metadata type for [VictoriaMetrics histograms](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#histogram) when `-metrics.exposeMetadata` is set. See [#82](https://github.com/VictoriaMetrics/metrics/issues/82).
* BUGFIX: [vmauth](https://docs.victoriametrics.com/victoriametrics/vmauth/): properly route requests to `default_url`. Previously, `request_path` query arg could be set incorrectly during concurrent requests. See [#10626](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/10626).
* BUGFIX: [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/), [vmsingle](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/), `vminsert` and `vmstorage` in [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): properly attach `host` label to the time series ingested via [/datadog/api/beta/sketches](https://docs.victoriametrics.com/victoriametrics/integrations/datadog/#) API. See [#10557](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/10557).
* BUGFIX: [vmui](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#vmui): use `increase_pure` instead of `rate` for histogram heatmaps in Explore Metrics to correctly display the first observation in each new bucket. See [#10365](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/10365). Thanks to @ab0utbla-k for the contribution.
* BUGFIX: `vmstorage` in [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): fix inaccurate `vm_filestream_write_duration_seconds_total` due to duplicate counting . After the fix, `vm_filestream_write_duration_seconds_total` will track the duration spent on calling the `write(2)` system call properly. See [#10564](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/10564).


## [v1.122.16](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.122.16)

Released at 2026-02-27

**v1.122.x is a line of [LTS releases](https://docs.victoriametrics.com/victoriametrics/lts-releases/). It contains important up-to-date bugfixes for [VictoriaMetrics enterprise](https://docs.victoriametrics.com/victoriametrics/enterprise/).
All these fixes are also included in [the latest community release](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/latest).
The v1.122.x line will be supported for at least 12 months since [v1.122.0](https://docs.victoriametrics.com/victoriametrics/changelog/#v11220) release**

* BUGFIX: [vmsingle](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/) and `vmstorage` in [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): prevent panic `error parsing regexp: expression nests too deeply` triggered by large repetition ranges in regex, for example `{"__name__"=~"a{0,1000}"}`. See [VictoriaLogs#1112](https://github.com/VictoriaMetrics/VictoriaLogs/issues/1112).
* BUGFIX: `vmstorage` in [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): properly search tenants for [multitenant](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/#multitenancy) query request. See [#10422](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/10422).
* BUGFIX: `vmstorage` in [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): properly apply `extra_filters[]` filter when querying `vm_account_id` or `vm_project_id` labels via [multitenant](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/#multitenancy) request for `/api/v1/label/…/values` API. Before, `extra_filters` was ignored. See [#10503](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/10503).
* BUGFIX: [vmui](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#vmui): fix escaping for label names with special characters. See [#10485](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/10485).


## [v1.122.15](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.122.15)

Released at 2026-02-13

**v1.122.x is a line of [LTS releases](https://docs.victoriametrics.com/victoriametrics/lts-releases/). It contains important up-to-date bugfixes for [VictoriaMetrics enterprise](https://docs.victoriametrics.com/victoriametrics/enterprise/).
All these fixes are also included in [the latest community release](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/latest).
The v1.122.x line will be supported for at least 12 months since [v1.122.0](https://docs.victoriametrics.com/victoriametrics/changelog/#v11220) release**

* SECURITY: upgrade base docker image (Alpine) from 3.23.2 to 3.23.3. See [Alpine 3.23.3 release notes](https://www.alpinelinux.org/posts/Alpine-3.20.9-3.21.6-3.22.3-3.23.3-released.html).
* SECURITY: upgrade Go builder from Go1.24.12 to Go1.24.13. See [the list of issues addressed in Go1.24.13](https://github.com/golang/go/issues?q=milestone%3AGo1.24.13+label%3ACherryPickApproved).

* BUGFIX: all VictoriaMetrics components: respect default http client proxy env variables (`HTTP_PROXY`, `HTTPS_PROXY`, `NO_PROXY`). See [#10385](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/10385). Thanks to @zane-deg for the contribution.
* BUGFIX: [vmagent](https://docs.victoriametrics.com/vmagent/) and [vmsingle](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/): properly expose `kubernetes_sd` discovery network dialer metrics `vm_promscrape_discovery_kubernetes_conn_*`. See [#10382](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/10382).
* BUGFIX: VictoriaMetrics [enterprise](https://docs.victoriametrics.com/enterprise/) [vmagent](https://docs.victoriametrics.com/vmagent/) and [vmsingle](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/): introduce time‑based manual offset commit for [kafka consumer](https://docs.victoriametrics.com/victoriametrics/integrations/kafka/) to fix performance degradation with enabled manual commit. After this change, the consumer will commit partition offsets in batch per second to avoid high commit QPS on the Kafka broker. It's no longer recommended to set `enable.auto.commit=true` in `-kafka.consumer.topic.options`, as `vmagent` will automatically manage it. See [#10395](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/10395).
* BUGFIX: [vmsingle](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/) and `vmselect` in [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): fix `vm_deduplicated_samples_total{type="select"}` to correctly count deduplicated identical samples with the same timestamp and value. See [#10400](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/10400).
* BUGFIX: [vmsingle](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/) and `vmselect` in [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): previously the [Graphite render API](https://docs.victoriametrics.com/victoriametrics/integrations/graphite/#render-api) used a fixed process timeout that could expire before long queries completed; now the timeout follows the query deadline, so users can extend it via `-search.maxQueryDuration` or the `timeout` [argument in the query](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#query-data). See [#8484](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/8484).
* BUGFIX: [vmsingle](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/) and `vmselect` in [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): avoid slow-path deduplication for time series with [staleness markers](https://docs.victoriametrics.com/victoriametrics/vmagent/#prometheus-staleness-markers). See [#10384](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/10384).
* BUGFIX: [vmsingle](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/) and `vmselect` in [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): properly prettify metricsql queries with `regex`. See [metricsql#60](https://github.com/VictoriaMetrics/metricsql/issues/60). Thanks to @freeseacher for the contribution.


## [v1.122.14](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.122.14)

Released at 2026-01-30

**Update Note 1:** `vmstorage` in [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): has a bug affecting the `/select/multitenant/*` APIs. Due to an issue in the tenant search logic [#10422](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/10422), these endpoints may return incorrect results. The bug has been fixed and the correction will be included in `v1.122.16`.

**v1.122.x is a line of [LTS releases](https://docs.victoriametrics.com/victoriametrics/lts-releases/). It contains important up-to-date bugfixes for [VictoriaMetrics enterprise](https://docs.victoriametrics.com/victoriametrics/enterprise/).
All these fixes are also included in [the latest community release](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/latest).
The v1.122.x line will be supported for at least 12 months since [v1.122.0](https://docs.victoriametrics.com/victoriametrics/changelog/#v11220) release**

* BUGFIX: [vmauth](https://docs.victoriametrics.com/victoriametrics/vmauth/): stop backend health checks for URL prefixes defined in `url_map` during configuration reloads. Previously, stale backends kept being health-checked and produced repeated warning logs after reloads. See [#10334](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/10334).
* BUGFIX: `vmstorage` in [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): correctly return tenants results for `/admin/tenants` when `start` or `end` are specified. See [#10312](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/10312)
* BUGFIX: [vmui](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#vmui): fix "Percentage from total" calculation on the Cardinality Explorer page when multiple metrics match the filter. See [#10323](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/10323). Thanks to @PleasingFungus for the contribution.
* BUGFIX: [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/): apply `-promscrape.maxScrapeSize` check to decompressed data instead of compressed data. See [#9481](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/9481).
* BUGFIX: [vmalert](https://docs.victoriametrics.com/victoriametrics/vmalert/): fix [alert restore](https://docs.victoriametrics.com/victoriametrics/vmalert/#alerts-state-on-restarts) when a group contains many rules and is slow to complete evaluation. Previously, the restore process might not retrieve the correct previous alert state. See [#10335](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/10335).
* BUGFIX: [MetricsQL](https://docs.victoriametrics.com/victoriametrics/metricsql/): fix `changes()` function when gaps between samples exceed the lookbehind window. Previously, it could yield a non-zero value even when the sample value remained unchanged. See [#10280](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/10280).
* BUGFIX: [vmauth](https://docs.victoriametrics.com/victoriametrics/vmauth/): fix an issue where canceling a client request (closing a browser tab or timeout) incorrectly marked all backends as unavailable for `-failTimeout` duration (3s by default), even though backends were healthy. See [#10318](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/10318).


## [v1.122.13](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.122.13)

Released at 2026-01-16

**v1.122.x is a line of [LTS releases](https://docs.victoriametrics.com/victoriametrics/lts-releases/). It contains important up-to-date bugfixes for [VictoriaMetrics enterprise](https://docs.victoriametrics.com/victoriametrics/enterprise/).
All these fixes are also included in [the latest community release](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/latest).
The v1.122.x line will be supported for at least 12 months since [v1.122.0](https://docs.victoriametrics.com/victoriametrics/changelog/#v11220) release**

* SECURITY: upgrade Go builder from Go1.24.11 to Go1.24.12. It addresses [CVE-2025-61729](http://scout.docker.com/v/CVE-2025-61729). See [the list of issues addressed in Go1.24.12](https://github.com/golang/go/issues?q=milestone%3AGo1.24.12+label%3ACherryPickApproved).

* BUGFIX: [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/): fix configuration reloading for `-remoteWrite.relabelConfig` and `-remoteWrite.urlRelabelConfig` when vmagent is launched with empty files. Previously, if vmagent started with an empty config, subsequent config reloads were ignored. See [#10211](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/10211).
* BUGFIX: `vmstorage` in [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): reduce default value for `storage.vminsertConnsShutdownDuration` flag from `25s` to `10s` seconds. It reduces probability of ungraceful storage shutdown at Kubernetes based environments, which has 30 seconds default graceful termination period value. See [#10273](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/10273)
* BUGFIX: [vmui](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#vmui): fix heatmap rendering issues where charts could break or appear empty when bucket values were uniform or sparse. See [#10240](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/10240).
* BUGFIX: all VictoriaMetrics components: prefer numerical values over [stale markers](https://docs.victoriametrics.com/victoriametrics/vmagent/#prometheus-staleness-markers) when samples share the same timestamp during deduplication. See [#10196](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/10196#issuecomment-3738433938).


## [v1.122.12](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.122.12)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2025/#v112212)


## [v1.122.11](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.122.11)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2025/#v112211)


## [v1.122.10](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.122.10)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2025/#v112210)


## [v1.122.9](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.122.9)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2025/#v11229)


## [v1.122.8](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.122.8)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2025/#v11228)


## [v1.122.7](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.122.7)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2025/#v11227)


## [v1.122.6](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.122.6)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2025/#v11226)


## [v1.122.5](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.122.5)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2025/#v11225)


## [v1.122.4](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.122.4)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2025/#v11224)


## [v1.122.3](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.122.3)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2025/#v11223)


## [v1.122.2](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.122.2)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2025/#v11222)


## [v1.122.1](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.122.1)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2025/#v11221)


## [v1.122.0](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.122.0)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2025/#v11220)


## [v1.121.0](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.121.0)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2025/#v11210)


## [v1.120.0](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.120.0)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2025/#v11200)


## [v1.119.0](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.119.0)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2025/#v11190)


## [v1.118.0](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.118.0)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2025/#v11180)


## [v1.117.1](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.117.1)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2025/#v11171)


## [v1.117.0](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.117.0)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2025/#v11170)


## [v1.116.0](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.116.0)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2025/#v11160)


## [v1.115.0](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.115.0)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2025/#v11150)


## [v1.114.0](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.114.0)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2025/#v11140)


## [v1.113.0](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.113.0)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2025/#v11130)
