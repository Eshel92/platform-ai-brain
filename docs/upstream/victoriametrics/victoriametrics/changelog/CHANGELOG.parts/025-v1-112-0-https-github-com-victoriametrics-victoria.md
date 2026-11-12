<!-- Part 25 of 27 of victoriametrics/changelog/CHANGELOG.md (split because the page is big). -->

## [v1.112.0](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.112.0)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2025/#v11120)


## [v1.111.0](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.111.0)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2025/#v11110)


## [v1.110.31](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.110.31)

Released at 2026-02-27

**v1.110.x is a line of [LTS releases](https://docs.victoriametrics.com/victoriametrics/lts-releases/). It contains important up-to-date bugfixes for [VictoriaMetrics enterprise](https://docs.victoriametrics.com/victoriametrics/enterprise/).
All these fixes are also included in [the latest community release](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/latest).
The v1.110.x line will be supported for at least 12 months since [v1.110.0](https://docs.victoriametrics.com/victoriametrics/changelog/#v11100) release**

* BUGFIX: `vmstorage` in [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): properly search tenants for [multitenant](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/#multitenancy) query request. See [#10422](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/10422).


## [v1.110.30](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.110.30)

Released at 2026-02-13

**v1.110.x is a line of [LTS releases](https://docs.victoriametrics.com/victoriametrics/lts-releases/). It contains important up-to-date bugfixes for [VictoriaMetrics enterprise](https://docs.victoriametrics.com/victoriametrics/enterprise/).
All these fixes are also included in [the latest community release](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/latest).
The v1.110.x line will be supported for at least 12 months since [v1.110.0](https://docs.victoriametrics.com/victoriametrics/changelog/#v11100) release**

* SECURITY: upgrade base docker image (Alpine) from 3.23.2 to 3.23.3. See [Alpine 3.23.3 release notes](https://www.alpinelinux.org/posts/Alpine-3.20.9-3.21.6-3.22.3-3.23.3-released.html).
* SECURITY: upgrade Go builder from Go1.24.12 to Go1.24.13. See [the list of issues addressed in Go1.24.13](https://github.com/golang/go/issues?q=milestone%3AGo1.24.13+label%3ACherryPickApproved).

* BUGFIX: VictoriaMetrics [enterprise](https://docs.victoriametrics.com/enterprise/) [vmagent](https://docs.victoriametrics.com/vmagent/) and [vmsingle](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/): introduce time‑based manual offset commit for [kafka consumer](https://docs.victoriametrics.com/victoriametrics/integrations/kafka/) to fix performance degradation with enabled manual commit. After this change, the consumer will commit partition offsets in batch per second to avoid high commit QPS on the Kafka broker. It's no longer recommended to set `enable.auto.commit=true` in `-kafka.consumer.topic.options`, as `vmagent` will automatically manage it. See [#10395](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/10395).
* BUGFIX: [vmsingle](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/) and `vmselect` in [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): previously the [Graphite render API](https://docs.victoriametrics.com/victoriametrics/integrations/graphite/#render-api) used a fixed process timeout that could expire before long queries completed; now the timeout follows the query deadline, so users can extend it via `-search.maxQueryDuration` or the `timeout` [argument in the query](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#query-data). See [#8484](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/8484).
* BUGFIX: [vmsingle](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/) and `vmselect` in [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): avoid slow-path deduplication for time series with [staleness markers](https://docs.victoriametrics.com/victoriametrics/vmagent/#prometheus-staleness-markers). See [#10384](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/10384). Thanks to @fxrlv for the contribution.
* BUGFIX: [vmsingle](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/) and `vmselect` in [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): fix `vm_deduplicated_samples_total{type="select"}` to correctly count deduplicated identical samples with the same timestamp and value. See [#10400](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/10400).
  [#10400](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/10400).
* BUGFIX: [vmsingle](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/) and `vmselect` in [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): properly prettify metricsql queries with `regex`. See [metricsql#60](https://github.com/VictoriaMetrics/metricsql/issues/60). Thanks to @freeseacher for the contribution.


## [v1.110.29](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.110.29)

Released at 2026-01-30

**Update Note 1:** `vmstorage` in [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): has a bug affecting the `/select/multitenant/*` APIs. Due to an issue in the tenant search logic [#10422](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/10422), these endpoints may return incorrect results. The bug has been fixed and the correction will be included in `v1.110.31`.

**v1.110.x is a line of [LTS releases](https://docs.victoriametrics.com/victoriametrics/lts-releases/). It contains important up-to-date bugfixes for [VictoriaMetrics enterprise](https://docs.victoriametrics.com/victoriametrics/enterprise/).
All these fixes are also included in [the latest community release](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/latest).
The v1.110.x line will be supported for at least 12 months since [v1.110.0](https://docs.victoriametrics.com/victoriametrics/changelog/#v11100) release**

* BUGFIX: [MetricsQL](https://docs.victoriametrics.com/victoriametrics/metricsql/): fix `changes()` function when gaps between samples exceed the lookbehind window. Previously, it could yield a non-zero value even when the sample value remained unchanged. See [#10280](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/10280).
* BUGFIX: [vmalert](https://docs.victoriametrics.com/victoriametrics/vmalert/): fix [alert restore](https://docs.victoriametrics.com/victoriametrics/vmalert/#alerts-state-on-restarts) when a group contains many rules and is slow to complete evaluation. Previously, the restore process might not retrieve the correct previous alert state. See [#10335](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/10335).
* BUGFIX: [vmauth](https://docs.victoriametrics.com/victoriametrics/vmauth/): fix an issue where canceling a client request (closing a browser tab or timeout) incorrectly marked all backends as unavailable for `-failTimeout` duration (3s by default), even though backends were healthy. See [#10318](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/10318).
* BUGFIX: [vmauth](https://docs.victoriametrics.com/victoriametrics/vmauth/): stop backend health checks for URL prefixes defined in `url_map` during configuration reloads. Previously, stale backends kept being health-checked and produced repeated warning logs after reloads. See [#10334](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/10334).
* BUGFIX: `vmstorage` in [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): correctly return tenants results for `/admin/tenants` when `start` or `end` are specified. See [#10312](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/10312)
* BUGFIX: [vmui](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#vmui): fix "Percentage from total" calculation on the Cardinality Explorer page when multiple metrics match the filter. See [#10323](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/10323). Thanks to @PleasingFungus for the contribution.


## [v1.110.28](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.110.28)

Released at 2026-01-16

**v1.110.x is a line of [LTS releases](https://docs.victoriametrics.com/victoriametrics/lts-releases/). It contains important up-to-date bugfixes for [VictoriaMetrics enterprise](https://docs.victoriametrics.com/victoriametrics/enterprise/).
All these fixes are also included in [the latest community release](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/latest).
The v1.110.x line will be supported for at least 12 months since [v1.110.0](https://docs.victoriametrics.com/victoriametrics/changelog/#v11100) release**

* SECURITY: upgrade Go builder from Go1.24.11 to Go1.24.12. See [the list of issues addressed in Go1.24.12](https://github.com/golang/go/issues?q=milestone%3AGo1.24.12+label%3ACherryPickApproved).

* BUGFIX: [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/): fix configuration reloading for `-remoteWrite.relabelConfig` and `-remoteWrite.urlRelabelConfig` when vmagent is launched with empty files. Previously, if vmagent started with an empty config, subsequent config reloads were ignored. See [#10211](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/10211).
* BUGFIX: `vmstorage` in [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): reduce default value for `storage.vminsertConnsShutdownDuration` flag from `25s` to `10s` seconds. It reduces probability of ungraceful storage shutdown at Kubernetes based environments, which has 30 seconds default graceful termination period value. See [#10273](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/10273)
* BUGFIX: [vmui](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#vmui): fix heatmap rendering issues where charts could break or appear empty when bucket values were uniform or sparse. See [#10240](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/10240).
* BUGFIX: all VictoriaMetrics components: prefer numerical values over [stale markers](https://docs.victoriametrics.com/victoriametrics/vmagent/#prometheus-staleness-markers) when samples share the same timestamp during deduplication. See [#10196](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/10196#issuecomment-3738433938).


## [v1.110.27](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.110.27)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2025/#v111027)


## [v1.110.26](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.110.26)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2025/#v111026)


## [v1.110.25](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.110.25)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2025/#v111025)


## [v1.110.24](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.110.24)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2025/#v111024)


## [v1.110.23](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.110.23)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2025/#v111023)


## [v1.110.22](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.110.22)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2025/#v111022)


## [v1.110.21](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.110.21)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2025/#v111021)


## [v1.110.20](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.110.20)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2025/#v111020)


## [v1.110.19](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.110.19)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2025/#v111019)


## [v1.110.18](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.110.18)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2025/#v111018)


## [v1.110.17](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.110.17)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2025/#v111017)


## [v1.110.16](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.110.16)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2025/#v111016)


## [v1.110.15](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.110.15)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2025/#v111015)


## [v1.110.14](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.110.14)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2025/#v111014)


## [v1.110.13](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.110.13)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2025/#v111013)


## [v1.110.12](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.110.12)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2025/#v111012)


## [v1.110.11](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.110.11)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2025/#v111011)


## [v1.110.10](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.110.10)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2025/#v111010)


## [v1.110.9](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.110.9)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2025/#v11109)


## [v1.110.8](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.110.8)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2025/#v11108)


## [v1.110.7](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.110.7)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2025/#v11107)


## [v1.110.6](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.110.6)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2025/#v11106)


## [v1.110.5](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.110.5)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2025/#v11105)


## [v1.110.4](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.110.4)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2025/#v11104)


## [v1.110.3](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.110.3)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2025/#v11103)


## [v1.110.2](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.110.2)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2025/#v11102)


## [v1.110.1](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.110.1)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2025/#v11101)


## [v1.110.0](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.110.0)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2025/#v11100)


## [v1.109.1](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.109.1)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2025/#v11091)


## [v1.109.0](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.109.0)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2025/#v11090)


## [v1.108.1](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.108.1)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2024/#v11081)


## [v1.108.0](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.108.0)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2024/#v11080)


## [v1.107.0](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.107.0)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2024/#v11070)


## [v1.106.1](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.106.1)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2024/#v11061)


## [v1.106.0](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.106.0)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2024/#v11060)


## [v1.105.0](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.105.0)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2024/#v11050)


## [v1.104.0](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.104.0)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2024/#v11040)


## [v1.103.0](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.103.0)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2024/#v11030)


## [v1.102.25](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.102.25)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2025/#v110225)


## [v1.102.24](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.102.24)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2025/#v110224)


## [v1.102.23](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.102.23)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2025/#v110223)


## [v1.102.22](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.102.22)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2025/#v110222)


## [v1.102.21](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.102.21)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2025/#v110221)


## [v1.102.20](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.102.20)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2025/#v110220)


## [v1.102.19](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.102.19)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2025/#v110219)


## [v1.102.18](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.102.18)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2025/#v110218)


## [v1.102.17](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.102.17)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2025/#v110217)
