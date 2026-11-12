<!-- Part 3 of 6 of victoriametrics/vmalert.md (split because the page is big). -->

## Reading rules from object storage

The [Enterprise version](https://docs.victoriametrics.com/victoriametrics/enterprise/) of `vmalert` may read alerting and recording rules
from object storage:

* `./bin/vmalert -rule=s3://bucket/dir/alert.rules` would read rules from the given path at S3 bucket
* `./bin/vmalert -rule=gs://bucket/dir/alert.rules` would read rules from the given path at GCS bucket

S3 and GCS paths support only matching by prefix, e.g. `s3://bucket/dir/rule_` matches
all files with prefix `rule_` in the folder `dir`.

The following [command-line flags](#flags) can be used for fine-tuning access to S3 and GCS:

* `-s3.credsFilePath` - path to file with GCS or S3 credentials. Credentials are loaded from default locations if not set.
* `-s3.configFilePath` - path to file with S3 configs. Configs are loaded from default location if not set.
* `-s3.configProfile` - profile name for S3 configs. If no set, the value of the environment variable will be loaded (`AWS_PROFILE` or `AWS_DEFAULT_PROFILE`).
* `-s3.customEndpoint` - custom S3 endpoint for use with S3-compatible storages (e.g. MinIO). S3 is used if not set.
* `-s3.forcePathStyle` - prefixing endpoint with bucket name when set false, true by default.

### S3 (AWS and S3-compatible)

The following example reads rules from an S3 bucket:

```sh
./bin/vmalert \
  -rule=s3://my-alert-bucket/rules/alerts_ \
  -s3.credsFilePath=/etc/vmalert/aws-credentials \
  -datasource.url=http://vmselect:8481/select/0/prometheus \
  -notifier.url=http://alertmanager:9093 \
  -licenseFile=/etc/vm-license
```

For S3-compatible backends such as [MinIO](https://www.min.io/) or [Ceph](https://ceph.io/), add `-s3.customEndpoint`:

```sh
./bin/vmalert \
  -rule=s3://victoriametrics-alert-rules/rules_ \
  -s3.credsFilePath=/etc/vmalert/aws-credentials \
  -s3.customEndpoint=http://minio.example.local:9000 \
  -datasource.url=http://vmselect:8481/select/0/prometheus \
  -notifier.url=http://alertmanager:9093 \
  -licenseFile=/etc/vm-license
```

See [Connecting VM components to cloud storage](https://docs.victoriametrics.com/guides/connecting-vm-components-to-cloud-storage/) for details on creating IAM users, credentials file format, environment variables, and IAM roles.

### Google Cloud Storage (GCS)

The following example reads rules from a GCS bucket:

```sh
./bin/vmalert \
  -rule=gs://my-alert-bucket/rules/alerts_ \
  -s3.credsFilePath=/etc/vmalert/gcp-service-account.json \
  -datasource.url=http://vmselect:8481/select/0/prometheus \
  -notifier.url=http://alertmanager:9093 \
  -licenseFile=/etc/vm-license
```

See [Connecting VM components to cloud storage](https://docs.victoriametrics.com/guides/connecting-vm-components-to-cloud-storage/) for details on creating service accounts and downloading JSON keys.


## Topology examples

The following sections are showing how `vmalert` may be used and configured
for different scenarios.

Please note, not all flags in examples are required:

* `-remoteWrite.url` and `-remoteRead.url` are optional and are needed only if
  you have recording rules or want to store [alerts state](#alerts-state-on-restarts) on `vmalert` restarts;
* `-notifier.url` is optional and is needed only if you have alerting rules.

### Single-node VictoriaMetrics

The simplest configuration where one single-node VM server is used for
rules execution, storing recording rules results and alerts state.

`vmalert` configuration flags:

```sh
./bin/vmalert -rule=rules.yml  \                    # Path to the file with rules configuration. Supports wildcard
    -datasource.url=http://victoriametrics:8428 \   # VM-single addr for executing rules expressions
    -remoteWrite.url=http://victoriametrics:8428 \  # VM-single addr to persist alerts state and recording rules results
    -remoteRead.url=http://victoriametrics:8428 \   # VM-single addr for restoring alerts state after restart
    -notifier.url=http://alertmanager:9093          # AlertManager addr to send alerts when they trigger
```

![vmalert single](vmalert_single.webp)
{width="500"}

### Cluster VictoriaMetrics

In [cluster mode](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/)
VictoriaMetrics has separate components for writing and reading path:
`vminsert` and `vmselect` components respectively. `vmselect` is used for executing rules expressions
and `vminsert` is used to persist recording rules results and alerts state.
Cluster mode could have multiple `vminsert` and `vmselect` components.

`vmalert` configuration flags:

```sh
./bin/vmalert -rule=rules.yml  \                                # Path to the file with rules configuration. Supports wildcard
    -datasource.url=http://vmselect:8481/select/0/prometheus    # vmselect addr for executing rules expressions
    -remoteWrite.url=http://vminsert:8480/insert/0/prometheus   # vminsert addr to persist alerts state and recording rules results
    -remoteRead.url=http://vmselect:8481/select/0/prometheus    # vmselect addr for restoring alerts state after restart
    -notifier.url=http://alertmanager:9093                      # AlertManager addr to send alerts when they trigger
```

![vmalert cluster](vmalert_cluster.webp)

In case when you want to spread the load on these components - add balancers before them and configure
`vmalert` with balancer addresses. Please, see more about [VictoriaMetrics cluster architecture](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/#architecture-overview).

### HA vmalert

For High Availability(HA) user can run multiple identically configured `vmalert` instances.
It means all of them will execute the same rules, write state and results to
the same destinations, and send alert notifications to multiple configured
Alertmanagers.

`vmalert` configuration flags:

```sh
./bin/vmalert -rule=rules.yml \                   # Path to the file with rules configuration. Supports wildcard
    -datasource.url=http://victoriametrics:8428 \   # VM-single addr for executing rules expressions
    -remoteWrite.url=http://victoriametrics:8428 \  # VM-single addr to persist alerts state and recording rules results
    -remoteRead.url=http://victoriametrics:8428 \   # VM-single addr for restoring alerts state after restart
    -notifier.url=http://alertmanager1:9093 \       # Multiple AlertManager addresses to send alerts when they trigger
    -notifier.url=http://alertmanagerN:9093         # The same alert will be sent to all configured notifiers
```

![vmalert ha](vmalert_ha.webp)

To avoid recording rules results and alerts state duplication in VictoriaMetrics server
don't forget to configure [deduplication](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#deduplication).
Multiple equally configured vmalerts should evaluate rules at the same timestamps, so it is recommended
to set `-dedup.minScrapeInterval` as equal to vmalert's `-evaluationInterval`.

If you have multiple different `interval` params for distinct rule groups, then set `-dedup.minScrapeInterval` to
the biggest `interval` value, or value which will be a multiple for all `interval` values. For example, if you have
two groups with `interval: 10s` and `interval: 15s`, then set `-dedup.minScrapeInterval=30s`. This would consistently
keep only a single data point on 30s time interval for all rules. However, try to avoid having inconsistent `interval`
values.

It is not recommended having `-dedup.minScrapeInterval` smaller than `-evaluationInterval`, as it may produce
results with inconsistent intervals between data points.

Alertmanager will automatically deduplicate alerts with identical labels, so ensure that
all `vmalert`s are having identical config.

Don't forget to configure [cluster mode](https://prometheus.io/docs/alerting/latest/alertmanager/)
for Alertmanagers for better reliability. List all Alertmanager URLs in vmalert `-notifier.url`
to ensure [high availability](https://github.com/prometheus/alertmanager#high-availability).

This example uses single-node VM server for the sake of simplicity.
Check how to replace it with [cluster VictoriaMetrics](#cluster-victoriametrics) if needed.

### Downsampling and aggregation via vmalert

_Please note, [stream aggregation](https://docs.victoriametrics.com/victoriametrics/stream-aggregation/) might be more efficient
for cases when downsampling or aggregation need to be applied **before data gets into the TSDB.**_

`vmalert` can't modify existing data. But it can run arbitrary queries
via [recording rules](#recording-rules) and backfill results to the configured `-remoteWrite.url`.
This ability allows to aggregate data. For example, the following rule will calculate the average value for
metric `http_requests` on the `5m` interval:

```yaml
  - record: http_requests:avg5m
    expr: avg_over_time(http_requests[5m])
```

Every time this rule will be evaluated, `vmalert` will backfill its results as a new time series `http_requests:avg5m`
to the configured `-remoteWrite.url`.

`vmalert` executes rules with specified interval (configured via flag `-evaluationInterval`
or as [group's](#groups) `interval` param). The interval helps to control "resolution" of the produced series.
This ability allows to downsample data. For example, the following config will execute the rule only once every `5m`:

```yaml
groups:
  - name: my_group
    interval: 5m
    rules:
    - record: http_requests:avg5m
      expr: avg_over_time(http_requests[5m])
```

Ability of `vmalert` to be configured with different `-datasource.url` and `-remoteWrite.url` command-line flags
allows reading data from one data source and backfilling results to another. This helps to build a system
for aggregating and downsampling the data.

The following example shows how to build a topology where `vmalert` will process data from one cluster
and write results into another. Such clusters may be called as "hot" (low retention,
high-speed disks, used for operative monitoring) and "cold" (long term retention,
slower/cheaper disks, low resolution data). With help of `vmalert`, user can setup
recording rules to process raw data from "hot" cluster (by applying additional transformations
or reducing resolution) and push results to "cold" cluster.

`vmalert` configuration flags:

```sh
./bin/vmalert -rule=downsampling-rules.yml \                                        # Path to the file with rules configuration. Supports wildcard
    -datasource.url=http://raw-cluster-vmselect:8481/select/0/prometheus            # vmselect addr for executing recording rules expressions
    -remoteWrite.url=http://aggregated-cluster-vminsert:8480/insert/0/prometheus    # vminsert addr to persist recording rules results
```

![vmalert multi cluster](vmalert_multicluster.webp)

Please note, [replay](#rules-backfilling) feature may be used for transforming historical data.

Flags `-remoteRead.url` and `-notifier.url` are omitted since we assume only recording rules are used.

See also [stream aggregation](https://docs.victoriametrics.com/victoriametrics/stream-aggregation/) and [downsampling](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#downsampling).

### Multiple remote writes

For persisting recording or alerting rule results `vmalert` requires `-remoteWrite.url` to be set.
But this flag supports only one destination. To persist rule results to multiple destinations
we recommend using [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/) as fan-out proxy:

![vmalert multiple remote write destinations](vmalert_multiple_rw.webp)

In this topology, `vmalert` is configured to persist rule results to `vmagent`. And `vmagent`
is configured to fan-out received data to two or more destinations.
Using `vmagent` as a proxy provides additional benefits such as
[data persisting when storage is unreachable](https://docs.victoriametrics.com/victoriametrics/vmagent/#replication-and-high-availability),
or time series modification via [relabeling](https://docs.victoriametrics.com/victoriametrics/relabeling/).


## Integrations

vmalert can be integrated with different data sources for alerting and recording rules. But it deliberately allows
configuring only one `datasource.url`. We recommend running separate instances of vmalert for each datasource type
with the specified `-rule.defaultRuleType=<datasource_type>` command-line flag.

###### VictoriaMetrics

vmalert natively integrates with [VictoriaMetrics](https://docs.victoriametrics.com/victoriametrics/) for alerting and
recording rules.

###### VictoriaLogs

vmalert integrates with [VictoriaLogs](https://docs.victoriametrics.com/victorialogs/) and allows configuring alerting and recording rules using [LogsQL](https://docs.victoriametrics.com/victorialogs/logsql/).
Results of recording rules and alerting state should be persisted to the remote-write compatible storage, such as VictoriaMetrics.
To enable VictoriaLogs compatibility set the `-rule.defaultRuleType=vlogs` command-line flag.

See [this doc](https://docs.victoriametrics.com/victorialogs/vmalert/) for details.

###### VictoriaTraces

vmalert integrates with [VictoriaTraces](https://docs.victoriametrics.com/victoriatraces/) in exactly the same way as
with [VictoriaLogs](https://docs.victoriametrics.com/victoriametrics/vmalert/#victorialogs).

###### Graphite

vmalert integrates with [Graphite Render API](https://graphite.readthedocs.io/en/stable/render_api.html) and allows configuring alerting and recording rules.
During evaluation, vmalert will send requests to `<-datasource.url>/render?format=json`.
To enable Graphite compatibility set the `-rule.defaultRuleType=graphite` command-line flag.

Since VictoriaMetrics supports both Graphite and Prometheus APIs, it is possible to mix Graphite and VictoriaMetrics rules.
On the group level, set the `type` field to specify to which datasource type it should belong: `prometheus` (MetricsQL) or `graphite` (GraphiteQL).
When using vmalert with both `graphite` and `prometheus` rules configured against the cluster version of VictoriaMetrics, don't forget
to set the `-datasource.appendTypePrefix` flag to `true`, so vmalert can adjust URL prefix automatically based on the query type.

###### Prometheus

vmalert uses [Prometheus HTTP API](https://prometheus.io/docs/prometheus/latest/querying/api/) for querying
and [Prometheus Remote Write v1 protocol](https://prometheus.io/docs/specs/prw/remote_write_spec/) for persisting
recording rules results and alerting state. Hence, it can be integrated with any Prometheus-compatible storage
that supports these protocols.

###### Grafana

To proxy requests from [Grafana Alerting UI](https://grafana.com/docs/grafana/latest/alerting/) configure `-vmalert.proxyURL`
on VictoriaMetrics [single-node](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#vmalert)
or [vmselect in cluster version](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/#vmalert).

###### vmui

To access rules UI through [vmui](https://docs.victoriametrics.com/victoriametrics/#vmui) configure `-vmalert.proxyURL`
on VictoriaMetrics [single-node](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#vmalert)
or [vmselect in cluster version](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/#vmalert).

###### vmanomaly

See how to integrate vmalert with [VictoriaMetrics Anomaly Detection](https://docs.victoriametrics.com/anomaly-detection/)
in the following [guide](https://docs.victoriametrics.com/anomaly-detection/guides/guide-vmanomaly-vmalert/).

###### VictoriaMetrics Cloud

For users of [VictoriaMetrics Cloud](https://console.victoriametrics.cloud/signUp?utm_source=website&utm_campaign=docs_vm_vmalert_config),
many of the configuration steps (including highly available setup of `vmalert` for cluster deployments) are handled automatically.
Please refer to the [VictoriaMetrics Cloud documentation](https://docs.victoriametrics.com/victoriametrics-cloud/alertmanager-setup-for-deployment/) for more details.


## Web

`vmalert` runs a web-server (`-httpListenAddr`) for serving metrics and alerts endpoints:

* `http://<vmalert-addr>` - UI;
* `http://<vmalert-addr>/api/v1/rules` - returns a list of all loaded groups and rules. Supports the `datasource_type`, `search`, `group_limit`, and `page_num` parameters, as well as additional [filtering](https://prometheus.io/docs/prometheus/latest/querying/api/#rules);
* `http://<vmalert-addr>/api/v1/alerts` - returns a list of all active alerts. Supports the `datasource_type`, `rule_group[]`, `file[]` and `match[]`(applied on templated alert labels) query parameters;
* `http://<vmalert-addr>/api/v1/notifiers` - returns a list of all available notifiers;
* `http://<vmalert-addr>/vmalert/api/v1/alert?group_id=<group_id>&alert_id=<alert_id>` - returns the alert status in JSON format;
* `http://<vmalert-addr>/vmalert/api/v1/rule?group_id=<group_id>&rule_id=<rule_id>` - returns the rule status in JSON format;
* `http://<vmalert-addr>/vmalert/api/v1/group?group_id=<group_id>` - returns the group status in JSON format. Used as the alert source in AlertManager;
* `http://<vmalert-addr>/vmalert/alert?group_id=<group_id>&alert_id=<alert_id>` - displays the alert status in the web UI;
* `http://<vmalert-addr>/vmalert/rule?group_id=<group_id>&rule_id=<rule_id>` - displays the rule status in the web UI;
* `http://<vmalert-addr>/metrics` - application metrics endpoint;
* `http://<vmalert-addr>/-/reload` - hot configuration reload.

`vmalert` web UI can be accessed from [single-node version of VictoriaMetrics](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/)
and from [cluster version of VictoriaMetrics](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/).
This may be used for better integration with Grafana unified alerting system. See the following docs for details:

* [How to query vmalert from single-node VictoriaMetrics](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#vmalert)
* [How to query vmalert from VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/#vmalert)
