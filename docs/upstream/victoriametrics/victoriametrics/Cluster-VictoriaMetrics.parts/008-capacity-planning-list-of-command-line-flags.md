<!-- Part 8 of 8 of victoriametrics/Cluster-VictoriaMetrics.md (split because the page is big). -->

## Capacity planning

VictoriaMetrics uses lower amounts of CPU, RAM and storage space on production workloads compared to competing solutions (Prometheus, Thanos, Cortex, TimescaleDB, InfluxDB, QuestDB, M3DB) according to [our case studies](https://docs.victoriametrics.com/victoriametrics/casestudies/).

Cluster capacity scales linearly with the available resources. The needed amounts of CPU and RAM for each node type highly depend on the workload - the number of [active time series](https://docs.victoriametrics.com/victoriametrics/faq/#what-is-an-active-time-series), [series churn rate](https://docs.victoriametrics.com/victoriametrics/faq/#what-is-high-churn-rate), query types, query QPS, etc. 
To start with capacity planning it is recommended to:
1. Setup a test VictoriaMetrics cluster for your production workload. Start with 20-30 `vmstorage` shards with low resource limits, as bigger number of shards contributes to the cluster's reliability and makes future scalability easier.
1. Setup [monitoring for the test cluster](#monitoring), so you can identify resource usage and bottlenecks.
1. Start ingesting production workload by replicating it from your metrics collection agents, run read queries that you expect to have in the production system. 
1. Iteratively scale resources until the cluster becomes stable:
   * Run approximately 1 `vminsert` for each 3-5 `vmstorage` shards. Scale vminserts horizontally if you have a high rate of write requests per-second, scale vertically otherwise. It is recommended running vmagent in front of vminserts, as it optimally compresses and batches data before forwarding it. Dedicate about 2GiB of RAM per 1 vCPU. 
   * Run an arbitrary number of `vmselect` nodes depending on the load. Scale vmselects horizontally if you have a high rate of read requests per-second. Scale vertically to improve query latency. Memory usage depends on queries: pick it accordingly to [-search.maxMemoryPerQuery and -search.maxConcurrentRequests](https://docs.victoriametrics.com/victoriametrics/#resource-usage-limits) limits. Dedicate at least 10GiB of disk volume for `vmselect` for storing local caches.
   * `vmstorage` nodes, unlike `vmselect` and `vminsert`, are stateful and their number can't be easily scaled up or down. This is why it is recommended to start with many small shards, and vertically scale resources until installation is stable. Scale horizontally to improve overall performance or to overcome hardware limitations, such as CPU/RAM/Disk size per instance.

The required storage space for the given retention (the retention is set via `-retentionPeriod` command-line flag at `vmstorage`) can be extrapolated from disk space usage in a test run. For example, if the storage space usage is 10GB after a day-long test run on a production workload, then it will need at least `10GB*100=1TB` of disk space for `-retentionPeriod=100d` (100-days retention period). Storage space usage can be monitored with [the official Grafana dashboard for VictoriaMetrics cluster](#monitoring).

It is recommended leaving the following amounts of spare resources to ensure the stability of the cluster:

- 50% of free RAM across all the node types for reducing the probability of OOM (out of memory) crashes and slowdowns during temporary spikes in workload.
- 50% of spare CPU across all the node types for reducing the probability of slowdowns during temporary spikes in workload.
- At least 20% of free storage space at the directory pointed by `-storageDataPath` command-line flag at `vmstorage` nodes. See also `-storage.minFreeDiskSpaceBytes` command-line flag [description for vmstorage](#list-of-command-line-flags-for-vmstorage).

Increase free storage space and `-storage.minFreeDiskSpaceBytes` to match at least the amount of data you plan to ingest in a calendar month: on each vmstorage pod, the monthly final deduplication process will temporarily need as much space as is used for the previous month's data, before it can free up space. For example, if you have a 3 month retention period and you want to keep at least 10 % space free at all times, you could pick 35 % of your total space as value. When some of your vmstorage pods are in [read-only mode](#readonly-mode), the remaining pods will have a higher share of the total data ingestion, and will therefore need more free space the next month.

Some capacity planning tips for VictoriaMetrics cluster:

- The [replication](#replication-and-data-safety) increases the amounts of needed resources for the cluster by up to `N` times where `N` is replication factor. This is because `vminsert` stores `N` copies of every ingested sample on distinct `vmstorage` nodes. These copies are de-duplicated by `vmselect` during querying. The most cost-efficient and performant solution for data durability is to rely on replicated durable persistent disks such as [Google Compute persistent disks](https://cloud.google.com/compute/docs/disks#pdspecs) instead of using the [replication at VictoriaMetrics level](#replication-and-data-safety).
- It is recommended to run a cluster with many small `vmstorage` nodes instead of a cluster with small number of big `vmstorage` nodes. This increases chances that the cluster remains available and stable when some of `vmstorage` nodes are temporarily unavailable during maintenance events such as upgrades, configuration changes or migrations. For example, when a cluster contains 10 `vmstorage` nodes and a single node becomes temporarily unavailable, then the workload on the remaining 9 nodes increases by `1/9=11%`. When a cluster contains 3 `vmstorage` nodes and a single node becomes temporarily unavailable, then the workload on the remaining 2 nodes increases by `1/2=50%`. The remaining `vmstorage` nodes may have no enough free capacity for handling the increased workload. In this case the cluster may become overloaded, which may result to decreased availability and stability.
- Cluster capacity for [active time series](https://docs.victoriametrics.com/victoriametrics/faq/#what-is-an-active-time-series) can be increased by increasing RAM and CPU resources per each `vmstorage` node or by adding new `vmstorage` nodes.
- Query latency can be reduced by increasing CPU resources per each `vmselect` node. Performance for heavy queries scales with the number of available CPU cores at `vmselect` node, since `vmselect` processes time series referred by the query on all the available CPU cores. Query latency also depends on performance of `vmstorage` nodes - you can identify the bottleneck by [tracing slow queries](https://docs.victoriametrics.com/victoriametrics/#query-tracing).
- If the cluster needs to process incoming queries at a high rate, then its capacity can be increased by adding more `vmselect` nodes, so incoming queries could be spread among bigger number of `vmselect` nodes. The query throughput also depends on performance of `vmstorage` nodes - you can identify the bottleneck by [tracing slow queries](https://docs.victoriametrics.com/victoriametrics/#query-tracing).
- By default `vmstorage` compresses the data it sends to `vmselect` during queries in order to reduce network bandwidth usage. The compression takes additional CPU resources at `vmstorage`. If `vmstorage` nodes have limited CPU, then the compression can be disabled by passing `-rpc.disableCompression` command-line flag at `vmstorage` nodes.

See also [resource usage limits docs](#resource-usage-limits).


## Helm

Helm chart simplifies managing cluster version of VictoriaMetrics in Kubernetes.
It is available in the [helm-charts](https://github.com/VictoriaMetrics/helm-charts) repository.


## Kubernetes operator

[K8s operator](https://github.com/VictoriaMetrics/operator) simplifies managing VictoriaMetrics components in Kubernetes.


## Binaries

Compiled binaries for the cluster version are available in the `assets` section of the [releases page](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/latest).
Also see archives containing the word `cluster`.

Docker images for the cluster version are available here:

- `vminsert` - [Docker Hub](https://hub.docker.com/r/victoriametrics/vminsert/tags) and [Quay](https://quay.io/repository/victoriametrics/vminsert?tab=tags)
- `vmselect` - [Docker Hub](https://hub.docker.com/r/victoriametrics/vmselect/tags) and [Quay](https://quay.io/repository/victoriametrics/vmselect?tab=tags)
- `vmstorage` - [Docker Hub](https://hub.docker.com/r/victoriametrics/vmstorage/tags) and [Quay](https://quay.io/repository/victoriametrics/vmstorage?tab=tags)


## Building from sources

The source code for the cluster version is available in the [cluster branch](https://github.com/VictoriaMetrics/VictoriaMetrics/tree/cluster).

### Production builds

There is no need to install Go on a host system since binaries are built
inside [the official docker container for Go](https://hub.docker.com/_/golang).
This allows reproducible builds.
So [install docker](https://docs.docker.com/install/) and run the following command:

```bash
make vminsert-prod vmselect-prod vmstorage-prod
```

Production binaries are built into statically linked binaries. They are put into the `bin` folder with `-prod` suffixes:

```bash
$ make vminsert-prod vmselect-prod vmstorage-prod
$ ls -1 bin
vminsert-prod
vmselect-prod
vmstorage-prod
```

### Development Builds

1. [Install go](https://golang.org/doc/install).
1. Run `make` from [the repository root](https://github.com/VictoriaMetrics/VictoriaMetrics). It should build `vmstorage`, `vmselect`
   and `vminsert` binaries and put them into the `bin` folder.

### Building docker images

Run `make package`. It will build the following docker images locally:

- `victoriametrics/vminsert:<PKG_TAG>`
- `victoriametrics/vmselect:<PKG_TAG>`
- `victoriametrics/vmstorage:<PKG_TAG>`

`<PKG_TAG>` is auto-generated image tag, which depends on source code in [the repository](https://github.com/VictoriaMetrics/VictoriaMetrics).
The `<PKG_TAG>` may be manually set via `PKG_TAG=foobar make package`.

By default, images are built on top of [alpine](https://hub.docker.com/_/scratch) image in order to improve debuggability.
It is possible to build an image on top of any other base image by setting it via `<ROOT_IMAGE>` environment variable.
For example, the following command builds images on top of [scratch](https://hub.docker.com/_/scratch) image:

```bash
ROOT_IMAGE=scratch make package
```


## Environment variables

See [these docs](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#environment-variables).


## Profiling

All the cluster components provide the following handlers for [profiling](https://blog.golang.org/profiling-go-programs):

- `http://vminsert:8480/debug/pprof/heap` for memory profile and `http://vminsert:8480/debug/pprof/profile` for CPU profile
- `http://vmselect:8481/debug/pprof/heap` for memory profile and `http://vmselect:8481/debug/pprof/profile` for CPU profile
- `http://vmstorage:8482/debug/pprof/heap` for memory profile and `http://vmstorage:8482/debug/pprof/profile` for CPU profile

Example command for collecting cpu profile from `vmstorage` (replace `0.0.0.0` with `vmstorage` hostname if needed):

```bash
curl http://0.0.0.0:8482/debug/pprof/profile > cpu.pprof
```

Example command for collecting memory profile from `vminsert` (replace `0.0.0.0` with `vminsert` hostname if needed):

```bash
curl http://0.0.0.0:8480/debug/pprof/heap > mem.pprof
```

It is safe sharing the collected profiles from security point of view, since they do not contain sensitive information.


## Community and contributions

Feel free asking any questions regarding VictoriaMetrics:

- [Slack Inviter](https://slack.victoriametrics.com/) and [Slack channel](https://victoriametrics.slack.com/)
- [X (Twitter)](https://x.com/VictoriaMetrics/)
- [Linkedin](https://www.linkedin.com/company/victoriametrics/)
- [Reddit](https://www.reddit.com/r/VictoriaMetrics/)
- [Telegram-en](https://t.me/VictoriaMetrics_en)
- [Telegram-ru](https://t.me/VictoriaMetrics_ru1)
- [Mastodon](https://mastodon.social/@victoriametrics/)

If you like VictoriaMetrics and want contributing, then please read [these docs](https://docs.victoriametrics.com/victoriametrics/contributing/).


## Reporting bugs

Report bugs and propose new features in our [GitHub Issues](https://github.com/VictoriaMetrics/VictoriaMetrics/issues).


## List of command-line flags

- [List of command-line flags for vminsert](#list-of-command-line-flags-for-vminsert)
- [List of command-line flags for vmselect](#list-of-command-line-flags-for-vmselect)
- [List of command-line flags for vmstorage](#list-of-command-line-flags-for-vmstorage)

### List of command-line flags for vminsert

Pass `-help` to vminsert in order to see the list of supported command-line flags with their description.

#### Common vminsert flags
These flags are available in both VictoriaMetrics OSS and VictoriaMetrics Enterprise.
{{% content "vminsert_common_flags.md" %}}

#### Enterprise vminsert flags
These flags are available only in [VictoriaMetrics enterprise](https://docs.victoriametrics.com/victoriametrics/enterprise/).
{{% content "vminsert_enterprise_flags.md" %}}


### List of command-line flags for vmselect

Pass `-help` to vmselect in order to see the list of supported command-line flags with their description.

#### Common vmselect flags
These flags are available in both VictoriaMetrics OSS and VictoriaMetrics Enterprise.
{{% content "vmselect_common_flags.md" %}}

#### Enterprise vmselect flags
These flags are available only in [VictoriaMetrics enterprise](https://docs.victoriametrics.com/victoriametrics/enterprise/).
{{% content "vmselect_enterprise_flags.md" %}}

### List of command-line flags for vmstorage

Pass `-help` to vmstorage in order to see the list of supported command-line flags with their description.

#### Common vmstorage flags
These flags are available in both VictoriaMetrics OSS and VictoriaMetrics Enterprise.
{{% content "vmstorage_common_flags.md" %}}

#### Enterprise vmstorage flags
These flags are available only in [VictoriaMetrics enterprise](https://docs.victoriametrics.com/victoriametrics/enterprise/).
{{% content "vmstorage_enterprise_flags.md" %}}
