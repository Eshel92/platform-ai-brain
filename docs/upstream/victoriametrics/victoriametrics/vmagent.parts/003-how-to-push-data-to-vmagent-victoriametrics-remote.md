<!-- Part 3 of 8 of victoriametrics/vmagent.md (split because the page is big). -->

## How to push data to vmagent

`vmagent` supports [the same set of push-based data ingestion protocols as VictoriaMetrics does](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#how-to-import-time-series-data)
in addition to the pull-based Prometheus-compatible targets' scraping:

* Datadog "submit metrics" API. See [these docs](https://docs.victoriametrics.com/victoriametrics/integrations/datadog/).
* InfluxDB line protocol via `http://<vmagent>:8429/write`. See [these docs](https://docs.victoriametrics.com/victoriametrics/integrations/influxdb/).
* Graphite plaintext protocol if the `-graphiteListenAddr` command-line flag is set. See [these docs](https://docs.victoriametrics.com/victoriametrics/integrations/graphite/#ingesting).
* OpenTelemetry HTTP API via `http://<vmagent>:8429/opentelemetry/v1/metrics`. See [these docs](https://docs.victoriametrics.com/victoriametrics/integrations/opentelemetry/).
* New Relic API. See [these docs](https://docs.victoriametrics.com/victoriametrics/integrations/newrelic/#sending-data-from-agent).
* OpenTSDB telnet and http protocols if `-opentsdbListenAddr` command-line flag is set. See [these docs](https://docs.victoriametrics.com/victoriametrics/integrations/opentsdb/).
* Zabbix Connector streaming protocol. See [these docs](https://docs.victoriametrics.com/victoriametrics/integrations/zabbixconnector/#send-data-from-zabbix-connector).
* Prometheus remote write protocol via `http://<vmagent>:8429/api/v1/write`.
* JSON lines import protocol via `http://<vmagent>:8429/api/v1/import`. See [these docs](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#how-to-import-data-in-json-line-format).
* Native data import protocol via `http://<vmagent>:8429/api/v1/import/native`. See [these docs](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#how-to-import-data-in-native-format).
* Prometheus exposition format via `http://<vmagent>:8429/api/v1/import/prometheus`. See [these docs](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#how-to-import-data-in-prometheus-exposition-format) for details.
* Arbitrary CSV data via `http://<vmagent>:8429/api/v1/import/csv`. See [these docs](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#how-to-import-csv-data).

See how `vmagent` [handles concurrency, decompression, and stream parsing](https://victoriametrics.com/blog/vmagent-how-it-works/#step-1-receiving-data-via-api-or-scrape) during ingestion.


## How to collect metrics in Prometheus format

Specify the path to the `prometheus.yml` file via the `-promscrape.config` command-line flag. `vmagent` takes into account the following
sections from [Prometheus config file](https://prometheus.io/docs/prometheus/latest/configuration/configuration/):

* `global`
* `scrape_configs`

All other sections are ignored, including the [remote_write](https://prometheus.io/docs/prometheus/latest/configuration/configuration/#remote_write) section.
Use the `-remoteWrite.*` command-line flag instead for configuring remote write settings. See [the list of unsupported config sections](#unsupported-prometheus-config-sections).

The file pointed to by `-promscrape.config` may contain `%{ENV_VAR}` placeholders that are substituted by the corresponding `ENV_VAR` environment variable values.

See also:

* [scrape config examples](https://docs.victoriametrics.com/victoriametrics/scrape_config_examples/)
* [the list of supported service discovery types for Prometheus scrape targets](https://docs.victoriametrics.com/victoriametrics/sd_configs/).

### scrape_config enhancements

`vmagent` supports the following additional options in [scrape_configs](https://docs.victoriametrics.com/victoriametrics/sd_configs/#scrape_configs) section:

* `headers` - a list of HTTP headers to send to a scrape target with each scrape request. This can be used when the scrape target
  needs custom authorization and authentication. For example:

```yaml
scrape_configs:
- job_name: custom_headers
  headers:
  - "TenantID: abc"
  - "My-Auth: TopSecret"
```

* `disable_compression: true` for disabling response compression on a per-job basis. By default, `vmagent` requests compressed responses
  from scrape targets to save network bandwidth.
* `disable_keepalive: true` for disabling [HTTP keep-alive connections](https://en.wikipedia.org/wiki/HTTP_persistent_connection)
  on a per-job basis. By default, vmagent uses keep-alive connections when scraping targets. This reduces overhead by eliminating the need to repeatedly reestablish connections.
* `series_limit: N` for limiting the number of unique time series a single scrape target can expose. See [these docs](#cardinality-limiter).
* `stream_parse: true` for scraping targets in a streaming manner. This may be useful when targets export a large number of metrics. See [these docs](#stream-parsing-mode).
* `scrape_align_interval: duration` for aligning scrapes to the given interval instead of using a random offset
  in the range `[0 ... scrape_interval]` for scraping each target. The random offset helps to spread scrapes evenly in time.
* `scrape_offset: duration` for specifying the exact offset for scraping instead of using a random offset in the range `[0 ... scrape_interval]`.

See [scrape_configs docs](https://docs.victoriametrics.com/victoriametrics/sd_configs/#scrape_configs) for more details on all the supported options.

### Loading scrape configs from multiple files

`vmagent` supports loading [scrape configs](https://docs.victoriametrics.com/victoriametrics/sd_configs/#scrape_configs) from multiple files specified
in the `scrape_config_files` section of the `-promscrape.config` file. For example, the following `-promscrape.config` instructs `vmagent`
to load scrape configs from all the `*.yml` files under the `configs` directory, from the local file `single_scrape_config.yml`
and from the URL `https://config-server/scrape_config.yml`:

```yaml
scrape_config_files:
- configs/*.yml
- single_scrape_config.yml
- https://config-server/scrape_config.yml
```

Every referred file can contain an arbitrary number of [supported scrape configs](https://docs.victoriametrics.com/victoriametrics/sd_configs/#scrape_configs).
There is no need to specify a top-level `scrape_configs` section in these files. For example:

```yaml
- job_name: foo
  static_configs:
  - targets: ["vmagent:8429"]
- job_name: bar
  kubernetes_sd_configs:
  - role: pod
```

`vmagent` can dynamically reload these files, see [these docs](#configuration-update).

### Unsupported Prometheus config sections

`vmagent` doesn't support the following sections in the Prometheus config file passed with the `-promscrape.config` command-line flag:

* [remote_write](https://prometheus.io/docs/prometheus/latest/configuration/configuration/#remote_write). This section is substituted
  with various `-remoteWrite*` command-line flags. See [the full list of flags](#advanced-usage). The `remote_write` section isn't supported
  in order to reduce possible confusion when `vmagent` is used for accepting incoming metrics via [supported push protocols](#how-to-push-data-to-vmagent).
  In this case, the `-promscrape.config` file isn't needed.
* `remote_read`. This section isn't supported at all, since `vmagent` doesn't provide the Prometheus querying API.
  Use the querying API on your `-remoteWrite.url` target instead, such as VictoriaMetrics.
  See [Prometheus querying API docs for VictoriaMetrics](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#prometheus-querying-api-usage).
* `rule_files` and `alerting`. These sections are supported by [vmalert](https://docs.victoriametrics.com/victoriametrics/vmalert/).

The list of supported service discovery types is available in [how-to-collect-metrics-in-prometheus-format](#how-to-collect-metrics-in-prometheus-format).

Additionally, `vmagent` doesn't support the `refresh_interval` option in the service discovery sections.
This option is replaced by the `-promscrape.*CheckInterval` command-line flags, which are specific to each service discovery type.
See [the full list of command-line flags for vmagent](#advanced-usage).


## Configuration update

`vmagent` should be restarted in order to update config options set via command-line arguments.
`vmagent` supports multiple approaches for reloading configs from updated config files, such as
`-promscrape.config`, `-remoteWrite.relabelConfig`, `-remoteWrite.urlRelabelConfig`, `-streamAggr.config`
and `-remoteWrite.streamAggr.config`:

* Sending `SIGHUP` signal to `vmagent` process:

  ```sh
  kill -SIGHUP `pidof vmagent`
  ```

* Sending HTTP request to `http://vmagent:8429/-/reload` endpoint. This endpoint can be protected with the `-reloadAuthKey` command-line flag.

There is also the `-promscrape.configCheckInterval` command-line flag, which can be used to automatically reload configs from the updated `-promscrape.config` file.


## DNS URLs

If `vmagent` encounters URLs with the `dns+` prefix in the hostname (such as `http://dns+some-addr:8428/some/path`), it resolves `some-addr` into IP addresses
via [DNS A records](https://datatracker.ietf.org/doc/html/rfc1035#section-3.4.1). The port from the original URL is appended to each discovered IP address.
Each discovered IP address is used for least-loaded balancing of write requests.

DNS URLs are supported in the following places:

* In `-remoteWrite.url` command-line flag. For example, if `victoria-metrics` [DNS A Record](https://datatracker.ietf.org/doc/html/rfc1035#section-3.4.1) record contains
  `192.168.1.15` IP address, then `-remoteWrite.url=http://dns+victoria-metrics:8428/api/v1/write` is automatically resolved into
  `-remoteWrite.url=http://192.168.1.15:8428/api/v1/write`.

DNS URLs are useful when client-side HTTP load balancing is needed. A good example
is a [Kubernetes headless Service](https://kubernetes.io/docs/concepts/services-networking/service/#headless-services),
which returns multiple IP addresses for a single hostname.

### DNS URLs and HTTPS

When a `dns+` URL uses the `https` scheme, `vmagent` connects to the discovered
IP addresses directly. This affects [TLS](https://en.wikipedia.org/wiki/Transport_Layer_Security)
in two ways:

* No [SNI](https://en.wikipedia.org/wiki/Server_Name_Indication) is sent in the TLS handshake,
  since the connection target is an IP address rather than a hostname.
* The server certificate is verified against the IP address, so the verification fails
  unless the certificate contains the corresponding
  [IP SAN](https://en.wikipedia.org/wiki/Subject_Alternative_Name) entries.

To use `dns+` URLs with HTTPS, pass the original hostname via the `-remoteWrite.tlsServerName`
command-line flag. It is used both as SNI and as the name the server certificate
is verified against:

```sh
-remoteWrite.url=https://dns+victoria-metrics:8428/api/v1/write
-remoteWrite.tlsServerName=victoria-metrics
```


## SRV URLs

If `vmagent` encounters URLs with `srv+` prefix in hostname (such as `http://srv+some-addr/some/path`), then it resolves `some-addr` [DNS SRV](https://en.wikipedia.org/wiki/SRV_record)
record into TCP address with hostname and TCP port, and then use the resulting URL when it needs to connect to it.

SRV URLs are supported in the following places:

* In `-remoteWrite.url` command-line flag. For example, if `victoria-metrics` [DNS SRV](https://en.wikipedia.org/wiki/SRV_record) record contains
  `victoria-metrics-host:8428` TCP address, then `-remoteWrite.url=http://srv+victoria-metrics/api/v1/write` is automatically resolved into
  `-remoteWrite.url=http://victoria-metrics-host:8428/api/v1/write`. If the DNS SRV record is resolved into multiple TCP addresses, then `vmagent`
   performs per request least-loaded load-balancing.

* In scrape target addresses aka `__address__` label. See [these docs](https://docs.victoriametrics.com/victoriametrics/relabeling/#how-to-modify-scrape-urls-in-targets) for details.

* In URLs used for [service discovery](https://docs.victoriametrics.com/victoriametrics/sd_configs/).

SRV URLs are useful when HTTP services run on different TCP ports or when their TCP ports can change over time (for instance, after a restart).


## VictoriaMetrics remote write protocol

`vmagent` supports sending data to the configured `-remoteWrite.url` either via the Prometheus or VictoriaMetrics remote write protocols.

When comparing the remote protocols between VictoriaMetrics and Prometheus, VictoriaMetrics provides the following benefits:

* Reduced network bandwidth usage by 2x-5x. This allows saving network bandwidth usage costs when `vmagent` and
  the configured remote storage systems are located in different datacenters, availability zones, or regions.

* Reduced disk read/write IO and disk space usage at `vmagent` when the remote storage is temporarily unavailable.
  In this case, `vmagent` buffers incoming data to disk using the VictoriaMetrics remote write format.
  This reduces disk read/write IO and disk space usage by 2x-5x compared to the Prometheus remote write format.

> See blogpost [Save network costs with VictoriaMetrics remote write protocol](https://victoriametrics.com/blog/victoriametrics-remote-write/).

`vmagent` uses VictoriaMetrics remote write protocol by default {{% available_from "v1.116.0" %}} when it sends data to VictoriaMetrics components such as other `vmagent` instances,
[single-node VictoriaMetrics](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/)
, `vminsert` at [cluster version](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/) or `vmstorage` at [cluster version](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/) (See [Remote write directly to vmstorage](https://docs.victoriametrics.com/victoriametrics/data-ingestion/vmagent/#remote-write-directly-to-vmstorage)). If needed, it can automatically downgrade to a Prometheus protocol at runtime.
It is possible to force switch to VictoriaMetrics remote write protocol by specifying `-remoteWrite.forceVMProto`
command-line flag for the corresponding `-remoteWrite.url`.
It is possible to tune the compression level for VictoriaMetrics remote write protocol with the `-remoteWrite.vmProtoCompressLevel` command-line flag.
Bigger values reduce network usage at the cost of higher CPU usage. Negative values reduce CPU usage but increase network usage.
The default value for the compression level is `0`, the minimum value is `-22`, and the maximum value is `22`. The default value works optimally
in most cases, so it isn't recommended to change it.

`vmagent` automatically switches to the Prometheus remote write protocol when it sends data to old versions of VictoriaMetrics components
or to other Prometheus-compatible remote storage systems. It is possible to force switch to Prometheus remote write protocol
by specifying `-remoteWrite.forcePromProto` command-line flag for the corresponding `-remoteWrite.url`.
