<!-- Part 18 of 19 of victoriametrics/changelog/CHANGELOG_2025.md (split because the page is big). -->

## [v1.97.17](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.97.17)

Released at 2025-01-28

**v1.97.x is a line of [LTS releases](https://docs.victoriametrics.com/victoriametrics/lts-releases/). It contains important up-to-date bugfixes for [VictoriaMetrics Enterprise](https://docs.victoriametrics.com/victoriametrics/enterprise/).
All these fixes are also included in [the latest community release](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/latest).
The v1.97.x line will be supported for at least 12 months since [v1.97.0](https://docs.victoriametrics.com/victoriametrics/changelog/#v1970) release**

* BUGFIX: [vmsingle](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/), `vminsert` in [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/) and [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/): log metric names for signals with unsupported delta temporality on ingestion via [OpenTelemetry protocol for metrics](https://docs.victoriametrics.com/victoriametrics/integrations/opentelemetry/). Thanks to @chenlujjj for [the pull request](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/8018).
* BUGFIX: [Single-node VictoriaMetrics](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/) and [vmselect](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): respect staleness detection in increase, increase_pure and delta functions when time series has gaps and `-search.maxStalenessInterval` is set. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/8072) for details.


## [v1.97.16](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.97.16)

Released at 2025-01-24

It is recommended upgrading to [v1.97.17](https://docs.victoriametrics.com/victoriametrics/changelog/#v19717) because [v1.97.16](https://docs.victoriametrics.com/victoriametrics/changelog/#v19716) contains a bug with staleness detection.

**v1.97.x is a line of [LTS releases](https://docs.victoriametrics.com/victoriametrics/lts-releases/). It contains important up-to-date bugfixes for [VictoriaMetrics Enterprise](https://docs.victoriametrics.com/victoriametrics/enterprise/).
All these fixes are also included in [the latest community release](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/latest).
The v1.97.x line will be supported for at least 12 months since [v1.97.0](https://docs.victoriametrics.com/victoriametrics/changelog/#v1970) release**

* BUGFIX: all VictoriaMetrics [enterprise](https://docs.victoriametrics.com/victoriametrics/enterprise/) components: remove unnecessary delay before failing if all online verification attempts have failed. This should reduce the time required for the component to proceed if all online verification attempts have failed.
* BUGFIX: [Single-node VictoriaMetrics](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/) and [vmselect](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): don't take into account the last raw sample before the lookbehind window is sample exceeds the staleness interval. This affects correctness of increase, increase_pure, delta functions when performing calculations on time series with gaps. See [this pull request](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/8002) for details.
* BUGFIX: [vmsingle](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/), `vminsert` in [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/) and [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/): allow ingesting histograms with missing `_sum` metric via [OpenTelemetry ingestion protocol](https://docs.victoriametrics.com/victoriametrics/integrations/opentelemetry/) in the same way as Prometheus does.


## [v1.97.15](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.97.15)

Released at 2025-01-14

**v1.97.x is a line of [LTS releases](https://docs.victoriametrics.com/victoriametrics/lts-releases/). It contains important up-to-date bugfixes for [VictoriaMetrics Enterprise](https://docs.victoriametrics.com/victoriametrics/enterprise/).
All these fixes are also included in [the latest community release](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/latest).
The v1.97.x line will be supported for at least 12 months since [v1.97.0](https://docs.victoriametrics.com/victoriametrics/changelog/#v1970) release**

* FEATURE: all VictoriaMetrics [enterprise](https://docs.victoriametrics.com/victoriametrics/enterprise/) components: add support of hot-reload for license key supplied by `-licenseFile` command-line flag.

* BUGFIX: [vmsingle](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/), `vmselect` in [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): make instant query results consistent. VictoriaMetrics detects and adjusts scrape interval and while this is very useful for range queries (i.e. this eliminates gaps on the graph), it may cause instant queries to return a non-empty result when no result is expected. The fix is to disable scrape interval detection and always use the step as the scrape interval in instant queries. This will guarantee that the samples are searched within the (time-step, time] interval. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/5796) for details.
* BUGFIX: [vmctl](https://docs.victoriametrics.com/victoriametrics/vmctl/): fix support for migrating influx series without any tag. See [this pull request](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/7935). Thanks to @bitbidu for reporting.
* BUGFIX: `vminsert` in [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): storage nodes defined in `-storageNode` are now sorted, ensuring that varying node orders across different vminsert instances do not result in inconsistent replication.


## [v1.97.14](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.97.14)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2024/#v19714)


## [v1.97.13](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.97.13)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2024/#v19713)


## [v1.97.12](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.97.12)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2024/#v19712)


## [v1.97.11](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.97.11)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2024/#v19711)


## [v1.97.10](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.97.10)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2024/#v19710)


## [v1.97.9](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.97.9)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2024/#v1979)


## [v1.97.8](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.97.8)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2024/#v1978)


## [v1.97.7](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.97.7)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2024/#v1977)


## [v1.97.6](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.97.6)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2024/#v1976)


## [v1.97.5](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.97.5)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2024/#v1975)


## [v1.97.4](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.97.4)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2024/#v1974)


## [v1.97.3](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.97.3)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2024/#v1973)


## [v1.97.2](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.97.2)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2024/#v1972)


## [v1.97.1](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.97.1)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2024/#v1971)


## [v1.97.0](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.97.0)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2024/#v1970)


## [v1.96.0](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.96.0)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2023/#v1960)


## [v1.95.1](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.95.1)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2023/#v1951)


## [v1.95.0](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.95.0)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2023/#v1950)


## [v1.94.0](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.94.0)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2023/#v1940)


## [v1.93.16](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.93.16)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2024/#v19316)


## [v1.93.15](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.93.15)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2024/#v19315)


## [v1.93.14](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.93.14)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2024/#v19314)


## [v1.93.13](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.93.13)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2024/#v19313)


## [v1.93.12](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.93.12)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2024/#v19311)


## [v1.93.11](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.93.11)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2024/#v19311)


## [v1.93.10](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.93.10)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2024/#v19310)


## [v1.93.9](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.93.9)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2023/#v1939)


## [v1.93.8](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.93.8)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2023/#v1938)


## [v1.93.7](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.93.7)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2023/#v1937)


## [v1.93.6](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.93.6)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2023/#v1936)


## [v1.93.5](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.93.5)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2023/#v1935)


## [v1.93.4](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.93.4)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2023/#v1934)


## [v1.93.3](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.93.3)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2023/#v1933)


## [v1.93.2](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.93.2)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2023/#v1932)


## [v1.93.1](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.93.1)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2023/#v1931)


## [v1.93.0](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.93.0)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2023/#v1930)


## [v1.92.1](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.92.1)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2023/#v1921)


## [v1.92.0](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.92.0)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2023/#v1920)


## [v1.91.3](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.91.3)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2023/#v1913)


## [v1.91.2](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.91.2)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2023/#v1912)


## [v1.91.1](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.91.1)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2023/#v1911)


## [v1.91.0](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.91.0)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2023/#v1910)


## [v1.90.0](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.90.0)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2023/#v1900)


## [v1.89.1](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.89.1)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2023/#v1891)


## [v1.89.0](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.89.0)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2023/#v1890)


## [v1.88.1](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.88.1)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2023/#v1881)


## [v1.88.0](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.88.0)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2023/#v1880)


## [v1.87.14](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.87.14)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2024/#v18714)


## [v1.87.13](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.87.13)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2024/#v18713)


## [v1.87.12](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.87.12)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2023/#v18712)


## [v1.87.11](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.87.11)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2023/#v18711)


## [v1.87.10](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.87.10)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2023/#v18710)


## [v1.87.9](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.87.9)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2023/#v1879)


## [v1.87.8](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.87.8)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2023/#v1878)


## [v1.87.7](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.87.7)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2023/#v1877)


## [v1.87.6](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.87.6)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2023/#v1876)


## [v1.87.5](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.87.5)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2023/#v1875)


## [v1.87.4](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.87.4)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2023/#v1874)


## [v1.87.3](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.87.3)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2023/#v1873)


## [v1.87.2](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.87.2)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2023/#v1872)


## [v1.87.1](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.87.1)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2023/#v1871)


## [v1.87.0](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.87.0)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2023/#v1870)


## [v1.86.2](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.86.2)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2023/#v1862)


## [v1.86.1](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.86.1)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2023/#v1861)


## [v1.86.0](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.86.0)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2023/#v1860)


## [v1.85.3](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.85.3)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2022/#v1853)


## [v1.85.2](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.85.2)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2022/#v1852)


## [v1.85.1](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.85.1)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2022/#v1851)


## [v1.85.0](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.85.0)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2022/#v1850)


## [v1.84.0](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.84.0)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2022/#v1840)


## [v1.83.1](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.83.1)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2022/#v1831)


## [v1.83.0](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.83.0)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2022/#v1830)


## [v1.82.1](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.82.1)

See changes [here](https://docs.victoriametrics.com/victoriametrics/changelog/changelog_2022/#v1821)
