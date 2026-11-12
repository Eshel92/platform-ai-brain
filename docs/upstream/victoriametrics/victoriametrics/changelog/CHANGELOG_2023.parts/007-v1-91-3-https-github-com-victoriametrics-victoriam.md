<!-- Part 7 of 14 of victoriametrics/changelog/CHANGELOG_2023.md (split because the page is big). -->

## [v1.91.3](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.91.3)

Released at 2023-06-30

* SECURITY: upgrade Go builder from Go1.20.4 to Go1.20.5. See [the list of issues addressed in Go1.20.5](https://github.com/golang/go/issues?q=milestone%3AGo1.20.5+label%3ACherryPickApproved).

* BUGFIX: [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/): fix possible panic at shutdown when [stream aggregation](https://docs.victoriametrics.com/victoriametrics/stream-aggregation/) is enabled. See [this pull request](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/4407) for details.
* BUGFIX: [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/): fixed service name detection for [consulagent service discovery](https://docs.victoriametrics.com/victoriametrics/sd_configs/#consulagent_sd_configs) in case of a difference in service name and service id. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/4390) for details.
* BUGFIX: [vmalert](https://docs.victoriametrics.com/victoriametrics/vmalert/): retry all errors except 4XX status codes while pushing via remote-write to the remote storage. Previously, errors like broken connection could prevent vmalert from retrying the request.
* BUGFIX: [vmalert](https://docs.victoriametrics.com/victoriametrics/vmalert/): properly interrupt retry attempts on vmalert shutdown. Before, vmalert could have waited for all retries to finish for shutdown.
* BUGFIX: [vmbackupmanager](https://docs.victoriametrics.com/victoriametrics/vmbackupmanager/): fix an issue with `vmbackupmanager` not being able to restore data from a backup stored in GCS. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/4420) for details.
* BUGFIX: [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/): properly return error from [/api/v1/query](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#instant-query) and [/api/v1/query_range](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#range-query) at `vmselect` when the `-search.maxSamplesPerQuery` or `-search.maxSamplesPerSeries` [limit](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/#resource-usage-limits) is exceeded. Previously incomplete response could be returned without the error if `vmselect` runs with `-replicationFactor` greater than 1. See [this pull request](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/4472).
* BUGFIX: [storage](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/): prevent from possible crashloop after the migration from versions below `v1.90.0` to newer versions. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/4336) for details.
* BUGFIX: [vmui](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#vmui): fix a memory leak issue associated with chart updates. See [this pull request](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/4455).
* BUGFIX: [vmbackupmanager](https://docs.victoriametrics.com/victoriametrics/vmbackupmanager/): fix removing storage data dir before restoring from backup.
* BUGFIX: vmselect: wait for all vmstorage nodes to respond when the `-replicationFactor` flag is set bigger than > 1. Before, vmselect could have [skip waiting for the slowest replicas](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/711) to respond. This could have resulted in issues illustrated [here](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/1207). Now, this optimization is disabled by default and could be re-enabled by passing `-search.skipSlowReplicas` cmd-line flag to vmselect. See more details [here](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/4538). 



## [v1.91.2](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.91.2)

Released at 2023-06-02

* BUGFIX: [vmalert](https://docs.victoriametrics.com/victoriametrics/vmalert/): fix nil map assignment panic in runtime introduced in this [change](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/4341).


## [v1.91.1](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.91.1)

Released at 2023-06-01

* FEATURE:[vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/): Adds `follow_redirects` at service discovery level of scrape configuration. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/4282). Thanks to @Haleygo for [the pull request](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/4286).
* FEATURE: vmselect: Decreases startup time for vmselect with a big number of vmstorage nodes. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/4364). Thanks to @Haleygo for [the pull request](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/4366).

* BUGFIX: [vmalert](https://docs.victoriametrics.com/victoriametrics/vmalert/): Properly form path to static assets in WEB UI if `http.pathPrefix` set. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/4349).
* BUGFIX: [vmalert](https://docs.victoriametrics.com/victoriametrics/vmalert/): Properly set datasource query params. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/4340). Thanks to @gsakun for [the pull request](https://github.com/VictoriaMetrics/VictoriaMetrics/pull/4341).
* BUGFIX: [vmalert](https://docs.victoriametrics.com/victoriametrics/vmalert/): properly return empty slices instead of nil for `/api/v1/rules` for groups with present name but absent `rules`. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/4221).
* BUGFIX: [vmauth](https://docs.victoriametrics.com/victoriametrics/vmauth/): Properly handle LOCAL command for proxy protocol. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/3335#issuecomment-1569864108).
* BUGFIX: [vmbackupmanager](https://docs.victoriametrics.com/victoriametrics/vmbackupmanager/): Fixes crash on startup. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/4378).
* BUGFIX: [vmui](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#vmui): fix bug with custom URL in global settings not respecting tenantID change. See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/4322).
