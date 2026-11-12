<!-- Part 7 of 8 of victoriametrics/Cluster-VictoriaMetrics.md (split because the page is big). -->

## Deduplication

Cluster version of VictoriaMetrics supports data deduplication in the same way as single-node version do.
See [these docs](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#deduplication) for details. The only difference is that
deduplication can't be guaranteed when samples and sample duplicates for the same time series end up on different
`vmstorage` nodes. This could happen in the following scenarios:

- when adding/removing `vmstorage` nodes a new samples for time series will be re-routed to another `vmstorage` nodes;
- when `vmstorage` nodes are temporarily unavailable (for instance, during their restart). Then new samples are re-routed to the remaining available `vmstorage` nodes;
- when `vmstorage` node has no enough capacity for processing incoming data stream. Then `vminsert` re-routes new samples to other `vmstorage` nodes.

It is recommended to set **the same** `-dedup.minScrapeInterval` command-line flag value to both `vmselect` and `vmstorage` nodes
to ensure query results consistency, even if [storage layer didn't complete deduplication](https://victoriametrics.com/blog/vmstorage-retention-merging-deduplication/#deduplication) yet.


## Metrics Metadata

Cluster version of VictoriaMetrics can store metric metadata (TYPE, HELP, UNIT) {{% available_from "v1.130.0" %}}.
Metadata ingestion is enabled by default{{% available_from "v1.137.0" %}}. To disable it, set `-enableMetadata=false` on `vminsert`, and `vmagent`.

The metadata is cached in-memory in a ring buffer and can use up to 1% of available memory by default (see `-storage.maxMetadataStorageSize` cmd-line flag).
When in-memory size is exceeded, the least updated entries are dropped first. Entries that weren't updated for 1h are cleaned up automatically.

> The following expression helps to understand if metadata cache capacity is utilized for more than 90%: `vm_metrics_metadata_storage_size_bytes / vm_metrics_metadata_storage_max_size_bytes > 0.9`.
Setup [monitoring](https://docs.victoriametrics.com/victoriametrics/quick-start/#monitoring) and recommended alerting rules
to get notified about cache capacity issues.

Metadata is ingested independently from metrics, so a metric can exist without metadata, and vice versa.
Metadata is expected to be ephemeral and constantly updated on ingestion. For this reason, metadata cache isn't
persisted during storage restarts.

Metadata supports [multitenancy](#multitenancy) and can be queried via the `/select/<accountID>/prometheus/api/v1/metadata` endpoint, which provides a response compatible with the Prometheus [metadata API](https://prometheus.io/docs/prometheus/latest/querying/api/#querying-metric-metadata).
If multiple vmstorage nodes return metadata for the same metric family name, or if multiple tenants have metadata for the same metric family name, vmselect returns only the first matching result.
Duplicate metadata entries are not merged or deduplicated across storages or tenants. See [/api/v1/metadata](https://docs.victoriametrics.com/victoriametrics/url-examples/#apiv1metadata) example.


## Retention filters

[VictoriaMetrics Enterprise](https://docs.victoriametrics.com/victoriametrics/enterprise/) supports configuring multiple retentions for distinct sets of time series
by passing `-retentionFilter` command-line flag to `vmstorage` nodes. See [these docs](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#retention-filters) for details on this feature.

Additionally, enterprise version of VictoriaMetrics cluster supports multiple retentions for distinct sets of [tenants](#multitenancy)
by specifying filters on `vm_account_id` and/or `vm_project_id` pseudo-labels in `-retentionFilter` command-line flag.
If the tenant doesn't match specified `-retentionFilter` options, then the global `-retentionPeriod` is used for it.

For example, the following config sets retention to 1 day for [tenants](#multitenancy) with `accountID` starting from `42`,
then sets retention to 3 days for time series with label `env="dev"` or `env="prod"` from any tenant,
while the rest of tenants will have 4 weeks retention:

```bash
-retentionFilter='{vm_account_id=~"42.*"}:1d' -retentionFilter='{env=~"dev|staging"}:3d' -retentionPeriod=4w
```

It is OK to mix filters on real labels with filters on `vm_account_id` and `vm_project_id` pseudo-labels.
For example, the following config sets retention to 5 days for time series with `env="dev"` label from [tenant](#multitenancy) `accountID=5`:

```bash
-retentionFilter='{vm_account_id="5",env="dev"}:5d'
```

See also [downsampling](#downsampling).

Enterprise binaries can be downloaded and evaluated for free from [the releases page](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/latest).
See how to request a free [trial license](https://victoriametrics.com/products/enterprise/trial/).


## Downsampling

[VictoriaMetrics Enterprise](https://docs.victoriametrics.com/victoriametrics/enterprise/) supports configuring downsampling rules for different time series sets by passing `-downsampling.period` command-line flag to `vmstorage` and `vmselect` nodes. See [these docs](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#downsampling) for details.

It is possible to downsample series, which belong to a particular [tenant](#multitenancy) by using [filters](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#filtering)
on `vm_account_id` or `vm_project_id` pseudo-labels in `-downsampling.period` command-line flag. For example, the following config leaves the last sample per each minute for samples
older than one hour only for [tenants](#multitenancy) with accountID equal to 12 and 42, while series for other tenants are dropped:

```bash
-downsampling.period='{vm_account_id=~"12|42"}:1h:1m'
```

It is OK to mix filters on real labels with filters on `vm_account_id` and `vm_project_id` pseudo-labels.
For example, the following config instructs leaving the last sample per hour after 30 days for time series with `env="dev"` label from [tenant](#multitenancy) `accountID=5`:

```bash
-downsampling.period='{vm_account_id="5",env="dev"}:30d:1h'
```

The same flag value must be passed to both `vmstorage` and `vmselect` nodes. Configuring `vmselect` node with `-downsampling.period`
command-line flag makes query results more consistent, because `vmselect` uses the maximum configured downsampling interval
on the requested time range if this time range covers multiple downsampling levels.
For example, if `-downsampling.period=30d:5m` and the query requests the last 60 days of data, then `vmselect`
downsamples all the [raw samples](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#raw-samples) on the requested time range
using 5 minute interval. If `-downsampling.period` command-line flag isn't set at `vmselect`,
then query results can be less consistent because of mixing raw and downsampled data.

See also [retention filters](#retention-filters).

Enterprise binaries can be downloaded and evaluated for free from [the releases page](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/latest).
See how to request a free [trial license](https://victoriametrics.com/products/enterprise/trial/).


## vmui

VictoriaMetrics cluster version provides UI for query troubleshooting and exploration. The UI is available at
`http://<vmselect>:8481/select/<accountID>/vmui/` in each `vmselect` service.
The UI allows exploring query results via graphs and tables. See more details about [vmui](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#vmui).


## vmalert

vmselect is capable of proxying requests to [vmalert](https://docs.victoriametrics.com/victoriametrics/vmalert/)
when `-vmalert.proxyURL` flag is set. Use this feature for the following cases:

- for proxying requests from [Grafana Alerting UI](https://grafana.com/docs/grafana/latest/alerting/);
- for accessing vmalert UI through vmselect Web interface.

For accessing vmalerts UI through vmselect configure `-vmalert.proxyURL` flag and visit
`http://<vmselect>:8481/select/<accountID>/prometheus/vmalert/` link.


## Security

General security recommendations:

- All the VictoriaMetrics cluster components must run in protected private network without direct access from untrusted networks such as Internet.
- External clients must access `vminsert` and `vmselect` via auth proxy such as [vmauth](https://docs.victoriametrics.com/victoriametrics/vmauth/)
  or [vmgateway](https://docs.victoriametrics.com/victoriametrics/vmgateway/).
- The auth proxy must accept auth tokens from untrusted networks only via https in order to protect the auth tokens from MitM attacks.
- It is recommended using distinct auth tokens for distinct [tenants](#multitenancy) in order to reduce potential damage in case of compromised auth token for some tenants.
- Prefer using lists of allowed [API endpoints](#url-format), while disallowing access to other endpoints when configuring auth proxy in front of `vminsert` and `vmselect`.
  This minimizes attack surface.

See also [security recommendation for single-node VictoriaMetrics](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#security)
and [the general security page at VictoriaMetrics website](https://victoriametrics.com/security/).

### mTLS protection

By default `vminsert` and `vmselect` nodes accept http requests at `8480` and `8481` ports accordingly (these ports can be changed via `-httpListenAddr` command-line flags),
since it is expected that [vmauth](https://docs.victoriametrics.com/victoriametrics/vmauth/) is used for authorization and [TLS termination](https://en.wikipedia.org/wiki/TLS_termination_proxy)
in front of `vminsert` and `vmselect`.
[Enterprise version of VictoriaMetrics](https://docs.victoriametrics.com/victoriametrics/enterprise/) supports the ability to accept [mTLS](https://en.wikipedia.org/wiki/Mutual_authentication)
requests at `8480` and `8481` ports for `vminsert` and `vmselect` nodes, by specifying `-tls` and `-mtls` command-line flags.
For example, the following command runs `vmselect`, which accepts only mTLS requests at port `8481`:

```bash
./vmselect -tls -mtls
```

By default, system-wide [TLS Root CA](https://en.wikipedia.org/wiki/Root_certificate) is used for verifying client certificates if `-mtls` command-line flag is specified.
It is possible to specify custom TLS Root CA via `-mtlsCAFile` command-line flag.

By default `vminsert` and `vmselect` nodes use unencrypted connections to `vmstorage` nodes, since it is assumed that all the cluster components [run in a protected environment](#security). [Enterprise version of VictoriaMetrics](https://docs.victoriametrics.com/victoriametrics/enterprise/) provides optional support for [mTLS connections](https://en.wikipedia.org/wiki/Mutual_authentication#mTLS) between cluster components. Pass `-cluster.tls=true` command-line flag to `vminsert`, `vmselect` and `vmstorage` nodes in order to enable mTLS protection. Additionally, `vminsert`, `vmselect` and `vmstorage` must be configured with mTLS certificates via `-cluster.tlsCertFile`, `-cluster.tlsKeyFile` command-line options. These certificates are mutually verified when `vminsert` and `vmselect` dial `vmstorage`.

The following optional command-line flags related to mTLS are supported:

- `-cluster.tlsInsecureSkipVerify` can be set at `vminsert`, `vmselect` and `vmstorage` in order to disable peer certificate verification. Note that this breaks security.
- `-cluster.tlsCAFile` can be set at `vminsert`, `vmselect` and `vmstorage` for verifying peer certificates issued with custom [certificate authority](https://en.wikipedia.org/wiki/Certificate_authority). By default, system-wide certificate authority is used for peer certificate verification.
- `-cluster.tlsCipherSuites` can be set to the list of supported TLS cipher suites at `vmstorage`. See [the list of supported TLS cipher suites](https://pkg.go.dev/crypto/tls#pkg-constants).

When `vmselect` or `vminsert` runs with `-clusternativeListenAddr` command-line option, then it can be configured with `-clusternative.tls*` options similar to `-cluster.tls*` for accepting `mTLS` connections from top-level `vmselect` or `vminsert` nodes in [multi-level cluster setup](#multi-level-cluster-setup).

See [these docs](https://gist.github.com/f41gh7/76ed8e5fb1ebb9737fe746bae9175ee6) on how to set up mTLS in VictoriaMetrics cluster.

[Enterprise version of VictoriaMetrics](https://docs.victoriametrics.com/victoriametrics/enterprise/) can be downloaded and evaluated for free from [the releases page](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/latest).
See how to request a free [trial license](https://victoriametrics.com/products/enterprise/trial/).


## Monitoring

All the cluster components [expose various metrics](https://github.com/VictoriaMetrics/VictoriaMetrics/blob/master/deployment/docker/prometheus-vm-cluster.yml)
in Prometheus-compatible format at `/metrics` page on the TCP port set in `-httpListenAddr` command-line flag.
By default, the following TCP ports are used:

- `vminsert` - 8480
- `vmselect` - 8481
- `vmstorage` - 8482

> Prefer giving distinct scrape job names per each component type. I.e. `vmstorage`, `vminsert` and `vmselect` should have corresponding job names.

Use [the official Grafana dashboard for VictoriaMetrics cluster](https://grafana.com/grafana/dashboards/11176).

See more details on [how to monitor VictoriaMetrics components](https://docs.victoriametrics.com/victoriametrics/#monitoring).


## Cardinality limiter

`vmstorage` nodes can be configured with limits on the number of unique time series across all the tenants with the following command-line flags:

- `-storage.maxHourlySeries` is the limit on the number of [active time series](https://docs.victoriametrics.com/victoriametrics/faq/#what-is-an-active-time-series) during the last hour.
- `-storage.maxDailySeries` is the limit on the number of unique time series during the day. This limit can be used for limiting daily [time series churn rate](https://docs.victoriametrics.com/victoriametrics/faq/#what-is-high-churn-rate).

It is possible to use `-1` as a value for these flags{{% available_from "v1.140.0" %}} in order to enable series tracking but set limit to maximum possible value.
This is useful in order to estimate the number of unique series written to `vmstorage` without enforcing limits.

Note that these limits are set and applied individually per each `vmstorage` node in the cluster. So, if the cluster has `N` `vmstorage` nodes, then the cluster-level limits will be `N` times bigger than the per-`vmstorage` limits.

See more details about cardinality limiter in [these docs](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#cardinality-limiter).
