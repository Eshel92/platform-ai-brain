<!-- Part 4 of 6 of victoriametrics/vmauth.md (split because the page is big). -->

## Concurrency limiting

`vmauth` may limit the number of concurrent requests according to the following command-line flags:

* `-maxConcurrentRequests` limits the global number of concurrent requests `vmauth` can serve across all the configured users.
* `-maxConcurrentPerUserRequests` limits the number of concurrent requests `vmauth` can serve per each configured user.

It is also possible to set individual limits on the number of concurrent requests per user with the `max_concurrent_requests` option.
For example, the following [`-auth.config`](#auth-config) limits the number of concurrent requests from the user `foo` to 10:

```yaml
users:
- username: foo
  password: bar
  url_prefix: "http://some-backend/"
  max_concurrent_requests: 10
```

`vmauth` responds with `429 Too Many Requests` HTTP error when the number of concurrent requests exceeds the configured limits for the duration
exceeding the `-maxQueueDuration` command-line flag value.

The following [metrics](https://docs.victoriametrics.com/victoriametrics/vmauth/#monitoring) related to concurrency limits are exposed by `vmauth`:

* `vmauth_concurrent_requests_capacity` - the global limit on the number of concurrent requests `vmauth` can serve.
  It is set via the `-maxConcurrentRequests` command-line flag.
* `vmauth_concurrent_requests_current` - the current number of concurrent requests `vmauth` processes.
* `vmauth_concurrent_requests_limit_reached_total` - the number of requests rejected with `429 Too Many Requests` error
  because the global concurrency limit has been reached.
* `vmauth_user_concurrent_requests_capacity{username="..."}` - the limit on the number of concurrent requests for the given `username`.
* `vmauth_user_concurrent_requests_current{username="..."}` - the current number of concurrent requests for the given `username`.
* `vmauth_user_concurrent_requests_limit_reached_total{username="..."}` - the number of requests rejected with `429 Too Many Requests` error
  because the concurrency limit has been reached for the given `username`.
* `vmauth_unauthorized_user_concurrent_requests_capacity` - the limit on the number of concurrent requests for unauthorized users (if `unauthorized_user` section is used).
* `vmauth_unauthorized_user_concurrent_requests_current` - the current number of concurrent requests for unauthorized users (if `unauthorized_user` section is used).
* `vmauth_unauthorized_user_concurrent_requests_limit_reached_total` - the number of requests rejected with `429 Too Many Requests` error
  because the concurrency limit has been reached for unauthorized users (if the `unauthorized_user` section is used).

See also [request body buffering](https://docs.victoriametrics.com/victoriametrics/vmauth/#request-body-buffering).


## Request body buffering

`vmauth` can buffer request bodies {{% available_from "v1.135.0" %}} before proxying the requests to backends. This prevents slow-writing clients from occupying backend connections.
This is especially important when clients send requests over unreliable or low-bandwidth networks (for example, [IoT](https://en.wikipedia.org/wiki/Internet_of_things) devices over EDGE networks),
where slow uploads can exhaust concurrency limits, increase latency, reduce ingestion rate, and trigger `429 Too Many Requests` responses even when backend resources are not saturated.

Request body buffering can be configured with the `-requestBufferSize` command-line flag, which defines the maximum number of bytes to buffer from the request body
before proxying the request to the backend. If buffering exceeds the duration specified by the `-maxQueueDuration` command-line flag, the request is rejected.

Request bodies are buffered before applying per-user [concurrency limits](https://docs.victoriametrics.com/victoriametrics/vmauth/#concurrency-limiting).

The following [metrics](https://docs.victoriametrics.com/victoriametrics/vmauth/#monitoring) related to request buffering are exposed by `vmauth`:

* `vmauth_http_request_errors_total{reason="reject_slow_client"}` - the number of rejected requests because the request body couldn't be read during `-maxQueueDuration`.
* `vmauth_buffer_request_body_duration_seconds` - the [summary](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#summary) for the request body buffering duration.
  Use this metric to understand buffering performance and identify slow clients.

See also [concurrency limits](https://docs.victoriametrics.com/victoriametrics/vmauth/#concurrency-limiting).


## Backend TLS setup

By default, `vmauth` uses system settings when performing requests to HTTPS backends specified via the `url_prefix` option in the [`-auth.config`](#auth-config). These settings can be overridden with the following command-line flags:

* `-backend.tlsInsecureSkipVerify` allows skipping TLS verification when connecting to HTTPS backends.
  This global setting can be overridden at the per-user level inside [`-auth.config`](#auth-config) via the `tls_insecure_skip_verify` option. For example:

  ```yaml
  - username: "foo"
    url_prefix: "https://localhost"
    tls_insecure_skip_verify: true
  ```

* `-backend.tlsCAFile` allows specifying the path to the TLS Root CA for verifying backend TLS certificates.
  This global setting can be overridden at the per-user level inside [`-auth.config`](#auth-config) via the `tls_ca_file` option.
  For example:

  ```yaml
  - username: "foo"
    url_prefix: "https://localhost"
    tls_ca_file: "/path/to/tls/root/ca"
  ```

* `-backend.tlsCertFile` and `-backend.tlsKeyFile` allow specifying a client TLS certificate for passing in requests to HTTPS backends,
  so these certificates could be verified on the backend side (aka [mTLS](https://en.wikipedia.org/wiki/Mutual_authentication)).
  This global setting can be overridden at the per-user level inside [`-auth.config`](#auth-config) via `tls_cert_file` and `tls_key_file` options. For example:

  ```yaml
  - username: "foo"
    url_prefix: "https://localhost"
    tls_cert_file: "/path/to/tls/cert"
    tls_key_file: "/path/to/tls/key"
  ```

* `-backend.tlsServerName` allows specifying optional [TLS ServerName](https://en.wikipedia.org/wiki/Server_Name_Indication) for passing in requests to HTTPS backends.
  This global setting can be overridden at the per-user level inside [`-auth.config`](#auth-config) via the `tls_server_name` option. For example:

  ```yaml
  - username: "foo"
    url_prefix: "https://localhost"
    tls_server_name: "foo.bar.com"
  ```

The `-backend.tlsCAFile`, `-backend.tlsCertFile`, `-backend.tlsKeyFile`, `tls_ca_file`, `tls_cert_file`, and `tls_key_file` may point either to a local file or to a `http` / `https` URL.
The file is checked for modifications every second and is automatically re-read when it is updated.


## IP filters

The [Enterprise version](https://docs.victoriametrics.com/victoriametrics/enterprise/) of `vmauth` can be configured to allow/deny incoming requests via global and per-user IP filters.

For example, the following config allows requests to `vmauth` from `10.0.0.0/24` network and from `1.2.3.4` IP address, while denying requests from `10.0.0.42` IP address:

```yaml
users:
# User configs here

ip_filters:
  allow_list:
  - 10.0.0.0/24
  - 1.2.3.4
  deny_list: [10.0.0.42]
```

The following config allows requests for the user `foobar` only from the IP `127.0.0.1`:

```yaml
users:
- username: "foobar"
  password: "***"
  url_prefix: "http://localhost:8428"
  ip_filters:
    allow_list: [127.0.0.1]
```

By default, the client's TCP address is utilized for IP filtering. In scenarios where `vmauth` operates behind a reverse proxy, it is advisable to configure `vmauth` to retrieve the client IP address from an [HTTP header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Forwarded-For) (e.g., `X-Forwarded-For`) {{% available_from "v1.107.0" %}} or via the [Proxy Protocol](https://www.haproxy.org/download/1.8/doc/proxy-protocol.txt) for TCP load balancers. This can be achieved using the global configuration flags:

* `-httpRealIPHeader=X-Forwarded-For` {{% available_from "v1.107.0" %}}
* `-httpListenAddr.useProxyProtocol=true`

### Per-User Configuration

The values of `httpRealIPHeader` {{% available_from "v1.107.0" %}} can be changed on a per-user basis in the user-specific configuration.

```yaml
users:
- username: "foobar"
  password: "***"
  url_prefix: "http://localhost:8428"
  ip_filters:
    allow_list: [127.0.0.1]
    real_ip_header: X-Forwarded-For
- username: "foobar"
  password: "***"
  url_prefix: "http://localhost:8428"
  ip_filters:
    allow_list: [127.0.0.1]
    real_ip_header: CF-Connecting-IP
```

See the config example of using [IP filters](https://github.com/VictoriaMetrics/VictoriaMetrics/blob/master/app/vmauth/example_config_ent.yml).


## Reading auth tokens from other HTTP headers

`vmauth` reads `username`, `password`, and `bearer_token` [config values](#auth-config) from the `Authorization` request header.
It is possible to read these auth tokens from any other request header by specifying it via the `-httpAuthHeader` command-line flag.
For example, the following command instructs `vmauth` to read the auth token from the `X-Amz-Firehose-Access-Key` header:

```sh
./vmauth -httpAuthHeader='X-Amz-Firehose-Access-Key'
```

It is possible to read auth tokens from multiple headers. For example, the following command instructs `vmauth` to read auth token
from both `Authorization` and `X-Amz-Firehose-Access-Key` headers:

```sh
./vmauth -httpAuthHeader='Authorization' -httpAuthHeader='X-Amz-Firehose-Access-Key'
```

See also [authorization](#authorization) and [security](#security) docs.


## Query args handling

By default, `vmauth` sends all query arguments specified in `url_prefix` to the backend. It also proxies query args from client requests if they do not clash with the args specified in the `url_prefix`. This is needed for security; e.g., it prevents the client from overriding security-sensitive query args specified at `url_prefix`, such as `tenant_id`, `password`, `auth_key`, `extra_filters`, etc.

`vmauth` provides the ability to specify a list of query args, which can be proxied from the client request to the backend if they clash with the args specified in the `url_prefix`. In this case, the client query args are added to the `url_prefix` args before being proxied to the backend. This can be done via the following options:

* Via `-mergeQueryArgs` command-line flag. This flag may contain a comma-separated list of client query arg names, which are allowed
  to merge with the `url_prefix` query args when sending the request to the backend. This option is applied globally to all the configured backends.

* Via `merge_query_args` option at the `user` and `url_map` level. These values override the `-mergeQueryArgs` command-line flag.

The example below sends the request to `http://victoria-logs:9429/select/logsql/query?extra_filters={env="prod"}&extra_filters={team="dev"}&query=error` when `vmauth` receives request to `http://vmauth/select/logsql/query?extra_filters={team="dev"}&query=error`:

```yaml
unauthorized_user:
  # Merge `extra_filter` query arg from the clients with the `extra_filter` query args specified in the `url_prefix` below
  merge_query_args: [extra_filters]
  url_map:
  - src_paths: ["/select/.+"]
    url_prefix: 'http://victoria-logs:9428/?extra_filters={env="prod"}'
```


## Access log

vmauth allows configuring access logs {{% available_from "v1.138.0" %}} printing per-user:
```yaml
users:
  - username: foo
    password: bar
    url_prefix: 'http://localhost:8428/'
    # Log all requests to this user
    access_log: {}
```

If you want to log requests with missing or invalid auth tokens, use unauthorized_user without configuring any URL routes{{% available_from "v1.147.0" %}}:
```yaml
unauthorized_user:
  access_log: {}
```

Access logs contain limited information to prevent exposing sensitive data. See an example of the printed access log below:
```bash
2026-02-26T15:00:00.207Z        info    VictoriaMetrics/app/vmauth/auth_config.go:134   access_log request_host="localhost:8427" request_uri="/prometheus/api/v1/query_range?query=1&start=1772116199.897&end=1772117999.897&step=5s" status_code=200 remote_addr="127.0.0.1:63425" user_agent="Mozilla/5.0..." referer="http://localhost:8427/vmui/?" duration_ms=8 username="unauthorized"
```

The printed log starts with `access_log` prefix and is followed with `request_host`, `request_uri`, `status_code`, `remote_addr`,
`user_agent`, `referer`, `duration_ms` and `username` fields in [logfmt](https://brandur.org/logfmt) format. Such logs can be later
analyzed in [VictoriaLogs](https://docs.victoriametrics.com/victorialogs/):
```logsql
access_log | extract 'access_log <access_log>' | unpack_logfmt from access_log
| stats by(username, request_host, status_code) count()
```

Access logs can skip logging requests with specified status codes:
```yaml
users:
- username: foo
  password: bar
  url_prefix: 'http://localhost:8428/'
  access_log:
    filters:
      # except requests with HTTP status codes below
      skip_status_codes: [200, 202]
```

vmauth can print HTTP headers in access logs if `headers` param is specified {{% available_from "v1.153.0" %}}. Only headers listed in `headers` param will be printed:
```yaml
unauthorized_user:
  access_log:
    headers:
      - "AccountID"
      - "ProjectID"
```

Access logs can be enabled or disabled per-user with [hot config reload](https://docs.victoriametrics.com/victoriametrics/vmauth/#config-reload).
