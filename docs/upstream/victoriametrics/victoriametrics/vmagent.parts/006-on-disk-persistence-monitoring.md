<!-- Part 6 of 8 of victoriametrics/vmagent.md (split because the page is big). -->

## On-disk persistence

`vmagent` stores pending data that cannot be sent to the configured remote storage systems in a timely manner.
By default, `vmagent` writes all the pending data to the folder configured via `-remoteWrite.tmpDataPath` cmd-line flag
until this data is sent to the configured `-remoteWrite.url` systems or until the folder becomes full.
The maximum data size that can be saved to `-remoteWrite.tmpDataPath` per every configured `-remoteWrite.url` can be
limited via `-remoteWrite.maxDiskUsagePerURL` command-line flag. When this limit is reached, `vmagent` drops the oldest
data from disk in order to save newly ingested data.

The folder structure of persisted data is as follows:

```
<remoteWrite.tmpDataPath>
└── persistent-queue
    └── 1_B9EB7BE220B91E9D
```

Each remote write URL corresponds to a folder similar to `1_B9EB7BE220B91E9D`.

It's generated based on the following information:

1. The **sequence order** of the remote write URL command-line flags, starting from **1**.
2. The **hash result** of the remote write URL itself, excluding query parameters and fragments.

For example, for the remote write configs:

```
-remoteWrite.url=http://example-1:8428/prometheus/api/v1/write?foo=bar#baz
-remoteWrite.url=http://user:pass@example-2:8428/prometheus/api/v1/write?qux=quux#quuz
```

vmagent will generate the following persistent queue folders:

```bash
# 1_<hash(http://example-1:8428/prometheus/api/v1/write)>, query parameters foo=bar and fragment baz are removed.
1_BA6E4303DCFA0D45
# 2_<hash(http://user:pass@example-2:8428/prometheus/api/v1/write)>, query parameters qux=quux and fragment quuz are removed.
2_0AAFDF53E314A72A
```

### Manual on-disk persistence paths

