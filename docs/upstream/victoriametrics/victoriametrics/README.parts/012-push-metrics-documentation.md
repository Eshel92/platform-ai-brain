<!-- Part 12 of 13 of victoriametrics/README.md (split because the page is big). -->

## Push metrics

All the VictoriaMetrics components support pushing their metrics exposed at `/metrics` page to remote storage in Prometheus text exposition format.
This functionality may be used instead of [classic Prometheus-like metrics scraping](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#how-to-scrape-prometheus-exporters-such-as-node-exporter)
if VictoriaMetrics components are located in isolated networks, so they cannot be scraped by local [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/).

The following command-line flags are related to pushing metrics from VictoriaMetrics components:

* `-pushmetrics.url` - the url to push metrics to. For example, `-pushmetrics.url=http://victoria-metrics:8428/api/v1/import/prometheus` instructs
  to push internal metrics to `/api/v1/import/prometheus` endpoint according to [these docs](#how-to-import-data-in-prometheus-exposition-format).
  The `-pushmetrics.url` can be specified multiple times. In this case metrics are pushed to all the specified urls.
  The url can contain basic auth params in the form `http://user:pass@hostname/api/v1/import/prometheus`.
  Metrics are pushed to the provided `-pushmetrics.url` in a compressed form with `Content-Encoding: gzip` request header.
  This allows reducing the required network bandwidth for metrics push. The compression can be disabled by passing `-pushmetrics.disableCompression` command-line flag.
* `-pushmetrics.extraLabel` - labels to add to all the metrics before sending them to every `-pushmetrics.url`. Each label must be specified in the format `label="value"`.
  It is OK to specify multiple `-pushmetrics.extraLabel` command-line flags. In this case all the specified labels
  are added to all the metrics before sending them to all the configured `-pushmetrics.url` addresses.
* `-pushmetrics.interval` - the interval between pushes. By default it is set to 10 seconds.
* `-pushmetrics.header` - an optional HTTP header to send to every `-pushmetrics.url`. For example, `-pushmetrics.header='Authorization: Basic foo'` instructs to send
  `Authorization: Basic foo` HTTP header with every request to every `-pushmetrics.url`. It is possible to set multiple `-pushmetrics.header` command-line flags
  for sending multiple different HTTP headers to `-pushmetrics.url`.

For example, the following command instructs VictoriaMetrics to push metrics from `/metrics` page to `https://maas.victoriametrics.com/api/v1/import/prometheus`
with `user:pass` [Basic auth](https://en.wikipedia.org/wiki/Basic_access_authentication). The `instance="foobar"` and `job="vm"` labels
are added to all the metrics before sending them to the remote storage:

```sh
/path/to/victoria-metrics \
  -pushmetrics.url=https://user:pass@maas.victoriametrics.com/api/v1/import/prometheus \
  -pushmetrics.extraLabel='instance="foobar"' \
  -pushmetrics.extraLabel='job="vm"'
```


## Caches

VictoriaMetrics uses various internal caches to optimize write and read load. Command-line flags `-memory.allowedPercent` and `-memory.allowedBytes` limit the amounts of memory that caches can use. To increase cache's memory limit, simply increase the amount of available memory to VictoriaMetrics, and it will automatically re-distribute it among the caches.

VictoriaMetrics stores caches on disk during graceful shutdown and re-loads them on startup. This helps VictoriaMetrics to catch up faster with the workload after restart. 
If VictoriaMetrics can't restore the cache from the disk, it will print the corresponding warning message in the logs. See [how to drop caches](https://docs.victoriametrics.com/victoriametrics/#cache-removal) if you need intentionally to remove the cache on startup.

> Note: due to specifics of the cache implementation, caches can reset automatically after changing the amount of available memory or CPUs.

VictoriaMetrics exposes various metrics for monitoring the cache usage. These metrics are available on [Grafana dashboards](https://docs.victoriametrics.com/victoriametrics/#monitoring) and are explained in [cache tuning docs](https://docs.victoriametrics.com/victoriametrics/#cache-tuning).

### Cache removal

Caches are stored in `<-storageDataPath>/cache` directory during graceful shutdown (e.g. when VictoriaMetrics is stopped by sending `SIGINT` signal), 
so they can be restored back during startup. To remove such caches on the next startup, use one of the following options:

* Manually remove the `<-storageDataPath>/cache` directory when VictoriaMetrics is stopped.
* Place `reset_cache_on_startup` file inside the `<-storageDataPath>/cache` directory before the restart of VictoriaMetrics.
  In this case VictoriaMetrics will automatically remove all the caches on the next start.
  See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/1447) for details.

It is also possible removing [rollup result cache](#rollup-result-cache) on startup by passing `-search.resetRollupResultCacheOnStartup` command-line flag to VictoriaMetrics.

### Rollup result cache

VictoriaMetrics caches query responses by default and utilizes the cache for future queries when possible. This improves performance for repeated queries
to [`/api/v1/query`](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#instant-query) and [`/api/v1/query_range`](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#range-query)
with the increasing `time`, `start` and `end` query args.

> For range query: the cache can be used for queries with the same expression and step.
> For instant query: the cache can be used for queries with the same expression that uses a lookbehind window larger than `-search.minWindowForInstantRollupOptimization` and specific functions such as `xx_over_time`, `increase`, `rate`. (For `rate`, the cache result may be inaccurate in edge cases, see [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/10098#issuecomment-3895011084) for details)

This cache may work incorrectly when ingesting historical data into VictoriaMetrics. See [these docs](#backfilling) for details.

The rollup cache can be disabled either globally by running VictoriaMetrics with `-search.disableCache` command-line flag
or on a per-query basis by passing `nocache=1` query arg to `/api/v1/query` and `/api/v1/query_range`.

See also [cache removal docs](#cache-removal).

### Cache tuning

The following metrics for each type of cache are exported at [`/metrics` page](#monitoring):

* `vm_cache_size_bytes` - the actual cache size
* `vm_cache_size_max_bytes` - cache size limit
* `vm_cache_requests_total` - the number of requests to the cache
* `vm_cache_misses_total` - the number of cache misses
* `vm_cache_entries` - the number of entries in the cache

Both Grafana [VictoriaMetrics - single-node](https://grafana.com/grafana/dashboards/10229)
and [VictoriaMetrics - cluster](https://grafana.com/grafana/dashboards/11176) dashboards
contain `Troubleshooting` section where the cache metrics are visualized. The `Cache usage %`
panel shows the percentage of used cache size from the allowed size by type. If the percentage
is below 100%, then no further tuning needed. The `Cache miss ratio` panel shows the percentage
of reads for which no value was found in the cache. If the cache utilization is 100% and there are
cache misses, then the cache is either not accepting new entries or evicting existing ones. Its
size may need to be increased.

> Please note, default cache sizes were carefully adjusted accordingly to the most
practical scenarios and workloads. Change the defaults only if you understand the implications
and vmstorage has enough free memory to accommodate new cache sizes.

To override the default values see command-line flag `-cacheExpireDuration` and flags with `-storage.cacheSize` prefix.
See the full description of [command-line flags](#list-of-command-line-flags).


## Data migration

### From VictoriaMetrics

The simplest way to migrate data from one single-node (source) to another (destination), or from one vmstorage node
to another is to do the following:

1. Stop the VictoriaMetrics (source) with `kill -INT`;
1. Copy (via [rsync](https://en.wikipedia.org/wiki/Rsync) or any other tool) the entire folder specified
via `-storageDataPath` from the source node to **an empty folder** at the destination node.
1. Once copy is done, stop the VictoriaMetrics (destination) with `kill -INT` and verify that
its `-storageDataPath` points to the copied folder from p.2;
1. Start the VictoriaMetrics (destination). The copied data should be now available.

Things to consider when copying data:

* Data formats between single-node and vmstorage node aren't compatible and can't be copied.
* Copying a data folder means complete replacement of the previous data on destination VictoriaMetrics.
* Data can't be mixed: make sure that the destination folder **is empty** before copying.

For scenarios like single-to-cluster, cluster-to-single, re-sharding or migrating only a fraction of data: 
[see how to migrate data from VictoriaMetrics via vmctl](https://docs.victoriametrics.com/victoriametrics/vmctl/victoriametrics/).

### From Single-node to Cluster

When, for some reason, the deployment needs to be switched from single-node to
cluster (such as the single-node can't be scaled vertically anymore, or
multitenancy becomes a requirement, etc.) the migration can be as simple as:

1. Restart the existing single-node with [vmselect RPC server enabled](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/#reading-from-single-node-victoriametrics)
1. Deploy an empty cluster next to the existing single-node.
1. Deploy higher-level `vmselect` and configure it to query both the existing
   single-node and the new cluster.
1. Start writing data to the cluster.
1. Stop writing data to the single-node.

This approach requires no data migration nor downtime (apart from restarting the
single-node at step 1). And once the single-node data becomes outside the
retention period, the single-node can be removed from the deployment.

Note that if you need to actually migrate data to cluster and/or modify it, you
will need to use
[vmctl](https://docs.victoriametrics.com/victoriametrics/vmctl/victoriametrics/)
instead.


### From other systems

Use [vmctl](https://docs.victoriametrics.com/victoriametrics/vmctl/) to migrate data from other systems to VictoriaMetrics.


## Backfilling

VictoriaMetrics accepts out-of-order historical data via [any supported ingestion method](#how-to-import-time-series-data)
without limitations. Only make sure that backfilled data is within of the configured [retention period](https://docs.victoriametrics.com/victoriametrics/#retention).

> See [how to backfill recording rules via vmalert](https://docs.victoriametrics.com/victoriametrics/vmalert/#rules-backfilling).

It is recommended disabling [query cache](#rollup-result-cache) with `-search.disableCache` command-line flag when writing
historical data with timestamps from the past, since the cache assumes that the data is written with
the current timestamps. Query cache can be enabled after the backfilling is complete.

An alternative solution is to query [/internal/resetRollupResultCache](https://docs.victoriametrics.com/victoriametrics/url-examples/#internalresetrollupresultcache)
after the backfilling is complete. This will reset the [query cache](#rollup-result-cache), which could contain incomplete data cached during the backfilling.

Yet another solution is to increase `-search.cacheTimestampOffset` flag value to disable caching
for data with timestamps close to the current time. Single-node VictoriaMetrics automatically resets response
cache when samples with timestamps older than `now - search.cacheTimestampOffset` are ingested to it.


## Data updates

VictoriaMetrics doesn't support updating already existing sample values to new ones. It stores all the ingested data points
for the same time series with identical timestamps. While it is possible substituting old time series with new time series via
[removal of old time series](#how-to-delete-time-series) and then [writing new time series](#backfilling), this approach
should be used only for one-off updates. It shouldn't be used for frequent updates because of non-zero overhead related to data removal.


## Replication

Single-node VictoriaMetrics doesn't support application-level replication. Use cluster version instead.
See [these docs](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/#replication-and-data-safety) for details.

Storage-level replication may be offloaded to durable persistent storage such as [Google Cloud disks](https://cloud.google.com/compute/docs/disks#pdspecs).

See also [high availability docs](#high-availability) and [backup docs](#backups).


## Backups

For backup configuration and setup, please refer to [vmbackup documentation](https://docs.victoriametrics.com/victoriametrics/vmbackup/).



## vmalert

A single-node VictoriaMetrics is capable of proxying requests to [vmalert](https://docs.victoriametrics.com/victoriametrics/vmalert/)
when `-vmalert.proxyURL` flag is set. Use this feature for the following cases:

* for proxying requests from [Grafana Alerting UI](https://grafana.com/docs/grafana/latest/alerting/);
* for accessing vmalerts UI through single-node VictoriaMetrics Web interface.

For accessing vmalerts UI through single-node VictoriaMetrics configure `-vmalert.proxyURL` flag and visit
`http://<victoriametrics-addr>:8428/vmalert/` link.


## Benchmarks

Note, that vendors (including VictoriaMetrics) are often biased when doing such tests. E.g. they try highlighting
the best parts of their product, while highlighting the worst parts of competing products.
So we encourage users and all independent third parties to conduct their benchmarks for various products
they are evaluating in production and publish the results.

As a reference, please see [benchmarks](https://docs.victoriametrics.com/victoriametrics/articles/#benchmarks) conducted by
VictoriaMetrics team. Please also see the [helm chart](https://github.com/VictoriaMetrics/benchmark)
for running ingestion benchmarks based on node_exporter metrics.


## Profiling

VictoriaMetrics provides handlers for collecting the following [Go profiles](https://blog.golang.org/profiling-go-programs):

* Memory profile. It can be collected with the following command (replace `0.0.0.0` with hostname if needed):

```sh
curl http://0.0.0.0:8428/debug/pprof/heap > mem.pprof
```

* CPU profile. It can be collected with the following command (replace `0.0.0.0` with hostname if needed):

```sh
curl http://0.0.0.0:8428/debug/pprof/profile > cpu.pprof
```

The command for collecting CPU profile waits for 30 seconds before returning.

The collected profiles may be analyzed with [go tool pprof](https://github.com/google/pprof).
It is safe sharing the collected profiles from security point of view, since they do not contain sensitive information.


## Third-party contributions

* [Prometheus -> VictoriaMetrics exporter #1](https://github.com/ryotarai/prometheus-tsdb-dump)
* [Prometheus -> VictoriaMetrics exporter #2](https://github.com/AnchorFree/tsdb-remote-write)
* [Prometheus Oauth proxy](https://gitlab.com/optima_public/prometheus_oauth_proxy) - see [this article](https://medium.com/@richard.holly/powerful-saas-solution-for-detection-metrics-c67b9208d362) for details.


## Contacts

Contact us with any questions regarding VictoriaMetrics at [info@victoriametrics.com](mailto:info@victoriametrics.com).


## Community and contributions

Feel free asking any questions regarding VictoriaMetrics:

* [Slack Inviter](https://slack.victoriametrics.com/) and [Slack channel](https://victoriametrics.slack.com/)
* [X (Twitter)](https://x.com/VictoriaMetrics/)
* [Linkedin](https://www.linkedin.com/company/victoriametrics/)
* [Reddit](https://www.reddit.com/r/VictoriaMetrics/)
* [Mastodon](https://mastodon.social/@victoriametrics/)
* Telegram:
  * [VictoriaMetrics_en](https://t.me/VictoriaMetrics_en) 
  * [VictoriaMetrics_ru](https://t.me/VictoriaMetrics_ru1)
  * [VictoriaLogs_ru](https://t.me/victorialogs_ru)
  * [VictoriaTraces_en](https://t.me/VictoriaTraces)

If you like VictoriaMetrics and want to contribute, then please [read these docs](https://docs.victoriametrics.com/victoriametrics/contributing/).


## Reporting bugs

Report bugs and propose new features in our [GitHub Issues](https://github.com/VictoriaMetrics/VictoriaMetrics/issues).


## Documentation

VictoriaMetrics documentation is available at [https://docs.victoriametrics.com/victoriametrics/](https://docs.victoriametrics.com/victoriametrics/).
It is built from `*.md` files located in [docs](https://github.com/VictoriaMetrics/VictoriaMetrics/tree/master/docs) folder
and gets automatically updated once changes are merged to [master](https://github.com/VictoriaMetrics/VictoriaMetrics/tree/master) branch.
To update the documentation follow the steps below:

* [Fork](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/about-forks)
  VictoriaMetrics repo and apply changes to the docs:
  * To update [the main page](https://docs.victoriametrics.com/victoriametrics/) modify [this file](https://github.com/VictoriaMetrics/VictoriaMetrics/blob/master/docs/victoriametrics/README.md).
  * To update other pages, apply changes to the corresponding file in [docs folder](https://github.com/VictoriaMetrics/VictoriaMetrics/tree/master/docs).
* If your changes contain an image then see [images in documentation](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#images-in-documentation).
* Create [a pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request)
  with proposed changes and wait for it to be merged. See [pull request checklist](https://docs.victoriametrics.com/victoriametrics/contributing/#pull-request-checklist).

Requirements for changes to docs:

* Keep backward compatibility of existing links. Avoid changing anchors or deleting pages as they could have been
  used or posted in other docs, GitHub issues, Stack Overflow answers, etc.
* Keep docs clear, concise and simple. Try using as simple wording as possible, without sacrificing clarity.
* Keep docs consistent. When modifying existing docs, verify that other places referencing to this doc are still relevant.
* Prefer improving the existing docs instead of adding new ones.
* Use absolute links. This simplifies moving docs between different files.

Periodically run `make spellcheck` - this command detects spelling errors at `docs/` folder. Please fix the found spelling errors
and commit the fixes in a separate commit.

### Images in documentation

Please, keep image size and number of images per single page low. Keep the docs page as lightweight as possible.

Image files must be placed in the same folder as the doc itself and they must have the same prefix as the doc filename.
For example, all the images for `docs/foo/bar.md` should have filenames starting from `docs/foo/bar`.
This simplifies lifetime management of the images:

* when the corresponding doc is removed, then it is clear how to remove the associated images
* when the corresponding doc is renamed, then it is clear how to rename the associated images.

If the page needs to have many images, consider using WEB-optimized image format [webp](https://developers.google.com/speed/webp).
When adding a new doc with many images use `webp` format right away. Or use a Makefile command below to
convert already existing images at `docs` folder automatically to `web` format:

```sh
make docs-images-to-webp
```

Once conversion is done, update the path to images in your docs and verify everything is correct.
