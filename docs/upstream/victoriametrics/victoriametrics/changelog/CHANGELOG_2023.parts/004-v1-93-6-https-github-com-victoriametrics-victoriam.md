<!-- Part 4 of 14 of victoriametrics/changelog/CHANGELOG_2023.md (split because the page is big). -->

## [v1.93.6](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.93.6)

Released at 2023-10-16

**v1.93.x is a line of [LTS releases](https://docs.victoriametrics.com/victoriametrics/lts-releases/). It contains important up-to-date bugfixes.
The v1.93.x line will be supported for at least 12 months since [v1.93.0](https://docs.victoriametrics.com/victoriametrics/changelog/#v1930) release**

* SECURITY: upgrade Go builder from Go1.21.1 to Go1.21.3. See [the list of issues addressed in Go1.21.2](https://github.com/golang/go/issues?q=milestone%3AGo1.21.2+label%3ACherryPickApproved) and [the list of issues addressed in Go1.21.3](https://github.com/golang/go/issues?q=milestone%3AGo1.21.3+label%3ACherryPickApproved).

* BUGFIX: [vmalert](https://docs.victoriametrics.com/victoriametrics/vmalert/): strip sensitive information such as auth headers or passwords from datasource, remote-read, remote-write or notifier URLs in log messages or UI. This behavior is by default and is controlled via `-datasource.showURL`, `-remoteRead.showURL`, `remoteWrite.showURL` or `-notifier.showURL` cmd-line flags. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/5044).
* BUGFIX: `vmselect`: improve performance and memory usage during query processing on machines with big number of CPU cores. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/5087) for details.
* BUGFIX: [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): bump hard-coded limit for search query size at `vmstorage` from 1MB to 5MB. The change should be more suitable for real-world scenarios and protect vmstorage from excessive memory usage. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/5154) for details
* BUGFIX: [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/): fix vmagent ignoring configuration reload for streaming aggregation if it was started with empty streaming aggregation config. Thanks to @aluode99 for the [pull request](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/5178).
* BUGFIX: [vmbackup](https://docs.victoriametrics.com/victoriametrics/vmbackup/): properly copy `appliedRetention.txt` files inside `<-storageDataPath>/{data}` folders during [incremental backups](https://docs.victoriametrics.com/victoriametrics/vmbackup/#incremental-backups). Previously the new `appliedRetention.txt` could be skipped during incremental backups, which could lead to increased load on storage after restoring from backup. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/5005).
* BUGFIX: [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/): suppress `context canceled` error messages in logs when `vmagent` is reloading service discovery config. This error could appear starting from [v1.93.5](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.93.5). See [this PR](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/5048).
* BUGFIX: [MetricsQL](https://docs.victoriametrics.com/victoriametrics/metricsql/): allow passing [median_over_time](https://docs.victoriametrics.com/victoriametrics/metricsql/#median_over_time) to [aggr_over_time](https://docs.victoriametrics.com/victoriametrics/metricsql/#aggr_over_time). See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/5034).
* BUGFIX: [vminsert](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): fix ingestion via [multitenant url](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/#multitenancy-via-labels) for opentsdbhttp. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/5061). The bug has been introduced in [v1.93.2](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.93.2).
* BUGFIX: [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/): fix support of legacy DataDog agent, which adds trailing slashes to urls. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/5078). Thanks to @maxb for spotting the issue.


## [v1.93.5](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.93.5)

Released at 2023-09-19

**v1.93.x is a line of [LTS releases](https://docs.victoriametrics.com/victoriametrics/lts-releases/). It contains important up-to-date bugfixes.
The v1.93.x line will be supported for at least 12 months since [v1.93.0](https://docs.victoriametrics.com/victoriametrics/changelog/#v1930) release**

* BUGFIX: [storage](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/): prevent from livelock when [forced merge](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#forced-merge) is called under high data ingestion. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/4987).
* BUGFIX: [Graphite Render API](https://docs.victoriametrics.com/victoriametrics/integrations/graphite/#render-api): correctly return `null` instead of `Inf` in JSON query responses. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/3783).
* BUGFIX: [vmbackup](https://docs.victoriametrics.com/victoriametrics/vmbackup/): properly copy `parts.json` files inside `<-storageDataPath>/{data,indexdb}` folders during [incremental backups](https://docs.victoriametrics.com/victoriametrics/vmbackup/#incremental-backups). Previously the new `parts.json` could be skipped during incremental backups, which could lead to inability to restore from the backup. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/5005). This issue has been introduced in [v1.90.0](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.90.0).
* BUGFIX: [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/): properly close connections to Kubernetes API server after the change in `selectors` or `namespaces` sections of [kubernetes_sd_configs](https://docs.victoriametrics.com/victoriametrics/sd_configs/#kubernetes_sd_configs). Previously `vmagent` could continue polling Kubernetes API server with the old `selectors` or `namespaces` configs additionally to polling new configs. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/4850).
* BUGFIX: [vmauth](https://docs.victoriametrics.com/victoriametrics/vmauth/): prevent configuration reloading if there were no changes in config. This improves memory usage when `-configCheckInterval` cmd-line flag is configured and config has extensive list of regexp expressions requiring additional memory on parsing. 


## [v1.93.4](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.93.4)

Released at 2023-09-10

**v1.93.x is a line of [LTS releases](https://docs.victoriametrics.com/victoriametrics/lts-releases/). It contains important up-to-date bugfixes.
The v1.93.x line will be supported for at least 12 months since [v1.93.0](https://docs.victoriametrics.com/victoriametrics/changelog/#v1930) release**

* SECURITY: upgrade Go builder from Go1.21.0 to Go1.21.1. See [the list of issues addressed in Go1.20.6](https://github.com/golang/go/issues?q=milestone%3AGo1.21.1+label%3ACherryPickApproved).

* BUGFIX: [vminsert enterprise](https://docs.victoriametrics.com/victoriametrics/enterprise/): properly parse `/insert/multitenant/*` urls, which have been broken since [v1.93.2](#v1932). See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/4947).
* BUGFIX: properly build production armv5 binaries for `GOARCH=arm`. This has been broken after the upgrading of Go builder to Go1.21.0. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/4965).
* BUGFIX: [vmselect](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): return `503 Service Unavailable` status code when [partial responses](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/#cluster-availability) are denied and some of `vmstorage` nodes are temporarily unavailable. Previously `422 Unprocessable Entity` status code was mistakenly returned in this case, which could prevent from automatic recovery by re-sending the request to healthy cluster replica in another availability zone.
* BUGFIX: [vmalert](https://docs.victoriametrics.com/victoriametrics/vmalert/): fix the bug when Group's `params` fields with multiple values were overriding each other instead of adding up. The bug was introduced in [this commit](https://github.com/VictoriaMetrics/VictoriaMetrics/commit/eccecdf177115297fa1dc4d42d38e23de9a9f2cb) starting from [v1.91.1](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.91.1). See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/4908).
* BUGFIX: [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/): fix possible corruption of labels in the collected samples if `-remoteWrite.label` is set together with multiple `-remoteWrite.url` options. The bug has been introduced in [v1.93.1](#v1931). See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/4972).


## [v1.93.3](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.93.3)

Released at 2023-09-02

**v1.93.x is a line of [LTS releases](https://docs.victoriametrics.com/victoriametrics/lts-releases/). It contains important up-to-date bugfixes.
The v1.93.x line will be supported for at least 12 months since [v1.93.0](https://docs.victoriametrics.com/victoriametrics/changelog/#v1930) release**

* BUGFIX: [vminsert](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): properly close broken vmstorage connection during [read-only state](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/#readonly-mode) checks at `vmstorage`. Previously it wasn't properly closed, which prevents restoring `vmstorage` node from read-only mode. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/4870).
* BUGFIX: [vmstorage](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/):  prevent from breaking `vmselect` -> `vmstorage` RPC communication when `vmstorage` returns an empty label name at `/api/v1/labels` request. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/4932).


## [v1.93.2](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.93.2)

Released at 2023-09-01

**v1.93.x is a line of [LTS releases](https://docs.victoriametrics.com/victoriametrics/lts-releases/). It contains important up-to-date bugfixes.
The v1.93.x line will be supported for at least 12 months since [v1.93.0](https://docs.victoriametrics.com/victoriametrics/changelog/#v1930) release**

* BUGFIX: [build](https://docs.victoriametrics.com/victoriametrics/): fix Docker builds for old Docker releases. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/4907).
* BUGFIX: [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/): consistently set `User-Agent` header to `vm_promscrape` during scraping with enabled or disabled [stream parsing mode](https://docs.victoriametrics.com/victoriametrics/vmagent/#stream-parsing-mode). See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/4884).
* BUGFIX: [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/): consistently set timeout for scraping with enabled or disabled [stream parsing mode](https://docs.victoriametrics.com/victoriametrics/vmagent/#stream-parsing-mode). See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/4847).
* BUGFIX: [vmalert](https://docs.victoriametrics.com/victoriametrics/vmalert/): correctly reuse HTTP request object on `EOF` retries when querying the configured datasource. Previously, there was a small chance that query retry wouldn't succeed.
* BUGFIX: [vmselect](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): correctly handle requests with `/select/multitenant` prefix. Such requests must be rejected since vmselect does not support multitenancy endpoint. Previously, such requests were causing panic. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/4910).
* BUGFIX: [vminsert](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): properly check for [read-only state](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/#readonly-mode) at `vmstorage`. Previously it wasn't properly checked, which could lead to increased resource usage and data ingestion slowdown when some of `vmstorage` nodes are in read-only mode. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/4870).


## [v1.93.1](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.93.1)

Released at 2023-08-23

**v1.93.x is a line of [LTS releases](https://docs.victoriametrics.com/victoriametrics/lts-releases/). It contains important up-to-date bugfixes.
The v1.93.x line will be supported for at least 12 months since [v1.93.0](https://docs.victoriametrics.com/victoriametrics/changelog/#v1930) release**

* BUGFIX: prevent from possible data loss during `indexdb` rotation. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/4873) for details.
* BUGFIX: do not allow starting VictoriaMetrics components with improperly set boolean command-line flags in the form `-boolFlagName value`, since this leads to silent incomplete flags' parsing. This form should be replaced with `-boolFlagName=value`. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/4845).
* BUGFIX: [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/): properly set labels from `-remoteWrite.label` command-line flag just before sending samples to the configured `-remoteWrite.url` according to [these docs](https://docs.victoriametrics.com/victoriametrics/vmagent/#adding-labels-to-metrics). Previously these labels were incorrectly set before [the relabeling](https://docs.victoriametrics.com/victoriametrics/relabeling/) configured via `-remoteWrite.urlRelabelConfigs` and [the stream aggregation](https://docs.victoriametrics.com/victoriametrics/stream-aggregation/) configured via `-remoteWrite.streamAggr.config`, so these labels could be lost or incorrectly transformed before sending the samples to remote storage. The fix allows using `-remoteWrite.label` for identifying `vmagent` instances in [cluster mode](https://docs.victoriametrics.com/victoriametrics/vmagent/#scraping-big-number-of-targets). See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/4247) and [these docs](https://docs.victoriametrics.com/victoriametrics/stream-aggregation/#cluster-mode) for more details.
* BUGFIX: remove `DEBUG` logging when parsing `if` filters inside [relabeling rules](https://docs.victoriametrics.com/victoriametrics/relabeling/#relabeling-enhancements) and when parsing `match` filters inside [stream aggregation rules](https://docs.victoriametrics.com/victoriametrics/stream-aggregation/).
* BUGFIX: properly replace `:` chars in label names with `_` when `-usePromCompatibleNaming` command-line flag is passed to `vmagent`, `vminsert` or single-node VictoriaMetrics. This addresses [this comment](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/3113#issuecomment-1275077071).
* BUGFIX: [vmbackup](https://docs.victoriametrics.com/victoriametrics/vmbackup/): correctly check if specified `-dst` belongs to specified `-storageDataPath`. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/4837).
* BUGFIX: [vmctl](https://docs.victoriametrics.com/victoriametrics/vmctl/): don't interrupt the migration process if no metrics were found for a specific tenant. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/4796).
