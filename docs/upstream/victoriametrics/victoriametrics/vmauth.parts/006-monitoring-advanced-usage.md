<!-- Part 6 of 6 of victoriametrics/vmauth.md (split because the page is big). -->

## Monitoring

`vmauth` exports various metrics in Prometheus exposition format at `http://vmauth-host:8427/metrics` page. It is recommended to set up regular scraping of this page either via [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/) or via a Prometheus-compatible scraper, so the exported metrics can be analyzed later.
Use the official [Grafana dashboard](https://grafana.com/grafana/dashboards/21394) and [alerting rules](https://github.com/VictoriaMetrics/VictoriaMetrics/blob/master/deployment/docker/rules/alerts-vmauth.yml) for `vmauth` monitoring.

If you use Google Cloud Managed Prometheus for scraping metrics from VictoriaMetrics components, then pass `-metrics.exposeMetadata`
command-line to them, so they add `TYPE` and `HELP` comments for each exposed metric on the `/metrics` page.
See [these docs](https://cloud.google.com/stackdriver/docs/managed-prometheus/troubleshooting#missing-metric-type) for details.

`vmauth` exports the following metrics for each defined user in [`-auth.config`](#auth-config):

* `vmauth_user_requests_total` [counter](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#counter) - the number of requests served for the given `username`
* `vmauth_user_request_errors_total` [counter](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#counter) - the number of request errors for the given `username`
* `vmauth_user_request_backend_requests_total` [counter](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#counter) - the number of backend requests for the given `username`
* `vmauth_user_request_backend_errors_total` [counter](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#counter) - the number of backend request errors for the given `username`
* `vmauth_user_request_duration_seconds` [summary](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#summary) - the duration of requests for the given `username`
* `vmauth_user_concurrent_requests_limit_reached_total` [counter](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#counter) - the number of failed requests
  for the given `username` because of exceeded [concurrency limits](#concurrency-limiting)
* `vmauth_user_concurrent_requests_capacity` [gauge](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#gauge) - the maximum number of [concurrent requests](#concurrency-limiting)
  for the given `username`
* `vmauth_user_concurrent_requests_current` [gauge](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#gauge) - the current number of [concurrent requests](#concurrency-limiting)
  for the given `username`

By default, per-user metrics contain only the `username` label. This label is set to the `username` field value at the corresponding user section in the [`-auth.config`](#auth-config) file.
It is possible to override the `username` label value by specifying the `name` field in addition to the `username` field.
For example, the following config will result in `vmauth_user_requests_total{username="foobar"}` instead of `vmauth_user_requests_total{username="secret_user"}`:

```yaml
users:
- username: "secret_user"
  name: "foobar"
  # other config options here
```

Additional labels for per-user metrics can be specified via the `metric_labels` section. For example, the following config defines `{dc="eu",team="dev"}` labels additionally to `username="foobar"` label:

```yaml
users:
- username: "foobar"
  metric_labels:
   dc: eu
   team: dev
  # other config options here
```

`vmauth` exports the following metrics if the `unauthorized_user` section is defined in [`-auth.config`](#auth-config):

* `vmauth_unauthorized_user_requests_total` [counter](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#counter) - the number of requests served for unauthorized user
* `vmauth_unauthorized_user_request_errors_total` [counter](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#counter) - the number of request errors for unauthorized user
* `vmauth_unauthorized_user_request_backend_requests_total` [counter](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#counter) - the number of backend requests for unauthorized user
* `vmauth_unauthorized_user_request_backend_errors_total` [counter](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#counter) - the number of backend request errors for unauthorized user
* `vmauth_unauthorized_user_request_duration_seconds` [summary](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#summary) - the duration of requests for unauthorized user
* `vmauth_unauthorized_user_concurrent_requests_limit_reached_total` [counter](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#counter) - the number of failed requests because of exceeded [concurrency limits](#concurrency-limiting) for unauthorized user
* `vmauth_unauthorized_user_concurrent_requests_capacity` [gauge](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#gauge) - the maximum number of [concurrent requests](#concurrency-limiting) for unauthorized user
* `vmauth_unauthorized_user_concurrent_requests_current` [gauge](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#gauge) - the current number of [concurrent requests](#concurrency-limiting) for unauthorized user


## How to build from sources

It is recommended to use [binary releases](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/latest) - `vmauth` is located in `vmutils-*` archives there.

### Development build

1. [Install Go](https://golang.org/doc/install).
1. Run `make vmauth` from the root folder of [the repository](https://github.com/VictoriaMetrics/VictoriaMetrics).
   It builds the `vmauth` binary and puts it into the `bin` folder.

### Production build

1. [Install Docker](https://docs.docker.com/install/).
1. Run `make vmauth-prod` from the root folder of [the repository](https://github.com/VictoriaMetrics/VictoriaMetrics).
   It builds the `vmauth-prod` binary and puts it into the `bin` folder.

### Building Docker images

Run `make package-vmauth`. It builds `victoriametrics/vmauth:<PKG_TAG>` docker image locally.
`<PKG_TAG>` is an auto-generated image tag, which depends on the source code in the repository.
The `<PKG_TAG>` may be manually set via `PKG_TAG=foobar make package-vmauth`.

The base Docker image is [alpine](https://hub.docker.com/_/alpine), but you can use any other base image by setting it via the `<ROOT_IMAGE>` environment variable. For example, the following command builds the image on top of [scratch](https://hub.docker.com/_/scratch) image:

```sh
ROOT_IMAGE=scratch make package-vmauth
```


## Profiling

`vmauth` provides handlers for collecting the following [Go profiles](https://blog.golang.org/profiling-go-programs):

* Memory profile. It can be collected with the following command (replace `0.0.0.0` with hostname if needed):

```sh
curl http://0.0.0.0:8427/debug/pprof/heap > mem.pprof
```

* CPU profile. It can be collected with the following command (replace `0.0.0.0` with hostname if needed):

```sh
curl http://0.0.0.0:8427/debug/pprof/profile > cpu.pprof
```

The command for collecting CPU profiles waits for 30 seconds before returning.

The collected profiles may be analyzed with [go tool pprof](https://github.com/google/pprof).
It is safe to share the collected profiles from a security perspective, as they do not contain sensitive information.


## Advanced usage

Pass `-help` command-line arg to `vmauth` in order to see all the configuration options:

### Common flags
These flags are available in both VictoriaMetrics OSS and VictoriaMetrics Enterprise.
{{% content "vmauth_common_flags.md" %}}

### Enterprise flags
These flags are available only in [VictoriaMetrics enterprise](https://docs.victoriametrics.com/victoriametrics/enterprise/).
{{% content "vmauth_enterprise_flags.md" %}}

---

Section below contains backward-compatible anchors for links that were moved or renamed.

###### Security Considerations

Moved to [security](#security).
