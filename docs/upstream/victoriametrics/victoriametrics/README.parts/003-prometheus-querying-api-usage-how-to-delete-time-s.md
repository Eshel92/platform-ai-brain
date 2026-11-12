<!-- Part 3 of 13 of victoriametrics/README.md (split because the page is big). -->

## Prometheus querying API usage

VictoriaMetrics supports the following handlers from [Prometheus querying API](https://prometheus.io/docs/prometheus/latest/querying/api/):

* [/api/v1/query](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#instant-query)
* [/api/v1/query_range](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#range-query)
* [/api/v1/series](https://docs.victoriametrics.com/victoriametrics/url-examples/#apiv1series)
* [/api/v1/labels](https://docs.victoriametrics.com/victoriametrics/url-examples/#apiv1labels)
* [/api/v1/label/.../values](https://docs.victoriametrics.com/victoriametrics/url-examples/#apiv1labelvalues)
* [/api/v1/status/tsdb](https://prometheus.io/docs/prometheus/latest/querying/api/#tsdb-stats). See [these docs](#tsdb-stats) for details.
* [/api/v1/targets](https://prometheus.io/docs/prometheus/latest/querying/api/#targets) - see [these docs](#how-to-scrape-prometheus-exporters-such-as-node-exporter) for more details.
* [/api/v1/metadata](https://prometheus.io/docs/prometheus/latest/querying/api/#querying-metric-metadata) - see [these docs](#metrics-metadata) for more details.
* [/federate](https://prometheus.io/docs/prometheus/latest/federation/) - see [these docs](#federation) for more details.

These handlers can be queried from Prometheus-compatible clients such as Grafana or curl.
All the Prometheus querying API handlers can be prepended with `/prometheus` prefix. For example, both `/prometheus/api/v1/query` and `/api/v1/query` should work.

### Prometheus querying API enhancements

VictoriaMetrics accepts optional `extra_label=<label_name>=<label_value>` query arg, which can be used
for enforcing additional label filters for queries. For example, `/api/v1/query_range?extra_label=user_id=123&extra_label=group_id=456&query=<query>`
would automatically add `{user_id="123",group_id="456"}` label filters to the given `<query>`.
This functionality can be used for limiting the scope of time series visible to the given tenant.
It is expected that the `extra_label` query args are automatically set by auth proxy sitting in front of VictoriaMetrics.
See [vmauth](https://docs.victoriametrics.com/victoriametrics/vmauth/) and [vmgateway](https://docs.victoriametrics.com/victoriametrics/vmgateway/) as examples of such proxies.

VictoriaMetrics accepts optional `extra_filters[]=series_selector` query arg, which can be used for enforcing arbitrary label filters for queries.
For example, `/api/v1/query_range?extra_filters[]={env=~"prod|staging",user="xyz"}&query=<query>` would automatically
add `{env=~"prod|staging",user="xyz"}` label filters to the given `<query>`. This functionality can be used for limiting
the scope of time series visible to the given tenant. It is expected that the `extra_filters[]` query args are automatically
set by auth proxy sitting in front of VictoriaMetrics.
See [vmauth](https://docs.victoriametrics.com/victoriametrics/vmauth/) and [vmgateway](https://docs.victoriametrics.com/victoriametrics/vmgateway/) as examples of such proxies.

VictoriaMetrics accepts multiple formats for `time`, `start` and `end` query args - see [these docs](#timestamp-formats).

VictoriaMetrics accepts `round_digits` query arg for [/api/v1/query](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#instant-query)
and [/api/v1/query_range](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#range-query) handlers. It can be used for rounding response values
to the given number of digits after the decimal point.
For example, `/api/v1/query?query=avg_over_time(temperature[1h])&round_digits=2` would round response values to up to two digits after the decimal point.

VictoriaMetrics accepts `optimize_repeated_binary_op_subexprs=1` query arg for [/api/v1/query_range](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#range-query)
handler. It allows `vmselect` to execute left and right sides of binary operators sequentially when they contain the same
optimized aggregate rollup result expression, so the second side may reuse the rollup result cache populated by the first side.
The optimization is disabled by default and applies only when rollup result cache can be used for the request.

VictoriaMetrics accepts `limit` query arg for [/api/v1/labels](https://docs.victoriametrics.com/victoriametrics/url-examples/#apiv1labels)
and [`/api/v1/label/<labelName>/values`](https://docs.victoriametrics.com/victoriametrics/url-examples/#apiv1labelvalues) handlers for limiting the number of returned entries.
For example, the query to `/api/v1/labels?limit=5` returns a sample of up to 5 unique labels, while ignoring the rest of labels.
If the provided `limit` value exceeds the corresponding `-search.maxTagKeys` / `-search.maxTagValues` command-line flag values,
then limits specified in the command-line flags are used.

By default, VictoriaMetrics returns time series for the last day starting at 00:00 UTC
from [/api/v1/series](https://docs.victoriametrics.com/victoriametrics/url-examples/#apiv1series),
[/api/v1/labels](https://docs.victoriametrics.com/victoriametrics/url-examples/#apiv1labels) and
[`/api/v1/label/<labelName>/values`](https://docs.victoriametrics.com/victoriametrics/url-examples/#apiv1labelvalues),
while the Prometheus API defaults to all time.  Explicitly set `start` and `end` to select the desired time range.
VictoriaMetrics rounds the specified `start..end` time range to day granularity because of performance optimization concerns.
If you need the exact set of label names and label values on the given time range, then send queries
to [/api/v1/query](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#instant-query) or to [/api/v1/query_range](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#range-query).

VictoriaMetrics accepts `limit` query arg at [/api/v1/series](https://docs.victoriametrics.com/victoriametrics/url-examples/#apiv1series)
for limiting the number of returned entries. For example, the query to `/api/v1/series?limit=5` returns a sample of up to 5 series, while ignoring the rest of series.
If the provided `limit` value exceeds the corresponding `-search.maxSeries` command-line flag values, then limits specified in the command-line flags are used.

VictoriaMetrics returns an extra object `stats` in JSON response for [`/api/v1/query`](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#instant-query)
and [`/api/v1/query_range`](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#range-query) APIs. This object contains two
fields: `executionTimeMsec` with number of milliseconds the request took and `seriesFetched` with number of series that
were fetched from database before filtering. The `seriesFetched` field is effectively used by vmalert for detecting
[misconfigured rule expressions](https://docs.victoriametrics.com/victoriametrics/vmalert/#never-firing-alerts). Please note, `seriesFetched`
provides approximate number of series, it is not recommended to rely on it in tests.

Additionally, VictoriaMetrics provides the following handlers:

* `/vmui` - Basic Web UI. See [these docs](#vmui).
* `/api/v1/series/count` - returns the total number of time series in the database. Some notes:
  * the handler scans all [IndexDBs](#indexdb) entirely, so it can be slow if the database contains tens of millions of time series;
  * it can return an inflated value if the same time series is stored in more than one IndexDB.
  * the handler may count [deleted time series](#how-to-delete-time-series) additionally to normal time series due to internal implementation restrictions;
* `/api/v1/status/active_queries` - returns the list of currently running queries. This list is also available at [`active queries` page at VMUI](#active-queries).
* `/api/v1/status/top_queries` - returns the following query lists:
  * the most frequently executed queries - `topByCount`
  * queries with the biggest average execution duration - `topByAvgDuration`
  * queries that took the most time for execution - `topBySumDuration`

  The number of returned queries can be limited via `topN` query arg. Old queries can be filtered out with `maxLifetime` query arg.
  For example, request to `/api/v1/status/top_queries?topN=5&maxLifetime=30s` would return up to 5 queries per list, which were executed during the last 30 seconds.
  VictoriaMetrics tracks the last `-search.queryStats.lastQueriesCount` queries with durations at least `-search.queryStats.minQueryDuration`.

  See also [`top queries` page at VMUI](#top-queries).

### Timestamp formats

VictoriaMetrics accepts the following formats for `time`, `start` and `end` query args
in [query APIs](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#prometheus-querying-api-usage) and
in [export APIs](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#how-to-export-time-series).

* Unix timestamps in seconds with optional milliseconds after the point. For example, `1562529662.678`.
* Unix timestamps in milliseconds. For example, `1562529662678`.
* Unix timestamps in microseconds. For example, `1562529662678901`.
* Unix timestamps in nanoseconds. For example, `1562529662678901234`.
* [RFC3339](https://www.ietf.org/rfc/rfc3339.txt). For example, `2022-03-29T01:02:03Z` or `2022-03-29T01:02:03+02:30`.
* Partial RFC3339. Examples: `2022`, `2022-03`, `2022-03-29`, `2022-03-29T01`, `2022-03-29T01:02`, `2022-03-29T01:02:03`.
  The partial RFC3339 time is in local timezone of the host where VictoriaMetrics runs.
  It is possible to specify the needed timezone by adding `Z` (UTC), `+hh:mm` or `-hh:mm` suffix to partial time.
  For example, `2022-03-01Z` corresponds to the given date in UTC timezone, while `2022-03-01+06:30` corresponds to `2022-03-01` date at `06:30` timezone.
* Relative duration comparing to the current time. For example, `1h5m`, `-1h5m` or `now-1h5m` means `one hour and five minutes ago`, while `now` means `now`.


## How to build from sources

We recommend using either [binary releases](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/latest) or
docker images ([Docker Hub](https://hub.docker.com/r/victoriametrics/victoria-metrics/) and [Quay](https://quay.io/repository/victoriametrics/victoria-metrics?tab=tags)) instead of building VictoriaMetrics
from sources. Building from sources is reasonable when developing additional features specific
to your needs or when testing bugfixes.

### Development build

1. [Install Go](https://golang.org/doc/install).
1. Run `make victoria-metrics` from the root folder of [the repository](https://github.com/VictoriaMetrics/VictoriaMetrics).
   It builds `victoria-metrics` binary and puts it into the `bin` folder.

### Production build

1. [Install docker](https://docs.docker.com/install/).
1. Run `make victoria-metrics-prod` from the root folder of [the repository](https://github.com/VictoriaMetrics/VictoriaMetrics).
   It builds `victoria-metrics-prod` binary and puts it into the `bin` folder.

### ARM build

ARM build may run on Raspberry Pi or on [energy-efficient ARM servers](https://blog.cloudflare.com/arm-takes-wing/).

### Development ARM build

1. [Install Go](https://golang.org/doc/install).
1. Run `make victoria-metrics-linux-arm` or `make victoria-metrics-linux-arm64` from the root folder of [the repository](https://github.com/VictoriaMetrics/VictoriaMetrics).
   It builds `victoria-metrics-linux-arm` or `victoria-metrics-linux-arm64` binary respectively and puts it into the `bin` folder.

### Production ARM build

1. [Install docker](https://docs.docker.com/install/).
1. Run `make victoria-metrics-linux-arm-prod` or `make victoria-metrics-linux-arm64-prod` from the root folder of [the repository](https://github.com/VictoriaMetrics/VictoriaMetrics).
   It builds `victoria-metrics-linux-arm-prod` or `victoria-metrics-linux-arm64-prod` binary respectively and puts it into the `bin` folder.

### Pure Go build (CGO_ENABLED=0)

`Pure Go` mode builds only Go code without [cgo](https://golang.org/cmd/cgo/) dependencies.

1. [Install Go](https://golang.org/doc/install).
1. Run `make victoria-metrics-pure` from the root folder of [the repository](https://github.com/VictoriaMetrics/VictoriaMetrics).
   It builds `victoria-metrics-pure` binary and puts it into the `bin` folder.

### Building docker images

Run `make package-victoria-metrics`. It builds `victoriametrics/victoria-metrics:<PKG_TAG>` docker image locally.
`<PKG_TAG>` is auto-generated image tag, which depends on source code in the repository.
The `<PKG_TAG>` may be manually set via `PKG_TAG=foobar make package-victoria-metrics`.

The base docker image is [alpine](https://hub.docker.com/_/alpine) but it is possible to use any other base image
by setting it via `<ROOT_IMAGE>` environment variable.
For example, the following command builds the image on top of [scratch](https://hub.docker.com/_/scratch) image:

```sh
ROOT_IMAGE=scratch make package-victoria-metrics
```

#### Building VictoriaMetrics with Podman

VictoriaMetrics can be built with Podman in either rootful or rootless mode.

When building via rootful Podman, simply add `DOCKER=podman` to the relevant `make` commandline.  To build
via rootless Podman, add `DOCKER=podman DOCKER_RUN="podman run --userns=keep-id"` to the `make`
commandline.

For example: `make victoria-metrics-pure DOCKER=podman DOCKER_RUN="podman run --userns=keep-id"`

Note that `production` builds are not supported via Podman because Podman does not support `buildx`.


## How to work with snapshots

### Create snapshot

Send a request to `http://<victoriametrics-addr>:8428/snapshot/create` endpoint in order to create
an [instant snapshot](https://medium.com/@valyala/how-victoriametrics-makes-instant-snapshots-for-multi-terabyte-time-series-data-e1f3fb0e0282).
The page returns the following JSON response on successful creation of snapshot:

```json
{"status":"ok","snapshot":"<snapshot-name>"}
```

Snapshots are created under `<-storageDataPath>/snapshots` directory, where `<-storageDataPath>`
is the corresponding command-line flag value. Snapshots can be archived to backup storage at any time
with [vmbackup](https://docs.victoriametrics.com/victoriametrics/vmbackup/).

Snapshots consist of a mix of hard-links and soft-links to various files and directories inside `-storageDataPath`.
See [this article](https://medium.com/@valyala/how-victoriametrics-makes-instant-snapshots-for-multi-terabyte-time-series-data-e1f3fb0e0282)
for more details. This adds some restrictions on what can be done with the contents of `<-storageDataPath>/snapshots` directory:

* Do not delete subdirectories inside `<-storageDataPath>/snapshots` with `rm` or similar commands, since this will leave some snapshot data undeleted.
  Prefer using the `/snapshot/delete` API for deleting snapshot. See below for more details about this API.
* Do not copy subdirectories inside `<-storageDataPath>/snapshot` with `cp`, `rsync` or similar commands, since there are high chances
  that these commands won't copy some data stored in the snapshot. Prefer using [vmbackup](https://docs.victoriametrics.com/victoriametrics/vmbackup/) for making copies of snapshot data.

See also [snapshot troubleshooting](#snapshot-troubleshooting).

The `http://<victoriametrics-addr>:8428/snapshot/list` endpoint returns the list of available snapshots.

### Delete snapshot

Send a query to `http://<victoriametrics-addr>:8428/snapshot/delete?snapshot=<snapshot-name>` in order
to delete the snapshot with `<snapshot-name>` name.

Navigate to `http://<victoriametrics-addr>:8428/snapshot/delete_all` in order to delete all the snapshots.

### How to restore from a snapshot

1. Stop VictoriaMetrics with `kill -INT`.
1. Restore snapshot contents from backup with [vmrestore](https://docs.victoriametrics.com/victoriametrics/vmrestore/)
   to the directory pointed by `-storageDataPath`.
1. Start VictoriaMetrics.

### Snapshot troubleshooting

Snapshot doesn't occupy disk space just after its' creation thanks to the [used approach](https://medium.com/@valyala/how-victoriametrics-makes-instant-snapshots-for-multi-terabyte-time-series-data-e1f3fb0e0282).
Old snapshots may start occupying additional disk space if they refer to old parts, which were already deleted during [background merge](#storage).
That's why it is recommended deleting old snapshots after they are no longer needed in order to free up disk space used by old snapshots.
This can be done either manually or automatically if the `-snapshotsMaxAge` command-line flag is set. Make sure that the backup process has enough time to complete
when setting `-snapshotsMaxAge` command-line flag.

VictoriaMetrics exposes the current number of available snapshots via `vm_snapshots` metric at [`/metrics`](#monitoring) page.


## How to delete time series

Send a POST request to `http://<victoriametrics-addr>:8428/api/v1/admin/tsdb/delete_series?match[]=<timeseries_selector_for_delete>`,
where `<timeseries_selector_for_delete>` may contain any [time series selector](https://prometheus.io/docs/prometheus/latest/querying/basics/#time-series-selectors)
for metrics to delete. Delete API doesn't support the deletion of specific time ranges, the series can only be deleted completely.
Storage space for the deleted time series isn't freed instantly - it is freed during subsequent
[background merges of data files](https://medium.com/@valyala/how-victoriametrics-makes-instant-snapshots-for-multi-terabyte-time-series-data-e1f3fb0e0282).

Note that background merges may never occur for data from previous months, so storage space won't be freed for historical data.
In this case [forced merge](#forced-merge) may help freeing up storage space.

It is recommended verifying which metrics will be deleted with the call to `http://<victoria-metrics-addr>:8428/api/v1/series?match[]=<timeseries_selector_for_delete>`
before actually deleting the metrics. By default, this query will only scan series in the past 5 minutes, so you may need to
adjust `start` and `end` to a suitable range to achieve match hits. Also, if the number of returned time series is
rather big you will need to set `-search.maxDeleteSeries` flag (see [Resource usage limits](#resource-usage-limits)).

The `/api/v1/admin/tsdb/delete_series` handler may be protected with `authKey` if `-deleteAuthKey` command-line flag is set.
Note that handler accepts only HTTP POST method.

The delete API is intended mainly for the following cases:

* One-off deleting of accidentally written invalid (or undesired) time series.
* One-off deleting of user data due to [GDPR](https://en.wikipedia.org/wiki/General_Data_Protection_Regulation).

Using the delete API is not recommended in the following cases, since it brings a non-zero overhead:

* Regular cleanups for unneeded data. Just prevent writing unneeded data into VictoriaMetrics.
  This can be done with [relabeling](#relabeling).
  See [this article](https://www.robustperception.io/relabelling-can-discard-targets-timeseries-and-alerts) for details.
* Reducing disk space usage by deleting unneeded time series. This doesn't work as expected, since the deleted
  time series occupy disk space until the next merge operation, which can never occur when deleting too old data.
  [Forced merge](#forced-merge) may be used for freeing up disk space occupied by old data.
  Note that VictoriaMetrics doesn't delete entries from [IndexDB](#indexdb) for the deleted time series.
  IndexDB is cleaned up along with the corresponding data partition once it becomes outside the [-retentionPeriod](#retention).

It's better to use the `-retentionPeriod` command-line flag for efficient pruning of old data.
