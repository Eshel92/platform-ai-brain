<!-- Part 8 of 13 of victoriametrics/README.md (split because the page is big). -->

## IndexDB

VictoriaMetrics identifies
[time series](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#time-series)
by `TSID` (time series ID) and stores
[raw samples](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#raw-samples)
sorted by TSID (see [Storage](#storage)). Thus, the TSID is a primary index and
could be used for searching and retrieving raw samples. However, the TSID is
never exposed to the clients, i.e. it is for internal use only.

Instead, VictoriaMetrics maintains an **inverted index** (known as `indexDB`)
that enables searching the raw samples by metric name, label name, and label
value by mapping these values to the corresponding TSIDs. Every data
[partition](#storage) has its own indexDB.

VictoriaMetrics uses two types of inverted indexes:

* Global index. Searches using this index is performed across the entire
  partition time range.
* Per-day index. This index stores mappings similar to ones in global index
  but also includes the date in each mapping. This speeds up data retrieval
  for queries within a shorter time range (which is often just the last day).

When the search query is executed, VictoriaMetrics decides which index to use
based on the time range of the query:

* Per-day index is used if the search time range is less than the partition time range.
* Global index is used for search queries with a time range that matches exactly
  or greater than the partition time range.

Mappings are added to the indexes during the data ingestion:

* In global index each mapping is created only once per partition.
* In the per-day index each mapping is created for each unique date that
  has been seen in the samples for the corresponding time series.

Since indexDB is a part of a partition, it is dropped along with it as it
becomes outside the [retention period](#retention).

See also [Why IndexDB size is so large?](https://docs.victoriametrics.com/victoriametrics/faq/#why-indexdb-size-is-so-large).

### Index tuning for low churn rate

By default, VictoriaMetrics uses the following indexes for data retrieval: `global` and `per-day`.
Both store the same data and on query time VictoriaMetrics can choose between indexes for optimal performance.
See [IndexDB](#indexdb) for details.

If your use case involves [high cardinality](https://docs.victoriametrics.com/victoriametrics/faq/#what-is-high-cardinality)
with [high churn rate](https://docs.victoriametrics.com/victoriametrics/faq/#what-is-high-churn-rate)
then this default setting should be ideal for you.

A prominent example is Kubernetes. Services in k8s expose big number of series with short lifetime, significantly
increasing churn rate. The per-day index speeds up data retrieval in this case.

But if your use case assumes low or no churn rate, then you might benefit from disabling the per-day index by setting
the flag `-disablePerDayIndex`{{% available_from "v1.112.0" %}}. This will improve the time series ingestion speed and decrease disk space usage,
since no time or disk space is spent maintaining the per-day index.

Example use cases:

* Historical weather data, such as [ERA5](https://cds.climate.copernicus.eu/datasets/reanalysis-era5-single-levels?tab=overview).
  It consists of millions time series whose hourly values span tens of years. The time series set never changes.
  If the per-day index is disabled, once the first hour of data is ingested the entire time series set will be written
  into the global index and subsequent portions of data will not result in index update. But if the per-day index
  is enabled, the same set of time-series will be written to the per-day index for every day of data.

* IoT: a huge set of sensors exports time series with the sensor ID used as a metric label value. Since sensor additions
  or removals happen infrequently, the time series churn rate will be low. With the per-day index disabled, the entire
  time series set will be registered in global index during the initial data ingestion and the global index will receive
  small updates when a sensor is added or removed.

What to expect:

* Prefer setting this flag on fresh installations.
* Disabling per-day index on installations with historical data is Ok.
* Re-enabling per-day index on installations with historical data will make it unsearchable.

See also [Why IndexDB size is so large?](https://docs.victoriametrics.com/victoriametrics/faq/#why-indexdb-size-is-so-large).


## Retention

Retention is configured with the `-retentionPeriod` command-line flag, which takes a number followed by a time unit
character - `h(ours)`, `d(ays)`, `w(eeks)`, `M(onth)`, `y(ears)`. If the time unit is not specified, a month (31 days) is assumed.
For instance, `-retentionPeriod=3` means that the data will be stored for 3 months (93 days) and then deleted.
The default retention period is one month: 1M (31 days). The **minimum retention** period is 24h or 1d.

Data is split in per-month partitions inside `<-storageDataPath>/data/{small,big}` folders.
**Data partitions** outside the configured retention are deleted **on the first day of the new month**.
Each partition consists of one or more **data parts**. Data parts outside the configured retention
are **eventually deleted** during [background merge](https://medium.com/@valyala/how-victoriametrics-makes-instant-snapshots-for-multi-terabyte-time-series-data-e1f3fb0e0282).
The time range covered by data part is **not limited by retention period unit**. One data part can cover hours or days of
data. Hence, a data part can be deleted only **when fully outside the configured retention**.
See more about partitions and parts in the [Storage section](#storage).
See how the [retention and free-disk watchers manage storage](https://victoriametrics.com/blog/vmstorage-retention-merging-deduplication/#retention-free-disk-space-guard-and-downsampling)
for implementation details and monitoring metrics.

The maximum disk space usage for a given `-retentionPeriod` is going to be (`-retentionPeriod` + 1) months.
For example, if `-retentionPeriod` is set to 1, data for January is deleted on March 1st.

It is safe to extend `-retentionPeriod` on existing data. If `-retentionPeriod` is set to a lower
value than before, then data outside the configured period will be eventually deleted.

VictoriaMetrics does not support indefinite retention, but you can specify an arbitrarily high duration, e.g. `-retentionPeriod=100y`.
Just keep in mind that VictoriaMetrics does not support samples with negative timestamps. Timestamps at `1970-01-01` are also not
supported because this date has a special meaning internally. It therefore rejects samples with timestamps before
`1970-01-02T00:00:00.000Z`.

By default, VictoriaMetrics doesn't accept samples with timestamps bigger than `now+2d`, e.g. 2 days in the future.
If you need accepting samples with bigger timestamps, then specify the desired "future retention" via `-futureRetention` command-line flag.
This flag accepts values starting from `2d`.

For example, the following command starts VictoriaMetrics, which accepts samples with timestamps up to a year in the future:

```sh
/path/to/victoria-metrics -futureRetention=1y
```

VictoriaMetrics does not support stamples after `2262-03-31T23:59:59.999Z`. If the future retention includes dates after this timestamp,
the samples for those dates will be rejected.

By default, VictoriaMetrics accepts samples with timestamps as old as the configured `-retentionPeriod` allows, e.g. it accepts backfilled
historical data as long as it fits into the retention. If you need rejecting samples with historical timestamps older than the specified
duration, then specify the desired duration via the `-maxBackfillAge` command-line flag. This can be useful for limiting ingestion of
historical samples, for example, when older data has been moved to another storage tier (nvme/hdd, hot/cold).
`-maxBackfillAge` cannot exceed the configured `-retentionPeriod` - bigger values are automatically clamped to `-retentionPeriod`.

For example, the following command starts VictoriaMetrics, which rejects ingested samples with timestamps older than 2 days:

```sh
/path/to/victoria-metrics -maxBackfillAge=2d
```

### Multiple retentions

Distinct retentions for distinct time series can be configured via [retention filters](#retention-filters)
in [VictoriaMetrics Enterprise](https://docs.victoriametrics.com/victoriametrics/enterprise/).

Community version of VictoriaMetrics supports only a single retention, which can be configured via [-retentionPeriod](#retention) command-line flag.
If you need multiple retentions in community version of VictoriaMetrics, then you may start multiple VictoriaMetrics instances with distinct values for the following flags:

* `-retentionPeriod`
* `-storageDataPath`, so the data for each retention period is saved in a separate directory
* `-httpListenAddr`, so clients may reach VictoriaMetrics instance with proper retention

Then set up [vmauth](https://docs.victoriametrics.com/victoriametrics/vmauth/) in front of VictoriaMetrics instances,
so it could route requests from particular user to VictoriaMetrics with the desired retention.

Similar scheme can be applied for multiple tenants in [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/).
See [these docs](https://docs.victoriametrics.com/guides/guide-vmcluster-multiple-retention-setup/) for multi-retention setup details.

### Retention filters

[Enterprise version of VictoriaMetrics](https://docs.victoriametrics.com/victoriametrics/enterprise/) supports `retention filters`,
which allow configuring multiple retentions for distinct sets of time series matching the configured [series filters](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#filtering)
via `-retentionFilter` command-line flag. This flag accepts `filter:duration` options, where `filter` must be
a valid [series filter](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#filtering), while the `duration`
must contain valid [retention](#retention) for time series matching the given `filter`.
The `duration` of the `-retentionFilter` must be lower or equal to [-retentionPeriod](#retention) flag value.
If series doesn't match any configured `-retentionFilter`, then the retention configured via [-retentionPeriod](#retention)
command-line flag is applied to it. If series matches multiple configured retention filters, then the smallest retention is applied.

For example, the following config sets 3 days retention for time series with `team="juniors"` label,
30 days retention for time series with `env="dev"` or `env="staging"` label and 1 year retention for the remaining time series:

```sh
-retentionFilter='{team="juniors"}:3d' -retentionFilter='{env=~"dev|staging"}:30d' -retentionPeriod=1y
```

There are two gauge metrics to monitor the retention filters process:

* `vm_retention_filters_partitions_scheduled` shows the total number of partitions scheduled for retention filters
* `vm_retention_filters_partitions_scheduled_size_bytes` shows the total size of scheduled partitions.

Additionally, a log message with the filter expression and the partition name is written to the log on the start and completion of the operation.

Important notes:

* The data outside the configured retention isn't deleted instantly - it is deleted eventually during [background merges](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#storage).
* The `-retentionFilter` doesn't remove old data from [IndexDB](#indexdb) until the configured [-retentionPeriod](#retention).
  So the IndexDB size can grow big under [high churn rate](https://docs.victoriametrics.com/victoriametrics/faq/#what-is-high-churn-rate)
  even for small retentions configured via `-retentionFilter`.

Retention filters configuration can be tested in enterprise version of vmui on the page `Tools.Retention filters debug`.
It is safe updating `-retentionFilter` during VictoriaMetrics restarts - the updated retention filters are applied eventually
to historical data.

It's expected that resource usage will temporarily increase when `-retentionFilter` is applied.
This is because additional operations are required to read the data, filter and apply retention to partitions,
which will cost extra CPU and memory.

See [how to configure multiple retentions in VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/#retention-filters).

See also [downsampling](#downsampling).

Retention filters can be evaluated for free by downloading and using enterprise binaries from [the releases page](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/latest).
See how to request a [free trial license](https://victoriametrics.com/products/enterprise/trial/).
