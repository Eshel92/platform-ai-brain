<!-- Part 9 of 13 of victoriametrics/README.md (split because the page is big). -->

## Downsampling

[VictoriaMetrics Enterprise](https://docs.victoriametrics.com/victoriametrics/enterprise/) supports multi-level downsampling via `-downsampling.period=offset:interval` command-line flag.
This command-line flag instructs leaving the last sample per each `interval` for [time series](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#time-series)
[samples](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#raw-samples) older than the `offset`. The `offset` must be a multiple of `interval`. For example, `-downsampling.period=30d:5m` instructs leaving the last sample
per each 5-minute interval for samples older than 30 days, while the rest of samples are dropped.

The `-downsampling.period` command-line flag can be specified multiple times in order to apply different downsampling levels for different time ranges (aka multi-level downsampling).
For example, `-downsampling.period=30d:5m,180d:1h` instructs leaving the last sample per each 5-minute interval for samples older than 30 days,
while leaving the last sample per each 1-hour interval for samples older than 180 days.

VictoriaMetrics supports{{% available_from "v1.100.0" %}} configuring independent downsampling per different sets of [time series](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#time-series)
via `-downsampling.period=filter:offset:interval` syntax. In this case the given `offset:interval` downsampling is applied only to time series matching the given `filter`.
The `filter` can contain arbitrary [series filter](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#filtering).
For example, `-downsampling.period='{__name__=~"(node|process)_.*"}:1d:1m` instructs VictoriaMetrics to downsample samples older than one day with one minute interval
only for [time series](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#time-series) with names starting with `node_` or `process_` prefixes.
The downsampling for other time series can be configured independently via additional `-downsampling.period` command-line flags.
Downsampling configuration can be tested in enterprise version of vmui on the page `Tools.Downsampling filters debug`.

If the time series doesn't match any `filter`, then it isn't downsampled. If the time series matches multiple filters, then the downsampling
for the first matching `filter` is applied. For example, `-downsampling.period='{env="prod"}:1d:30s,{__name__=~"node_.*"}:1d:5m'` de-duplicates
samples older than one day with 30 seconds interval across all the time series with `env="prod"` [label](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#labels),
even if their names start with `node_` prefix. All the other time series with names starting with `node_` prefix are de-duplicated with 5 minutes interval.

If downsampling shouldn't be applied to some time series matching the given `filter`, then pass `-downsampling.period=filter:0s:0s` command-line flag to VictoriaMetrics.
For example, if series with `env="prod"` label shouldn't be downsampled, then pass `-downsampling.period='{env="prod"}:0s:0s'` command-line flag in front of other `-downsampling.period` flags.
But `-downsampling.period=0s:interval` or `-downsampling.period=filter:0s:0s` cannot be used with [deduplication](#deduplication) simultaneously as they could conflict.

Downsampling is applied independently per each time series and leaves a single [raw sample](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#raw-samples)
with the biggest [timestamp](https://en.wikipedia.org/wiki/Unix_time) on the configured interval, in the same way as [deduplication](#deduplication) does.
It works the best for [counters](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#counter) and [histograms](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#histogram),
as their values are always increasing. Downsampling [gauges](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#gauge)
and [summaries](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#summary) lose some changes within the downsampling interval,
since only the last sample on the given interval is left and the rest of samples are dropped.

You can use [recording rules](https://docs.victoriametrics.com/victoriametrics/vmalert/#rules) or [streaming aggregation](https://docs.victoriametrics.com/victoriametrics/stream-aggregation/)
to apply custom aggregation functions, like min/max/avg etc., in order to make gauges more resilient to downsampling.

Downsampling can reduce disk space usage and improve query performance if it is applied to time series with big number
of samples per each series. The downsampling doesn't improve query performance and doesn't reduce disk space if the database contains big number
of time series with small number of samples per each series, since downsampling doesn't reduce the number of time series.
So there is little sense in applying downsampling to time series with [high churn rate](https://docs.victoriametrics.com/victoriametrics/faq/#what-is-high-churn-rate).
In this case the majority of query time is spent on searching for the matching time series instead of processing the found samples.
See [Why IndexDB size is so large?](https://docs.victoriametrics.com/victoriametrics/faq/#why-indexdb-size-is-so-large).

Downsampling is performed during [background merges](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#storage).
It cannot be performed if there is not enough of free disk space or if vmstorage is in [read-only mode](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/#readonly-mode).

Downsampling period changes `/api/v1/export` API output. During query requests, if export `start` period is not specified and `reduce_mem_usage` param is omitted, the biggest `downsampling.period` is applied.
As an example, export request  `/api/v1/export?match[]=series` with `-downsampling.period=30d:1h,180d:24h` will return samples downsampled with `24h` interval.

It's expected that resource usage will temporarily increase when **downsampling with filters** is applied.
This is because additional operations are required to read historical data, downsample, and persist it back,
which will cost extra CPU and memory.

Please, note that intervals of `-downsampling.period` for a single filter must be multiples of each other.
In case [deduplication](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#deduplication) is enabled, value of `-dedup.minScrapeInterval` command-line flag must also
be multiple of `-downsampling.period` intervals. This is required to ensure consistency of deduplication and downsampling results.

It is safe updating `-downsampling.period` during VictoriaMetrics restarts - the updated downsampling configuration will be
applied eventually to historical data during  [background merges](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#storage).

See [how to configure downsampling in VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/#downsampling).

See also [retention filters](#retention-filters).

The downsampling can be evaluated for free by downloading and using enterprise binaries from [the releases page](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/latest).
See how to request a [free trial license](https://victoriametrics.com/products/enterprise/trial/).


## Multitenancy {#multi-tenancy}

Single-node VictoriaMetrics does not support [multitenancy](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/#multitenancy) as cluster version does.
But it can emulate it via [labels](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#labels).

Multitenancy via labels requires all ingested data to have a label set that would uniquely identify the tenant. For example:
```text
up{job="node_exporter", team="analytics"} 1
up{job="node_exporter", team="developers"} 1
```

Here, `team` label can be treated as a tenant identifier. Assuming that all metrics have label `team` attached, we can [enforce a tenant filter for all queries](https://docs.victoriametrics.com/victoriametrics/#prometheus-querying-api-enhancements) via `extra_label` query parameter:
```sh
/api/v1/query?match[]=up&extra_label=team=developers
```

The query above will return metrics matching the `up` name and having `team=developers` label. The `extra_label` query parameter can be enforced in Grafana datasource settings.
Or enforced by vmauth [based on user credentials](https://docs.victoriametrics.com/victoriametrics/vmauth/#basic-auth-proxy):
```yaml
users:
  - username: team-developers
    password: "***"
    url_map:
      - url_prefix: "http://victoriametrics:8428/?extra_label=team=developers"

  - username: team-analytics
    password: "***"
    url_map:
      - url_prefix: "http://victoriametrics:8428/?extra_label=team=analytics"
```

It is allowed to set multiple `extra_label` query parameters, or even `extra_filters` with regex support - see more details [here](https://docs.victoriametrics.com/victoriametrics/#prometheus-querying-api-enhancements).

The extra label can be unconditionally applied to all ingested data within a request if `extra_label` param is set:
```sh
curl -X POST "http://victoriametrics:8428/api/v1/import?extra_label=team=developers" -T data_to_import.jsonl 
```

All samples ingested in this way will have the `team=developers` label attached, making it easier to control ingestion flow.
The `extra_label` can be enforced based on user credential by vmauth in the same way as described above.


## Scalability and cluster version

Single-node VictoriaMetrics is a single process responsible for ingestion, storing, and querying data.
Its resource usage is significantly more efficient compared to distributed installations that require transferring data between multiple processes over the network.
Single-node VictoriaMetrics has linear vertical scalability and can substitute a moderately sized cluster built with competing solutions
such as Thanos, Uber M3, InfluxDB or TimescaleDB. See [vertical scalability benchmarks](https://medium.com/@valyala/measuring-vertical-scalability-for-time-series-databases-in-google-cloud-92550d78d8ae).

For moderate workloads single-node VictoriaMetrics will be the most efficient solution. See how to [achieve high availability](https://docs.victoriametrics.com/victoriametrics/#high-availability).

Try the single-node first. If you face scalability limits - try horizontal scaling with cluster version. [Cluster version of VictoriaMetrics](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/) splits the single process into multiple processes that can be scaled horizontally. See [cluster architecture overview](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/#architecture-overview) for more details.

Cluster version of VictoriaMetrics allows scaling beyond hardware limits of a single physical instance. But it also introduces additional complexity and resource usage as cluster components become distributed and have to communicate with each other over the network.

Due to historical reasons, data format on disk differs between single-node and cluster versions. It makes it impossible to move data from single-node to the `vmstorage` (a storage component in cluster version) without re-ingesting it. But it is possible to [query data from single-node and cluster installations at the same time](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/#reading-from-single-node-victoriametrics).

See also [how to migrate from single-node to cluster version](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#from-single-node-to-cluster).


## Alerting

It is recommended using [vmalert](https://docs.victoriametrics.com/victoriametrics/vmalert/) for alerting.

Additionally, alerting can be set up with the following tools:

* With Prometheus - see [the corresponding docs](https://prometheus.io/docs/alerting/overview/).
* With Promxy - see [the corresponding docs](https://github.com/jacksontj/promxy/blob/master/README.md#how-do-i-use-alertingrecording-rules-in-promxy).
* With Grafana - see [the corresponding docs](https://grafana.com/docs/alerting/rules/).
