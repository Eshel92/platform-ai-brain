<!-- Part 6 of 6 of victoriametrics/vmalert.md (split because the page is big). -->

## Configuration

### Flags

Pass `-help` to `vmalert` in order to see the full list of supported
command-line flags with their descriptions.

The shortlist of configuration flags is the following:

#### Common flags
These flags are available in both VictoriaMetrics OSS and VictoriaMetrics Enterprise.
{{% content "vmalert_common_flags.md" %}}

#### Enterprise flags
These flags are available only in [VictoriaMetrics enterprise](https://docs.victoriametrics.com/victoriametrics/enterprise/).
{{% content "vmalert_enterprise_flags.md" %}}

### Hot config reload

`vmalert` supports "hot" config reload via the following methods:

* send SIGHUP signal to `vmalert` process;
* send GET request to `/-/reload` endpoint (this endpoint can be protected with `-reloadAuthKey` command-line flag);
* configure `-configCheckInterval` flag for periodic reload on config change.

On config reload, vmalert re-reads configurations specified via `-rule`, `-rule.templates` and `-notifier.config` cmd-line
flags. 

If configuration has changed, vmalert will update its internal states accordingly, log the corresponding message,
set `vmalert_config_last_reload_successful` to `1` and `vmalert_config_last_reload_success_timestamp_seconds` to the moment
when the update happened. If configuration hasn't changed, vmalert won't do anything.

If vmalert failed to load or parse the configuration, it will log a corresponding error message and set 
`vmalert_config_last_reload_successful` to `0`. It will keep the previous config and will continue operating as before. 

### URL params

To set additional URL params for `datasource.url`, `remoteWrite.url` or `remoteRead.url`
just add them in address: `-datasource.url=http://localhost:8428?nocache=1`.

To set additional URL params for specific [group of rules](#groups) modify
the `params` group:

```yaml
groups:
  - name: TestGroup
    params:
      denyPartialResponse: ["true"]
      extra_label: ["env=dev"]
```

Please note, `params` are used only for executing rules expressions (requests to `datasource.url`).
If there would be a conflict between URL params set in `datasource.url` flag and params in group definition
the latter will have higher priority.

### Chaining groups

For chaining groups, they must be executed in a specific order, and the next group should be executed after
the results from previous group are available in the datasource.
In `vmalert`, user can specify `eval_offset` to achieve that {{% available_from "v1.113.0" %}}.

For example:

```yaml
groups:
  - name: BaseGroup
    interval: 5m
    eval_offset: 1m
    rules:
      - record: http_server_request_duration_seconds:sum_rate:5m:http_get
        expr: |
          sum without(instance, pod) (
            rate(
              http_server_request_duration_seconds{
                http_request_method="GET"
              }[5m]
            )
          )
      - record: http_server_request_duration_seconds:sum_rate:5m:http_post
        expr: |
          sum without(instance, pod) (
            rate(
              http_server_request_duration_seconds{
                http_request_method="POST"
              }[5m]
            )
          )
  - name: TopGroup
    interval: 5m
    eval_offset: 3m
    rules:
      - record: http_server_request_duration_seconds:sum_rate:5m:merged
        expr: |
          http_server_request_duration_seconds:sum_rate:5m:http_get
          or
          http_server_request_duration_seconds:sum_rate:5m:http_post
```

This configuration ensures that rules in `BaseGroup` are executed at(assuming vmalert starts at `12:00:00`):

```
[12:01:00, 12:06:00, 12:11:00, 12:16:00...]
```

while rules in group `TopGroup` are executed at:

```
[12:03:00, 12:08:00, 12:13:00, 12:18:00...]
```

As a result, `TopGroup` can consistently obtain the latest results from `BaseGroup` if `BaseGroup` completes its evaluation and uploads its results to the datasource within 2 minutes.

By default, the `eval_offset` values should be at least 30 seconds apart to accommodate the
`-search.latencyOffset(default 30s)` command-line flag at vmselect or VictoriaMetrics single-node.
The minimum `eval_offset` gap should be adjusted according to the sum of the execution duration of `BaseGroup` and `-search.latencyOffset`.

### Notifier configuration file

Notifier also supports configuration via file specified with flag `notifier.config`:

```sh
./bin/vmalert -rule=app/vmalert/config/testdata/rules.good.rules \
  -datasource.url=http://localhost:8428 \
  -notifier.config=app/vmalert/notifier/testdata/consul.good.yaml
```

The configuration file allows to configure static notifiers, discover notifiers via
[Consul](https://prometheus.io/docs/prometheus/latest/configuration/configuration/#consul_sd_config)
and [DNS](https://prometheus.io/docs/prometheus/latest/configuration/configuration/#dns_sd_config):
For example:

```yaml
static_configs:
  - targets:
      # support using full url
      - 'http://alertmanager:9093/test/api/v2/alerts'
      - 'https://alertmanager:9093/api/v2/alerts'
      # the following target with only host:port will be used as <scheme>://localhost:9093/<path_prefix>/api/v2/alerts
      - localhost:9093

consul_sd_configs:
  - server: localhost:8500
    services:
      - alertmanager

dns_sd_configs:
  - names:
      - my.domain.com
    type: 'A'
    port: 9093
```

The list of configured or discovered Notifiers can be explored via [UI](#web).
If Alertmanager runs in cluster mode then all its URLs needs to be available during discovery
to ensure [high availability](https://github.com/prometheus/alertmanager#high-availability).

The configuration file [specification](https://github.com/VictoriaMetrics/VictoriaMetrics/blob/master/app/vmalert/notifier/config.go)
is the following:

```yaml
# Per-target Notifier timeout when pushing alerts.
[ timeout: <duration> | default = 10s ]

# Prefix for the HTTP path alerts are pushed to.
[ path_prefix: <path> | default = / ]

# Configures the protocol scheme used for requests.
[ scheme: <scheme> | default = http ]

# Sets the `Authorization` header on every request with the
# configured username and password.
# password and password_file are mutually exclusive.
basic_auth:
  [ username: <string> ]
  [ password: <string> ]
  [ password_file: <string> ]

# Optional `Authorization` header configuration.
authorization:
  # Sets the authentication type.
  [ type: <string> | default: Bearer ]
  # Sets the credentials. It is mutually exclusive with
  # `credentials_file`.
  [ credentials: <secret> ]
  # Sets the credentials to the credentials read from the configured file.
  # It is mutually exclusive with `credentials`.
  [ credentials_file: <filename> ]

# Configures the scrape request's TLS settings.
# see https://prometheus.io/docs/prometheus/latest/configuration/configuration/#tls_config
tls_config:
  [ <tls_config> ]

# Configures Bearer authentication token via string
bearer_token: <string>
# or by passing path to the file with token.
bearer_token_file: <string>

# Configures OAuth 2.0 authentication
# see https://prometheus.io/docs/prometheus/latest/configuration/configuration/#oauth2
oauth2:
  [ <oauth2_config> ]

# Optional list of HTTP headers in form `header-name: value`
# applied for all requests to notifiers
# For example:
#  headers:
#    - "CustomHeader: foo"
#    - "CustomHeader2: bar"
headers:
  [ <string>, ...]

# List of labeled statically configured Notifiers.
#
# Each list of targets may be additionally instructed with
# authorization params. Target's authorization params will
# inherit params from global authorization params if there
# are no conflicts.
static_configs:
  [ - targets: ]
      [ - '<host>' ]
      [ oauth2 ]
      [ basic_auth ]
      [ authorization ]
      [ tls_config ]
      [ bearer_token ]
      [ bearer_token_file ]
      [ headers ]
      # Relabel configurations for static notifiers.
      # If used with the external `alert_relabel_configs`, the external configs are applied first.
      alert_relabel_configs:
        [ - <relabel_config> ... ]

# List of Consul service discovery configurations.
consul_sd_configs:
  # See https://prometheus.io/docs/prometheus/latest/configuration/configuration/#consul_sd_config
  [ - <consul_sd_config> ]
  # Relabel configurations for Consul SD notifiers.
  # If used with the external `alert_relabel_configs`, the external configs are applied first.
  alert_relabel_configs:
    [ - <relabel_config> ... ]

# List of DNS service discovery configurations.
dns_sd_configs:
  # See https://prometheus.io/docs/prometheus/latest/configuration/configuration/#dns_sd_config
  [ - <dns_sd_config> ]
  # Relabel configurations for DNS SD notifiers.
  # If used with the external `alert_relabel_configs`, the external configs are applied first.
  alert_relabel_configs:
    [ - <relabel_config> ... ]

# List of relabel configurations for entities discovered via service discovery.
# Supports the same relabeling features as the rest of VictoriaMetrics components.
# See https://docs.victoriametrics.com/victoriametrics/relabeling/
relabel_configs:
  [ - <relabel_config> ... ]

# List of relabel configurations for alert labels sent via Notifier.
# Supports the same relabeling features as the rest of VictoriaMetrics components.
# See https://docs.victoriametrics.com/victoriametrics/relabeling/
alert_relabel_configs:
  [ - <relabel_config> ... ]
```

The configuration file can be [hot-reloaded](#hot-config-reload).


## DNS URLs

If `vmalert` encounters URLs with the `dns+` prefix in the hostname (such as `http://dns+some-addr:8428/some/path`), it resolves `some-addr` into IP addresses via DNS A/AAAA records.
The port from the original URL is appended to each discovered IP address.
Each discovered IP address is used for least-loaded balancing of write requests.

DNS URLs are supported in the following places:

* In `-remoteWrite.url`, `-remoteRead.url` and `-datasource.url` command-line flags. For example, if `victoria-metrics` [DNS A Record](https://datatracker.ietf.org/doc/html/rfc1035#section-3.4.1) record contains
  `192.168.1.15` IP address, then `-remoteWrite.url=http://dns+victoria-metrics:8428` is automatically resolved into
  `-remoteWrite.url=http://192.168.1.15:8428`.

DNS URLs are useful when client-side HTTP load balancing is needed. A good example
is a [Kubernetes headless Service](https://kubernetes.io/docs/concepts/services-networking/service/#headless-services),
which returns multiple IP addresses for a single hostname.

### DNS URLs and HTTPS

When a `dns+` URL uses the `https` scheme, `vmalert` connects to the discovered
IP addresses directly. No [SNI](https://en.wikipedia.org/wiki/Server_Name_Indication)
is sent in the TLS handshake, and the server certificate is verified against the IP address,
which fails unless the certificate contains the corresponding
[IP SAN](https://en.wikipedia.org/wiki/Subject_Alternative_Name) entries.

To use `dns+` URLs with HTTPS, pass the original hostname via the corresponding
`tlsServerName` command-line flag - `-datasource.tlsServerName`, `-remoteRead.tlsServerName`
or `-remoteWrite.tlsServerName`. It is used both as SNI and as the name the server
certificate is verified against:

```sh
-datasource.url=https://dns+victoria-metrics:8428
-datasource.tlsServerName=victoria-metrics
```

Alternatively, issue server certificates with IP SAN entries for every backend IP address.
Avoid `tlsInsecureSkipVerify` flags for working around this, since they disable
server certificate verification completely.


## SRV URLs

If `vmalert` encounters URLs with `srv+` prefix in hostname (such as `http://srv+some-addr/some/path`), then it resolves `some-addr` [DNS SRV](https://en.wikipedia.org/wiki/SRV_record)
record into TCP address with hostname and TCP port, and then use the resulting URL when it needs to connect to it.

SRV URLs are supported in the following places:

* In `-remoteWrite.url`, `-remoteRead.url` and `-datasource.url` command-line flags. For example, if `victoria-metrics` [DNS SRV](https://en.wikipedia.org/wiki/SRV_record) record contains
  `victoria-metrics-host:8085`, then `-remoteWrite.url=http://srv+victoria-metrics:8428` is automatically resolved into
  `-remoteWrite.url=http://victoria-metrics-host:8085`. If the DNS SRV record is resolved into multiple TCP addresses, then `vmalert`
   performs per request round-robin load-balancing.

SRV URLs are useful when HTTP services run on different TCP ports or when their TCP ports can change over time (for instance, after a restart).



## Contributing

`vmalert` is mostly designed and built by VictoriaMetrics community.
Feel free to share your experience and ideas for improving this
software. Please keep simplicity as the main priority.


## How to build from sources

It is recommended using
[binary releases](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/latest)

* `vmalert` is located in `vmutils-*` archives there.

### Docker image

You can build `vmalert` docker image from source and push it to your own docker repository.
Run the following commands from the root folder of [the repository](https://github.com/VictoriaMetrics/VictoriaMetrics):

```sh
make package-vmalert
docker tag victoria-metrics/vmalert:version my-repo:my-version-name
docker push my-repo:my-version-name
```

To run the built image in `victoria-metrics-k8s-stack` or `VMAlert` CR object apply the following config change:

```yaml
kind: VMAlert
spec:
  image:
    repository: my-repo
    tag: my-version-name
```

### Development build

1. [Install Go](https://golang.org/doc/install).
1. Run `make vmalert` from the root folder of [the repository](https://github.com/VictoriaMetrics/VictoriaMetrics).
   It builds `vmalert` binary and puts it into the `bin` folder.

### Production build

1. [Install docker](https://docs.docker.com/install/).
1. Run `make vmalert-prod` from the root folder of [the repository](https://github.com/VictoriaMetrics/VictoriaMetrics).
   It builds `vmalert-prod` binary and puts it into the `bin` folder.

### ARM build

ARM build may run on Raspberry Pi or on [energy-efficient ARM servers](https://blog.cloudflare.com/arm-takes-wing/).

### Development ARM build

1. [Install Go](https://golang.org/doc/install).
1. Run `make vmalert-linux-arm` or `make vmalert-linux-arm64` from the root folder of [the repository](https://github.com/VictoriaMetrics/VictoriaMetrics).
   It builds `vmalert-linux-arm` or `vmalert-linux-arm64` binary respectively and puts it into the `bin` folder.

### Production ARM build

1. [Install docker](https://docs.docker.com/install/).
1. Run `make vmalert-linux-arm-prod` or `make vmalert-linux-arm64-prod` from the root folder of [the repository](https://github.com/VictoriaMetrics/VictoriaMetrics).
   It builds `vmalert-linux-arm-prod` or `vmalert-linux-arm64-prod` binary respectively and puts it into the `bin` folder.
