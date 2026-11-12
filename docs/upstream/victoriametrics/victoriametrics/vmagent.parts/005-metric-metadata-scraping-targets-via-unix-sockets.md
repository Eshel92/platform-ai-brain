<!-- Part 5 of 8 of victoriametrics/vmagent.md (split because the page is big). -->

## Metric metadata

`vmagent` accepts{{% available_from "v1.137.0" %}} metric metadata exposed by scrape targets in [Prometheus exposition format](https://github.com/prometheus/docs/blob/main/docs/instrumenting/exposition_formats.md), received via [Prometheus remote write v1](https://prometheus.io/docs/specs/prw/remote_write_spec/) or [OpenTelemetry protocol](https://github.com/open-telemetry/opentelemetry-proto/blob/v1.7.0/opentelemetry/proto/metrics/v1/metrics.proto) by default. Set `-enableMetadata=false` to disable metadata processing{{% available_from "v1.125.1" %}}.
During processing, metadata won't be dropped or modified by [relabeling](https://docs.victoriametrics.com/victoriametrics/relabeling/) or [streaming aggregation](https://docs.victoriametrics.com/victoriametrics/stream-aggregation/).

When `-enableMultitenantHandlers` is enabled, vmagent adds tenant info to metadata specified in [multitenant endpoint](https://docs.victoriametrics.com/victoriametrics/vmagent/#multitenancy) (`/insert/<accountID>/<suffix>`).
However, if the `/insert/multitenant/<suffix>` endpoint is used, vmagent preserves the tenant information provided in the metadata by the sender. If the sender does not specify tenant information, the default tenant `0:0` is used.

> Metadata requires extra memory, disk space, and network traffic.

Use `-remoteWrite.disableMetadata`{{% available_from "v1.140.0" %}} to fully disable sending metadata from vmagent.
This reduces network traffic and resource usage when metadata is not required.

Metadata sending is always disabled for `-remoteWrite.url` destinations with [MDX](https://docs.victoriametrics.com/victoriametrics/vmagent/#monitoring-data-exchange) enabled,
even when the corresponding `-remoteWrite.disableMetadata=false` value is set explicitly.


## Stream parsing mode

By default, `vmagent` parses the full response from the scrape target, applies [relabeling](https://docs.victoriametrics.com/victoriametrics/relabeling/)
and then pushes the resulting metrics to the configured `-remoteWrite.url` in one go. This mode works great for the majority of cases
when the scrape target exposes a small number of metrics (e.g., less than 10K). But this mode may take large amounts of memory
when the scrape target exposes a large number of metrics (for example, when `vmagent` scrapes [`kube-state-metrics`](https://github.com/kubernetes/kube-state-metrics)
in a large Kubernetes cluster. It is recommended to enable stream parsing for such targets.
When stream parsing is enabled, `vmagent` processes the response from the scrape target in chunks.
This saves memory when scraping targets that expose millions of metrics.

Stream parsing is automatically enabled for scrape targets returning response bodies with sizes larger than
the `-promscrape.minResponseSizeForStreamParse` command-line flag value. Additionally,
stream parsing can be explicitly enabled in the following places:

* Via `-promscrape.streamParse` command-line flag. In this case, all the scrape targets defined
  in the file pointed by `-promscrape.config` are scraped in stream parsing mode.
* Via `stream_parse: true` option at `scrape_configs` section. In this case, all the scrape targets defined
  in this section are scraped in stream parsing mode.
* Via `__stream_parse__=true` label, which can be set via [relabeling](https://docs.victoriametrics.com/victoriametrics/relabeling/) at `relabel_configs` section.
  In this case, stream parsing mode is enabled for the corresponding scrape targets.
  Typical use case: to set the label via [Kubernetes annotations](https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/)
  for targets exposing a large number of metrics.

Examples:

```yaml
scrape_configs:
- job_name: 'big-federate'
  stream_parse: true
  static_configs:
  - targets:
    - big-prometheus1
    - big-prometheus2
  honor_labels: true
  metrics_path: /federate
  params:
    'match[]': ['{__name__!=""}']
```

Note that `vmagent` in stream parsing mode stores up to `sample_limit` samples to the configured `-remoteStorage.url`
instead of dropping all the samples read from the target, because the parsed data is sent to the remote storage
as soon as it is parsed in stream parsing mode.


## Scraping big number of targets

A single `vmagent` instance can scrape tens of thousands of scrape targets. Sometimes this isn't enough due to limitations on CPU, network, RAM, etc.
In this case, scrape targets can be split among multiple `vmagent` instances (aka `vmagent` horizontal scaling, sharding, and clustering).
The number of `vmagent` instances in the cluster must be passed to the `-promscrape.cluster.membersCount` command-line flag.
Each `vmagent` instance in the cluster must use identical `-promscrape.config` files with distinct `-promscrape.cluster.memberNum` values
in the range `0 ... N-1`, where `N` is the number of `vmagent` instances in the cluster specified via `-promscrape.cluster.membersCount`.
For example, the following commands spread scrape targets among a cluster of two `vmagent` instances:

```sh
/path/to/vmagent -promscrape.cluster.membersCount=2 -promscrape.cluster.memberNum=0 -promscrape.config=/path/to/config.yml ...
/path/to/vmagent -promscrape.cluster.membersCount=2 -promscrape.cluster.memberNum=1 -promscrape.config=/path/to/config.yml ...
```

The `-promscrape.cluster.memberNum` can be set to a StatefulSet pod name when `vmagent` runs in Kubernetes.
The pod name must end with a number in the range `0 ... promscrape.cluster.membersCount-1`. For example, `-promscrape.cluster.memberNum=vmagent-0`.

By default, targets are sharded among `vmagent` instances by all target labels after relabeling.
Use `-promscrape.cluster.shardByLabels` {{% available_from "v1.146.0" %}} to shard targets by specified labels instead.
For example, with `-promscrape.cluster.shardByLabels=service`, the targets with the same `service` label value will be scraped by the same `vmagent` instance, 
which is useful when perform stream aggregation that requires all metrics with the same `service` label value to be processed on the same `vmagent` instance. 
If none of the specified labels are present in the target labels, then all target labels will be used for sharding.

By default, each scrape target is scraped only by a single `vmagent` instance in the cluster. If there is a need for replicating scrape targets among multiple `vmagent` instances,
then `-promscrape.cluster.replicationFactor` command-line flag must be set to the desired number of replicas. For example, the following commands
start a cluster of three `vmagent` instances, where two `vmagent` instances scrape each target:

```sh
/path/to/vmagent -promscrape.cluster.membersCount=3 -promscrape.cluster.replicationFactor=2 -promscrape.cluster.memberNum=0 -promscrape.config=/path/to/config.yml ...
/path/to/vmagent -promscrape.cluster.membersCount=3 -promscrape.cluster.replicationFactor=2 -promscrape.cluster.memberNum=1 -promscrape.config=/path/to/config.yml ...
/path/to/vmagent -promscrape.cluster.membersCount=3 -promscrape.cluster.replicationFactor=2 -promscrape.cluster.memberNum=2 -promscrape.config=/path/to/config.yml ...
```

Every `vmagent` in the cluster exposes all the discovered targets in the `http://vmagent:8429/service-discovery` page.
Each discovered target on this page contains its status (`UP`, `DOWN`, or `DROPPED` with the reason why the target has been dropped).
If the target is dropped because of sharding to other `vmagent` instances in the cluster, then the status column contains
`-promscrape.cluster.memberNum` values for `vmagent` instances where the given target is scraped.

The `/service-discovery` page provides links to the corresponding `vmagent` instances if the `-promscrape.cluster.memberURLTemplate` command-line flag is set.
Every occurrence of `%d` inside the `-promscrape.cluster.memberURLTemplate` is substituted with the `-promscrape.cluster.memberNum`
for the corresponding `vmagent` instance. For example, `-promscrape.cluster.memberURLTemplate='http://vmagent-instance-%d:8429/targets'`
generates `http://vmagent-instance-42:8429/targets` URL for `vmagent` instance, which runs with `-promscrape.cluster.memberNum=42`.

Note that `vmagent` shows up to `-promscrape.maxDroppedTargets` dropped targets on the `/service-discovery` page.
Increase the `-promscrape.maxDroppedTargets` command-line flag value if the `/service-discovery` page misses some dropped targets.

If multiple `vmagent` instances scrape the same target, data deduplication must be enabled for the remote storage specified by `-remoteWrite.url`.
The `-dedup.minScrapeInterval` must be set to the `scrape_interval` configured at `-promscrape.config`.
See [these docs](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#deduplication) for details.

The `-promscrape.cluster.memberLabel` command-line flag allows specifying a name for the `member num` label to add to all the scraped metrics.
The value of the `member num` label is set to `-promscrape.cluster.memberNum`. For example, the following config instructs adding `vmagent_instance="0"` label
to all the metrics scraped by the given `vmagent` instance:

```sh
/path/to/vmagent -promscrape.cluster.membersCount=2 -promscrape.cluster.memberNum=0 -promscrape.cluster.memberLabel=vmagent_instance
```

See also [how to shard data among multiple remote storage systems](#sharding-among-remote-storages).


## High availability

It is possible to run multiple **identically configured** `vmagent` instances or `vmagent`
[clusters](#scraping-big-number-of-targets), so they [scrape](#how-to-collect-metrics-in-prometheus-format)
the same set of targets and push the collected data to the same set of VictoriaMetrics remote storage systems.
Two **identically configured** vmagent instances or clusters are usually called an HA pair.

When running HA pairs, [deduplication](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#deduplication) must be configured
on the VictoriaMetrics side to deduplicate received samples.
See [these docs](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#deduplication) for details.

It is also recommended to pass different values to the `-promscrape.cluster.name` command-line flag per `vmagent`
instance or per `vmagent` cluster in a HA setup. This is needed for proper data de-duplication.
See [this issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/2679) for details.


## Scraping targets via a proxy

`vmagent` supports scraping targets via HTTP, HTTPS, and SOCKS5 proxies. Proxy address must be specified in the `proxy_url` option. For example, the following scrape config instructs
target scraping via https proxy at `https://proxy-addr:1234`:

```yaml
scrape_configs:
- job_name: foo
  proxy_url: https://proxy-addr:1234
```

Proxy can be configured with the following optional settings:

* `proxy_authorization` for generic token authorization. See [these docs](https://docs.victoriametrics.com/victoriametrics/sd_configs/#http-api-client-options).
* `proxy_basic_auth` for Basic authorization. See [these docs](https://docs.victoriametrics.com/victoriametrics/sd_configs/#http-api-client-options).
* `proxy_bearer_token` and `proxy_bearer_token_file` for Bearer token authorization
* `proxy_oauth2` for OAuth2 config. See [these docs](https://prometheus.io/docs/prometheus/latest/configuration/configuration/#oauth2).
* `proxy_tls_config` for TLS config. See [these docs](https://prometheus.io/docs/prometheus/latest/configuration/configuration/#tls_config).
* `proxy_headers` for passing additional HTTP headers in requests to the proxy.

For example:

```yaml
scrape_configs:
- job_name: foo
  proxy_url: https://proxy-addr:1234
  proxy_basic_auth:
    username: foobar
    password: secret
  proxy_tls_config:
    insecure_skip_verify: true
    cert_file: /path/to/cert
    key_file: /path/to/key
    ca_file: /path/to/ca
    server_name: real-server-name
  proxy_headers:
  - "Proxy-Auth: top-secret"
```


## Scraping targets via unix sockets

`vmagent` can scrape targets listening on a Unix domain socket. The socket path must be set in the `__unix_socket__` label:

```yaml
scrape_configs:
- job_name: node_exporter
  static_configs:
  - targets: ["node_exporter:9100"]
    labels:
      __unix_socket__: /var/run/node_exporter.sock
```

The connection goes through the socket, while `__address__` is still used for the scrape URL and the `instance` label.
`proxy_url` cannot be used for such targets.
