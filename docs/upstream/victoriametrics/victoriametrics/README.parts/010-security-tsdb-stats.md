<!-- Part 10 of 13 of victoriametrics/README.md (split because the page is big). -->

## Security

### Supported Versions

The following versions of VictoriaMetrics receive regular security fixes:

| Version                                                                        | Supported          |
|--------------------------------------------------------------------------------|--------------------|
| [Latest release](https://docs.victoriametrics.com/victoriametrics/changelog/)  | ✅                 |
| [LTS releases](https://docs.victoriametrics.com/victoriametrics/lts-releases/) | ✅                 |
| other releases                                                                 | ❌                 |

### Reporting a Vulnerability

Please report any security issues to <security@victoriametrics.com>

### CVE handling policy

**Source code:** Go dependencies are scanned by [govulncheck](https://pkg.go.dev/golang.org/x/vuln/cmd/govulncheck) in CI.
All vulnerabilities must be fixed before the next scheduled release and backported to [LTS releases](https://docs.victoriametrics.com/victoriametrics/lts-releases/).

**Docker images:** CVE findings in the [Alpine](https://security.alpinelinux.org/) base image pose minimal risk since VictoriaMetrics binaries are statically compiled with no OS dependencies.
When detected, only the Alpine base tag is updated.
Releases proceed as planned even if upstream fixes are not yet available.
For maximum security, hardened [scratch](https://hub.docker.com/_/scratch)-based images are also provided.
All images are continuously scanned by Docker Hub and verified before release using [grype](https://github.com/anchore/grype).

### General security recommendations:

* All VictoriaMetrics components must run in protected private networks without direct access from untrusted networks such as the Internet.
  The exception is [vmauth](https://docs.victoriametrics.com/victoriametrics/vmauth/) and [vmgateway](https://docs.victoriametrics.com/victoriametrics/vmgateway/),
  which are intended for serving public requests and performing authorization with [TLS termination](https://en.wikipedia.org/wiki/TLS_termination_proxy).
* All the requests from untrusted networks to VictoriaMetrics components must go through an auth proxy, such as [vmauth](https://docs.victoriametrics.com/victoriametrics/vmauth/)
  or [vmgateway](https://docs.victoriametrics.com/victoriametrics/vmgateway/). The proxy must be set up with proper authentication and authorization.
* Prefer using lists of allowed API endpoints, while disallowing access to other endpoints when configuring [vmauth](https://docs.victoriametrics.com/victoriametrics/vmauth/)
  in front of VictoriaMetrics components.
* Set a reasonable [`Strict-Transport-Security`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Strict-Transport-Security) header value on all the components to mitigate [MitM attacks](https://en.wikipedia.org/wiki/Man-in-the-middle_attack), for example: `max-age=31536000; includeSubDomains`. See `-http.header.hsts` flag.
* Set reasonable [`Content-Security-Policy`](https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP) header value to mitigate [XSS attacks](https://en.wikipedia.org/wiki/Cross-site_scripting). See `-http.header.csp` flag.
* Set reasonable [`X-Frame-Options`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options) header value to mitigate [clickjacking attacks](https://en.wikipedia.org/wiki/Clickjacking), for example `DENY`. See `-http.header.frameOptions` flag.

The following security-related command-line flags are available for all components with HTTP API:

* `-tls`, `-tlsCertFile` and `-tlsKeyFile` for switching from HTTP to HTTPS at `-httpListenAddr`.
  [Enterprise version of VictoriaMetrics](https://docs.victoriametrics.com/victoriametrics/enterprise/) supports automatic issuing of TLS certificates.
  See [these docs](#automatic-issuing-of-tls-certificates).
* `-mtls` and `-mtlsCAFile` for enabling [mTLS](https://en.wikipedia.org/wiki/Mutual_authentication) for requests to `-httpListenAddr`. See [these docs](#mtls-protection).
* `-httpAuth.username` and `-httpAuth.password` for protecting all the HTTP endpoints
  with [HTTP Basic Authentication](https://en.wikipedia.org/wiki/Basic_access_authentication).
* `-httpListenAddr=unix:/path/to/socket` for listening on a Unix domain socket instead of a TCP address.
  The socket file permissions are determined by the [umask](https://en.wikipedia.org/wiki/Umask) of the process.
  With the default systemd umask `0022`, only the owner of the socket file can connect to it.
  Set `UMask=0007` in the systemd unit and add other users to the group of the socket file in order to grant them access.
  Note that `-tls` and `-httpListenAddr.useProxyProtocol` cannot be used with Unix domain sockets.
* `-http.header.hsts`, `-http.header.csp`, and `-http.header.frameOptions` for serving `Strict-Transport-Security`, `Content-Security-Policy`
  and `X-Frame-Options` HTTP response headers.

### Protecting service endpoints

All VictoriaMetrics components expose internal metrics in Prometheus exposition format at the `/metrics` page for [#Monitoring](https://docs.victoriametrics.com/victoriametrics/#monitoring).
Consider limiting access to the `/metrics` page to trusted networks only.

The following service endpoints may require protection:

* `-deleteAuthKey` for protecting the `/api/v1/admin/tsdb/delete_series` endpoint. See [how to delete time series](#how-to-delete-time-series).
* `-snapshotAuthKey` for protecting the `/snapshot*` endpoints. See [how to work with snapshots](#how-to-work-with-snapshots).
* `-forceFlushAuthKey` for protecting the `/internal/force_flush` endpoint. See [force flush docs](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#forced-flush).
* `-forceMergeAuthKey` for protecting the `/internal/force_merge` endpoint. See [force merge docs](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#forced-merge).
* `-search.resetCacheAuthKey` for protecting the `/internal/resetRollupResultCache` endpoint. See [backfilling](#backfilling) for more details.
* `-reloadAuthKey` for protecting the `/-/reload` endpoint, which is used to force reload the [`-promscrape.config`](#how-to-scrape-prometheus-exporters-such-as-node-exporter).
* `-configAuthKey` for protecting the `/config` endpoint, since it may contain sensitive information such as passwords.
* `-flagsAuthKey` for protecting the `/flags` endpoint.
* `-pprofAuthKey` for protecting the `/debug/pprof/*` endpoints, which can be used for [profiling](#profiling).
* `-metricNamesStatsResetAuthKey` for protecting the `/api/v1/admin/status/metric_names_stats/reset` endpoint, used for [Metric Names Tracker](#track-ingested-metrics-usage).
* `-denyQueryTracing` for disallowing [query tracing](#query-tracing).

Explicitly set internal network interface for TCP and UDP ports for data ingestion with Graphite and OpenTSDB formats.
For example, substitute `-graphiteListenAddr=:2003` with `-graphiteListenAddr=<internal_iface_ip>:2003`. This protects from unexpected requests from untrusted network interfaces.

See also [security recommendation for VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/#security)
and [the general security page at VictoriaMetrics website](https://victoriametrics.com/security/).

### mTLS protection

By default `VictoriaMetrics` accepts http requests at `8428` port (this port can be changed via `-httpListenAddr` command-line flags).
[Enterprise version of VictoriaMetrics](https://docs.victoriametrics.com/victoriametrics/enterprise/) supports the ability to accept [mTLS](https://en.wikipedia.org/wiki/Mutual_authentication)
requests at this port, by specifying `-tls` and `-mtls` command-line flags. For example, the following command runs `VictoriaMetrics`, which accepts only mTLS requests at port `8428`:

```sh
./victoria-metrics -tls -mtls
```

By default, system-wide [TLS Root CA](https://en.wikipedia.org/wiki/Root_certificate) is used for verifying client certificates if `-mtls` command-line flag is specified.
It is possible to specify custom TLS Root CA via `-mtlsCAFile` command-line flag.

### Automatic issuing of TLS certificates

All the VictoriaMetrics [Enterprise](https://docs.victoriametrics.com/victoriametrics/enterprise/) components support automatic issuing of TLS certificates for public HTTPS server running at `-httpListenAddr`
via [Let's Encrypt service](https://letsencrypt.org/). The following command-line flags must be set in order to enable automatic issuing of TLS certificates:

* `-httpListenAddr` must be set for listening TCP port `443`. For example, `-httpListenAddr=:443`. This port must be accessible by the [Let's Encrypt service](https://letsencrypt.org/).
* `-tls` must be set in order to accept HTTPS requests at `-httpListenAddr`. Note that `-tlcCertFile` and `-tlsKeyFile` aren't needed when automatic TLS certificate issuing is enabled.
* `-tlsAutocertHosts` must be set to comma-separated list of hosts, which can be reached via `-httpListenAddr`. TLS certificates are automatically issued for these hosts.
* `-tlsAutocertEmail` must be set to contact email for the issued TLS certificates.
* `-tlsAutocertCacheDir` may be set to the directory path for persisting the issued TLS certificates between VictoriaMetrics restarts. If this flag isn't set,
  then TLS certificates are re-issued on every restart.

This functionality can be evaluated for free according to [these docs](https://docs.victoriametrics.com/victoriametrics/enterprise/).

See also [security recommendations](#security).

### Software Bill of Materials (SBOM)

Every VictoriaMetrics container{{% available_from "v1.137.0" %}} image published to
[Docker Hub](https://hub.docker.com/u/victoriametrics) and [Quay.io](https://quay.io/organization/victoriametrics) include an [SPDX](https://spdx.dev/) SBOM attestation generated automatically by BuildKit during `docker buildx build`.

To inspect the SBOM for an image:

```sh
docker buildx imagetools inspect \
  docker.io/victoriametrics/victoria-metrics:latest \
  --format "{{ json .SBOM }}"
```

To scan an image using its SBOM attestation with [Trivy](https://github.com/aquasecurity/trivy):

```sh
trivy image --sbom-sources oci \
  docker.io/victoriametrics/victoria-metrics:latest
```


## Tuning

* No need to tune for VictoriaMetrics - it uses reasonable defaults for command-line flags,
  which are automatically adjusted for the available CPU and RAM resources.
* No need to tune for Operating System - VictoriaMetrics is optimized for default OS settings.
  The only option is increasing the limit on [the number of open files in the OS](https://medium.com/@muhammadtriwibowo/set-permanently-ulimit-n-open-files-in-ubuntu-4d61064429a).
  The recommendation is not specific to VictoriaMetrics only, but also for any service that handles many HTTP connections and stores data on disk.
* VictoriaMetrics is a write-heavy application, and its performance depends on disk performance. So be careful with other
  applications or utilities (like [fstrim](https://manpages.ubuntu.com/manpages/noble/en/man8/fstrim.8.html))
  which could [exhaust disk resources](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/1521).
* The recommended filesystem is `ext4`, the recommended persistent storage is [persistent HDD-based disk on GCP](https://cloud.google.com/compute/docs/disks/#pdspecs),
  since it is protected from hardware failures via internal replication, and it can be [resized on the fly](https://cloud.google.com/compute/docs/disks/add-persistent-disk#resize_pd).
  If you plan to store more than 1TB of data on an `ext4` partition, then the following options are recommended to pass to `mkfs.ext4`:

```sh
mkfs.ext4 ... -O 64bit,huge_file,extent -T huge
```


## Monitoring

VictoriaMetrics exports internal metrics in Prometheus exposition format at `/metrics` page.
These metrics [can be scraped](https://github.com/VictoriaMetrics/VictoriaMetrics/blob/master/deployment/docker/prometheus-vm-single.yml)
via [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/) or any other Prometheus-compatible scraper.

> Single-node VictoriaMetrics can self-scrape its metrics when `-selfScrapeInterval` command-line flag is
set to duration greater than 0. For example, `-selfScrapeInterval=10s` scrapes `/metrics` page every 10 seconds.

See the list of official [Grafana dashboards for VictoriaMetrics components](https://grafana.com/orgs/victoriametrics/dashboards).

Please follow the monitoring recommendations below:

* Prefer giving distinct scrape job names per each component type. I.e. `vmagent` and `vmalert` should have corresponding job names.
* Never use load balancer address for scraping metrics. All the monitored components should be scraped directly by their address.
* Set up [recommended alerts](https://github.com/VictoriaMetrics/VictoriaMetrics/tree/master/deployment/docker#alerts)
via [vmalert](https://docs.victoriametrics.com/victoriametrics/vmalert/) or via Prometheus.
* See currently running queries and their execution times at [`active queries` page](#active-queries).
* See queries that take the most time to execute at [`top queries` page](#top-queries).

See also [VictoriaMetrics Monitoring](https://victoriametrics.com/blog/victoriametrics-monitoring/)
and [troubleshooting docs](https://docs.victoriametrics.com/victoriametrics/troubleshooting/).

> [VictoriaMetrics Cloud](https://console.victoriametrics.cloud/signUp?utm_source=website&utm_campaign=docs_vm_single_monitoring)
> provides built-in monitoring dashboards and automatic alerts when resource consumption is high or configured limits are approached,
> so you get notified before issues impact your workload. See the [VictoriaMetrics Cloud documentation](https://docs.victoriametrics.com/victoriametrics-cloud/) to get started.

> VictoriaMetrics components do not expose metadata `TYPE` and `HELP` fields on `/metrics` page.
> Services like Google Cloud Managed Prometheus could require metadata to be present for scraping. In this case, pass `-metrics.exposeMetadata`
command-line to them. See [these docs](https://cloud.google.com/stackdriver/docs/managed-prometheus/troubleshooting#missing-metric-type) for details.


## TSDB stats

VictoriaMetrics returns TSDB stats at `/api/v1/status/tsdb` page in the way similar to Prometheus - see [these Prometheus docs](https://prometheus.io/docs/prometheus/latest/querying/api/#tsdb-stats). VictoriaMetrics accepts the following optional query args at `/api/v1/status/tsdb` page:

* `topN=N` where `N` is the number of top entries to return in the response. By default, top 10 entries are returned.
* `date=YYYY-MM-DD` where `YYYY-MM-DD` is the date for collecting the stats. By default, the stats is collected for the current day.
* `focusLabel=LABEL_NAME` returns label values with the highest number of time series for the given `LABEL_NAME` in the `seriesCountByFocusLabelValue` list.
* `match[]=SELECTOR` where `SELECTOR` is an arbitrary [time series selector](https://prometheus.io/docs/prometheus/latest/querying/basics/#time-series-selectors) for series to take into account during stats calculation. By default all the series are taken into account.
* `extra_label=LABEL=VALUE`. See [these docs](#prometheus-querying-api-enhancements) for more details.

In [cluster version of VictoriaMetrics](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/) each vmstorage tracks the stored time series individually.
vmselect requests stats via [/api/v1/status/tsdb](https://docs.victoriametrics.com/victoriametrics/url-examples/#apiv1statustsdb) API from each vmstorage node and merges the results by summing per-series stats.
This may lead to inflated values when samples for the same time series are spread across multiple vmstorage nodes
due to [replication](#replication) or [rerouting](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/#cluster-availability).

VictoriaMetrics provides UI on top of `/api/v1/status/tsdb` - see [cardinality explorer docs](#cardinality-explorer).

VictoriaMetrics enhances Prometheus stats with `requestsCount` and `lastRequestTimestamp` for `seriesCountByMetricName`. This stats added if [tracking metric names stats](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#track-ingested-metrics-usage) is configured.