By default, `vmagent` [generates persistent queue directory names](https://docs.victoriametrics.com/victoriametrics/vmagent/#on-disk-persistence)
from the position and the value of every `-remoteWrite.url`. So adding, removing, reordering or editing `-remoteWrite.url` flags
changes the directory names, and pending data in the old directories is no longer sent: it is dropped as a dangling queue on the next start,
unless `-remoteWrite.keepDanglingQueues` is set.
If you plan to modify `-remoteWrite.url` flags often, consider setting the persistent queue directory
for each `-remoteWrite.url` manually via `-remoteWrite.queuePath`{{% available_from "v1.156.0" %}} command-line flag.

`-remoteWrite.queuePath` must be set once per `-remoteWrite.url`; the n-th `-remoteWrite.queuePath` is used by the n-th `-remoteWrite.url`.
For example:

```bash
./bin/vmagent \
  -remoteWrite.url=http://url-0 \
  -remoteWrite.url=http://url-1 \
  -remoteWrite.url=http://url-2 \
  -remoteWrite.queuePath=/vmagent-data/url-0 \
  -remoteWrite.queuePath=/vmagent-data/url-1 \
  -remoteWrite.queuePath=/vmagent-data/url-2
```

Now `-remoteWrite.url=http://url-1` can be removed together with `-remoteWrite.queuePath=/vmagent-data/url-1`,
and `http://url-2` keeps its pending data in `/vmagent-data/url-2`.

Keep in mind the following when using `-remoteWrite.queuePath`:

* Every `-remoteWrite.queuePath` must point to a dedicated directory used only by a single `-remoteWrite.url`.
  `vmagent` deletes all the contents of a directory that doesn't contain a valid persistent queue.
* `vmagent` doesn't track which `-remoteWrite.url` a directory belongs to. If a directory is assigned to another `-remoteWrite.url`,
  pending data from it is sent to that new `-remoteWrite.url`.
* `vmagent` doesn't remove directories that are no longer referenced by any `-remoteWrite.queuePath`. Delete them manually when they aren't needed.
* `-remoteWrite.tmpDataPath` is still created and used for internal files, but `vmagent` doesn't remove
  [dangling queues](https://docs.victoriametrics.com/victoriametrics/vmagent/#on-disk-persistence) from it.

To keep pending data when switching from auto-generated directories to `-remoteWrite.queuePath`, pass the existing directory as the flag value,
for example `-remoteWrite.queuePath=<remoteWrite.tmpDataPath>/persistent-queue/1_B9EB7BE220B91E9D`.
Auto-generated directories not listed in `-remoteWrite.queuePath` stay on disk and are no longer sent, so remove them manually when they aren't needed.

### On-disk persistence and data processing order

By default, vmagent processes data in FIFO order. If data has been written to the on-disk queue,
it must be flushed to the remote storage before newly ingested data can be forwarded there.
During long outages, vmagent may accumulate large amounts of data in the file-based queue,
which can introduce a significant lag between the moment data is collected by vmagent and the
moment it becomes visible at the remote storage.

This behavior can be changed with the `-remoteWrite.inmemoryQueues` {{% available_from "v1.146.0" %}} command-line flag.
When set to a non-zero value, vmagent starts the given number of additional workers,
which send only recently ingested data from the in-memory queue, while the workers configured via `-remoteWrite.queues` drain the file-based backlog concurrently.
This reduces the delivery lag for fresh samples after remote storage outages or slowdowns. The flag can be set individually per each `-remoteWrite.url`.
See how the [in-memory and file-based queues manage blocks](https://victoriametrics.com/blog/vmagent-how-it-works/#in-memory-queue) for implementation details.

Note that these workers are started in addition to the workers configured via `-remoteWrite.queues`, so the total number of concurrent connections to
the remote storage becomes the sum of both flags. Take this into account if the remote storage limits the number of concurrent requests.

This flag has the following possible limitations:

* Samples may arrive at the remote storage out of order, since recent data can be delivered before the older backlogged data.
  Do not use this option if the remote storage doesn't accept out-of-order samples.
* Recent data isn't guaranteed to take the fast path: if the in-memory queue  is full,
  newly ingested data is still written to the file-based queue and is delivered in FIFO order by the generic workers.

### Disabling On-disk persistence

There are cases when it is better to disable on-disk persistence for pending data on the `vmagent` side:

* When the persistent disk performance isn't enough for the given data processing rate.
* When clients can buffer pending data more efficiently on their side than on the `vmagent` side (on the `-remoteWrite.tmpDataPath` folder).
* When the data is already buffered at [Kafka](https://docs.victoriametrics.com/victoriametrics/integrations/kafka/#reading-metrics) or [Google PubSub](https://docs.victoriametrics.com/victoriametrics/integrations/pubsub/#reading-metrics).
* When dropping pending data is better than buffering it.

In this case, the `-remoteWrite.disableOnDiskQueue` command-line flag can be passed to `vmagent` for each configured `-remoteWrite.url`.
`vmagent` works in the following way if the corresponding remote storage system at `-remoteWrite.url` cannot keep up with the data ingestion rate
and the `-remoteWrite.disableOnDiskQueue` command-line flag is set:

* It returns `429 Too Many Requests` HTTP error to clients, which send data to `vmagent` via [supported HTTP endpoints](#how-to-push-data-to-vmagent).
  If the `-remoteWrite.dropSamplesOnOverload` command-line flag is set or if multiple `-remoteWrite.url` command-line flags are set,
  then the ingested samples are silently dropped instead of returning an error to clients.
* It suspends consuming data from [Kafka](https://docs.victoriametrics.com/victoriametrics/integrations/kafka/#reading-metrics) or [Google PubSub](https://docs.victoriametrics.com/victoriametrics/integrations/pubsub/) until the remote storage becomes available.
  If the `-remoteWrite.dropSamplesOnOverload` command-line flag is set or if multiple `-remoteWrite.disableOnDiskQueue` command-line flags are set
  for different `-remoteWrite.url` options, then the fetched samples are silently dropped instead of suspending data consumption from Kafka or Google PubSub.
* It drops samples pushed to `vmagent` via non-HTTP protocols and logs the error. Pass `-remoteWrite.dropSamplesOnOverload` command-line flag in order
  to suppress error messages in this case.
* It drops samples [scraped from Prometheus-compatible targets](#how-to-collect-metrics-in-prometheus-format), because it is better from operations perspective
  to drop samples instead of blocking the scrape process.
* It drops [stream aggregation](https://docs.victoriametrics.com/victoriametrics/stream-aggregation/) output samples, because it is better from an operations perspective
  to drop output samples instead of blocking the stream aggregation process.

The number of dropped samples because of overloaded remote storage can be [monitored](#monitoring) via `vmagent_remotewrite_samples_dropped_total` metric.
The number of unsuccessful attempts to send data to overloaded remote storage can be [monitored](#monitoring) via `vmagent_remotewrite_push_failures_total` metric.

Running `vmagent` on hosts with more RAM or increasing the value for `-memory.allowedPercent` may reduce the number of unsuccessful attempts or dropped samples
on spiky workloads, since `vmagent` may buffer more data in memory before returning the error or dropping data.

`vmagent` still may write pending in-memory data to `-remoteWrite.tmpDataPath` on graceful shutdown
if `-remoteWrite.disableOnDiskQueue` command-line flag is specified. It may also read buffered data from `-remoteWrite.tmpDataPath`
on startup.

When the `-remoteWrite.disableOnDiskQueue` command-line flag is set, `vmagent` may send the same samples multiple times to the configured remote storage
if it cannot keep up with the data ingestion rate. In this case [deduplication](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#deduplication)
must be enabled on all the configured remote storage systems.


## Cardinality limiter

By default, `vmagent` doesn't limit the number of time series each scrape target can expose.
The limit can be enforced in the following places:

* Via `-promscrape.seriesLimitPerTarget` command-line flag. This limit is applied individually
  to all the scrape targets defined in the file pointed to by `-promscrape.config`.
* Via `series_limit` config option at [scrape_config](https://docs.victoriametrics.com/victoriametrics/sd_configs/#scrape_configs) section.
  The `series_limit` allows overriding the `-promscrape.seriesLimitPerTarget` on a per-`scrape_config` basis.
  If `series_limit` is set to `0` or to a negative value, then it isn't applied to the given `scrape_config`,
  even if the `-promscrape.seriesLimitPerTarget` command-line flag is set.
* Via `__series_limit__` label, which can be set with [relabeling](https://docs.victoriametrics.com/victoriametrics/relabeling/) at `relabel_configs` section.
  The `__series_limit__` allows overriding the `series_limit` on a per-target basis.
  If `__series_limit__` is set to `0` or to a negative value, then it isn't applied to the given target.
  Typical use case: to set the limit via [Kubernetes annotations](https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/)
  for targets, which may expose too many time series.

Scraped metrics are dropped for time series exceeding the given limit for the 24h time window.
`vmagent` creates the following additional per-target metrics for targets with non-zero series limit:

* `scrape_series_limit_samples_dropped` - the number of dropped samples during the scrape when the unique series limit is exceeded.
* `scrape_series_limit` - the series limit for the given target.
* `scrape_series_current` - the current number of series for the given target.

These metrics are automatically sent to the configured `-remoteWrite.url` alongside the scraped per-target metrics.

These metrics allow building the following alerting rules:

* `scrape_series_current / scrape_series_limit > 0.9` - alerts when the number of series exposed by the target reaches 90% of the limit.
* `sum_over_time(scrape_series_limit_samples_dropped[1h]) > 0` - alerts when some samples are dropped because the series limit on a particular target is reached.

See also `sample_limit` option at [scrape_config section](https://docs.victoriametrics.com/victoriametrics/sd_configs/#scrape_configs).

By default, `vmagent` doesn't limit the number of time series written to remote storage systems specified at `-remoteWrite.url`.
The limit can be enforced by setting the following command-line flags:

* `-remoteWrite.maxHourlySeries` - limits the number of unique time series `vmagent` can write to remote storage systems during the last hour.
  Useful for limiting the number of active time series.
* `-remoteWrite.maxDailySeries` - limits the number of unique time series `vmagent` can write to remote storage systems during the last day.
  Useful for limiting daily churn rate.

It is possible to use `-1` as a value for these flags{{% available_from "v1.140.0" %}} in order to enable series tracking while setting the limit to the maximum possible value. 
This is useful for estimating the number of unique series written to remote storage systems without enforcing limits.

Both limits can be set simultaneously. If any of these limits are reached, then samples for the new time series are dropped instead of being sent to remote storage systems. A sample of dropped series is logged with a `WARNING` level message.

`vmagent` exposes the following metrics at `http://vmagent:8429/metrics` page (see [monitoring docs](#monitoring) for details):

* `vmagent_hourly_series_limit_rows_dropped_total` - the number of metrics dropped due to exceeding the hourly limit on the number of unique time series.
* `vmagent_hourly_series_limit_max_series` - the hourly series limit set via `-remoteWrite.maxHourlySeries`.
* `vmagent_hourly_series_limit_current_series` - the current number of unique series registered during the last hour.
* `vmagent_daily_series_limit_rows_dropped_total` - the number of metrics dropped due to exceeding the daily limit on the number of unique time series.
* `vmagent_daily_series_limit_max_series` - the daily series limit set via `-remoteWrite.maxDailySeries`.
* `vmagent_daily_series_limit_current_series` - the current number of unique series registered during the last day.

These limits are approximate, so `vmagent` can underflow or overflow them by a small percentage (usually less than 1%).

See also:
- [Cardinality Explorer](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#cardinality-explorer).
- [vmestimator](https://docs.victoriametrics.com/victoriametrics/vmestimator/).


## Monitoring

`vmagent` exports various metrics in Prometheus exposition format at `http://vmagent-host:8429/metrics` page.
We recommend setting up regular scraping of this page either through `vmagent` itself or by a Prometheus-compatible scraper,
so that the exported metrics may be analyzed later.

If you use Google Cloud Managed Prometheus for scraping metrics from VictoriaMetrics components, then pass `-metrics.exposeMetadata`
command-line to them, so they add `TYPE` and `HELP` comments for each exposed metric on the `/metrics` page.
See [these docs](https://cloud.google.com/stackdriver/docs/managed-prometheus/troubleshooting#missing-metric-type) for details.

Use the official [Grafana dashboard](https://grafana.com/grafana/dashboards/12683) for the `vmagent` state overview.
Graphs on this dashboard contain useful hints - hover the `i` icon at the top left corner of each graph in order to read it.
If you have suggestions for improvements or have found a bug, please open an issue on [GitHub](https://github.com/VictoriaMetrics/VictoriaMetrics/issues)
, or add a review to the dashboard.

`vmagent` also exports the status for various targets at the following pages:

* `http://vmagent-host:8429/targets`. This page shows the current status for every active target.
* `http://vmagent-host:8429/service-discovery`. This page shows the list of discovered targets with the discovered `__meta_*` labels
  according to [these docs](https://docs.victoriametrics.com/victoriametrics/sd_configs/).
  This page may help with debugging target [relabeling](https://docs.victoriametrics.com/victoriametrics/relabeling/).
* `http://vmagent-host:8429/api/v1/targets`. This handler returns a JSON response
  compatible with [the corresponding page from Prometheus API](https://prometheus.io/docs/prometheus/latest/querying/api/#targets).
* `http://vmagent-host:8429/ready`. This handler returns an HTTP 200 status code when `vmagent` finishes
  its initialization for all the [service_discovery configs](https://docs.victoriametrics.com/victoriametrics/sd_configs/).
  It may be useful to perform a `vmagent` rolling update without any scrape loss.
