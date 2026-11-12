<!-- Part 1 of 13 of victoriametrics/README.md (split because the page is big). -->

## Prominent features

VictoriaMetrics has the following prominent features:

* It can be used as long-term storage for Prometheus. See [these docs](https://docs.victoriametrics.com/victoriametrics/integrations/prometheus/) for details.
* It can be used as a drop-in replacement for Prometheus in Grafana, because it supports the [Prometheus querying API](#prometheus-querying-api-usage).
* It can be used as a drop-in replacement for Graphite in Grafana, because it supports the [Graphite API](https://docs.victoriametrics.com/victoriametrics/integrations/graphite/#graphite-api-usage).
  VictoriaMetrics allows reducing infrastructure costs by more than 10x comparing to Graphite - see [this case study](https://docs.victoriametrics.com/victoriametrics/casestudies/#grammarly).
* It is easy to setup and operate:
  * VictoriaMetrics consists of a single [small executable](https://medium.com/@valyala/stripping-dependency-bloat-in-victoriametrics-docker-image-983fb5912b0d)
    without external dependencies.
  * All the configuration is done via explicit command-line flags with reasonable defaults.
  * All the data is stored in a single directory specified by the `-storageDataPath` command-line flag.
  * Easy and fast backups from [instant snapshots](https://medium.com/@valyala/how-victoriametrics-makes-instant-snapshots-for-multi-terabyte-time-series-data-e1f3fb0e0282)
    can be done with [vmbackup](https://docs.victoriametrics.com/victoriametrics/vmbackup/) / [vmrestore](https://docs.victoriametrics.com/victoriametrics/vmrestore/) tools.
    See [this article](https://medium.com/@valyala/speeding-up-backups-for-big-time-series-databases-533c1a927883) for more details.
* It supports storage and retrieval of samples with timestamps that fall within the `[1970-01-02T00:00:00.000Z, 2262-03-31T23:59:59.999Z]` time range with millisecond precision.
  See [Retention](#retention) for details.
* It implements a PromQL-like query language - [MetricsQL](https://docs.victoriametrics.com/victoriametrics/metricsql/), which provides improved functionality on top of PromQL.
* It provides a global query view. Multiple Prometheus instances or any other data sources may ingest data into VictoriaMetrics. Later this data may be queried via a single query.
* It provides high performance and good vertical and horizontal scalability for both
  [data ingestion](https://medium.com/@valyala/high-cardinality-tsdb-benchmarks-victoriametrics-vs-timescaledb-vs-influxdb-13e6ee64dd6b)
  and [data querying](https://medium.com/@valyala/when-size-matters-benchmarking-victoriametrics-vs-timescale-and-influxdb-6035811952d4).
  It [outperforms InfluxDB and TimescaleDB by up to 20x](https://medium.com/@valyala/measuring-vertical-scalability-for-time-series-databases-in-google-cloud-92550d78d8ae).
* It [uses 10x less RAM than InfluxDB](https://medium.com/@valyala/insert-benchmarks-with-inch-influxdb-vs-victoriametrics-e31a41ae2893)
  and [up to 7x less RAM than Prometheus, Thanos or Cortex](https://valyala.medium.com/prometheus-vs-victoriametrics-benchmark-on-node-exporter-metrics-4ca29c75590f)
  when dealing with millions of unique time series (aka [high cardinality](https://docs.victoriametrics.com/victoriametrics/faq/#what-is-high-cardinality)).
* It is optimized for time series with [high churn rate](https://docs.victoriametrics.com/victoriametrics/faq/#what-is-high-churn-rate).
* It provides high data compression: up to 70x more data points may be stored into limited storage compared with TimescaleDB
  according to [these benchmarks](https://medium.com/@valyala/when-size-matters-benchmarking-victoriametrics-vs-timescale-and-influxdb-6035811952d4),
  and up to 7x less storage space is required compared to Prometheus, Thanos or Cortex.
  according to [this benchmark](https://valyala.medium.com/prometheus-vs-victoriametrics-benchmark-on-node-exporter-metrics-4ca29c75590f).
* It is optimized for storage with high-latency IO and low IOPS (HDD and network storage in AWS, Google Cloud, Microsoft Azure, etc).
  See [disk IO graphs from these benchmarks](https://medium.com/@valyala/high-cardinality-tsdb-benchmarks-victoriametrics-vs-timescaledb-vs-influxdb-13e6ee64dd6b).
* A single-node VictoriaMetrics may substitute moderately sized clusters built with competing solutions such as Thanos, M3DB, Cortex, InfluxDB or TimescaleDB.
  See [vertical scalability benchmarks](https://medium.com/@valyala/measuring-vertical-scalability-for-time-series-databases-in-google-cloud-92550d78d8ae),
  [comparing Thanos to VictoriaMetrics cluster](https://medium.com/@valyala/comparing-thanos-to-victoriametrics-cluster-b193bea1683)
  and [Remote Write Storage Wars](https://promcon.io/2019-munich/talks/remote-write-storage-wars/) talk
  from [PromCon 2019](https://promcon.io/2019-munich/talks/remote-write-storage-wars/).
* It protects the storage from data corruption on unclean shutdown (i.e. OOM, hardware reset or `kill -9`) thanks to
  [the storage architecture](https://medium.com/@valyala/how-victoriametrics-makes-instant-snapshots-for-multi-terabyte-time-series-data-e1f3fb0e0282).
* It supports metrics scraping, ingestion and [backfilling](#backfilling) via the following protocols:
  * [Metrics scraping from Prometheus exporters](#how-to-scrape-prometheus-exporters-such-as-node-exporter).
  * [Prometheus remote write API](https://docs.victoriametrics.com/victoriametrics/integrations/prometheus/).
  * [Prometheus exposition format](#how-to-import-data-in-prometheus-exposition-format).
  * [InfluxDB line protocol](https://docs.victoriametrics.com/victoriametrics/integrations/influxdb/) over HTTP, TCP and UDP.
  * [Graphite plaintext protocol](https://docs.victoriametrics.com/victoriametrics/integrations/graphite/#ingesting) with [tags](https://graphite.readthedocs.io/en/latest/tags.html#carbon).
  * [OpenTSDB put message](https://docs.victoriametrics.com/victoriametrics/integrations/opentsdb/#sending-data-via-telnet).
  * [HTTP OpenTSDB /api/put requests](https://docs.victoriametrics.com/victoriametrics/integrations/opentsdb/#sending-data-via-http).
  * [JSON line format](#how-to-import-data-in-json-line-format).
  * [Arbitrary CSV data](#how-to-import-csv-data).
  * [Native binary format](#how-to-import-data-in-native-format).
  * [DataDog agent or DogStatsD](https://docs.victoriametrics.com/victoriametrics/integrations/datadog/).
  * [NewRelic infrastructure agent](https://docs.victoriametrics.com/victoriametrics/integrations/newrelic/#sending-data-from-agent).
  * [OpenTelemetry metrics format](https://docs.victoriametrics.com/victoriametrics/integrations/opentelemetry/).
  * [Zabbix Connector streaming format](https://docs.victoriametrics.com/victoriametrics/integrations/zabbixconnector/#send-data-from-zabbix-connector).
* It supports powerful [stream aggregation](https://docs.victoriametrics.com/victoriametrics/stream-aggregation/), which can be used as a [statsd](https://github.com/statsd/statsd) alternative.
* It supports metrics [relabeling](#relabeling).
* It can deal with [high cardinality issues](https://docs.victoriametrics.com/victoriametrics/faq/#what-is-high-cardinality) and
  [high churn rate](https://docs.victoriametrics.com/victoriametrics/faq/#what-is-high-churn-rate) issues via [series limiter](#cardinality-limiter).
* It ideally works for big amounts of time series with both [high churn rate](https://docs.victoriametrics.com/victoriametrics/faq/#what-is-high-churn-rate) (APM, Kubernetes)
  and low churn rate (IoT sensors, connected cars, industrial telemetry, financial data - see
  [these docs](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#index-tuning-for-low-churn-rate)),
  plus various [Enterprise workloads](https://docs.victoriametrics.com/victoriametrics/enterprise/).
* It has an open source [cluster version](https://github.com/VictoriaMetrics/VictoriaMetrics/tree/cluster).
* It can store data on [NFS-based storages](https://en.wikipedia.org/wiki/Network_File_System) such as [Amazon EFS](https://aws.amazon.com/efs/)
  and [Google Filestore](https://cloud.google.com/filestore).

See [case studies for VictoriaMetrics](https://docs.victoriametrics.com/victoriametrics/casestudies/) and [various Articles about VictoriaMetrics](https://docs.victoriametrics.com/victoriametrics/articles/).


## Components

VictoriaMetrics ecosystem contains the following components additionally to [single-node VictoriaMetrics](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/):

* [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/) - lightweight agent for receiving metrics via [pull-based](https://docs.victoriametrics.com/victoriametrics/vmagent/#how-to-collect-metrics-in-prometheus-format)
  and [push-based](https://docs.victoriametrics.com/victoriametrics/vmagent/#how-to-push-data-to-vmagent) protocols, transforming and sending them to the configured Prometheus-compatible
  remote storage systems such as VictoriaMetrics.
* [vmalert](https://docs.victoriametrics.com/victoriametrics/vmalert/) - a service for processing Prometheus-compatible alerting and recording rules.
* [vmalert-tool](https://docs.victoriametrics.com/victoriametrics/vmalert-tool/) -  a tool for validating alerting and recording rules.
* [vmauth](https://docs.victoriametrics.com/victoriametrics/vmauth/) - authorization proxy and load balancer optimized for VictoriaMetrics products.
* [vmgateway](https://docs.victoriametrics.com/victoriametrics/vmgateway/) - authorization proxy with per-[tenant](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/#multitenancy) rate limiting capabilities.
* [vmctl](https://docs.victoriametrics.com/victoriametrics/vmctl/) - a tool for migrating and copying data between different storage systems for metrics.
* [vmbackup](https://docs.victoriametrics.com/victoriametrics/vmbackup/), [vmrestore](https://docs.victoriametrics.com/victoriametrics/vmrestore/) and [vmbackupmanager](https://docs.victoriametrics.com/victoriametrics/vmbackupmanager/) -
  tools for creating backups and restoring from backups for VictoriaMetrics data.
* `vminsert`, `vmselect` and `vmstorage` - components of [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/).
* [VictoriaLogs](https://docs.victoriametrics.com/victorialogs/) - user-friendly cost-efficient database for logs.


## Operation

### Install

To quickly try VictoriaMetrics, just download the [VictoriaMetrics executable](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/latest)
or docker image from [Docker Hub](https://hub.docker.com/r/victoriametrics/victoria-metrics/) or [Quay](https://quay.io/repository/victoriametrics/victoria-metrics?tab=tags) and start it with the desired command-line flags.
See also [QuickStart guide](https://docs.victoriametrics.com/victoriametrics/quick-start/) for additional information.

VictoriaMetrics can also be installed via these installation methods:

* [Helm charts for single-node and cluster versions of VictoriaMetrics](https://github.com/VictoriaMetrics/helm-charts).
* [Kubernetes operator for VictoriaMetrics](https://github.com/VictoriaMetrics/operator).
* [Ansible role for installing cluster VictoriaMetrics (by VictoriaMetrics)](https://github.com/VictoriaMetrics/ansible-playbooks).
* [Ansible role for installing cluster VictoriaMetrics (by community)](https://github.com/Slapper/ansible-victoriametrics-cluster-role).
* [Ansible role for installing single-node VictoriaMetrics (by community)](https://github.com/dreamteam-gg/ansible-victoriametrics-role).

### How to start VictoriaMetrics

The following command-line flags are used the most:

* `-storageDataPath` - VictoriaMetrics stores all the data in this directory. The default path is `victoria-metrics-data` in the current working directory.
* `-retentionPeriod` - retention for stored data. Older data is automatically deleted. Default retention is 1 month (31 days). The minimum retention period is 24h or 1d. See [these docs](#retention) for more details.

Other flags have good enough default values, so set them only if you really need to. Pass `-help` to see [all the available flags with description and default values](#list-of-command-line-flags).

The following docs may be useful during initial VictoriaMetrics setup:

* [How to set up scraping of Prometheus-compatible targets](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#how-to-scrape-prometheus-exporters-such-as-node-exporter)
* [How to ingest data to VictoriaMetrics](#how-to-import-time-series-data)
* [How to set up Prometheus to write data to VictoriaMetrics](https://docs.victoriametrics.com/victoriametrics/integrations/prometheus/)
* [How to query VictoriaMetrics via Grafana](https://docs.victoriametrics.com/victoriametrics/integrations/grafana/)
* [How to query VictoriaMetrics via Graphite API](https://docs.victoriametrics.com/victoriametrics/integrations/graphite/#graphite-api-usage)
* [How to handle alerts](#alerting)

VictoriaMetrics accepts [Prometheus querying API requests](#prometheus-querying-api-usage) on port `8428` by default.

It is recommended setting up [monitoring](#monitoring) for VictoriaMetrics.

### Environment variables

All the VictoriaMetrics components allow referring environment variables in `yaml` configuration files (such as `-promscrape.config`)
and in command-line flags via `%{ENV_VAR}` syntax.
For example, `-metricsAuthKey=%{METRICS_AUTH_KEY}` is automatically expanded to `-metricsAuthKey=top-secret`
if `METRICS_AUTH_KEY=top-secret` environment variable exists at VictoriaMetrics startup.
This expansion is performed by VictoriaMetrics itself.

VictoriaMetrics recursively expands `%{ENV_VAR}` references in environment variables on startup.
For example, `FOO=%{BAR}` environment variable is expanded to `FOO=abc` if `BAR=a%{BAZ}` and `BAZ=bc` environment variables exist.

Additionally, all the VictoriaMetrics components allow setting flag values via environment variables according to these rules:

* The `-envflag.enable` flag must be set.
* Each `.` char in flag name must be substituted with `_` (for example `-insert.maxQueueDuration <duration>` will translate to `insert_maxQueueDuration=<duration>`).
* Repeated flags can be replaced by an environment variable with comma separated values for the repeated flags.
  For example `-storageNode <nodeA> -storageNode <nodeB>` command-line flags can be set as `storageNode=<nodeA>,<nodeB>` environment variable.
* Environment var prefix can be set via `-envflag.prefix` flag. For instance, if `-envflag.prefix=VM_`, then env vars must be prepended with `VM_`.

### Setting up service

Read [instructions](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/43) on how to set up VictoriaMetrics
as a service for your OS. See also [ansible playbooks](https://github.com/VictoriaMetrics/ansible-playbooks).

### Running as Windows service

In order to run VictoriaMetrics as a Windows service it is required to create a service configuration for [WinSW](https://github.com/winsw/winsw)
and then install it as a service according to the following guide:

1. Create a service configuration:

    ```xml
    <service>
      <id>VictoriaMetrics</id>
      <name>VictoriaMetrics</name>
      <description>VictoriaMetrics</description>
      <executable>%BASE%\victoria-metrics-windows-amd64-prod.exe"</executable>

      <onfailure action="restart" delay="10 sec"/>
      <onfailure action="restart" delay="20 sec"/>

      <resetfailure>1 hour</resetfailure>

      <arguments>-envflag.enable</arguments>

      <priority>Normal</priority>

      <stoptimeout>15 sec</stoptimeout>

      <stopparentprocessfirst>true</stopparentprocessfirst>
        <startmode>Automatic</startmode>
        <waithint>15 sec</waithint>
        <sleeptime>1 sec</sleeptime>

      <logpath>%BASE%\logs</logpath>
      <log mode="roll">
        <sizeThreshold>10240</sizeThreshold>
        <keepFiles>8</keepFiles>
      </log>

      <env name="loggerFormat" value="json" />
      <env name="loggerOutput" value="stderr" />
      <env name="promscrape_config" value="C:\Program Files\victoria-metrics\promscrape.yml" />

    </service>
    ```

1. Install WinSW by following this [documentation](https://github.com/winsw/winsw#download).

1. Install VictoriaMetrics as a service by running the following from elevated PowerShell:

    ```sh
    winsw install VictoriaMetrics.xml
    Get-Service VictoriaMetrics | Start-Service
    ```

See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/3781) for more details.

### Start with docker-compose

[Docker-compose](https://github.com/VictoriaMetrics/VictoriaMetrics/tree/master/deployment/docker#readme)
helps to spin up VictoriaMetrics, [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/) and Grafana with one command.


## How to upgrade VictoriaMetrics

VictoriaMetrics is developed at a fast pace, so it is recommended periodically checking [the CHANGELOG page](https://docs.victoriametrics.com/victoriametrics/changelog/) and performing regular upgrades.

It is safe upgrading VictoriaMetrics to new versions unless [release notes](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/latest) say otherwise.
It is safe skipping multiple versions during the upgrade unless [release notes](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/latest) say otherwise.
It is recommended performing regular upgrades to the latest version, since it may contain important bug fixes, performance optimizations or new features.

It is also safe downgrading to older versions unless [release notes](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/latest) say otherwise.

The following steps must be performed during the upgrade / downgrade procedure:

* Send `SIGINT` signal to VictoriaMetrics process in order to gracefully stop it. See [how to send signals to processes](https://stackoverflow.com/questions/33239959/send-signal-to-process-from-command-line).
* Wait until the process stops. This can take a few seconds.
* Start the upgraded VictoriaMetrics.

Prometheus doesn't drop data during VictoriaMetrics restart. See [this article](https://grafana.com/blog/whats-new-in-prometheus-2-8-wal-based-remote-write/) for details. The same applies also to [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/).

> If you'd prefer not to manage upgrades yourself, [VictoriaMetrics Cloud](https://console.victoriametrics.cloud/signUp?utm_source=website&utm_campaign=docs_vm_single_upgrade)
> performs version upgrades automatically during maintenance windows with no action required on your part.
> See the [VictoriaMetrics Cloud documentation](https://docs.victoriametrics.com/victoriametrics-cloud/) to get started.
