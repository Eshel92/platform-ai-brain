<!-- Part 12 of 14 of victoriametrics/changelog/CHANGELOG_2023.md (split because the page is big). -->

## [v1.87.5](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.87.5)

Released at 2023-04-06

**v1.87.x is a line of [LTS releases](https://docs.victoriametrics.com/victoriametrics/lts-releases/). It contains important up-to-date bugfixes.
The v1.87.x line will be supported for at least 12 months since [v1.87.0](https://docs.victoriametrics.com/victoriametrics/changelog/#v1870) release**

* SECURITY: upgrade base docker image (alpine) from 3.17.2 to 3.17.3. See [alpine 3.17.3 release notes](https://alpinelinux.org/posts/Alpine-3.17.3-released.html).
* SECURITY: upgrade Go builder from Go1.20.2 to Go1.20.3. See [the list of issues addressed in Go1.20.3](https://github.com/golang/go/issues?q=milestone%3AGo1.20.3+label%3ACherryPickApproved).

* BUGFIX: [MetricsQL](https://docs.victoriametrics.com/victoriametrics/metricsql/): properly convert [VictoriaMetrics histogram buckets](https://valyala.medium.com/improving-histogram-usability-for-prometheus-and-grafana-bc7e5df0e350) to Prometheus histogram buckets when VictoriaMetrics histogram contain zero buckets. Previously these buckets were ignored, and this could lead to missing Prometheus histogram buckets after the conversion. Thanks to @zklapow for [the fix](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/4021).
* BUGFIX: [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/): fix CPU and memory usage spikes when files pointed by [file_sd_config](https://docs.victoriametrics.com/victoriametrics/sd_configs/#file_sd_configs) cannot be re-read. See [this_issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/3989).
* BUGFIX: prevent unexpected merges on start-up when `-storage.minFreeDiskSpaceBytes` is set. See [the issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/4023).
* BUGFIX: properly support comma-separated filters inside [retention filters](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#retention-filters). See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/3915).
* BUGFIX: verify response code when fetching configuration files via HTTP. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/4034).


## [v1.87.4](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.87.4)

Released at 2023-03-25

**v1.87.x is a line of [LTS releases](https://docs.victoriametrics.com/victoriametrics/lts-releases/). It contains important up-to-date bugfixes.
The v1.87.x line will be supported for at least 12 months since [v1.87.0](https://docs.victoriametrics.com/victoriametrics/changelog/#v1870) release**

* BUGFIX: prevent from slow [snapshot creating](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#how-to-work-with-snapshots) under high data ingestion rate. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/3551).
* BUGFIX: [vmauth](https://docs.victoriametrics.com/victoriametrics/vmauth/):  suppress [proxy protocol](https://www.haproxy.org/download/2.3/doc/proxy-protocol.txt) parsing errors in case of `EOF`. Usually, the error is caused by health checks and is not a sign of an actual error.
* BUGFIX: [vmbackup](https://docs.victoriametrics.com/victoriametrics/vmbackup/): fix snapshot not being deleted in case of error during backup. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/2055).
* BUGFIX: allow using dashes and dots in environment variables names referred in config files via `%{ENV-VAR.SYNTAX}`. See [these docs](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#environment-variables) and [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/3999).
* BUGFIX: return back query performance scalability on hosts with big number of CPU cores. The scalability has been reduced in [v1.86.0](https://docs.victoriametrics.com/victoriametrics/changelog/#v1860). See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/3966).


## [v1.87.3](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.87.3)

Released at 2023-03-12

**v1.87.x is a line of [LTS releases](https://docs.victoriametrics.com/victoriametrics/lts-releases/). It contains important up-to-date bugfixes.
The v1.87.x line will be supported for at least 12 months since [v1.87.0](https://docs.victoriametrics.com/victoriametrics/changelog/#v1870) release**

* SECURITY: upgrade Go builder from Go1.20.1 to Go1.20.2. See [the list of issues addressed in Go1.20.2](https://github.com/golang/go/issues?q=milestone%3AGo1.20.2+label%3ACherryPickApproved).

* BUGFIX: vmstorage: fix a bug, which could lead to incomplete or empty results for heavy queries selecting tens of thousands of time series. See [this pull request](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/3946).
* BUGFIX: vmselect: reduce memory usage and CPU usage when performing heavy queries. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/3692).
* BUGFIX: prevent from possible `invalid memory address or nil pointer dereference` panic during [background merge](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#storage). The issue has been introduced at [v1.85.0](https://docs.victoriametrics.com/victoriametrics/changelog/#v1850). See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/3897).
* BUGFIX: prevent from possible `SIGBUS` crash on ARM architectures (Raspberry Pi), which deny unaligned access to 8-byte words. Thanks to @oliverpool for narrowing down the issue and for [the initial attempt to fix it](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/3927).
* BUGFIX: [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): always return `is_partial: true` in partial responses. Previously partial responses could be returned as non-partial in some cases.
* BUGFIX: [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): properly take into account `-rpc.disableCompression` command-line flag at `vmstorage`. It was ignored since [v1.78.0](https://docs.victoriametrics.com/victoriametrics/changelog/#v1780). See [this pull request](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/3932).
* BUGFIX: [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/): do not register `vm_promscrape_config_*` metrics if `-promscrape.config` flag is not used. Previously those metrics were registered and never updated, which was confusing and could trigger false-positive alerts.
* BUGFIX: [vmctl](https://docs.victoriametrics.com/victoriametrics/vmctl/): skip measurements with no fields when migrating data from influxdb. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/3837).
* BUGFIX: [vmauth](https://docs.victoriametrics.com/victoriametrics/vmauth/): fix `cannot serve http` panic when plain HTTP request is sent to `vmauth` configured to accept requests over [proxy protocol](https://www.haproxy.org/download/2.3/doc/proxy-protocol.txt)-encoded request (e.g. when `vmauth` runs with `-httpListenAddr.useProxyProtocol` command-line flag). The issue has been introduced at [v1.87.0](https://docs.victoriametrics.com/victoriametrics/changelog/#v1870) when implementing [this feature](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/3335).


## [v1.87.2](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.87.2)

Released at 2023-02-24

**v1.87.x is a line of [LTS releases](https://docs.victoriametrics.com/victoriametrics/lts-releases/). It contains important up-to-date bugfixes.
The v1.87.x line will be supported for at least 12 months since [v1.87.0](https://docs.victoriametrics.com/victoriametrics/changelog/#v1870) release**

* SECURITY: upgrade base docker image (alpine) from 3.17.1 to 3.17.2. See [alpine 3.17.2 release notes](https://alpinelinux.org/posts/Alpine-3.17.2-released.html).
* SECURITY: upgrade Go builder from Go1.20.0 to Go1.20.1. See [the list of issues addressed in Go1.20.1](https://github.com/golang/go/issues?q=milestone%3AGo1.20.1+label%3ACherryPickApproved).

* BUGFIX: [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/): immediately cancel in-flight scrape requests during configuration reload when [stream parsing mode](https://docs.victoriametrics.com/victoriametrics/vmagent/#stream-parsing-mode) is disabled. Previously `vmagent` could wait for long time until all the in-flight requests are completed before reloading the configuration. This could significantly slow down configuration reload. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/3747).
* BUGFIX: [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/): do not wait for 2 seconds after the first unsuccessful attempt to scrape the target before performing the next attempt. This should improve scrape speed when the target closes [http keep-alive connection](https://en.wikipedia.org/wiki/HTTP_persistent_connection) between scrapes. See [this](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/3293) and [this](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/3747) issues.
* BUGFIX: [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/): fix [Azure service discovery](https://docs.victoriametrics.com/victoriametrics/sd_configs/#azure_sd_configs) inside [Azure Container App](https://learn.microsoft.com/en-us/azure/container-apps/overview). See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/3830). Thanks to @MattiasAng for the fix!
* BUGFIX: do not put auxiliary directories scheduled for removal into snapshots. This should prevent from `cannot create hard links from ...must-remove...` errors when making snapshots / backups. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/3858).
* BUGFIX: prevent from possible data ingestion slowdown and query performance slowdown during [background merges of big parts](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#storage) on systems with small number of CPU cores (1 or 2 CPU cores). The issue has been introduced in [v1.85.0](https://docs.victoriametrics.com/victoriametrics/changelog/#v1850) when implementing [this feature](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/3337). See also [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/3790).
* BUGFIX: properly parse timestamps in milliseconds when [ingesting data via OpenTSDB telnet put protocol](https://docs.victoriametrics.com/victoriametrics/integrations/opentsdb/#sending-data-via-telnet). Previously timestamps in milliseconds were mistakenly multiplied by 1000. Thanks to @Droxenator for the [pull request](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/3810).
* BUGFIX: [MetricsQL](https://docs.victoriametrics.com/victoriametrics/metricsql/): do not add extrapolated points outside the real points when using [interpolate()](https://docs.victoriametrics.com/victoriametrics/metricsql/#interpolate) function. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/3816).


## [v1.87.1](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.87.1)

Released at 2023-02-09

**v1.87.x is a line of [LTS releases](https://docs.victoriametrics.com/victoriametrics/lts-releases/). It contains important up-to-date bugfixes.
The v1.87.x line will be supported for at least 12 months since [v1.87.0](https://docs.victoriametrics.com/victoriametrics/changelog/#v1870) release**

* FEATURE: [vmalert](https://docs.victoriametrics.com/victoriametrics/vmalert/): alerts state restore procedure was changed to become asynchronous. It doesn't block groups start anymore which significantly improves vmalert's startup time.
  This also means that `-remoteRead.ignoreRestoreErrors` command-line flag becomes deprecated now and will have no effect if configured.
  While previously state restore attempt was made for all the loaded alerting rules, now it is called only for alerts which became active after the first evaluation. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/2608).
* FEATURE: [vmui](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#vmui): optimize VMUI for use from smartphones and tablets. See [this feature request](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/3707).
* FEATURE: [vmui](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#vmui): add ability to search tenants in the drop-down list for the tenant selector. See [this feature request](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/3792).
* FEATURE: [vmui](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#vmui): add avg/min/max/last values to line legends and tooltips for graphs. See [this feature request](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/3706).
* FEATURE: [vmui](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#vmui): hide the default `per-job resource usage` dashboard if there is a custom dashboard exists at the directory specified via `-vmui.customDashboardsPath` command-line flag. See [this feature request](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/3740).

* BUGFIX: [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/): fix panic in [HashiCorp Nomad service discovery](https://docs.victoriametrics.com/victoriametrics/sd_configs/#nomad_sd_configs). Thanks to @mr-karan for the [pull request](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/3784).
* BUGFIX: [vmalert](https://docs.victoriametrics.com/victoriametrics/vmalert/): fix display of rules number per-group for groups with identical names in UI.
* BUGFIX: [vmalert](https://docs.victoriametrics.com/victoriametrics/vmalert/): prevent disabling state updates tracking per rule via setting values < 1. The minimum number of update states to track is now set to 1.
* BUGFIX: [vmalert](https://docs.victoriametrics.com/victoriametrics/vmalert/): properly update `debug` and `update_entries_limit` rule's params on config's hot-reload.
* BUGFIX: properly initialize the `vm_concurrent_insert_current` metric before exposing it. Previously this metric could be left uninitialized in some cases, e.g. its value was zero. This could lead to false alerts for the query `avg_over_time(vm_concurrent_insert_current[1m]) >= vm_concurrent_insert_capacity`. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/3761).
* BUGFIX: [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/): immediately cancel in-flight scrape requests during configuration reload when using [stream parsing mode](https://docs.victoriametrics.com/victoriametrics/vmagent/#stream-parsing-mode). Previously `vmagent` could wait for long time until all the in-flight requests are completed before reloading the configuration. This could significantly slow down configuration reload. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/3747).
* BUGFIX: [vmgateway](https://docs.victoriametrics.com/victoriametrics/vmgateway/): do not validate JWT signature if no public keys are provided. Previously this could result in the `error setting up jwt verification` error.
