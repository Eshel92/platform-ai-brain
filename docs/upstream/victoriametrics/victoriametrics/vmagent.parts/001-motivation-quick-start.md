<!-- Part 1 of 8 of victoriametrics/vmagent.md (split because the page is big). -->

## Motivation

While VictoriaMetrics provides an efficient solution to store and observe metrics, our users needed something fast
and RAM-friendly to scrape metrics from Prometheus-compatible exporters into VictoriaMetrics.
Also, we found that our users' infrastructure is like snowflakes in that no two are alike. Therefore, we decided to add more flexibility
to `vmagent` such as the ability to [accept metrics via popular push protocols](#how-to-push-data-to-vmagent)
and to [discover Prometheus-compatible targets and scrape metrics from them](#how-to-collect-metrics-in-prometheus-format).


## Features

* Can be used as a drop-in replacement for Prometheus for discovering and scraping targets such as [node_exporter](https://github.com/prometheus/node_exporter).
  Note that single-node VictoriaMetrics can also discover and scrape Prometheus-compatible targets in the same way `vmagent` does -
  see [these docs](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#how-to-scrape-prometheus-exporters-such-as-node-exporter).
* Can add, remove, and modify labels (aka tags) via Prometheus relabeling and filter data before sending it to remote storage. See [these docs](https://docs.victoriametrics.com/victoriametrics/relabeling/) for details.
* Can accept data via all the ingestion protocols supported by VictoriaMetrics. See [these docs](#how-to-push-data-to-vmagent).
* Can aggregate incoming samples by time and by labels before sending them to remote storage. See [these docs](https://docs.victoriametrics.com/victoriametrics/stream-aggregation/).
* Can replicate collected metrics simultaneously to multiple Prometheus-compatible remote storage systems . See [these docs](#replication-and-high-availability).
* Can save egress network bandwidth usage costs when [VictoriaMetrics remote write protocol](#victoriametrics-remote-write-protocol)
  is used to send data to VictoriaMetrics.
* Works smoothly in environments with unstable connections to remote storage. If the remote storage is unavailable, the collected metrics
  are buffered at `-remoteWrite.tmpDataPath`. The buffered metrics are sent to remote storage as soon as the connection
  to the remote storage is repaired. The maximum disk usage for the buffer can be limited with `-remoteWrite.maxDiskUsagePerURL`.
* Uses much lower amounts of RAM, CPU, disk IO, and network bandwidth than Prometheus. The RAM usage and CPU usage can be reduced further
  if needed according to [these docs](#performance-optimizations).
* Scrape targets can be spread among multiple `vmagent` instances when a large number of targets must be scraped. See [these docs](#scraping-big-number-of-targets).
* Can load scrape configs from multiple files. See [these docs](#loading-scrape-configs-from-multiple-files).
* Can efficiently scrape targets that expose millions of time series, such as the [/federate endpoint in Prometheus](https://prometheus.io/docs/prometheus/latest/federation/).
  See [these docs](#stream-parsing-mode).
* Can deal with [high cardinality](https://docs.victoriametrics.com/victoriametrics/faq/#what-is-high-cardinality)
  and [high churn rate](https://docs.victoriametrics.com/victoriametrics/faq/#what-is-high-churn-rate) issues by limiting the number of unique time series at scrape time
  and before sending them to remote storage systems. See [these docs](#cardinality-limiter).
* Can write collected metrics to multiple tenants. See [these docs](#multitenancy).
* Can read and write data from / to Kafka. See [these docs](https://docs.victoriametrics.com/victoriametrics/integrations/kafka/).
* Can read and write data from / to Google PubSub. See [these docs](https://docs.victoriametrics.com/victoriametrics/integrations/pubsub/).


## Quick Start

Download `vmutils-*` archive from [releases page](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/latest) (
`vmagent` is also available in Docker images [Docker Hub](https://hub.docker.com/r/victoriametrics/vmagent/tags) and [Quay](https://quay.io/repository/victoriametrics/vmagent?tab=tags)),
unpack it, and pass the following flags to the `vmagent` binary in order to start scraping Prometheus-compatible targets
and sending the data to the Prometheus-compatible remote storage:

* `-promscrape.config` with the path to the [Prometheus config file](https://docs.victoriametrics.com/victoriametrics/sd_configs/) (usually located at `/etc/prometheus/prometheus.yml`).
  The path can point either to a local file or to an HTTP URL. See [scrape config examples](https://docs.victoriametrics.com/victoriametrics/scrape_config_examples/).
  `vmagent` doesn't support some sections of the Prometheus config file, so you may need either to delete these sections or
   to run `vmagent` with `-promscrape.config.strictParse=false` command-line flag.
  In this case, `vmagent` ignores unsupported sections. See [the list of unsupported sections](#unsupported-prometheus-config-sections).
* `-remoteWrite.url` of a Prometheus-compatible remote storage endpoint (e.g., VictoriaMetrics) to send data to.
  The `-remoteWrite.url` may refer to a [DNS SRV](https://en.wikipedia.org/wiki/SRV_record) address. See [these docs](#srv-urls) for details.

Example command for writing the data received via [supported push-based protocols](#how-to-push-data-to-vmagent)
to [single-node VictoriaMetrics](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/) located at `victoria-metrics-host:8428`:

```sh
/path/to/vmagent -remoteWrite.url=https://victoria-metrics-host:8428/api/v1/write
```

See [these docs](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/#url-format) if you need to write data to a [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/).

Example command for scraping Prometheus targets and writing the data to single-node VictoriaMetrics:

```sh
/path/to/vmagent -promscrape.config=/path/to/prometheus.yml -remoteWrite.url=https://victoria-metrics-host:8428/api/v1/write
```

See [how to scrape Prometheus-compatible targets](#how-to-collect-metrics-in-prometheus-format) for more details.

If you use single-node VictoriaMetrics, then you can discover and scrape Prometheus-compatible targets directly from VictoriaMetrics
without the need to use `vmagent` . See [these docs](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#how-to-scrape-prometheus-exporters-such-as-node-exporter).

`vmagent` can reduce network bandwidth costs under high load when the [VictoriaMetrics remote write protocol is used](#victoriametrics-remote-write-protocol).

Common `vmagent` issues are covered in the [troubleshooting docs](#troubleshooting).

See [various use cases](#use-cases) for vmagent.

Pass `-help` to `vmagent` in order to see [the full list of supported command-line flags with their descriptions](#advanced-usage).
