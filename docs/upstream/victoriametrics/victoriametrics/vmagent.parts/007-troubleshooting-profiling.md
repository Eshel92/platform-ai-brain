<!-- Part 7 of 8 of victoriametrics/vmagent.md (split because the page is big). -->

## Troubleshooting

* It is recommended [to set up the official Grafana dashboard](#monitoring) in order to monitor the state of `vmagent`.

* It is recommended to increase the maximum number of open files in the system (`ulimit -n`) when scraping a large number of targets,
  as `vmagent` establishes at least one TCP connection per target.

* If `vmagent` uses too much RAM or CPU, then follow [these recommendations](#performance-optimizations).

* When `vmagent` scrapes many unreliable targets, it can flood the error log with scrape errors. It is recommended to investigate and fix these errors.
  If it is unfeasible to fix all the reported errors, then scrape errors logging can be disabled completely by passing the `-promscrape.suppressScrapeErrors` command-line flag to `vmagent`.
  Repeated errors for failed scrapes (such as network errors or timeouts) per each target can be logged less frequently with the `-promscrape.suppressScrapeErrorsDelay` command-line flag.
  This flag doesn't apply to errors when parsing the scraped response.
  The number of logged parse errors per each scrape of a target is limited by the `-promscrape.maxParseErrorsPerScrape` command-line flag {{% available_from "v1.155.0" %}};
  the number of suppressed parse errors is logged after the scrape.
  The most recent scrape error for each target can be observed at `http://vmagent-host:8429/targets` and `http://vmagent-host:8429/api/v1/targets`.

* The `http://vmagent-host:8429/config` page shows the current active `-promscrape.config` configuration.
  Access to the endpoint can be protected via the `-configAuthKey` command-line flag.

* Pages `http://vmagent-host:8429/remotewrite-relabel-config` and `http://vmagent-host:8429/remotewrite-url-relabel-config`
  {{% available_from "v1.129.0" %}} show current active `-remoteWrite.relabelConfig` and `-remoteWrite.urlRelabelConfig` configuration
  correspondingly. Access to endpoints can be protected via the `-configAuthKey` command-line flag.

* The `http://vmagent-host:8429/service-discovery` page could be useful for debugging the relabeling process for scrape targets.
  This page contains original labels for targets dropped during relabeling.
  By default, the `-promscrape.maxDroppedTargets` targets are shown here. If your setup drops more targets during relabeling,
  then increase the `-promscrape.maxDroppedTargets` command-line flag value to see all the dropped targets.
  Note that tracking each dropped target requires up to 10Kb of RAM. Therefore, big values for `-promscrape.maxDroppedTargets`
  may result in increased memory usage if a large number of scrape targets are dropped during relabeling.

* It is recommended to increase `-remoteWrite.queues` if `vmagent_remotewrite_pending_data_bytes` [metric](#monitoring)
  grows constantly. It is also recommended to increase `-remoteWrite.maxBlockSize` and `-remoteWrite.maxRowsPerBlock` command-line flags in this case.
  This can improve data ingestion performance to the configured remote storage systems at the cost of higher memory usage.

* If you see gaps in the data pushed by `vmagent` to remote storage when `-remoteWrite.maxDiskUsagePerURL` is set,
  try increasing `-remoteWrite.queues`. Such gaps may appear because `vmagent` cannot keep up with sending the collected data to remote storage.
  Therefore, it starts dropping the buffered data if the on-disk buffer size exceeds `-remoteWrite.maxDiskUsagePerURL`.

* `vmagent` drops data blocks if remote storage replies with `400 Bad Request` or `409 Conflict` HTTP responses.
  The number of dropped blocks can be monitored via the `vmagent_remotewrite_packets_dropped_total` metric, which is exported on the [/metrics page](#monitoring).

* Use `-remoteWrite.queues=1` when `-remoteWrite.url` points to remote storage, which doesn't accept out-of-order samples (aka data backfilling).
  Such storage systems include Prometheus, Mimir, Cortex, and Thanos, which typically emit `out of order sample` errors.
  The best solution is to use remote storage with [backfilling support](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#backfilling) such as VictoriaMetrics.

* `vmagent` buffers scraped data at the `-remoteWrite.tmpDataPath` directory until it is sent to `-remoteWrite.url`.
  The directory can grow large when remote storage is unavailable for extended periods of time, and if the maximum directory size isn't limited
  with the `-remoteWrite.maxDiskUsagePerURL` command-line flag.
  If you don't want to send all the buffered data from the directory to remote storage, then simply stop `vmagent` and delete the directory.

* If `vmagent` runs on a host with slow persistent storage, which cannot keep up with the volume of processed samples, then it is possible to disable
  the persistent storage with the `-remoteWrite.disableOnDiskQueue` command-line flag. See [these docs](#disabling-on-disk-persistence) for more details.

* By default, `vmagent` masks `-remoteWrite.url` with `secret-url` values in logs and at the `/metrics` page because
  the URL may contain sensitive information such as auth tokens or passwords.
  Pass `-remoteWrite.showURL` command-line flag when starting `vmagent` in order to see all the valid URLs.

* By default, `vmagent` evenly spreads scrape load in time. If a particular scrape target must be scraped at the beginning of some interval,
  then the `scrape_align_interval` option must be used. For example, the following config aligns hourly scrapes to the beginning of the hour:

  ```yaml
  scrape_configs:
  - job_name: foo
    scrape_interval: 1h
    scrape_align_interval: 1h
  ```

* By default, vmagent evenly spreads scrape load in time. If a particular scrape target needs scraping at a specific offset, use the `scrape_offset` option.
  For example, the following config instructs `vmagent` to scrape the target 10 seconds after the start of every 1-minute interval:

  ```yaml
  scrape_configs:
  - job_name: foo
    scrape_interval: 1m
    scrape_offset: 10s
  ```

* If you see `skipping duplicate scrape target with identical labels` errors when scraping Kubernetes pods, then it is likely these pods listen to multiple ports
  or they use an init container. These errors can either be fixed or suppressed with the `-promscrape.suppressDuplicateScrapeTargetErrors` command-line flag.
  See the available options below if you prefer fixing the root cause of the error:

  The following relabeling rule may be added to the `relabel_configs` section in order to filter out pods with unneeded ports:

  ```yaml
  - action: keep_if_equal
    source_labels: [__meta_kubernetes_pod_annotation_prometheus_io_port, __meta_kubernetes_pod_container_port_number]
  ```

  The following relabeling rule may be added to the `relabel_configs` section in order to filter out init container pods:

  ```yaml
  - action: drop
    source_labels: [__meta_kubernetes_pod_container_init]
    regex: true
  ```

See also:

* [Relabel Debugging](https://docs.victoriametrics.com/victoriametrics/relabeling/#relabel-debugging)
* [General Troubleshooting](https://docs.victoriametrics.com/victoriametrics/troubleshooting/)


## Calculating disk space for persistence queue

`vmagent` buffers collected metrics on disk at the directory specified via `-remoteWrite.tmpDataPath` command-line flag
until the metrics are sent to remote storage configured via `-remoteWrite.url` command-line flag.
The `-remoteWrite.tmpDataPath` directory can grow large when remote storage is unavailable for extended
periods of time and if the maximum directory size isn't limited with the `-remoteWrite.maxDiskUsagePerURL` command-line flag.

To estimate the allocated disk size for the persistent queue, or to estimate the `-remoteWrite.maxDiskUsagePerURL` command-line flag value,
take into account the following attributes:

1. The **size in bytes** of the data stream sent by vmagent:

   Run the query `sum(rate(vmagent_remotewrite_bytes_sent_total[1h])) by(instance,url)` in [vmui](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#vmui)
   or Grafana to get the amount of bytes sent by each vmagent instance per second.

1. The amount of **time** a persistent queue should keep the data before starting to drop it.

   For example, if `vmagent` should be able to buffer the data for at least 6 hours, then the following query
   can be used for estimating the needed amounts of disk space in gigabytes:

   ```metricsql
   sum(rate(vmagent_remotewrite_bytes_sent_total[1h])) by(instance,url) * 6h / 1Gi
   ```

Additional notes:

1. Ensure that `vmagent` [monitoring](#monitoring) is configured properly.
1. Re-evaluate the estimation each time when:
    * there is an increase in the vmagent's workload
    * there is a change in [relabeling rules](https://docs.victoriametrics.com/victoriametrics/relabeling/) which could increase the amount metrics to send
    * there is a change in the number of configured `-remoteWrite.url` addresses
1. The minimum disk size to allocate for the persistent queue is 500Mi per each `-remoteWrite.url`.
1. The on-disk persistent queue can be disabled if needed. See [these docs](https://docs.victoriametrics.com/victoriametrics/vmagent/#disabling-on-disk-persistence).


## Security

See general recommendations regarding [security](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#security).

vmagent's `/remotewrite-relabel-config` and `/remotewrite-url-relabel-config` endpoints {{% available_from "v1.129.0" %}}
can be protected via the `-configAuthKey` command-line flag.

### mTLS protection

By default, `vmagent` accepts HTTP requests at port `8429` (this port can be changed via `-httpListenAddr` command-line flags).
It is expected that `vmagent` runs in an isolated, trusted network.
The [Enterprise version of vmagent](https://docs.victoriametrics.com/victoriametrics/enterprise/) supports the ability to accept [mTLS](https://en.wikipedia.org/wiki/Mutual_authentication)
requests at this port, by specifying `-tls` and `-mtls` command-line flags. For example, the following command runs `vmagent`, which accepts only mTLS requests at port `8429`:

```sh
./vmagent -tls -mtls -remoteWrite.url=...
```

By default, the system-wide [TLS Root CA](https://en.wikipedia.org/wiki/Root_certificate) is used for verifying client certificates if the `-mtls` command-line flag is specified.
It is possible to specify a custom TLS Root CA via the `-mtlsCAFile` command-line flag.


## Performance optimizations

`vmagent` is optimized for low CPU and RAM usage, with no need to tune any configs. Sometimes, however, it is necessary to further optimize the CPU/RAM usage of `vmagent`.
For example, if `vmagent` needs to scrape thousands of targets in resource-constrained environments, then the following options may help to reduce CPU and RAM usage:

* Set the [GOGC](https://pkg.go.dev/runtime#hdr-Environment_Variables) environment variable to `100`. This reduces CPU usage at the cost of higher RAM usage.

* Set [GOMAXPROCS](https://pkg.go.dev/runtime#hdr-Environment_Variables) environment variable to a value slightly bigger than the number of CPU cores used by `vmagent`.
  Another option is to set the CPU limit in Kubernetes / Docker to an integer value bigger than the number of CPU cores used by `vmagent`.
  This reduces RAM and CPU usage when `vmagent` runs in an environment with a large number of available CPU cores. Note that it may be necessary to increase the `-remoteWrite.queues`
  command-line flag to a larger value if `GOMAXPROCS` is set to too small of a value, since by default `-remoteWrite.queues` is proportional to `GOMAXPROCS`.

* Avoid increasing the value for the `-maxConcurrentRequests` command-line flag. The default value is optimized for the best performance in most cases,
  even if many clients send data to `vmagent` via many concurrent connections and the number of these connections significantly exceeds the default value
  for the `-maxConcurrentRequests` command-line flag. `vmagent` puts incoming requests into a wait queue if the number of concurrently executed requests
  exceeds `-maxConcurrentRequests`. The pending requests at the wait queue do not consume CPU and do not consume significant amounts of RAM, so it is OK to have
  thousands of pending requests in the wait queue. Pending requests in the wait queue are canceled if they wait for their execution for longer than
  the duration specified in the `-insert.maxQueueDuration` command-line flag. Canceled requests can be [monitored](https://docs.victoriametrics.com/victoriametrics/vmagent/#monitoring)
  via `vm_concurrent_insert_limit_timeout_total` metric.

* Disable response compression at scrape targets via `-promscrape.disableCompression` command-line flag or via `disable_compression: true` option
  in the [scrape_config](https://docs.victoriametrics.com/victoriametrics/sd_configs/#scrape_configs). This reduces CPU usage at the cost of higher network bandwidth usage
  between `vmagent` and scrape targets.

* Disable tracking of original labels for the discovered targets via `-promscrape.dropOriginalLabels` command-line flag. This helps to reduce RAM usage when `vmagent`
  discovers a large number of scrape targets, and the majority of these targets are [dropped](https://docs.victoriametrics.com/victoriametrics/relabeling/#how-to-drop-discovered-targets).
  This is a typical case when `vmagent` discovers Kubernetes targets. The downside of using the `-promscrape.dropOriginalLabels` command-line flag
  is the reduced [debuggability](https://docs.victoriametrics.com/victoriametrics/relabeling/#relabel-debugging) for improperly configured per-target relabeling.

* Disable [staleness markers](https://docs.victoriametrics.com/victoriametrics/vmagent/#prometheus-staleness-markers) via `-promscrape.noStaleMarkers` command-line flag
  or via `no_stale_markers: true` option in the [scrape_config](https://docs.victoriametrics.com/victoriametrics/sd_configs/#scrape_configs). This reduces RAM and CPU usage.
  Note that disabling staleness markers may yield unexpected query results when scrape targets are frequently rotated (which is typical in Kubernetes).

* Set `-memory.allowedBytes` command-line flag to a value close to the actual memory usage of `vmagent`. Another option is to set the memory limit in Kubernetes / Docker
  to the value 50% larger than the actual memory usage of `vmagent`. This should reduce memory usage spikes for `vmagent` running in the environment with a large amount of available memory and
  when the remote storage cannot keep up with the data ingestion rate. Increasing the `-remoteWrite.queues` command-line flag value may help in this case, too.

* In extreme cases, it may be useful to set the `-promscrape.disableKeepAlive` command-line flag in order to save RAM on HTTP keep-alive connections to thousands of scrape targets.

* Increase the `scrape_interval` option in the `global` section of the `-promscrape.config` and/or at every [scrape_config](https://docs.victoriametrics.com/victoriametrics/sd_configs/#scrape_configs)
  to reduce CPU usage. For example, increasing the `scrape_interval` from `10s` to `30s` across all targets reduces CPU usage on `vmagent` by up to 3x.

Example command, which runs `vmagent` in an optimized mode:

```sh
GOGC=100 GOMAXPROCS=1 ./vmagent -promscrape.disableCompression -promscrape.dropOriginalLabels -promscrape.noStaleMarkers -memory.allowedBytes=1GiB -promscrape.disableKeepAlive ...
```


## How to build from sources

We recommend using the [official binary releases](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/latest) - `vmagent` is located in the `vmutils-...` archives.

It may be necessary to build `vmagent` from source code when developing or testing a new feature or bug fix.

### Development build

1. [Install Go](https://golang.org/doc/install).
1. Run `make vmagent` from the root folder of [the repository](https://github.com/VictoriaMetrics/VictoriaMetrics).
   It builds the `vmagent` binary and puts it into the `bin` folder.

### Production build

1. [Install Docker](https://docs.docker.com/install/).
1. Run `make vmagent-prod` from the root folder of [the repository](https://github.com/VictoriaMetrics/VictoriaMetrics).
   It builds the `vmagent-prod` binary and puts it into the `bin` folder.

### Building docker images

Run `make package-vmagent`. It builds `victoriametrics/vmagent:<PKG_TAG>` docker image locally.
`<PKG_TAG>` is an auto-generated image tag, which depends on source code in [the repository](https://github.com/VictoriaMetrics/VictoriaMetrics).
The `<PKG_TAG>` may be manually set via `PKG_TAG=foobar make package-vmagent`.

The base Docker image is [alpine](https://hub.docker.com/_/alpine), but it is possible to use any other base image
by setting it via the `<ROOT_IMAGE>` environment variable. For example, the following command builds the image on top of [scratch](https://hub.docker.com/_/scratch) image:

```sh
ROOT_IMAGE=scratch make package-vmagent
```

### ARM build

ARM build may run on Raspberry Pi or on [energy-efficient ARM servers](https://blog.cloudflare.com/arm-takes-wing/).

### Development ARM build

1. [Install Go](https://golang.org/doc/install).
1. Run `make vmagent-linux-arm` or `make vmagent-linux-arm64` from the root folder of [the repository](https://github.com/VictoriaMetrics/VictoriaMetrics)
   It builds `vmagent-linux-arm` or `vmagent-linux-arm64` binary, respectively, and puts it into the `bin` folder.

### Production ARM build

1. [Install Docker](https://docs.docker.com/install/).
1. Run `make vmagent-linux-arm-prod` or `make vmagent-linux-arm64-prod` from the root folder of [the repository](https://github.com/VictoriaMetrics/VictoriaMetrics).
   It builds `vmagent-linux-arm-prod` or `vmagent-linux-arm64-prod` binary, respectively, and puts it into the `bin` folder.


## Profiling

`vmagent` provides handlers for collecting the following [Go profiles](https://blog.golang.org/profiling-go-programs):

* Memory profile can be collected with the following command (replace `0.0.0.0` with hostname if needed):

```sh
curl http://0.0.0.0:8429/debug/pprof/heap > mem.pprof
```

* CPU profile can be collected with the following command (replace `0.0.0.0` with hostname if needed):

```sh
curl http://0.0.0.0:8429/debug/pprof/profile > cpu.pprof
```

The command for collecting the CPU profile waits for 30 seconds before returning.

The collected profiles may be analyzed with [go tool pprof](https://github.com/google/pprof).

It is safe to share the collected profiles from a security perspective, since they do not contain sensitive information.
